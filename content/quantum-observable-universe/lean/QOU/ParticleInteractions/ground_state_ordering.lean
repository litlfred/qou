import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.ground_state_ordering

**Placeholder canonical** for content block
[`prop:ground-state-ordering`](../../../quantum-observable-universe/particle-interactions/ground-state-ordering.md): *Ground-state ordering from transfer matrix eigenvalues*.

The full Lean statement and proof are pending; this stub exists so
the `lean.ref` URI `qou:QOU.ParticleInteractions.ground_state_ordering` resolves to a real declaration in
the `qou` Lake package.  The body is `sorry` carrying the
manuscript citation per AGENTS.md §1.
-/

namespace QOU.ParticleInteractions


/-- Abstract context for the `ground_state_ordering` claim —
    manuscript-themed typed fields below; the ground-state ordering
    is selected by the transfer-matrix eigenvalues `λ_±` and the
    Z, N counts. -/
class GroundStateOrderingContext where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Mass number `A = Z + N`. -/
  A : ℕ
  A_eq : A = Z + N
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- Transfer-matrix dominant eigenvalue (`T_pp`). -/
  lam_plus : ℝ
  /-- Transfer-matrix subdominant eigenvalue (`T_pp`). -/
  lam_minus : ℝ
  /-- The ground-state ordering at position `k`: `1` = proton,
      `0` = neutron. -/
  ordering : ℕ → ℕ

/-- **Proposition statement** (from manuscript):

The nuclear ground state ordering for a nucleus with $Z$ protons
and $N$ neutrons ($A = Z + N$) is determined by:*

    The Lean encoding **names** the conditional conjecture as a `Prop`
    (pattern C of the vacuity-fix playbook): the context class is the
    carrier of the transfer-matrix / ordering data, and
    `ground_state_ordering` is the proposition that interleaving,
    boundary correction, and the Vieta eigenvalue product hold for that
    data.  It is *not* asserted (no `theorem … := ⟨ctx.claim_*⟩`
    self-assuming projection); a discharging instance is the open
    conditional claim. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/ground-state-ordering.ts
def ground_state_ordering (ctx : GroundStateOrderingContext) : Prop :=
    (ctx.Z ≤ ctx.N → 4 ≤ ctx.A →
      ∀ k : ℕ, ctx.ordering k =
        if k % 2 = 1 ∧ k < 2 * ctx.Z then 1 else 0) ∧
    (ctx.A ≤ 3 → ∀ k : ℕ, k < ctx.Z → ctx.ordering k = 1) ∧
    ctx.lam_plus * ctx.lam_minus = -1

end QOU.ParticleInteractions
