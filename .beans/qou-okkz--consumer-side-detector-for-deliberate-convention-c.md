---
# qou-okkz
title: Consumer-side detector for deliberate convention-C control arms (qou-q0zk drain safety)
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T14:10:58Z
updated_at: 2026-08-24T14:55:03Z
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
