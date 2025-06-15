from Bio import SeqIO
import you

# Load reference genes
wt_genes = {record.id: str(record.seq) for record in SeqIO.parse(«genes_wt.fasta», «fasta»)}

# Search for SNPs in blast alignments
for blast_file in os.listdir("blast_results"):
if blast_file.endswith(«_blast.tsv»):
snps = []
sample = blast_file.replace(«_blast.tsv», «»)

with open(f«results_blast/{blast_file}») as f:
for line in f:
fields = line.strip().split()
ref = wt_genes[fields[1]]
alt = fields[9]

for i, (r, a) in enumerate(zip(ref, alt)):
Yeah r != a:
snps.append(f«pos:{i+1} {r}>{a}»)

with open(f«snps_results/{sample}_snps.txt», «w») as f:
for snp in snps:
f.write(snp + “\n”)
