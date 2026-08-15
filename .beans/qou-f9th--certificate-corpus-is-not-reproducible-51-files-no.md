---
# qou-f9th
title: 'Certificate corpus is not reproducible: 51 files, no recoverable generator params'
status: todo
type: task
created_at: 2026-08-15T04:05:44Z
updated_at: 2026-08-15T04:05:44Z
---


## Established by PR #5082 — this is a CLOSED question, not an open task

The 51 `tools/hecke-engine/certificate-*.json` **cannot be regenerated or
corrected from what is committed.** Do not attempt it; anyone who "fixes"
them is fabricating numbers. Recorded here because it looks like an
obviously-doable chore and is not.

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
