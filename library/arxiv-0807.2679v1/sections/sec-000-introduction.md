---
doc_id: arxiv-0807.2679v1
doc_title: "A cabling formula for the colored Jones polynomial"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-4
source_pdf: 0807.2679v1.pdf
source_sha256: 69ef10f8e70fc6f6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.996
doc_brief: "A cabling formula for the colored Jones polynomial — We prove an explicit cabling formula for the colored Jones polynomial."
---
In this note we study how the unnormalized colored Jones polynomial or quantum $sl_2$ invariant of a link changes under the operation of cabling. We work with a banded link or ribbon link $L$ so that every component is an embedded annulus. Given a diagram $D$ of a banded link inside an annulus we can construct a satellite of $L$ by embedding $D$ into a component $L_i$ of $L$. The $(r,s)$-cabling operation is the special case where we take $D$ to be the closure of the $(r,s)$-torus braid $B_s^r = (\sigma_1\cdots \sigma_{s-1})^r$, where $r\in \mathbb{Z},s\in\mathbb{N}$. To turn $B^r_s$ into a banded tangle we use the blackboard framing and add a positive curl to every overpassing arc, see figure 1 below. The banded link obtained by $(r,s)$-cabling the component $L_i$ of a banded link $L$ will be denoted by $L_{i;s}^r$, we will also call it the $(i;r,s)$-cabling of $L$.

In order to state our cabling formula we need to introduce the following generalizations of the trinomial (not multinomial) coefficients defined in [@Andrews]. For a vector $\mathbf{N} = (n_0,\hdots,n_{g-1})$ define ${g \choose w}_{\mathbf{N}}$ to be the coefficient of $x^w$ in the expansion of the product $\prod_{k=0}^{g-1}(x^{\frac{N_k-1}{2}}+x^{\frac{N_k-1}{2}-1}+\hdots + x^{-\frac{N_k-1}{2}})$.

::: st
Let $g = \mathrm{gcd}(r,s)$, $p = s/g$ and $\mathbf{N} = (N_0,\cdots,N_{g-1})$. The unnormalized colored Jones polynomial of the $(i;r,s)$-cabling of a banded link $L$ with $c$ components can be expressed as follows: $J_{M_1,\hdots,M_{i-1},\mathbf{N},\hdots,M_{c}}(L^r_{i;s})(q)=$ $$\sum_{w = -\frac{|\mathbf{N}|-g}{2}}^{\frac{|\mathbf{N}|-g}{2}} {g \choose w}_{\mathbf{N}} q^{\frac{rw(wp+1)}{g}}J_{M_1,\hdots,M_{i-1},2wp+1,\hdots,M_{c}}(L)(q)$$
:::

In the statement of the theorem we have used the notation $|\mathbf{N}| = N_0+\hdots+N_{g-1}$ and the convention that $J_{M_1,\hdots,M_{i-1},-j,\hdots,M_{c}}(L)(q) = -J_{M_1,\hdots,M_{i-1},j,\hdots,M_{c}}(L)(q)$.

<figure>
<div class="center">
<embed src="Kabeling3.eps" />
</div>
<figcaption>We have drawn the link <span class="math inline"><em>L</em><sub>1; 3</sub><sup>4</sup></span>, the <span class="math inline">(1;3,4)</span>-cabling of <span class="math inline"><em>L</em> = (<em>L</em><sub>1</sub>,<em>L</em><sub>2</sub>)</span>, where <span class="math inline"><em>L</em><sub>1</sub></span> is the figure eight knot and <span class="math inline"><em>L</em><sub>2</sub></span> is an unknot. We have indicated the torus braid <span class="math inline"><em>B</em><sub>3</sub><sup>4</sup></span> and the opened tangle <span class="math inline"><em>T</em><sub>1; 3</sub></span> mentioned in section 2.</figcaption>
</figure>

In the case where $g =1$ and $L$ is the unknot the above cabling formula agrees with Morton's formula for the $(r,s)$-torus knot [@Morton], where his variables are related to ours as $s^2 = q, m = r, p = s$. The case of a $(r,2)$-cabling is also known [@ZhengHao]. In all other cases our formula seems to be new.

Our main motivation for proving such a formula is to verify the volume conjecture [@Kashaev],[@MurakamiMurakami] in the cases where cabling is involved. The volume conjecture states that the normalized colored Jones polynomial $J'(L)$ of a link $L$ determines the simplicial volume of the link complement as follows: $$\lim_{N\to \infty}\frac{2\pi}{N}|J'_{N,N,\hdots,N}(L)(e^{\frac{2\pi i}{N}})| = \mathrm{Vol}(\mathbb{S}^3-L)$$ As an immediate corollary to our cabling formula we will find a proof of the volume conjecture for all knots and links whose complement has zero simplicial volume. This is because it is shown in [@Gordon] that all such links can be obtained from the unknot by repeated cabling and connected sum. Using the cabling formula we can therefore in principle write down the colored Jones polynomial of any such link. A simple estimate is enough to prove that there cannot be exponential growth, see also section 3.

::: cor
The volume conjecture is true for all zero volume knots and links.
:::

So far the only zero volume and links for which the volume conjecture has been proven are the torus knots [@KashTirk] and the $(2,s)$-torus links [@ZhengHao], [@Hikami2].

The cabling formula of Theorem 1 makes it possible to conduct a detailed study of cabled knots and iterated cabling. In the context of the volume conjecture some natural questions would be the following:

::: q
Is the volume conjecture stable under cabling?
:::

Since cabling does not contribute to the simplical volume this would mean that the existing exponential growth is unchanged under cabling.

::: q
What is the exact asymptotic expansion for a zero volume link?
:::

In [@KashTirk] and [@DubKash] explicit asymptotic expansions are given in the case torus knots at the $N$-th root of unity. Away from the root of unity the asymptotics of torus knots has also been studied in the context of the generalized volume conjecture [@MurakamiGen]. It would be especially interesting to see whether the polynomial growth related to the roots of the Alexander polynomial predicted and studied in [@MurakamiHikami] persists.

::: q
How is the colored Jones polynomial of a zero volume link related to q-series identities?
:::

In the case of torus knots and and some special torus links K. Hikami has shown many interesting relations between colored Jones polynomials, modular forms and q-series [@Hikami1], [@Hikami2].

::: q
What is the behavior of the non-commutative A-polynomial of a knot under cabling?
:::

It is known [@GaLe] that the colored Jones polynomial satisfies a linear recursion relation. This relation can be encoded in a two variable polynomial with q-coefficients called the non-commutative A-polynomial and it is conjectured [@GAJ] to be related to the character variety of the knot group. The knot group behaves well under cabling and according to our cabling formula so does the colored Jones polynomial. It would be interesting to see how these two relate. As before the zero volume knots provide many cases where explicit computations can be made. So far these have only been done for torus knots [@Hikami1].

An investigation of these questions will be postponed to a subsequent publication.

**Acknowledgment** I would like to thank the organizers of the International Conference on Quantum topology 2007 in Hanoi for providing the atmosphere that got this paper started and Stavros Garoufalidis and Hitoshi Murakami for stimulating conversations.
