Let $X$ be a compact Riemann surface of genus $g \geq 2$, let $K$ be its canonical bundle, and let $L$ be a holomorphic line bundle of degree $d$. For $n \geq 1$ the jet bundles fit into exact sequences
$$
  0 \longrightarrow K^n \otimes L
    \longrightarrow J^n L
    \longrightarrow J^{n-1} L
    \longrightarrow 0 .
$$
Each extension class $e_n$ lies in $\mathrm{Ext}^1(J^{n-1}L, K^n \otimes L)$. The group $\mathrm{Ext}^1(J^{n-1}L, K^n \otimes L)$ is filtered by the bundles $K^m$ with $1 \leq m \leq n$. By Serre duality $H^1(X, K^m) = 0$ for $m \geq 2$, and $H^1(X, K) \cong \mathbb{C}$. Hence the group is one-dimensional, and $e_n$ is a single scalar,
$$
  e_n = c \cdot n \bigl( d + (n-1)(g-1) \bigr),
$$
for a non-zero universal constant $c$. At $n = 1$ this is the Atiyah class, proportional to $d$. At $n = 2$ with $L = K^{-1/2}$ it vanishes, which is the existence of projective structures. In general it vanishes exactly when $L = K^{-(n-1)/2}$, where Bol's operators of order $n$ exist.

For the tangent bundle of Bring's surface, $g = 4$ and $d = -6$, so $e_n \propto 3n(n-3)$. The holomorphic jet tower of the tangent bundle fails to split at every level except $n = 3$, where it splits. In the smooth category every $e_n$ vanishes, because the relevant sheaves are fine.

The classes $e_n$ are extension classes in degree $1$. They obstruct a splitting of the tower rather than the existence of the next level. They are therefore not the obstructions $\kappa_n$ of the [QU-to-QOU theorem](#thm:qu-to-qou), whose persistence statement is the Kummer form in item 3.
