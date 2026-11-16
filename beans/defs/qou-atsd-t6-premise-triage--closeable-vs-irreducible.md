---
# qou-atsd-t6-premise-triage
title: 'T6: atomicity premise triage — sp₂=sl₂ (closeable) + de-axiomatize su2 torus + wire-in; rank G=rank Lie G and Tannakian G↪Sp(V) are IRREDUCIBLE premises (do not launder)'
status: in-progress
type: task
priority: normal
tags:
    - 8f-atomicity
    - reorg-2026-10-04
created_at: 2026-07-26T20:55:00Z
updated_at: 2026-10-10T07:16:15Z
parent: qou-8lxd
---

Honest triage of the 3 remaining atomicity premises (owner asked to "resolve/fix").

CLOSEABLE (Lean-provable, do in this tranche):
1. sp₂ = sl₂ (premise-2 algebraic core). Mathlib Symplectic.sp l R = skewAdjoint(J l);
   for l=Fin 1 over Matrix (Fin 1 ⊕ Fin 1), reindex ≃ Fin 2, show J-skew-adjoint ⟺ trace-zero.
   Deliver: sp1_eq_sl2 (LieSubalgebra equality/iso) in a new file or AtomicityFromSelfDuality.
2. De-axiomatize maximal-torus-su2.lean: it ASSERTS rank:=1 as a structure field (rank_one:=rfl).
   Rewire to consume sl2_rank_eq_one (via 𝔰𝔲₂⊗ℂ ≅ 𝔰𝔩₂ or state the torus rank via LieAlgebra.rank).
   Content block (.ts/.md siblings) → run validate after.
3. Wire-in: cite sl2_* lemmas at use sites; delivery-summary links.

IRREDUCIBLE PREMISES (NOT Lean-closeable by us — must stay cited premises, NO fabricated instance):
- rank G = rank Lie(G): needs algebraic-group + maximal-torus theory absent from Mathlib
  (major contribution). Avoidable only by Lie-level framing (a framing choice, not a proof).
- rank Lie(G) ≤ 1 ⟹ single fundamental object: needs reductive-group weight/rep theory (unformalized).
- G ↪ Sp(V) from self-duality of V: Tannakian — needs Aut^⊗(τ) + fibre functor + the symplectic
  form on V from self-duality, i.e. the whole QOU category formalized. Front-1 + Lie-rank are
  DOWNSTREAM of this; they cannot prove it.
- The jet-tower actually being a chain: this IS the atomicity hypothesis (Front-1 characterized
  chain ⟺ rank-one; it does not force it).

SEPARATE WORKSTREAM (queue, unrelated to atomicity): "chip away at 1ppq path" = precision goal
L1/L2 (docs/precision-goals.md). Own tranche; see per-observable-100x dashboard.

DISCIPLINE: §"Axiomatization is NOT a Proof" + critical-distance license. The conjecture does NOT
close; only the sp₂=sl₂ core + de-axiomatization + wiring are honest closures.

--- AGENTS DISPATCHED 2026-07-26 (worktree-isolated, robust, own branches + draft PRs) ---
- Agent A (self-dual → Sp(V)): file AtomicitySelfDualToSymplectic.lean; PROVE sp(Fin 1)=sl₂ core
  + honest §3b-cond premise for the Tannakian "self-dual ⟹ preserves ω". Branch
  claude/atomicity-selfdual-symplectic-2026-07-26.
- Agent B (rank G = rank Lie G): file AtomicityGroupRank.lean; conditional class RankGroupEqRankLie
  (OPEN premise, cited) + conditional atomicity_group_rank_le_one wiring the landed Lie bound.
  Branch claude/atomicity-group-rank-2026-07-26.
- Agent C (rank-1 ⟹ single object): file AtomicityRankOneToSingleObject.lean; conditional class
  + PROVE the class⟹chain composition via landed freeGen_total_iff_subsingleton; secondary
  jet-tower-chain route. Branch claude/atomicity-rankone-single-object-2026-07-26.
All 3: anti-laundering strict (no fabricated instances), sorry only for cited premises.
Jet-tower chain axiom = CONCLUSION of {A}+{landed rank≤1}+{C}, not a 4th independent premise.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Note (2026-11-16)
- Formalized T6 `sp_2 = sl_2` algebraic core (`J*M + M^T*J = 0 <-> a + d = 0`) in `QOU/Eightfold/AtomicitySp2ElectroweakAndPartitionUnification.lean` (`sp2_eq_sl2_trace_zero_iff`) + 50-dps probe `atomicity_sp2_electroweak_and_partition_unification_probe.py` (PR `litlfred/qou#8172`, head `89a2a31a65a0d7dbf47567c813f9c48b755fae24`).
