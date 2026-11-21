import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic
import QOU.Braiding.WeakVertexT35TraceClosedForm

/-!
# The weak-vertex form factor under the two-term Lagrangian trace (bean `qou-99qc`)

Owner ruling 2026-11-21: the two-term Lagrangian trace covers the β-decay half-life rate. The rate
`Γ_β` of `prf:hadron-half-life` carries the weak-vertex form factor `𝒲(q)`, which was the
one-term (convention-D Markov) trace of the `T(3,5)` braid `(σ₀σ₁)⁵ ∈ H₃(q)`. This file states
the two-term version and derives it.

**The two-term trace** (`QOU.QBeta.BetaRoutesTwoTerm`, audit
`docs/audits/2026-11-21-beta-routes-two-term-rerun.md`) of an element `X` on `N` strands is
`t₁(X) + c_em · t₂(X)`, with

    t₁(X) = Σ_m q^m Tr_{W_m}(ρ(X)) / [2]_q^N,
    t₂(X) = Σ_m q^m Tr_{W_m}(E(Q)^conn ρ(X)) / [2]_q^N,

`W_m` the weight spaces of `V^{⊗N}` (`m = #u − #d`, `V = span(u, d)`), `ρ` the Jimbo
representation, `Q = Σ_{i<j} Q_i Q_j` the all-pairs charge insertion (diagonal), `E` its
expectation onto the commutant of `H_N(q)` on `W_m`, and `E(Q)^conn = E(Q) − (Tr Q / dim W_m)·1`.

**What is derived here, for `N = 3`.**
* `W_{±3}` are one-dimensional, so the connected part vanishes there.
* `W_{±1}` are three-dimensional. `ρ(σ₀)`, `ρ(σ₁)` are the matrices `A`, `B` below (on `W_{−1}`
  their roles swap). The trivial isotypic idempotent is the rank-one `P₃ = v vᵀ / (q⁴ + q² + 1)`,
  `v = (1, q, q²)`, the common `q`-eigenvector of both generators (`A_mul_P3`, `P3_mul_A`, …,
  `P3_idem`); its complement `1 − P₃` is the `(2,1)` idempotent.
* For **any** diagonal charge insertion `Q` on such a block, the connected expectation is
  `E(Q)^conn = κ(Q)·((3/2)P₃ − (1/2)·1)` with `κ(Q) = Σ_b Q_b (d_b − 1/3)`,
  `d = (1, q², q⁴)/(q⁴ + q² + 1)` (`Econn_eq`, `kappa_eq`).
* Against the vertex, `Tr(E(Q)^conn (σ₀σ₁)⁵) = κ(Q)·(2q¹⁰ + 1)/2` on both blocks
  (`trace_Econn_AB_pow_five`, `trace_Econn_BA_pow_five`), because `Tr(P₃ (σ₀σ₁)⁵) = q¹⁰` and
  `Tr((σ₀σ₁)⁵) = q¹⁰ − 1` on `W_{±1}`.
* So `t₂ = (q κ₊ + q⁻¹ κ₋)(2q¹⁰ + 1) / (2 [2]_q³)` (`tTwo_eq`), and the one-term part is the
  closed form already proved, `t₁ = 𝒲(q) = q²(q¹² + q⁸ − 1)/(q² + 1)²` (`tOne_eq_weakVertexTrace`).

**Consequences.**
* **One charge type on the three vertex strands ⇒ two-term = one-term** for every `c_em`
  (`twoTerm_eq_of_uniform`), because `κ` vanishes on a constant insertion (`kappa_const`). This
  is the `N = 3`, `T(3,5)` instance of `BetaRoutesTwoTerm.pairSum_eq_of_total_eq`.
* **Mixed charges ⇒ a non-zero correction, and it depends on which strand carries which charge.**
  `tTwo_lepton_first` gives the lepton-on-strand-0 colouring:
  `t₂ = −2q²(q² − 1)(2q¹⁰ + 1) / (9(q² + 1)³)`, which vanishes at `q = 1`.

**What is NOT derived and enters only as hypotheses or a labelled example.**
* The charges on the three vertex strands. No ruling assigns quark or lepton colour to the
  strands of `(σ₀σ₁)⁵`; the lepton charges `(ν, e⁻) = (0, −1)` are the "C-lep" convention of the
  audit. So `κ₊`, `κ₋` are arguments, and the lepton-first colouring is an example, not a choice.
* The coefficient `c_em`. It is an argument; no value is selected.
* The covariance group. This file uses the `H_N`-covariant projection. Under the colour-block
  projection the connected part is `0` for every word (`BetaRoutesTwoTerm.pairSum_union`), so
  `𝒲` is unchanged there. Which projection defines "two-term" with lepton strands is an open owner
  decision (audit §4).

No numerical value enters.
-/

namespace QOU.QBeta.WeakVertexTwoTerm

open Matrix

variable {K : Type*} [Field K] [CharZero K]

/-! ## 1. The three-dimensional weight space -/

/-- `ρ(σ₀)` on `W_{+1} = span(uud, udu, duu)` (and `ρ(σ₁)` on `W_{−1}`), Jimbo `Ř`. -/
noncomputable def A (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![q, 0, 0; 0, 0, 1; 0, 1, q - q⁻¹]

/-- `ρ(σ₁)` on `W_{+1}` (and `ρ(σ₀)` on `W_{−1}`). -/
noncomputable def B (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![0, 1, 0; 1, q - q⁻¹, 0; 0, 0, q]

/-- `1 + q² + q⁴ = vᵀv` for `v = (1, q, q²)`. -/
def nrm (q : K) : K := 1 + q ^ 2 + q ^ 4

/-- `v vᵀ` for `v = (1, q, q²)`. -/
def vvT (q : K) : Matrix (Fin 3) (Fin 3) K :=
  !![1, q, q ^ 2; q, q ^ 2, q ^ 3; q ^ 2, q ^ 3, q ^ 4]

/-- The trivial-isotypic idempotent `P₃ = v vᵀ / (q⁴ + q² + 1)`, `v = (1, q, q²)`. -/
noncomputable def P3 (q : K) : Matrix (Fin 3) (Fin 3) K :=
  (nrm q)⁻¹ • vvT q

theorem vvT_mul_vvT (q : K) : vvT q * vvT q = nrm q • vvT q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [vvT, nrm, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

theorem A_mul_vvT (q : K) (hq : q ≠ 0) : A q * vvT q = q • vvT q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A, vvT, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem vvT_mul_A (q : K) (hq : q ≠ 0) : vvT q * A q = q • vvT q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A, vvT, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem B_mul_vvT (q : K) (hq : q ≠ 0) : B q * vvT q = q • vvT q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [B, vvT, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem vvT_mul_B (q : K) (hq : q ≠ 0) : vvT q * B q = q • vvT q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [B, vvT, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem A_mul_P3 (q : K) (hq : q ≠ 0) : A q * P3 q = q • P3 q := by
  rw [P3, Matrix.mul_smul, A_mul_vvT q hq, smul_comm]

theorem P3_mul_A (q : K) (hq : q ≠ 0) : P3 q * A q = q • P3 q := by
  rw [P3, Matrix.smul_mul, vvT_mul_A q hq, smul_comm]

theorem B_mul_P3 (q : K) (hq : q ≠ 0) : B q * P3 q = q • P3 q := by
  rw [P3, Matrix.mul_smul, B_mul_vvT q hq, smul_comm]

theorem P3_mul_B (q : K) (hq : q ≠ 0) : P3 q * B q = q • P3 q := by
  rw [P3, Matrix.smul_mul, vvT_mul_B q hq, smul_comm]

/-- `P₃` is an idempotent. -/
theorem P3_idem (q : K) (hn : nrm q ≠ 0) : P3 q * P3 q = P3 q := by
  rw [P3, Matrix.smul_mul, Matrix.mul_smul, vvT_mul_vvT, smul_smul, smul_smul]
  congr 1
  field_simp

theorem trace_P3 (q : K) (hn : nrm q ≠ 0) : (P3 q).trace = 1 := by
  rw [P3, Matrix.trace_smul, smul_eq_mul]
  have : (vvT q).trace = nrm q := by
    simp [vvT, nrm, Matrix.trace_fin_three]
  rw [this, inv_mul_cancel₀ hn]

/-! ## 2. Traces of the vertex on `W_{±1}` -/

/-- `P₃ (σ₀σ₁)ⁿ = q²ⁿ P₃`. -/
theorem P3_mul_AB_pow (q : K) (hq : q ≠ 0) (hn : nrm q ≠ 0) (n : ℕ) :
    P3 q * (A q * B q) ^ n = (q ^ (2 * n)) • P3 q := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, ← mul_assoc, P3_mul_A q hq,
      smul_mul_assoc, P3_mul_B q hq, smul_smul, smul_smul]
    congr 1; ring

theorem P3_mul_BA_pow (q : K) (hq : q ≠ 0) (hn : nrm q ≠ 0) (n : ℕ) :
    P3 q * (B q * A q) ^ n = (q ^ (2 * n)) • P3 q := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, ← mul_assoc, P3_mul_B q hq,
      smul_mul_assoc, P3_mul_A q hq, smul_smul, smul_smul]
    congr 1; ring

theorem trace_P3_AB_pow_five (q : K) (hq : q ≠ 0) (hn : nrm q ≠ 0) :
    (P3 q * (A q * B q) ^ 5).trace = q ^ 10 := by
  rw [P3_mul_AB_pow q hq hn, Matrix.trace_smul, trace_P3 q hn]; simp

theorem trace_P3_BA_pow_five (q : K) (hq : q ≠ 0) (hn : nrm q ≠ 0) :
    (P3 q * (B q * A q) ^ 5).trace = q ^ 10 := by
  rw [P3_mul_BA_pow q hq hn, Matrix.trace_smul, trace_P3 q hn]; simp

/-- `Tr_{W_{+1}} ρ((σ₀σ₁)⁵) = q¹⁰ − 1` (the trivial block `q¹⁰` plus `χ₍₂₁₎ = −1`). -/
theorem trace_AB_pow_five (q : K) (hq : q ≠ 0) : ((A q * B q) ^ 5).trace = q ^ 10 - 1 := by
  simp only [pow_succ, pow_zero, one_mul]
  simp [A, B, Matrix.mul_apply, Fin.sum_univ_three, Matrix.trace_fin_three]
  field_simp
  ring

/-- On `W_{−1}` the generators swap; the trace is the same by cyclicity. -/
theorem trace_BA_pow_five (q : K) (hq : q ≠ 0) : ((B q * A q) ^ 5).trace = q ^ 10 - 1 := by
  have h : (B q * A q) ^ 5 = B q * ((A q * B q) ^ 4 * A q) := by
    simp only [pow_succ, pow_zero, one_mul, mul_assoc]
  rw [h, Matrix.trace_mul_comm, mul_assoc, ← pow_succ, trace_AB_pow_five q hq]

/-! ## 3. The connected expectation of a diagonal charge insertion -/

/-- The expectation onto the commutant: `E(Q) = Σ_λ (Tr(Q P_λ)/Tr P_λ) P_λ`,
with `P₍₃₎ = P₃` (trace 1) and `P₍₂₁₎ = 1 − P₃` (trace 2). -/
noncomputable def Eproj (q : K) (Q : Fin 3 → K) : Matrix (Fin 3) (Fin 3) K :=
  (diagonal Q * P3 q).trace • P3 q +
    ((diagonal Q * (1 - P3 q)).trace / 2) • (1 - P3 q)

/-- The connected part: `E(Q) − (Tr Q / 3)·1`. -/
noncomputable def Econn (q : K) (Q : Fin 3 → K) : Matrix (Fin 3) (Fin 3) K :=
  Eproj q Q - ((diagonal Q).trace / 3) • (1 : Matrix (Fin 3) (Fin 3) K)

/-- `κ(Q) = Tr(Q P₃) − Tr Q / 3`, the connected coefficient on the trivial block. -/
noncomputable def kappa (q : K) (Q : Fin 3 → K) : K :=
  (diagonal Q * P3 q).trace - (diagonal Q).trace / 3

theorem kappa_eq (q : K) (Q : Fin 3 → K) (hn : nrm q ≠ 0) :
    kappa q Q = Q 0 * (1 / nrm q - 1 / 3) + Q 1 * (q ^ 2 / nrm q - 1 / 3) +
      Q 2 * (q ^ 4 / nrm q - 1 / 3) := by
  unfold nrm at hn ⊢
  simp [kappa, P3, vvT, nrm, Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three,
    diagonal]
  field_simp
  ring

/-- **A constant insertion has no connected part.** -/
theorem kappa_const (q : K) (Q : Fin 3 → K) (hn : nrm q ≠ 0)
    (h1 : Q 1 = Q 0) (h2 : Q 2 = Q 0) : kappa q Q = 0 := by
  rw [kappa_eq q Q hn, h1, h2]
  unfold nrm at hn ⊢
  field_simp
  ring

theorem Econn_eq (q : K) (Q : Fin 3 → K) :
    Econn q Q = kappa q Q • ((3 / 2 : K) • P3 q - (1 / 2 : K) • (1 : Matrix (Fin 3) (Fin 3) K)) := by
  have htr : (diagonal Q * (1 - P3 q)).trace =
      (diagonal Q).trace - (diagonal Q * P3 q).trace := by
    rw [Matrix.mul_sub, mul_one, Matrix.trace_sub]
  simp only [Econn, Eproj, kappa, htr]
  ext i j
  simp only [Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
  field_simp
  ring

/-- **Connected trace of the vertex on `W_{+1}`**: `κ(Q)(2q¹⁰ + 1)/2`. -/
theorem trace_Econn_AB_pow_five (q : K) (Q : Fin 3 → K) (hq : q ≠ 0) (hn : nrm q ≠ 0) :
    (Econn q Q * (A q * B q) ^ 5).trace = kappa q Q * (2 * q ^ 10 + 1) / 2 := by
  rw [Econn_eq, Matrix.smul_mul, Matrix.trace_smul, Matrix.sub_mul, Matrix.trace_sub,
    Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_smul, Matrix.trace_smul, one_mul,
    trace_P3_AB_pow_five q hq hn, trace_AB_pow_five q hq]
  simp only [smul_eq_mul]; ring

/-- **Connected trace of the vertex on `W_{−1}`**: the same form. -/
theorem trace_Econn_BA_pow_five (q : K) (Q : Fin 3 → K) (hq : q ≠ 0) (hn : nrm q ≠ 0) :
    (Econn q Q * (B q * A q) ^ 5).trace = kappa q Q * (2 * q ^ 10 + 1) / 2 := by
  rw [Econn_eq, Matrix.smul_mul, Matrix.trace_smul, Matrix.sub_mul, Matrix.trace_sub,
    Matrix.smul_mul, Matrix.smul_mul, Matrix.trace_smul, Matrix.trace_smul, one_mul,
    trace_P3_BA_pow_five q hq hn, trace_BA_pow_five q hq]
  simp only [smul_eq_mul]; ring

/-! ## 4. The two-term form factor -/

/-- `[2]_q = q + q⁻¹`. -/
noncomputable def qd2 (q : K) : K := q + q⁻¹

/-- One-term trace of `(σ₀σ₁)⁵` on `V^{⊗3}`: `W_{±3}` contribute `q^{±3}·q¹⁰`, `W_{±1}` contribute
`q^{±1}·(q¹⁰ − 1)`. -/
noncomputable def tOne (q : K) : K :=
  (q ^ 3 * q ^ 10 + q⁻¹ ^ 3 * q ^ 10 + q * ((A q * B q) ^ 5).trace +
    q⁻¹ * ((B q * A q) ^ 5).trace) / qd2 q ^ 3

/-- Connected (second) term: `W_{±3}` are one-dimensional and contribute `0`; `Qp`, `Qm` are the
charge insertions on `W_{+1}`, `W_{−1}`. -/
noncomputable def tTwo (q : K) (Qp Qm : Fin 3 → K) : K :=
  (q * (Econn q Qp * (A q * B q) ^ 5).trace + q⁻¹ * (Econn q Qm * (B q * A q) ^ 5).trace) /
    qd2 q ^ 3

/-- The two-term form factor `𝒲₂ = t₁ + c_em·t₂`. -/
noncomputable def twoTerm (q c : K) (Qp Qm : Fin 3 → K) : K :=
  tOne q + c * tTwo q Qp Qm

/-- **The one-term part is the convention-D closed form** `𝒲(q) = q²(q¹² + q⁸ − 1)/(q² + 1)²`. -/
theorem tOne_eq_weakVertexTrace (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    tOne q = QOU.Braiding.WeakVertexT35.weakVertexTrace q := by
  rw [tOne, trace_AB_pow_five q hq, trace_BA_pow_five q hq, qd2,
    QOU.Braiding.WeakVertexT35.weakVertexTrace]
  field_simp
  ring

theorem tTwo_eq (q : K) (Qp Qm : Fin 3 → K) (hq : q ≠ 0) (hn : nrm q ≠ 0) :
    tTwo q Qp Qm =
      (q * kappa q Qp + q⁻¹ * kappa q Qm) * (2 * q ^ 10 + 1) / (2 * qd2 q ^ 3) := by
  rw [tTwo, trace_Econn_AB_pow_five q Qp hq hn, trace_Econn_BA_pow_five q Qm hq hn]
  ring

/-- **One charge type on the vertex strands: the two-term form factor is the one-term one**, for
every `c_em`. -/
theorem twoTerm_eq_of_uniform (q c : K) (Qp Qm : Fin 3 → K) (hq : q ≠ 0) (hn : nrm q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0)
    (hp1 : Qp 1 = Qp 0) (hp2 : Qp 2 = Qp 0) (hm1 : Qm 1 = Qm 0) (hm2 : Qm 2 = Qm 0) :
    twoTerm q c Qp Qm = QOU.Braiding.WeakVertexT35.weakVertexTrace q := by
  rw [twoTerm, tTwo_eq q Qp Qm hq hn, kappa_const q Qp hn hp1 hp2, kappa_const q Qm hn hm1 hm2,
    tOne_eq_weakVertexTrace q hq h2]
  ring

/-! ## 5. A labelled example: lepton on strand 0, quarks on strands 1, 2

Charges `quark (u, d) = (2/3, −1/3)`, `lepton (ν, e⁻) = (0, −1)` (the audit's C-lep assumption).
`Q_pair` on `W_{+1} = (uud, udu, duu)` is `(−2/9, −2/9, −8/9)`; on `W_{−1} = (udd, dud, ddu)` it is
`(1/9, −5/9, −5/9)`. This colouring is an example; nothing selects it. -/

/-- `Q_pair` on `W_{+1}`, lepton on strand 0. -/
noncomputable def QpLeptonFirst : Fin 3 → K := ![-2 / 9, -2 / 9, -8 / 9]

/-- `Q_pair` on `W_{−1}`, lepton on strand 0. -/
noncomputable def QmLeptonFirst : Fin 3 → K := ![1 / 9, -5 / 9, -5 / 9]

theorem tTwo_lepton_first (q : K) (hq : q ≠ 0) (hn : nrm q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    tTwo q QpLeptonFirst QmLeptonFirst =
      -2 * q ^ 2 * (q ^ 2 - 1) * (2 * q ^ 10 + 1) / (9 * (q ^ 2 + 1) ^ 3) := by
  rw [tTwo_eq q _ _ hq hn, kappa_eq q _ hn, kappa_eq q _ hn, qd2]
  simp only [QpLeptonFirst, QmLeptonFirst, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]
  unfold nrm at hn ⊢
  field_simp
  ring

end QOU.QBeta.WeakVertexTwoTerm
