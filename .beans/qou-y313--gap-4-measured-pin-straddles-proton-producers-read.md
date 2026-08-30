---
# qou-y313
title: 'GAP: 4 measured pin straddles — proton producers reading muon artifacts'
status: todo
type: task
priority: normal
created_at: 2026-08-30T04:51:16Z
updated_at: 2026-08-30T05:00:52Z
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


## CORRECTION 2026-08-30 — two of the four were mine, not the corpus's

The table above listed four. **Two are RETRACTED**, both because I wrote the
finding before reading what the consumer does with the loaded data:

- `y_lambda_macdonald_telescope.py` — `cross_check_mpfr` reads the artifact's
  OWN q (`q_val = mp.mpf(table.get("q") or ...)`) and evaluates the closed form
  there. It checks the witness against theory at the witness's own pin. NOT a
  straddle. My note above speculating that its 1e-30 assertion was "skipped
  rather than passing" was answering the wrong question entirely.
- `qbeta/qlommel_delta_lambda_lin_vs_sym_ladder.py` — same:
  `q0 = mp.mpf(str(w["parameters"]["q_0"]))`. NOT a straddle.

This is a seventh false-positive mechanism, and the subtlest: reconciliation by
USING the artifact's pin rather than by comparing against it. Stage 2's
"producer anchor != artifact stamp" test cannot distinguish it from a real
straddle by the numbers alone. Closed in `c036ca4cca`.

## The two that stand

**`y_lambda_symbolic_validate.py:102`** — CONFIRMED, and it is the sharp
contrast case: it reads the SAME file as macdonald_telescope but
`load_mpfr_witness()` DROPS the witness's `q` at load, returning only
`{n: {partition: y}}`. `test_1_cross_q` then compares against the Wenzl bridge
evaluated at `Q0_STR = Q_50_DIGIT_STR`, which resolves to PROTON for this stem.

MEASURED: at n=3 the bridge at the proton pin differs from the muon witness by
**1.19e-9** (n=4: **1.49e-9**) against its own `TOL_CROSS_Q = 1e-30`. So the
q_0 probe is **21 orders over tolerance** — this test is not silently absorbing
a layer gap, it is FAILING, for a layer reason rather than a mathematical one.
Fix: point at `y-lambda-mpfr-proton-witness.json`, or key by anchor.

**`atomic_tr_m_helium4.py:133`** — CONFIRMED. `disjoint_product_value()` reads
`tr_M_at_q0_50dps` for proton and neutron out of the muon witness and returns
`tr_p**2 * tr_n**2`, so the layer error enters at fourth power. The proton twin
`atomic-tr-m-mpfr-50dps-proton.witness.json` exists, and
`tr_m_q_hecke_seminormal.py:103` already selects between the two by anchor with
a ternary — copy that shape.
