Continuing the [brane tower for SU(2)](#ex:recursive-brane-tower-su2), we construct the [direct limit algebra](#def:direct-limit-algebra) $A_\infty$ for $G = \mathrm{SU}(2)$.

**The tower.** The recursive brane tower yields a sequence of jet-level endomorphism algebras

$$
  \mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))
   \hookrightarrow 
  \mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2)))
   \hookrightarrow 
  \mathrm{End}(J^2\mathcal{O}(\mathrm{SU}(2)))
   \hookrightarrow  \cdots
$$

connected by jet prolongation maps $\ell_n \colon \mathrm{End}(J^n\mathcal{O}(\mathrm{SU}(2))) \hookrightarrow \mathrm{End}(J^{n+1}\mathcal{O}(\mathrm{SU}(2)))$. At level $n$, the algebra is $(3 + 3n)$-dimensional: $3$ dimensions from $\mathfrak{su}(2)$ plus $3n$ from the $n$-th order cotangent directions.

**The direct limit.** The direct limit algebra is

$$
  A_\infty
  =  \varinjlim_n \mathrm{End}(J^n\mathcal{O}(\mathrm{SU}(2)))),
$$

the union of all finite-order jet endomorphisms. An element of $A_\infty$ acts on jets of some finite (but arbitrarily large) order.

**Identification with differential operators.** Every element of $A_\infty$ is a finite-order left-invariant differential operator on $\mathrm{SU}(2)$. The direct limit coincides with the algebra $\mathcal{D}(\mathrm{SU}(2))^{\mathrm{SU}(2)}$ of left-invariant differential operators, which is isomorphic to the universal enveloping algebra $U(\mathfrak{su}(2))$ by the Poincaré–Birkhoff–Witt theorem:

$$
  A_\infty  \cong  U(\mathfrak{su}(2))
   \cong  \mathbb{C}\langle e_1, e_2, e_3 \rangle
  \big/ \bigl(e_a e_b - e_b e_a - \epsilon_{abc} e_c\bigr).
$$

**Filtration.** The jet order induces a filtration $A_\infty^{(0)} \subset A_\infty^{(1)} \subset \cdots$ with $A_\infty^{(n)} = \mathrm{End}(J^n\mathcal{O}(\mathrm{SU}(2)))$. The associated graded is the symmetric algebra $\mathrm{gr}(A_\infty) \cong \mathrm{Sym}(\mathfrak{su}(2)^*) \cong \mathbb{C}[x_1, x_2, x_3]$, the algebra of polynomial functions on $\mathfrak{su}(2)$.
