import Mathlib.Data.Real.Basic

/-!
# QOU.FluidDynamics.dss_escapes_nrs — why discretely self-similar escapes NRŠ

Structural backing for the Finding-1 re-scope of the Leray profile
(`prop:leray-profile`, `conj:regularity-breakdown`) from *continuous*
backward-self-similar to **discretely self-similar** (DSS), per the q-NS gap
audit ([`docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md`](../../../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md)).

**Scope discipline (owner directive 2026-07-24).** The profile `U(s)` is the
QOU's own internal blow-up profile in similarity time. This file is a structural
fact about the steady-vs-periodic profile *classes*; it explains why scoping the
QOU-internal profile to discretely self-similar is consistent with the NRŠ no-go.
It is a statement about QOUs / profile classes, not about the classical `ℝ³` PDE.

## The point

In Leray's similarity variables the profile is a function `U = U(s)` of
`s = -log(T* - t)`. Two regularity classes:

* **continuous self-similar** — `U` is `s`-*independent* (steady);
* **discretely self-similar (DSS)** — `U` is `s`-*periodic* with some period
  `P > 0` (`P = 2 log λ` for the scaling factor `λ > 1`; no value of `P` is
  fixed, and in particular it is not tied to the root-of-unity ladder
  `q_κ = exp(iπ/κ)`, which `def:substrate-parameter` excludes — see
  `QOU.FluidDynamics.DSSObstructions.qKappa_is_root_of_unity`).

Nečas–Růžička–Šverák (Acta Math. 176, 1996) exclude the *steady* finite-energy
profile. This file records the clean structural reason the DSS class **survives**
that no-go:

`selfSimilar_iff_all_periods` — a profile is steady **iff** it is periodic for
*every* period. So the NRŠ-excluded (steady) class is exactly the intersection of
all the periodic classes; a genuinely *single*-period DSS profile
(`dss_not_selfSimilar_of_nonconstant`) is **not** steady, hence not touched by
the no-go.

## Honest scope

This is a structural fact about the profile classes — it explains why the DSS
re-scope is *consistent* with NRŠ. It does **not** construct a nontrivial DSS
profile (that existence — the finite-dimensional Leray shooting problem — is the
open content of `prop:leray-profile` / `conj:regularity-breakdown`). The NRŠ
no-go itself is a cited literature theorem, not re-proved here.

## Base ring (§7c)
Archimedean: `U : ℝ → ℝ` on the similarity time `s ∈ ℝ`. `ℝ` is correct.

## References
- [leitner2026] fluid-dynamics/leray-profile, leray-profile-construction,
  regularity-breakdown, leray-profile-exclusions
- Nečas–Růžička–Šverák, Acta Math. 176 (1996) 283–294 (`necas-ruzicka-sverak1996`)
-/

namespace QOU.FluidDynamics

/-- The similarity profile `U(s)` is **(continuously) self-similar** if it is
    independent of the similarity time `s` (steady). This is the class NRŠ
    excludes for finite energy. -/
def SelfSimilar (U : ℝ → ℝ) : Prop := ∀ s, U s = U 0

/-- The similarity profile `U(s)` is **discretely self-similar** with period `P`
    if it is `P`-periodic in `s` (`P = 2 log λ` for the scaling factor `λ`;
    no value of `P` is fixed). -/
def DSSPeriodic (U : ℝ → ℝ) (P : ℝ) : Prop := ∀ s, U (s + P) = U s

/-- **Steady = periodic for every period.** A similarity profile is
    (continuously) self-similar iff it is discretely self-similar for *every*
    period `P`. Hence the NRŠ-excluded steady class is precisely the intersection
    of all the DSS classes. -/
-- Ref: [leitner2026] fluid-dynamics/leray-profile
theorem selfSimilar_iff_all_periods (U : ℝ → ℝ) :
    SelfSimilar U ↔ ∀ P, DSSPeriodic U P := by
  constructor
  · intro h P s; rw [h (s + P), h s]
  · intro h s
    have := h s 0
    simpa using this

/-- **Single-period DSS is not steady** (given a non-constant value). A DSS
    profile that takes some value `≠ U 0` is not self-similar — so it lies in the
    complement of the NRŠ-excluded steady class and is not touched by the no-go.
    This is the class the discretely-self-similar re-scope lives in. -/
-- Ref: [leitner2026] fluid-dynamics/leray-profile, regularity-breakdown
theorem dss_not_selfSimilar_of_nonconstant {U : ℝ → ℝ}
    (hwit : ∃ s, U s ≠ U 0) : ¬ SelfSimilar U := by
  rintro h
  obtain ⟨s, hs⟩ := hwit
  exact hs (h s)

/-- **The steady class is the strict floor.** Any self-similar profile is DSS for
    every period (its `s`-independence is the degenerate case of periodicity);
    the content of the re-scope is that the converse fails — non-steady
    single-period profiles exist in principle and are what NRŠ leaves open. -/
-- Ref: [leitner2026] fluid-dynamics/leray-profile
theorem selfSimilar_isDSS {U : ℝ → ℝ} (h : SelfSimilar U) (P : ℝ) :
    DSSPeriodic U P :=
  (selfSimilar_iff_all_periods U).mp h P

end QOU.FluidDynamics
