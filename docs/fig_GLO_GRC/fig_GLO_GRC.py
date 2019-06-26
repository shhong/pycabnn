# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Glomerulus - GrC connectivity
import numpy as np
import matplotlib.pyplot as plt

fname = "../fig_POPGEN/coords_20190614_1e.npz"
f = np.load(fname)


def limit_to_box(x, box):
    mf = x.copy()
    for i, t in enumerate(box):
        mf = mf[mf[:, i] >= t[0], :]
        mf = mf[mf[:, i] <= t[1], :]
    return mf


def print_range(goc):
    print(
        "Current range:\n",
        "x: [{}, {}]\n".format(goc[:, 0].min(), goc[:, 0].max()),
        "y: [{}, {}]\n".format(goc[:, 1].min(), goc[:, 1].max()),
        "z: [{}, {}]".format(goc[:, 2].min(), goc[:, 2].max()),
    )


def fix_coords(x, bbox):
    y = x - 25
    y = limit_to_box(y, bbox)
    print_range(y)
    return y


bbox = [[0, 700], [0, 700], [0, 200]]
grc = fix_coords(f['grc_nop'], bbox)
glo = fix_coords(f['glo'], bbox)

scale_factor = 0.29/0.75

src = grc.copy()
tgt = glo.copy()
src[:, 1] = src[:, 1]*scale_factor
tgt[:, 1] = tgt[:, 1]*scale_factor

from sklearn.neighbors import NearestNeighbors

# +
nn = NearestNeighbors()
nn.fit(tgt)
# conns = nn.radius_neighbors(src, radius=8.7, return_distance=False)
# nconns = np.frompyfunc(lambda x: x.size, 1, 1)(conns).astype(int)
# _ = plt.hist(nconns,np.arange(nconns.max()))
# print('Mean connection = {}'.format(np.mean(nconns))
      
conns = nn.kneighbors(src, n_neighbors=4, return_distance=False)

# -

dendvs = np.vstack([glo[conn,:] - grc[i,:] for i, conn in enumerate(conns)])
dendlens = np.sqrt((dendvs**2).sum(axis=-1))
dendlens

dendlens.mean()

dendvs = [glo[conn,:] - grc[i,:] for i, conn in enumerate(conns) if conn.size>0]

dendvs[0][:,0].max()

# +
ml_spread = np.array([z[:,0].max()-z[:,0].min() for z in dendvs])

plt.hist(ml_spread)
print('{}±{}'.format(ml_spread.mean(), ml_spread.std()))

# +
sg_spread = np.array([z[:,1].max()-z[:,1].min() for z in dendvs])

plt.hist(sg_spread)
print('{}±{}'.format(sg_spread.mean(), sg_spread.std()))
# -



plt.hist(dendvs[:,0], 50)

plt.hist(dendvs[:,2], 50)

