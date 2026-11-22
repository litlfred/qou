/-
  # T_β = S · 1 — General H_n(R, q) lift of the Markov-Frobenius
  # min-norm collapse theorem.

  Follow-up to PR #1750 (merged) where the theorem was proved in the
  substrate model `A = R, τ = id`.  The substrate-model proof captured
  the essential algebraic content (the completing-the-square identity)
  but specialised the algebra to its ground field.

  This file lifts the theorem to the GENERAL unital R-algebra setting:

      A : Type, [Ring A], [Algebra R A]
      τ : A → R, R-linear, τ 1 = 1, cyclic (τ(xy) = τ(yx))
      τ positive-semi-definite on squares, non-degenerate

  Then the SDP-min-norm primal-feasible element of A satisfying
  `τ X = S` is `X = S • 1`, exactly.  The hypotheses FAIL for
  A = H_n(R, q), n ≥ 3, with τ = τ_M (τ_M(X·X) < 0 at σ₁σ₂ − σ₂σ₁);
  the Hecke case needs the twisted form τ_M(X · X†), which the
  `TraceTwist` section at the end of this file covers (bean
  `qou-baov`, owner ruling 2026-11-22).

  **Strategy.**

  1. State the COMPLETING-THE-SQUARE algebraic identity:

         τ (X · X) = τ ((X - S·1)(X - S·1)) + 2·S·τ(X) - S²

     for any X ∈ A, S ∈ R.  Proof: ring expansion of (X - S·1)² inside
     τ, using linearity of τ.

  2. Under the constraint τ X = S and normalisation τ 1 = 1:

         τ (X·X) = τ ((X - S·1)²) + S²

  3. Use PSD + non-degeneracy of τ on squares:

         τ ((X - S·1)²) ≥ 0,  equality ⇔ X - S·1 = 0.

  4. Conclude min-norm value S², attained iff X = S · 1.

  **Sorries.** Two sorries, both with Ref to PR #1750 audit doc.  The
  full Mathlib-tactic proofs require non-commutative ring manipulation
  (the algebra A is non-commutative in general; H_n(q) is non-commutative
  at generic q) plus the smul-vs-mul expansion `S • X = (algebraMap R A S) * X`.
  Both are mechanical but verbose; queued as separate commits in this
  branch.

  Ref: [pr1750] https://github.com/litlfred/qou/pull/1750
       Markov-trace SHAPE collapse + paper / Lean substrate proof
       docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
       prop:t-beta-markov-frobenius-collapse content block (.md).
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.Abel
import QOU.SchurWeyl.WtraceTwistedPositivity
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.QBeta.MarkovFrobeniusCollapse.General

universe u v

/-- **Normalized R-linear trace** on a unital R-algebra `A`.

    A trace is an R-linear map `τ : A → R` satisfying

    - **Normalisation:** `τ(1) = 1`.
    - **Cyclicity (trace property):** `τ(x · y) = τ(y · x)`.

    The Jones–Markov trace `τ_M` on the Iwahori–Hecke algebra `H_n(R, q)`
    is the canonical example (Wenzl 1988, Jones 1987; uniqueness at a
    fixed Ocneanu parameter `z`, and the derivation of `z` itself, in
    `QOU.BraidsAndKnots.markovWeights_eq_jones_of_threeRow_eq_zero`).

    **Updated 2026-08-09.** This used to cite
    `QOU.BraidKnot.MarkovTraceUniqueness`, retired that day as
    unsatisfiable — see the retraction note at the head of
    `markov-trace-frobenius-selection.lean`. -/
structure NormalizedTrace (R : Type u) [CommSemiring R]
    (A : Type v) [Semiring A] [Algebra R A] where
  tau : A →ₗ[R] R
  tau_one : tau 1 = 1
  tau_cyc : ∀ x y : A, tau (x * y) = tau (y * x)

/-- **Frobenius positive-semi-definiteness on squares.**

    The trace `τ` is positive-semi-definite on the Frobenius bilinear
    form `⟨X, Y⟩_τ := τ(X · Y)`, i.e. `0 ≤ τ(X · X)` for every `X`.

    **Not satisfied by the Jones–Markov `τ_M` on `H_n(R, q)` for
    `n ≥ 3` (corrected 2026-11-15).**  At `X = σ₁σ₂ − σ₂σ₁ ∈ H₃`,
    `τ_M(X · X) = −2(q⁴ + q² + 1)/(q² + 1)² < 0`.  The positive form on
    `H_n` is the twisted one, `τ_M(X · X†)` with `†` the anti-involution
    fixing each `σ_i`; this class does not encode it.

    Class hypothesis per AGENTS.md §3b-cond: the substantive analytic
    content is axiomatised here so the downstream min-norm theorem is
    sorry-free **conditional on the class instance**. -/
class PSDTrace (R : Type u) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (A : Type v) [Ring A] [Algebra R A] (τ : NormalizedTrace R A) :
    Prop where
  psd : ∀ x : A, 0 ≤ τ.tau (x * x)

/-- **Non-degeneracy on squares.**

    `τ(X · X) = 0 ⇒ X = 0`.  Stronger than PSD; equivalent under
    PSD to "the Frobenius form has trivial radical on squares".

    **Not available for Jones–Markov `τ_M` on `H_n(R, q)` (corrected
    2026-08-09).**  This docstring used to cite `tau_M_non_degenerate`
    in `markov-trace-frobenius-selection.lean` as establishing the
    hypothesis.  That declaration is retired: under production
    convention D, `z = q³/(q²+1)`, the Markov–Frobenius form is
    degenerate on `H_n(R, q)` for `n ≥ 3`, with radical exactly the
    Temperley–Lieb ideal `I_n`.  The class is satisfied instead by
    `A = TL_n(q) = H_n(q)/I_n`, on which the descended pairing *is*
    non-degenerate.  The lemmas below are unaffected — they take this
    class as a hypothesis and never claimed to discharge it. -/
class NonDegTrace (R : Type u) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (A : Type v) [Ring A] [Algebra R A] (τ : NormalizedTrace R A) :
    Prop where
  nondeg : ∀ x : A, τ.tau (x * x) = 0 → x = 0

/-- **Reusable lemma: `(r • 1) * (r • 1) = (r * r) • 1`** in any
    unital R-algebra `A`.  Used in both `completing_the_square_general`
    and `markov_frobenius_min_norm_uniqueness` (reverse direction).
    Extracted per Copilot review #1761 to avoid duplication. -/
theorem smul_one_sq {R : Type u} [CommRing R] {A : Type v} [Ring A]
    [Algebra R A] (r : R) :
    (r • (1 : A)) * (r • (1 : A)) = (r * r) • (1 : A) := by
  simp only [Algebra.smul_def, mul_one, map_mul]

/-- **Completing-the-square algebraic identity (general algebra).**

    For any `X ∈ A`, `S ∈ R`:

    $$τ(X · X) = τ((X - S·1)(X - S·1)) + 2 S τ(X) - S².$$

    Proof reduces to (a) expanding `(X - S•1)·(X - S•1)` via the
    R-algebra ring identities, then (b) applying `τ`'s linearity +
    `τ(S²•1) = S² τ(1) = S²` via normalisation.

    Mechanical but verbose with the smul-vs-mul expansion
    (`S • X = (algebraMap R A S) * X`) and non-commutative ring
    manipulation.  Queued as a separate commit on this branch.

    Ref: [leitner2026] docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
         §"Categorical reading" + prop:t-beta-markov-frobenius-collapse .md
         §"Proof — Lagrangian / completing-the-square argument" -/
theorem completing_the_square_general (R : Type u) [CommRing R]
    (A : Type v) [Ring A] [Algebra R A]
    (τ : NormalizedTrace R A) (X : A) (S : R) :
    τ.tau (X * X) =
      τ.tau ((X - S • 1) * (X - S • 1)) + 2 * (S * τ.tau X) - S * S := by
  -- Ref: [leitner2026] docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
  -- Per copilot-review #1761 thread 5: theorem statement uses `- S * S`
  -- directly (using τ.tau_one = 1 inline) rather than `- S * S * τ.tau 1`,
  -- which reduces downstream simp/rw churn.
  -- Step 1: algebra identity using centrality of algebraMap R A S.
  have h_smul_one_mul : (S • (1 : A)) * X = S • X := by
    rw [Algebra.smul_def, mul_assoc, one_mul, ← Algebra.smul_def]
  have h_mul_smul_one : X * (S • (1 : A)) = S • X := by
    rw [Algebra.smul_def, mul_one, ← Algebra.commutes, ← Algebra.smul_def]
  -- Step 2: expand the square in A using reusable lemma smul_one_sq.
  have h_expand : (X - S • (1 : A)) * (X - S • (1 : A)) =
                  X * X - S • X - S • X + (S * S) • (1 : A) := by
    rw [sub_mul, mul_sub, mul_sub, h_smul_one_mul, h_mul_smul_one, smul_one_sq]
    abel
  -- Step 3: apply τ, using R-linearity + τ_one (= 1).
  -- Generalised h_tau_smul to take ANY scalar (not just S), so the third
  -- rewrite can dispatch τ.tau ((S * S) • 1) too.
  have h_tau_smul : ∀ (r : R) (Y : A), τ.tau (r • Y) = r * τ.tau Y :=
    fun r Y => by rw [τ.tau.map_smul, smul_eq_mul]
  have h_rearrange : X * X - S • X - S • X + (S * S) • (1 : A) =
                     X * X + (-(S • X)) + (-(S • X)) + (S * S) • (1 : A) := by abel
  have h_tau_expand : τ.tau ((X - S • 1) * (X - S • 1)) =
                      τ.tau (X * X) - S * τ.tau X - S * τ.tau X + S * S := by
    rw [h_expand, h_rearrange]
    -- Use simp only for order-independence: map_add / map_neg / h_tau_smul /
    -- tau_one all apply, then ring closes.  Robust to mathlib's per-call
    -- simp-set quirks (LSP observed inconsistent auto-application).
    simp only [τ.tau.map_add, τ.tau.map_neg, h_tau_smul, τ.tau_one, mul_one]
    ring
  -- Step 4: rearrange (R is a CommRing — use linear_combination, not linarith).
  -- Coefficient: -1 (goal moves S² to LHS, h_tau_expand moves it to RHS).
  linear_combination -h_tau_expand

/-- **T_β = S · 1 — general algebra min-Frobenius-norm LOWER BOUND.**

    Under the SDP constraint `τ(X) = S` and PSD of `τ` on squares
    (class hypothesis per §3b-cond), the Frobenius norm-squared
    `τ(X · X)` is bounded below by `S²`.

    The companion theorem `markov_frobenius_min_norm_uniqueness`
    below (using `NonDegTrace`) establishes that the lower bound is
    attained iff `X = S • 1`, giving the full SHAPE-collapse claim
    `T_β = S · 1_H` of PR #1750.

    This does not apply to `A = H_n(R, q)`, `n ≥ 3`, with `τ = τ_M`,
    where `PSDTrace` fails (see the class docstring).  The L2 SHAPE × S
    decomposition of PR #1739 is basis-dependence of the
    coordinate-vector Euclidean norm on `ℝ^6`, NOT the categorical
    Frobenius norm on H_3(ℝ, q).

    Ref: [leitner2026] docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
         §"Categorical reading" + prop:t-beta-markov-frobenius-collapse .md -/
theorem markov_frobenius_min_norm_lift
    (R : Type u) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (A : Type v) [Ring A] [Algebra R A]
    (τ : NormalizedTrace R A)
    [PSDTrace R A τ]
    (S : R) (X : A) (h_constraint : τ.tau X = S) :
    S * S ≤ τ.tau (X * X) := by
  -- Ref: [leitner2026] docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
  -- Step 1: invoke completing-the-square (statement uses simplified
  --   `- S * S` form; τ_one absorbed inline).
  have h := completing_the_square_general R A τ X S
  -- Step 2: substitute h_constraint (τ X = S).
  rw [h_constraint] at h
  -- h : τ(X*X) = τ((X - S•1)²) + 2 * (S * S) - S * S
  --          = τ((X - S•1)²) + S * S
  -- Step 3: PSD of τ on squares.
  have h_psd : 0 ≤ τ.tau ((X - S • 1) * (X - S • 1)) :=
    PSDTrace.psd (R := R) (A := A) (τ := τ) (X - S • 1)
  -- Step 4: arithmetic conclusion.
  linarith

/-- **T_β = S · 1 uniqueness — equality case of the min-norm bound.**

    Companion to `markov_frobenius_min_norm_lift`.  Under the same
    constraint `τ(X) = S` plus PSD + non-degeneracy of `τ` on
    squares, the equality `τ(X · X) = S²` holds iff `X = S · 1`.

    Combined with `markov_frobenius_min_norm_lift`, this gives the
    full SHAPE-collapse claim: the minimum-Frobenius-norm
    primal-feasible element is `T_β = S · 1`, attained uniquely.

    Proof sketch:
    - (⇒) `τ(X*X) = S²` + completing_the_square + constraint ⇒
      `τ((X - S•1)²) = 0` ⇒ `X - S•1 = 0` by NonDegTrace.
    - (⇐) `X = S • 1` ⇒ `τ(X*X) = τ((S•1)*(S•1)) = τ((S²)•1)
      = S² τ(1) = S²` by NormalizedTrace.tau_one.

    Ref: [leitner2026] docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
         §"Proof — Lagrangian / completing-the-square argument" -/
theorem markov_frobenius_min_norm_uniqueness
    (R : Type u) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (A : Type v) [Ring A] [Algebra R A]
    (τ : NormalizedTrace R A)
    [PSDTrace R A τ] [NonDegTrace R A τ]
    (S : R) (X : A) (h_constraint : τ.tau X = S) :
    τ.tau (X * X) = S * S ↔ X = S • 1 := by
  -- Ref: [leitner2026] docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
  constructor
  · -- Forward direction (⇒): τ(X²) = S² ⇒ X = S•1
    intro h_eq
    have h := completing_the_square_general R A τ X S
    rw [h_constraint] at h
    -- h : τ(X*X) = τ((X - S•1)²) + 2 * (S * S) - S * S
    --          = τ((X - S•1)²) + S * S
    have h_psd : 0 ≤ τ.tau ((X - S • 1) * (X - S • 1)) :=
    PSDTrace.psd (R := R) (A := A) (τ := τ) (X - S • 1)
    -- From h + h_eq: τ((X-S•1)²) = 0
    have h_zero : τ.tau ((X - S • 1) * (X - S • 1)) = 0 := by linarith
    -- NonDegTrace ⇒ X - S•1 = 0 ⇒ X = S•1
    have h_sub_zero : X - S • (1 : A) = 0 :=
      NonDegTrace.nondeg (R := R) (A := A) (τ := τ) (X - S • 1) h_zero
    exact sub_eq_zero.mp h_sub_zero
  · -- Reverse direction (⇐): X = S•1 ⇒ τ(X²) = S²
    intro h_eq
    rw [h_eq]
    -- Goal: τ.tau ((S•1) * (S•1)) = S * S
    -- Use reusable lemma smul_one_sq (extracted per Copilot review).
    rw [smul_one_sq, τ.tau.map_smul, smul_eq_mul, τ.tau_one, mul_one]

/-! ## Twisted form (owner ruling 2026-11-22, bean `qou-baov`)

The positive form on `H_n(R, q)` is the twisted one, `τ(X · X†)`. The
statements below replace `τ(X · X)` by `τ(X · X†)` for an `R`-linear
map `† : A → A` with `1† = 1` and `τ(X†) = τ(X)`. Nothing else about
`†` is used, so `† = id` is allowed and recovers the untwisted
statements above as a special case. For `H_n(R, q)`, `†` is the
anti-involution fixing each `σ_i`. Positivity of `τ_M(Y Y†)` at `z_D`, `q > 1`, is proved in
`QOU.SchurWeyl.SeminormalRep.wtrace_mul_dag_nonneg` (instance at the end of this file). -/

/-- An `R`-linear map `†` on `A` that fixes `1` and preserves `τ`. -/
structure TraceTwist (R : Type u) [CommRing R] (A : Type v) [Ring A] [Algebra R A]
    (τ : NormalizedTrace R A) where
  dag : A →ₗ[R] A
  dag_one : dag 1 = 1
  tau_dag : ∀ x : A, τ.tau (dag x) = τ.tau x

/-- Positivity of the twisted form: `0 ≤ τ(X · X†)`. -/
class TwistedPSDTrace (R : Type u) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (A : Type v) [Ring A] [Algebra R A] (τ : NormalizedTrace R A)
    (t : TraceTwist R A τ) : Prop where
  psd : ∀ x : A, 0 ≤ τ.tau (x * t.dag x)

/-- Non-degeneracy of the twisted form: `τ(X · X†) = 0 → X = 0`. -/
class TwistedNonDegTrace (R : Type u) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (A : Type v) [Ring A] [Algebra R A] (τ : NormalizedTrace R A)
    (t : TraceTwist R A τ) : Prop where
  nondeg : ∀ x : A, τ.tau (x * t.dag x) = 0 → x = 0

/-- Completing the square for the twisted form:
    `τ(X X†) = τ((X − S·1)(X − S·1)†) + 2 S τ(X) − S²`. -/
theorem completing_the_square_twisted (R : Type u) [CommRing R]
    (A : Type v) [Ring A] [Algebra R A]
    (τ : NormalizedTrace R A) (t : TraceTwist R A τ) (X : A) (S : R) :
    τ.tau (X * t.dag X) =
      τ.tau ((X - S • 1) * t.dag (X - S • 1)) + 2 * (S * τ.tau X) - S * S := by
  have hd : t.dag (X - S • (1 : A)) = t.dag X - S • 1 := by
    rw [map_sub, map_smul, t.dag_one]
  rw [hd]
  have hexp : (X - S • (1 : A)) * (t.dag X - S • 1)
      = X * t.dag X - S • X - S • t.dag X + (S * S) • 1 := by
    simp only [sub_mul, mul_sub, mul_smul_comm, smul_mul_assoc, one_mul, mul_one, smul_smul,
      smul_sub]
    abel
  rw [hexp, map_add, map_sub, map_sub, map_smul, map_smul, map_smul, t.tau_dag, τ.tau_one]
  simp only [smul_eq_mul, mul_one]
  ring

/-- **T_β = S · 1, general algebra, twisted form — lower bound.**
    Under `τ(X) = S` and positivity of `τ(Y Y†)`, `S² ≤ τ(X X†)`. -/
theorem markov_frobenius_min_norm_twisted
    (R : Type u) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (A : Type v) [Ring A] [Algebra R A]
    (τ : NormalizedTrace R A) (t : TraceTwist R A τ) [TwistedPSDTrace R A τ t]
    (S : R) (X : A) (h_constraint : τ.tau X = S) :
    S * S ≤ τ.tau (X * t.dag X) := by
  have h := completing_the_square_twisted R A τ t X S
  rw [h_constraint] at h
  have h_psd := TwistedPSDTrace.psd (τ := τ) (t := t) (X - S • 1)
  linarith

/-- **T_β = S · 1, general algebra, twisted form — equality case.**
    With non-degeneracy as well, `τ(X X†) = S²` iff `X = S · 1`. -/
theorem markov_frobenius_min_norm_twisted_uniqueness
    (R : Type u) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (A : Type v) [Ring A] [Algebra R A]
    (τ : NormalizedTrace R A) (t : TraceTwist R A τ)
    [TwistedNonDegTrace R A τ t]
    (S : R) (X : A) (h_constraint : τ.tau X = S) :
    τ.tau (X * t.dag X) = S * S ↔ X = S • 1 := by
  have h := completing_the_square_twisted R A τ t X S
  rw [h_constraint] at h
  constructor
  · intro h_eq
    exact sub_eq_zero.mp
      (TwistedNonDegTrace.nondeg (τ := τ) (t := t) _ (by linarith))
  · rintro rfl
    rw [h, sub_self, zero_mul, map_zero]
    ring


/-! ## The instance at convention D (W8, bean `qou-baov`)

The Markov trace `tr_M` at `z_D = q³/(q²+1)` is `QOU.SchurWeyl.SeminormalRep.wtrace` on the
presented Hecke algebra `Hecke K q q⁻¹ n = H_{n+1}(q)`. For `q > 1` over any ordered field it is a
`NormalizedTrace`, the anti-involution `†` fixing each `σᵢ` is a `TraceTwist` for it, and the
twisted form is positive (`wtrace_mul_dag_nonneg`). So `markov_frobenius_min_norm_twisted` applies
to `tr_M` at `z_D`: `S² ≤ tr_M(X·X†)` whenever `tr_M(X) = S`.

**`TwistedNonDegTrace` is not supplied, and is false here for `n + 1 ≥ 3`.** The Ocneanu weights
at `z_D` vanish on every shape with three rows
(`ocneanuWeight_conventionD_eq_zero_of_three_rows`), so the form has a nonzero radical
(`QOU.SchurWeyl.OcneanuTraceNotFaithful.exists_nonzero_wtrace_orthogonal`, at `n + 1 = 3` over `ℝ`). The
equality case `markov_frobenius_min_norm_twisted_uniqueness` therefore does not apply to `tr_M`
at `z_D`. -/

section ConventionD

open QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

theorem one_lt_ne_zero {q : K} (hq : 1 < q) : q ≠ 0 := ne_of_gt (lt_trans one_pos hq)

/-- `tr_M` at `z_D`, as a normalized trace on `H_{n+1}(q)`, for `q > 1`. -/
noncomputable def markovTraceZD (q : K) (hq : 1 < q) (n : ℕ) :
    NormalizedTrace K (QOU.SchurWeyl.Hecke K q q⁻¹ n) where
  tau := wtrace q (one_lt_ne_zero hq) (notRootOfUnity_of_one_lt q hq) n
  tau_one := wtrace_one q (one_lt_ne_zero hq) (notRootOfUnity_of_one_lt q hq)
    (by positivity) (fun i hi => (one_lt_pow₀ (by nlinarith) hi.ne').ne') n
  tau_cyc := wtrace_cyclic q (one_lt_ne_zero hq) (notRootOfUnity_of_one_lt q hq) n

/-- The anti-involution `σᵢ ↦ σᵢ` as a twist of `tr_M` at `z_D`. -/
noncomputable def markovTraceZDTwist (q : K) (hq : 1 < q) (n : ℕ) :
    TraceTwist K (QOU.SchurWeyl.Hecke K q q⁻¹ n) (markovTraceZD q hq n) where
  dag := QOU.SchurWeyl.Hecke.dag K q q⁻¹ n
  dag_one := QOU.SchurWeyl.Hecke.dag_one K q q⁻¹ n
  tau_dag x := wtrace_dag q hq _ _ n x

/-- **`TwistedPSDTrace` for `tr_M` at `z_D`**, `q > 1`. -/
instance markovTraceZD_twistedPSD (q : K) (hq : 1 < q) (n : ℕ) :
    TwistedPSDTrace K (QOU.SchurWeyl.Hecke K q q⁻¹ n) (markovTraceZD q hq n)
      (markovTraceZDTwist q hq n) where
  psd x := wtrace_mul_dag_nonneg q hq _ _ n x

/-- **The T_β lower bound for `tr_M` at `z_D`:** if `tr_M(X) = S` then `S² ≤ tr_M(X·X†)`. -/
theorem markov_frobenius_min_norm_zD (q : K) (hq : 1 < q) (n : ℕ) (S : K)
    (X : QOU.SchurWeyl.Hecke K q q⁻¹ n) (h : (markovTraceZD q hq n).tau X = S) :
    S * S ≤ (markovTraceZD q hq n).tau (X * QOU.SchurWeyl.Hecke.dag K q q⁻¹ n X) :=
  markov_frobenius_min_norm_twisted K _ (markovTraceZD q hq n) (markovTraceZDTwist q hq n) S X h

end ConventionD

end QOU.QBeta.MarkovFrobeniusCollapse.General
