## 🔹 Scripts used:

- **translate_wt.py:**
Translates reference genes from nucleotides to proteins.

- **run_blastx.sh:**
Searches for homologues of its isolates in the reference protein (using BLASTX).

- **compare_mutations.py:**  
  Detects and reports amino acid mutations in each isolate compared to the wild type.

- **detect_snps.py:**
Searches for SNPs directly in the DNA (without taking the reading frame into account).

# Candida Auris Mutation Analysis

This pipeline performs:
- Translation of wild-type genes to proteins.
- BLASTX alignment of isolates against wild-type proteins.
- Amino acid mutation calling.

## 🔹 Installation

```bash
pip install biopython pandas
```

## 🔹 RUN PIPELINE
```
python traducir_wt.py
chmod +x run_blastx.sh
./run_blastx.sh
python comparar_mutaciones.py
```
