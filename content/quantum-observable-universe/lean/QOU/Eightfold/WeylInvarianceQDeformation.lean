import Mathlib.Algebra.GeomSum
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

/-!
# QOU.Eightfold.WeylInvarianceQDeformation — A₂ root datum is q-independent

Bean `qou-d9wj` (T1), epic `qou-8lxd`.

The Drinfeld–Jimbo quantisation replaces the binomial coefficient `2 = C(2,1)`
in the classical Serre relation with the Gaussian binomial `[2]_q = q + q⁻¹`.
The **Cartan matrix entry** `a₁₂ = -1` (which determines the root angle
`cos θ = -1/2`, hence `θ = 120°`) is **not touched** by the q-deformation.

This file proves:

1. `gaussianBinomial2_classical`: at q = 1, [2]_q = 2 (the classical limit).
2. `cartanMatrixAt_const`: the A₂ Cartan datum is constant in q — **true by
   construction, no content on its own** (see its docstring).
3. `qSerre_not_constant`: the Serre coefficient genuinely moves with q
   (witness at q = 2).  This is the half with content.
4. `cartan_fixed_while_qSerre_moves`: the conjunction of 2 and 3 — the "two 2s"
   separation, which is the file's actual claim.
5. `qSerre_neq_cartan_diag`: for (q-1)² ≠ 0, the Gaussian binomial [2]_q differs
   from the diagonal Cartan entry 2.
6. `root_angle_ratio_A2`: the root angle ratio a₁₂/a₁₁ = -1/2 is q-independent,
   stated division-free over ℤ as the cross-multiplied `2·a₁₂ = -a₁₁`.

## Scope — what this file does NOT establish

It does **not** prove that Drinfeld–Jimbo quantisation leaves the root datum
invariant.  That is a theorem of Lusztig/Kashiwara, cited by the chapter and
not formalised here.  What is formalised is the *arithmetic* of the "two 2s"
separation on the A₂ datum.  Anything citing this file as machine-checked
evidence for q-independence of the eightfold classification is over-reading it.

## History

Repaired 2026-08-08: the file was **red on `main`** (two "No goals to be
solved" errors from dead `ring` / `native_decide` after a closing `simp`), and
its headline declaration was `cartanMatrix_A2 = cartanMatrix_A2 := rfl` — a
tautology with unused `q₁ q₂` binders, banned by AGENTS.md §"Strict Lean
Discipline" item 5, yet cited in three places as proving q-independence.
`qSerre_neq_cartan_diag` additionally took its own conclusion as hypothesis.
See `docs/audits/2026-08-08-weyl-invariance-file-repair.md`.

Formalises the key observation from
docs/audits/2026-08-03-eightfold-way-a2-q-deformation-dialog-assessment.md §1.

## Anti-fitting note

Pure algebra. The q-independence of root data under Drinfeld–Jimbo
quantisation is a theorem of Lusztig/Kashiwara, not a physics claim.

## Namespace

Added 2026-08-08 (bean `qou-ref10`).  The file previously declared everything
at the root, which (a) violates AGENTS.md §2 — *all declarations live under the
`QOU` root namespace* — and (b) made every content-block `lean.ref` into this
module name a declaration that does not exist.  The namespace matches the
module path, as in the three sibling files of this directory
(`RowCapObstruction`, `GellMannOkuboIdentity`, `Sym2GateParity`).
-/

namespace QOU.Eightfold.WeylInvarianceQDeformation

-- § 1. Gaussian binomial [2]_q (framed form avoids inverses)

/-- The framed Gaussian binomial: q · [2]_q = q² + 1.
    Working in framed form so the file lives over a generic `CommRing`
    with no inverses and no archimedean input (§7c wall discipline). -/
def gaussianBinomial2Framed (R : Type*) [CommRing R] (q : R) : R :=
  q ^ 2 + 1

/-- At q = 1, the framed Gaussian binomial is 2. -/
theorem gaussianBinomial2_classical (R : Type*) [CommRing R] :
    gaussianBinomial2Framed R 1 = 2 := by
  simp [gaussianBinomial2Framed]; ring

-- § 2. A₂ Cartan matrix (fixed integer data)

/-- The A₂ Cartan matrix: `[[2, -1], [-1, 2]]`. -/
def cartanMatrix_A2 : Matrix (Fin 2) (Fin 2) ℤ :=
  !![2, -1; -1, 2]

/-- The Cartan datum the quantisation functor consumes, presented as a
    `q`-indexed family so that "does not depend on `q`" is a statement one
    can actually write down.  The parameter is deliberately ignored. -/
def cartanMatrixAt {R : Type*} [CommRing R] (_q : R) : Matrix (Fin 2) (Fin 2) ℤ :=
  cartanMatrix_A2

/-- The A₂ Cartan datum is constant in `q`.

**This is true by construction, not a discovery** — `cartanMatrixAt` ignores its
argument, so the statement is `rfl`, and it carries no information on its own.
It is recorded only as the trivial half of the "two 2s" separation; the half
with content is `qSerre_not_constant` below, and the separation itself is
`cartan_fixed_while_qSerre_moves`.

Do **not** cite this lemma as evidence that the substrate's `q₀` cannot reach
the root datum: that is a theorem of Drinfeld–Jimbo quantisation
(Lusztig/Kashiwara), which this file does not formalise. -/
theorem cartanMatrixAt_const {R : Type*} [CommRing R] (q₁ q₂ : R) :
    cartanMatrixAt q₁ = cartanMatrixAt q₂ := rfl

/-- Off-diagonal entry: a₁₂ = -1. -/
theorem cartan_A2_offdiag : cartanMatrix_A2 0 1 = -1 := by decide

/-- Serre exponent: 1 - a₁₂ = 2.  The binomial C(2,1) = 2 that gets
    q-deformed to [2]_q. -/
theorem serre_exponent_A2 : 1 - cartanMatrix_A2 0 1 = 2 := by decide

-- § 3. The "two 2s" are different objects

/-- For `q ≠ 1` — stated as `(q - 1)² ≠ 0`, the honest upstream hypothesis —
the framed Gaussian binomial differs from the framed Cartan diagonal.  The
Cartan entry stays `2`; the Serre coefficient moves.  They are different
mathematical objects.

The hypothesis is genuinely upstream of the conclusion: the proof supplies the
identity `(q² + 1) - 2q = (q - 1)²`.  (An earlier version took `q² + 1 ≠ 2q`
as the hypothesis, which is definitionally the conclusion — it assumed what it
claimed to prove.) -/
theorem qSerre_neq_cartan_diag (R : Type*) [CommRing R] (q : R)
    (hq : (q - 1) ^ 2 ≠ 0) :
    gaussianBinomial2Framed R q ≠ 2 * q := by
  intro h
  apply hq
  have : q ^ 2 + 1 = 2 * q := h
  linear_combination this

/-- The Serre coefficient genuinely **moves** with `q`: it is not a constant
function, witnessed at `q = 2` where the framed binomial is `5` and the framed
Cartan diagonal is `4`.

This is the half of the "two 2s" separation that has content — without it,
`cartanMatrixAt_const` is compatible with both sides being constant, which is
precisely the confusion the file exists to dispel. -/
theorem qSerre_not_constant :
    ∃ q : ℤ, gaussianBinomial2Framed ℤ q ≠ 2 * q :=
  ⟨2, by decide⟩

/-- **The "two 2s" separation.**  The Cartan datum is constant in `q` while the
Serre coefficient is not: they cannot be the same object.  This conjunction —
not either half alone — is the file's actual claim. -/
theorem cartan_fixed_while_qSerre_moves :
    (∀ q₁ q₂ : ℤ, cartanMatrixAt q₁ = cartanMatrixAt q₂)
      ∧ (∃ q : ℤ, gaussianBinomial2Framed ℤ q ≠ 2 * q) :=
  ⟨fun q₁ q₂ => cartanMatrixAt_const q₁ q₂, qSerre_not_constant⟩

/-- At q = 1, the coincidence: [2]₁ = 2·1 = 2 = a₁₁.
    This numerical accident is the source of the confusion. -/
theorem qSerre_eq_cartan_at_classical :
    gaussianBinomial2Framed ℤ 1 = 2 * 1 := by
  simp [gaussianBinomial2Framed]

-- § 4. Root angle is q-independent

/-- The root angle `cos θ = a₁₂/a₁₁ = -1/2`, hence `θ = 120°`.
    Both entries are fixed integers, so the ratio is q-independent.

    §7c: stated **division-free over the Cartan datum's own ring ℤ**, as the
    cross-multiplied identity `2·a₁₂ = -a₁₁`.  This is the R[h] pattern — the
    ratio claim `a₁₂/a₁₁ = -1/2` is recovered from it in any ℚ-algebra by
    dividing through by the unit `a₁₁ = 2`, so nothing is lost by not passing
    to ℚ, and the integrality of the Cartan entries stays visible. -/
theorem root_angle_ratio_A2 :
    2 * cartanMatrix_A2 0 1 = -(cartanMatrix_A2 0 0) := by
  decide

end QOU.Eightfold.WeylInvarianceQDeformation
