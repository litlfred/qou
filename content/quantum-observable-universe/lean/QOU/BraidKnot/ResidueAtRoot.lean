import Mathlib.Algebra.Field.Basic

/-!
# QOU.BraidKnot.ResidueAtRoot — Cyclotomic residue at a root of unity

The residue at a primitive `n`-th root of unity `ζ_n` is the
projection of an element of the Habiro completion
`ℤ̂[q]` onto `ℤ[q] / Φ_{n}(q) ≅ ℤ[ζ_n]`.

This is **purely algebraic** — no analytic continuation, no Cauchy
contour, no Archimedean function theory.  The "residue" name is
borrowed from analytic number theory but the operation is the
projection induced by quotienting by a cyclotomic polynomial.

**Formal-chain version.**  Lives under `lean/QOU/` and is compiled
by `lake build`.

**Conditional-class role (AGENTS.md §3b-cond).**  The class
`ResidueAtRoot` below is the class axiomatisation of
`conj:gs-residue-at-root-existence`: an instance supplies the
Habiro-completion cyclotomic projection, whose existence is the
conjectural input.  The proposition `prop:residue-at-root` is stated
*conditionally* on this class (content-block sibling
`mass-theory/residue-at-root.lean`, theorem
`residue_isRingHom_of_residueAtRoot`).

LaTeX label: `conj:gs-residue-at-root-existence` (the class);
consumed conditionally by `prop:residue-at-root`.
-/

namespace QOU.BraidKnot

universe u

/-- **Cyclotomic residue at a root of unity (axiomatised class).**

    A class instance carries:
    * `target n` — the target ring `ℤ[ζ_n] ≅ ℤ[q]/Φ_n(q)`.
    * `project n` — the cyclotomic projection from the Habiro
      completion to the target ring, encoded as a ring
      homomorphism `R →+* target n` (well-definedness is carried
      by the `RingHom` type).

    The conjectural input is the Habiro-completion machinery on
    which `project` depends; concrete instances use the cyclotomic
    quotient ring as the target.  This class is the §3b-cond
    axiomatisation of `conj:gs-residue-at-root-existence`. -/
-- @conjecture: primary
class ResidueAtRoot (R : Type u) [CommRing R] where
  /-- The target ring at a given root index `n`. -/
  target : ℕ → Type u
  [targetRing : ∀ n, CommRing (target n)]
  /-- The cyclotomic projection at index `n`. -/
  project : (n : ℕ) → R →+* target n

attribute [instance] ResidueAtRoot.targetRing

/-- The residue value at a substrate element `x : R` and root index `n`. -/
def residue
    {R : Type u} [CommRing R] [r : ResidueAtRoot R]
    (n : ℕ) (x : R) : r.target n :=
  r.project n x

end QOU.BraidKnot
