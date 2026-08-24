---
# qou-rcvc
title: 'The content-block backlog, triaged: 17 witnesses cite a proposition the corpus does not contain'
status: todo
type: task
created_at: 2026-08-24T00:01:06Z
updated_at: 2026-08-24T00:01:06Z
---

Repointing `content_block_label_audit`'s glob (1ca6fe52b) took its scan from 43
of 2717 witnesses to the whole corpus, and the true `missing_label` count is
**90 fields across 36 distinct labels** — not the 1 the blind scan reported, and
more than double the 43 last honestly measured in June.

Triaged. The 90 split into three populations with very different remedies, and
**one of them is a substantive editorial finding rather than bookkeeping.**

---

## A. OVER-CLAIM — 17 fields, 4 labels. The significant one.

The witness cites a **stronger block type than the corpus contains**: a
`prop:` where only a `rem:` or `conj:` exists. These computations are attached
to a proposition that is not there.

     12  prop:alpha-em-categorical-trace          exists only as  rem:
          alpha_em/alpha-em-2I-total-quantum-dimension-gate-test
          alpha_em/alpha-em-count-carrying-object
          alpha_em/alpha-em-fibre-Dzeta-shared-wall-test
          … and 9 more, all under alpha_em/

      3  prop:depth-stratified-frobenius-reciprocity   exists only as  conj:
          delta-lambda-full-variance-phase5e-1
          k-star-search-phase5d-5
          k-star-variance-phase5d-5b

      1  prop:eigenbasis-structural-lemmas        exists only as  rem:
          hecke-conjugation-duality-sign

      1  prop:term6-binding-density               exists only as  rem:
          term6-habiro-residue-mpfr-50dps

This is not a typo class. Either the block should be promoted — the work exists
and the corpus has not caught up — or the witnesses are claiming a status their
computation does not support, and the citation should be demoted to `rem:` /
`conj:`. **Twelve of the seventeen are one label in one directory**, which
suggests a single decision covers most of it.

Note the third and fourth: `hecke-conjugation-duality-sign` and
`term6-habiro-residue-mpfr-50dps` are both witnesses this branch has already
touched for other reasons, so the over-claim has been sitting under active work.

## B. STALE CITATION — 22 fields, 4 labels. Mechanically safe.

The block was re-typed to an equal or stronger form and the witness still names
the old one. The stem is unambiguous; only the prefix moved.

     11  conj:lambda-scale-substrate-form           ->  prop: (and prf:)
      6  conj:magic-shell-coupling-kappa            ->  def:
      4  conj:categorical-neutrality-saturated-shells -> prop:
      1  conj:diagrammatic-double-magic-lr-fusion   ->  prop:

`conj:lambda-scale-substrate-form` has BOTH `prop:` and `prf:` registered — the
conjecture was stated, proved, and the proof written up, while eleven witnesses
still cite the conjecture. Remapping these is safe, but it is 22 editorial
citations and should be one deliberate change with the mapping above, not a
drive-by sed.

## C. GENUINELY ABSENT — 51 fields, 28 labels.

No block with that stem exists in `content/**/*.ts` at all. The concentrated
ones first:

     15  conj:qbeta-precision-ladder
      4  prop:mass-formula-iterative-lp-dual
      4  conj:faddeev-phi-b-quasiperiod
      2  conj:lambda-scale-bring-bloch-identity
      2  rem:difference-knot-jsj-volume
      2  conj:shell-correction-term-seven

and 22 more at one field each — `prop:mostow-confinement`,
`def:linking-weight-borromean-3-categorical`, `cor:archimedean-knot-eigenbasis`,
`prop:yekutieli-non-abelian-stokes`, `rem:lepton-mass-integrals`, and so on.
Full list from the audit's own `--list missing_label`.

`conj:qbeta-precision-ladder` at 15 fields is the single largest item in the
whole backlog and has no stem in the registry under any prefix — worth checking
first whether it was renamed wholesale rather than never written.

Note `prop:proven-unwired-regression-2026-05-25` in this bucket: a label whose
own name says it is a proved-but-unwired regression marker. That one is
probably scaffolding, not a missing block.

---

## Why this sat unseen since June

Not neglect — the audit could not see it. `content_block_label_audit.py:133`
globbed its own directory non-recursively after the Phase-6 refactor moved the
module into `audits/` on 2026-06-02, one day after its last honest run. It
reported `missing_label` 43 -> 1 and that read as progress. See bean qou-ra19,
where this is the fourth of five instances of the same shape.

The audit is now registered ADVISORY in `staleness-gates.sh` with a stated
flip-to-blocking condition at `missing_label = 0`; `--strict` already exits 1 on
any, so the flip is a one-word edit once this backlog is drained.

## Deliberately not done here

No citation was edited. Population A is an editorial decision about proved
status, and population B — though safe — is 22 claims about which content block
a computation belongs to. Both deserve one considered change with the mapping
recorded, which is what this bean is for.
