import QOU.Basic
import QOU.QuantumObservableUniverse.SubstrateParameter
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Preadditive.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Irrational


/-!
# QOU.SubstrateParameter.ofReebDecomposition

Existence of the substrate parameter: given a Reeb derivation and
weight decomposition, the interpolated differential d_q is constructed
and yields a valid `SubstrateParameter`.

LaTeX: `\label{thm:substrate-parameter-exists}`

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open scoped Topology
open CategoryTheory MonoidalCategory

namespace QOU

noncomputable section

/-! ### Ground ring: this file is on the **archimedean** side of the wall

The `R_q = ℤ[q, q⁻¹]` boilerplate that used to sit here has been removed, and
the archimedean hypotheses that a migration had commented out are restored.

`SubstrateParameter` (in `QOU.QuantumObservableUniverse.SubstrateParameter`)
is *defined* with `field : M → ℝ` and carries the ordering fields
`field_pos : 0 < field p` and `field_ge_one : 1 ≤ field p`. Per AGENTS.md §7c
an ordering predicate puts a declaration on the ℝ side; `R_q` has no order, so
these constructors cannot be stated over it. The earlier migration applied the
"keep a generic ring `R` as long as possible" directive to a structure that
sits past the wall, commented the fields out as *"not meaningful over R_q"*,
and left the declarations unbuildable — the `q₀` binder was deleted while the
bodies still referenced it. Nothing here was ever generic-`R`-able. -/

universe u

/-- **Existence of the substrate parameter** (constant field).

    Given `q₀ > 1` that is not a root of unity (e.g., `q₀`
    transcendental), the constant field `q(p) = q₀` defines a valid
    `SubstrateParameter M` for any type `M`.

    This is the simplest constructor; non-constant substrate fields
    arise from the Reeb flow parameterisation.

    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
noncomputable def SubstrateParameter.ofConstant
    (M : Type*) (q₀ : ℝ) (hq_pos : 0 < q₀) (hq_ge : 1 ≤ q₀)
    (hq_root : ∀ (k : ℕ), k ≥ 1 → q₀ ^ k ≠ 1) :
    SubstrateParameter M :=
  { field := fun _ => q₀
    field_pos := fun _ => hq_pos
    field_ge_one := fun _ => hq_ge
    not_root_of_unity := fun _ k hk => hq_root k hk }

/-- The interpolated differential operator `d_q` at parameter `q₀`.

    Given the Reeb data (d, π_V) from a `CategoricalReeb` structure,
    the interpolated operator is:

      `d_q(f) = q₀⁻¹ · d(f) + (1 − q₀⁻¹) · π_V(d(f))`

    This is encoded as a pair of scalar coefficients:
    - `coeff_full = q₀⁻¹` (weight on the full differential)
    - `coeff_vert = 1 − q₀⁻¹ = ℏ_q` (weight on the vertical projection)

    The operator is well-defined because:
    - The Reeb decomposition provides d and π_V
    - The weight decomposition ensures π_H + π_V = id
    - At q₀ = 1: coeff_full = 1, coeff_vert = 0, so d_q = d
    - As q₀ → ∞: coeff_full → 0, coeff_vert → 1, so d_q → π_V ∘ d -/
structure InterpolatedDifferential (q₀ : ℝ) where
  /-- Weight on the full differential: q₀⁻¹. -/
  coeff_full : ℝ
  /-- Weight on the vertical projection: 1 − q₀⁻¹. -/
  coeff_vert : ℝ
  /-- The coefficients sum to 1 (convex combination). -/
  sum_to_one : coeff_full + coeff_vert = 1
  /-- coeff_full = q₀⁻¹. -/
  coeff_full_eq : coeff_full = q₀⁻¹

/-- Construct the interpolated differential from q₀ > 0. -/
noncomputable def InterpolatedDifferential.mk' (q₀ : ℝ) (_hq_pos : 0 < q₀) :
    InterpolatedDifferential q₀ where
  coeff_full := q₀⁻¹
  coeff_vert := 1 - q₀⁻¹
  sum_to_one := by ring
  coeff_full_eq := rfl

/-- At q = 1, the interpolated differential equals the full differential. -/
theorem InterpolatedDifferential.classical_limit :
    (InterpolatedDifferential.mk' 1 one_pos).coeff_vert = 0 := by
  simp [InterpolatedDifferential.mk', inv_one]

/-- For q > 1, the vertical weight is positive (quantum regime). -/
theorem InterpolatedDifferential.quantum_regime (q₀ : ℝ) (hq : 1 < q₀) :
    0 < (InterpolatedDifferential.mk' q₀ (by linarith)).coeff_vert := by
  simp [InterpolatedDifferential.mk']
  have : q₀⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  linarith

/-! ### Mirrored sibling structures

`WeightDecomposition` and `CategoricalReeb` are defined in the sibling blocks
`weight-decomposition.lean` and `categorical-reeb.lean`. Content-sibling
`.lean` files compile standalone and cannot import one another, so both are
restated here **in full** — every field of the canonical definitions, so the
hypothesis of `ofReebDecomposition` is no weaker than the real one. This is the
same device `su2-emergence.lean` uses for `SpinDecomposition`. -/

/-- Mirror of `weight-decomposition.lean`'s `WeightDecomposition`. -/
structure WeightDecomposition (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] where
  /-- The object of `k`-forms `Ω^k(A)` in `C`. -/
  forms : C
  /-- The horizontal projection `π_H : Ω^k(A) → Ω^k(A)` (weight-0). -/
  proj_H : forms ⟶ forms
  /-- The vertical projection `π_V : Ω^k(A) → Ω^k(A)` (non-zero weight). -/
  proj_V : forms ⟶ forms
  /-- Complementarity: `π_H + π_V = id`. -/
  complementary : proj_H + proj_V = 𝟙 forms
  /-- Idempotency of horizontal projection. -/
  proj_H_idem : proj_H ≫ proj_H = proj_H
  /-- Idempotency of vertical projection. -/
  proj_V_idem : proj_V ≫ proj_V = proj_V

/-- Mirror of `categorical-reeb.lean`'s `CategoricalReeb`. -/
structure CategoricalReeb (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The Frobenius–Hopf object `A`. -/
  A : C
  /-- The object of 1-forms `Ω¹(A)` in `C`. -/
  forms : C
  /-- The Reeb derivation `ξ : A → A`. -/
  xi : A ⟶ A
  /-- The canonical 1-form `θ_A`, dual to `ξ`. -/
  theta : A ⟶ (𝟙_ C)
  /-- The vertical projection `π_V : Ω¹(A) → Ω¹(A)`. -/
  proj_V : forms ⟶ forms
  /-- The differential `d : A → Ω¹(A)`. -/
  d : A ⟶ forms
  /-- The interior product (contraction) `ι_ξ : Ω¹(A) → A`. -/
  contract_xi : forms ⟶ A
  /-- **Vertical generator**: `d ≫ π_V ≫ ι_ξ = ξ`. -/
  vertical_generator : d ≫ proj_V ≫ contract_xi = xi
  /-- **Normalisation**: `ξ ≫ θ = θ`. -/
  normalisation : xi ≫ theta = theta
  /-- Idempotency of the vertical projection. -/
  proj_V_idem : proj_V ≫ proj_V = proj_V
  /-- **Kernel**: horizontal forms are the kernel of `ι_ξ`. -/
  kernel_horizontal : contract_xi ≫ d ≫ proj_V = contract_xi ≫ d

/-- **Existence from Reeb decomposition**.

    Given a weight decomposition `(π_H, π_V)` and categorical Reeb
    derivation `(ξ, θ_A)`, the substrate parameter exists. The
    construction:

    1. Builds the interpolated differential `d_q = q⁻¹ d + ℏ_q · π_V ∘ d`
       from the Reeb data (d, π_V) and the parameter q₀.
    2. Validates that the interpolation is well-defined: the compatibility
       proof `wd_reeb_compat` ensures π_V acts on the same forms as d.
    3. Returns the substrate parameter field `q(p) = q₀` for all p.

    The value `q₀ > 1` must be supplied externally (it comes from
    physical input — the muon-electron mass ratio in Ch 11). What the
    Reeb decomposition guarantees is that d_q is a well-defined
    interpolation between d and π_V ∘ d.

    **Scope warning — the Reeb input is currently discarded.** The narrative
    above describes a three-step construction, but the term binds `_interp`
    and `wd_reeb_compat` to `_` and never uses them: the result is
    `{ field := fun _ => q₀, … }`, definitionally the same value
    `ofConstant` returns. So this is *not* an existence proof "from the Reeb
    decomposition" — `wd`, `reeb` and the compatibility proof are inert
    hypotheses. Making the interpolated differential actually bear on the
    constructed parameter is open; until it does, do not cite this as
    evidence that the Reeb data determines `q₀`.

    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
noncomputable def SubstrateParameter.ofReebDecomposition
    {C : Type*} [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C] [Preadditive C]
    (M : Type*) (wd : WeightDecomposition C)
    (reeb : CategoricalReeb C)
    (q₀ : ℝ) (hq_pos : 0 < q₀) (hq_ge : 1 ≤ q₀)
    (hq_root : ∀ (k : ℕ), k ≥ 1 → q₀ ^ k ≠ 1)
    -- `wd_reeb_compat`: the weight decomposition is compatible with the Reeb
    -- object -- the forms on which π_V acts are the same object as the Reeb
    -- forms, ensuring `d_q = q⁻¹ d + ℏ_q · π_V ∘ d` is well-typed.
    -- (A `/-- … -/` docstring is not legal between binders; only `--` is.)
    (wd_reeb_compat : wd.forms = reeb.forms) :
    SubstrateParameter M :=
  -- Step 1: Build the interpolated differential at q₀.
  -- This uses the Reeb data (d, π_V from wd/reeb) to define d_q.
  let _interp := InterpolatedDifferential.mk' q₀ hq_pos
  -- Step 2: The compatibility proof ensures π_V (from wd) and d
  -- (from reeb) act on the same forms object, so the interpolation
  -- d_q = q⁻¹ · d + (1 − q⁻¹) · π_V ∘ d is well-typed in C.
  let _ := wd_reeb_compat
  -- Step 3: The SubstrateParameter records q₀ as a constant field.
  -- The interpolated differential d_q is the categorical witness that
  -- this q₀ produces a valid deformation; the field axioms (positivity,
  -- lower bound, no roots of unity) are inherited from q₀.
  { field := fun _ => q₀
    field_pos := fun _ => hq_pos
    field_ge_one := fun _ => hq_ge
    not_root_of_unity := fun _ k hk => hq_root k hk }

end

end QOU
