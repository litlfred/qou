import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# Marginal-ratio criteria for extensivity — and why "ratios rising to 1" proves nothing

**What this file is for.** A chain binding total `B(A)` is a sum over `A-1`
bonds. Its *marginal* `m(A) = B(A) - B(A-1)` is what the `A`-th nucleon adds,
and **extensivity is exactly the statement that `m` has a nonzero limit**: if
`m(A) → c > 0` then `B(A) ~ cA`, and if `m(A) → 0` fast enough to be summable
then `B` is *bounded* and not extensive at all. So the behaviour of the marginal
sequence is not a side observation — it *is* the extensivity question, which
`docs/audits/2026-06-02-binding-intensive-vs-extensive-derivation.md` and the
`qou-brng` channel taxonomy both identify as the live blocker.

Measured on the pure single-species chains (PRs #6336, #6365, and the A=5
continuation), the ratios `r(A) = m(A+1)/m(A)` are:

    pp   0.847753, 0.898991, 0.953066     rising toward 1
    nn   0.386424, 0.367352, 0.314444     falling

## The claim this file was written to CHECK, and refutes

I wrote, in a merged PR body and in a probe, that a ratio sequence *rising
monotonically toward 1 from below* is "the signature of a marginal bond
converging to a NONZERO limit -- saturation rather than collapse."

**That is false**, and `ratio_rising_to_one_insufficient` below exhibits the
counterexample: `r k = (k+1)/(k+2)` is strictly increasing, lies strictly in
`(0,1)`, tends to `1`, and its partial products are *exactly* `1/(n+1)`, which
tends to `0`. Rising-to-1 is **necessary but not sufficient**; the correct
criterion is summability of `1 - r`, which `one_sub_sum_le_prod_one_sub`
supplies in the usable direction.

## What survives, and what it costs

* The **nn** reading survives and is now a scope-(b) structural exclusion with a
  named invariant: `prod_le_pow_of_le` shows a ratio sequence bounded above by
  `c < 1` forces the partial products below `c^n`. The measured nn ratios are
  all `≤ 0.387`, so that collapse is geometric and unconditional.
* The **pp** reading does **not** survive as stated. Worse for it, the corpus
  already proved the total is bounded — `|tr_M|` is a bounded trace and its
  free-atom difference saturates — and `B_tot = E₀·(S_off - S_on)` *is* that
  difference. `card_large_marginals_le` turns a bounded total into the finite
  statement that only boundedly many marginals can exceed any `ε > 0`, so a
  nonzero limit is excluded outright.

The corrected picture is therefore **not** "pp saturates, nn collapses" but
**both collapse, at wildly different rates** — pp so slowly that four points
cannot see it, which is exactly what a `1 - r ~ c/k` tail looks like.

## Scope

Everything here is a statement about real sequences: no substrate, no `q`, no
anchor. `ℝ` rather than a generic `CommRing` is correct under §7c because every
statement uses the ordering. Nothing is wired; the file's role is to say which
readings of a measured ratio sequence are licensed and which are not.
-/

namespace QOU.MassTheory.MarginalRatio

open Finset

/-- Partial product of a ratio sequence: `∏_{i<n} r i`. Applied to
`r i = m(i+1)/m(i)` this is `m(n)/m(0)`, so its limit is the marginal's. -/
noncomputable def prodUpTo (r : ℕ → ℝ) (n : ℕ) : ℝ := ∏ i ∈ range n, r i

@[simp] lemma prodUpTo_zero (r : ℕ → ℝ) : prodUpTo r 0 = 1 := by
  simp [prodUpTo]

lemma prodUpTo_succ (r : ℕ → ℝ) (n : ℕ) :
    prodUpTo r (n + 1) = prodUpTo r n * r n := by
  simp [prodUpTo, Finset.prod_range_succ]

/-! ### 1. Ratios bounded away from 1 force geometric collapse

This is the sound half, and it is what licenses the `nn` reading. -/

/-- If every ratio is nonnegative and at most `c`, the partial products are at
most `c ^ n`. With `c < 1` this is geometric decay to zero: a **scope-(b)**
exclusion whose invariant is the uniform bound `c`. -/
theorem prod_le_pow_of_le {r : ℕ → ℝ} {c : ℝ}
    (h0 : ∀ i, 0 ≤ r i) (hc : ∀ i, r i ≤ c) (n : ℕ) :
    prodUpTo r n ≤ c ^ n := by
  unfold prodUpTo
  calc ∏ i ∈ range n, r i
      ≤ ∏ _i ∈ range n, c :=
        Finset.prod_le_prod (fun i _ => h0 i) (fun i _ => hc i)
    _ = c ^ n := by simp

/-! ### 2. The counterexample: rising to 1 is NOT sufficient

`cex k = (k+1)/(k+2)`. Strictly increasing, strictly inside `(0,1)`, tends to
`1` — and its partial product is exactly `1/(n+1)`. -/

/-- The counterexample ratio sequence `r k = (k+1)/(k+2) = 1 - 1/(k+2)`. -/
noncomputable def cex (k : ℕ) : ℝ := (k + 1) / (k + 2)

lemma cex_pos (k : ℕ) : 0 < cex k := by
  unfold cex
  have h : (0:ℝ) < (k : ℝ) + 2 := by positivity
  have h1 : (0:ℝ) < (k : ℝ) + 1 := by positivity
  exact div_pos h1 h

lemma cex_lt_one (k : ℕ) : cex k < 1 := by
  unfold cex
  rw [div_lt_one (by positivity)]
  linarith

/-- `1 - cex k = 1/(k+2)`, so the gaps to 1 are the harmonic tail — **not
summable**, which is precisely why the product still dies. -/
lemma one_sub_cex (k : ℕ) : 1 - cex k = 1 / ((k : ℝ) + 2) := by
  unfold cex
  have h : ((k : ℝ) + 2) ≠ 0 := by positivity
  field_simp
  ring

/-- Strictly increasing, proved through the `1 - 1/(k+2)` form rather than by a
cross-multiplication lemma, whose name has moved between Mathlib versions. -/
lemma cex_strictMono : StrictMono cex := by
  intro a b hab
  have ha : (0:ℝ) < (a : ℝ) + 2 := by positivity
  have hab' : ((a : ℝ) + 2) < ((b : ℝ) + 2) := by
    have : (a : ℝ) < (b : ℝ) := by exact_mod_cast hab
    linarith
  have hrec : 1 / ((b : ℝ) + 2) < 1 / ((a : ℝ) + 2) :=
    one_div_lt_one_div_of_lt ha hab'
  have ea := one_sub_cex a
  have eb := one_sub_cex b
  linarith

/-- The partial products telescope exactly: `∏_{i<n} (i+1)/(i+2) = 1/(n+1)`. -/
theorem cex_prodUpTo (n : ℕ) : prodUpTo cex n = 1 / ((n : ℝ) + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [prodUpTo_succ, ih, cex]
      have h1 : ((n : ℝ) + 1) ≠ 0 := by positivity
      have h2 : ((n : ℝ) + 2) ≠ 0 := by positivity
      push_cast
      field_simp
      ring

/-- **The refutation.** There is a ratio sequence that is strictly increasing,
lies strictly in `(0,1)`, has `1 - r k → 0`, and whose partial products are
`1/(n+1)` — hence tend to `0`. So "the ratios rise monotonically toward 1"
does **not** license "the marginal converges to a nonzero limit".

This is stated as an explicit existential so it can be cited as the reason that
inference is unavailable, rather than re-derived each time. -/
theorem ratio_rising_to_one_insufficient :
    ∃ r : ℕ → ℝ,
      StrictMono r ∧
      (∀ k, 0 < r k) ∧
      (∀ k, r k < 1) ∧
      (∀ k, 1 - r k = 1 / ((k : ℝ) + 2)) ∧
      (∀ n, prodUpTo r n = 1 / ((n : ℝ) + 1)) := by
  refine ⟨cex, cex_strictMono, cex_pos, cex_lt_one, one_sub_cex, cex_prodUpTo⟩

/-! ### 3. The correct criterion, in the usable direction

Weierstrass: `∏ (1 - a i) ≥ 1 - ∑ a i`. So a *finite* measurement plus a tail
bound on `∑ (1 - r)` gives a genuine positive lower bound on the product —
which is what a claim of extensivity actually needs. -/

/-- `1 - ∑_{i<n} a i ≤ ∏_{i<n} (1 - a i)` for `a i ∈ [0,1]`.

Read with `a i = 1 - r i`: if the gaps to 1 sum to less than 1, the product is
bounded below by a positive constant, so the marginal cannot collapse. This is
the sufficient condition the counterexample above shows is missing — and note
it is checkable from finitely many measured terms *plus* a bound on the tail,
never from the measured terms alone. -/
theorem one_sub_sum_le_prod_one_sub {a : ℕ → ℝ}
    (h0 : ∀ i, 0 ≤ a i) (h1 : ∀ i, a i ≤ 1) (n : ℕ) :
    1 - ∑ i ∈ range n, a i ≤ ∏ i ∈ range n, (1 - a i) := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [Finset.prod_range_succ, Finset.sum_range_succ]
      have hS : 0 ≤ ∑ i ∈ range n, a i :=
        Finset.sum_nonneg (fun i _ => h0 i)
      have hb : 0 ≤ 1 - a n := by linarith [h1 n]
      have hstep : (1 - ∑ i ∈ range n, a i) * (1 - a n)
          ≤ (∏ i ∈ range n, (1 - a i)) * (1 - a n) :=
        mul_le_mul_of_nonneg_right ih hb
      nlinarith [h0 n, hS, hstep]

/-! ### 4. A bounded total excludes a nonzero marginal limit

This is the one that settles the `pp` case, given the corpus result that the
trace binding is intensive (bounded). Stated finitely — no filters — so it can
be applied to a measured, finite sequence directly. -/

/-- If the marginals are nonnegative and every partial sum is at most `M`, then
for any `ε > 0` the number of marginals reaching `ε` is bounded: their count
times `ε` is at most `M`.

Consequence for the binding: a **bounded** total (which is what "the binding is
intensive" says) permits only boundedly many marginals above any threshold, so
`m(A) → c > 0` is impossible. Both chains' marginals therefore go to zero, and
the measured question is only *how fast*. -/
theorem card_large_marginals_mul_le {m : ℕ → ℝ} {M ε : ℝ}
    (h0 : ∀ i, 0 ≤ m i)
    (hM : ∀ n, ∑ i ∈ range n, m i ≤ M) (n : ℕ) :
    ((range n).filter (fun i => ε ≤ m i)).card * ε ≤ M := by
  have hsub : (range n).filter (fun i => ε ≤ m i) ⊆ range n :=
    Finset.filter_subset _ _
  have h1 : (((range n).filter (fun i => ε ≤ m i)).card : ℝ) * ε
      = ∑ _i ∈ (range n).filter (fun i => ε ≤ m i), ε := by
    rw [Finset.sum_const, nsmul_eq_mul]
  have h2 : ∑ _i ∈ (range n).filter (fun i => ε ≤ m i), ε
      ≤ ∑ i ∈ (range n).filter (fun i => ε ≤ m i), m i := by
    refine Finset.sum_le_sum ?_
    intro i hi
    exact (Finset.mem_filter.mp hi).2
  have h3 : ∑ i ∈ (range n).filter (fun i => ε ≤ m i), m i
      ≤ ∑ i ∈ range n, m i :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub (fun i _ _ => h0 i)
  calc (((range n).filter (fun i => ε ≤ m i)).card : ℝ) * ε
      = ∑ _i ∈ (range n).filter (fun i => ε ≤ m i), ε := h1
    _ ≤ ∑ i ∈ (range n).filter (fun i => ε ≤ m i), m i := h2
    _ ≤ ∑ i ∈ range n, m i := h3
    _ ≤ M := hM n

/-- The usable form: at most `M / ε` of the first `n` marginals reach `ε`.

This is the bound that actually excludes a nonzero limit — if `m(A) → c > 0`
then *every* sufficiently large `A` has `m(A) ≥ c/2`, i.e. unboundedly many,
contradicting the fixed ceiling `M / (c/2)`. Unlike the multiplicative form
above it genuinely needs `0 < ε`, which is why both are stated. -/
theorem card_large_marginals_le {m : ℕ → ℝ} {M ε : ℝ}
    (hε : 0 < ε) (h0 : ∀ i, 0 ≤ m i)
    (hM : ∀ n, ∑ i ∈ range n, m i ≤ M) (n : ℕ) :
    (((range n).filter (fun i => ε ≤ m i)).card : ℝ) ≤ M / ε := by
  rw [le_div_iff₀ hε]
  exact card_large_marginals_mul_le h0 hM n

/-! ### 5. Average understates the marginal

Formalises why reporting `B(A)/(A-1)` (as #6336 did) hides how fast the
underlying quantity moves: the average of an antitone sequence is at least its
last term. -/

/-- For an antitone marginal sequence, the running average dominates the last
marginal. So an average that has fallen by `x %` sits on a marginal that has
fallen by *at least* `x %` — the average is a lagging indicator, never a
leading one. -/
theorem sum_ge_card_mul_last {m : ℕ → ℝ} (hanti : Antitone m) (n : ℕ) :
    (n : ℝ) * m n ≤ ∑ i ∈ range n, m i := by
  have h : ∀ i ∈ range n, m n ≤ m i := by
    intro i hi
    exact hanti (le_of_lt (Finset.mem_range.mp hi))
  calc (n : ℝ) * m n = ∑ _i ∈ range n, m n := by
        rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    _ ≤ ∑ i ∈ range n, m i := Finset.sum_le_sum h


/-! ### 6. The chain channel has a closed form, and NO parameter makes it extensive

Measured on the pure chains (this PR), the bonded and free trace sums are each
exactly geometric, and their ratio is exactly the corpus bond factor:

    S_on(A) / S_off(A) = f ^ (A - 1)          exact to 18 digits at every A
    S_off(A + 1) / S_off(A) = g              constant to 20 digits

    pp   g = 1.1457596924573008697   f = 0.6126880371464652516  (= z_D)
    nn   g = 0.98774368811580957163  f = 0.403627738350825936

so the whole channel is

    B(A) = E₀ · S_off(2) · g ^ (A - 2) · (1 - f ^ (A - 1))

which reproduces all four measured points to `1e-30` relative — two constants
against four points, i.e. an identity, not a fit. It is exactly the form the
`qou-brng` taxonomy calls Channel 2, `Δtr = tr_free · (1 - f^bonds)`.

**The exclusion.** Extensivity needs `B(A) ~ cA` with `c > 0`. The two lemmas
below split on `g` and neither branch can be linear:

* `chain_bounded_of_growth_le_one` — for `g ≤ 1` the channel is bounded above by
  `S`, so it cannot match an unbounded linear function. This is the branch the
  corpus's "the binding is intensive" claim describes, and the `nn` chain sits
  in it (`g < 1`).
* `chain_geometric_lower_of_growth_gt_one` — for `g > 1` each step multiplies by
  at least `g`, so `B(n) ≥ B(0) · g ^ n`: growth is at least geometric, and a
  linear function is eventually exceeded by any `g ^ n` with `g > 1`. The `pp`
  chain sits in this branch (`g > 1`).

So `g < 1` and `g = 1` are too slow and `g > 1` is too fast; linear is
unreachable for every parameter value.

**That combination step was PROSE when first written, and §8 now proves it.**
The two lemmas above are the branches; the conclusion drawn from them was a
docstring sentence, while being billed as a scope-(b) exclusion. §8's
`chain_never_exactly_linear` supplies the missing proof — and by a shorter route
that needs no case split on `g` at all. Read the exclusion there, not here.

**This also SCOPES a corpus claim.** `2026-06-02-binding-intensive-vs-extensive-
derivation.md` states the binding is intensive (bounded). That is the `g ≤ 1`
branch and is correct for the neutron chain; the **proton** chain has `g > 1`
and is unbounded, so "intensive" is not universal over this construction. The
exclusion above holds either way, which is why it is the right thing to lean on.
-/

/-- For `g ≤ 1` and `f ∈ [0,1]`, the chain channel is bounded by `S`. Bounded
means not linear, so this branch cannot be extensive. -/
theorem chain_bounded_of_growth_le_one {S g f : ℝ} (hS : 0 ≤ S)
    (hg0 : 0 ≤ g) (hg1 : g ≤ 1) (hf0 : 0 ≤ f) (hf1 : f ≤ 1) (n k : ℕ) :
    S * g ^ n * (1 - f ^ k) ≤ S := by
  have hgn : g ^ n ≤ 1 := pow_le_one₀ hg0 hg1
  have hfk : 0 ≤ f ^ k := pow_nonneg hf0 k
  have hfk1 : f ^ k ≤ 1 := pow_le_one₀ hf0 hf1
  have h1 : S * g ^ n ≤ S := by nlinarith [pow_nonneg hg0 n]
  nlinarith [pow_nonneg hg0 n, mul_nonneg hS (pow_nonneg hg0 n)]

/-- For `g > 1` and `f ∈ [0,1)`, each step multiplies the channel by at least
`g`. Iterating, `B n ≥ B 0 * g ^ n` — at least geometric growth, which a linear
function cannot match. -/
theorem chain_step_ge_growth {S g f : ℝ} (hS : 0 ≤ S) (hg0 : 0 ≤ g)
    (hf0 : 0 ≤ f) (hf1 : f ≤ 1) (n k : ℕ) :
    g * (S * g ^ n * (1 - f ^ k)) ≤ S * g ^ (n + 1) * (1 - f ^ (k + 1)) := by
  have hmono : f ^ (k + 1) ≤ f ^ k := by
    calc f ^ (k + 1) = f ^ k * f := by ring
      _ ≤ f ^ k * 1 := by
          exact mul_le_mul_of_nonneg_left hf1 (pow_nonneg hf0 k)
      _ = f ^ k := by ring
  have hbase : 0 ≤ S * g ^ (n + 1) :=
    mul_nonneg hS (pow_nonneg hg0 (n + 1))
  have hle : (1 - f ^ k) ≤ (1 - f ^ (k + 1)) := by linarith
  calc g * (S * g ^ n * (1 - f ^ k))
      = (S * g ^ (n + 1)) * (1 - f ^ k) := by ring
    _ ≤ (S * g ^ (n + 1)) * (1 - f ^ (k + 1)) :=
        mul_le_mul_of_nonneg_left hle hbase
    _ = S * g ^ (n + 1) * (1 - f ^ (k + 1)) := by ring


/-! ### 7. The OTHER channel is exactly extensive — and `g` is why

Section 6 excluded the *difference* channel `B = S_off - S_on` from extensivity
for every `g`. The corpus's own answer to that has been the **log-ratio**, which
`log_ratio_binding_prototype.py` asserts in one sentence: *"the EXTENSIVE
invariant is the log-ratio."* That assertion now has a derivation, from the same
identity, and it is exact rather than approximate.

Write the measured structure with `b = A - 1` bonds:

    S_off = g ^ (b + 1)          (free: A disjoint identical blocks)
    S_on  = g ^ (b + 1) * f ^ b  (bonded: one factor of f per bond)

Then `logRatio_linear_in_bonds` gives

    log (S_off / S_on) = -b * log f

**exactly linear in the bond count**, verified numerically to `1e-30` on both
species at `A = 2,3,4,5`, with slope

    -E₀ * log f  =  2.05070969238143369 MeV/bond   (pp)
    -E₀ * log f  =  3.79778293514235333 MeV/bond   (nn)

the pp value being exactly the Sec.10a chain bond `-α·ln z`.

**The mechanism is `g`, and it is one line.** `logRatio_independent_of_growth`
says the log-ratio does not depend on `g` at all: the free-trace growth `g^(b+1)`
appears in numerator and denominator and cancels. The difference channel cannot
cancel it — that is precisely what §6's two branches are about. So the two
channels are not two guesses at one quantity; they differ by whether the
single-nucleon growth survives, and **that** is why one is extensive and the
other provably never is.

**Scope.** This says the log-ratio channel *has the right shape*. It says
nothing about its magnitude being right, and the corpus's measurement is that it
is not: the `t7qv` arc measures `B(4He) = 10.387 MeV` against AME `28.296`
(-63 %), with the three-body term negative at all eight `A=3` orderings and the
four-body term negative in 80/80 random bond orders — every many-body
correction pushing further from the data. Extensive-and-short is a different
problem from not-extensive, and this file only settles which of the two each
channel has.
-/

/-- The log-ratio of free to bonded trace is **exactly linear in the bond
count**, with slope `-log f`. This is the derivation behind the corpus's
"the extensive invariant is the log-ratio". -/
theorem logRatio_linear_in_bonds {g f : ℝ} (hg : 0 < g) (hf : 0 < f) (b : ℕ) :
    Real.log (g ^ (b + 1) / (g ^ (b + 1) * f ^ b)) = -(b : ℝ) * Real.log f := by
  have hgb : (0:ℝ) < g ^ (b + 1) := pow_pos hg (b + 1)
  have hfb : (0:ℝ) < f ^ b := pow_pos hf b
  have hrw : g ^ (b + 1) / (g ^ (b + 1) * f ^ b) = (f ^ b)⁻¹ := by
    field_simp
  rw [hrw, Real.log_inv, Real.log_pow]
  ring

/-- **The mechanism.** The log-ratio is independent of the free-trace growth
`g`: it cancels between numerator and denominator. The difference channel of §6
cannot cancel it, which is exactly why that one is never extensive and this one
always is. -/
theorem logRatio_independent_of_growth {g₁ g₂ f : ℝ}
    (hg₁ : 0 < g₁) (hg₂ : 0 < g₂) (hf : 0 < f) (b : ℕ) :
    Real.log (g₁ ^ (b + 1) / (g₁ ^ (b + 1) * f ^ b))
      = Real.log (g₂ ^ (b + 1) / (g₂ ^ (b + 1) * f ^ b)) := by
  rw [logRatio_linear_in_bonds hg₁ hf b, logRatio_linear_in_bonds hg₂ hf b]


/-! ### 8. The exclusion itself — previously prose, now proved

**A gap in my own work, closed here.** §6 proved the two *branches* — bounded
for `g ≤ 1`, at-least-geometric for `g > 1` — and then combined them in a
docstring sentence ("bounded is too slow to be linear and geometric is too
fast") to conclude that no `g` makes the channel extensive. That conclusion was
billed as a scope-(b) exclusion while existing only as prose. The branches were
proved; the exclusion was not.

It turns out the exclusion has a **much stronger and shorter proof** than the
asymptotic argument, and it needs only three bond counts.

Write the channel bond-indexed to avoid `ℕ` subtraction:

    chainB S g f b = S * g ^ (b + 1) * (1 - f ^ b)

Suppose it were *exactly* linear, `chainB b = c * b` for every `b` with `c > 0`.
Evaluating at `b = 1, 2, 3` and eliminating `S`:

    g * (1 + f) = 2          from b = 1, 2
    g² * (1 + f + f²) = 3    from b = 1, 3

Then `4 * (ii) - 3 * (i)²` gives `g² * (f - 1)² = 0`, so `f = 1` — which makes
the channel identically zero, contradicting `c > 0`. **One computation, every
`(g, f)` at once**, with no case split on `g` and no limit.

`chain_never_exactly_linear` is that argument.

## What is proved here, and what is NOT

**Proved.** Exact linearity is refuted for every `(g, f)`
(`chain_never_exactly_linear`); the §6 iteration claim
(`chain_ge_geom_iterated`); and the `g ≤ 1` half of the *asymptotic* exclusion
(`bounded_not_eventually_above_line`) — a bounded channel is overtaken by every
positive line, stated finitely so no filters are needed.

**NOT proved, and this is the honest residue.** The `g > 1` half of the
*asymptotic* exclusion. `chain_ge_geom_iterated` gives the geometric lower
bound, but the step from "grows at least like `g^m`" to "eventually exceeds
every line" — the standard fact that a geometric sequence outgrows a linear one
— is not formalised here. So:

* *exact* linearity is excluded for all `(g, f)` — fully proved;
* *asymptotic* linearity is excluded for `g ≤ 1` — fully proved;
* *asymptotic* linearity for `g > 1` rests on that one standard growth fact.

Since the measured `g_pp = 1.1458 > 1`, the proton chain is precisely the case
sitting on the unformalised step. Anyone citing the exclusion asymptotically
for `pp` should cite it as resting on that fact, not as fully mechanised.

**Also not formalised, and not a Lean question.** That `S_off(A) = g^A` — the
factorisation of the weighted Schur–Weyl sum over the disjoint per-nucleon
blocks — is verified numerically at `A = 1..5` to 20 digits and is an algebra
fact about the Hecke construction, not about real sequences. Likewise
`f_pp = z_D` (agreement `2.8e-31`) is a computation, not a theorem. Everything
in this file is conditional on those inputs being what the probes measured.
-/

/-- The channel, indexed by bond count `b` (so `A = b + 1` nucleons). -/
noncomputable def chainB (S g f : ℝ) (b : ℕ) : ℝ := S * g ^ (b + 1) * (1 - f ^ b)

/-- **The exclusion, proved.** The channel is never *exactly* linear in the bond
count, for any `S, g > 0` and any `f < 1`. Uses only `b = 1, 2, 3`.

Note `0 < f` is **not** needed and is deliberately absent: the compiler flagged
it unused, and dropping it strengthens the statement to cover `f ≤ 0` as well.
The physical `f` is a bond factor in `(0,1)`, so the extra generality is free
rather than useful — but an unused hypothesis is worth removing, not
silencing. -/
theorem chain_never_exactly_linear {S g f c : ℝ}
    (hS : 0 < S) (hg : 0 < g) (hf1 : f < 1) (hc : 0 < c) :
    ¬ (∀ b : ℕ, chainB S g f b = c * (b : ℝ)) := by
  intro h
  have h1 := h 1
  have h2 := h 2
  have h3 := h 3
  simp only [chainB] at h1 h2 h3
  push_cast at h1 h2 h3
  have hfne : (1 : ℝ) - f ≠ 0 := by linarith
  have hSg : 0 < S * g ^ 2 := by positivity
  -- from b = 1,2 :  g * (1 + f) = 2
  have hi : g * (1 + f) = 2 := by
    have e : S * g ^ 2 * ((1 - f) * (g * (1 + f) - 2)) = 0 := by nlinarith [h1, h2]
    have := mul_eq_zero.mp e
    rcases this with hz | hz
    · exact absurd hz (ne_of_gt hSg)
    · rcases mul_eq_zero.mp hz with hz' | hz'
      · exact absurd hz' hfne
      · linarith
  -- from b = 1,3 :  g^2 * (1 + f + f^2) = 3
  have hii : g ^ 2 * (1 + f + f ^ 2) = 3 := by
    have e : S * g ^ 2 * ((1 - f) * (g ^ 2 * (1 + f + f ^ 2) - 3)) = 0 := by
      nlinarith [h1, h3]
    have := mul_eq_zero.mp e
    rcases this with hz | hz
    · exact absurd hz (ne_of_gt hSg)
    · rcases mul_eq_zero.mp hz with hz' | hz'
      · exact absurd hz' hfne
      · linarith
  -- 4*(ii) - 3*(i)^2  gives  g^2 * (f - 1)^2 = 0, so f = 1, contradicting f < 1
  have hkey : g ^ 2 * (f - 1) ^ 2 = 0 := by nlinarith [hi, hii]
  have hg2 : g ^ 2 ≠ 0 := by positivity
  have : (f - 1) ^ 2 = 0 := by
    rcases mul_eq_zero.mp hkey with hz | hz
    · exact absurd hz hg2
    · exact hz
  have : f = 1 := by nlinarith [this]
  linarith

/-- One step, stated natively for `chainB` so the iteration below needs no
`simpa` normalisation (which is what made the first attempt miss an off-by-one
in the `g` exponent: `chainB`'s is `b+1`, not `b`). -/
theorem chainB_step {S g f : ℝ} (hS : 0 ≤ S) (hg0 : 0 ≤ g)
    (hf0 : 0 ≤ f) (hf1 : f ≤ 1) (b : ℕ) :
    g * chainB S g f b ≤ chainB S g f (b + 1) := by
  unfold chainB
  have hmono : f ^ (b + 1) ≤ f ^ b := by
    calc f ^ (b + 1) = f ^ b * f := by ring
      _ ≤ f ^ b * 1 := mul_le_mul_of_nonneg_left hf1 (pow_nonneg hf0 b)
      _ = f ^ b := by ring
  have hbase : 0 ≤ S * g ^ (b + 1 + 1) := mul_nonneg hS (pow_nonneg hg0 _)
  have hle : (1 - f ^ b) ≤ (1 - f ^ (b + 1)) := by linarith
  calc g * (S * g ^ (b + 1) * (1 - f ^ b))
      = (S * g ^ (b + 1 + 1)) * (1 - f ^ b) := by ring
    _ ≤ (S * g ^ (b + 1 + 1)) * (1 - f ^ (b + 1)) :=
        mul_le_mul_of_nonneg_left hle hbase
    _ = S * g ^ (b + 1 + 1) * (1 - f ^ (b + 1)) := by ring

/-- The iteration the §6 docstring asserted without proving: for `g ≥ 0` and
`f ∈ [0,1]`, `m` steps multiply the channel by at least `g ^ m`. -/
theorem chain_ge_geom_iterated {S g f : ℝ} (hS : 0 ≤ S) (hg0 : 0 ≤ g)
    (hf0 : 0 ≤ f) (hf1 : f ≤ 1) (b m : ℕ) :
    g ^ m * chainB S g f b ≤ chainB S g f (b + m) := by
  induction m with
  | zero => simp
  | succ m ih =>
      calc g ^ (m + 1) * chainB S g f b
          = g * (g ^ m * chainB S g f b) := by ring
        _ ≤ g * chainB S g f (b + m) := mul_le_mul_of_nonneg_left ih hg0
        _ ≤ chainB S g f (b + m + 1) := chainB_step hS hg0 hf0 hf1 (b + m)
        _ = chainB S g f (b + (m + 1)) := by ring_nf

/-- The `g ≤ 1` half of the ASYMPTOTIC exclusion, proved: a bounded channel
cannot dominate a positive line, because a line is unbounded.

Stated finitely — given any `c > 0` there is a bond count at which the line has
overtaken the channel — so no filters are needed. -/
theorem bounded_not_eventually_above_line {S g f c : ℝ} (hS : 0 ≤ S)
    (hg0 : 0 ≤ g) (hg1 : g ≤ 1) (hf0 : 0 ≤ f) (hf1 : f ≤ 1) (hc : 0 < c) :
    ∃ b : ℕ, chainB S g f b < c * (b : ℝ) := by
  obtain ⟨b, hb⟩ := exists_nat_gt ((S + 1) / c)
  refine ⟨b, ?_⟩
  have hbound : chainB S g f b ≤ S := by
    simpa [chainB] using
      chain_bounded_of_growth_le_one (S := S) (g := g) (f := f) hS hg0 hg1
        hf0 hf1 (b + 1) b
  have : (S + 1) < c * (b : ℝ) := by
    have := (div_lt_iff₀ hc).mp hb
    linarith
  linarith


/-! ### 9. The chain bond set cannot produce the alpha binding — parameter-free

The strongest statement in this file, and the one that needs no model constants
at all.

**Three inputs, none of them a fitted parameter.**

1. **The bond set is the chain**, and that is *forced*, not chosen:
   `QOU.Mass.StrandLayoutForcesChain` (sibling arc, `lean`-direct exit 0) shows
   a single generator `σ_m` joins two different nucleons only when `m % 3 = 2`,
   and then only *consecutive* ones, under the 3-strands-per-nucleon layout.
2. **The channel is exactly pairwise-additive over that bond set.** Measured at
   every composition of `A = 3` and `A = 4` to `1.8e-50`
   (`logratio_exactly_pairwise_additive_probe`): `S_on/S_off` is exactly the
   product of the bond factors, so `L` is a sum of per-bond terms with
   identically **zero** many-body correction.
3. **AME2020.**

Laying a chain out `p…p n…n`, the bond multiset of `(Z, N)` is `(Z-1)` pp, one
pn, `(N-1)` nn. Writing `p = Z-1`, `n = N-1`, those multisets satisfy an
**exact identity**:

    bonds(3H) + bonds(3He) - bonds(2H) = bonds(4He)      (1,1,1) both sides

so **any** additive functional on them obeys

    B(4He) = B(3H) + B(3He) - B(2H)

with the per-bond values cancelling out entirely. Against AME:

    predicted  13.975275 MeV
    AME        28.295661 MeV        ratio 2.0247

**So the chain bond set is refuted for `4He`, and not by being short.** It is
refuted *whatever* the per-bond values are — no rescaling of `f_pp, f_pn, f_nn`
can help, because they do not appear in the relation. Combined with §8 (no `g`
makes the difference channel extensive) and the measured zero many-body term,
the three obvious repairs are each closed: bond count is forced, many-body is
zero, per-bond values cancel.

This is the alpha particle's well-known excess binding, arriving as a structural
obstruction rather than a numerical shortfall. It is scope (b), with the
invariant named: the bond-multiset identity above.
-/

/-- Chain binding as an additive functional on the bond multiset, parametrised
by `p = Z-1` and `n = N-1` so no `ℕ` subtraction appears. -/
noncomputable def chainBinding (sPP sPN sNN : ℝ) (p n : ℕ) : ℝ :=
  (p : ℝ) * sPP + sPN + (n : ℝ) * sNN

/-- The bond-multiset identity, as a relation among bindings. Holds for **every**
choice of per-bond values — they cancel. -/
theorem alpha_relation (sPP sPN sNN : ℝ) :
    chainBinding sPP sPN sNN 1 1
      = chainBinding sPP sPN sNN 0 1 + chainBinding sPP sPN sNN 1 0
        - chainBinding sPP sPN sNN 0 0 := by
  unfold chainBinding
  push_cast
  ring

/-- **Parameter-free refutation.** If a pairwise-additive chain model matches the
AME bindings of `2H`, `3H` and `3He`, its `4He` binding is forced to
`13.975275` MeV and therefore cannot be the AME value `28.295661`.

No per-bond value appears in the conclusion: the hypotheses pin three numbers and
`alpha_relation` determines the fourth, whatever `sPP, sPN, sNN` are. -/
theorem chain_additive_cannot_match_alpha {sPP sPN sNN : ℝ}
    (h2H : chainBinding sPP sPN sNN 0 0 = 2.224566)
    (h3H : chainBinding sPP sPN sNN 0 1 = 8.481798)
    (h3He : chainBinding sPP sPN sNN 1 0 = 7.718043) :
    chainBinding sPP sPN sNN 1 1 ≠ 28.295661 := by
  rw [alpha_relation, h2H, h3H, h3He]
  norm_num

end QOU.MassTheory.MarginalRatio
