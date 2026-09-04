---
# qou-ib3g
title: 'GAP-2: missing additive extensive term - B_sym/A saturates at 2.998 MeV/nucleon vs nature''s 8.790'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T16:43:39Z
updated_at: 2026-09-04T10:34:38Z
parent: qou-9ot5
---

## 2026-09-04 — the number is 3.0075 and there are 3 strands per nucleon

`computations/qbeta/qbeta_strand_multiplicity_probe.py` (7/7).

**Compare to the PEAK, not the plateau.** A law with no surface, Coulomb,
asymmetry or pairing term is a pure volume term, so the honest comparison is
where those corrections vanish. Per-nucleon coefficient at `N = Z` is
`E_0 . 0.698581 = 2.92425 MeV`; over 2548 measured AME nuclides:

    peak B/A (A = 62)   8.79456  ->  required 3.00746   (3 is -0.248 % off)
    this bean's 8.790   8.790    ->  required 3.00590   (3 is -0.196 %)
    qou-59j5's 8.5      8.5      ->  required 2.90673   (3 is +3.209 %)
    median B/A          8.17357  ->  required 2.79510   (3 is +7.331 %)

The peak sits at **A = 62** — exactly where the `B/(E_0.S)` ratio ceiling of
3.00-3.01 was measured on 2026-09-04. **The ceiling and this factor are one
observation**, and the ceiling was already recorded then as a target to check a
future derivation AGAINST. The candidate has now arrived and it is the strand
count, which is not a free parameter: it is `atom_braid_word_3A`'s name and its
`base_g0 = 3*k` indexing, and `qou-59j5`'s probe already used
`STRANDS_PER_NUCLEON = 3` for this same conversion.

**The mechanism already in the word is REFUTED.** `atom_braid_word_3A` takes
`m_pp`/`m_pn`/`m_nn`, but it repeats the same letter on the SAME generator, so
`m = 3` is `X^3` inside a 2-dim subalgebra reduced by `sigma^2 = h.sigma + 1` —
not `b^3`. Factors at `m=3`: **0.335 (pp), 0.984 (pn), 1.709 (nn)** — non-uniform,
nowhere near 3, and the p-p bond gets WEAKER. At `m = 2`, `pp` and `pn` give
`b > 1`, i.e. a **negative bond energy**, so `m` is not a multiplicity of bond
strength at all.

**The surviving candidate is a colour tube, and it is not expressible here.**
Three crossings on three INDEPENDENT strand pairs give `b -> b^3` exactly IF the
trace factorises over disjoint supports; the coefficient is then
`8.77274 MeV/nucleon`, **0.25 % below the peak**. Two undischarged assumptions:
(a) disjoint-support factorisation of `tr_M` is ASSUMED, not verified — the
load-bearing step; (b) the 3A layout **cannot express it** — nucleon `k` occupies
strands `3k..3k+2`, so colour-matched pairs across an interface are distance 3
apart and need a braid, not the single generator `sigma_{3k+2}` the word emits.

**Not evidence, and this matters:** `3.E_0.S` has p5-p95 **identical to every
digit** with `E_0.S` (a constant cannot change a spread) and moves the median to
0.895 — 10.5 % over-bound. That is the expected signature of a pure volume term,
i.e. the absence of evidence against, not evidence for.

Direct successor to `qou-0c19` (the colour-tube localisation), which this makes
quantitative: the colour tube would supply exactly 3, and the gap is 3.0075.

## 2026-09-04 (later) — the colour tube's trace assumption is DISCHARGED

`qbeta_disjoint_support_factorisation_probe.py` (7/7): `tr_M` factorises over
disjoint non-adjacent generator blocks EXACTLY (rel. diff 0.0 at 40 dps), for
non-trivial words with generators repeated inside each block. So the `b -> b^3`
step is exact and the factor is exactly 3, not approximately.

The previous probe listed two undischarged assumptions. **(a) is now
discharged.** (b) is sharpened from "the couplings are distance 3 apart" to a
LAYOUT CONFLICT: intra-nucleon crossings want a nucleon's three strands adjacent,
colour-blocked inter-nucleon coupling wants them `A` apart, and one ordering
cannot do both. Detail on `qou-0c19`.

Still not a derivation, and the scale is still unpinned (`E_0` is CAL-1;
`qou-59j5`'s normaliser family spans 1.33x).

## 2026-09-04 (third) — the deficit is a COUNTING statement

`qbeta_layout_conflict_probe.py` (5/5) + `QOU/Hecke/LayoutConflict.lean`.
Exhaustively, no ordering of the `3A` strands makes the nucleon triples
contiguous AND the three colour-matched interface couplings single generators;
under contiguity the maximum is `A-1` of `3(A-1)` — one third. Proved for general
`A`: two disjoint intervals touch at one boundary.

So the missing factor of 3 and the interface shortfall are the SAME 3. That
sharpens the gap but does not close it: it says the colour tube is unrealisable
in this construction family, not what a realisable one would be worth. The energy
scale is untouched — `E_0` is CAL-1, the normaliser family spans 1.33x.
