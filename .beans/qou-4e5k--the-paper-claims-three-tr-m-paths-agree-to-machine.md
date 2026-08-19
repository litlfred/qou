---
# qou-4e5k
title: The paper claims three tr_M paths agree to machine epsilon; two committed witnesses disagree at 1.4e-4 on the deuteron
status: todo
type: bug
created_at: 2026-08-19T21:29:48Z
updated_at: 2026-08-19T21:29:48Z
---

Found while regenerating the qou-mass vendor mirror (`qou-wpp2`): the mirrored
witness moved 99 lines, which sent me to compare it against its siblings.

## The published claim

`content/quantum-observable-universe/mass-endomorphism/recomputed-low-isotope-mass-table.md:3`

  "three independent production paths to the Markov trace tr_M(B_K) at q = q_0
   **agree to machine epsilon** across the proton, neutron, deuteron, tritium,
   and 3He."

## Measured on origin/main 5b158ef06c, 2026-08-19

Two committed witnesses, both dated 2026-08-15, both declaring 50 dps, on the
same object:

    atom   atomic-tr-m-mpfr-50dps      low-isotope-mass-table      relative
    p      1.145759692457300869689     1.145759782287835504726     +7.84e-08
    n      0.987743688115809571634     0.987743756687661111334     +6.94e-08
    D      0.575172243917771870827     0.575090958682446712092     -1.41e-04

Machine epsilon at 50 dps is ~1e-50. The framework's own L1 target is 1 ppQ
(1e-15). The deuteron gap is **35 orders of magnitude** above the stated
agreement and **11 orders** above the L1 target.

## The deuteron gap is exactly the colour weighting

Feeding each witness its OWN p and n into `closed_form_tau_M(1,1,q0,tau_p,tau_n)`
so the only free variable is the p-n convention:

    atomic-tr-m-mpfr-50dps  D  ==  bring_color_weighted   to  6.0e-25   <== exact
                               vs strict_averaged             1.41e-04
                               vs chi_lambda_braid            1.71e-01

    low-isotope-mass-table  D  vs bring_color_weighted        1.41e-04
                               ==  strict_averaged      to    3.5e-09
                               vs chi_lambda_braid            1.71e-01

So `atomic-tr-m-mpfr-50dps` reproduces the canonical colour-weighted closed form
to 25 digits. The mass-table pair does not — it is 1.41e-4 away, which is the
per-bond weighted/averaged ratio (`+1.414947e-04`, independently computed) to
within 0.12%.

## The producer declares the weighting it does not appear to apply

`canonical_mass_table_extended.py` (which `low_isotope_mass_table.py` is a thin
subprocess wrapper over, so both witnesses come from it) contains **zero**
occurrences of `pn_convention`. Its own docstring says:

  "Composites (A >= 2) need the operator-valued `branching` combiner for the
   **color-weighted p-n interface** ... it linearity-splits sigma - h(1/2-d/4)*1
   into a sign-0 averaged term plus an identity term"

Declared behaviour and emitted number disagree. This is the shape the owner-ruling
audit flagged as a **convention hybrid** (`borromean_binding_recompute.py:98` --
"its own docstring DECLARES convention D ... Binding = tau(D) x bonds(C)").

Neither witness records a `pn_convention` parameter at all, so nothing downstream
can tell which frame it is reading. That is the lesson of `45789ddfa0`
(`convention_fingerprint`) unlearned one directory over.

## What I did NOT establish -- do not read past this

1. **Which one is right.** I have not shown that `closed_form_tau_M`'s
   `bring_color_weighted` and the branching combiner's weighting are the same
   object. The mass-table value is 3.5e-9 from `strict_averaged` -- close, but
   3.5e-9 is not 1e-50, so it is not simply "strict_averaged computed another
   way" either. It is near neither exactly.
2. **The free-nucleon gap has a different cause.** p and n have no p-n bond, so
   their 7.8e-8 / 6.9e-8 disagreement cannot be the colour weighting. Unexplained.
3. **Whether any cross-method check covers this pair.** If one exists and is
   green, that is a detector-blindness instance and belongs in the taxonomy.

## Where it belongs

`docs/audits/2026-08-15-detector-blindness-taxonomy.md` row 8 -- *"each entry
independently (R9) / entries disagreeing with each other"* -- names
`pyhecke.gram` as its example. This is a second instance of that class, in the
production mass table, and it reaches a published sentence.

Related: `qou-cds4` (S4, p/n convention) owns the convention question but is
scoped to `pn_convention` **assignment sites**; this producer has none, so S4's
grep does not see it.

## Next step

Decide which frame the canonical mass table should be in (S4 / ruling R3 say
`bring_color_weighted`), then either fix the producer or correct the content
block -- but **not** by relaxing the claim to fit the numbers. Whichever way it
lands, both witnesses must start recording their `pn_convention`.
