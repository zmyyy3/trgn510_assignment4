About the app
======
This app will take comma-delimited file as an argument and column number as an input and print a file with Ensembl gene name has been converted to HUGO gene name.

Installation & Usage
-------
1.  Use `git clone https://github.com/zmyyy3/trgn510_assignment4` to clone this application into your server.
2.  "Homo_sapiens.GRCh37.75.gtf" is the reference file used to build a dictionary. You need to download this file by using `wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz`, and unzip this file by using `gunzip Homo_sapiens.GRCh37.75.gtf.gz`.
3.  In the repository, "expres.anal.hugo.example.csv" is an example result of a unit test. If you want to take a unit test, you could download "expres.anal.csv" by using `wget https://github.com/davcraig75/unit/expres.anal.csv`, and run this application by using `python ensg2hugo.py -f2 expres.anal.csv > expres.anal.hugo.csv`. Then you will get a file named "expres.anal.hugo.csv", and you can check if the "expres.anal.hugo.csv" is the same as "expres.anal.hugo.example.csv".
4.  For the command `python ensg2hugo.py -f2 expres.anal.csv > expres.anal.hugo.csv`, "-f[0-9]" is an option for column number. In the example, we used command "-f2" because the Ensembl gene name is in the second column, and "2" means picking up second column. If there is no "-f", the first column will be picked up. Therefore, you can according to your file to change the column number with this option"-f[0-9]".

Notes
----------
The dictionary in this application is not comprehensive, and some Ensembl gene names in your file may not have matched HUGO gene names, so it will show "Unknown" in the column of "gene_id".

Dependencies
----------
1.  git
2.  wget
3.  sys
4.  re
5.  pandas
6.  csv

Contact
--------
mzhang11@usc.edu
