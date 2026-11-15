---
# qou-5vhf
title: The substrate complexity bound cannot select a link — n_braid is a readout, and the slack grows with A
status: completed
type: task
priority: normal
created_at: 2026-08-31T03:00:48Z
updated_at: 2026-09-04T02:32:22Z
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


## CORRECTION 2026-08-31 (supersedes the follow-on above) — the gate's quoted number was never the evidence

I scoped `tr_M(2H) ~ 0.388` as convention-C and reported the gap against
`J_{6_2}(q0) ~ 1.027` as 62.19 % / 43.99 % low. **Both figures are withdrawn.**
I corrected an input to a comparison that is not evidential at all.

`markov_trace_to_jones` in `atom_nf_symbolic_D.py` -- the producer both audits
cite -- **is the identity function**. Its docstring names the normalisation
factor `((-1/sqrt q)^{n-1} * (q/(1-q^2))^{n-1})` and then says *"for ease, we
return `tr` as-is"*. `main()` calls it and compares the result straight against
a normalised `J(6_2)`. So the pair is an **unnormalised** 6-strand Markov trace
against a **normalised** Jones polynomial: they must differ, and the size of the
gap carries no information about the identification. Verified by AST inspection
of the producer rather than by grep.

**The gate stands anyway, on evidence neither audit cites.** `main()` knows the
normalisation is missing and computes the convention-independent discriminator
-- *"even if they differ by a writhe/normalization factor, the ratio should be a
pure power of `-q^{1/2}`"* -- recorded as `symbolic_ratio`. Measured: a rational
function with **83 terms over 11**, half-integer powers past `q^{2713/2}`. Not a
monomial. **The ratio test fails, so the A<=3 anchor non-confirmation is real and
C9 stands as written.**

The convention C-vs-D scoping is still correct *about the `tr_M` value*
(`0.388` is C, `0.5751722439177719` is canonical D per #6318, re-verified live)
and is retained in both audits as such -- it just does not bear on this
comparison.

**For whoever attacks `conj:canonical-knot-id-sdp`:** aim at the ratio being a
pure power of `-q^{1/2}`. Do not read the raw gap as "how far off" the
identification is; at n=6 strands that distance is dominated by the omitted
normalisation factor.

Probe: `computations/probes/r5full_anchor_gate_evidence_probe.py`, 3/3, exit 0,
writes no witness, performs no q0 evaluation for any conclusion.
Scope **(a)**: about the evidence for the gate, not about the knot.

## The pattern across all three corrections in this bean

Each was caught by opening the artifact a summary describes, not the summary:
AGENTS.md's note (accurate about `binding_canonical`, silent about the GS
route); the sibling's merged PR (which had already settled what I read as a
live disagreement); and now the producer's own source (which documents the
step it does not perform). **A summary that is accurate can still be the wrong
object.**


## 2026-09-03 — the handover target in this bean is MISCALIBRATED; the gate stands on a different test

This bean's closing line — *"For whoever attacks `conj:canonical-knot-id-sdp`:
aim at the ratio being a pure power of `-q^{1/2}`"* — points the next agent at a
test that cannot discriminate. I took up that target and found the problem in the
producer the bean itself cites.

**Two statements in `atom_nf_symbolic_D.py` cannot both be right.** Line 290 says
*"the ratio should be a pure power of `-q^{1/2}`"*. Line 194, in
`markov_trace_to_jones`'s own docstring, names the omitted factor as
`((-1/√q)^{n-1} · (q/(1-q²))^{n-1})`. The second is a **rational function** with a
`(1-q²)^{n-1}` denominator; the first demands a **monomial**. If the docstring
names what is omitted, then *"the ratio is not a monomial"* is precisely what a
**correct** identification would produce — so the recorded verdict ("not a
monomial, 83 terms over 11, therefore the anchor is not confirmed") does not
follow from its stated premise.

**The ratio is not opaque.** Factoring the committed `symbolic_ratio`:

    32 · q^1327 · (q+1)^5 · (q^6 − q^5 + 2q^4 − 2q^3 + 2q^2 − 2q + 1)

- `(q+1)^5` carries exponent **n−1 = 5** at the atom's 6 strands — the same
  exponent the omitted normalisation carries. **Accounted for**, not evidence.
  (A matching exponent is not a verified convention, and I claim only the former.)
- the degree-6 factor is **exactly `q^5·J(6₂)`** — the numerator of the very Jones
  polynomial being compared against, surviving in the **denominator**.

**THE GATE STANDS, on a sharper and convention-independent test.** Polynomial
division (after `q → t²` clears the half-integer powers) shows `q^5·J(6₂)` does
**not** divide the ratio's numerator — remainder nonzero, **12 terms**. And that
divisor is **irreducible over ℚ** and **coprime to both `(q−1)` and `(q+1)`**
(gcd 1 with each; `P(1) = 1`, `P(−1) = 11`). So **no** normalisation of the shape
`monomial · (1±q)^k` — the shape every Markov-trace-to-Jones convention takes —
can supply the missing factor:

    tr ≠ N · J(6₂)   for every N of that shape.

That is strictly stronger than "the ratio is not a monomial", and unlike it, it
cannot be dismissed as an artifact of the omitted normalisation. **So C9 stands,
and this bean's verdict survives — but its stated reason does not, and its
handover target should not be attacked as written.**

**Corrected handover.** Do not aim at the ratio being a monomial. The live
discriminator is **divisibility**: whether the Hecke trace is a multiple of
`q^5·J(6₂)` at all. It is not, and being coprime to the normalisation factors,
nothing about framing or convention will change that.

Probe: `computations/probes/r5full_anchor_gate_divisibility_probe.py` + witness,
4/4. Reads the committed `atom-nf-symbolic-D.witness.json`; exact sympy
throughout, no numeric evaluation anywhere, no `q₀` substitution.

**Scope (a), on the EVIDENCE and not on the knot.** This does not show D's atom
link is not `6₂` by some other route. It shows the *Hecke-level* identification
fails in a way no framing or normalisation convention can repair — which is what
the gate needed and did not previously have.

**This is a fourth instance of this bean's own closing pattern.** Its three
recorded corrections were each caught by opening the artifact a summary describes
rather than the summary. So was this one: the bean's handover quotes the
producer's *inline comment*, and the producer's *docstring* ninety lines earlier
contradicts it. The comment is the wrong object.


## 2026-09-04 — follow-on landed (qou-kru4, branch claude/monotone-word-trace-factorizes-2026-09-04)

The carrier box this bean closed on has its algebraic half proved: monotone words factorize under the Markov trace (`MonotoneWordTraceFactorizes.lean`), and the production word IS monotone, so its derived closure is a torus-link connected sum (Vol = 0, consistent with owner ruling A) AND its trace carries no n=4 cross term — for one and the same reason. A derived hyperbolic carrier and a derived collective term are now one question: does the substrate emit a non-monotone word? See docs/audits/2026-09-04-monotone-word-trace-factorizes-derived-link-map.md.
