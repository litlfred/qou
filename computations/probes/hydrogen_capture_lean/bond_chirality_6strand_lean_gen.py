"""Emits one Lean text for the given cases (GL,GR,GpL,GpR); split into modules by bond_chirality_6strand_lean_split.py."""
import sys
import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bond_chirality_6strand_lean_gen_common.py")).read())
which = sys.argv[1].split(',') if len(sys.argv) > 1 else list(CASES)
out = []
W = out.append
W("""import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

/-!
# Bond chirality on six strands: the weight-space reduction and the four values

Level-2 Jimbo braiding on `(C²)^{⊗6}`, `h = q - q⁻¹`:
`Ř e₀₀ = q e₀₀`, `Ř e₀₁ = e₁₀`, `Ř e₁₀ = e₀₁ + h e₁₀`, `Ř e₁₁ = q e₁₁`; `σ⁻¹ = σ − h`.
A basis state is `s : Fin 64`; bit `j` of `s` is the spin on strand `j` (`false` = zero).
`gen64 q i` is `Ř` on strands `i, i + 1`; a word is the matrix product in list order.

**The functional (B1 of the six-strand arm of `mn_hydrogen_capture_chirality_probe`, draft PR
#8804 §43).** `F(O) = Σ_s T³(s) · W s s` over the states whose three proton strands carry two
zeros (`O₊`) or one zero (`O₋`), with `T³ = (#0 − #1)/2 = #0 − 3` over all six strands.
`S = F(O₊) + F(O₋)`. These are `Fp64`, `Fm64` below, defined on the full 64-dimensional space.

**Reduction.** `Ř` preserves `#0`, and `#0 = 3` has `T³ = 0`, so only the weight spaces
`#0 ∈ {1, 2, 4, 5}` (dimensions 6, 15, 15, 6) enter. `mul_Emb_eq` proves `M · E = E · M|_W` for
any `M` that maps the weight space `W` to itself; closure under each generator and injectivity
of the inclusion are checked by `decide`. So for every word, `F(O₊)` and `F(O₋)` on the full space
equal explicit sums of 15 weight-space diagonal entries each (`Fp_L_reduction`, `Fm_L_reduction`,
and the `R` versions for the proton on strands `3–5`).

**Values (generic field, `q ≠ 0`).** The four words of §43:
* `G` proton left, `(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂σ₃⁻¹)³`: `S = −4q·h⁴`.
* `G` proton right, `σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂σ₃⁻¹)³`: `S = (3q² + 1)h⁴/q`.
* `G′` (non-ruled comparison arm) proton left, `(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂⁻¹σ₃)³`: `S = (q² + 1)(3q⁴ − 2q² + 1)h⁴/q`.
* `G′` (non-ruled comparison arm) proton right, `σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂⁻¹σ₃)³`: `S = −(3q² + 1)q³h⁴`.
At `q = 1`, all four have `F(O₊) = 6` and `F(O₋) = −6`. (The `±3` of §43 belongs to the
four-strand capture words, `HydrogenCaptureWeightSpace`, not to these.)

**Ruled form and comparison arm.** Owner ruling 2026-11-22 (reading A plus right-hand closure,
`docs/coordination/owner-rulings.md`): the photon vertex at strands `(i, i+1)` is `σ_iσ_{i+1}⁻¹`,
the larger letter inverted, so the bond `G = (σ₂σ₃⁻¹)³` is the ruled form. `G′ = (σ₂⁻¹σ₃)³` is
proved only as the non-ruled comparison arm; it is not an alternative convention.

**What the theorems assume about closure.** None. `F(O±)` is a weighted sum of diagonal entries
of the open six-strand braid matrix, so no closure (left or right) enters any statement here.
The placement of the proton (strands `0–2` or `3–5`) enters only through the projector `O±` and
the word as written; in every word the bond is the rightmost factor, i.e. it acts first. Whether
the right-hand-closure rule ("a bond enters the newer nucleon") selects one of the two placements
is not decided in this file. `(σ₀σ₁⁻¹)³` is the γγ product of the photon
`1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`. No numerical value enters.
-/

namespace QOU.BraidsAndKnots.BondChiralitySixStrand

open Matrix

variable {R : Type*} [Field R]

set_option linter.unusedVariables false
set_option maxHeartbeats 1000000

/-- A letter: generator index and `true` for an inverse crossing. -/
abbrev Letter := Fin 5 × Bool

/-- `Ř` on strands `i, i+1` of `(C²)^{⊗6}`, as a `64 × 64` matrix (column `s` is `Ř e_s`). -/
def gen64 (q : R) (i : ℕ) : Matrix (Fin 64) (Fin 64) R := fun t s =>
  if s.val.testBit i = s.val.testBit (i + 1) then (if t = s then q else 0)
  else if s.val.testBit i = false then (if t.val = s.val ^^^ (3 <<< i) then 1 else 0)
  else (if t.val = s.val ^^^ (3 <<< i) then 1 else 0) + (if t = s then q - q⁻¹ else 0)

/-- A letter on the full space; the inverse crossing is `σ_i⁻¹ = σ_i − h`. -/
def g64 (q : R) : Letter → Matrix (Fin 64) (Fin 64) R
  | (i, false) => gen64 q i.val
  | (i, true) => gen64 q i.val - (q - q⁻¹) • 1

/-- A braid word on the full space (product in list order). -/
def word64 (q : R) : List Letter → Matrix (Fin 64) (Fin 64) R
  | [] => 1
  | l :: w => g64 q l * word64 q w

/-! ### Restriction to an invariant coordinate subspace -/

section Embedding

variable {d : ℕ}

/-- Inclusion of the coordinate subspace spanned by the states `idx k`. -/
def Emb (idx : Fin d → Fin 64) : Matrix (Fin 64) (Fin d) R :=
  fun s k => if s = idx k then 1 else 0

/-- `M` maps the span of the `idx k` into itself. -/
def Closed (idx : Fin d → Fin 64) (M : Matrix (Fin 64) (Fin 64) R) : Prop :=
  ∀ s k, (∀ j, s ≠ idx j) → M s (idx k) = 0

theorem mul_Emb_eq (idx : Fin d → Fin 64) (hinj : Function.Injective idx)
    (M : Matrix (Fin 64) (Fin 64) R) (hM : Closed idx M) :
    M * Emb idx = Emb idx * M.submatrix idx idx := by
  ext s k
  simp only [Matrix.mul_apply, Emb, Matrix.submatrix_apply, mul_ite, mul_one, mul_zero,
    ite_mul, one_mul, zero_mul]
  rw [Finset.sum_ite_eq' Finset.univ (idx k), if_pos (Finset.mem_univ _)]
  by_cases h : ∃ j, s = idx j
  · obtain ⟨j, rfl⟩ := h
    rw [Finset.sum_eq_single j]
    · simp
    · intro b _ hb; rw [if_neg]; exact fun e => hb (hinj e).symm
    · simp
  · push_neg at h
    rw [hM s k h]
    symm; apply Finset.sum_eq_zero; intro j _; rw [if_neg (h j)]

/-- The coordinate set is closed under the swap of strands `i, i+1` where they differ. -/
def SwapClosed (idx : Fin d → Fin 64) (i : ℕ) : Prop :=
  ∀ k, (idx k).val.testBit i ≠ (idx k).val.testBit (i + 1) →
    ∃ j, (idx j).val = (idx k).val ^^^ (3 <<< i)

theorem closed_gen64 (idx : Fin d → Fin 64) (i : ℕ) (hc : SwapClosed idx i) (q : R) :
    Closed idx (gen64 q i) := by
  intro s k hs
  have hne : s ≠ idx k := hs k
  unfold gen64
  by_cases hb : (idx k).val.testBit i = (idx k).val.testBit (i + 1)
  · rw [if_pos hb, if_neg hne]
  · obtain ⟨j, hj⟩ := hc k hb
    have hsv : s.val ≠ (idx k).val ^^^ (3 <<< i) := by
      intro e; exact hs j (Fin.ext (e.trans hj.symm))
    rw [if_neg hb]
    split_ifs <;> simp_all

theorem closed_g64 (idx : Fin d → Fin 64) (hsc : ∀ i : Fin 5, SwapClosed idx i.val) (q : R)
    (l : Letter) : Closed idx (g64 q l) := by
  obtain ⟨i, b⟩ := l
  cases b
  · exact closed_gen64 idx i.val (hsc i) q
  · intro s k hs
    simp only [g64, Matrix.sub_apply, Matrix.smul_apply, Matrix.one_apply, if_neg (hs k),
      smul_zero, sub_zero]
    exact closed_gen64 idx i.val (hsc i) q s k hs

/-- A letter restricted to the subspace. -/
def gW (q : R) (idx : Fin d → Fin 64) (l : Letter) : Matrix (Fin d) (Fin d) R :=
  (g64 q l).submatrix idx idx

/-- A word restricted to the subspace (product in list order). -/
def wordW (q : R) (idx : Fin d → Fin 64) : List Letter → Matrix (Fin d) (Fin d) R
  | [] => 1
  | l :: w => gW q idx l * wordW q idx w

theorem emb_word (q : R) (idx : Fin d → Fin 64) (hinj : Function.Injective idx)
    (hsc : ∀ i : Fin 5, SwapClosed idx i.val) (w : List Letter) :
    word64 q w * Emb idx = Emb idx * wordW q idx w := by
  induction w with
  | nil => simp [word64, wordW]
  | cons l w ih =>
    simp only [word64, wordW]
    rw [Matrix.mul_assoc, ih, ← Matrix.mul_assoc,
      mul_Emb_eq idx hinj (g64 q l) (closed_g64 idx hsc q l), Matrix.mul_assoc]
    rfl

/-- **The reduction, entrywise.** A diagonal entry of a word on the full space, at a state of an
invariant coordinate subspace, is the diagonal entry of the restricted word. -/
theorem diag_word (q : R) (idx : Fin d → Fin 64) (hinj : Function.Injective idx)
    (hsc : ∀ i : Fin 5, SwapClosed idx i.val) (w : List Letter) (k : Fin d) :
    word64 q w (idx k) (idx k) = wordW q idx w k k := by
  have e := congrFun (congrFun (emb_word q idx hinj hsc w) (idx k)) k
  simp only [Matrix.mul_apply, Emb, mul_ite, mul_one, mul_zero, ite_mul, one_mul, zero_mul] at e
  rw [Finset.sum_ite_eq' Finset.univ (idx k), if_pos (Finset.mem_univ _)] at e
  rw [e, Finset.sum_eq_single k]
  · simp
  · intro b _ hb; rw [if_neg]; exact fun h => hb (hinj h).symm
  · simp

/-- The inverse letter on the subspace is the forward letter minus `h`. -/
theorem gW_inv_mulVec (q : R) (idx : Fin d → Fin 64) (hinj : Function.Injective idx) (i : Fin 5)
    (v : Fin d → R) :
    (gW q idx (i, true)).mulVec v = fun t => (gW q idx (i, false)).mulVec v t - (q - q⁻¹) * v t := by
  funext t
  simp only [gW, g64, Matrix.mulVec, dotProduct, Matrix.submatrix_apply, Matrix.sub_apply,
    Matrix.smul_apply, Matrix.one_apply, hinj.eq_iff, sub_mul, Finset.sum_sub_distrib, smul_eq_mul,
    mul_ite, mul_one, mul_zero, ite_mul, zero_mul]
  simp

theorem wordW_mulVec_cons (q : R) (idx : Fin d → Fin 64) (l : Letter) (w : List Letter)
    (v : Fin d → R) :
    (wordW q idx (l :: w)).mulVec v = (gW q idx l).mulVec ((wordW q idx w).mulVec v) := by
  simp [wordW, Matrix.mulVec_mulVec]

theorem wordW_nil (q : R) (idx : Fin d → Fin 64) : wordW q idx [] = 1 := rfl

theorem entry_eq_mulVec_single (M : Matrix (Fin d) (Fin d) R) (i j : Fin d) :
    M i j = (M.mulVec (Pi.single j 1)) i := by
  simp [Matrix.mulVec, dotProduct, Pi.single_apply]

end Embedding
""")
def vec(lst): return "![" + ", ".join(lst) + "]"
# spaces
for K, sts in SPACES.items():
    d = len(sts)
    W(f"/-! ### The weight space with {K} zero{'s' if K>1 else ''} (dimension {d}) -/\n")
    W(f"/-- The states with {K} zero{'s' if K>1 else ''}, in increasing order. -/")
    W(f"def idx{K} : Fin {d} → Fin 64 := {vec([str(s) for s in sts])}")
    W(f"theorem idx{K}_inj : Function.Injective idx{K} := by decide")
    W(f"theorem idx{K}_sc : ∀ i : Fin 5, SwapClosed idx{K} i.val := by unfold SwapClosed; decide +kernel\n")
    for i in range(5):
        comps = []
        for t in sts:
            b = bits(t)
            if b[i] == b[i+1]: comps.append(f"q * v {POS[K][t]}")
            elif b[i] == 0: comps.append(f"v {POS[K][flip(t,i)]}")
            else: comps.append(f"v {POS[K][flip(t,i)]} + (q - q⁻¹) * v {POS[K][t]}")
        W(f"/-- `σ_{i}` on the {K}-zero weight space, row by row. -/")
        W(f"def act{K}_{i} (q : R) (v : Fin {d} → R) : Fin {d} → R :=\n  {vec(comps)}")
        W(f"theorem bridge{K}_{i} (q : R) (v : Fin {d} → R) :\n    (gW q idx{K} ({i}, false)).mulVec v = act{K}_{i} q v := by")
        W(f"  funext t; fin_cases t <;>\n    simp +decide [gW, g64, gen64, Matrix.mulVec, dotProduct, Fin.sum_univ_succ, idx{K}, act{K}_{i}] <;> (try ring)\n")

# ---- functional and reduction ----
def tab(f): return vec([str(f(s)) for s in range(64)])
W("""/-! ### The functional on the full space -/

/-- Number of zeros (`false` bits) of `s` on the strands in `js`. -/
def zerosIn (js : List ℕ) (s : Fin 64) : ℕ := (js.filter (fun j => !s.val.testBit j)).length
""")
W(f"/-- Table of `zerosIn [0, 1, 2, 3, 4, 5]`. -/\ndef zTab : Fin 64 → ℕ := {tab(zc)}")
W(f"/-- Table of `zerosIn [0, 1, 2]`. -/\ndef pLTab : Fin 64 → ℕ := {tab(lambda s: pz(s,[0,1,2]))}")
W(f"/-- Table of `zerosIn [3, 4, 5]`. -/\ndef pRTab : Fin 64 → ℕ := {tab(lambda s: pz(s,[3,4,5]))}")
W("""theorem zeros6_eq : ∀ s, zerosIn [0, 1, 2, 3, 4, 5] s = zTab s := by decide +kernel
theorem zerosL_eq : ∀ s, zerosIn [0, 1, 2] s = pLTab s := by decide +kernel
theorem zerosR_eq : ∀ s, zerosIn [3, 4, 5] s = pRTab s := by decide +kernel

/-- `F(O₊) = Σ_s T³(s)·W s s` over the states whose proton strands `js` carry two zeros;
`T³ = (#0 − #1)/2 = #0 − 3`. -/
def Fp64 (js : List ℕ) (W : Matrix (Fin 64) (Fin 64) R) : R :=
  ∑ s, if zerosIn js s = 2 then (((zerosIn [0, 1, 2, 3, 4, 5] s : ℕ) : R) - 3) * W s s else 0
/-- `F(O₋)`: the proton strands carry one zero. -/
def Fm64 (js : List ℕ) (W : Matrix (Fin 64) (Fin 64) R) : R :=
  ∑ s, if zerosIn js s = 1 then (((zerosIn [0, 1, 2, 3, 4, 5] s : ℕ) : R) - 3) * W s s else 0
""")
def coefstr(c, term):
    if c == 1: return f"+ {term}"
    if c == -1: return f"- {term}"
    return (f"+ {c} * {term}" if c > 0 else f"- {-c} * {term}")
def sumstr(lst):
    s = " ".join(coefstr(c, t) for c, t in lst)
    return s[2:] if s.startswith("+ ") else s
PL = {"L": ([0,1,2], "pLTab", "zerosL_eq", "`0–2`"), "R": ([3,4,5], "pRTab", "zerosR_eq", "`3–5`")}
for side, (prot, ptab, peq, sdesc) in PL.items():
    plus, minus = needed(prot)
    js = "[" + ", ".join(map(str, prot)) + "]"
    for nm, lst, val in (("Fp", plus, 2), ("Fm", minus, 1)):
        W("set_option maxRecDepth 20000 in")
        W(f"theorem {nm}64_{side}_eq (W : Matrix (Fin 64) (Fin 64) R) :\n    {nm}64 {js} W = {sumstr([(c, f'W {s} {s}') for s, c in lst])} := by")
        W(f"  simp only [{nm}64, zeros6_eq, {peq}, Fin.sum_univ_succ, Fin.sum_univ_zero]")
        W(f"  simp [zTab, {ptab}, Fin.succ]")
        W(f"  norm_num; ring\n")
        body = sumstr([(c, f"wordW q idx{zc(s)} w {POS[zc(s)][s]} {POS[zc(s)][s]}") for s, c in lst])
        W(f"/-- **Reduction, proton on strands {sdesc}.** For every word, `{'F(O₊)' if val==2 else 'F(O₋)'}` on the full space is a sum of\nweight-space diagonal entries. -/")
        W(f"theorem {nm}_{side}_reduction (q : R) (w : List Letter) :\n    {nm}64 {js} (word64 q w) = {body} := by")
        W(f"  rw [{nm}64_{side}_eq]")
        hs = []
        for k, (s, c) in enumerate(lst):
            K = zc(s); p = POS[K][s]
            W(f"  have e{k} : word64 q w {s} {s} = wordW q idx{K} w {p} {p} := diag_word q idx{K} idx{K}_inj idx{K}_sc w {p}")
            hs.append(f"e{k}")
        W("  rw [" + ", ".join(hs) + "]\n")
W("""set_option hygiene false in
macro "stepTac" : tactic => `(tactic| (funext t; fin_cases t <;>
  simp [act1_0, act1_1, act1_2, act1_3, act1_4, act2_0, act2_1, act2_2, act2_3, act2_4,
    act4_0, act4_1, act4_2, act4_3, act4_4, act5_0, act5_1, act5_2, act5_3, act5_4,
    Pi.single_apply] <;> (try field_simp) <;> (try ring)))
""")
W("-- @@SPLIT_WORDS")
# words
def lean_word(w): return "[" + ", ".join(f"({i}, {'true' if b else 'false'})" for i, b in w) + "]"
for c in which:
    w, prot, desc = CASES[c]
    W(f"/-- {desc}. -/\ndef w{c} : List Letter := {lean_word(w)}\n")
entries = {}
for c in which:
    w, prot, desc = CASES[c]
    plus, minus = needed(prot)
    for s, _ in plus + minus:
        K = zc(s); p = POS[K][s]; d = len(SPACES[K])
        vecd = {s: sp.Integer(1)}
        prev = f"(Pi.single {p} 1)"
        names = []
        for j, (i, inv) in enumerate(reversed(w)):
            vecd = act_full(i, inv, vecd)
            comps = [lean_expr(vecd.get(t, 0)) for t in SPACES[K]]
            nm = f"c{c}_{K}_{p}_v{j}"
            W(f"def {nm} (q : R) : Fin {d} → R := {vec(comps)}")
            br = f"bridge{K}_{i}"
            rws = f"rw [gW_inv_mulVec q idx{K} idx{K}_inj, {br}]" if inv else f"rw [{br}]"
            unf = f"{names[-1]} {nm}" if names else nm
            W(f"theorem {nm}_step (q : R) (hq : q ≠ 0) :\n    (gW q idx{K} ({i}, {'true' if inv else 'false'})).mulVec {prev} = {nm} q := by\n  {rws}; unfold {unf}; stepTac")
            prev = f"({nm} q)"; names.append(nm)
        final = vecd.get(s, 0)
        entries[(c, s)] = (K, p, final)
        W(f"theorem c{c}_{K}_{p}_col (q : R) (hq : q ≠ 0) :\n    (wordW q idx{K} w{c}).mulVec (Pi.single {p} 1) = {names[-1]} q := by")
        W(f"  simp only [w{c}, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]")
        W("  rw [" + ", ".join(f"{n}_step q hq" for n in names) + "]")
        W(f"theorem c{c}_{K}_{p}_entry (q : R) (hq : q ≠ 0) :\n    wordW q idx{K} w{c} {p} {p} = {lean_expr(final)} := by")
        W(f"  rw [entry_eq_mulVec_single (wordW q idx{K} w{c}) {p} {p}, c{c}_{K}_{p}_col q hq]; simp [{names[-1]}]\n")

for c in which:
    w, prot, desc = CASES[c]
    side = "L" if prot[0] == 0 else "R"
    js = "[" + ", ".join(map(str, prot)) + "]"
    plus, minus = needed(prot)
    ents = []
    for s, _ in plus + minus:
        K = zc(s); p = POS[K][s]
        ents.append(f"c{c}_{K}_{p}_entry q hq")
    W(f"/-- **`S` for {desc}.** -/")
    W(f"theorem S_{c} (q : R) (hq : q ≠ 0) :\n    Fp64 {js} (word64 q w{c}) + Fm64 {js} (word64 q w{c}) = {TARGET_LEAN[c]} := by")
    W(f"  rw [Fp_{side}_reduction, Fm_{side}_reduction, " + ", ".join(ents) + "]")
    W("  field_simp; ring\n")
    ents1 = lambda lst: ", ".join(f"c{c}_{zc(s)}_{POS[zc(s)][s]}_entry 1 one_ne_zero" for s, _ in lst)
    W(f"theorem Fp_{c}_at_one : Fp64 {js} (word64 (1 : R) w{c}) = 6 := by")
    W(f"  rw [Fp_{side}_reduction, {ents1(plus)}]; norm_num\n")
    W(f"theorem Fm_{c}_at_one : Fm64 {js} (word64 (1 : R) w{c}) = -6 := by")
    W(f"  rw [Fm_{side}_reduction, {ents1(minus)}]; norm_num\n")
W("-- @@SPLIT_END")
W("end QOU.BraidsAndKnots.BondChiralitySixStrand")

open(sys.argv[2] if len(sys.argv) > 2 else 'Out.lean', 'w').write("\n".join(out) + "\n")
print(len(out))
