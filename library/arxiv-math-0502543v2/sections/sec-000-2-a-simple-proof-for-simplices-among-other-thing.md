---
doc_id: arxiv-math-0502543v2
doc_title: "CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MILNOR"
section_id: sec-000-2-a-simple-proof-for-simplices-among-other-thing
section_title: "A simple proof for simplices (among other things)"
section_number: 2
pages: 3-5
source_pdf: 0502543v2.pdf
source_sha256: 227ef8150cb08faf
doc_brief: "CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MILNOR — In his paper [6] J."
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.989
---
[]{#simplices label="simplices"}

In dimension $2,$ the result follows immediately from Gauss' formula, which states that area is a linear function of the angles, so we will only discuss dimensions $3$ or above.

The simple proof relies on the *Schläfli differential equality* (see [@milnorcol], which states that in a space of constant curvature $K,$ and dimension $n$ the volume of a smooth family of polyhedra $P$ satisfies the differential equation:

$$\label{schlafli1}
K d V(P) = \dfrac{1}{n-1} \sum_F V_{n-2}(F) d \theta_F,$$

where the sum is over all codimension-$2$ faces, $V_{n-2}$ is the $n-2$ dimensional volume of $F,$ and $\theta_F$ is the dihedral angle at $F.$

Another way of writing the Schläfli formula is:

$$\label{schlafli2}
K \dfrac{\partial V(P)}{\partial \theta_F} = V_{n-2}(F).$$

This is the form we will use.

The first observation is that $V_{n-2}(F)$ is bounded by a constant (dimensional for $\mathbb{S}^n,$ , depending on the number of vertices of $F,$ but nothing else, and if $n \geq 4,$ in $\mathbb{H}^n.$).

This immediately shows the continuity of volume for all $\mathbb{S}^n,$ and for $\mathbb{H}^n,$ whenever $n \geq 4.$

We are left with dimension $3.$ All we really need is noting that the partial derivatives of $V$ with respect to the dihedral angles develop at worst logarithmic singularities as we approach the frontier of $\overline{\Omega_{\mathbb{H}^3}}$ -- this result suffices by the following form of the Sobolev Embedding Theorem (this is [@gilbrtru Theorem 7.26]):

::: theorem
[]{#sobemb label="sobemb"} Let $\Omega$ be a $C^{0,1}$ domain in $\mathbb{R}^n.$ Then,

-   (i) If $k p < n,$ the space $W^{k,p}(\Omega)$ is continuously imbedded in $L^{p^*}(\Omega),$ where $p^* = np/(n - kp),$ and compactly imbedded in $L^q(\Omega)$ for any $q < p^*.$

-   (ii) If $0 \leq m < k - \frac{n}{p} < m+1,$ the space $W^{k, p}$ is continously embedded in $C^{m, \alpha}(\overline{\Omega}),$ $\alpha=k -n/p - m,$ and compactly embedded in $C^{m, \beta}(\overline{\Omega})$ for any $\beta < \alpha.$
:::

Here, the Sobolev space $W^{k, p}$ is the space of functions whose first $k$ (distributional) derivatives are in $L^p.$

In our case, we know that the domain $\Omega$ is bounded, convex "curvilinear polyhedral" (hence $C^{0, 1}$) domain, volume is a bounded function, and we assume that the gradient grows logarithmically as we approach the boundary. This implies that $V$ is in $W^{1, p}$ for *all* $p > 0,$ so we get the following corollary:

::: corollary
Volume is in $C^{0, \alpha}(\overline{\Omega})$ for any $\alpha < 1.$
:::

The logarithmic growth of diameter of the simplex as a function of the distance to $\partial \Omega$ can be shown in a completely elementary way using Eq. [\[schlafli2\]](#schlafli2){reference-type="eqref" reference="schlafli2"} and elementary reasoning about Gram matrices, as follows:

Let $G$ be "angle Gram matrix" of a simplex $\Delta$, that is, $G_{ij} = - \cos\theta_{ij},$ where $\theta_{ij}$ is the angle between the $i$-th and the $j$-th face. Let $S$ be the matrix whose columns are the normals to the faces of $\Delta$ (all the computations take place in Minkowski space, and we use the hyperboloid model of $\mathbb{H}^n.$ It is immediate that $G = S^t S.$

Let now $W$ be the matrix whose columns are the (possibly scaled) vertices of $\Delta.$ $W$ satisfies the equation $S^t W = I,$ and to get the vertices to lie on the hyperboloid $\langle x, x\rangle = -1$ we must rescale in such a way that the squared norms of the columns of $W$ become $-1.$ Call the scaled matrix $W_s.$ Since the usual "length" Gram matrix $G^*$ of $\Delta$S can be written as $W_s^tW_s,$ and $G^*_{ij} = - \cosh(d(v_i, v_j)),$ a simple computation using Cramer's rule gives: $$\cosh d(v_i, v_j) = \dfrac{c_{ij}}{\sqrt{c_{ii} c_{jj}}},$$ where $c_{ij}$ is the $ij$-th cofactor of $G.$ (see [@muraushi] for many related results).

It follows that the distances between the vertices (which are the lengths of the edges, which are the faces of codimension $2.$) behave as $|\log\ c_{ii}|.$ Since the cofactors are polynomial in the cosines of the angles, we are done.

It should be noted that this argument works *mutatis mutandis* for *hyperideal* simplices, or simplices with some finite and some hyperinfinite vertices..
