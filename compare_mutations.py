from Bio import SeqIO
import pandas as pd
import os

def load_proteins_wt(fasta_file): 
wt_proteins = {} 
for record in SeqIO.parse(fasta_file, "fasta"): 
gene_id = record.id.split()[0].split('[')[0] 
wt_proteins[gene_id] = str(record.seq) 
return wt_proteins

def detect_mutations(wt_seq, query_seq): 
mutations = [] 
for i, (wt_aa, query_aa) in enumerate(zip(wt_seq, query_seq), start=1): 
if wt_aa != query_aa and query_aa != '-': 
mutations.append(f"{wt_aa}{i}{query_aa}") 
return mutations if mutations else ["WT"]

def process_blastx_results(results_folder, wt_proteins): 
results = [] 
for file in os.listdir(results_folder): 
if archivo.endswith(".tsv"): 
path = os.path.join(results_folder, file) 
df = pd. read_csv(route, sep='\t', header=None, 
names=['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 
'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore', 'qseq', 'sseq'])

mutations_strain = []

            for _, row in df.iterrows():
 gen_id_blast = row["sseqid"]
 if gen_id_blast in wt_proteins:
 wt_seq = wt_proteins[gen_id_blast]
 query_seq = row["qseq"]
 mutations = detect_mutations(wt_seq, query_seq)
 mutations_strain. extend([f"{gen_id_blast}_{m}" for m in mutations if m != "WT"])

            strain_name = file.replace(".tsv", "")
 if strain_mutations:
 results.append((strain_name, ",".join(sorted(set(strain_mutations)))))
 else:
 results.append((strain_name, "WT"))

    return results

if __name__ == "__main__":
 fasta_wt = "genes_wt_proteins.fasta"

    for suffix, folder in [("aq20", "results_blastx_aq20"),
 ("aq30", "results_blastx_aq30")]:

        wt_proteins = load_proteins_wt(fasta_wt)
 results = process_blastx_results(folder, wt_proteins).

        df = pd.DataFrame(results, columns=[‘strain’, ‘mutations’])

        df.to_csv(f'mutations_{suffix}.tsv', sep='\t', index=False)
 print(f "Generated file: mutations_{suffix}.tsv")
  
