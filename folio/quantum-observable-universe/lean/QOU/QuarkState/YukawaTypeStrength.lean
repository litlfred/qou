import QOU.QuarkState.YukawaStrandOrder

/-!
# Is a type-dependent (quark vs lepton) Yukawa strength derived?

Bean `qou-99qc`. Owner (Carl, 2026-11-21) chose option 3 of PR #8740, *"Research type-dependent
strength"*. Pre-registered in
`computations/probes/qbeta_yukawa_strand_order/PREREGISTRATION-part2-type-dependent-strength.md`
(commit `fbbd12c26a`). The split of part 1 is `split y_u y_d y_ν y_e c_Φ c_Φ̃`
(`YukawaStrandOrder.split`); type-only strengths give `−(y_q² − y_ℓ²)(q² − 1)/(q² + 1)`
matter-left.

This file proves the structural facts that decide each candidate. **No candidate derives
`y_q ≠ y_ℓ`.**

## Results (generic field `K`, §7c)

**Candidate 1 — the matter object's amplitude in its own closure.**
* `ptrR_Rc_K` : the right pivotal partial trace of one crossing is the twist `θ = q²`;
  `ptrR_RcInv_K` : of the inverse crossing, `q⁻²`.
* `cutOpen_unknot_framing` : the unknot is the closure of the empty word on one strand
  (cut-open amplitude `1`) and of `σ₀` on two strands (amplitude `θ = q² ≠ 1` unless `q² = 1`).
  So the cut-open amplitude is a FRAMED invariant: it depends on the word, not only on the link.
* `cutOpen_hopf` : `σ₀²` (closure the Hopf link) has cut-open amplitude `(q⁴ + 1)/q`, a scalar.
  The ruled electron `σ₀σ₁σ₀` closes to the same link with one more unit of writhe; the probe
  verifies its amplitude is `θ·(q⁴ + 1)/q = q(q⁴ + 1)` (exact, `ℚ(q)`).
  Reading the quark as its own knot type (the ruled unknot) gives amplitude `1`, the same as
  the neutrino's unknot carrier. Reading it as the cut-open Borromean gives a different scalar
  (probe). Using any of these as a Yukawa strength is a NEW identification, with framing,
  amplitude-vs-square and reading unforced.

**Candidate 2 — strand number / Hecke level.** Under the ruling the electron word and `V³` both
live on three strands, so a strength through the level is type-blind:
`split_typeOnly_equal` gives `0`.

**Candidate 3 — the volume formula component-wise.** `volFormula_hopf_ne` : with `Vol = 0`
(the Hopf link and the unknot are torus links) `m_e·Vol·ρ/ℏ_q² = 0 ≠ m_e` whenever `m_e ≠ 0`
(CAL-1). Scope (b) for this formula as the electron's strength; invariant `Vol(Hopf) = 0`.

**Candidate 4 — colour.** `PR_scale_invariant` : rescaling the crossing by any `c ≠ 0` (the
sl_N colour framing `q^{-1/N}` included) leaves the right-line projector, hence both vev weights,
unchanged. `split_colourMultiplicity` : IF a multiplicity `N` were put on quark strands only
(no corpus object does), the matter-left split would be `−(N − 1)y²(q² − 1)/(q² + 1)`; labelled
consequence, not adopted.

**Candidate 5 — a Higgs line threading the object.** `RcInv_eq` gives `Ř⁻¹ = Ř − h`.
`vev_cross_u`, `vev_cross_d_over`, `vev_cross_d_under` : carrying the vev slot `d` past a matter
strand keeps it with amplitude `1` past `u`, `q` (over) or `q⁻¹` (under) past `d`. The factor
depends on the crossed strand's weight (flavour) and on the chosen threading, not on its type.

## What is NOT claimed

* No strength is derived, no strand order is selected, no split is evaluated, nothing is
  compared with `Q_β` or `m_n − m_p`.
* That the cut-open amplitude is irrelevant. It is the one candidate that separates the links;
  adopting it would be a new rule (owner decision), with three further unforced choices.

-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §XIV (twist, pivotal partial traces)
-- Ref: [turaev1994] Quantum Invariants of Knots and 3-Manifolds, de Gruyter, §I.2 (framed links)
-/

namespace QOU.QuarkState.YukawaTypeStrength

open Matrix
open QOU.QuarkState.YukawaStrandOrder

variable {K : Type*} [Field K]

/-- The inverse crossing `Ř⁻¹ = Ř − h·1`, `h = q − q⁻¹`. -/
def RcInv (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q⁻¹, 0, 0, 0; 0, -(q - q⁻¹), 1, 0; 0, 1, 0, 0; 0, 0, 0, q⁻¹]

local macro "mat4" : tactic =>
  `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> (try field_simp) <;> (try ring)))

theorem RcInv_eq (q : K) :
    RcInv q = Rc q - (q - q⁻¹) • (1 : Matrix (Fin 4) (Fin 4) K) := by
  simp only [RcInv, Rc]; ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.one_apply]

theorem Rc_mul_RcInv (q : K) (hq : q ≠ 0) : Rc q * RcInv q = 1 := by
  simp only [Rc, RcInv]; mat4

/-! ## Candidate 1: cut-open amplitudes are framed invariants -/

/-- **The twist.** Right pivotal partial trace (`K = diag(q, q⁻¹)`) of one crossing: `q²·1`. -/
theorem ptrR_Rc_K (q : K) (hq : q ≠ 0) :
    ptrR (Rc q) q q⁻¹ = (q ^ 2) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [ptrR, Rc, Matrix.one_apply] <;> field_simp <;> ring

/-- The inverse twist `q⁻²·1`. -/
theorem ptrR_RcInv_K (q : K) (hq : q ≠ 0) :
    ptrR (RcInv q) q q⁻¹ = (q⁻¹ ^ 2) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [ptrR, RcInv, Matrix.one_apply] <;>
    field_simp <;> ring

/-- **Framing dependence.** The unknot is the closure of the empty one-strand word (cut-open
amplitude `1`) and of `σ₀` on two strands (amplitude `q²`). The two agree only if `q² = 1`. -/
theorem cutOpen_unknot_framing (q : K) (hq : q ≠ 0) (hq1 : q ^ 2 ≠ 1) :
    ptrR (Rc q) q q⁻¹ = (q ^ 2) • (1 : Matrix (Fin 2) (Fin 2) K) ∧
      (q ^ 2) • (1 : Matrix (Fin 2) (Fin 2) K) ≠ (1 : Matrix (Fin 2) (Fin 2) K) := by
  refine ⟨ptrR_Rc_K q hq, fun h => hq1 ?_⟩
  have := congrFun (congrFun h 0) 0
  simpa using this

/-- **The Hopf link `σ₀²`:** cut-open amplitude `(q⁴ + 1)/q`, a scalar. -/
theorem cutOpen_hopf (q : K) (hq : q ≠ 0) :
    ptrR (Rc q * Rc q) q q⁻¹ = ((q ^ 4 + 1) / q) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [ptrR, Rc, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;>
    field_simp <;> ring

/-! ## Candidate 2: equal levels give equal strengths -/

/-- Any rule through the strand number gives `y_q = y_ℓ` under the ruling (both on three
strands), and then the type-only split is `0`. -/
theorem split_typeOnly_equal (y cPhi cConj : K) : split y y y y cPhi cConj = 0 := by
  unfold split; ring

/-! ## Candidate 3: the volume formula on a volume-zero closure -/

/-- With `Vol = 0` the volume–density formula gives `0`, which is not `m_e` when `m_e ≠ 0`. -/
theorem volFormula_hopf_ne (me rho hbar : K) (hme : me ≠ 0) :
    me * 0 * rho / hbar ^ 2 = 0 ∧ me * 0 * rho / hbar ^ 2 ≠ me := by
  refine ⟨by simp, ?_⟩
  simp only [mul_zero, zero_mul, zero_div]
  exact fun h => hme h.symm

/-! ## Candidate 4: a scalar framing does not move the vev weights -/

/-- **Scale invariance.** The right-line projector of `c·Ř` (eigenvalues `c q`, `−c q⁻¹`) is the
projector of `Ř`. -/
theorem PR_scale_invariant (q c : K) (hq : q ≠ 0) (hc : c ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (c * q + c * q⁻¹)⁻¹ • ((c * q) • (1 : Matrix (Fin 4) (Fin 4) K) - c • Rc q) = PR q := by
  have hq2 : q + q⁻¹ ≠ 0 := by
    intro h; apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  have e1 : c * q + c * q⁻¹ = c * (q + q⁻¹) := by ring
  have e2 : (c * q) • (1 : Matrix (Fin 4) (Fin 4) K) - c • Rc q =
      c • (q • (1 : Matrix (Fin 4) (Fin 4) K) - Rc q) := by
    rw [smul_sub, smul_smul]
  rw [e1, e2, smul_smul, mul_inv_rev, mul_assoc, inv_mul_cancel₀ hc, mul_one, PR]

/-- **If** a multiplicity `N` sat on quark strands only (`y_q² = N y²`, `y_ℓ² = y²`), the
matter-left split would be `−(N − 1)y²(q² − 1)/(q² + 1)`. Labelled consequence; no corpus object
carries `N`. -/
theorem split_colourMultiplicity (q yq y N : K) (hN : yq ^ 2 = N * y ^ 2) (h2 : q ^ 2 + 1 ≠ 0) :
    splitML q yq yq y y = -((N - 1) * y ^ 2 * ((q ^ 2 - 1) / (q ^ 2 + 1))) := by
  rw [split_typeOnly_matterLeft q yq y h2, hN]; ring

/-! ## Candidate 5: threading the vev past a matter strand -/

/-- Basis vectors of `V ⊗ V`. -/
def e (i : Fin 4) : Fin 4 → K := Pi.single i 1

/-- Past a `u` strand (`u ⊗ d ↦ d ⊗ u`): amplitude `1`. -/
theorem vev_cross_u (q : K) : Rc q *ᵥ e 1 = e 2 := by
  ext i; fin_cases i <;> simp [Rc, e, mulVec, dotProduct, Fin.sum_univ_four, Pi.single_apply]

/-- Past a `d` strand, over: amplitude `q`. -/
theorem vev_cross_d_over (q : K) : Rc q *ᵥ e 3 = q • e 3 := by
  ext i; fin_cases i <;> simp [Rc, e, mulVec, dotProduct, Fin.sum_univ_four, Pi.single_apply]

/-- Past a `d` strand, under: amplitude `q⁻¹`. -/
theorem vev_cross_d_under (q : K) : RcInv q *ᵥ e 3 = q⁻¹ • e 3 := by
  ext i; fin_cases i <;> simp [RcInv, e, mulVec, dotProduct, Fin.sum_univ_four, Pi.single_apply]

end QOU.QuarkState.YukawaTypeStrength
