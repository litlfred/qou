/-!
# QOU.BraidKnot.UnstableAtom.decay_channel — placeholder stub

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
  λ_star : PartitionIdx
  /-- Manuscript sub-claim (i): the decay-channel partition is
      well-defined for any unstable atom-knot `K` at `q`. -/
  claim_i_well_defined : Prop
  /-- Manuscript sub-claim (ii): uniqueness off the boundary variety
      `{q : E(λ*, q) = 0}` of measure zero. -/
  claim_ii_unique_off_boundary : Prop
  /-- Manuscript sub-claim (iii): an atom stable at `q_1` and unstable
      at `q_2` necessarily crosses some `q* ∈ [q_1, q_2]` where
      `E(λ*, q*) = 0`. -/
  claim_iii_phase_boundary_crossing : Prop

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
theorem decay_channel [ctx : DecayChannelContext] :
    ctx.claim_i_well_defined ∧
    ctx.claim_ii_unique_off_boundary ∧
    ctx.claim_iii_phase_boundary_crossing :=
  ⟨ctx.claim_i_well_defined, ctx.claim_ii_unique_off_boundary,
   ctx.claim_iii_phase_boundary_crossing⟩

end QOU.BraidKnot.UnstableAtom
