import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-!
# Distinct proton and neutron words: the crossing-local charge dressing (C2 replaced)

Beans `qou-2skq` (this item), `qou-myts` (compute-accuracy epic), item C1 route 2. Owner, 2026-11-27: *"Build different
proton and neutron elements. Use uud and udd words under the three-colour working assumption.
This changes C2"*.

## Why a new element is needed

`QOU.QBeta.NucleonSplitSingleElement` (PR #9453) proves that one braid-algebra element used for
both nucleons has equal plain traces on `W_p` (`uud, udu, duu`) and `W_n` (`udd, dud, ddu`); only
the Cartan weight `K` separates them. The three-colour working assumption (2026-11-22) does not
change this: the colour singlet `ε_q` is one-dimensional and shared by `p` and `n`, and on it the
strand braid is `−q⁻¹` times the flavour braid (`JimboGl3Singlet.singlet_unique`,
`ColourSingletDownstream.trace_word_smul`). So colour multiplies both nucleons by the same factor,
and a word-dependent split has to carry flavour inside the word.

## The construction

A strand carries a flavour, and at a crossing `σ_k` the two strands that meet are strands `k` and
`k+1`. Dress each letter with the product of their charges:

    σ_k^{±1}  ↦  σ_k^{±1} · (1 + c · Q_k Q_{k+1}),     Q = diag(a, b)  (u ↦ a, d ↦ b).

`Q_k Q_{k+1}` is diagonal in the flavour basis and symmetric in the two strands, so it commutes
with the Jimbo crossing on those strands (`chP12_comm`, …): the dressing does not depend on whether
it is put before or after the crossing. It is **not** in the image of the braid algebra, so the
single-element theorem does not apply to it. On the weight spaces it is the diagonal matrix of the
charge products of the strands at the crossing positions:

| basis | `Q₁Q₂` | `Q₂Q₃` |
|---|---|---|
| `uud, udu, duu` | `a², ab, ab` | `ab, ab, a²` |
| `udd, dud, ddu` | `ab, ab, b²` | `b², ab, ab` |

The proton and neutron elements are the dressed `V³ = (σ₁σ₂⁻¹)³` on `W_p` and on `W_n`:
`Mp = (σ₁ D₁₂ σ₂⁻¹ D₂₃)³` read with the `uud` labels, `Mn` the same word read with the `udd` labels.

## What is proved (generic field, no number enters)

* `chP12_comm`, `chP23_comm`, `chN12_comm`, `chN23_comm`: the dressing commutes with its crossing.
* `Lp_eq`, `Ln_eq`: closed forms of one period `σ₁D₁₂σ₂⁻¹D₂₃` on each weight space.
* `trace_dressed_split`: `tr Mn − tr Mp = c·(a − b)·(1 + abc)³·G(q,a,b,c)/q⁶`, with `G` explicit.
* `trace_dressed_split_zero_of_c` (undressed: back to `tr_n = tr_p`, consistent with PR #9453),
  `trace_dressed_split_zero_of_charge_eq` (equal charges: no split).
* `trace_dressed_split_ne_zero`: the split is non-zero whenever `c ≠ 0`, `a ≠ b`, `1 + abc ≠ 0`
  and `G ≠ 0`. So with distinct quark charges, the dressed `uud` and `udd` words are distinct
  elements whose traces differ, and the difference depends on the word through `G`.
* `firstOrder_eq`: the coefficient of `c` in the split is `3(a − b)·(a·G₁(q) + b·G₂(q))/q⁶`.

`NucleonElementsAreChargeDressed` states the replacement for conjecture C2 as a `Prop` class with
no instance. Nothing here assigns a value to the coupling `c`; it is the same undetermined coupling
as the two-term `c_em`, and route 1 of the nucleon split (the Gibbs map) is the thread deriving it.
The charges are left generic; the quark charges `2/3, −1/3` are one instance. No measured value
enters this file. Numbers at the proton `q₀` are in
`computations/probes/nucleon_charge_dressed_words_probe.py`.

-- Ref: [leitner2026] docs/audits/2026-11-27-nucleon-charge-dressed-words.md
-- Ref: [leitner2026] docs/audits/2026-11-27-nucleon-split-single-element-theorem.md
-- Ref: [leitner2026] docs/audits/2026-11-22-strand-colour-downstream-impact.md
-/

namespace QOU.QBeta.NucleonChargeDressedWords

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {R : Type*} [Field R]

/-! ## 1. The charge products at the two crossing positions -/

/-- `Q₁Q₂` on `W_p` (basis `uud, udu, duu`). -/
def chP12 (a b : R) : Matrix (Fin 3) (Fin 3) R := !![a * a, 0, 0; 0, a * b, 0; 0, 0, a * b]
/-- `Q₂Q₃` on `W_p`. -/
def chP23 (a b : R) : Matrix (Fin 3) (Fin 3) R := !![a * b, 0, 0; 0, a * b, 0; 0, 0, a * a]
/-- `Q₁Q₂` on `W_n` (basis `udd, dud, ddu`). -/
def chN12 (a b : R) : Matrix (Fin 3) (Fin 3) R := !![a * b, 0, 0; 0, a * b, 0; 0, 0, b * b]
/-- `Q₂Q₃` on `W_n`. -/
def chN23 (a b : R) : Matrix (Fin 3) (Fin 3) R := !![b * b, 0, 0; 0, a * b, 0; 0, 0, a * b]

theorem chP12_comm (q a b : R) : A₁ q * chP12 a b = chP12 a b * A₁ q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A₁, chP12, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem chP23_comm (q a b : R) : A₂ q * chP23 a b = chP23 a b * A₂ q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A₂, chP23, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem chN12_comm (q a b : R) : B₁ q * chN12 a b = chN12 a b * B₁ q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [B₁, chN12, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem chN23_comm (q a b : R) : B₂ q * chN23 a b = chN23 a b * B₂ q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [B₂, chN23, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

/-! ## 2. The dressed words -/

/-- The dressing `1 + c·Q₁Q₂` on `W_p`, written out. -/
def dP12 (c a b : R) : Matrix (Fin 3) (Fin 3) R :=
  !![1 + c * (a * a), 0, 0; 0, 1 + c * (a * b), 0; 0, 0, 1 + c * (a * b)]
/-- `1 + c·Q₂Q₃` on `W_p`. -/
def dP23 (c a b : R) : Matrix (Fin 3) (Fin 3) R :=
  !![1 + c * (a * b), 0, 0; 0, 1 + c * (a * b), 0; 0, 0, 1 + c * (a * a)]
/-- `1 + c·Q₁Q₂` on `W_n`. -/
def dN12 (c a b : R) : Matrix (Fin 3) (Fin 3) R :=
  !![1 + c * (a * b), 0, 0; 0, 1 + c * (a * b), 0; 0, 0, 1 + c * (b * b)]
/-- `1 + c·Q₂Q₃` on `W_n`. -/
def dN23 (c a b : R) : Matrix (Fin 3) (Fin 3) R :=
  !![1 + c * (b * b), 0, 0; 0, 1 + c * (a * b), 0; 0, 0, 1 + c * (a * b)]

theorem dP12_eq (c a b : R) : dP12 c a b = 1 + c • chP12 a b := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [dP12, chP12, Matrix.one_apply]
theorem dP23_eq (c a b : R) : dP23 c a b = 1 + c • chP23 a b := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [dP23, chP23, Matrix.one_apply]
theorem dN12_eq (c a b : R) : dN12 c a b = 1 + c • chN12 a b := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [dN12, chN12, Matrix.one_apply]
theorem dN23_eq (c a b : R) : dN23 c a b = 1 + c • chN23 a b := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [dN23, chN23, Matrix.one_apply]

/-- One period `σ₁ (1 + c Q₁Q₂) σ₂⁻¹ (1 + c Q₂Q₃)` on `W_p`. -/
def Lp (q c a b : R) : Matrix (Fin 3) (Fin 3) R :=
  A₁ q * dP12 c a b * A₂Inv q * dP23 c a b

/-- The same period on `W_n`. -/
def Ln (q c a b : R) : Matrix (Fin 3) (Fin 3) R :=
  B₁ q * dN12 c a b * B₂Inv q * dN23 c a b

/-- The dressed proton element: the `uud` reading of the dressed `V³`. -/
def Mp (q c a b : R) : Matrix (Fin 3) (Fin 3) R := Lp q c a b ^ 3

/-- The dressed neutron element: the `udd` reading of the dressed `V³`. -/
def Mn (q c a b : R) : Matrix (Fin 3) (Fin 3) R := Ln q c a b ^ 3

theorem Lp_eq (q c a b : R) (hq : q ≠ 0) :
    Lp q c a b =
      !![-(q - q⁻¹) * q * (1 + a * a * c) * (1 + a * b * c),
          q * (1 + a * a * c) * (1 + a * b * c), 0;
        0, 0, q⁻¹ * (1 + a * a * c) * (1 + a * b * c);
        (1 + a * b * c) ^ 2, 0, (q - q⁻¹) * q⁻¹ * (1 + a * a * c) * (1 + a * b * c)] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Lp, A₁, A₂Inv, dP12, dP23, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem Ln_eq (q c a b : R) (hq : q ≠ 0) :
    Ln q c a b =
      !![0, -(q - q⁻¹) * (1 + a * b * c) ^ 2, (1 + a * b * c) ^ 2;
        q⁻¹ * (1 + b * b * c) * (1 + a * b * c), -(q - q⁻¹) ^ 2 * (1 + a * b * c) ^ 2,
          (q - q⁻¹) * (1 + a * b * c) ^ 2;
        0, q * (1 + b * b * c) * (1 + a * b * c), 0] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Ln, B₁, B₂Inv, dN12, dN23, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

/-- `trace (L³) = Σ L_ij L_jk L_ki` for a `3 × 3` matrix. -/
theorem trace_pow_three (L : Matrix (Fin 3) (Fin 3) R) :
    trace (L ^ 3) = ∑ i, ∑ j, ∑ k, L i j * L j k * L k i := by
  simp only [pow_succ, pow_zero, one_mul, trace, diag, Matrix.mul_apply, Finset.sum_mul]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Finset.sum_comm]

/-- Coefficient of `c⁰` in the cofactor `G`. -/
def Gc0 (q a b : R) : R :=
  3 * (a * (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 4 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1)
    + b * (q ^ 10 - 4 * q ^ 8 + 4 * q ^ 6 - 4 * q ^ 4 + q ^ 2))
/-- Coefficient of `c¹` in `G`. -/
def Gc1 (q a b : R) : R :=
  3 * (a ^ 3 * (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 3 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1)
    + a ^ 2 * b * (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1)
    + a * b ^ 2 * (2 * q ^ 10 - 8 * q ^ 8 + 9 * q ^ 6 - 8 * q ^ 4 + 2 * q ^ 2) - b ^ 3 * q ^ 6)
/-- Coefficient of `c²` in `G`. -/
def Gc2 (q a b : R) : R :=
  a * (a ^ 4 * (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 2 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1)
    + a ^ 3 * b * (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1)
    + a ^ 2 * b ^ 2 * (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1)
    + a * b ^ 3 * (3 * q ^ 10 - 12 * q ^ 8 + 15 * q ^ 6 - 12 * q ^ 4 + 3 * q ^ 2) - 3 * b ^ 4 * q ^ 6)

/-- The cofactor `G(q,a,b,c)` of the split (times `q⁶`, a polynomial, quadratic in `c`). -/
def G (q a b c : R) : R := Gc0 q a b + c * Gc1 q a b + c ^ 2 * Gc2 q a b

/-! ## 3. The split -/

/-- **The dressed `uud` and `udd` words have different traces.**
`tr Mn − tr Mp = c·(a − b)·(1 + abc)³·G/q⁶`. -/
theorem trace_dressed_split (q c a b : R) (hq : q ≠ 0) :
    trace (Mn q c a b) - trace (Mp q c a b) =
      c * (a - b) * (1 + a * b * c) ^ 3 * G q a b c / q ^ 6 := by
  rw [Mn, Mp, trace_pow_three, trace_pow_three, Ln_eq q c a b hq, Lp_eq q c a b hq]
  simp only [Fin.sum_univ_three, G, Gc0, Gc1, Gc2]
  simp [Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one]
  field_simp
  ring

/-- Undressed (`c = 0`): the traces agree, as PR #9453 proves for every single element. -/
theorem trace_dressed_split_zero_of_c (q a b : R) (hq : q ≠ 0) :
    trace (Mn q 0 a b) = trace (Mp q 0 a b) := by
  have h := trace_dressed_split q 0 a b hq
  simp at h
  exact sub_eq_zero.mp h

/-- Equal charges: the dressing is a scalar on each weight space and the split vanishes. -/
theorem trace_dressed_split_zero_of_charge_eq (q c a : R) (hq : q ≠ 0) :
    trace (Mn q c a a) = trace (Mp q c a a) := by
  have h := trace_dressed_split q c a a hq
  simp at h
  exact sub_eq_zero.mp h

/-- With distinct charges, a non-zero coupling, `1 + abc ≠ 0` and `G ≠ 0`, the dressed proton
and neutron elements have different traces. -/
theorem trace_dressed_split_ne_zero (q c a b : R) (hq : q ≠ 0) (hc : c ≠ 0) (hab : a ≠ b)
    (habc : 1 + a * b * c ≠ 0) (hG : G q a b c ≠ 0) :
    trace (Mn q c a b) ≠ trace (Mp q c a b) := by
  intro h
  have h2 := trace_dressed_split q c a b hq
  rw [h, sub_self] at h2
  have : c * (a - b) * (1 + a * b * c) ^ 3 * G q a b c / q ^ 6 ≠ 0 := by
    apply div_ne_zero _ (pow_ne_zero _ hq)
    exact mul_ne_zero (mul_ne_zero (mul_ne_zero hc (sub_ne_zero.mpr hab)) (pow_ne_zero _ habc)) hG
  exact this h2.symm

/-- `G₁`, `G₂`: the two `q`-polynomials of the first-order coefficient. -/
def G₁ (q : R) : R := q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 4 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1
def G₂ (q : R) : R := q ^ 10 - 4 * q ^ 8 + 4 * q ^ 6 - 4 * q ^ 4 + q ^ 2

/-- **First order in the coupling.** `G` at `c = 0` is `3(a·G₁ + b·G₂)`, so the coefficient of
`c` in the split is `3(a − b)(a·G₁(q) + b·G₂(q))/q⁶`. -/
theorem firstOrder_eq (q a b : R) : G q a b 0 = 3 * (a * G₁ q + b * G₂ q) := by
  simp only [G, Gc0, G₁, G₂]; ring

/-- At `q = 1`: `G₁(1) = −2`, `G₂(1) = −2`. -/
theorem G₁_one : G₁ (1 : R) = -2 := by simp [G₁]; norm_num
theorem G₂_one : G₂ (1 : R) = -2 := by simp [G₂]; norm_num

/-! ## 4. Conjecture C2′ (replacement for C2), stated, not asserted -/

/-- **Conjecture C2′.** The proton and neutron elements are the charge-dressed `V³` read with the
`uud` and the `udd` labels, for some coupling `c` and charges `a, b`. No instance is given:
the coupling is not derived here. -/
class NucleonElementsAreChargeDressed (q : R) (Mp' Mn' : Matrix (Fin 3) (Fin 3) R) : Prop where
  exists_coupling : ∃ c a b : R, Mp' = Mp q c a b ∧ Mn' = Mn q c a b

end QOU.QBeta.NucleonChargeDressedWords
