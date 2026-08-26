---
# qou-1oxx
title: 'Bar-parity pairs are frame-mismatched: chi at-q0 colour-weighted, at-qinv colour-blind'
status: todo
type: task
priority: normal
created_at: 2026-08-26T07:07:20Z
updated_at: 2026-08-26T07:07:56Z
---

Found 2026-08-26 while fully discharging `qou-cds4`'s witness line. Third
instance of one root pattern: a SIGN-based representation that cannot carry
the crossing coefficient `d` (cf. qou-qu2w, qou-iu3m).

## The mismatch

    chi-deuteron-h6-at-q0-50dps      colour-weighted-averaged-crossing  2026-08-10
    chi-deuteron-h6-at-qinv-50dps    averaged-crossings                 2026-07-18
    ... and identically for tritium-h9, helium-3-h9, helium-4-h12.

All FOUR pairs. The q0 side was regenerated colour-weighted and the qinv side
was left behind a month earlier.

## Why it matters: a live observable compares across frames

Seven live consumers reference the qinv witnesses, several of them bar-parity
/ conjugation probes whose entire job is to pair chi(q) against chi(1/q):

    bar_pairing_binding_observable.py          (docstring names both)
    probes/probe_d_barparity_binding.py:97-99  (loads one of each)
    probes/probe_d_delta_lambda_terms.py
    deltalambda/deuteron_conjugation_parity_categorical_probe.py
    deltalambda/deltalambda_conjugation_symmetric_excluded_probe.py

So the bar-parity observable is currently built from a colour-weighted q0 and
a colour-blind qinv. Bar-parity feeds Delta_lambda reasoning.

## It is NOT a label bug — the label is honest

`chi_at_q_inv_via_native_mpfr._word_to_signed` maps each crossing to a SIGN:

    |d| ~ 0        -> sgn = +1
    |d + h0| ~ 0   -> sgn = -1
    |d + h0/2| ~ 0  OR  |d + h0(1/2 - delta/4)| ~ 0  -> sgn = 0

Both averaged variants land on sgn=0. The in-file comment records that the
colour-weighted one "used to hit the raise below" and was added as an accepted
case (bean qou-gdtb) — i.e. made not to CRASH, not made REPRESENTABLE. It even
imports `_pn_delta()` solely to RECOGNISE the weighted crossing and then
discard the distinction.

Note `run_atom` calls `atom_braid_word_3A(Z, N)` — the CANONICAL default — so
the word going in is colour-weighted and the representation throws the
weighting away. The witness's "averaged-crossings" label is therefore accurate
about the value.

## Severity, bounded

That path has THREE channels, so it DOES distinguish averaged from plain
sigma. It collapses only the two AVERAGED variants. The error is the
colour-weighting delta — 0.0141 % per p-n interface — NOT the 17 % plain-sigma
collapse of qou-qu2w. Real and structural, but small.

## Fix shape

Needs a d-preserving qinv path, mirroring the qou-qu2w fix (which re-pointed
at `chi_monotone_transfer.chi_all_lambda`). Not done inline because it moves
bar-parity numbers that feed Delta_lambda, and because the qinv path currently
routes through `pyhecke_native`, so the substitute has to be chosen rather than
assumed.

Cheap first step for whoever takes it: confirm by MEASUREMENT, as with the
chi-*-at-q0 oracles — recompute one qinv witness under both averaged variants
and check whether the committed value matches the blind one. If it does, the
diagnosis above is confirmed end-to-end rather than read off the source.
