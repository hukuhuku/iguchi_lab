#!/usr/bin/env python

from xml.etree import ElementTree

import sys

xml = ElementTree.parse(sys.argv[1])#xmlファイル読み込み
Con = sys.argv[2]#国名指定(特に指定がない場合は”hoge"と入力)
Org = sys.argv[3]#種名指定(とくに指定がない場合は”hoge"と入力)

root = xml.getroot()#xmlのrootをとる

for item in root:#root直下の子要素
    locus = item.findtext("INSDSeq_locus")
    sequence = item.findtext("INSDSeq_sequence")
    for child in item:
        if child.tag == "INSDSeq_feature-table":
            for ref in child:#featrure-table直下の子要素
                for fea in ref:
                    if fea.tag == "INSDFeature_quals":
                        for qua in fea:#Feature_qualsの子要素
                            name = qua.findtext("INSDQualifier_name")#<…name>に囲まれている部分をとる
                            value = qua.findtext("INSDQualifier_value")#<…value>に囲まれている部分をとる
                            if name == "country":
                                country = value
                            if name == "organism":
                                organism = value

    Output = True
    if Org != "hoge" and Con != "hoge":#どちらも指定があるとき
        if organism != Org and country != Con:
            Output = False
    elif Con != "hoge":#国めいにのみ指定があるとき
        if country != Con:
            Output = False
    elif Org != "hoge":#種名にのみ指定があるとき
        if organism != Org:
            Output = False

    #条件を満たす(与えられた国,種名)場合のみ出力
    if Output:
        print(locus+"_"+organism+"_"+country)
        print(sequence)
        print("")