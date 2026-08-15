---
# htw2
title: 'GAP: per-chiral-fermion framed braid words — derive strand-twist totals (not enumerate). Residual of qou-q377 after the total-twist reduction.'
status: open
type: task
priority: normal
created_at: 2026-08-02T00:00:00Z
updated_at: 2026-08-02T00:00:00Z
---

Child of `qou-q377` (hypercharge Y second invariant). PR #4561 /
`claude/hypercharge-twist-derivation-2026-08-02`.

## What was closed (derived, Lean sorry-free)

The candidate `Y = 2(totalTwist/3 − I₃)` is a function of the **total
twist alone**, not the multiset (`TwistDatum.Ycand_factors_totalTwist`);
and reproducing a prescribed `Y` against `I₃` is **equivalent** to
`totalTwist = 3(I₃ + Y/2) = 3Q` (`TwistDatum.totalTwist_pinned_of_Ycand`).
So the SM first-generation spectrum **uniquely pins** each fermion's
total twist: `(u,d,ν,e) = (2,−1,0,−3) = 3Q`. The enumeration battery's
"4 of 10 000 survivors" is `1·2·2·1` — the count of size-3 `{−1,0,1}`
multisets realising each pinned total; the residual is `Y`-invisible
strand-refinement at fixed total, NOT hypercharge non-uniqueness.

## The precise residual (still open)

1. **Per-chiral-fermion framed braid words are missing.** The corpus
   carries no braid word `β_f` (with framing) for `u_L, d_L, ν_L, e_L,
   u_R, …`. Without them, `totalTwist(f)` cannot be *computed* from the
   framework — it is currently *pinned by the SM target* (an inversion,
   i.e. an anchor, not a derivation).
2. **`totalTwist = 3Q` is a consistency requirement, not a derivation.**
   It is `Q_twist = Q` (the falsifiable clause of
   `conj:sm-hypercharge-invariant`). Deriving the individual-fermion
   electric charge `Q(f)` — equivalently the framed braid word — from the
   framework is the actual open object. Note the framework's derived
   `Q = w/2` (Coulomb) is a *hadron-level* result; it does not assign a
   writhe/charge to an individual chiral fermion.
3. **The `1/3` normalisation is the helon (Bilson-Thompson) precedent,
   NOT derived.** `Q_twist = totalTwist/3` is assumed; a framework
   derivation of the colour-tube charge quantum is a sub-gap.

## Why the `1·2·2·1` residual can't be narrowed by hypercharge

The two `d`-survivors `{−1,−1,1}`, `{−1,0,0}` (total −1) and the two
`ν`-survivors `{−1,0,1}`, `{0,0,0}` (total 0) are provably
indistinguishable by `Y` (`TwistDatum.Ycand_factors_totalTwist`; concrete
witness in the same file). The `ℤ₆` condition and bar-negation are also
total-only, so none of them separate the multisets. A separating
constraint must see the **per-strand** assignment — i.e. the braid word
/ colour structure of item 1. That is the whole gap.

## Next honest step

Assign a *framework* framed braid word to each first-generation chiral
fermion (candidate home: the abelian-H, t=0 crossed-module datum +
level-k string extension recorded in the 2026-08-01 uploads-round-2
audit), then COMPUTE its total twist and check `= 3Q` — rather than
inverting the SM spectrum. Until then Y stays enumerated, not derived,
and `conj:sm-hypercharge-invariant` stays open.
