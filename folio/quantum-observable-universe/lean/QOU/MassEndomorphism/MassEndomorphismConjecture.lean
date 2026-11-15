import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.MassEndomorphism.MassEndomorphismConjecture — closed-form NF decomposition

The mass-endomorphism conjecture asserts that the Hecke mass element
Φ_mass(β) ∈ H_n(R, q) admits a closed-form NF decomposition expressible
in terms of:
  - the braid word β,
  - the substrate parameter q,
  - the quantum dilogarithm Φ_q.

**Conditional-class axiomatisation** (AGENTS.md §3b).  This file
encodes the conjecture as a Lean `class` whose fields are the
asserted (but not yet derived) closed-form data.  Downstream
results conditional on the conjecture take this class as an
instance hypothesis.

**Formal-chain version.**  Lives under `lean/QOU/` and is compiled
by `lake build`.  The co-located documentation stub at
`braids-and-knots/mass-endomorphism-conjecture.lean` mirrors this
content; that stub uses `namespace QOU.WedderburnMass` for legacy
reasons.

-- Ref: [manuscript] conj:mass-endomorphism
-- Ref: [manuscript] conj:brane-tower-z-habiro
-- Ref: [manuscript] prop:quantum-dilogarithm-stratified
LaTeX label: `conj:mass-endomorphism`
-/

namespace QOU.MassEndomorphism

/-- **The mass-endomorphism conjecture (axiomatised class).**

    A `MassEndomorphism R β` instance asserts the existence of a
    closed-form NF decomposition for the Hecke mass element
    Φ_mass(β).  The fields encode the closed-form data:
    - `q : R` — the substrate parameter (in any commutative ring R
      ⊇ ℤ[q^±1]).
    - `N : ℕ` — the number of brane levels.
    - `z : Fin N → R` — the algebraic-volume coordinates `z_i`.
    - `tr_transient : R` — `Σ Φ_q(z_i)`.
    - `tr_descended : R` — `tr_M(ρ(β))`.
    - `vol_identity : R` — the value `Vol(K_β)/ℏ_q²`.
    - `vol_eq` — the asserted equality
      `tr_transient = vol_identity − tr_descended`.

    Polymorphic in the ground ring `R` (per
    `QOU.GroundRingAnnotations`, the formal-chain stub keeps `R`
    abstract; instances may specialise to `ℤ[q^±1]` or `ℝ`). -/
-- Ref: [manuscript] conj:mass-endomorphism
class MassEndomorphism (R : Type*) [CommRing R] (β : Type*) where
  q : R
  N : ℕ
  z : Fin N → R
  tr_transient : R
  tr_descended : R
  vol_identity : R
  vol_eq : tr_transient = vol_identity - tr_descended

/-- The full categorical mass at brane-tower-saturation. -/
-- Ref: [manuscript] conj:mass-endomorphism §"Step 2"
def fullMass {R : Type*} [CommRing R] (β : Type*)
    [M : MassEndomorphism R β] : R :=
  M.tr_descended + M.tr_transient

/-- Conditional theorem: under the mass-endomorphism conjecture, the
    full categorical mass equals the volume identity term. -/
-- Ref: [manuscript] conj:mass-endomorphism §"What is known", Step 2
theorem fullMass_eq_volume {R : Type*} [CommRing R] (β : Type*)
    [M : MassEndomorphism R β] :
    fullMass β = M.vol_identity := by
  unfold fullMass
  rw [M.vol_eq]
  ring

/-- The brane-tower partial sum at level N, conditional on a
    `MassEndomorphism` instance.  Mirrors the
    `conj:brane-tower-z-habiro` Cauchy-sequence claim. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro
def braneTowerPartialSum {R : Type*} [CommRing R] (β : Type*)
    [M : MassEndomorphism R β] : R :=
  M.tr_transient

/-- **The all-zero model of `MassEndomorphism`.**  Every field is `0`:
    `q = 0`, `N = 0`, the coordinate family `z` is empty, and all three
    traces vanish, so `vol_eq` is the arithmetic identity `0 = 0 - 0`.
    It encodes no closed-form NF decomposition for any braid; it
    witnesses only that the class is inhabitable.

    **A `def`, not an `instance`, since 2026-08-24.**  It was declared
    `instance` and its docstring called it *"Faithful"*, which it is
    not — it is the zero model.  The defect was its **globality**: both
    carriers are implicit (`{R : Type*} [CommRing R] {β : Type*}`), so
    typeclass resolution supplied it for every commutative ring and
    every braid type.  `fullMass`, `fullMass_eq_volume` and
    `braneTowerPartialSum` each take `[M : MassEndomorphism R β]`; with
    the instance in scope those were not hypotheses, and
    `fullMass_eq_volume` proved `0 = 0` at every instantiation.  That is
    what §3b-tax forbids — *"an unproved primary is honestly represented
    by a content-bearing class with **no** instance; do not fabricate a
    trivial instance to 'close' it."*

    As a `def` the zero model stays available to anyone who wants it
    (`letI := canonical (R := ℤ) (β := β)`) and nothing is discharged
    behind a caller's back.  Blast radius of the demotion, measured:
    **zero** errors — the three in-file uses are binder positions, and
    no module outside `QOU/MassEndomorphism/` mentions the class.

    The instance-free alternative for conditional work is
    `QOU.MassEndomorphism.VolumeBridge`, which ships no instance at all. -/
def canonical {R : Type*} [CommRing R] {β : Type*} : MassEndomorphism R β where
  q := 0
  N := 0
  z := fun _ => 0
  tr_transient := 0
  tr_descended := 0
  vol_identity := 0
  vol_eq := by ring

end QOU.MassEndomorphism
