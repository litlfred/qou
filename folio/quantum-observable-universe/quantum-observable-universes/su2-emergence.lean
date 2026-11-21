import QOU.Basic
import QOU.Glossary
import QOU.QuantumObservableUniverse.Structures
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
-- Supplies `LaurentPolynomial` / `LaurentPolynomial.T` for the `R_q` ground-ring
-- declarations below.  Its absence made this file fail to elaborate with three
-- `unknownIdentifier` errors; nothing caught it, because content-block `.lean`
-- siblings have no CI (workflow_dispatch-only) and no `.qa.json` compile gate.
import Mathlib.Algebra.Polynomial.Laurent


/-!
# QOU.SU2Emergence — Emergence of the gauge group

Given a quantum observable universe (C, A, ω), the gauge group
G_q = Aut⊗(ω) is isomorphic to SU(2) (or SL(2, R) depending on
the signature of the Frobenius pairing).

This is the most depended-upon theorem on the critical path:
spin labels, maximal torus, projective line, and everything
downstream relies on this result.

## References

- [lusztig1993] Introduction to Quantum Groups
- [leitner2026] §1 Theorem: Emergence of SU(2)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

noncomputable section

universe u v

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ

/-- The canonical indeterminate `q` of `R_q`. -/
def q_param : R_q := LaurentPolynomial.T 1

/-- The inverse indeterminate `q⁻¹` of `R_q`. -/
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Rank-1 characterisation** (hypotheses): in a QOU, the fundamental
    object has categorical dimension 2, the volume form forces determinant 1,
    and adjoint vanishing forces the gauge group to be rank 1.

    **Scope warning — only one of the three fields constrains the QOU.**
    The narrative above describes three constraints "that together force
    SU(2)"; the type delivers one:

    * `fund_dim_two` is an arithmetic fact about the *literal*
      `{ twice_j := 1 }` and is discharged by `decide`.  It never mentions
      `qou`, so it does **not** say that this QOU's fundamental object has
      dimension 2 — the intended tie to `qou.fundamentalObj` is missing.
    * `volume_nondeg` is a genuine constraint on `qou.volumeForm`.
    * `adjoint_trivial` carries the default value `qou.adjoint_vanishing`,
      so every QOU satisfies it automatically; it restates a QOU axiom
      rather than adding a hypothesis.

    The encoding gap in `fund_dim_two` is structural, not a typo: tying it
    to `qou.fundamentalObj` needs the spin indexing that `SpinDecomposition`
    supplies, and that is the *conclusion* `su2_emergence` produces — so the
    hypothesis cannot reference it without circularity.  Restructuring is
    tracked as a bean; it is deliberately not done inline, because this is
    the most depended-upon declaration on the critical path.

    Consequently `su2_emergence` should be read as "volume non-degeneracy
    (plus the QOU axioms) yields a spin decomposition", not as a
    three-legged derivation. -/
structure RankOneGaugeData (k : Type*) [Field k] where
  /-- The underlying QOU. -/
  qou : QuantumObservableUniverse.{u, v} k
  /-- The fundamental representation V has categorical dimension 2,
      encoded as: the spin label for V is j = 1/2 (twice_j = 1). -/
  fund_dim_two : ({ twice_j := 1 : SpinLabels }).cat_dim = 2
  /-- Volume constraint: Λ²V → 𝟙 is non-degenerate (epimorphism).

      **No longer a hypothesis** (bean `qou-n1dj`, 2026-08-22).  Condition
      (iii) of `QuantumObservableUniverse` is now the isomorphism
      `volumeIso : exteriorSquare ≅ (𝟙_ C)`, and an isomorphism is epi, so
      this field carries a default value and every QOU satisfies it.

      Read this together with the scope warning above.  `volume_nondeg` was
      the *one* field of the three that constrained the QOU; with it
      discharged, `RankOneGaugeData` adds nothing to
      `QuantumObservableUniverse`.  The content did not disappear — it moved
      upstream into the framework axiom, which is where the corpus states it —
      but a reader told "one of three constrains" should now be told "none of
      the three, because the axiom already does". -/
  volume_nondeg :
    letI := qou.catInst
    letI := qou.monInst
    ∀ (f g : (𝟙_ qou.C) ⟶ (𝟙_ qou.C)),
      qou.volumeIso.hom ≫ f = qou.volumeIso.hom ≫ g → f = g := by
    letI := qou.catInst
    letI := qou.monInst
    intro f g h
    exact (CategoryTheory.cancel_epi qou.volumeIso.hom).mp h
  /-- Adjoint vanishing: Hom(𝟙, Ad(A)) is trivial. -/
  adjoint_trivial :
    letI := qou.catInst
    letI := qou.monInst
    Subsingleton ((𝟙_ qou.C) ⟶ qou.adjointObj) :=
      qou.adjoint_vanishing

/-- **Spin decomposition** in a QOU: the simple objects of `C` are
    indexed by `SpinLabels`, and the fundamental object has spin `1/2`.

    Mirrors the sibling `spin-labels.lean` definition; restated here so
    `su2_emergence` is self-contained (content-sibling `.lean` files
    compile standalone and cannot import one another). -/
structure SpinDecomposition (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The simple object in `C` at spin label `j`. -/
  simpleObj : SpinLabels → C
  /-- The fundamental object `V` corresponds to spin `1/2`. -/
  fundamentalObj : C
  /-- `V = V_{1/2}` (the spin-1/2 representation). -/
  fundamental_is_half : fundamentalObj = simpleObj { twice_j := 1 }
  /-- The adjoint object `Ad(A)` corresponds to spin `1`. -/
  adjointObj : C
  /-- `Ad(A) = V_1` (the spin-1 representation). -/
  adjoint_is_one : adjointObj = simpleObj { twice_j := 2 }

-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
-- Ref: [deligne1990] Catégories tannakiennes — see folio/schema/references.ts
/-- **The former `su2_emergence` axiom asserted nothing, and is now a
    one-line theorem.**

    It stood as

        axiom su2_emergence … :
          ∃ (sd : SpinDecomposition data.qou.C),
            sd.fundamentalObj = data.qou.fundamentalObj

    which is **vacuously true**: `SpinDecomposition` has five fields, of
    which `simpleObj`, `fundamentalObj` and `adjointObj` are free and the
    two remaining are equations satisfiable by taking `simpleObj`
    constant.  The witness below does exactly that, and the whole
    statement closes by `rfl`.

    This is not a false axiom -- it is worse in one respect and better in
    another.  Better: nothing unsound was ever derivable from it.  Worse:
    a false axiom announces itself the moment anyone looks for a
    counterexample, while this one could stand indefinitely, cited as
    Tannaka-Krein reconstruction, asserting only that a record with three
    free fields can be filled in.

    **What the structure does not say.**  The old docstring described the
    consequence as *"simple objects indexed by half-integer spin labels
    with dim = 2j + 1"*.  `SpinDecomposition` carries **no** simplicity
    condition, **no** injectivity of `simpleObj`, and **no** dimension
    field -- so none of that is in the statement.  Encoding it is a
    structure refactor and is deliberately not guessed at here; the
    Tannaka duality and the SL(2) subgroup classification the proof
    sketch needs are genuinely absent from Mathlib, and that gap is
    real.  What was not real is the suggestion that an axiom was
    carrying it.

    LaTeX: `\label{thm:su2-emergence}` -/
theorem su2_emergence {k : Type*} [Field k]
    (data : RankOneGaugeData.{u, v} k) :
    letI := data.qou.catInst
    letI := data.qou.monInst
    ∃ (sd : SpinDecomposition data.qou.C),
      sd.fundamentalObj = data.qou.fundamentalObj := by
  letI := data.qou.catInst
  letI := data.qou.monInst
  exact ⟨{ simpleObj := fun _ => data.qou.fundamentalObj
           fundamentalObj := data.qou.fundamentalObj
           fundamental_is_half := rfl
           adjointObj := data.qou.fundamentalObj
           adjoint_is_one := rfl }, rfl⟩

end

end QOU
