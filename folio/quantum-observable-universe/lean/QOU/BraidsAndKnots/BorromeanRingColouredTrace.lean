import QOU.BraidsAndKnots.NucleonWeightSpaceQTrace
import QOU.QBeta.FlavourWeightSplit

/-!
# The ring-coloured trace of the Borromean nucleon `V³`

Bean `qou-99qc`. Owner question 2026-11-21: *"Why are you not doing a trace on the Borromean
ring with the strands?"* Pre-registered in
`computations/probes/borromean_ring_coloured_trace/PREREGISTRATION.md`.

## Setting

`V = K²`, basis `u = e₁` (`K u = q u`) and `d = e₂`; level-2 Jimbo braiding (matrices of
`NucleonWeightSpaceTraces`). The nucleon element `V³ = (σ₁σ₂⁻¹)³` is a pure braid, so its closure
is the Borromean rings with one component per strand. A colouring `c : Fin 3 → {u, d}` gives the
rank-one projector `P_c = P_{c₀} ⊗ P_{c₁} ⊗ P_{c₂}`, and

  `τ_c(b) = Tr(K^{⊗3} P_c ρ(b)) / [2]_q³ = q^{2T³(c)} ⟨c|ρ(b)|c⟩ / [2]_q³`.

On the proton-type space `W_p` (basis `uud, udu, duu`) this is `tauP`, on the neutron-type space
`W_n` (basis `udd, dud, ddu`) it is `tauN` (`tauP_eq_trace_proj`). The normalisation `[2]_q³` is
the corpus's (whole-space trace = convention-D Markov trace, `qtrace_crossing_eq_zD`); it is also
the Reshetikhin–Turaev normalisation with quantum dimension `[2]_q` on each component.

## What is proved

1. **The six colourings** (`borromeanV3A_diag_*`, `borromeanV3B_diag_*`): closed forms of the
   diagonal entries. They are not constant on a class: `⟨udu|V³|udu⟩ = 1` while
   `⟨uud|V³|uud⟩ = 1 − (q−1)³(q+1)³` (`borromeanV3A_diag_zero_sub_one`).
2. **Not a link invariant** (`conj_s1sq_V3A_diag_one`, `conj_s2sq_V3B_diag_one`,
   `tauP_not_conj_invariant`): conjugating `V³` by the pure braid `σ₁²` (or `σ₂²`) does not change
   the closure but changes the `udu` (resp. `dud`) entry by `∓(q−1)³(q+1)³(q⁴+1)(q⁴−q²+1)/q⁸`.
   So "the flavour of a ring" is not a well-defined label on the closed Borromean rings: it is a
   boundary condition on the open braid. Scope (b), invariant: the strand-tracked crossing
   `P·Ř = R₀ + h·E` (`strand_crossing_pos`, `strand_crossing_neg`) has a flavour-changing part, so
   flavour is not conserved along a component. Colouring by representations (Habiro's coloured
   Jones of the Borromean rings, `library/1172-3`) is invariant; `u` and `d` are weights of the one
   representation `V`, not representations.
3. **Two invariant versions, and both give `τ_p = q² τ_n`.**
   * Class sums (`sum_tauP_eq_epsP`, `sum_tauN_eq_epsN`): the sum over one class is the
     already-scored `ε_p`, `ε_n` of `FlavourWeightSplit`; `epsP_V3_eq_qsq_mul_epsN_V3`.
   * W-free strict colouring (`strictAmp_V3`): keeping only `R₀` (each component keeps its
     flavour) the amplitude is `Π q^{±[c_a = c_b]}`, and it is `1` for every colouring because
     every pair of strands crosses once with each sign (`track_v3`, Borromean pairwise linking
     number `0`). So `τ^{strict}_c = kWeight c / [2]_q³` and the braid drops out
     (`tauStrict_V3`, `strict_class_diff`).
4. **Flip** (`flip_diag`): `⟨flip c|V³|flip c⟩(q) = ⟨c|(σ₁⁻¹σ₂)³|c⟩(q⁻¹)`, the `u ↔ d` flip is
   mirror plus bar.
5. **Two-term insertions per colouring** (`allPairsP_diag`, `allPairsN_connected_diag`,
   `adjacentP_diag`, `adjacentN_diag`): the covariant all-pairs insertion is a scalar on each
   class (`0` on `W_p`, `−1/3` on `W_n`), so its connected part vanishes colouring by colouring;
   the adjacent insertion (non-covariant, labelled comparison) weights the three colourings by
   `(2,−4,2)/9` and `(−1,−4,−1)/9`.

No numerical value enters. Generic `[Field R]`.
-/

namespace QOU.BraidsAndKnots.BorromeanRingColouredTrace

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.BraidsAndKnots.NucleonWeightSpaceQTrace
open QOU.QBeta.FlavourWeightSplit

variable {R : Type*} [Field R]

/-! ## 1. Definition -/

/-- Ring-coloured trace on the proton-type space `W_p` (colourings `uud, udu, duu`). -/
def tauP (q : R) (M : Matrix (Fin 3) (Fin 3) R) (i : Fin 3) : R := q * M i i / qd2 q ^ 3

/-- Ring-coloured trace on the neutron-type space `W_n` (colourings `udd, dud, ddu`). -/
def tauN (q : R) (M : Matrix (Fin 3) (Fin 3) R) (i : Fin 3) : R := q⁻¹ * M i i / qd2 q ^ 3

/-- `P_c` restricted to a weight space is the diagonal unit `Pi.single i 1`; the coloured trace is
the `K`-weighted trace of `P_c ρ(b)`. -/
theorem tauP_eq_trace_proj (q : R) (M : Matrix (Fin 3) (Fin 3) R) (i : Fin 3) :
    tauP q M i = trace (Kp q * (diagonal (Pi.single i 1) * M)) / qd2 q ^ 3 := by
  unfold tauP Kp
  rw [Matrix.smul_mul, Matrix.one_mul, Matrix.trace_smul, smul_eq_mul]
  congr 2
  fin_cases i <;> simp [Matrix.trace, Matrix.diagonal_mul, Pi.single_apply]

theorem tauN_eq_trace_proj (q : R) (M : Matrix (Fin 3) (Fin 3) R) (i : Fin 3) :
    tauN q M i = trace (Kn q * (diagonal (Pi.single i 1) * M)) / qd2 q ^ 3 := by
  unfold tauN Kn
  rw [Matrix.smul_mul, Matrix.one_mul, Matrix.trace_smul, smul_eq_mul]
  congr 2
  fin_cases i <;> simp [Matrix.trace, Matrix.diagonal_mul, Pi.single_apply]

/-! ## 2. The six colourings of `V³` -/

theorem borromeanV3A_diag_zero (q : R) (hq : q ≠ 0) :
    borromeanV3A q 0 0 = -(q ^ 2 - 2) * (q ^ 4 - q ^ 2 + 1) := by
  simp [borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; try ring

theorem borromeanV3A_diag_one (q : R) (hq : q ≠ 0) : borromeanV3A q 1 1 = 1 := by
  simp [borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; try ring

theorem borromeanV3A_diag_two (q : R) (hq : q ≠ 0) :
    borromeanV3A q 2 2 = (2 * q ^ 2 - 1) * (q ^ 4 - q ^ 2 + 1) / q ^ 6 := by
  simp [borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; try ring

theorem borromeanV3B_diag_zero (q : R) (hq : q ≠ 0) :
    borromeanV3B q 0 0 = (q ^ 6 - 2 * q ^ 4 + 3 * q ^ 2 - 1) / q ^ 4 := by
  simp [borromeanV3B, borromeanVB, B₁, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; try ring

theorem borromeanV3B_diag_one (q : R) (hq : q ≠ 0) :
    borromeanV3B q 1 1 =
      -(q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 3 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6 := by
  simp [borromeanV3B, borromeanVB, B₁, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; try ring

theorem borromeanV3B_diag_two (q : R) (hq : q ≠ 0) :
    borromeanV3B q 2 2 = -(q ^ 6 - 3 * q ^ 4 + 2 * q ^ 2 - 1) / q ^ 2 := by
  simp [borromeanV3B, borromeanVB, B₁, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; try ring

/-- The `uud` colouring is not the `udu` one: the W-exchange part starts at `h³`. -/
theorem borromeanV3A_diag_zero_sub_one (q : R) (hq : q ≠ 0) :
    borromeanV3A q 0 0 - 1 = -(q - 1) ^ 3 * (q + 1) ^ 3 := by
  rw [borromeanV3A_diag_zero q hq]; ring

theorem borromeanV3A_diag_two_sub_one (q : R) (hq : q ≠ 0) :
    borromeanV3A q 2 2 - 1 = (q - 1) ^ 3 * (q + 1) ^ 3 / q ^ 6 := by
  rw [borromeanV3A_diag_two q hq]; field_simp; try ring

theorem borromeanV3B_diag_one_sub_one (q : R) (hq : q ≠ 0) :
    borromeanV3B q 1 1 - 1 = -(q - 1) ^ 4 * (q + 1) ^ 4 * (q ^ 4 + 1) / q ^ 6 := by
  rw [borromeanV3B_diag_one q hq]; field_simp; try ring

/-! ## 3. Not a link invariant -/

/-- Explicit `V³` on `W_p`. -/
theorem borromeanV3A_eq (q : R) (hq : q ≠ 0) :
    borromeanV3A q = !![-(q ^ 2 - 2) * (q ^ 4 - q ^ 2 + 1), q * (q - 1) ^ 2 * (q + 1) ^ 2,
        -(q - 1) ^ 2 * (q + 1) ^ 2 / q ^ 2;
      -(q - 1) ^ 2 * (q + 1) ^ 2 / q ^ 3, 1, (q - 1) ^ 2 * (q + 1) ^ 2 / q ^ 5;
      (q - 1) ^ 2 * (q + 1) ^ 2 * (q ^ 4 - q ^ 2 + 1) / q ^ 4, -(q - 1) ^ 2 * (q + 1) ^ 2 / q,
        (2 * q ^ 2 - 1) * (q ^ 4 - q ^ 2 + 1) / q ^ 6] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three];
      field_simp; try ring)

/-- Explicit `V³` on `W_n`. -/
theorem borromeanV3B_eq (q : R) (hq : q ≠ 0) :
    borromeanV3B q = !![(q ^ 6 - 2 * q ^ 4 + 3 * q ^ 2 - 1) / q ^ 4,
        -(q - 1) ^ 2 * (q + 1) ^ 2 * (q ^ 3 - q ^ 2 + 1) * (q ^ 3 + q ^ 2 - 1) / q ^ 5,
        (q - 1) ^ 2 * (q + 1) ^ 2 * (q ^ 4 - q ^ 2 + 1) / q ^ 4;
      (q - 1) ^ 2 * (q + 1) ^ 2 * (q ^ 4 - q ^ 2 + 1) / q ^ 5,
        -(q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 3 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6,
        (q - 1) ^ 2 * (q + 1) ^ 2 * (q ^ 3 - q - 1) * (q ^ 3 - q + 1) / q ^ 5;
      -(q - 1) ^ 2 * (q + 1) ^ 2 / q ^ 2, (q - 1) ^ 2 * (q + 1) ^ 2 * (q ^ 4 - q ^ 2 + 1) / q ^ 3,
        -(q ^ 6 - 3 * q ^ 4 + 2 * q ^ 2 - 1) / q ^ 2] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [borromeanV3B, borromeanVB, B₁, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three];
      field_simp; try ring)

/-- Conjugation by the pure braid `σ₁²` changes the `udu` colouring of `V³`. -/
theorem conj_s1sq_V3A_diag_one (q : R) (hq : q ≠ 0) :
    (A₁ q * A₁ q * borromeanV3A q * (A₁Inv q * A₁Inv q)) 1 1 - borromeanV3A q 1 1 =
      -(q - 1) ^ 3 * (q + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 - q ^ 2 + 1) / q ^ 8 := by
  rw [borromeanV3A_eq q hq]
  simp [A₁, A₁Inv, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; try ring

/-- Conjugation by the pure braid `σ₂²` changes the `dud` colouring of `V³`. -/
theorem conj_s2sq_V3B_diag_one (q : R) (hq : q ≠ 0) :
    (B₂ q * B₂ q * borromeanV3B q * (B₂Inv q * B₂Inv q)) 1 1 - borromeanV3B q 1 1 =
      (q - 1) ^ 3 * (q + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 - q ^ 2 + 1) / q ^ 8 := by
  rw [borromeanV3B_eq q hq]
  simp [B₂, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; try ring

/-- `A₁Inv` is a two-sided inverse of `A₁`. -/
theorem A₁Inv_mul_A₁ (q : R) (hq : q ≠ 0) : A₁Inv q * A₁ q = 1 :=
  Matrix.mul_eq_one_comm.mp (A₁_mul_A₁Inv q hq)

/-- The class sum (the trace) IS invariant under the same conjugation. -/
theorem trace_conj_s1sq_V3A (q : R) (hq : q ≠ 0) :
    trace (A₁ q * A₁ q * borromeanV3A q * (A₁Inv q * A₁Inv q)) = trace (borromeanV3A q) := by
  have hinv : (A₁Inv q * A₁Inv q) * (A₁ q * A₁ q) = 1 := by
    rw [mul_assoc, ← mul_assoc (A₁Inv q) (A₁ q), A₁Inv_mul_A₁ q hq, one_mul,
      A₁Inv_mul_A₁ q hq]
  rw [Matrix.trace_mul_comm, ← mul_assoc, hinv, one_mul]

/-- **The single-colouring trace is not a link invariant.** For `q` with `q ≠ 0, ±1`,
`q⁴ + 1 ≠ 0`, `q⁴ − q² + 1 ≠ 0`, `q² + 1 ≠ 0`, the coloured trace `τ_{udu}` takes different values
on `V³` and on its conjugate by `σ₁²`, which have the same closure. -/
theorem tauP_not_conj_invariant (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hm : q - 1 ≠ 0) (hp : q + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) (h6 : q ^ 4 - q ^ 2 + 1 ≠ 0) :
    tauP q (A₁ q * A₁ q * borromeanV3A q * (A₁Inv q * A₁Inv q)) 1 ≠ tauP q (borromeanV3A q) 1 := by
  intro h
  have hd : qd2 q ^ 3 ≠ 0 := pow_ne_zero 3 (qd2_ne_zero q hq hq2)
  unfold tauP at h
  rw [div_left_inj' hd] at h
  have h' := mul_left_cancel₀ hq h
  have key := conj_s1sq_V3A_diag_one q hq
  rw [h', sub_self] at key
  have : -(q - 1) ^ 3 * (q + 1) ^ 3 * (q ^ 4 + 1) * (q ^ 4 - q ^ 2 + 1) / q ^ 8 ≠ 0 := by
    apply div_ne_zero _ (pow_ne_zero 8 hq)
    exact mul_ne_zero (mul_ne_zero (mul_ne_zero (neg_ne_zero.mpr (pow_ne_zero 3 hm))
      (pow_ne_zero 3 hp)) h4) h6
  exact this key.symm

/-! ## 4. Strand-tracked crossing: a flavour-preserving part and a W-exchange part -/

/-- The position swap on `C² ⊗ C²` (basis `uu, ud, du, dd`). -/
def swap4 : Matrix (Fin 4) (Fin 4) R := !![1, 0, 0, 0; 0, 0, 1, 0; 0, 1, 0, 0; 0, 0, 0, 1]

/-- Unit matrix at row `1` (`ud`), column `2` (`du`): raise the left strand `d → u`. -/
def eUD : Matrix (Fin 4) (Fin 4) R := !![0, 0, 0, 0; 0, 0, 1, 0; 0, 0, 0, 0; 0, 0, 0, 0]

/-- Unit matrix at row `2` (`du`), column `1` (`ud`): lower the left strand `u → d`. -/
def eDU : Matrix (Fin 4) (Fin 4) R := !![0, 0, 0, 0; 0, 0, 0, 0; 0, 1, 0, 0; 0, 0, 0, 0]

/-- Inverse Jimbo crossing. -/
def crossingRInv (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q⁻¹, 0, 0, 0; 0, -(q - q⁻¹), 1, 0; 0, 1, 0, 0; 0, 0, 0, q⁻¹]

theorem crossingR_mul_inv (q : R) (hq : q ≠ 0) : crossingR q * crossingRInv q = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [crossingR, crossingRInv, Matrix.mul_apply, Fin.sum_univ_four] <;> field_simp

/-- Positive crossing, labelled by strand: `R₀ = diag(q,1,1,q)` plus `h` times a W exchange. -/
theorem strand_crossing_pos (q : R) :
    swap4 * crossingR q = diagonal ![q, 1, 1, q] + (q - q⁻¹) • eUD := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [swap4, crossingR, eUD, Matrix.mul_apply, Fin.sum_univ_four, Matrix.diagonal]

/-- Negative crossing, labelled by strand: `R₀' = diag(q⁻¹,1,1,q⁻¹)` minus `h` times the opposite
exchange. -/
theorem strand_crossing_neg (q : R) :
    swap4 * crossingRInv q = diagonal ![q⁻¹, 1, 1, q⁻¹] - (q - q⁻¹) • eDU := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [swap4, crossingRInv, eDU, Matrix.mul_apply, Fin.sum_univ_four, Matrix.diagonal]

/-! ## 5. The W-free strict colouring -/

/-- The letters of `V³ = (σ₁σ₂⁻¹)³`: position of the crossing and its sign (`true` = positive). -/
def v3Letters : List (Fin 2 × Bool) :=
  [(0, true), (1, false), (0, true), (1, false), (0, true), (1, false)]

/-- Strand tracking. `pos p` is the strand at position `p`; a letter at position `i` crosses the
strands at positions `i` and `i + 1` and swaps them. Output: `(strand, strand, sign)`. -/
def track : List (Fin 2 × Bool) → (Fin 3 → Fin 3) → List (Fin 3 × Fin 3 × Bool)
  | [], _ => []
  | (i, s) :: w, pos =>
      (pos i.castSucc, pos i.succ, s) :: track w (pos ∘ Equiv.swap i.castSucc i.succ)

/-- Final position map. -/
def trackPos : List (Fin 2 × Bool) → (Fin 3 → Fin 3) → (Fin 3 → Fin 3)
  | [], pos => pos
  | (i, _) :: w, pos => trackPos w (pos ∘ Equiv.swap i.castSucc i.succ)

/-- `V³` is a pure braid. -/
theorem trackPos_v3 : trackPos v3Letters id = id := by decide

/-- The six crossings of `V³`, by strand: each pair of strands crosses once with each sign
(pairwise linking number `0`). -/
theorem track_v3 :
    track v3Letters id =
      [(0, 1, true), (0, 2, false), (1, 2, true), (1, 0, false), (2, 0, true), (2, 1, false)] := by
  decide

/-- Weight of one crossing in the flavour-preserving part `R₀`: `q^{±1}` if the two strands have
the same flavour, `1` otherwise (`strand_crossing_pos`, `strand_crossing_neg`). -/
def crossWeight (q : R) (c : Fin 3 → Bool) : Fin 3 × Fin 3 × Bool → R
  | (a, b, s) => if c a = c b then (if s then q else q⁻¹) else 1

/-- Amplitude of the W-free history: each component keeps its flavour all the way round. -/
def strictAmp (q : R) (c : Fin 3 → Bool) : R := ((track v3Letters id).map (crossWeight q c)).prod

/-- **The W-free amplitude of `V³` is `1` for every colouring.** -/
theorem strictAmp_V3 (q : R) (hq : q ≠ 0) (c : Fin 3 → Bool) : strictAmp q c = 1 := by
  unfold strictAmp
  rw [track_v3]
  cases h0 : c 0 <;> cases h1 : c 1 <;> cases h2 : c 2 <;>
    simp [crossWeight, h0, h1, h2, hq]

/-- The `K^{⊗3}` weight of a colouring (`true` = `u`). -/
def kWeight (q : R) (c : Fin 3 → Bool) : R := ∏ i, (if c i then q else q⁻¹)

/-- Strict (W-free) ring-coloured trace. -/
def tauStrict (q : R) (c : Fin 3 → Bool) : R := kWeight q c * strictAmp q c / qd2 q ^ 3

theorem tauStrict_V3 (q : R) (hq : q ≠ 0) (c : Fin 3 → Bool) :
    tauStrict q c = kWeight q c / qd2 q ^ 3 := by
  rw [tauStrict, strictAmp_V3 q hq, mul_one]

/-- Strict class difference: (one-`u` class) − (two-`u` class) `= 3(q⁻¹ − q)/[2]³`. -/
theorem strict_class_diff (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    (tauStrict q ![true, false, false] + tauStrict q ![false, true, false] +
        tauStrict q ![false, false, true]) -
      (tauStrict q ![true, true, false] + tauStrict q ![true, false, true] +
        tauStrict q ![false, true, true]) =
      -3 * q ^ 2 * (q - 1) * (q + 1) / (q ^ 2 + 1) ^ 3 := by
  simp only [tauStrict_V3 q hq, kWeight, Fin.prod_univ_three]
  simp [qd2]
  field_simp; try ring

/-! ## 6. Class sums: the already-scored components, and `ε_p = q² ε_n` -/

theorem sum_tauP_eq_epsP (q : R) (M : Matrix (Fin 3) (Fin 3) R) :
    tauP q M 0 + tauP q M 1 + tauP q M 2 = epsP q M := by
  unfold tauP epsP; rw [Matrix.trace, Fin.sum_univ_three]; simp; ring

theorem sum_tauN_eq_epsN (q : R) (M : Matrix (Fin 3) (Fin 3) R) :
    tauN q M 0 + tauN q M 1 + tauN q M 2 = epsN q M := by
  unfold tauN epsN; rw [Matrix.trace, Fin.sum_univ_three]; simp; ring

theorem epsP_V3_eq_qsq_mul_epsN_V3 (q : R) (hq : q ≠ 0) :
    epsP q (borromeanV3A q) = q ^ 2 * epsN q (borromeanV3B q) := by
  unfold epsP epsN
  rw [trace_borromeanV3A q hq, trace_borromeanV3B q hq]
  field_simp

/-! ## 7. Flip `u ↔ d` = mirror + bar -/

/-- The mirror word `(σ₁⁻¹σ₂)³` on `W_p`. -/
def mirrorV3A (q : R) : Matrix (Fin 3) (Fin 3) R :=
  (A₁Inv q * A₂ q) * (A₁Inv q * A₂ q) * (A₁Inv q * A₂ q)

/-- `⟨flip c|V³|flip c⟩(q) = ⟨c|(σ₁⁻¹σ₂)³|c⟩(q⁻¹)`; `flip` sends `udd, dud, ddu` to
`duu, udu, uud`, i.e. reverses the index. -/
theorem flip_diag (q : R) (hq : q ≠ 0) (i : Fin 3) :
    borromeanV3B q i i = mirrorV3A q⁻¹ i.rev i.rev := by
  fin_cases i <;>
    (simp [borromeanV3B, borromeanVB, B₁, B₂Inv, mirrorV3A, A₁Inv, A₂, Matrix.mul_apply,
        Fin.sum_univ_three, Fin.rev];
      try field_simp; try ring; try simp)

/-! ## 8. Two-term insertions, colouring by colouring -/

/-- Covariant all-pairs on `W_p`: zero on every colouring. -/
theorem allPairsP_diag (M : Matrix (Fin 3) (Fin 3) R) (i : Fin 3) :
    ((Q12p + Q23p + Q13p : Matrix (Fin 3) (Fin 3) R) * M) i i = 0 := by
  rw [QPairP_eq_sum, QPairP, Matrix.zero_mul]; rfl

/-- Covariant all-pairs on `W_n`, connected: zero on every colouring. -/
theorem allPairsN_connected_diag (h3 : (3 : R) ≠ 0) (M : Matrix (Fin 3) (Fin 3) R) (i : Fin 3) :
    ((Q12n + Q23n + Q13n : Matrix (Fin 3) (Fin 3) R) * M) i i + (1 / 3 : R) * M i i = 0 := by
  rw [QPairN_eq_sum h3, QPairN, Matrix.smul_mul, Matrix.one_mul, Matrix.smul_apply,
    smul_eq_mul]
  ring

/-- Adjacent insertion on `W_p` (non-covariant, labelled comparison). -/
theorem adjacentP_diag (M : Matrix (Fin 3) (Fin 3) R) (i : Fin 3) :
    ((Q12p + Q23p : Matrix (Fin 3) (Fin 3) R) * M) i i = ![2 / 9, -4 / 9, 2 / 9] i * M i i := by
  fin_cases i <;> simp [Q12p, Q23p, Matrix.mul_apply, Fin.sum_univ_three] <;> left <;> ring

/-- Adjacent insertion on `W_n` (non-covariant, labelled comparison). -/
theorem adjacentN_diag (M : Matrix (Fin 3) (Fin 3) R) (i : Fin 3) :
    ((Q12n + Q23n : Matrix (Fin 3) (Fin 3) R) * M) i i = ![-1 / 9, -4 / 9, -1 / 9] i * M i i := by
  fin_cases i <;> simp [Q12n, Q23n, Matrix.mul_apply, Fin.sum_univ_three] <;> left <;> ring

end QOU.BraidsAndKnots.BorromeanRingColouredTrace
