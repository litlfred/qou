import QOU.QBeta.BarOddLadderShape

/-!
# One-instanton normalization: the geometric realization of the bar-odd ladder

`BarOddLadderShape` (the c₃ bar-odd `S = A/u³` kit) records that its **geometric
instance** — realizing the numerator `A` as `Im 𝔙_q` of a categorical meridian
assignment — is the single named open problem (`conj:algebraic-geometric-dilog-equivalence`).
A literature pass on the fibre-Stokes → archimedean map (Écalle bridge equation;
Garoufalidis–Gu–Mariño resurgence of complex Chern–Simons) identifies the shape that
realization must take: the **one-instanton imaginary part** of the median-resummed
knot state integral,

  `A(q) = Im 𝔙_q(q) = 𝒜_K · e^{ − Re 𝔙_K(q)/(π ℏ_q(q)) } · sin(Im 𝔙_K(q)/(π ℏ_q(q)))`
        ≕ `M(q) · Z(q)`,

with `𝒜_K` the **integer** (`b = 0` weight branch, `GZWeightSelection`/`GZWeightGeneral`)
Stokes amplitude, `M` the smooth nonzero amplitude
`𝒜_K·e^{−Re𝔙/πℏ}·(subexponential prefactor)`, and `Z` the **Im-phase factor** whose
simple zero at `q*` is the substrate point where `𝔙_K` becomes **real**
(`Im 𝔙 = 0`) — an amphichiral-type locus, matching `A(q*) = 0` *geometrically* rather
than by construction.

**The structural payoff (this file).** The committed exactness
`BarOddLadderShape.hasDerivAt_S_at_qstar` — the `S`-slope at `q*` has **zero
log-derivative correction** — is *not* an extra assumption the one-instanton form must
satisfy: it is an automatic **consequence** of the product shape `A = M·Z` at a simple
zero of `Z`. The product rule gives `A′(q*) = M′(q*)·Z(q*) + M(q*)·Z′(q*)`, and
`Z(q*) = 0` kills the first term, so `A′(q*) = M(q*)·Z′(q*)` — the amplitude times the
phase-slope, with **no** `M′/M` (log-derivative of the exponential amplitude) term.
That is exactly the log-derivative-free static slope the ladder kit proves. So the
one-instanton normalization map is **structurally consistent** with the committed
`N_odd` shape, and the capstone reduces to a **magnitude identification**:
`M(q*)·Z′(q*) = A′ ≈ +2.37`.

**Honesty / scope (STRICT — conditional-proved ≠ premise-established).** This file
proves the *implication* "one-instanton structure ⇒ `BarOddLadderShape` numerator",
**not** that the actual geometric `𝔙_q` has this structure. The identification of
`M, Z` with the real `Im 𝔙_q(q₀)` data — and the magnitude match to the measured
`A′ ≈ +2.37` — remains the open capstone
(`conj:algebraic-geometric-dilog-equivalence`). Nothing is wired; no instance for the
actual `𝔙_q` is exhibited. Distinct from the refuted `β = 3/2` (a type error on the
*trivial-connection* weight): here the amplitude is the integer `b = 0` datum and the
anchor-dependence lives in the exponent. Verified `lean`-direct (exit 0), sorry-free.

-- Ref: [garoufalidis-gu-marino2021] https://doi.org/10.1007/s00220-021-04076-0 (Stokes = rotated 3d-index; discontinuity)
-- Ref: [leitner2026] docs/audits/2026-07-25-aomega-normalization-one-instanton-map.md
-/

namespace QOU.QBeta.OneInstantonNormalization

open QOU.QBeta

/-- **The one-instanton numerator slope is log-derivative-free at the simple zero.**
For `A = M·Z` with `M` differentiable and `Z` vanishing at `q*`, the derivative at
`q*` is `M(q*)·Z′(q*)` — the `M′·Z` term is killed by `Z(q*) = 0`. This is the
product-rule content behind `BarOddLadderShape.hasDerivAt_S_at_qstar`'s "zero
log-derivative correction": the smooth exponential amplitude `M`'s own slope drops out
at the zero. -/
theorem numerator_hasDerivAt_at_zero {M Z : ℝ → ℝ} {qstar M' Z' : ℝ}
    (hM : HasDerivAt M M' qstar) (hZ : HasDerivAt Z Z' qstar) (hZ0 : Z qstar = 0) :
    HasDerivAt (fun q => M q * Z q) (M qstar * Z') qstar := by
  have h := hM.mul hZ
  rwa [hZ0, mul_zero, zero_add] at h

/-- **The one-instanton Im form realizes a `BarOddLadderShape`.** Given the
one-instanton structure — a differentiable amplitude `M` (the smooth
`𝒜_K·e^{−Re𝔙/πℏ}·prefactor`), an Im-phase factor `Z` with a simple zero at `q*`
(`Z(q*) = 0`, slope `Z′`), a positive combined numerator slope `M(q*)·Z′ > 0`, and the
positive ladder lever `u` — the categorical meridian numerator `A = M·Z` and its lever
`S = A/u³` inhabit `BarOddLadderShape` with `A′ = M(q*)·Z′`. This is the geometric
realization `BarOddLadderShape` names as open, *conditional on* the one-instanton
structure holding for the actual `𝔙_q` (not proved here). -/
theorem barOddLadderShape_of_oneInstanton
    {M Z u : ℝ → ℝ} {qstar M' Z' : ℝ}
    (hM : HasDerivAt M M' qstar) (hZ : HasDerivAt Z Z' qstar) (hZ0 : Z qstar = 0)
    (hslope : 0 < M qstar * Z') (hu : ∀ q, 0 < u q) :
    BarOddLadderShape (fun q => M q * Z q / u q ^ 3) (fun q => M q * Z q) u qstar
      (M qstar * Z') where
  ladder := fun _ => rfl
  u_pos := hu
  zero_at_qstar := by simp [hZ0]
  deriv_at_qstar := numerator_hasDerivAt_at_zero hM hZ hZ0
  slope_pos := hslope

/-- **Consequence: the geometric `S`-slope at `q*` is `M(q*)·Z′ / u(q*)³`, exact.**
Chaining the realization into `BarOddLadderShape.hasDerivAt_S_at_qstar`: the
one-instanton lever slope at `q*` is the pure static lever with the amplitude
log-derivative dropping out — the committed exactness, now with the numerator slope
given geometrically as amplitude × phase-slope. The open magnitude check is
`M(q*)·Z′ = A′ ≈ +2.37`. -/
theorem hasDerivAt_S_at_qstar_oneInstanton
    {M Z u : ℝ → ℝ} {qstar M' Z' u' : ℝ}
    (hM : HasDerivAt M M' qstar) (hZ : HasDerivAt Z Z' qstar) (hZ0 : Z qstar = 0)
    (hslope : 0 < M qstar * Z') (hu : ∀ q, 0 < u q) (hu' : HasDerivAt u u' qstar) :
    HasDerivAt (fun q => M q * Z q / u q ^ 3) (M qstar * Z' / u qstar ^ 3) qstar := by
  have hinst : BarOddLadderShape (fun q => M q * Z q / u q ^ 3) (fun q => M q * Z q) u
      qstar (M qstar * Z') := barOddLadderShape_of_oneInstanton hM hZ hZ0 hslope hu
  exact hinst.hasDerivAt_S_at_qstar hu'

end QOU.QBeta.OneInstantonNormalization
