---
# qou-rx0r
title: 'Term 6 is structurally absent for A>=2: LaurentQ.from_sympy rejects every multi-nucleon residue'
status: todo
type: task
created_at: 2026-08-23T21:48:42Z
updated_at: 2026-08-23T21:48:42Z
---

`term6_residues_at_roots.py` computes the Term-6 Habiro residue at roots of
unity. It **succeeds for A=1** (proton, neutron) and **fails for every
multi-nucleon braid** — deuteron, tritium, helium-3, helium-4 — with

    ValueError: LaurentQ.from_sympy: non-Laurent factor
    -(1 - 1/q**4)*(q - 1)**2/12 + 1/2  in  (-q + 1/q)*(...)

and writes an `error` string into the witness where the value belongs.

## This is old, and it was hidden twice

`git log` on `term6-residues-at-roots.witness.json` (`e5d44bfb1`, 2026-08-21,
the q0 muon→proton re-pin sweep) shows the A≥2 rows were **already error rows
before that commit**. The re-pin changed the error text and the A=1 numbers,
nothing more.

It stayed invisible because both consumers swallowed it:

1. `term6_habiro_residue_mpfr_50dps_bridge.py` let an error row become the
   representative for its A and then indexed the missing key — `KeyError:
   'term6_at_q0_real'`. Fixed (156628c88): failed rows are now separated from
   canonical ones, and an A with no value gets a null row quoting the verbatim
   upstream error.
2. `paper_six_term_isotope_sweep._t6_by_A` reads `results_by_atom` at the TOP
   level while `WitnessBuilder` nests it under `data`, so its cache was empty
   and **every Term 6 in the sweep was 0** — a 5-term sum wearing a 6-term
   label. Handed to the sibling that owns that file.

## The load-bearing part

The previously committed `term6-habiro-residue-mpfr-50dps.witness.json`
carried A=2/3/4 values — 55.82 / −21375.48 / 692957.92 MeV — bridged from a
**pre-failure** upstream: recorded sha256 `299c86d8…`, computed 2026-05-05,
not reachable in a shallow clone. They are not reproducible from anything on
disk. Any downstream number that used them rests on an upstream state nobody
can re-derive.

## What is actually needed

A decision on `LaurentQ.from_sympy`. The rejected factor
`-(1 - 1/q**4)*(q - 1)**2/12 + 1/2` is a sum of a Laurent term and a rational
constant, so either

  (a) the caller is handing it an expression that has not been put over a
      common denominator / expanded into Laurent form, and the fix is at the
      call site; or
  (b) the residue genuinely leaves the Laurent ring for A≥2, and Term 6 is
      not defined by this route for multi-nucleon braids — in which case the
      6-term formula is structurally a 5-term formula above A=1 and that has
      to be stated, not patched.

These are very different conclusions and only (a) is a bug. Do not fill the
column to make it look complete: the null rows are currently honest.

Surfaced by the b1 producer repair on branch
`claude/mass-table-comprehensive-triage`.
