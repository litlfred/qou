import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Set.Finite.Basic
import QOU.Common.MagicNumbers


/-!
# Categorical neutrality of saturated shells (Lean class)

The conjecture asserts that the categorical mass endomorphism `Φ_n`
at level `n ∈ {2, 8, 20, 28, 50, 82, 126}` is a fixed point of the
full-twist action on `H_n(q)`. Equivalently, `Φ_n` is supported on
self-conjugate partitions `λ ⊢ n` (those with content-sum zero).

We axiomatise the conjecture as a `class` per AGENTS.md §3b: the
typeclass instance is the conjectural input; downstream results
become conditional theorems parameterised on
`[SaturatedShellConjecture n]`.

-- Ref: [leitner2026] conj:categorical-neutrality-saturated-shells
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
-- Ref: [geckpfeiffer2000] Geck & Pfeiffer, "Characters of Finite Coxeter Groups and Iwahori-Hecke Algebras," LMS Monographs 21, OUP 2000
-- Ref: [mathas1999] Mathas, "Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group," AMS Univ. Lect. Series 15, 1999
-/

namespace QOU.ShellNeutrality

-- The seven magic numbers + Saturated predicate are defined once
-- in `QOU.Common.MagicNumbers` (single source of truth — see PR
-- #501 review). Re-exported here for ergonomic local access.
abbrev magicSet : Finset ℕ := QOU.Common.magicSet
abbrev Saturated (n : ℕ) : Prop := QOU.Common.Saturated n

/-- The mass-endomorphism module at level `n`, abstracted: any type
    with a designated full-twist action and a designated mass
    endomorphism. The conjecture below asks whether the latter is
    fixed by the former at saturated levels.

    Concretely, in the QOU substrate `Endo n` will be instantiated
    as `End (A^⊗n)` in the rigid braided monoidal category `C`, the
    `fullTwist` is the central element `Δ_n²`, and `phi` is the
    global section of the mass functor at level `n`. -/
class MassEndoModule (n : ℕ) where
  /-- The endomorphism algebra at level `n`. -/
  Endo : Type*
  /-- Endomorphism algebras are monoids (composition). -/
  endoMonoid : Monoid Endo
  /-- The image of the full-twist `Δ_n²` in `Endo`. -/
  fullTwist : Endo
  /-- The categorical mass endomorphism `Φ_n`. -/
  phi : Endo

attribute [instance] MassEndoModule.endoMonoid

/-- The conjecture, encoded as a class.

    A `SaturatedShellConjecture n` instance asserts that, at the
    saturated level `n`, the full-twist `Δ_n²` acts trivially on
    `Φ_n` in the endomorphism algebra `Endo n`. The unproved input
    is the existence of the instance; downstream conditional
    theorems are then fully verified by Lean.

    **🛑 Vacuity status (audited 2026-11-20, bean `qou-dx7g`; triage rank 77).**
    As encoded this class does **not** state the conjecture, and no repair is
    available in the corpus.  `Endo`, `fullTwist` and `phi` are instance fields
    of `MassEndoModule`, so the trivial monoid (`Endo := Unit`) satisfies both
    neutrality fields at every magic `n`; even with `Endo := H_n(q)` and the
    genuine central full twist `Δ_n²` (which acts on the block `V_λ` by
    `q^{2κ_λ}`), a free `phi` can be taken to be `0`, or the block idempotent
    of any self-conjugate `λ ⊢ n`, and the class holds.  The claim is about one
    specific element, the categorical mass endomorphism `Φ_n`, and `Φ_n` is not
    defined anywhere in the corpus: `conj:mass-endomorphism-conjecture` is itself
    a conjecture and lists only candidate constructions.  Encoding this
    conjecture therefore needs (i) a definition of `Φ_n` in a concrete Hecke
    algebra, and (ii) `fullTwist` as the genuine `Δ_n²` there; both fields would
    then become definitions and only `neutrality_left/right` would remain as
    the conjectural content.  Until then `Endo`, `fullTwist` and `phi` are
    free, and the conditional theorems below hold for any monoid element fixed
    by another. -/
-- Ref: [leitner2026] conj:categorical-neutrality-saturated-shells
class SaturatedShellConjecture (n : ℕ) extends MassEndoModule n where
  /-- The level `n` lies in the magic set (precondition). -/
  saturated : Saturated n
  /-- The asserted neutrality: full-twist commutes-and-fixes `Φ_n`
      from the left. -/
  neutrality_left : fullTwist * phi = phi
  /-- The asserted neutrality: full-twist commutes-and-fixes `Φ_n`
      from the right. -/
  neutrality_right : phi * fullTwist = phi

/-- Conditional theorem: under the saturated-shell conjecture, the
    full-twist commutes with `Φ_n`. -/
-- Ref: [leitner2026] conj:categorical-neutrality-saturated-shells §"Statement"
theorem fullTwist_commutes
    (n : ℕ) [c : SaturatedShellConjecture n] :
    c.fullTwist * c.phi = c.phi * c.fullTwist := by
  rw [c.neutrality_left, c.neutrality_right]

/-- Conditional theorem: at a saturated level, two applications of
    the full-twist still leave `Φ_n` invariant — the discrete
    `ℤ`-action of the full-twist factors through the trivial
    representation on `Φ_n`. -/
-- Ref: [leitner2026] conj:categorical-neutrality-saturated-shells §"Statement"
theorem fullTwist_iter_neutral
    (n : ℕ) [c : SaturatedShellConjecture n] (k : ℕ) :
    c.fullTwist ^ k * c.phi = c.phi := by
  induction k with
  | zero => simp
  | succ k ih =>
      rw [pow_succ, mul_assoc, c.neutrality_left]
      exact ih

/-- The right-iteration analogue of `fullTwist_iter_neutral`:
    `Φ_n · fullTwist^k = Φ_n` for any `k : ℕ`. Proves directly by
    induction using `neutrality_right`, mirroring the left-side
    proof. -/
-- Ref: [leitner2026] conj:categorical-neutrality-saturated-shells §"Statement"
theorem fullTwist_iter_neutral_right
    (n : ℕ) [c : SaturatedShellConjecture n] (k : ℕ) :
    c.phi * c.fullTwist ^ k = c.phi := by
  induction k with
  | zero => simp
  | succ k ih =>
      -- pow_succ: fullTwist^{k+1} = fullTwist^k * fullTwist
      rw [pow_succ, ← mul_assoc]
      -- now: (phi * fullTwist^k) * fullTwist = phi
      rw [ih, c.neutrality_right]

/-- Two-sided iteration: `fullTwist^a · Φ_n · fullTwist^b = Φ_n`
    for any `a, b : ℕ` at a saturated level. The full-twist's
    discrete `ℕ × ℕ`-monoid action on `Φ_n` factors through the
    trivial representation under the saturated-shell conjecture. -/
-- Ref: [leitner2026] conj:categorical-neutrality-saturated-shells §"Statement"
theorem fullTwist_iter_two_sided_neutral
    (n : ℕ) [c : SaturatedShellConjecture n] (a b : ℕ) :
    c.fullTwist ^ a * c.phi * c.fullTwist ^ b = c.phi := by
  -- Collapse via composition of left- and right-iteration:
  -- `(fullTwist^a · phi) · fullTwist^b
  --    = phi · fullTwist^b           (by left-iter)
  --    = phi                          (by right-iter)
  have hL : c.fullTwist ^ a * c.phi = c.phi := fullTwist_iter_neutral n a
  have hR : c.phi * c.fullTwist ^ b = c.phi := fullTwist_iter_neutral_right n b
  calc
    c.fullTwist ^ a * c.phi * c.fullTwist ^ b
        = c.phi * c.fullTwist ^ b := by rw [hL]
    _ = c.phi := hR

end QOU.ShellNeutrality
