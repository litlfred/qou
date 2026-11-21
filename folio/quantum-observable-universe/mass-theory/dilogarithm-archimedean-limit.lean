import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic
import QOU.Archimedean.DilogarithmArchimedeanLimit


/-!
# Archimedean limit of Φ_n(x; q): conjecture statement

The conjecture: under the joint Faddeev scaling q → 1, n → ∞,
n(1-q) → ∞, the rescaled logarithm (1-q) · log Φ_n(x; q) converges
to the classical dilogarithm Li₂(x).

This file provides:
* a concrete Mathlib-backed definition of `LiTwo : ℝ → ℝ` as the
  series Σ_{k≥1} x^k / k², replacing the previous `opaque`
  placeholder. The series converges absolutely on the closed unit
  disc, divergently outside it; at `|x| ≤ 1` the value coincides
  with the principal-branch real dilogarithm.
* unconditional boundary lemmas (`LiTwo_zero`, `partialProduct_zero`)
  that anchor the conjecture's class instances at the only points
  where the Faddeev limit is trivial.
* the conjecture, packaged as the typeclass `ArchimedeanLimit`, with
  one field stating the convergence of `(1-q) log Φ_n(x;q)` to
  `LiTwo x` along Faddeev's joint scaling. The class is the §3b-cond
  hook used by `prop:archimedean-functor-uniqueness`.

Difficulty split (see audit
`docs/audits/2026-06-07-dilog-archimedean-limit-part-A-elementary.md`):
* **Part A** — fixed `x ∈ (0,1)`, convergence side `q → 1⁻` — is
  mathematically ELEMENTARY (a monotone left-Riemann-sum limit, an
  exponential tail bound, and the factor `(1-q)/ℏ → 1`; no Tauberian
  theorem, no branch cut, since `1 - x q^k ≥ 1 - x > 0`). The identity
  `Li₂(x) = ∫₀ˣ -log(1-t)/t` — the integral-representation bottleneck
  noted in the 2026-05-30 / 2026-06-07 closure audits — is now **proved
  sorry-free** as `QOU.Archimedean.DilogReflection.LiTwo_eq_integral`
  (FTC on the dilogarithm derivative `hasDerivAt_LiTwo`, which Mathlib
  lacked; built 2026-07-19). A sorry-free Lean proof of Part A is now
  gated only on the remaining Mathlib Riemann-sum-to-integral convergence
  of `(1-q) log Φ_n → ∫`.
* **Part B** — the substrate continuation `q → 1⁺` (to `q₀ ≈ 1.11`) and
  uniformity as `x → 1⁻` — is the genuine open content: there the factors
  `1 - x q^k` change sign (the poles of `Φ_n` approach the `Li₂` branch
  cut) and the Frobenius-pairing pole cancellation must do real work.

The class formulation isolates these gaps; the unconditional `x = 0`
instance below is the boundary anchor.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] Faddeev, "Current-like variables in massive and massless integrable models," Lectures 1994
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
-/

namespace QOU.QPochhammer

/-! The concrete primitives `denomPolyLocal`, `partialProductLocal`,
    `LiTwo`, the boundary lemmas `LiTwo_zero`, `denomPoly_zero`,
    `partialProduct_zero`, `faddeev_limit_at_zero`, **and** the open
    conjecture class `ArchimedeanLimit`, its stated form
    `partialProduct_to_LiTwo`, and the unconditional boundary instance
    `archimedeanLimit_zero` now all live in the importable lib module
    `QOU.Archimedean.DilogarithmArchimedeanLimit` (imported above) —
    their single source of truth — so downstream content blocks
    (e.g. `cl2-pentagon-and-faddeev-partial`,
    `phi-q-wkb-greens-function`, whose `WKBGreensFunction` class
    `extends ArchimedeanLimit`) can reuse them across content-sibling
    boundaries.  The class and instance were promoted to the lib module
    2026-06-29; this content sibling re-exports them via the import. -/

end QOU.QPochhammer
