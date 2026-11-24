import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-!
# A pairwise charge energy escapes the conserved-charge no-go for `n ⊗ ν → p ⊗ e⁻`

Bean `qou-99qc`. Pre-registered in
`computations/probes/qbeta_pairwise_em_split/PREREGISTRATION.md`.

PR #8676 (`QOU.QuarkState.HyperchargeGradingNoGo`) proves that an energy depending only on the
total of a **separable** additive strand charge `α(type) + β(flavour)` gives a zero split between
`n ⊗ ν = (q u)(q d)(q d)(ℓ u)` and `p ⊗ e⁻ = (q u)(q u)(q d)(ℓ d)`, and that an additive charge `χ`
has equal totals iff `χ(q,d) + χ(ℓ,u) = χ(q,u) + χ(ℓ,d)`. Electric charge `Q = T³ + Y/2` is
separable. This file asks whether a **pairwise** charge energy escapes that no-go.

## Results (generic field `R`, §7c; an ordered field only in §B's sign lemma)

**§A — uniform pairwise energy.** Strand charges are parameters `c_u, c_d` (quark doublet) and
`c_ν, c_e` (lepton doublet).
* `two_mul_pairSum` : `2 Σ_{i<j} Q_iQ_j = (Σ Q_i)² − Σ Q_i²` for every list.
* `uniformEnergy_eq` : `w Σ_{i<j}Q_iQ_j + s ΣQ_i² = (w/2)Q_tot² + (s − w/2) ΣQ_i²`.
  The first term is a function of a conserved total (killed by #8676); the second is the total of
  the additive charge `Q²`, which is NOT separable.
* `sqSum_diff` : under charge conservation `c_d + c_ν = c_u + c_e`,
  `ΣQ²(n⊗ν) − ΣQ²(p⊗e⁻) = (c_u − c_d)·((c_ν + c_e) − (c_u + c_d))`
  — a product of the flavour gap and the type (hypercharge) gap: exactly the type × flavour
  interaction #8676's `total_eq_iff` requires, produced by the cross term of `(T³ + Y/2)²`.
* `uniform_split` : the split is `(s − w/2)(c_u − c_d)((c_ν + c_e) − (c_u + c_d))`.
* `uniform_split_SM` : at `Q = (2/3, −1/3; 0, −1)` the split is `(2w − 4s)/3`;
  `uniform_split_SM_eq_zero_iff` : zero iff `w = 2s`. `pairOnly_split_SM` : the pure pairwise
  term (`s = 0`) gives `2w/3 ≠ 0` for `w ≠ 0`. **So a pairwise charge energy escapes the no-go.**

**§B — intra-nucleon vs nucleon–lepton weights.**
* `twoWeight_split_SM` : intra-nucleon `w_N`, nucleon–lepton `w_L`, self `s_q`, `s_ℓ`:
  split `= w_L − w_N/3 − s_q/3 − s_ℓ`. Its zero locus is one linear condition on four weights,
  and nothing in the corpus imposes it.
* `nucleon_em_split_SM` : the nucleon-only part `E(udd) − E(uud) = −w_N/3 − s_q/3`;
  `nucleon_em_split_neg` : negative for `w_N > 0`, `s_q ≥ 0` (EM makes the proton heavier).

**§C — the corpus two-term QED insertion, extended by one lepton strand.** Premises (not
corpus-derived): E1 the lepton strand is a spectator the braid `V³` does not touch, so the
4-strand weight space is `W_N ⊗ ℂ_ℓ`; E2 the derived quantum-trace weighting
`Tr(K^{⊗4} X (V³ ⊗ 1))/[2]_q⁴`, i.e. `NucleonWeightSpaceQTrace`'s rule at `n = 4`. The lepton `K`
weight is `q` (ν) or `q⁻¹` (e⁻), so both final states carry `K`-weight `q⁻¹·q = q·q⁻¹ = 1`.
* `Q12p_eq_mul` … `Q23n_eq_mul` : the corpus pair matrices are products of the single-strand
  charge matrices defined here.
* `allPairs4_nNu`, `allPairs4_pE` : the covariant all-pairs insertion is the scalar `−1/3` on
  `n ⊗ ν` and `−1` on `p ⊗ e⁻`.
* `covariant_raw_split` : raw split `= −2P(q)/(3q²(q²+1)⁴)`, `P = q¹²−3q¹⁰+3q⁸−5q⁶+3q⁴−3q²+1`
  (`= 1/8` at `q = 1`).
* `connTrace_smul_one`, `covariant_connected_split` : the connected subtraction removes every
  scalar insertion, so the connected covariant split is `0`. **The pairwise term that escapes
  the no-go lives entirely in the static part that the scored "connected" convention discards.**
* `trace_Q3p_borromeanV3`, `adjacent_raw_split` : the non-covariant adjacent `Q₁₂ + Q₂₃ + Q₃₄`
  (labelled comparison, not braid-covariant, #8552) gives
  `(3q¹⁰ − 10q⁸ + 13q⁶ − 8q⁴ + 4q² − 1)/(3(q²+1)⁴)` raw.

## What is NOT claimed

* No coupling `w`, `w_N`, `w_L`, `s` is derived: `NeutronProtonEMSign` already records that the
  EM coupling is not derived. The overall sign of `m_e · t` is not fixed by the corpus
  (`two_term_qtrace_weighting.py`: pre-registered `+`, compute `−`). E1 and E2 are premises.
* Nothing here identifies any split with `Q_β` or with `m_n − m_p`.

-- Ref: [leitner2026] bean qou-99qc; PR #8676; issue #8524
-/

namespace QOU.QuarkState.PairwiseChargeEnergyBeta

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {R : Type*} [Field R]

/-! ## §A. Uniform pairwise energy on strand-charge lists -/

/-- `Σ_{i<j} Q_i Q_j` of a list of strand charges. -/
def pairSum : List R → R
  | [] => 0
  | a :: L => a * L.sum + pairSum L

/-- `Σ Q_i²`. -/
def sqSum : List R → R
  | [] => 0
  | a :: L => a ^ 2 + sqSum L

theorem two_mul_pairSum (L : List R) : 2 * pairSum L = L.sum ^ 2 - sqSum L := by
  induction L with
  | nil => simp [pairSum, sqSum]
  | cons a L ih =>
    simp only [pairSum, sqSum, List.sum_cons]
    linear_combination ih

/-- `n ⊗ ν` strand charges `(c_u, c_d, c_d, c_ν)`. -/
def nNu (cu cd cnu : R) : List R := [cu, cd, cd, cnu]

/-- `p ⊗ e⁻` strand charges `(c_u, c_u, c_d, c_e)`. -/
def pE (cu cd ce : R) : List R := [cu, cu, cd, ce]

/-- Uniform pairwise charge energy with a self term. -/
def uniformEnergy (w s : R) (L : List R) : R := w * pairSum L + s * sqSum L

theorem uniformEnergy_eq (h2 : (2 : R) ≠ 0) (w s : R) (L : List R) :
    uniformEnergy w s L = w / 2 * L.sum ^ 2 + (s - w / 2) * sqSum L := by
  have h := two_mul_pairSum L
  have hp : pairSum L = (L.sum ^ 2 - sqSum L) / 2 := by
    field_simp; linear_combination h
  unfold uniformEnergy; rw [hp]; field_simp; ring

/-- Charge conservation of the exchange is `c_d + c_ν = c_u + c_e`. -/
theorem total_eq_iff_conserved (cu cd cnu ce : R) :
    (nNu cu cd cnu).sum = (pE cu cd ce).sum ↔ cd + cnu = cu + ce := by
  simp only [nNu, pE, List.sum_cons, List.sum_nil]
  constructor <;> intro h <;> linear_combination h

/-- **The `Q²` total is not conserved**: its change is (flavour gap) × (type gap). -/
theorem sqSum_diff (cu cd cnu ce : R) (hcons : cd + cnu = cu + ce) :
    sqSum (nNu cu cd cnu) - sqSum (pE cu cd ce) = (cu - cd) * ((cnu + ce) - (cu + cd)) := by
  have hn : cnu = cu + ce - cd := by linear_combination hcons
  simp only [sqSum, nNu, pE]
  rw [hn]; ring

/-- **Uniform pairwise split**, general charges. -/
theorem uniform_split (h2 : (2 : R) ≠ 0) (cu cd cnu ce w s : R) (hcons : cd + cnu = cu + ce) :
    uniformEnergy w s (nNu cu cd cnu) - uniformEnergy w s (pE cu cd ce) =
      (s - w / 2) * ((cu - cd) * ((cnu + ce) - (cu + cd))) := by
  have ht := (total_eq_iff_conserved cu cd cnu ce).mpr hcons
  rw [uniformEnergy_eq h2, uniformEnergy_eq h2, ht, ← sqSum_diff cu cd cnu ce hcons]; ring

/-- **Uniform pairwise split at the Standard-Model charges** `(2/3, −1/3; 0, −1)`. -/
theorem uniform_split_SM (h3 : (3 : R) ≠ 0) (w s : R) :
    uniformEnergy w s (nNu (2 / 3) (-1 / 3) 0) - uniformEnergy w s (pE (2 / 3) (-1 / 3) (-1)) =
      (2 * w - 4 * s) / 3 := by
  simp only [uniformEnergy, pairSum, sqSum, nNu, pE, List.sum_cons, List.sum_nil]
  field_simp; ring

theorem uniform_split_SM_eq_zero_iff (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) (w s : R) :
    uniformEnergy w s (nNu (2 / 3) (-1 / 3) 0) - uniformEnergy w s (pE (2 / 3) (-1 / 3) (-1)) = 0 ↔
      w = 2 * s := by
  rw [uniform_split_SM h3, div_eq_zero_iff, or_iff_left h3, sub_eq_zero]
  constructor
  · intro h
    have h4 : (2 : R) * (w - 2 * s) = 0 := by linear_combination h
    rcases mul_eq_zero.mp h4 with h' | h'
    · exact absurd h' h2
    · exact sub_eq_zero.mp h'
  · intro h; rw [h]; ring

/-- **The pure pairwise term escapes**: split `2w/3`. -/
theorem pairOnly_split_SM (h3 : (3 : R) ≠ 0) (w : R) :
    uniformEnergy w 0 (nNu (2 / 3) (-1 / 3) 0) - uniformEnergy w 0 (pE (2 / 3) (-1 / 3) (-1)) =
      2 * w / 3 := by
  rw [uniform_split_SM h3]; ring

/-! ## §B. Intra-nucleon vs nucleon–lepton weights -/

/-- Nucleon (quark list `Lq`) plus one lepton of charge `cl`, four weights. -/
def twoWeightEnergy (wN wL sq sl : R) (Lq : List R) (cl : R) : R :=
  wN * pairSum Lq + wL * cl * Lq.sum + sq * sqSum Lq + sl * cl ^ 2

/-- **Two-weight split at Standard-Model charges.** -/
theorem twoWeight_split_SM (h3 : (3 : R) ≠ 0) (wN wL sq sl : R) :
    twoWeightEnergy wN wL sq sl [2 / 3, -1 / 3, -1 / 3] 0 -
        twoWeightEnergy wN wL sq sl [2 / 3, 2 / 3, -1 / 3] (-1) =
      wL - wN / 3 - sq / 3 - sl := by
  simp only [twoWeightEnergy, pairSum, sqSum, List.sum_cons, List.sum_nil]
  field_simp; ring

/-- Equal weights recover §A. -/
theorem twoWeight_uniform_SM (h3 : (3 : R) ≠ 0) (w s : R) :
    twoWeightEnergy w w s s [2 / 3, -1 / 3, -1 / 3] 0 -
        twoWeightEnergy w w s s [2 / 3, 2 / 3, -1 / 3] (-1) =
      uniformEnergy w s (nNu (2 / 3) (-1 / 3) 0) - uniformEnergy w s (pE (2 / 3) (-1 / 3) (-1)) := by
  rw [twoWeight_split_SM h3, uniform_split_SM h3]; field_simp; ring

/-- **Nucleon-only EM split** `E(udd) − E(uud) = −w_N/3 − s_q/3`. -/
theorem nucleon_em_split_SM (h3 : (3 : R) ≠ 0) (wN sq : R) :
    twoWeightEnergy wN 0 sq 0 [2 / 3, -1 / 3, -1 / 3] 0 -
        twoWeightEnergy wN 0 sq 0 [2 / 3, 2 / 3, -1 / 3] 0 = -wN / 3 - sq / 3 := by
  simp only [twoWeightEnergy, pairSum, sqSum, List.sum_cons, List.sum_nil]
  field_simp; ring

/-- For a repulsive like-charge coupling `w_N > 0` and `s_q ≥ 0`, EM makes the neutron lighter. -/
theorem nucleon_em_split_neg {S : Type*} [Field S] [LinearOrder S] [IsStrictOrderedRing S]
    (wN sq : S) (hw : 0 < wN) (hs : 0 ≤ sq) :
    twoWeightEnergy wN 0 sq 0 [2 / 3, -1 / 3, -1 / 3] 0 -
        twoWeightEnergy wN 0 sq 0 [2 / 3, 2 / 3, -1 / 3] 0 < 0 := by
  rw [nucleon_em_split_SM (by norm_num)]
  linarith

/-! ## §C. The corpus two-term insertion with one spectator lepton strand -/

/-- Single-strand quark charges on the proton `(2,1)` space, basis `uud, udu, duu`. -/
def Q1p : Matrix (Fin 3) (Fin 3) R := !![2 / 3, 0, 0; 0, 2 / 3, 0; 0, 0, -1 / 3]
def Q2p : Matrix (Fin 3) (Fin 3) R := !![2 / 3, 0, 0; 0, -1 / 3, 0; 0, 0, 2 / 3]
def Q3p : Matrix (Fin 3) (Fin 3) R := !![-1 / 3, 0, 0; 0, 2 / 3, 0; 0, 0, 2 / 3]
/-- Single-strand quark charges on the neutron `(1,2)` space, basis `udd, dud, ddu`. -/
def Q1n : Matrix (Fin 3) (Fin 3) R := !![2 / 3, 0, 0; 0, -1 / 3, 0; 0, 0, -1 / 3]
def Q2n : Matrix (Fin 3) (Fin 3) R := !![-1 / 3, 0, 0; 0, 2 / 3, 0; 0, 0, -1 / 3]
def Q3n : Matrix (Fin 3) (Fin 3) R := !![-1 / 3, 0, 0; 0, -1 / 3, 0; 0, 0, 2 / 3]

section consistency
variable (h3 : (3 : R) ≠ 0)
include h3

theorem Q12p_eq_mul : (Q12p : Matrix (Fin 3) (Fin 3) R) = Q1p * Q2p := by
  have h9 : (9 : R) = 3 * 3 := by ring
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q12p, Q1p, Q2p, Matrix.mul_apply, Fin.sum_univ_three] <;> rw [h9] <;> field_simp <;> try ring
theorem Q23p_eq_mul : (Q23p : Matrix (Fin 3) (Fin 3) R) = Q2p * Q3p := by
  have h9 : (9 : R) = 3 * 3 := by ring
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q23p, Q2p, Q3p, Matrix.mul_apply, Fin.sum_univ_three] <;> rw [h9] <;> field_simp <;> try ring
theorem Q13p_eq_mul : (Q13p : Matrix (Fin 3) (Fin 3) R) = Q1p * Q3p := by
  have h9 : (9 : R) = 3 * 3 := by ring
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q13p, Q1p, Q3p, Matrix.mul_apply, Fin.sum_univ_three] <;> rw [h9] <;> field_simp <;> try ring
theorem Q12n_eq_mul : (Q12n : Matrix (Fin 3) (Fin 3) R) = Q1n * Q2n := by
  have h9 : (9 : R) = 3 * 3 := by ring
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q12n, Q1n, Q2n, Matrix.mul_apply, Fin.sum_univ_three] <;> rw [h9] <;> field_simp <;> try ring
theorem Q23n_eq_mul : (Q23n : Matrix (Fin 3) (Fin 3) R) = Q2n * Q3n := by
  have h9 : (9 : R) = 3 * 3 := by ring
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q23n, Q2n, Q3n, Matrix.mul_apply, Fin.sum_univ_three] <;> rw [h9] <;> field_simp <;> try ring
theorem Q13n_eq_mul : (Q13n : Matrix (Fin 3) (Fin 3) R) = Q1n * Q3n := by
  have h9 : (9 : R) = 3 * 3 := by ring
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Q13n, Q1n, Q3n, Matrix.mul_apply, Fin.sum_univ_three] <;> rw [h9] <;> field_simp <;> try ring

end consistency

/-- Covariant all-pairs insertion on `W_N ⊗ ℂ_ℓ`, lepton charge `cl`. -/
def allPairs4 (Q12 Q23 Q13 Q1 Q2 Q3 : Matrix (Fin 3) (Fin 3) R) (cl : R) :
    Matrix (Fin 3) (Fin 3) R :=
  Q12 + Q23 + Q13 + cl • (Q1 + Q2 + Q3)

/-- Non-covariant adjacent insertion `Q₁₂ + Q₂₃ + Q₃₄` on `W_N ⊗ ℂ_ℓ` (comparison). -/
def adjacent4 (Q12 Q23 Q3 : Matrix (Fin 3) (Fin 3) R) (cl : R) : Matrix (Fin 3) (Fin 3) R :=
  Q12 + Q23 + cl • Q3

theorem allPairs4_nNu (h3 : (3 : R) ≠ 0) :
    allPairs4 Q12n Q23n Q13n Q1n Q2n Q3n (0 : R) = (-1 / 3 : R) • (1 : Matrix (Fin 3) (Fin 3) R) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [allPairs4, Q12n, Q23n, Q13n] <;> rw [h9] <;> field_simp <;> try ring

theorem allPairs4_pE (h3 : (3 : R) ≠ 0) :
    allPairs4 Q12p Q23p Q13p Q1p Q2p Q3p (-1 : R) = (-1 : R) • (1 : Matrix (Fin 3) (Fin 3) R) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [allPairs4, Q12p, Q23p, Q13p, Q1p, Q2p, Q3p] <;> rw [h9] <;> field_simp <;> try ring

private theorem qdim4 (q : R) (hq : q ≠ 0) : (q + q⁻¹) ^ 4 = (q ^ 2 + 1) ^ 4 / q ^ 4 := by
  field_simp
  try ring

/-- **Raw covariant split** with the spectator lepton (premises E1, E2). -/
theorem covariant_raw_split (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h3 : (3 : R) ≠ 0) :
    (q⁻¹ * q) * trace (allPairs4 Q12n Q23n Q13n Q1n Q2n Q3n (0 : R) * borromeanV3B q) /
          (q + q⁻¹) ^ 4 -
        (q * q⁻¹) * trace (allPairs4 Q12p Q23p Q13p Q1p Q2p Q3p (-1 : R) * borromeanV3A q) /
          (q + q⁻¹) ^ 4 =
      -2 * (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) /
        (3 * q ^ 2 * (q ^ 2 + 1) ^ 4) := by
  rw [allPairs4_nNu h3, allPairs4_pE h3]
  simp only [Matrix.smul_mul, Matrix.one_mul, Matrix.trace_smul, smul_eq_mul]
  rw [trace_borromeanV3B q hq, trace_borromeanV3A q hq, qdim4 q hq]
  field_simp; ring

/-- Connected trace: the scalar part `tr X / 3` of the insertion removed. -/
def connTrace (X V : Matrix (Fin 3) (Fin 3) R) : R := trace (X * V) - trace X / 3 * trace V

/-- **The connected subtraction removes every scalar insertion.** -/
theorem connTrace_smul_one (h3 : (3 : R) ≠ 0) (c : R) (V : Matrix (Fin 3) (Fin 3) R) :
    connTrace (c • (1 : Matrix (Fin 3) (Fin 3) R)) V = 0 := by
  simp only [connTrace, Matrix.smul_mul, Matrix.one_mul, Matrix.trace_smul, Matrix.trace_one,
    Fintype.card_fin, smul_eq_mul]
  push_cast
  field_simp; ring

/-- **The connected covariant split vanishes** (with the spectator lepton). -/
theorem covariant_connected_split (q : R) (h3 : (3 : R) ≠ 0) :
    (q⁻¹ * q) * connTrace (allPairs4 Q12n Q23n Q13n Q1n Q2n Q3n (0 : R)) (borromeanV3B q) -
        (q * q⁻¹) * connTrace (allPairs4 Q12p Q23p Q13p Q1p Q2p Q3p (-1 : R)) (borromeanV3A q) =
      0 := by
  rw [allPairs4_nNu h3, allPairs4_pE h3, connTrace_smul_one h3, connTrace_smul_one h3]; ring

theorem trace_Q3p_borromeanV3 (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    trace (Q3p * borromeanV3A q) =
      (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 + 4 * q ^ 6 - 6 * q ^ 4 + 6 * q ^ 2 - 2) / (3 * q ^ 6) := by
  simp [Q3p, borromeanV3A, borromeanVA, A₁, A₂Inv, Matrix.trace_fin_three]
  field_simp; ring

/-- **Raw adjacent split** `Q₁₂ + Q₂₃ + Q₃₄` (non-covariant comparison). -/
theorem adjacent_raw_split (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h3 : (3 : R) ≠ 0) :
    (q⁻¹ * q) * trace (adjacent4 Q12n Q23n Q3n (0 : R) * borromeanV3B q) / (q + q⁻¹) ^ 4 -
        (q * q⁻¹) * trace (adjacent4 Q12p Q23p Q3p (-1 : R) * borromeanV3A q) / (q + q⁻¹) ^ 4 =
      (3 * q ^ 10 - 10 * q ^ 8 + 13 * q ^ 6 - 8 * q ^ 4 + 4 * q ^ 2 - 1) /
        (3 * (q ^ 2 + 1) ^ 4) := by
  simp only [adjacent4, zero_smul, add_zero, Matrix.add_mul, Matrix.smul_mul, Matrix.trace_add,
    Matrix.trace_smul, smul_eq_mul]
  rw [← Matrix.trace_add, ← Matrix.add_mul, trace_QAdjn_borromeanV3 q hq h3,
    ← Matrix.trace_add, ← Matrix.add_mul, trace_QAdjp_borromeanV3 q hq h3,
    trace_Q3p_borromeanV3 q hq h3, qdim4 q hq]
  have h9 : (9 : R) = 3 * 3 := by ring
  rw [h9]; field_simp; ring

end QOU.QuarkState.PairwiseChargeEnergyBeta
