import QOU.SchurWeyl.MarkovTraceUnique

/-!
# QOU.Interactions.HopfElectronTwoTermMass — the electron conjecture on σ₀σ₁σ₀, two-term

Owner ruling 2026-11-21 (`docs/coordination/owner-rulings.md`): **the electron is
`σ₀σ₁σ₀ ∈ B₃`, whose closure is the Hopf link**; the trefoil `σ₀³ ∈ B₂` is kept as a backup
(`QOU.Interactions.TrefoilCanonicalMassUnit.TrefoilElectronMassConj`). Same day: mass uses the
**two-term Lagrangian trace** `τ(ℒ) = τ(𝒟²) + τ(ψ*𝒟ψ)`
(`QOU.CategoricalLagrangianTwoTermBridge.trace_lagrangian_two_term_split`), not a single trace.
Rulings are conjectures until derived, so this file **states** the ruling as a conjecture
carrier and proves what can be proved about it.

## What is proved

* `electronWord` — `σ₀σ₁σ₀` in the corpus's `Hecke K q qi 2 = H₃(q)`.
* `tr_electronWord` — for **any** Markov trace family with parameter `z` on the tower,
  `tr₂(σ₀σ₁σ₀) = (q − qi)·z² + (q·qi)·z`. With `qi = q⁻¹` this is `(q − q⁻¹) z² + z`. The
  physics weighting (the quantum trace of the Jimbo action, ruling 2026-11-20) is the family at
  `z_D = q³/(q²+1)` (`JimboActionKernel.jimboMarkov`), so this is the braid term of the
  electron's two-term trace, in closed form.

## The conjecture carrier

`HopfElectronTwoTermMassConj U ρ matter` is a predicate on **given** data: a Markov trace family
`U`, a multiplicity `ρ`, and the value `matter` of the matter term `τ(ψ*𝒟ψ)` for the electron.
It asserts `ρ · |τ(σ₀σ₁σ₀) + matter| = 1`: the two-term trace is one electron mass unit (CAL-1).

**GAP.** The matter term for a lepton is not defined in the corpus; its derivation is in progress
on a sibling branch (PR #8743, bean `qou-99qc`). `matter` is therefore a parameter, never an
instance-chosen field: there is no instance, and none may be built by choosing `matter`. With
`matter = 0` the statement is the one-term reading, which the ruling says is not the mass.

## Base ring (§7c)

The trace computation is generic `[CommRing K]`. The conjecture needs an absolute value, so it is
stated over a linearly ordered field.
-/

namespace QOU.Interactions.HopfElectronTwoTermMass

open QOU.SchurWeyl QOU.SchurWeyl.Hecke QOU.SchurWeyl.HeckeInclusion

section Trace

variable {K : Type*} [CommRing K] {q qi z : K}

/-- `σ₀ ∈ H₃(q)`. -/
noncomputable abbrev s0 (K : Type*) [CommRing K] (q qi : K) : Hecke K q qi 2 := σ K q qi 2 0

/-- `σ₁ ∈ H₃(q)`. -/
noncomputable abbrev s1 (K : Type*) [CommRing K] (q qi : K) : Hecke K q qi 2 := σ K q qi 2 1

/-- **The electron word** `σ₀σ₁σ₀ ∈ H₃(q)` (owner ruling 2026-11-21; closure: the Hopf link,
`ElectronWordCandidates.numCycles_s0s1s0`). -/
noncomputable def electronWord (K : Type*) [CommRing K] (q qi : K) : Hecke K q qi 2 :=
  s0 K q qi * s1 K q qi * s0 K q qi

/-- `tr₁(σ₀) = z`. -/
theorem tr_one_sigma (U : HeckeCoset.MarkovTraceFamily K q qi z) :
    U.tr 1 (σ K q qi 1 0) = z := U.param_eq

/-- `σ₀ ∈ H₃` is the image of `σ₀ ∈ H₂`. -/
theorem s0_eq_incl : s0 K q qi = heckeIncl K q qi 1 (σ K q qi 1 0) := by
  rw [heckeIncl_σ]; rfl

/-- `σ₁ ∈ H₃` is the top generator. -/
theorem s1_eq_last : s1 K q qi = σ K q qi 2 (Fin.last 1) := rfl

/-- `tr₂(σ₁) = z`. -/
theorem tr_s1 (U : HeckeCoset.MarkovTraceFamily K q qi z) : U.tr 2 (s1 K q qi) = z := by
  have h := U.tr_markov 1 1
  rw [map_one, one_mul, U.tr_one, mul_one] at h
  rw [s1_eq_last]; exact h

/-- `tr₂(σ₀σ₁) = z²`. -/
theorem tr_s0_s1 (U : HeckeCoset.MarkovTraceFamily K q qi z) :
    U.tr 2 (s0 K q qi * s1 K q qi) = z * z := by
  rw [s0_eq_incl, s1_eq_last, U.tr_markov 1, tr_one_sigma]

/-- **The braid term of the electron's trace, in closed form.** For any Markov trace family
with parameter `z`: `tr₂(σ₀σ₁σ₀) = (q − qi)·z² + (q·qi)·z`. -/
theorem tr_electronWord (U : HeckeCoset.MarkovTraceFamily K q qi z) :
    U.tr 2 (electronWord K q qi) = (q - qi) * (z * z) + (q * qi) * z := by
  have hcyc : U.tr 2 (electronWord K q qi) = U.tr 2 (s0 K q qi * s0 K q qi * s1 K q qi) := by
    rw [electronWord, U.tr_cyclic 2 (s0 K q qi * s1 K q qi) (s0 K q qi), ← mul_assoc]
  rw [hcyc, σ_quadratic K q qi 2 0, add_mul, smul_mul_assoc, smul_mul_assoc, one_mul,
    map_add, map_smul, map_smul, tr_s0_s1, tr_s1, smul_eq_mul, smul_eq_mul]

end Trace

section Conjecture

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {q z : K}

/-- **Conjecture (owner ruling 2026-11-21, two-term): the electron `σ₀σ₁σ₀` is one mass unit.**

For a given Markov trace family `U` (the physics weighting is `JimboActionKernel.jimboMarkov`, at
`z_D`), a given multiplicity `ρ` and the given value `matter` of the electron's matter term
`τ(ψ*𝒟ψ)`: `ρ · |τ(σ₀σ₁σ₀) + matter| = 1`.

All data are parameters, so this is a falsifiable statement about them; no instance exists and
none may be manufactured by choosing `matter`. The matter term for a lepton is the open part
(PR #8743, bean `qou-99qc`). Backup model: `TrefoilElectronMassConj`.
@conjecture: primary -/
class HopfElectronTwoTermMassConj (U : HeckeCoset.MarkovTraceFamily K q q⁻¹ z) (ρ : ℕ)
    (matter : K) : Prop where
  /-- The two-term trace of the electron word is one electron mass unit. -/
  two_term_unit : (ρ : K) * |U.tr 2 (electronWord K q q⁻¹) + matter| = 1

omit [IsStrictOrderedRing K] in
/-- The conjecture, with the braid term written out: `ρ · |(q − q⁻¹) z² + z + matter| = 1`. -/
theorem HopfElectronTwoTermMassConj.closed_form {U : HeckeCoset.MarkovTraceFamily K q q⁻¹ z}
    {ρ : ℕ} {matter : K} (hq : q ≠ 0) (h : HopfElectronTwoTermMassConj U ρ matter) :
    (ρ : K) * |(q - q⁻¹) * (z * z) + z + matter| = 1 := by
  have h1 := h.two_term_unit
  rwa [tr_electronWord, mul_inv_cancel₀ hq, one_mul] at h1

end Conjecture

end QOU.Interactions.HopfElectronTwoTermMass
