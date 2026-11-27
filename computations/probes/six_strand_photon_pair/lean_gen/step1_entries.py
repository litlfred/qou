import sys, json
sys.path.insert(0, "computations/probes/six_strand_photon_pair")
import six_strand_pair_probe as P
import sympy as sp
q = sp.Symbol("q")
rows = P.part1()[0]
targets = [r for r in rows if r["vertices"] in (3, 5) and r["match"] != "other link"]
fact = {("V0V1V0",1,0),("V0V1V0",2,0),("V0V1V2V0V3",0,3),("V0V1V2V0V3",3,0),("V0V1V2V3V0",0,3),("V0V1V2V3V0",3,0),("V1V2V1",2,1),("V1V2V1",3,1),("V2V0V3V1V0",0,3),("V2V0V3V1V0",3,0),("V2V3V0V1V0",0,3),("V2V3V0V1V0",3,0),("V2V3V2",3,2)}
def inb(i,p): return p in (i,i+1,i+2)
def r1(j,s,p):
    if s==j: return p in (j,j+1)
    if inb(j,s): return inb(j,p)
    return p==s
def r2(i,j,s,r):
    if r1(j,s,r): return True
    if r in (i,i+1): return r1(j,s,i) or r1(j,s,i+1) or r1(j,s,i+2)
    if r==i+2: return r1(j,s,i+1) or r1(j,s,i+2)
    return False
out=[]
for row in targets:
    w = P.gg_word(row["verts"])
    amp = {}
    for s in range(6):
        v = P._act({1 << (5-s): sp.Integer(1)}, w, q, 6)   # site s -> bit (n-1-s)
        for k, c in v.items():
            r = 5 - (k.bit_length()-1)
            c = sp.factor(sp.together(c))
            if c != 0: amp[(s, r)] = c
    cells = [(i,j) for i in range(4) for j in range(4) if (row["word"],i,j) not in fact]
    groups = {}
    for (i,j) in cells:
        good = [(s,r) for (s,r) in amp if not r2(i,j,s,r)]
        if not good: continue
        good.sort(key=lambda sr: (sp.degree(sp.numer(amp[sr]),q), sr))
        groups.setdefault(None, []).append(((i,j), good))
    # greedy cover
    rem = dict((c,set(g)) for c,g in groups.get(None,[]))
    chosen=[]
    while rem:
        cnt={}
        for c,g in rem.items():
            for sr in g: cnt[sr]=cnt.get(sr,0)+1
        best=max(cnt, key=lambda sr:(cnt[sr], -sp.degree(sp.numer(amp[sr]),q)))
        cs=[c for c,g in rem.items() if best in g]
        chosen.append((best, cs, str(amp[best])))
        for c in cs: del rem[c]
    out.append({"word":row["word"],"letters":w,"groups":[{"s":b[0][0],"r":b[0][1],"cells":b[1],"amp":b[2]} for b in chosen]})
json.dump(out, open(sys.argv[1],"w"))
print(len(out), sum(len(o["groups"]) for o in out), sum(len(g["cells"]) for o in out for g in o["groups"]))
