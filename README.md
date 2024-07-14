# Atomic Distance Calculator
 This repo calculates the distances of alpha carbon atoms between two chains of a protein.

## Motivation
 Protein structure and dynamics play a crucial role in many biological processes and are involved in a wide range of diseases. Understanding the structural relationships between different regions of a protein can provide insights into protein function, stability and evolution. The ability to accurately predict the atomic distance between Cα atoms of two proteins can aid in the identification of structural motifs, prediction of protein flexibility, comparison of the similarity of the structure of different proteins and identification of conformational changes.
 This script aims to provide an efficient and easy-to-use tool for researchers and scientists working in structural biology and bioinformatics to calculate the atomic distance between Cα atoms of two proteins. By automating the process of calculating Cα atomic distances, this script can save valuable time and resources for researchers, allowing them to focus on analyzing and interpreting the results.

## Dependencies
 - Numpy
 - Pandas
 - Seaborn
 - Matplotlib

## Installation
 ```git clone https://github.com/mehdikosaca/Atomic-Distance-Calculator.git```

## Usage
 The script takes a PDB filea as input and calculates the atomic distance between Cα atoms between two chains.
 ```python distance.py <pdb-file> <chain 1> <chain 2> ```

### Input
 - PDB File

### Output
 - <b>Pairwise Distance List:</b> Text file including the residue and distance information.
 - <b>Distance Plot:</b> Cluster map displays the atomic distance between residues of each chains.

 
