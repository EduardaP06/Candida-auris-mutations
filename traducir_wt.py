  from Bio import SeqIO

with open(“genes_wt_proteins.fasta”, “w”) as output:
    for record in SeqIO.parse(“genes_wt.fasta”, “fasta”):
        sequence = record.seq
        sequence = sequence[:len(sequence) - len(sequence) % 3]
        protein = sequence.translate()
        record.seq = protein
        record.description += “ [translation]”
        SeqIO.write(record, output)
