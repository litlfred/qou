**Proof.**
The argument proceeds in two steps, combined to identify $G$.

By ([volume determinant](#lem:su2-emergence-volume-determinant)), the
volume constraint $\epsilon \colon \Lambda^2 V \to \mathbf{1}$ together
with naturality of $g \in G$ forces $\det(g_V) = 1$, restricting the
natural automorphisms from $\mathrm{GL}(2)$ to $\mathrm{SL}(2)$.

By ([dagger unitarity](#lem:su2-emergence-dagger-unitarity)), the
non-degenerate Frobenius form $\int_A$ induces a positive-definite
dagger structure preserved by every $g \in G$, giving $G \subseteq
\mathrm{U}(2)$.

Combining both constraints:

$$
  G =  \mathrm{SL}(2) \cap \mathrm{U}(2)
  =  \mathrm{SU}(2).
$$

The volume constraint provides the special-linear condition
($\det = 1$); the positive-definite dagger structure provides
the compactness (unitarity). $\square$
