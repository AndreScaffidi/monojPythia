#########################################################################################################
import numpy as np
from scipy import stats
from scipy.stats import chi2
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
#########################################################################################################
# Calculate stats for ams run.

# SIgnificance calculators
def conv_to_q0(nSigma,dof):
	alphaS = stats.norm.sf(nSigma)
	return stats.chi2.isf(alphaS,dof)

def Gauss_nSigma(q0,dof):
	alphaS = stats.chi2.sf(q0, dof)
	return stats.norm.isf(0.5*alphaS)

# Get AMS data
data_ams       = np.loadtxt('/home/andre/Uni/MG5_aMC_v2.6.4/MG5_aMC_v2_6_4/PLUGIN/maddm/ExpData/AMS_2019.dat')
Flux_AMS       = data_ams[:,1]

multinest_data = np.loadtxt('multinest_AMS_debug.txt')
chi2           = multinest_data[:,3]
mx             = multinest_data[:,0]
order          = np.argsort(mx)
chi2           = chi2[order]
mx             = mx[order]


mCHI = mx[chi2==min(chi2)]
minchi    = min(chi2)
numParams = 1
k         = np.size(Flux_AMS)-numParams
print("###################################################")
print("Mass DM                     = ", mCHI )
print("Min chi2                    = ", minchi)
print("Exclusion significance      = ", Gauss_nSigma(minchi,k))
print("P-val                       = ", 1-stats.chi2.cdf(minchi, k))
print("N.dof                       = ", k)
print("chi2/d.o.f                  = ", minchi/k)
print("###################################################")
############################################################################



# # Plot best fit spectrum
params = {'legend.fontsize': 18,
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
          'font.serif'       : "Times New Roman", # or "Times"          
         }
plt.rcParams.update(params)
fig, ax = plt.subplots(figsize=(12,8), dpi=100)
plt.xlabel(r'$m_\chi$ [GeV]',fontsize=30,labelpad=15)
plt.ylabel(r'$\chi^2$',fontsize=30,labelpad=25)

plt.plot(mx,chi2,'-',color='k',linewidth=2)
# plt.hlins(0.05)


ax.set_yscale('log', nonposy='clip')

plt.tick_params(axis='both', which='major', labelsize=20)
plt.tick_params(axis='both', which='minor', labelsize=20)
# ax.errorbar(DAMA_bin_centers,Data,yerr=Errors,fmt='o',linewidth=2, capsize=4,color='red')
plt.tight_layout()
ax.legend(loc=4,frameon=True, prop={'size':22})


# Saving
# plt.savefig('/home/andre/Uni/Dropbox/Project/Directional/MultiDM_DAMA/tex_DAMA/v8/Figures/4D_fit_%s.pdf' %(lightHeavy))

plt.show()


