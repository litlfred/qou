---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-001-2-the-milnor--invariant
section_title: "The Milnor -invariant"
section_number: 2
pages: 9-12
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.941
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
[]{#sec:milnor label="sec:milnor"}

Let $L$ be a three-component link in either $\mathbb R^3$ or $S^3$, with oriented components $X$, $Y$ and $Z$, and pairwise linking numbers $p$, $q$ and $r$. Milnor's original definition of the triple linking number $\mu(L)$, typically denoted $\bar\mu_{123}(L)$, was algebraic. The formulation in his PhD thesis [@Milnor57] is expressed in terms of the lower central series of the link group $G$, the fundamental group of the complement of $L$, as follows.

Choose based meridians for the link components $X$, $Y$ and $Z$, and let $x$, $y$ and $z$ denote the corresponding elements of $G$. In general, these three elements do not generate $G$, but they do generate the quotient of $G$ by the third term $[[G,G],G]$ in its lower central series. In this quotient group, the longitude of $Z$ can be written as a word $w$ in $x$, $y$ and $z$ and their inverses. Assign an integer $m_{xy}(w)$ to this word that counts with signs the number of times that $x$ appears before $y$ in $w$, allowing intervening letters. More precisely, each appearance of $x\cdot\!\cdot\!\cdot y$ or $x^{-1}\cdot\!\cdot\!\cdot y^{-1}$ contributes $+1$ to $m_{xy}(w)$, while $x\cdot\!\cdot\!\cdot y^{-1}$ or $x^{-1}\cdot\!\cdot\!\cdot y$ contributes $-1$. Then $\mu(L)$ is the element of $\mathbb Z_{\gcd(p,q,r)}$ defined by $$\mu(L) \ = \ m_{xy}(w)\ \ \textup{mod}\gcd(p,q,r).$$

There is a geometric reformulation of this definition, found by Mellor and Melvin [@MellorMelvin], that is more convenient for our purposes: choose Seifert surfaces $F_X$, $F_Y$ and $F_Z$ for the components of $L$, and move these into general position. Starting at any point on $X$, record its intersection with the Seifert surfaces for $Y$ and $Z$ by a word $w_X$ in $y$ and $z$. For example a $y$ or $y^{-1}$ in $w_X$ indicates a positive or negative intersection point of $X$ with $F_Y$. Set $m_X = m_{yz}(w_X)$, where the right hand side is computed as in the last paragraph, and similarly set $m_Y = m_{zx}(w_Y)$ and $m_Z = m_{xy}(w_Z)$. Finally, let $t$ be the signed count of the number of triple points of intersection of the three Seifert surfaces. Then $$\mu(L) \ =  \ m_X+m_Y+m_Z - t \ \ \textup{mod}\gcd(p,q,r).$$ It follows from this formula that $\mu(L)$ is invariant under even permutations of the components of $L$, but changes sign under odd permutations. This is a well known property of Milnor's triple linking number.

We give two sample calculations of the triple linking number, using this geometric formulation, that will feature in our inductive proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} in Section [\[sec:A\]](#sec:A){reference-type="ref" reference="sec:A"}.

::: example
[]{#ex:Lpqr label="ex:Lpqr"} Let $L_{pqr}$ be the link shown in Figure [1](#fig:Lpqr){reference-type="ref" reference="fig:Lpqr"}, with components $X$, $Y$ and $Z$ and with pairwise linking numbers $p$, $q$ and $r$. Choose the Seifert surfaces $F_X$, $F_Y$ and $F_Z$ to be the obvious disks, essentially lying in the page, bounded by $X$, $Y$ and $Z$.

<figure id="fig:Lpqr">
<p><embed src="FigLpqr.pdf" style="height:2.08333in" /> (-80,25)<span><span class="math inline"><em>X</em></span></span> (-30,90)<span><span class="math inline"><em>Y</em></span></span> (-125,90)<span><span class="math inline"><em>Z</em></span></span> (-58,62)<span><span class="math inline"><em>r</em></span></span> (-96,64)<span><span class="math inline"><em>q</em></span></span> (-78,95)<span><span class="math inline"><em>p</em></span></span></p>
<figcaption>The base link <span class="math inline"><em>L</em><sub><em>p</em><em>q</em><em>r</em></sub></span> for <span class="math inline"><em>p</em> = 5</span>, <span class="math inline"><em>q</em> = 3</span>, <span class="math inline"><em>r</em> =  − 2</span></figcaption>
</figure>

Starting at appropriate points on the link components, we can read off the words $$w_X = y^rz^q \ , \ \ w_Y = z^px^r \quad\textup{and}\quad w_Z = x^qy^p.$$ Thus $m_X = qr$, $m_Y = rp$ and $m_Z = pq$. Furthermore, it is clear that there are no triple points of intersection of the three disks. Therefore $$\mu(L_{pqr}) \ = \ qr+rp+pq-0 \ = \ 0 \ \in \ \mathbb Z_{\gcd(p,q,r)}.$$ The links $L_{pqr}$ will serve as the ***base links*** for our proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}.
:::

::: example
[]{#ex:delta label="ex:delta"} Consider the ***delta move*** shown in Figure [2](#fig:delta){reference-type="ref" reference="fig:delta"}, transforming the link $L$ on the left to the link $\widehat{L}$ on the right.

<figure id="fig:delta">
<p><embed src="FigD.pdf" style="height:1.38889in" /> (-228,95)<span><span class="math inline"><em>X</em></span></span> (-28,99)<span><span class="math inline"><em>X̂</em></span></span> (-230,-5)<span><span class="math inline"><em>Y</em></span></span> (-22,-5)<span><span class="math inline"><em>Ŷ</em></span></span> (-315,45)<span><span class="math inline"><em>Z</em></span></span> (-113,46)<span><span class="math inline"><em>Ẑ</em></span></span></p>
<figcaption>The delta move <span class="math inline"><em>L</em> → <em>L̂</em></span></figcaption>
</figure>

This move takes place within a $3$-ball, outside of which the link is left fixed. It does not alter the pairwise linking numbers of $L$, and may be thought of as a higher order variant of a crossing change.

The delta move was introduced by Matveev [@Matveev]. It was shown by Murakami and Nakanishi [@MurakamiNakanishi] that a suitable sequence of such moves can transform any link into any other link with the same number of components and the same pairwise linking numbers. In particular, the base link $L_{pqr}$ above can be transformed into any other three-component link with pairwise linking numbers $p$, $q$ and $r$ by a sequence of delta moves. The inductive step of our proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} will be based on this observation, and so we determine right now the effect of the delta move on the $\mu$-invariant.

If the three arcs involved in the delta move *do not* come from three distinct components of the link $L$, then the change can be achieved by a link homotopy, and hence neither Milnor's $\mu$-invariant nor Pontryagin's $\nu$-invariant for $g_L$ will change.

But if the arcs *do* come from three distinct components of $L$ as shown in the figure, then $\mu$ increases by $1$, that is $\mu(\widehat{L}) = \mu(L) + 1.$ This can be seen as follows, using the geometric formula for the $\mu$-invariant.

In Figure [3](#fig:seifert){reference-type="ref" reference="fig:seifert"}, we display on the left fragments of the Seifert surfaces $F_X$, $F_Y$ and $F_Z$ before the delta move, while on the right, after the delta move, each old surface is enlarged a bit to provide new surfaces $F_{\widehat{X}}$, $F_{\widehat{Y}}$ and $F_{\widehat{Z}}$.

<figure id="fig:seifert">
<p><embed src="FigS.pdf" style="height:1.66667in" /> (-300,90)<span><span class="math inline"><em>F</em><sub><em>X</em></sub></span></span> (-185,90)<span><span class="math inline"><em>F</em><sub><em>Y</em></sub></span></span> (-275,-5)<span><span class="math inline"><em>F</em><sub><em>Z</em></sub></span></span> (-125,90)<span><span class="math inline"><em>F</em><sub><em>X̂</em></sub></span></span> (-10,90)<span><span class="math inline"><em>F</em><sub><em>Ŷ</em></sub></span></span> (-30,-3)<span><span class="math inline"><em>F</em><sub><em>Ẑ</em></sub></span></span></p>
<figcaption>A negative triple point appears</figcaption>
</figure>

On the left, the three surface fragments are disjoint, while on the right, after their enlargement, they are not. Where these surfaces now come together, we have an additional isolated triple point, and since the normals to the surfaces at this point form a left-handed frame, this triple point gets a minus sign. Thus $t$ drops by $1$. We also see that after the delta move, the curve $\widehat{Z}$ has two extra intersections with $F_{\widehat{Y}}$, the first positive and the second negative, and no extra intersections with $F_{\widehat{X}}$. Since these new intersection points are adjacent along the curve, and of opposite signs, it follows that the new count $m_{\widehat{Z}} =  m_{xy}(w_{\widehat{Z}})$ is equal to the old one $m_Z$. Similarly $m_{\widehat{X}} = m_X$ and $m_{\widehat{Y}} = m_Y$. Hence $\mu =  m_X + m_Y + m_Z  - t$ increases by 1, as claimed.

The heart of the proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} will be to show that application of the delta move increases Pontryagin's $\nu$-invariant by $2$.
:::
