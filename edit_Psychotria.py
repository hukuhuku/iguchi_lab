###元データがrubra_Amami_a230_rbcLだったりrubra_Amamia230_rbcLだったりと表記ゆれがあるので
###すべて「種名_サンプル名_遺伝子領域名」に統一する

from Bio import SeqIO
import sys

fasta_in = sys.argv[1] #fastaファイルを読みこみ


for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    seq = record.seq

    ID = list(map(str,id_part.split("_")))
    
    if 1 < (len(ID)-2):
        sample_name = "".join(ID[1:-1])
    else:
        sample_name = ID[1]

    print(">"+ID[0] +"_"+ sample_name +"_"+ ID[-1])
    print(seq)
    
    
#結果をファイルに保存したい場合はリダイレクトを使う

#コマンドプロンプトでの例
#python edit_Psychoria Psychotria_rbcK.fas >> hoge.fas



