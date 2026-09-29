import QOU.MassTheory.Mu3BlockwiseExclusion

/-!
# The exclusion survives the GAP-7 slot correction: `∑Δ²g + Δ³g ≥ 0` on the whole class

`Mu3BlockwiseExclusion` (merged) shows that a per-block multiplicatively-damped Wedderburn
trace has `Δ²g ≥ 0`, closing the μ₃ door for that class **at the level of the pair term**.
But the merged GAP-7 work (`UrsellSlotAlignment.triangle_moment_decomp`) established that the
moments and the differences are indexed differently — `μₖ` by *particle* count, `Δᵐg` by
*bond* count — so the triangle's correct assembly is

    μ₃-slot  =  ∑_{pairs} Δ²g  +  Δ³g .

That correction is **not** a formality here, because the third difference of a multiplicative
block has the **opposite sign**:

    Δ³ = −c(1−r_a)(1−r_b)(1−r_c)  ≤ 0     (`thirdDiff_multiplicative`)

so the triple term pushes *toward* the door and could in principle overturn the pair-term
exclusion.  This file proves it does not.

## The result

With damping factors in `[0, 1]`, writing `u = 1−r_a`, `v = 1−r_b`, `w = 1−r_c ∈ [0,1]`:

    ∑Δ² + Δ³  =  c·(uv + uw + vw − uvw)  ≥  0

because `uvw ≤ uv` (as `w ≤ 1`) while `uw, vw ≥ 0`.  Hence
`slot_nonneg_multiplicative` and, by block-linearity of both differences,
`mu3_slot_ne_blockwise_multiplicative` — **`μ₃ > 0` is unreachable by a per-block
multiplicatively-damped trace even under the corrected slot assembly.**

This is the structural counterpart of the numerical observation reported when GAP-7 landed
(the correction "roughly doubles the magnitude but preserves the sign"): here the
sign-preservation is proved for the entire class, not measured on two isotopes.

## Honest scope

Unchanged from `Mu3BlockwiseExclusion`: this excludes the per-block multiplicatively-damped
class.  It does **not** show the H₉ `|χ|` joint traces lie in that class.  Note also that the
triple result needs, beyond the pair result's `r ≤ 1`, only a **single** extra lower bound
`0 ≤ r_c` (used for `uv(1−w) ≥ 0`) — not `0 ≤ r` on all three.  The formalization found this:
`nlinarith` closed the goal without the other two, so they were dropped rather than left in as
decorative hypotheses.

Verified `lean`-direct exit 0, sorry-free.

-- Ref: [manuscript] docs/audits/2026-07-26-deltalambda-mu4-rhoF-cluster.md
-/

namespace QOU.MassTheory.Mu3SlotExclusion

open QOU.MassTheory.Mu3ClusterModularity QOU.MassTheory.Mu3BlockwiseExclusion

variable {ι : Type*}

/-! ### The third mixed difference -/

/-- The **third mixed finite difference** on the three-bond Boolean lattice:
`Δ³g = g_abc − g_ab − g_ac − g_bc + g_a + g_b + g_c − g_∅`. -/
def thirdDiff (g₀ gₐ g_b g_c gₐᵦ gₐ_c g_bc gₐᵦ_c : ℝ) : ℝ :=
  gₐᵦ_c - gₐᵦ - gₐ_c - g_bc + gₐ + g_b + g_c - g₀

/-- **`Δ³` commutes with finite sums** — the three-bond analogue of `secondDiff_sum`. -/
theorem thirdDiff_sum (B : Finset ι) (g₀ gₐ g_b g_c gₐᵦ gₐ_c g_bc gₐᵦ_c : ι → ℝ) :
    thirdDiff (∑ l ∈ B, g₀ l) (∑ l ∈ B, gₐ l) (∑ l ∈ B, g_b l) (∑ l ∈ B, g_c l)
              (∑ l ∈ B, gₐᵦ l) (∑ l ∈ B, gₐ_c l) (∑ l ∈ B, g_bc l) (∑ l ∈ B, gₐᵦ_c l)
      = ∑ l ∈ B, thirdDiff (g₀ l) (gₐ l) (g_b l) (g_c l)
                           (gₐᵦ l) (gₐ_c l) (g_bc l) (gₐᵦ_c l) := by
  unfold thirdDiff
  rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, Finset.sum_add_distrib,
    Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_sub_distrib,
    Finset.sum_sub_distrib]

/-- **The third difference of a multiplicative block flips sign.**
`Δ³ = −c(1−r_a)(1−r_b)(1−r_c)`, non-positive for damping factors `≤ 1` — the opposite sign
to `Δ² = +c(1−r_a)(1−r_b)`.  So the triple term pushes *toward* the μ₃ door. -/
theorem thirdDiff_multiplicative (c rₐ r_b r_c : ℝ) :
    thirdDiff c (c * rₐ) (c * r_b) (c * r_c)
              (c * rₐ * r_b) (c * rₐ * r_c) (c * r_b * r_c) (c * rₐ * r_b * r_c)
      = -(c * (1 - rₐ) * (1 - r_b) * (1 - r_c)) := by
  unfold thirdDiff; ring

/-! ### The corrected slot is still non-negative -/

/-- **The slot sum of a single multiplicative block is non-negative.**
`∑_{pairs}Δ² + Δ³ = c(uv + uw + vw − uvw)` with `u = 1−r_a`, `v = 1−r_b`, `w = 1−r_c`.
Factoring as `uv(1−w) + uw + vw` shows it is `≥ 0`: the triple term never outweighs the three
pair terms.

**Sharp hypotheses.**  This needs `u, v, w ≥ 0` (i.e. all three `r ≤ 1`, each bond damps) but
only the *single* extra bound `w ≤ 1` (i.e. `0 ≤ r_c`), which is what makes `uv(1−w) ≥ 0`.
The lower bounds on `r_a, r_b` are **not** needed — the factoring singles out one bond, and by
symmetry it suffices that *some* one of the three has `r ≥ 0`. -/
theorem slot_nonneg_multiplicative {c rₐ r_b r_c : ℝ} (hc : 0 ≤ c)
    (ha1 : rₐ ≤ 1) (hb1 : r_b ≤ 1) (hc0 : 0 ≤ r_c) (hc1 : r_c ≤ 1) :
    0 ≤ secondDiff c (c * rₐ) (c * r_b) (c * rₐ * r_b)
      + secondDiff c (c * rₐ) (c * r_c) (c * rₐ * r_c)
      + secondDiff c (c * r_b) (c * r_c) (c * r_b * r_c)
      + thirdDiff c (c * rₐ) (c * r_b) (c * r_c)
                  (c * rₐ * r_b) (c * rₐ * r_c) (c * r_b * r_c) (c * rₐ * r_b * r_c) := by
  rw [multiplicative_second_diff, multiplicative_second_diff, multiplicative_second_diff,
    thirdDiff_multiplicative]
  have hu : 0 ≤ 1 - rₐ := by linarith
  have hv : 0 ≤ 1 - r_b := by linarith
  have hw : 0 ≤ 1 - r_c := by linarith
  have hw1 : 1 - r_c ≤ 1 := by linarith
  -- uv + uw + vw − uvw ≥ 0 : uvw ≤ uv since w ≤ 1, and uw, vw ≥ 0
  nlinarith [mul_nonneg (mul_nonneg hc hu) hv, mul_nonneg (mul_nonneg hc hu) hw,
    mul_nonneg (mul_nonneg hc hv) hw,
    mul_nonneg (mul_nonneg (mul_nonneg hc hu) hv) (sub_nonneg.mpr hw1)]

/-- **The exclusion survives the slot correction, blockwise.**  If every Wedderburn block is
multiplicatively damped by the three bonds (factors in `[0,1]`, non-negative bases), the
corrected slot `∑_{pairs}Δ²g + Δ³g` is non-negative — so a **positive** `μ₃` cannot equal it.

Together with `Mu3BlockwiseExclusion.mu3_ne_blockwise_multiplicative_cluster` this closes the
per-block multiplicative class against **both** the raw pair reading and the GAP-7-corrected
slot reading of the μ₃ residual. -/
theorem slot_nonneg_blockwise_multiplicative (B : Finset ι) (c rₐ r_b r_c : ι → ℝ)
    (hc : ∀ l ∈ B, 0 ≤ c l)
    (ha1 : ∀ l ∈ B, rₐ l ≤ 1) (hb1 : ∀ l ∈ B, r_b l ≤ 1)
    (hc0 : ∀ l ∈ B, 0 ≤ r_c l) (hc1 : ∀ l ∈ B, r_c l ≤ 1) :
    0 ≤ ∑ l ∈ B,
        (secondDiff (c l) (c l * rₐ l) (c l * r_b l) (c l * rₐ l * r_b l)
        + secondDiff (c l) (c l * rₐ l) (c l * r_c l) (c l * rₐ l * r_c l)
        + secondDiff (c l) (c l * r_b l) (c l * r_c l) (c l * r_b l * r_c l)
        + thirdDiff (c l) (c l * rₐ l) (c l * r_b l) (c l * r_c l)
            (c l * rₐ l * r_b l) (c l * rₐ l * r_c l) (c l * r_b l * r_c l)
            (c l * rₐ l * r_b l * r_c l)) :=
  Finset.sum_nonneg (fun l hl =>
    slot_nonneg_multiplicative (hc l hl) (ha1 l hl) (hb1 l hl) (hc0 l hl) (hc1 l hl))

/-- **`μ₃ > 0` is unreachable under the corrected slot assembly**, for any per-block
multiplicatively-damped trace. -/
theorem mu3_slot_ne_blockwise_multiplicative (B : Finset ι) (c rₐ r_b r_c : ι → ℝ)
    {μ₃ : ℝ} (hμ : 0 < μ₃)
    (hc : ∀ l ∈ B, 0 ≤ c l)
    (ha1 : ∀ l ∈ B, rₐ l ≤ 1) (hb1 : ∀ l ∈ B, r_b l ≤ 1)
    (hc0 : ∀ l ∈ B, 0 ≤ r_c l) (hc1 : ∀ l ∈ B, r_c l ≤ 1) :
    μ₃ ≠ -(∑ l ∈ B,
        (secondDiff (c l) (c l * rₐ l) (c l * r_b l) (c l * rₐ l * r_b l)
        + secondDiff (c l) (c l * rₐ l) (c l * r_c l) (c l * rₐ l * r_c l)
        + secondDiff (c l) (c l * r_b l) (c l * r_c l) (c l * r_b l * r_c l)
        + thirdDiff (c l) (c l * rₐ l) (c l * r_b l) (c l * r_c l)
            (c l * rₐ l * r_b l) (c l * rₐ l * r_c l) (c l * r_b l * r_c l)
            (c l * rₐ l * r_b l * r_c l))) := by
  have h := slot_nonneg_blockwise_multiplicative B c rₐ r_b r_c hc ha1 hb1 hc0 hc1
  intro hEq
  rw [hEq] at hμ
  linarith

/-! ### No non-negative re-weighting of Fréchet-obeying blocks can open the door -/

/-- **Re-weighting cannot rescue a Fréchet-obeying spectrum.**  If every block's own second
difference is non-negative (each block Fréchet-obeying, per
`Mu3BlockwiseExclusion.frechet_lower_bound_supermodular`), then *any* non-negative
re-weighting `w_λ ≥ 0` of the blocks is still supermodular.

**The hypothesis `0 ≤ w` is the whole content, and under the production convention it HOLDS —
so this lemma DOES foreclose the escape "keep the operator, change the Wedderburn weights".**

Under convention D, `y_λ = [n−2k+1]_q / [2]_q^n ≥ 0` on the two-row stratum `λ = (n−k, k)` and
`y_λ = 0` identically for `ℓ(λ) ≥ 3` (`QOU.QBeta.TemperleyLiebTower`, sorry-free).  Measured over
`n = 4 … 12` at `q₀`: **zero negative weights at every n** — the blocks split into a positive
two-row stratum and a vanishing `ℓ(λ) ≥ 3` radical.  So `0 ≤ w` is satisfied on the physical
spectrum and the sum is supermodular.

**Superseded C-frame claim, kept for readers of the older audits.**  This docstring previously
read *"the hypothesis FAILS on the physical spectrum … at `n = 9, q₀`, 10 of the 30 weights are
negative"*, citing `docs/audits/2026-05-19-weight-factor-audit.md` §W3 and
`computations/deltalambda/mu3-frechet-perblock.witness.json`.  Both belong to the **excised
convention C**, where `y_λ` was genuinely sign-indefinite for `n ≥ 4`.  The content block
`mass-theory/y-lambda-sign-pattern` withdrew that claim on 2026-08-09; this file did not follow
until the cited witness was itself drained of convention C.  Two further cautions about the old
figure: "10 of 30" was a hardcoded literal in the probe, never computed, and it did not match
that witness's own payload (20 of 60).

Consequence for the door: the mixed-sign machinery below is not reached under D.  See
`door_mechanism_dichotomy`. -/
theorem reweight_cannot_open_door (B : Finset ι) (w d₂ : ι → ℝ)
    (hw : ∀ l ∈ B, 0 ≤ w l) (hd : ∀ l ∈ B, 0 ≤ d₂ l) :
    0 ≤ ∑ l ∈ B, w l * d₂ l :=
  Finset.sum_nonneg (fun l hl => mul_nonneg (hw l hl) (hd l hl))

/-! ### Mixed-sign weights: the exhaustive door-mechanism dichotomy -/

/-- **The Fréchet slack IS the normalized second difference.**  In damping coordinates
`Δ² = c·(r_ab − (r_a + r_b − 1))`, i.e. the baseline times the Fréchet–Hoeffding slack.  This
is what makes the slack the weight-independent invariant: the block weight `y_λ` cancels out of
every ratio `r`, so the slack is a statement about the *character* alone, and the weight enters
only as the outer factor. -/
theorem secondDiff_eq_baseline_mul_slack (c rₐ r_b rₐᵦ : ℝ) :
    secondDiff c (c * rₐ) (c * r_b) (c * rₐᵦ) = c * (rₐᵦ - (rₐ + r_b - 1)) := by
  unfold secondDiff; ring

/-- **Exhaustive dichotomy of the two door mechanisms.**  A block can only push the total
submodular in one of exactly two structurally distinct ways:

* `0 < w ∧ d < 0` — **submodular geometry carried by a positive weight**: a genuine
  Fréchet–Hoeffding violation (the block's joint damping falls below `r_a + r_b − 1`);
* `w < 0 ∧ 0 < d` — **supermodular geometry carried by a negative weight**: no Fréchet
  violation at all, just a sign-indefinite Wedderburn coefficient.

Conflating these reports a bookkeeping sign as a geometric fact.  They are measured
separately by `mu3_frechet_perblock_probe.py`.

**Under convention D the second branch is VACUOUS.**  `w < 0` never occurs on the physical
spectrum (see `reweight_cannot_open_door` above: zero negative `y_λ` for `n = 4 … 12`), so a
submodular total can only come from the first mechanism — submodular geometry carried by a
positive weight.  The dichotomy itself is a theorem about arbitrary reals and is unaffected;
what changes is which branch the physics can occupy. -/
theorem door_mechanism_dichotomy {w d : ℝ} (h : w * d < 0) :
    (0 < w ∧ d < 0) ∨ (w < 0 ∧ 0 < d) := by
  rcases lt_trichotomy w 0 with hw | hw | hw
  · exact Or.inr ⟨hw, by nlinarith⟩
  · exact absurd h (by simp [hw])
  · exact Or.inl ⟨hw, by nlinarith⟩

/-- **A submodular total needs a block realising one of the two mechanisms.**  This is the
mixed-sign replacement for `reweight_cannot_open_door`: dropping the `0 ≤ w` hypothesis, one
cannot conclude supermodularity, but one *can* still name where the door must come from.

Retained as the general statement, but note it is **not** the operative one under convention D,
where `0 ≤ w` holds and `reweight_cannot_open_door` applies directly.  It
strictly refines `Mu3BlockwiseExclusion.submodular_needs_interfering_block`, which only asserts
the existence of a block with negative contribution — here that block is classified. -/
theorem door_needs_one_of_two_mechanisms (B : Finset ι) (w d : ι → ℝ)
    (h : ∑ l ∈ B, w l * d l < 0) :
    ∃ l ∈ B, (0 < w l ∧ d l < 0) ∨ (w l < 0 ∧ 0 < d l) := by
  have hlt : ∑ l ∈ B, w l * d l < ∑ _l ∈ B, (0 : ℝ) := by simpa using h
  obtain ⟨l, hl, hlt'⟩ := Finset.exists_lt_of_sum_lt hlt
  exact ⟨l, hl, door_mechanism_dichotomy hlt'⟩

end QOU.MassTheory.Mu3SlotExclusion
