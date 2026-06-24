*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
Let $\mathcal{X}_5 \colon y^2 = x^5 - 1$ be the hyperelliptic quintic
of Definition [def:hyperelliptic-quintic](#def:hyperelliptic-quintic).
The map

$$
  \phi_5 \colon \mathcal{X}_5 \longrightarrow \mathcal{X}_5,
  \qquad
  \phi_5(x, y)  =  (\zeta_5 x,\, y),
  \qquad
  \zeta_5  =  e^{2\pi i/5},
$$

is an automorphism of $\mathcal{X}_5$ of order $5$.  It generates
a cyclic group $\langle \phi_5 \rangle \cong \mathbb{Z}_5$ inside
$\mathrm{Aut}(\mathcal{X}_5)$.

**Interpretation.**  Under the identification of $x$ with the first
Lagrange resolvent $w_1$ (Remark
[rem:lagrange-resolvents](#rem:lagrange-resolvents)), the automorphism
$\phi_5$ is the diagonalised action of the cyclic generator $\sigma$ on
$w_1$ via $\phi_5 \leftrightarrow \sigma$ with $\sigma(w_1) = \zeta_5^{-1} w_1$.
The orbit $\{x, \zeta_5 x, \zeta_5^{2} x, \zeta_5^{3} x, \zeta_5^{4} x\}$
is a single $\mathbb{Z}_5$-orbit of size five, matching the five finite
branch points of the double cover.
