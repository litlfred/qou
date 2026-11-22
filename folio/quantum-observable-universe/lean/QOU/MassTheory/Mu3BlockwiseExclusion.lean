import QOU.MassTheory.Mu3ClusterModularity

/-!
# The μ₃ door is closed for every *per-block* multiplicatively-damped trace

`Mu3ClusterModularity` (merged, #4404) reframed the open μ₃ sign question exactly:
`c₃ = −E₀·Δ²g`, so `μ₃ > 0` is reachable by the joint block-trace cluster **iff** that
trace is strictly **submodular** (`Δ²g < 0`).  Three independently-derived operators have
now been measured and all three landed **supermodular** — the wrong side:

1. the multiplicative pairwise product model (scope-(b), Lean: `Mu4RhoFCluster`);
2. the H₉ `|χ|`-joint-trace over the two **adjacent** chain bonds
   (`Δ²g = +0.4225` for T, `+0.3357` for ³He);
3. the **non-adjacent** (1–3) Birman–Ko–Lee band bond
   (`triangle_bond_submodularity_probe.py`, GAP-3): every pair supermodular.

Three coincidences invite a structural question, which this file answers.

## The result

The block-trace is a **Wedderburn sum** `g(S) = Σ_λ y_λ |χ_λ(w_S)|` — a sum over blocks.
`Δ²` is **linear**, so `Δ²g = Σ_λ Δ²(block λ)` (`secondDiff_sum`).  Hence if *each block*
is multiplicatively damped by the bonds — block `λ` contributing `c_λ`, `c_λ r_{λ,a}`,
`c_λ r_{λ,b}`, `c_λ r_{λ,a} r_{λ,b}` with `c_λ ≥ 0` and damping factors `≤ 1` — then every
per-block `Δ²` is `c_λ(1−r_{λ,a})(1−r_{λ,b}) ≥ 0`, so the **total is supermodular** and
`μ₃ > 0` is **unreachable** (`mu3_ne_blockwise_multiplicative_cluster`).

This is a **scope-(b) structural exclusion of a whole class**, and the class is strictly
larger than the one already excluded: `Mu3ClusterModularity.multiplicative_supermodular`
assumes a *single global* pair of damping factors, whereas here **each Wedderburn block
carries its own** `(c_λ, r_{λ,a}, r_{λ,b})` — which is the physically relevant shape, since
each block has its own character and therefore its own response to adding a bond.  The
hypotheses are also weaker: only `r ≤ 1` is needed, never `0 ≤ r`.

## What this does NOT claim (honest scope)

It does **not** prove the H₉ `|χ|`-joint traces of operators 2 and 3 lie in this class —
`|χ_λ(w_S)|` need not factor as `c_λ ∏_{i∈S} r_{λ,i}`.  Their supermodularity remains a
**measured scope-(a)** fact.  What is proved is that *no* per-block multiplicatively-damped
trace can open the door, whatever the blocks and factors.

## What it sharpens

`submodular_needs_interfering_block` is the contrapositive: a submodular total **forces at
least one Wedderburn block whose own `Δ²` is negative**.  The §Fréchet section below then
pins down *exactly* what such a block must do, and the answer is sharper (and in the
opposite direction) to the loose reading "sub-multiplicative":

writing a block's values as `c, c·r_a, c·r_b, c·r_ab`, one has `Δ² = c(r_ab − r_a − r_b + 1)`,
so with `c > 0` the block is submodular **iff `r_ab < r_a + r_b − 1`** — strictly below the
**Fréchet–Hoeffding lower bound**.  Since `r_a + r_b − 1 ≤ r_a·r_b` whenever `r_a, r_b ≤ 1`
(gap exactly `(1−r_a)(1−r_b)`), an interfering block must damp **strictly more strongly than
multiplicatively**: the two bonds together must suppress the block *more* than the product of
their separate suppressions, and by more than that gap.  Any block whose joint damping obeys
the Fréchet lower bound — as a genuine joint survival probability must — is supermodular.

Consistent with the FKG epic (`qou-x631`), which found `f^λ` is *not* universally
log-supermodular: there is no forced invariant, so intra-block interference is not excluded
— it is simply not yet exhibited.

Verified `lean`-direct exit 0, sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-26-deltalambda-mu4-rhoF-cluster.md
-/

namespace QOU.MassTheory.Mu3BlockwiseExclusion

open QOU.MassTheory.Mu3ClusterModularity

variable {ι : Type*}

/-! ### `Δ²` is linear: the second difference of a Wedderburn sum is the sum of the blocks' -/

/-- **`Δ²` commutes with finite sums.**  The second mixed difference of a block-decomposed
trace is the sum of the per-block second differences.  This is the whole engine: the
Wedderburn sum `g = Σ_λ (block λ)` has `Δ²g = Σ_λ Δ²(block λ)`. -/
theorem secondDiff_sum (B : Finset ι) (g₀ gₐ g_b gₐᵦ : ι → ℝ) :
    secondDiff (∑ l ∈ B, g₀ l) (∑ l ∈ B, gₐ l) (∑ l ∈ B, g_b l) (∑ l ∈ B, gₐᵦ l)
      = ∑ l ∈ B, secondDiff (g₀ l) (gₐ l) (g_b l) (gₐᵦ l) := by
  unfold secondDiff
  rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_sub_distrib]

/-! ### Per-block multiplicative damping ⇒ the total is supermodular -/

/-- **The class exclusion.**  If every Wedderburn block is multiplicatively damped by the
two bonds — block `λ` contributing `c_λ`, `c_λ r_{λ,a}`, `c_λ r_{λ,b}`, `c_λ r_{λ,a} r_{λ,b}`
with `c_λ ≥ 0` and each damping factor `≤ 1` — then the **total** block-trace is
supermodular (`Δ²g ≥ 0`).

Note the damping factors may differ **per block**, which is what makes this strictly wider
than `Mu3ClusterModularity.multiplicative_supermodular` (a single global pair).  Note also
that `0 ≤ r` is *not* needed: only `r ≤ 1`, i.e. that each bond damps rather than amplifies. -/
theorem blockwise_multiplicative_supermodular (B : Finset ι) (c rₐ r_b : ι → ℝ)
    (hc : ∀ l ∈ B, 0 ≤ c l)
    (ha : ∀ l ∈ B, rₐ l ≤ 1) (hb : ∀ l ∈ B, r_b l ≤ 1) :
    0 ≤ secondDiff (∑ l ∈ B, c l) (∑ l ∈ B, c l * rₐ l) (∑ l ∈ B, c l * r_b l)
                   (∑ l ∈ B, c l * rₐ l * r_b l) := by
  rw [secondDiff_sum]
  refine Finset.sum_nonneg (fun l hl => ?_)
  rw [multiplicative_second_diff]
  exact mul_nonneg (mul_nonneg (hc l hl) (by linarith [ha l hl])) (by linarith [hb l hl])

/-- **`μ₃ > 0` is unreachable by any per-block multiplicatively-damped block-trace.**
The connected cluster of such a trace is `c₃ = −E₀·Δ²g ≤ 0`, so it cannot equal a positive
residual moment.  Scope-(b): a structural exclusion of the entire class, not a measurement
of one operator. -/
theorem mu3_ne_blockwise_multiplicative_cluster (B : Finset ι) (c rₐ r_b : ι → ℝ)
    {μ₃ E₀ : ℝ} (hμ : 0 < μ₃) (hE : 0 ≤ E₀)
    (hc : ∀ l ∈ B, 0 ≤ c l)
    (ha : ∀ l ∈ B, rₐ l ≤ 1) (hb : ∀ l ∈ B, r_b l ≤ 1) :
    μ₃ ≠ cluster3 E₀ (∑ l ∈ B, c l) (∑ l ∈ B, c l * rₐ l) (∑ l ∈ B, c l * r_b l)
                     (∑ l ∈ B, c l * rₐ l * r_b l) := by
  have hsm := blockwise_multiplicative_supermodular B c rₐ r_b hc ha hb
  intro hEq
  rw [cluster_eq_neg_second_diff] at hEq
  nlinarith [mul_nonneg hE hsm]

/-! ### The sharpened target: the door needs an interfering block -/

/-- **A submodular total forces an interfering block.**  Contrapositive of the class
exclusion, stated for an arbitrary block decomposition: if the Wedderburn sum is submodular
(`Δ²g < 0`, the only regime in which `μ₃ > 0` is reachable), then **some** block `λ` has its
own `Δ²` negative.

This is the concrete residual target.  Since a per-block multiplicatively-damped block has
`Δ² = c_λ(1−r_a)(1−r_b) ≥ 0`, an interfering block is precisely one where the two bonds
damp **sub-multiplicatively** — the joint effect weaker than the product of the separate
effects.  The open question is therefore no longer "find a submodular operator" but
"exhibit intra-block bond interference in a single Wedderburn block". -/
theorem submodular_needs_interfering_block (B : Finset ι) (g₀ gₐ g_b gₐᵦ : ι → ℝ)
    (hsub : secondDiff (∑ l ∈ B, g₀ l) (∑ l ∈ B, gₐ l) (∑ l ∈ B, g_b l) (∑ l ∈ B, gₐᵦ l) < 0) :
    ∃ l ∈ B, secondDiff (g₀ l) (gₐ l) (g_b l) (gₐᵦ l) < 0 := by
  by_contra hcon
  push_neg at hcon
  rw [secondDiff_sum] at hsub
  exact absurd (Finset.sum_nonneg hcon) (not_le.mpr hsub)

/-! ### The Fréchet threshold: exactly how far an interfering block must go

Writing a single block's four values as `c, c·r_a, c·r_b, c·r_ab` (base `c`, single-bond
damping factors `r_a, r_b`, joint factor `r_ab`), the block's second difference is
`Δ² = c(r_ab − r_a − r_b + 1)`.  The three lemmas below locate the submodular regime
exactly, and show it lies strictly beyond multiplicative damping. -/

/-- A block in damping-factor coordinates: `Δ² = c·(r_ab − r_a − r_b + 1)`. -/
theorem secondDiff_damping (c rₐ r_b rₐᵦ : ℝ) :
    secondDiff c (c * rₐ) (c * r_b) (c * rₐᵦ) = c * (rₐᵦ - rₐ - r_b + 1) := by
  unfold secondDiff; ring

/-- **The Fréchet lower bound forces supermodularity.**  If the joint damping factor obeys
`r_ab ≥ r_a + r_b − 1` — the Fréchet–Hoeffding lower bound, which any genuine joint survival
probability satisfies — then the block is supermodular (`Δ² ≥ 0`), whatever `r_a, r_b` are.

So an interfering block must **violate the Fréchet lower bound**. -/
theorem frechet_lower_bound_supermodular {c rₐ r_b rₐᵦ : ℝ} (hc : 0 ≤ c)
    (hfr : rₐ + r_b - 1 ≤ rₐᵦ) :
    0 ≤ secondDiff c (c * rₐ) (c * r_b) (c * rₐᵦ) := by
  rw [secondDiff_damping]
  exact mul_nonneg hc (by linarith)

/-- **Submodular ⟺ strictly below the Fréchet lower bound** (for a block of positive base).
This is the exact characterisation of an interfering block. -/
theorem block_submodular_iff_below_frechet {c rₐ r_b rₐᵦ : ℝ} (hc : 0 < c) :
    secondDiff c (c * rₐ) (c * r_b) (c * rₐᵦ) < 0 ↔ rₐᵦ < rₐ + r_b - 1 := by
  rw [secondDiff_damping]
  constructor
  · intro h; nlinarith [h]
  · intro h; nlinarith [mul_pos hc (show (0:ℝ) < rₐ + r_b - 1 - rₐᵦ by linarith)]

/-- **The Fréchet bound is below the multiplicative one**, with gap exactly `(1−r_a)(1−r_b)`.
Hence "beats multiplicative damping" is *strictly weaker* than "interferes": a block must
damp more strongly than `r_a·r_b` — by at least that gap — before it can turn submodular. -/
theorem frechet_le_multiplicative {rₐ r_b : ℝ} (ha : rₐ ≤ 1) (hb : r_b ≤ 1) :
    rₐ + r_b - 1 ≤ rₐ * r_b := by
  nlinarith [mul_nonneg (sub_nonneg.mpr ha) (sub_nonneg.mpr hb)]

/-- **The interference threshold, assembled.**  An interfering block (submodular, positive
base, damping bonds) has joint factor strictly below the multiplicative prediction:
`r_ab < r_a·r_b`.  The two bonds must jointly suppress the block *more* than the product of
their separate suppressions — the opposite direction from "weaker than multiplicative". -/
theorem interfering_block_beats_multiplicative {c rₐ r_b rₐᵦ : ℝ} (hc : 0 < c)
    (ha : rₐ ≤ 1) (hb : r_b ≤ 1)
    (hsub : secondDiff c (c * rₐ) (c * r_b) (c * rₐᵦ) < 0) :
    rₐᵦ < rₐ * r_b :=
  lt_of_lt_of_le ((block_submodular_iff_below_frechet hc).mp hsub)
    (frechet_le_multiplicative ha hb)

end QOU.MassTheory.Mu3BlockwiseExclusion
