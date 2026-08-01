import Mathlib.Topology.Instances.Real.Lemmas

/-!
# QOU.BraidKnot.jet_convergence_classical_limit — conjectural class (§3b)

**§3b class axiomatisation** for content block
[`conj:jet-convergence-classical-limit`](../../../quantum-observable-universe/mass-theory/jet-convergence-classical-limit.md):
*The jet-filtered per-level knot invariant $a_k(\beta)$ converges to the
$q$-dimension-weighted average $a_\infty(\beta)$ as $k \to \infty$ (Part
C; Parts A/B are proved in the manuscript).*

This is a **conjecture**: the class carries the conjecture's actual
content as the `converges` field; the `noncomputable instance`'s `sorry`
represents the open conjecture itself (per AGENTS.md §3b), NOT a missing
proof.

**Mathlib-infra pass (2026-06-25).** The convergence is now the *real*
Mathlib `Filter.Tendsto … atTop (nhds aInfty)` (the standard sequential
limit on `ℝ`), replacing the hand-rolled $\varepsilon$–$N$ statement. The
manuscript gives an $O(1/\sqrt{k})$ rate (Kerov $q$-hook walk /
Féray–Méliot $q$-Plancherel CLT); here only the bare limit is encoded.
-/

namespace QOU.BraidKnot

open Filter Topology

/-- **Jet-convergence classical limit** $a_k(\beta) \to a_\infty(\beta)$.

    Conjectural class — see
    [`conj:jet-convergence-classical-limit`](../../../quantum-observable-universe/mass-theory/jet-convergence-classical-limit.md). -/
class jet_convergence_classical_limit where
  /-- Per-jet-level knot invariant $a_k(\beta)$. -/
  a : ℕ → ℝ
  /-- The limiting $q$-dimension-weighted average $a_\infty(\beta)$. -/
  aInfty : ℝ
  /-- **The conjecture** (Part C): $a_k \to a_\infty$ as $k \to \infty$,
      as the real Mathlib sequential limit. -/
  converges : Filter.Tendsto a Filter.atTop (nhds aInfty)

-- The conjecture itself: the specific per-level invariant `a_k(β)`
-- converges to the q-dimension-weighted average `a_∞(β)`.  Per AGENTS.md
-- §3b-cond we provide NO global instance.
--
-- History (bean cj8c): an earlier revision discharged this class with a
-- FABRICATED trivial instance `⟨fun _ => 0, 0, tendsto_const_nhds⟩` — the
-- constant-zero sequence, which trivially converges.  That is an
-- audit-dodge (§1a / §3b-tax: do not fabricate a trivial instance to
-- "close" an open conjecture): the class's freely-chosen data fields make
-- it satisfiable by a convenient sequence, so a fabricated instance
-- asserts nothing about the *actual* `a_k(β)`.  Removed here — the honest
-- open state is a content-bearing class with no instance, matching the
-- sibling `jet_filtered_knot_factor`.
-- Ref: [manuscript] quantum-observable-universe/mass-theory/jet-convergence-classical-limit.ts

end QOU.BraidKnot
