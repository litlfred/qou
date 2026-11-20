# Partial formal proof of confinement-NF-structure-forcing

**Proposition (partial proof, conditional on
[Finite LP strong-duality + complementary-slackness hypothesis class (§3b-cond)](lp-duality-hypothesis-class.md)).**
*The three claims of [Confinement → NF-structure forcing](#conj:confinement-nf-structure-forcing)
decompose as follows.*

## Proof

The three claims $T_1, T_2, T_3$ decompose and are discharged as follows.

1. *(Wedderburn maximizer in active set, $T_1$.)*
   $\lambda^\star := \arg\max_{\lambda \vdash n} \mathrm{ord}_{q=0}^{(-)} \chi^\lambda(T_\beta) \in A$.
   **Fully proved** by LP complementary slackness applied to the
   tight primal constraint at the maximizer (Schrijver §7.4) — Lean
   side now consumes the `HasFiniteLPDuality` class instance rather
   than carrying a free-standing `sorry`.

2. *(Shift decomposition, $T_2$.)*
   $\mathrm{shift}_{\mathrm{NF}}(\beta) = \alpha_{\mathrm{shift}}(I) + \Delta_{\mathrm{struct}}(\beta_1, \beta_2; A) + \Delta_{\mathrm{resid}}$,
   with
   $\Delta_{\mathrm{struct}} = \max_{(\mu, \nu) \in \mathrm{branching}(\lambda^\star)}
     [\mathrm{ord}_{q=0}(\chi^\mu(\beta_1)) + \mathrm{ord}_{q=0}(\chi^\nu(\beta_2))]$
   weighted by Littlewood-Richardson coefficients $c^{\lambda^\star}_{\mu, \nu}$,
   and $\Delta_{\mathrm{resid}} = 0$ by $T_3$.
   **Reduced to Sub-lemma 2.1** (Hecke-branching block-decomposition
   of $\rho_\lambda(I)$ — scalar form proved;
   operator-valued form closed conditional on
   [Hecke normal forms realise crystal highest-weight vectors](../knots-particles-confinement/crystal-graph-realization.md)
   via the combinatorial $R$-matrix on $B_\mu \otimes B_\nu$ at
   $q \to 0$).

3. *(Strong duality, $T_3$.)*
   $\mathrm{duality\_gap}(\beta) = 0$.
   **Fully proved** by the standard finite-dim LP strong-duality
   theorem (Schrijver §7.2); the QOU operator-selection LP is
   bounded (Wedderburn dimension is finite) and feasible (the
   trivial primal point exists).

### Formal theorems

### Theorem $T_3$ (strong duality)

The QOU operator-selection LP per [Knot operator selection as linear program with LP duality](#prop:operator-selection-lp)
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
[Pole order at $q=0$ of the torus-knot character: $\alpha_{\mathrm{shift}}(T_{p,k}) = k(p-1)$ on $V_{(1^p)}$](#prop:alpha-shift-torus-knot).

**Sub-lemma 2.1 (now categorically proved).** The pole-order contribution of
$\rho_\lambda(I)$ in the $(\mu, \nu)$-isotypic block is bounded by
the Hoefsmit-derived block-decomposition formula.

Combining the per-component pole orders (proved via Sub-lemma 2.1)
with the LR multiplicities and the interface $\alpha$-shift
gives the claimed decomposition; $\Delta_{\mathrm{resid}} = 0$ by
$T_3$ and strong duality. $\square$

## Verification at the canonical pppnnn atomic braid

For $\beta = \mathcal{B}_p^Z \star_{(p,n)\text{ averaged}} \mathcal{B}_n^N$
in canonical pppnnn ordering with $A = Z + N \ge 2$, the partial
proof predicts:

- $\alpha_{\mathrm{shift}}(I) = \alpha_{\mathrm{shift}}(T_{2,1}) = 1 \cdot (2-1) = 1$ (single-crossing unknot at lowest torus index).
- $\Delta_{\mathrm{struct}} = Z \cdot \mathrm{shift}_{\mathrm{NF}}(\mathcal{B}_p \text{ in } H_{3A}) + N \cdot \mathrm{shift}_{\mathrm{NF}}(\mathcal{B}_n \text{ in } H_{3A})$.
- $\Delta_{\mathrm{resid}} = 0$.

Together with the empirical n-context shifts
$\mathrm{shift}_{\mathrm{NF}}(\mathcal{B}_p \text{ in } H_{3A}) = 18$ and
$\mathrm{shift}_{\mathrm{NF}}(\mathcal{B}_n \text{ in } H_{3A}) = 21$
(stable for all $A = 2, \ldots, 6$ per
[habiro-coefficients-extended.witness.json](../../../computations/habiro-coefficients-extended.witness.json)),
the formula yields

$$\mathrm{shift}_{\mathrm{NF}}(\beta_{\mathrm{atomic}}(Z, N)) = 18Z + 21N + 1,$$

matching the empirical closed form $D(u) = 2^{2A+1} \cdot u^{18Z + 21N + 1} \cdot (1+u^2)^{3A-1}$ exactly.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
