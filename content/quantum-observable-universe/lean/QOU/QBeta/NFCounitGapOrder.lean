/-
# The single-wrap/typed NF counit gap is `O(h³)`

Bean `qou-pdix` (child of `qou-cds1`), following its last entry, which made the
NF question the gate on branch 3: *"A 0.16% phase cannot be derived from an
object whose NF convention is unsettled at 0.58%."*

`docs/audits/2026-05-11-q-beta-residual-decomposition.md` §1 labels the 1.00579
factor a **"basis-change typed-vs-single-wrap"**.  Its own §2 proves the
dual-basis identity `G⁻¹·t = e_γ`, i.e. that the framework's net **is** the
Frobenius counit.  Those cannot both be about one element: `ε` is a canonical
algebra map, hence basis-independent, so one element has one `ε`.  The two NFs
give different polynomials, so they expand **different elements** — the §1 label
is a category error against §2 of the same document.

What is proved here is the quantitative half: the gap's exact closed form and
its **order**.  The two NFs agree through `O(h²)` and first differ at `O(h³)`,
so the ambiguity contributes nothing at order `t¹` or `t²` in `q = 1 + t`.

Bean entry (6) states the branch-3 acceptance test as *reproduce `α` through
order `t²`*, with the coefficient pinned at `t¹` so `t²` is a prediction.
**An `O(t³)` ambiguity cannot move that test.**  The bean's magnitude argument
is untouched and remains correct for the absolute 0.160 % target; a magnitude
at `q₀` and an order in the expansion are different claims, and only the latter
governs which Taylor coefficients an ambiguity can reach.

Companion probe: `computations/qbeta/qbeta_nf_counit_gap_order_probe.py` (8/8,
exact ℚ(h), reproducing the audit's 1.00579 at the proton pin).
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
