
# b. Write a Python program for the following DNA application using dictionaries


seq = 'AAAGGGTTTTTT'

n = 3

codon = [seq[i:i+n] for i in range(0, len(seq), n)]

print(codon)


