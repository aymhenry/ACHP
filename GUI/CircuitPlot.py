# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Fri Jun 18 20:16:58 2010

import sys,os
import wx
import math
from matplotlib.figure import Figure
import numpy as np
##sys.path=[os.path.join('..','Props')]+sys.path ## Prepend to ensure that the local version of CoolProp
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from CoolProp.CoolProp import Props

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class CircuitPlot(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: CircuitPlot.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.figure=Figure(figsize=(2,6),dpi=100)
        self.axes=self.figure.add_subplot(111)
        self.canvas=FigureCanvas(self,wx.ID_ANY,self.figure)

    def __set_properties(self):
        # begin wxGlade: CircuitPlot.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: CircuitPlot.__do_layout
        pass
        # end wxGlade
        
    def doPlot(self,**kwargs):
        self.figure.clf()
        self.figure=Figure(figsize=(2,6),dpi=100,facecolor='w')
        self.axes=self.figure.add_subplot(111)
        self.axes.axis([0,0,1,1])
        self.canvas=FigureCanvas(self,wx.ID_ANY,self.figure)
        
        pl=kwargs['pl']
        pt=kwargs['pt']
        Ntubes_bank=int(kwargs['Ntubes_bank'])
        Nbank=int(kwargs['Nbank'])
        Ncircuits=int(kwargs['Ncircuits'])
        
        #plot all the tubes
        for i in range(Ntubes_bank):
            for j in range(Nbank):
                if j % 2 == 0: 
                    self.axes.plot(j*pl,i*pt,'bo')
                else:
                    self.axes.plot(j*pl,i*pt+pt/2.0,'bo')
        
        
        #plot the circuits
        N=int(math.floor(Ntubes_bank/Ncircuits))
        Remainder=int(Ntubes_bank % Ncircuits)
        
        #You have Remainder circuits with N+1 tubes, all others are N tubes
        Nt=[]
        for i in range(Remainder):
            Nt.append(N+1)
        for i in range(Ncircuits-Remainder):
            Nt.append(N)
#        print Nt
        
        r=0
        for i in range(len(Nt)):
            x=np.array([])
            y=np.array([])
            for k in range(Nbank):
                J=np.linspace(0,Nt[i]-1,Nt[i])
                Y=(r+J)*pt
                X=k*pl*(1+0.0*J)
                if k % 2 ==0: #even index
                    x=np.append(x,X)
                    y=np.append(y,Y)
                else:
                    x=np.append(x,X[::-1])
                    y=np.append(y,Y[::-1]+pt/2.0)
            self.axes.plot(x,y,'k',lw=1.5)
#            print x
#            print y
            r=r+Nt[i]
            
        self.axes.axis('off')
        self.axes.axis('equal')


# end of class CircuitPlot

