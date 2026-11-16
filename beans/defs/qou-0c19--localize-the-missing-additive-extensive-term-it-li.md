---
# qou-0c19
title: 'Missing additive extensive term: is the inter-nucleon COLOR-TUBE channel (conj:inter-nucleon-channel-color-tube) its home? The arc-count diagnostic that motivated this is REFUTED — R²=0.83/0.26 are not in the cited witness (true 0.2653/0.0018, its own verdict "weak"), and arc count = A−1 so the fit is degenerate with A. W_{c1c2} now rests on the categorical argument alone. OPEN Q: does color-tube weighting saturate at A=4 giving ρ_4? Conditional on conj:s5-so3-fiber-action.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T15:55:10Z
updated_at: 2026-10-04T15:13:21Z
parent: qou-10v9
---


---
**Update 2026-08-30 (session arc-count-degeneracy, PR pending) — 🛑 THE TITLE'S
EVIDENCE DOES NOT SURVIVE READING ITS OWN SOURCE. Re-scope before acting.**

Scope (a). Nothing refuted, nothing wired. This bean had a title and no body;
the title's diagnostic was its whole content, so this is most of it.

**The citation does not match the witness.** The title asserts *"per-isotope
error ∝ inter-nucleon arc count R²=0.83 (vs signed-h R²=0.26) = the extensive
∝A signature"*. The same sentence is in
`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`
§4 and in `brings-surface/inter-nucleon-channel-color-tube.md:34`, which names
the source: `computations/low-isotope-sign-flip-diagnostic.witness.json`.

Read it. The string `0.83` occurs **zero** times. What it records:

| | quoted | actually in the witness |
|---|---|---|
| err_pct ~ n_inter (arc count) | 0.83 | **0.26529448…** |
| err_pct ~ signed_h            | 0.26 | **0.00175532…** |
| sample                        | —    | **n = 5**, two are A=1 anchors at \|err_pct\| < 1e-3 |
| its own verdict               | "localizes it" | **"WEAK correlation … sign-flips are NOT explained by simple linear channel models"** |

So the durable artifacts cite a witness for a number it does not contain, in
support of a conclusion its own recorded verdict contradicts, on three
informative points. Note the quoted `0.26` for SIGNED-H is, to three digits, the
witness's ARC-COUNT value.

**And the claim as written is degenerate anyway.** Read as "the extensive ∝A
signature" — an ABSOLUTE-error statement — it cannot discriminate, twice over,
both exact:
- R² is invariant under scaling the response, so a model short by a constant
  FRACTION has R²(err ~ X) = R²(B ~ X) for every X; and R²(B_AME ~ arc) =
  **0.9943** over the 2449 AME2020 nuclei with 2 ≤ A ≤ 240, with no model at all.
  Clearing 0.83 needs nothing missing.
- R² is invariant under affine reparametrisation of the regressor and arc = A−1,
  so arc count scores EXACTLY what bare A scores (and what 7A−3 scores). The
  diagnostic cannot tell the inter-nucleon arc structure from the mass number.
  "It beats signed-h" then says only that binding is extensive and signed-h is
  not a proxy for A.

**SCOPE LIMIT, kept explicit because it cuts against my own argument:** the
witness fits `err_pct`, RELATIVE error, for which a constant fractional
shortfall has zero variance — so the two bullets above govern the claim as
WRITTEN in this title, the audit and the block (all of which say "extensive ∝A"),
NOT the witness's own regression. What disposes of that one is its n=5 and its
own WEAK verdict.

**NOT claimed:** that `conj:inter-nucleon-channel-color-tube` is false — it may
hold on the categorical argument, untested here. Not that 0.83 was fabricated:
this clone is shallow, only 2 commits touching that witness are in the fetched
window and both carry 0.2653, so an earlier version cannot be excluded. The
claim is about the witness as committed today, which is what a reader following
the citation finds.

**Re-scope.** The premise "the missing object is an additive extensive term,
localized to the inter-nucleon channel" is not supported by the evidence this
bean cites. Companion finding the same day (PR #6271, bean `qou-brng`): for the
chain assembly the extensive framing does not apply at all — B_model is affine
in (Z,N), B/A converges, and the shortfall is a SHAPE mismatch whose missing
piece is the Z(Z−1) Coulomb multiplicity that
`CrossingCountAffine.no_crossing_combination_is_protonPairs` proves the crossing
counts cannot supply. Retitle to the Z(Z−1) + A^{1/3} target, or close as
superseded.

Corrected in the same PR: the audit §4 paragraph (struck through, with what the
source actually says) and the content block's claim. Probe:
`computations/probes/arc_count_diagnostic_degeneracy_probe.py` (6/6, exact
rational arithmetic, no float64).

## 2026-09-04 — the colour tube now has a NUMBER, and a structural obstruction

`qbeta_strand_multiplicity_probe.py` (7/7). Three crossings on three independent
strand pairs give `-ln b -> 3(-ln b)` exactly (if `tr_M` factorises over disjoint
supports), and the additive law's coefficient becomes `8.77274 MeV/nucleon`
against a measured peak `B/A` of `8.79456` at `A = 62` — **0.25 %**. The required
factor is 3.0075 and the strand count is 3.

So this bean's conjecture, if true, closes the extensive-term magnitude gap
(`qou-ib3g`) with no free parameter.

**Two obstructions, both new here:**

1. **The existing `m_pp`/`m_pn`/`m_nn` parameter is NOT it.** It repeats the same
   letter on the same generator, giving `X^3` in a 2-dim subalgebra: factors
   0.335 / 0.984 / 1.709, and `b > 1` (negative bond energy) at `m = 2`.
2. **The 3A layout cannot express a colour tube.** Nucleon `k` holds strands
   `3k, 3k+1, 3k+2`, so colour-matched pairs across an interface are distance 3
   apart; reaching them needs a braid, not the single `sigma_{3k+2}` emitted.

The decidable next step is (a): **does `tr_M` factorise over disjoint supports?**
That is checkable without building the tube, and it is what the `b -> b^3` claim
rests on entirely.

## 2026-09-04 (later) — assumption (a) DISCHARGED: `tr_M` does factorise. The obstruction is now a LAYOUT CONFLICT.

`computations/qbeta/qbeta_disjoint_support_factorisation_probe.py` (7/7), at
40 dps through `build_seminormal_matrices_mp` (the exact-precision builder, not
the float64 `chi_lambda_of_word` kernel).

**The result.** With `W = s0 s1 s0` on block `{0,1}` and `W' = s3 s4 s3` on
`{3,4}` — generators REPEATED inside each block, blocks separated by
`|1-3| = 2` — `tr(W.W') = tr(W).tr(W')` with relative difference **0.0** at the
working precision, and the same for all three physical bond letters. So
`b -> b^3` under a colour tube is **exact, not approximate**, and the additive
law's coefficient becomes `8.77274 MeV/nucleon` against a measured peak
`B/A = 8.79456` at `A = 62` — 0.25 %.

**Methodological trap worth keeping.** My first control was "adjacent supports
must NOT factorise". It is worthless: `tr(s0.s1) = tr(s0)tr(s1)` to 2.6e-40,
because a word using each generator ONCE in INCREASING order is collapsed one
generator at a time by the Markov property, adjacency irrelevant. A real control
needs a REPEATED generator, where `sigma^2 = h.sigma + 1` bites:
`tr(s0^2) = 1.12809` vs `z^2 = 0.37539`, and `tr(s0s1s0) = 0.69117` vs
`z^3 = 0.22999`. Both fail, as they must. Reading the first as a positive would
have been an overclaim.

**Where the obstruction moved.** A colour-BLOCKED layout realises the hypothesis
— colour `c` of nucleon `k` at strand `c.A + k` gives blocks `{0..A-2}`,
`{A..2A-2}`, `{2A..3A-2}`, disjoint and separated by one unused generator each.
So the trace cooperates and a layout exists. What blocks it is that the two
demands are **incompatible on one strand ordering**:

  * intra-nucleon structure (3 `g0` + 3 `g1`, quarks, gluons) wants a nucleon's
    three strands ADJACENT — `atom_braid_word_3A`'s `base_g0 = 3k`;
  * colour-blocked inter-nucleon coupling wants them `A` APART.

That is sharper than the previous probe's "distance 3 apart", and it is a
construction question with a definite answer rather than an open assumption.

## 2026-09-04 (third) — SETTLED: no strand ordering carries the colour tube

`computations/qbeta/qbeta_layout_conflict_probe.py` (5/5), exhaustive — not
sampled — over all `(3A)!` orderings, plus
`folio/quantum-observable-universe/lean/QOU/Hecke/LayoutConflict.lean` for
general `A`.

    A   strands   contiguous   tube-realising   BOTH   max matched under (1)
    2      6           72            48           0      1 of 3 needed
    3      9         1296            48           0      2 of 6 needed

**Zero at both sizes**, and each demand is individually satisfiable, so the
conflict is genuine rather than an impossible demand. Under contiguity the
maximum is exactly `A-1` colour-matched single-generator couplings against the
`3(A-1)` a tube needs — **exactly one third**.

**The reason, proved for every `A`:** two disjoint intervals on a line touch at
one boundary, so a contiguous layout admits at most ONE single-generator coupling
per interface (`adjacent_pair_unique`,
`contiguous_layout_cannot_carry_a_colour_tube`). And in the canonical `3k` layout
that one boundary is `(3k+2, 3k+3)` — **colour 2 of `k` to colour 0 of `k+1`,
colour-MISMATCHED** (`canonical_boundary_is_the_top_of_the_lower_block`). The one
available matched coupling needs a colour permutation inside the nucleons, which
`atom_braid_word_3A` does not do.

**The tube-realising orderings are exactly the colour-blocked ones** — at `A=3`
the search returns `(0,3,6,1,4,7,2,5,8)`, i.e. strand `(k,c)` at position
`c.A + k`, predicted before the search and failing contiguity completely.

**So this bean's conjecture is not wrong — it is unrealisable in this
construction family.** Two escape routes, named and not taken: drop contiguity
(intra-nucleon crossings become conjugated braids), or drop single-generator
couplings (in which case the disjoint-support factorisation no longer applies
and `b -> b^3` is not exact). Both are larger constructions.

**And the deficit is now one statement:** the canonical layout realises one third
of a colour-complete interface, and the missing scale factor against the peak
`B/A` is 3.0075. Same 3 — a restatement, not a derivation. `E_0` is still CAL-1
and `qou-59j5`'s normaliser family still spans 1.33x.

## 2026-09-05 — synthesis landed; this bean is the surviving mechanism gap

The arc is written up at
`docs/audits/2026-09-05-binding-law-arc-synthesis.md`. This bean is §6 item 4:
the factor of 3 is the strand count, `tr_M` cooperates exactly, and no strand
ordering carries the colour tube. Both escape routes remain named and untaken —
drop contiguity (intra-nucleon crossings become conjugated braids), or drop
single-generator couplings (and `b -> b^3` stops being exact).


## 2026-09-07 — the 2026-08-30 correction LANDED; the title had not caught up

Two verifications, both against the live tree rather than the bean's own note:

1. **"PR pending" is stale — both durable artifacts are corrected.**
   `brings-surface/inter-nucleon-channel-color-tube.md:34` now reports
   `R² = 0.2653` and `R² = 0.0018`, quotes the witness's own **weak** verdict,
   states in terms that it does **not** establish the per-arc claim, and adds
   both degeneracy cautions (arc count `= A − 1`, so the fit scores exactly
   what bare `A` scores; and `R²(B ~ A−1) = 0.9943` over 2449 AME2020 nuclei
   with no model at all). `docs/audits/2026-08-02-...-additive-term.md` carries
   its correction inline at :134 with the shallow-clone caveat at :157.
   Re-confirmed independently: `0.83` occurs **zero** times in
   `computations/low-isotope-sign-flip-diagnostic.witness.json`.

2. **The TITLE still asserted the refuted diagnostic**, as a positive finding
   (*"Diagnostic: per-isotope error ∝ inter-nucleon arc count R²=0.83 (vs
   signed-h R²=0.26) = the extensive ∝A signature"*), with the refutation
   visible only after opening the body. Retitled.

**Why retitle here when `qou-e9pp`'s stale "~700" was deliberately left alone
this same session** — the two cases are not alike, and the distinction is the
point. `qou-e9pp`'s figure is **stale** (700 against a decided population of
559–628); its title still points at a real thing. This one asserted numbers
that **do not exist in the source it cites**, in support of a conclusion that
source's own verdict contradicts. Staleness in a citation handle is tolerable;
a false citation in the most-read line is not. The former title is quoted above
so the handle survives a grep.

**Bean stays OPEN.** Its subject — whether the colour-tube channel is where the
missing additive extensive term lives, and whether the weighting saturates at
`A = 4` — is an open conjecture, conditional on `conj:s5-so3-fiber-action`.
Only the discredited *motivation* has been removed; `W_{c1c2}` now rests on the
categorical argument alone, which is weaker support but is not a refutation of
the conjecture.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- **Round 56 Progress (`2026-11-16T21:20:58Z`)**: Opened [`litlfred/qou#8207`](https://github.com/litlfred/qou/pull/8207) (`cfc03c4131df1ea758c17554768f2274e708f38b`, Commit 1 `0a9d3f269d6c23f614dc40aac55d5f0a7b2baafd`). Keeping bean at `status: in-progress` pending owner review.
