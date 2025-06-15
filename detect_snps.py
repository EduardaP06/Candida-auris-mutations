from Bio import SeqIO
import os

# Carga genes de referencia
wt_genes = {record.id: str(record.seq) for record in SeqIO.parse(«genes_wt.fasta», «fasta»)}

# Busca SNPs en alineaciones de blast
for blast_file in os.listdir(«resultados_blast»):
    if blast_file.endswith(«_blast.tsv»):
        snps = []
        sample = blast_file.replace(«_blast.tsv», «»)

        with open(f«resultados_blast/{blast_file}») as f:
            for line in f:
                fields = line.strip().split()
                ref = wt_genes[fields[1]]
                alt = campos[9]

                para i, (r, a) en enumerate(zip(ref, alt)):
                    si r != a:
                        snps.append(f«pos:{i+1} {r}>{a}»)

        con abierto(f«snps_resultados/{muestra}_snps.txt», «w») como f:
            for snp in snps:
                f.write(snp + “\n”)
