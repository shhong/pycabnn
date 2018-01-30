
# coding: utf-8

# ## Parallel fiber - GoC

# In[1]:


from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[12]:


output_path = Path.cwd().parent.parent / 'output_2'


# In[13]:


adend = np.loadtxt(output_path / 'GoCadendcoordinates.dat')
bdend = np.loadtxt(output_path / 'GoCbdendcoordinates.dat')
grcs = np.loadtxt(output_path / "GCcoordinates.sorted.dat")
gcts = np.loadtxt(output_path / "GCTcoordinates.dat")


# In[14]:


adend = adend.reshape((1995,50,3))
bdend = bdend.reshape((1995,24,3))


# Here we check if the dendritic point alignment is ok.

# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
i = 1
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(adend[i][:,0], adend[i][:,1], adend[i][:,2],'.r')
ax.plot(bdend[i][:,0], bdend[i][:,1], bdend[i][:,2],'.k')

i = 1000
ax.plot(adend[i][:,0], adend[i][:,1], adend[i][:,2],'.r')
ax.plot(bdend[i][:,0], bdend[i][:,1], bdend[i][:,2],'.k')


# Now we check if connections look ok.

# In[16]:


data_index = 10

data_dir = output_path
fcoords = "PFtoGoCcoords{}.dat".format(data_index)
fsrcs = "PFtoGoCsources{}.dat".format(data_index)
ftgts = "PFtoGoCtargets{}.dat".format(data_index)
fdsts = "PFtoGoCdistances{}.dat".format(data_index)


xyz = np.loadtxt(data_dir / fcoords)
srcs = np.loadtxt(data_dir / fsrcs).astype(int)
tgts = np.loadtxt(data_dir / ftgts).astype(int)
dsts = np.loadtxt(data_dir / fdsts)


# In[17]:


i = 4000
tgt = tgts[i]
src = srcs[i]
dst = dsts[i]

pt2 = xyz[i]

print("{} -> {} with d = {}".format(src, tgt, dst))


# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
pt0 = grcs[src]
pt1 = gcts[src]
ax.plot([pt0[0], pt1[0]], [pt0[1], pt1[1]], [pt0[2], pt1[2]], 'o-k')
ax.plot([pt1[0], pt1[0]+1e3], [pt1[1], pt1[1]], [pt1[2], pt1[2]], '-k')
ax.plot([pt1[0], pt1[0]-1e3], [pt1[1], pt1[1]], [pt1[2], pt1[2]], '-k')
ax.plot(adend[tgt][:,0], adend[tgt][:,1], adend[tgt][:,2],'.r')
ax.plot(bdend[tgt][:,0], bdend[tgt][:,1], bdend[tgt][:,2],'.m')
pt2 = xyz[i]
ax.plot([pt2[0]], [pt2[1]], [pt2[2]], 'oc')
# ax.set_xlim([0, 1500])


# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')

fig, ax = plt.subplots(ncols=2, figsize=(10, 5), sharex=False)
ax[0].plot([pt0[0], pt1[0]], [pt0[1], pt1[1]], 'o-k')
ax[0].plot([pt1[0], pt1[0]+1e3], [pt1[1], pt1[1]], '-k')
ax[0].plot([pt1[0], pt1[0]-1e3], [pt1[1], pt1[1]], '-k')
ax[0].plot(adend[tgt][:,0], adend[tgt][:,1], '.r')
ax[0].plot(bdend[tgt][:,0], bdend[tgt][:,1], '.m')
ax[0].plot([pt2[0]], [pt2[1]], 'oc')


ax[1].plot([pt0[0], pt1[0]], [pt0[2], pt1[2]], 'o-k')
ax[1].plot([pt1[0], pt1[0]+1e3], [pt1[2], pt1[2]], '-k')
ax[1].plot([pt1[0], pt1[0]-1e3], [pt1[2], pt1[2]], '-k')
ax[1].plot(adend[tgt][:,0], adend[tgt][:,2],'.r')
ax[1].plot(bdend[tgt][:,0], bdend[tgt][:,2],'.m')
ax[1].plot([pt2[0]], [pt2[2]], 'oc')


# ## Ascending axon - GoC

# In[20]:


data_index = 80

data_dir = output_path
fcoords = "AAtoGoCcoords{}.dat".format(data_index)
fsrcs = "AAtoGoCsources{}.dat".format(data_index)
ftgts = "AAtoGoCtargets{}.dat".format(data_index)
fdsts = "AAtoGoCdistances{}.dat".format(data_index)

xyz = np.loadtxt(data_dir / fcoords)
srcs = np.loadtxt(data_dir / fsrcs).astype(int)
tgts = np.loadtxt(data_dir / ftgts).astype(int)
dsts = np.loadtxt(data_dir / fdsts)


# In[27]:


i = 6900
tgt = tgts[i]
src = srcs[i]
dst = dsts[i]

pt2 = xyz[i]

print("{} -> {} with d = {}".format(src, tgt, dst))


# In[28]:


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
pt0 = grcs[src]
pt1 = gcts[src]
ax.plot([pt0[0], pt1[0]], [pt0[1], pt1[1]], [pt0[2], pt1[2]], 'o-k')
ax.plot([pt1[0], pt1[0]+1e3], [pt1[1], pt1[1]], [pt1[2], pt1[2]], '-k')
ax.plot([pt1[0], pt1[0]-1e3], [pt1[1], pt1[1]], [pt1[2], pt1[2]], '-k')
ax.plot(adend[tgt][:,0], adend[tgt][:,1], adend[tgt][:,2],'.r')
ax.plot(bdend[tgt][:,0], bdend[tgt][:,1], bdend[tgt][:,2],'.m')
pt2 = xyz[i]
ax.plot([pt2[0]], [pt2[1]], [pt2[2]], 'oc')
ax.set_xlim([0, 1500])


# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')

fig, ax = plt.subplots(ncols=2, figsize=(10, 5), sharex=True)
ax[0].plot([pt0[0], pt1[0]], [pt0[1], pt1[1]], 'o-k')
ax[0].plot([pt1[0], pt1[0]+1e3], [pt1[1], pt1[1]], '-k')
ax[0].plot([pt1[0], pt1[0]-1e3], [pt1[1], pt1[1]], '-k')
ax[0].plot(adend[tgt][:,0], adend[tgt][:,1], '.r')
ax[0].plot(bdend[tgt][:,0], bdend[tgt][:,1], '.m')
ax[0].plot([pt2[0]], [pt2[1]], 'oc')


ax[1].plot([pt0[0], pt1[0]], [pt0[2], pt1[2]], 'o-k')
ax[1].plot([pt1[0], pt1[0]+1e3], [pt1[2], pt1[2]], '-k')
ax[1].plot([pt1[0], pt1[0]-1e3], [pt1[2], pt1[2]], '-k')
ax[1].plot(adend[tgt][:,0], adend[tgt][:,2],'.r')
ax[1].plot(bdend[tgt][:,0], bdend[tgt][:,2],'.m')
ax[1].plot([pt2[0]], [pt2[2]], 'oc')


# ## Convert big files to the npy format

# In[ ]:


output_path = Path('/Users/shhong/Dropbox/network_data/output_ines')
# output_path = Path('/Users/shhong/Dropbox/network_data/output_brep')
src = np.loadtxt(output_path / "PFtoGoCsources.dat")
tgt = np.loadtxt(output_path / "PFtoGoCtargets.dat")
src = src.astype(int)
tgt = tgt.astype(int)


# In[ ]:


np.save(output_path / 'PFtoGoCsources.npy', src)
np.save(output_path / 'PFtoGoCtargets.npy', tgt)


# In[ ]:


src = np.loadtxt(output_path.parent / "AAtoGoCsources.dat")
tgt = np.loadtxt(output_path.parent / "AAtoGoCtargets.dat")
src = src.astype(int)
tgt = tgt.astype(int)

np.save(output_path.parent / 'AAtoGoCsources.npy', src)
np.save(output_path.parent / 'AAtoGoCtargets.npy', tgt)


# ## Load back data and check PFs

# In[30]:


output_path = Path('/Users/shhong/Dropbox/network_data/output_ines')

srcs = np.load(output_path / 'PFtoGoCsources.npy')
tgts = np.load(output_path / 'PFtoGoCtargets.npy')

grcxy = np.loadtxt(output_path / 'GCcoordinates.sorted.dat')
gocxy = np.loadtxt(output_path / 'GoCcoordinates.sorted.dat')


# In[31]:


import dask.dataframe as dd

df = dd.from_array(np.vstack((srcs, tgts)).T, columns=('src', 'tgt'))


# In[32]:


cons_per_goc = df.groupby('tgt').count().compute()
cons_per_goc
cons_per_pf = df.groupby('src').count().compute()
cons_per_pf


# In[33]:


import dask.dataframe as dd

def convert_from_dd(x, size):
    temp = np.zeros(size)
    temp[x.index] = x.values
    return temp

cons_per_goc = convert_from_dd(cons_per_goc.src, gocxy.shape[0])
cons_per_pf = convert_from_dd(cons_per_pf.tgt, grcxy.shape[0])


# In[34]:


fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(16, 10))
ax[0,0].plot(cons_per_goc, '.')
ax[0,0].set(xlabel="GoC id", ylabel='Connections')
_ = ax[0,1].hist(cons_per_goc, 200)
ax[0,1].set(xlabel="Connections per GoC", ylabel='Count')
ax[1,0].scatter(gocxy[:,0], gocxy[:,1], 100, cons_per_goc, '.')
ax[1,0].set(xlabel="x (um)", ylabel="y (um)")
ax[1,1].scatter(gocxy[:,1], gocxy[:,2], 100, cons_per_goc, '.')
ax[1,1].set(xlabel="x (um)", ylabel="z (um)")


# In[35]:


print("Connections per GoC = {} ± {}".format(np.mean(cons_per_goc), np.std(cons_per_goc)/np.sqrt(cons_per_goc.size)))


# In[36]:


fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(16, 10))
ax[0,0].plot(cons_per_pf, '.')
ax[0,0].set(xlabel="PF id", ylabel='Connections')
ax[0,1].set(xlabel="Connections per PF", ylabel='Count')
_ = ax[0,1].hist(cons_per_pf, 200)
ax[1,0].scatter(grcxy[:,0], grcxy[:,1], 0.25, cons_per_pf, '.')
ax[1,0].set(xlabel="x (um)", ylabel="y (um)")
ax[1,1].scatter(grcxy[:,1], grcxy[:,2], 0.25, cons_per_pf, '.')
ax[1,1].set(xlabel="x (um)", ylabel="z (um)")


# In[37]:


print("Connections per PF = {} ± {}".format(np.mean(cons_per_pf), np.std(cons_per_pf)/np.sqrt(cons_per_pf.size)))


# ## Perform the same analysis on BREP outputs

# In[ ]:


# output_path = Path('/Users/shhong/Dropbox/network_data/output_brep')
# src = np.loadtxt(output_path / "PFtoGoCsources.dat")
# tgt = np.loadtxt(output_path / "PFtoGoCtargets.dat")
# src = src.astype(int)
# tgt = tgt.astype(int)

# np.save(output_path / 'PFtoGoCsources.npy', src)
# np.save(output_path / 'PFtoGoCtargets.npy', tgt)

# src = np.loadtxt(output_path / "AAtoGoCsources.dat")
# tgt = np.loadtxt(output_path / "AAtoGoCtargets.dat")
# src = src.astype(int)
# tgt = tgt.astype(int)

# np.save(output_path / 'AAtoGoCsources.npy', src)
# np.save(output_path / 'AAtoGoCtargets.npy', tgt)


# In[38]:


output_path = Path('/Users/shhong/Dropbox/network_data/output_brep')

srcs = np.load(output_path / 'PFtoGoCsources.npy')
tgts = np.load(output_path / 'PFtoGoCtargets.npy')
grcxy = np.loadtxt(output_path / 'GCcoordinates.sorted.dat')
gocxy = np.loadtxt(output_path / 'GoCcoordinates.sorted.dat')

df = dd.from_array(np.vstack((srcs, tgts)).T, columns=('src', 'tgt'))


# In[39]:


cons_per_goc = df.groupby('tgt').count().compute()
cons_per_pf = df.groupby('src').count().compute()

cons_per_goc = convert_from_dd(cons_per_goc.src, gocxy.shape[0])
cons_per_pf = convert_from_dd(cons_per_pf.tgt, grcxy.shape[0])


# In[40]:


fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(16, 10))
ax[0,0].plot(cons_per_goc, '.')
ax[0,0].set(xlabel="GoC id", ylabel='Connections')
_ = ax[0,1].hist(cons_per_goc, 200)
ax[0,1].set(xlabel="Connections per GoC", ylabel='Count')
ax[1,0].scatter(gocxy[:,0], gocxy[:,1], 100, cons_per_goc, '.')
ax[1,0].set(xlabel="x (um)", ylabel="y (um)")
ax[1,1].scatter(gocxy[:,1], gocxy[:,2], 100, cons_per_goc, '.')
ax[1,1].set(xlabel="x (um)", ylabel="z (um)")


# In[41]:


print("Connections per GoC = {} ± {}".format(np.mean(cons_per_goc), np.std(cons_per_goc)/np.sqrt(cons_per_goc.size)))


# In[42]:


fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(16, 10))
ax[0,0].plot(cons_per_pf, '.')
ax[0,0].set(xlabel="PF id", ylabel='Connections')
ax[0,1].set(xlabel="Connections per PF", ylabel='Count')
_ = ax[0,1].hist(cons_per_pf, 200)
ax[1,0].scatter(grcxy[:,0], grcxy[:,1], 0.25, cons_per_pf, '.')
ax[1,0].set(xlabel="x (um)", ylabel="y (um)")
ax[1,1].scatter(grcxy[:,1], grcxy[:,2], 0.25, cons_per_pf, '.')
ax[1,1].set(xlabel="x (um)", ylabel="z (um)")


# In[43]:


print("Connections per PF = {} ± {}".format(np.mean(cons_per_pf), np.std(cons_per_pf)/np.sqrt(cons_per_pf.size)))


# In[44]:


9708.829573934838/7840.988471177945


# In[45]:


24.272073934837092/19.602471177944864


# In[46]:


np.sqrt(1.238215004)

