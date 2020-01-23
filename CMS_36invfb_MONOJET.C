#ifdef __CLING__
R__LOAD_LIBRARY(libDelphes)
#include "classes/DelphesClasses.h"
#include "external/ExRootAnalysis/ExRootTreeReader.h"
#endif
#include <vector>
#include <iterator>
#include <algorithm>
#include <fstream>


void CMS_36invfb_MONOJET(const char *inputFile, const char *outFileone) {
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
  TClonesArray *branchPhoton = treeReader->UseBranch("Photon");


  //TClonesArray *branchEvent = treeReader->UseBranch("HepMCEvent");

  // MET cuts for signal regions based on: https://journals.aps.org/prd/pdf/10.1103/PhysRevD.97.092005
  const vector<double> METMINS = {250., 280., 310., 340., 370., 400., 430.,470.,510.,550.,590.,640.,690.,740.,790.,840.,900.,960.,1020.,1090.,1160.,1250.};
  vector<double> SRS_EXCL(METMINS.size(), 0.0), SRS_INCL(METMINS.size(), 0.0); 
  

  int monojet_count = 0;
  Long64_t numberOfEntries = treeReader->GetEntries();

  // Loop over all events
  //cout << "Reading " << treeReader->GetEntries() << " events..." << endl;
  for (Int_t entry = 0; entry < treeReader->GetEntries(); ++entry) {
    // Load selected branches with data from specified event
    treeReader->ReadEntry(entry);

    // Require large MET
    // Missing ET cut
    TLorentzVector vmet = ( (MissingET*) branchMET->At(0))->P4();

    
    vmet.SetPz(0);
    const double met = vmet.Perp();
    if (met < 250) continue;

    // Get baseline jets and leptons
    // Note that taus are reconstructed as jets with TauTag=1 according to the DelphesClasses.h file
    vector<const Jet*> basejets;
    vector<const Jet*> basetaus;
    for (int ij = 0; ij < branchJet->GetEntries(); ++ij) {
      const Jet* j = (const Jet*) branchJet->At(ij);
      if (j->PT > 20.)basejets.push_back(j);
      if (j->TauTag && j->PT > 18 && fabs(j->Eta) < 2.3)basetaus.push_back(j);
    }

    vector<const Electron*> baseelecs;
    for (int ie = 0; ie < branchElec->GetEntries(); ++ie) {
      const Electron* e = (const Electron*) branchElec->At(ie);
      if (e->PT > 10 && fabs(e->Eta) < 2.5)baseelecs.push_back(e);
    }
    vector<const Muon*> basemuons;
    for (int im = 0; im < branchMuon->GetEntries(); ++im) {
      const Muon* m = (const Muon*) branchMuon->At(im);
      if (m->PT > 10 && fabs(m->Eta) < 2.4)basemuons.push_back(m);
    }

    vector<const Photon*> basephotons;
    for (int ip = 0; ip < branchPhoton->GetEntries(); ++ip) {
      const Photon* p = (const Photon*) branchPhoton->At(ip);
      if (p->PT > 15 && fabs(p->Eta) < 2.5)basephotons.push_back(p);
    }

    // Veto on isolated leptons and photons
    if(baseelecs.size()   > 0)continue;
    if(basemuons.size()   > 0)continue;
    if(basetaus.size()    > 0)continue;
    if(basephotons.size() > 0)continue;

    // Veto if there are any b-tagged jets (reduce top background)
    vector<const Jet*> basebjets;
    for (const Jet* jet : basejets) {
      if(jet->BTag && jet->PT > 15. && fabs(jet->Eta) < 2.4)basebjets.push_back(jet);
    }
    
    if(basebjets.size() > 0)continue;

  
    // Get the 4 leading jets > 30 GeV, and veto if pTmiss is too close to them

    bool metveto=false;
    for (size_t i = 0; i < 4; ++i) {
      if (i >= basejets.size()) break;
      if (basejets[i]->PT < 30.) break;
      if (fabs(basejets[i]->P4().DeltaPhi(vmet)) < 0.5) metveto=true; //< VETO
    }
    if(metveto)continue;

    // Now the signal regions, but we'll just look at the monojet one
    if (basejets.empty()) continue;
    if (basejets[0]->PT < 100 || basejets[0]->Eta > 2.4) continue;
    
    // SRs defined by MET alone
    const size_t isr = std::distance(METMINS.begin(), std::upper_bound(METMINS.begin(), METMINS.end(), met))-1;
    SRS_EXCL[isr] += 1; //evt->Weight

  }


// CMS only use inclusive bins?

  ofstream oFile;
  oFile.open(outFileone, std::ofstream::out | std::ofstream::trunc); //wipe ouput file clean
  for (size_t i = 0; i <= METMINS.size(); ++i) {
    cout << SRS_EXCL[i] << " "  << numberOfEntries << " " << SRS_EXCL[i]/numberOfEntries <<  endl;
    oFile<< SRS_EXCL[i] << " "  << numberOfEntries << " " << SRS_EXCL[i]/numberOfEntries <<  endl;
    for (size_t j = 0; j <= i; ++j) SRS_INCL[j] += SRS_EXCL[i];
  }
  oFile.close();

}
