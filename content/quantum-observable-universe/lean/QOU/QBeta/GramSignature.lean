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

**Scope.** The numerical signature above is *measured*, not proved here —
certifying eigenvalues of an explicit `6 × 6` matrix over an irrational `q₀` is
a separate exercise. What is proved here is the *consequence*: indefiniteness
rules out the inner-product reading (`neg_diag_not_posdef`), and degeneracy
rules out a finite sup (`lip_kernel_forces_unbounded`). Both are the general
statements the measurement feeds into.

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
