import QOU.Basic
import QOU.BraidKnot.CrystalGraphRealization

/-!
# QOU.BraidKnot.CemeteryGroupEmergence — cemetery group as ker τ (conjecture)

Class axiomatisation of [conj:cemetery-group-emergence]: monotonicity
of the cemetery group `Z_n = ker τ` under crystal extensions.  Once a
crystal path enters `Z_n` it cannot escape, and the corresponding
normal form vanishes under the observation functor `τ`.

The class takes `[CrystalGraphRealization R q]` and `[CemeteryGroup R]`
as upstream inputs.  The `monotone_under_extension` field is the
conjectural content.

LaTeX: `\label{conj:cemetery-group-emergence}`

References:
- Khovanov, M. & Lauda, A. D. (2009). A diagrammatic approach …
- Brundan, J. & Kleshchev, A. (2009). Blocks of cyclotomic Hecke …
-/

namespace QOU.BraidKnot

universe u

/-- **Cemetery-group emergence (conjecture).**

    Encodes monotonicity of the cemetery filter under crystal
    extensions: if a prefix lies in `Z_n`, every continuation also
    lies in `Z_n`, and `τ` annihilates the extended normal form. -/
-- Ref: [khovanovlauda2009] Khovanov & Lauda, "A diagrammatic approach to categorification of quantum groups," Repr. Theory 13 (2009), arXiv:0803.4121
-- Ref: [brundankleshchev2009] Brundan & Kleshchev, "Blocks of cyclotomic Hecke algebras and Khovanov-Lauda algebras," Invent. Math. 178 (2009), arXiv:0808.2032
class CemeteryGroupEmergence (R : Type u) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] where
  /-- Predicate: a crystal node lies in the cemetery group `Z_n`. -/
  inCemetery : C.CrystalNode → Prop
  /-- Image under the observation functor `τ` (graded character) of
      a normal form.  Lives in `R` for definiteness; abstract
      instances may refine this. -/
  tauImage : C.NormalForm → R
  /-- **The conjecture (monotonicity)**: if `nodeOf T` lies in `Z_n`,
      then `τ T = 0`.  Plays the role of `sorry`. -/
  monotone_under_extension : ∀ (T : C.NormalForm),
    inCemetery (C.nodeOf T) → tauImage T = 0

namespace CemeteryGroupEmergence

/-- Unconditional structural corollary: any normal form whose crystal
    node is in the cemetery has `τ`-image zero. -/
-- Ref: [manuscript] braids-and-knots/cemetery-group-emergence
theorem tauImage_eq_zero_of_inCemetery
    {R : Type u} [CommRing R] {q : R}
    [C : CrystalGraphRealization R q] [E : CemeteryGroupEmergence R q]
    (T : C.NormalForm) (h : E.inCemetery (C.nodeOf T)) :
    E.tauImage T = 0 :=
  E.monotone_under_extension T h

/-- **Conditional theorem (kill-switch property).**

    Conditional on `[CemeteryGroupEmergence R q]`: if the crystal
    node of `T` is in the cemetery, then the observation-functor
    image vanishes, *and* the value `R`-multiplied by anything stays
    zero — formalising the "kill switch" pruning property used by
    the GS reduction engine. -/
-- Ref: [manuscript] braids-and-knots/cemetery-group-emergence
theorem killSwitch_zero_mul
    {R : Type u} [CommRing R] {q : R}
    [C : CrystalGraphRealization R q] [E : CemeteryGroupEmergence R q]
    (T : C.NormalForm) (h : E.inCemetery (C.nodeOf T)) (r : R) :
    r * E.tauImage T = 0 := by
  rw [E.monotone_under_extension T h]; ring

/-- **The trivial model — a `def`, not an `instance`, and not "faithful".**

    Its docstring said *"Faithful instance. Carries the explicit research-grade
    conjecture as a sorry."* Neither half was true. There is no `sorry`: it sets
    `tauImage _ := 0`, so `monotone_under_extension` is discharged by `rfl` on
    `0 = 0` and the `inCemetery` hypothesis is never used. The observation
    functor annihilates cemetery nodes here because it annihilates everything.
    A `sorry` would at least be visible to `#print axioms`; this was not.

    `inCemetery v := ∃ T, nodeOf T = v` is the one non-degenerate field, and it
    is the field the conjecture does not turn on: monotonicity is vacuous
    against a `τ` that is identically zero.

    As an unconditional `instance` it made `tauImage_eq_zero_of_inCemetery` and
    `killSwitch_zero_mul` — the kill-switch property the GS reduction engine is
    supposed to prune with — unconditional theorems about the zero map.

    Demoted the same way as `ConfinementGradingCorrespondence.canonical`
    (bean `qou-fngs`). Nothing consumed it: the class has no users outside this
    file.

    **Still open:** `conj:cemetery-group-emergence` — that `Z_n = ker τ` is
    monotone under crystal extension for a `τ` that is not identically zero. -/
def canonical (R : Type u) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] : CemeteryGroupEmergence R q where
  inCemetery v := ∃ T : C.NormalForm, C.nodeOf T = v
  tauImage _ := 0
  -- Ref: [manuscript] conj:cemetery-group-emergence (§3b-cond conjectural class;
  --      discharged here by `tauImage := 0`, not by a `sorry` and not by the conjecture)
  monotone_under_extension _ _ := rfl

end CemeteryGroupEmergence

end QOU.BraidKnot
