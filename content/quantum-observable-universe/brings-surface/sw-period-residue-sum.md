Let $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a
branch point $z_c$ ([Bring's surface smoothness](#rem:brings-smoothness)), and
let $\lambda_{\mathrm{SW}}^{(n)}$ be the $n$-th prolonged Seiberg--Witten
differential of the
[MI--SW abelianisation](#prop:mi-sw-abelianisation). Because
$\lambda_{\mathrm{SW}}^{(n)}$ is a meromorphic $1$-form on the compact Riemann
surface $\mathcal{S}_c$, with poles only at the branch points, its period is the
sum of its residues:

$$
\oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}
\;=\;
2\pi i \sum_{p\,\in\,\mathcal{S}_c}\operatorname{Res}_p\,\lambda_{\mathrm{SW}}^{(n)}.
$$

In particular the prolonged Seiberg--Witten period
$a_D^{(n)} = \oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}$ is an **algebraic
residue sum**: it is evaluated by collecting the local residues at the
branch-point poles, with no contour integration required.

**Residue support and body order.** The residues are supported at the
branch-point poles, and the number of contributing poles is governed by the
vertical (jet) degree $n$: the $n$-th prolongation lifts the connection to the
$n$-jet bundle $J^n E$, so the residue family at level $n$ is indexed by the
weight data of rank $n$. The residue sum is therefore the natural carrier of the
**body-order grading** — the period at vertical degree $n$ is the $n$-body
contribution — and each residue is a per-block quantum-dimensional weight on the
Wedderburn decomposition restricted to that level.
