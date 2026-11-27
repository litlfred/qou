import Mathlib.Data.Matrix.Mul
import Mathlib.Data.Fin.VecNotation
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic
import QOU.BraidsAndKnots.StrangeStrandOctet

/-!
# Weighted Jucys–Murphy sums on three strands: Coleman–Glashow is an identity

Three-strand companion to `IsospinMurphyOctet.lean`. That file proves the two-strand lemmas;
the three-strand statements of `docs/audits/2026-11-21-isospin-murphy-octet.md` were only an
exact symbolic probe (`computations/flavour_strange_strand/murphy_octet_probe.py`). This file
proves them, and finds that the Coleman–Glashow part is a structural identity.

## Setting

Jimbo braiding on `(C³)^{⊗3}` with a flavour order: on `eₓ ⊗ e_y`,
`Ř = q` if `x = y`, `Ř (eₓ ⊗ e_y) = e_y ⊗ eₓ` if `x` comes first, and
`Ř (eₓ ⊗ e_y) = e_y ⊗ eₓ + h · eₓ ⊗ e_y` (`h = q - q⁻¹`) if `x` comes second.
Murphy elements `L₁ = 1`, `L₂ = σ₁²`, `L₃ = σ₂σ₁²σ₂`; the weighted sum is
`M_w = Σ_k w(flavour on strand k) · L_k`.

Every octet isospin member (`uud, udd, uus, dds, uss, dss`) has a weight space spanned by the
three words `aab, aba, baa` of a multiset `{a, a, b}`, and `σ₁, σ₂` preserve it. On that basis
they are the 3 × 3 blocks `blockS1`, `blockS2` below, where `ea` is the coefficient that `Ř`
picks up on the pair `(a, b)` and `eb` the one on `(b, a)`: for the Jimbo braiding one of them
is `h` and the other `0`. The section *Bridge* proves that these blocks are the restriction of the repo's
`StrangeStrandOctet.jimbo` acting on strands `(1,2)` and `(2,3)` of `(Cⁿ)^{⊗3}`
(`weightSpaceTrace_eq`), and restates Coleman–Glashow for that operator
(`coleman_glashow_weightSpace`).

## Results

1. `murphyTrace_eq`: the weighted trace on a block is the polynomial
   `A·(ea²eb² + eb²(q²+2) + 3(q²+1)) + B·(ea²(q²+2) + 3)`, over any commutative ring.
2. `coleman_glashow_of_one_sided`: the Coleman–Glashow combination `Σ − N − Ξ` of the three
   isospin splittings vanishes for **every** flavour weight, as soon as for each flavour pair
   at most one of the two coefficients is nonzero. The Jimbo braiding satisfies this for every
   flavour order (`coleman_glashow_jimbo`).
3. So exact Coleman–Glashow carries no information about the weight: hypercharge, isospin,
   charge or any other weight all give it. This is the operator-level counterpart of
   `QOU.Eightfold.ColemanGlashowIdentity.cg_cannot_discriminate`.
4. `nucleon_split_zero_of_equal_weight` and `sigma_split_eq`: with `w_u = w_d` (hypercharge),
   the nucleon splitting is always zero, but the `Σ` and `Ξ` splittings vanish only when `s`
   is on the same side of `u` and `d` in the flavour order. When `s` sits between them the
   `Σ` splitting is `h²(q² + 2)(w_s − w_u)`, which is nonzero for hypercharge. So the audit's
   "hypercharge-Murphy cannot split any isospin pair" holds for the orders `u < d < s` and
   `s < u < d` (and their reversals), not for every order.

Generic commutative ring throughout (§7c), except the three isospin values, which need a field
with `2 ≠ 0` because `I₃ = ±1/2`; no ordering, no numerical value of `q`.
-/

namespace QOU.BraidsAndKnots.IsospinMurphyOctetThreeStrand

open Matrix

variable {R : Type*} [CommRing R]

/-- `σ₁` on the weight block with basis `aab, aba, baa` (column = input word). -/
def blockS1 (q ea eb : R) : Matrix (Fin 3) (Fin 3) R :=
  !![q, 0, 0; 0, ea, 1; 0, 1, eb]

/-- `σ₂` on the weight block with basis `aab, aba, baa` (column = input word). -/
def blockS2 (q ea eb : R) : Matrix (Fin 3) (Fin 3) R :=
  !![ea, 1, 0; 1, eb, 0; 0, 0, q]

/-- The trace of `M_w = w₁ L₁ + w₂ L₂ + w₃ L₃` over the block, with weight `A` on flavour `a`
and `B` on flavour `b`. Word `aab` carries `(A, A, B)`, `aba` carries `(A, B, A)`, `baa`
carries `(B, A, A)`. -/
def murphyTrace (q ea eb A B : R) : R :=
  let L2 := blockS1 q ea eb * blockS1 q ea eb
  let L3 := blockS2 q ea eb * blockS1 q ea eb * blockS1 q ea eb * blockS2 q ea eb
  (A + A * L2 0 0 + B * L3 0 0) + (A + B * L2 1 1 + A * L3 1 1) +
    (B + A * L2 2 2 + A * L3 2 2)

/-- **Closed form of the block trace.** -/
theorem murphyTrace_eq (q ea eb A B : R) :
    murphyTrace q ea eb A B =
      A * (ea ^ 2 * eb ^ 2 + eb ^ 2 * (q ^ 2 + 2) + 3 * (q ^ 2 + 1)) +
        B * (ea ^ 2 * (q ^ 2 + 2) + 3) := by
  simp only [murphyTrace, blockS1, blockS2, Matrix.mul_apply, Fin.sum_univ_three,
    Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_cons,
    Matrix.head_fin_const, Matrix.tail_cons]
  ring

/-- The three isospin splittings `D = tr(lower member) − tr(upper member)` for flavours
`u, d, s` with weights `wu wd ws`. `e x y` is the coefficient `Ř` picks up on the pair `(x, y)`;
the six values are passed as `eud = e u d`, `edu = e d u`, and so on.

* nucleon: `udd` (block `a = d, b = u`) minus `uud` (`a = u, b = d`);
* Σ: `dds` minus `uus`;
* Ξ: `dss` (`a = s, b = d`) minus `uss` (`a = s, b = u`). -/
def splitN (q eud edu wu wd : R) : R :=
  murphyTrace q edu eud wd wu - murphyTrace q eud edu wu wd

def splitSigma (q eus esu eds esd wu wd ws : R) : R :=
  murphyTrace q eds esd wd ws - murphyTrace q eus esu wu ws

def splitXi (q eus esu eds esd wu wd ws : R) : R :=
  murphyTrace q esd eds ws wd - murphyTrace q esu eus ws wu

/-- **Coleman–Glashow for the weighted Murphy sum, for every weight.** If for each flavour
pair at most one of the two braiding coefficients is nonzero, then
`D_Σ = D_N + D_Ξ` identically in `q` and in the three weights. -/
theorem coleman_glashow_of_one_sided (q eud edu eus esu eds esd wu wd ws : R)
    (hud : eud * edu = 0) (hus : eus * esu = 0) (hds : eds * esd = 0) :
    splitSigma q eus esu eds esd wu wd ws =
      splitN q eud edu wu wd + splitXi q eus esu eds esd wu wd ws := by
  simp only [splitSigma, splitN, splitXi, murphyTrace_eq]
  linear_combination (eud * edu * (wu - wd)) * hud + (eus * esu * (ws - wu)) * hus +
    (eds * esd * (wd - ws)) * hds

/-- The Jimbo coefficient for a flavour order `pos`: `h` when `x` comes after `y`, else `0`. -/
def jimboCoeff {F : Type*} (pos : F → ℕ) (h : R) (x y : F) : R :=
  if pos y < pos x then h else 0

theorem jimboCoeff_one_sided {F : Type*} (pos : F → ℕ) (h : R) (x y : F) :
    jimboCoeff pos h x y * jimboCoeff pos h y x = 0 := by
  unfold jimboCoeff
  split_ifs with h1 h2 <;> first | simp | omega

/-- **Coleman–Glashow holds for the Jimbo braiding in every flavour order and for every
weight.** Here `u d s : F` are the three flavours and `pos` is any order on them. -/
theorem coleman_glashow_jimbo {F : Type*} (pos : F → ℕ) (q h : R) (u d s : F)
    (w : F → R) :
    splitSigma q (jimboCoeff pos h u s) (jimboCoeff pos h s u) (jimboCoeff pos h d s)
        (jimboCoeff pos h s d) (w u) (w d) (w s) =
      splitN q (jimboCoeff pos h u d) (jimboCoeff pos h d u) (w u) (w d) +
        splitXi q (jimboCoeff pos h u s) (jimboCoeff pos h s u) (jimboCoeff pos h d s)
          (jimboCoeff pos h s d) (w u) (w d) (w s) :=
  coleman_glashow_of_one_sided q _ _ _ _ _ _ _ _ _ (jimboCoeff_one_sided pos h u d)
    (jimboCoeff_one_sided pos h u s) (jimboCoeff_one_sided pos h d s)

/-- **Non-discrimination.** Two arbitrary weights give the same Coleman–Glashow defect
(namely zero). Exact Coleman–Glashow of this operator is therefore no evidence for the
weight that produced it. -/
theorem cg_defect_weight_independent {F : Type*} (pos : F → ℕ) (q h : R) (u d s : F)
    (w w' : F → R) :
    let e := jimboCoeff (R := R) pos h
    splitSigma q (e u s) (e s u) (e d s) (e s d) (w u) (w d) (w s) -
        splitN q (e u d) (e d u) (w u) (w d) -
        splitXi q (e u s) (e s u) (e d s) (e s d) (w u) (w d) (w s) =
      splitSigma q (e u s) (e s u) (e d s) (e s d) (w' u) (w' d) (w' s) -
        splitN q (e u d) (e d u) (w' u) (w' d) -
        splitXi q (e u s) (e s u) (e d s) (e s d) (w' u) (w' d) (w' s) := by
  intro e
  rw [coleman_glashow_jimbo pos q h u d s w, coleman_glashow_jimbo pos q h u d s w']
  ring

/-! ### Hypercharge blindness, and where it fails -/

/-- With equal weight on `u` and `d`, the nucleon splitting vanishes for any coefficients. -/
theorem nucleon_split_zero_of_equal_weight (q eud edu w : R) :
    splitN q eud edu w w = 0 := by
  simp only [splitN, murphyTrace_eq]
  ring

/-- The `Σ` splitting in closed form. With `u` and `d` on the same side of `s`
(`eus = eds`, `esu = esd`) and equal weights it vanishes; otherwise it need not. -/
theorem sigma_split_eq (q eus esu eds esd wu wd ws : R) :
    splitSigma q eus esu eds esd wu wd ws =
      wd * (eds ^ 2 * esd ^ 2 + esd ^ 2 * (q ^ 2 + 2) + 3 * (q ^ 2 + 1)) +
          ws * (eds ^ 2 * (q ^ 2 + 2) + 3) -
        (wu * (eus ^ 2 * esu ^ 2 + esu ^ 2 * (q ^ 2 + 2) + 3 * (q ^ 2 + 1)) +
          ws * (eus ^ 2 * (q ^ 2 + 2) + 3)) := by
  simp only [splitSigma, murphyTrace_eq]

theorem sigma_split_zero_same_side (q e e' w ws : R) :
    splitSigma q e e' e e' w w ws = 0 := by
  rw [sigma_split_eq]
  ring

/-- **`s` between `u` and `d`** (order `u < s < d`: `s` after `u`, `d` after `s`). Then the
`Σ` splitting with `w_u = w_d = w` is `h²(q² + 2)(w_s − w)`. For hypercharge
(`w = 1/3`, `w_s = −2/3`) this is `−h²(q² + 2)`, nonzero whenever `h ≠ 0` and `q² + 2 ≠ 0`. -/
theorem sigma_split_s_between (q h w ws : R) :
    splitSigma q 0 h h 0 w w ws = h ^ 2 * (q ^ 2 + 2) * (ws - w) := by
  rw [sigma_split_eq]
  ring

/-! ### The isospin values, as in the probe (order `u < d < s`) -/

/-- Isospin weight `I₃ = (1/2, −1/2, 0)`, order `u < d < s`, `h = q − q⁻¹`:
`D_N = −3q²`. Over a field with `2 ≠ 0` (the weights use `1/2`). -/
theorem isospin_nucleon_split {K : Type*} [Field K] (q : K) (h2 : (2 : K) ≠ 0) :
    splitN q 0 (q - q⁻¹) (1 / 2) (-1 / 2) = -3 * q ^ 2 := by
  simp only [splitN, murphyTrace_eq]
  field_simp
  ring

theorem isospin_xi_split {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    splitXi q 0 (q - q⁻¹) 0 (q - q⁻¹) (1 / 2) (-1 / 2) 0 = -(q ^ 6 + 2) / q ^ 2 := by
  simp only [splitXi, murphyTrace_eq]
  field_simp
  ring

theorem isospin_sigma_split {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    splitSigma q 0 (q - q⁻¹) 0 (q - q⁻¹) (1 / 2) (-1 / 2) 0 =
      -(q ^ 6 + 3 * q ^ 4 + 2) / q ^ 2 := by
  simp only [splitSigma, murphyTrace_eq]
  field_simp
  ring

/-! ### Bridge: the block is the repo's Jimbo braiding on three strands

`StrangeStrandOctet.jimbo n q` is the braiding on `Cⁿ ⊗ Cⁿ`. Below, `sigma1` and `sigma2` act
with it on strands `(1,2)` and `(2,3)` of `(Cⁿ)^{⊗3}`, the weighted Murphy trace over the weight
space of a multiset `{a, a, b}` is taken on that 27-dimensional (for `n = 3`) space, and it is
shown to equal `murphyTrace` with the Jimbo coefficients. So the block results above are
statements about the repo's braiding, not about a separately written matrix. -/

section Bridge

open StrangeStrandOctet

variable {K : Type*} [Field K] {n : ℕ}

/-- Words on three strands. -/
abbrev Word (n : ℕ) := Fin n × Fin n × Fin n

/-- `σ₁ = Ř ⊗ 1` on `(Cⁿ)^{⊗3}`. -/
def sigma1 (n : ℕ) (q : K) : Matrix (Word n) (Word n) K :=
  fun x y => jimbo n q (x.1, x.2.1) (y.1, y.2.1) * if x.2.2 = y.2.2 then 1 else 0

/-- `σ₂ = 1 ⊗ Ř` on `(Cⁿ)^{⊗3}`. -/
def sigma2 (n : ℕ) (q : K) : Matrix (Word n) (Word n) K :=
  fun x y => (if x.1 = y.1 then 1 else 0) * jimbo n q (x.2.1, x.2.2) (y.2.1, y.2.2)

/-- The Murphy elements `L₂ = σ₁²`, `L₃ = σ₂σ₁²σ₂` on three strands. -/
def murphyL2 (n : ℕ) (q : K) : Matrix (Word n) (Word n) K := sigma1 n q * sigma1 n q

def murphyL3 (n : ℕ) (q : K) : Matrix (Word n) (Word n) K :=
  sigma2 n q * sigma1 n q * sigma1 n q * sigma2 n q

/-- The weighted Murphy operator's trace over a set of words: word `x` contributes
`w(x₁) + w(x₂)·L₂(x,x) + w(x₃)·L₃(x,x)`. -/
def weightedMurphyDiag (q : K) (w : Fin n → K) (x : Word n) : K :=
  w x.1 + w x.2.1 * murphyL2 n q x x + w x.2.2 * murphyL3 n q x x

/-- The three words of the weight space of `{a, a, b}`: `aab, aba, baa`. -/
def wordEmb (a b : Fin n) : Fin 3 → Word n := ![(a, a, b), (a, b, a), (b, a, a)]

/-- Trace of the weighted Murphy operator over the weight space of `{a, a, b}`, computed on
the full space `(Cⁿ)^{⊗3}`. -/
def weightSpaceTrace (q : K) (w : Fin n → K) (a b : Fin n) : K :=
  ∑ i : Fin 3, weightedMurphyDiag q w (wordEmb a b i)

/-- The Jimbo coefficient of the pair `(x, y)` for the order on `Fin n`. -/
def jc (q : K) (x y : Fin n) : K := if y < x then q - q⁻¹ else 0

theorem jc_eq_jimboCoeff (q : K) (x y : Fin n) :
    jc q x y = jimboCoeff (fun i : Fin n => i.val) (q - q⁻¹) x y := by
  simp only [jc, jimboCoeff, Fin.lt_iff_val_lt_val]

/-- A matrix maps the span of `S` into itself. -/
def Closed (S : Set (Word n)) (A : Matrix (Word n) (Word n) K) : Prop :=
  ∀ x y, y ∈ S → A x y ≠ 0 → x ∈ S

theorem closed_mul {S : Set (Word n)} {A B : Matrix (Word n) (Word n) K}
    (hA : Closed S A) (hB : Closed S B) : Closed S (A * B) := by
  intro x y hy h
  rw [Matrix.mul_apply] at h
  obtain ⟨z, -, hz⟩ := Finset.exists_ne_zero_of_sum_ne_zero h
  exact hA x z (hB z y hy (right_ne_zero_of_mul hz)) (left_ne_zero_of_mul hz)

theorem submatrix_mul_of_closed {e : Fin 3 → Word n} (he : Function.Injective e)
    (A B : Matrix (Word n) (Word n) K) (hB : Closed (Set.range e) B) :
    (A * B).submatrix e e = A.submatrix e e * B.submatrix e e := by
  ext i j
  simp only [Matrix.submatrix_apply, Matrix.mul_apply]
  symm
  refine Fintype.sum_of_injective e he _ (fun z => A (e i) z * B z (e j)) ?_ (fun _ => rfl)
  intro z hz
  by_contra hne
  exact hz (hB z (e j) ⟨j, rfl⟩ (right_ne_zero_of_mul hne))

theorem wordEmb_injective {a b : Fin n} (hab : a ≠ b) : Function.Injective (wordEmb a b) := by
  intro i j h
  fin_cases i <;> fin_cases j <;> simp_all [wordEmb, Prod.ext_iff, eq_comm]

theorem sigma1_closed (q : K) (a b : Fin n) : Closed (Set.range (wordEmb a b)) (sigma1 n q) := by
  rintro x y ⟨j, rfl⟩ h
  unfold sigma1 at h
  have h3 : x.2.2 = (wordEmb a b j).2.2 := by
    by_contra hc; simp [hc] at h
  have hj := jimbo_entry_ne_zero q _ _ (left_ne_zero_of_mul h)
  obtain ⟨x1, x2, x3⟩ := x
  fin_cases j <;> simp only [wordEmb, Prod.mk.injEq] at hj h3 ⊢ <;>
    rcases hj with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩ <;> subst h3 <;>
    first
    | exact ⟨0, rfl⟩ | exact ⟨1, rfl⟩ | exact ⟨2, rfl⟩

theorem sigma2_closed (q : K) (a b : Fin n) : Closed (Set.range (wordEmb a b)) (sigma2 n q) := by
  rintro x y ⟨j, rfl⟩ h
  unfold sigma2 at h
  have h1 : x.1 = (wordEmb a b j).1 := by
    by_contra hc; simp [hc] at h
  have hj := jimbo_entry_ne_zero q _ _ (right_ne_zero_of_mul h)
  obtain ⟨x1, x2, x3⟩ := x
  fin_cases j <;> simp only [wordEmb, Prod.mk.injEq] at hj h1 ⊢ <;>
    rcases hj with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩ <;> subst h1 <;>
    first
    | exact ⟨0, rfl⟩ | exact ⟨1, rfl⟩ | exact ⟨2, rfl⟩

/-- **`σ₁` on the weight block is `blockS1`** with the Jimbo coefficients. -/
theorem sigma1_block (q : K) {a b : Fin n} (hab : a ≠ b) :
    (sigma1 n q).submatrix (wordEmb a b) (wordEmb a b) = blockS1 q (jc q a b) (jc q b a) := by
  have hba : b ≠ a := Ne.symm hab
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sigma1, wordEmb, jimbo, blockS1, jc, hab, hba]

/-- **`σ₂` on the weight block is `blockS2`** with the Jimbo coefficients. -/
theorem sigma2_block (q : K) {a b : Fin n} (hab : a ≠ b) :
    (sigma2 n q).submatrix (wordEmb a b) (wordEmb a b) = blockS2 q (jc q a b) (jc q b a) := by
  have hba : b ≠ a := Ne.symm hab
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sigma2, wordEmb, jimbo, blockS2, jc, hab, hba]

/-- **Bridge.** The weighted Murphy trace over the weight space of `{a, a, b}`, computed with
the repo's Jimbo braiding on the full three-strand space, is `murphyTrace` with the Jimbo
coefficients. -/
theorem weightSpaceTrace_eq (q : K) (w : Fin n → K) {a b : Fin n} (hab : a ≠ b) :
    weightSpaceTrace q w a b = murphyTrace q (jc q a b) (jc q b a) (w a) (w b) := by
  have he := wordEmb_injective hab
  have c1 := sigma1_closed q a b
  have c2 := sigma2_closed q a b
  have hL2 : (murphyL2 n q).submatrix (wordEmb a b) (wordEmb a b) =
      blockS1 q (jc q a b) (jc q b a) * blockS1 q (jc q a b) (jc q b a) := by
    rw [murphyL2, submatrix_mul_of_closed he _ _ c1, sigma1_block q hab]
  have hL3 : (murphyL3 n q).submatrix (wordEmb a b) (wordEmb a b) =
      blockS2 q (jc q a b) (jc q b a) * blockS1 q (jc q a b) (jc q b a) *
        blockS1 q (jc q a b) (jc q b a) * blockS2 q (jc q a b) (jc q b a) := by
    rw [murphyL3, submatrix_mul_of_closed he _ _ c2,
      submatrix_mul_of_closed he _ _ c1, submatrix_mul_of_closed he _ _ c1,
      sigma1_block q hab, sigma2_block q hab]
  have e2 : ∀ i, murphyL2 n q (wordEmb a b i) (wordEmb a b i) =
      (blockS1 q (jc q a b) (jc q b a) * blockS1 q (jc q a b) (jc q b a)) i i := by
    intro i; rw [← hL2]; rfl
  have e3 : ∀ i, murphyL3 n q (wordEmb a b i) (wordEmb a b i) =
      (blockS2 q (jc q a b) (jc q b a) * blockS1 q (jc q a b) (jc q b a) *
        blockS1 q (jc q a b) (jc q b a) * blockS2 q (jc q a b) (jc q b a)) i i := by
    intro i; rw [← hL3]; rfl
  simp only [weightSpaceTrace, weightedMurphyDiag, Fin.sum_univ_three, e2, e3]
  simp only [murphyTrace, wordEmb]
  simp

/-- **Coleman–Glashow for the repo's Jimbo braiding, for every weight.** For three distinct
flavours `u d s : Fin n` and any weight `w`, with `T a b` the weighted Murphy trace over the
weight space of `{a, a, b}`:
`D_Σ = T(d,s) − T(u,s)` equals `D_N + D_Ξ = (T(d,u) − T(u,d)) + (T(s,d) − T(s,u))`. -/
theorem coleman_glashow_weightSpace (q : K) (w : Fin n → K) {u d s : Fin n}
    (hud : u ≠ d) (hus : u ≠ s) (hds : d ≠ s) :
    weightSpaceTrace q w d s - weightSpaceTrace q w u s =
      (weightSpaceTrace q w d u - weightSpaceTrace q w u d) +
        (weightSpaceTrace q w s d - weightSpaceTrace q w s u) := by
  rw [weightSpaceTrace_eq q w hds, weightSpaceTrace_eq q w hus, weightSpaceTrace_eq q w hud.symm,
    weightSpaceTrace_eq q w hud, weightSpaceTrace_eq q w hds.symm,
    weightSpaceTrace_eq q w hus.symm]
  have := coleman_glashow_jimbo (fun i : Fin n => i.val) q (q - q⁻¹) u d s w
  simp only [jc_eq_jimboCoeff]
  simpa [splitSigma, splitN, splitXi] using this

end Bridge

end QOU.BraidsAndKnots.IsospinMurphyOctetThreeStrand
