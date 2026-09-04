# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-k5r5`: the ratio route is a constant-factor gain, not a rate gain — the exciting branch is excluded

**Date:** 2026-09-04 · **Branch:** `claude/m1-k5r5-delta-ratio-structure-2026-09-04` ·
**Tier:** measurement (negative) + correction of this probe's own verdict logic · **Epic:** `qou-x631`; gap `qou-k5r5`.

## The question, and why it had to be settled before the proof was attempted

PR #6576 established that the right target is a rigorous finite-`n` bound on `ρ_P` and on the ratio
`V_D/V_A` — 1.137× lossy, 40.5× headroom. It did not establish **why** the ratio is better behaved,
and that decides which of two very different projects the remaining work is:

- **Rate gain.** If `δ_D/δ_A → 1`, the two variances share their leading finite-`n` correction and it
  *cancels* in the ratio. Then `δ_R = δ_D − δ_A` is higher order, and a rigorous ratio bound could be
  far weaker than a variance bound and still close the gap. That would be a structural fact to
  formalize.
- **Constant gain.** If `δ_D/δ_A → r ≠ 1`, the corrections are proportional but not equal, so
  `δ_R ≈ (r−1)·δ_A`: the same rate, smaller by a constant. Then bounding the ratio is exactly as hard
  as bounding `δ_A`, and the ratio is bookkeeping applied at the end.

Formalize-first says settle which before starting either.

## Measured ([`…_delta_ratio_structure.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_delta_ratio_structure.py), exit 0, exact `Fraction` covariances over every partition to n = 46, NO float64)

| n | `δ_A` | `δ_D` | `ρ_δ = δ_D/δ_A` | `δ_R` (exact) |
|---|---|---|---|---|
| 8 | −0.171847 | −0.210396 | 1.2243 | −0.0465487 |
| 16 | −0.0553321 | −0.0687131 | 1.2418 | −0.0141648 |
| 24 | −0.0617528 | −0.0874126 | 1.4155 | −0.0273486 |
| 32 | −0.0323515 | −0.049502 | 1.5301 | −0.0177238 |
| 40 | −0.0368927 | −0.0583581 | 1.5818 | −0.0222876 |
| 46 | −0.0254454 | −0.0406663 | 1.5982 | −0.0156183 |

### Q1 — is `ρ_δ → 1`? **NO, decisively.**

Every tail value (`n ≥ 30`) is at least **0.4613** away from 1; the tail minimum is **1.46132**, and
nowhere in the table — not even at `n = 4` — does `ρ_δ` approach 1. **The rate-gain branch is
excluded.** This conclusion does not require the limit to be pinned.

### Q2 — what is `r`? **Unpinned.**

Tail range **[1.46132, 1.59818]**, relative spread **0.0895** — not settled to 5 %, and still
drifting upward across the window. Pinning it needs a wider exact table; Q1 does not.

### The rate comparison is inconclusive *by construction*, and the spreads say so

Local log-log exponents over `n ≥ 30`: `|δ_A|` mean 0.8236 with spread **4.667**; `|δ_R|` mean 0.1887
with spread **5.25**. The scatter is ~8× the difference of the means, so **the means are not rates and
must not be quoted as such**. This is the same oscillation that turned peak-ratio exponent fitting
into noise in PR #6500 — on these sequences the running-max envelope of PR #6576 is the tool that
works, and pointwise exponent fitting is not.

## What this changes

> **The remaining work is a rigorous finite-`n` bound on `δ_A` itself.** The ratio divides its
> constant by `|r − 1| ≈ 0.53`, i.e. **~1.89×**, and nothing more. Effort goes to `δ_A`; the ratio is
> applied at the end.

### Reconciling two gain figures that look contradictory and are not

PR #6576 measured the ratio route as worth **4.37×** over the three-ingredient budget. The gain over
bounding `δ_A` **alone** is only **~1.89×**. Both are correct and they measure different things: the
three-ingredient budget pays for `δ_A` *and* `δ_D` separately (0.113 + 0.163 = 0.276 in margin units)
while the ratio pays once (0.0537). **Most of the 4.37× is not the cancellation — it is not
double-paying.** Quote the two separately; conflating them would overstate what the cancellation is
worth by ~2.3×.

## Correction to this probe's own verdict logic

The first run printed **"UNANSWERED — a wider exact table is needed before either project is
chosen"**, on identical data.

The defect: the verdict tree gated everything on `settled` (spread < 5 %), so a tail that had not
pinned `r` reported that it had answered nothing — while its own numbers answered the dichotomy
decisively. **"Have I pinned `r`?" and "is `r` = 1?" are different claims**, and only the second
decides the project. `ρ_δ → 1` requires the tail to *approach* 1, so a tail whose minimum is 1.46
excludes it whatever the spread.

The fix reports the two questions separately and answers Q1 from the tail **minimum** rather than
from a midpoint-plus-spread test. Recorded because the cost of the original logic was a real result
suppressed by a threshold answering the wrong question — the same shape as the `da-arity-conflation`
class in [`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md):
a claim about a *family* tested as a claim about a *point*.

## Status of `qou-k5r5`

Gap **OPEN**. Requirement unchanged: `C ≤ m_∞√79 = 2.6681` at the proved `n^{-1/2}` shape, empirical
envelope 0.0580, `n ≤ 78` certified exhaustively (`b1-kappa-window-extension.witness.json`).

Newly known: the ratio route's advantage is arithmetic, not structural. The single open analytic
target is a **rigorous finite-`n` bound on `δ_A = (V_A/n² − 8/(9π²))·9π²/8`**, whose leading order is
already rigorous on the `V_D` side
([`…_VD_ceiling_rigorous.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_VD_ceiling_rigorous.py):
`V_D < 64/(75π²)` by certified interval arithmetic plus an explicit analytic tail majorant).

**Open and not claimed here:** whether the elementary closed forms
`Â_k = 8(−1)^{(k+1)/2}/(π(k²−4))` and `Ô_k = (8/π²)[1/k − 1/(2(k−2)) − 1/(2(k+2)) + 1/(2(k−2)²) −
1/(2(k+2)²)]` extend to a finite-`n` remainder with an explicit constant.

## Cross-references

- The route this refines: [`…-ratio-route-is-the-target.md`](2026-09-04-covariance-kernel-M1-k5r5-ratio-route-is-the-target.md) (#6576)
- The envelope tool that works on these sequences: `…_ingredient_envelope_convergence.py`
- Epic `qou-x631`; gap `qou-k5r5`.
