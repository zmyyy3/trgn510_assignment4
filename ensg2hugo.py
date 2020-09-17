
#!/usr/bin/python

import re
import sys
import pandas as pd
import csv

hugo_name = {}   
with open ('Homo_sapiens.GRch37.75.gtf') as file:
     data = file.readlines()   
        
for line in data[5:]:
    gene_id_ensg = re.findall(r'gene_id\s"(.*?)"',line)
    gene_name = re.findall(r'gene_name\s"(.*?)"',line)
    if gene_id_ensg and gene_name:
        hugo_name[gene_id_ensg[0]] = gene_name[0]        
        
if sys.argv[1][:2] != '-f':
    df = sys.argv[1]
    column_number = 0
else:
    df = sys.argv[2] 
    column_number = int(sys.argv[1][2:])-1

df = pd.read_csv(df, quoting=csv.QUOTE_NONE)
gene_id = []
for i in df['"gene_id"']:
    if i.split('.')[0][1:] in hugo_name.keys():
        gene_id.append('\"'+hugo_name[i.split('.')[0][1:]]+'\"')
    else:
        gene_id.append('"Unknown"')
df.iloc[:,column_number]=gene_id   
print(df.to_csv(quoting=csv.QUOTE_NONE, index=False))
