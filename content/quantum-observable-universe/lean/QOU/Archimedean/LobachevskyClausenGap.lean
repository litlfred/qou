import QOU.Archimedean.CatalanClausenBridge
import QOU.Archimedean.BorromeanVolumeCatalan

/-!
# QOU.Archimedean.LobachevskyClausenGap — the residual gap, with Catalan eliminated

`BorromeanVolumeCatalan.lobachevsky_pi_div_four_eq_half_catalan` is an `axiom`:

    Λ(π/4) = catalan_G / 2,   where  Λ(θ) := -∫₀^θ log|2 sin t| dt.

Its docstring used to attribute this to "Mathlib's full polylogarithm machinery
(Clausen function `Cl_2`, dilogarithm `Li_2`, ...) — none of which is currently
upstream". Two of those three are no longer the obstruction: `Cl_2` is defined
in-repo (`ClausenFunctionMathlibFiller`), and `CatalanClausenBridge` now proves
`catalan_G = Cl_2 (π/2)` outright, sorry-free.

`lobachevsky_catalan_iff_clausen` uses that to restate the axiom with **Catalan
gone entirely**:

    Λ(π/4) = catalan_G / 2   ↔   Λ(π/4) = Cl_2 (π/2) / 2

The right-hand form is the `θ = π/4` instance of the **Clausen integral
representation** `Λ(θ) = Cl_2 (2θ) / 2`, equivalently `Cl_2' θ = -log|2 sin(θ/2)|`.
That single analytic fact is now the *whole* residual obstruction: no Catalan, no
`Li_2`, no dilogarithm — one identity between a log-sine integral and a Fourier
series.

## Why it is still not closeable here — measured, not assumed

Probed against the pinned olean tree (401,418 constants visible; positive controls
pass). Three ingredients any proof of that identity needs, **none present**:

1. **The log-sine integral** `∫₀^{π/2} log(sin x) dx = -(π/2) log 2`. Mathlib has no
   `integral`-and-`log` lemma of this kind at all at this toolchain.
2. **Abel's limit theorem** / boundary behaviour of the log power series. Mathlib has
   `Real.hasSum_pow_div_log_of_abs_lt_one` — the series `∑ xⁿ/n = -log(1-x)` strictly
   *inside* the disc — and nothing carrying it to `|z| = 1, z ≠ 1`, which is exactly
   where `∑ cos(kθ)/k = -log|2 sin(θ/2)|` lives.
3. **Term-by-term integration of a conditionally-convergent Fourier series** against an
   integrand that is improper at the endpoint `t = 0`.

Both classical routes hit the same wall. The Fourier route needs (2) and (3). The
route via `∫₀^{π/4} log(cot t) dt = G` (substituting `u = tan t` and expanding
`1/(1+u²)` geometrically, which avoids the boundary) still needs (1) to convert
`∫ log sin` and `∫ log cos` into `Λ`.

So the axiom remains correctly classified **External** by
`docs/audits/2026-06-03-lean-axiom-tractability-triage.md`. What has changed is only
that the gap is now one named identity with three named missing prerequisites,
rather than "the polylogarithm machinery is absent".

**This file proves an equivalence, not the axiom.** It reduces what must be shown; it
does not show it. The axiom count is unchanged.
-/

open Real QOU.Archimedean

namespace QOU.Archimedean

/-- **The residual gap, with Catalan eliminated.**

`Λ(π/4) = catalan_G / 2` holds iff `Λ(π/4) = Cl_2 (π/2) / 2`, because
`catalan_G = Cl_2 (π/2)` (`CatalanClausenBridge.catalan_G_eq_Cl_2_pi_div_two`).

The right-hand side is the `θ = π/4` instance of the Clausen integral
representation `Λ(θ) = Cl_2 (2θ)/2`. Isolating it is the point: it names the one
analytic fact still missing, with no Catalan constant in the statement. -/
theorem lobachevsky_catalan_iff_clausen :
    (lobachevsky (Real.pi/4) = catalan_G / 2)
      ↔ (lobachevsky (Real.pi/4) = Cl_2 (Real.pi/2) / 2) := by
  rw [catalan_G_eq_Cl_2_pi_div_two]

end QOU.Archimedean
