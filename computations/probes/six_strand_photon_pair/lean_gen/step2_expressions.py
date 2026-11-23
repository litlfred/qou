import json, sys, sympy as sp
S=sys.argv[1]
d=json.load(open(S+"/entries2.json"))
q,qi=sp.symbols("q qi")
def sig(i,v):
    o={}
    for p in set(v)|{i,i+1}:
        if p==i: val=v.get(i+1,0)+(q-qi)*v.get(i,0)
        elif p==i+1: val=v.get(i,0)
        else: val=q*v.get(p,0)
        o[p]=sp.expand(val)
    return o
def sigInv(i,v):
    o={}
    for p in set(v)|{i,i+1}:
        if p==i: val=v.get(i+1,0)
        elif p==i+1: val=v.get(i,0)-(q-qi)*v.get(i+1,0)
        else: val=qi*v.get(p,0)
        o[p]=sp.expand(val)
    return o
def act(letters,v):
    for (i,s) in reversed(letters):
        v = sig(i,v) if s>0 else sigInv(i,v)
    return v
def lean(e): return str(e).replace("**","^")
out=[]; nth=0
words=[]
for k,o in enumerate(d):
    L=o["letters"]
    lw="[" + ", ".join(f"({i}, {'true' if s>0 else 'false'})" for i,s in L) + "]"
    words.append((k,o["word"],lw))
    for g,grp in enumerate(o["groups"]):
        s,r=grp["s"],grp["r"]
        E=act(L,{s:sp.Integer(1)}).get(r,0)
        amp=sp.sympify(grp["amp"]); qq=sp.Symbol("q")
        assert sp.simplify(E.subs(qi,1/q)-amp.subs(qq,q))==0
        # factor amp = sign * q^k * (q^2-1)^e
        f=sp.factor(amp.subs(qq,q)); e=0
        num,den=sp.fraction(f)
        if sp.rem(num, q**2-1, q)==0: e=1; core=sp.cancel(f/(q**2-1))
        else: core=f
        sign=1
        if core.could_extract_minus_sign(): sign=-1; core=-core
        k_=sp.degree(sp.numer(core),q)-sp.degree(sp.denom(core),q)
        assert sp.simplify(core-q**k_)==0
        A=k_+e
        T = sign*(q**A if A>=0 else qi**(-A))*(q-qi)**e
        quo,rem=sp.div(sp.expand(E-T), q*qi-1, q, qi)
        assert rem==0, (o["word"],E,T,rem)
        cells="[" + ", ".join(f"({i}, {j})" for i,j in grp["cells"]) + "]"
        nz=[]
        if sign<0: nz.append("neg")
        out.append(dict(k=k,g=g,s=s,r=r,E=lean(E),T=lean(T),cof=lean(sp.expand(quo)),cells=cells,
                        A=int(A),e=int(e),sign=int(sign),word=o["word"],n=len(grp["cells"])))
json.dump({"groups":out,"words":words},open(S+"/lean_gen.json","w"))
print(len(out), max(len(x["E"]) for x in out), max(len(x["cof"]) for x in out))
