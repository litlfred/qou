---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Introduction"
section_id: sec-004-23-shaded-planar-algebras
section_title: "Shaded planar algebras"
section_number: 2.3
pages: 6-9
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.996
doc_brief: "Non-cyclotomic fusion categories Introduction — Etingof, Nikshych and Ostrik ask in [7, §2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
---
One of the main tools for understanding monoidal categories (and more generally $2$-categories) is the diagram calculus (pioneered by Penrose [@MR0281657], Joyal-Street [@MR1113284], Reshetikhin-Turaev [@MR1036112], etc.) of string diagrams. Planar algebras are a version of this diagram calculus which allows you to study monoidal categories from the point of view of a particular object, where you only consider strings labelled by that object.

In particular, given a subfactor the resulting string diagrams have regions which are checkerboard shaded (corresponding to $A$ and $B$) and unoriented unlabelled strings (depending on the shading this string represents either ${}_A B_B$ or ${}_B B_A$). The structure here is a called a "shaded planar algebra.\"

We sketch the definition here. For further details, see [@MR1865703 §2], [@math.QA/9909027 §0], or [@MR1957084].

::: defn
A *(shaded) planar tangle* has an outer disk, a finite number of inner disks, and a finite number of non-intersecting strings. A string can be either a closed loop or an edge with endpoints on boundary circles. We require that there be an even number of endpoints on each boundary circle, and a checkerboard shading of the regions in the complement of the interior disks. We further require that there be a marked point on the boundary of each disk, and that the inner disks are ordered.

Two planar tangles are considered equal if they are isotopic (not necessarily rel boundary).

Here is an example of a planar tangle. $$\inputtikz{SampleTangle}$$

Planar tangles can be composed by placing one planar tangle inside an interior disk of another, lining up the marked points, and connecting endpoints of strands. The numbers of endpoints and the shadings must match up appropriately. This composition turns the collection of planar tangles into a colored operad.
:::

::: defn
A *(shaded) planar algebra* over a field $k$ consists of

-   A family of vector spaces $\{V_{(n,\pm,)}\}_{n\in \Natural}$ over $k$, called the positive and negative $n$-box spaces.

-   For each planar tangle, a multilinear map $V_{n_1, \pm_1} \otimes \ldots \otimes V_{n_j, \pm_j} \rightarrow V_{n_0, \pm_0}$ where $n_i$ is half the number of endpoints on the $i$th interior boundary circle, $n_0$ is half the number of endpoints on the outer boundary circle, and the signs $\pm$ are positive (respectively negative) when the marked point on the corresponding boundary circle is in an unshaded (respectively shaded) region.

For example, the planar tangle above gives a map $$V_{1,+} \otimes V_{2,+} \otimes V_{2,-} \rightarrow V_{3,+}.$$

The linear map associated to a 'radial' tangle (with one inner disc, radial strings, and matching marked points) must be the identity. We require that the action of planar tangles be compatible with composition of planar tangles. In other words, composition of planar tangles must correspond to the obvious composition of multilinear maps.
:::

We will refer to an element of $V_{n,\pm}$ (and specifically $V_{n,+}$, unless otherwise stated) as an "$n$-box."

We make frequent use of three families of planar tangles called multiplication, trace, and tensor product, which are shown in Figure [1](#fig:timestracetensor){reference-type="ref" reference="fig:timestracetensor"}. "Multiplication" gives an associative product $V_{n,\pm} \otimes V_{n,\pm} \rightarrow V_{n,\pm}$. "Trace" gives a map $V_{n,\pm} \rightarrow V_{0,\pm}$. "Tensor product" gives an associative product $V_{m,\pm} \otimes V_{n,\pm} \rightarrow V_{m+n,\pm}$ if $m$ is even, or $V_{m,\pm} \otimes V_{n,\mp} \rightarrow V_{m+n,\pm}$ if $m$ is odd.

<figure id="fig:timestracetensor">
<p><span class="math display">$$\inputtikz{multiplication} \quad , \quad \inputtikz{trace} \quad , \quad \inputtikz{tensor}$$</span></p>
<figcaption>The multiplication, trace, and tensor product tangles.</figcaption>
</figure>

The (shaded or unshaded) empty diagrams can be thought of as elements of $V_{0,\pm}$, since the 'empty tangle' induces a map from the empty tensor product $\Complex$ to the space $V_{0,\pm}$. If the space $V_{0,\pm}$ is one dimensional then we can identify it with $\Complex$ by sending the empty diagram to one.

::: defn
A planar algebra is called *irreducible* if $\dim V_{0,\pm} = 1$ and $\dim V_{1,\pm} = 1$.
:::

::: defn
[]{#defn:uncappable label="defn:uncappable"} An $n$-box $S$ is *uncappable* if $\epsilon_i(S)=0$ for all $i=1,\cdots, 2n$ where $$\epsilon_1 = \inputtikz{epsilon1} \, , \qquad 
 \epsilon_2 = \inputtikz{epsilon2} \, , \quad \ldots , \qquad 
 \epsilon_{2n}= \inputtikz{epsilon2k} \, .$$

We say $S$ is a *rotational eigenvector with eigenvalue $\omega$* if $\rho(S)= \omega S$ where $$\rho=\inputtikz{rho} \, .$$ Note that $\omega$ must be a $n^{th}$ root of unity.
:::

Given a shaded planar algebra we can recover two tensor categories called its even parts. However to describe this we need to deal with an annoying technical point. Recall that the planar algebra only captures maps between tensor products of a fixed generating object. If every object of a semisimple tensor category appears as a summand of some tensor power of a fixed object, then the tensor category can be recovered from the full subcategory of these tensor powers by taking the idempotent completion.

::: defn
The idempotent completion of a tensor category $\check{\cC}$ is a tensor category $\cC$ which contains $\check{\cC}$ as a full sub-category. The objects of $\cC$ are pairs $(o,p)$, where $o$ is an object of $\check{\cC}$ and $p:o \to o$ is an idempotent in $\check{\cC}$. We define $$\Hom{\cC}{(o,p)}{(o',p')} = \setcl{ f \in \Hom{\check{\cC}}{o}{o'} }{ f p = f = p' f}$$ and inherit composition and tensor product. (When we say $\check{\cC}$ is a full sub-category of $\cC$ we are implicitly identifying $o$ with $(o,\id_o)$.)
:::

::: defn
If $\cP$ is a shaded planar algebra, let $\check{\cP}^p$ be the category whose objects are even integers and whose morphisms are given by $$\Hom{\check{\cP}^p}{2m}{2n} = V_{m+n,+}.$$ Let $\cP^p$, called the principal even part of $\cP$ be the idempotent completion of the additive completion of $\check{\cP}^p$.

Similarly define $\check{\cP}^d$ whose objects are even integers and whose morphisms are given by $$\Hom{\check{\cP}^d}{2m}{2n} = V_{m+n,-},$$ and the dual even part $\cP^d$ to be the idempotent completion of the additive completion of $\check{\cP}^d$.
:::

A planar algebra is called *unitary* if there is an antilinear adjoint operation $*$ on each $V_{n,\pm}$, compatible with the adjoint operation on planar tangles given by reflection such that the sesquilinear form $\langle x,y \rangle = \tr{x y^*}$ is positive definite. The even parts of a unitary planar algebra are semisimple because all the endomorphism algebras are finite dimensional $\Complex^*$ algebras which are necessarily semisimple. Often in order to construct a unitary planar algebra from a non-unitary planar algebra we quotient out by the radical of $\langle x,y \rangle = \tr{x y^*}$, which is called the ideal of negligible morphisms.

Suppose that $k<K$ is an inclusion of fields and suppose that $\cP$ is a planar algebra over $K$. A *rational form* of $\cP$ over $k$ is a planar algebra $\cP_k$ over $k$ such that $\cP_k \otimes_k K$ is isomorphic to $\cP$. If $\cP_k$ is a rational form for $\cP$ then the corresponding fusion categories $\cP_k^p$ and $\cP_k^d$ are rational forms for $\cP^p$ and $\cP^d$. The rational form $\cP_k^p$ is a complete rational form for $\cP^p$ if every isomorphism class of projection in $V_{m+n,+}(\cP)$ has a representative coming from $V_{m+n,+}(\cP^p)$ (and similarly for the dual even part).
