# Low-isotope sign-flip diagnostic — interpretation + color-tube reading

**Date:** 2026-05-24
**Branch:** `claude/post-1089-followups-2026-05-24`
**Parent PR:** [#1089](https://github.com/litlfred/qou/pull/1089) (merged)
**Parent audit:** [`2026-05-24-low-isotope-mass-error-anatomy.md`](2026-05-24-low-isotope-mass-error-anatomy.md)
**Status:** Interpretation only — no production change. Identifies the load-bearing categorical question and points to the Bring color-tube weighted averaging as the likely closure mechanism.

## Diagnostic data (from [`low-isotope-sign-flip-diagnostic.witness.json`](../../computations/low-isotope-sign-flip-diagnostic.witness.json))

Per-isotope inter-nucleon channel count vs prediction error:

| Atom | A | pp | pn | nn | n_inter | err_pct |
|------|---|----|----|----|---------|---------|
| p    | 1 | 0  | 0  | 0  | 0       | +2.890% |
| n    | 1 | 0  | 0  | 0  | 0       | +2.890% |
| ²H   | 2 | 0  | 1  | 0  | 1       | +1.090% |
| ³H   | 3 | 0  | 1  | 1  | 2       | −0.156% |
| ³He  | 3 | 1  | 1  | 0  | 2       | −2.969% |

(⁴He is NOT in the current low-iso witness — see "⁴He scope caveat" below.)

### Linear fits

| Predictor | slope | intercept | R² |
|-----------|-------|-----------|----|
| n_inter (channel count) | **−2.226 % / arc** | +2.975 % | **0.829** |
| signed_h_weight (Hecke d-coefficient sum) | +9.711 % / unit | +1.764 % | 0.258 |

**Reading:** the per-isotope error tracks the **count** of inter-nucleon arcs almost linearly, NOT their signed Hecke weights. Each inter-nucleon arc shifts the prediction by ≈ −2.23% regardless of whether the channel is pp / pn / nn.

The fit intercept (+2.975%) closely matches the bare-nucleon (p, n) over-prediction (+2.89%) — confirming the baryon-class uniform VolDensity(𝓑₃) gap is the **starting point** and the per-isotope correction enters at the inter-nucleon layer.

## ⁴He scope caveat

The diagnostic ran on the **current 5-atom** `low-isotope-mass-table.witness.json` (p, n, ²H, ³H, ³He). ⁴He's prediction was present in the 8-atom version (PR #1089 commit) but the current main-side witness was regenerated with restricted scope. Re-running with ⁴He included would test whether ⁴He's +5.87% over-prediction (3 inter-nucleon arcs) breaks the linear trend — which it does substantially: the linear fit predicts `+2.97 − 3·2.23 = −3.71%` for ⁴He, but the measured value is +5.87% (delta ≈ +9.6%). **⁴He is the outlier** — likely the magic A·8G shell closure introduces a discontinuous shift.

See [`2026-05-24-4he-magic-shell-color-tube-audit.md`](2026-05-24-4he-magic-shell-color-tube-audit.md) for the ⁴He-specific analysis.

## The categorical reading — Bring color-tube weighted averaging

The current production rule (per [`isotope_record_schema.py:176-178`](../../computations/isotope_record_schema.py)) assigns inter-nucleon Hecke generators by **flavor only**:

| Channel | Hecke generator | d-coefficient |
|---------|-----------------|---------------|
| pp | σ              | 0             |
| nn | σ⁻¹            | −h            |
| pn | σ_avg          | −h/2          |

These are flavor-uniform: every pp arc uses bare σ regardless of which proton-color-state pair sits at that crossing.

The cheat-sheet ([`docs/canonical-derivation-cheat-sheet.md` §"Bring color-tube weighted averaging — open audit finding (Phase 5q)"](../canonical-derivation-cheat-sheet.md)) records the owner's intuition that the canonical assignment should be **color-weighted**: each nucleon carries 3 quark color sheets (`(μ_u, μ_u, μ_d)` for proton uud, `(μ_u, μ_d, μ_d)` for neutron udd), and each inter-nucleon arc averages over **9 color-pair assignments** (3 × 3) weighted by quark content.

Under color-weighting:

| Channel | Color-pair structure | Refined effective d-coefficient |
|---------|---------------------|-------------------------------|
| pp (uud × uud) | 4 same-color, 5 different | **closer to 0** but not exactly 0 |
| nn (udd × udd) | 4 same-color, 5 different | **closer to −h** but shifted by color-mix |
| pn (uud × udd) | 3 same-color, 6 different | **closer to −h/2** but shifted by quark-content |

The current uniform-averaging convention is a **flavor-only projection** of the color-weighted form — it loses the color-content distinction that empirically explains Δm_{n−p} to 0.14% (per [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py) Scheme 4 finding referenced in the cheat-sheet).

**Hypothesis:** the +2.23%/arc linear shift in the diagnostic above reflects a uniform-projection bias that color-weighting would resolve. Each color-pair contributes a different effective h-weight; the uniform σ_avg averages them but loses the per-pair structure. If the color-weighted form gives ANY per-channel weight refinement, the per-isotope corrections would no longer be uniform per arc.

## Falsification of the PR [#1063](https://github.com/litlfred/qou/pull/1063) framing for A ≥ 3

The "single-knot `VolDensity(𝓑₃)` categorical-exactness refinement" framing predicts every isotope overshoots by the same uniform fraction. The diagnostic data (R² = 0.83 on n_inter) directly falsifies that for A ≥ 3 — the per-arc residual structure is dominant.

The PR [#1063](https://github.com/litlfred/qou/pull/1063) framing **is** valid for the p/n baseline (+2.89% uniform) and for the linear-fit intercept (+2.975% ≈ +2.89%); the framing **does not** capture the per-arc layer.

## Three-substrate attribution

| Substrate | Where it enters | Sign-flip contribution |
|-----------|----------------|------------------------|
| Algebraic (Hecke / Wedderburn / Family A) | linking weight `(3q²+4+3q⁻²)/4` | baseline +2.89% (uniform across isotopes) |
| Geometric (Bring's surface / color tubes) | per-arc Hecke generator assignment via color-pair averaging | per-arc −2.23% residual + ⁴He magic-shell outlier |
| Archimedean (m_e, q_0) | CAL-1 anchor + q_0 substrate | no per-isotope contribution |

The diagnostic localises the closure work to the **geometric** substrate — specifically the color-tube structure on Bring's surface.

## Recommended next actions

1. **Author `prop:inter-nucleon-channel-from-color-tube`** (conditional on the S₅ ↔ SO(3) fiber action class from PR [#1081](https://github.com/litlfred/qou/pull/1081) Task 3) — done as `inter-nucleon-channel-color-tube.{md,ts}` on this branch.
2. **Wire `probe_pn_flavor_asymmetry.py` Scheme 4 into the canonical pipeline** — currently a probe; promotion needs the prop block from (1) + Lean class skeleton.
3. **Re-run sign-flip diagnostic with color-tube-weighted predictions** — compare R² of color-weighted vs uniform; if color-weighted R² > 0.95, the closure is essentially complete.
4. **⁴He magic-shell audit** — [`2026-05-24-4he-magic-shell-color-tube-audit.md`](2026-05-24-4he-magic-shell-color-tube-audit.md) — does the A·8G shell saturate a color-tube count (5 × 8G = 40, 9 × 8G = 72)?

## Cross-references

- Parent audit: [`2026-05-24-low-isotope-mass-error-anatomy.md`](2026-05-24-low-isotope-mass-error-anatomy.md)
- Coordination ledger: [`docs/coordination/2026-05-24-low-isotope-mass-anatomy-ledger.md`](../coordination/2026-05-24-low-isotope-mass-anatomy-ledger.md)
- Sign-flip diagnostic script: [`low_isotope_sign_flip_diagnostic.py`](../../computations/low_isotope_sign_flip_diagnostic.py)
- Color-tube infrastructure: `content/quantum-observable-universe/archimedean-universe/color-tube-*.md` (existing)
- Color-tube weighting open finding: [`docs/canonical-derivation-cheat-sheet.md` §"Bring color-tube weighted averaging"](../canonical-derivation-cheat-sheet.md)
- PR [#1063](https://github.com/litlfred/qou/pull/1063) — Family A gap audit (single-VolDensity refinement framing falsified for A ≥ 3 by this diagnostic)
- PR [#1081](https://github.com/litlfred/qou/pull/1081) — Task 3 S₅ ↔ SO(3) fiber action (supplier for the categorical class)
