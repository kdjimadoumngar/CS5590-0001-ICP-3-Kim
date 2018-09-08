
import csv

with open('codon.tsv') as tsvfile:
print(codon)

  reader = csv.reader(tsvfile, delimiter='\t')

  for row in reader:
      if row[0
seq = 'AAAGGGTGCTTTTT'
n = 3] in c
odon:
codon = [seq[i:i+n] for i in range(0, len(seq), n)]

          print(row[1])

    #
    # for line in row:
    #     if codon in line:
    #         print(codon)