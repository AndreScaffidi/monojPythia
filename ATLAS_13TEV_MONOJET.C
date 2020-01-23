#ifdef __CLING__
R__LOAD_LIBRARY(libDelphes)
#include "classes/DelphesClasses.h"
#include "external/ExRootAnalysis/ExRootTreeReader.h"
#endif
#include <vector>
#include <iterator>
#include <algorithm>
#include <fstream>


void ATLAS_13TEV_MONOJET(const char *inputFile, const char *outFileone) {
  using namespace std;
  gSystem->Load("libDelphes");

  // Create chain of root trees
  TChain chain("Delphes");
  chain.Add(inputFile);

  // Create object of class ExRootTreeReader and get branches
  ExRootTreeReader *treeReader = new ExRootTreeReader(&chain);
  TClonesArray *branchMET = treeReader->UseBranch("MissingET");
  TClonesArray *branchJet = treeReader->UseBranch("Jet");
  TClonesArray *branchElec = treeReader->UseBranch("Electron");
  TClonesArray *branchMuon = treeReader->UseBranch("Muon");
  //TClonesArray *branchEvent = treeReader->UseBranch("HepMCEvent");

  // MET cuts for signal regions
  const vector<double> METMINS = {250., 300., 350., 400., 500., 600., 700., 800., 900., 1000.};
  vector<double> SRS_EXCL(METMINS.size(), 0.0), SRS_INCL(METMINS.size(), 0.0);
  

  int monojet_count = 0;
  Long64_t numberOfEntries = treeReader->GetEntries();
  // Loop over all events
  //cout << "Reading " << treeReader->GetEntries() << " events..." << endl;
  for (Int_t entry = 0; entry < treeReader->GetEntries(); ++entry) {
    // Load selected branches with data from specified event
    treeReader->ReadEntry(entry);
    // const HepMCEvent* = (const HepMCEvent*) branchEvent->At(0);

    // Get baseline jets and leptons
    vector<const Jet*> basejets;
    for (int ij = 0; ij < branchJet->GetEntries(); ++ij) {
      const Jet* j = (const Jet*) branchJet->At(ij);
      if (j->PT < 30 || fabs(j->Eta) > 2.8) continue;
      basejets.push_back(j);
    }
    vector<const Electron*> baseelecs;
    for (int ie = 0; ie < branchElec->GetEntries(); ++ie) {
      const Electron* e = (const Electron*) branchElec->At(ie);
      if (e->PT < 20 || fabs(e->Eta) > 2.47) continue;
      baseelecs.push_back(e);
    }
    vector<const Muon*> basemuons;
    for (int im = 0; im < branchMuon->GetEntries(); ++im) {
      const Muon* m = (const Muon*) branchMuon->At(im);
      if (m->PT < 10 || fabs(m->Eta) > 2.5) continue;
      basemuons.push_back(m);
    }
    // cout << "J" << basejets.size() << " E" << baseelecs.size() << " M" << basemuons.size() << endl;

    // Explicit e/jet isolation (needed?)
    vector<const Jet*> anajets;
    for (const Jet* j : basejets) {
      if (fabs(j->Flavor) != 5) { //< if a b-jet, consider overlapping electrons to be from B decay
        bool iso = true;
        for (const Electron* e : baseelecs) {
          if (e->P4().DeltaR(j->P4()) < 0.2) { iso = false; break; }
        }
        if (!iso) continue;
      }
      anajets.push_back(j);
    }


    vector<const Electron*> anaelecs;
    for (const Electron* e : baseelecs) {
      bool iso = true;
      for (const Jet* j : anajets) {
        if (j->P4().DeltaR(e->P4()) < 0.4) { iso = false; break; }
      }
      if (!iso) continue;
      anaelecs.push_back(e);
    }

    vector<const Muon*> anamuons;
    for (const Muon* m : basemuons) {
      bool iso = true;
      for (const Jet* j : anajets) {
        if (j->P4().DeltaR(m->P4()) < 0.4) { iso = false; break; }
      }
      if (!iso) continue;
      anamuons.push_back(m);
    }
    // cout << "J" << anajets.size() << " E" << anaelecs.size() << " M" << anamuons.size() << endl;

    // Veto on remaining electrons and muons
    if (!anaelecs.empty()) continue;
    if (!anamuons.empty()) continue;

    // Missing ET cut
    TLorentzVector vmet = ( (MissingET*) branchMET->At(0))->P4();
    // Have to include muons in MET -- we add them back
    for (const Muon* m : anamuons) vmet += m->P4();
    // Zero z-component
    vmet.SetPz(0);
    // Require ETmiss > 250 GeV
    const double met = vmet.Perp();
    //cout << "MET=" << met << endl;
    if (met < 250) continue;


    // Isolate jets from MET
    // NB. Loose selection = no spurious noise = no action needed?
    vector<const Jet*> anajets2;
    for (const Jet* j : anajets) {
      if (fabs(j->P4().DeltaPhi(vmet)) > 0.4) anajets2.push_back(j);
    }



    //cout << "MET=" << met << "; J" << basejets.size() << "->" << anajets.size() << "->" << anajets2.size() << endl;

    // Require 1..4 jets
    if (anajets2.empty()) continue;
    if (anajets2.size() > 4) continue;

    // Require leading jet pT > 250 GeV, and within |eta| < 2.4
    if (anajets2[0]->PT < 250) continue;
    if (fabs(anajets2[0]->Eta) > 2.4) continue;

    // Get monojet count after cuts: Savif (abs(idup(i,1,iproc)).eq.62) is_a_nu(i)=.true.
    if (anajets2.size() == 1) monojet_count++;
    
    // SRs defined by MET alone
    const size_t isr = std::distance(METMINS.begin(), std::upper_bound(METMINS.begin(), METMINS.end(), met))-1;
    SRS_EXCL[isr] += 1; //evt->Weight

  }

  // ofstream oFile;
  // oFile.open(outFileone, std::ofstream::out | std::ofstream::trunc); //wipe ouput file clean
  // oFile << monojet_count<< " "  << endl;
  // oFile.close();

  ofstream oFile;
  oFile.open(outFileone, std::ofstream::out | std::ofstream::trunc); //wipe ouput file clean
  for (size_t i = 0; i <= METMINS.size(); ++i) {
    cout << SRS_EXCL[i] << " "  << numberOfEntries << " " << SRS_EXCL[i]/numberOfEntries << endl;
    oFile<< SRS_EXCL[i] << " "  << numberOfEntries << " " << SRS_EXCL[i]/numberOfEntries << endl;
    for (size_t j = 0; j <= i; ++j) SRS_INCL[j] += SRS_EXCL[i];
  }
  oFile.close();

}
 