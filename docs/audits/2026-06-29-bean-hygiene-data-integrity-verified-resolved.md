# Data-integrity bean hygiene — verified resolved on main (2026-06-29)

Verification sweep of five data-integrity beans. Four are **resolved on
`main`** (the fixes landed after the beans were written); one is
**half-resolved** and re-scoped. No production code or witness changed by
this pass — this is bookkeeping against the current `origin/main`
(`30101a61`).

## Closed (verified resolved on main)

| bean | claim | verification on main | disposition |
|---|---|---|---|
| `me3r` | three m_e CODATA registries, two truncated | both package copies now `0.51099895069`: `qou-substrate/.../constants.py:283`, `qou-mass/.../codata_constants.py:99` (PR #2725) | **completed** |
| `ct80` | `experimental_constants.py` m_e truncated (`…000`) | `experimental_constants.py:47` now `from codata_2022_source import M_E_MEV` (full) | **completed** |
| `ce18` | `binding_alpha_shift_witness.py` stale CODATA-2018 m_e | producer imports CODATA-2022 (`:50`); **witness baked with `0.51099895069`** (`binding-alpha-shift-witness.witness.json:8`) | **completed** |
| `t2vq` | `delta_lambda_empirical_tabulation.py` ImportError (`m_n_derived_3input` unexported) | `experimental_constants.py:88` exports `m_n_derived_3input`; the consumer imports it (`:100`) and the file parses cleanly (commit `6e233cf0`) | **completed** |

The only residual CODATA-2018 m_e literals (`0.5109989461`) are in
`fsh-guts/deprecated/computations/` (3 files) — off-limits by policy, correctly
untouched.

## Re-scoped (half-resolved)

**`gnb1`** — *iterative-lp-dual-h6-deuteron producer un-runnable
(IndentationError) + tr_M cross-validation failing.*

- **Un-runnable blocker: FIXED.** `computations/iterative_lp_dual_h6_deuteron.py`
  parses cleanly — the broken 3-input anomaly-fixer block that caused the
  `IndentationError` was removed by the 3-input-purge (`ca475e2f` /
  `1e22e4e0`).
- **Remaining (research-grade):** the witness assertion
  `tr_M_cross_validation_within_1e-6` still fails — computed
  `0.00018235144298500055` vs a `1e-6` threshold (a ~1.8e-4 cross-method
  tr_M disagreement on the deuteron H₆ frame). This is a genuine numerical
  discrepancy, pre-existing and independent of the purge; it is **not** a
  mechanical fix and stays open under `gnb1` (re-scoped to this assertion
  only).

## adhb (context, unchanged)

Separately confirmed `adhb` (He-3 R5 multi-term re-run) remains
research-blocked per its own 2026-06-28 audit: the mechanical re-run is
refuted (deuteron `6_2` not PSD-feasible; `L6a4` underpredicts He-3 binding
by ~5.7 MeV), and forcing the canonical winner would be fitting. No action.
