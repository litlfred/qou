---
# b9sp
title: Specht/S_n brick program (foundational, MULTI-SESSION) — unlock axiomatized Wedderburn facts
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T12:55:00Z
updated_at: 2026-10-04T15:24:35Z
parent: b9ms
---

Mathlib-absent rep theory. Bricks: hook-length formula (StandardYoungTableau.lean:113 numSYT_mul_hookProduct), Specht dim = #SYT (Specht.lean:313), dominance triangularity (SpechtStandardBasis.lean:264), James submodule (SpechtIrreducible.lean:160,172), distinct-shape non-iso (SpechtClassification.lean:414,436), char-0 Wedderburn split (SnWedderburnPartitionBridge.lean:232,427), Burnside sum f^lambda^2 = n! (DeltaLambdaSignRule.lean:292), JM commuting (JucysMurphy.lean:440). Attempt most self-contained brick first; the full program unlocks IwahoriHeckeAPI central-idempotent axioms (prove not assert). Scope honestly: not one session.

SCOPED 2026-07-05: all 8 bricks confirmed MULTI-SESSION (Mathlib v4.24.0 has no StandardYoungTableau/RSK/Specht-modules/Jucys-Murphy). None bounded; none faked (honest sorries kept). ENV FINDING: the brick files ARE lean-direct verifiable here (invoke ~/.elan/toolchains/lean-v4.24.0/bin/lean directly) — blocker is math depth, not tooling. Recommended phase order for a dedicated sub-campaign: A) specht_submodule_dichotomy + specht_form_nondegenerate (=> specht_isSimple) B) standardPolytabloid_triangular + _straightening (=> dim=#SYT) C) pairwise_noniso + exhausts (=> sn_rational_specht_split capstone) D) parallel: numSYT_mul_hookProduct (FRT), seminormalVector_data_exists (OV), burnside (RSK). Start with specht_submodule_dichotomy (largest downstream cone).

PROGRESS 2026-07-05: MILESTONE — specht_submodule_dichotomy (James's submodule theorem) FULLY sorry-free (source-level #print axioms: no sorryAx). Closed via 3 verified reduction rounds: kapL column-antisymmetrizer operator theory + clash/no-clash legs (kap_of_mem_line) + ~170-line Gale-Ryser saturation (noclash_match_exists) over Mathlib YoungDiagram. SpechtIrreducible.lean down 2->1 sorry. REMAINING (each a genuine Mathlib-absent development, NOT bounded fills): specht_form_nondegenerate (char-0 Gram non-deg; needs Cauchy-Binet or char-0 base-change of the radical — gates specht_isSimple irreducibility); seminormalVector_data_exists (OV seminormal eigenvector, famous); numSYT_mul_hookProduct (FRT hook-length, famous); standardPolytabloid_straightening (Garnir); + Phase C classification/Wedderburn capstone (depend on above).



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [B] sp00 (completed) lists all 10 bricks axiom-clean; b9sp is the same brick programme
