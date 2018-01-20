from nexus import NexusReader
from Bio import SeqIO
import sys

n = NexusReader()
n.read_file("Razafimandimbison_AppS1.txt")

for taxon,characters in n.data:
    print("id:",taxon)
    print("seq:","".join(characters))
    print("")

fasta_in = "Psychotria_rbcLrps16trn.fas" #fastaファイルを読みこみ

for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    desc_part = record.description
    seq = record.seq

    print('id:', id_part)
    print('seq:', seq)
    print("")
    