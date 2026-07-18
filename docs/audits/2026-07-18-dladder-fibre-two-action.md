# D-ladder per-parity fibre action — k=31 cannot feed the two-critical-time accelerator (honest negative)

**Date:** 2026-07-18 · **Axis:** c₃ / Q_β bar-odd swing / 1ppQ (D-ladder Écalle,
sibling #3818) · **Tier:** numerical scope-(a) structural measurement (a negative —
what k=31 can and cannot support) · **Discipline:** no fit (nothing tuned to CODATA),
no c_k wired, nothing to production, no tier change.

## Question

The whole D-ladder Écalle program hinges on one structural gate: is the bar-odd
D-ladder genuinely **two-level** (a sum of two Gevrey series with *distinct* Borel
actions — so a non-commutative two-critical-time Écalle accelerator is the required
tool, and its two critical times are those actions) or **single-level** (one action —
the accelerator is overkill and the swing is a plain single Borel object)? The merged
Φ_b probe (#3818, "M2") found two distinct divergence *classes* `C_odd ≈ 0.052`,
`C_even ≈ 0.115`; my #3861 found the parity *orders* soften toward a common value at
k=31 — an unresolved tension. The
[fibre-branch probe](2026-07-18-dladder-fibre-branch-stokes-ambiguity.md) then showed
the fibre effective action drifts `0.38 → 0.23`, which a two-action sum would produce.

## Test (accelerator prerequisite)

[`qbeta_dladder_fibre_two_action_probe.py`](../../computations/qbeta/qbeta_dladder_fibre_two_action_probe.py)
splits the exact ℚ(√3) ladder by k-parity (the M2 split: odd `k ≥ 3`, even `k ≥ 4`)
and measures **each half's own least-term action** `A = −|ũ|·ln δ_np` on the fibre,
where the least term is interior and no Padé is needed. On the substrate both halves
are pinned at the `k = KMAX` edge (unmeasurable); the fibre resolves them.

## Result — the actions COINCIDE where both are resolved, then the odd half drops out

| `‖ũ‖` | `N*_odd` | `A_odd` | `N*_even` | `A_even` |
|---|---|---|---|---|
| `0.148` | `27` | `0.420606` | `28` | `0.420597` |
| `0.152` | `15` | `0.349336` | `16` | `0.349293` |
| `0.156` | `11` | `0.306129` | `10` | `0.306569` |
| `0.160` | `3` | — (dropped) | `8` | `0.27778` |
| `0.168` | `3` | — | `6` | `0.234044` |
| `0.180` | `3` | — | `6` | `0.176250` |

- **Where both parities are simultaneously well-resolved** (`|ũ| ≈ 0.148–0.156`,
  interior `N*` of `27/28`, `15/16`, `11/10`), `A_odd` and `A_even` **coincide to
  4–5 digits**. There is **no** sign of two distinct actions in the one window where
  both are measurable.
- Past `|ũ| ≈ 0.16` the **odd half's `N*` collapses to `3`** (its least term hits the
  bottom of the shorter odd sub-ladder) and leaves the interior, so `A_odd` is no
  longer measurable. The even half continues and its `A_even` drifts down
  (`0.278 → 0.176`) — but with the odd half gone there is nothing to compare it to.

So the two plateaus are **not** cleanly flat-and-distinct: `both_flat = False`,
`distinct = False`, separation `|A_odd − A_even| = 0.065` (rel `0.196`) — but that
separation compares an odd mid over 3 edge-proximate points against an even mid over
9 points spanning the whole drift, an apples-to-oranges artifact of the odd half's
early drop-out, **not** evidence of two resolved actions.

## Reading (careful — neither confirms nor cleanly refutes two-level)

**k=31 is insufficient to feed the accelerator two clean critical times.** The one
window where both parities are measurable shows a **common** action to 4–5 digits
(a mild lean toward *single*-level / the #3861 softening), but that window is
edge-proximate (`N* ≈ 27–28` near `KMAX = 31`), so it partly reflects shared
top-rung behaviour rather than each sub-series' own asymptotics; and the odd half
cannot be resolved deep in the interior at this length. The honest conclusion:

- The M2 "two distinct critical times" reading is **not supported** at the
  resolvable scale — the leading actions coincide wherever both are visible.
- But two *separately-resolved* per-parity actions **cannot be extracted at k=31**;
  the accelerator's inputs are not available from this length.
- **Deliverable for #3818:** do not attempt the two-critical-time accelero-summation
  on the current 31 exact rungs — it cannot be fed clean, distinct critical times.
  Resolving two-level-vs-single-level needs either more exact rungs (ORD > 63) so the
  odd half stays interior deeper, or a genuine transseries fit rather than
  optimal-truncation least-term reads.

## Scope (anti-laundering)

A structural *negative*: records what k=31 can and cannot support for the accelerator,
and re-scopes the M2 two-level claim as *not-resolvable-here* (not *refuted* — the odd
half is under-resolved). Derives no c₃ value; wires nothing; no tier change. No fit;
no c_k.

## Cross-references

- Companion (branch selector): [`2026-07-18-dladder-fibre-branch-stokes-ambiguity.md`](2026-07-18-dladder-fibre-branch-stokes-ambiguity.md)
- M2 two-level claim: [`2026-07-17-dladder-ecalle-phib-resummation.md`](2026-07-17-dladder-ecalle-phib-resummation.md) (#3818)
- Parity-order softening: [`2026-07-17-dladder-odd-singularity-even-order.md`](2026-07-17-dladder-odd-singularity-even-order.md) (#3861)
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
