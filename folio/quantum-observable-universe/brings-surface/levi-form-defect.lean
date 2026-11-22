import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Data.Set.Basic


/-!
# QOU.AlgebraicSubstrate.LeviFormDefect — Matter as Frobenius failure

The Levi form measures the non-degeneracy of the contact structure at
a point in the spectral fiber. When non-zero, the Frobenius form cannot
extend smoothly, creating a topological defect — the matter locus.

LaTeX label: `def:levi-form-defect`

## 2026-09-03 — the matter locus was named but never defined

`matter_locus_nonempty` was `:= d.nondeg`, at that field's type verbatim:

    theorem matter_locus_nonempty (d : LeviFormDefect R) :
        ∃ (x y : d.carrier), d.leviForm x y ≠ 0 := d.nondeg

This block is a **`definition`** (`def:levi-form-defect`, `lean.ref` pointing
at the structure), so a field carrying its own axiom is the accessor idiom
and not by itself the AGENTS.md §3b-cond item-5 failure. What made this one a
defect is the **name**: there was no matter locus in the file. `Sing(λ)` — the
object the `.md` is about — existed only as the word "matter_locus" in a
theorem whose statement was an existential over the structure's own field, so
"the matter locus is nonempty" restated "the witness I was given exists".

**Fixed** by defining the locus, `matterLocus = {(x, y) | ℒ(x, y) ≠ 0}`, and
proving things about *it*:

* `matter_locus_nonempty` now concludes `d.matterLocus.Nonempty` — still one
  step from `nondeg`, but a step about a defined set rather than a
  restatement of the field's type.
* `zero_left_notMem_matterLocus` / `zero_right_notMem_matterLocus` — the
  locus misses the zero section, which is forced by bilinearity and is not
  assumed anywhere.
* `matterLocus_ne_univ` and `matterLocus_proper` — the locus is a **proper,
  non-empty** subset. That is what makes it a defect *locus* rather than
  either the empty set or everything, and it is the first statement in this
  file that neither `nondeg` nor any other field contains.

## What the `.md` claims and this file does not encode

1. **The implication that gives the definition its content** — *"when
   `ℒ_p ≠ 0`, the Frobenius form `λ` cannot extend smoothly through `p`"*.
   There is no `λ`, no smoothness and no extension anywhere here, so the file
   names the defect locus without connecting it to the Frobenius failure it
   is supposed to measure. This is the substance of the block.
2. **The bidegree split.** The `.md` has
   `ℒ_p : T_p^{1,0}A × T_p^{0,1}A → ℂ`; the Lean has a bilinear form on a
   single `R`-module in both arguments. The structure's own comment calls
   this "abstracting", and the abstraction drops the conjugate splitting that
   makes a Levi form a Levi form.
3. **`Sing(λ) ⊂ Spec(A)`.** The locus here lives in `carrier × carrier`, not
   in a spectrum; there is no `Spec` in the file.

## References

- [leitner2026] Ch 8 §2, The unit particle as a cohomological defect
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

-- §7d U2 + U3. `LeviFormDefect` carries a `Type*`-valued field, so it is
-- universe-carrying: any signature mentioning it in two places elaborates each
-- with a fresh metavariable, and every theorem below that both takes a `d` and
-- says something about `d.matterLocus` died on `max ?u ?v =?= u_2`.
--
-- U2 alone is not enough here. Pinning `carrier : Type v` was tried first and
-- changed nothing, because `v` then appears nowhere in a theorem's *signature*
-- and is re-metavariable'd per declaration. What fixes it is U3: name `R`'s
-- universe as well (`R : Type w`) and TIE both at each use site,
-- `LeviFormDefect.{v, w} R`.
--
-- Nor was it the `Prod`. `((0, 0) : d.carrier × d.carrier)` as a single
-- ascription looked like the fix and is not: with the universes tied, the
-- per-component form compiles too, and it was reverted rather than left in
-- carrying a comment claiming credit.
universe u v w

variable {C : Type u} [CategoryTheory.Category C]

/-- The Levi form defect structure: captures the failure of the
    Frobenius form at a point in the spectral fiber.

    At a point p, the Levi form ℒ_p measures non-degeneracy of the
    contact structure. The matter locus is the set of points where
    ℒ_p ≠ 0. -/
structure LeviFormDefect (R : Type w) [CommRing R] where
  /-- The ambient algebra (spectral fiber).  Pinned to `Type v` per §7d U2. -/
  carrier : Type v
  /-- Additive structure on the carrier (presupposed by the module structure). -/
  [addCommInst : AddCommMonoid carrier]
  /-- Module structure on the carrier. -/
  [modulInst : Module R carrier]
  /-- The Levi form as a bilinear map (abstracting T^{1,0} × T^{0,1} → k). -/
  leviForm : carrier →ₗ[R] carrier →ₗ[R] R
  /-- Non-degeneracy: there exists a point where the Levi form is nonzero. -/
  -- Ref: [leitner2026] Ch 8 §2
  nondeg : ∃ (x y : carrier), leviForm x y ≠ 0

attribute [instance] LeviFormDefect.addCommInst LeviFormDefect.modulInst

/-- **The matter locus** `Sing(λ)`: the pairs at which the Levi form fails to
    vanish.

    The `.md` defines matter as this set — *"the set of such points forms the
    matter locus `Sing(λ) ⊂ Spec(A)`"* — and until 2026-09-03 it had no
    counterpart in the Lean, so a theorem could name it without any object to
    be about. It lives in `carrier × carrier` rather than in a spectrum; see
    the module docstring. -/
-- Ref: [leitner2026] Ch 8 §2
def LeviFormDefect.matterLocus {R : Type w} [CommRing R]
    (d : LeviFormDefect.{v, w} R) : Set (d.carrier × d.carrier) :=
  {p | d.leviForm p.1 p.2 ≠ 0}

/-- The matter locus is non-empty — one step from `nondeg`, but about the
    defined set rather than a restatement of the field's type. -/
-- Ref: [leitner2026] Ch 8 §2
theorem matter_locus_nonempty {R : Type w} [CommRing R]
    (d : LeviFormDefect.{v, w} R) : d.matterLocus.Nonempty := by
  obtain ⟨x, y, h⟩ := d.nondeg
  exact ⟨(x, y), h⟩

/-- The matter locus misses the zero section in the first argument: bilinearity
    forces `ℒ(0, y) = 0`. Derived, not assumed. -/
theorem zero_left_notMem_matterLocus {R : Type w} [CommRing R]
    (d : LeviFormDefect.{v, w} R) (y : d.carrier) : (0, y) ∉ d.matterLocus := by
  simp [LeviFormDefect.matterLocus]

/-- The matter locus misses the zero section in the second argument. -/
theorem zero_right_notMem_matterLocus {R : Type w} [CommRing R]
    (d : LeviFormDefect.{v, w} R) (x : d.carrier) : (x, 0) ∉ d.matterLocus := by
  simp [LeviFormDefect.matterLocus]

/-- The matter locus is not everything. -/
theorem matterLocus_ne_univ {R : Type w} [CommRing R]
    (d : LeviFormDefect.{v, w} R) : d.matterLocus ≠ Set.univ := by
  intro h
  have hmem : ((0 : d.carrier), (0 : d.carrier)) ∈ d.matterLocus := by
    rw [h]; trivial
  exact zero_left_notMem_matterLocus d 0 hmem

/-- **The matter locus is a proper, non-empty subset.**

    This is the first statement in the file that no field contains: `nondeg`
    supplies the left half, and bilinearity — which nothing assumes about the
    locus — supplies the right. A defect *locus* that were empty or that were
    the whole space would not be a locus, and neither is excluded by the
    structure's fields alone. -/
-- Ref: [leitner2026] Ch 8 §2
theorem matterLocus_proper {R : Type w} [CommRing R]
    (d : LeviFormDefect.{v, w} R) :
    d.matterLocus.Nonempty ∧ d.matterLocus ≠ Set.univ :=
  ⟨matter_locus_nonempty d, matterLocus_ne_univ d⟩

end QOU.AlgebraicSubstrate
