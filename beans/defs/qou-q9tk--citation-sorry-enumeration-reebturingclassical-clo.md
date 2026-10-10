---
# qou-q9tk
title: Citation-sorry enumeration + ReebTuringClassical closure (false-encoding fix)
status: completed
type: task
created_at: 2026-08-01T23:23:45Z
updated_at: 2026-08-01T23:23:45Z
parent: qou-pddf
---

Branch: claude/citation-conjecture-lean-formalization-2026-08-01
Audit doc: docs/audits/2026-08-01-citation-justified-conjecture-lean-formalization.md

Enumerated all citation-justified cited sorries in content/quantum-observable-universe/lean/QOU:
86 cited sorries total; 47 [manuscript] (QOU-internal, out of scope); 39 external.

CLOSED (1): QOU.Information.ReebTuringClassical [cardona2021].
  - The prior encoding `∃ halts:ℕ→Prop, ¬∃ dec:ℕ→Bool, ∀n, halts n ↔ dec n=true`
    was PROVABLY FALSE (dec ranged over ALL functions, not computable ones;
    classically decide(halts n) decides every predicate). The cited sorry sat on
    an unsatisfiable proposition. Refutation machine-checked in pure Lean core.
  - Re-stated to the honest computational shadow and PROVED sorry-free via Mathlib
    `ComputablePred.halting_problem` on countable `Nat.Partrec.Code`. lean-direct exit 0.
  - Scope-(b) refutation of the ENCODING, not the Cardona theorem. Exactly the
    "not all physics papers are fully accurate" case.

BLOCKED (rest) — two missing-Mathlib-infra clusters, all correct/well-scoped cited sorries:
  1. S_n rep theory / RSK / Specht / hook-length (BraidKnot/* : Specht*, YoungTableau*,
     StandardYoungTableau, JucysMurphy, DeltaLambdaSignRule burnside) — [sagan2001],
     [james1984representation], [vershik-kerov1977]. Mathlib has YoungDiagram but no
     Specht modules, no RSK, no hook-length formula, no S_n irrep classification.
  2. LP/SDP strong duality (ParticleInteractions/* , Interactions/ConfinementSDP) —
     [bertsimas1997], [boyd-vandenberghe-2004], [wenzl1990]. Context classes carry data
     but not certificate relations; not derivable, not false. LP strong duality not in Mathlib.
  Isolated: hyperbolic-volume independence [zagier1986] (open transcendence, honest
  instance-less §3b class); q-Gevrey Newton polygon [ramis-sauloy-zhang2013] (real analysis);
  pair_skein_mass_formula [jones1987] (opaque object; needs categorical construction).

Already-closed precedent: partitionDom_antisymm (prior agent) — elementary order theory
despite a deep [james1984] citation. That + Reeb are the two "elementary/mis-stated
as-formalized" wins; the rest genuinely need the infra.

Future candidates (not attempted): JucysMurphy.syt_content_tuple_injective /
syt_adjacentSwap_connected (pure combinatorics, hand-formalizable, dozens of lines);
hecke_baer_star_generic [kassel1995] (algebraic).
