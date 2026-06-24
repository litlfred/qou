# Partial formal proof of confinement-NF-structure-forcing

**Proposition (partial proof, conditional on
[`def:lp-duality-hypothesis-class`](lp-duality-hypothesis-class.md)
per AGENTS.md §3b-cond).**
*The three claims of [`conj:confinement-nf-structure-forcing`](#conj:confinement-nf-structure-forcing)
decompose as follows.*

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
   of $\rho_\lambda(I)$ — scalar form proved in
   [scalar audit](../../../docs/audits/-sub-lemma-2-1-categorical-proof.md);
   operator-valued form closed conditional on
   [`conj:crystal-graph-realization`](crystal-graph-realization.md)
   via the combinatorial $R$-matrix on $B_\mu \otimes B_\nu$ at
   $q \to 0$ — see
   [crystal audit](../../../docs/audits/-crystal-r-matrix-sublemma-2-1.md)).

3. *(Strong duality, $T_3$.)*
   $\mathrm{duality\_gap}(\beta) = 0$.
   **Fully proved** by the standard finite-dim LP strong-duality
   theorem (Schrijver §7.2); the QOU operator-selection LP is
   bounded (Wedderburn dimension is finite) and feasible (the
   trivial primal point exists).

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

matching the empirical W-3 closed form $D(u) = 2^{2A+1} \cdot u^{18Z + 21N + 1} \cdot (1+u^2)^{3A-1}$ exactly.
