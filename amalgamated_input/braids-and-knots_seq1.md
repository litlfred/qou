<!-- FILE_START: categorical-braiding-intro.md -->
The braid group is conventionally introduced through the topology of
configuration spaces or knot complements.  In the QOU framework, however,
braiding has a *categorical* origin that is logically prior to any
geometric realisation and carries over unchanged to non-archimedean settings
([Chapter 5](#chap:models-qou)) where knot complements in $S^3$ are unavailable.

The section is organised in three layers.  We first promote the
abstract braiding $c_{X,Y} : X \otimes Y \xrightarrow{\sim} Y \otimes X$
from the rigid monoidal structure to a substrate-parametrised family
indexed by $q \in \mathrm{End}(\mathbf{1})$, prove existence and
uniqueness of the family, and verify the hexagon coherence
conditions under the substrate flow.  The middle blocks specialise
the categorical braiding to the Reshetikhin–Turaev framework and
extract the categorical $R$-matrix; the closing blocks tie the
categorical $R$-matrix to the Hecke-skein relation that drives the
chapter's normal-form computations.

The output is the categorical braiding apparatus — substrate-
parametrised $R$-matrix, hexagon coherence, and Hecke-skein
relation — that the rest of the chapter consumes.  This is the
chapter's foundational section; subsequent sections build on the
apparatus introduced here without reopening it.
<!-- FILE_END: categorical-braiding-intro.md -->

<!-- FILE_START: braid-action-tensor.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) whose ambient category
$\mathbf{C}$ is braided monoidal with braiding
$c_{X,Y}\colon X\otimes Y \xrightarrow{ \sim } Y\otimes X$.
For each object $V$ in $\mathbf{C}$ and each $n \geq 2$, there is a
group homomorphism

$$
  \rho_n\colon B_n  \longrightarrow  \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})
$$

given on the Artin generators by

```tex
\begin{equation}\label{eq:categorical-braid-rep}
  \rho_n(\sigma_i)
  = 
  \mathrm{id}^{\otimes(i-1)}
  \otimes c_{V,V}
  \otimes \mathrm{id}^{\otimes(n-i-1)},
  \qquad 1 \leq i \leq n-1.
\end{equation}
```

The braid relation
$\rho_n(\sigma_i)\rho_n(\sigma_{i+1})\rho_n(\sigma_i) = \rho_n(\sigma_{i+1})\rho_n(\sigma_i)\rho_n(\sigma_{i+1})$
is equivalent to the Yang--Baxter equation for the braiding $c_{V,V}$.



**Mathematical Novelty:** While the braid-group action is a standard result (e.g., Kassel Thm XIII.1.3), its complete, sorry-free categorical Lean formalization in a generic braided monoidal category via an explicit hexagon and naturality chase represents a non-trivial engineering contribution to formal verification.
<!-- FILE_END: braid-action-tensor.md -->

<!-- FILE_START: why-b3.md -->
The Descartes condition $\chi(A) = -6$ forces the gauge group to be a
quantum form of $\mathrm{SU}(2)$ (rank $2$), so the fundamental
representation $V$ is $2$-dimensional.  On $V^{\otimes 2}$ the braiding
gives a single operator $c_{V,V}$; the first non-trivial braid group
action is on $V^{\otimes 3}$, where the two generators $\sigma_1, \sigma_2$
of $B_3$ act via the categorical braid representation.

<!-- FILE_END: why-b3.md -->

<!-- FILE_START: categorical-boson-fermion.md -->
The Schur--Weyl decomposition
$V^{\otimes 3} \cong V_{\frac{3}{2}} \oplus V_{\frac{1}{2}}^{\oplus 2}$
separates the symmetric (spin-$\frac{3}{2}$) and mixed-symmetry
(spin-$\frac{1}{2}$) sectors. The $B_3$-action preserves this
decomposition: on the symmetric sector the generators act as scalars
(bosonic exchange), while on the mixed-symmetry sector they act
non-by definition (fermionic exchange). This categorical distinction between
bosons and fermions requires no appeal to topology.
<!-- FILE_END: categorical-boson-fermion.md -->

<!-- FILE_START: symmetric-quotient-colour.md -->
The quotient $B_3 \twoheadrightarrow S_3$ obtained by imposing
$\sigma_i^2 = \mathrm{id}$ corresponds categorically to passing from a
:refterm[braided monoidal category]{#braided-monoidal-category} to a symmetric monoidal one (i.e. requiring
$c_{V,V}^2 = \mathrm{id}$).  In the Descartes universe, the three copies of
$S_3$ inside $S_5 = \mathrm{Aut}(\Sigma_4)$
([chirality and trefoil](#rem:chirality-trefoil)) are images of three such quotients,
one for each colour sector $\mathfrak{r}, \mathfrak{g}, \mathfrak{b}$
([color sector coords](#def:color-sector-coords)).  The lifts of these three
$S_3$ subgroups back to $B_3$ --- via the braiding of
$\mathrm{Rep}(\mathrm{SU}_q(2))$ --- recover the non-trivial exchange
phases that distinguish quarks from leptons.
<!-- FILE_END: symmetric-quotient-colour.md -->

<!-- FILE_START: braid-base-field.md -->
[braid action on tensor products](#prop:braid-action-tensor) uses only the braided monoidal
structure of $\mathbf{C}$.  In particular:

1. For the archimedean realisation
   ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), the braiding
   is computed by the $R$-matrix of
   $\mathcal{U}_q(\mathfrak{su}(2))$, and the $B_n$-action
   recovers the skein relations of [Chapter 6](#chap:brings-surface)
   as traces on braid-group representations.
2. For the $\mathfrak{p}$-adic realisation
   ([$p$-adic realisation](#ex:p-adic-realisation)), the same braiding exists
   on $\mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$ over
   $\mathbb{Q}_\mathfrak{p}$; the Yang--Baxter equation is an identity in
   the endomorphism algebra and holds over any base ring.
3. For the finite-field realisation
   ([finite field realisation](#ex:finite-field-realisation)), the braiding
   persists on the fusion category
   $\mathrm{Rep}_{\mathbb{F}_\mathfrak{p}}(\mathrm{SU}_q(2))$.

The skein relations, knot invariants, and hyperbolic volumes that appear
in the archimedean setting ([Chapter 6](#chap:brings-surface)) are
*consequences* of the categorical braiding evaluated via a specific
fibre functor --- they are not the source of the braid-group structure.
<!-- FILE_END: braid-base-field.md -->

<!-- FILE_START: braid-lifting-compatibility.md -->
The ([jet prolongation](#prop:jet-prolongation)) preserves
braided monoidal structure: if $\mathbf{C}$ is braided, then the jet
object $J^1(A) = A \otimes \Omega^1(A)$ inherits a braiding from the
tensor product of braidings on $A$ and $\Omega^1(A)$.  Consequently the
braid-group representations $\rho_n$ at each level of the brane tower are
compatible with the transition maps, and the direct-limit algebra
$\mathcal{A}_\infty = \varinjlim\Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2))$ carries a well-defined $B_n$-action for
every $n$.
<!-- FILE_END: braid-lifting-compatibility.md -->

