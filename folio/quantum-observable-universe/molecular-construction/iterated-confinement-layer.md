Let $K$ be a commutative ring equipped with a compatible linear order when inequalities are invoked, and let $d, m \in \mathbb{N}$.

1. A **confinement layer** $\mathcal{L} = (A, c, \mathcal{A})$ consists of an integer conserved-charge matrix $A \in \mathbb{Z}^{d \times m}$, a column cost vector $c \in K^m$ defining $c(z) := \sum_{j=1}^m z_j c_j$ on signed configurations $z \in \mathbb{Z}^m$, and an admissibility predicate $\mathcal{A} \subseteq \mathbb{N}^m$ on nonnegative column multiplicities.
2. Given dual shadow prices $y \in K^d$, the **reduced cost** of column $j \in \{1,\dots,m\}$ is
   $$
     \bar{c}(y)_j := c_j - \sum_{i=1}^d A_{ij} y_i.
   $$
3. A configuration $w \in \mathbb{N}^m$ is a **confined motif** of $\mathcal{L}$ if $w \neq 0$, $w \in \mathcal{A}$, and for every nontrivial decomposition into nonzero admissible configurations $u_1, u_2 \in \mathcal{A} \setminus \{0\}$ satisfying $A w = A u_1 + A u_2$, strict binding sub-additivity holds:
   $$
     c(w) < c(u_1) + c(u_2).
   $$
4. Given a selected family of $m'$ motifs $W = (w_1, \dots, w_{m'}) \in (\mathbb{N}^m)^{m'}$, a residual inter-motif cost shift $\delta c \in K^{m'}$, and a next-layer admissibility predicate $\mathcal{A}' \subseteq \mathbb{N}^{m'}$, **functorial column promotion** \cite{dantzig-wolfe1960,benders1962,deloera-hemmecke-koeppe2013} produces the next confinement layer $\mathcal{L}' = (A', c', \mathcal{A}')$ with
   $$
     A'_{i\alpha} := (A w_\alpha)_i,
     \qquad
     c'_\alpha := c(w_\alpha) + \delta c_\alpha
     \qquad (\alpha = 1,\dots,m'),
   $$
   and constituent expansion $\mathcal{E}_W(v)_j := \sum_{\alpha=1}^{m'} v_\alpha w_{\alpha,j}$ satisfying $A' v = A\,\mathcal{E}_W(v)$ for all $v \in \mathbb{Z}^{m'}$.
