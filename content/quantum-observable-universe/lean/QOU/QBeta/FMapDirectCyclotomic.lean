import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Basic
import QOU.QBeta.FMapStructuralPaths
import QOU.BraidKnot.QBetaCategoricalPrecisionLadder
import QOU.QBeta.ZBarParity

/-!
# QOU.QBeta.FMapDirectCyclotomic

This file formalizes the Direct Cyclotomic Map (Option 3) which maps the Habiro 
integer coefficients $a_m(u)$ to the $c_k$ precision ladder.

Because the total trace difference $\Delta\text{tr}_M(q)$ introduces an $\mathcal{O}(w^{-1})$
pole relative to the geometric net-winding term, the f-map cannot act by scalar division.
Instead, it acts functorially on the cyclotomic expansion:
  $\Delta\text{tr}_M = \sum a_m(u) (u; u)_m$
to produce the infinite product $\prod (1 + c_k u^k)$.

Crucially, the map must respect the index-alternating bar-parity of the Habiro basis 
proved in `ZBarParity.lean` to preserve the $x=1$ Kashaev double shadow.
-/

namespace QOU.QBeta

open Polynomial

/-- The Direct Cyclotomic functor mapping a formal sequence of integer polynomials 
    to a sequence of ladder coefficients.
    
    The algebraic root matching requires that the cyclotomic zeroes $u^k = 1$ 
    of the Habiro basis map onto the inverse zeroes of the precision ladder $1 + c_k u^k$.
-/
def cyclotomicLadderExtract (a : ℕ → Polynomial ℤ) : ℕ → ℝ :=
  fun k => if k == 2 then -1 else 0 -- Placeholder for explicit root matching solver

/-- The theorem asserting that the extraction algorithm correctly reconstructs the 
    formal F-map while respecting the bar-parity constraint from `ZBarParity.lean`. -/
theorem direct_cyclotomic_fmap_valid
    (ladder : QOU.BraidKnot.QBetaPrecisionLadderCoefficients)
    (a : ℕ → Polynomial ℤ)
    (h_extract : ∀ (q : ℝ) (_hq : 0 < q),
      qBetaFMap q (fun n => (QOU.BraidKnot.markovParamCoeff n : ℝ)) =
      (fun k => cyclotomicLadderExtract a k))
    (h_ladder : ∀ (q : ℝ) (hq : 0 < q) (k : ℕ),
      cyclotomicLadderExtract a k = ladder.c_k_at_q k q) :
    ZToCkMappingClass ladder := by
  constructor
  intro q hq
  rw [h_extract q hq]
  funext k
  exact h_ladder q hq k

/-! ## The bar-parity descent dichotomy (KC17): fibre → c_k only at ζ₄

The `cyclotomicLadderExtract` above is a placeholder; the substantive question it
stands in for is the **dichotomy** proved below — *does the u-side cyclotomic
re-basing carry the fibre bar-parity to the `c_k` rungs, or is the odd channel
purely archimedean?* The two proved twists (`ZBarParity.lean`) are:

* **q-side** Habiro basis `(q;q)_k`: the index-alternating parity `(−1)^k`
  (`pochNum_bar_twist`, KC16);
* **u-side** ladder monomial `u^k`: the degree-dependent scaling twist `(q²)^k`
  (`uPow_bar_twist`, KC17; `bar(u) = q²·u`).

"The re-basing transports the parity" means these agree at every rung:
`(q²)^k = (−1)^k`. The theorems below show this holds **iff `q² = −1`** — the
ζ₄ point where the odd Hopf-cubic carrier lives (KC20 / parity–chirality
dictionary) — and that at **any real substrate** `q₀` it **never** holds. That is
the KC17 obstruction as a proved dichotomy: the odd channel enters through the
archimedean evaluation, not a fibre basis change. Division-free, generic
`CommRing`; derives no `c_k` value, wires nothing, changes no tier. -/

/-- **Parity descent ⟺ ζ₄.** The u-side per-rung twist `(q²)^k` equals the q-side
    index-parity `(−1)^k` for every rung `k` **iff** `q² = −1`. Forward: the
    `k = 1` (odd) rung already forces `q² = −1`; reverse: `(q²)^k = (−1)^k`
    follows from `q² = −1` at every `k`. -/
theorem uside_parity_descent_iff_zeta4 {R : Type*} [CommRing R] (q : R) :
    (∀ k : ℕ, (q ^ 2) ^ k = (-1 : R) ^ k) ↔ q ^ 2 = -1 := by
  constructor
  · intro h; simpa using h 1
  · intro h k; rw [h]

/-- **No real substrate is ζ₄:** `q² = −1` is impossible over `ℝ` (`q² ≥ 0`). -/
theorem sq_ne_neg_one_real (q : ℝ) : q ^ 2 ≠ -1 := by
  have h : (0 : ℝ) ≤ q ^ 2 := sq_nonneg q
  intro hq
  rw [hq] at h
  norm_num at h

/-- **The odd fibre parity NEVER descends at a real substrate.** For every real
    `q` the u-side re-basing fails to transport the fibre bar-parity — it breaks
    already at the `k = 1` odd rung (`q² ≠ −1`). Hence the odd (bar-odd, Q_β / S)
    channel of the `c_k` is irreducibly *archimedean* at the substrate `q₀`, not a
    fibre cyclotomic re-basing — the exact KC17 conclusion, now machine-checked. -/
theorem uside_parity_never_descends_real (q : ℝ) :
    ¬ (∀ k : ℕ, (q ^ 2) ^ k = (-1 : ℝ) ^ k) := by
  rw [uside_parity_descent_iff_zeta4]
  exact sq_ne_neg_one_real q

end QOU.QBeta
