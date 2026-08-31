/-
# The A = 3 count-channel carrier space is a single integer — and it is exhausted

`qou-brng`'s next step was *"search the 20 binding-relevant triples and select on
something that is not the Markov trace."* **There is nothing to search.** The
space collapses once more, to one integer, and enumerating it is a proof rather
than a scan.

## The collapse, in two steps

`QOU.Mass.EnumeratorSelectionDegeneracy.countChannel_depends_only_on_total` gives
the first: the binding sees only `n₊ + n₋` per nucleon-pair, so all nine bands
joining a pair are equivalent and a carrier's binding-relevant content is a triple
`(m₁, m₂, m₃)` — `n₊ = n₋ = mᵢ` on each pair, with `mᵢ ≥ 1` because a Brunnian
carrier links every pair. That reduced `382,637,520` band words to `20` triples at
`c ≤ 12`.

The second step is here. With `c₂ = 2` (the owner-ruled Hopf pair carrier) and
`c₃ = 2(m₁+m₂+m₃)`, `CarrierCrossingQuantisation.bRatio_hopf_pair` gives

    b₃/b₂ = c₃/2 − 3 = M − 3,   M := m₁ + m₂ + m₃.

**`b₃` cannot see the triple either — only its sum.** So the 20 triples collapse
to the four values `M ∈ {3,4,5,6}`, and the carrier space that `b₃` can
distinguish is `ℕ`.

## The exhaustion, and why `c ≤ 12` was never a restriction

`M ≥ 3` (`brunnian_sum_ge_three`), so `b₃/b₂ = M − 3` is a **non-negative
integer**. The measured value is `950815/1483044 ≈ 0.6411`, strictly between `0`
and `1`, so no `M` hits it (`no_carrier_reproduces_b3`) and every `M` misses by at
least `532229/1483044 ≈ 0.35888` — **55.98 %** of the measured value
(`carrier_gap_bounded_below`).

The bound is attained at `M = 4` and `b₃/b₂` **increases** with `M`, so nothing
above `M = 4` can do better (`gap_increases_beyond_four`). **The enumeration is
therefore complete over every crossing number, not merely `c ≤ 12`** — there is no
larger carrier to try, and no search that could find one.

| `M` | `c₃` | `b₃/b₂` | vs measured | triples |
|---|---|---|---|---|
| 3 | 6 | `0` | −100 % | 1 — forced to `(1,1,1)`, the Borromean |
| 4 | 8 | `1` | **+55.98 %** | 3 |
| 5 | 10 | `2` | +211.95 % | 6 |
| 6 | 12 | `3` | +367.93 % | 10 |

`M = 3` is forced to be `(1,1,1)` — one clasp per pair, the Borromean — and lands
exactly on the degenerate locus. There is nothing between it and `M = 4`.

## What is excluded, precisely

Scope **(b)** on the conjunction {`b₃` carried by the count channel, `μ ∝ c`,
Hopf pair carrier `c₂ = 2`, Brunnian A = 3 carrier}, with the invariant named:
**`M` is an integer `≥ 3`**, so `b₃/b₂` is a non-negative integer while the
measured ratio is not one.

Scope **(a)** on each ingredient. In particular this does **not** say the count
channel is wrong, nor that the carrier is not Brunnian — `brunnian_binding_survives`
is untouched, and the Brunnian mechanism remains the only thing letting binding
exist at `lk = 0`. What it says is that these four cannot hold together.

**The live reading is the third ingredient.** Owner ruling A fixes the pair
carrier; dropping Brunnian-ness runs into `CrossingModelPairLocality.brunnian_not_pairLocal`
(a pair-local carrier forces `b₃ = 0`, refuted by AME); and
`CarrierCrossingQuantisation.bRatio_scale_invariant` shows `μ ∝ c` is not a
convention one can simply relax. So the ingredient with room in it is **that `b₃`
is carried by the count channel at all** — which returns `qou-brng` to its
original framing: the extensive term is somewhere the crossing count does not
reach.

## What this closes

The "search the triples" step, and with it the whole count-channel carrier route
for `A = 3`. Not by failing to find a carrier — by enumerating every carrier the
channel admits and proving none is within 55.98 %.

Ground ring `ℚ` (the measured ratio is exact rational; the carrier sums are
integers). No `native_decide`.

Beans `qou-brng`.
-/
import QOU.Mass.CarrierCrossingQuantisation

namespace QOU.Mass.BrunnianTripleExhaustion

open QOU.Mass.CarrierCrossingQuantisation

/-! ## 1. The triple collapses to its sum -/

/-- `b₃/b₂` for a Brunnian `A = 3` carrier with per-pair crossing counts
`n₊ = n₋ = mᵢ`, against the owner-ruled Hopf pair carrier `c₂ = 2`. The total
crossing count is `c₃ = 2(m₁+m₂+m₃)`, so this is `c₃/2 − 3`. -/
def bRatioOfTriple (m₁ m₂ m₃ : ℚ) : ℚ := m₁ + m₂ + m₃ - 3

/-- **`b₃` sees only the sum.** Two carriers whose per-pair counts differ but sum
alike are indistinguishable — the second collapse, after
`countChannel_depends_only_on_total`. -/
theorem bRatio_depends_only_on_sum (m₁ m₂ m₃ m₁' m₂' m₃' : ℚ)
    (h : m₁ + m₂ + m₃ = m₁' + m₂' + m₃') :
    bRatioOfTriple m₁ m₂ m₃ = bRatioOfTriple m₁' m₂' m₃' := by
  unfold bRatioOfTriple; rw [h]

/-- It agrees with the crossing-count form already proved: with `c₂ = 2` and
`c₃ = 2M`, `bRatio = M − 3`. -/
theorem bRatioOfTriple_eq_bRatio (m₁ m₂ m₃ : ℚ) :
    bRatioOfTriple m₁ m₂ m₃
      = bRatio (muOfCrossings 2) (muOfCrossings (2 * (m₁ + m₂ + m₃))) := by
  rw [bRatio_hopf_pair]; unfold bRatioOfTriple; ring

/-- **A Brunnian carrier links every pair**, so each `mᵢ ≥ 1` and the sum is `≥ 3`.
This is what makes `b₃/b₂` a *non-negative* integer rather than merely an integer. -/
theorem brunnian_sum_ge_three {m₁ m₂ m₃ : ℤ}
    (h₁ : 1 ≤ m₁) (h₂ : 1 ≤ m₂) (h₃ : 1 ≤ m₃) : 3 ≤ m₁ + m₂ + m₃ := by
  omega

/-! ## 2. The exhaustion -/

/-- **No carrier reproduces the measured `b₃`** — and the Brunnian hypothesis is
not even needed. `b₃/b₂ = M − 3` is an *integer* for any integer `M`, while
`rMeasured` lies strictly between `0` and `1`, so no integer works at all. Stated
without `3 ≤ M` because the proof does not use it; `brunnian_sum_ge_three` is what
makes the *gap* bound below sharp, not what makes this true. -/
theorem no_carrier_reproduces_b3 (M : ℤ) :
    (M : ℚ) - 3 ≠ rMeasured := by
  intro hEq
  obtain ⟨hlo, hhi⟩ := rMeasured_mem_gap
  rw [← hEq] at hlo hhi
  have h3 : (3 : ℚ) < (M : ℚ) := by linarith
  have h4 : (M : ℚ) < 4 := by linarith
  have h3' : (3 : ℤ) < M := by exact_mod_cast h3
  have h4' : M < (4 : ℤ) := by exact_mod_cast h4
  omega

/-- **And it misses by at least `532229/1483044 ≈ 0.35888` — 55.98 % of the
measured value.** The bound is attained at `M = 4`. -/
theorem carrier_gap_bounded_below (M : ℤ) (hM : 3 ≤ M) :
    532229 / 1483044 ≤ |(M : ℚ) - 3 - rMeasured| := by
  obtain ⟨hlo, hhi⟩ := rMeasured_mem_gap
  have hr1 : rMeasured < 1 := by unfold rMeasured; norm_num
  rcases le_or_gt M 3 with h | h
  · have hM3 : M = 3 := le_antisymm h hM
    subst hM3
    rw [abs_of_nonpos (by norm_num; linarith)]
    unfold rMeasured at hhi ⊢
    norm_num
  · have hm : (4 : ℚ) ≤ (M : ℚ) := by exact_mod_cast h
    rw [abs_of_nonneg (by linarith)]
    unfold rMeasured at hr1 ⊢
    linarith

/-- **`c ≤ 12` was never a restriction.** `b₃/b₂ = M − 3` increases with `M`, so
every carrier beyond `M = 4` is strictly further from the measured value than
`M = 4` is. The exhaustion above therefore covers **every** crossing number, and
no larger search exists to run. -/
theorem gap_increases_beyond_four (M : ℤ) (hM : 5 ≤ M) :
    |(4 : ℚ) - 3 - rMeasured| < |(M : ℚ) - 3 - rMeasured| := by
  obtain ⟨_, hhi⟩ := rMeasured_mem_gap
  have hr1 : rMeasured < 1 := by unfold rMeasured; norm_num
  have hm : (5 : ℚ) ≤ (M : ℚ) := by exact_mod_cast hM
  rw [abs_of_nonneg (by linarith), abs_of_nonneg (by linarith)]
  linarith

/-- **`M = 3` is forced to be the Borromean.** One clasp per pair is the only
triple summing to `3`, and it lands exactly on the degenerate locus `b₃ = 0` —
agreeing with `CountChannelCarrierLocus.canonical_carriers_b3_eq_zero`, reached
here by exhaustion rather than by assignment. -/
theorem borromean_is_the_unique_minimal_carrier {m₁ m₂ m₃ : ℤ}
    (h₁ : 1 ≤ m₁) (h₂ : 1 ≤ m₂) (h₃ : 1 ≤ m₃) (hsum : m₁ + m₂ + m₃ = 3) :
    m₁ = 1 ∧ m₂ = 1 ∧ m₃ = 1 := by
  omega

/-- And that minimal carrier gives exactly zero. -/
theorem minimal_carrier_bRatio_eq_zero : bRatioOfTriple 1 1 1 = 0 := by
  unfold bRatioOfTriple; norm_num

end QOU.Mass.BrunnianTripleExhaustion
