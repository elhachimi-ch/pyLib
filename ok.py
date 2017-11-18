import lib
import re
import math
import sys
def dist(e, p):
    return abs(e.cord[0]-p.cord[0])+abs(e.cord[1]-p.cord[1])
def chercher(l, l2):
    return set(l).intersection(l2)
class personne:
    pass

sys.stdin= open("ok.txt", "r+")
T= int(input())
for i in range(T):
    j= int(input())
    l=[]
    for k in range(j):
        p= personne()
        s= input().split(" ")
        p.name= s[0]
        p.cord= (int(s[1]), int(s[2]))
        p.criDist= int(s[3])
        s= input()
        p.lTal= list(map(int, s.split(" ")))
        s= input()
        p.lTalCh= list(map(int, s.split(" ")))
        l.append(p)
    print("Case {} :".format(i+1))
    for q in l:
        for e in l:
            if e != q:
                if q.criDist == 0:
                    ll= chercher(q.lTalCh, e.lTal)
                    if ll:
                        print("{} : {}".format(q.name, e.name))
                elif dist(q, e) <= q.criDist:
                    ll= chercher(q.lTalCh, e.lTal)
                    if ll:
                        print("{} : {}".format(q.name, e.name))
