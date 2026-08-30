---
# qou-nsih
title: 'OWNER-AUTHORIZED SWEEP: excise convention C in python AND rust, everywhere'
status: todo
type: task
priority: normal
created_at: 2026-08-30T06:53:56Z
updated_at: 2026-08-30T08:05:06Z
---

## Measured 2026-08-30 — the surface, before any edit

Owner instruction, verbatim: *"Excise convention C in python and rust and
wherever you see it."* That supersedes the standing caution in AGENTS.md
against launching a corpus-wide sweep off the recorded counts — but the counts
below are freshly measured, not quoted.

### Python — 93 blocking sites

`scripts/convention-c-value-audit.py` (the VALUE audit, which evaluates each
binding at two sample points rather than matching its shape, so it sees the
sqrt-variable disguise the shape audit is blind to):

    BLOCKING — confirmed convention C, unadjudicated   93
    ADJUDICATED as comparisons (ledger)                 1
    UNRESOLVED — variable name not recognised           2
    NOT C — 1/[2]_q on a q-variable                      3

The 2 unresolved are real C in a spelling the audit cannot name:
  - computations/probes/toffoli_qand_convention_d_derivation.py:185  (var `_s`)
  - computations/qbeta/qbeta_braid_image_eigenphase_exclusion_probe.py:134 (`ss`)

The 3 "NOT C" are 1/[2]_q on a q-variable — correctly excluded, do not touch.

### Rust — essentially already D

  tools/hecke-engine/src/main.rs:82        z: q*q*q/(q*q+1.0)   -> D
  tools/hecke-engine/src/bin/h9_beta.rs:76 z: q*q*q/(q*q+1.0)   -> D
  tools/hecke-engine/src/archive/v2.rs:205 z: 1/(sqrt q+sqrt qi) -> **C**, in archive/

One C site, and it is in `archive/`. All language bindings
(hecke-engine-{c,node,jvm,julia,gap,octave}) are clean; the Octave one is
explicitly labelled `// z = q^3 / (q^2 + 1), trace convention D`.

### Discipline for the sweep

Per AGENTS.md's own record of how this has gone wrong before: migrate
site-by-site, never by relabelling a manifest; NEVER touch an anchor-defining
witness; a producer that holds C as a DELIBERATE comparison stays (the ledger
has 1 such); and re-run the value audit rather than the shape audit to check
progress — the shape audit reported 26 where the value audit reports 93, and
21 of those were invisible to it entirely.

## 2026-08-30 — CORRECTION: 'INERT' does NOT mean safe to migrate, and there are ZERO measured-safe targets

I reported the 2 INERT sites as 'the safest migration targets, the only ones
where I have positive evidence that nothing moves'. **That was wrong twice.**

### 1. qbeta_utils.py:248 — the verdict is a HARNESS ARTIFACT

The module has **no `__main__`**. Running it standalone executes imports and
nothing else, so 'output identical' measured precisely nothing. It has **82
importers**. This is the measuring-my-own-harness failure for the third time
this session.

And the site must not be migrated on its merits either: it sits inside
`if convention == 'C':` — reachable only by asking for C by name — and carries
a documented bit-exactness reason for its exact spelling:

    the two spellings are algebraically equal but NOT bit-equal --
    1/(sqrt q + 1/sqrt q) against sqrt(q)/(1+q) differ by 1.6e-61 relative at
    60 dps -- and this is the one ladder that must not be perturbed by a
    substitution, however small

### 2. qbeta_phase_bar_parity_completeness_probe.py:105 — verdict REAL, reading wrong

Hand-verified: output is byte-identical under substitution. But that is not
evidence the migration is safe. `z_C` feeds `a_C`, which the file's own
docstring contrasts against `a_D_odd`; it IS a comparison arm whose contrast
the printed output happens not to expose.

### The general correction

**INERT means 'this probe's own output cannot detect the substitution', NOT
'the substitution is harmless.'** So the count of measured-safe migration
targets is **0, not 2**.

Note the ASYMMETRY, which does hold: COMPARISON_ARM is a POSITIVE detection --
assertions actually flipped -- so those 23 adjudications stand. It is the
NEGATIVE verdicts (INERT, and by the same argument DISCRIMINATES) that carry no
safety guarantee. A harness like this can confirm load-bearing; it cannot
certify harmless.

### What the INERT signal DID find

Chasing why the output could not move surfaced a real defect in that probe --
two assertions that cannot fail. Filed separately.
