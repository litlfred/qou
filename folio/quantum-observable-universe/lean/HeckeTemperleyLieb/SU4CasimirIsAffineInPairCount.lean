/-
# The SU(4) Casimir carries no three-body content — it is affine in the pair count

`qou-edt7` asked for a derivation of `β`, the coefficient in the fitted form
`w(A) = α − β · C₂([1^A])` that predicted `w(3)` to 0.71 %. **`β` cannot be
derived, and this file says why: the form it belongs to has no origin in a
two-body SU(4)-invariant interaction, because the Casimir is an affine function
of the pair count.**

## The two identities

Writing `C₂([1^n]) = (5/8)·n·(4−n)` for the quadratic Casimir of the fully
antisymmetric representation of SU(4), and clearing denominators (`casimirX8`
is `8·C₂`, `pairCountX2` is `2·C(n,2) = n(n−1)`):

* `casimirX8_eq` — `8·C₂ = 15n − 5·n(n−1)`, i.e.

      C₂([1^n]) = (15/8)·n − (5/4)·C(n,2)

  the Casimir is **affine in the pair count**, with `n` the only other term.

* `pairSum_eq` — the two-body sum `S(n) = Σ_{i<j} λᵢ·λⱼ = ½(C₂ − n·C₂(fund))`
  with `C₂(fund) = 15/8` satisfies `16·S = −5·n(n−1)`, i.e.

      S(n) = −(5/8)·C(n,2)      **exactly, for every n**

## What that costs the candidate

`S` is what a two-body SU(4)-invariant interaction contributes when summed over
the `A`-body state. It is **exactly proportional to the pair count**, so such an
interaction contributes a *constant* per pair. In the coordination-weight
coordinate that is `w` constant, hence `b₃ = 0` — the pairwise wall again, now
reached from the group theory rather than from the counting bound of
`QOU.Mass.UniformBondSimpleGraphExclusion`. The two agree, which is a check on
both.

So the SU(4) Casimir **cannot** produce the measured rise from two-body physics.
The fitted `w(A) = α − β·C₂` is therefore *not* the SU(4) prediction; by
`casimirX8_eq` it is just `w` linear in `n` and `C(n,2)` along one fixed
direction, and no group-theoretic content survives the affine reduction. There
is nothing for a derivation of `β` to attach to.

## What the fit actually was

Because `C₂` takes the values `2.5, 1.875, 0` at `A = 2,3,4`, fitting the two
endpoints and predicting the middle is the fixed interpolation

    w(3) = ¾·w(2) + ¼·w(4)        (λ = 3/4 exactly)

equivalently the linear relation `B(4) = 8·B(3) − 18·B(2)`. Two consequences,
both recorded in `computations/probes/su4_casimir_beta_derivation_probe.py`:

1. It is a **better** relation than the corpus simplex baseline `μ₄ = 0`
   (`B(4) = 4B(3) − 6B(2)`), which misses `B(4)` by 32.7 %; this one misses by
   1.7 % on the Coulomb-corrected convention. That is real and is why the fit
   looked good.
2. The residual is **not** convention- or variable-independent. On the
   Coulomb-corrected convention it reads 0.71 % stated on `B(3)` and 1.71 %
   stated on `B(4)` — an amplification of `8·B(3)/B(4) ≈ 2.4`, since `B(3)`
   enters the relation with a factor 8. Quoting the smaller of the two was
   flattering.

## Scope

This does not refute Wigner SU(4) as physics, and it does not touch the
**support** bound (`dim [1^n] = C(4,n) = 0` for `n ≥ 5`) that locates the
turnover at `A = 4` — that argument uses the *vanishing of the representation*,
not its Casimir, and is untouched. What is closed is the specific route
"derive `β` from an SU(4)-invariant two-body interaction": there is no such `β`,
because that interaction has no Casimir term to carry one.

Base ring is a generic `CommRing`; the content is polynomial identity.

Bean `qou-edt7`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

namespace QOU.Mass.SU4CasimirIsAffineInPairCount

variable {R : Type*} [CommRing R]

/-- `8 · C₂([1^n])` for the fully antisymmetric representation of SU(4), whose
Casimir is `(5/8)·n·(4−n)`. Scaled by 8 to stay in a ring without division. -/
def casimirX8 (n : R) : R := 5 * n * (4 - n)

/-- `2 · C(n,2) = n(n−1)`, the pair count scaled by 2. -/
def pairCountX2 (n : R) : R := n * (n - 1)

/-- `16 · S(n)` where `S(n) = Σ_{i<j} λᵢ·λⱼ = ½(C₂([1^n]) − n·C₂(fund))` and
`C₂(fund) = 15/8`; scaled by 16, so `16·S = 8·C₂ − 15n`. -/
def pairSumX16 (n : R) : R := casimirX8 n - 15 * n

/-- **The Casimir is affine in the pair count.** `8·C₂ = 15n − 5·n(n−1)`, i.e.
`C₂([1^n]) = (15/8)·n − (5/4)·C(n,2)`. Every apparent dependence of the Casimir
on the many-body structure is carried by `n` and the pair count alone. -/
theorem casimirX8_eq (n : R) : casimirX8 n = 15 * n - 5 * pairCountX2 n := by
  unfold casimirX8 pairCountX2
  ring

/-- **The two-body sum is exactly proportional to the pair count.**
`16·S = −5·n(n−1)`, i.e. `S(n) = −(5/8)·C(n,2)` for every `n`.

This is the load-bearing statement: a two-body SU(4)-invariant interaction
summed over the fully antisymmetric `A`-body state contributes a *constant per
pair*, so it gives a constant coordination weight and `b₃ = 0`. The SU(4)
Casimir cannot produce a three-body cumulant. -/
theorem pairSum_eq (n : R) : pairSumX16 n = -5 * pairCountX2 n := by
  unfold pairSumX16 casimirX8 pairCountX2
  ring

/-- Restated as the proportionality itself: `16·S + 5·(2·C(n,2)) = 0`, so the
ratio `S / C(n,2)` is the constant `−5/8` and carries no `n`-dependence for a
coordination weight to inherit. -/
theorem pairSum_add_five_pairCount (n : R) :
    pairSumX16 n + 5 * pairCountX2 n = 0 := by
  rw [pairSum_eq]; ring

/-- The Casimir differences that the fit actually used, as a ring identity:
`C₂` at `n` and `n+1` differ by `(5/8)(3 − 2n)`, scaled here by 8. Included so
the `λ = 3/4` interpolation of the fitted model is checkable from the file
rather than only from the probe. -/
theorem casimirX8_succ_sub (n : R) :
    casimirX8 (n + 1) - casimirX8 n = 5 * (3 - 2 * n) := by
  unfold casimirX8
  ring

end QOU.Mass.SU4CasimirIsAffineInPairCount
