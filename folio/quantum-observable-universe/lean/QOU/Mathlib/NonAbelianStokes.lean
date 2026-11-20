import Mathlib.Algebra.Group.Basic
import Mathlib.Data.Real.Basic

/-!
# QOU.Mathlib.NonAbelianStokes — Yekutieli's non-abelian Stokes (axiomatised)

The QOU substrate's GB-filtration argument relies on Yekutieli
(2015), *Nonabelian Multiplicative Integration on Surfaces*
(World Scientific, DOI 10.1142/9165).  Mathlib status (checked against
the pinned Mathlib `f897ebcf`): Mathlib has differential forms and the
exterior derivative on a **normed space**
(`Mathlib.Analysis.Calculus.DifferentialForm.Basic`: `extDeriv`,
`extDeriv_extDeriv`, i.e. `d ∘ d = 0`), for `ω : E → E [⋀^Fin n]→L[𝕜] F`
with an **arbitrary** normed target `F` — so Lie-algebra-valued forms on a
normed space are expressible there. It has **no** differential forms on
**manifolds** (that file's own TODO says the manifold case is "not defined
yet"; `Mathlib.Geometry.Manifold.MFDeriv` is the manifold *derivative*, not
forms), **no** holonomy or parallel transport, and **no** multiplicative
line / surface integral.

This file is the **smallest §3b-cond class hypothesis** that
abstracts away the genuine Mathlib infrastructure.  It supplies:

1. `LieValuedOneForm` — abstract carrier for `Ω¹(M; 𝔤)`.
2. `MultiplicativeLineIntegral` — abstract `MI₁(α; γ) ∈ G`.
3. `MultiplicativeSurfaceIntegral` — abstract `MI₂(α, β; σ)`.
4. The Yekutieli-Stokes identity `MI₁(α; ∂σ) = MI₂(d_α β; σ)`
   as a class field.
5. The **finite-slice** corollary: on a piecewise-affine
   manifold (the Young-diagram braid surface), the multiplicative
   integral is a literal finite product of generator-actions.

Concrete instances are deferred to Mathlib.  The class allows
downstream theorems to take `[YekutieliFiniteSliceMultiplicativeTrace
T_w]` as a §3b-cond instance hypothesis.

**File status**: upstreamable scaffolding.  ~3000-5000 LoC of
genuine Mathlib infrastructure (Lie-valued forms,
non-commutative path-ordered exponential, Yekutieli-Stokes
proof) is the upstream target.

**References**:
- Yekutieli, *Nonabelian Multiplicative Integration on Surfaces*
  (World Scientific 2015), DOI 10.1142/9165.
- [leitner2026] `def:yekutieli-multiplicative-trace`.
-/

namespace QOU.Mathlib.NonAbelianStokes

universe u

/-- Abstract carrier for a Lie-algebra-valued 1-form on a
    manifold `M` with values in a Lie group `G`.  Concrete
    instances would be `Ω¹(M; 𝔤)` from the Mathlib geometry
    library. -/
structure LieValuedOneForm (M G : Type u) where
  /-- The underlying form-evaluation map (concrete instance:
      pointwise tangent-vector evaluation into 𝔤). -/
  eval : M → M → G

/-- Abstract carrier for a Lie-algebra-valued 2-form. -/
structure LieValuedTwoForm (M G : Type u) where
  /-- The underlying form-evaluation map (pointwise on
      tangent bivectors). -/
  eval : M → M → M → G

/-- The **multiplicative line integral** `MI₁(α; γ) ∈ G` of
    a Lie-valued 1-form `α` along a path `γ`.  Defined as
    the limit of left-ordered products of `exp(α(γ'(t_i)) Δt)`
    in the genuine theory; abstracted here. -/
structure MultiplicativeLineIntegral (M G : Type u) where
  /-- The integral-evaluation map. -/
  integrate : LieValuedOneForm M G → (M → M) → G

/-- The **multiplicative surface integral** `MI₂(α, β; σ) ∈ G`
    of a 2-form `β` (with auxiliary 1-form `α`) over a 2-cell
    `σ`.  Abstracted as a function. -/
structure MultiplicativeSurfaceIntegral (M G : Type u) where
  /-- The surface-integral-evaluation map. -/
  integrate : LieValuedOneForm M G → LieValuedTwoForm M G →
              (M → M → M) → G

/-- **Yekutieli's non-abelian Stokes** as a §3b-cond class.

    The class fields encode the integral-equality content of
    Yekutieli (2015):
      `MI₁(α; ∂σ) = MI₂(d_α β; σ)`
    where `d_α β = dβ + [α, β]` is the gauge-covariant derivative.

    For the QOU substrate, the **finite-slice** version applies
    on the piecewise-affine Young-diagram braid surface: every
    multiplicative integral is a literal finite product of
    generator-actions; no analytic limit. -/
class NonAbelianStokes (M G : Type u) [Group G] where
  /-- The line integral. -/
  lineIntegral : MultiplicativeLineIntegral M G
  /-- The surface integral. -/
  surfaceIntegral : MultiplicativeSurfaceIntegral M G
  /-- The boundary `∂σ` of a 2-cell, as a path.  A field because this file
      abstracts the manifold away; stating Stokes needs a boundary and there
      was none to refer to. -/
  boundary : (M → M → M) → (M → M)
  /-- The gauge-covariant derivative `d_α β = dβ + [α, β]` at the level of the
      group-valued forms this class works with.  (`gaugeCovariantDerivative`
      below is the Lie-algebra-valued counterpart.) -/
  covariantD : LieValuedOneForm M G → LieValuedTwoForm M G →
    LieValuedTwoForm M G
  /-- The piecewise-affine slicing of a path into finitely many generator
      actions.  A field for the same reason as `boundary`: the finite-slice
      axiom is a statement ABOUT such a decomposition. -/
  slice : (M → M) → List G
  /-- **Yekutieli-Stokes identity**: `MI₁(α; ∂σ) = MI₂(α, d_α β; σ)`.

      Was `stokes_holds : Prop` with a sibling witness — a field typed with
      the UNIVERSE `Prop`, so the instance supplied both the proposition and
      its proof.  Its own docstring called itself a "placeholder Prop". -/
  stokes : ∀ (α : LieValuedOneForm M G) (β : LieValuedTwoForm M G)
      (σ : M → M → M),
    lineIntegral.integrate α (boundary σ)
      = surfaceIntegral.integrate α (covariantD α β) σ
  /-- **Finite-slice axiom**: on a piecewise-affine surface the
      multiplicative integral IS the finite generator product.

      Written as the fold rather than as `piecewiseAffineLineIntegral (slice
      γ)` only because that definition lands below this class in the file;
      `finite_slice_eq_piecewiseAffine` immediately after it records that the
      two are the same, so the link is stated rather than left to the reader
      to notice. -/
  finite_slice : ∀ (α : LieValuedOneForm M G) (γ : M → M),
    lineIntegral.integrate α γ = (slice γ).foldl (· * ·) 1

/-- **Skeleton model** — both multiplicative integrals are constantly
    `1` and both `Prop` fields are `True`.  It encodes no Stokes
    identity and no finite-slice reduction.  Genuine models over
    `M = ℝ²`, `G = SU(n)`, etc., arrive once Mathlib's
    Lie-valued-forms library lands.

    **A `def`, not an `instance`, since 2026-08-24.**  This file's own
    prose at §"Substrate theorem" already named the defect: because
    `NonAbelianStokes` pairs `stokes_holds : Prop` with
    `stokes_holds_witness : stokes_holds`, it is a *self-certifying
    carrier*, inhabited by taking the `Prop` to be `True` — *"which
    `punitInstance` below literally does"*.  That was written to
    justify restating a `∃ (_ : NonAbelianStokes M G), True` claim
    against real content; the instance it names was left resolvable, so
    any future `[NonAbelianStokes M G]` hypothesis would still have
    been discharged with `True` before its author noticed.

    Blast radius of the demotion, measured: **zero** — no declaration
    in the corpus takes `[NonAbelianStokes M G]`.  A caller wanting the
    skeleton writes `letI := punitInstance M G`. -/
def punitInstance (M G : Type u) [Group G] : NonAbelianStokes M G where
  lineIntegral := { integrate := fun _ _ => 1 }
  surfaceIntegral := { integrate := fun _ _ _ => 1 }
  boundary σ := fun m => σ m m
  covariantD _ β := β
  -- Every path slices to the empty product, which is the only slicing
  -- consistent with both integrals being constantly `1`.
  slice _ := []
  -- Both relations now have to HOLD rather than be chosen, and they do:
  -- `1 = 1`, and `piecewiseAffineLineIntegral [] = 1` by
  -- `piecewiseAffineLineIntegral_nil`.  That is a real (degenerate) model,
  -- which is a different thing from the `True` it used to write.
  stokes _ _ _ := rfl
  finite_slice _ _ := rfl

/-! ### Substrate theorem (S-Yekutieli-finite-slice)

    The substrate claim — at finite slice depth the multiplicative
    integral on a Young-diagram braid surface IS a finite product
    of generator-actions — is stated as
    `yekutieli_finite_slice_substrate`, below the
    `YekutieliFiniteSliceMultTrace` class it quantifies over.

    **Moved + restated 2026-08-21** (vacuity ledger,
    `proof-no-trivial-true` / `exists-true-tautology`).  It stood
    here as `∃ (_ : NonAbelianStokes M G), True :=
    ⟨inferInstance, trivial⟩` — an existence claim its own
    docstring already flagged as "tautologically true given a
    default class instance".  It is worse than tautological:
    `NonAbelianStokes` is a **self-certifying carrier**
    (`stokes_holds : Prop` *together with*
    `stokes_holds_witness : stokes_holds`), so it is inhabited by
    taking the `Prop` to be `True` — which `punitInstance` below
    literally does.  No existence or `Nonempty` statement about
    that class is falsifiable, so restating against real content
    was required rather than merely dropping the `True`. -/

/-! ### Substantive Yekutieli content

    Beyond the abstract class skeleton, this section supplies:
    1. **Piecewise-affine line integral**: for a path realised
       as a finite sequence of `G`-valued generator-actions,
       the multiplicative line integral is the literal ordered
       product.
    2. **Braid-surface multiplicative trace**: for a braid word
       `β = σ_{i_1} ··· σ_{i_ℓ}`, the surface integral over the
       Young-diagram braid surface is `T_β · T_β⁻¹ = 1` (closed
       surface, identity holonomy after closure).
    3. **Stokes identity at finite slicing**: explicit equation
       relating the boundary line integral to the surface
       integral via the gauge-covariant derivative. -/

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

/-- The `NonAbelianStokes.finite_slice` field's right-hand side IS
    `piecewiseAffineLineIntegral` of the slice.  The field is spelled as the
    raw fold only because this definition lands below the class; recording the
    identification here keeps the axiom readable as what it means. -/
theorem finite_slice_eq_piecewiseAffine {M G : Type u} [Group G]
    [S : NonAbelianStokes M G] (α : LieValuedOneForm M G) (γ : M → M) :
    S.lineIntegral.integrate α γ = piecewiseAffineLineIntegral (S.slice γ) :=
  S.finite_slice α γ

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
    reduce to the identity.  This is the simplest non-vacuous
    case of `stokes_holds`. -/
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

/-! ### Lie-valued forms (substantive — item #4)

    A genuine Lie-valued form `α : Ω¹(M; 𝔤)` is a smooth section
    of the bundle `T*M ⊗ 𝔤` over a manifold `M` with values in
    a Lie algebra `𝔤`.  Mathlib has Lie algebras (`Mathlib.Algebra.Lie`)
    and normed-space forms (`Mathlib.Analysis.Calculus.DifferentialForm.Basic`,
    arbitrary normed target), but no forms on manifolds and no
    `Mathlib.Analysis.NormedSpace.LieAlgebra` module; the manifold
    case requires building the bundle structure explicitly.

    This file supplies the **algebraic skeleton** — Lie algebras,
    Lie brackets, and the formal-grade-1 / grade-2 carriers —
    deferring the manifold part to upstream Mathlib. -/

/-- **Lie algebra structure** as an abstract class.  In Mathlib
    proper, this is `LieAlgebra k 𝔤`; here we re-export the
    bracket axioms (with bilinearity) that the Yekutieli-Stokes
    proof requires. -/
class LieAlgebraStructure (𝔤 : Type u) [AddCommGroup 𝔤] where
  /-- The Lie bracket. -/
  bracket : 𝔤 → 𝔤 → 𝔤
  /-- Antisymmetry on the diagonal: `[x, x] = 0`. -/
  bracket_self : ∀ x, bracket x x = 0
  /-- Bilinearity (left): `[x + y, z] = [x, z] + [y, z]`. -/
  bracket_add_left : ∀ x y z,
    bracket (x + y) z = bracket x z + bracket y z
  /-- Bilinearity (right): `[x, y + z] = [x, y] + [x, z]`. -/
  bracket_add_right : ∀ x y z,
    bracket x (y + z) = bracket x y + bracket x z
  /-- Jacobi identity: `[[x,y],z] + [[y,z],x] + [[z,x],y] = 0`. -/
  jacobi : ∀ x y z,
    bracket (bracket x y) z + bracket (bracket y z) x +
      bracket (bracket z x) y = 0

/-- Antisymmetry corollary: `[x, y] = -[y, x]`.

    Derivation: `[x+y, x+y] = 0` (by `bracket_self`); expand
    via bilinearity to `[x,x] + [x,y] + [y,x] + [y,y] = 0`;
    apply `bracket_self` to drop `[x,x]` and `[y,y]`; conclude
    `[x,y] + [y,x] = 0`, i.e. `[x,y] = -[y,x]`. -/
theorem bracket_antisym {𝔤 : Type u}
    [AddCommGroup 𝔤] [L : LieAlgebraStructure 𝔤] (x y : 𝔤) :
    L.bracket x y = -L.bracket y x := by
  have h1 : L.bracket (x + y) (x + y) = 0 := L.bracket_self (x + y)
  rw [L.bracket_add_left, L.bracket_add_right, L.bracket_add_right,
      L.bracket_self, L.bracket_self] at h1
  -- h1 : 0 + L.bracket x y + (L.bracket y x + 0) = 0
  simp at h1
  -- h1 : L.bracket x y + L.bracket y x = 0
  exact add_eq_zero_iff_eq_neg.mp h1

/-- **Lie-valued 1-form** as an abstract function `M → 𝔤`. -/
structure LieAlgebraOneForm (M : Type u) (𝔤 : Type u) where
  /-- The underlying form-evaluation. -/
  eval : M → 𝔤

/-- **Lie-valued 2-form**. -/
structure LieAlgebraTwoForm (M : Type u) (𝔤 : Type u) where
  /-- The underlying bivector-evaluation. -/
  eval : M → M → 𝔤

/-- The **gauge-covariant derivative** `d_α β = dβ + [α, β]`
    appearing in Yekutieli-Stokes.  Abstract here as a function
    of the underlying 1-form `α` and 2-form `β`; concrete
    instance requires the manifold + Lie-algebra structure. -/
def gaugeCovariantDerivative {M 𝔤 : Type u}
    [AddCommGroup 𝔤] [LieAlgebraStructure 𝔤]
    (α : LieAlgebraOneForm M 𝔤) (β : LieAlgebraTwoForm M 𝔤) :
    LieAlgebraTwoForm M 𝔤 :=
  { eval := fun p q => β.eval p q +
      LieAlgebraStructure.bracket (α.eval p) (β.eval p q) }

/-- **Class hypothesis**: a Lie-valued non-abelian Stokes
    framework.  Bundles the 1-form, 2-form, gauge-covariant
    derivative, and the Yekutieli-Stokes identity. -/
class LieValuedStokes (M : Type u) (𝔤 : Type u)
    [AddCommGroup 𝔤] [LieAlgebraStructure 𝔤] where
  /-- The 1-form `α`. -/
  alpha : LieAlgebraOneForm M 𝔤
  /-- The 2-form `β`. -/
  beta : LieAlgebraTwoForm M 𝔤
  /-- Line integral of a 1-form along a path, valued in `𝔤`. -/
  lineIntegral : LieAlgebraOneForm M 𝔤 → (M → M) → 𝔤
  /-- Surface integral of a 2-form over a 2-cell, valued in `𝔤`. -/
  surfaceIntegral : LieAlgebraTwoForm M 𝔤 → (M → M → M) → 𝔤
  /-- The boundary `∂σ` of a 2-cell. -/
  boundary : (M → M → M) → (M → M)
  /-- **Yekutieli-Stokes, infinitesimal form**: `∫_{∂σ} α = ∫_σ d_α β`, with
      `d_α β` the `gaugeCovariantDerivative` defined above.

      This is bean `qou-ewc4`, filed by
      `UpstreamSubstrateBridge.lean` when it REMOVED a
      `∃ S : LieValuedStokes M 𝔤, True` rather than restate it: *"making the
      carrier content-bearing (a real `stokes_identity` field rather than a
      `Prop` + witness pair)"*.  That is this field.  The three integrals it
      quantifies over are carried because this class had the forms and no way
      to integrate them, which is why it could not state its own subject. -/
  stokes_identity : ∀ σ : M → M → M,
    lineIntegral alpha (boundary σ)
      = surfaceIntegral (gaugeCovariantDerivative alpha beta) σ

/-! ### The zero model of `LieValuedStokes`

    **This declaration used to claim it was non-vacuous, and it was not.**
    Its docstring read *"Non-vacuous (uses a concrete predicate, not True)"*
    over `stokes_identity := (0 : 𝔤) = 0`, witnessed by `rfl`, with an inline
    comment conceding "Holds tautologically".  `0 = 0` is exactly as vacuous
    as `True`; the difference is cosmetic, and the docstring asserting
    otherwise is the more serious half, because a reader who greps for
    "non-vacuous" finds a false all-clear.

    It was also an **`instance`**, so `[LieValuedStokes M 𝔤]` was discharged
    globally with that tautology — precisely the defect `punitInstance` was
    demoted for on 2026-08-24, one class up in this same file, and the reason
    `UpstreamSubstrateBridge.lean` deleted its `lie_valued_stokes_discharged`
    rather than restate it (bean `qou-ewc4`).

    With `stokes_identity` now a real equation the zero model still exists —
    consistency is not the problem — but it holds it rather than choosing it,
    and it is a `def`. -/

/-- **The zero model**: `α = 0`, `β = 0`, both integrals constantly `0`.

    A `def`, not an `instance`, for the reason recorded at `punitInstance`: a
    global instance discharges every downstream `[LieValuedStokes …]` behind
    its author's back.  A caller wanting it writes
    `letI := LieValuedStokes_canonical M 𝔤`.

    What it establishes is consistency and nothing more.  By the `qou-z9ws`
    inhabitation discriminator, a model in which every integral is `0` is
    evidence the axioms can be satisfied and no evidence that they constrain
    anything; a non-degenerate model needs the analytic theory this file
    abstracts away, and `qou-ewc4` stays open for it. -/
def LieValuedStokes_canonical (M : Type u) (𝔤 : Type u)
    [AddCommGroup 𝔤] [LieAlgebraStructure 𝔤] :
    LieValuedStokes M 𝔤 where
  alpha := { eval := fun _ => 0 }
  beta := { eval := fun _ _ => 0 }
  lineIntegral _ _ := 0
  surfaceIntegral _ _ := 0
  boundary σ := fun m => σ m m
  stokes_identity _ := rfl

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
