#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import os

pdb_file = sys.argv[1]
pdb = pdb_file[:-4] #pdb filename without .pdb extension
chain_1 = sys.argv[2]
chain_2 = sys.argv[3]
import seaborn as sns
import matplotlib.pyplot as plt
	


class InterfaceResidues():	
	def __init__(self):
		self.chain_ids = []
		self.unique_chains = []
		self.amino_acids = []
		self.chains = []
		self.chain_1 = []
		self.chain_2 = []
		self.chain_1_coord = []
		self.chain_2_coord = []
		self.chain_1_coord_float = []
		self.chain_2_coord_float = []
		self.interaction_list = []
		self.one_letter_codes = []
	
	def PDBParse(self):
		with open("{}".format(pdb_file), "r") as pdbfile:
			for line in pdbfile:
				if line[:4] == "ATOM":
					if line[21] == chain_1:
						if line[13:15] == "CA":
							splitted_chain_1 = [line[:6], line[6:11], line[12:16], line[17:20], line[21], line[22:26], line[30:38], line[38:46], line[46:54]]
							self.chain_1.append(splitted_chain_1)
							self.chain_1_coord.append(splitted_chain_1[6:9])
					if line[21] == chain_2:
						if line[13:15] == "CA":
							splitted_chain_2 = [line[:6], line[6:11], line[12:16], line[17:20], line[21], line[22:26], line[30:38], line[38:46], line[46:54]]
							self.chain_2.append(splitted_chain_2)
							self.chain_2_coord.append(splitted_chain_2[6:9])
	
	def ChainCoordinates(self):
		for i in np.arange(0,len(self.chain_1),1):
			self.chain_1_coord_float.append([float(ele) for ele in self.chain_1_coord[i]])
		for i in np.arange(0,len(self.chain_2),1):
			self.chain_2_coord_float.append([float(ele) for ele in self.chain_2_coord[i]]) 			
			
	def FindDistances(self):
		interaction = open("{}_pairwise_distance_list".format(pdb), "w")
		print("Atom1|AA1|ChainID1|Atom2|AA2|ChainID2|Distance", file = interaction)
		for i in np.arange(0,len(self.chain_1),1):
			for j in np.arange(0,len(self.chain_2),1):
				distance = ((self.chain_2_coord_float[j][0]-self.chain_1_coord_float[i][0])**2+(self.chain_2_coord_float[j][1]-self.chain_1_coord_float[i][1])**2+(self.chain_2_coord_float[j][2]-self.chain_1_coord_float[i][2])**2)**0.5
				print(self.chain_1[i][2],self.chain_1[i][3]+"_"+self.chain_1[i][5],self.chain_1[i][4],self.chain_2[j][2],self.chain_2[j][3]+"_"+self.chain_2[j][5],self.chain_2[j][4],distance, file = interaction,sep = "|")

		interaction.close()


def main():
	s = InterfaceResidues()
	s.PDBParse()
	s.ChainCoordinates()
	s.FindDistances()
	df = pd.read_table("6m0j_pairwise_distance_list",sep = "|")
	pivot = df.pivot_table(index=['AA1'], columns=['AA2'], values='Distance')
	sns.clustermap(pivot,cmap="RdBu",figsize=(15, 15))
	plt.savefig("{}_distance_plot.pdf".format(pdb))
	
if __name__ == "__main__":
	main()
