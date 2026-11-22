---
# qou-1o8n
title: 'T3: UGB Gröbner-Shirshov formalization (20 axioms + 7 sorries)'
status: in-progress
type: epic
priority: normal
created_at: 2026-08-03T15:06:36Z
updated_at: 2026-11-22T21:33:43Z
parent: qou-rtxm
---


## Reorganisation 2026-10-04

Now the epic for P3.GS under Lean / Mathlib foundations.


## Round 58 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8276 (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`)
- **Module:** `QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy` (`folio/quantum-observable-universe/lean/QOU/Foundations/IsotypicBlockSpolyLaurentHolonomy.lean`), wired into `QOU.lean`.
- **Theorem:** `overlap_spolynomial_assoc_and_joinable` — proves overlap S-polynomial `f · w - u · g` vanishing under associative reduction rules `u · v = f`, `v · w = g` and normal-form joinability over generic `CommRingCarrier R`, verified at 80 dps in `isotypic-block-spoly-laurent-holonomy.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.

- Round 78 (`lane-e667`): Formalized `qou-pan0`, `qou-tgci`, `qou-ykt7`, `qou-bq5e`, `qou-ch3j` in `QOU.Foundations.FilteredDifferentialSquareIdempotentBlockDecompositionIsometryTransportFinitePresentationDiamondConfluence` with 80-dps `mpmath` 2-commit witness stamp (`0869f3f0f137dac72b436e92a747c174449acb33` -> `8147a3388c97af1335cf6c164bd3eb4c9b4bd78a`, `scriptHash=f8a29b2aeceb36b8f640091b101ca03046313573b1d604a9e680784ae71f9af4`) in PR `litlfred/qou#8422` (`status: in-progress`).

- Round 79 (`lane-e667`): Formalized `qou-ix9e`, `qou-lncp`, `qou-ulfe`, `qou-znz5`, `qou-pso0` in `QOU.Foundations.MonicRewritingRuleOrientationOverlapCriticalPairResolutionFormalGroupLawDistributionConfluenceSpecializationFlatness` with 80-dps `mpmath` 2-commit witness stamp (`0e73e1d84b41af22cbe0a7adb5792bfd6ad829c7` -> `f1e0c5f0a53084f645586bcab55a711f50415015`, `scriptHash=6f730a2d7a28822fd4184de185390b3fa00ae1e8c3c649430e85284ae55ef0da`) in PR `litlfred/qou#8430` (`status: in-progress`).

## 2026-11-22: input from the GS-citation review thread (recorded by hecke-schur-weyl-lean drain)
Not yet verified in Lean here. Exact sympy check (see /mnt/project-files/gs-braid-citations/review.md, h_n_gs_check.py): in convention D with deg-lex s1<s2, heckeRewritingSystem 3 is already a GS basis (5 overlaps reduce to 0 over Q(q); 6 standard words), so a sorry-free n=3 GS theorem is a small target. At n=4 the uncompleted system has one bad composition (on s3 s2 s3 s1), matching hecke_not_gs_basis_four; with the Bokut-Shiao family added all compositions close at n=4,5. Citation gap: the q-deformed type-A completion is Kang-Lee 2000 (J. Algebra 232) Ex. 1.11, not Bokut-Shiao 2001 (q=1); neither is held, upload requested by that thread.

## 2026-11-22 correction to the note above (relayed from the GS-citation thread, not re-verified here)
General-n completeness is already on main: UGB/GrobnerShirshov/HeckeCompletion.lean states heckeCompleted_isGrobnerShirshovBasis for every n. What is missing is the primary-source citation (Kang-Lee 2000 / Kang-Lee-Lee-Oh 2002). The GS-citation thread is adding UGB/GrobnerShirshov/HeckeGSThree.lean (transfer lemma, uncompleted system GS at n=3, six irreducible words) on branch claude/hecke-gs-three-2026-11-22.
