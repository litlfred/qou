---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A"
section_id: sec-004-5-rectangles
section_title: "Rectangles"
section_number: 5
pages: 9-13
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.966
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A — Let U be the quantum group associated to a Lie algebra g of type An."
---
[]{#rectangles label="rectangles"} The above provides us with a description of the spanning vectors of a Lusztig cone as multisets of positive roots. We would also like a description of the monomial of Kashiwara operators corresponding to such a vector. We will use this in the next section to calculate Lusztig parametrizations $c_j(\mathbf{j})$, $c_P(\mathbf{j})$ of the canonical basis elements arising in Theorem [\[natural\]](#natural){reference-type="ref" reference="natural"}. We shall show that these monomials can be described by a remarkable 'rectangle combinatorics' (invented by R. W. Carter) which we shall now describe.

::: definition
[]{#diagonal label="diagonal"} Let $P$ be a partial quiver, and $Y$ a component of $P$. Let $a=a(Y)$ and let $b=b(Y)$ (see Theorem [\[multiset\]](#multiset){reference-type="ref" reference="multiset"}). We define the *rectangle* $\rho(Y)$ of $Y$, as follows. If $Y$ is of type $L$, then $\rho(Y)$ is as in the left hand diagram in Figure [1](#rectanglesf){reference-type="ref" reference="rectanglesf"}; if $Y$ is of type $R$ then $\rho(Y)$ is as in the right hand diagram in Figure [1](#rectanglesf){reference-type="ref" reference="rectanglesf"}. We also define, for $j=1,2,\ldots ,n$, $\rho(j)$ to be the type $L$ rectangle with $a=j$ and $b=j+1$ (for these values of $a$ and $b$, both diagrams in Figure [1](#rectanglesf){reference-type="ref" reference="rectanglesf"} coincide).

<figure id="rectanglesf">
<p>units &lt;0.8cm,0.8cm&gt; x from -4 to 14, y from -4.5 to 3</p>
<p>[c] at 0.5 0 [c] at 1 0.5 [c] at 1.5 1.0 [c] at 2 1.5 [c] at 2.5 2.0</p>
<p>[c] at 3 1.5 [c] at 3.5 1 [c] at 4 0.5 [c] at 4.5 0 [c] at 4.4 -0.5</p>
<p>[c] at 4.5 -1 [c] at 4 -1.5 [c] at 3 -1.9 [c] at 3 -2.3</p>
<p>[c] at 2 -1.5 [c] at 1.5 -1 [c] at 1 -0.5</p>
<p>0 2.5 2.5 / 2.5 5.5 -0.5 / -0.5 3 -3 / -3 0 0 /</p>
<p>[c] at 2.75 -4</p>
<p>[c] at 9.7 0 [c] at 10.3 0.5 [c] at 10.5 1.0 [c] at 11 1.5 [c] at 11.5 1.8</p>
<p>[c] at 12 1.5 [c] at 12.5 1 [c] at 13 0.5 [c] at 13.5 0 [c] at 13.4 -0.5</p>
<p>[c] at 13.5 -1 [c] at 13 -1.5 [c] at 12.5 -2 [c] at 12 -2.5</p>
<p>[c] at 11.5 -2 [c] at 11 -1.5 [c] at 10.5 -1 [c] at 10 -0.5</p>
<p>0 11.5 2.5 / 2.5 14.5 -0.5 / -0.5 12 -3 / -3 9 0 /</p>
<p>[c] at 11.75 -4</p>
<figcaption>The rectangles <span class="math inline"><em>ρ</em>(<em>Y</em>)</span>.<span id="rectanglesf" label="rectanglesf"></span></figcaption>
</figure>

In each case, the rectangle is filled in with numbers in diagonal rows, with the numbers along a diagonal row from top right to bottom left increasing by 1 at each step and similarly from top left to bottom right. We define the diagram $D(P)$ of $P$ in the following way. Go through the components $Y$ of $P$ one by one, from left to right. Fit the corresponding rectangles $\rho(Y)$ together, so that if a component of type $L$ is followed by one of type $R$, the rectangles share leftmost corners, and if one of type $R$ is followed by one of type $L$, they share rightmost corners. In each case, it is easy to see that the overlapping numbers agree. We associate a multiplicity $m(s)$ to each position in $D(P)$ where a number $s$ is placed; if $t$ is the number of rectangles $\rho(Y)$ that $s$ lies in, then $m(s)$ is defined to be $\lceil t/2\rceil$. We label each rectangle with the corresponding component $Y$ of $P$; on the left hand corner if $Y$ is of type $R$, and on the right hand corner if $Y$ is of type $L$. We define, for $j=1,2,\ldots ,n$, $D(j)$ to be the diagram $\rho(j)$, with each position given multiplicity $1$.
:::

\
We consider the case when $n=5$ and $P=LRL-$. Then $P$ has three components, $L_1=L---$, $R_1=-R--$ and $L_2=--L-$. The diagrams $\rho(Y)$ are as in Figure [2](#egrectangles){reference-type="ref" reference="egrectangles"}.

<figure id="egrectangles">
<p>units &lt;0.8cm,0.8cm&gt; x from -6 to 10, y from -4.5 to 3</p>
<p>at -2 1</p>
<p>[c] at 0.5 0 [c] at 1 0.5 [c] at 1.5 1.0 [c] at 2 1.5</p>
<p>0 2 2 / 2 2.5 1.5 / 1.5 0.5 -0.5 / -0.5 0 0 /</p>
<p>at 2.8 1.5</p>
<p>at 7 1</p>
<p>[c] at 10 0 [c] at 10.5 0.5 [c] at 11 1.0</p>
<p>[c] at 10.5 -0.5 [c] at 11 0 [c] at 11.5 0.5</p>
<p>0 11 1.5 / 1.5 12 0.5 / 0.5 10.5 -1 / -1 9.5 0 /</p>
<p>at 9.2 0</p>
<p>at 2 -2.5</p>
<p>[c] at 4 -2.5 [c] at 4.5 -2</p>
<p>[c] at 4.5 -3 [c] at 5 -2.5</p>
<p>[c] at 5 -3.5 [c] at 5.5 -3</p>
<p>-2.5 4.5 -1.5 / -1.5 6 -3 / -3 5 -4 / -4 3.5 -2.5 /</p>
<p>at 6.3 -3</p>
<figcaption>Examples of the rectangles <span class="math inline"><em>ρ</em>(<em>Y</em>)</span>.<span id="egrectangles" label="egrectangles"></span></figcaption>
</figure>

We put them together, so that the $4$ in $\rho(L---)$ matches the leftmost $4$ in $\rho(-R--)$ and so that the rightmost $3$ in $\rho(-R--)$ matches the rightmost $3$ in $\rho(--L-)$, to get the complete diagram $D(LRL-)$; see Figure [3](#lrl){reference-type="ref" reference="lrl"}. The numbers $2$ and $3$ in the middle of the diagram each have multiplicity $2$.

<figure id="lrl">
<p>units &lt;0.8cm,0.8cm&gt; x from -9 to 3, y from -1 to 2.75</p>
<p>at -2 1</p>
<p>[c] at 0.5 0 [c] at 1 0.5 [c] at 1.5 1.0 [c] at 2 1.5</p>
<p>0 2 2 / 2 2.5 1.5 / 1.5 0.5 -0.5 / -0.5 0 0 /</p>
<p>[c] at 1 -0.5 [c] at 1.5 0 [c] at 2 0.5</p>
<p>0 1.5 1.5 / 1.5 2.5 0.5 / 0.5 1 -1 / -1 0 0 /</p>
<p>[c] at 0.5 1 [c] at 1 1.5</p>
<p>1 1 2 / 2 2.5 0.5 / 0.5 1.5 -0.5 / -0.5 0 1 /</p>
<p>[c] at 2.8 1.5 [c] at -0.3 0 [c] at 2.8 0.5</p>
<figcaption>The diagram <span class="math inline"><em>D</em>(<em>L</em><em>R</em><em>L</em>−)</span>.<span id="lrl" label="lrl"></span></figcaption>
</figure>

::: definition
[]{#diagonalrow label="diagonalrow"} Suppose $P$ is a partial quiver or $P=j$ for some $j\in [1,n]$. We define a *diagonal row* of $D(P)$ to be a diagonal row of numbers in $D(P)$ running from top left to bottom right. Such a diagram $D(P)$ defines a sequence $\mu(P)$ which is obtained by reading off the digits in the diagonal rows in the diagram, starting with the bottom left row. Each digit is repeated according to its multiplicity. In our example, $\mu(LRL-)=(4,5,2,3,3,4,1,2,2,3,1)$. There is a corresponding monomial $F(P)$ in $U^-$, obtained by replacing each digit, $s$, occurring with multiplicity $m(s)$, by the divided power $F_s^{(m(s))}$. In our example, $F(LRL-)=
F_4F_5F_2F_3^{(2)}F_4F_1F_2^{(2)}F_3F_1$. Similarly, there is a corresponding monomial in the Kashiwara operators which we denote $\widetilde{F}(P)$. So in our example, $\widetilde{F}(LRL-)=\widetilde{F}_4\widetilde{F}_5\widetilde{F}_2\widetilde{F}_3^{2}
\widetilde{F}_4\widetilde{F}_1\widetilde{F}_2^{2}\widetilde{F}_3\widetilde{F}_1\cdot 1$.
:::

The following theorem was conjectured by Carter:

::: theorem
[]{#spanningmonomial label="spanningmonomial"} Suppose $\bf i\in \chi_n$ is compatible with a quiver $Q$, and let $(c,{\bf i})$ be a chamber in CD$({\bf i})$. Let $P=P(c,{\bf i})$ be the corresponding partial quiver (so $P\leq Q$), with ${\bf a}=a(c,{\bf i})=(a_1,a_2,\ldots ,a_k)$. Alternatively, let $P=j\in [1,n]$. In either case, $$F_{i_1}^{(a_1)}F_{i_2}^{(a_2)}\cdots F_{i_k}^{(a_k)}=F(P).$$ In particular, the left hand side depends only upon $P$.
:::

Suppose first that $P$ is a partial quiver, and let $Y$ be a component of $P$. Our first step will be to understand where the roots in $M(Y)$ occur in CD$({\bf i})$ (as labels of crossings). Let us suppose in the first case that $Y$ is of type $L$, with $a=a(Y)$ and $b=b(Y)$. We draw the diagram for the arrangement corresponding to $Q$, defined by Berenstein, Fomin and Zelevinsky. We mark the crossing of strings $i$ and $j$, $i\leq j$ by the root $\alpha_{ij}=\alpha_i+\alpha_{i+1}+\cdots +\alpha_{j-1}$, and we write the quiver $Q$ up the left hand side, so that edge $j$ of $Q$ appears next to the left hand end of string $j$, for each $j$. We write $Q$ down the right hand side also.

Draw $4$ dashed lines on the diagram. The first, $A$, should intersect the left vertical boundary between strings $a$ and $a+1$, and go down and to the right at an angle of $-\pi/4$ (to the horizontal). The next, $B$, should intersect the left vertical boundary between strings $b$ and $b-1$ and go up and to the right at an angle of $\pi/4$. Line $C$ should intersect the right vertical boundary between strings $a$ and $a+1$ and go up and to the left at an angle of $3\pi/4$. Finally, line $D$ should intersect the right vertical boundary between strings $b$ and $b-1$, and go down and to the left, at an angle of $-3\pi/4$. For an example, in type $A_7$, where $Q=RRLLRL$ and $Y=--LL--$, with $a(Y)=3$ and $b(Y)=6$, see Figure [4](#rho){reference-type="ref" reference="rho"}.

<figure id="rho">
<p>units &lt;0.8cm,0.8cm&gt; x from -7 to 9, y from -.5 to 8</p>
<p>at 0 0 *7 0 1 / at 7 0 *7 0 1 /</p>
<p>at -0.4 0 at -0.4 1 at -0.4 2 at -0.4 3 at -0.4 4 at -0.4 5 at -0.4 6 at -0.4 7</p>
<p>at 7.4 0 at 7.4 1 at 7.4 2 at 7.4 3 at 7.4 4 at 7.4 5 at 7.4 6 at 7.4 7</p>
<p>at -1 1 at -1 2 at -1 3 at -1 4 at -1 5 at -1 6</p>
<p>at 8 1 at 8 2 at 8 3 at 8 4 at 8 5 at 8 6</p>
<p>7 7 0 / 6 6 0 / 0 7 1 / 5 2 7 / 7 7 2 / 4 4 0 / 0 7 3 / 3 3 0 / 0 7 4 / 2 2 0 / 0 7 5 / 1 6 7 / 7 7 6 / 0 7 7 /</p>
<p>4.5 4.5 0 / 2.5 4.5 7 / 4.5 2.5 0 / 2.5 2.5 7 /</p>
<p>at 2.5 3.5 at 3 4 at 4 5</p>
<p>at 3 3 at 3.5 3.5 at 4.5 4.5</p>
<p>at 4 2 at 4.5 2.5 at 5.5 3.5</p>
<p>at 2.65 3.5 at 3.15 4 at 4.15 5</p>
<p>at 3.15 3 at 3.65 3.5 at 4.65 4.5</p>
<p>at 4.15 2 at 4.65 2.5 at 5.65 3.5</p>
<p>at 4.3 -0.2 at 4.5 7 at 2.57 7 at 2.3 -0.2</p>
<figcaption>Example: <span class="math inline"><em>Q</em> = <em>R</em><em>R</em><em>L</em><em>L</em><em>R</em><em>L</em>, <em>Y</em> =  −  − <em>L</em><em>L</em> − −</span>.<span id="rho" label="rho"></span></figcaption>
</figure>

These four dashed lines bound a rectangle in the diagram; we shall see that the crossings inside it form a rectangle, $\rho$, and that their labels are precisely the positive roots in $M(Y)$. (In the example, these crossings are marked by filled circles.)

By construction, the lines crossing $\rho$ parallel to $A$ and $C$ are parts of the strings $c$ with $c\leq a$, and the lines crossing $\rho$ parallel to $B$ and $D$ are parts of the strings $d$ with $b\leq d$. Thus the crossings appearing inside $\rho$ are those labelled with roots $\alpha_{cd}$ with $1\leq c\leq a\leq b\leq d\leq n+1$, that is, the roots in $M(Y)$.

Let $E$ be the line in the rectangle we are interested in which is parallel to $C$ and closest to $C$, and suppose it is part of string $x$ and that this corresponds to an $R$ in $Q$. Let $y$ be the first string that $x$ intersects with after changing direction at the top of the diagram. By the construction of the diagram, the strings corresponding to the $L$'s of $Y$ are below the rectangle, so $y$ cannot be one of these strings. Similarly, if $y$ were a string corresponding to an $L$ to the right of $Y$, it would be parallel to $E$ initially (i.e. in the left part of the diagram) and then would only be perpendicular to $E$ below $\rho$. Also, if $y$ corresponded to an $R$ to the right of $Y$ in $Q$, $x$ and $y$ would intersect to the left of the point where $x$ changed direction. We conclude that $x$ and $y$ intersect inside $\rho$.

Thus in the corresponding chamber diagram, the top crossing of the rectangle is on row $1$ (so the corresponding simple reflection is $s_1$). Suppose next that $x$ corresponds to an $L$ in $Q$. Let $y$ be the first string that $x$ intersects. Since there can in this case be no $R$'s to the right of $Y$ in $Q$, $x$ intersects every string corresponding to an arrow of $Q$ to the right of $Y$ below the rectangle $\rho$; similarly with the $L$'s in $Y$. Thus $y$ is to the left of $P$ and $x$ and $y$ intersect in the rectangle.

Thus in both cases the top corner of the rectangle $\rho$ is in row $1$. Let us write the row of each crossing in $\rho$ next to it. The number of crossings in a side of the rectangle parallel to $A$ or $C$ (equal to the number of crossings involving $E$ inside $\rho$) is equal to $n+2-b$, and the number in a side parallel to $B$ or $D$ is $a$. Thus the labels of the crossings inside $\rho$ are the same and in the same configuration as the numbers in $\rho(Y)$.

The case when $Y$ is of type $R$ is similar; in this case the bottom corner of the rectangle in the arrangement diagram is labelled $n$.

Now suppose that $Y$ is of type $L$ and immediately to the right of $Y$ in $P$ is a component $Z$ of type $R$. By the construction of the rectangles, the leftmost crossings inside them coincide. Similarly, if $Y$ is of type $R$ and $Z$ is of type $L$, the rightmost crossings in the rectangles coincide.

Thus the structure of the rectangles corresponding to components of $P$ in the arrangement diagram, or the chamber diagram, corresponding to $\bf i$, is the same as in $D(P)$. The result follows by Theorem [\[multiset\]](#multiset){reference-type="ref" reference="multiset"}.

In the case where $P=j\in [1,n]$, let $Y=j$; here we consider $Y$ to be the vertex $j$ of $Q$, with no edges. We then argue as in the above proof for $Y$ of type $L$. $\square$

::: cor
[]{#spanningmonomialcor label="spanningmonomialcor"} Suppose we are in the situation of the Theorem, and let $\widetilde{F}(P)$ be the monomial in the root operators as defined in [\[diagonalrow\]](#diagonalrow){reference-type="ref" reference="diagonalrow"}. Then $\widetilde{F}_{i_1}^{a_1}\widetilde{F}_{i_2}^{a_2}\cdots \widetilde{F}_{i_k}^{a_k}
\cdot 1=\widetilde{F}(P)$.
:::

: This follows immediately from the Theorem, since the only relations in $U^-$ that are used are commutations, which the root operators $\widetilde{F}_i$ also satisfy. $\square$
