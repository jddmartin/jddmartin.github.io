#!/usr/bin/python

import os

cp=[(1,'a'),(1,'b'),(1,'c'),(1,'d'),(2,'a'),(2,'b'),(2,'c')]

for component,part in cp:
    precursor='component_'+str(component)+"_part_"+part
    inputfilename='diagrams/'+precursor+'_setup.png'
    outputfilename=precursor+'.jpg'
    command=("convert -bordercolor white -border 50x50 "+
        "-density 600x600 -quality 100 -define pdf:use-cropbox=true "+
        "-geometry 600 "+inputfilename+" "+outputfilename)
    os.system(command)

           
