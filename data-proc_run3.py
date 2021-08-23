import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import colors
#matplotlib inline

# XENON LIMIT. CROSS-CHECK WITH JONAS
def Xenon(mass):
    Xe= 8.91598734*10**(-49)*mass+4.14492233*10**(-48)+(-1.63834054*10**(-45))/mass+(3.16104724*10**(-43))/(mass**2)+(-2.04967758*10**(-41))/(mass**3)+(6.57376179*10**(-40))/(mass**4)+(-1.12392625*10**(-38))/(mass**5)+(1.06415326*10**(-37))/(mass**6)+(-5.25586284*10**(-37))/(mass**7)+(1.08588969*10**(-36))/(mass**8)
    return Xe

#Import file
#df = pd.read_csv('NLOsub_run3.csv' , sep = ',' )
#df.to_csv('NLOsub_run3_new.csv' , sep = '\t')

df = pd.read_csv('NLOsub_run3.csv' , usecols = ['mH1','mH2','mHD', 'mA', 'mHp' , 'tbeta', 'alphaEXT', 'L7', 'L8',  'omega_c', 'cxn_SI_LO', 'cxn_SI_NLO', 'fq_VERT', 'fq_MED', 'fq_LV', 'fq_BOX', 'gq_BOX', 'fq_LO','fqVERTEX', 'CTLam7','CTLam8','cxn_SI_NLO_OS'], sep = "\t")

#Drop invalid columns
df = df.drop(df[df.cxn_SI_NLO_OS == 'Indeterminate'].index)

#Change dtype from str to float
#df.cxn_SI_NLO = df.cxn_SI_NLO.astype(float)
df.cxn_SI_NLO_OS = df.cxn_SI_NLO_OS.astype(float)
#print(df)
#Define extra columns


# plot of blabla
fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()
plt.ylim(-100, 100)
plt.xlim(-0.025, 0.025)
#plt.yscale('log')
cxnmHD=plt.scatter(df.fqVERTEX, df.cxn_SI_NLO_OS/df.cxn_SI_LO,s=8,label="cxn_SI_NLO_OS")
#cxnmHD=plt.scatter(df.cxn_SI_LO, df.cxn_SI_NLO_OS/df.cxn_SI_LO,s=8,label="cxn_SI_NLO_OS")
#cxnmHD=plt.scatter(df.mHD, df.cxn_SI_NLO_OS/df.cxn_SI_LO,s=8, c=df.tbeta,label="cxn_SI_NLO_OS")
#plt.xlabel(r'$m_\chi$ [GeV]')
plt.xlabel(r'fq_Vertex')
plt.ylabel(r'$K-factor$')
#plt.scatter(df.mH1, df.cxn_SI_NLO_OS, s=8, c=df.alphaEXT)
mpl.pyplot.savefig('r3KVert0025')
