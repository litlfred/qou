---
# qou-urt1
title: Remark interpreting 0110001v3.pdf at computations/gap2_borromean_triple_count.py
status: todo
type: task
priority: normal
created_at: 2026-08-08T23:37:03Z
updated_at: 2026-08-21T17:05:06Z
---

The GAP-2 audit's M3(K) = mu-bar-irreducible triple count is currently defined only combinatorially on the contact graph. A remark recording the geometric triple-point form of the same count would make the definition checkable on an explicit link realisation. What would need checking first: the corpus's contact graphs are not currently realised as links with Seifert surfaces, so the translation is not automatic.

**From the source**
- p. 562, remark following the Theorem — When the boundary of F is disjoint from the double-point set (possible only if all pairwise linkings vanish) mu-bar(ijk) = -t(ijk)(F), a pure signed triple-point count.
  Use here: The Brunnian-case corollary is the geometric form of the 'Milnor-irreducible triple' the GAP-2 audit uses to define M3(K); it gives a surface-level object to count rather than a braid-word Magnus coefficient.

Source: `library/0110001v3/0110001v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/0110001v3/  ->  [mellor-melvin2003]
  A geometric interpretation of Milnor's triple linking numbers

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [mellor-melvin2003] as the citation key when you do it.
