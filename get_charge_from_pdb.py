"""Code to get the charge of a protein from the PDB file.

Usage: python3 get_charge_from_pdb.py <file-name>"""

from Bio.PDB import *
from sys import argv

def get_charge(sequence):
"""Determines charge from sequence.
  D, E = -1
  K, R = +1
  C, H = write a message because of their unknown protonation states."""
  charge, hc = 0, 0
	for aa in sequence:
		if aa in ['D', 'E']:
			charge -= 1
		elif aa in ['K', 'R']:
			charge += 1
		elif aa in ['H', 'C']:
			hc +=1
	print(f"Found {hc} HIS/CYS. The charge is {charge}.")

def get_seq_ch(sequence):
  """Prints the sequence and its charge."""
	print(f"Sequence is: {sequence}")
	get_charge(sequence)

# check if a file is supplied
if len(argv) == 1 :  #no arguments specified
	print("No input pdb file specified!")
	exit(1)
	
# get structure and sequence
parser = PDBParser(QUIET = True)
try:
	structure = parser.get_structure("A", argv[1])
except:
	print("Cannot get structure from file. The file likely does not exist or does not contain a PDB structure.")
ppb = PPBuilder()
polypeptides = ppb.build_peptides(structure)

# get the sequence
pepnum = 1
sequence = ''
if len(polypeptides) == 0:			# no polypeptide produced
	print("Cannot determine sequence! The file likely contains DNA/RNA.")
elif len(polypeptides) > 1:			# more than one polypeptide produced
	for i in range(0, len(polypeptides)):
		sequence += str(polypeptides[i].get_sequence())
		if i != len(polypeptides) - 1:
			if polypeptides[i][-1].get_id()[1] > polypeptides[i+1][1].get_id()[1]:			# check if there are more chains or if one is broken
				print(f"--- Polypeptide #{pepnum} ---")
				get_seq_ch(sequence)
				sequence = ''
				pepnum += 1
		else:
			print(f"--- Polypeptide #{pepnum} ---")
			get_seq_ch(sequence)
else:							# exactly one polypeptide produced
	print(f"--- Polypeptide #{pepnum} ---")
	sequence = polypeptides[0].get_sequence()
	get_seq_ch(sequence)
