# Add the functions in this file
import math
import json

def load_journal(filename):
 f=open(filename)
 journal_dict=json.load(f)
 return journal_dict
            
def compute_phi(filename,event):
 n=[0,0,0,0]
 journal_dict=load_journal(filename)

 for i in range(0,91):
  if event in journal_dict[i]['events'] and journal_dict[i]['squirrel']==True:
   n[3]=n[3]+1
  elif journal_dict[i]['squirrel']==True:
   n[1]=n[1]+1
  elif event in journal_dict[i]['events']:
   n[2]=n[2]+1
  else:
   n[0]=n[0]+1
 
 value=(n[3]*n[0]-n[2]*n[1])/math.sqrt((n[3]+n[2])*(n[0]+n[1])*(n[3]+n[1])*(n[0]+n[2]))
 return value
 
def compute_correlations(filename):
 journal_dict=load_journal(filename)
 final_dict={}

 for i in range(0,91):
  for event in journal_dict[i]['events']:
   if event not in final_dict:
    final_dict[event]=compute_phi(filename,event)
     
 return final_dict
    
def diagnose(filename):
 final_dict={}
 final_dict=compute_correlations(filename)
 max_dict={}
 maximum=-1
  
 for event in final_dict:
  if final_dict[event]>maximum:
   maximum=final_dict[event]
   positive=event
   max_dict={}
   max_dict[event]=maximum

 min_dict={}
 minimum=1 

 for event in final_dict:
  if final_dict[event]<minimum:
   minimum=final_dict[event]
   min_dict={}
   negative=event
   min_dict[event]=minimum
 
 return positive,negative
 
print(diagnose('journal.json'))
 
