---
# qou-40kk
title: Przytycki and Bullock are held (15 and 3 library dirs) but unregistered in references.ts
status: todo
type: task
priority: normal
created_at: 2026-09-04T09:40:05Z
updated_at: 2026-09-04T09:43:23Z
---

MEASURED 2026-09-04, corpus-grep path 5. I had reported that 'the corpus has nothing on Przytycki or K_q(S^3)'. That was content/ and docs/ only. In library/: Przytycki 15 dirs, character variety 35, 'skein module of' 10, 'Kauffman bracket skein module' 4, Bullock 3.

ON POINT: library/gn2 is Gelca & Nagasato, 'Some results about the Kauffman bracket skein module of the twist knot EXTERIOR' - the KBSM of a knot exterior, which is the object the qou-yb2b extension question needs. Bullock is the author of the KBSM-as-quantization-of-the-SL(2,C)-character-variety theorem.

ABSENT: the registration. grep -in 'przytycki|bullock' content/schema/references.ts returns ZERO. This is the citation inventory's held-but-unregistered class (its instance was library/0803219); these are two more, on the question this PR is about. There is already an open bean to add a reference for gn2.pdf - check it before filing a third.

TWO CAUTIONS. (1) gn2's extracted sections/ carry NO free/rank/basis statement - a grep returns nothing - so it is the 'held does not mean held in full' trap one document over: the PDF is on disk, the structural claims did not survive extraction. Read the PDF or re-extract before citing a rank claim to it. (2) A twist-knot EXTERIOR is not S^3. The rank-1 case the degeneration theorem (QOU.Eightfold.operator_basis_degenerates) needs is the SIMPLY-CONNECTED one; the only held section pairing 'skein module' with a 3-sphere is arxiv-2111.06645v3, unexamined.

SCOPE: this is a registry task, not research. Registering the keys does not establish the rank-1 premise - it makes the premise citable when someone does establish it.

LEAD CLOSED, NEGATIVE, 2026-09-04. I named arxiv-2111.06645v3 as 'the only held section pairing skein module with a 3-sphere' and said it was unexamined. Examined now: it is Garoufalidis-Gu-Marino, 'Knots, Perturbative Series and Quantum Modularity' (Habiro ring, quantum modularity conjecture, matrix-valued cocycles) - NOT a skein-module paper. Its sections carry no extractable 'skein module' passage and no S^3 rank/free statement; both context greps over library/arxiv-2111.06645v3/sections/*.md returned nothing. The co-occurrence that put it on the list is incidental.

SO THE RANK-1 PREMISE IS NOT CITABLE FROM THE LIBRARY AS INDEXED. Paths searched, per the standing rule: library/INDEX.md (tier 1), library/*/sections/ (tier 3) for Przytycki / Bullock / 'skein module of' / 'Kauffman bracket skein module' / 'character variety', and library/*/ocr/ (tier 4, returns 0 dirs for all three terms). NOT searched: the 15 Przytycki-mentioning PDFs themselves (a mention is a citation, not necessarily the theorem), and corpus_search (path 0) which has been down four sessions.

The classical statement wanted is Przytycki's: the Kauffman bracket skein module of S^3 is free of rank 1 on the empty link. A MENTION of Przytycki in 15 directories is not that theorem - see the 'held does not mean held in full' caution above, which applies here too.

SIDE NOTE, not this bean's business: arxiv-2111.06645v3 is highly relevant to the qbeta_habiro producers and the c_k ladder for a different reason (new elements of the Habiro ring, smoothed optimal truncation). Whoever works those should know it is held.
