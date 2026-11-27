exec(open('coef.py').read().split("for (a,b),(x,y)")[0])
def lean(d,v):
    ks=[k for k in sorted(d) for _ in range(d[k])]
    t=' + '.join(v+names[k] for k in ks)
    return t if len(ks)==1 else '('+t+')'
def comb(sol,items,v):
    parts=[]
    for i,c in enumerate(sol):
        if c==0: continue
        a,b=items[i]; A,B=lean(a,v),lean(b,v)
        term=f"({A} * {B} - {B} * {A})"
        parts.append(('+ ' if c>0 else '- ')+term)
    s=' '.join(parts)
    return s[2:] if s.startswith('+ ') else '-'+s[1:] if False else s
fieldnames=['f12_34','f13_24','f14_23','n12_3','n13_2','n23_1','n12_4','n14_2','n24_1','n13_4','n14_3','n34_1','n23_4','n24_3','n34_2']
used=[0,1,2,3,4,6,8,9,10,12,15]
FV=[comm(a,b) for _,a,b in facts]
items=[(a,b) for _,a,b in facts]
out=[]
out.append("/-- A six-tuple satisfying ten bracketing-local commutations and the far relation `[s₁₃, s₂₄] = 0`\nis a `DK4` family. (Pure linear algebra on commutators; the coefficients are `±1`.) -/")
out.append("theorem dk4_of_locals {s12 s13 s14 s23 s24 s34 : R}")
for i in used:
    a,b=items[i]; out.append(f"    (h{i} : Commute {lean(a,'s')} {lean(b,'s')})")
out[-1]+=" :"
out.append("    DK4 s12 s13 s14 s23 s24 s34 := by")
for i in used:
    a,b=items[i]; A,B=lean(a,'s'),lean(b,'s')
    out.append(f"  have z{i} : {A} * {B} - {B} * {A} = 0 := sub_eq_zero.mpr h{i}.eq")
out.append("  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩")
for (a,b),(x,y) in zip(DKp,targets):
    sol=solve(comm(x,y))
    A,B=lean(x,'s'),lean(y,'s')
    zs=', '.join(f"z{i}" for i,c in enumerate(sol) if c)
    out.append(f"  · show {A} * {B} = {B} * {A}")
    out.append(f"    rw [← sub_eq_zero, show {A} * {B} - {B} * {A} = {comb(sol,items,'s')} by noncomm_ring, {zs}]; simp")
open('gen_dk4.lean','w').write('\n'.join(out)+'\n')
# locals of dk4 (t side) for used facts except 15
FV=[comm(x,y) for x,y in targets]
titems=[(x,y) for x,y in targets]
out=["/-- The bracketing-local commutations of a `DK4` family. -/","theorem locals_of_dk4 {t12 t13 t14 t23 t24 t34 : R} (h : DK4 t12 t13 t14 t23 t24 t34) :"]
concl=[]
for i in used[:-1]:
    a,b=items[i]; concl.append(f"Commute {lean(a,'t')} {lean(b,'t')}")
out.append("    "+" ∧\n    ".join(concl)+" := by")
for j,f in enumerate(fieldnames):
    x,y=titems[j]; A,B=lean(x,'t'),lean(y,'t')
    out.append(f"  have z{j} : {A} * {B} - {B} * {A} = 0 := sub_eq_zero.mpr h.{f}.eq")
out.append("  refine ⟨"+", ".join("?_" for _ in used[:-1])+"⟩")
for i in used[:-1]:
    a,b=items[i]; sol=solve(comm(a,b)); A,B=lean(a,'t'),lean(b,'t')
    zs=', '.join(f"z{j}" for j,c in enumerate(sol) if c)
    out.append(f"  · show {A} * {B} = {B} * {A}")
    out.append(f"    rw [← sub_eq_zero, show {A} * {B} - {B} * {A} = {comb(sol,titems,'t')} by noncomm_ring, {zs}]; simp")
# c4 central: each generator commutes with total
out2=["/-- In a `DK4` family each generator commutes with the total `c₄ = Σ tᵢⱼ`. -/","theorem commute_total {t12 t13 t14 t23 t24 t34 : R} (h : DK4 t12 t13 t14 t23 t24 t34) :"]
tot=L('12','13','14','23','24','34'); concl=[]
for n in names: concl.append(f"Commute t{n} {lean(tot,'t')}")
out2.append("    "+" ∧\n    ".join(concl)+" := by")
for j,f in enumerate(fieldnames):
    x,y=titems[j]; A,B=lean(x,'t'),lean(y,'t')
    out2.append(f"  have z{j} : {A} * {B} - {B} * {A} = 0 := sub_eq_zero.mpr h.{f}.eq")
out2.append("  refine ⟨"+", ".join("?_" for _ in names)+"⟩")
for n in names:
    a=L(n); sol=solve(comm(a,tot)); A,B=lean(a,'t'),lean(tot,'t')
    zs=', '.join(f"z{j}" for j,c in enumerate(sol) if c)
    out2.append(f"  · show {A} * {B} = {B} * {A}")
    out2.append(f"    rw [← sub_eq_zero, show {A} * {B} - {B} * {A} = {comb(sol,titems,'t')} by noncomm_ring, {zs}]; simp")
open('gen_loc.lean','w').write('\n'.join(out)+'\n\n'+'\n'.join(out2)+'\n')
