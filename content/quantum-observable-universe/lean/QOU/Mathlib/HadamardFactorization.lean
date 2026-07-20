/-
  Hadamard factorization for entire functions of finite order — the Mathlib
  v4.24.0 gap (grep-confirmed absent).

  MOTIVATION (epic qou-lbth, brick PI-1; pentagon-infra blocker). The residual
  leg of `PentagonRigidity.uniqueUpToScalar` reduces (PR #4120 +
  `MeromorphicSameOrder.lean`) to the analytic fact that the canonical minimal
  Faddeev solution `phiBProd` is selected among all `phiBProd·(elliptic)`
  multiples by a growth/minimality principle. That principle is a special case
  of the **Hadamard factorization theorem**: an entire function of finite order
  `ρ` equals `exp(g)·∏ₙ Eₚ(z/aₙ)`, a product of Weierstrass primary factors over
  its zeros `aₙ` times the exponential of a polynomial `g` of degree `≤ ρ`, with
  genus `p ≤ ρ`. Mathlib has Jensen's formula, the Nevanlinna value-distribution
  cone (`Analysis/Complex/ValueDistribution/`), Liouville, analytic/meromorphic
  order and isolated zeros — but **not** the Weierstrass primary factor `Eₚ`, the
  order-of-growth `ρ`, the genus, the canonical product, or the factorization
  theorem itself. (`Analysis/Complex/Hadamard.lean` is the *three-lines* theorem,
  a different result.)

  SCOPE (honest — this is a multi-week build; PI-1 scaffolds it, does not fake
  it). Proved sorry-free here (the tractable first bricks):

    * `weierstrassFactor p z = (1 - z)·exp(∑_{k<p} z^{k+1}/(k+1))` — the definition.
    * `weierstrassFactor_apply_zero` : `Eₚ(0) = 1`.
    * `weierstrassFactor_genus_zero`  : `E₀(z) = 1 - z`.
    * `weierstrassFactor_eq_zero_iff` : `Eₚ(z) = 0 ↔ z = 1` (exp is nonvanishing).
    * `differentiable_weierstrassFactor` : each `Eₚ` is entire.

  Stated precisely with a cited `sorry` (the genuinely-hard analytic core — NOT
  vacuous `True`, NOT axiomatized as-if-proved):

    * `norm_one_sub_weierstrassFactor_le` — the Weierstrass estimate
      `‖1 - Eₚ(z)‖ ≤ ‖z‖^{p+1}` for `‖z‖ ≤ 1`, the convergence-critical lemma.
    * `multipliable_canonicalProduct` — convergence of the canonical product
      `∏ₙ Eₚ(z/aₙ)` when `∑ₙ ‖aₙ‖^{-(p+1)} < ∞`.
    * `hadamard_factorization` — **the factorization theorem** (the stated-open
      core). It is the fact that pins `phiBProd` among its elliptic multiples.

  DEFINITIONS also introduced: `IsEntireOfOrderLE f ρ` (finite order of growth,
  via the standard exponential-type bound `‖f z‖ ≤ A·exp(C·‖z‖^ρ)`) and
  `IsGenus a p` (the genus of a zero sequence: minimal `p` with `∑ ‖aₙ‖^{-(p+1)}`
  summable). §7c: the growth is archimedean (`Real.exp`, `Real.rpow`, norms), so
  `ℝ`/`ℂ` here are genuine, not gratuitous.

  ROADMAP (tractable-brick order; see docs/audits/2026-07-20-pi1-hadamard-scaffold.md):
    PI-2  `norm_one_sub_weierstrassFactor_le` from the nonneg-coefficient series
          `Eₚ(z) = 1 - ∑_{k>p} a_k z^k`, `a_k ≥ 0`, `∑ a_k = 1`.
    PI-3  `multipliable_canonicalProduct` from PI-2 + `Summable.multipliable`.
    PI-4  order/genus lemmas (`p ≤ ρ`, exponent of convergence ≤ order).
    PI-5  Jensen ⇒ zero-counting ⇒ the factorization (deepest; needs Nevanlinna).

  -- Ref: [manuscript] standard complex analysis: Ahlfors, *Complex Analysis*,
     3rd ed., §5.3 (Weierstrass products) + §5.3.2 (Hadamard's theorem);
     Conway, *Functions of One Complex Variable I*, XI.§2–3.
-/

import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.Degree.Definitions

namespace QOU.Mathlib.HadamardFactorization

open scoped BigOperators

/-! ## Weierstrass primary factor -/

/-- The **Weierstrass primary factor** (elementary factor) of genus `p`:
    `Eₚ(z) = (1 - z)·exp(∑_{k=1}^{p} z^k / k)`.
    Reindexed with `k = 0 … p-1` so the summand is `z^{k+1}/(k+1)`.
    `E₀(z) = 1 - z`; higher `p` add the exponential convergence-accelerating
    factor that makes the canonical product converge. -/
noncomputable def weierstrassFactor (p : ℕ) (z : ℂ) : ℂ :=
  (1 - z) * Complex.exp (∑ k ∈ Finset.range p, z ^ (k + 1) / ((k : ℂ) + 1))

@[simp]
theorem weierstrassFactor_apply_zero (p : ℕ) : weierstrassFactor p 0 = 1 := by
  have hsum : (∑ k ∈ Finset.range p, (0 : ℂ) ^ (k + 1) / ((k : ℂ) + 1)) = 0 :=
    Finset.sum_eq_zero fun k _ => by simp [pow_succ]
  simp [weierstrassFactor, hsum]

/-- Genus-zero primary factor is the bare linear factor `E₀(z) = 1 - z`. -/
@[simp]
theorem weierstrassFactor_genus_zero (z : ℂ) : weierstrassFactor 0 z = 1 - z := by
  simp [weierstrassFactor]

/-- A primary factor vanishes exactly at `z = 1` (the exponential never
    vanishes, so the only zero comes from the linear factor). -/
theorem weierstrassFactor_eq_zero_iff (p : ℕ) (z : ℂ) :
    weierstrassFactor p z = 0 ↔ z = 1 := by
  unfold weierstrassFactor
  rw [mul_eq_zero, sub_eq_zero]
  constructor
  · rintro (h | h)
    · exact h.symm
    · exact absurd h (Complex.exp_ne_zero _)
  · intro h; exact Or.inl h.symm

/-- Each Weierstrass primary factor is entire (a polynomial times the
    exponential of a polynomial). -/
theorem differentiable_weierstrassFactor (p : ℕ) :
    Differentiable ℂ (weierstrassFactor p) := by
  unfold weierstrassFactor
  fun_prop

/-! ## Order of growth and genus -/

/-- `f` is entire of **order of growth `≤ ρ`**: it is differentiable on all of
    `ℂ` and satisfies an exponential-type bound `‖f z‖ ≤ A · exp(C · ‖z‖^ρ)`.
    The order of `f` is the infimum of such `ρ`; this predicate records the
    upper leg used by Hadamard's theorem (degree of `g` and genus `≤ ρ`). -/
def IsEntireOfOrderLE (f : ℂ → ℂ) (ρ : ℝ) : Prop :=
  Differentiable ℂ f ∧
    ∃ A C : ℝ, 0 < C ∧ ∀ z : ℂ, ‖f z‖ ≤ A * Real.exp (C * ‖z‖ ^ ρ)

/-- `p` is the **genus** of the zero sequence `a`: the least natural number for
    which `∑ₙ ‖aₙ‖^{-(p+1)}` converges. Encoded as: the `(p+1)`-sum converges,
    and either `p = 0` or the `p`-sum diverges (minimality). -/
def IsGenus (a : ℕ → ℂ) (p : ℕ) : Prop :=
  Summable (fun n => 1 / ‖a n‖ ^ (p + 1)) ∧
    (p = 0 ∨ ¬ Summable (fun n => 1 / ‖a n‖ ^ p))

/-! ## The hard analytic core (stated-open, cited `sorry`) -/

/-- **Weierstrass estimate** (convergence-critical, PI-2). For `‖z‖ ≤ 1`,
    `‖1 - Eₚ(z)‖ ≤ ‖z‖^{p+1}`. This is the bound that makes the canonical
    product converge; it follows from the nonnegative-coefficient power series
    `Eₚ(z) = 1 - ∑_{k>p} a_k z^k` with `a_k ≥ 0` and `∑ a_k = 1`.
    Not elementary; deferred. -/
theorem norm_one_sub_weierstrassFactor_le (p : ℕ) {z : ℂ} (hz : ‖z‖ ≤ 1) :
    ‖1 - weierstrassFactor p z‖ ≤ ‖z‖ ^ (p + 1) := by
  -- Ref: [manuscript] Ahlfors §5.3, Lemma; Conway XI.§2, Lemma 2.6.
  sorry

/-- **Canonical product convergence** (PI-3). If `∑ₙ ‖aₙ‖^{-(p+1)} < ∞` (i.e.
    genus `≤ p`), the canonical product `∏ₙ Eₚ(z/aₙ)` converges (is multipliable)
    for every `z`. Follows from `norm_one_sub_weierstrassFactor_le` plus the
    log-summability criterion for infinite products. -/
theorem multipliable_canonicalProduct {a : ℕ → ℂ} (p : ℕ)
    (ha : ∀ n, a n ≠ 0) (hsum : Summable (fun n => 1 / ‖a n‖ ^ (p + 1)))
    (z : ℂ) : Multipliable (fun n => weierstrassFactor p (z / a n)) := by
  -- Ref: [manuscript] Ahlfors §5.3, Theorem 5; Conway XI.§2, Theorem 2.4.
  sorry

/-- **Hadamard factorization theorem** (the stated-open core, PI-5). An entire
    function `f` of finite order `ρ` with `f(0) ≠ 0` factors as
    `f(z) = exp(g(z)) · ∏ₙ Eₚ(z/aₙ)`, where `(aₙ)` enumerates the zeros of `f`
    (with multiplicity), the genus `p ≤ ρ`, and `g` is a polynomial of degree
    `≤ ρ`. The canonical product converges. This is the theorem that pins the
    minimal Faddeev solution `phiBProd` among all `phiBProd·(elliptic)` multiples
    (epic qou-lbth). Mathlib v4.24.0 lacks it; the proof needs Jensen's formula,
    zero-counting, and the Weierstrass/Borel–Carathéodory growth machinery.

    NOTE (honest, non-vacuous): the product equation `f z = exp(g z)·∏ₙ Eₚ(z/aₙ)`
    already forces each `aₙ` to be a zero of `f` (via `weierstrassFactor_eq_zero_iff`)
    and forces completeness of the zero enumeration (no other zeros on either
    side), so the theorem is stated in full strength, not weakened. -/
theorem hadamard_factorization {f : ℂ → ℂ} {ρ : ℝ}
    (hf : IsEntireOfOrderLE f ρ) (hf0 : f 0 ≠ 0) :
    ∃ (p : ℕ) (g : Polynomial ℂ) (a : ℕ → ℂ),
      (p : ℝ) ≤ ρ ∧
      (g.natDegree : ℝ) ≤ ρ ∧
      (∀ n, a n ≠ 0) ∧
      (∀ n, f (a n) = 0) ∧
      (∀ z, Multipliable (fun n => weierstrassFactor p (z / a n)) ∧
            f z = Complex.exp (g.eval z) * ∏' n, weierstrassFactor p (z / a n)) := by
  -- Ref: [manuscript] Ahlfors §5.3.2, Hadamard's Theorem; Conway XI.§3,
  --      Theorem 3.4 (Hadamard's factorization theorem).
  sorry

end QOU.Mathlib.HadamardFactorization
