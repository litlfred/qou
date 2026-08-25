---
# qou-wlaf
title: 'STALE: gram-norm-binding-probe.witness.json on main fails its own cross-check assertion by 7 orders of magnitude'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T16:43:22Z
updated_at: 2026-08-25T16:43:58Z
---

MEASURED 2026-08-25, branch `claude/gram-norm-threshold-investigation-v8ck94`.

## What is stale

`computations/probes/gram-norm-binding-probe.witness.json` as committed on
`main` does not reproduce from today's code, and it is wrong by far more than a
rounding difference. Against the independent 50-dps transfer engine
`tr_m_atom_via_transfer.tr_m_atom_zn` — which is the very cross-check the probe
itself asserts on:

    iso    field      engine (50 dps)   committed witness   rel err
    2H     tr_atom      0.5751722439      0.3883571887       3.25e-01
    2H     tr_free      1.1317169043      0.9835261820       1.31e-01
    3H     tr_atom      0.2293101021      0.1040710693       5.46e-01
    3H     tr_free      1.1178462290      0.9080241198       1.88e-01
    3He    tr_atom      0.4037670369      0.2065784751       4.88e-01
    3He    tr_free      1.2966756122      1.0477565676       1.92e-01

Everything derived from those moves with them: `G_atom`/`G_free` 5-12 %,
`B_sym` ~27-28 %, `B_gram` up to 49 %, `R_abs`/`R_signed` 6-33 %.

## It fails its OWN assertion, which is what makes this unambiguous

The committed witness records

    linear_trace_matches_transfer_engine   computed = 5.77e-15   tol = 1e-8   passed

so the cross-check held when the file was written. Recomputing that same
assertion against the committed numbers today gives **3.2e-01** — seven orders
of magnitude outside the witness's own stated tolerance. This is not a judgement
call about staleness heuristics; the artifact contradicts itself.

## Not caused by the float64 coercion committed on this branch

The `_letters` float64 coercion (see `qou-9ohz`) was verified at ²H to agree
with the object-dtype path to **9e-16** relative — the float64 floor. It cannot
produce a 5-100 % move. The freshly recomputed values agree with the 50-dps
engine to ~1e-9 and the probe's assertions pass.

## Probable cause, and the part that is NOT established

The committed witness records `wall_sec` of **0.71 s for ³H** — matching the
module docstring's "A <= 3 (n <= 9, instant)" and matching the 0.5 s measured
after the coercion fix. A session on 2026-08-24/25 measured **>2131 s** for that
same isotope on unmodified code. So between the witness being written and now,
`atom_braid_word_3A` began emitting `mpmath.mpf` coefficients — which is correct
for the word under the NO-FLOAT64 discipline, and which simultaneously (a) moved
these numbers and (b) turned this probe's matmuls into object dtype (1.8e4x).
One upstream change, both effects.

**Not established:** exactly which commit did it. Agent clones here are shallow
— `git log` on `mass_at_3A_proper.py`, `wedderburn_jones_markov.py` and the
witness all return only the single merge `fed69b1c4`, so the drift cannot be
dated from this checkout. Do not assert a commit without fetching real history.

## Done on this branch

Witness regenerated (all four isotopes, `--with-4he`) under the fixed probe.
Both assertions pass: `linear_trace_matches_transfer_engine` = 6.03e-15 against
a 1e-8 tolerance, and reversal invariance 5.17e-16 against 1e-10.

Wall times, regenerated vs committed: ²H 0.02 / 0.01, ³H **0.45 / 0.71**,
³He 0.42 / 0.62, ⁴He **418 / 1169** s.

**Raw-float64 field count is 248, i.e. FLAT against the 248 in the baseline —
it does not drain.** (An earlier note of mine said "248 -> 148, drains"; that
148 was a three-isotope run without `--with-4he` and comparing it to the
four-isotope baseline was not a like-for-like comparison. Corrected here.) The
repo ratchet reports `REGRESSED (count increased): 0`, so this change is
ratchet-neutral, not ratchet-draining. Draining it would mean carrying `mpf`
through serialization, which this probe cannot do while its seminormal operand
is float64 — the same open item as above.

## What this bean is still for

The sibling question nobody has answered: **which other witnesses were produced
by consumers of `atom_braid_word_3A` before it was mpf-ified, and are therefore
stale in the same way?** The generic staleness triage keys on `scriptHash` of
the producer, and this class is invisible to it — the producer file is unchanged;
a *dependency* changed. That is the import-cone drift case AGENTS.md flags as
"the one that actually bites". The count is unmeasured. Do not assume it is 1.
