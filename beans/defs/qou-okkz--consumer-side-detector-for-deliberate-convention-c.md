---
# qou-okkz
title: Consumer-side detector for deliberate convention-C control arms (qou-q0zk drain safety)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T14:10:58Z
updated_at: 2026-10-10T07:47:08Z
parent: qou-cdx1
---

## MEASURED on main, 2026-08-24 (PR #5669, branch claude/consumer-control-arm-detector-2026-08-24)

The control arm is a **CONSUMER**, not a witness. My earlier intersection test
ran at the witness layer -- candidate witnesses against the fingerprint
detector's control arms, intersection genuinely empty -- and concluded there
were no control arms in scope. The arithmetic was right; the layer was wrong.

New: `computations/audits/consumer_control_arm_audit.py` + its witness.

| quantity | measured |
|---|---|
| witnesses scanned | 2938 |
| carrying the z_C fingerprint | 36 |
| carrying the muon-q0 fingerprint | 389 |
| python files scanned / naming a witness | 3758 / 1854 |
| **foreign READ edges of convention-C witnesses** | **229 across 122 consumers** |
| foreign-transcription edges | 15 |
| ... **CONTROL-ARM (>=1 specific value)** | **1** -- h4_markov_weights_closed_form.py |
| ... shared-constant only (m_e, hbar-c, a q0 pin) | 14 across 12 consumers |
| self-written pairs dropped | 371 |

**The 229 is the blast radius; the 1 is what is provable. The other 228 are
`unmeasured`, NOT clear.** The detector only sees a control arm that
TRANSCRIBES its reference values into its own source. PR #5616's own edit moved
`published_q0` in the known positive from a transcription to a run-time read;
had it moved XCHECK_Z and XCHECK_WEIGHTS too, this would report nothing.

## How it keys, and why not by name

`XCHECK_*` is one SPELLING. Keying on it would be entry fourteen in the
detector-blindness taxonomy. It keys on the fact instead: a control arm has
copied numbers OUT OF the artifact it reads INTO its own source, checkable
against the bytes of both files.

  A1 transcription -- a high-precision literal in the consumer's own code whose
     exact value is in a stale-frame witness it READS AND DOES NOT WRITE.
  A2 specificity -- that value is in <= 3 witnesses corpus-wide, so it
     identifies THAT artifact rather than being a shared constant.
  A3 dual anchor -- NAME-BASED, reported, never promotes a verdict.

## Three blind spots hit, and two were mine

1. **A witness write spelled as a STEM.** b_over_a_evaluator.py emits via
   `WitnessBuilder.wrap_legacy("b-over-a", ...).save()` and carries a DEAD
   `out = HERE / "b-over-a.witness.json"`. A `.witness.json`-keyed detector
   cannot see the write, so it read as a foreign consumer of its own output.
   235 wrap_legacy sites in tree.
2. **My fix for (1) was worse than the bug.** I put `witness_path` in the write
   set. `_path_bridge.witness_path` RESOLVES a path and is overwhelmingly a
   READ helper (324 sites). It suppressed 300+ pairs and would have made the
   audit blind to the class it exists to find.
3. **The audit flagged ITSELF** -- it names the known positive's witness as a
   string constant. Self-excluded, citing qou-a6yh: "a detector that flags its
   own control arm trains the reader to ignore it."

Also: 197.3269804 in b_over_a is hbar-c. Specificity is necessary, not
sufficient -- rarity is not provenance.

## Verification (CI is dispatch-only; Copilot does not arrive, qou-gwe9)

  * --selftest PASS (25 s full scan).
  * MUTATION-TESTED: SPECIFICITY_MAX->0, MIN_SIG_DIGITS->30, and disabling the
    write-exclusion each flip --selftest to FAIL. It does not pass by
    construction.
  * All 29 pairs the write-exclusion suppressed hand-checked: every one is
    script-to-own-witness. The exclusion hides no control arm.
  * Witness has 0 raw float64 fields; Decimal end to end.


## Follow-up (c3b23173d7): the CM tag does not say what the CONSUMER depends on

The witness frame tag says what the ARTIFACT carries. A drain can get the
convention axis and the pin axis wrong INDEPENDENTLY, so each edge now carries
`frame_evidence`. Measured on the known positive, and it contradicts what the
`CM` tag suggests:

  h4_markov_weights_closed_form.py is DELIBERATELY ON C, and NOT deliberately
  on muon.

  z_C in consumer source      True   -> a convention fix breaks it LOUDLY
  muon q0 in consumer source  False  -> PR #5616 moved that to a run-time read
                                        specifically to avoid embedding a stale
                                        q0 literal
  payload reproduced          5      -> frame INHERITED from the artifact

Consequence for the drain: **re-pinning the artifact silently changes the
numbers this control reproduces and nothing in the consumer objects**, whereas
changing the convention breaks visibly. The silent one is the dangerous one and
is invisible to any check that only asks "does this file mention convention C".
This overlaps qou-a6yh's audit/check-context class -- both classes co-occur here.

## The self-poisoning census (the better catch)

The audit's own witness records every transcribed value verbatim, so each run
added itself to the corpus-wide specificity census: the known positive's five
weights went 2 -> 3 witnesses the moment the witness was first committed. The
test is `census[v] <= 3`, so at 3 it still reads specific -- but ONE MORE such
artifact tips them to `common` and the CONTROL-ARM verdict vanishes with no
error. A detector that goes quiet by writing down what it found. Self-excluded;
same hazard as SELF_OUTPUT_PREFIX in compute-author 5.1. Census verified stable
at 2 over repeated runs; output idempotent.

## Mutation test, re-run with proper exit codes

  SPECIFICITY_MAX -> 0            FAIL (exit 1)
  MIN_SIG_DIGITS -> 30            FAIL (exit 1)
  write-exclusion disabled        FAIL (exit 1)
  self-witness exclusion disabled PASS (exit 0)  <- CORRECT, not a gap

The fourth passes because with the self-witness counted the census is exactly 3
and `3 <= 3` still reads specific. The poisoning is LATENT: the tree is one such
artifact away from it firing. Recorded rather than tuned away.

## 2026-09-08: canonical ledger for the convention-C excision family is qou-wgta (the P0 excision tracker; owner-ruling milestone qou-cdx1, S2 science blocker qou-cds2); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 2 / §7.3 C3. Nine trackers, previously linked only cds2↔8iru and htsi→t9r1, now all point there.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

A consumer-side detector for deliberate convention-C control arms. Live and
now more load-bearing, not less: today's pass added SIX ledger adjudications,
so the population of declared control arms grew 137 -> 143 and the risk this
bean names -- a deliberate C object cited as though it were D -- grew with it.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-10-10 re-measure on `main` `ac111c1814`: the blast radius is down 29×

`computations/audits/consumer_control_arm_audit.py --selftest` **PASSES** on
`main` — the known positive is still detected, with the same five transcribed
weights. The detector is delivered. What moved is the population it scans:

| quantity | 2026-08-24 | 2026-10-10 | |
|---|---:|---:|---|
| witnesses scanned | 2938 | **3728** | corpus **+27 %** |
| carrying the `z_C` fingerprint | 36 | **14** | |
| carrying the muon-q0 fingerprint | 389 | **255** | |
| python files scanned | 3758 | **4937** | |
| ...naming a witness | 1854 | **2330** | |
| **foreign READ edges of convention-C witnesses** | **229 / 122 consumers** | **8 / 8** | **−29×** |
| foreign-transcription edges | 15 | **5** | |
| ...**CONTROL-ARM (≥1 specific value)** | **1** | **1** | unchanged |
| ...shared-constant only | 14 / 12 | **4 / 3** | |
| self-written pairs dropped | 371 | 232 | |

**This is genuine drain, not a denominator artifact** — and that distinction is
the whole value of re-running rather than quoting. The corpus *grew* 27 % over
the window while the C-fingerprinted witnesses fell 36 → 14 and the consumer
edges 229 → 8. A shrinking count against a growing denominator cannot be
explained by anything but the artifacts going away.

### What this does to the bean's open item

The bean's standing warning is *"the 229 is the blast radius; the 1 is what is
provable. The other 228 are `unmeasured`, NOT clear."* That warning is intact in
kind and transformed in scale: **7 unmeasured edges, not 228.** Hand verdicts on
228 edges is a tranche nobody was going to run; on 7 it is an afternoon. The
seven, verbatim from the run:

    [unmeasured ] deuteron_from_scratch_ledger.py          -> confinement-operator-selection.witness.json
    [unmeasured ] onepb_status_dashboard.py                -> confinement-operator-selection.witness.json
    [unmeasured ] probes/ep_decomposition_reachability_probe.py -> hadron-knot-table.witness.json
    [unmeasured ] audits/muon_pin_three_values_probe.py    -> qbeta/qbeta-ladder-required-phase.witness.json
    [unmeasured ] qbeta/qbeta_ladder_alpha_form_filter_probe.py -> qbeta/qbeta-ladder-required-phase.witness.json
    [unmeasured ] qbeta/qbeta_n1_constant_two_anchor_filter_probe.py -> qbeta/qbeta-ladder-required-phase.witness.json

    [TRANSCRIBES] audits/muon_pin_A_residual_surface_audit.py -> hadron-knot-table.witness.json
                  (shared-constant only -- NOT a control arm)

The single CONTROL ARM is unchanged: `h4_markov_weights_closed_form.py` reading
`alpha-k-jones-markov-h4.witness.json`, five specific weights, `frame CM`. The
2026-08-24 `frame_evidence` finding stands and is the thing a drain must still
respect — `z_C` IS in the consumer source (so a convention fix breaks it
**loudly**) while the muon pin is NOT (so a re-pin changes its numbers
**silently**).

### Two things worth noticing in the new list, neither of them the detector's doing

**`hadron-knot-table.witness.json` appears twice.** That is the file AGENTS.md
names as the corpus's **one remaining `Q0_FLIP`** — the single witness still
carrying the retired self-certified muon pin `1.1099785955573347…`. This audit
reaches it from a completely independent direction (consumer transcription, not
anchor stamping), which is corroboration rather than a new finding, but it does
mean two of the seven hand verdicts sit on an artifact that is independently
known to need a re-pin.

**A second `[TRANSCRIBES]` appeared where August had one.**
`muon_pin_A_residual_surface_audit.py` now transcribes out of
`hadron-knot-table.witness.json` — correctly classed *shared-constant only*, so
not a control arm. A muon-pin audit transcribing the muon pin is the expected
shape, not a defect; recorded so the next reader does not count it as a
regression from 1 to 2 control arms.

### Status

**Staying `todo`**, with the scope now tractable and explicitly named: 7 hand
verdicts, listed above. The detector half of the title is **delivered**
(selftest PASS on `main`, mutation-tested per the record above); the open half
is the drain-safety verdict on those 7. Nothing here is an open conjecture, so
13a is not what holds it open — the measurement simply has not been done.
