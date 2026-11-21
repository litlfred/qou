One constructs the [direct limit algebra](#def:direct-limit-algebra) $A_\infty$ for $G = \mathrm{SU}(2)$ from the [brane tower for SU(2)](#ex:recursive-brane-tower-su2).

**The tower.** The recursive brane tower yields a sequence of jet-level endomorphism algebras:
$$
  \mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))
   \hookrightarrow 
  \mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2)))
   \hookrightarrow 
  \mathrm{End}(J^2\mathcal{O}(\mathrm{SU}(2)))
   \hookrightarrow  \cdots
$$
Jet prolongation maps $\ell_n \colon \mathrm{End}(J^n\mathcal{O}(\mathrm{SU}(2))) \hookrightarrow \mathrm{End}(J^{n+1}\mathcal{O}(\mathrm{SU}(2)))$ connect the levels. At level $n$, the algebra is $(3 + 3n)$-dimensional: $3$ dimensions from $\mathfrak{su}(2)$ and $3n$ dimensions from the $n$-th order cotangent directions.

**The direct limit.** The direct limit algebra is:
$$
  A_\infty
  =  \varinjlim_n \mathrm{End}(J^n\mathcal{O}(\mathrm{SU}(2)))),
$$
the union of all finite-order jet endomorphisms. An element of $A_\infty$ acts on jets of some finite order.

**Identification with differential operators.** Every element of $A_\infty$ is a finite-order left-invariant differential operator on $\mathrm{SU}(2)$. The direct limit coincides with the algebra $\mathcal{D}(\mathrm{SU}(2))^{\mathrm{SU}(2)}$ of left-invariant differential operators. By the Poincaré–Birkhoff–Witt theorem, this is isomorphic to the universal enveloping algebra $U(\mathfrak{su}(2))$:
$$
  A_\infty  \cong  U(\mathfrak{su}(2))
   \cong  \mathbb{C}\langle e_1, e_2, e_3 \rangle
  \big/ \bigl(e_a e_b - e_b e_a - \epsilon_{abc} e_c\bigr).
$$

**Filtration.** The jet order induces a filtration $A_\infty^{(0)} \subset A_\infty^{(1)} \subset \cdots$ with $A_\infty^{(n)} = \mathrm{End}(J^n\mathcal{O}(\mathrm{SU}(2)))$. The associated graded algebra is the symmetric algebra $\mathrm{gr}(A_\infty) \cong \mathrm{Sym}(\mathfrak{su}(2)^*) \cong \mathbb{C}[x_1, x_2, x_3]$ of polynomial functions on $\mathfrak{su}(2)$.
