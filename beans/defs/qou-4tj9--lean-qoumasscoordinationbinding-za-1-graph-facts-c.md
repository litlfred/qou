---
# qou-4tj9
title: 'Lean: QOU.Mass.CoordinationBinding — z=A-1 graph facts + conditional BondExtensiveBinding class (needs full Lean env)'
status: completed
type: task
priority: normal
created_at: 2026-07-11T17:38:10Z
updated_at: 2026-08-22T15:25:00Z
---

**2026-08-19 (PR #5346): SHIPPED + machine-verified — awaiting owner close.** The sandbox
blocker is gone: the full `lake-cache/qou-v4-24-0` restore carries the SimpleGraph +
ProofWidgets olean cone, so `content/quantum-observable-universe/lean/QOU/Mass/CoordinationBinding.lean`
is `lean`-direct **exit 0**, sorry-free. Lemma names updated to current Mathlib
(`SimpleGraph.complete_graph_degree`, `card_edgeFinset_top_eq_card_choose_two`,
`sum_degrees_eq_twice_card_edges`); needed `import Mathlib.Data.Real.Basic` for the ℝ fields.
All four theorems + the `BondExtensiveBinding` conditional class present as specced.


Ship the QOU-library Lean file deferred from PR #3551 (could not machine-verify in
sandbox: ProofWidgets widgetJsAll JS assets network-blocked → SimpleGraph olean cone
won't build without them).

Target file: content/quantum-observable-universe/lean/QOU/Mass/CoordinationBinding.lean
Namespace: QOU.Mass.CoordinationBinding
Imports: Mathlib.Combinatorics.SimpleGraph.Finite, Mathlib.Combinatorics.SimpleGraph.DegreeSum

Lemmas (all thin wrappers over verified Mathlib results):
  - coordination_degree : (completeGraph (Fin A)).degree v = A - 1
      via complete_graph_degree + Fintype.card_fin  (prefer `simp` over `rw`; note
      completeGraph vs ⊤ syntactic-match care for the edge lemma).
  - bond_count : #(completeGraph (Fin A)).edgeFinset = A.choose 2
      via card_edgeFinset_top_eq_card_choose_two + Fintype.card_fin.
  - coordination_handshake : ∑ v, degree v = 2 * A.choose 2
      via sum_degrees_eq_twice_card_edges + bond_count.
  - structure BondExtensiveBinding (A) { epsilon≥0 ; binding ; extensive : binding =
      epsilon * (A.choose 2 : ℝ) }  -- conditional class, the OPEN input (not derived).
  - binding_eq_bond_energy (= h.extensive), binding_nonneg (mul_nonneg + Nat.cast_nonneg).
  (Optional: binding_eq_coordination_bonds 2*B = eps*A*(A-1) — needs the nat-even /
   Nat.choose_two_right / Nat.mul_div_cancel' cast; verify with LSP before shipping.)

Verify: restore lake-cache/qou-<slug>, then `lake build QOU.Mass.CoordinationBinding`
in a full env (ProofWidgets reachable), or lean-direct once SimpleGraph oleans exist.
Base ring: ℝ only in BondExtensiveBinding (binding energy = archimedean); graph facts
are ℕ/generic. No sidecar (standalone library file) — add to lean-vacuity review
ledger if the conditional class trips the empty-carrier detector (it has real fields).

Refs: audit docs/audits/2026-07-11-bk-coordination-degree-and-alpha-contact.md;
merged rem:bk-coordination-multiplicity (#3549); this PR #3551.

## 2026-08-22 — CLOSED (owner-authorised in session)
Work merged to main in PR #5346: content/quantum-observable-universe/lean/QOU/Mass/CoordinationBinding.lean
verified present on main and sorry-free (lean-direct exit 0; 0 sorry/native_decide). All four specced
items shipped — coordination_degree (z=A-1), bond_count (C(A,2)), coordination_handshake, and the
conditional BondExtensiveBinding class carrying the OPEN extensive law. The 07-11 blocker (SimpleGraph
olean cone unbuildable: ProofWidgets network-blocked) was cleared by the full lake-cache restore.
Closed on explicit owner instruction this session.
