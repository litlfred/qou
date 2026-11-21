import QOU.Basic
import QOU.Glossary
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic


/-!
# QOU.CategoricalAction

Extracted from folio/quantum-observable-universe/lean/ for content-block co-location.
Source: folio/quantum-observable-universe/lean/QOU/CategoricalAction.lean (monolithic).
That file no longer exists — the library was split, and `CategoricalAction` now lives at
  folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/GaugeTheory.lean
-/

-- Pre-Archimedean stub: this declaration lives in a rigid monoidal category
-- with abstract ground ring `R`.  Real / Analysis / Topology / Manifold /
-- InnerProductSpace imports were dead-weight (the body uses only
-- CategoryTheory morphisms) and were removed to make the pre-Arch ground-ring
-- discipline visible (cf. QOU.GroundRingAnnotations and audit
-- docs/audits/2026-05-03-pre-archimedean-proof-audit.md §1).

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Categorical connection** on a Frobenius–Hopf object.
    LaTeX: `\label{def:categorical-connection}` -/
structure CategoricalConnection (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The object of 1-forms `Ω¹` in `C`. -/
  Omega1 : C
  /-- The connection morphism `∇ : A → A ⊗ Ω¹`. -/
  nabla : fh.obj ⟶ (fh.obj ⊗ Omega1)
  /-- The Leibniz rule RHS. -/
  leibniz_rhs : (fh.obj ⊗ fh.obj) ⟶ (fh.obj ⊗ Omega1)
  /-- **Leibniz rule**: `∇ ∘ μ = leibniz_rhs`. -/
  leibniz : fh.mul ≫ nabla = leibniz_rhs

/-- **Categorical action functional** `S_q[∇, λ, ψ]`.

    The `R`-valued functional on a quantum observable universe equipped with
    connection `∇`, Frobenius form `λ`, and state `ψ : 𝟙 → A`:

    ```
    S_q = tr(q · R_λ)          (gravity)
        + λ ∘ tr_A(F_∇ ∧_q ⋆_q F_∇)  (gauge)
        + λ(ψ* · D_∇ ψ)        (matter)
    ```

    LaTeX: `\label{def:categorical-action}`
    Ref: [kock2004] -/
structure CategoricalAction (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The connection on `A` (Definition `def:categorical-connection`). -/
  connection : CategoricalConnection C fh
  /-- The state morphism `ψ : 𝟙 → A`. -/
  state : (𝟙_ C) ⟶ fh.obj
  /-- **Gravity term**: `tr(q · R_λ)`, the Frobenius–Ricci scalar. -/
  gravity : (𝟙_ C) ⟶ (𝟙_ C)
  /-- **Gauge term**: `λ ∘ tr_A(F_∇ ∧_q ⋆_q F_∇)`, the q-Yang–Mills action. -/
  gauge : (𝟙_ C) ⟶ (𝟙_ C)
  /-- **Matter term**: `λ(ψ* · D_∇ ψ)`, the q-Dirac action. -/
  matter : (𝟙_ C) ⟶ (𝟙_ C)

/-! **Variational equations of the categorical action.**

    Given a categorical action `S_q[∇, λ, ψ]`, its critical points satisfy
    three Euler–Lagrange equations obtained by varying each field:
    (1) Vary `λ` → categorical Einstein equation: `R_λ - ½ tr(R_λ) id = T_q`
    (2) Vary `∇` → categorical Yang–Mills equation: `∇ ★_q F + q[F, ★_q F] = J_ψ`
    (3) Vary `ψ` → categorical transport equation: `D_∇ ψ = 0`

    LaTeX: `\label{prop:variational-equations}`
    Ref: [kock2004] -/

/-! The Einstein and Yang–Mills equations are stated and proved in the
    library, conditional on `HasCategoricalEOM`:
    `QOU.variational_einstein` / `QOU.variational_yang_mills` in
    `QOU/QuantumObservableUniverse/GaugeTheory.lean`. The tautologies that
    stood here (`P → P`) shadowed them and asserted nothing; removed. -/

/-- **Categorical transport equation**, as a predicate on the action data:
    the state is critical iff the covariant derivative `D_∇ ψ = 0`, i.e. the
    matter term factors through the unit — `ca.matter = fh.unit ≫ fh.counit`.
    Named (§3b), not asserted: the previous
    `(h_critical : P) : P := h_critical` was self-assuming and stated
    nothing about the action. -/
-- Ref: [leitner2026] §1
def variational_transport {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C)
    (ca : CategoricalAction C fh) : Prop :=
  ca.matter = fh.unit ≫ fh.counit

end QOU
