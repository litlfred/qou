---
doc_id: arxiv-math-0410233v4
doc_title: "Cusp shapes under cone deformation"
section_id: sec-019-62-finding-values-for-tube-radius
section_title: "Finding values for tube radius"
section_number: 6.2
pages: 39-41
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "Cusp shapes under cone deformation — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.973
---
[]{#subsec:tube label="subsec:tube"}

We need to ensure that the tube radius remains larger than $R_1 =
0.56$ throughout the cone deformation. We can do so by again applying work of Hodgson and Kerckhoff [@hk:univ]. They show that in the neighborhood of the $j$-th component of the singular locus, we can increase the cone angle from $0$ to $2\pi$, maintaining the tube radius $R \geq R_1$, provided equation ([\[eq:Lhat_int\]](#eq:Lhat_int){reference-type="ref" reference="eq:Lhat_int"}) of the proof of Lemma [\[lemma:b_j-bound\]](#lemma:b_j-bound){reference-type="ref" reference="lemma:b_j-bound"} holds.

That is, consider a particular component of the singular locus $\Sigma_j$. The singular locus consists of crossing circles of the link $L$. At the $j$-th crossing circle, the hyperbolic cone deformation performs Dehn filling along a slope of the form $1/n_j$. Let $L_0$ denote the normalized length of this slope in $S^3-L$. We can then increase the cone angle from $0$ to $2\pi$, maintaining the tube radius bound $R \geq R_1$, provided the normalized length $L_0^2$ is larger than the increasing function $I(R_1)$ defined in equation ([\[eq:Lhat_int\]](#eq:Lhat_int){reference-type="ref" reference="eq:Lhat_int"}).

So to ensure $R \geq R_1 \geq 0.56$, we compute that $L_0^2$ must be at least $113.044$. By Proposition [\[prop:proj-height\]](#prop:proj-height){reference-type="ref" reference="prop:proj-height"}, we know $L_0^2$ is at least $c_i$, where $c_i$ is the number of crossings in the $i$-th twist region. Thus by ensuring there are at least $114$ crossings in the $i$-th twist region, we will guarantee that our tube radius is at least $0.56$. For general $R_1$, we have the following result.

::: lemma
Let $K$, $L$ be as above, such that we have a cone deformation from $S^3-L$ to $S^3-K$. Fix $R_1 \geq 0.531$. Then $R \geq R_1$ throughout the deformation provided the number of crossings in each twist region is at least $I(R_1)$, where $I(R_1)$ is defined in equation ([\[eq:Lhat_int\]](#eq:Lhat_int){reference-type="ref" reference="eq:Lhat_int"}). []{#lemma:crossings-vs-R label="lemma:crossings-vs-R"}
:::

## Proof of Theorem [\[thm:main-knot-cusp\]](#thm:main-knot-cusp){reference-type="ref" reference="thm:main-knot-cusp"} {#subsec:numeric}

**Theorem [\[thm:main-knot-cusp\]](#thm:main-knot-cusp){reference-type="ref" reference="thm:main-knot-cusp"}** *Let $K$ be a knot in $S^3$ which admits a prime, twist reduced diagram with a total of $n\geq 2$ twist regions, with each twist region containing at least $c\geq 116$ crossings. In a hyperbolic structure on $S^3-K$, take a horoball neighborhood $U$ about $K$. Normalize so that the meridian on $\partial U$ has length $1$. Then the height $H$ of the cusp of $S^3-K$ satisfies: $$H\geq n\,(1-f(c))^2.$$ Here $f(c)$ is a positive function of $c$ which approaches $0$ as $c$ increases to infinity. Additionally, $H\leq n(\sqrt{n-1} + f(c))^2$.*

::: proof
*Proof.* If $K$ admits a prime, twist reduced diagram with at least $2$ twist regions, then we may form the augmented link $L$ from the diagram of $K$. We have seen in §[\[subsec:crossings\]](#subsec:crossings){reference-type="ref" reference="subsec:crossings"} that, provided there are at least $113$ crossings in each twist region of the diagram of $K$, then $S^3-L$ and $S^3-K$ are connected by a hyperbolic cone deformation $X_t$, with $X_0=S^3-L$, $X_\tau=S^3-K$. The singular locus will consist of the crossing circle components of $L$. There will be $n$ of these.

By results of Section [\[subsec:tube\]](#subsec:tube){reference-type="ref" reference="subsec:tube"}, if there are at least $114$ crossings per twist region then the tube radius of the deformation is at least $R_1=0.56$. Then by Theorem [\[thm:main-norm-height\]](#thm:main-norm-height){reference-type="ref" reference="thm:main-norm-height"}, $$-(2\pi)^2\frac{\sqrt{n\,C(R_1)}}{(1-e^{-2R_1})\sqrt{2}}
  \leq h_\tau-h_0
  \leq
  (2\pi)^2\frac{\sqrt{n\,C(R_1)}}{(1-e^{-2R_1})\sqrt{2}},$$ where $h_t$ denotes the normalized height of the cusp at time $t$.

And so: $$h_0 - (2\pi)^2 \frac{\sqrt{n\,C(R_1)}}{(1-e^{-2R_1})\sqrt{2}} \leq
h_\tau \leq
h_0 + (2\pi)^2 \frac{\sqrt{n\,C(R_1)}}{(1-e^{-2R_1})\sqrt{2}}.
\label{eqn:2-sides}$$

We may now apply part (2) of Proposition [\[prop:proj-height\]](#prop:proj-height){reference-type="ref" reference="prop:proj-height"}. This implies that the initial normalized height $h_0$, i.e. the normalized height on $S^3-L$, is between $\sqrt{n}$ and $\sqrt{n(n-1)}$.

Plug this into the left hand side of the above equation and we find: $$h_\tau \geq \sqrt{n}\left(1-(2\pi)^2
  \frac{\sqrt{C(R_1)}}{(1-e^{-2R_1})\sqrt{2}}\right).
\label{eqn:h}$$

For the right hand side, we find: $$h_\tau \leq \sqrt{n}\left(\sqrt{n-1} + (2\pi)^2
  \frac{\sqrt{C(R_1)}}{(1-e^{-2R_1})\sqrt{2}}\right).
\label{eqn:hright}$$

The term $C(R_1)$ can be computed explicitly using the formulas in the proof of Lemma [\[lemma:b_j-bound\]](#lemma:b_j-bound){reference-type="ref" reference="lemma:b_j-bound"}. Recall $C(R_1)$ is strictly decreasing, approaching $0$ as $R_1$ approaches infinity. Thus the function $$\bar{f}(R_1)= (2\pi)^2\frac{\sqrt{C(R_1)}}{(1-e^{-2R_1})\sqrt{2}},$$ which appears in both ([\[eqn:h\]](#eqn:h){reference-type="ref" reference="eqn:h"}) and ([\[eqn:hright\]](#eqn:hright){reference-type="ref" reference="eqn:hright"}), is decreasing with $R_1$, approaching $0$. The graph of $\bar{f}$, as well as that of $I(R)$, is shown in Figure [1](#fig:F-I-graphs){reference-type="ref" reference="fig:F-I-graphs"}.

<figure id="fig:F-I-graphs">
<div class="center">

</div>
<figcaption>Graphs of <span class="math inline"><em>f̄</em>(<em>R</em>)</span> and <span class="math inline"><em>I</em>(<em>R</em>)</span>. Here <span class="math inline"><em>f̄</em>(<em>R</em>)</span> gives the bounds in Theorem <a href="#thm:main-knot-cusp" data-reference-type="ref" data-reference="thm:main-knot-cusp">[thm:main-knot-cusp]</a> for given tube radius <span class="math inline"><em>R</em></span>. <span class="math inline"><em>I</em>(<em>R</em>)</span> gives the number of crossings required to guarantee tube radius <span class="math inline"><em>R</em></span>.</figcaption>
</figure>

When $R_1=0.56$, $1-\bar{f}(R_1)$ is negative. Since $h_\tau$ is known to be positive, this doesn't give a very good estimate in ([\[eqn:h\]](#eqn:h){reference-type="ref" reference="eqn:h"}). To get a better estimate, we increase $R_1$. The value $1-\bar{f}(R_1)$ becomes positive when $R_1$ is about $0.6624$. However, as $R_1$ increases, so does $I(R_1)$, so by Lemma [\[lemma:crossings-vs-R\]](#lemma:crossings-vs-R){reference-type="ref" reference="lemma:crossings-vs-R"}, we need to increase the number of crossings in each twist region to guarantee that the tube radius remains larger than $R_1$ throughout the deformation. In particular, $c$ must be at least $116$ to ensure $R_1 \geq 0.6624$.

In general, let $f(c) = \bar{f}(I^{-1}(c))$. Since $I(R)$ is strictly increasing for $R\geq 0.56$, this is well defined. Then for $c\geq 116$, $1-f(c)$ is positive.

To finish the proof, note that we can scale so that the meridian of the cusp of $S^3-K$ has length $1$. Then the actual height $H$ of the cusp of $S^3-K$ will be at least $(h_\tau)^2$. ◻
:::

Notice in Figure [1](#fig:F-I-graphs){reference-type="ref" reference="fig:F-I-graphs"} that $\bar{f}$ is close to $0$ for values of $R$ near $2$. However for $R$ this size, $I(R)$, or the number of crossings required per twist region, is nearly $700$. We find a nice compromise by choosing $R=1.0$. Then $I(R)$ is not much larger than $116$, and yet $1-\bar{f}$ is already over $0.8$. We use this fact in the following corollary, which gives more explicit numbers to the results of Theorem [\[thm:main-knot-cusp\]](#thm:main-knot-cusp){reference-type="ref" reference="thm:main-knot-cusp"}.

::: corollary
Let $K$ be as in the previous theorem, with at least $c\geq 145$ crossings in each twist region. Then when the meridian of the cusp of $S^3-K$ is normalized to have length $1$, the height of the cusp satisfies: $$H \geq n\,(0.81544)^2.$$ []{#cor:0.8 label="cor:0.8"}
:::

::: proof
*Proof.* Letting $c\geq 145$ in the above theorem ensures that $R> R_1 =
  1.0$. Then $1-f(c) = 1-\bar{f}(1.0) \geq 0.81544$. ◻
:::
