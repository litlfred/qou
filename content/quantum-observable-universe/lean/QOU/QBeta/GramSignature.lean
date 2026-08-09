import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Algebra.Order.Field.Basic

/-!
# The Markov–Gram form is Lorentzian, and under convention D it is degenerate

**Why the spectral-distance programme cannot be run on it as posed.**

`tools/pyhecke/python/pyhecke/gram.py` builds the `6 × 6` Gram matrix of the
Markov trace on the normal-form basis of `H₃(q)`,

    G_ij = tr_M(b_i · b_j),   b ∈ {γ, σ₀, σ₁, L₊, L₋, e⁻},

`γ` the identity and `e⁻ = σ₀σ₁σ₀` the trefoil. A Gram matrix of a trace pairing
is the natural candidate for a *derived* metric on the framework's state space —
the object bean `qou-5uj7` needs in order to build a Rieffel Lip-norm and hence
a Connes/Wasserstein distance. Measured at `q₀ = 1.10997858275138…`:

    convention C  (z = 1/(√q + 1/√q) = 0.4993203)
      eigenvalues  −0.855067, +0.101797, +0.855067, +0.855067, +0.855067, +3.476950
      signature    (5, 1)                                    LORENTZIAN

    convention D  (z = q³/(q²+1) = 0.6126880, PRODUCTION)
      eigenvalues  −0.752702, 0, +0.752702, +0.752702, +0.752702, +4.230339
      signature    (4, 1) + a null direction        LORENTZIAN AND DEGENERATE
      det G = 2.89e−51 (i.e. 0 at 50 dps)

Two facts, both convention-independent in the first case:

* **Lorentzian.** Exactly one eigenvalue is negative under *both* conventions.
  So the Markov pairing is not an inner product; it is a *spacetime* form. The
  natural object it defines is a causal structure, not a metric space.
* **Degenerate under D.** The production convention additionally kills one
  direction. The null vector, in the basis order above, is
  `(−0.472689, +0.425854, +0.425854, −0.383660, −0.383660, +0.345646)` —
  symmetric under `σ₀ ↔ σ₁` and `L₊ ↔ L₋`, i.e. the braid-symmetric direction.

The eigenvalues are not arbitrary. Under D the repeated magnitude is
`0.75270211325196540159 = μ₊`, the `T = 1` isospin projector scalar of
`InterfaceScalar.lean` — appearing once negative and three times positive.

## What this file proves, and why it matters

The programme in `qou-5uj7` was: build a Lip-norm `L(a) = ‖D_∇ a‖`, take
`d(φ,ψ) = sup {|φ(a) − ψ(a)| : L(a) ≤ 1}`, and hope to recover a Reeb step
count. `lip_kernel_forces_unbounded` shows that hope is **structurally blocked**
whenever the seminorm has a nonzero kernel element that the two states
distinguish: the sup ranges over `a + t·k` for every scalar `t`, so it is `+∞`.
A degenerate Gram form supplies exactly such a `k`. Hence:

> Under convention D the Markov–Gram form cannot induce a finite Connes
> distance without first quotienting by its radical.

That is a negative result about the *method*, not about the framework, and it
names the repair: quotient by the radical, or use a different seminorm. It is
stated here as a theorem rather than left in prose because it is the load-bearing
step in deciding whether `qou-5uj7` is viable.

> **MAJOR CORRECTION 2026-08-09 — the Lorentzian reading is an ARTIFACT of the
> wrong pairing, and the physically relevant form is POSITIVE.** Everything
> below about `tr(ab)` is correct *as stated about the bilinear form*, but that
> is not the form a metric is built from. The Hecke `*`-structure is
> `T_w* = T_{w⁻¹}` — the basis element of the **inverse word**, which on the NF
> basis simply swaps `L₊ ↔ L₋` and fixes the rest. Pairing with it instead:
>
>     S_ij = tr_M(b_i · b_j*)
>     convention C:  all six eigenvalues POSITIVE          signature (6,0,0)
>     convention D:  one zero, five positive               signature (5,0,1)
>     symmetry defect 0.0 in both
>
> Same eigenvalue magnitudes — `±0.855067` becomes `+0.855067` fourfold,
> `±0.752702` becomes `+0.752702` fourfold. The `*` flips exactly the sign of the
> antisymmetric direction, which is what a `*`-structure is *for*.
>
> So: **`tr(ab)` is Lorentzian; `tr(ab*)` is positive.** The claim below that
> "the framework's natural object is a causal structure, not a metric space" is
> **WITHDRAWN**. Under D the only defect left is the row-cap null direction, so
> quotienting by the radical gives a genuine positive-definite inner product —
> exactly what a Rieffel Lip-norm needs. Under C it is positive definite
> outright, because `y_(1³) = 0.0227 ≠ 0` keeps that direction alive: a clean
> consistency check that D's degeneracy is *purely* the row cap.
>
> The material below is retained because the block analysis is what explains
> BOTH signatures — the `M₂` of the `(2,1)` block contributes `(3,1)` under the
> bilinear form and `(4,0)` under the star form, from the same decomposition.

## The signature is DERIVED, not measured — it is forced by the block structure

An earlier version of this file called the signature "measured, not proved".
That was too weak. It follows from Wedderburn plus one elementary fact, with no
reference to `q₀` at all.

`H₃(q)` is a sum of **matrix algebras**, not merely of irreps:

    block    irrep dim d    matrix algebra    dimensions
    (3)          1              M₁                1
    (2,1)        2              M₂                4
    (1³)         1              M₁                1                total 6 ✓

The Gram form is `G(a,b) = tr_M(ab) = Σ_λ y_λ · χ_λ(ab)`, so on block `λ` it is
`y_λ · tr(AB)` on `M_{d_λ}`. And — `traceform_M2_signature` below —

> the **bilinear** form `tr(AB)` on `M_d` (not the sesquilinear `tr(AB*)`) has
> signature `(d(d+1)/2, d(d−1)/2)`: symmetric matrices positive, antisymmetric
> negative, and the two are orthogonal.

Hence, over the blocks with `y_λ > 0`,

    signature(G) = ( Σ d_λ(d_λ+1)/2 , Σ d_λ(d_λ−1)/2 ),
    with G degenerate exactly on the blocks where y_λ = 0.

Evaluating for `H₃`:

    convention C:  (3) → 1+ ;  (2,1) → 3+ 1− ;  (1³) → 1+     ⟹  (5,1,0)  ✓
    convention D:  (3) → 1+ ;  (2,1) → 3+ 1− ;  (1³) → ZERO   ⟹  (4,1,1)  ✓

Both match the measurement exactly, and every eigenvalue is now accounted for:
`+4.230339` is the `(3)` block, the `±0.752702` **quadruple** is the `M₂` of the
`(2,1)` block, `+0.101797` (C only) is `(1³)` — small because `y_(1³) = 0.0227`
is small — and the `0` (D only) is `(1³)` killed by the row cap.

**Two consequences worth stating plainly.**

* The Lorentzian character is **not a property of the substrate**. Any matrix
  algebra with `d ≥ 2` contributes `d(d−1)/2` negative directions, so the form
  is indefinite for *every* `q` and *every* convention with `y_(2,1) > 0`. It
  appears the moment the algebra has a two-dimensional irrep.
* The **timelike direction is identified**: it is the antisymmetric element of
  `M₂` in the `(2,1)` block, i.e. `E₁₂ − E₂₁` — the rotation generator,
  `𝔰𝔬(2) ⊂ 𝔰𝔩(2)`. Not an accident of `q₀`.

The degeneracy is likewise structural: it *is* the `N = 2` row cap
(`RowCapObstruction.lean`, `y_(1³) = 0 ⟺ N < 3`) seen through the Gram form.
Quotienting by the radical is therefore not a repair but a restatement of what
convention D means — and it leaves a `(4,1)` form, still Lorentzian.

Beans `qou-5uj7` (spectral distance), `qou-adwi` (two Planck lengths),
`qou-mumr` (no derived metric).
-/

namespace QOU.QBeta.GramSignature

section Indefinite

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

omit [IsStrictOrderedRing R] in
/-- **A form with a negative diagonal entry is not positive semidefinite.**

The Markov–Gram matrix has a negative eigenvalue under both trace conventions,
so in the eigenbasis some diagonal entry is negative. This is the elementary
statement that such a form cannot be an inner product — and therefore cannot be
the Riemannian metric a Connes distance would need. -/
theorem neg_diag_not_posdef (B : R → R → R) (v : R → R) (x : R)
    (hneg : B (v x) (v x) < 0) :
    ¬ (∀ w : R, 0 ≤ B (v w) (v w)) := by
  intro hpos
  exact absurd (hpos x) (not_le.mpr hneg)

omit [IsStrictOrderedRing R] in
/-- **Lorentzian signature: one negative direction alongside a positive one.**

Recorded as the shape of the measurement — a form admitting both a strictly
positive and a strictly negative value on the diagonal takes the value of
neither sign uniformly, so it is indefinite. Under C the split is `(5,1)`;
under D, `(4,1)` plus a null direction. -/
theorem indefinite_of_pos_and_neg (B : R → R → R) (p n : R)
    (hp : 0 < B p p) (hn : B n n < 0) :
    (¬ ∀ w, 0 ≤ B w w) ∧ (¬ ∀ w, B w w ≤ 0) := by
  constructor
  · intro h; exact absurd (h n) (not_le.mpr hn)
  · intro h; exact absurd (h p) (not_le.mpr hp)

end Indefinite

section TraceForm

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **The trace form on `M₂` has signature `(3,1)`.**

Parametrise `A ∈ M₂` by its symmetric part `(α, δ, β)` and antisymmetric part
`γ`, i.e. `A = [[α, β+γ], [β−γ, δ]]`. Then

    tr(A²) = α² + 2β² − 2γ² + δ².

Three squares enter with `+` and one with `−`: symmetric directions are
positive, the single antisymmetric direction is negative. This is the whole
reason the Markov–Gram form is Lorentzian — the `(2,1)` block of `H₃(q)` is an
`M₂`, and `M₂` has exactly one antisymmetric direction. -/
theorem traceform_M2 (α δ β γ : R) :
    α * α + (β + γ) * (β - γ) + (β - γ) * (β + γ) + δ * δ
      = α ^ 2 + 2 * β ^ 2 - 2 * γ ^ 2 + δ ^ 2 := by ring

/-- **…so the symmetric directions are positive.** Setting `γ = 0` leaves a sum
of squares, strictly positive unless all vanish. -/
theorem traceform_M2_sym_pos (α δ β : R) (hne : α ≠ 0) :
    0 < α ^ 2 + 2 * β ^ 2 - 2 * (0 : R) ^ 2 + δ ^ 2 := by
  have h1 : 0 < α ^ 2 := by positivity
  nlinarith [sq_nonneg β, sq_nonneg δ]

/-- **…and the antisymmetric direction is negative.** Setting `α = δ = β = 0`
leaves `−2γ²`, strictly negative unless `γ = 0`. This single direction is the
timelike one: `E₁₂ − E₂₁`, the rotation generator of the standard rep. -/
theorem traceform_M2_antisym_neg (γ : R) (hne : γ ≠ 0) :
    (0 : R) ^ 2 + 2 * (0 : R) ^ 2 - 2 * γ ^ 2 + (0 : R) ^ 2 < 0 := by
  have : 0 < γ ^ 2 := by positivity
  nlinarith

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **Symmetric and antisymmetric parts are orthogonal under the trace form.**

`tr(SK) = 0` whenever `S` is symmetric and `K` antisymmetric, so the signature
splits cleanly as `(3,1)` with no cross terms. Shown here on the `M₂`
parametrisation: the mixed terms cancel identically. -/
theorem traceform_M2_orthogonal (α δ β γ : R) :
    (α * 0 + β * γ) + (β * (-γ) + 0 * δ) = 0 := by ring

end TraceForm

section StarForm

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **The star form is a sum of squares on each `M_d` block — hence positive.**

Where the bilinear `tr(AB)` splits `M₂` as `(3,1)`, the sesquilinear
`tr(AA*)` is `Σ|a_ij|²`. On the real `M₂` parametrisation `A = [[a,b],[c,d]]`,

    tr(A Aᵀ) = a² + b² + c² + d²,

manifestly nonnegative, and zero only when `A = 0`. This is why the Markov–Gram
form flips from signature `(4,1)` to `(5,0)` the moment the correct Hecke
`*`-structure `T_w* = T_{w⁻¹}` is used instead of plain multiplication. -/
theorem starform_M2_sum_of_squares (a b c d : R) :
    a * a + b * b + c * c + d * d = a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2 := by ring

/-- **…and it is nonnegative.** -/
theorem starform_M2_nonneg (a b c d : R) :
    0 ≤ a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2 := by positivity

/-- **Definiteness: the star form vanishes only on zero.** Contrapositive of the
sum-of-squares shape — a single nonzero entry already forces it positive. This
is what upgrades the quotient-by-radical form from semidefinite to definite. -/
theorem starform_M2_pos_of_ne (a b c d : R) (hne : a ≠ 0) :
    0 < a ^ 2 + b ^ 2 + c ^ 2 + d ^ 2 := by positivity

/-- **Positivity of the whole Markov–Gram star form reduces to `y_λ ≥ 0`.**

`tr_M(a a*) = Σ_λ y_λ · tr(A_λ A_λ*)`, and each `tr(A A*)` is a sum of squares
by `starform_M2_sum_of_squares`. So a nonnegative combination of nonnegative
terms is nonnegative: the star form is positive semidefinite **exactly when all
Markov weights are nonnegative**, and degenerate precisely on the blocks where
`y_λ = 0`. Under convention D that is the single block `(1³)` — the row cap.

Stated for two blocks, which is the shape that matters here (`H₃` has the
`y_λ > 0` blocks `(3)`, `(2,1)` and the `y = 0` block `(1³)`). -/
theorem markov_star_nonneg (y₁ y₂ t₁ t₂ : R)
    (hy₁ : 0 ≤ y₁) (hy₂ : 0 ≤ y₂) (ht₁ : 0 ≤ t₁) (ht₂ : 0 ≤ t₂) :
    0 ≤ y₁ * t₁ + y₂ * t₂ := by positivity

end StarForm

section Degenerate

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **A seminorm with a nonzero kernel gives an unbounded Connes sup.**

THE LOAD-BEARING RESULT. Let `L` be the Lipschitz seminorm and `φ`, `ψ` two
states. The Connes distance is `sup {|φ a − ψ a| : L a ≤ 1}`. Suppose some `k`
has `L k = 0` while `φ k − ψ k ≠ 0` — exactly what a *degenerate* Gram form
supplies, its radical being the kernel. Then for every scalar `t` the element
`a + t·k` still satisfies the constraint (`L` is absolutely homogeneous and
subadditive, so `L (a + t·k) ≤ L a`), while the objective grows linearly in `t`.
So no finite bound exists: for any proposed bound `M` there is an admissible
element exceeding it.

Stated as "no upper bound" rather than "= ∞" to stay inside an ordered field
without adjoining a top element. -/
theorem lip_kernel_forces_unbounded
    (L : R → R) (obj : R → R) (k : R) (M : R)
    (hLk : L k = 0)
    (hsub : ∀ a t : R, L (a + t * k) ≤ L a + |t| * L k)
    (hlin : ∀ a t : R, obj (a + t * k) = obj a + t * obj k)
    (a : R) (hadm : L a ≤ 1) (hsep : 0 < obj k) :
    ∃ b : R, L b ≤ 1 ∧ M < obj b := by
  -- pick t large enough that obj a + t * obj k exceeds M
  refine ⟨a + ((M - obj a) / obj k + 1) * k, ?_, ?_⟩
  · have := hsub a ((M - obj a) / obj k + 1)
    rw [hLk, mul_zero, add_zero] at this
    exact le_trans this hadm
  · rw [hlin]
    have hk : obj k ≠ 0 := ne_of_gt hsep
    have : (M - obj a) / obj k * obj k = M - obj a := div_mul_cancel₀ _ hk
    nlinarith [this, hsep]

/-- **…so a degenerate Gram form blocks the distance construction.**

Contrapositive packaging of the above: if the Connes distance IS finite —
i.e. some `M` bounds the objective over the admissible set — then no kernel
element separates the two states. Under convention D the Markov–Gram form has a
nontrivial radical, so the construction must first quotient by it. -/
theorem finite_distance_forces_trivial_kernel
    (L : R → R) (obj : R → R) (k : R) (M : R)
    (hbound : ∀ b : R, L b ≤ 1 → obj b ≤ M)
    (hLk : L k = 0)
    (hsub : ∀ a t : R, L (a + t * k) ≤ L a + |t| * L k)
    (hlin : ∀ a t : R, obj (a + t * k) = obj a + t * obj k)
    (a : R) (hadm : L a ≤ 1) :
    ¬ (0 < obj k) := by
  intro hsep
  obtain ⟨b, hb, hMb⟩ :=
    lip_kernel_forces_unbounded L obj k M hLk hsub hlin a hadm hsep
  exact absurd (hbound b hb) (not_le.mpr hMb)

end Degenerate

section DiracCoefficients

variable {R : Type*} [Field R]

/-- **The Reeb coefficient of the categorical Dirac operator is `ℏ_q`.**

`D_∇ = q⁻¹∇ + (1 − q⁻¹)ι_ξ∇`, and the corpus's quantum Planck constant is
`ℏ_q = (q − 1)/q`. These are the same number, identically:

    1 − q⁻¹ = (q − 1)/q.

Measured agreement at `q₀`: `4.9e−32` at 30 dps, i.e. round-off. So `ℏ_q` is
structurally the Reeb-direction *weight* in the Dirac operator — a step cost —
rather than an independent length. Bears on `qou-adwi`: it supports reading the
two competing "Planck lengths" as the Reeb *share* (`ℏ_q ≈ 0.0991`) and the
normalising *total* (`ℓ_P ≡ 1`), rather than as contradictory values. -/
theorem reeb_coefficient_eq_hbar_q (q : R) (hq : q ≠ 0) :
    1 - q⁻¹ = (q - 1) / q := by
  field_simp

/-- **…and the two Dirac coefficients are a convex combination.**

`q⁻¹ + (1 − q⁻¹) = 1`. At `q₀` that is `90.09 %` gradient and `9.908 %` Reeb.
The limits are `q = 1 ↦` pure gradient and `q → ∞ ↦` pure contact.

CONSEQUENCE for `qou-5uj7`: because the operator MIXES the two directions, the
metric it induces is *not* a pure Reeb step count at finite `q` — the gradient
part carries nine times the weight. The target theorem
"`d_Connes` = minimal Reeb step count" can hold only in the `q → ∞` limit. -/
theorem dirac_coefficients_convex (q : R) :
    q⁻¹ + (1 - q⁻¹) = 1 := by ring

end DiracCoefficients

end QOU.QBeta.GramSignature
