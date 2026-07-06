Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe and let
$\{A_n\}_{n \geq 0}$ be its
([recursive brane tower](#def:recursive-brane-tower)); let $q$ denote the substrate parameter.  Equipped with the Yekutieli
triples $(x^{(n)}, g^{(n)}, a^{(n)})$ of
[Yekutieli triple](#def:yekutieli-triple).  Then the assignment

$$
  [n]  \longmapsto  \mathfrak{G}_n
$$

from the simplex category $\Delta$ to the $2$-category of gerbes on $M$
extends to a *cosimplicial crossed groupoid*: a cosimplicial object
in the category of crossed groupoids, where

1. the coface maps $\delta^i \colon \mathfrak{G}_{n} \to \mathfrak{G}_{n+1}$ are given by the jet prolongation acting on
   objects (inserting the $i$-th degeneracy in the Cech nerve),
2. the codegeneracy maps $\sigma^j \colon \mathfrak{G}_{n+1} \to \mathfrak{G}_{n}$ are given by the :refterm[descent]{#descent} homomorphism
   $\mathfrak{d}_{n+1}$ (collapsing the $j$-th face),
3. the crossed structure is furnished by the conjugation action of
   the $1$-morphisms $g_{ij}^{(n)}$ on the $2$-morphisms
   $a_{ij}^{(n)}$ via the adjoint representation of
   $\mathrm{SU}_{q_n}(2)$.
