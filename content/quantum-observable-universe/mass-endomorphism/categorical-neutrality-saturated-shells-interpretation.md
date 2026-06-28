## Why this is structural, not a matrix identity

The full-twist $\Delta_n^2$ acts on each Wedderburn block $V_\lambda$
of $H_n(q)$ by the central scalar $q^{c(\lambda)}$, where
$c(\lambda) = \sum_{x \in \lambda}(j_x - i_x)$ is the **content sum**
of the partition $\lambda \vdash n$ \cite{geckpfeiffer2000,
mathas1999}. Trivial action of the full-twist on $\Phi_n$ therefore
constrains the partitions that appear in the Wedderburn decomposition
of $\Phi_n$ to those with content sum zero — the **self-conjugate**
partitions $\lambda = \lambda'$ on Young's lattice. The statement is
that *at saturated $n$, $\Phi_n$ is supported on
self-conjugate partitions*.

For $n \notin \mathfrak{M}$ the constraint fails — non-self-conjugate
partitions enter $\Phi_n$ and the full-twist acts by a non-trivial
scalar. The transition from "supported on self-conjugates only" to
"non-trivial full-twist action" is the categorical content of shell
closure, replacing the *ad hoc* shell-model selection rule.

## Relation to the Hoefsmit / matrix-evaluation programme

The Hoefsmit seminormal form
([prop:hoefsmit-seminormal-form](#prop\:hoefsmit-seminormal-form))
gives explicit matrices for $\sigma_i$ on each $V_\lambda$, with the
full-twist eigenvalue $q^{c(\lambda)}$ recoverable by direct
multiplication. Numerical verification at $k = 3, \dots, 10$ confirms
the predicted shell pattern at the small magic values $n = 2, 8, 20$;
combinatorial growth in $|\{\lambda \vdash n\}|$ blocks the
matrix-evaluation approach at $k \geq 12$. The conjecture above is
the **homological reformulation** of the same statement: instead of
verifying $\Phi_n$ at each $n$ by matrices, one verifies the
self-conjugate-support condition by content-sum arithmetic. Saturation
at $n \in \{50, 82, 126\}$ then follows without resort to matrices.

## Locality assumption: dropped

Earlier formulations
([atom-knot-mass-derivation](#prop\:atom-knot-mass-derivation))
treated $\Phi_n$ as a *local* object — defined per-vortex and
combined by tensor product. In that setting "screening" or "local
trivialisation" was needed to explain shell closure. The refactor
drops the locality assumption: $\Phi_n$ is the **global section** of
the mass functor over $\mathbf{C}$
([rem:phi-n-global-section](#rem\:phi-n-global-section)). A
non-trivial full-twist action would propagate unbounded ribbon /
framing flux through the brane tower; finite observable mass forces
**global topological neutrality** at saturation.

## Operator-level support vs character sum (clarification)

The phrase *"$\Phi_n$ is supported on self-conjugate partitions"*
in this block means **operator-level**: the categorical mass
operator $\Phi_n$ has zero matrix entries on every
non-self-conjugate isotypical component of the Wedderburn
decomposition $H_n(q) = \bigoplus_\lambda \mathrm{End}(V_\lambda)$.
It does **not** mean the Plancherel-weighted character sum

$$
\sum_{\lambda = \lambda'} w_\lambda \cdot \chi^\lambda(\beta_{\mathrm{atom}}).
$$

The character sum vanishes identically at certain atomic-braid
cycle types (a representation-theoretic identity, invariant under
any per-$\lambda$ positive Plancherel weight). The binding-energy
enhancement at magic shells is the *non-vanishing* of $\Phi_n$ on
the self-conjugate isotypical operator blocks — not the
character sum. Empirically, the magic-shell signal is captured
by the GS-filtration Term 6 plus an `is_magic_pair`
operator-correction with correlation $+0.74$ to the AME residual
([reframing memo](../../../docs/audits/-self-conj-support-reframing.md)).

## Discussion

**Status: conjectural** under AGENTS.md §3b. Numerical witnesses at
$k = 3, \dots, 10$ are supportive but not a proof; the conjecture
asserts the saturation condition for all $n \in \mathfrak{M}$
including $\{50, 82, 126\}$ where matrix-evaluation is unavailable.

The downstream cone (per the
[ conjecture-cones audit](../../../docs/audits/conjecture-cones.md))
is anticipated to include
[`prop:magic-numbers-from-q`](#prop\:magic-numbers-from-q) and the
shell-closure portion of the BW formula
([`thm:wedderburn-mass-formula`](#thm\:wedderburn-mass-formula)).
Per §3b the upgrade of these to fully provable status requires
either a derivation of this conjecture or its retention as a
class-axiomatised input to a conditional theorem.
