/-
# The single-wrap/typed NF **counit** gap is `O(h³)` — and that does NOT free the phase

Bean `qou-pdix` (child of `qou-cds1`).

## Read the scope before reusing these theorems

Every theorem below is about the **counit** `ε`, and each is correct. The
docstring first attached to them drew a conclusion about the **phase** `α`, and
that conclusion is **RETRACTED**. They are different functionals:

    α = (ε(n−p) − tr_M(n−p)) / 2                    [bean entry (9)]

Measured, first nonzero order in `t` with `q = 1 + t`, the same in **both**
conventions:

    ε      gap   t³   (coeff −2)
    tr_M   gap   t¹   (coeff −1/4)
    **α**  gap   **t¹**  (coeff **1/8**)

So the NF choice moves the phase at **first** order, and the bean's gate on
branch 3 **stands exactly as written**. The bean was right; the correction of it
was not.

**Why the two halves differ, which is the part worth keeping.** The counit sets
every `z^k ↦ 1`; the Markov trace weights by `z^{#cr}`. The two NFs differ
precisely in the `L₊/L₋/e⁻` coefficients, whose crossing numbers are 2, 2, 3 —
so under `ε` those differences cancel down to `O(h³)`, and under `tr_M` they
survive at `O(t)`. **The NF sensitivity of the phase lives entirely in the
crossing-number grading**, not in the algebra, so no re-basing of the counit can
remove it.

## What these theorems do establish

The exact closed form of the counit gap, reproducing the 1.00579 factor of
`docs/audits/2026-05-11-q-beta-residual-decomposition.md` §1 to six digits.

That audit labels the factor a **"basis-change typed-vs-single-wrap"**, while
its own §2 proves the dual-basis identity `G⁻¹·t = e_γ` — *"the net **is** the
Frobenius counit"*. Those cannot both be about one element: `ε` is a canonical
algebra map, hence basis-independent, so one element has one `ε`. The two NFs
give different polynomials (`epsTyped_ne_epsSingleWrap`), so they expand
**different elements**, and §1's label is a category error against §2 of the
same document. That much is unaffected by the retraction above, and it reframes
the open question as *"which braid element is the canonical nucleon pair"*
rather than a convention to be picked.

Companion probe: `computations/qbeta/qbeta_nf_counit_gap_order_probe.py`
(17/17, exact ℚ(h); reproduces both the audit's 1.00579 and bean entry (6)'s
independently-computed `α` coefficients).
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic

namespace QOU.QBeta.NFCounitGap

variable {K : Type*} [Field K]

/-- Counit of the neutron−proton difference in the **single-wrap** nucleon NF:
`ε(n−p) = h(h−2)/2`.  (Recomputed symbolically in the companion probe and
validated against the live `PROTON_NF`/`NEUTRON_NF`; it is the vector asserted
in the 2026-06-16 counit-vs-trace audit.) -/
def epsSingleWrap (h : K) : K := h * (h - 2) / 2

/-- Counit of the same difference in the **typed 6-term** NF, the one the live
mass compute uses:
`ε(n−p) = h(h⁶+2h⁵+2h⁴+2h³−h²+2h−4)/4`. -/
def epsTyped (h : K) : K :=
  h * (h ^ 6 + 2 * h ^ 5 + 2 * h ^ 4 + 2 * h ^ 3 - h ^ 2 + 2 * h - 4) / 4

/-- **The gap, in closed form.**  Reproduces the audit's `1.00579` at `q₀`. -/
theorem gap_closed_form (h2 : (2 : K) ≠ 0) (h : K) :
    epsTyped h - epsSingleWrap h
      = h ^ 3 * (h ^ 4 + 2 * h ^ 3 + 2 * h ^ 2 + 2 * h - 1) / 4 := by
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by norm_num
    rw [e]; exact mul_ne_zero h2 h2
  unfold epsTyped epsSingleWrap
  field_simp
  ring

/-- **The gap is divisible by `h³`** — the two NFs agree through `O(h²)`.
Stated as an exact factorisation rather than an asymptotic claim, so it carries
no analytic side conditions. -/
theorem gap_eq_h_cubed_mul (h2 : (2 : K) ≠ 0) (h : K) :
    epsTyped h - epsSingleWrap h
      = h ^ 3 * ((h ^ 4 + 2 * h ^ 3 + 2 * h ^ 2 + 2 * h - 1) / 4) := by
  rw [gap_closed_form h2]; ring

/-- The cofactor at `h = 0` is `−1/4`: the leading term of the gap is `−h³/4`,
so the vanishing is **exactly** to third order, not higher. -/
theorem gap_cofactor_at_zero :
    ((0 : K) ^ 4 + 2 * 0 ^ 3 + 2 * 0 ^ 2 + 2 * 0 - 1) / 4 = -(1 / 4) := by
  norm_num
  ring

/-- **The two counits are different**, so — `ε` being canonical, hence
basis-independent — the two NFs expand **different elements**.  Witnessed at
`h = 1`, where the gap is `−1/4 ≠ 0`. -/
theorem epsTyped_ne_epsSingleWrap :
    epsTyped (1 : ℚ) ≠ epsSingleWrap (1 : ℚ) := by
  unfold epsTyped epsSingleWrap; norm_num

/-- The gap at `h = 1` is exactly `3/2` — `1 − (−1/2)`, matching the closed
form's cofactor `(1+2+2+2−1)/4 = 3/2`.  (Not `−1/4`: that is the cofactor's
value at `h = 0`, a different quantity, and Lean caught the conflation.) -/
theorem gap_at_one : epsTyped (1 : ℚ) - epsSingleWrap (1 : ℚ) = 3 / 2 := by
  unfold epsTyped epsSingleWrap; norm_num

/-- **The consequence for the acceptance test.**  Any quantity of the form
`h³ · c` vanishes to third order, so for the purposes of a Taylor comparison
pinned at first order and predicting second order, the gap is invisible:
substituting `h = 0` kills it, as does its first and second derivative data.
Stated concretely as: the gap is a multiple of `h³`, hence of `h²`, hence of
`h` — each of which is the algebraic content of "contributes nothing below
order three". -/
theorem gap_dvd_h_sq (h2 : (2 : K) ≠ 0) (h : K) :
    ∃ c : K, epsTyped h - epsSingleWrap h = h ^ 2 * c :=
  ⟨h * ((h ^ 4 + 2 * h ^ 3 + 2 * h ^ 2 + 2 * h - 1) / 4), by
    rw [gap_closed_form h2]; ring⟩

/-- The gap vanishes at `h = 0` (the classical point `q = 1`). -/
theorem gap_at_zero (h2 : (2 : K) ≠ 0) :
    epsTyped (0 : K) - epsSingleWrap (0 : K) = 0 := by
  rw [gap_closed_form h2]; ring

end QOU.QBeta.NFCounitGap
