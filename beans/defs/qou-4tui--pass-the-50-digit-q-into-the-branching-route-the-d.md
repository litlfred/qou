---
# qou-4tui
title: Pass the 50-digit q into the branching route; the D row is 16 digits, not 50
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T06:38:32Z
updated_at: 2026-11-20T08:32:31Z
parent: qou-cdx1
---


Opened 2026-09-05 from a delegated precision audit of the branching binding
route, which I had flagged on the strength of `q_val=float(Q_FLOAT)` at
`canonical_mass_table_extended.py:323`.

## The flag was right to raise and wrong about the mechanism

`float(Q_FLOAT)` was a **no-op**: `q_parameter.Q` is already binary64 by
construction (`Q = float(_d["q"])`, the declared f64 twin of `Q_50_DIGIT_STR`),
gap `2.72e-17` from `Q_MP`. And for `A >= 3` the downcast never reached the
arithmetic: a guard at `canonical_tr_m_via_branching.py:555` compares
`abs(float(q_val) - float(Q_FLOAT)) < 1e-30`, sees `0.0`, and dispatches with
`q_arg=None`, so `tr_m_atom_zn` used the full 50-digit q throughout. Had the
guard not fired the cost would have been ~15 digits (measured: rel diff
`4.6e-16` / `5.9e-16` / `7.0e-16` for T / 3He / 4He).

## Where the precision actually is short

**`A = 2` only.** The D row goes through `compute_chi_lambda_via_branching`,
which is NumPy `complex128` end to end (`_compiled_sigmas(shape,"double")`,
`np.kron`, `np.trace`). `mp.mpf(str(chi.real))` then lifts ~16 real digits into
a 70-dps accumulator and `fmt` writes 60. Two independent confirmations the
tail is not real: raising `mp.mp.dps` 70 -> 120 leaves D bit-identical, and the
tail moves with unrelated process history (a prior `tr_m_atom_zn` call in the
same process shifts digit ~48 on).

    Atom   route                 rel diff from arbiter   real digits   published
    D      branching (NumPy)     3.79e-15                14            60
    T      transfer              0 (bit-identical)       ~49           60
    3He    transfer              0                       ~49           60
    4He    transfer              0                       ~49           60

## The change

One behavioural line: `q_val=Q_MP` in place of `float(Q_FLOAT)`, plus `Q_MP` on
the import and a comment recording the measurements. Safe because
`float(Q_MP) == Q_FLOAT` bit-exactly, so the `A >= 3` dispatch still takes
`q_arg=None`. Full nine-row re-run: **eight rows bit-identical, D improved**,
`3.79e-15 -> 8.69e-17` from the arbiter, two digits recovered, because
`build_A_extract_at_q` now builds at the true 50-digit q. No runtime cost.

Residual, not forced: the remaining `8.69e-17` is the combiner's `complex128`
floor. Removing it needs `_compiled_sigmas`/`np.kron`/`np.trace` rewritten in
mpmath, or the D row routed to the transfer as `A >= 3` already is. Both are
algorithm changes. **So the D row is ~16 digits under either spelling.**

## Good news for the published table

The 2-dp errors do NOT come from this route: `canonical_mass_table_extended.py`
"does NOT compute B_pred from |tr_M|". Recomputed independently at 80 dps they
reproduce exactly (`+1.090306...`, `-0.155601...`, `-2.968654...`,
`+5.866676...`). Two decimal places is understated, not overstated.

- [x] Trace the precision path
- [x] Quantify the damage
- [x] Fix the tractable part
- [x] Verify; gate 5 hits -> 1 on the touched file

## Left open, deliberately, for a decision

- [x] **`canonical_mass_table_extended.py:492`, `float(nucleon_mass_mev(species))`**
      — a genuine pre-existing float64 leak landing in `prediction_MeV_50dps`
      for the p/n rows (hence `938.2720894273243`, 16 digits, in a 50dps
      column). It feeds the L2 dashboard and the p/n route has an open
      adjudication (`qou-khue`). NOT silenced with a false `float64-ok`; the
      gate still reports it.
- [x] Truncating the emitted `tr_M` digits to what is real (D publishes 60 from
      a 14-digit computation). Witness/schema change, one code consumer, no
      content pin — editorial, not a precision fix.
- [ ] **`± 0.0000 %` in the rendered table is the AME EXPERIMENTAL uncertainty,
      not a prediction error bar.** Correctly computed (1.8e-5 % … 2.8e-6 %),
      but a reader can take "+5.87 ± 0.0000 %" as a four-decimal claim about the
      framework's miss. The 5.87 % carries no model or compute uncertainty at
      all. Worth rewording.
- [x] `atlas_render_canonical_table.py` targets `recursive-atom-knot-atlas.md`,
      which has no markers; the live AUTO block is in
      `recursive-atom-knot-atlas-registry.md`. Its dry-run footer also disagrees
      with the committed .md on method and link prefix.

## 2026-11-15 — 50-dps D-row transfer routing, p/n 50-dps lift, and atlas renderer fix (`litlfred/qou#7995`)

- Per owner ruling `Q-AVTQ-1 = 1`:
  - Routed the `D` (`A = 2`) row in `computations/canonical_mass_table_extended.py` through the 50-dps transfer-matrix path `tr_m_atom_zn` (matching `A >= 3`), lifting `tr_M_q0_canonical_50dps` on the `D` row from 16-digit `complex128` (`0.1519683392042316303185...`) to 50+ dps (`0.151968339204231607592665697751066141271240964655247542840855`).
  - Removed the `float(...)` truncation on `nucleon_mass_mev(species)` (eliminating the I8 float64 leak in `canonical_mass_table_extended.py`) and formatted `prediction_MeV_50dps` on `p, n` at 50 dps via `fmt(pred, dps=50)`.
  - Repointed `ATLAS_MD` in `computations/atlas_render_canonical_table.py` to `recursive-atom-knot-atlas-registry.md`, stripped the obsolete `/folio-assistant/` URL prefix, updated the nucleon mass footer attribution to `canonical_mass.nucleon_mass_mev()`, and re-rendered the table.
- PR: [`litlfred/qou#7995`](https://github.com/litlfred/qou/pull/7995) (commit `4552d3620d0f14bf058a5a7031606034f7a2a6be`, signed `ready:` comment [`#issuecomment-6901100726`](https://github.com/litlfred/qou/pull/7995#issuecomment-6901100726)).


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch A):** in-progress → completed. Work commit 4552d3620d0 is on main.
