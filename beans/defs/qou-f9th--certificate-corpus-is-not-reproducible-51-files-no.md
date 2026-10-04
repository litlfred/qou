---
# qou-f9th
title: 'RETRACTED: certificates ARE reproducible (f64 = eval/2^pn_count); repair script ready'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T04:05:44Z
updated_at: 2026-10-04T15:24:09Z
---


## ⚠️ RETRACTED 2026-08-15 — the certificates ARE reproducible

**Everything below the retraction line was wrong, and this bean's original
title ("closed question, do not retry") is exactly the scope-(b)
over-narrowing AGENTS.md forbids.** I turned a failed probe into a
structural exclusion and told the next agent not to look. Reopened.

### What is actually true

* **The 2-adic denominator is exactly `2^pn_count`** — an integer power of
  two, matching `pn_count`, on all 9 certificates whose f64 still has >=8
  valid digits (3,4,6,6,5,12,6,10,16). `pn_count` is IN the file. My original
  hunch was right; I abandoned it one step early.
* **The non-integer ratios are CATASTROPHIC CANCELLATION**, not a dropped
  `mid_strip_threshold`. The sums are ill-conditioned to log10(cond) = **359**
  (60Co), 187 (40Ar), 142 (40Ca). My headline evidence for the threshold story
  — 11Li at "13.35 against 24" — is a number with ~0 valid digits. There was
  never evidence for that story.
* **Agreement tracks conditioning exactly**, which confirms both mechanisms:
  2-3 valid digits -> reproduces to 1e-3; -1 -> 0.5-1.9; -5 -> 1.0.

### Corrections to the retraction itself (review, 2026-08-15)

The retraction was right about the mechanism and wrong about three numbers.

* **"log10(cond) = 203" is reproducible from nothing.** True value 359.2; the
  script reported 52 because `conditioning()` measured the cancellation at the
  precision the cancellation had already exhausted. A diagnostic cannot run at
  the precision it is diagnosing. Fixed: precision is now chosen per file from
  a high-precision scratch pass.
* **"15/35 retain ZERO valid digits" is wrong for the one file it matters
  most for.** v9 falls back to MPFR (`v9.rs:838`) when the normalised f64 eval
  overflows, and those certificates have ACCURATE committed values. Measured:
  exactly one took that path — 60Co, also the worst-conditioned. The repair
  script would have overwritten the best data in the set with `-inf`.
* **"35 re-anchorable, 0 flagged" asserted a check that never ran.** The
  `--max-rel` guard was dead code: `max_rel` was never read inside
  `process()` and no path returned `FLAG`, so `flagged: 0` was structurally
  guaranteed. The guard is deleted rather than repaired — its premise (compare
  against the committed value) was comparing against noise.

Current, from a run: **22 re-anchorable, 12 blocked, 1 keep, 16 skipped.**
The 12 blocked carry a `tr_markov_f64` with no exact source (`tr_markov_cleared`
exists in ONE certificate), so writing the other fields would leave a file
straddling two anchors. `--write` stays disabled — not for defects now, but
because rewriting committed published data is an owner call.

### Lesson

I inferred a mechanism (term-dropping) instead of measuring one, then wrote
it into a durable artifact as settled. The measurement that would have caught
it — conditioning of the sum — took one command. Then I wrote the *correction*
with three unmeasured numbers in it, which is the same failure one level up.

---

## SUPERSEDED — original entry follows

> **FALSE. Struck, not deleted, so the error stays visible.** Everything in
> this section is withdrawn — see the retraction above. It is reproduced only
> as a record of what was claimed.

~~The 51 `tools/hecke-engine/certificate-*.json` **cannot be regenerated or
corrected from what is committed.** Do not attempt it; anyone who "fixes"
them is fabricating numbers. Recorded here because it looks like an
obviously-doable chore and is not.~~

The imperative above survived the first retraction as running prose under a
"SUPERSEDED" heading. A reader skimming for the answer would have found a
direct instruction not to look, with nothing in the sentence itself marking it
as withdrawn — a heading does not neutralise an imperative underneath it.
Struck inline for that reason.

### Three independent blockers

1. **Four different generators, different schemas.**

       35  hecke-bigint (v9)   <- exact symbolic Laurent terms + parity
        8  hecke-modular 0.11.0
        7  hecke-crt 0.10.1
        1  hecke-crt 0.10.0

   Re-running the wrong one downgrades exact rational data to an f64
   summary. Measured: a `hecke-crt` re-run of 10B emitted
   `f_pauli_f64: 0.0` and dropped 4188 lines of exact terms.

2. **Cutoff parameters never recorded.** 10He records
   `elapsed_seconds = 0.0187`; the same isotope at `hecke-crt`'s default
   threshold does not finish in 120 s in a RELEASE build (>6000x).

3. **Even the exact data cannot be re-anchored.** The obvious safe path —
   re-evaluate each file's own stored polynomial at the right q0 — was
   built and FAILED on all 35:
   * unrecorded 2-adic denominator (`2^(pn - v2)`); where log2(ratio) hits
     `pn_count` that is the whole gap (10B 24.998 vs 25; 11C 29.994 vs 30)
   * **non-integer** log2 elsewhere (10He 14.91 vs 16; 11Li 13.35 vs 24),
     which cannot be a 2-adic factor — `mid_strip_threshold` dropped terms
     during accumulation and was never recorded, so which terms survived is
     unknowable.

   Diagnostic retained: `tools/hecke-engine/scripts/reanchor_certificates.py`
   (`--write` disabled — there is no correct value to write).

### Also: a 1277 ppb anchor, now fixed forward

`hecke-bigint` evaluated at `q0 = 1.10998` (5 significant digits) — 111x the
muon/proton gap. Every `*_f64` in those 35 carries it. The exact symbolic
terms do NOT (they are exact in q). Fixed to `gram::Q_0` for future runs.

### What IS actionable

Nothing on the existing files. Going forward, `crate::provenance::Generation`
records binary + argv + reproduce + q0 + q0_pin on every new certificate, so
this class cannot recur. If the corpus is ever genuinely needed at the proton
pin, the answer is a fresh full run with the parameters chosen and recorded —
a new campaign, not a migration.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [B] RETRACTED: certificates are reproducible; repair script ready - finish or close
