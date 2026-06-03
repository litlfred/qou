/-
  # c_k precision-ladder recursion from Habiro q-difference equation

  Sibling .lean for the `prop:q-beta-c-k-recursion-from-habiro-q-difference`
  block.  Encodes the depth-d linear recursion structure on the c_k
  ladder coefficients induced by a fibre-level Habiro element F(q)
  satisfying a q-difference equation of depth d.

  The recursion machinery is independent of the specific kernel —
  once a particular F(q) is identified categorically, instantiating
  `CKRecursion ℝ` with the extracted kernel turns this scaffold into
  a concrete c_k predictor.  The proved seed c_2 = -1 (PR #1602,
  bar-even constraint) is an input to `applyRecursion`.

  Sorry-free.  Two ingredients:

  * `structure CKRecursion R` — depth + kernel-vector data.
  * `def applyRecursion` — one step of the recursion (inner product
    of the kernel with the last `depth` c_k values).

  Ref: [pr1602] https://github.com/litlfred/qou/pull/1602
       [pr1750] https://github.com/litlfred/qou/pull/1750
       [pr1752] https://github.com/litlfred/qou/pull/1752
       [pr1769] https://github.com/litlfred/qou/pull/1769
       [habiro2004] https://doi.org/10.4310/MRL.2004.v11.n4.a4
       [jones1987] https://doi.org/10.1090/S0273-0979-1985-15304-2
       [wenzl1988] https://doi.org/10.1007/BF02101492
       docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
       docs/audits/2026-06-03-qbeta-sdp-strict-complementarity-partial.md
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Tactic.Ring

namespace QOU.QBeta.CKRecursion

universe u

/-- **Depth-$d$ linear recursion data for the $c_k$ precision-ladder
    coefficients.**

    A fibre-level Habiro element $F$ satisfying a $q$-difference equation
    of depth $d$ — `F(q ξ) = R(q,ξ) · F(ξ)` with $R$ a Laurent polynomial
    of degree $d$ in $\xi^{-1}$ — induces a depth-$d$ linear recursion
    among the Taylor coefficients of $F$.  The change-of-basis from
    the Habiro `(u;u)_m` ring to the ladder $u^k$ inherits the same
    depth, so the precision-ladder $c_k$ satisfy

    $$c_{k+1} = \sum_{j=0}^{d-1} \text{kernel}(j) \cdot c_{k - j}.$$

    Fields:
    * `depth` — order of the recursion (number of prior $c_k$ consumed)
    * `kernel : Fin depth → R` — the ring-valued recursion coefficients

    Instantiation requires specifying the kernel.  The seed value
    $c_2 = -1$ (PR #1602) is supplied to `applyRecursion` as input. -/
structure CKRecursion (R : Type u) [Field R] where
  depth : ℕ
  kernel : Fin depth → R

namespace CKRecursion

/-- **Apply one step of the recursion.**

    Given the last `depth` values of the $c_k$ sequence in
    chronological order (`history 0` is the most recent, `history
    (depth-1)` the oldest), output the next $c_k$ as the inner product
    of the kernel with the history.

    The recursion is *purely linear* — no nonlinear iteration, no
    fixed-point search.  Once the kernel is identified (e.g. via the
    categorical $f$-construction of `rem:markov-trace-inductive-limit`),
    every $c_k$ for $k \ge 2 + \text{depth}$ follows by repeated
    application from the seed values. -/
def applyRecursion {R : Type u} [Field R] (rec : CKRecursion R)
    (history : Fin rec.depth → R) : R :=
  Finset.sum (Finset.univ : Finset (Fin rec.depth))
    (fun j => rec.kernel j * history j)

/-- **Recursion is linear in the history.**  Mixing two history vectors
    `h1, h2` and applying the recursion gives the same result as
    applying the recursion separately to each and adding.  Pure
    structural identity — `Finset.sum_add_distrib` + `mul_add`. -/
theorem applyRecursion_linear {R : Type u} [Field R] (rec : CKRecursion R)
    (h1 h2 : Fin rec.depth → R) :
    rec.applyRecursion (fun j => h1 j + h2 j) =
      rec.applyRecursion h1 + rec.applyRecursion h2 := by
  unfold applyRecursion
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro j _
  ring

end CKRecursion

end QOU.QBeta.CKRecursion
