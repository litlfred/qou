---
doc_id: arxiv-math-0611181v2
doc_title: "Proof of the volume conjecture for Whitehead chains"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0611181v2.pdf
source_sha256: 6931e3ebca584de9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.994
doc_brief: "Proof of the volume conjecture for Whitehead chains — We prove the volume conjecture for an inﬁnite family of links called White- head chains that generalizes both the Whitehead link and the"
---
The volume conjecture relates the colored Jones polynomials of a knot to the simplicial volume of its complement. More precisely, let us denote the normalized $N$-colored Jones polynomial of a knot $K$ by $J_N(K)$ and let $\mathrm{Vol}(K)$ be $v_3$ times the simplicial volume (Gromov norm) of $\mathbb{S}^3 - K$, where $v_3$ is the volume of the hyperbolic regular ideal tetrahedron. The volume conjecture can now be stated as follows:

::: conj
(**Volume conjecture**) [@Murakami2]\
For any knot $K$ we have: $$\lim_{N\to\infty}\frac{2\pi}{N}\log|J_N(K)(e^{\frac{2\pi i}{N}})| = \mathrm{Vol}(K)$$
:::

So far the conjecture has been proven for only the figure eight knot, torus knots, Whitehead doubles of certain torus knots and connected sums of these knots, [@Murakamiintro], [@KashaevTirkkonen], [@HaoZheng].

It is well known that the volume conjecture is false for many splittable links so it is unclear how to extend the volume conjecture to links. On the other hand, the volume conjecture has been shown to hold for the Whitehead link [@HaoZheng] and the Borromean rings [@Garoufalidis]. In this paper, we introduce the family of Whitehead chains generalizing both the Whitehead link and the Borromean rings and we settle the volume conjecture for this family.

The Whitehead chains are defined in terms of the tangles Belt, Clasp and Twist depicted in figure 1 on the next page.

<figure>
<div class="center">
<img src="BTC" />
</div>
<figcaption>The tangles Belt, Twist and Clasp</figcaption>
</figure>

::: defs
Let $a,b,c,d$ be integers such that $b\geq 1$ and $c,d\geq 0$. Define the Whitehead chain $W_{a,b,c,d}$ to be the closure of the composition of $a$ tangles of type Twist (or $a$ mirror images of type Twist when $a<0$), $b$ tangles of type Belt, $c$ tangles of type Clasp and $d$ mirror images of tangles of type Clasp.
:::

The tangles Belt, Twist, Clasp and their mirror images commute, so the order of composition is immaterial. Therefore the Whitehead chains are well defined. In the notation of the previous definition the Whitehead link is $W_{0,1,1,0}$ and the Borromean rings are $W_{0,1,1,1}$.

Our main theorem is the following asymptotic expansion for the colored Jones polynomial of a Whitehead chain. As usual $x \sim y$ means that the quotient converges to $1$.\
**Main theorem.** *Let $a,b,c,d$ be integers, such that $b\geq 1$ and $c,d\geq 0$.* $$J_N(W_{a,b,c,d})(e^{\frac{2\pi i}{N}}) \sim \exp\left(\frac{1}{2\pi}\left\{(\mathrm{Vol}(W_{a,b,c,d})+ i \mathrm{CS})N+\mathrm{D}\log(N)+ \mathrm{E}\right\}\right)$$

By taking absolute values and restricting ourselves to the leading term we see that the volume conjecture holds true for $b = 1$, while it is false for $b \geq 2$. In the latter case the volume conjecture is true when we restrict to odd values of $N$. This phenomenon might have something to do with the fact that the complement of the Whitehead chain is hyperbolic when $b = 1$, while the torus decomposition contains a Seifert-fibered piece when $b \geq 2$.

According to the complexified volume conjecture proposed in [@MMOTY] the value of $\mathrm{CS}$ is equal to $2\pi^2$ times the Chern-Simons invariant. For $a = 0$ this is indeed the case because the Chern-Simons invariant is additive with respect to belted sum and its value on the Whitehead link and its mirror image is $\pm\frac{1}{8}$, [@Ouyang].

In [@Hikami] the number $\mathrm{D}$ in the above asymptotic expansion is conjectured to be the number of prime factors of a knot. In [@GM] a different interpretation is given in terms of the knot complement. In the same paper it is also conjectured that the number $\mathrm{E}$ is determined by the Ray-Singer torsion of the complement twisted by the holonomy representation. We hope to investigate these conjectures for the Whitehead chains in a subsequent publication.

The main theorem shows that the original volume conjecture may fail even for non-splittable links, but adds credibility to the following weaker version of the volume conjecture for links:

::: conj
For any non-splittable link $L$ we have: $$\limsup_{N\to\infty}\frac{2\pi}{N}\log|J_N(L)(e^{\frac{2\pi i}{N}})| = \mathrm{Vol}(L)$$
:::
