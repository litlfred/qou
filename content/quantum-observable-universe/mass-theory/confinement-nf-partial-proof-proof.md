### Theorem $T_3$ (strong duality)

The QOU operator-selection LP per [`prop:operator-selection-lp`](#prop:operator-selection-lp)
is a finite-dim convex program over partitions of $n$. We verify:

- **Bounded.** Variables $t_\lambda \ge 0$ for $\lambda \vdash n$,
  bounded above by the normalisation constraint
  $\sum_\lambda t_\lambda \le 1$. The objective is linear in
  bounded coefficients, so achieves its maximum on a compact
  polytope.
- **Feasible.** The trivial point $t_\lambda = 0\ \forall \lambda$
  (or $t_\lambda = 1/p(n)$ for the $\sum_\lambda t_\lambda = 1$
  variant) satisfies all non-negativity constraints; the
  identity element gives a feasible primal point.

Bounded and feasible LP $\Rightarrow$ strong duality
$\Rightarrow \mathrm{duality\_gap} = 0$. $\square$

### Theorem $T_1$ (Wedderburn maximizer in active set)

By LP complementary slackness applied to the operator-selection LP:
$$y_\lambda^* > 0 \iff \text{the primal constraint for } \lambda \text{ is tight at the optimum.}$$

The Wedderburn-maximizer constraint
$\mathrm{ord}_{q=0}^{(-)} \chi^\lambda(T_\beta) \le M^*$
is tight at $\lambda^\star$ (the maximizer achieves the LP optimum
$M^*$).  By complementary slackness, $y_{\lambda^\star}^* > 0$,
hence $\lambda^\star \in A$. $\square$

### Theorem $T_2$ (shift decomposition, conditional on Sub-lemma 2.1)

The Markov-trace shift is, by Wedderburn,

$$\mathrm{ord}_{q=0}(\mathrm{tr}_M(T_\beta)) = \max_{\lambda \in A} \mathrm{ord}_{q=0}(y_\lambda \cdot \chi^\lambda(T_\beta)),$$

with the maximum achieved at $\lambda = \lambda^\star \in A$ by $T_1$.

For the compound braid $\beta = \beta_1 \star_I \beta_2$, the
Hecke-branching rule decomposes $\rho_{\lambda^\star} \downarrow_{H_{n_1} \times H_{n_2}}$
as $\bigoplus_{(\mu, \nu)} c^{\lambda^\star}_{\mu, \nu}\,\rho_\mu \otimes \rho_\nu$.
Components $\beta_1, \beta_2$ act block-diagonally in this
decomposition (each on its disjoint strand set); the interface
$I$ acts on the boundary strands and contributes the
$\alpha_{\mathrm{shift}}(I)$ term per
[`prop:alpha-shift-torus-knot`](#prop:alpha-shift-torus-knot).

**Sub-lemma 2.1 (now categorically proved).** The pole-order contribution of
$\rho_\lambda(I)$ in the $(\mu, \nu)$-isotypic block is bounded by
the Hoefsmit-derived block-decomposition formula.  See
[full categorical proof](../../../docs/audits/-sub-lemma-2-1-categorical-proof.md).

Combining the per-component pole orders (proved via Sub-lemma 2.1)
with the LR multiplicities and the interface $\alpha$-shift
gives the claimed decomposition; $\Delta_{\mathrm{resid}} = 0$ by
$T_3$ and strong duality. $\square$
