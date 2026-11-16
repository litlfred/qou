---
# qou-efqx
title: 'GAP: the gamma-gamma character exclusion does not reach the colour-weighted letter (four-letter alphabet)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T11:46:21Z
updated_at: 2026-10-04T15:20:25Z
parent: qou-10v9
---

Child of `qou-99qc`, sibling of `qou-cblw`. Opened by PR #7295 rather than
papered over, per AGENTS.md §13 ("if you cannot close a derivation, CREATE A
BEAN").

## What IS closed (#7295, do not redo)

The alternating character `sigma_i |-> -1/q` is a 1-dim rep of `H_3(q)`, so a
word's character is a product of scalars and depends only on the MULTISET of
its letter shifts -- not the order, not the generator assignment. Over the
three-shift alphabet the census actually uses,

    altChar(w) = (-1)^(a+b+c) q^(b-a-c) ((q^2+1)/2)^c
               = 1  <=>  c = 0 and a = b

because `q^2+1` is irreducible over Q and coprime to `q`. Every corpus nucleon
carries `c = 2`, so no reading and no re-ordering is a gamma-gamma word.
Lean: `QOU.Mass.AltCharShiftMultiset` (sorry-free, `lean`-direct exit 0).

## What is OPEN, and why the argument stops

`word_to_mpfr` recognises a FOURTH crossing template, `averaged_weighted`:

    delta(q) = (q-1)^2 (1 - q^-4) / 3          [flavor_split_leading, exact]
    d_cw     = -h (1/2 - delta/4)
    altChar  = (q^2+1)(q^6 - 2q^5 - 7q^4 + 4q^3 - q^2 - 2q + 1) / (12 q^5)

That numerator carries an **irreducible sextic**, so the character is NOT of
the form `+/- q^k` or `+/- ((q^2+1)/2)^c` and the unique-factorisation argument
that closes the three-letter case **has no analogue**. `ud_mul_ne_one`'s finite
case analysis likewise has none.

**Why this matters rather than being a curiosity:** the 2026-08-15 owner ruling
R3 makes `bring_color_weighted` canonical as the p/n convention. No census
reading uses the fourth template today, so nothing in #7295 is weakened -- but a
word the corpus builds NEXT, under the canonical convention, sits exactly in
this gap.

## What IS measured (the pin-level fact, not the general one)

None of the 7 colour-weighted pairings over the four-letter alphabet equals 1
at `q_0`. They reach 1 only at

    q ~ 0.398656, 0.462828, 0.503932, 0.564995,
        2.668466, 3.235960, 3.458099, 4.139416    (plus the trivial q = 1)

nearest 0.564995 against `q_0 = 1.1099785828`. Probe assertions
`no_colour_weighted_pairing_equals_one_at_the_substrate_pin` and
`colour_weighted_character_is_outside_the_monomial_family`, in
`computations/qbeta/qbeta_altchar_is_a_shift_multiset_invariant_probe.py`.

**A pairwise fact is not a word-level fact.** A product of many letters can be
1 with no pair equal to 1, so the pin-level measurement does not close the
general statement even at `q_0`.

## What would close it

Either (a) a valuation/irreducibility argument on
`Z[q, q^-1, (q^2+1), sextic]` showing no monomial in the four letter characters
is 1 for `q > 1`; or (b) a bounded exponent-sweep with a stated bound, of the
`qou-avt6` shape (which swept `m in [-14,14]`, `c in [0,9]`) extended to the
fourth exponent; or (c) a demonstration that the canonical colour-weighted word
does not in fact use that letter, which would make the gap vacuous.

(b) is cheapest and is what I would do first, but it gives a BOUNDED result and
must say so -- `qou-avt6` was careful about exactly that and this bean should be
too.

## Not covered by #7295 either, and separate from this

`blocks AS STATED` -- the sixth census Delta family. The census probe
deliberately does not construct it (the properties blocks give the typed shifts
but never say which generator each quark crossing sits on, which is why the 16
`blocks CONSTRUCTED` readings are enumerated in its place). There is no word and
no vector to test, so it is an authoring gap rather than a mathematical one.

### Progress Update (2026-11-16, PR #8179)
- Formalized the fourth (`averaged_weighted`) letter character `altCharCw` and `flavorSplitLeading` in `QOU/Mass/AltCharShiftMultiset.lean`, proving `altCharCw_sextic_closed_form`, `altCharCw_sub_ud`, `uu_sub_altCharCw`, and `altCharCw_strict_sandwich` (`letterChar q .ud < altCharCw q < letterChar q .uu < 0` on $1 < q$ with $0 < \delta(q) < 2$, `0` `sorry`).
- Verified at 80 dps at $q_0$ in `computations/probes/tail_d6_lp_dual_altchar_vlevel_probe.py`.
- Opened PR `litlfred/qou#8179` (`bf3902040cf206123f8aa0b5dc2b79c176dd9ce1`). Keeping status `in-progress` pending owner review.
