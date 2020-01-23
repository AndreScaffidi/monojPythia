#include <vector>
#include <iostream>
#include <fstream>
#include <limits>
#include <math.h>

//Delphes and root stuff
#ifdef __CLING__
R__LOAD_LIBRARY(libDelphes)
#include "classes/DelphesClasses.h"
#include "external/ExRootAnalysis/ExRootTreeReader.h"
#endif

 
void get_nJets(const char *inputFile, const char *outFileone){
  gSystem->Load("libDelphes");

  // Create chain of root trees
  TChain chain("Delphes");
  chain.Add(inputFile);

  // Create object of class ExRootTreeReader
  ExRootTreeReader *treeReader = new ExRootTreeReader(&chain);
  Long64_t numberOfEntries = treeReader->GetEntries();

  // Get pointers to branches used in this analysis
  TClonesArray *branchJet = treeReader->UseBranch("Jet");

  // Output file
  
  cout << "Total number of events:" << setw(10) << numberOfEntries << endl;
   // numberOfEntries = 10000;
  // Loop over all events and write to output file

  // Counter for mono-jet events
  int monojet_count = 0;

  for(Int_t entry = 0; entry < numberOfEntries; ++entry)
    {
      treeReader->ReadEntry(entry);
      
      // if(branchJet->GetEntriesFast() != 1){continue;}
      int jet_count = 0;
      for(int i=0; i < branchJet->GetEntriesFast(); i++){
        // Jet *candidate = (Jet*)branchJet->At(i);
        jet_count += 1;
      }

      if(jet_count == 1){
      monojet_count += 1;
      }

  }
  
  // Print to the file
  cout << "Number of monojet events:" << setw(10) << monojet_count << endl;
    
  ofstream oFile;
  oFile.open(outFileone, std::ofstream::out | std::ofstream::trunc); //wipe ouput file clean
  oFile << monojet_count  << endl;
  oFile.close();

  return;

}
