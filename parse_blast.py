from Bio.Blast import NCBIXML

path ="2VJM4KYR014-Alignment.xml"

with open(path, mode = 'r', encoding = 'utf-8') as fh:
    blast_records = NCBIXML.parse(fh)
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
             for hsp in alignment.hsps:
                 he = '>' + alignment.title + '|'
                 he += str(hsp.score) + '|'
                 he += str(hsp.bits) + '|'       
                 he += str(hsp.identities)
                 """
                 ある条件によって抽出したい場合は,ここでif文を追加する
                 
                 [例]
                 scoreによって抽出したい場合は if hsp.score < ("数値"): 
                 生物種によって抽出したい場合は　if hsp.identites.find("Homo sapiens"):
                 
                 """
                 print(he)
                 print(hsp.query[1:80])
                 print(hsp.match[1:80])
                 print(hsp.sbjct[1:80])
