from nexus import NexusReader


n = NexusReader()
n.read_file("Razafimandimbison_AppS1.txt")

for taxon,characters in n.data:
    print("id:",taxon)
    print("seq:","".join(characters))
    print("")