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

    Fields:
    * `lefschetz : K0` — the Lefschetz motive `𝕃 = [𝔸¹]`.
    * `inclusion : K0 →+* Mhat` — the canonical map into the
      dimension completion.
    * `lefschetz_invertible` — `𝕃` is a unit in `Mhat`.
    * `realize : (v : Place) → Mhat →+* Target v` — the
      realization functor at each place.

    Substrate axioms (paired place compatibility): the realization
    target is nontrivial at the archimedean place AND at some
    finite place — the minimal non-vacuous fragment of the Tate
    factorisation `ρ_tot([X]) = (ρ_v([X]))_v` of
    `def:adelic-substrate`.  This guarantees the substrate is
    genuinely adelic (supported neither entirely at `∞` nor entirely
    at one finite place) without committing to a specific integral
    subring data.  The full place-compatibility statement (almost-
    integral finite-place components for every motivic class)
    requires auxiliary `Integral : ∀ v, Subring (Target v)` data
    and is supplied as a `sorry`-axiom in concrete instances of
    an extension class.

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
  /-- **Substrate axiom (archimedean non-degeneracy).**

      The archimedean realization target is nontrivial — i.e. the
      substrate has a non-degenerate archimedean shadow.  This is
      the minimal non-vacuous fragment of the Tate factorisation
      `ρ_tot([X]) = (ρ_v([X]))_v` of `def:adelic-substrate`: the
      restricted product over places assembles a non-trivial
      classical-limit object only when the archimedean place
      contributes non-degenerately.

      Note: this is genuinely an axiom, not a consequence of
      `lefschetz_invertible`. A trivial `Target Place.infty` (where
      `0 = 1` in the target ring) admits a perfectly valid `RingHom`
      from `Mhat` regardless of whether `inclusion lefschetz` is a
      unit in `Mhat`; the existence of `realize Place.infty` does
      not force `Target Place.infty` to be nontrivial.

      Ref: [tate1967]. -/
  archimedean_nontrivial : Nontrivial (Target Place.infty)
  /-- **Substrate axiom (non-archimedean non-degeneracy).**

      At least one finite place `p` has a non-trivial realization
      target.  Together with `archimedean_nontrivial`, this is the
      minimal restricted-product condition of `def:adelic-substrate`:
      the substrate is genuinely adelic, supported neither entirely
      at `∞` nor entirely on the archimedean continuum, but spread
      across the archimedean place AND at least one non-archimedean
      place.

      The full place-compatibility statement — that for every
      motivic class `x ∈ Mhat` the family `(realize v x)_v` is a
      finite-support adelic class with almost all finite-place
      components in a designated integral subring — requires the
      auxiliary integral-subring data `Integral : ∀ v, Subring
      (Target v)` and is supplied as a `sorry`-axiom in concrete
      instances of an extension class (AGENTS.md §3b).

      Ref: [tate1967]. -/
  nonarchimedean_nontrivial :
    ∃ p : Nat.Primes, Nontrivial (Target (Place.finite p))

end QOU.AlgebraicSubstrate
