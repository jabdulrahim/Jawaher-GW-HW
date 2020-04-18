

import os
import csv

with open('Resources\cereal.csv') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csvheader = next (csvfile)
    

    
    for row in csvreader:
        
     
        
        if  ( float (row [7]) >= 5 ):
    
           print (row)
       
     
      