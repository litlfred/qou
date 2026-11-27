import sympy as sp, itertools, sys
q=sp.symbols('q'); h=q-1/q
R2={ (0,0):{(0,0):q}, (0,1):{(1,0):1}, (1,0):{(0,1):1,(1,0):h}, (1,1):{(1,1):q} }  # column map: input -> {output:coef}
def states(z): return [b for b in itertools.product((0,1),repeat=4) if b.count(0)==z]
def gen(z,i,inv):
    S=states(z); idx={s:k for k,s in enumerate(S)}; M=sp.zeros(len(S))
    for s in S:
        out=R2[(s[i],s[i+1])]
        for (a,b),c in out.items():
            t=list(s); t[i]=a; t[i+1]=b; M[idx[tuple(t)],idx[s]]+=c
    if inv: M=M-h*sp.eye(len(S))
    return M
def lean(e):
    e=sp.factor(sp.simplify(e))
    n,d=sp.fraction(sp.together(e))
    def s(x): return str(sp.expand(x)).replace('**','^')
    if d==1: return '('+s(n)+')'
    return '(('+s(n)+') / ('+s(d)+'))'
blocks={1:'B1',2:'B2',3:'B3'}
def leanf(e):
    n,d=sp.fraction(sp.factor(sp.simplify(e)))
    return '(('+str(sp.expand(n)).replace('**','^')+') / ('+str(d).replace('**','^')+'))'
words={
 'wL':[(0,0),(1,1)]*3+[(2,1),(1,1),(0,1),(0,1),(1,1),(2,1)],
 'wAL':[(0,0),(1,1)]*3+[(2,1),(2,1)],
 'wR':[(2,0),(1,1)]*3+[(0,1),(1,1),(2,1),(2,1),(1,1),(0,1)],
}
def wordmat(z,w):
    X=sp.eye(len(states(z)))
    for i,e in w: X=X*gen(z,i,e)
    return X
K=lambda s: q**(2*s.count(0)-4)
def sector(W,z,strands,nz):
    S=states(z); return sum((K(s)*W[k,k] for k,s in enumerate(S) if sum(1 for t in strands if s[t]==0)==nz), sp.Integer(0))
if sys.argv[1]=='check':
  for nm,w in words.items():
    st=[0,1,2] if nm in('wL','wAL') else [1,2,3]
    Wz={z:wordmat(z,w) for z in (1,2,3)}
    tp=sum(sector(Wz[z],z,st,2) for z in (1,2,3)); tn=sum(sector(Wz[z],z,st,1) for z in (1,2,3))
    print(nm,'tp=',sp.factor(sp.simplify(tp)),' tn=',sp.factor(sp.simplify(tn)),' tn-tp/q^2=',sp.factor(sp.simplify(tn-tp/q**2)),' eps=',sp.factor(sp.simplify((tp-tn)/(q+1/q)**4)))
if sys.argv[1]=='emit':
  N={1:4,2:6,3:4}; sumn={4:'Fin.sum_univ_four',6:'Fin.sum_univ_six'}
  out=[]
  P=out.append
  P('''import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination

/-!
# Ruled flavour split on the four-strand hydrogen element: left placement keeps `q⁻²`

Level-2 Jimbo braiding `Ř` on `(C²)^{⊗4}` (`Ř e₀₀ = q e₀₀`, `Ř e₀₁ = e₁₀`,
`Ř e₁₀ = e₀₁ + h e₁₀`, `Ř e₁₁ = q e₁₁`, `h = q − q⁻¹`; bit `0` is the `K = q` vector, the
up strand). `Ř` keeps the number `z` of zeros, so a braid word is block diagonal; this file
uses the blocks `z = 1, 2, 3` (`blk z`, basis = the bit strings with `z` zeros in
lexicographic order). Inverse letters are `σ − h` (Hecke relation).

**The ruled functional** (`FlavourWeightSplit`, `NeutronHeavierSign`):
`E_c(W) = Tr(K^{⊗4} Π_c W)/[2]⁴`, `K = diag(q, q⁻¹)`. With the nucleon on strands `0–2`,
`Π_p` keeps states with two zeros there and `Π_n` states with one. `tp`, `tn` below are
`[2]⁴ · E_p`, `[2]⁴ · E_n`, written out on the blocks (weight `q^{2z−4}`); the blocks
`z = 0, 4` do not meet either sector.

**Elements** (product in list order, as in
`computations/probes/np_splitting/np_hydrogen_flavour_split_probe.py`):
* `wL = (σ₀σ₁⁻¹)³ · (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹` — the γγ core with the electron capture on strand 3;
* `wAL = (σ₀σ₁⁻¹)³ · σ₂⁻²` — the adjacent capture;
* `wR = (σ₂σ₁⁻¹)³ · (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹` — the strand reflection of `wL`, nucleon on strands `1–3`.

**Results (generic field, `q ≠ 0`, `q² + 1 ≠ 0`).**
* `left_ratio`: for **every** four-strand braid word, with the nucleon on strands `0–2`,
  `tn = q⁻² · tp`, the same ratio as on the bare core `V³` (`FlavourWeightSplit`). Proof: two
  explicit intertwiners `P32 : blk 3 → blk 2`, `P21 : blk 2 → blk 1` commute with every letter,
  and the functional `tn − q⁻²tp` is `Σ_z tr(M_z W_z)` with `M = (P21N21, P32N32 − N21P21,
  −N32P32)`, which cancels by cyclicity. So the electron strand on the right never changes the
  ratio, whatever the capture word.
* Closed forms `wL_tp`, `wAL_tp`, and `wL_eps` for the ruled split `ε = (tp − tn)/[2]⁴`.
* Right placement (nucleon on `1–3`): the ratio fails for the mirrored capture `wR`, with an
  explicit defect of order `h²` (`wR_defect`).

This is exact algebra; no numerical value enters. Which placement is the hydrogen element is
not derived here (audit `2026-11-21-neutron-heavier-sign.md` §20).
-/

namespace QOU.QBeta.HydrogenFlavourSplit

open Matrix

variable {R : Type*} [Field R]

set_option linter.unusedVariables false

/-- A letter: strand index and `true` for an inverse crossing. -/
abbrev Letter := Fin 3 × Bool
''')
  def matlean(M):
    rows=[', '.join(lean(M[r,c]) for c in range(M.shape[1])) for r in range(M.shape[0])]
    return '!![' + '; '.join(rows) + ']'
  defs=[]
  for z in (1,2,3):
    n=N[z]
    for i in range(3):
      for inv in (0,1):
        nm=f'g{z}_{i}{"i" if inv else ""}'; defs.append(nm)
        P(f'def {nm} (q : R) : Matrix (Fin {n}) (Fin {n}) R :=\n  {matlean(gen(z,i,inv))}\n')
    P(f'''def gl{z} (q : R) : Letter → Matrix (Fin {n}) (Fin {n}) R
  | (0, false) => g{z}_0 q | (1, false) => g{z}_1 q | (2, false) => g{z}_2 q
  | (0, true) => g{z}_0i q | (1, true) => g{z}_1i q | (2, true) => g{z}_2i q

/-- A braid word on block `z = {z}` (product in list order). -/
def word{z} (q : R) : List Letter → Matrix (Fin {n}) (Fin {n}) R
  | [] => 1
  | l :: w => gl{z} q l * word{z} q w

theorem word{z}_mulVec_cons (q : R) (l : Letter) (w : List Letter) (v : Fin {n} → R) :
    (word{z} q (l :: w)).mulVec v = (gl{z} q l).mulVec ((word{z} q w).mulVec v) := by
  simp [word{z}, Matrix.mulVec_mulVec]

theorem word{z}_nil (q : R) : word{z} q [] = 1 := rfl
''')
  P('''theorem entry_eq_mulVec_single {n : ℕ} (M : Matrix (Fin n) (Fin n) R) (i j : Fin n) :
    M i j = (M.mulVec (Pi.single j 1)) i := by
  simp [Matrix.mulVec, dotProduct, Pi.single_apply]
''')
  P('set_option hygiene false in\nmacro "stepTac" : tactic => `(tactic| (ext i; fin_cases i <;>\n  simp [' + ', '.join(defs) + ', Matrix.mulVec, dotProduct,\n    Fin.sum_univ_four, Fin.sum_univ_six, Pi.single_apply] <;> (try field_simp) <;> (try ring)))\n')
  def lst(w): return '['+', '.join(f'({i}, {"true" if e else "false"})' for i,e in w)+']'
  for nm,w in words.items():
    P(f'def {nm} : List Letter :=\n  {lst(w)}\n')
  # sector functionals
  for side,st in (('L',[0,1,2]),('R',[1,2,3])):
    for sec,nz in (('p',2),('n',1)):
      terms=[]
      for z in (1,2,3):
        for k,s in enumerate(states(z)):
          if sum(1 for t in st if s[t]==0)==nz:
            terms.append(f'{lean(K(s))} * W{z} {k} {k}')
      P(f'/-- `[2]⁴ · E_{sec}` with the nucleon on strands {st[0]}–{st[-1]}, on blocks `z = 1, 2, 3`. -/\ndef t{sec}{side} (q : R) (W1 W3 : Matrix (Fin 4) (Fin 4) R) (W2 : Matrix (Fin 6) (Fin 6) R) : R :=\n  ' + ' + '.join(terms) + '\n')
  exec(open('intw_emit.py').read())
  need={}
  for nm in words:
    st=[0,1,2] if nm in ('wL','wAL') else [1,2,3]
    cols=set()
    for z in (1,2,3):
      for k,s_ in enumerate(states(z)):
        nz=sum(1 for t in st if s_[t]==0)
        if nz==2 or (nm=='wR' and nz==1): cols.add((z,k))
    need[nm]=sorted(cols)
  for nm,w in words.items():
    for z in (1,2,3):
      n=N[z]
      for j in range(n):
        if (z,j) not in need[nm]: continue
        v=sp.zeros(n,1); v[j]=1
        prev=f'(Pi.single {j} 1)'; steps=[]
        for k,(i,e) in enumerate(reversed(w)):
          v=(gen(z,i,e)*v).applyfunc(lambda x: sp.factor(sp.simplify(x)))
          vn=f'{nm}_{z}_{j}_v{k}'
          P(f'@[simp] def {vn} (q : R) : Fin {n} → R := ![{", ".join(lean(x) for x in v)}]\n')
          P(f'theorem {nm}_{z}_{j}_s{k} (q : R) (hq : q ≠ 0) :\n    (g{z}_{i}{"i" if e else ""} q).mulVec {prev if k==0 else "("+f"{nm}_{z}_{j}_v{k-1}"+" q)"} = {vn} q := by\n  stepTac\n')
          steps.append(f'{nm}_{z}_{j}_s{k} q hq')
        last=f'{nm}_{z}_{j}_v{len(w)-1}'
        P(f'theorem {nm}_{z}_{j}_entry (q : R) (hq : q ≠ 0) :\n    word{z} q {nm} {j} {j} = {lean(v[j])} := by\n  rw [entry_eq_mulVec_single (word{z} q {nm}) {j} {j}]\n  simp only [{nm}, word{z}_mulVec_cons, word{z}_nil, Matrix.one_mulVec, gl{z}]\n  rw [{", ".join(steps)}]\n  simp [{last}]\n')
  for nm,w in words.items():
    side='L' if nm in ('wL','wAL') else 'R'; st=[0,1,2] if side=='L' else [1,2,3]
    Wz={z:wordmat(z,w) for z in (1,2,3)}
    tp=sp.factor(sp.simplify(sum(sector(Wz[z],z,st,2) for z in (1,2,3))))
    tn=sp.factor(sp.simplify(sum(sector(Wz[z],z,st,1) for z in (1,2,3))))
    entries=', '.join(f'{nm}_{z}_{j}_entry q hq' for (z,j) in need[nm])
    args=f'q (word1 q {nm}) (word3 q {nm}) (word2 q {nm})'
    P(f'theorem {nm}_tp (q : R) (hq : q ≠ 0) :\n    tp{side} {args} = {lean(tp)} := by\n  simp only [tp{side}, {entries}]\n  field_simp <;> ring\n')
    if side=='R': P(f'theorem {nm}_tn (q : R) (hq : q ≠ 0) :\n    tn{side} {args} = {lean(tn)} := by\n  simp only [tn{side}, {entries}]\n  field_simp <;> ring\n')
    if side=='L':
      eps=sp.factor(sp.simplify((tp-tn)/(q+1/q)**4))
      P(f'/-- The ruled split `ε = (tp − tn)/[2]⁴` on `{nm}`, using `left_ratio`. -/\ntheorem {nm}_eps (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :\n    (tp{side} {args} - tn{side} {args}) / (q + q⁻¹) ^ 4 = {leanf(eps)} := by\n  rw [left_ratio q hq h2, {nm}_tp q hq]\n  have : q + q⁻¹ ≠ 0 := by\n    intro h0\n    apply h2\n    have e : q * (q + q⁻¹) = q ^ 2 + 1 := by rw [mul_add, mul_inv_cancel₀ hq]; ring\n    rw [← e, h0, mul_zero]\n  field_simp <;> ring\n')
    else:
      d=sp.factor(sp.simplify(tn-tp/q**2))
      P(f'/-- **Right placement breaks the ratio:** the defect `E_n − q⁻²E_p`, of order `h²`. -/\ntheorem {nm}_defect (q : R) (hq : q ≠ 0) :\n    tn{side} {args} - q⁻¹ ^ 2 * tp{side} {args} = {lean(d)} := by\n  rw [{nm}_tp q hq, {nm}_tn q hq]\n  field_simp <;> ring\n')
  P('end QOU.QBeta.HydrogenFlavourSplit\n')
  for t in ('left_ratio','wL_eps','wAL_eps','wR_defect'): P(f'#print axioms QOU.QBeta.HydrogenFlavourSplit.{t}')
  open('HydrogenFlavourSplit.lean','w').write('\n'.join(out)+'\n')
