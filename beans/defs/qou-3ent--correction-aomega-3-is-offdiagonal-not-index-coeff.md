---
# qou-3ent
title: 'CORRECTION: A_omega = 3 is the OFF-DIAGONAL Stokes constant, NOT a 3d-index coefficient — eq (21) is diagonal-only'
status: todo
type: task
priority: high
tags:
    - g3-aomega
    - correction
    - reorg-2026-10-04
created_at: 2026-08-11T11:20:00Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

Found by the LIT3 sweep of GGM 2012.00062v3. The corpus has been treating the exact dictionary
(Conjecture 4, eq 21) as licensing "3 is a 3d-index/DT coefficient". IT DOES NOT:

 * eq (21) S+_{s1 s1}(x;q) = Ind^rot(0,x;q) is DIAGONAL-ONLY, and that entry's q^0 term is 1,
   not 3 (its series is 1 - 8q - 9q^2 + ...).
 * The 3 lives in the OFF-DIAGONAL (s1,s2) entry, which eq (21) does not cover — only the
   weaker eq (20) "up to GL(r, Z(x,q))" statement touches it.

So the repo's A_omega = 3 and its per-winding I(0,e) table are describing TWO DIFFERENT MATRIX
ENTRIES. Honest statement: 3 is the off-diagonal Stokes constant at the singularity
iota_{1,2} = Vol(4_1)/pi, conjecturally (Conj 3(d), NO CATEGORY NAMED) a DT/BPS degeneracy.

TWO further constraints on any "explain the 3" attempt:
 * eq (188): S+(x;0) = [[1, x^-1 + 1 + x],[0,1]], so 3 = s(1) for s(x) = x + 1 + x^-1 — three
   unit-multiplicity states graded by meridian charge e in {-1,0,+1}. The SAME s(x) appears for
   5_2 (eqs 239/277/307), where eq (98) is s(1)=3 and s(1)+1=4. So the 3 is NOT a 4_1-specific
   invariant — any such story is refuted by 5_2 before it starts.
 * The 3 is the first of the tower 3, 9, 75, 642, 5580, 48558 (eq 62). An explanation of 3 that
   says nothing about the tower is not an explanation.

ACTION: grep the corpus for text asserting the stronger reading and correct it.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Verified 2026-10-10 against library/arxiv-2012.00062v3. GGM prove Conjecture 4 (eqs 20/21) and Conjecture 5 for 4₁/5₂; Conj 3(d) (Stokes = DT) is unproved. The correction is still owed in mass-theory/aomega-fourone-dt-count.md:38-39, which says GGM proved Conjecture 3 for 4₁.

Evidence: Every factual claim checks against the held GGM text. Eq (21) `S⁺_{σ1σ1}(x;q)=Ind^rot(0,x;q)` is diagonal-only (`sec-003…md:106-107`). Eq (61) gives S⁺₁₁ = 1−8q−9q²… (`sec-007…md:442`). The tower 9, 75, 642, 5580, 48558 is eq (62) (`:445`). `S⁺(x;0)=[[1,x⁻¹+1+x],[0,1]]` is eq (188) (`sec-011…md:724`). s(x) = x⁻¹+1+x is eq (239) and (277) for 5₂. The ACTION is not done: `mass-theory/aomega-fourone-dt-count.md:38` still says GGM "proved peacock Conjecture 3".

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
