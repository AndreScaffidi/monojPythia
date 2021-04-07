#############################
# Script to go and read all results
# from madgraph output
#############################
import matplotlib
import os
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy.interpolate import Rbf
import itertools
import json
#############################
# Dim-6
# Grid_size = 4
# MASS      = np.linspace(1,150,Grid_size)
# THETA     = np.linspace(0,np.pi,Grid_size)  
# Dim-7
Grid_size = 19    
MASS      = np.linspace(1,1000,Grid_size)
#############################
# Get data
FILES  = {"ATLAS":"NUMBER_OF_M_JETS.csv","CMS":"NUMBER_OF_M_JETS_CMS.csv"}
DIR    = {1:'C62_C63_low', 2: 'C61_C64_low', 3:'C62_C63', 4: 'C61_C64'} # just need to change to _low
DIR7   = {1:'C71', 2: 'C72', 3:'C73', 4: 'C74'} # just need to change to _low
BIN_S  = {"ATLAS": 10,"CMS":22}
def get_dim_6():
	for group,name in DIR.items():
		print "For opperator combination %s..." %(name)
		for experiment, file in FILES.items():
			print "Doing ", experiment
			DATA     = []
			MET_BINS = []
			for m in MASS:  
				for th in THETA:
					if os.path.exists('%s/MONO_JET_%1.2F_%1.2F/Events/run_01/%s' %(name,m,th,file)):
						# Do not include nans ************ just remove points
						binInfo                  = np.loadtxt('%s/MONO_JET_%1.2F_%1.2F/Events/run_01/%s'%(name,m,th,file)) 
						nJets                    = binInfo[5,0]
						CS_data                  = np.loadtxt('%s/MONO_JET_%1.2F_%1.2F/Events/run_01/tag_1_merged_xsecs.txt'%(name,m,th),skiprows=1) 
						DATA.append([float(m),float(th),nJets,float(CS_data[2,1])])
						# print "Size of met_bins  = ", len(binInfo)
						# print "For experiment: ", experiment 
						MET_BINS.append(binInfo[:,2][:-1])
					else:
						print "Uncompleted run! mass = %1.2F, th = %1.2F" %(m,th)
						# continue
						print "Padding bin entries as placeholder..."   
						# CS_data                  = np.loadtxt('%s/MONO_JET_%1.2F_%1.2F/Events/run_01/tag_1_merged_xsecs.txt'%(name,m,th),skiprows=1) 
						DATA.append([float(m),float(th),-1,-1])
						# print "Size of met_bins  = ", len(binInfo)
						MET_BINS.append(-1*np.ones(BIN_S[experiment]))
			############################# 
			# Generate text output
			DATA    = np.array(DATA)
			MET_BINS= np.array(MET_BINS) 
			#############################
			# # BE CAREFUL ################
			# np.savetxt('Grid_Interpolator/grid_output_%s_%s.txt'%(experiment,name)                                     ,np.c_[DATA],fmt="%f")
			# np.savetxt('Grid_Interpolator/X_Y_%s_%s.txt' %(experiment,name)                                            ,np.c_[MASS,THETA],fmt="%f")
			# np.savetxt('Grid_Interpolator/met_hist_%s_%s.txt' %(experiment,name)                                       ,np.c_[MET_BINS],fmt="%f")
			

			# np.savetxt('/fast/users/a1607156/gambitgit/ColliderBit/data/DMEFT/grid_output_%s_%s.txt'%(experiment,name) ,np.c_[DATA],fmt="%f")
			# np.savetxt('/fast/users/a1607156/gambitgit/ColliderBit/data/DMEFT/X_Y_%s_%s.txt' %(experiment,name)        ,np.c_[MASS,THETA],fmt="%f")
			# np.savetxt('/fast/users/a1607156/gambitgit/ColliderBit/data/DMEFT/met_hist_%s_%s.txt' %(experiment,name)   ,np.c_[MET_BINS],fmt="%f")
			


			# np.savetxt('/fast/users/a1607156/gambitgit/ColliderBit/data/DMEFT/grid_output_%s_%s.txt'%(experiment,name) ,np.c_[DATA],fmt="%f")
			# np.savetxt('/fast/users/a1607156/gambitgit/ColliderBit/data/DMEFT/X_Y_%s_%s.txt' %(experiment,name)        ,np.c_[MASS,THETA],fmt="%f")

def get_dim_7():
	for group,name in DIR7.items():
		print "For opperator combination %s..." %(name)
		for experiment, file in FILES.items():
			print "Doing ", experiment
			DATA     = []
			MET_BINS = []
			for m in MASS:  
				if os.path.exists('%s/MONO_JET_%s_%1.2F/Events/run_01/%s' %(name,name,m,file)):
					# Do not include nans ************ just remove points
					binInfo                  = np.loadtxt('%s/MONO_JET_%s_%1.2F/Events/run_01/%s'%(name,name,m,file)) 
					CS_data                  = np.loadtxt('%s/MONO_JET_%s_%1.2F/Events/run_01/tag_1_merged_xsecs.txt'%(name,name,m),skiprows=1) 
					DATA.append([float(m),float(CS_data[2,1])])
					# print "Size of met_bins  = ", len(binInfo)
					# print "For experiment: ", experiment 
					MET_BINS.append(binInfo[:,2][:-1])
				else:
					print "Uncompleted run! mass = %1.2F, th = %1.2F" %(m,th)
					# continue
					print "Padding bin entries as placeholder..."   
					# CS_data                  = np.loadtxt('%s/MONO_JET_%1.2F_%1.2F/Events/run_01/tag_1_merged_xsecs.txt'%(name,m,th),skiprows=1) 
					DATA.append([float(m),-1])
					# print "Size of met_bins  = ", len(binInfo)
					MET_BINS.append(-1*np.ones(BIN_S[experiment]))
			############################# 
			# Generate text output
			DATA    = np.array(DATA)
			MET_BINS= np.array(MET_BINS) 
			#############################
			# # BE CAREFUL ################
			np.savetxt('Grid_Interpolator/grid_output_%s_%s.txt'%(experiment,name)                                     ,np.c_[DATA],fmt="%f")
			np.savetxt('Grid_Interpolator/X_Y_%s_%s.txt' %(experiment,name)                                            ,np.c_[MASS],fmt="%f")
			np.savetxt('Grid_Interpolator/met_hist_%s_%s.txt' %(experiment,name)                                       ,np.c_[MET_BINS],fmt="%f")
			

			# np.savetxt('/fast/users/a1607156/gambitgit/ColliderBit/data/DMEFT/grid_output_%s_%s.txt'%(experiment,name) ,np.c_[DATA],fmt="%f")
			# np.savetxt('/fast/users/a1607156/gambitgit/ColliderBit/data/DMEFT/X_Y_%s_%s.txt' %(experiment,name)        ,np.c_[MASS,THETA],fmt="%f")
			# np.savetxt('/fast/users/a1607156/gambitgit/ColliderBit/data/DMEFT/met_hist_%s_%s.txt' %(experiment,name)   ,np.c_[MET_BINS],fmt="%f")
			


			# np.savetxt('/fast/users/a1607156/gambitgit/ColliderBit/data/DMEFT/grid_output_%s_%s.txt'%(experiment,name) ,np.c_[DATA],fmt="%f")
			# np.savetxt('/fast/users/a1607156/gambitgit/ColliderBit/data/DMEFT/X_Y_%s_%s.txt' %(experiment,name)        ,np.c_[MASS,THETA],fmt="%f")

get_dim_7()








#############################
# Data listed as [DM mass, theta, #No. mono jets, cross-section (merged)]
# xi, yi = np.meshgrid(MASS, THETA)
# print "Interpolating!"
# rbf    = Rbf(DATA[:,0], DATA[:,1], DATA[:,3],smooth = 0, function='linear')
# zi     = rbf(xi, yi)
# rbfJet = Rbf(DATA[:,0], DATA[:,1], np.array(DATA[:,2]),smooth = 0, function='linear')
# ziJet  = rbfJet(xi, yi)
# #############################
# # Plotting
# print "Plotting!"
# params = {'legend.fontsize': 18,
# 				'axes.labelsize': 25,
# 				'axes.titlesize': 18,
# 				'xtick.labelsize' :12,
# 				'ytick.labelsize': 12,
# 				'grid.color': 'k',
# 				'grid.linestyle': ':',
# 				'grid.linewidth': 0.5,
# 				'mathtext.fontset' : 'stix',
# 				'mathtext.rm'      : 'serif',
# 				'font.family'      : 'serif',
# 				'font.serif'       : "Times New Roman",      # or "Times"          
# 				}
# plt.rcParams.update(params)
# # Cross-section
# fig,ax = plt.subplots(figsize=(10.5,7.8), dpi=100)
# ax.set_xlabel(r'$m_\chi$ [GeV]',fontsize=50)
# ax.set_ylabel(r'$\theta$ [rad]',fontsize=50)
# ax.tick_params(axis='both', which='major', labelsize=50)
# ax.tick_params(axis='both', which='minor', labelsize=50)
# cax    = ax.imshow(zi, vmin=zi.min(), origin='lower',extent=[xi.min(), xi.max(), yi.min(), yi.max()],aspect='auto')
# cbar   = fig.colorbar(cax,orientation='vertical',aspect=20,pad=0.1)
# cbar.set_label(r'$\sigma$ [pb]',size=50,rotation='horizontal',labelpad=80)
# cbar.ax.tick_params(labelsize=20)
# plt.tight_layout()
# plt.savefig('plots/CS_plot.pdf')

# # Njets
# fig2,ax2 = plt.subplots(figsize=(10.5,7.8), dpi=100)
# ax2.set_xlabel(r'$m_\chi$ [GeV]',fontsize=50)
# ax2.set_ylabel(r'$\theta$ [rad]',fontsize=50)
# ax2.tick_params(axis='both', which='major', labelsize=50)
# ax2.tick_params(axis='both', which='minor', labelsize=50)
# cax    = ax2.imshow(ziJet, vmin=ziJet.min(), origin='lower',extent=[xi.min(), xi.max(), yi.min(), yi.max()],aspect='auto')
# cbar   = fig2.colorbar(cax,orientation='vertical',aspect=20,pad=0.1)
# cbar.set_label(r'Accep.',size=20,rotation='horizontal',labelpad=50)
# cbar.ax.tick_params(labelsize=20)
# plt.tight_layout()
# plt.savefig('plots/A_plot.pdf')

# # Show
# plt.show()

