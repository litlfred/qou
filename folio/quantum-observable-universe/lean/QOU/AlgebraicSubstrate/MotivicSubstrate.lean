import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.RingTheory.Localization.Basic

/-!
# The motivic substrate

The QOU framework's algebraic substrate is axiomatized as a triple

  𝓢_mot := (K₀(Var_k), 𝕃, {ρ_v})

consisting of the Grothendieck ring of varieties, the Lefschetz
motive `𝕃 = [𝔸¹]`, and a tower of realization functors indexed by
the places of `ℚ`.  The Frobenius–Hopf substrate, the adelic
substrate, and the Habiro ring are all realizations of this single
underlying object: `ρ_∞` lands in `ℝ` (archimedean / topological
realization), `ρ_p` lands in `ℚ_p` (non-archimedean / cyclotomic
realization), and the inverse limit over `p` recovers the Habiro
completion.

This class is axiomatised: an instance carries the substrate data
plus a place-compatibility axiom.  Any `sorry` in an instance is to
be read as a **substrate axiom** (AGENTS.md §3b), not as a missing
proof.

**Formal-chain version.**  This file lives under `lean/QOU/` and is
compiled by `lake build`.  The co-located documentation stub at
`folio/quantum-observable-universe/algebraic-substrate/motivic-substrate.lean`
mirrors this content (per `QOU.GroundRingAnnotations`).

Out of scope here: mixed motives, Bloch–Kato exact sequences,
motivic Galois action between realizations.  The realization tower
is presented purely as a family of place-indexed evaluations.

Ref: [kontsevich1995] — Kontsevich's motivic integration lecture
Ref: [denef-loeser2001] https://doi.org/10.1090/S0894-0347-01-00374-7
Ref: [tate1967] Fourier analysis in number fields and Hecke's zeta functions
LaTeX label: `def:motivic-substrate`
-/

namespace QOU.AlgebraicSubstrate

/-- A **place** of `ℚ`: either the archimedean place `∞` or a
    finite prime `p`. The `finite` constructor takes a
    `Nat.Primes` value (Mathlib subtype `{p : ℕ // p.Prime}`) so
    that non-prime indices are ruled out at the type level. -/
inductive Place : Type
  | infty : Place
  | finite : Nat.Primes → Place
  deriving DecidableEq

/-- **The motivic substrate** (axiomatic class).

    `MotivicSubstrate K0 Mhat Target` axiomatises the QOU motivic
    substrate over:
    * `K0` — the Grothendieck ring `K₀(Var_k)`.
    * `Mhat` — the dimension-completed localization
      `𝓜̂ = K₀[𝕃⁻¹]^∧`.
    * `Target : Place → Type*` — the realization target at each
      place (e.g. `ℝ` at `∞`, `ℚ_p` at finite primes).

    Substrate axioms (paired place compatibility): the realization
    target is nontrivial at the archimedean place AND at some
    finite place — the minimal non-vacuous fragment of the Tate
    factorisation `ρ_tot([X]) = (ρ_v([X]))_v` of
    `def:adelic-substrate`.

    Ref: [kontsevich1995], [denef-loeser2001], [tate1967]. -/
class MotivicSubstrate
    (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat]
    (Target : Place → Type*) [∀ v, CommRing (Target v)] where
  /-- The Lefschetz motive `𝕃 = [𝔸¹] ∈ K₀(Var_k)`. -/
  lefschetz : K0
  /-- Canonical inclusion `K₀ → 𝓜̂` of the Grothendieck ring into
      the dimension-completed localization. -/
  inclusion : K0 →+* Mhat
  /-- `𝕃` is invertible in `𝓜̂`. -/
  lefschetz_invertible : IsUnit (inclusion lefschetz)
  /-- The realization functor at place `v`, taking values in the
      target ring `Target v`. -/
  realize : (v : Place) → Mhat →+* Target v
  /-- **Substrate axiom (archimedean non-degeneracy).**  The
      archimedean realization target is nontrivial.

      Ref: [tate1967]. -/
  archimedean_nontrivial : Nontrivial (Target Place.infty)
  /-- **Substrate axiom (non-archimedean non-degeneracy).**  At
      least one finite place `p` has a non-trivial realization
      target.

      Ref: [tate1967]. -/
  nonarchimedean_nontrivial :
    ∃ p : Nat.Primes, Nontrivial (Target (Place.finite p))

/-- At every place `v`, the realized Lefschetz class `realize v (inclusion lefschetz)`
is a unit in the target ring `Target v`. -/
theorem realize_lefschetz_isUnit
    {K0 Mhat : Type*} [CommRing K0] [CommRing Mhat]
    {Target : Place → Type*} [∀ v, CommRing (Target v)]
    [ms : MotivicSubstrate K0 Mhat Target] (v : Place) :
    IsUnit (ms.realize v (ms.inclusion ms.lefschetz)) := by
  have hu : IsUnit (ms.inclusion ms.lefschetz) := ms.lefschetz_invertible
  exact hu.map (ms.realize v)

end QOU.AlgebraicSubstrate
