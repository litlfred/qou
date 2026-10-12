---
# qou-2vt5
title: '#7673 gaps 2+3: Wedderburn split continuous in q; base point other than coupling 0'
status: completed
type: task
priority: normal
created_at: 2026-10-12T18:13:09Z
updated_at: 2026-10-12T18:37:08Z
parent: qou-xhci
---

audit §5.1 gaps 2 and 3.


## 2026-10-12 — CLOSED (PR #7738, branch claude/kz-wedderburn-continuity-2026-10-12, head 965081e098)
Gap 2: QOU/SchurWeyl/JMProjector.lean heckeWedderburn_symm_single gives the inverse Wedderburn image of each matrix unit E^λ_TT as an explicit Lagrange polynomial in the additive Jucys–Murphy elements Y_k (Y_{k+1} = σ_k Y_k σ_k + q⁻¹σ_k), denominators q and [c]_{q²}−[d]_{q²} (nonzero at q = 1 and every positive real q). JMProjectorContinuity.lean: continuousOn_projFamily (gap 2), isIdempotentElem_projFamily (gap 3: idempotence at q = 1 by density of generic points), generic_of_pos (positive real q admissible, q = 1 included). Note: the old surjectivity proof separates blocks by multiplicative JM eigenvalues q^{2c}, which collapse at q = 1 — so the additive JM form was needed, not a restatement.
Coordinator re-check: lean -DautoImplicit=false -s 65536 exit 0 on both files (14.4 s, 8.9 s); #print axioms heckeWedderburn_symm_single, isIdempotentElem_projFamily, continuousOn_projFamily, generic_of_pos = [propext, Classical.choice, Quot.sound].
Interface lemma conj_of_isPreconnected_hecke posted as code in #7673 comment 6130311989 (needs #7673 modules); handed to the assembly prover (bean qou-gzsp). This bean's subject (continuity + base point) is proved, so completed; KZ≅Jimbo overall stays open under qou-s5v5 / qou-gzsp.
