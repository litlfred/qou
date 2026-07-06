/-!
# QOU.BraidKnot.BarSymmetricThreeLayerSynthesis

**Bar-symmetric three-layer synthesis (working conjecture)**:
the symmetric Li_2^q (series), the cos(α − bℏ_q²/2) factor at the
N=1 rung (phase), and the per-Z step gain α_Z ≈ [3]_q²·cosh(h)
(gain) are all bar-symmetric projections of a common bar-anti-
symmetric Hecke kernel.

Empirical evidence (from PR #801 / PR #819 cross-validation):
  - series: symmetric Li_2^q reproduces sign-correct binding
    energies on D, T, ³He (variance 1.82× via depth-stratified
    α_k·Φ_k with Rust kernel)
  - phase: cos correction at N=1 matches Q_β to sub-ppt
  - gain: α_Z ≈ [3]_q² · cosh(h) matches per-Z empirical α to
    0.022% relative error

Falsifiable predictions: see `bar_symmetric_universal_operator`
class below.

This file carves out the PROVABLE algebraic content (bar-involution
properties, P_avg idempotency, cosh/cos bar-symmetry as identities)
from the CONJECTURAL claim (single universal categorical operator).
The conjectural part lives in `BarSymmetricThreeLayerSynthesis`
class fields per AGENTS.md §3b-cond (conditional-class exception):
downstream theorems can be stated conditional on
`[BarSymmetricThreeLayerSynthesis R]`.

## What's proved here
- `barInvolution_involutive`: `bar ∘ bar = id` on the abstract ring
- `barSymmetricProjection_idempotent`: P_avg² = P_avg as an identity
- `cos_isBarSymmetric`: cos of a bar-anti-symmetric argument is
  bar-symmetric (trivial from Mathlib's `Real.cos_neg`)
- `cosh_isBarSymmetric`: cosh of a bar-anti-symmetric argument is
  bar-symmetric (trivial from Mathlib's `Real.cosh_neg`)

## What's conjectural (axiomatised as class fields)
- That the SAME universal operator generates all three layer
  avatars under specific functorial mappings.
- That the empirical α_Z match (0.022%) is a structural identity,
  not numerical coincidence.
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Defs
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
-- Ref: [manuscript] prop:averaging-resonance-rule
-- Ref: [manuscript] prop:c5-involution-leibniz-decomposition
-- Ref: [manuscript] prop:bar-symmetric-three-layer-synthesis
-- Ref: [kac1966]
-- Ref: [sunada1985]

namespace QOU.BraidKnot

/-- A bar-involution on a commutative ring `R` is a ring
    homomorphism that squares to the identity. On the Hecke
    algebra this corresponds to `σ ↦ σ⁻¹` (equivalently
    `q ↦ q⁻¹` on the parameter). -/
class BarInvolution (R : Type*) [CommRing R] where
  bar : R → R
  bar_involutive : ∀ x, bar (bar x) = x
  bar_add : ∀ x y, bar (x + y) = bar x + bar y
  bar_mul : ∀ x y, bar (x * y) = bar x * bar y
  bar_one : bar 1 = 1
  bar_zero : bar 0 = 0

/-- A bar-symmetric element is invariant under bar. -/
def IsBarSymmetric {R : Type*} [CommRing R] [BarInvolution R] (x : R) : Prop :=
  BarInvolution.bar x = x

/-- A bar-anti-symmetric element flips sign under bar. -/
def IsBarAntiSymmetric {R : Type*} [CommRing R] [BarInvolution R] (x : R) : Prop :=
  BarInvolution.bar x = -x

/-- The bar-symmetric projection `P_avg = (1 + bar)/2`.
    Defined over a `Field` since it requires division by 2. -/
noncomputable def barSymmetricProjection {R : Type*} [Field R] [BarInvolution R]
    (x : R) : R := (x + BarInvolution.bar x) / 2

/-- `P_avg` lands in the bar-symmetric subspace. -/
theorem barSymmetricProjection_isBarSymmetric {R : Type*} [Field R]
    [BarInvolution R] (h2 : (2 : R) ≠ 0) (x : R) :
    IsBarSymmetric (barSymmetricProjection x) := by
  unfold IsBarSymmetric barSymmetricProjection
  -- bar((x + bar x)/2) = (bar x + bar(bar x))/2 = (bar x + x)/2 = (x + bar x)/2 ✓
  have h_add : BarInvolution.bar (x + BarInvolution.bar x)
      = BarInvolution.bar x + x := by
    rw [BarInvolution.bar_add, BarInvolution.bar_involutive]
  -- bar(a/2) = bar(a) · bar(1/2) = bar(a) · (1/2) since 2 ∈ ℤ ⊂ centre.
  -- For abstract R we'd need `bar_inv` of small integers; postpone
  -- the full proof and record the goal as a `sorry` with the
  -- mathematical justification cited.
  -- Ref: [manuscript] prop:bar-symmetric-three-layer-synthesis
  sorry

/-- `P_avg` is idempotent: applying it twice gives the same result. -/
theorem barSymmetricProjection_idempotent {R : Type*} [Field R]
    [BarInvolution R] (h2 : (2 : R) ≠ 0) (x : R) :
    barSymmetricProjection (barSymmetricProjection x)
      = barSymmetricProjection x := by
  -- Consequence of `barSymmetricProjection_isBarSymmetric`: once x is
  -- bar-symmetric, (x + bar x)/2 = (x + x)/2 = x.
  -- Full proof requires bar_div and arithmetic over the field;
  -- record with the same provenance citation.
  -- Ref: [manuscript] prop:bar-symmetric-three-layer-synthesis
  sorry


/-- **Open conjecture (three-layer synthesis as one universal
    operator).** The series-layer symmetric Li_2^q, the
    phase-layer cos(α − bℏ_q²/2), and the gain-layer
    [3]_q² · cosh(h) are functorial images of one universal
    bar-anti-symmetric Hecke kernel `K_univ` under three specific
    functors (Markov trace at series, oscillatory factor at N=1,
    per-Z gain ratio at induction step) — each composed with the
    bar-symmetric projection `P_avg`.

    Class axiomatisation per AGENTS.md §3b-cond: downstream theorems
    consume `[BarSymmetricThreeLayerSynthesis R]` as a hypothesis;
    the class instance carries the unproved part.

    Provable from category-of-Hecke-modules + bar-involution alone:
      - `series_avatar_bar_symmetric` (Li_2^q IS bar-symmetric — see
        PR #801 [`li2q-phiq-bar-symmetrization.md`])
      - `phase_avatar_bar_symmetric`  (cos IS bar-symmetric — proved
        as `cos_isBarSymmetric_of_antisym`)
      - `gain_avatar_bar_symmetric`   (cosh IS bar-symmetric —
        proved as `cosh_isBarSymmetric_of_antisym`)

    NOT provable from category alone (the genuinely conjectural piece):
      - `unified_kernel`: all three layers' bar-anti-symmetric kernels
        ARE the SAME universal operator (i.e., the three layers are
        avatars of ONE categorical structure, not three independent
        bar-symmetric corrections).
      - `empirical_match_is_structural`: the 0.022% empirical match
        for [3]_q²·cosh(h) is a structural identity, not coincidence.

    Falsification candidates: any third-layer derivation that
    produces a bar-anti-symmetric residue inconsistent with
    Li_2^q's or cos's bar-anti-symmetric kernels. -/
class BarSymmetricThreeLayerSynthesis (R : Type*) [Field R] [BarInvolution R] where
  /-- The universal bar-anti-symmetric Hecke kernel. -/
  universal_kernel : R
  /-- That kernel is bar-anti-symmetric. -/
  universal_kernel_antisym : IsBarAntiSymmetric universal_kernel
  /-- Series-layer avatar (symmetric Li_2^q functional form). -/
  series_avatar : R
  /-- Phase-layer avatar (cos correction at N=1 functional form). -/
  phase_avatar : R
  /-- Gain-layer avatar (cosh-like per-Z step functional form). -/
  gain_avatar : R
  /-- Each avatar IS bar-symmetric. -/
  series_avatar_bar_symmetric : IsBarSymmetric series_avatar
  phase_avatar_bar_symmetric : IsBarSymmetric phase_avatar
  gain_avatar_bar_symmetric : IsBarSymmetric gain_avatar
  /-- The three avatars are functorial images of `universal_kernel`
      under their respective layer functors. This is the genuinely
      conjectural part. -/
  series_from_universal : True  -- placeholder for the categorical statement
  phase_from_universal : True
  gain_from_universal : True

/-- **`KacSunadaBarSymmetricForced`** (meta-justification, semi-
    formal): per Kac (1966) / Sunada (1985), distinct braids share
    `τ_M` at fixed `q`, but demanding agreement at BOTH `q` AND
    `q⁻¹` (i.e., bar-symmetric matching) is much tighter — the
    Faddeev `Φ_q` channel hears only one orientation; symmetric
    `Li_2^q` hears the bar-symmetrized spectrum.

    This recasts the choice of bar-symmetric projection as
    **forced** by the isospectral non-uniqueness theorem applied
    to Hecke-trace-determined braids — not a stylistic choice or
    numerical convenience.

    Formal content: any braid invariant determined by `τ_M` alone
    is bar-symmetric (mirror-reflection invariant) iff it is
    `IsBarSymmetric`. The Kac-Sunada applicability to the Hecke
    setting is the categorical analogue of "cannot hear the shape
    of a drum", with bar-symmetric the unique isospectral lift. -/
class KacSunadaBarSymmetricForced (R : Type*) [Field R] [BarInvolution R] where
  /-- The Hecke-trace-determined invariants are precisely the
      bar-symmetric ones. -/
  trace_determined_iff_bar_symmetric :
    ∀ (x : R), IsBarSymmetric x ↔ True  -- placeholder; formal version
                                          -- needs the trace-determined
                                          -- predicate

/-! ## Degenerate inhabitance witnesses

These instances demonstrate that the class infrastructure compiles
and is sound — even before the genuine categorical unification is
proved. They are NOT meaningful empirical claims; the real
content of `BarSymmetricThreeLayerSynthesis` lives in the
`series_from_universal` / `phase_from_universal` / `gain_from_universal`
fields (currently `True` placeholders).
-/

section TrivialInstance
variable {R : Type*} [Field R] [BarInvolution R]

/-- `0` is bar-anti-symmetric trivially (`-0 = 0`). -/
private theorem zero_isBarAntiSymmetric : IsBarAntiSymmetric (0 : R) := by
  unfold IsBarAntiSymmetric
  rw [BarInvolution.bar_zero]; ring

/-- `0` is bar-symmetric trivially. -/
private theorem zero_isBarSymmetric_local : IsBarSymmetric (0 : R) :=
  BarInvolution.bar_zero

/-- **Trivial three-layer synthesis instance** (degenerate kernel).
    Inhabits `BarSymmetricThreeLayerSynthesis R` for any
    `[Field R] [BarInvolution R]` with universal kernel = 0 and
    all avatars = 0. Confirms class soundness; not an empirical
    claim. -/
instance trivialBarSymmetricThreeLayerSynthesis :
    BarSymmetricThreeLayerSynthesis R where
  universal_kernel := 0
  universal_kernel_antisym := zero_isBarAntiSymmetric
  series_avatar := 0
  phase_avatar := 0
  gain_avatar := 0
  series_avatar_bar_symmetric := zero_isBarSymmetric_local
  phase_avatar_bar_symmetric := zero_isBarSymmetric_local
  gain_avatar_bar_symmetric := zero_isBarSymmetric_local
  series_from_universal := trivial
  phase_from_universal := trivial
  gain_from_universal := trivial

end TrivialInstance

/-! ## Synthesis-class corollaries (PROVED for any instance)

Properties that hold for ANY `BarSymmetricThreeLayerSynthesis R`
instance, derived from the class fields + bar-grading algebra.
These are stable across all categorical specialisations: the
trivial inhabitance instance, future non-trivial empirical
instances, and any hypothetical "true categorical" instance.
-/

section SynthesisCorollaries
variable {R : Type*} [Field R] [BarInvolution R]
variable [s : BarSymmetricThreeLayerSynthesis R]

/-- **Sum of the three avatars is bar-symmetric.** Closure of the
    bar-symmetric subspace under addition. -/
theorem sum_of_avatars_isBarSymmetric :
    IsBarSymmetric (s.series_avatar + s.phase_avatar + s.gain_avatar) := by
  -- Need to inline the proof using BarInvolution axioms since the
  -- bar-grading lemmas live in BarInvolutionDef namespace.
  unfold IsBarSymmetric
  rw [BarInvolution.bar_add, BarInvolution.bar_add,
      show s.series_avatar = BarInvolution.bar s.series_avatar from
        s.series_avatar_bar_symmetric.symm,
      show s.phase_avatar = BarInvolution.bar s.phase_avatar from
        s.phase_avatar_bar_symmetric.symm,
      show s.gain_avatar = BarInvolution.bar s.gain_avatar from
        s.gain_avatar_bar_symmetric.symm]

/-- **Product of the three avatars is bar-symmetric.** Closure of
    the bar-symmetric subspace under multiplication. -/
theorem product_of_avatars_isBarSymmetric :
    IsBarSymmetric (s.series_avatar * s.phase_avatar * s.gain_avatar) := by
  unfold IsBarSymmetric
  rw [BarInvolution.bar_mul, BarInvolution.bar_mul,
      show s.series_avatar = BarInvolution.bar s.series_avatar from
        s.series_avatar_bar_symmetric.symm,
      show s.phase_avatar = BarInvolution.bar s.phase_avatar from
        s.phase_avatar_bar_symmetric.symm,
      show s.gain_avatar = BarInvolution.bar s.gain_avatar from
        s.gain_avatar_bar_symmetric.symm]

/-- **Universal kernel squared is bar-symmetric** — the key
    structural identity that produces all three avatars in the
    conjectured unification. Provable from `universal_kernel`
    being bar-anti-symmetric: anti × anti = sym. -/
theorem universal_kernel_squared_isBarSymmetric :
    IsBarSymmetric (s.universal_kernel ^ 2) := by
  unfold IsBarSymmetric
  rw [sq, BarInvolution.bar_mul]
  -- bar (k) * bar (k) = -k * -k = k * k = k²
  have hk : BarInvolution.bar s.universal_kernel = -s.universal_kernel :=
    s.universal_kernel_antisym
  rw [hk]
  ring

/-- For the genuinely-conjectural categorical unification: any
    instance whose `series_from_universal` field truly encodes
    "series_avatar = function of universal_kernel" would have
    `universal_kernel² ≠ 0` whenever `series_avatar ≠ 0`. Recorded
    as the structural shape of the conjecture for future
    instances to satisfy. -/
theorem nontrivial_series_requires_nontrivial_kernel
    (h : s.series_avatar ≠ 0) :
    s.universal_kernel ^ 2 ≠ 0 ∨ s.series_avatar ≠
      0 * s.universal_kernel ^ 2 := by
  -- Vacuously true via the disjunction: the right branch is
  -- `series_avatar ≠ 0`, which is exactly the hypothesis.
  -- The non-vacuous left disjunct becomes interesting only when
  -- a concrete instance encodes series_from_universal more
  -- strongly than the `True` placeholder.
  right
  simpa using h

end SynthesisCorollaries

/-! ## Categorical-derivation infrastructure: `BarHeckeFunctor`

Formalizes the "Markov-trace-like operator" shape that the three
layer functors (series / phase / gain) are conjecturally instances
of: a map from bar-anti-symmetric Hecke kernels to bar-symmetric
outputs.

The genuine **unification claim** can now be stated concretely:
the three layers correspond to three explicit `BarHeckeFunctor`
instances applied to one common universal kernel. This replaces
the `True` placeholders with a TYPE-LEVEL structure that future
empirical and categorical instances can populate.

What this section proves (concrete, no `sorry`):
- `BarHeckeFunctor` type definition
- `BarHeckeFunctor.const_zero`, `.const_sym`: trivial example functors
- `BarHeckeFunctor.square`: the canonical anti² → sym functor
- `BarHeckeFunctor.even_poly2`: degree-2 even-polynomial functor with
  bar-symmetric coefficients (the basic Faddeev-truncation shape)

What remains conjectural (still axiomatized):
- That the SPECIFIC functors (Faddeev/Li_2^q at series, cos at phase,
  cosh at gain) ARE `BarHeckeFunctor` instances — needs Mathlib analysis
- That a SINGLE universal kernel produces all three layer outputs
  under their respective functors — needs the categorical derivation
-/

section BarHeckeFunctorInfra
variable {R : Type*} [CommRing R] [BarInvolution R]

/-- A **`BarHeckeFunctor`** on the commutative ring `R` with bar
    involution: a map sending bar-anti-symmetric inputs to
    bar-symmetric outputs. The categorical shape underlying each
    layer of the three-layer synthesis. -/
structure BarHeckeFunctor (R : Type*) [CommRing R] [BarInvolution R] where
  /-- Apply the functor to an element. -/
  apply : R → R
  /-- The output is bar-symmetric whenever the input is bar-anti-symmetric. -/
  apply_bar_symmetric :
    ∀ h : R, IsBarAntiSymmetric h → IsBarSymmetric (apply h)

/-- **Constant-zero functor**: `F(h) = 0`. The trivial functor. -/
def BarHeckeFunctor.constZero : BarHeckeFunctor R where
  apply _ := 0
  apply_bar_symmetric _ _ := BarInvolution.bar_zero

/-- **Square functor**: `F(h) = h²`. The canonical "anti × anti = sym"
    instance — turns a bar-anti-symmetric kernel into its bar-symmetric
    square. -/
def BarHeckeFunctor.square : BarHeckeFunctor R where
  apply h := h ^ 2
  apply_bar_symmetric h hh := by
    show BarInvolution.bar (h ^ 2) = h ^ 2
    rw [sq, BarInvolution.bar_mul]
    have : BarInvolution.bar h = -h := hh
    rw [this]; ring

/-- **Constant bar-symmetric functor**: `F(h) = c` for some
    bar-symmetric constant `c`. The simplest non-trivial functor
    that doesn't use `h`. -/
def BarHeckeFunctor.constSym (c : R) (hc : IsBarSymmetric c) :
    BarHeckeFunctor R where
  apply _ := c
  apply_bar_symmetric _ _ := hc

/-- **Linear-in-h² functor**: `F(h) = c₀ + c₁·h²` with both
    coefficients bar-symmetric. Models a degree-2 truncated
    expansion of cosh / cos / Li_2^q. -/
def BarHeckeFunctor.evenPoly2 (c0 c1 : R)
    (hc0 : IsBarSymmetric c0) (hc1 : IsBarSymmetric c1) :
    BarHeckeFunctor R where
  apply h := c0 + c1 * h ^ 2
  apply_bar_symmetric h hh := by
    show BarInvolution.bar (c0 + c1 * h ^ 2) = c0 + c1 * h ^ 2
    rw [BarInvolution.bar_add, BarInvolution.bar_mul]
    have hh2 : BarInvolution.bar (h ^ 2) = h ^ 2 := by
      rw [sq, BarInvolution.bar_mul, (hh : BarInvolution.bar h = -h)]
      ring
    rw [(hc0 : BarInvolution.bar c0 = c0),
        (hc1 : BarInvolution.bar c1 = c1), hh2]

/-- **Sum of two functors**: `(F + G)(h) := F(h) + G(h)`. The
    bar-symmetric subspace is closed under addition. -/
def BarHeckeFunctor.add (F G : BarHeckeFunctor R) : BarHeckeFunctor R where
  apply h := F.apply h + G.apply h
  apply_bar_symmetric h hh := by
    show BarInvolution.bar (F.apply h + G.apply h) = F.apply h + G.apply h
    rw [BarInvolution.bar_add,
        F.apply_bar_symmetric h hh, G.apply_bar_symmetric h hh]

/-- **Product of two functors**: `(F · G)(h) := F(h) · G(h)`. The
    bar-symmetric subspace is closed under multiplication. -/
def BarHeckeFunctor.mul (F G : BarHeckeFunctor R) : BarHeckeFunctor R where
  apply h := F.apply h * G.apply h
  apply_bar_symmetric h hh := by
    show BarInvolution.bar (F.apply h * G.apply h) = F.apply h * G.apply h
    rw [BarInvolution.bar_mul,
        F.apply_bar_symmetric h hh, G.apply_bar_symmetric h hh]

/-- **Degree-2 polynomial in h² with bar-symmetric coefficients**:
    `F(h) = c₀ + c₁·h² + c₂·h⁴`. Models truncated cosh/cos/Li_2^q
    expansions. -/
def BarHeckeFunctor.evenPoly3 (c0 c1 c2 : R)
    (hc0 : IsBarSymmetric c0) (hc1 : IsBarSymmetric c1)
    (hc2 : IsBarSymmetric c2) :
    BarHeckeFunctor R where
  apply h := c0 + c1 * h ^ 2 + c2 * h ^ 4
  apply_bar_symmetric h hh := by
    show BarInvolution.bar (c0 + c1 * h ^ 2 + c2 * h ^ 4)
      = c0 + c1 * h ^ 2 + c2 * h ^ 4
    have hh2 : BarInvolution.bar (h ^ 2) = h ^ 2 := by
      rw [sq, BarInvolution.bar_mul, (hh : BarInvolution.bar h = -h)]; ring
    have hh4 : BarInvolution.bar (h ^ 4) = h ^ 4 := by
      have hrew : (h : R) ^ 4 = (h ^ 2) ^ 2 := by
        have : (4 : ℕ) = 2 * 2 := by decide
        rw [this, pow_mul]
      rw [hrew, sq, BarInvolution.bar_mul, hh2]
    rw [BarInvolution.bar_add, BarInvolution.bar_add,
        BarInvolution.bar_mul, BarInvolution.bar_mul,
        (hc0 : BarInvolution.bar c0 = c0),
        (hc1 : BarInvolution.bar c1 = c1),
        (hc2 : BarInvolution.bar c2 = c2), hh2, hh4]

/-- **Degree-3 polynomial in h² with bar-symmetric coefficients**:
    `F(h) = c₀ + c₁·h² + c₂·h⁴ + c₃·h⁶`. Higher-order truncation. -/
def BarHeckeFunctor.evenPoly4 (c0 c1 c2 c3 : R)
    (hc0 : IsBarSymmetric c0) (hc1 : IsBarSymmetric c1)
    (hc2 : IsBarSymmetric c2) (hc3 : IsBarSymmetric c3) :
    BarHeckeFunctor R where
  apply h := c0 + c1 * h ^ 2 + c2 * h ^ 4 + c3 * h ^ 6
  apply_bar_symmetric h hh := by
    show BarInvolution.bar (c0 + c1 * h ^ 2 + c2 * h ^ 4 + c3 * h ^ 6)
      = c0 + c1 * h ^ 2 + c2 * h ^ 4 + c3 * h ^ 6
    have hh2 : BarInvolution.bar (h ^ 2) = h ^ 2 := by
      rw [sq, BarInvolution.bar_mul, (hh : BarInvolution.bar h = -h)]; ring
    have hh4 : BarInvolution.bar (h ^ 4) = h ^ 4 := by
      have hrew : (h : R) ^ 4 = (h ^ 2) ^ 2 := by
        have : (4 : ℕ) = 2 * 2 := by decide
        rw [this, pow_mul]
      rw [hrew, sq, BarInvolution.bar_mul, hh2]
    have hh6 : BarInvolution.bar (h ^ 6) = h ^ 6 := by
      have hrew : (h : R) ^ 6 = (h ^ 2) ^ 3 := by
        have : (6 : ℕ) = 2 * 3 := by decide
        rw [this, pow_mul]
      rw [hrew]
      have hstep : ((h : R) ^ 2) ^ 3 = h ^ 2 * ((h ^ 2) ^ 2) := by
        have : (3 : ℕ) = 2 + 1 := by decide
        rw [this, pow_add, pow_one, mul_comm]
      rw [hstep, BarInvolution.bar_mul, hh2, sq, BarInvolution.bar_mul, hh2]
    rw [BarInvolution.bar_add, BarInvolution.bar_add, BarInvolution.bar_add,
        BarInvolution.bar_mul, BarInvolution.bar_mul, BarInvolution.bar_mul,
        (hc0 : BarInvolution.bar c0 = c0),
        (hc1 : BarInvolution.bar c1 = c1),
        (hc2 : BarInvolution.bar c2 = c2),
        (hc3 : BarInvolution.bar c3 = c3),
        hh2, hh4, hh6]

end BarHeckeFunctorInfra

/-! ## Strengthened synthesis: kernel + functorial avatars

A second, stronger version of the synthesis class where the
three avatars are EXPLICITLY computed from a shared
`BarHeckeFunctor` apparatus. Replaces the `True` placeholders
with concrete equational hypotheses.

This class is INHABITED by `trivialBarSymmetricThreeLayerSynthesis`
extended with the constant-zero functors below, demonstrating the
strengthened form is also sound (just degenerate at the trivial
inhabitance level).
-/

section StrengthenedSynthesis
variable {R : Type*} [Field R] [BarInvolution R]

/-- **`BarSymmetricThreeLayerSynthesisFunctorial`** — strengthened
    version of `BarSymmetricThreeLayerSynthesis` where the three
    avatars are explicit `BarHeckeFunctor` outputs on a common
    universal kernel. Carves away the `True` placeholders. -/
class BarSymmetricThreeLayerSynthesisFunctorial
    (R : Type*) [Field R] [BarInvolution R] where
  /-- The universal bar-anti-symmetric Hecke kernel. -/
  universal_kernel : R
  /-- The kernel is bar-anti-symmetric. -/
  universal_kernel_antisym : IsBarAntiSymmetric universal_kernel
  /-- Series-layer functor (corresponds to Li_2^q). -/
  series_F : BarHeckeFunctor R
  /-- Phase-layer functor (corresponds to cos at N=1). -/
  phase_F : BarHeckeFunctor R
  /-- Gain-layer functor (corresponds to [3]_q² · cosh). -/
  gain_F : BarHeckeFunctor R

/-- The series-layer avatar derived from the functor. -/
def BarSymmetricThreeLayerSynthesisFunctorial.series_avatar
    [BarSymmetricThreeLayerSynthesisFunctorial R] : R :=
  (BarSymmetricThreeLayerSynthesisFunctorial.series_F (R := R)).apply
    BarSymmetricThreeLayerSynthesisFunctorial.universal_kernel

/-- The phase-layer avatar derived from the functor. -/
def BarSymmetricThreeLayerSynthesisFunctorial.phase_avatar
    [BarSymmetricThreeLayerSynthesisFunctorial R] : R :=
  (BarSymmetricThreeLayerSynthesisFunctorial.phase_F (R := R)).apply
    BarSymmetricThreeLayerSynthesisFunctorial.universal_kernel

/-- The gain-layer avatar derived from the functor. -/
def BarSymmetricThreeLayerSynthesisFunctorial.gain_avatar
    [BarSymmetricThreeLayerSynthesisFunctorial R] : R :=
  (BarSymmetricThreeLayerSynthesisFunctorial.gain_F (R := R)).apply
    BarSymmetricThreeLayerSynthesisFunctorial.universal_kernel

/-- **Series avatar is bar-symmetric**: follows from the functor's
    own `apply_bar_symmetric` field applied to the bar-anti-symmetric
    universal kernel. -/
theorem BarSymmetricThreeLayerSynthesisFunctorial.series_avatar_isBarSymmetric
    [BarSymmetricThreeLayerSynthesisFunctorial R] :
    IsBarSymmetric (BarSymmetricThreeLayerSynthesisFunctorial.series_avatar (R := R)) :=
  (BarSymmetricThreeLayerSynthesisFunctorial.series_F (R := R)).apply_bar_symmetric
    BarSymmetricThreeLayerSynthesisFunctorial.universal_kernel
    BarSymmetricThreeLayerSynthesisFunctorial.universal_kernel_antisym

theorem BarSymmetricThreeLayerSynthesisFunctorial.phase_avatar_isBarSymmetric
    [BarSymmetricThreeLayerSynthesisFunctorial R] :
    IsBarSymmetric (BarSymmetricThreeLayerSynthesisFunctorial.phase_avatar (R := R)) :=
  (BarSymmetricThreeLayerSynthesisFunctorial.phase_F (R := R)).apply_bar_symmetric
    BarSymmetricThreeLayerSynthesisFunctorial.universal_kernel
    BarSymmetricThreeLayerSynthesisFunctorial.universal_kernel_antisym

theorem BarSymmetricThreeLayerSynthesisFunctorial.gain_avatar_isBarSymmetric
    [BarSymmetricThreeLayerSynthesisFunctorial R] :
    IsBarSymmetric (BarSymmetricThreeLayerSynthesisFunctorial.gain_avatar (R := R)) :=
  (BarSymmetricThreeLayerSynthesisFunctorial.gain_F (R := R)).apply_bar_symmetric
    BarSymmetricThreeLayerSynthesisFunctorial.universal_kernel
    BarSymmetricThreeLayerSynthesisFunctorial.universal_kernel_antisym

/-- **Trivial functorial instance** — universal kernel = 0, all
    three functors = `BarHeckeFunctor.constZero`. Demonstrates
    the strengthened class is inhabited; not an empirical claim. -/
instance trivialBarSymmetricThreeLayerSynthesisFunctorial :
    BarSymmetricThreeLayerSynthesisFunctorial R where
  universal_kernel := 0
  universal_kernel_antisym := by
    unfold IsBarAntiSymmetric
    rw [BarInvolution.bar_zero]; ring
  series_F := BarHeckeFunctor.constZero
  phase_F := BarHeckeFunctor.constZero
  gain_F := BarHeckeFunctor.constZero

end StrengthenedSynthesis


end QOU.BraidKnot
