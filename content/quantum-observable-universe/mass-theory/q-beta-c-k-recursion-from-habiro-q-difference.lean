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

  Sorry-free.  Ingredients:

  * `structure CKRecursion R` — depth + kernel-vector data.
  * `def applyRecursion` — one step of the recursion (inner product
    of the kernel with the last `depth` c_k values).
  * `def esymm` + `esymm_neg` + `esymm_bar_parity` — the
    **parity-alternation theorem**: the recursion coefficients
    `a_j = e_j({rates})` alternate bar-parity (`bar(e_j) = (-1)^j e_j`)
    when the f-map feeds bar-odd per-mode rates.  Mode-set-independent;
    the structural law behind the ladder's parity bookkeeping.

  Ref: [pr1602] https://github.com/litlfred/qou/pull/1602
       [pr1750] https://github.com/litlfred/qou/pull/1750
       [pr1752] https://github.com/litlfred/qou/pull/1752
       [pr1769] https://github.com/litlfred/qou/pull/1769
       [habiro2004] https://doi.org/10.4310/MRL.2004.v11.n4.a4
       [jones1987] https://doi.org/10.2307/1971403
       [wenzl1988] https://doi.org/10.1007/BF02101492
       docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
       docs/audits/2026-06-03-qbeta-sdp-strict-complementarity-partial.md
       docs/audits/2026-06-13-qbeta-root-of-unity-residue-program.md
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fintype.Basic
import Mathlib.Tactic.Ring
import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.RingTheory.Polynomial.Cyclotomic.Expand
import Mathlib.Tactic.FieldSimp

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

/-! ## Parity-alternation of the recursion coefficients

  In the heat-route product picture the depth-$d$ recursion coefficients
  $a_j$ are the **elementary symmetric polynomials** $e_j$ of the
  per-mode rates $r_\lambda = (q-1)\,\mu_\lambda$.  When the $f$-map feeds
  *bar-odd* rates (the bar-odd projections, which still carry each mode's
  root-of-unity content by the cyclotomic bar-stability lemma), the
  coefficients alternate bar-parity:
  $\overline{e_j} = (-1)^j e_j$.  So $a_j$ is bar-EVEN for even $j$ and
  bar-ODD for odd $j$ — the structural law behind the ladder's parity
  bookkeeping (bar-even seed $c_2 = -1$ driven by a bar-odd $a_1 = -c_3$,
  a bar-even $a_2$, a bar-odd $a_3$, …).  It is a one-line consequence of
  $e_j(-x) = (-1)^j e_j(x)$, and is independent of which modes are active. -/

open Finset in
/-- **Elementary symmetric polynomial** $e_j(r)$ of a finite family
    `r : Fin n → R`: the sum, over $j$-element subsets, of the product of
    the chosen rates.  The depth-$d$ recursion coefficient $a_j$ is
    $e_j$ of the active per-mode rates $r_\lambda = (q-1)\mu_\lambda$. -/
def esymm {R : Type u} [CommRing R] {n : ℕ} (r : Fin n → R) (j : ℕ) : R :=
  ∑ S ∈ powersetCard j (univ : Finset (Fin n)), ∏ i ∈ S, r i

/-- **Negating the rates scales $e_j$ by $(-1)^j$.**  Each $j$-subset
    product picks up one sign per chosen element, i.e. $(-1)^j$, which
    factors out of the sum. -/
theorem esymm_neg {R : Type u} [CommRing R] {n : ℕ} (r : Fin n → R) (j : ℕ) :
    esymm (fun i => - r i) j = (-1 : R) ^ j * esymm r j := by
  unfold esymm
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun S hS => ?_
  rw [Finset.mem_powersetCard] at hS
  calc ∏ i ∈ S, -(r i)
      = ∏ i ∈ S, ((-1 : R) * r i) := by
        refine Finset.prod_congr rfl fun i _ => ?_
        ring
    _ = (∏ i ∈ S, (-1 : R)) * ∏ i ∈ S, r i := Finset.prod_mul_distrib
    _ = (-1 : R) ^ S.card * ∏ i ∈ S, r i := by rw [Finset.prod_const]
    _ = (-1 : R) ^ j * ∏ i ∈ S, r i := by rw [hS.2]

/-- **Parity-alternation theorem.**  For an involutive ring homomorphism
    `bar` under which every rate is **bar-odd** (`bar (r i) = - r i`), the
    elementary symmetric polynomials satisfy $\overline{e_j} = (-1)^j e_j$.
    Hence the recursion coefficient $a_j = e_j$ is bar-EVEN for even $j$ and
    bar-ODD for odd $j$ — they alternate bar-parity, independent of which
    modes are active.  (The bar `q ↦ q⁻¹` of the fibre ring instantiates
    `bar`.) -/
theorem esymm_bar_parity {R : Type u} [CommRing R] {n : ℕ} (bar : R →+* R)
    (r : Fin n → R) (j : ℕ) (hodd : ∀ i, bar (r i) = - r i) :
    bar (esymm r j) = (-1 : R) ^ j * esymm r j := by
  have hmap : bar (esymm r j) = esymm (fun i => bar (r i)) j := by
    unfold esymm
    rw [map_sum]
    refine Finset.sum_congr rfl fun S _ => ?_
    rw [map_prod]
  rw [hmap, show (fun i => bar (r i)) = (fun i => - r i) from funext hodd, esymm_neg]

/-! ## Cyclotomic bar-stability — the lemma behind ζ₆-closed

  The period-3/ζ₆ closure (root-of-unity residue program, #2240) rests on a
  general fact: every cyclotomic polynomial `Φ_d` (`d > 1`) is **self-reciprocal**,
  `bar(Φ_d) = q^{-φ(d)}·Φ_d` under the fibre bar involution `q ↦ q⁻¹`. Cleared of
  denominators this reads `Φ_d(1/q)·q^{φ(d)} = Φ_d(q)`. The lemmas below verify it
  for the qbeta-relevant `d ∈ {2, 3, 6}` (`φ = 1, 2, 2`) — in particular `Φ_6`,
  the period-3 carrier — from Mathlib's explicit forms `cyclotomic_two/three/six`.

  **Corollary (divisibility bar-invariance), narrative.** Since `bar(Φ_d)` is a
  unit multiple (`q^{-φ(d)}`) of `Φ_d`, one has `Φ_d ∣ X ⟺ Φ_d ∣ bar(X)`, hence
  `Φ_d ∣ (X)_odd := (X - bar X)/2` whenever the odd part is nonzero. That is why
  the bar-ODD projection of a single ζ₆-carrier still carries ζ₆ — closing
  period-3/ζ₆ with no cross-mode cancellation.

  Ref: docs/audits/2026-06-13-qbeta-root-of-unity-residue-program.md -/

open Polynomial in
/-- `Φ_2` is self-reciprocal: `Φ_2(1/q)·q = Φ_2(q)` (`φ(2)=1`). -/
theorem cyclotomic_two_bar_stable {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    (cyclotomic 2 R).eval (1 / q) * q ^ 1 = (cyclotomic 2 R).eval q := by
  rw [cyclotomic_two]
  simp only [eval_add, eval_X, eval_one, pow_one]
  field_simp
  ring

open Polynomial in
/-- `Φ_3` is self-reciprocal: `Φ_3(1/q)·q² = Φ_3(q)` (`φ(3)=2`). -/
theorem cyclotomic_three_bar_stable {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    (cyclotomic 3 R).eval (1 / q) * q ^ 2 = (cyclotomic 3 R).eval q := by
  rw [cyclotomic_three]
  simp only [eval_add, eval_pow, eval_X, eval_one]
  field_simp
  ring

open Polynomial in
/-- `Φ_6` is self-reciprocal: `Φ_6(1/q)·q² = Φ_6(q)` (`φ(6)=2`) — the period-3/ζ₆
    carrier whose bar-stability closes the period-3 constraint. -/
theorem cyclotomic_six_bar_stable {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    (cyclotomic 6 R).eval (1 / q) * q ^ 2 = (cyclotomic 6 R).eval q := by
  rw [cyclotomic_six]
  simp only [eval_add, eval_sub, eval_pow, eval_X, eval_one]
  field_simp
  ring

end QOU.QBeta.CKRecursion
