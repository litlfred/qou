# cds1 ladder/correction side — no parameter-free admissible correction; the aug near-match is the forbidden z=1 return

**Date:** 2026-08-29 · **Bean:** `qou-cds1` (S1, ladder/correction side; takeover
of #5337's unstarted goal) · **Tier:** scope-(a) measured negative + a diagnosed
near-match · **Discipline:** no fit, nothing wired, `free_parameters = 0`,
`sqrt(1−h)` NOT adopted.

## Context

The convention-D Q_β re-derivation splits into a **base** and a **correction**.
The base side is settled: the admissible base functional is one of exactly two
(`QOU.QBeta.AdmissibleRoots.admissible_markov_param_iff`, Lean — roots `{q, z_D}`;
`net` at `z=1` excluded by `one_not_root`). Both admissible bases miss CODATA
badly (qou-99qc, on the NF vector):

| base | Markov parameter | `|Q|` MeV | dev vs CODATA |
|---|---|---|---|
| augmentation | `z = q` | 0.8798905613 | +12.470 % |
| Markov trace | `z = z_D` | 0.4447004085 | −43.157 % |

So each needs a multiplicative correction `F_required = Q_codata/base`:
`F_required(aug) = 0.88913`, `F_required(tr_M) = 1.75924`. #5337's stated goal
("fold the Wenzl two-row cap into the D decay correction") reduces to: **is there
a parameter-free categorical object supplying `F_required`, or only a fit?** The
single candidate "F = the two-row restriction fraction" is already pruned
([`qbeta_d_frame_two_row_cap_prune_probe.py`](../../computations/qbeta/qbeta_d_frame_two_row_cap_prune_probe.py),
13.6×). This audit does the systematic enumeration on **both** bases.

## Method

[`computations/qbeta/qbeta_d_frame_admissible_base_correction_search_probe.py`](../../computations/qbeta/qbeta_d_frame_admissible_base_correction_search_probe.py)
(mpmath 50 dps, no float64; witness `qbeta-d-frame-admissible-base-correction-search.witness.json`,
2 assertions). Enumerate the natural parameter-free objects in `{q, h, z_D}`,
report distances to each `F_required`. Anti-fit: a match counts only if uniquely
singled out by a categorical principle *before* seeing the target; a basket
coincidence is a fit.

## Result

**tr_M base — WALLED.** `F_required = 1.75924`; the closest parameter-free object
is `q⁶` at **6.31 %**, then `1/z_D` at 7.22 %. No parameter-free correction
exists near this base.

**augmentation base — the near-match is the forbidden `z=1` return.** The tempting
`sqrt(1−h) = 0.889348` lands **0.025 %** from `F_required` (isolated; next is
`1−h/2` at 0.71 %). But it is a basket coincidence pointing in the *forbidden*
direction. The base is `∝ tr_M(Δ_S)`, which is affine, `tr_M(Δ_S)(z) = h²/2 − h·z`
(#5897). So the required correction is, to 0.17 % (**exactly** the net-vs-CODATA
gap), the trace's own `z=q → z=1` ratio:

```
  net/aug  =  tr_M(Δ_S)|_{z=1} / tr_M(Δ_S)|_{z=q}  =  (h/2 − 1)/(h/2 − q)  =  0.8906174
```

and the measured base ratio agrees with this to **1.3 × 10⁻¹¹** (proving
`base ∝ tr_M(Δ_S)`). "Correcting" the augmentation base back to CODATA is
therefore the **return to the `z=1` (net) value that convention D excludes**
(`one_not_root`). `sqrt(1−h)` sits 0.025 % from `F_required` and 0.14 % from that
forbidden ratio — a clean form near a forbidden object, not an admissible
derivation.

Ordering: `F_required 0.88913 < sqrt(1−h) 0.88935 < net/aug 0.89062`.

## Verdict — scope-(a)

**No parameter-free ADMISSIBLE correction closes either convention-D base.** The
one sub-0.1 % near-match is the forbidden `z=1` return in disguise. The D
re-derivation does not close at the current framing (admissible base × one
multiplicative correction). This closes #5337's stated question with a measured
negative and extends the single-candidate two-row-cap prune to both bases.

Nothing is wired; `free_parameters = 0`; `sqrt(1−h)` is explicitly **not** adopted.
The anti-fit discipline is the point: a 0.025 % basket near-match, diagnosed, is
the forbidden move — not a derivation.

## What would change the verdict

An admissible correction must come from an object that does **not** route through
`z=1`. The current framing (base at an admissible `z`, times a scalar) cannot
supply it, because the accurate value lives at the inadmissible `z=1`. A genuinely
different D-frame construction of Q_β — not `tr_M(Δ)` at a single Markov
parameter — would be needed. None is known; this is the open core of `qou-cds1`,
now sharpened rather than closed.
