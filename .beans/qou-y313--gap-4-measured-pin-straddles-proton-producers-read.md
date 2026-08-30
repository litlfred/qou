---
# qou-y313
title: 'GAP: 4 measured pin straddles — proton producers reading muon artifacts'
status: completed
type: task
priority: normal
created_at: 2026-08-30T04:51:16Z
updated_at: 2026-08-30T12:15:17Z
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


## CONFIRMED END-TO-END by the producer's own verdict (2026-08-30)

Running `y_lambda_symbolic_validate.py` on current main flips its own
`all_passed` from **true** to **false**. Every n from 2 to 11+ fails at
**exactly probe index 2** -- the `Q0_STR` probe, the only one whose reference
is `"ref": "mpfr-witness"` rather than the self-consistent
`wenzl-bridge@100dps`. Every other probe passes at ~1e-51.

    n=2   max_abs_diff 5.93e-10      n=7   1.06e-9
    n=3               1.19e-9        n=8   8.04e-10
    n=4               1.49e-9        n=9   5.82e-10
    n=5               1.49e-9        n=10  4.06e-10
    n=6               1.31e-9        n=11  2.75e-10

against `TOL_CROSS_Q = 1e-30`. The self-referential probes are unaffected,
which is what localises the defect to the witness comparison rather than to
the bridge.

### The committed witness is also STALE, and in an instructive way

`computations/y-lambda-symbolic-validation.json` on main records
`all_passed: true` and exactly one q value: **`1.1099785955541805`**.

Two things wrong with that string. It is a MUON value, so the record was
produced when this stem resolved to muon -- which is why it passed. And it is
**17 significant digits**, not 50, in a witness whose whole subject is 50-dps
validation. Per AGENTS.md's three-muon-values note, `...595554 1805` is
specifically the lepton-tower derivation at **CODATA 2018**, not the frozen
canonical pin `...5955573347`. So the committed record is a pass obtained at
a third q that is neither of the two live anchors.

DO NOT simply regenerate this witness to "refresh" it -- that would land
`all_passed: false` as the recorded state. Fix the producer first (point
`load_mpfr_witness` at `y-lambda-mpfr-proton-witness.json`, or key it by
anchor the way `tr_m_q_hecke_seminormal.py:103` does), THEN regenerate.

Not done here: the regenerated file was a diagnostic side-effect and was
restored, per the contended-witness rule (qou-v0t8).


## FIXED (1 of 2): y_lambda_symbolic_validate — 45dbc808f4, PR #6104

`load_mpfr_witness` now selects the reference by the artifact's OWN recorded
`q` rather than by a hardcoded path or via the manifest. Reconciles against the
stamp instead of trusting a filename, and degrades honestly: an unmatched pin
returns `{}` and every probe falls back to its self-consistent
`wenzl-bridge@100dps` reference rather than comparing across a layer boundary.

    n=3   1.19e-9  ->  2.53e-51        tolerance TOL_CROSS_Q = 1e-30
    n=4   1.49e-9  ->  2.91e-51
    coverage 11 -> 17 values of n (the proton table is the more complete one)

Two independent checks agree and neither was tuned to the other: the arithmetic
moves 42 orders, and `pin_straddle_unguarded_audit` stage 2 — written before
this fix — stops flagging the module (2 mismatches -> 1).

### WITNESS REGENERATION IS STILL OPEN, and it is a LONG COMPUTE

`computations/y-lambda-symbolic-validation.json` on main is still the stale
record (`all_passed: true` at `1.1099785955541805`). Do not commit a partial
regeneration: the producer writes incrementally per-n, so a killed run leaves a
witness carrying TWO different q values at once — measured, n=11 and n=12 still
held the old muon value while every completed n held proton. That is the exact
defect this branch is about.

MEASURED BUDGET: a `timeout 900` run completed Tests 1 and 2 across all n with
**zero [FAIL]**, then was killed partway through Test 3. So >900 s, and the
true figure is higher than the old record implies — the fix RAISES coverage
from 11 to 17 values of n, so Test 3 now runs on 6 more (and larger) partition
sets than the committed witness ever did.

Run it with `python3 -u ... 2>&1 | tee /tmp/ylsv.log` and a budget of 3000 s+,
to completion, in one go. Re-verify `all_passed` and that exactly ONE q value
appears in the file before committing.

TRAP for whoever picks this up: a waiter that greps only for
`ALL TESTS PASSED|SOME TESTS FAILED` hangs forever on a timeout kill, because a
killed process prints neither. Watch for process death as well as for the
marker.


## The SECOND straddle is now SIZED (read-only measurement, nothing written)

`atomic_tr_m_helium4.disjoint_product_value()`, computed directly from the two
committed witnesses:

    tr_M(p)   muon 1.14575978232   proton 1.14575969246   rel 7.84e-8
    tr_M(n)   muon 0.987743756821  proton 0.987743688116  rel 6.96e-8
    tr_p^2 * tr_n^2                                       rel 2.96e-7 = 296 ppb

The fourth-power amplification is explicit in the arithmetic:
(1+e)^2(1+f)^2 - 1 = 2e + 2f = 2(7.84e-8) + 2(6.96e-8) = 2.96e-7. So the
per-factor 78 ppb becomes 296 ppb on the product.

INDEPENDENT CONFIRMATION. These are the same numbers the `93888aa431` fix
comment records for `canonical_tr_m_via_chi_cache` -- "7.84e-8 on the proton,
2.9e-7 at 4He" -- reached here by a different route entirely (differencing the
two committed witnesses rather than instrumenting the combiner). Two unrelated
paths landing on the same figure is what makes this a measurement rather than
a reading.

FIX: same stamp-reconciliation as `y_lambda_symbolic_validate` -- select the
witness whose recorded q matches the runtime pin. `_pb.witness_path(...)` at
line 133 hardcodes the muon basename; the proton twin
`atomic-tr-m-mpfr-50dps-proton.witness.json` carries identical structure and
the same five atoms. `tr_m_q_hecke_seminormal.py:103` already picks between
them with a ternary.

Deferred off PR #6104 for regeneration cost (DIRECT_BUDGET_SEC = 480 per
trace), NOT for difficulty. The load-path change itself is one line.


## CORRECTION 2026-08-30 (second) — the "coverage 11 -> 17" claim is WRONG

I wrote, in this bean and in the PR body, that the witness regeneration is
longer than the old record implies "because the fix RAISES coverage from 11 to
17 values of n, so Test 3 now runs on six more and larger partition sets."

That is false. `main()` sets `ns = list(range(2, 13))` -- the n range is
HARDCODED at 2..12 and is not driven by the witness table. `load_mpfr_witness`
now returns 17 entries instead of 11, but only n=2..12 are ever consumed, so
the extra proton entries are available and unused.

Two things this changes:

- **The regeneration cost is UNCHANGED by my fix.** The >900 s figure was
  measured and stands; my explanation for it was invented. Test 3 at n=11-12
  (all partitions x 5 probes x 2 mu) is simply expensive, and was equally so
  before. The committed record contains test_3 for all of n=2..12, which proves
  the run IS achievable -- 900 s was just short of it.
- **The fix's benefit is narrower than I stated.** It corrects WHICH table is
  compared against, not HOW MUCH is validated. No additional n is checked.

The 42-order accuracy improvement (1.19e-9 -> 2.53e-51) is unaffected and was
measured directly. Only the coverage claim was wrong.

Also worth recording: `main()` is MERGE-AWARE ("preserve entries for n not in
this run"). That is exactly why a killed run leaves a genuinely mixed-pin file
rather than a truncated one -- the stale n survive by design. It confirms the
decision to restore rather than commit the partial.

Corrected in the producer docstring so the next reader does not inherit it.


## CLOSED 2026-08-30 — all four resolved, verified by measurement

Final disposition of the four entries in the table above:

| module | outcome |
|---|---|
| `y_lambda_macdonald_telescope.py` | **RETRACTED** — reads the artifact's own `q`. Never a straddle. |
| `qbeta/qlommel_delta_lambda_lin_vs_sym_ladder.py` | **RETRACTED** — same. |
| `y_lambda_symbolic_validate.py` | **FIXED** in PR #6104 (`45dbc808f4` + `3e03eff95c`) |
| `atomic_tr_m_helium4.py` | **FIXED AND REGENERATED** |

**The helium-4 leg is confirmed done, not assumed.** `_pick_witness_for_pin()`
is live in the producer, and the committed witness records
`source_witness: "atomic-tr-m-mpfr-50dps-proton.witness.json"`. Checked by
value rather than by that field:

    committed abs_tr_p_50dps  vs proton reference   rel = 0.0   (exact)
    committed abs_tr_n_50dps  vs proton reference   rel = 0.0   (exact)
    committed abs_tr_p_50dps  vs MUON layer         rel = 7.84e-8

So the 296 ppb fourth-power error this bean was opened for is gone, and the
witness sits on the layer its producer pins to.

**Detector agrees:** `pin_straddle_unguarded_audit.py` stage 2 reports
**0 measured mismatches, 0 artifacts** on a full scan.

## What closing it exposed — split to its own work, not left here

Both fixed modules were **still flagged by stage 1** after being correctly
fixed. The detector could not see its own recommended remedy: RECONCILIATION 2
tracked derivation on the stamp side (`_stamp_derived`) and demanded a literal
on the runtime-pin side, while both fixes bind the pin first
(`want = mp.mpf(Q_50_DIGIT_STR)`).

That is not cosmetic — the #6104 PR body states "candidate list triaged to
zero" as the precondition for making this gate blocking, and a detector blind
to its own fix can never reach zero.

Fixed in the same tranche (`2861f0a73f`): added the mirror `_pin_derived`,
iterated to a fixed point (a module-level alias plus an in-loader conversion is
two hops, and one hop left `y_lambda_symbolic_validate` flagged), and added
`"q"` to `STAMP_KEYS` — which looks too generic and is not: **5 of 5**
`.get("q")` sites in live `computations/` read a pin stamp off an artifact
table, and `y-lambda-mpfr-witness.json` stamps every per-n table with exactly
that key.

**133 → 123 shape candidates, `--selftest` PASS, stage 2 unchanged at 0.**
