/-
# The UIC per-block log: the exact pair defect, the discriminator, and the forced sign

Bean `qou-zlra`. Companion to `QOU/Mass/GradedBindingFunctionalPairTerm.lean` (PR #7223),
which proved that **no product-additive functional** — `log`, `−log`, `α·log`, any sign,
any scale — carries the Vassiliev type-two pair convolution `Σ_{i<j} bᵢbⱼ`. That closed
the `+c_k / −c_k` question for the live binding law `B = E₀·log(tr_free/tr_atom)`, a
logarithm of the **total** trace.

`prop:unified-iterative-correction` is the corpus's second, inequivalent log reading:
a weighted sum of logs of **single Wedderburn blocks**. A single block's trace is not
multiplicative over the word even when the total is, so the additive-census theorem does
**not** apply to it. This file supplies the three structural facts that the scan in
`computations/probes/uic_per_block_log_valley_scan_probe.py` needs.

## What is proved here

1. **The mechanism (§1).** For a two-branch block — two distinct crossing eigenvalues
   `x`, `y` on one generator, branch weights `wP + wM = 1` — the trace of two crossings
   differs from the product of the two single-crossing traces by exactly

       twoCrossing − oneCrossing·oneCrossing = wP · wM · (x − y)²,

   **independent of both bond offsets** (`twoCrossing_defect`,
   `twoCrossing_defect_offset_independent`). Under the normalisation `wM·(x−y)² = 1`,
   which convention D satisfies at `x = q`, `y = −q⁻¹` because `(q + q⁻¹)² = [3]_q + 1`,
   the defect is exactly `wP` (`twoCrossing_defect_eq_wPlus`). A nonzero defect is
   precisely the failure of `log tr` to be additive over bonds.

2. **The discriminator (§2).** The UIC word is the **all-pairs** layout
   (`_step_chain_generic` crosses each nucleon with every previous one), on which the
   bond census is `n_pp = C(Z,2)`, `n_pn = Z·(A−Z)`, `n_nn = C(A−Z,2)`. So any functional
   that is an affine function of that census is **exactly quadratic in `Z`**:

       Δ²_Z = 2·(f_pp + f_nn − 2·f_pn)   (constant),      Δ³_Z = 0.

   Hence a nonzero **second** difference is *not* evidence of a two-bond correlation on
   this layout — the layout supplies it. `Δ³_Z ≠ 0` is the clean separator
   (`census_secondDiff`, `census_thirdDiff`, `not_censusAffine_of_thirdDiff_ne_zero`).

3. **The forced sign** lives in the sibling `UICPerBlockLogSymmetryCurvature.lean`,
   because it is a statement about `Real.log` and an ordering and cannot be generic
   (§7c: the archimedean specialisation goes in its own file). It proves that the
   all-pairs symmetry curvature `L_pp + L_nn − 2·L_pn` is strictly **positive**, i.e.
   the symmetric nucleus is a **minimum** of the binding — an anti-valley — forced for
   every `q > 1`.

## Scope

Everything in THIS file is an exact algebraic identity holding in any commutative ring;
the archimedean half is the sibling file named above (§7c).
§1 describes a **two-branch** block; the UIC's general `λ`-block spreads crossings over
several generators via the cyclic map, where the matrices do not commute and the
two-branch form does not apply. §1 is therefore the *mechanism* by which a per-block log
leaves the additive class, not a closed form for the production accumulator.

Nothing here asserts that the UIC has, or lacks, a valley. That is measured in the probe;
§2 is what makes the measurement's discriminator meaningful.

-- Ref: [leitner2026] prop:unified-iterative-correction (mass-theory chapter); the
-- convention-D letters are `QOU/Mass/ChainTraceFactor.lean`.
-/
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

namespace QOU.Mass.UICPerBlockLogPairTerm

/-! ## 1. The non-multiplicativity defect of a two-branch block trace -/

section Defect

variable {R : Type*} [CommRing R]

/-- The trace of **one** crossing with offset `d` in a two-branch block: the two
eigenvalues `x`, `y` are shifted by `d` and weighted by `wP`, `wM`.

At `x = q`, `y = −q⁻¹` this is `ChainTraceFactor.twoStrandTrace`, which equals `z + d`
for the convention-D Markov parameter `z = q³/(q²+1)`. -/
def oneCrossing (wP wM x y d : R) : R := wP * (x + d) + wM * (y + d)

/-- The trace of **two** crossings on the *same* generator, offsets `d₁`, `d₂`. Within
each branch the eigenvalues multiply, so the two branches are summed *after* multiplying,
not before — which is exactly why this is not the product of the two one-crossing
traces. -/
def twoCrossing (wP wM x y d₁ d₂ : R) : R :=
  wP * (x + d₁) * (x + d₂) + wM * (y + d₁) * (y + d₂)

/-- **The exact non-multiplicativity defect.** For branch weights summing to one,

    twoCrossing − oneCrossing(d₁)·oneCrossing(d₂) = wP · wM · (x − y)².

The right-hand side mentions **neither offset**: the failure of multiplicativity is the
same for every pair of bonds. This is the mechanism by which a per-block logarithm leaves
the additive class of `GradedBindingFunctionalPairTerm.additive_census`. -/
theorem twoCrossing_defect (wP wM x y d₁ d₂ : R) (hw : wP + wM = 1) :
    twoCrossing wP wM x y d₁ d₂
        - oneCrossing wP wM x y d₁ * oneCrossing wP wM x y d₂
      = wP * wM * (x - y) ^ 2 := by
  have hM : wM = 1 - wP := by rw [← hw]; ring
  subst hM
  unfold twoCrossing oneCrossing
  ring

/-- The defect does not depend on the bond offsets at all. -/
theorem twoCrossing_defect_offset_independent
    (wP wM x y d₁ d₂ e₁ e₂ : R) (hw : wP + wM = 1) :
    twoCrossing wP wM x y d₁ d₂
        - oneCrossing wP wM x y d₁ * oneCrossing wP wM x y d₂
      = twoCrossing wP wM x y e₁ e₂
        - oneCrossing wP wM x y e₁ * oneCrossing wP wM x y e₂ := by
  rw [twoCrossing_defect wP wM x y d₁ d₂ hw, twoCrossing_defect wP wM x y e₁ e₂ hw]

/-- Under the normalisation `wM·(x−y)² = 1` the defect is exactly the plus-branch weight
`wP`. Convention D satisfies it at `x = q`, `y = −q⁻¹`, `wM = 1/([3]_q + 1)`, because
`(q + q⁻¹)² = q² + 2 + q⁻² = [3]_q + 1`. -/
theorem twoCrossing_defect_eq_wPlus (wP wM x y d₁ d₂ : R)
    (hw : wP + wM = 1) (hnorm : wM * (x - y) ^ 2 = 1) :
    twoCrossing wP wM x y d₁ d₂
        - oneCrossing wP wM x y d₁ * oneCrossing wP wM x y d₂ = wP := by
  rw [twoCrossing_defect wP wM x y d₁ d₂ hw, mul_assoc, hnorm, mul_one]

/-- The block trace is multiplicative over two bonds **iff** the defect vanishes; under
the `wM·(x−y)² = 1` normalisation that happens exactly when `wP = 0`, i.e. when the block
has only one live branch. So a genuinely two-branch block is never multiplicative. -/
theorem twoCrossing_mul_iff (wP wM x y d₁ d₂ : R)
    (hw : wP + wM = 1) (hnorm : wM * (x - y) ^ 2 = 1) :
    twoCrossing wP wM x y d₁ d₂
        = oneCrossing wP wM x y d₁ * oneCrossing wP wM x y d₂ ↔ wP = 0 := by
  rw [← sub_eq_zero, twoCrossing_defect_eq_wPlus wP wM x y d₁ d₂ hw hnorm]

end Defect

/-! ## 2. The discriminator: all-pairs census functionals are quadratic in `Z` -/

section Census

variable {R : Type*} [CommRing R]

/-- Forward difference in the proton number, step 1. -/
def fwd (g : R → R) (Z : R) : R := g (Z + 1) - g Z

/-- **Twice** the all-pairs bond census functional, doubled so that `C(Z,2) = Z(Z−1)/2`
needs no division and the statement holds over any commutative ring:

    2·F(Z) = f_pp·Z(Z−1) + 2·f_pn·Z(A−Z) + f_nn·(A−Z)(A−Z−1) + c.

`c` absorbs everything constant in `Z` (in the UIC that is the per-nucleon intra-nucleon
part, which is `A` letters regardless of how many are protons). -/
def census (c fpp fpn fnn A Z : R) : R :=
  c + fpp * (Z * (Z - 1)) + 2 * fpn * (Z * (A - Z)) + fnn * ((A - Z) * (A - Z - 1))

/-- The second difference of an all-pairs census functional is the **constant**
`2·(f_pp + f_nn − 2 f_pn)`. In particular it is nonzero in general — so on this layout a
nonzero second difference in `Z` is supplied by the *layout*, and is not evidence of a
two-bond correlation in the functional. -/
theorem census_secondDiff (c fpp fpn fnn A Z : R) :
    fwd (fwd (census c fpp fpn fnn A)) Z = 2 * (fpp + fnn - 2 * fpn) := by
  unfold fwd census
  ring

/-- **The discriminator.** The third difference of an all-pairs census functional vanishes
identically: such a functional is exactly quadratic in `Z`. -/
theorem census_thirdDiff (c fpp fpn fnn A Z : R) :
    fwd (fwd (fwd (census c fpp fpn fnn A))) Z = 0 := by
  unfold fwd census
  ring

/-- Contrapositive, and the form the probe actually uses: a functional with a nonzero
third difference in `Z` is **not** an affine function of the all-pairs bond census —
it carries a correlation the census cannot express. -/
theorem not_censusAffine_of_thirdDiff_ne_zero {g : R → R} {Z : R}
    (h : fwd (fwd (fwd g)) Z ≠ 0) (c fpp fpn fnn A : R) :
    g ≠ census c fpp fpn fnn A := by
  intro hg
  exact h (by rw [hg]; exact census_thirdDiff c fpp fpn fnn A Z)

end Census

#print axioms twoCrossing_defect
#print axioms twoCrossing_defect_offset_independent
#print axioms twoCrossing_defect_eq_wPlus
#print axioms twoCrossing_mul_iff
#print axioms census_secondDiff
#print axioms census_thirdDiff
#print axioms not_censusAffine_of_thirdDiff_ne_zero

end QOU.Mass.UICPerBlockLogPairTerm
