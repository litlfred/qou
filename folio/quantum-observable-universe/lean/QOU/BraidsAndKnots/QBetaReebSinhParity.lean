import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse
import Mathlib.Tactic.Ring

/-!
# QOU.BraidKnot.QBetaReebSinhParity

**The bar-parity invariant that prunes the Reeb-holonomy candidate class
for the Q_β c_3 source.**

The Reeb flow `exp(t·R)` on the state bundle 𝒮 is a hyperbolic
(`SU(1,1)`-type) holonomy whose `cosh`/`sinh` decomposition splits by
parity under the bar involution `q ↔ q⁻¹`, i.e. under `η ↦ -η` where
`η = log q`:

  - `cosh(k·η)` is **bar-EVEN**  → sources bar-symmetric c_k (c_2 = -1 ✓);
  - `sinh(k·η)` is **bar-ODD**   → the only parity-admissible source for
                                   the first bar-antisymmetric coefficient c_3.

This is the same parity wall that refuted the cos/cosh closed-form avatars
(PR #1866: even ⇒ c_3 = 0). It is the formalize-first invariant
(AGENTS.md §3.3) that prunes the Reeb candidate class **before** any
numerical scan: a c_3 source must be bar-antisymmetric, so among the Reeb
components only the `sinh` part survives.

The lemmas below are one-line consequences of Mathlib's `Real.cosh_neg`
and `Real.sinh_neg`. The companion compute
`qbeta_reeb_sinh_parity_probe.py` runs the (pruned) numerical
sign + cross-anchor-swing check on the `sinh` component.

LaTeX label: `prop:qbeta-reeb-sinh-parity`

## References
- Parity wall (even slice empty): PR #1866
- Odd reduction + recurrence data-block: PR #1880
- `P_m(h)` cosh avatar precedent: cheat-sheet §3
-/

namespace QOU.BraidKnot

/-! The bar involution on the substrate hyperbolic angle: `q ↦ q⁻¹`
corresponds to `η = log q ↦ -η` (since `q = e^η`). A function `f` of `η`
is **bar-even** if `f (-η) = f η` and **bar-odd** if `f (-η) = -f η`.
The two lemmas below establish the parity of the Reeb `cosh`/`sinh`
components; the split corollary follows. -/

/-- **Reeb cosh component is bar-even.** `cosh(k·η)` is invariant under the
bar involution `η ↦ -η`, hence sources only bar-symmetric coefficients
(the c_2 = -1 rung). -/
theorem reeb_cosh_bar_even (k : ℝ) (η : ℝ) :
    Real.cosh (k * (-η)) = Real.cosh (k * η) := by
  rw [mul_neg, Real.cosh_neg]

/-- **Reeb sinh component is bar-odd.** `sinh(k·η)` flips sign under the bar
involution `η ↦ -η`, making it the only parity-admissible source for a
bar-antisymmetric coefficient such as c_3. -/
theorem reeb_sinh_bar_odd (k : ℝ) (η : ℝ) :
    Real.sinh (k * (-η)) = -Real.sinh (k * η) := by
  rw [mul_neg, Real.sinh_neg]

/-- **Reeb-holonomy parity split.** Write a Reeb holonomy scalar as
`H(η) = a · cosh(k·η) + b · sinh(k·η)` (the `cosh`/`sinh` decomposition of
the hyperbolic flow). Its bar-conjugate `H(-η)` keeps the `cosh` term and
flips the `sinh` term:

  `H(-η) = a · cosh(k·η) − b · sinh(k·η)`.

Hence the **bar-antisymmetric part** `(H(η) − H(-η))/2 = b · sinh(k·η)` is
carried entirely by the `sinh` component. A bar-antisymmetric coefficient
(c_3) can only come from `b · sinh(k·η)` — the cosh part is parity-blocked,
exactly as the even cos/cosh avatars were (PR #1866). -/
theorem reeb_holonomy_bar_antisymmetric_part
    (a b k η : ℝ) :
    ((a * Real.cosh (k * η) + b * Real.sinh (k * η))
       - (a * Real.cosh (k * (-η)) + b * Real.sinh (k * (-η)))) / 2
      = b * Real.sinh (k * η) := by
  rw [reeb_cosh_bar_even, reeb_sinh_bar_odd]
  ring

/-- **Corollary: a bar-symmetric (cosh-only) Reeb scalar has zero
bar-antisymmetric part.** Setting `b = 0` in the split above: a pure
`cosh` Reeb holonomy contributes nothing to c_3 — the formal statement of
"the cosh/even component cannot source the first bar-antisymmetric
coefficient." -/
theorem reeb_cosh_only_no_bar_antisymmetric_part (a k η : ℝ) :
    ((a * Real.cosh (k * η)) - (a * Real.cosh (k * (-η)))) / 2 = 0 := by
  rw [reeb_cosh_bar_even]
  ring

/-! ### Phase-series reframe (PR #1871 §3 ↔ the c_k ladder)

PR #1871 derived that the Q_β observables are `cosh`/`sinh` of a single
hyperbolic phase. At the c_k-ladder level this means
`Q_β / Q_A = cos(Φ(u))` (cosh of an imaginary fibre phase), with
`Φ(u) = Φ₁·u + Φ₂·u² + …`. The truncated cosine `1 − Φ²/2` gives the
order-u² and order-u³ coefficients as exact ring identities, which pin
the phase coefficients to the (proved) c_2 and the (cal-anchored) c_3.
The companion compute `qbeta_cosh_phase_series_reframe_probe.py` reads
off `Φ₁ = √2` (from `c_2 = −1`) and the hand-off target
`Φ₂ = −c_3/√2`. -/

/-- **Phase ↔ (c_2, c_3) algebraic core.** For the truncated cosine phase
`P(u) = 1 − (Φ₁u + Φ₂u²)²/2`, the order-u² coefficient is `−Φ₁²/2` and the
order-u³ coefficient is `−Φ₁·Φ₂` (the rest is the `−Φ₂²/2·u⁴` tail):

  `1 − (Φ₁u + Φ₂u²)²/2 = 1 − (Φ₁²/2)·u² − (Φ₁·Φ₂)·u³ − (Φ₂²/2)·u⁴`.

Reading coefficients: `c_2 = −Φ₁²/2` (⇒ `Φ₁² = 2` from the proved
`c_2 = −1`) and `c_3 = −Φ₁·Φ₂` (the odd-rung reduction `c_3 = g` of
PR #1880, with `g = −Φ₁·Φ₂`). One-line `ring` identity. -/
theorem qbeta_phase_cos_truncation (Φ₁ Φ₂ u : ℝ) :
    1 - (Φ₁ * u + Φ₂ * u ^ 2) ^ 2 / 2
      = 1 - (Φ₁ ^ 2 / 2) * u ^ 2 - (Φ₁ * Φ₂) * u ^ 3 - (Φ₂ ^ 2 / 2) * u ^ 4 := by
  ring

/-- **`Φ₁² = 2` from `c_2 = −1`.** With the u² coefficient `c_2 = −Φ₁²/2`
set to the Lean-proved value `−1`, the leading phase coefficient satisfies
`Φ₁² = 2` — i.e. `Φ₁ = √2` (the fibre `cos(√2·u)` slice; the imaginary
hyperbolic angle `i√2` of the bar-even `cosh` channel). -/
theorem qbeta_phase_leading_sq_eq_two (Φ₁ : ℝ) (hc2 : -(Φ₁ ^ 2 / 2) = -1) :
    Φ₁ ^ 2 = 2 := by
  linarith

/-- Subtracting two from the squared leading phase coefficient yields zero when the quadratic coefficient is negative one. -/
theorem qbeta_phase_leading_sq_sub_two_eq_zero (Φ₁ : ℝ) (hc2 : -(Φ₁ ^ 2 / 2) = -1) :
    Φ₁ ^ 2 - 2 = 0 := by
  rw [qbeta_phase_leading_sq_eq_two Φ₁ hc2, sub_self]

end QOU.BraidKnot
