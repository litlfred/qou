import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.ground_state_ordering

**Canonical declaration** for content block
[`prop:ground-state-ordering`](../../../quantum-observable-universe/particle-interactions/ground-state-ordering.md): *Ground-state ordering from transfer matrix eigenvalues*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.ParticleInteractions


/-- Abstract context for the `ground_state_ordering` claim —
    manuscript-themed typed fields below; the ground-state ordering
    is selected by the transfer-matrix eigenvalues `λ_±` and the
    Z, N counts.

    §7c base ring: the claim's only arithmetic is the Vieta product
    `λ₊ · λ₋ = -1`, which needs a `Ring` and nothing more — no
    ordering on the eigenvalues, no square root, no archimedean
    construct. The `Z ≤ N`, `4 ≤ A`, `A ≤ 3` comparisons are over
    `ℕ`, not over the eigenvalue carrier. The carrier is therefore a
    type variable `R`; the archimedean realisation is `R := ℝ`. -/
class GroundStateOrderingContext (R : Type*) [Ring R] where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Mass number `A = Z + N`. -/
  A : ℕ
  A_eq : A = Z + N
  /-- Substrate parameter `q`, in the generic base ring. -/
  q : R
  /-- Transfer-matrix dominant eigenvalue (`T_pp`). -/
  lam_plus : R
  /-- Transfer-matrix subdominant eigenvalue (`T_pp`). -/
  lam_minus : R
  /-- The ground-state ordering at position `k`: `1` = proton,
      `0` = neutron. -/
  ordering : ℕ → ℕ

/-- **REFUTED — retained only as the historical statement** (bean `qou-48is`,
    2026-08-09).  The two ordering conjuncts below are **false**: an
    exhaustive `Φ_q` sweep over every `C(A,Z)` arrangement for `A ≤ 16` at
    the experimental (proton) anchor shows the interleaved + tail-packed
    arrangement is not the minimiser for `A ≥ 4` (it is the strict
    *maximiser* at `A = 5, Z = 1`), and the `A ≤ 3` conjunct fails as stated
    at `A = 2`.  The counterexample is proved sorry-free, for an interval of
    `q` containing the anchor, in
    `QOU.MassTheory.GroundStateOrderingRefutation.prescribed_not_minimiser_A5`;
    the third conjunct (`λ₊ · λ₋ = -1`) survives and is proved there as
    `transferEigen_vieta`.  This `def` names the historical claim and is not
    asserted; **do not** attempt to discharge it.  See
    `docs/audits/2026-08-09-ground-state-ordering-truth-value.md`.

    **Original proposition statement** (from manuscript):

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
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/ground-state-ordering.ts
def ground_state_ordering {R : Type*} [Ring R] (ctx : GroundStateOrderingContext R) : Prop :=
    (ctx.Z ≤ ctx.N → 4 ≤ ctx.A →
      ∀ k : ℕ, ctx.ordering k =
        if k % 2 = 1 ∧ k < 2 * ctx.Z then 1 else 0) ∧
    (ctx.A ≤ 3 → ∀ k : ℕ, k < ctx.Z → ctx.ordering k = 1) ∧
    ctx.lam_plus * ctx.lam_minus = -1

end QOU.ParticleInteractions
