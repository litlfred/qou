---
# qou-7arp
title: 'Author a def: block for the octonion algebra O — the ledger row is an EXPOSITION gap, not a citation gap'
status: completed
type: task
priority: normal
created_at: 2026-08-25T18:48:30Z
updated_at: 2026-08-29T09:58:31Z
parent: qou-8lxd
---

RE-SCOPED by the 2026-08-25 upload triage. The eightfold §8 ledger row reads 'The octonion algebra O and G_2 = Aut(O) -- OPEN: used throughout but never defined -- this paper has no definition of O to point at', which reads as a mathematical or citation gap. It is NEITHER:

- CITATION side is already closed: baez2002 ('The Octonions', BAMS 39) is in references.ts with a note recording Der(O) = g_2, and is cited by QOU/MathlibExt/OctonionDerivationsBound.lean.
- LEAN side is already substantial: ten Octonion*.lean files under QOU/MathlibExt/, including a concrete octMul in the Baez convention and OctonionComplexStructure.lean proving Le^2 = -id in exact rational arithmetic -- its own docstring calls this 'the algebraic heart of the 1 + 3 colour decomposition'.

So the actual gap is EXPOSITION: there is no `definition` CONTENT BLOCK for O. No external paper can close that; an author writes it. That is a much smaller job than the row implies, and the row should be re-worded so a future agent does not go hunting for a source that is already there.

If a modern restatement is wanted alongside baez2002: library/arxiv-2403.00360v2 §2.3 is complete and self-contained (basis, conjugate, norm, inverse, Cayley-Dickson provenance, the seven H subalgebras, non-associativity witness, alternativity, Aut(O)=G_2, and the C+C^3 splitting), and its octonion section is free of causal-fermion-system commitments -- cite §2.3 only, not §3-5. For the multiplication table specifically, library/arxiv-2202.06733v1 Table 2 is in the BAEZ convention, matching the corpus's own octMul, and notes that 480 tables are compatible with e_0=1 -- a caveat worth carrying wherever the corpus fixes a table.
