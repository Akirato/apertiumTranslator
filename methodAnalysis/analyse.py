from __future__ import print_function
import goslate
import sys
gs=goslate.Goslate()
def phrase_wise(filePath):
    a=open(filePath,"r").read()
    lines = a.splitlines()
    need = []
    for i in lines:
        if len(i)>0:
            if not(i[0].isdigit()):
                need.append(i)
    return need

def word_wise(filePath):
    a=open(filePath,"r").read()
    lines = a.splitlines()
    need = []
    for i in lines:
        if len(i)>0:
            if not i[0].isdigit():
            	for j in i.split():
            	    need.append(i+" ")
    return need

def fullSentence_wise(filePath):
    a=open(filePath,"r").read()
    lines = a.splitlines()
    need = ""
    for i in lines:
        need = need + i + " "
    return [need]

def translate(need,langid):
    translated=[]
    for i in need:
        translated.append(gs.translate(i,langid))
    return translated

print(sys.argv[1][:-4])
#print phrase_wise(sys.argv[0])
fp = open("result_phrase.txt","w")
for i in phrase_wise(sys.argv[1]):
    if i[0]!='<':
        print((translate([i],sys.argv[2])[0].encode('utf-8')),file=fp)
fp.close()
fp2 = open("result_sentence.txt","w")
for i in fullSentence_wise(sys.argv[1]):
    if i[0]!='<':
        print((translate([i],sys.argv[2])[0].encode('utf-8')),file=fp2)
fp2.close()
fp3 = open("result_word.txt","w")
for i in word_wise(sys.argv[1]):
    if i[0]!='<':
        print((translate([i],sys.argv[2])[0].encode('utf-8')),file=fp3)
fp3.close()

exit()

