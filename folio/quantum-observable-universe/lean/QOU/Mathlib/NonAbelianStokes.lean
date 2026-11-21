import Mathlib.Algebra.Group.Basic
import Mathlib.Data.Real.Basic
import QOU.Mathlib.LieValuedForms

/-!
# QOU.Mathlib.NonAbelianStokes — Yekutieli's non-abelian Stokes

The QOU substrate's GB-filtration argument relies on Yekutieli (2015),
*Nonabelian Multiplicative Integration on Surfaces* (World Scientific,
DOI 10.1142/9165).  This file states that theorem as a §3b-cond class
**over concrete Lie-algebra-valued forms**.

## What is concrete (definitions and proved lemmas, no hypotheses)

The forms, the connection calculus and the boundary of a 2-cell are
Mathlib objects, taken from `QOU.Mathlib.LieValuedForms` (bean `qou-ghc6`):

* `LieValuedOneForm E 𝔤` / `LieValuedTwoForm E 𝔤` are **abbreviations** for
  `LieValuedForms.OneForm E 𝔤 = E → E [⋀^Fin 1]→L[ℝ] 𝔤` and
  `LieValuedForms.TwoForm E 𝔤` — Mathlib differential forms on a real normed
  space `E` with values in a normed space `𝔤`.  The Lie bracket is a
  `LieValuedForms.ContinuousLieBracket 𝔤` (a continuous bilinear bracket, which
  `ContinuousLieBracket.toLieAlgebra` shows is a genuine Lie algebra).
* The curvature `F_α = dα + ½[α ∧ α]` (`LieValuedForms.curvature`, built from
  Mathlib's `extDeriv`) and the covariant exterior derivative
  `d_α β = dβ + [α ∧ β]` (`LieValuedForms.covExtDeriv`).  These were class
  **fields** (`covariantD`) before; they are now definitions.
* `cellBoundary σ` — the boundary loop of a 2-cell `σ : ℝ → ℝ → E`
  (parametrised on `[0, 1]²`), traversed on `[0, 4]`.  Also a former field
  (`boundary`), now a definition; `cellBoundary_closed` proves the loop closes.
* `piecewiseAffineLineIntegral` — the finite-slice ordered product.

## What is still assumed (the §3b-cond class `NonAbelianStokes E 𝔤 G L`)

Mathlib (pinned `f897ebcf`) has **no** path-ordered exponential, holonomy,
parallel transport, multiplicative line or surface integral, and no forms on
**manifolds**.  So the class still carries, as data plus axioms:

1. `lineIntegral` — the multiplicative line integral `MI₁(α; γ) ∈ G`;
2. `surfaceIntegral` — the multiplicative surface integral `MI₂(α, β; σ) ∈ G`;
3. `slice` — the finite generator decomposition of `MI₁(α; γ)`;
4. `stokes` — **Yekutieli-Stokes** `MI₁(α; ∂σ) = MI₂(α, F_α; σ)`, with `∂σ`
   the concrete `cellBoundary σ` and `F_α` the concrete `curvature L α`;
5. `finite_slice` — `MI₁(α; γ) = piecewiseAffineLineIntegral (slice α γ)`.

Consequences proved from the concrete calculus, not assumed: the abelian
reduction of Stokes to `dα` (`stokes_of_bracket_eq_zero`), the flat-constant
connection case (`stokes_const_flat`), the restatement through `d_α α`
(`stokes_via_covExtDeriv`), and the finite-slice form of Stokes
(`stokes_finite_slice`).

The only model given is the degenerate `punitInstance` (all integrals `1`),
a `def` and not an `instance`.  It shows consistency, not content.

**References**:
- Yekutieli, *Nonabelian Multiplicative Integration on Surfaces*
  (World Scientific 2015), DOI 10.1142/9165.
- [leitner2026] `def:yekutieli-multiplicative-trace`.
-/

namespace QOU.Mathlib.NonAbelianStokes

open QOU.Mathlib.LieValuedForms

universe u

/-! ### Finite-slice (piecewise-affine) multiplicative integral

    Group-level material, independent of the forms: for a path realised as a
    finite sequence of `G`-valued generator-actions, the multiplicative line
    integral is the literal ordered product. -/

/-- **Piecewise-affine line integral**: for a list of generator
    actions `g₁, g₂, …, gₖ : G`, the multiplicative line integral
    is the left-ordered product `g₁ · g₂ · ⋯ · gₖ`.  This is the
    QOU-substrate's finite-slice realisation of `MI₁`. -/
def piecewiseAffineLineIntegral {G : Type u} [Group G]
    (generators : List G) : G :=
  generators.foldl (· * ·) 1

/-- The empty path's line integral is the identity. -/
theorem piecewiseAffineLineIntegral_nil {G : Type u} [Group G] :
    piecewiseAffineLineIntegral ([] : List G) = 1 := rfl

/-- The line integral of a single generator is that generator. -/
theorem piecewiseAffineLineIntegral_singleton {G : Type u} [Group G]
    (g : G) : piecewiseAffineLineIntegral [g] = g := by
  show 1 * g = g
  exact one_mul g

/-- **Helper**: `foldl (· * ·) a` distributes over the base
    multiplication, i.e. `l.foldl (· * ·) a = a * l.foldl
    (· * ·) 1`.  Standard monoid lemma; proved by induction. -/
theorem foldl_mul_distributes {G : Type u} [Monoid G]
    (l : List G) (a : G) :
    l.foldl (· * ·) a = a * l.foldl (· * ·) 1 := by
  induction l generalizing a with
  | nil => simp
  | cons x xs ih =>
    show xs.foldl (· * ·) (a * x) = a * xs.foldl (· * ·) (1 * x)
    rw [one_mul, ih (a * x), ih x, mul_assoc]

/-- **Concatenation rule**: the line integral of a concatenated
    path is the product of the individual integrals. -/
theorem piecewiseAffineLineIntegral_append {G : Type u} [Group G]
    (gs hs : List G) :
    piecewiseAffineLineIntegral (gs ++ hs) =
      piecewiseAffineLineIntegral gs * piecewiseAffineLineIntegral hs := by
  unfold piecewiseAffineLineIntegral
  rw [List.foldl_append, foldl_mul_distributes]

/-- **Inverse-pair closure**: a path followed by its inverse
    integrates to the identity. -/
theorem piecewiseAffineLineIntegral_inverse {G : Type u} [Group G]
    (g : G) : piecewiseAffineLineIntegral [g, g⁻¹] = 1 := by
  show 1 * g * g⁻¹ = 1
  rw [one_mul, mul_inv_cancel]

/-! ### Lie-algebra-valued forms (concrete, from `LieValuedForms`)

    Until 2026-11-21 this file carried its own abstract carriers,
    `structure LieValuedOneForm (M G : Type u) where eval : M → M → G` and a
    3-argument `LieValuedTwoForm`, with no model: the "form" took two points of
    `M` and returned a **group** element, so it was neither linear in a tangent
    vector nor Lie-algebra-valued.  They are replaced by the Mathlib forms of
    `QOU.Mathlib.LieValuedForms` (owner-approved refactor, bean `qou-ghc6`). -/

section Forms

/-- The **boundary loop** of a 2-cell `σ : ℝ → ℝ → E` (the cell being
    `σ` restricted to `[0, 1]²`), traversed counter-clockwise on `[0, 4]`:
    bottom edge, right edge, top edge reversed, left edge reversed.

    This was the `boundary` field of `NonAbelianStokes`, carried because the
    abstract carrier had no 2-cells to take the boundary of. -/
noncomputable def cellBoundary {E : Type*} (σ : ℝ → ℝ → E) : ℝ → E := fun t =>
  if t ≤ 1 then σ t 0
  else if t ≤ 2 then σ 1 (t - 1)
  else if t ≤ 3 then σ (3 - t) 1
  else σ 0 (4 - t)

theorem cellBoundary_zero {E : Type*} (σ : ℝ → ℝ → E) : cellBoundary σ 0 = σ 0 0 := by
  simp [cellBoundary]

theorem cellBoundary_one {E : Type*} (σ : ℝ → ℝ → E) : cellBoundary σ 1 = σ 1 0 := by
  simp [cellBoundary]

theorem cellBoundary_two {E : Type*} (σ : ℝ → ℝ → E) : cellBoundary σ 2 = σ 1 1 := by
  simp only [cellBoundary]; norm_num

theorem cellBoundary_three {E : Type*} (σ : ℝ → ℝ → E) : cellBoundary σ 3 = σ 0 1 := by
  simp only [cellBoundary]; norm_num

theorem cellBoundary_four {E : Type*} (σ : ℝ → ℝ → E) : cellBoundary σ 4 = σ 0 0 := by
  simp only [cellBoundary]; norm_num

/-- The boundary of a 2-cell is a **closed** loop. -/
theorem cellBoundary_closed {E : Type*} (σ : ℝ → ℝ → E) : cellBoundary σ 4 = cellBoundary σ 0 := by
  rw [cellBoundary_four, cellBoundary_zero]


variable {E 𝔤 : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤]

variable (E 𝔤) in
/-- `Ω¹(E; 𝔤)`: a `𝔤`-valued 1-form on the real normed space `E`. -/
abbrev LieValuedOneForm := OneForm E 𝔤

variable (E 𝔤) in
/-- `Ω²(E; 𝔤)`: a `𝔤`-valued 2-form on the real normed space `E`. -/
abbrev LieValuedTwoForm := TwoForm E 𝔤

/-- The **multiplicative line integral** `MI₁(α; γ) ∈ G` of a `𝔤`-valued
    1-form `α` along a path `γ : ℝ → E`.  In the genuine theory it is the limit
    of ordered products of `exp(α_{γ(tᵢ)}(γ'(tᵢ)) Δt)`; Mathlib has no
    path-ordered exponential, so it is data here. -/
structure MultiplicativeLineIntegral (E 𝔤 G : Type*) [NormedAddCommGroup E]
    [NormedSpace ℝ E] [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] where
  /-- The integral-evaluation map. -/
  integrate : LieValuedOneForm E 𝔤 → (ℝ → E) → G

/-- The **multiplicative surface integral** `MI₂(α, β; σ) ∈ G` of a `𝔤`-valued
    2-form `β`, with auxiliary connection 1-form `α`, over a 2-cell `σ`.  Data,
    for the same reason as `MultiplicativeLineIntegral`. -/
structure MultiplicativeSurfaceIntegral (E 𝔤 G : Type*) [NormedAddCommGroup E]
    [NormedSpace ℝ E] [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] where
  /-- The surface-integral-evaluation map. -/
  integrate : LieValuedOneForm E 𝔤 → LieValuedTwoForm E 𝔤 → (ℝ → ℝ → E) → G

/-- **Yekutieli's non-abelian Stokes** as a §3b-cond class, over the concrete
    forms, for a fixed continuous Lie bracket `L` on `𝔤`.

    Only the two multiplicative integrals and the finite slicing are data;
    the boundary (`cellBoundary`) and the curvature (`curvature L`) are
    definitions.  The Stokes field is Yekutieli's
      `MI₁(α; ∂σ) = MI₂(α, F_α; σ)`,  `F_α = dα + ½[α ∧ α]`.

    **Restated 2026-11-21.**  The abstract version read
    `MI₁(α; ∂σ) = MI₂(α, covariantD α β; σ)` for an arbitrary 2-form `β` and a
    `covariantD` that was itself a field.  Over concrete forms that does not
    typecheck as mathematics: the covariant derivative of a 2-form is a 3-form,
    which cannot be integrated over a 2-cell.  The degree-consistent statement,
    and the one Yekutieli proves, puts the curvature of `α` on the right; by
    `stokes_via_covExtDeriv` it is equivalently written through
    `covExtDeriv L α α = d_α α`.

    **`slice` now takes `α`.**  The abstract field was `slice : path → List G`,
    which forced `MI₁(α; γ)` to be the same for every connection `α` — false in
    any model with a non-trivial connection.  The generator actions of the
    finite slicing depend on the connection being integrated. -/
class NonAbelianStokes (E 𝔤 G : Type*) [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] [Group G]
    (L : ContinuousLieBracket 𝔤) where
  /-- The line integral. -/
  lineIntegral : MultiplicativeLineIntegral E 𝔤 G
  /-- The surface integral. -/
  surfaceIntegral : MultiplicativeSurfaceIntegral E 𝔤 G
  /-- The piecewise-affine slicing of `MI₁(α; γ)` into finitely many generator
      actions. -/
  slice : LieValuedOneForm E 𝔤 → (ℝ → E) → List G
  /-- **Yekutieli-Stokes identity**: `MI₁(α; ∂σ) = MI₂(α, F_α; σ)`. -/
  stokes : ∀ (α : LieValuedOneForm E 𝔤) (σ : ℝ → ℝ → E),
    lineIntegral.integrate α (cellBoundary σ)
      = surfaceIntegral.integrate α (curvature L α) σ
  /-- **Finite-slice axiom**: on a piecewise-affine surface the
      multiplicative integral IS the finite generator product. -/
  finite_slice : ∀ (α : LieValuedOneForm E 𝔤) (γ : ℝ → E),
    lineIntegral.integrate α γ = piecewiseAffineLineIntegral (slice α γ)

/-- **Skeleton model** — both multiplicative integrals are constantly `1` and
    every slicing is empty.  It satisfies both equations (by `rfl`), so it shows
    the axioms are consistent and nothing more: in it the Stokes identity
    carries no information about `α` or `F_α`.

    **A `def`, not an `instance`** (since 2026-08-24): as an instance it would
    discharge every `[NonAbelianStokes E 𝔤 G L]` hypothesis behind its author's
    back.  A caller wanting it writes `letI := punitInstance E 𝔤 G L`. -/
def punitInstance (E 𝔤 G : Type*) [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] [Group G]
    (L : ContinuousLieBracket 𝔤) : NonAbelianStokes E 𝔤 G L where
  lineIntegral := { integrate := fun _ _ => 1 }
  surfaceIntegral := { integrate := fun _ _ _ => 1 }
  slice _ _ := []
  stokes _ _ := rfl
  finite_slice _ _ := rfl

variable {G : Type*} [Group G] {L : ContinuousLieBracket 𝔤}

/-- The `finite_slice` field, named as the identification it records. -/
theorem finite_slice_eq_piecewiseAffine [S : NonAbelianStokes E 𝔤 G L]
    (α : LieValuedOneForm E 𝔤) (γ : ℝ → E) :
    S.lineIntegral.integrate α γ = piecewiseAffineLineIntegral (S.slice α γ) :=
  S.finite_slice α γ

/-- **Stokes at finite slice depth**: the ordered generator product along the
    boundary loop equals the surface integral of the curvature. -/
theorem stokes_finite_slice [S : NonAbelianStokes E 𝔤 G L]
    (α : LieValuedOneForm E 𝔤) (σ : ℝ → ℝ → E) :
    piecewiseAffineLineIntegral (S.slice α (cellBoundary σ))
      = S.surfaceIntegral.integrate α (curvature L α) σ := by
  rw [← S.finite_slice, S.stokes]

/-- `F_α = d_α α − ½[α ∧ α]`, from `LieValuedForms.covExtDeriv_self`. -/
theorem curvature_eq_covExtDeriv_sub (L : ContinuousLieBracket 𝔤) (α : LieValuedOneForm E 𝔤) :
    curvature L α = fun x => covExtDeriv L α α x - (1 / 2 : ℝ) • bracketWedge L α α x := by
  funext x
  rw [covExtDeriv_self, add_sub_cancel_right]

/-- **Stokes through the covariant exterior derivative**:
    `MI₁(α; ∂σ) = MI₂(α, d_α α − ½[α ∧ α]; σ)`. -/
theorem stokes_via_covExtDeriv [S : NonAbelianStokes E 𝔤 G L]
    (α : LieValuedOneForm E 𝔤) (σ : ℝ → ℝ → E) :
    S.lineIntegral.integrate α (cellBoundary σ)
      = S.surfaceIntegral.integrate α
          (fun x => covExtDeriv L α α x - (1 / 2 : ℝ) • bracketWedge L α α x) σ := by
  rw [S.stokes, curvature_eq_covExtDeriv_sub]

/-- **Abelian reduction**: for the zero bracket, the Stokes identity has the
    ordinary exterior derivative `dα` on the right
    (`LieValuedForms.curvature_of_bracket_eq_zero`). -/
theorem stokes_of_bracket_eq_zero [S : NonAbelianStokes E 𝔤 G L] (hL : L.bracket = 0)
    (α : LieValuedOneForm E 𝔤) (σ : ℝ → ℝ → E) :
    S.lineIntegral.integrate α (cellBoundary σ)
      = S.surfaceIntegral.integrate α (extDeriv α) σ := by
  rw [S.stokes, curvature_of_bracket_eq_zero L hL]

/-- **Flat constant connection**: if a constant 1-form `A` has all brackets
    `⁅A v, A w⁆ = 0`, its curvature vanishes
    (`LieValuedForms.curvature_const_eq_zero_iff`), so the boundary holonomy is
    the surface integral of the zero 2-form. -/
theorem stokes_const_flat [S : NonAbelianStokes E 𝔤 G L] (A : E [⋀^Fin 1]→L[ℝ] 𝔤)
    (hA : ∀ v w : E, L.bracket (A (fun _ => v)) (A (fun _ => w)) = 0) (σ : ℝ → ℝ → E) :
    S.lineIntegral.integrate (fun _ => A) (cellBoundary σ)
      = S.surfaceIntegral.integrate (fun _ => A) 0 σ := by
  rw [S.stokes, (curvature_const_eq_zero_iff L A).mpr hA]

end Forms

/-! ### Substrate theorem (S-Yekutieli-finite-slice)

    The substrate claim — at finite slice depth the multiplicative
    integral on a Young-diagram braid surface IS a finite product
    of generator-actions — is stated as
    `yekutieli_finite_slice_substrate`, below the
    `YekutieliFiniteSliceMultTrace` class it quantifies over.

    **Moved + restated 2026-08-21** (vacuity ledger,
    `proof-no-trivial-true` / `exists-true-tautology`).  It stood
    here as `∃ (_ : NonAbelianStokes M G), True :=
    ⟨inferInstance, trivial⟩`, an existence claim that any default
    instance discharges; no existence statement about that class is
    falsifiable, so it was restated against real content. -/

/-! ### Braid-surface multiplicative trace -/

/-- **Braid-surface multiplicative trace**: for a braid word
    expressed as a list of generators, the trace of the closed
    braid is the multiplicative line integral over the closure
    path.  Concretely modelled as a function of the braid word's
    Coxeter length. -/
def braidSurfaceMultTrace {G : Type u} [Group G] (z : G)
    (braidLength : ℕ) : G := z ^ braidLength

/-- Empty braid trace: `tr_M(1) = z⁰ = 1`. -/
theorem braidSurfaceMultTrace_zero {G : Type u} [Group G] (z : G) :
    braidSurfaceMultTrace z 0 = 1 := by
  unfold braidSurfaceMultTrace
  exact pow_zero z

/-- **Markov-axiom-style cocycle**: appending a generator to a
    braid multiplies the Markov trace by `z`. -/
theorem braidSurfaceMultTrace_succ {G : Type u} [Group G] (z : G) (n : ℕ) :
    braidSurfaceMultTrace z (n + 1) = braidSurfaceMultTrace z n * z := by
  unfold braidSurfaceMultTrace
  exact pow_succ z n

/-- **Stokes identity** for the trivial case: on a trivial
    surface (no boundary), both line and surface integrals
    reduce to the identity.  It is the empty-product fact
    `piecewiseAffineLineIntegral [] = 1`, which is the right side of the
    `NonAbelianStokes.finite_slice` field for an empty slicing. -/
theorem stokes_trivial_case {G : Type u} [Group G] :
    piecewiseAffineLineIntegral ([] : List G)
      = (1 : G) := piecewiseAffineLineIntegral_nil

/-- **`YekutieliFiniteSliceMultTrace` class** (substantive
    version): provides the per-braid-word multiplicative trace
    as a class field, plus the Markov-axiom cocycle.  Concrete
    instances at small braid lengths discharge by direct
    computation. -/
class YekutieliFiniteSliceMultTrace (G : Type u) [Group G] (z : G) where
  /-- The trace value for a braid of given Coxeter length. -/
  trace : ℕ → G
  /-- Normalisation: trace at length 0 is the identity. -/
  trace_zero : trace 0 = 1
  /-- Markov-axiom recursion: trace at length `n+1` is `z`
      times the trace at length `n`. -/
  trace_succ : ∀ n, trace (n + 1) = trace n * z

/-- **Canonical instance** of `YekutieliFiniteSliceMultTrace`
    using `braidSurfaceMultTrace` directly.  Concrete; not vacuous. -/
instance YekutieliFiniteSliceMultTrace_canonical (G : Type u) [Group G]
    (z : G) : YekutieliFiniteSliceMultTrace G z where
  trace := braidSurfaceMultTrace z
  trace_zero := braidSurfaceMultTrace_zero z
  trace_succ := braidSurfaceMultTrace_succ z

/-- **Substrate theorem** (S-Yekutieli-finite-slice).  At finite slice
    depth, the multiplicative integral on a Young-diagram braid surface
    IS a finite product of generator-actions: **any** multiplicative
    trace satisfying the two finite-slice axioms is the `n`-fold product
    `z ^ n`.

    Quantified over an arbitrary `Y`, so both class axioms are
    load-bearing (`trace_zero` in the base case, `trace_succ` in the
    step) and a trace differing from `z ^ n` at any `n` would refute it.
    Contrast the canonical instance, for which `trace n = z ^ n` holds
    by `rfl` (`finite_slice_trace_at_depth`) and therefore says nothing:
    the content here is that the axioms *determine* the trace, not that
    one chosen model satisfies them.

    See the "Substrate theorem" note above for what this replaced. -/
-- Ref: [yekutieli2015] yekutieli2015 §3 (Stokes on piecewise-affine surfaces);
--      [leitner2026] def:yekutieli-multiplicative-trace.
theorem yekutieli_finite_slice_substrate {G : Type u} [Group G] {z : G}
    (Y : YekutieliFiniteSliceMultTrace G z) (n : ℕ) :
    Y.trace n = z ^ n := by
  induction n with
  | zero => simpa using Y.trace_zero
  | succ k ih => rw [Y.trace_succ, ih, pow_succ]


/-! ### Lie-valued (additive) Stokes — over the concrete forms

    **Changed 2026-11-21 (bean `qou-ghc6`).**  This section used to define
    its own abstract Lie algebra and forms:

    - `class LieAlgebraStructure 𝔤` (bracket, bilinearity, Jacobi) with
      `bracket_antisym` — replaced by `LieValuedForms.ContinuousLieBracket`,
      which `ContinuousLieBracket.toLieAlgebra` shows is a genuine Mathlib
      `LieAlgebra ℝ 𝔤`; `bracket_antisym` below is now its antisymmetry;
    - `structure LieAlgebraOneForm M 𝔤 := (eval : M → 𝔤)` and
      `LieAlgebraTwoForm M 𝔤 := (eval : M → M → 𝔤)` — replaced by
      `LieValuedOneForm E 𝔤` / `LieValuedTwoForm E 𝔤`;
    - `gaugeCovariantDerivative α β := β + [α, β]` — replaced by
      `LieValuedForms.covExtDeriv L α β = dβ + [α ∧ β]`.  The removed
      definition had **no exterior derivative in it**, so it was not the
      covariant derivative its name and docstring claimed.

    `LieValuedStokes` keeps its shape — a connection `alpha`, a form `beta`,
    two `𝔤`-valued integrals carried as data, and the identity
    `∫_{∂σ} α = ∫_σ d_α β` — with the boundary and `d_α` now concrete.
    `beta` is a **1-form**: `d_α` raises degree by one, so a 2-cell integrand
    `d_α β` needs `β` of degree 1 (the old `β` was a 2-form only because the
    old `d_α` did not raise degree). -/

section LieValued

variable {E 𝔤 : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤]

/-- Antisymmetry of a continuous Lie bracket: `⁅x, y⁆ = -⁅y, x⁆`
    (`ContinuousLieBracket.swap`, derived from `⁅x, x⁆ = 0` and bilinearity). -/
theorem bracket_antisym (L : ContinuousLieBracket 𝔤) (x y : 𝔤) :
    L.bracket x y = -L.bracket y x :=
  L.swap y x

/-- For the zero bracket, `d_α β = dβ` whatever the connection `α`. -/
theorem covExtDeriv_of_bracket_eq_zero (L : ContinuousLieBracket 𝔤) (hL : L.bracket = 0)
    (α β : LieValuedOneForm E 𝔤) : covExtDeriv L α β = extDeriv β := by
  funext x; ext v
  simp [covExtDeriv, bracketWedge_apply, hL]

/-- **Class hypothesis**: a Lie-valued (additive) Stokes framework over the
    concrete forms, for a continuous Lie bracket `L`.  The two `𝔤`-valued
    integrals are data; `cellBoundary` and `covExtDeriv` are definitions. -/
class LieValuedStokes (E 𝔤 : Type*) [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] (L : ContinuousLieBracket 𝔤) where
  /-- The connection 1-form `α`. -/
  alpha : LieValuedOneForm E 𝔤
  /-- The 1-form `β` whose covariant derivative is integrated. -/
  beta : LieValuedOneForm E 𝔤
  /-- Line integral of a 1-form along a path, valued in `𝔤`. -/
  lineIntegral : LieValuedOneForm E 𝔤 → (ℝ → E) → 𝔤
  /-- Surface integral of a 2-form over a 2-cell, valued in `𝔤`. -/
  surfaceIntegral : LieValuedTwoForm E 𝔤 → (ℝ → ℝ → E) → 𝔤
  /-- **Yekutieli-Stokes, infinitesimal form**: `∫_{∂σ} α = ∫_σ d_α β`, with
      `∂σ = cellBoundary σ` and `d_α β = covExtDeriv L alpha beta`. -/
  stokes_identity : ∀ σ : ℝ → ℝ → E,
    lineIntegral alpha (cellBoundary σ)
      = surfaceIntegral (covExtDeriv L alpha beta) σ

/-- **Abelian reduction** of `LieValuedStokes`: for the zero bracket the right
    side is `∫_σ dβ`. -/
theorem LieValuedStokes.stokes_of_bracket_eq_zero {L : ContinuousLieBracket 𝔤}
    [S : LieValuedStokes E 𝔤 L] (hL : L.bracket = 0) (σ : ℝ → ℝ → E) :
    S.lineIntegral S.alpha (cellBoundary σ) = S.surfaceIntegral (extDeriv S.beta) σ := by
  rw [S.stokes_identity, covExtDeriv_of_bracket_eq_zero L hL]

/-- **The zero model**: `α = 0`, `β = 0`, both integrals constantly `0`.

    A `def`, not an `instance`, for the reason recorded at `punitInstance`.  It
    establishes consistency and nothing more: a model in which every integral
    is `0` is no evidence that the axioms constrain anything.  A non-degenerate
    model needs the analytic theory Mathlib lacks; `qou-ewc4` records this. -/
def LieValuedStokes_canonical (E 𝔤 : Type*) [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] (L : ContinuousLieBracket 𝔤) :
    LieValuedStokes E 𝔤 L where
  alpha := 0
  beta := 0
  lineIntegral _ _ := 0
  surfaceIntegral _ _ := 0
  stokes_identity _ := rfl

end LieValued

/-! ### Closed-path holonomy

    A **closed path** in the QOU substrate is a braid word
    whose closure (Markov-trace) yields the multiplicative
    holonomy `tr_M(T_β)`.  The Yekutieli framework asserts
    this equals `z^{ℓ(β)}` for trivial-NF braids. -/

/-- **Closed path holonomy**: for a path expressed as a list
    of generator actions returning to the identity (closed
    loop), the multiplicative line integral equals 1.  This
    is the "trivially closed loop" Yekutieli identity. -/
theorem closedPathHolonomy_via_inverse {G : Type u} [Group G]
    (g : G) :
    piecewiseAffineLineIntegral [g, g⁻¹] = (1 : G) :=
  piecewiseAffineLineIntegral_inverse g

/-- **Generator-pair holonomy**: a closed path `[g, g⁻¹, h, h⁻¹]`
    integrates to 1 (two cancelling pairs). -/
theorem closedPathHolonomy_two_pairs {G : Type u} [Group G]
    (g h : G) :
    piecewiseAffineLineIntegral [g, g⁻¹, h, h⁻¹] = (1 : G) := by
  show ((1 * g) * g⁻¹) * h * h⁻¹ = 1
  rw [one_mul, mul_inv_cancel, one_mul, mul_inv_cancel]

/-- **`braidSurfaceMultTrace` is `z`-multiplicative**: at
    `n = m + k`, the trace decomposes as `z^m * z^k`. -/
theorem braidSurfaceMultTrace_add_split {G : Type u} [Group G]
    (z : G) (m k : ℕ) :
    braidSurfaceMultTrace z (m + k) = braidSurfaceMultTrace z m *
      braidSurfaceMultTrace z k := by
  unfold braidSurfaceMultTrace
  exact pow_add z m k

/-- **Holonomy of identity braid**: `tr_M(1) = z^0 = 1`. -/
theorem braidSurfaceMultTrace_identity {G : Type u} [Group G]
    (z : G) :
    braidSurfaceMultTrace z 0 = (1 : G) := braidSurfaceMultTrace_zero z

/-- **Finite-slice trace explicit formula** at depth k:
    `tr_M(σ^k) = z^k` for any single-generator braid. -/
theorem finite_slice_trace_at_depth {G : Type u} [Group G]
    (z : G) (k : ℕ) :
    braidSurfaceMultTrace z k = z ^ k := rfl

/-- **`YekutieliFiniteSliceMultTrace` instance commutes with
    `braidSurfaceMultTrace_add_split`**: the Markov axiom
    `tr_M(x · σ_n) = z · tr_M(x)` follows by setting `m = ℓ(x)`
    and `k = 1`. -/
theorem yekutieli_markov_axiom_via_split {G : Type u} [Group G]
    (z : G) (m : ℕ) :
    braidSurfaceMultTrace z (m + 1) = braidSurfaceMultTrace z m * z := by
  rw [braidSurfaceMultTrace_add_split z m 1, finite_slice_trace_at_depth]
  show braidSurfaceMultTrace z m * z ^ 1 = braidSurfaceMultTrace z m * z
  rw [pow_one]

/-! ### Path-extension theorems (Tier 2 round 7)

    Additional structural results on the piecewise-affine line
    integral, lifting to the genuine non-abelian holonomy
    properties expected of the Yekutieli framework. -/

/-- **Replicate path holonomy**: integrating the same generator `n`
    times gives `g^n`.  Connects piecewise-affine path integration
    to the natural-number power on the group. -/
theorem piecewiseAffineLineIntegral_replicate {G : Type u} [Group G]
    (g : G) (n : ℕ) :
    piecewiseAffineLineIntegral (List.replicate n g) = g ^ n := by
  induction n with
  | zero => simpa using piecewiseAffineLineIntegral_nil (G := G)
  | succ k ih =>
    show piecewiseAffineLineIntegral (List.replicate (k + 1) g) = g ^ (k + 1)
    rw [List.replicate_succ]
    -- replicate (k+1) g = g :: replicate k g
    -- piecewiseAffineLineIntegral (g :: rs) = g * piecewiseAffineLineIntegral rs
    show ((List.replicate k g).foldl (· * ·) (1 * g)) = g ^ (k + 1)
    -- cast the IH to the unfolded foldl form so the rewrite finds it
    have ih' : (List.replicate k g).foldl (· * ·) 1 = g ^ k := ih
    rw [foldl_mul_distributes, ih', one_mul, ← pow_succ']

/-- **Reverse-and-invert closure**: integrating the reverse list of
    inverses yields the inverse of the original integral.

    For a path `[g₁, g₂, …, gₙ]` with integral `∏ = g₁·g₂·⋯·gₙ`,
    the inverse path `[gₙ⁻¹, …, g₂⁻¹, g₁⁻¹]` integrates to `∏⁻¹`. -/
theorem piecewiseAffineLineIntegral_reverse_inverse_pair {G : Type u} [Group G]
    (g h : G) :
    piecewiseAffineLineIntegral [g, h] *
      piecewiseAffineLineIntegral [h⁻¹, g⁻¹] = (1 : G) := by
  show (1 * g * h) * (1 * h⁻¹ * g⁻¹) = 1
  rw [one_mul, one_mul, ← mul_assoc, mul_assoc g h h⁻¹, mul_inv_cancel, mul_one,
      mul_inv_cancel]

/-- **Concatenation identity-left**: prepending an empty path
    leaves the integral unchanged. -/
theorem piecewiseAffineLineIntegral_nil_append {G : Type u} [Group G]
    (gs : List G) :
    piecewiseAffineLineIntegral ([] ++ gs) =
      piecewiseAffineLineIntegral gs := by
  rw [List.nil_append]

/-- **Concatenation identity-right**: appending an empty path
    leaves the integral unchanged. -/
theorem piecewiseAffineLineIntegral_append_nil {G : Type u} [Group G]
    (gs : List G) :
    piecewiseAffineLineIntegral (gs ++ []) =
      piecewiseAffineLineIntegral gs := by
  rw [List.append_nil]

/-- **Concatenation associativity**: piecewise-affine line integral
    behaves associatively under three-way concatenation. -/
theorem piecewiseAffineLineIntegral_append_assoc {G : Type u} [Group G]
    (gs hs ks : List G) :
    piecewiseAffineLineIntegral ((gs ++ hs) ++ ks) =
      piecewiseAffineLineIntegral (gs ++ (hs ++ ks)) := by
  rw [List.append_assoc]

/-- **Single-step holonomy**: integrating `[g]` is `g`. -/
theorem piecewiseAffineLineIntegral_one_step {G : Type u} [Group G]
    (g : G) : piecewiseAffineLineIntegral [g] = g :=
  piecewiseAffineLineIntegral_singleton g

/-- **Two-step holonomy**: integrating `[g, h]` is `g · h`. -/
theorem piecewiseAffineLineIntegral_two_step {G : Type u} [Group G]
    (g h : G) :
    piecewiseAffineLineIntegral [g, h] = g * h := by
  show 1 * g * h = g * h
  rw [one_mul]

/-- **Three-step holonomy**: integrating `[g, h, k]` is `g · h · k`. -/
theorem piecewiseAffineLineIntegral_three_step {G : Type u} [Group G]
    (g h k : G) :
    piecewiseAffineLineIntegral [g, h, k] = g * h * k := by
  show ((1 * g) * h) * k = g * h * k
  rw [one_mul]

/-! ### Named-degeneration Stokes identity

    This section replaces the `stokes_holds := True` of the skeleton
    model with `(1 : G) = 1`, the form the Yekutieli-Stokes equation
    `MI₁(α; ∂σ) = MI₂(d_α β; σ)` takes on a closed (boundaryless)
    2-cell **once both multiplicative integrals have been set to the
    constant `1`**.

    **Retitled 2026-08-24.**  It was headed *"Content-bearing Stokes
    identity (Tier 2 deep)"*.  Substituting a tautology for `True`
    carries no content and reaches no deeper tier: the Prop is still
    closed by `rfl` and still says nothing about forms, paths or
    2-cells.  What it does earn over `True` is that a reader can see
    *which* degeneration is in force.  The substantive material in this
    file is `piecewiseAffineLineIntegral` and `braidSurfaceMultTrace`
    below, which compute. -/

/-! ### `closedCellStokesIdentity` and `content_bearing_stokes` — REMOVED 2026-09-07

    They existed only to hold a differently-spelled tautology in a `Prop`
    field, and that field is gone.

    `closedCellStokesIdentity G` was `(1 : G) = 1`, and
    `content_bearing_stokes` was a second `NonAbelianStokes` model using it
    for both `stokes_holds` and `finite_slice`. Its own docstring had already
    withdrawn the "Substantive" / "Non-vacuous (uses an explicit equation, not
    `True`)" claims a still earlier version made, and said what remained:
    it *"differs from `punitInstance` in the syntax of the `Prop` field and in
    nothing else"*.

    Both models carry the same constantly-`1` integrals. Once `stokes` and
    `finite_slice` became real equations there is no `Prop` field left for the
    two to differ in, so `content_bearing_stokes` became `punitInstance`
    under another name — and `punitInstance` now satisfies the real equations
    by `rfl` rather than by choosing them, which is the whole content the
    removed pair was reaching for.

    Nothing referenced either declaration outside this file.

    History worth keeping, because the correction happened twice: a
    tautology re-spelled as an equation reads as content to a detector and to
    a skimming reader, and both times the docstring claimed more than the Lean
    did. Encoding the field is what settled it — there is now nowhere for a
    re-spelling to live. -/

/-- **Continuous-path 2-form pairing (skeleton)**: a placeholder
    for the `MI₂` evaluation on a continuous (non-piecewise-affine)
    2-cell.  Concrete model: the constant-1 surface integral.
    This bridges the piecewise-affine finite-slice case to the
    Yekutieli continuous-path framework that Mathlib's
    differential-forms library is the upstream target for. -/
def continuousPath2FormPairing (G : Type u) [Group G]
    (_β : G → G → G) (_σ : G → G → G → G) : G := 1

/-- The continuous-path 2-form pairing is identity-valued on the
    skeleton. -/
theorem continuousPath2FormPairing_eq_one (G : Type u) [Group G]
    (β : G → G → G) (σ : G → G → G → G) :
    continuousPath2FormPairing G β σ = (1 : G) := rfl

/-- **Yekutieli-Stokes for the continuous-path pairing**: the
    line integral over the boundary of a 2-cell agrees with the
    surface-integral pairing.  On the skeleton, both sides equal
    1 by definition; the genuine analytic identity is the
    upstream target. -/
theorem yekutieli_stokes_continuous_path (G : Type u) [Group G]
    (β : G → G → G) (σ : G → G → G → G) :
    piecewiseAffineLineIntegral ([] : List G) =
      continuousPath2FormPairing G β σ := by
  rw [piecewiseAffineLineIntegral_nil, continuousPath2FormPairing_eq_one]

/-! ### Boundary holonomy = ordered braid Hecke image (PROVABLE-NOW item #1)

    The original `braidSurfaceMultTrace z braidLength = z ^ braidLength`
    models a braid's surface holonomy as a *scalar power* of a single
    element `z` — it ignores the actual generator content of the
    braid word `β = σ_{i₁} σ_{i₂} ⋯ σ_{i_ℓ}`.  That is a toy: a braid
    word's boundary holonomy is the **ordered product of the
    generator-actions in the Hecke image** `ρ(σ_{i₁}) ⋯ ρ(σ_{i_ℓ})`,
    not a single generator raised to the word length.

    Per `docs/audits/2026-06-01-qhyperbolic-nonabelian-stokes-wiring.md`
    (item: *boundary-holonomy = braid Hecke image*), this is a finite
    computation provable from the existing `piecewiseAffineLineIntegral`
    ordered-product machinery above.  We supply the real
    `braidWordHolonomy` (the ordered product over the Hecke images of
    the braid letters), prove it carries the Markov cocycle, and show
    the toy scalar model is the degenerate single-letter special case. -/

/-- **Braid-word boundary holonomy.**  For a braid word presented as a
    list of its Hecke-image generator-actions `[ρ(σ_{i₁}), …,
    ρ(σ_{i_ℓ})] : List G`, the boundary holonomy of the Seifert
    surface is the left-ordered product `ρ(σ_{i₁}) · ⋯ · ρ(σ_{i_ℓ})`.
    This is the genuine non-abelian Stokes boundary holonomy (the
    surface-ordered exponential reduces to the ordered product on the
    piecewise-affine Young-diagram surface), replacing the toy scalar
    power `z ^ ℓ`. -/
def braidWordHolonomy {G : Type u} [Group G] (heckeImages : List G) : G :=
  piecewiseAffineLineIntegral heckeImages

/-- The empty braid word's boundary holonomy is the identity. -/
theorem braidWordHolonomy_nil {G : Type u} [Group G] :
    braidWordHolonomy ([] : List G) = 1 :=
  piecewiseAffineLineIntegral_nil

/-- **Markov cocycle (append a generator).**  Appending one more
    Hecke-image letter `g` to a braid word multiplies its boundary
    holonomy on the right by `g` — the non-abelian Markov-axiom
    recursion `Hol(β · σ_i) = Hol(β) · ρ(σ_i)`. -/
theorem braidWordHolonomy_append_letter {G : Type u} [Group G]
    (word : List G) (g : G) :
    braidWordHolonomy (word ++ [g]) = braidWordHolonomy word * g := by
  unfold braidWordHolonomy
  rw [piecewiseAffineLineIntegral_append, piecewiseAffineLineIntegral_singleton]

/-- **Concatenation of braid words.**  The boundary holonomy of a
    concatenated braid word is the product of the two holonomies —
    functoriality of the holonomy under braid composition. -/
theorem braidWordHolonomy_append {G : Type u} [Group G]
    (w₁ w₂ : List G) :
    braidWordHolonomy (w₁ ++ w₂) =
      braidWordHolonomy w₁ * braidWordHolonomy w₂ :=
  piecewiseAffineLineIntegral_append w₁ w₂

/-- **Toy model is the single-letter special case.**  The original
    scalar model `braidSurfaceMultTrace z n = z ^ n` IS the boundary
    holonomy of the braid word `[z, z, …, z]` (`n` copies of the same
    Hecke-image generator `z`).  So the real ordered-product holonomy
    `braidWordHolonomy` strictly generalises the toy: the toy is
    recovered exactly when every letter of the word is the same
    generator `z`. -/
theorem braidSurfaceMultTrace_eq_braidWordHolonomy_replicate
    {G : Type u} [Group G] (z : G) (n : ℕ) :
    braidSurfaceMultTrace z n = braidWordHolonomy (List.replicate n z) := by
  unfold braidWordHolonomy braidSurfaceMultTrace
  rw [piecewiseAffineLineIntegral_replicate]

/-- **Closed-braid (Markov-closure) holonomy is conjugation-stable.**
    A braid word and any cyclic permutation of its letters yield
    boundary holonomies that are conjugate in `G` (the Markov-trace
    closure is a *class function*, invariant under conjugation).  We
    prove the one-letter rotation case: rotating the first letter `g`
    to the end conjugates the holonomy by `g`. -/
theorem braidWordHolonomy_cyclic_one {G : Type u} [Group G]
    (g : G) (rest : List G) :
    braidWordHolonomy (rest ++ [g]) =
      g⁻¹ * braidWordHolonomy (g :: rest) * g := by
  have hsplit : braidWordHolonomy (g :: rest) =
      g * braidWordHolonomy rest := by
    have : (g :: rest) = [g] ++ rest := by rfl
    rw [this, braidWordHolonomy_append]
    congr 1
    show braidWordHolonomy [g] = g
    unfold braidWordHolonomy
    exact piecewiseAffineLineIntegral_singleton g
  rw [braidWordHolonomy_append_letter, hsplit]
  -- goal: braidWordHolonomy rest * g = g⁻¹ * (g * braidWordHolonomy rest) * g
  rw [inv_mul_cancel_left]

/-! ### Chern–Simons / hyperbolic-volume correspondence (NEEDS-NEW-INPUT)

    The audit's *baselineHolonomy = knotVolume* item is the Volume
    Conjecture (Kashaev; Murakami–Murakami): the asymptotic growth of
    the colored Jones invariant — the trace of the boundary holonomy —
    recovers the hyperbolic volume `Vol(S³ ∖ K)`.  This is NOT provable
    from the existing finite-product machinery: it is a deep analytic
    correspondence with no Mathlib infrastructure.  We carry it as an
    explicit axiom with a Volume-Conjecture citation, NOT as a `True`
    stub, so the dependency is honest and auditable. -/

/-! ### Retired: `chernSimons_volume_correspondence` (2026-09-06, bean `qou-85cg`)

The theorem that stood here,

    theorem chernSimons_volume_correspondence (G : Type u) [Group G] :
        ∃ vol : G → ℝ, ∀ holonomy : G, vol holonomy = vol holonomy := ⟨fun _ => 0, fun _ => rfl⟩

was a tautology — the inner clause is reflexive for every `vol`, and the witness was the
constant-zero function — kept, by its own docstring, "to maintain audit visibility of the
dependency point". It is **retired rather than upgraded**, because the honest carrier of the
Volume-Conjecture content it stood in for **already exists**:
`QOU.MassEndomorphism.VolumeBridge` (§3b-cond, non-degenerate, deliberately **no instance**)
axiomatises exactly the archimedean bridge `volTerm = descTrace + transient` at `q₀` — the open
Step 3 of `conj:mass-endomorphism` — and *derives* the manuscript's identities from it. Adding a
second carrier for the same conjecture here would be the overload trap AGENTS.md warns about
("attributes do not transfer across overloaded symbols"); the 2026-07-12 audit's §G6 request to
"upgrade" this tautology is discharged by pointing at `VolumeBridge`, not by building a twin.

Nothing in `content/` consumed the retired name: the only references were two dated audit docs
(2026-06-01 §"surface-boundary", 2026-07-12 §G6). The Kashaev-asymptotic form of the same
conjecture, `log‖J_N(K; e^{2πi/N})‖ / N → Vol(S³∖K)/2π`, is expressible with
`QOU.MathlibExt.ExponentialGrowthRate` (`tendsto_log_norm_model`: the growth rate is `Re ζ`) and
is deliberately **not** added here for the same reason. Citations for the conjecture itself:
[kashaev1997] https://doi.org/10.1023/A:1007364912784, [murakami-murakami2001]
https://doi.org/10.1007/BF02392716 — both held (`arxiv-q-alg-9601025v2`; MM2001 registered).
-/

end QOU.Mathlib.NonAbelianStokes
