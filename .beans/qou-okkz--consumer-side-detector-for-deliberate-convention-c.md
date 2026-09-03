---
# qou-okkz
title: Consumer-side detector for deliberate convention-C control arms (qou-q0zk drain safety)
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T14:10:58Z
updated_at: 2026-08-24T15:06:42Z
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
