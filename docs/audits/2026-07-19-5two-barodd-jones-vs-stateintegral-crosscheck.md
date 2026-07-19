# 5₂ bar-odd cross-check: the algebraic (Jones) and analytic (state-integral) faces carry DISTINCT normalizations — kill-criterion (b)

**Date:** 2026-07-19 · **Branch:** `claude/agent-pickup-stalled-rtugin` ·
**Axis:** G3 / c₃ bar-odd fibre datum · **Tier:** bounded cross-check with
pre-stated kill-criteria, scope-(a) · **Discipline:** no fit, nothing inverted
from `S`, nothing wired; fibre-vs-fibre only (does not cross the G3 wall).
**Probe:** [`computations/probes/qbeta_5two_jones_vs_stateintegral_barodd_crosscheck_probe.py`](../../computations/probes/qbeta_5two_jones_vs_stateintegral_barodd_crosscheck_probe.py)
· **Witness:** `qbeta-5two-jones-vs-stateintegral-barodd-crosscheck.witness.json` (2/2).

## The question (scout G3 step #2)

There are two 5₂ bar-odd faces at the substrate `q₀`:

- **Algebraic (Jones):** `bar-odd(J_{5₂})(q₀) ≈ 0.0209909` — the framing-invariant
  0-framing knot-invariant bar-odd built in PR #4099, prefactor-free by
  construction.
- **Analytic (state integral):** `Im(𝔏_odd) ≈ 2.2721850` — the intrinsic bar-odd
  *phase*, the imaginary part of the Theorem-22 state-integral log-split
  `𝔏_odd = (log Z_{5₂}(q) − log Z_{5₂}(q⁻¹))/2 ≈ 34.432 + 2.272i` after the
  classical exponential (`Re 𝔏_odd = 34.43`, the volume asymmetry) is stripped —
  the very step `qbeta_g3_5two_barodd_substrate.py` flagged as open.

Is the framing-invariant Jones bar-odd the intrinsic datum the state-integral
route could not cleanly extract, up to a **derived** normalization?

## Kill-criteria (stated before the run) and outcome

`Im(𝔏_odd) / bar-odd(J)(q₀) = 108.246`. Tested against a fixed pre-stated basis
of derived normalizations `{1, 2π, π², [3]_q, Vol(5₂), [3]_q!, 2π[3]_q, π²[3]_q,
2π², 4π}`; the nearest is `π²·[3]_q ≈ 32.98`, off by **228 %** — nothing within the
1 % state-integral drift floor.

**Verdict: (b) DISTINCT normalizations.** The two 5₂ faces are **not** related by a
trivial/pre-stated derived factor. The algebraic (framing-invariant) face and the
analytic (prefactor-stripped phase) face are genuinely different-normalization
objects; the bridge between them is the **open §4e quantum-modularity
identification** (algebraic ζ_N face + analytic q₀ face agreeing forces the Stokes
`A_ω`), not a direct substitution.

## What this means for G3

The result **sharpens the argument→S attack**: one cannot simply substitute the
new Jones `𝔙_q(5₂)` bar-odd into the state-integral machinery as the intrinsic
datum — the normalization connecting the two faces is exactly the open
quantum-modularity content. So the honest G3 path keeps both faces and closes the
bridge (§4e / the pentagon-rigidity lane), rather than treating the algebraic
datum as a shortcut. Consistent with the measurement-limited value leg
(`no_anchor_invariant_realizes_swing`) and the open `Im 𝔙_q → N_odd` normalization
capstone — neither is touched here.

This is a scope-(a) negative on a *specific trivial-normalization hypothesis*, not
a structural exclusion: it says the two faces differ by more than a pre-stated
derived factor, leaving the derived-bridge (§4e) as the open, correct route.
