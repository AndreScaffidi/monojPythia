################################
import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
################################
# Plot spectra output from MadDM
# Data
datahh   = np.loadtxt('/home/andre/Uni/MG5_aMC_v2.6.4/MG5_aMC_v2_6_4/weak_test/Indirect/Events/run_01/gammas_spectrum_pythia8.dat')
dataall  = np.loadtxt('/home/andre/Uni/MG5_aMC_v2.6.4/MG5_aMC_v2_6_4/weak_test2/Indirect/Events/run_01/gammas_spectrum_pythia8.dat')
dataww   = np.loadtxt('/home/andre/Uni/MG5_aMC_v2.6.4/MG5_aMC_v2_6_4/weak_test3/Indirect/Events/run_01/gammas_spectrum_pythia8.dat')

# Axis
params         = {'legend.fontsize': 18,
				'axes.labelsize': 25,
				'axes.titlesize': 18,
				'xtick.labelsize' :12,
				'ytick.labelsize': 12,
				'grid.color': 'k',
				'grid.linestyle': ':',
				'grid.linewidth': 0.5,
				'mathtext.fontset' : 'stix',
				'mathtext.rm'      : 'serif',
				'font.family'      : 'serif',
				'font.serif'       : "Times New Roman",      # or "Times"          
				}
plt.rcParams.update(params)
fig, ax        = plt.subplots(figsize=(12,8), dpi=100)
plt.xlabel(r'$x$',fontsize=40,labelpad=15)
plt.ylabel(r'$\frac{dN_\gamma}{dx}$',fontsize=40,labelpad=30,rotation=0)
plt.tick_params(axis='both', which='major', labelsize=30)
plt.tick_params(axis='both', which='minor', labelsize=30)
# Plot
plt.plot(10**(dataall[:,0]),dataall[:,1],color='k',linestyle='-',linewidth=2,label=r'$\chi\chi\rightarrow All$')
plt.plot(10**(dataww[:,0]),dataww[:,1],color='green',linestyle='-',linewidth=2,label=r'$\chi\chi\rightarrow W^+ W^-$')
plt.plot(10**(datahh[:,0]),datahh[:,1],color='blue',linestyle='-',linewidth=2,label=r'$\chi\chi\rightarrow h h$')

ax.legend(loc=2,frameon=False, prop={'size':26})
ax.set_yscale('log', nonposy='clip')
ax.set_xscale('log')
ax.set_ylim([1E-2,500])
ax.set_xlim([1E-5,1])
plt.tight_layout()
# Saving
# plt.savefig("spectra.pdf")
#Showing
plt.show()
