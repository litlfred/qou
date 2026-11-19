Each row names a content block in which measure-theoretic language — Lebesgue, Haar, or Hausdorff — occurs, and records what the argument actually uses. Only [the Möbius energy proof](#prf:mobius-energy) performs a genuine measure computation; every other reference invokes the language by analogy over an object that is categorical, algebraic, or given by a rational formula.

| Reference | What is actually used |
|---|---|
| [Frobenius integration](#sec:frobenius-integration) | Calls $\int_A$ a "categorical Haar measure" *by analogy*. The actual object is the Frobenius counit $A \to \mathbf{1}$, purely categorical — survives over any field. |
| [categorical Laplace transform](#def:categorical-laplace) | Compares to Haar on $\mathbb{R}_{\geq 0}$ as motivation; the categorical Laplace transform is defined over any ground ring. |
| [Julia set and Reeb dynamics](#rem:julia-set-reeb) | Mentions the Julia measure $\mu_J$ and Hausdorff dimension $d_H(q)$. The dimension is given by the **rational formula** $d_H(q) = (2q-1)^2/q^3$ (see [birthday grading](#def:birthday-grading)), so it lifts to $\mathbf{No}$ exactly. The measure itself is used only for intuitive language. |
| [statistical-mechanical time](#rem:statistical-mechanical-time), [double-slit two-mode decomposition](#rem:double-slit-two-modes) | Interpretive prose; no measure-theoretic computation is performed. |
| [Möbius energy proof](#prf:mobius-energy) | **Genuine use.** The Möbius energy integral $\int_{S^1 \times S^1} d\ell(x) d\ell(y) / |x - y|^2$ uses the Lebesgue measure on $S^1$, with diagonal regularisation. |
