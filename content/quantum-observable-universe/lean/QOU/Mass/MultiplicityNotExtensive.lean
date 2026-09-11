/-
# The multiplicity channel of a trace-sum binding law is sub-extensive

## Why this file exists

The binding arc's one open problem is the **super-pairwise additive extensive
object**: `B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ` needs a term that grows like the
nucleon count `A` and is not a per-block reweighting.

`QOU/Hecke/BondCutSymmetry.lean` (bean `qou-qve5`) excludes one whole class of
candidates — a **positive pair-additive bond count**. Its two load-bearing
theorems both quantify over hypotheses that a *trace sum* does not satisfy:

* `bondSum` is the three-term shape `e_pp·n_pp + e_pn·n_pn + e_nn·n_nn`;
* `bondSum_nonneg` needs `0 ≤ n_pp`, `0 ≤ n_pn`, `0 ≤ n_nn` — the summands are
  **counts**.

The Frobenius pairing escapes both at once. It is a sum over *partitions*, not
over pairs, and its summands carry the proved sign
`Δ_λ = (-1)^{n(λ)}·dim V_λ`, so they are not counts. Nothing in
`BondCutSymmetry` reaches it.

This file asks whether the escape *buys* anything, and answers **no for one
sub-channel**, unconditionally.

## The decomposition

A trace sum over the partitions of `n = 3A` has two ways to be large: one
summand can be large, or there can be many summands. Write the second as the
**multiplicity surplus**

```
multiplicitySurplus T M  :=  log T  -  log M
```

with `T` the sum's amplitude and `M` its dominant summand's — the amount by
which the sum's log-amplitude exceeds its own largest term's. The triangle
inequality plus a uniform bound gives `|Σ| ≤ card · max`, hence

```
multiplicitySurplus  ≤  log (card s)         (`multiplicitySurplus_le_log_card`)
```

and **that is the whole content of the multiplicity channel**: no matter how the
signs fall, how the weights are distributed, or what the braid word is, having
`m` summands instead of one can add at most `log m` to the log-amplitude. The
bound is one-sided, which is the direction that matters — cancellation only
makes the sum smaller, and the claim under test is that multiplicity makes the
binding *bigger*.

## The verdict, and it is quantitative rather than asymptotic

Under the archimedean bridge (`QOU/Mass/ArchimedeanTraceBridge.lean`) the
binding in MeV is `E₀` times a log-amplitude, so the multiplicity channel
contributes at most `E₀ · log (card s)` MeV. For an `A`-nucleon atom word on
`3A` strands the index set is the partitions of `3A`, and

```
log p(n)  ≤  π√(2n/3)      (Hardy–Ramanujan 1918; Erdős 1942 elementary proof)
log p(3A) ≤  π√(2A)
```

so the channel is `O(√A)`. Three consequences are proved below, each stated for
an arbitrary `√`-law so that nothing depends on the constant:

1. `sqrt_lt_linear_of_sq_lt` — a `c√A` law falls strictly below any positive
   linear rate `a·A` once `A > (c/a)²`. An explicit threshold, not a limit.
2. `card_ge_exp_of_linear_le_log_card` — the contrapositive with teeth: for the
   multiplicity channel to *supply* rate `a`, the number of summands must be at
   least `exp(a·A)`, i.e. **exponential** in `A`. The partition count is
   `exp(O(√A))`, and no reading of the corpus changes that.
3. `sqrt_law_shortfall` — the **scale-free** form, and the one that decides it.
   `E₀` is not determined (`QOU/Hecke/BindingScaleCandidates.lean`, bean
   `qou-v8ct`: a uniform factor is 98.6 % of the squared log-residual and is
   undecidable against a uniform rescaling of the bond energies at fixed law),
   so any argument that turns on the *value* of `E₀` is worthless here. Instead:
   normalise the `√` law to agree with the measured binding at one mass number
   `A₁`. Then at every `A₂ > A₁` it undershoots by exactly `√(A₂/A₁)` —
   **independent of `E₀` and of `c`.** The shape is wrong, and no choice of
   scale repairs a shape.

`sqrt_per_nucleon_antitone` records the same fact per nucleon: the channel's
contribution per nucleon is non-increasing in `A`, against a measured `B/A` that
is flat to within a few per cent over `A = 12 … 238`. A decaying quantity is not
a saturating one.

## Scope

**Scope-(b) structural exclusion** in the sense of AGENTS.md §"Before declaring
refuted": the invariant cited is the triangle inequality together with the
sub-exponential growth of the partition function, so the exclusion is of an
*ingredient* — the multiplicity of the partition sum — and not merely of one
construction's magnitude. What is excluded is that channel **alone**; the
theorems say nothing against a law in which multiplicity appears beside
something else.

**What this does NOT exclude, and it is the live remainder.** The dominant
summand's own log-weight `log |y_λ χ^λ(β_A)|` is untouched. The atom word on
`3A` strands has word length `Θ(A)`, so a single character's log *can* grow
linearly — that channel has the right growth class and is where the extensive
term must live if the trace sum carries one at all. This is an independent,
unconditional reason for the concentration that
`QOU/BraidKnot/BindingConcentration.lean` argues from LP sparsity: there,
concentration is a property of the chosen linear program; here it is forced by
counting, whatever program is written.

## What is proved and what is hypothesis

Everything below is proved. Part 1 is generic over a linearly ordered ring
(§7c); the archimedean parts are over `ℝ` because `Real.log` and `Real.sqrt`
are archimedean constructs. The Hardy–Ramanujan bound is **not** proved here —
it enters `hardyRamanujan_gives_sqrt_law` as an explicit hypothesis, named and
citable, in the `_of_` style of AGENTS.md §"Conditional-proved ≠
premise-established". No nuclear datum appears in any statement; `A₁`, `A₂`,
`B₁` are universally quantified.

Producer: `computations/brng_multiplicity_channel_bound_probe.py`.
Bean `qou-brng`. Companion exclusions that this one does not overlap:
`QOU/Hecke/BondCutSymmetry.lean`, `QOU/Mass/CoordinationSaturation.lean`,
`QOU/MassTheory/ChainBondOrderDependence.lean`,
`QOU/MassTheory/BodyOrderRecurrenceDepth.lean`,
`QOU/MassTheory/MayerThreeBodySign.lean`,
`QOU/Mass/BrunnianTripleExhaustion.lean`.

-- Ref: [macdonald1995] https://doi.org/10.1093/oso/9780198534891.001.0001
-/

import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace QOU.Mass.MultiplicityNotExtensive

/-! ## Part 1 — the counting bound, over a generic ordered ring (§7c)

Nothing here knows about partitions, traces, or `q`. The only input is that the
summands are bounded in absolute value; the signs are arbitrary, which is what
lets this apply to `Σ_λ y_λ χ^λ Δ_λ` where `BondCutSymmetry.bondSum_nonneg`
cannot. -/

section Ring

variable {R : Type*} [Ring R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Many summands buy at most a factor of their number.** A signed sum whose
summands are bounded by `M` is bounded by `card · M`. This is the entire
multiplicity channel: the triangle inequality, and no more is available. -/
theorem abs_sum_le_card_mul {ι : Type*} (s : Finset ι) (a : ι → R) (M : R)
    (hM : ∀ i ∈ s, |a i| ≤ M) :
    |∑ i ∈ s, a i| ≤ (s.card : R) * M := by
  calc |∑ i ∈ s, a i| ≤ ∑ i ∈ s, |a i| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ s.card • M := Finset.sum_le_card_nsmul _ _ _ hM
    _ = (s.card : R) * M := nsmul_eq_mul _ _

/-- The same bound stated against the dominant summand: if `a i₀` attains the
maximum absolute value, the whole sum is at most `card` times it. Cancellation
can only make the left side smaller, so the inequality is one-sided by design —
and one-sided in the direction the extensivity question asks about. -/
theorem abs_sum_le_card_mul_dominant {ι : Type*} (s : Finset ι) (a : ι → R)
    (i₀ : ι) (hdom : ∀ i ∈ s, |a i| ≤ |a i₀|) :
    |∑ i ∈ s, a i| ≤ (s.card : R) * |a i₀| :=
  abs_sum_le_card_mul s a _ hdom

end Ring

/-! ## Part 2 — the log form: the multiplicity surplus -/

/-- The **multiplicity surplus**: how much the sum's log-amplitude exceeds the
log-amplitude of its own largest summand. Under the archimedean bridge
(`ArchimedeanTraceBridge`) binding is `E₀` times a log-amplitude, so this is the
part of the binding that multiplicity — as opposed to any single partition's
weight — could be responsible for. -/
noncomputable def multiplicitySurplus (T M : ℝ) : ℝ :=
  Real.log T - Real.log M

/-- **The multiplicity surplus is at most `log (card)`.** With `T ≤ m · M` and
both `T` and `M` positive, the log of the ratio is at most `log m`. -/
theorem multiplicitySurplus_le_log_card {T M m : ℝ}
    (hT : 0 < T) (hM : 0 < M) (hm : 0 < m) (h : T ≤ m * M) :
    multiplicitySurplus T M ≤ Real.log m := by
  have hlog : Real.log T ≤ Real.log (m * M) := Real.log_le_log hT h
  rw [Real.log_mul (ne_of_gt hm) (ne_of_gt hM)] at hlog
  unfold multiplicitySurplus
  linarith

/-- The surplus is non-negative when the sum is at least its dominant summand —
the other side of the sandwich, recorded so the surplus is visibly a *channel*
with a floor as well as a cap and not merely an error term. -/
theorem multiplicitySurplus_nonneg {T M : ℝ} (hM : 0 < M) (h : M ≤ T) :
    0 ≤ multiplicitySurplus T M := by
  unfold multiplicitySurplus
  have := Real.log_le_log hM h
  linarith

/-! ## Part 3 — a `√` law is not a linear law, with an explicit threshold -/

/-- **A `c√A` law falls strictly below any positive linear rate once
`A > (c/a)²`.** No limits: the threshold is exhibited. With `c = π√2` from
Hardy–Ramanujan and `a` the required per-nucleon rate in units of `E₀`, this is
what makes the exclusion quantitative at every physical mass number rather than
merely asymptotic. -/
theorem sqrt_lt_linear_of_sq_lt {a c A : ℝ} (ha : 0 < a) (hc : 0 ≤ c)
    (hA : (c / a) ^ 2 < A) :
    c * Real.sqrt A < a * A := by
  have hApos : 0 < A := lt_of_le_of_lt (by positivity) hA
  have hca : 0 ≤ c / a := by positivity
  have hlt : c / a < Real.sqrt A := by
    have h := Real.sqrt_lt_sqrt (by positivity) hA
    rwa [Real.sqrt_sq hca] at h
  have hspos : 0 < Real.sqrt A := lt_of_le_of_lt hca hlt
  have hsq : Real.sqrt A * Real.sqrt A = A := Real.mul_self_sqrt hApos.le
  have hstep : c / a * Real.sqrt A < Real.sqrt A * Real.sqrt A :=
    mul_lt_mul_of_pos_right hlt hspos
  have hca' : c / a * a = c := by field_simp
  nlinarith [hstep, hsq, ha, hspos, hca']

/-- **The contrapositive with teeth.** If the multiplicity channel is to supply
a term linear in `A` at rate `a`, the number of summands must be at least
`exp (a·A)` — exponential in the nucleon count. The partitions of `3A` number
`exp(O(√A))`, so this is not a bound that a larger search could meet; it is a
bound on the index set itself. -/
theorem card_ge_exp_of_linear_le_log_card {m a A : ℝ} (hm : 0 < m)
    (h : a * A ≤ Real.log m) :
    Real.exp (a * A) ≤ m := by
  have h2 := Real.exp_le_exp.mpr h
  rwa [Real.exp_log hm] at h2

/-! ## Part 4 — the scale-free shape statement

`E₀` is undetermined (`BindingScaleCandidates`, bean `qou-v8ct`), so the
exclusion must not turn on its value. Normalise instead: let the `√` law agree
with the measured binding at one mass number, and read off what it does
everywhere else. -/

/-- **The shortfall of a `√` law against saturation is exactly `√(A₂/A₁)`,
independent of the scale and of the constant.** Normalise any `c√A` law to
reproduce the binding `B₁` at mass number `A₁`; it then predicts
`B₁·√(A₂/A₁)` at `A₂`, while a saturating (constant `B/A`) law gives
`B₁·(A₂/A₁)`. The identity below says the second is `√(A₂/A₁)` times the first,
exactly — an equality, so no tolerance and no fit is involved. -/
theorem sqrt_law_shortfall (r B₁ : ℝ) (hr : 0 ≤ r) :
    B₁ * r = Real.sqrt r * (B₁ * Real.sqrt r) := by
  have h : Real.sqrt r * Real.sqrt r = r := Real.mul_self_sqrt hr
  linear_combination (-B₁) * h

/-- The shortfall is a genuine one — strict — as soon as the mass ratio exceeds
one. This is the falsifiable edge of `sqrt_law_shortfall`: matching at `A₁`
forces an undershoot at every larger `A₂`, for every positive scale. -/
theorem sqrt_law_undershoots {r B₁ : ℝ} (hr : 1 < r) (hB : 0 < B₁) :
    B₁ * Real.sqrt r < B₁ * r := by
  have h0 : (0 : ℝ) < r := lt_trans zero_lt_one hr
  have hsq : Real.sqrt r * Real.sqrt r = r := Real.mul_self_sqrt h0.le
  have h1 : 1 < Real.sqrt r := by
    nlinarith [hsq, Real.sqrt_nonneg r]
  have hs : Real.sqrt r < r := by nlinarith [hsq, h1]
  exact mul_lt_mul_of_pos_left hs hB

/-- **Per nucleon, a `√` law decays.** `c√A / A = c/√A` is non-increasing in
`A`. The measured `B/A` is flat across the mass table — that is what nuclear
*saturation* means — so the two have different shapes, again with no scale in
the statement. -/
theorem sqrt_per_nucleon_antitone {c A₁ A₂ : ℝ} (hc : 0 ≤ c)
    (h1 : 0 < A₁) (h12 : A₁ ≤ A₂) :
    c * Real.sqrt A₂ / A₂ ≤ c * Real.sqrt A₁ / A₁ := by
  have h2 : 0 < A₂ := lt_of_lt_of_le h1 h12
  have hs1 : 0 < Real.sqrt A₁ := Real.sqrt_pos.mpr h1
  have key : ∀ x : ℝ, 0 < x → c * Real.sqrt x / x = c / Real.sqrt x := by
    intro x hx
    have hs : 0 < Real.sqrt x := Real.sqrt_pos.mpr hx
    rw [div_eq_div_iff (ne_of_gt hx) (ne_of_gt hs), mul_assoc,
      Real.mul_self_sqrt hx.le]
  rw [key A₁ h1, key A₂ h2]
  gcongr

/-! ## Part 5 — the applied corollary, with Hardy–Ramanujan named

The growth bound on the partition function is classical and is **not** proved
here. It is carried as an explicit hypothesis so that the conditional is visibly
a conditional, per AGENTS.md §"Conditional-proved ≠ premise-established". -/

/-- **Hardy–Ramanujan gives the `√` law.** If the number of summands `m` of the
`A`-nucleon trace sum obeys `log m ≤ c·√A` — which the partition count `p(3A)`
does, with `c = π√2`, by Hardy–Ramanujan — then the multiplicity surplus obeys
the same bound, and hence (`sqrt_lt_linear_of_sq_lt`) is strictly below any
positive linear rate beyond an explicit threshold. -/
theorem hardyRamanujan_gives_sqrt_law {T M m c A : ℝ}
    (hT : 0 < T) (hM : 0 < M) (hm : 0 < m) (h : T ≤ m * M)
    (hHR : Real.log m ≤ c * Real.sqrt A) :
    multiplicitySurplus T M ≤ c * Real.sqrt A :=
  le_trans (multiplicitySurplus_le_log_card hT hM hm h) hHR

/-- **The exclusion, assembled.** Under a Hardy–Ramanujan-type bound on the
number of summands, the multiplicity surplus is strictly less than the extensive
term `a·A` for every `A` past the exhibited threshold `(c/a)²`. So the
multiplicity channel of a trace-sum binding law cannot be the extensive term —
on any graph, at any scale, with any signs, for any braid word. -/
theorem multiplicity_not_extensive {T M m a c A : ℝ}
    (hT : 0 < T) (hM : 0 < M) (hm : 0 < m) (h : T ≤ m * M)
    (hHR : Real.log m ≤ c * Real.sqrt A)
    (ha : 0 < a) (hc : 0 ≤ c) (hA : (c / a) ^ 2 < A) :
    multiplicitySurplus T M < a * A :=
  lt_of_le_of_lt (hardyRamanujan_gives_sqrt_law hT hM hm h hHR)
    (sqrt_lt_linear_of_sq_lt ha hc hA)

/-- **The exclusion has content: a witness that the hypotheses are satisfiable.**
Not a vacuous conditional — at `T = M = m = 1`, `c = 0`, `a = A = 1` the
antecedents hold and the conclusion is a genuine strict inequality. Guards
against the failure mode of AGENTS.md §"No trivial trues". -/
example : multiplicitySurplus 1 1 < (1 : ℝ) * 1 := by
  refine multiplicity_not_extensive (T := 1) (M := 1) (m := 1) (a := 1) (c := 0)
    (A := 1) one_pos one_pos one_pos (by norm_num) ?_ one_pos le_rfl (by norm_num)
  simp

end QOU.Mass.MultiplicityNotExtensive
