/-
  Hadamard factorization for entire functions of finite order — the Mathlib
  v4.24.0 gap (grep-confirmed absent).

  ⚠ MOTIVATION RETRACTED 2026-08-08 — THIS CHAIN IS NOT THE ROUTE TO
  `uniqueUpToScalar`. See `docs/audits/2026-08-08-hadamard-vs-liouville-route.md`.

  Two things are wrong with the motivation as stated below.

  (1) `phiBProd` is NOT ENTIRE, so `IsEntireOfOrderLE (phiBProd b) ρ` — whose
      first conjunct is `Differentiable ℂ` — is unavailable at every `ρ`. It is a
      RATIO of two products whose denominator factor vanishes at an explicit
      point for every `b ≠ 0` (`QOU.Mathlib.HadamardApplicability.denFactor_eq_zero`,
      sorry-free). Its two HALVES are entire and Hadamard applies to those
      (`differentiable_numProd`, `differentiable_denProd`), but that is a
      different statement from the one below.

  (2) More decisively, the target does not need this chain at all.
      `QOU.MathlibExt.DoublyPeriodicLiouville` is SORRY-FREE and already reduces
      `uniqueUpToScalar` to two smaller named inputs — `hratio` (bean qou-cons:
      the ratio of two FaddeevPhi solutions is entire, their divisors coinciding)
      and `hibinv` (bean qou-rp5f) — with the doubly-periodic ⇒ constant step
      PROVED. Bean qou-lv34 calls that "the only honest route". Neither remaining
      input is Hadamard factorization, and neither is made easier by it.

      That file also states, correctly and in prose, that `Φ_b` "is meromorphic
      with a genuine zero/pole lattice" — a sibling file in this repository
      contradicted the motivation below before it was written.

  WHAT IS NOT RETRACTED: the bricks. PI-2 (`WeierstrassFactorEstimate`), PI-3
  (`multipliable_canonicalProduct`), `BorelCaratheodory`, and the entirety
  results are correct, sorry-free and reusable Mathlib-gap infrastructure. They
  simply have no current consumer. Do not finish PI-4/PI-5 on the justification
  below; name a target that actually needs canonical products first.

  ORIGINAL MOTIVATION, kept for history (epic qou-lbth, brick PI-1;
  pentagon-infra blocker). The residual
  leg of `PentagonRigidity.uniqueUpToScalar` reduces (PR #4120 +
  `MeromorphicSameOrder.lean`) to the analytic fact that the canonical minimal
  Faddeev solution `phiBProd` is selected among all `phiBProd·(elliptic)`
  multiples by a growth/minimality principle. That principle was claimed to be a
  special case of the **Hadamard factorization theorem**: an entire function of finite order
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
    * `norm_one_sub_weierstrassFactor_le` — the Weierstrass estimate
      `‖1 - Eₚ(z)‖ ≤ ‖z‖^{p+1}` for `‖z‖ ≤ 1`, the convergence-critical lemma.
      PI-2, closed 2026-08-07 in `QOU.Mathlib.WeierstrassFactorEstimate`.
    * `multipliable_canonicalProduct` — convergence of the canonical product
      `∏ₙ Eₚ(z/aₙ)` when `∑ₙ ‖aₙ‖^{-(p+1)} < ∞`. PI-3, closed 2026-08-08.

  Stated precisely with a cited `sorry` (the genuinely-hard analytic core — NOT
  vacuous `True`, NOT axiomatized as-if-proved):

    * `hadamard_factorization` — **the factorization theorem** (the stated-open
      core, PI-5, the ONLY remaining `sorry` in this file). It is the fact that
      pins `phiBProd` among its elliptic multiples.

  DEFINITIONS also introduced: `IsEntireOfOrderLE f ρ` (finite order of growth,
  via the standard exponential-type bound `‖f z‖ ≤ A·exp(C·‖z‖^ρ)`) and
  `IsGenus a p` (the genus of a zero sequence: minimal `p` with `∑ ‖aₙ‖^{-(p+1)}`
  summable). §7c: the growth is archimedean (`Real.exp`, `Real.rpow`, norms), so
  `ℝ`/`ℂ` here are genuine, not gratuitous.

  ROADMAP (tractable-brick order; see docs/audits/2026-07-20-pi1-hadamard-scaffold.md):
    PI-2  DONE (2026-08-07). `norm_one_sub_weierstrassFactor_le` — but NOT from
          the nonneg-coefficient series this roadmap proposed; that route needs
          real power-series machinery. See `WeierstrassFactorEstimate`.
    PI-3  DONE (2026-08-08). `multipliable_canonicalProduct` from PI-2 plus
          `Complex.multipliable_one_add_of_summable`. The roadmap's
          "`Summable.multipliable`" does not exist under that name; the working
          criterion is `Summable f → Multipliable (1 + f)`, and the `‖z‖ ≤ 1`
          side condition of PI-2 holds only EVENTUALLY, which is exactly what
          `Summable.of_norm_bounded_eventually_nat` accepts.
    PI-4  order/genus lemmas (`p ≤ ρ`, exponent of convergence ≤ order).
          Exponent of convergence ≤ order is PROVED (2026-11-20) in
          `QOU.Mathlib.ExponentOfConvergence.summable_divisor_mul_rpow_neg`, via Jensen
          (`QOU.Mathlib.JensenZeroCounting`); genus corollary `summable_divisor_floor_genus`.
    PI-5  progress (2026-11-20). PROVED: the canonical product is entire and of order
          ≤ σ when ∑‖aₙ‖^{-σ} < ∞ (`QOU.Mathlib.CanonicalProductGrowth`); a zero-free
          entire function of order ≤ ρ is exp of a polynomial of degree ≤ ρ
          (`QOU.Mathlib.HadamardZeroFree.exists_polynomial_of_zeroFree`). STILL OPEN:
          enumerating the zeros (divisor → sequence with multiplicity), showing f/P is
          entire and zero-free, and the lower bound on |P| off small discs that gives
          f/P order ≤ ρ (minimum-modulus estimate). So `HasHadamardFactorization`
          below is still an unproved class.
    PI-5  Jensen ⇒ zero-counting ⇒ the factorization (deepest; needs Nevanlinna).

  -- Ref: [leitner2026] standard complex analysis: Ahlfors, *Complex Analysis*,
     3rd ed., §5.3 (Weierstrass products) + §5.3.2 (Hadamard's theorem);
     Conway, *Functions of One Complex Variable I*, XI.§2–3.
-/

import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Summable
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.Degree.Definitions
import QOU.Mathlib.WeierstrassFactorEstimate

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
    product converge.

    PROVED (2026-08-07), sorry-free, in `QOU.Mathlib.WeierstrassFactorEstimate`.

    Not by the textbook route. Ahlfors/Conway argue from the nonneg-coefficient
    power series `Eₚ(z) = 1 - ∑_{k>p} a_k z^k`, which needs real power-series
    machinery. The proof used instead runs through the derivative identity
    `Eₚ'(z) = -z^p·exp(Sₚ(z))` — the telescoping `(1-z)∑_{k<p} z^k = 1 - z^p`
    kills the `-1` — giving `1 - Eₚ(z) = ∫₀¹ z^{p+1} t^p exp(Sₚ(tz)) dt`. The
    constant is exactly `1` because that integral's real total mass is
    `1 - Eₚ(1) = 1` on the nose; the crude bound `exp(H_p)/(p+1)` exceeds `1`
    for every `p ≥ 1` and would not suffice. -/
theorem norm_one_sub_weierstrassFactor_le (p : ℕ) {z : ℂ} (hz : ‖z‖ ≤ 1) :
    ‖1 - weierstrassFactor p z‖ ≤ ‖z‖ ^ (p + 1) := by
  -- Ref: [leitner2026] Ahlfors §5.3, Lemma; Conway XI.§2, Lemma 2.6.
  have hdef : weierstrassFactor p z
      = QOU.Mathlib.WeierstrassFactorEstimate.weierstrassFactor p z := rfl
  rw [hdef]
  exact QOU.Mathlib.WeierstrassFactorEstimate.norm_one_sub_weierstrassFactor_le p hz

/-- **Canonical product convergence** (PI-3). If `∑ₙ ‖aₙ‖^{-(p+1)} < ∞` (i.e.
    genus `≤ p`), the canonical product `∏ₙ Eₚ(z/aₙ)` converges (is multipliable)
    for every `z`. Follows from `norm_one_sub_weierstrassFactor_le` plus the
    log-summability criterion for infinite products. -/
theorem multipliable_canonicalProduct {a : ℕ → ℂ} (p : ℕ)
    (ha : ∀ n, a n ≠ 0) (hsum : Summable (fun n => 1 / ‖a n‖ ^ (p + 1)))
    (z : ℂ) : Multipliable (fun n => weierstrassFactor p (z / a n)) := by
  -- Ref: [leitner2026] Ahlfors §5.3, Theorem 5; Conway XI.§2, Theorem 2.4.
  -- PROVED 2026-08-08. The estimate does the work, but note where the `‖z‖ ≤ 1`
  -- hypothesis is discharged: it is NOT true for every `n`, only eventually.
  -- Summability forces `1/‖aₙ‖^{p+1} → 0`, hence `‖aₙ‖ → ∞`, hence `‖z/aₙ‖ ≤ 1`
  -- off a finite set — and `Summable.of_norm_bounded_eventually_nat` only needs
  -- the bound eventually, so no finite-set surgery is required.
  have hpos : ∀ n, (0 : ℝ) < ‖a n‖ := fun n => norm_pos_iff.mpr (ha n)
  -- Comparing against `1/(‖z‖^{p+1} + 1)` rather than `1/‖z‖^{p+1}` keeps the
  -- constant positive at `z = 0`, avoiding a case split.
  have hc : (0 : ℝ) < 1 / (‖z‖ ^ (p + 1) + 1) := by positivity
  have hev : ∀ᶠ n in Filter.atTop,
      ‖weierstrassFactor p (z / a n) - 1‖ ≤ ‖z‖ ^ (p + 1) * (1 / ‖a n‖ ^ (p + 1)) := by
    filter_upwards [hsum.tendsto_atTop_zero.eventually_lt_const hc] with n hn
    have hA : (0 : ℝ) < ‖a n‖ ^ (p + 1) := pow_pos (hpos n) _
    have hB : (0 : ℝ) < ‖z‖ ^ (p + 1) + 1 := by positivity
    have hbig : ‖z‖ ^ (p + 1) + 1 < ‖a n‖ ^ (p + 1) := lt_of_one_div_lt_one_div hA hn
    have hzn : ‖z / a n‖ ≤ 1 := by
      rw [norm_div, div_le_one (hpos n)]
      have hlt : ‖z‖ ^ (p + 1) < ‖a n‖ ^ (p + 1) := by linarith
      exact le_of_lt (lt_of_pow_lt_pow_left₀ _ (norm_nonneg _) hlt)
    rw [norm_sub_rev]
    calc ‖1 - weierstrassFactor p (z / a n)‖ ≤ ‖z / a n‖ ^ (p + 1) :=
          norm_one_sub_weierstrassFactor_le p hzn
      _ = ‖z‖ ^ (p + 1) * (1 / ‖a n‖ ^ (p + 1)) := by rw [norm_div, div_pow]; ring
  have key : Summable (fun n => weierstrassFactor p (z / a n) - 1) :=
    Summable.of_norm_bounded_eventually_nat (hsum.mul_left _) hev
  simpa using Complex.multipliable_one_add_of_summable key

/-! ### The `ℕ`-indexed statement was FALSE — refuted, then repaired

An earlier version of `hadamard_factorization` enumerated the zeros as
`a : ℕ → ℂ` with `∀ n, f (a n) = 0`. That is not merely hard to prove; it is
**false**, and the two theorems below are a sorry-free refutation.

`Complex.exp` has order `1` and `exp 0 = 1 ≠ 0`, so it satisfies every
hypothesis — but it has NO zeros at all, so no `a : ℕ → ℂ` can satisfy
`∀ n, f (a n) = 0`. A `ℕ`-indexed enumeration cannot express "finitely many
zeros", let alone none. The sorry on that statement could never have been
closed; it could only ever have been used to derive anything at all.

The repair existentially quantifies the index type, so `ι = Empty` covers the
zero-free case. `hadamard_factorization_statement_satisfiable_for_exp` checks
that the repaired statement really is satisfiable in exactly the case that
refuted the old one — a regression test, not a restatement. -/

theorem isEntireOfOrderLE_exp : IsEntireOfOrderLE Complex.exp 1 := by
  refine ⟨Complex.differentiable_exp, 1, 1, one_pos, fun z => ?_⟩
  rw [Complex.norm_exp]
  simp only [one_mul, Real.rpow_one]
  exact Real.exp_le_exp.mpr (Complex.re_le_norm z)

/-- The refutation: for `f = exp`, no `ℕ`-indexed zero enumeration exists. -/
theorem no_nat_indexed_zero_enumeration_for_exp :
    ¬ ∃ (a : ℕ → ℂ), ∀ n, Complex.exp (a n) = 0 := by
  rintro ⟨a, hz⟩
  exact Complex.exp_ne_zero (a 0) (hz 0)

/-- The repair is satisfiable exactly where the old statement failed. -/
theorem hadamard_factorization_statement_satisfiable_for_exp :
    ∃ (p : ℕ) (g : Polynomial ℂ) (ι : Type) (_ : Countable ι) (a : ι → ℂ),
      (p : ℝ) ≤ 1 ∧ (g.natDegree : ℝ) ≤ 1 ∧
      (∀ i, a i ≠ 0) ∧ (∀ i, Complex.exp (a i) = 0) ∧
      (∀ z, Multipliable (fun i => weierstrassFactor p (z / a i)) ∧
            Complex.exp z
              = Complex.exp (g.eval z) * ∏' i, weierstrassFactor p (z / a i)) := by
  refine ⟨0, Polynomial.X, Empty, inferInstance, Empty.elim, by norm_num, ?_,
    fun i => i.elim, fun i => i.elim, fun z => ⟨?_, ?_⟩⟩
  · simp [Polynomial.natDegree_X]
  · exact multipliable_empty
  · simp

/-- **The `0 ≤ ρ` hypothesis of `hadamard_factorization` is necessary** — without
    it the statement is FALSE (machine-proved, no `sorry`).

    `IsEntireOfOrderLE f ρ` is satisfiable at negative `ρ`: for `ρ < 0` the
    exponent `‖z‖^ρ` is bounded above on `‖z‖ ≥ 1` and Mathlib's `rpow` sends
    `0 ^ ρ` to `0`, so the constant function `1` satisfies it with `A = C = 1`.
    But the conclusion demands `(p : ℝ) ≤ ρ` for a natural number `p`, and
    `(p : ℝ) ≥ 0 > ρ`. So the existential cannot be met.

    Classically the order of a nonzero entire function is `≥ 0` by construction,
    which is why the hypothesis is invisible in the textbooks; here the predicate
    takes `ρ` as an input, so it has to be said. Same for `(g.natDegree : ℝ) ≤ ρ`.
    Axioms `[propext, Classical.choice, Quot.sound]`. -/
theorem hadamard_factorization_needs_nonneg_order :
    ¬ ∀ (f : ℂ → ℂ) (ρ : ℝ), IsEntireOfOrderLE f ρ → f 0 ≠ 0 →
        ∃ (p : ℕ) (g : Polynomial ℂ) (ι : Type) (_ : Countable ι) (a : ι → ℂ),
          (p : ℝ) ≤ ρ ∧
          (g.natDegree : ℝ) ≤ ρ ∧
          (∀ i, a i ≠ 0) ∧
          (∀ i, f (a i) = 0) ∧
          (∀ z, Multipliable (fun i => weierstrassFactor p (z / a i)) ∧
                f z = Complex.exp (g.eval z) * ∏' i, weierstrassFactor p (z / a i)) := by
  intro h
  have hone : IsEntireOfOrderLE (fun _ => (1 : ℂ)) (-1) := by
    refine ⟨differentiable_const 1, 1, 1, one_pos, fun z => ?_⟩
    have hnn : (0 : ℝ) ≤ ‖z‖ ^ (-1 : ℝ) := Real.rpow_nonneg (norm_nonneg z) _
    have h0 : Real.exp 0 ≤ Real.exp (1 * ‖z‖ ^ (-1 : ℝ)) :=
      Real.exp_le_exp.mpr (by linarith)
    simpa using h0
  obtain ⟨p, -, -, -, -, hp, -⟩ := h _ (-1) hone (by norm_num)
  have : (0 : ℝ) ≤ (p : ℝ) := Nat.cast_nonneg p
  linarith

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
    side), so the theorem is stated in full strength, not weakened.

    NOTE (`0 ≤ ρ`): `IsEntireOfOrderLE` takes `ρ` as an input and is satisfiable
    at negative `ρ` (the constant `1`), where `(p : ℝ) ≤ ρ` is unsatisfiable for
    `p : ℕ`.  Without the hypothesis the statement is false —
    `hadamard_factorization_needs_nonneg_order` proves it.  The classical theorem
    hides this because the order of a nonzero entire function is `≥ 0` by
    construction. -/
class HasHadamardFactorization where
  factorization : ∀ {f : ℂ → ℂ} {ρ : ℝ},
    IsEntireOfOrderLE f ρ → f 0 ≠ 0 → 0 ≤ ρ →
    ∃ (p : ℕ) (g : Polynomial ℂ) (ι : Type) (_ : Countable ι) (a : ι → ℂ),
      (p : ℝ) ≤ ρ ∧
      (g.natDegree : ℝ) ≤ ρ ∧
      (∀ i, a i ≠ 0) ∧
      (∀ i, f (a i) = 0) ∧
      (∀ z, Multipliable (fun i => weierstrassFactor p (z / a i)) ∧
            f z = Complex.exp (g.eval z) * ∏' i, weierstrassFactor p (z / a i))

theorem hadamard_factorization [HasHadamardFactorization] {f : ℂ → ℂ} {ρ : ℝ}
    (hf : IsEntireOfOrderLE f ρ) (hf0 : f 0 ≠ 0) (hρ : 0 ≤ ρ) :
    ∃ (p : ℕ) (g : Polynomial ℂ) (ι : Type) (_ : Countable ι) (a : ι → ℂ),
      (p : ℝ) ≤ ρ ∧
      (g.natDegree : ℝ) ≤ ρ ∧
      (∀ i, a i ≠ 0) ∧
      (∀ i, f (a i) = 0) ∧
      (∀ z, Multipliable (fun i => weierstrassFactor p (z / a i)) ∧
            f z = Complex.exp (g.eval z) * ∏' i, weierstrassFactor p (z / a i)) :=
  HasHadamardFactorization.factorization hf hf0 hρ

end QOU.Mathlib.HadamardFactorization
