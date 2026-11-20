## Structural constraint

The full-twist $\Delta_n^2$ acts on each Wedderburn block $V_\lambda$ of $H_n(q)$ by the central scalar $q^{c(\lambda)}$, where $c(\lambda) = \sum_{x \in \lambda}(j_x - i_x)$ provides the content sum of the partition $\lambda \vdash n$ \cite{geckpfeiffer2000, mathas1999}. Trivial action of the full-twist on $\Phi_n$ restricts the partitions in the Wedderburn decomposition of $\Phi_n$ to those with content sum zero. These form the self-conjugate partitions $\lambda = \lambda'$ on Young's lattice. At saturated $n$, $\Phi_n$ finds support strictly on self-conjugate partitions.

For $n \notin \mathfrak{M}$, the constraint fails. Non-self-conjugate partitions enter $\Phi_n$, and the full-twist acts by a non-trivial scalar. This transition formalizes shell closure, replacing ad hoc selection rules with categorical constraints.

## Homological reformulation

The Hoefsmit seminormal form ([prop:hoefsmit-seminormal-form](#prop:hoefsmit-seminormal-form)) supplies explicit matrices for $\sigma_i$ on each $V_\lambda$. Direct multiplication recovers the full-twist eigenvalue $q^{c(\lambda)}$. Numerical verification at $k = 3, \dots, 10$ confirms the shell pattern at small magic values $n = 2, 8, 20$. At $k \geq 12$, combinatorial growth in $|\{\lambda \vdash n\}|$ blocks matrix evaluation.

The conjecture reformulates this homologically. Instead of verifying $\Phi_n$ with matrices, we verify the self-conjugate-support condition via content-sum arithmetic. This approach accesses saturation at $n \in \{50, 82, 126\}$ without matrix multiplication.

## Global topological neutrality

Earlier models ([atom-knot-mass-derivation](#conj:atom-knot-mass-derivation)) treated $\Phi_n$ as a local object. They required "screening" or "local trivialisation" to explain shell closure. This refactor abandons the locality assumption. We identify $\Phi_n$ as the global section of the mass functor over $\mathbf{C}$ ([rem:phi-n-global-section](#rem:phi-n-global-section)). A non-trivial full-twist action propagates unbounded ribbon flux through the brane tower. Finite observable mass demands global topological neutrality at saturation.

## Operator-level support

The claim that $\Phi_n$ receives support on self-conjugate partitions applies at the operator level. The categorical mass operator $\Phi_n$ exhibits zero matrix entries on every non-self-conjugate isotypical component in $H_n(q) = \bigoplus_\lambda \mathrm{End}(V_\lambda)$.

This does not imply the Plancherel-weighted character sum:

$$
\sum_{\lambda = \lambda'} w_\lambda \cdot \chi^\lambda(\beta_{\mathrm{atom}}).
$$

The character sum vanishes identically at certain atomic-braid cycle types. The binding-energy enhancement at magic shells derives from the non-vanishing of $\Phi_n$ on the self-conjugate isotypical operator blocks. Empirically, the GS-filtration Term 6 plus an `is_magic_pair` operator-correction captures the magic-shell signal, correlating at $+0.74$ to the AME residual.

## Discussion

Numerical witnesses at $k = 3, \dots, 10$ support the saturation condition. The conjecture extends this to all $n \in \mathfrak{M}$, including the high-mass region $\{50, 82, 126\}$.

The downstream cone includes [`conj:magic-numbers-from-q`](#conj:magic-numbers-from-q) and the shell-closure portion of the BW formula ([`thm:wedderburn-mass-formula`](#thm:wedderburn-mass-formula)). Proving these requires either a derivation of this conjecture or its retention as a class-axiomatised input.
