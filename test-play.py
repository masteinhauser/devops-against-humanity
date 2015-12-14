#!/usr/bin/env python
import urllib,csv,random,re

white=[]
black=[]

with open('cards-DevOpsAgainstHumanity.csv', 'rb') as csvfile:
    for r in csv.reader(csvfile):
        if r[0]: white.append(r[0])
        if r[1]: black.append(r[1])

blank=re.compile(r"( +)?(\b|[^_])_+(\b|[^_])( +)?")
rpl=lambda _:" %s " % random.choice(white)
for _ in range(10):
    print(re.sub(blank,rpl,random.choice(black)).strip().replace(' .','.'))
