import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Algebra.Module.LinearMap.Basic


/-!
# QOU.Torsion.weak_equiv_invariance — Weak equivalence invariance

Physical states (expectation values under the vacuum state τ) are
invariant under weak equivalences between brane levels.

A weak equivalence is a zigzag of coface and codegeneracy maps in
the cosimplicial crossed groupoid. For every observable a ∈ A_∞,
  τ(ιₙ(a|ₙ)) = τ(ιₘ(a|ₘ))
where ιₙ is the canonical embedding of level n into A_∞.

LaTeX label: `prop:weak-equiv-invariance`

## References

- [yekutieli2010] https://doi.org/10.1016/j.aim.2009.12.006
- [leitner2026] §3-lifting-of-quantum-torsion/weak-equiv-invariance
-/

namespace QOU.Torsion

/-- **Weak equivalence between brane levels**.

    A zigzag of coface and codegeneracy maps connecting level `n`
    to level `m` in the cosimplicial crossed groupoid. -/
-- Ref: [yekutieli2010] §3
structure WeakEquivalence (R : Type*) [CommRing R] where
  /-- The algebra at each brane level. -/
  AlgAtLevel : ℕ → Type*
  /-- Each level is an additive abelian group. -/
  [instAddCommGroup : ∀ n, AddCommGroup (AlgAtLevel n)]
  /-- Each level carries a module structure. -/
  [instModule : ∀ n, Module R (AlgAtLevel n)]
  /-- The direct limit algebra A_∞. -/
  DirectLimit : Type*
  /-- The direct limit is an additive abelian group. -/
  [instDLAddCommGroup : AddCommGroup DirectLimit]
  /-- The direct limit carries a module structure. -/
  [instDL : Module R DirectLimit]
  /-- Canonical embedding of level n into A_∞. -/
  embed : ∀ n, AlgAtLevel n →ₗ[R] DirectLimit
  /-- Restriction of an element of A_∞ to level n. -/
  restrict : ∀ n, DirectLimit →ₗ[R] AlgAtLevel n
  /-- Source level. -/
  srcLevel : ℕ
  /-- Target level. -/
  tgtLevel : ℕ
  /-- The zigzag map connecting level n to level m. -/
  zigzag : AlgAtLevel srcLevel →ₗ[R] AlgAtLevel tgtLevel

attribute [instance] WeakEquivalence.instAddCommGroup WeakEquivalence.instModule
attribute [instance] WeakEquivalence.instDLAddCommGroup WeakEquivalence.instDL

/-- **Linear vacuum state**: a linear functional `τ : A_∞ → R`.

    Renamed from `VacuumState` (bean `qou-u87j`). That name is already taken,
    in the same namespace, by a **different** structure:
    `QOU.Torsion.VacuumState` in `lean/QOU/Torsion/BraneTower.lean:66` is the
    real-valued state of `prop:vacuum-state`, carrying `invariant` and
    `extends_haar`. This one is the `R`-linear functional that
    `def:weak-equiv-invariance` needs, over a generic ring and a generic
    module.

    They are not two copies of one declaration that drifted apart — they are
    two concepts that collided on a name, which is the case the mirror-drift
    checker's own limits section warns it cannot distinguish. Making them match
    would merge two different things; renaming is the fix. The block that owns
    the bare name is `prop:vacuum-state`, so this one yields it. -/
-- Ref: [leitner2026] §3
structure LinearVacuumState (R : Type*) [CommRing R] (DL : Type*) [AddCommGroup DL]
    [Module R DL] where
  /-- The vacuum state as a linear functional. -/
  tau : DL →ₗ[R] R

/-- **Weak equivalence invariance**: the expectation value
    `τ(ιₙ(a|ₙ))` is independent of the brane level `n`.

    This ensures that physical predictions do not depend on which
    level of the brane tower we compute them at. -/
-- Ref: [yekutieli2010] §3, [leitner2026] §3
structure WeakEquivInvariance (R : Type*) [CommRing R] where
  /-- The weak equivalence data. -/
  weq : WeakEquivalence R
  /-- The vacuum state on A_∞. -/
  vac : LinearVacuumState R weq.DirectLimit
  /-- **Invariance**: for all elements a ∈ A_∞,
      `τ(ιₙ(a|ₙ)) = τ(ιₘ(a|ₘ))`. -/
  invariance : ∀ (a : weq.DirectLimit),
    vac.tau (weq.embed weq.srcLevel (weq.restrict weq.srcLevel a)) =
    vac.tau (weq.embed weq.tgtLevel (weq.restrict weq.tgtLevel a))

/-- Weak equivalence invariance is transitive: if levels n ∼ m and
    m ∼ k share the same direct limit algebra and vacuum state,
    then τ at level n equals τ at level k.

    We express this within a single WeakEquivInvariance over three
    levels: srcLevel = n, midLevel = m, tgtLevel = k. -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
theorem weak_equiv_transitive {R : Type*} [CommRing R]
    (weq : WeakEquivalence R)
    (vac : LinearVacuumState R weq.DirectLimit)
    (midLevel : ℕ)
    (h_src_mid : ∀ (a : weq.DirectLimit),
      vac.tau (weq.embed weq.srcLevel (weq.restrict weq.srcLevel a)) =
      vac.tau (weq.embed midLevel (weq.restrict midLevel a)))
    (h_mid_tgt : ∀ (a : weq.DirectLimit),
      vac.tau (weq.embed midLevel (weq.restrict midLevel a)) =
      vac.tau (weq.embed weq.tgtLevel (weq.restrict weq.tgtLevel a))) :
    ∀ (a : weq.DirectLimit),
      vac.tau (weq.embed weq.srcLevel (weq.restrict weq.srcLevel a)) =
      vac.tau (weq.embed weq.tgtLevel (weq.restrict weq.tgtLevel a)) :=
  fun a => (h_src_mid a).trans (h_mid_tgt a)

end QOU.Torsion
