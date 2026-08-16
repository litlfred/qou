---
# qou-cwin
title: 'MIGRATION: express the Q_beta c_k ladder in h = q - 1/q instead of u = b*hbar_q^2'
status: in-progress
type: task
priority: high
created_at: 2026-08-16T12:45:00Z
updated_at: 2026-08-16T12:45:00Z
---

Owner-authorised 2026-08-16: *"bean up and start = express the ladder in h"*.
Parent: `qou-cds1` (S1 of the convention ruling). Evidence for the decision is
on PR #5210.

## Why (the reasons that survived measurement)

- **Analyticity.** `u ~ h^2`, so reverting `u -> h` needs `sqrt(u)` and the
  ladder is non-analytic at `u = 0` (corpus:
  `qbeta_ck_from_operator_markov_trace_probe`). In `h` the same function is a
  genuine power series: measured, `cos(alpha - u/2) = 1 + 0*s - s^2/8 +
  ((1-sqrt3)/8)s^3 + ...` with `s = q-1`, integer powers throughout.
- **Expressiveness.** Odd-order content is half-integer in `u` and therefore
  structurally unrepresentable there. In `h` it is an ordinary rung. Note
  `s^1 = 0` exactly, so the h-frame has no linear rung -- the `u^1` rung
  (`a_1 = -sqrt(3)/12`) is an artifact of expanding in a squared variable.
- **Literature alignment.** The Ohtsuki series is a power series in `q - 1`
  with integral coefficients (Lawrence conj., Rozansky proof); the Habiro ring
  is described as analytic functions at roots of unity.
- **Channel consistency.** alpha_EM's Habiro element is ALREADY written in h:
  `[2]_q * (1 - h^2 * a)`. Q_beta is the odd channel out.

## Why NOT (measured, and it must not be over-sold)

**The reframe does not fix anchor-instability.** Tested at matched
magnification (`h^k` chosen so `h^k ~ u^3`) in
`qbeta_h_vs_u_frame_stability_probe`:

    frame       proton         muon      rel swing
      u^3    -2.069343    -2.020200      2.3748%
      h^9    -1.676039    -1.636236      2.3748%
    residual R                           2.3747%

Identical to five significant figures; the variables' own swings are ~1e-6.
The instability is in the RESIDUAL, not the coordinate. This refuted a
hypothesis I had put in writing (that half-integer leakage drives the drift) --
scope-(a), as the explanation of THIS drift at THESE anchors.

**Cost: ~3x the rungs** for equal precision (7.2 -> 22.1 for 1e-15). It is
3.045x rather than 2x because `u = 0.195 h^2`, and that prefactor costs about
as much as an extra power at these magnitudes.

So this migration is **hygiene and expressiveness, not a fix.** Do not
describe it as one in any PR, witness, or content block.

## Blast radius

Every `c_k`-derived statement is u-frame and becomes a different number:
`c_2`, `c_3`, `c_4...`, `S_leak = c_3 + Vol(4_1)`, `q*_S`,
`c_3^even = -Vol(4_1)`, `[3]_q/25`, `J - hbar^2`. Plus AGENTS.md's truncation
rule `N >= log10(1/eps)/2.07 - 1`, whose `2.07` is `-log10(u)`.

## Ordered plan

**T0 (FIRST, before any number moves) -- make the frame DECLARABLE.**
Add a `ladder_frame: "u" | "h"` field to every c_k-bearing witness and require
it. This is the lesson from the convention C->D campaign, learned the hard
way: PR #5210's own `--impact-vs-main` had to report *"0 of 12 declare
`markov_convention`, so the count is a lower bound."* A migration whose
artifacts do not declare their frame cannot be measured, only guessed at. Do
NOT skip this step to get to the interesting part.

**T1** -- extract the h-frame rungs at both anchors; establish the h-ladder as
a computed object with a witness, alongside (not replacing) the u-ladder.

**T2** -- registry: record the frame on every c_k row; pair with `qou-f09n`'s
`c_2` / `\tilde c_2` naming so a reader can tell which coefficient in which
frame.

**T3** -- re-derive the truncation-order rule in h and correct AGENTS.md
line 1062. Owner sign-off required (STRICT banner, contested channel).

**T4** -- downstream content blocks. NOT started without owner sign-off:
changes published statements.

## Discipline

The anti-fit rules are unchanged. A rung obtained by matching a target is a
fit regardless of which variable it is written in. `alpha` remains un-derived
in both frames and this migration does not change that.

---

## T0.5 VERIFIED (2026-08-16) — and it re-scopes this migration substantially

#5187's claim was flagged by the coordination sweep as "worth reconciling
before T1". Checked. **It is confirmed, and it is stronger than stated.**

### `c_4..c_7` are not zero — they are never computed

`qbeta_ck_cache.py:139-146` extracts recursively:

    for k in range(3, 8):
        ratio_m1 = Q_codata / Q_prev - 1
        if abs(ratio_m1) < EPS_RESIDUAL: break
        ck_extracted = ratio_m1 / u ** k
        Q_next = Q_prev * (1 + ck_extracted * u ** k)

`Q_next = Q_prev * (1 + ratio_m1) = Q_prev * (Q_codata/Q_prev) = Q_codata`
**exactly**. So `c_3` absorbs the entire residual by construction and the
guard fires immediately. Run output, verbatim:

    c_3 (extracted) =   -974.4318877
    c_4: residual below compute precision (0.00e+00) — ladder converged

Residual **exactly** `0.00e+00`. The `structural_candidates` entries for
k = 4,5,6,7 (`c_3*b^4`, `-(b^2+1/2)`, `c_3^2*b^2`, `c_3^3 = -8`) are
**unreachable dead code** — nothing is ever compared against them.

### So the "ladder" has ONE extracted rung

`c_2 = -1` is hardcoded and `c_3` is defined to make the product exact. That
is a two-parameter model fitted through one point, not a convergent series.

**This contradicts AGENTS.md line 1062**, which describes the ladder as *"a
convergent series; N is the truncation order chosen by target precision
(N >= log10(1/eps)/2.07 - 1)"*. There is no truncation order to choose: the
ladder terminates at k=3 by construction, at every anchor, always.

To its credit the producer is honest in its own output — it labels `c_3+` as
*"extracted from Q_codata, CIRCULAR & q0-dependent ... NOT a prediction.
Never counts toward a 100x/1x pass."* The defect is that the AGENTS.md
framing does not match the producer.

### Second finding: the producer is ALREADY convention D

`qbeta_ck_cache.py:85` is `z = q**3 / (q**2 + 1)` — convention D. So its
committed `c_3 = -974.43` is a D-frame value already on main, while
AGENTS.md and the registry still carry the C-frame `c_3 ~ -2.07`. Those are
not competing measurements; they are the same quantity in two frames, and
only one of them is what the producer now emits.

## Consequence: RE-SCOPE

| justification | status after T0.5 |
|---|---|
| Analyticity in h | **stands** |
| Ohtsuki / Habiro literature alignment | **stands** |
| alpha_EM channel consistency | **stands** |
| **Odd rungs become representable** | **VOID** — there are no higher rungs to represent |
| Churn across `c_4...` | **VOID** — those values do not exist |

The migration is now materially smaller than advertised: it touches `c_2`,
`c_3`, and the framing, not a tower. **The siblings told to expect `c_4...`
churn must be re-briefed** — that list was wrong, and it was my broadcast.

The strongest remaining reason to do it is no longer expressiveness. It is
that the h-frame makes the ladder's actual shape legible: a one-rung exact
interpolation is easier to recognise as such when it is not dressed as a
truncated series in a variable chosen to make it converge fast.

## New follow-ups this surfaced

- **AGENTS.md line 1062 is wrong on a second count** (beyond `qou-f09n`'s
  "PROVED Taylor-exact"): the convergent-series / truncation-order framing
  does not describe the producer. Owner sign-off needed — STRICT banner.
- **`qbeta_ck_cache.py` emits 11 raw float64 fields** (the run warns:
  `.assertions[0].computed/expected/tolerance`,
  `.data.rows[*].err_ppb_after_this_rung`, `structural_candidates[*].err_pct`).
  Pre-existing, not mine, worth its own bean.
