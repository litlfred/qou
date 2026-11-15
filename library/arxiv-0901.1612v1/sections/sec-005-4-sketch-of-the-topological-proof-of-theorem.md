---
doc_id: arxiv-0901.1612v1
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-005-4-sketch-of-the-topological-proof-of-theorem
section_title: "Sketch of the topological proof of Theorem ??"
section_number: 4
pages: 8-13
source_pdf: 0901.1612v1.pdf
source_sha256: b4f3efcadd1e5caf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.971
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
duplicate_of: "deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin"
---
[]{#sec:top_proof label="sec:top_proof"}

Starting with a link in the $3$-sphere, consider the ***delta move*** shown in Figure [1](#fig:delta){reference-type="ref" reference="fig:delta"}, which may be thought of as a higher order variant of a crossing change. It takes place within a $3$-ball, outside of which the link is left fixed.

<figure id="fig:delta">
<p><embed src="FigD.pdf" style="height:1.38889in" /> (-228,95)<span><span class="math inline"><em>X</em></span></span> (-28,99)<span><span class="math inline"><em>X</em>′</span></span> (-230,-5)<span><span class="math inline"><em>Y</em></span></span> (-20,-3)<span><span class="math inline"><em>Y</em>′</span></span> (-320,45)<span><span class="math inline"><em>Z</em></span></span> (-115,46)<span><span class="math inline"><em>Z</em>′</span></span></p>
<figcaption>The delta move <span class="math inline"><em>L</em> → <em>L</em>′</span></figcaption>
</figure>

The delta move was introduced by Murakami and Nakanishi [@MurakamiNakanishi], who proved that an appropriate sequence of such moves can transform any link into any other link with the same number of components, provided the two links have the same pairwise linking numbers.

The key organizational idea for this proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} is to show that the delta move, when applied to the three components $X$, $Y$ and $Z$ of the link $L$, as shown in Figure [1](#fig:delta){reference-type="ref" reference="fig:delta"}, increases its Milnor $\mu$-invariant by $1$, while increasing the Pontryagin $\nu$-invariant of its characteristic map $g_L$ by $2$.

The fact that the delta move increases $\mu$ by $1$ is well known to experts; our proof relies on the geometric formula for $\mu$ due to Mellor and Melvin [@MellorMelvin] in terms of how each link component pierces the Seifert surfaces of the other two components, plus a count of the triple point intersections of these surfaces. In particular, one can use a family of Seifert surfaces that differ only near the delta move, as shown in Figure [2](#fig:seifert){reference-type="ref" reference="fig:seifert"}.

![Seifert surfaces for $L$ and $L'$](FigS.pdf){#fig:seifert height="120pt"}

To see how the delta move affects the $\nu$-invariant, we will view $\nu$ as a relative Euler class, following Gompf [@Gompf] and Cencelj, Repovš and Skopenkov [@Cencelj].

To that end let $L$ and $L'$ be two three-component links in $S^3$ with the same pairwise linking numbers $p$, $q$ and $r$, and let $\mathbb L$ and $\mathbb L'$ be the framed links in the $3$-torus[^1] that are the preimages of a common regular value of their characteristic maps $g_L$ and $g_{L'}$. Orient $\mathbb L$ and $\mathbb L'$ so that, when combined with the pullback of the orientation on $S^2$ to a tangent $2$-plane transverse to these links, we get the given orientation on $T^3$. Since $L$ and $L'$ have the same pairwise linking numbers, $\mathbb L$ and $\mathbb L'$ are homologous in $T^3$. It then follows by a standard argument that $\mathbb L\times0$ and $\mathbb L'\times1$ together bound an embedded surface $\mathbb F$ in $T^3\times[0,1]$.

The ***relative normal Euler class*** $e(\mathbb F)$ is the intersection number of $\mathbb F$ with a generic perturbation of itself that is directed by the given framings along $\mathbb L\times0$ and $\mathbb L'\times1$, but is otherwise arbitrary. Then, according to Gompf and Cencelj--Repovš--Skopenkov, $$\nu(g_{L'},g_L) \ \equiv \ e(\mathbb F) \ \mod{2\gcd(p,q,r)}.$$

The key step in seeing how the delta move affects the $\nu$-invariant is to adjust $L$ and $L'$ by link homotopies so that up to isotopy $$\mathbb L' = \mathbb L\cup \mathbb L^*$$ where $\mathbb L^*$ is a two-component link bounding an annulus $\mathbb A\subset T^3- \mathbb L$ with relative normal Euler class 2. Then the surface $\mathbb F\ = \ (\mathbb L\times[0,1])\cup(\mathbb A\times 1)$, with $\partial\mathbb F= \mathbb L'\times1-\mathbb L\times0$, has $e(\mathbb F)=2$, since $e(\mathbb L\times[0,1])=0$. Thus $\nu(g_{L'},g_L) \equiv e(\mathbb F) = 2$, showing that the delta move increases the $\nu$-invariant of $L$ by $2$. Explaining how this step is carried out will complete our sketch of the topological proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}.

We begin with the delta move as shown above and change it by an isotopy so that it now appears as pictured in Figure [3](#fig:deltanu){reference-type="ref" reference="fig:deltanu"}.

<figure id="fig:deltanu">
<p><embed src="FigDelta3.pdf" style="height:1.66667in" /> (-300,10)<span><span class="math inline"><em>B</em></span></span> (-17,9)<span><span class="math inline"><em>B</em></span></span> (-320,58)<span><span class="math inline"><em>C</em></span></span> (3,58)<span><span class="math inline"><em>C</em></span></span> (-269,117)<span><span class="math inline"><em>X</em></span></span> (-275,65)<span><span class="math inline"><em>Y</em></span></span> (-272,22)<span><span class="math inline"><em>Z</em></span></span> (-67,117)<span><span class="math inline"><em>X</em>′</span></span> (-75,65)<span><span class="math inline"><em>Y</em>′</span></span> (-69,22)<span><span class="math inline"><em>Z</em>′</span></span></p>
<figcaption>A different view of the delta move</figcaption>
</figure>

From this picture, we see that the delta move can be regarded as a pair of crossing changes of opposite sign which introduce a pair of small "clasps" $\put(0,-3){\includegraphics[height=10pt]{FigUnClasp.pdf}} \put(20,0){$\longrightarrow$} \put(40,-3){\includegraphics[height=10pt]{FigClasp.pdf}}$.

We may assume that the move takes place inside the large ball $B$ in $S^3$ of radius $\pi/2$ centered at $-1$. If we think of $1$ and $-1$ as the north and south poles of $S^3$, then $B$ is just the southern hemisphere. Figure [3](#fig:deltanu){reference-type="ref" reference="fig:deltanu"} shows that inside $B$, the portions of $X$ and $X'$ lie along the great circle through $1$ and $i$ (so in fact $X$ and $X'$ coincide) while the portions of $Y$, $Z$, $Y'$ and $Z'$ lie close to the great circle $C$ through $j$ and $k$.

Outside $B$, the links $L$ and $L'$ coincide and, maintaining this coincidence, we move them into a more favorable position as follows. First unknot $X=X'$ by a link homotopy, and move it to the rest of the great circle through $1$ and $i$. Then by an isotopy move $Y$ and $Z$ into a small neighborhood of the great circle $C$, and position them so that their orthogonal projections to $C$ are Morse functions with just one critical point per critical value. As intended, $Y'$ and $Z'$ move likewise outside $B$. Note that each of the aforementioned clasps contributes two critical values to these projections, and we may assume that no other critical values fall between these two.

Now we use the asymmetric versions $\widetilde g_L$ and $\widetilde g_{L'}$ of the characteristic maps $T^3 \to S^2$, identifying the target $S^2$ with the unit $2$-sphere in the purely imaginary $ijk$-subspace of the quaternions. We interpret Figure [3](#fig:deltanu){reference-type="ref" reference="fig:deltanu"} as showing the image of $S^3 - \{1\}$ under the stereographic projection $\mathrm{\wp}_1$, and view $i$ as the north pole of $S^2$.

It is straightforward to check that, under the genericity conditions imposed above, the point $i \in S^2$ is a common regular value for $\widetilde g_L$ and $\widetilde g_{L'}$, and that the framed links $\mathbb L$ and $\mathbb L'$ in $T^3$ that are the inverse images of $i$ under these maps are for the most part the same. In fact we will show that, up to isotopy $\mathbb L' = \mathbb L\cup\mathbb L^*$ where $\mathbb L^*$ consists of a pair of oppositely oriented spiral perturbations of $S^1\times \text{pt} \times \text{pt}$, coming from the two clasps shown in Figure [3](#fig:deltanu){reference-type="ref" reference="fig:deltanu"}, and that these two spirals bound an annulus $\mathbb A$ in $T^3-\mathbb L$ whose relative normal Euler class $e(\mathbb A)$ is $2$. The argument will be given as we explain Figures [4](#fig:borromean){reference-type="ref" reference="fig:borromean"}--[6](#fig:annulus){reference-type="ref" reference="fig:annulus"}.

The discussion is independent of what the links $L$ and $L'$ look like outside the ball $B$ shown in Figure [3](#fig:deltanu){reference-type="ref" reference="fig:deltanu"}. The simplest case occurs when $L$ is the three-component unlink, and $L' = X' \cup Y' \cup Z'$ is the Borromean rings, whose stereographic image is shown in Figure [4](#fig:borromean){reference-type="ref" reference="fig:borromean"}.

<figure id="fig:borromean">
<p><embed src="BR2.pdf" style="height:1.80556in" /> (-83,65)<span><span class="math inline"> − 1</span></span> (-75,118)<span><span class="math inline"><em>i</em></span></span> (-82,11)<span><span class="math inline"> − <em>i</em></span></span> (-84,134)<span><span class="math inline">∞ ↔︎ 1</span></span> (-150,37)<span><span class="math inline"><em>C</em></span></span> (-60,1)<span><span class="math inline"><em>X</em>′</span></span> (-88,27)<span><span class="math inline"><em>Z</em>′</span></span> (-12,36)<span><span class="math inline"><em>Y</em>′</span></span></p>
<figcaption>Borromean Rings</figcaption>
</figure>

We have, as before, that $X'$ is the great circle through $1$ and $i$, with image the blue vertical axis, while $Y'$ and $Z'$ lie in a small tubular neigborhood of the great circle $C$ through $j$ and $k$, with images shown in red and green. In this circumstance, the general formula $\mathbb L' = \mathbb L\cup \mathbb L^*$ has $\mathbb L$ empty, and hence $\mathbb L' = \mathbb L^*$.

Figure [5](#fig:clasps){reference-type="ref" reference="fig:clasps"} shows enlargements of the two clasps between red $Y'$ and green $Z'$, with points on their segments labeled by numbers on $Y'$ and by letters on $Z'$, ordered consistently with their orientations.

<figure id="fig:clasps">
<p><embed src="FigCL.pdf" style="height:1.11111in" /> (-322,23)<span><span class="math inline"><em>Y</em>′</span></span> (-16,52)<span><span class="math inline"><em>Y</em>′</span></span> (-192,65)<span><span class="math inline"><em>Z</em>′</span></span> (-130,10)<span><span class="math inline"><em>Z</em>′</span></span> (-276,14)<span><span class="math inline">1</span></span> (-226,38)<span><span class="math inline">2</span></span> (-263,59)<span><span class="math inline">3</span></span> (-55,60)<span><span class="math inline">4</span></span> (-92,38)<span><span class="math inline">5</span></span> (-44,13)<span><span class="math inline">6</span></span> (-84,5)<span><span class="math inline"><em>a</em></span></span> (-55,38)<span><span class="math inline"><em>b</em></span></span> (-84,70)<span><span class="math inline"><em>c</em></span></span> (-233,69)<span><span class="math inline"><em>d</em></span></span> (-263,38)<span><span class="math inline"><em>e</em></span></span> (-233,4)<span><span class="math inline"><em>f</em></span></span></p>
<figcaption>The two clasps</figcaption>
</figure>

Our job is to find the preimage $\mathbb L'$ in $S^1 \times S^1 \times S^1$ of the regular value $i$ of the map $g_{L'}$, which means we must find the points where the vector from the green $\mathrm{\wp}_1(zx^{-1})$ to the red $\mathrm{\wp}_1(yx^{-1})$ points straight up.

We pause to see the effect of right multiplication by $x^{-1}$. Let $x$ travel along $X = X'$ from $1$ to $-i$ to $-1$ to $i$ and back to $1$, which is the direction in which this component is oriented. Then right multiplication by $x^{-1}$ gradually rotates this component in the opposite direction. In the image $3$-space, it looks like the vertical axis is moving downwards. At the same time, the great circle $C$ through $j$ and $k$ is gradually rotated in the direction from $j$ towards $-k$. A small tubular neighborhood of $C$ follows this rotation and twists as it goes, dragged by the downward motion of the vertical axis.

Now focusing on the left clasp, and starting with $x = 1$, we see that the arrow $\vec{f2}$ from green $f$ to red $2$ points up. As $x$ moves around $X'$ from $1$ towards $-i$ (up on the blue vertical axis) a loop of upward pointing vectors is traced out, passing successively through $\vec{e1}$, $\vec{d2}$, $\vec{e3}$, and finally back to $\vec{f2}$. In Figure [6](#fig:annulus){reference-type="ref" reference="fig:annulus"}, the $3$-torus is depicted as a cube, in which this loop is shown near the front left corner of the bottom red-green square, traced in a counterclockwise direction. When the progression of $x(s)$ values is taken into account, we get the orange spiral curve shown above this loop. This is one component of $\mathbb L'$, and is oriented according to the convention for framed links.

<figure id="fig:annulus">
<p><embed src="FigAN.pdf" style="height:2.22222in" /> (-175,90)<span><span class="math inline"><em>T</em><sup>3</sup></span></span> (-85,75)<span><span class="math inline">𝔸</span></span> (-142,-7)<span><span class="math inline"><em>f</em></span></span> (-131,-7)<span><span class="math inline"><em>e</em></span></span> (-120,-7)<span><span class="math inline"><em>d</em></span></span> (-94,-7)<span><span class="math inline"><em>c</em></span></span> (-83,-7)<span><span class="math inline"><em>b</em></span></span> (-72,-7)<span><span class="math inline"><em>a</em></span></span> (-8,34)<span><span class="math inline">6</span></span> (-11,28)<span><span class="math inline">5</span></span> (-15.5,24)<span><span class="math inline">4</span></span> (-21,17)<span><span class="math inline">3</span></span> (-26,11)<span><span class="math inline">2</span></span> (-30,6)<span><span class="math inline">1</span></span> (-40,127)<span><span class="math inline"><em>s</em></span></span> (2,57)<span><span class="math inline"><em>t</em></span></span> (-163,2)<span><span class="math inline"><em>u</em></span></span></p>
<figcaption>Computing <span class="math inline"><em>e</em>(𝔸) = 2</span></figcaption>
</figure>

Focusing on the right clasp and repeating the above procedure, we get the orange spiral curve shown at the right rear, lying over the loop $\vec{a5}\,\vec{b6}\,\vec{c5}\,\vec{b4}$. This is the other component of $\mathbb L'$, and is also oriented according to convention.[^2]

Together, the components of $\mathbb L'$ bound the orange annulus $\mathbb A$ shown in the cube. This annulus is constructed as follows. Each point on the left spiral loop is joined to the point on the right spiral loop at the same height $s$ by a straight line segment in the 2-torus $s \times S^1 \times S^1$. The $t$-coordinate moves steadily so that $y(t)$ travels along the arc of $Y'$ which lies in the ball $B$ (joining $3$ to $4$) and the $u$-coordinate moves steadily so that $z(u)$ travels along the arc of $Z'$ which lies in $B$ (joining $d$ to $c$). It is easy to see that this annulus $\mathbb A$ is embedded in the $3$-torus and that, even in the general case where $\mathbb L$ is not empty, it would still be disjoint from $\mathbb L$.

Now since $\mathbb A$ lies in $T^3$, its relative normal Euler class $e(\mathbb A)$ (when viewed as a surface in $T^3\times[0,1]$) can be computed as the intersection number of $\mathbb A$ with the inverse image of any other regular value of $\widetilde g_{L'}$. In particular, the point $-i$ is also a regular value, and its inverse image $\widehat\mathbb L'$ is calculated from an analysis of the clasps, just as we did for the inverse image of $i$. It consists of two spirals, which can be obtained from the spirals in $\mathbb L'$ by moving them half-way along in the vertical (blue) direction. We show $\widehat\mathbb L'$ in Figure [6](#fig:annulus){reference-type="ref" reference="fig:annulus"} as a pair of purple spirals, which are oriented the same way as the orange spirals.

It is seen in this figure that the purple spirals pierce the orange annulus twice in the positive direction, confirming that $$e(\mathbb A)  \ =  \ \mathbb A\,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\, \widehat\mathbb L'  \ =  \ 2,$$ and completing the sketch of the topological proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}.

[^1]: For the reader's convenience, all subsets of $T^3$ in this section are written in blackboard bold to distinguish them from subsets of $S^3$.

[^2]: In fact, one need not go through the careful analysis to determine the orientations of the spirals. All that is important is that they are oppositely oriented, which follows from the fact that the pairwise linking numbers for the Borromean rings are zero.
