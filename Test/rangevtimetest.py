#!/usr/bin/env python
"""
quad plot
REQUIRES mayavi for upper left plot (python 2.7 only)

@author: John Swoboda
"""
from __future__ import division,absolute_import
from matplotlib.pyplot import subplots, show
#
from GeoData.plotting import rangevstime
#
from load_isropt import load_risromti

def makeplot(risrName):
    risr = load_risromti(risrName)[0]
#%%
    (figmplf, [ax1,ax2]) = subplots(2, 1,figsize=(16, 10))

    vbnd = [5e10,5e11]
    beamnum=1
    beampair = risr.dataloc[0,1:]

    rangevstime(risr,beamnum,vbnd,'ne',fig=figmplf,ax=ax1)
    rangevstime(risr,beampair,vbnd,'ne',fig=figmplf,ax=ax2)

if __name__ == "__main__":
    makeplot('ran120219.004.hdf5')
    show()
