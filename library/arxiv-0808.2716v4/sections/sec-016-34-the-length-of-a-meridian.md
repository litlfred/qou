---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-016-34-the-length-of-a-meridian
section_title: "The length of a meridian"
section_number: 3.4
pages: 20-20
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 1.0
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
To make the estimate of Proposition [\[prop:horosize\]](#prop:horosize){reference-type="ref" reference="prop:horosize"} independent of $\mu$, we prove a bound on the value of $\mu$. We note that the following lemma is the *only* result in this section that does not apply to all Farey manifolds: it fails for 2--bridge links.

::: lemma
In an equivariant cusp of a 4--punctured sphere bundle $M$, $\mu \geq
\sqrt{2}$. []{#lemma:meridian label="lemma:meridian"}
:::

::: proof
*Proof.* Lift the hyperbolic structure on $M$ to ${\mathbb{H}}^3$. The cusps lift to collections of horoballs. Conjugate such that the horoball about infinity of height $1$ projects to a cusp neighborhood. Since we took a maximal cusp neighborhood of $M$, that is, since we expanded cusps until they bumped, there must be some full--sized horoball $H$ projecting to a cusp of $M$, tangent to the horoball of height $1$ about infinity.

There is an isometry of ${\mathbb{H}}^3$ corresponding to the slope of length $\mu$ which is a covering transformation of $M$. It takes $H$ to another full--sized horoball $H'$. The Euclidean distance between $H$ and $H'$ is the length $\mu$.

Consider the geodesic $\gamma$ running from the center of $H$ to the center of $H'$. This projects to a geodesic in $M$ running from one puncture of the fiber back to the same puncture. Note that under the equivariant cusp expansion, any canonical edge runs between two distinct punctures of the fiber. Hence by Lemma [\[lemma:length-non-canonical\]](#lemma:length-non-canonical){reference-type="ref" reference="lemma:length-non-canonical"}, the length of the portion of $\gamma$ outside $H$ and $H'$ is at least $\ln(2)$.

Now, recall the following formula for lengths along "right angled hexagons" (see, for example, [@gmm:smallest-cusped Lemma 3.4]). Let $H_\infty$ denote the horosphere about infinity, and let $H_p$ and $H_q$ be disjoint horospheres not equal to $H_\infty$, centered over $p$ and $q$ in ${\mathbb{C}}$, respectively. Denote by $d_p$ the hyperbolic distance between $H_p$ and $H_\infty$, by $d_q$ the hyperbolic distance between $H_q$ and $H_\infty$, and by $d_r$ the hyperbolic distance between $H_p$ and $H_q$. Then the Euclidean distance between $p$ and $q$ is given by $$d(p,q) = \exp( (d_r - (d_p+d_q))/2 ).
\label{eqn:right-hex}$$

In our case, $d_p = d_q = 0$, since the corresponding horospheres ($H$ and $H'$) are tangent to $H_\infty$, and $d_r$ is at least $\ln(2)$. So $\mu = d(p,q)$ is at least $\sqrt{2}$. ◻
:::

By commensurability, the meridian in a punctured torus bundle has length $2 \mu \geq 2 \sqrt{2}$. In the setting of two-bridge links, on the other hand, Lemma [\[lemma:meridian\]](#lemma:meridian){reference-type="ref" reference="lemma:meridian"} fails because a meridian of the link is spanned by a single edge of the canonical triangulation. For two--bridge links, the best available estimate is Adams's result that $\mu \geq \sqrt[4]{2}$, which works for all links except the figure--8 and $5_2$ knots [@adams:waist2].
