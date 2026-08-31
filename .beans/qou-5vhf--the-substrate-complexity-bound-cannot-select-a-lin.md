---
# qou-5vhf
title: The substrate complexity bound cannot select a link — n_braid is a readout, and the slack grows with A
status: completed
type: task
priority: normal
created_at: 2026-08-31T03:00:48Z
updated_at: 2026-08-31T03:11:11Z
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


## Follow-on 2026-08-31 — the gate figure I named is convention-C-stale

Having named the r5full anchor non-confirmation as the remaining route, I
checked its own number. `tr_M(2H) ~ 0.388` is **convention C**. Convention D
is canonical (owner ruling 2026-08-15) and PR #6318, merged the same day,
regenerated the table from its producers at the proton pin:
`0.3882864240747888 -> 0.5751722439177719` (**+48.13 %**). Re-verified live:
`binding_canonical(1,1)` gives `tr_M_atom = 0.575172243917772`.

**Verdict unchanged.** Against `J_{6_2}(q0) ~ 1.027` the atom trace is
62.19 % low under C and 43.99 % low under D. Neither matches, so the gate is
still live and still the right target.

**Not established:** that the comparison is convention-clean. `tr_M` depends
on `z`, and whether `1.027` was computed in the same frame has NOT been
checked. Read the pair as a scope-(a) non-match, not a quantified gap.

Scoped in both audits that carry it (`2026-07-04-he4-vol4-gated-on-r5full`,
`2026-07-13-atom-knot-rule-a5plus-constraints` §5-bis).

## Two near-errors, both caught by reading the cited artifact

1. I read AGENTS.md's `0.388 -> 0.575` note as proof the gate figure was
   stale. **The gate cites `atom-nf-symbolic-D.witness.json` — the
   GS-symbolic route, a DIFFERENT producer from `binding_canonical`** — and
   that witness still reads `0.3882864717176122`. Nearly reported a
   producer confusion as a staleness finding.
2. I then read the two values as a live disagreement between routes and was
   about to flag it to the sibling. #6318 had settled it hours earlier as
   the C->D migration, and was already merged.

Both were caught by opening the artifact the audit cites instead of trusting
a summary of it — including AGENTS.md's own summary, which is accurate about
`binding_canonical` and says nothing about the GS route.
