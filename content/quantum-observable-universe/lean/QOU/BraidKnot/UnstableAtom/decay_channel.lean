import Mathlib.Tactic

/-!
# QOU.BraidKnot.UnstableAtom.decay_channel

**Placeholder canonical** for content block at
[`quantum-observable-universe/braids-and-knots/unstable-atom-decay-channel.ts`](quantum-observable-universe/braids-and-knots/unstable-atom-decay-channel.ts).

The full Lean statement is pending; this stub exists so the
`lean.ref` URI `qou:QOU.BraidKnot.UnstableAtom.decay_channel` resolves to a real declaration in the `qou`
Lake package.
-/

namespace QOU.BraidKnot.UnstableAtom


/-- Abstract context for the `decay_channel` claim — manuscript-themed
    typed fields below; sub-claims encode (i) well-definedness of the
    decay channel `λ*(K, q)`, (ii) uniqueness off the boundary variety,
    and (iii) the phase-boundary crossing condition. -/
class DecayChannelContext where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- Partition / Young-diagram indexing. -/
  PartitionIdx : Type
  /-- The decay-channel partition `λ*(K, q) : PartitionIdx`. -/
  lam_star : PartitionIdx
  /-- Energy `E(λ, q)` of constraint-violation at partition `λ`. -/
  E_lambda : ℝ
  /-- Manuscript sub-claim (i) — `λ*` is well-defined whenever the
      atom is unstable (energy is non-zero at `q`). -/
  claim_i_well_defined : E_lambda ≠ 0
  /-- Predicate: `q` is on the boundary variety `{q : E(λ*, q) = 0}`. -/
  on_boundary : ℝ → Prop
  /-- A candidate alternative decay-channel partition `λ'`. -/
  lam_alt : PartitionIdx
  /-- Manuscript sub-claim (ii) — Uniqueness off the boundary variety:
      off the boundary, every alternative `λ'` that also minimises
      `E_λ` must coincide with `λ*`. -/
  claim_ii_unique_off_boundary : ¬ on_boundary q → lam_alt = lam_star
  /-- The two endpoints of the phase-crossing interval. -/
  q_1 : ℝ
  q_2 : ℝ
  /-- Manuscript sub-claim (iii) — Phase-boundary crossing: stable at
      `q_1`, unstable at `q_2` implies `∃ q* ∈ [q_1, q_2]` with
      `E(λ*, q*) = 0` (the boundary variety is crossed). -/
  claim_iii_phase_boundary_crossing :
    q_1 ≤ q ∧ q ≤ q_2 → ∃ q_star : ℝ, q_1 ≤ q_star ∧ q_star ≤ q_2 ∧
      on_boundary q_star

/-- **Manuscript statement** (full body):

**Proposition.**
*If atom-knot $K$ is [unstable](#def:unstable-atom) at $q$, then
the **decay channel** $\lambda^*(K, q)$ — the unique violated
constraint — is well-defined.*

*Proof.*
*Since $K$ is unstable, the ILP
$\{x \in \mathbb{Z}_{\geq 0}^N : G(q) x \geq 0\}$ has no
solution within the confinement filtration $J^{\ell(K, q)}(q)$.*

*Run the LP relaxation
$\{x \in \mathbb{R}_{\geq 0}^N : G(q) x \geq 0\}$.  This is
always feasible (the trivial $x = 0$ vector satisfies $G \cdot 0
= 0 \geq 0$, and the relaxation is the convex hull of integer
solutions).  Pick the unique optimal vertex $x^*_{LP} \in
\mathbb{R}_{\geq 0}^N$ closest to an integer point.*

*The **violated constraint** is*

$$
  \gamma^*(K, q)
  \;:=\;
  \arg\min_\gamma\;
    (G(q)\, \lceil x^*_{LP} \rceil)_\gamma,
$$

*the constraint with the smallest (most negative) Frobenius
positivity value at the rounded integer point.  By LP duality
([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)),
this corresponds to a unique partition $\lambda^*(K, q)$ — the
operator $e_{\lambda^*}$ that fails to satisfy positivity.*

*Uniqueness: if two distinct partitions $\lambda_1, \lambda_2$
both achieve the minimum at the same integer point, they have
identical shadow prices at $q$, i.e., $|y_{\lambda_1}(q)| =
|y_{\lambda_2}(q)|$ — these lie on the **boundary variety**
([local shadow ordering](#def:local-shadow-ordering)) of measure
zero.  Generically (off the boundary variety), $\lambda^*$ is
unique.  $\square$*

**Connection to phase boundary.**
*An atom that is stable at $q_1$ and unstable at $q_2$
necessarily crosses a $q^* \in [q_1, q_2]$ where
$E(\lambda^*, q^*) = |y_{\lambda^*}(q^*)| = 0$ — the LP
boundary for the violated constraint vanishes.  Crossing $q^*$
flips ILP feasibility.*

    The Lean encoding below splits the manuscript claim into named
    sub-claim fields; concretisation requires per-block manuscript
    translation. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/unstable-atom-decay-channel.ts
def decay_channel [ctx : DecayChannelContext] :
    ctx.E_lambda ≠ 0 ∧
    (¬ ctx.on_boundary ctx.q → ctx.lam_alt = ctx.lam_star) ∧
    (ctx.q_1 ≤ ctx.q ∧ ctx.q ≤ ctx.q_2 →
      ∃ q_star : ℝ, ctx.q_1 ≤ q_star ∧ q_star ≤ ctx.q_2 ∧
        ctx.on_boundary q_star) :=
  ⟨ctx.claim_i_well_defined, ctx.claim_ii_unique_off_boundary,
   ctx.claim_iii_phase_boundary_crossing⟩

end QOU.BraidKnot.UnstableAtom
