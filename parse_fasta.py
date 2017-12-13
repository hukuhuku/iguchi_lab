#!/usr/bin/env python

import sys
from Bio import SeqIO

fasta_in = sys.argv[1] #fastaファイルを読みこみ


for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    desc_part = record.description
    seq = record.seq

    print('id:', id_part)
    print('desc:', desc_part)
    print('seq:', seq[49:499])
    
    
#結果をファイルに保存したい場合はリダイレクトを使う

#コマンドプロンプトでの例
#python fasta_extraction.py fasta_extraction arsa_result.fasta palmata > res.fasta



