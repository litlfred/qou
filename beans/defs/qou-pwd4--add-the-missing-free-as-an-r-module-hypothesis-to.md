---
# qou-pwd4
title: Add the missing 'free as an R-module' hypothesis to cor:pbw and cor:ugb-pbw, and cite [bokutchen2015pbw] §3.7
status: todo
type: bug
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T18:29:01Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-q4oa
---

BOTH copies of the PBW corollary state the result over an arbitrary commutative
ring with unity with NO hypothesis on the Lie algebra, and BOTH proofs then use
freeness. Verified in the working tree 2026-08-09:

- `content/unital-groebner-bases/unital-groebner-bases-chapter/pbw-corollary.md`
  "Let g be a Lie algebra over R, a commutative ring with unity ... is
  isomorphic as an R-module to Sg". Its proof
  (`pbw-corollary-proof.md`) opens: "Choose a well-ordered basis {x_i | i in I}
  for g."
- `content/unital-groebner-bases/buchberger-and-pbw/pbw-corollary.md`
  (`cor:ugb-pbw`) states the same thing and its inline proof opens "Choosing a
  well-ordered basis {x_i | i in I} for g".

Every neighbouring block in the chapter says "free as an R-module" explicitly
(buchberger.md, main-theorem.md, remainder-module.md, s-polynomial-decomposition.md,
unital-groebner-basis.md, monomial-basis.md, groebner-basis.md,
division-algorithm.md, generator-choice-lemma.md), so this reads as a drafting
slip rather than a deliberate stronger claim.

The hypothesis is not cosmetic. [bokutchen2015pbw] section 3.7 (p. 6, read
2026-08-09) records that PBW genuinely FAILS for Lie algebras over a commutative
algebra: Shirshov 1953 and Cartier 1958 give counterexamples, and Cohn's 1963
family L_p = Lie_K(x1,x2,x3 | y3x3 = y2x2 + y1x1) over
K = k[y1,y2,y3 | y_i^p = 0] is proved not to embed in its universal enveloping
algebra for p = 2, 3, 5 (Bokut-Chen-Chen). K is a commutative ring with unity and
L_p is not K-free, so the family sits inside the corollary's stated hypotheses,
and Ug =~ Sg compatible with the canonical map would force g -> Ug injective.

WORK: add "which is free as an R-module" (matching the chapter's existing
wording) to both statements in one change so the copies do not drift, add
`bokutchen2015pbw` to the `cites` of both .ts files (neither has a cites field
today; `pbw-corollary-proof.ts` has none either), and update the Lean docstrings
that restate the manuscript claim verbatim -- `UGB/UnitalGroebner/pbw_corollary.lean`
and `UGB/BuchbergerPBW/ugb_pbw_corollary.lean`, "## Manuscript statement"
sections -- or they will preserve the unqualified claim.

This bean is the join target for the two `cite-in-block` actions on the ledger
row for library/arxiv-1502.06472v1/1502.06472v1.pdf.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8467, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — paper-structure drain (https://claude.ai/code/session_01Qmmkt8R1YXFpKDbBiKB3hh)

Live on main: both cor:pbw and cor:ugb-pbw (buchberger-and-pbw/ugb-pbw-corollary.md) still lack 'free as an R-module'; both Lean 'Manuscript statement' docstrings too. bokutchen2015pbw is registered. Corpus-derived fix proposed, owner-gated.

Report: docs/audits/2026-11-21-paper-structure-bean-drain.md on branch claude/paper-structure-drain-2026-11-21.

Ruling check (owner-rulings.md on main 2ae54ab401, 2026-11-21): no superseded premise (photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ = 2 − h⁴, fitted values in proofs) is used by this bean's finding.

Fix applied on owner card (2026-11-21) in PR #8825 (branch claude/paper-structure-drain-2026-11-21). Close when it merges.
