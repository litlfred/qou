---
# qou-5vhf
title: The substrate complexity bound cannot select a link — n_braid is a readout, and the slack grows with A
status: completed
type: task
priority: normal
created_at: 2026-08-31T03:00:48Z
updated_at: 2026-08-31T03:01:24Z
---

Answers the open question `docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md`
closed on: *"the registry already asserts `n_braid: 3`, `n_0: 6` -- check
whether that is derived or also handed over."*  PR #6327.

## Why this bean exists rather than an A>4 assignment

The obvious form of "extend the nucleus->link map past A=4" is a fit. The
A<=4 assignments are an admitted AME-driven census search (`jsj_verification.py`
keeps volumes near `B_AME/(rho*m_e)`), and the 2026-07-13 C1-C9 table already
excludes the constructed alternatives at A>=5 from the other side. So the only
non-fitting move was to ask whether the substrate supplies the restriction that
gives the existing match its apparent selectivity (0 better matches inside the
tabulated links vs 796 without).

## Result -- two parts, opposite signs

**n_0 = 3A IS derived**, and is measured rather than assumed: the canonical atom
word's max generator index is exactly 3A-2 on all eight isotopes tested, so it
uses all 3A strands and no more.

**n_braid is NOT derived.** It equals 1 + max|generator| of the ASSIGNED knot's
own SnapPy braid word -- 6_2 -> 3, 8_11 -> 5, L6a4 -> 3, all three exact. It is
computed FROM the chosen knot, so it is downstream of the assignment and cannot
restrict it. Using it as a selection class is CIRCULAR, not merely underived.
That is stronger than the audit's own conjecture, which allowed for "handed
over" as the worse case.

**The derived bound is too loose and its slack GROWS.** Exact integer word laws:
total = 12A-1, genuine braid letters = 10A-2, superpositions = 2A+1, strands
= 3A. So crossings <= 10A-2, braid index <= 3A. Slack against the assigned
knots: 12/20/22 crossings and 3/4/6 index, rising linearly.

## Consequence

A census search at higher A is FREER than at A=2, never tighter. The A=2 search
is already 796-fold degenerate once the underived low-crossing restriction is
dropped, so no A>=5 census assignment can be better supported than the
deuteron's.

## Lean (sorry-free, lean-direct exit 0, axiom-clean on all six)

`QOU/Mass/SubstrateComplexityBoundMonotone.lean` -- both bounds strictly
increase; `admissible_mono` (a link admissible at A is admissible at every
larger A, so the class is a strictly increasing chain); `not_selective` (two
distinct links admissible at every A >= 1); `slack_unbounded`.

## Scope

**(a)** for the census route. Does NOT refute a derived nucleus->link map --
it says the map cannot be recovered by volume-matching inside the class the
substrate actually cuts out.

## What is still open, and what I would NOT do

Still open: a nucleus->link map derived from something other than volume
proximity. The corpus's own candidate is the R5-full categorical SDP
(`conj:canonical-knot-id-sdp`, #604) -- GS normal form + Markov trace of the
atom Hecke element in H_{3A}. It is blocked on VALIDITY, not scale: it does not
confirm its own A<=3 anchors (tr_M(2H) ~ 0.388 vs J_{6_2}(q0) ~ 1.027), so
running it at H_18 first would produce IDs with no more standing than the
volume matches it would replace.

Would NOT do: run the census search at A=5..16. It is a fitted parameter per
nucleus with zero out-of-sample support, and this bean is the measurement
showing it cannot become evidential.

## Error caught by the probe before it landed

I asserted "stored braid word length == crossing number". True for 6_2 and
L6a4 (both 6), FALSE for 8_11 (14-letter word, c = 8). Braid word length is an
upper bound on crossing number, never an identity. Fixed at the assertion.
