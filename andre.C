void andre(){

  TString filename = "tag_1_delphes_events.root";
  TString treename = "Delphes";
  TString description = "signal region";
  TString variable = "MissingET.MET";


  TFile * file = new TFile(filename,"READ");
  TTree *tree  = new TTree(treename,description);
  tree->GetListOfLeaves()->Print();
  
  // tree->Draw(variable);

}
