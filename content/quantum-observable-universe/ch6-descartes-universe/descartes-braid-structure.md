Let $(\mathcal{C}, A, \omega)$ be a Descartes universe
([Definition](#def:descartes-condition)).  Then:

1. The braiding of $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$
   induces a faithful representation
   $\rho_3\colon B_3 \to \mathrm{Aut}_{\mathcal{C}}(V^{\otimes 3})$
   on the fundamental representation $V$
   ([Proposition](#prop:braid-action-tensor)).
2. The image of $\rho_3$ in $\mathrm{SU}(2)$ (via the fibre
   functor $\omega$) is the binary dihedral group
   $\mathrm{Dic}_3$ of order $12$
   ([Definition](#def:su2-generators)).
3. The composite $B_3 \xrightarrow{\;\rho_3\;}
   \mathrm{Dic}_3 \twoheadrightarrow S_3$ recovers the three
   copies of $S_3$ inside $S_5 = \mathrm{Aut}(\Sigma_4)$
   ([Remark](#rem:chirality-trefoil)), one for each
   colour sector.
4. This structure is defined over any base ring $R$ with
   $30 \in R^{\times}$; in particular it applies to the
   $\mathfrak{p}$-adic realisation
   ([Example](#ex:p-adic-realisation)), where knot complements
   and skein relations are not available.

---

*Item (1)* follows from [Proposition](#prop:braid-action-tensor)
applied to the fundamental representation $V$ of
$\mathrm{SU}_q(2)$, which is $2$-dimensional.  The braiding
$c_{V,V}$ is computed by the $R$-matrix of
$\mathcal{U}_q(\mathfrak{su}(2))$
([Remark](#rem:r-matrix-braiding)), and faithfulness follows from the
fact that the eigenvalues of $c_{V,V}$ are $q$ and $-q^{-1}$, which
are distinct for $q \neq \pm 1$.

For *item (2)*, the fibre functor $\omega$ sends the braiding to the
matrix $\check{R} = P \circ \mathcal{R}$ acting on
$\mathbb{C}^2 \otimes \mathbb{C}^2$.  The generators $\sigma_1, \sigma_2$
map to the $\mathrm{SU}(2)$ elements $\alpha, \beta$
([Definition](#def:su2-generators)) generating $\mathrm{Dic}_3$, as
verified in [Example](#ex:trefoil-operator-algebra).

*Item (3)*: the projection $\mathrm{Dic}_3 \to S_3$ sends
$\alpha \mapsto (1\,2\,3)$ and $\beta \mapsto (1\,2)$.  The three
copies of $S_3$ inside $S_5$ are the stabilisers of the three pairs
of chiral coordinates
([Definition](#def:chiral-sector-coords)), and conjugation by
elements of $S_5 \setminus S_3$ permutes these copies.

*Item (4)*: the braided monoidal structure of
$\mathrm{Rep}(\mathrm{SU}_q(2))$ is defined over $R[q, q^{-1}]$
with $30 \in R^{\times}$
([Proposition](#prop:brings-is-qou)(1)), and
[Proposition](#prop:braid-action-tensor) requires no topological
input beyond the hexagon axioms.
