import json

f1data = f2data = "" 
 
with open('sampleJson/pos_0.png.json') as f1: 
  f1data = f1.read() 
with open('sampleJson/pos_10010.png.json') as f2: 
  f2data = f2.read() 
with open('sampleJson/pos_10492.png.json') as f3: 
  f3data = f3.read() 
 
f1data += "\n"
f1data += f2data + "\n" + f3data
with open ('sampleJson/merge.json', 'a') as f4: 
  f4.write(f1data)





