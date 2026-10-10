---
# qou-sg2y
title: Add reference for AIF_2000__50_4_1021_0.pdf at QOU.MathlibExt.QCharacter
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:37:12Z
updated_at: 2026-08-21T17:03:54Z
---

Core and orphan; QCharacter.lean credits this work in prose with no ref() entry to resolve, and it is the construction the whole W2 Birkhoff-matrix layer rests on.

**From the source**
- sections 1-2 (construction of the characters e_{q,c}; 'Matrice de connexion et classification', the Birkhoff matrix with elliptic coefficients) — For a regular singular q-difference system the canonical solutions at 0 and infinity are built from theta-quotient characters, and their connection matrix P = (X^infinity)^{-1} X^0 has elliptic coefficients; the triplet (N^(0), P, N^(infinity)) is a complete classifying invariant.
  Use here: The literature source for QCharacter.lean's e_{q,c} theta quotient, for its ellipticity lemma, and for the pole-divisor claim in prop:c1-theta-zero-locus-and-pole-divisor — all currently carried without a bibliographic entry.
- section 4 ('Comportement de la matrice de connexion lorsque q -> 1') — As q tends to 1 the connection matrix converges, recovering the monodromy of the confluent differential system.
  Use here: The classical-limit statement the corpus needs whenever it argues that a q-difference object is the q-lift of a classical monodromy datum rather than an analogy; it sits beside the existing confluence references in the q-lift cluster.

Source: `library/aif-2000-50-4-1021-0/AIF_2000__50_4_1021_0.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/aif-2000-50-4-1021-0/  ->  [sauloy2000]
  Systèmes aux q-différences singuliers réguliers : classification, matrice de connexion et monodromie

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
