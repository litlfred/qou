---
# qou-q0zk
title: 'DRAIN: 99 witnesses may be convention-C-frame under D producers (#4899 sweep tail)'
status: todo
type: task
priority: normal
created_at: 2026-08-19T20:13:39Z
updated_at: 2026-08-23T17:00:27Z
---

PR #4899 excised convention C from the producer layer ("178 sites -> 0") and
reported "witnesses regenerated across 68 producers". **Two witnesses it missed
were found independently, by two sessions, from different directions:**

* `qou-580o` — a `qbeta` witness, found auditing the c_3 ladder (PR #5265).
* `qou-h4ab` — `wedderburn-lp-ew-wiring`, found porting that producer off
  float64; `t_legacy_matrix_entries` moved 13-21%.

Two independent hand-finds of one class is the signal the class is not two
items long. New scanner: [`computations/convention_frame_staleness_audit.py`].

## Measured

    producers with a D-form bound to a Markov-named variable : 137
    their witnesses                                          : 138
    witness predates the 2026-08-10 migration                : 101
    ... and producer changed since (SUSPECT)                 :  99
    ... dropped, producer unchanged (same D code wrote it)   :   2

## Confirmed by the decisive test, 2 of 2 attempted

The test is: swap the producer's `z` back to the C form and check the
**committed** value reappears.

| witness | committed | conv D | conv C |
|---|---|---|---|
| `wedderburn-lp-ew-wiring` (proton) | 0.6003377241833765 | 0.68036969746 | **2.1e-16** |
| `wedderburn-lp-ew-wiring` (neutron) | 0.3727036271108378 | 0.44938418327 | **5.7e-16** |
| `fr-pullback-cosh-h` `best_variance_finite` | 1.537500801376956 | 1.488319082475366 | **1.537500801376956 exact** |

`fr-pullback-cosh-h` was found BY the scan and then confirmed, which is what
makes the scan worth trusting rather than a grep someone ran once. Its
producer + witness were restored after the test; nothing committed from it.

## What the 99 is NOT

A count of confirmed-stale witnesses. It is a **high-recall candidate list**,
same standing as the lean-vacuity candidates and the raw-float64 ratchet — the
verdict is an agent call, per candidate. Specifically:

* `q**3/(q**2+1)` is a shape, not a meaning. The scan requires it bound to a
  Markov-NAMED variable (`z`, `z_mark`, `z_D`, `z_electron`, ...). A producer
  computing the Markov parameter under another name is **missed** — so 99 is
  also not an upper bound.
* "witness predates the migration" does not prove its values are C-frame; the
  producer may not use `z` in anything serialized.
* `scriptHash` matching means the producer is unchanged, so that same D code
  wrote the witness. Those 2 are dropped, not counted.

## Do NOT bulk-regenerate

Re-running `fr_pullback_cosh_h_test.py` alone dirtied its witness with **40
raw float64 fields** and dropped `clarabel` from the environment block (main's
new `_check_environment_regression` caught it). A 99-file sweep in this
container would import that damage wholesale. Each item needs: decisive test
-> confirm -> regenerate in an environment that matches the recorded one ->
check the raw-float64 ratchet did not grow.

Related: `qou-1c4y` (the muon->proton witness migration) has the same
"large tracked sweep, needs scoped sign-off" shape.


## 2026-08-23 — re-measured after merging main, and RANKED

**73, down from 99.** Main drained 26 of the candidates during the four days
this branch was open — independent corroboration that the detector tracks a
real class rather than a grep artifact.

**Every one of the 73 is CONSUMED.** Ranked by in-corpus references
(`_deprecated/` consumers excluded, since those do not matter):

| refs | witness | reached by |
|---|---|---|
| content 2 | `alpha-k-jones-markov-h3` | `explicit-alpha-k-h3-proof.md`, `categorical-mass-markov-proof.ts`, `codata_reconciliation.py` |
| content 2 | `wedderburn-pair-volumes` | `knot-operator-lp-selection.ts` + `.qa.json` |
| content 2 | `probes/gauge-coupling-uniqueness-probe` | `gauge-coupling-uniqueness.ts` + proof `.qa.json` |
| content 1, code 22 | `free-neutron-decay` | `energy-scale-planck.qa.json`, `beta-decay-energy-scale.py` |
| content 1, code 7 | `binding-depth-stratified` | `depth-stratified-frobenius-reciprocity.ts`, `low_isotope_binding_model_comparison.py` |
| content 1, code 2 | `demazure-markov-trace` | `demazure-fiber-markov-trace.ts`, **`onepb_status_dashboard.py`** |
| content 1, code 2 | `qbeta/qbeta-c3even-exact-sseries` | `binding-qbeta-complex-volume.md` |

**0 of 73 are terminal probes.** So this is not a backwater: the class reaches
content blocks (the paper itself), the **L1 status dashboard**, and the CODATA
reconciliation.

### What this ranking does and does not establish

It says **which to check first**, not that any of them is stale. Consumption
is a priority signal, not evidence. The confirmed count is still **2 of 2
attempted** (`wedderburn-lp-ew-wiring`, `fr-pullback-cosh-h`) — every other
row needs its own decisive test (swap `z` to the C form, check the committed
value reappears) before being called anything.

Suggested order for a drainer: the three content-cited rows first, since a
stale frame there propagates into the paper rather than into another probe.
