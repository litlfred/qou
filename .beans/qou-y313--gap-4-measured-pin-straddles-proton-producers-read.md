---
# qou-y313
title: 'GAP: 4 measured pin straddles — proton producers reading muon artifacts'
status: todo
type: task
priority: normal
created_at: 2026-08-30T04:51:16Z
updated_at: 2026-08-30T04:51:46Z
---

Found by `computations/audits/pin_straddle_unguarded_audit.py` stage 2 (PR #6104),
which reads the producer's anchor from `q0_anchor_manifest.json` and the artifact's
recorded q0 off disk and compares them. All four hand-verified at the load site.

| module | line | pins | loads (muon-built) |
|---|---|---|---|
| `atomic_tr_m_helium4.py` | 133 | proton | `atomic-tr-m-mpfr-50dps.witness.json` |
| `qbeta/qlommel_delta_lambda_lin_vs_sym_ladder.py` | 74 | proton | `binding-single-pipeline-comparison.witness.json` |
| `y_lambda_macdonald_telescope.py` | 352 | proton | `y-lambda-mpfr-witness.json` |
| `y_lambda_symbolic_validate.py` | 102 | proton | `y-lambda-mpfr-witness.json` |

Expected magnitude: the mu-p substrate tension, ~11.5-18 ppb, per the
`block_swap_binding` straddle (6e1009bed8) which measured 18 ppb.

THREE OF FOUR HAVE A CHEAP FIX. The proton twin already exists on disk:
`atomic-tr-m-mpfr-50dps-proton.witness.json` and
`y-lambda-mpfr-proton-witness.json`. And `tr_m_q_hecke_seminormal.py:103` --
a sibling reader of the same atomic-tr-m artifact -- ALREADY selects between
the two by anchor with a ternary. Copy that shape rather than hardcoding.

Two worth reading before fixing:

- `y_lambda_macdonald_telescope.py:352` asserts `mpfr_cross_check_max_abs_diff
  == 0` with `tolerance=1e-30` against the MUON table while the module pins
  proton. Either that assertion is currently absorbing a layer difference far
  larger than its own tolerance, or the check is being SKIPPED
  (`mpfr_check.get("available")` false). Establish which before touching it --
  a passing assertion at 1e-30 across an 11.5 ppb layer gap would mean the
  comparison is not running.
- `atomic_tr_m_helium4.disjoint_product_value()` reads `tr_M_at_q0_50dps` for
  proton and neutron and SQUARES both, so the layer error enters at fourth
  power in `tr_p**2 * tr_n**2`.

NOT DONE IN #6104 ON PURPOSE: each fix needs a producer re-run and a witness
refresh, which is a separate tranche from landing the detector.
