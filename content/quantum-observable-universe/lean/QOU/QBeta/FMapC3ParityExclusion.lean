import Mathlib.Tactic

/-!
# Bar-parity exclusion of a bar-odd derivation of `c₃ = J_Hopf(1) = −2`

Bean `qou-cds1` (f-map attack). Three feasibility probes tried to DERIVE the
c₃ identification `c₃ = J_Hopf(1) = −2` from the convention-D two-row Markov
trace: route A (the bar-odd crossing term), route B (the Z3 carrier `G·D`,
bar-even functional × bar-odd carrier), and the bar-even redirect. Routes A and
B both fail for the SAME reason, and it is a proved parity invariant, not a
numeric near-miss.

`c₃ = J_Hopf(1) = −2` is the value of the Hopf-link Jones polynomial
`−(q²+q⁻²)` at `q = 1` — a **bar-EVEN** quantity (`q ↦ q⁻¹` fixes `q²+q⁻²`),
value `−2 ≠ 0`. But every **bar-odd** construction vanishes at the bar fixed
point `q = 1`. So no bar-odd object — crossing term or Z3 carrier — can produce
the bar-even value `−2` there. This file formalises that invariant.

Symbolic cross-check (all 19 assertions, exact ℚ(q)):
`computations/qbeta/fmap_c3_parity_genericity_exclusion.py`. The bar-EVEN
channel fails separately, by genericity (scope-(a)) — `−2` at `q=1` is hit by
many bar-even combinations and none equals the full (non-bar-even) Hopf
polynomial — recorded in the probe and the audit, not here (it is not a proved
invariant). Sorry-free.

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
-- Ref: docs/audits/2026-08-21-fmap-c3-parity-genericity-exclusion.md
-/

namespace QOU.QBeta

/-- The bar-odd part of a function of `q` under the bar involution `q ↦ q⁻¹`:
    `barOdd f q = (f q − f q⁻¹)/2`. -/
noncomputable def barOdd (f : ℝ → ℝ) (q : ℝ) : ℝ := (f q - f q⁻¹) / 2

/-- **Any bar-odd part vanishes at the bar fixed point `q = 1`.** Since
    `(1 : ℝ)⁻¹ = 1`, `barOdd f 1 = (f 1 − f 1)/2 = 0`. -/
@[simp] theorem barOdd_at_one (f : ℝ → ℝ) : barOdd f 1 = 0 := by
  unfold barOdd; rw [inv_one]; ring

/-- **Parity exclusion of the bar-odd routes to `c₃`.** The bar-odd content of
    any construction is `0` at `q = 1`, but the c₃ target — the Hopf-link Jones
    value at `q = 1` — is `−2 ≠ 0`. So `c₃ = J_Hopf(1) = −2` cannot be the
    bar-odd content of any object: it is a **bar-EVEN q=1 shadow**. This is the
    single invariant behind the refutation of both route A (crossing term) and
    route B (Z3 carrier); both are bar-odd, hence vanish here. -/
theorem barOdd_ne_hopf_value_at_one (f : ℝ → ℝ) : barOdd f 1 ≠ -2 := by
  rw [barOdd_at_one]; norm_num

/-- **The Hopf-link Jones value `−(q²+q⁻²)` is bar-EVEN**, so it is *not* an
    obstruction to the parity argument: it sits in the complementary channel to
    every bar-odd construction. (`bar` sends `q ↦ q⁻¹`; `q²+q⁻²` is fixed.) -/
theorem hopfValue_bar_even (q : ℝ) (hq : q ≠ 0) :
    (-(q ^ 2 + (q⁻¹) ^ 2)) = (-((q⁻¹) ^ 2 + ((q⁻¹)⁻¹) ^ 2)) := by
  rw [inv_inv]; ring

/-- The Hopf value at the classical point is `−2` (bar-even, nonzero). -/
theorem hopfValue_at_one : (-((1 : ℝ) ^ 2 + (1⁻¹) ^ 2)) = -2 := by
  norm_num

/-! ### Route A, concretely: the D two-row trace's bar-odd part vanishes at q=1 -/

/-- The dimension-weighted convention-D two-row (Temperley–Lieb) Markov trace of
    the crossing power `σ^k`: block `(3)` scalar `q^k`, block `(2,1)` eigenvalues
    `q^k, (−q⁻¹)^k`, weights `y₃ᴰ, y₂₁ᴰ`. -/
noncomputable def traceD (k : ℕ) (q : ℝ) : ℝ :=
  ((q ^ 4 + 1) / (q ^ 2 + 1) ^ 2) * q ^ k
    + (q ^ 2 / (q ^ 2 + 1) ^ 2) * (q ^ k + (-(q⁻¹)) ^ k)

/-- **Route A, formalised.** The bar-odd part of the D two-row trace of any
    crossing power `σ^k` vanishes at `q = 1` — an instance of `barOdd_at_one`, so
    it can never equal the bar-even `c₃ = −2` there. -/
theorem barOdd_traceD_at_one (k : ℕ) : barOdd (traceD k) 1 = 0 := barOdd_at_one _

/-! ### Redirect, concretely: genericity + the Hopf polynomial is not bar-even -/

/-- **Genericity (scope-(a)).** Four unrelated bar-even D-quantities all equal
    `−2` at `q = 1` — `−[2]_q`, `−(q²+q⁻²)`, `−y₃ᴰ/y₂₁ᴰ = −(q⁴+1)/q²`, and
    `−1/(2y₂₁ᴰ)`. Matching the q=1 value distinguishes none of them, so it cannot
    force the Hopf identification: the anti-fit genericity that refutes the
    bar-even-weight route. -/
theorem targetValue_generic_at_one :
    (-((1 : ℝ) + 1⁻¹) = -2)
      ∧ (-((1 : ℝ) ^ 2 + 1⁻¹ ^ 2) = -2)
      ∧ (-(((1 : ℝ) ^ 4 + 1) / (1 : ℝ) ^ 2) = -2)
      ∧ (-(1 / (2 * ((1 : ℝ) ^ 2 / ((1 : ℝ) ^ 2 + 1) ^ 2))) = -2) := by
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- The skein-derived Hopf-link Jones polynomial in `s = √q`: `V(Hopf)(s) = −(s+s⁵)`. -/
noncomputable def VhopfS (s : ℝ) : ℝ := -(s + s ^ 5)

/-- **The Hopf polynomial is NOT bar-even.** It differs from its bar image at
    the witness point `s = 2` (`−34 ≠ −17/32`), so no bar-even object can equal
    it as a q-identity — only its `s = 1` *value* coincides. -/
theorem VhopfS_not_bar_even : VhopfS 2 ≠ VhopfS (2⁻¹) := by
  unfold VhopfS; norm_num

/-- The Hopf polynomial's value at the classical point `s = 1` is `−2`. -/
theorem VhopfS_at_one : VhopfS 1 = -2 := by unfold VhopfS; norm_num

end QOU.QBeta
