from Bio import SeqIO

with open("genes_wt_proteins.fasta", "w") as salida:
    for record in SeqIO.parse("genes_wt.fasta", "fasta"):
        secuencia = record.seq
        secuencia = secuencia[:len(secuencia) - len(secuencia) % 3]
        proteina = secuencia.translate()
        record.seq = proteina
        record.description += " [traducción]"
        SeqIO.write(record, salida)
