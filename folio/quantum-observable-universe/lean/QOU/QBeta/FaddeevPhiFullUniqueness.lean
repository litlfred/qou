import QOU.QBeta.PhiBProdLociDensity
import QOU.MathlibExt.FaddeevQuantumDilogarithm

/-!
# `Φ_b` uniqueness — conditional on strip-growth + meromorphic normal form

Composes `PhiBProdLociDensity.phiBProd_uniqueUpToScalar_of_normalForm` into a
single-class interface: `FaddeevPhiPhysical` packages the three requirements
(shift equations + strip-growth + normal form) that the uniqueness chain needs.

**Honest accounting of what this file does and does not do.**

* **What it does:** reduces Faddeev uniqueness to a single typeclass with three
  families of axioms (shift equations, growth bound, regularity). No further
  hypotheses appear as explicit arguments — they are all class fields.

* **What it does NOT do:** the two added fields (`instStripGrowth`, `hNF`) are
  **carried axioms**, not proved theorems. They are the QOU §3b conjecture-class
  pattern: open inputs packaged as class fields so downstream composition is
  clean. The class is non-vacuous (the concrete `phiBProd` satisfies all three),
  but instantiating it for a second solution IS the remaining analytic content.

* **`instStripGrowth` (physical content):** the strip-growth bound
  `‖Φ₁ z‖ ≤ C · ‖phiBProd b z‖` is the physical asymptotic condition that
  Faddeev and Kashaev use to single out `Φ_b` among solutions of the shift
  equations. It excludes elliptic multipliers (which grow in the strip). This
  is a standard and physically motivated uniqueness input.

* **`hNF` (Lean technicality):** `MeromorphicNFOn Φ₁ Set.univ` says the
  total-function encoding of `Φ₁` has value 0 at poles (Mathlib's convention
  for meromorphic functions as total functions). This is NOT a mathematical
  hypothesis — any meromorphic function can be put in normal form. It is a
  **Lean formalization regularity condition** needed because `FaddeevPhi` works
  with raw `ℂ → ℂ` (which could have arbitrary junk values at poles). For the
  concrete `Φ_b = num/den` (quotient of entire functions), `MeromorphicNFOn`
  holds by construction.

* **Scope:** the uniqueness is **conditional on the class axioms**. Saying
  "A_ω is uniquely determined" means: uniquely determined for any `Φ₁` that
  is a FaddeevPhi + strip-growth + NF solution. The class axioms are the
  honest open inputs.

-- Ref: [faddeev1995] Faddeev 1995 — the integral solution s(P) of the shift
--      equation s(P+p)/s(P) = 1/(1 + e^{iPq/ħ}) and its factorisation into
--      the θ and −1/θ halves. The source states no uniqueness theorem; the
--      strip-growth condition used here to single out Φ_b is not taken from
--      a held source.
-- Ref: docs/coordination/delta-lambda-magnitude-derivation.md — T1/T2
-/

open Complex
open QOU.MathlibExt.FaddeevQuantumDilogarithm
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta.FaddeevPhiFullUniqueness

/-- **`Φ_b` with strip-growth + normal form (conjecture-class, §3b).**
Extends `FaddeevPhi` with the two regularity conditions that the uniqueness
chain needs. Both are **carried axioms** (open inputs packaged as class fields):

- **strip-growth comparability** to `phiBProd` — the physical asymptotic
  condition (Faddeev–Kashaev) excluding elliptic multipliers.
- **meromorphic normal form** on `ℂ` — a Lean technicality (total-function
  values at poles are 0); holds by construction for quotients of entire
  functions.

The class is non-vacuous: `phiBProd` itself satisfies all fields. But
instantiating it for a *second* solution IS the remaining analytic content
(the open input that the shift equations alone do not provide). -/
class FaddeevPhiPhysical (t : ℝ) (Φ : ℂ → ℂ)
    extends FaddeevPhi (substrateB t) Φ : Prop where
  /-- `Φ` is comparable in modulus to `phiBProd` (physical strip-growth bound). -/
  instStripGrowth : FaddeevPhiStripGrowth (substrateB t) Φ
  /-- `Φ` is in meromorphic normal form on `ℂ` (Lean regularity, not a math
  hypothesis — any meromorphic function can be represented this way). -/
  hNF : MeromorphicNFOn Φ Set.univ

/-- **Uniqueness conditional on class axioms.** Any `FaddeevPhiPhysical` solution
is proportional to `phiBProd`. The conclusion is conditional on the class fields
(shift equations + strip-growth + NF); no further hypotheses appear as explicit
arguments. Composes the full sorry-free chain:
`PhiBProdLociDensity.phiBProd_uniqueUpToScalar_of_normalForm`. -/
theorem faddeevPhi_uniqueUpToScalar {t : ℝ} (ht : 0 < t) {Φ₁ : ℂ → ℂ}
    [h : FaddeevPhiPhysical t Φ₁] :
    ∃ c, ∀ z, phiBProd (substrateB t) z ≠ 0 → Φ₁ z = c * phiBProd (substrateB t) z := by
  letI : FaddeevPhi (substrateB t) Φ₁ := h.toFaddeevPhi
  letI : FaddeevPhiStripGrowth (substrateB t) Φ₁ := h.instStripGrowth
  exact PhiBProdLociDensity.phiBProd_uniqueUpToScalar_of_normalForm ht h.hNF

end QOU.QBeta.FaddeevPhiFullUniqueness
