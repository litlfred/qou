**Definition.**
*For two partitions $\lambda_1, \lambda_2$ with shadow prices
$y_{\lambda_1}(q), y_{\lambda_2}(q) \in R$, the **local shadow-price
ordering** at $q$ is:*

$$
  \lambda_1 \;\preceq_q\; \lambda_2
  \;\iff\;
  \exists\, U \ni q\;\text{open such that}\;
  |y_{\lambda_1}(q')| \;\leq\; |y_{\lambda_2}(q')|
  \;\;\forall q' \in U.
$$

*Read: "$\lambda_1$ has at most the energy of $\lambda_2$ on a
neighborhood of $q$".*

**Continuity.**
*Each shadow price $u_\lambda(q) = w_\lambda(q)/d_\lambda(q) -
1/[k]_q!$ is a **rational function** of $q$ over the base ring,
with denominator $[k]_q! \cdot d_\lambda(q)$.  On the generic
locus $\{q : [k]_q! \cdot d_\lambda(q) \neq 0\}$, $u_\lambda$ is
continuous in $q$ (smooth in the $\mathbb{R}$ realisation,
$p$-adic continuous in $\mathbb{Q}_p$, well-defined Zariski
on $\mathbb{F}_p$).*

*By continuity, if $|y_{\lambda_1}(q)| < |y_{\lambda_2}(q)|$
strictly, then $\lambda_1 \preceq_q \lambda_2$ holds on a
neighborhood.*

**Boundary variety.**
*The locus*

$$
  \mathcal{B}_{\lambda_1, \lambda_2}
  \;:=\;
  \{q \in Q : |y_{\lambda_1}(q)| = |y_{\lambda_2}(q)|\}
$$

*is a **Zariski-closed** subvariety of $Q$, generically of
codimension $\geq 1$ (defined by the polynomial equation
$y_{\lambda_1}^2(q) = y_{\lambda_2}^2(q)$).  The full **phase-
boundary variety** is*

$$
  \mathcal{B}
  \;:=\;
  \bigcup_{\lambda_1 \neq \lambda_2}
    \mathcal{B}_{\lambda_1, \lambda_2}
  \;\cup\;
  \bigcup_\lambda
    \{q : u_\lambda(q) = 0\},
$$

*the union of pairwise-equality varieties and shadow-price-vanishing
varieties.  $\mathcal{B}$ is measure-zero in $Q$.*

**Local constancy of confinement.**
*The [confinement level](#def:confinement-level) $\ell(K, q)$ is
**locally constant** on $Q \setminus \mathcal{B}$: for any $q
\notin \mathcal{B}$, there is an open $U \ni q$ such that
$\ell(K, q') = \ell(K, q)$ for all $q' \in U$.  The level changes
only at points of $\mathcal{B}$ — these are exactly the
**categorical phase boundaries**.*

**Computational shortcut.**
*Per [unstable-atom](#def:unstable-atom) "Computational shortcut",
expensive computations (per-generator $\hat V_i^{\mathrm{full}}$
extraction in the tower formula
[mass-endomorphism-tower](#prop:mass-endomorphism-tower)) need
exact evaluation only at points of $\mathcal{B}$.  In the
complement $Q \setminus \mathcal{B}$, all shadow prices, the
filtration, and the per-generator data are locally constant —
linear interpolation between nearest magic-number anchors is
mathematically justified.*
