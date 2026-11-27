"""Step 4: the 25 cells step 1 cannot block with a single entry.

Usage (from the repo root, OUT as for steps 1-3):
    python3 computations/probes/six_strand_photon_pair/lean_gen/step4_sector_certificates.py \
        $OUT/entries2.json folio/quantum-observable-universe/lean/QOU/MassTheory/PhotonPairNoFactorSector.lean

For each uncovered cell it writes the one-marked-strand sector equations (sites 0..6, with the
Lean semantics of sig / sigInv / photon / wordAct) and asks Singular (apt package "singular") for
a Groebner basis. 19 cells give the unit ideal; for those it takes a Singular "lift" certificate
1 = sum g_k f_k (with q*qi = 1, t*mu = 1, u*(q - qi) = 1), checks it exactly in sympy, and emits
a Lean proof by linear_combination. The other 6 cells have solutions: they are the two-photon
products proved in PhotonPairIdleFactor.lean. Exact arithmetic only.
"""
import sys, json, re, subprocess
import sympy as sp
q,qi,a,b,c,A,B,C,mu=sp.symbols('q qi a b c A B C mu')
N=8
def sig(i,v):
    return [ (v[i+1]+(q-qi)*v[i]) if p==i else (v[i] if p==i+1 else q*v[p]) for p in range(N)]
def sigInv(i,v):
    return [ v[i+1] if p==i else ((v[i]-(q-qi)*v[i+1]) if p==i+1 else qi*v[p]) for p in range(N)]
def photon(x,y,z,i,v):
    s1=sig(i,v); s2=sig(i+1,v); s3=sig(i,sigInv(i+1,v))
    return [v[p]+x*s1[p]+y*s2[p]+z*s3[p] for p in range(N)]
def word(w,v):
    for (k,pos) in reversed(w):
        v = sig(k,v) if pos==1 else sigInv(k,v)
    return v
def eqs(w,i,j):
    out=[]
    for s in range(7):
        e=[sp.Integer(1) if p==s else sp.Integer(0) for p in range(N)]
        L=photon(a,b,c,i,photon(A,B,C,j,e)); R=word(w,e)
        for r in range(7):
            d=sp.expand(L[r]-mu*R[r])
            if d!=0: out.append(((s,r),d))
    return out

FACT = {("V0V1V0",1,0),("V0V1V0",2,0),("V0V1V2V0V3",0,3),("V0V1V2V0V3",3,0),("V0V1V2V3V0",0,3),("V0V1V2V3V0",3,0),("V1V2V1",2,1),("V1V2V1",3,1),("V2V0V3V1V0",0,3),("V2V0V3V1V0",3,0),("V2V3V0V1V0",0,3),("V2V3V0V1V0",3,0),("V2V3V2",3,2)}
d = json.load(open(sys.argv[1]))
miss = []
for o in d:
    cov = {tuple(cc) for g in o["groups"] for cc in g["cells"]}
    for i in range(4):
        for j in range(4):
            if (o["word"], i, j) not in FACT and (i, j) not in cov:
                miss.append((o["word"], i, j, o["letters"]))
assert len(miss) == 25, len(miss)
NF = []
for k, (nm, i, j, w) in enumerate(miss):
    gens = [str(dd) for _, dd in eqs(w, i, j)] + ["q*qi-1", "t*mu-1", "u*(q-qi)-1"]
    prog = "ring R=0,(a,b,c,A,B,C,mu,t,u,q,qi),dp;\nideal I=" + ",".join(gens) + ";\nprint(std(I));\nquit;\n"
    out = subprocess.run(["Singular", "-q"], input=prog, capture_output=True, text=True, timeout=600).stdout.split()
    if out == ["_[1]=1"] or out == ["1"]:
        NF.append(k)
    else:
        print("solution exists:", nm, i, j)
assert len(NF) == 19, NF
q,qi,a,b,c,A,B,C,mu,t,u=sp.symbols('q qi a b c A B C mu t u')
res=[]
for k in NF:
    nm,i,j,w=miss[k]
    E=eqs(w,i,j)
    gens=[str(d) for _,d in E]+["q*qi-1","t*mu-1","u*(q-qi)-1"]
    prog="ring R=0,(a,b,c,A,B,C,mu,t,u,q,qi),dp;\nideal I="+",\n".join(gens)+";\nmatrix T=lift(I,ideal(1));\nint k;for(k=1;k<=ncols(I);k++){print(string(T[k,1]));print(\"@@\");}\n"
    out=subprocess.run(["Singular","-q"],input=prog+"quit;\n",capture_output=True,text=True,timeout=600).stdout
    cof=[x.strip().replace("\n","") for x in out.split("@@")][:len(gens)]
    G=[sp.sympify(x) for x in cof]; F=[sp.sympify(x) for x in gens]
    chk=sp.expand(sum(g*f for g,f in zip(G,F)))
    assert chk==1, (k,chk)
    res.append({"k":k,"word":nm,"i":i,"j":j,"letters":w,"entries":[list(sr) for sr,_ in E],"cof":[str(g) for g in G],"nterms":sum(len(sp.Add.make_args(sp.expand(g))) for g in G if g!=0)})
    print(k,nm,i,j,res[-1]["nterms"],flush=True)
ren={'A':'a2','B':'b2','C':'c2','mu':'μ','t':'tt','u':'uu'}
def lean(e):
    s=str(sp.sympify(e)).replace('**','^')
    return re.sub(r'\b(A|B|C|mu|t|u)\b', lambda m: ren[m.group(1)], s)
words={}
for r in res: words.setdefault(r["word"], r["letters"])
L=[]
L.append('''import QOU.MassTheory.PhotonPairReachability

/-!
# The last 19 non-factorising cells of the six-strand photon-pair test

`PhotonPairNoFactor` proves, by a single blocked matrix entry, that 1370 (word, i, j) cells of the
pair test are not two-photon products. Of the 25 cells it leaves out, 6 ARE two-photon products
(`PhotonPairIdleFactor`). This file proves the other 19 are not, on the one-marked-strand sector.

Each proof takes the sector equations `γᵢγⱼ eₛ = μ·w eₛ` at the entries listed, together with
`q·qi = 1`, `tt·μ = 1` and `uu·(q − qi) = 1`, and derives `1 = 0` by `linear_combination` with an
explicit polynomial certificate (a Nullstellensatz certificate). So the statement holds for every
`q` with `q·qi = 1` and `q ≠ ±1`, and every `μ ≠ 0`, over any field.

The certificates were found with Singular's `lift` and checked exactly in sympy before emission;
Lean re-checks each one with `ring`.

-- Ref: [leitner2026] computations/probes/six_strand_photon_pair/six_strand_pair_probe.py
-/

namespace QOU.MassTheory.PhotonPairNoFactorSector

open QOU.MassTheory.PhotonPairReachability

variable {K : Type*} [Field K]
''')
names={}
for n,(wname,lets) in enumerate(words.items()):
    names[wname]=f"u{n}"
    body=", ".join(f"({x}, {'true' if s==1 else 'false'})" for x,s in lets)
    L.append(f"/-- The γγ word `{wname}`. -/\ndef u{n} : List (ℕ × Bool) := [{body}]\n")
for r in res:
    used=[(sr,g) for sr,g in zip(r["entries"]+[None,None,None], r["cof"]) ]
    eqterms=[]; haves=[]; hn=[]
    for idx,(sr,g) in enumerate(used[:len(r["entries"])]):
        if sp.sympify(g)!=0:
            s_,r_=sr; nm=f"e{s_}_{r_}"; hn.append(nm)
            haves.append(f"  have {nm} := congrFun (H (basisVec {s_})) {r_}")
            eqterms.append(f"({lean(g)}) * {nm}")
    gq,gt,gu=r["cof"][-3:]
    for g,nm in ((gq,'hqi'),(gt,'ht'),(gu,'hu')):
        if sp.sympify(g)!=0: eqterms.append(f"({lean(g)}) * {nm}")
    wn=names[r["word"]]
    L.append(f'''/-- `{r["word"]}` at photon positions `({r["i"]}, {r["j"]})` is not a two-photon product. -/
theorem noPair_{r["word"]}_{r["i"]}_{r["j"]} (q qi : K) (hqi : q * qi = 1) (hh : q - qi ≠ 0)
    (a b c a2 b2 c2 μ : K) (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c {r["i"]} (photon q qi a2 b2 c2 {r["j"]} v) = fun p => μ * wordAct q qi {wn} v p := by
  intro H
  obtain ⟨tt, ht⟩ : ∃ tt : K, tt * μ = 1 := ⟨μ⁻¹, inv_mul_cancel₀ hμ⟩
  obtain ⟨uu, hu⟩ : ∃ uu : K, uu * (q - qi) = 1 := ⟨(q - qi)⁻¹, inv_mul_cancel₀ hh⟩
{chr(10).join(haves)}
  simp only [photon, wordAct, {wn}, sig, sigInv, basisVec, Nat.reduceAdd, Nat.reduceEqDiff,
    ↓reduceIte] at {" ".join(hn)}
  exact one_ne_zero (by linear_combination {" + ".join(eqterms)} : (1 : K) = 0)
''')
L.append("end QOU.MassTheory.PhotonPairNoFactorSector\n")
open(sys.argv[2],"w").write("\n".join(L))
