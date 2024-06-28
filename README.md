
# Ancestral State of Proteins  
  
## Overview  
  
The "Ancestral State of Proteins" project is dedicated to studying the evolutionary processes of protein metamorphism through phylogenetics. By analyzing the evolutionary lineage of proteins, this project aims to uncover how proteins have transformed and adapted through various evolutionary stages.  
  
## Objective  
  
The primary objective of this study is to understand the mechanisms behind protein evolution. By reconstructing the ancestral state of proteins, we can gain insights into the structural and functional adaptations that have occurred over millennia, helping to predict protein functions and interactions in a phylogenetic context.  
  
## Tools  
  
This project utilizes a suite of bioinformatics tools to perform sequence alignments, construct phylogenetic trees, and analyze evolutionary relationships:  
- **MAFFT**: A multiple sequence alignment program which is critical for aligning sequences in preparation for phylogenetic analysis.  
- **HMMER**: Utilized to handle and analyze sequence data using profile hidden Markov models, aiding in the identification and alignment of protein families.  
- **IQ-TREE**: A fast and effective stochastic algorithm to infer phylogenetic trees by maximum likelihood, providing insights into protein evolutionary pathways.  
- **MEGA**: An integrated tool for conducting statistical analysis of molecular evolution and constructing phylogenetic trees with a user-friendly interface.
- **ITOL**: An online tool for the visualization, annotation, and management of phylogenetic trees, allowing for detailed graphical representations of evolutionary data.
- **BELVU**: A versatile tool for viewing and manipulating multiple sequence alignments. It supports various alignment formats and provides functionalities such as alignment editing, filtering, and visualization of conservation patterns.

## Installation  
  
To run the analyses, you will need to install various Python libraries and tools used in this project. All dependencies are listed in the `requirements.txt` file. To install these dependencies, please run the following command in your terminal:  
  
```bash 
pip3 install -r requirements.txt
```   

## Pipeline Steps

### Step 1: Data Preparation and Sequence Extraction

The first step involves preparing the data by loading configurations, input files, and executing functions to rename and process columns accordingly. This includes extracting amino acid sequences from PDB files based on identifiers provided in the input data. This step ensures the data is in the proper format for further analysis.

### Step 2: Search of Homologous sequences

Once we have the sequence of interest, we have to execute another script to find homologous sequences that allow us to do an MSA with MAFFT. However, the MSA was done in the official site of MAFFT due to the facilities that provided the website

### Step 3: Deletion of Residues

After doing the MSA of our homologous sequences and deleted the redundant sequences using belvu. It is necessary the creation of a new script to eliminate the residues from the index before searching them in the proper database The aim of this is to extract the organism whose sequence belong to.

### Step 4: Extract of ID Proteins

The new script, takes the result of step 3 to generate one new plaint text with the ID of each protein, in which using UniProt, we are able to find correctly the organism.

### Step 5: Correction of Index

Finally, we correct the index of each protein, in which appears the entry ID and the organism, to visualize each protein properly later when we upload the treefile in ITOL.

### Step 6: Obtain nodes for visualization

Finally after executing IQ-Tree externally, we obtained a state file that contain the ancestors of each node (From the phylogenetic tree). For obtain the sequences of aminoacids, we need to run this script. The result is a fasta file, crucial to evaluate the changes of the residues using MEGA.
