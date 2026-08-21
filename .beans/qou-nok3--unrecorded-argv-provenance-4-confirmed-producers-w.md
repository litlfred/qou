---
# qou-nok3
title: 'Unrecorded argv provenance: 4 confirmed producers whose flag changes the payload'
status: todo
type: task
priority: normal
created_at: 2026-08-21T23:15:31Z
updated_at: 2026-08-21T23:16:17Z
---

## The class

`provenance.rs` records, for the Rust binaries: *"The parameters were not
recorded at all ... none of them wrote it down."* The same holds on the
Python side, and it is not theoretical -- it was found by walking into it.

**Worked case, measured (not inferred).** `whitehead_c0_mpmath.py` gates its
N=12 data point behind an opt-in flag:

    EXTEND_N12 = "--n12" in sys.argv        # line 47

The committed `whitehead-c0-mpmath.witness.json` CONTAINS N=12, so it was
generated with `--n12`, and nothing in the witness says so. Re-running it the
obvious way silently drops the point:

    committed   "10": 7062.35924065477,  "12": 29287.27767465885
    plain re-run "10": 7062.35924065477
    factor       1.9678009716166576  ->  1.8973391741766672     (3.6%)

The verdict ("nearest prediction: FACTOR 2; excludes factor 1 & 4") survives,
but by luck rather than by design. I nearly committed that as a precision fix.

## Scan: 4 confirmed, 6 to triage, 11 benign

Producers with argv-gated behaviour that emit a COMMITTED witness which does
not record the flag:

**AFFECTS PAYLOAD (4)** -- the flag's `if` body does more than return/exit:

    computations/whitehead_c0_mpmath.py                  --n12        (MEASURED)
    computations/em_linking_cusp_geometry_probe.py       --live
    computations/he4_link_volume_braid_closure.py        --live
    computations/probes/borromean_nz_adjoint_torsion.py  --recompute

**INLINE, unclassified (6)** -- flag tested inline, needs manual reading:

    computations/whitehead_c0_tower.py                    --hi
    computations/whitehead_recurrence_hunt_fast.py        --nmax
    computations/whitehead_diagonal_recurrence_hunt.py    --nmax
    computations/takata_fig8_recurrence_hunt.py           --nmax
    computations/derived_chi_catalogue_matrix_m_mpfr.py   --use-mu-n-blocks
    computations/probes/borromean_cusp_framing_factor.py  --recompute

**EXIT-CODE ONLY (11), benign** -- all `--strict` on `computations/audits/*`,
where the flag only selects the return code and the payload is identical.
These are NOT defects and must not be counted as such.

## Two heuristics over-flagged before the AST one worked

Recording this because the wrong number was nearly the reported one:

1. *"Producer has argv-gated behaviour + committed witness lacking the flag"*
   -> **21**. Counts the 11 benign `--strict` audits.
2. *"Variable is used on a line without `return`"* -> also flagged the
   `--strict` set, because it matched the variable name inside DOCSTRINGS and
   because `if strict and X: return 1` has the `return` on a different line
   from the test. `stale_probe_audit.py`'s own docstring says
   *"With --strict, exits non-zero ... Without --strict, returns 0 and reports
   the breakdown"* -- i.e. the file states it is exit-code only, and the
   heuristic flagged it anyway.
3. AST: find `If` nodes testing the flag variable, check whether every
   statement in the body is Return/Raise/Pass/sys.exit -> **4 payload,
   11 exit-only, 6 inline**. Defensible.

Same lesson as the hyperbolic-volume audit in bean `qou-ckbv`: a
high-recall grep over "has the feature" is not a defect count, and the
separation has to be mechanical rather than assumed.

## Fix shape (not yet applied)

For each of the 4: record the invocation in the witness. `Generation` in
`tools/hecke-engine/src/provenance.rs` already does exactly this on the Rust
side -- it stores raw `argv` plus a ready-to-run `reproduce` string, and its
design note argues for argv over modelled per-flag fields precisely because
modelling silently drops what it does not know. The Python `WitnessBuilder`
should carry the same.

That is a `WitnessBuilder` change plus 4 regenerations, and the regenerations
must be done WITH the flags their committed witnesses imply, or they lose
data -- as demonstrated above.

## Standing rule this yields

**Before regenerating any witness, check its producer for argv-gated
behaviour, because the witness will not tell you.** Diffing the regenerated
output against the committed one is not sufficient either -- the difference
looks like ordinary drift.
