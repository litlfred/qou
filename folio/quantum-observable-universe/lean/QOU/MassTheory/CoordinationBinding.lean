/-
QOU.Mass.CoordinationBinding — the per-nucleon coordination number z(A) = A − 1 and the
bond-count C(A,2), as thin wrappers over verified Mathlib `SimpleGraph` facts, plus the
conditional `BondExtensiveBinding` class encoding the (OPEN, not-derived) extensive
binding law  B = ε · C(A,2).

Arc context (docs/audits/2026-07-11-bk-crossing-coordination-multiplicity.md): the open
many-body multiplicity `M_n(A)` decomposes as `z(A) · a_D^(A)` with `z(A) = A − 1` the
per-nucleon coordination number — the degree of a vertex in the fully-coordinated
(complete-graph) nucleon cluster on `A` nucleons — and `C(A,2)` the total nucleon–nucleon
bond count. This file formalizes those two graph facts (and the handshake identity linking
them) so the numerical identification `M_need(A=3 pair) ≈ z = 2` (<3%, fit-free) rests on a
machine-checked combinatorial statement rather than an asserted count.

The binding LAW `B = ε · C(A,2)` itself is NOT derived from the 13 categorical drivers; it
is carried here as a `structure BondExtensiveBinding` hypothesis (a conditional class in the
§3b-cond sense — its field `extensive` is the open input, not a proved conclusion). The
lemmas below that consume it (`binding_eq_bond_energy`, `binding_nonneg`) are fully verified
GIVEN that hypothesis; they do not assert the law holds.

**Status 2026-11-21: the law `B = ε·C(A,2)` is EXCLUDED, not merely open.**
`QOU.Mass.CoordinationSaturation.complete_graph_no_saturation` proves it gives
`B(A)/A = ε·(A−1)/2`, unbounded in `A`, so nuclear saturation rules out the
complete-graph coordination this class encodes (scope (b), invariant =
saturation). The class is kept only as the named object that theorem refutes.
Do not instantiate it as a binding model. The graph facts above
(`coordination_degree`, `bond_count`, `coordination_handshake`) are unaffected
and are used by `QOU.MassTheory.BraidPathNotCoordination`.

Base ring: the graph facts are `ℕ`-valued (generic); `ℝ` appears only inside
`BondExtensiveBinding`, where the binding energy is an archimedean quantity (§7c).

Standalone library file (no `.ts`/`.md` sibling) — deferred from PR #3551, where the
sandbox could not build the `SimpleGraph` olean cone (ProofWidgets JS assets
network-blocked). Bean qou-4tj9.
-/
import Mathlib.Combinatorics.SimpleGraph.Finite
import Mathlib.Combinatorics.SimpleGraph.DegreeSum
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

namespace QOU.Mass.CoordinationBinding

open Finset SimpleGraph

variable {A : ℕ}

/-- **Per-nucleon coordination number `z(A) = A − 1`.** In the fully-coordinated cluster of
`A` nucleons — the complete graph `⊤ : SimpleGraph (Fin A)` — every nucleon is bonded to the
other `A − 1`, i.e. its degree is `A − 1`. This is the topological integer the arc identifies
with the open-shell multiplier `M(open shell)`. -/
theorem coordination_degree (v : Fin A) : (⊤ : SimpleGraph (Fin A)).degree v = A - 1 := by
  simp [Fintype.card_fin]

/-- **Total nucleon–nucleon bond count `C(A,2)`.** The number of edges of the
fully-coordinated cluster on `A` nucleons is `A.choose 2`. -/
theorem bond_count :
    (⊤ : SimpleGraph (Fin A)).edgeFinset.card = A.choose 2 := by
  rw [SimpleGraph.card_edgeFinset_top_eq_card_choose_two, Fintype.card_fin]

/-- **Handshake identity.** Summing the per-nucleon coordination degree over all `A` nucleons
double-counts every bond: `∑_v deg v = 2 · C(A,2)`. Ties the two counts above together. -/
theorem coordination_handshake :
    ∑ v : Fin A, (⊤ : SimpleGraph (Fin A)).degree v = 2 * A.choose 2 := by
  rw [SimpleGraph.sum_degrees_eq_twice_card_edges, bond_count]

/-- **Conditional extensive-binding class (the OPEN input, not derived).** Asserts that the
many-body binding energy of the `A`-nucleon cluster is `ε` per nucleon–nucleon bond times the
bond count `C(A,2)`, with a non-negative per-bond energy `ε`. The field `extensive` is the
arc's open hypothesis (`b_αα`-type per-bond constant is empirical, not from the 13 drivers);
this class carries it so downstream facts are verified *conditional on it*, never asserting it
holds. -/
structure BondExtensiveBinding (A : ℕ) where
  /-- per-bond binding energy (archimedean, ℝ) -/
  epsilon : ℝ
  /-- the many-body binding energy of the `A`-nucleon cluster -/
  binding : ℝ
  /-- per-bond energy is non-negative -/
  epsilon_nonneg : 0 ≤ epsilon
  /-- OPEN hypothesis: binding is extensive in the bond count `C(A,2)` -/
  extensive : binding = epsilon * (A.choose 2 : ℝ)

/-- Given the conditional class, the binding energy equals the per-bond energy times the
bond count. (Just `h.extensive`, exposed as a named consumer.) -/
theorem binding_eq_bond_energy (h : BondExtensiveBinding A) :
    h.binding = h.epsilon * (A.choose 2 : ℝ) := h.extensive

/-- Given the conditional class, the binding energy is non-negative. -/
theorem binding_nonneg (h : BondExtensiveBinding A) : 0 ≤ h.binding := by
  rw [h.extensive]
  exact mul_nonneg h.epsilon_nonneg (Nat.cast_nonneg _)

/-- **Coordination bridge: `2·B = ε · ∑_v z(A)`.** Twice the (conditional)
extensive binding energy equals the per-bond energy times the summed
coordination degrees `∑_v deg v`. This is the machine-checked combinatorial
certificate the file's purpose calls for: it routes the binding law's bond
count through the proved handshake identity (`coordination_handshake`) rather
than through the bare `A.choose 2`, so the extensivity is tied to the actual
per-nucleon coordination degrees. Still fully conditional on
`BondExtensiveBinding` — it certifies the *shape* of the law against the graph,
it does not assert the law holds. -/
theorem two_mul_binding_eq_epsilon_sum_degrees (h : BondExtensiveBinding A) :
    2 * h.binding
      = h.epsilon * ((∑ v : Fin A, (⊤ : SimpleGraph (Fin A)).degree v : ℕ) : ℝ) := by
  rw [h.extensive, coordination_handshake]
  push_cast
  ring

/-- Given the conditional class, the binding vanishes below two nucleons: with
fewer than two nucleons there are no bonds (`C(A,2) = 0`), so the extensive
binding is exactly zero. -/
theorem binding_eq_zero_of_lt_two (h : BondExtensiveBinding A) (hA : A < 2) :
    h.binding = 0 := by
  rw [h.extensive, Nat.choose_eq_zero_of_lt hA, Nat.cast_zero, mul_zero]

/-- Given the conditional class with a strictly positive per-bond energy, the
binding energy is strictly positive once there is at least one bond (`2 ≤ A`,
so `C(A,2) > 0`). Sharpens `binding_nonneg` on the coordinated regime. -/
theorem binding_pos (h : BondExtensiveBinding A) (heps : 0 < h.epsilon) (hA : 2 ≤ A) :
    0 < h.binding := by
  rw [h.extensive]
  exact mul_pos heps (by exact_mod_cast Nat.choose_pos hA)

end QOU.Mass.CoordinationBinding
