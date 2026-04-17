The **$q$-Casimir element** is the distinguished central element of the
quantum group $\mathcal{U}_q(\mathfrak{su}(2))$ (cf.
[def:quantum-su2](#def:quantum-su2)) whose eigenvalue on the spin-$j$
irreducible encodes the categorical $q$-angular momentum.

**Definition.**
Inside $\mathcal{U}_q(\mathfrak{su}(2))$ with generators $E, F, K,
K^{-1}$ and parameter $q \neq 1$, the **$q$-Casimir element** is

$$
  C_q  =  F E  +  \frac{q\,K + q^{-1} K^{-1}}{(q - q^{-1})^2}
      =  E F  +  \frac{q^{-1}\,K + q\,K^{-1}}{(q - q^{-1})^2}.
$$

Both expressions coincide as elements of
$\mathcal{U}_q(\mathfrak{su}(2))$, because the commutation relation
$[E, F] = (K - K^{-1})/(q - q^{-1})$ rearranges the quadratic part.
The element is **central**: it commutes with each generator, i.e.
$C_q E = E C_q$, $C_q F = F C_q$, and $C_q K = K C_q$.

**Action on the spin-$j$ representation.**
On the $(2j+1)$-dimensional highest-weight module $V_j$ of
$\mathcal{U}_q(\mathfrak{su}(2))$, the central element acts as the
scalar

$$
  C_q \big|_{V_j}  =  [j]_q\,[j+1]_q\,\mathrm{id}_{V_j},
$$

which is the **$q$-Casimir eigenvalue** already defined as
`qCasimir` in [def:q-angular-momentum](#def:q-angular-momentum).
In the classical limit $q \to 1$ this recovers the usual Casimir
$C = F E + \tfrac12 H (\tfrac12 H + 1)$ with eigenvalue $j(j+1)$.

**Role in the categorical framework.**
Because $C_q$ is central, it descends to an endomorphism of the
identity functor on $\mathbf{Rep}(\mathrm{SU}_q(2))$ — equivalently,
a natural transformation $C_q \colon \mathrm{id} \Rightarrow \mathrm{id}$
whose component at each simple object $V_j$ is the scalar
$[j]_q[j+1]_q \cdot \mathrm{id}_{V_j}$. It is the categorical
incarnation of angular momentum squared in the rigid monoidal setting
of Chapter 3.
