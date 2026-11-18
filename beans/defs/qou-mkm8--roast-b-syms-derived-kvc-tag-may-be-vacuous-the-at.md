---
# qou-mkm8
title: 'ROAST: B_sym''s DERIVED* KVC tag may be vacuous — the atom closures are NOT hyperbolic'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T05:27:07Z
updated_at: 2026-11-18T11:45:08Z
parent: qou-6qbv
---

Surfaced by the owner's question "what is conjecture? can we prove?" -- which
turned out to be the most productive question of the session.

## The finding

`B_sym` -- EVERY binding number in the dashboard -- is tagged `DERIVED*`,
KVC-conditional: `ln|tr_M|` is `Vol` only via `prop:vol-through-tau`, which
opens *"Proposition (conditional on conj:kashaev-volume-conjecture)"*.

KVC says: for a **hyperbolic** knot, `Vol = 2*pi*lim log|J_N|/N`; and **the RHS
vanishes when K is not hyperbolic**.

But `vol-through-tau`'s own quantifier note (which I wrote on 2026-08-25) says:

> the production binding pipeline evaluates `tr_M` on `atom_braid_word_3A`,
> whose letters are `c*sigma_g + d*1` -- general Hecke elements, not braid
> generators. [...] the corresponding `Vol` is in fact **0**.

And landed on main today: `c64833a979 no branch closure of the atom element is
hyperbolic -- 0 of 40, both controls green`.

**So for every object production actually evaluates, KVC's content is the
TRIVIAL branch: Vol = 0.** The hard open part of KVC is about hyperbolic knots.
The pipeline never evaluates one.

## THE ROAST

**1. The `DERIVED*` tag may be pointing at the wrong risk entirely.** It tells
every reader "this rests on a famous open conjecture" -- which sounds like
appropriate humility and may be a *misdirection*. If the closures are
non-hyperbolic, the conjecture is not what is load-bearing. What IS load-bearing
is whatever licenses `ln|tr_M|` as a binding energy, and the tag does not name
it.

**2. There is a number-shaped tension nobody has stated.** `Vol(atom closure)
= 0` (measured, 0 of 40). `alpha*ln(tr_free/tr_atom) = 2.83 MeV` at 2H
(measured). Those are both true. **They are only compatible if `B_sym` is not
actually computing a volume** -- in which case the volume proposition is not the
step it rests on, and the whole KVC framing of the binding column is wrong
labelling rather than honest conditionality.

**3. I had both halves and did not put them together.** I wrote the quantifier
correction yesterday. I reported the `DERIVED*` KVC tag to the owner hours ago,
as a caveat qualifying all five fronts. I did not notice they contradict. It
took the owner asking a four-word question.

**4. If it IS wrong labelling, it is the good outcome -- and still bad.** A
mislabel means the binding numbers are less conditional than advertised. But it
also means the corpus has been carrying a prominent `DERIVED*` that discharges
scrutiny in the wrong direction: readers see "conditional on a famous
conjecture" and stop, rather than asking the harder question of what licenses
the log-trace at all.

**5. The alternative is worse and must not be assumed away.** If `B_sym`
genuinely does route through `vol-through-tau`, then it is claiming a nonzero
volume for a closure measured to have volume zero. I have NOT established which
reading holds. **Do not let this bean be cited as though I had.**

## The question this replaces

"Can we prove KVC?" is now the wrong question. Proving it in general is a major
open problem in quantum topology. Proving it for the knots QOU needs was the
owner's earlier suggestion and is far more tractable -- except this finding
suggests the needed cases are the NON-hyperbolic ones, where it is trivially
true and buys nothing.

**The right question: what actually licenses `ln|tr_M|` as a binding energy,
if not `vol-through-tau`?** That is answerable by reading the dependency cone,
and it is upstream of everything the five fronts measured.

## Fix

1. Trace `B_sym`'s ACTUAL dependency cone in the code, not the prose tag.
2. Determine which reading holds: mislabel, or unfounded.
3. Either re-tag `B_sym` with the step it really rests on, or record the
   tension as a live defect at the top of the binding chain.
4. Do NOT start work on proving KVC cases until 1-3 are settled.


---

## RESOLVED 2026-08-26 — steps 1–3 done. Verdict: POSITED, and the tag was mine.

**Step 1 (trace the code cone, not the prose tag).** `B_sym`'s dependency cone
contains no knot, no closure and no coloured-Jones limit. Three neighbouring
objects have three different licences:

1. **The log's extensivity is DERIVED, conjecture-free.** `σ² = hσ + 1` makes the
   interface subalgebra 2-dimensional (`span{1, σ₂}`), so with the Markov
   property `tr_M(W·σ₂) = z·tr_M(W)` we get
   `tr_atom = tr_free·∏_bonds (z + d_XY)`. A product has an additive logarithm.
   That is *why* a log appears, and it is elementary. It says nothing about MeV.
2. **`E₀ × trace DIFFERENCE`** is licensed by `conj:knot-factor-frobenius-pairing`
   — a **conjecture** block, and the *difference*, i.e. the `B_can0` column. The
   code comment there already said "NOT the log `B_sym`".
3. **`ln|tr_M| = Vol`** is `prop:vol-through-tau`, KVC-conditional, and does not
   reach this object (braid quantifier + 0/40 non-hyperbolic ⇒ Vol = 0 while
   `B_sym(²H) = 3.89 MeV`).

`B_sym` has (1)'s extensivity and (2)'s prefactor. **No block asserts the
combination.**

**Step 2 (which reading holds).** Neither cleanly — the tag was wrong in **both**
directions. Over-hedging in form (an irrelevant open conjecture attached), and
under-stating in substance (concealing that nothing licenses the energy
identification at all). The honest tier is **`POSITED`**.

**Step 3 (re-tag).** Done: `B_sym` and `B_qCLT_fac` are now `POSITED`; a
`POSITED` tier was added to the dashboard legend; the module docstring and the
footer `Defn:` line no longer cite `vol-through-tau`. No number moves.

**Self-correction.** I introduced the KVC tag myself in `933053614f`
(2026-08-25 18:59:59), a commit that *retracted* an earlier "posited" finding of
mine. Then in `1c83073b3c` — **47 minutes later, same session** — I corrected
`vol-through-tau`'s quantifier and wrote a note saying the production object is
not covered and "the corresponding Vol is in fact 0". I never went back. The
retraction is retracted; the original finding was closer to right.

**Still open → step 4.** Nothing here derives the log-form. Two candidate
closures, and note they are *not* trivially the same: with `s = 1 − tr_atom/tr_free`,
`B_can0 = α·tr_free·s` while `B_sym = α(s + s²/2 + …)`, so difference-form and
log-form agree only for small `s` **and** `tr_free ≈ 1`, neither of which holds
here. Either (a) derive the log-form from the difference-form conjecture plus a
stated condition, or (b) find/write a block that licenses the log directly.
**Do not close this by re-citing `vol-through-tau`.**

Audit: `docs/audits/2026-08-26-what-licenses-the-log-not-the-volume-conjecture.md`



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 85 (`lane-e667`): Formalized `qou-ep4e`, `qou-fpjy`, `qou-i6bn`, `qou-i6cn`, `qou-mkm8` in `QOU.Foundations.TableauSquareSumPromotionBinderObligationVisibilityLogDeterminantBoundaryStandaloneAxiomDistributionNonHyperbolicVolumeVanishing` with 80-dps `mpmath` 2-commit witness stamp (`dfc69944cbe55f3b2622843a90dea18c98e576d7` -> `cbb6c21aa01988c4135bc7451f24b559c8179f67`, `scriptHash=0e68280fe3476a3f8543bf6de4770766624506d689b2ae34edd201278173e989`) in PR `litlfred/qou#8455` (`status: in-progress`).
