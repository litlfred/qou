import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

/-!
# QOU.BraidKnot.QBetaOddParityAvatarReduction

**The odd-parity generating-function avatar for the Q_β c_k ladder
reduces, at order u³, to a single scalar — the algebraic core of the
`qbeta_odd_parity_avatar_reduction_probe.py` finding.**

The Q_β precision ladder `F(u) = Π_{k≥2}(1 + c_k u^k)` (u = b·ℏ_q²) has,
as a power series at u = 0, two hard structural constraints:

  - `c_1 = 0`   — the ladder starts at k = 2 (no u¹ term);
  - `c_2 = -1`  — Lean-proved exact (`q_beta_categorical_precision_ladder`
                  N=2 rung, Kashiwara f̃₁²), q-independent, and EVEN.

A generating-function "avatar" of the cosh/cos family is EVEN in u, so
its Taylor series has only even powers — the companion compute probe
`qbeta_cosh_avatar_crossanchor_multicoeff_probe.py` used this to refute
the entire even-parity slice (predicted c_3 = 0 ≠ cal-anchored ≈ −2.07).

The natural fix is an ODD-parity extension. Writing such an avatar as
`F(u) = A(u) · G(u)` with `A` the even baseline (`cos(√2·u)`, whose
truncation through u³ is `1 − u²`, giving c_2 = −1) and `G` the odd
extension, the lowest odd term `G` can contribute while preserving
`c_1 = 0` is u³: `G(u) = 1 + g·u³ + O(u⁴)`.

This file proves the algebraic consequence: **through order u³ the
product carries c_2 = −1 independently of g, and c_3 = g exactly.**
Hence an odd-parity closure of c_3 requires a closed-form g(q) matching
the cal-anchored c_3 target — which is exactly the (already saturated)
single-formula c_3 search. The generating-function reframing opens no
new c_3 search space.

These are the EXACT (truncated-polynomial) coefficients: `cos(√2·u)`
contributes nothing at u³ (it is even), so the through-u³ truncation
`1 − u²` of the baseline is faithful for c_2 and c_3. The baseline's
higher even terms (u⁴, …) affect c_4 and up, not c_2 / c_3, so they are
correctly outside the scope of this reduction.

Proof: one-line `ring` identities over any `CommRing`.

LaTeX label: `prop:qbeta-odd-parity-avatar-reduction`

## References
- Companion compute: `computations/qbeta/qbeta_odd_parity_avatar_reduction_probe.py`
- Even-parity refutation: `qbeta_cosh_avatar_crossanchor_multicoeff_probe.py` (PR #1866)
- Ladder N=2 rung (c_2 = −1): `prop:q-beta-categorical-precision-ladder`
- Generating-function hypothesis: `docs/audits/2026-06-04-ck-generating-function-derivation-chain-scope.md`
-/

namespace QOU.BraidKnot

/-- **Odd-parity avatar product (general even baseline).** The product
of an even baseline `1 + a₂·u²` (carrying the u² coefficient `a₂`, and
no u¹/u³ term — the through-u³ truncation of an even function) with the
minimal odd extension `1 + g·u³` expands exactly as

  `(1 + a₂u²)(1 + g u³) = 1 + a₂u² + g u³ + a₂ g u⁵`.

Reading coefficients: the u² coefficient is `a₂` (contains no `g`), and
the u³ coefficient is `g`. There is no u⁴ term; the only higher term is
`a₂ g u⁵`. -/
theorem qbeta_odd_parity_avatar_product {R : Type*} [CommRing R]
    (a2 g u : R) :
    (1 + a2 * u ^ 2) * (1 + g * u ^ 3)
      = 1 + a2 * u ^ 2 + g * u ^ 3 + a2 * g * u ^ 5 := by
  ring

/-- **The odd-parity content collapses to g·u³.** Subtracting the even
baseline `1 + a₂u²` and the residual `a₂ g u⁵` from the product leaves
exactly `g·u³`: the entire order-u³ (c_3) content is the single scalar
`g`, independent of the baseline coefficient `a₂`. -/
theorem qbeta_odd_parity_c3_content_eq_g {R : Type*} [CommRing R]
    (a2 g u : R) :
    (1 + a2 * u ^ 2) * (1 + g * u ^ 3) - (1 + a2 * u ^ 2) - a2 * g * u ^ 5
      = g * u ^ 3 := by
  ring

/-- **Reduction at the c_2 = −1 baseline.** With `a₂ = −1` (the
`cos(√2·u)` baseline truncated through u³), the avatar product is

  `(1 − u²)(1 + g u³) = 1 − u² + g u³ − g u⁵`,

so the u² coefficient is `−1` (independent of `g`, matching the proved
N=2 rung) and the u³ coefficient is exactly `g`. A non-fitted closure of
c_3 therefore demands a closed-form `g(q)` reproducing the cal-anchored
c_3 target — the saturated single-formula search. -/
theorem qbeta_odd_parity_avatar_reduction {R : Type*} [CommRing R]
    (g u : R) :
    (1 - u ^ 2) * (1 + g * u ^ 3)
      = 1 - u ^ 2 + g * u ^ 3 - g * u ^ 5 := by
  ring

/-- Subtracting the cubic scalar term from the stripped two-factor product yields zero. -/
theorem qbeta_odd_parity_c3_content_sub_g_eq_zero {R : Type*} [CommRing R]
    (a2 g u : R) :
    ((1 + a2 * u ^ 2) * (1 + g * u ^ 3) - (1 + a2 * u ^ 2) - a2 * g * u ^ 5)
      - g * u ^ 3 = 0 := by
  rw [qbeta_odd_parity_c3_content_eq_g, sub_self]

end QOU.BraidKnot
