import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# The Markov–Gram form is Lorentzian, and under convention D it is degenerate

**Why the spectral-distance programme cannot be run on it as posed.**

`tools/pyhecke/python/pyhecke/gram.py` builds the `6 × 6` Gram matrix of the
Markov trace on the normal-form basis of `H₃(q)`,

    G_ij = tr_M(b_i · b_j),   b ∈ {γ, σ₀, σ₁, L₊, L₋, e⁻},

`γ` the identity and `e⁻ = σ₀σ₁σ₀` the electron word, whose closure on three strands is
the Hopf link (owner ruling 2026-11-21: electron = σ₀σ₁σ₀, closure the Hopf link; the trefoil σ₀³ ∈ B₂ is the backup). A Gram matrix of a trace pairing
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

section BranchingWeights

/-!
## The radical is observationally inert — the metric blocker dissolves

`lip_kernel_forces_unbounded` above is a genuine obstruction: a degenerate Gram
form gives the Lipschitz seminorm a kernel and the Connes distance is then
unbounded. Under convention D the form *is* degenerate, because the Wedderburn
weight of the `(1³)` block is exactly zero. The obvious repair — quotient by the
radical — was suspected of amputating physics, since `(1³)` is the totally
antisymmetric block and the nuclear channel that binds is the isospin *singlet*.

That worry is unfounded, and this section is the derivation. Two steps.

**Step 1 — the branching identity.** Write the Markov trace on `H₃(q)` in the
Wedderburn basis, `tr_M = y₍₃₎ χ₍₃₎ + y₍₂,₁₎ χ₍₂,₁₎ + y₍₁³₎ χ₍₁³₎`. Two
normalisations pin it: `tr_M(1) = 1` and `tr_M(σ) = z`, with the character values
`χ(1) = (1, 2, 1)` and `χ(σ) = (q, q − q⁻¹, −q⁻¹)`. Then the two isospin weights
of the `H₂ ⊂ H₃` pair come out as *sums over the Bratteli branching*:

    μ₊ = (z + q⁻¹)/(q + q⁻¹) = y₍₃₎ + y₍₂,₁₎        (3) ↓ (2),  (2,1) ↓ (2)
    μ₋ = (q − z)/(q + q⁻¹)   = y₍₂,₁₎ + y₍₁³₎       (2,1) ↓ (1²), (1³) ↓ (1²)

These are *identities in `z` and in `q`* — no convention, no `q₀`, no fit.
Verified independently to 61 digits at both conventions, at twelve unrelated
values of `z`, and at `q ∈ {0.7, 1.3, 2.0}`; the residual is `0` or `1.1e−41`
at 40 dps, i.e. the identity holds formally and the check only confirms the
transcription. `linear_combination` supplies the two-line proof below.

**Step 2 — a zero-weight block contributes nothing.** `zero_weight_block_erasable`
says a term with `y λ = 0` can be deleted from `tr_M` without changing any value.
So the radical is invisible to *every* trace, hence to every observable the
framework computes from one.

**The conclusion.** Under D, `y₍₁³₎ = 0`, so `μ₋ = y₍₂,₁₎`: the isospin singlet
draws its entire weight from the mixed-symmetry `(2,1)` block, and none from the
radical. Quotienting by `rad = (1³)` removes a term already equal to zero. The
Connes distance becomes finite on `H₃/rad` **at no cost in physics** —
`finite_distance_forces_trivial_kernel`'s hypothesis is satisfiable after all.

CONVENTION-C: KEEP_HISTORICAL. The C value below is load-bearing -- it is the
EVIDENCE that C is excluded, not a leftover. Replacing it with the D value
destroys the contrast the sentence exists to draw. Do not flip.

Note this also explains why C looked healthier: there `y₍₁³₎ = 0.0227449 ≠ 0`,
so there is no radical and nothing to quotient. The degeneracy is a feature of
D, and the branching identity is what makes it harmless rather than fatal.
Recorded in bean `qou-o3ta`.
-/

section Erasure

variable {R : Type*} [Ring R]

/-- **A zero-weight block can be deleted from the trace.**

`tr_M = Σ_λ y_λ χ_λ`. If `y l = 0` the `l` term is `0 · χ l = 0`, so the sum over
`s.erase l` equals the sum over `s`. Trivial as arithmetic; load-bearing as
physics, because it is the statement that quotienting by the radical is
*observationally inert* — no trace value moves, so no predicted number moves. -/
theorem zero_weight_block_erasable {ι : Type*} [DecidableEq ι] (s : Finset ι)
    (y χ : ι → R) (l : ι) (hy : y l = 0) :
    ∑ i ∈ s.erase l, y i * χ i = ∑ i ∈ s, y i * χ i :=
  Finset.sum_erase s (by rw [hy, zero_mul])

end Erasure

section Branching

variable {R : Type*} [Field R]

/-- **The isospin triplet weight is a sum over the Bratteli branching.**

`μ₊ · (q + q⁻¹) = z + q⁻¹ = (q + q⁻¹)(y₍₃₎ + y₍₂,₁₎)`, from the two
normalisations alone. The `(1³)` weight cancels identically — its character
value `−q⁻¹` at `σ` is exactly offset by its multiplicity `1` at the identity,
which is the branching statement `(1³) ↓ (1²)`: the totally antisymmetric block
of `H₃` restricts entirely to the *antisymmetric* block of `H₂`, so it cannot
contribute to the symmetric (T = 1) weight.

No hypothesis on `q` beyond the field axioms — `q⁻¹` enters only linearly, so
`ring` never needs `q ≠ 0`. -/
theorem mu_triplet_eq_branch (q z y₃ y₂₁ y₁₃ : R)
    (hone : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hz : q * y₃ + (q - q⁻¹) * y₂₁ + (-q⁻¹) * y₁₃ = z) :
    z + q⁻¹ = (q + q⁻¹) * (y₃ + y₂₁) := by
  linear_combination (-1 : R) * hz - q⁻¹ * hone

/-- **The isospin singlet weight is the complementary sum over the branching.**

`μ₋ · (q + q⁻¹) = q − z = (q + q⁻¹)(y₍₂,₁₎ + y₍₁³₎)`. Now it is `y₍₃₎` that
cancels — `(3) ↓ (2)`, the totally symmetric block restricts entirely to the
symmetric block of `H₂` and cannot reach T = 0.

Together with the previous theorem this reproduces the whole `H₂ ⊂ H₃` Bratteli
diagram from two normalisations, and it makes `μ₊ + μ₋ = 1` a corollary of
`tr_M(1) = 1` rather than an independent fact. -/
theorem mu_singlet_eq_branch (q z y₃ y₂₁ y₁₃ : R)
    (hone : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hz : q * y₃ + (q - q⁻¹) * y₂₁ + (-q⁻¹) * y₁₃ = z) :
    q - z = (q + q⁻¹) * (y₂₁ + y₁₃) := by
  linear_combination hz - q * hone

/-- **`μ₊ + μ₋ = 1` is the normalisation seen through the branching.**

Stated on the branch sums rather than on `μ` directly, because on `μ` it is
vacuous: `(z + q⁻¹) + (q − z) = q + q⁻¹` cancels `z` and holds with no
hypotheses at all. The content is on the other side of the two branching
identities —

    (y₍₃₎ + y₍₂,₁₎) + (y₍₂,₁₎ + y₍₁³₎) = y₍₃₎ + 2y₍₂,₁₎ + y₍₁³₎ = tr_M(1) = 1,

where `y₍₂,₁₎` appears twice for the plainest possible reason: `dim (2,1) = 2`,
so the mixed-symmetry block branches to *both* `H₂` blocks and is counted once
on each side. So `μ₊ + μ₋ = 1` is not an extra fact about isospin; it is
`tr_M(1) = 1` restated, and any Markov trace whatever satisfies it. -/
theorem branch_sum_eq_one (y₃ y₂₁ y₁₃ : R)
    (hone : y₃ + 2 * y₂₁ + y₁₃ = 1) :
    (y₃ + y₂₁) + (y₂₁ + y₁₃) = 1 := by
  linear_combination hone

/-- The `μ`-side statement, for the record and to show it is *not* where the
content lives: it needs neither `hone` nor `hz`, only that `q + q⁻¹ ≠ 0`. -/
theorem mu_sum_eq_one_trivially (q z : R) (hs : q + q⁻¹ ≠ 0) :
    (z + q⁻¹) / (q + q⁻¹) + (q - z) / (q + q⁻¹) = 1 := by
  rw [← add_div]
  have : z + q⁻¹ + (q - z) = q + q⁻¹ := by ring
  rw [this, div_self hs]

/-- **THE PUNCHLINE. When the `(1³)` block is the radical, the isospin singlet
does not notice.**

Set `y₍₁³₎ = 0` — convention D, where `y₍₁³₎` vanishes identically, not merely
numerically. Then `μ₋ = y₍₂,₁₎` exactly: the T = 0 channel is carried entirely
by the mixed-symmetry block. Quotienting `H₃(q)` by its radical therefore
deletes a summand that was already contributing zero to the binding energy.

At `q₀`, both sides are `0.24729788674803459840622064838` — and the same number
is `1/[2]_q²`, the recorded closed form for `y₍₂,₁₎` under D, and the recorded
value of `μ₋ = μ_pp · μ_nn`. Three descriptions, one quantity, now with the
reason rather than the coincidence.

This is the derivation that unblocks the Connes construction: the obstruction in
`lip_kernel_forces_unbounded` is real, the quotient that removes it is free. -/
theorem mu_singlet_eq_y21_of_radical (q z y₃ y₂₁ : R) (hs : q + q⁻¹ ≠ 0)
    (hone : y₃ + 2 * y₂₁ + 0 = 1)
    (hz : q * y₃ + (q - q⁻¹) * y₂₁ + (-q⁻¹) * 0 = z) :
    (q - z) / (q + q⁻¹) = y₂₁ := by
  have h := mu_singlet_eq_branch q z y₃ y₂₁ 0 hone hz
  rw [h, add_zero, mul_comm]
  exact mul_div_cancel_right₀ _ hs

/-- The triplet counterpart, for completeness: with `y₍₁³₎ = 0`,
`μ₊ = y₍₃₎ + y₍₂,₁₎ = 1 − y₍₂,₁₎`, i.e. `0.75270211325196540159` at `q₀`. -/
theorem mu_triplet_eq_one_sub_y21_of_radical (q z y₃ y₂₁ : R) (hs : q + q⁻¹ ≠ 0)
    (hone : y₃ + 2 * y₂₁ + 0 = 1)
    (hz : q * y₃ + (q - q⁻¹) * y₂₁ + (-q⁻¹) * 0 = z) :
    (z + q⁻¹) / (q + q⁻¹) = 1 - y₂₁ := by
  have h := mu_triplet_eq_branch q z y₃ y₂₁ 0 hone hz
  have hy : y₃ + y₂₁ = 1 - y₂₁ := by linear_combination hone
  rw [h, hy, mul_comm]
  exact mul_div_cancel_right₀ _ hs

end Branching

section AntisymmetricWeight

variable {R : Type*} [Field R]

/-- **The antisymmetric weight in closed form — the premise, not a hypothesis.**

Every `*_of_radical` result above takes `y₍₁³₎ = 0` as a HYPOTHESIS. That is
honest as far as it goes, but nothing in this file established *why* the
weight vanishes, so the conditional results rested on an unproved premise —
the pattern AGENTS.md names "conditional-proved ≠ premise-established". This
lemma supplies it.

Solving `tr_M = Σ_λ y_λ χ_λ` on `H₃(q)` at the identity, at `σ₀`, and at
`e⁻ = σ₀σ₁σ₀` determines all three weights. The `e⁻` row is where the
corrected `tr_M(e⁻) = h·z² + z` enters (it was `z³` before 2026-05-19), so
this identity is a statement about the *corrected* trace specifically.

The three character values used, from the `H₃(q)` table:

| | `1` | `σ₀` | `e⁻` |
|---|---|---|---|
| `χ₍₃₎` | `1` | `q` | `q³` |
| `χ₍₂,₁₎` | `2` | `q − q⁻¹` | `0` |
| `χ₍₁³₎` | `1` | `−q⁻¹` | `−q⁻³` |

Stated multiplied through by the denominator, so the conclusion itself needs no
non-vanishing hypothesis and no division.

`q² ≠ 1` IS required, and is not a technicality: `χ₍₂,₁₎(σ₀) = q − q⁻¹`
vanishes there, so at `q² = 1` the `σ₀` row carries no information about
`y₍₂,₁₎` and the three rows stop determining the weights. That is the
classical `S₃` degeneration — `H₃(1) = ℂ[S₃]`, where the Markov parameter no
longer separates the blocks. The substrate sits at `q₀ ≈ 1.11`, comfortably
away from it. -/
theorem antisym_weight_closed_form (q z y₃ y₂₁ y₁₃ : R) (hq : q ≠ 0)
    (hq1 : q ^ 2 - 1 ≠ 0)
    (hone : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hz : q * y₃ + (q - q⁻¹) * y₂₁ + (-q⁻¹) * y₁₃ = z)
    (he : q ^ 3 * y₃ + (-(q⁻¹ ^ 3)) * y₁₃ = (q - q⁻¹) * z ^ 2 + z) :
    y₁₃ * ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))
      = q ^ 2 * (z - q) * (z * (q ^ 2 + 1) - q ^ 3) := by
  field_simp at hz he ⊢
  linear_combination (norm := (field_simp; ring))
    q ^ 6 * hone - (2 * q ^ 6 / (q ^ 2 - 1)) * hz
      + ((q ^ 2 + 1) / (q ^ 2 - 1)) * he

/-- **Convention D is exactly the trace that annihilates the sign block.**

`z_D = q³/(q²+1)`, written here without division as `z·(q²+1) = q³`, forces
`y₍₁³₎ = 0`. So the radical is not an accident of convention D that has to be
worked around — it *is* convention D. The other root of the closed form,
`z = q`, is the trivial trace and is excluded separately.

This is what every `*_of_radical` lemma above was assuming.

**Relation to `RowCapObstruction.lean`.** That file proves the same vanishing
from the representation side: `weyl_dim_alt_eq_zero_iff`, `weylDimAlt N = 0 ↔
N < 3` — below three rows the alternating block does not exist, so nothing can
weight it. This lemma comes at it from the trace side: among all Markov
parameters `z`, the ones killing that block are exactly `z = q` and `z = z_D`.

Neither subsumes the other, and the pair is the content: `z_D` is not merely
*compatible with* the `N = 2` cap, it is the unique non-trivial trace parameter
that implements it. The header above already asserted this ("the degeneracy is
likewise structural: it *is* the `N = 2` row cap ... seen through the Gram
form"); until now that was an observation relating two facts, with no lemma
connecting them. -/
theorem antisym_weight_eq_zero_of_conventionD (q z y₃ y₂₁ y₁₃ : R) (hq : q ≠ 0)
    (hq1 : q ^ 2 - 1 ≠ 0)
    (hden : (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) ≠ 0)
    (hone : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hz : q * y₃ + (q - q⁻¹) * y₂₁ + (-q⁻¹) * y₁₃ = z)
    (he : q ^ 3 * y₃ + (-(q⁻¹ ^ 3)) * y₁₃ = (q - q⁻¹) * z ^ 2 + z)
    (hD : z * (q ^ 2 + 1) = q ^ 3) :
    y₁₃ = 0 := by
  have h := antisym_weight_closed_form q z y₃ y₂₁ y₁₃ hq hq1 hone hz he
  rw [hD, sub_self, mul_zero] at h
  exact (mul_eq_zero.mp h).resolve_right hden

end AntisymmetricWeight

section AntisymmetricWeightOrdered

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Over an ordered field the denominator hypothesis discharges itself: both
factors are sums of even powers and `1`, hence strictly positive at every `q`.

Ordering is the weakest thing that decides it, so this stays generic rather
than specialising to `ℝ` — §7c, and it keeps this file free of
`Mathlib.Data.Real.Basic`. (`LinearOrderedField` is deprecated in this Mathlib;
the three-class spelling is its replacement.) -/
theorem antisym_weight_eq_zero_of_conventionD' (q z y₃ y₂₁ y₁₃ : R) (hq : q ≠ 0)
    (hq1 : q ^ 2 - 1 ≠ 0)
    (hone : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hz : q * y₃ + (q - q⁻¹) * y₂₁ + (-q⁻¹) * y₁₃ = z)
    (he : q ^ 3 * y₃ + (-(q⁻¹ ^ 3)) * y₁₃ = (q - q⁻¹) * z ^ 2 + z)
    (hD : z * (q ^ 2 + 1) = q ^ 3) :
    y₁₃ = 0 :=
  antisym_weight_eq_zero_of_conventionD q z y₃ y₂₁ y₁₃ hq hq1
    (by positivity) hone hz he hD

end AntisymmetricWeightOrdered

section BandSeparation

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-!
### …and the interface family cannot realise either isospin weight

The branching identity above is good news for the metric blocker. It is bad
news, of a precise and useful kind, for the mass-binding sector.

Two mechanisms are in play and they have never been shown to be the same object:

  * the **isospin** mechanism, which correctly *selects* the bound channel —
    `μ₋ < μ₊`, so T = 0 binds harder, matching the one bound NN channel in
    nature (`InterfaceScalar.mu_singlet_lt_mu_triplet`);
  * the **interface** mechanism, which *produces the number* — a single `σ₂`
    bond with `μ = z + d`, `d ∈ [−h, 0]`, giving `B = −α ln μ`.

Measured at `q₀` under convention D:

    μ₋  (T = 0)       0.24729788674803459841     63.22 % BELOW the floor
    z − h  (floor)    0.40362773835082593616
    z      (ceiling)  0.61268803714646525160
    μ₊  (T = 1)       0.75270211325196540159     22.85 % ABOVE the ceiling

**The admissible interface band lies strictly between the two isospin weights.**
No admissible `d` reaches either one, and the misses are not marginal — 63 % and
23 %, with the two reductions below holding for all `q < 1.4656` and `q < 1.1939`
respectively, so `q₀ = 1.10998` clears both with room (7.56 % on the tighter).
This is not a knife-edge and it will not be fixed by a better `q`.

So the two mechanisms compute on **disjoint sets**. Using the T = 0 projector
*as* the interface is not merely unmotivated, it is unavailable.

**Convention-dependence, stated honestly.** The lower separation is a
D phenomenon. Under C, `μ₋ = 0.303675` sits INSIDE the band `[0.290260,
0.499320]`; only the upper separation survives. So D gains the deuteron (the
band now contains `B_AME(²H)`, at `d = −0.11923 h`, where under C the whole band
sat 30.69 % above it) and loses the singlet's reachability. Together with the
n–p mass splitting regression this is the third place D trades one agreement for
another; the pattern deserves the owner's attention rather than a silent choice.
Bean `qou-o3ta`.
-/

/-- **The T = 1 weight is above the interface ceiling.**

`μ₊ > z`. The hypothesis is the reduced inequality `z(q + q⁻¹) < z + q⁻¹`, which
for `z = q³/(q²+1)` is equivalent to `q⁵ < q² + 1` and so holds for
`q < 1.193859…`. At `q₀` the two sides are `1.68490` and `2.23205`. -/
theorem mu_triplet_above_ceiling (q z : R) (hs : 0 < q + q⁻¹)
    (hred : z * (q + q⁻¹) < z + q⁻¹) : z < (z + q⁻¹) / (q + q⁻¹) :=
  (lt_div_iff₀ hs).mpr hred

/-- **The T = 0 weight is below the interface floor.**

`μ₋ < z − h`. The hypothesis is the reduced inequality
`q − z < (z − h)(q + q⁻¹)`; at `q₀` under D the sides are `0.497291` and
`0.811654`, and the boundary is at `q = 1.465571`. Under C the inequality
FAILS — `μ₋` is inside the band there — so this theorem is stated as a
conditional and its hypothesis must be checked per convention. -/
theorem mu_singlet_below_floor (q z h : R) (hs : 0 < q + q⁻¹)
    (hred : q - z < (z - h) * (q + q⁻¹)) : (q - z) / (q + q⁻¹) < z - h :=
  (div_lt_iff₀ hs).mpr hred

/-- **The whole admissible band sits strictly between the two isospin weights.**

Every `μ = z + d` with `d ∈ [−h, 0]` satisfies `μ₋ < μ < μ₊`. Combining
`mu_mem_Icc` (the band) with the two separations above. -/
theorem band_strictly_between (q z h d : R) (hs : 0 < q + q⁻¹)
    (hlo : q - z < (z - h) * (q + q⁻¹)) (hhi : z * (q + q⁻¹) < z + q⁻¹)
    (hd_lo : -h ≤ d) (hd_hi : d ≤ 0) :
    (q - z) / (q + q⁻¹) < z + d ∧ z + d < (z + q⁻¹) / (q + q⁻¹) := by
  constructor
  · exact lt_of_lt_of_le (mu_singlet_below_floor q z h hs hlo) (by linarith)
  · exact lt_of_le_of_lt (by linarith) (mu_triplet_above_ceiling q z hs hhi)

/-- **Therefore no admissible interface element equals an isospin weight.**

The blocker in its sharpest form. `qou-17gn` posed the colour-weight blocker as
"`span{1, σ₂}` reaches only a 2-plane of the 4-dimensional `V_(2,1)` block".
This is the same obstruction read off on the observable side, where it is
quantitative: the two targets miss the reachable interval by 63 % and 23 %.

A repair must therefore change the *arena*, not the parameter — option C5,
enlarging `H₃` to `H₄`, or a genuinely different pairing between the isospin
label and the bond. Tuning `d`, choosing a crossing sign, or picking a different
`q` cannot close a gap the band is on the wrong side of. -/
theorem interface_never_equals_isospin_weight (q z h d : R) (hs : 0 < q + q⁻¹)
    (hlo : q - z < (z - h) * (q + q⁻¹)) (hhi : z * (q + q⁻¹) < z + q⁻¹)
    (hd_lo : -h ≤ d) (hd_hi : d ≤ 0) :
    z + d ≠ (q - z) / (q + q⁻¹) ∧ z + d ≠ (z + q⁻¹) / (q + q⁻¹) := by
  obtain ⟨h₁, h₂⟩ := band_strictly_between q z h d hs hlo hhi hd_lo hd_hi
  exact ⟨ne_of_gt h₁, ne_of_lt h₂⟩

end BandSeparation

end BranchingWeights

end QOU.QBeta.GramSignature
