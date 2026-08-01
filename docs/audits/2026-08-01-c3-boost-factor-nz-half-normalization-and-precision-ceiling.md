# c₃ boost factor `c = √A ≈ 1.4305`: the NZ-½ structural identity + the precision ceiling — REDUCED (scope-a)

**Date:** 2026-08-01 · **Axis:** Q_β c₃ bar-odd `S` — the sole surviving open target
(`qou-iyj5` / PR #4515). **Branch:** `claude/derive-c-sqrtA-boost-factor-2026-08-01`.
**Tier:** structural (Lean-exact identity) + measurement (scope-(a) precision prune).
**No `c_k` wired; nothing inverts `Q_β`/CODATA; registry untouched; no
`SDeformedVolumeChannel` instance fabricated; no tier change.**

- **Lean:** [`QOU/QBeta/BoostFactorNZNormalization.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BoostFactorNZNormalization.lean) (`lean`-direct exit 0, sorry-free).
- **Probe:** [`qbeta_c3_boost_factor_normalization_probe.py`](../../computations/qbeta/qbeta_c3_boost_factor_normalization_probe.py) → witness `qbeta-c3-boost-factor-normalization.witness.json` (3/3).
- **Sibling (coordinated):** PR #4515 (`qou-iyj5`) — the exact-CS-integral numerics that
  first isolated `c = √A ≈ 1.4305`.

## The target (from the sibling)

PR #4515 established, with the **exact** figure-8 complex volume, that the muon bar-odd
leak `S(muon) ≈ 0.009683` needs an effective boost `Re u = c·ln q₀` with

$$
c = \sqrt{A} \approx 1.4305,\qquad A = \frac{S(\text{muon})}{\kappa_{\mathrm{pot}}\,(\ln q_0)^2}\approx 2.054,
$$

because `Im 𝔙₄₁(u) = κ_pot·(Re²u − Im²u)` with the **Lean-exact potential coefficient**
`κ_pot = √3/4` ([`FigureEightComplexVolume.cuspModulus`](../../content/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean))
and the meridian boost `Re u = ln q₀` gives only `A = 1`. The spin part `Im u ≠ 0` only
*decreases* `Im 𝔙₄₁` (that is this session's "leading bound" `Im 𝔙₄₁ ≤ κ_pot(Re u)²`), so
the gap is unambiguously a `Re u` boost-rapidity enhancement — a single `O(1)` factor `c`.
The sibling's addendum already noted `A = 2` (`c = √2`) sits `2.27 %` off, a q₀-shift of
`5.7×10⁻¹¹` — below the pin. **This note brings two things that sibling context did not.**

## Contribution 1 — the clean value `A = 2` is EXACTLY the Neumann–Zagier ½ normalization

`A = 2` is not ad hoc. The figure-8 cusp **shape** and the NZ complex-volume **potential**
coefficient differ by exactly the NZ ½:

$$
\kappa_{\mathrm{shape}} = \tfrac{\sqrt3}{2} = \sin\tfrac{\pi}{3} = \operatorname{Im} e^{i\pi/3},
\qquad
\kappa_{\mathrm{pot}} = \tfrac{\sqrt3}{4} = \tfrac12\,\kappa_{\mathrm{shape}},
\qquad
\boxed{\ \frac{\kappa_{\mathrm{shape}}}{\kappa_{\mathrm{pot}}} = 2\ \ (\text{exactly})\ }
$$

— the `1/2` being "the NZ potential normalisation" named verbatim in the
`FigureEightComplexVolume.lean` docstring, and appearing as the `½∫` in the sibling's exact
CS integral `Im 𝔙₄₁ = ½∫₀^u arg(−L) du'`. Because `Im 𝔙` is **quadratic** in `Re u`, an
observable that carries the cusp-**shape** quadratic form `κ_shape·(Re u)²` rather than the
NZ **potential** form `κ_pot·(Re u)²` has

$$
A_{\text{shape}} = \frac{\kappa_{\mathrm{shape}}}{\kappa_{\mathrm{pot}}} = 2\ \text{(exact)},
\qquad c = \sqrt{A_{\text{shape}}} = \sqrt 2,
$$

with **no free parameter**. The whole "why `c = √A`?" question therefore **reduces** to one
named, binary, falsifiable normalization question:

> **Does the bar-odd observable `S` carry the NZ ½ potential normalization (`κ_pot`, giving
> the naive `A=1`) or the raw cusp-shape quadratic form (`κ_shape`, giving `A=2`, `c=√2`)?**

This is Lean-exact (`kappa_shape_eq_two_mul_pot`, `boost_factor_sq_two_of_shape`,
`cuspShape_eq_sin_pi_div_three`, all sorry-free over `ℝ`). It converts an opaque `O(1)`
number `1.4305` into a specific CS-convention question with a clean answer `c = √2`.

## Contribution 2 — the precision ceiling: `c = √A` cannot be *identified*, only reduced

`S(muon)` is a `1/u³`-amplified near-threshold quantity (registry `dc₃/dq₀ ≈ 4.6×10⁶`).
Measuring `dA/dq₀` directly by finite difference:

| quantity | value |
|---|---|
| `dA/dq₀` (finite diff) | `≈ 8.14×10⁸` |
| q₀-pin (ppb) → `σ_A` | `≈ 0.81` (**39.6 % of A**) |
| → `σ_c` | `≈ 0.28` (**19.8 % of c**) |
| Δq₀ mapping `A_meas → 2` exactly | `6.63×10⁻¹¹` (**below the pin**) |
| clean-candidate spread (max miss) | `≤ 2.63 %` (`≪ σ_A`) |

The clean structural candidates all sit inside the amplification band:

| candidate `A` | `A` | `c = √A` | miss vs measured |
|---|---|---|---|
| **`A = 2` (NZ ½: `κ_shape/κ_pot`; `c = √2`)** | `2.0` | `1.41421` | `−2.63 %` |
| `A = q₀+q₀⁻¹` (barEven `q₀`) | `2.0109` | `1.41806` | `−2.10 %` |
| `A = Vol(4₁) = 2·Cl₂(π/3)` | `2.02988` | `1.42474` | `−1.17 %` |
| `A = q₀²+q₀⁻²` (barEven `q₀²`) | `2.04371` | `1.42958` | `−0.50 %` |
| `A = 2.054` (measured) | `2.054` | `1.43318` | `0` |

Because `σ_A ≈ 40 % ≫` the `≤ 2.63 %` spread, **the measurement cannot select among these
candidates.** Any claim that `c = 1.4305` matches a particular constant to 3–4 sig figs is
numerology, not a derivation — the PR #1805 entropy/precision pattern applied to the boost
factor. This is the forward formalize-first prune: the identification search is
under-determined and must not be run as a high-precision constant hunt.

## Verdict — REDUCED (not derived, not refuted)

- **Not derived.** We do **not** assert that `S` carries `κ_shape` — doing so to force
  `A = 2` would be a fit (the anti-laundering line). `A = 2` (`c = √2`) is the *cleanest
  candidate*, exactly `= 1/(NZ ½)`, and consistent with the amplified readout `2.054` to
  within the intrinsic uncertainty.
- **Not refuted.** The meridian-deformation / complex-volume route is not excluded; this is
  scope-(a) (per AGENTS.md §"Before declaring refuted"): it constrains the *value* and its
  *identifiability*, not the *ingredient*.
- **The reduction is the progress.** `c = √A ≈ 1.4305` → the single binary question
  "*does the bar-odd leak drop the NZ ½ potential normalization?*", whose clean answer is
  `A = 2`, `c = √2`. That is a named, falsifiable CS-normalization sub-obstruction —
  tractable, unlike an opaque `O(1)` factor — and the honest open content (bean `qou-yh67`).

## Anti-laundering

No `c_k` value produced or wired; `S(muon)` is *measured* against the structural factor,
never fitted to it; nothing inverts `Q_β`/CODATA; no `SDeformedVolumeChannel` instance is
fabricated; `c₃` stays a q₀-dependent near-match (SETTLED #1580). Base ring: the identity
file is genuinely archimedean (`Real.sqrt`, `Real.sin`) — §7c-correct `ℝ`.

## Coordination

Posted intent on PR #4515 (`qou-iyj5`) naming this parallel route and its distinct angle
(structural NZ-½ identity + precision-ceiling prune vs the exact-CS-integral numerics), per
the measured-overlap rule. Converges with the sibling's own `A=2`-vs-`2.054` addendum: this
note supplies the *reason* `A=2` is clean (`= 1/(NZ ½)`) and the *quantitative* ceiling that
makes the residual `0.054` amplification noise rather than open physics.

## Cross-references

- [`2026-08-01-c3-exact-volume-boost-rapidity-enhancement.md`](2026-08-01-c3-exact-volume-boost-rapidity-enhancement.md) (#4515) — the exact-CS-integral origin of `c=√A`.
- [`2026-08-01-fibre-to-observable-bridge-verdict.md`](2026-08-01-fibre-to-observable-bridge-verdict.md) — c₃-odd home is the complex volume; the anchor-dependent value is a CAL-2 (Subgoal-2) input.
- [`2026-07-25-meridian-holonomy-c3-anchor.md`](2026-07-25-meridian-holonomy-c3-anchor.md) — the boost hyperbola `barEven²−barOdd²=4`; magnitude channel anchor-smooth.
- [`FigureEightComplexVolume.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean) — `κ_pot = √3/4`, the NZ ½; `Im 𝔙₄₁ = κ(Re²−Im²)`.
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).

-- Ref: [manuscript] docs/coordination/1ppq-qbeta.md
