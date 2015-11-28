# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:31:37 2015

@author: Bellatrics
"""

import re
import networkx as nx
import json



def myfile2graph(fname):
  
  with open(fname,'r') as f:
    ll = f.readlines()
  
  
  commands = []
  for l in ll:
    l = re.sub(r'[\n]+','',l)
    if len(l)==0:
      
      continue
    #print l
    
    oper = re.findall(r'-\s*>|<\s*-|=',l)
    if len(oper) != 1:
      print l, 'a'
      continue
    oper = oper[0]
    ss = re.split(oper,l)
      
    #print ss
    
    #nuska r'([\w\.-]+)'
    #new   r'([\w-]+)'
    ss =  [oper] +[re.findall( r'([\w\.-]+)', s) for s in ss]
  
    commands.append (tuple(ss))
  
  
  atoms = []
  for c,xx,yy in commands:
    for x in xx:
      for y in yy:
        atoms.append((c,x,y))
    
  
  G = nx.DiGraph()
  
  for c,a,b in atoms:
    if c=='->':
      G.add_edge(a, b)
    if c=='<-':
      G.add_edge(b, a)
    if c=='<-':
      G.add_edge(a, b)
      G.add_edge(b, a)
  
  return G
  
  

def graph2json (G, fname):
  data = nx.readwrite.json_graph.node_link_data(G)
  s = json.dumps(data)
  with open(fname,'w') as f:
    f.write(s)

  

