---
# qou-2re6
title: Cite [li2026-two-sphere] Thm 1.0.8 at rem:tqft-context — 'A carries the 2d cobordism data' is Cob(2) ≅ Cob(3)_{S²,CF}
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T13:41:39Z
updated_at: 2026-09-07T06:55:15Z
parent: qou-2akx
---

Source: triage of the 2026-09-06 uploads (docs/audits/2026-09-06-uploads-triage-eight-documents.md; ledger row library/arxiv-2605.20846v1).

WHAT. rem:tqft-context (content/quantum-observable-universe/quantum-observable-universes/tqft-context.md, line 1) says the Frobenius–Hopf object A 'carries the 2d cobordism data' of the 3d TQFT, citing atiyah1988 / kock2004 / lurie2009 / turaev2010 for the general TQFT frame. Li (arXiv:2605.20846, math.AT, 2026) proves the precise statement: Thm 1.0.8 (= Thm 3.3.6) — a canonical isomorphism Cob(2) ≅ Cob(3)_{S²,CF}, the commutative-Frobenius sub-bordism category of the S²-sector of Cob(3); so for EVERY 3d TFT Z, Z(S²) is a commutative Frobenius monoid and its Frobenius structure is exactly the 2d cobordism data. Thms 1.0.5 / 1.0.6 give the full presentation of Cob(3)_{S²}: extra generators labelled by closed oriented irreducible prime 3-manifolds (a unit 1_p : ∅ → S² per prime p), with 'legs' relations; Def 5.1.7 / Lemma 5.1.2 = P-monoids ≅ L-monoids.

DO. Add 'li2026-two-sphere' to cites[] in tqft-context.ts and one sentence to the .md after the first sentence: the 2d-cobordism claim is Li's Cob(2) ≅ Cob(3)_{S²,CF} (Thm 1.0.8); the S²-sector's remaining generators — one unit per prime closed 3-manifold (Thm 1.0.5) — are not used by the QOU axioms. Render-QA + sidecar refresh.

CAVEAT (state it in the sentence, do not overclaim). Li's monoids are COMMUTATIVE Frobenius monoids in a SYMMETRIC monoidal target; QOU's A is a Hopf algebra in a BRAIDED category and is not assumed commutative. The identification is at the Frobenius-structure level only; it does not say A is Z(S²) of some 3d TFT, and it says nothing about the Hopf half of the Frobenius–Hopf object. Corpus grep before writing: content/ has no 'Cob(' / bordism-category vocabulary outside this block and quantum-universes/frobenius-relation.md.

Correction 2026-09-06 (same session): the last sentence's corpus-grep claim is slightly off — 'Cob(' / 'bordism' occur in content/ ONLY in rem:tqft-context (quantum-universes/frobenius-relation.md does not use that vocabulary; it states the Frobenius relation diagrammatically). The action is unchanged.



Claimed 2026-09-07 on branch claude/uploads-triage-chips-2026-09-07 (one PR for the three remaining citation/framing chips of the 2026-09-06 uploads triage).
