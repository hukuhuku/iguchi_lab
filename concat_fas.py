from Bio import SeqIO
import sys

fasta_in_1 = sys.argv[1]
fasta_in_2 = sys.argv[2]

id_dict = {}
seq_dict = {}
queue = []


for record in SeqIO.parse(fasta_in_1, 'fasta'):
    id_part = record.id
    species_name,sample_name,genome_name = list(map(str,id_part.split("_")))
    seq = record.seq
    len_seq1 = len(seq)

    id_dict[sample_name] = species_name+"_"+sample_name
    seq_dict[sample_name] = seq
    
    queue.append(sample_name)

for record in SeqIO.parse(fasta_in_2, 'fasta'):
    id_part = record.id
    seq = record.seq
    len_seq2 = len(seq)

    species_name,sample_name,genome_name = list(map(str,id_part.split("_")))
    
    print(">"+ species_name +"_"+ sample_name)
    if sample_name in queue:
        print(seq + seq_dict[sample_name])
        queue.remove(sample_name)
    else:
        print(seq+"*"*len_seq1)

for sample in queue:
    print(">"+id_dict[sample])
    print(seq_dict[sample_name]+"*"*len_seq2)


#二つのfasファイルをdescripiton部分の情報から結合する
#一致するものがない場合は＊によってギャップを入れている
#ギャップの長さは一致しなかった遺伝子領域の一つのサンプルのseqの長さを利用している
#サンプルごとに遺伝子領域の長さが違うことを考慮していないのでそこは調べる必要がありそう


#python concat_fas.py test.fas test2.fas　>> res.fas みたいな感じでやれば結合出力できる
    