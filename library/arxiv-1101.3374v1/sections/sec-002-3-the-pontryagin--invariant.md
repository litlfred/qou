---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-002-3-the-pontryagin--invariant
section_title: "The Pontryagin -invariant"
section_number: 3
pages: 12-20
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.98
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
[]{#sec:pontryagin label="sec:pontryagin"}

Heinz Hopf proved in 1931 that homotopy classes of maps from the $3$-sphere to the $2$-sphere are in one-to-one correspondence with the integers via his now famous Hopf invariant. Pontryagin [@Pontryagin41] generalized this to give the homotopy classification for maps from an arbitrary finite $3$-complex to the $2$-sphere. It is convenient for our purposes to restrict to smooth maps from $3$-manifolds to the $2$-sphere, and to use Poincaré duality to take Pontryagin's result, originally presented via cohomology, and reformulate it in homological terms.

Fix a closed oriented smooth $3$-manifold $M$. The homotopy classification of maps $f: M\to S^2$ can be expressed using two differential topological invariants.

The primary invariant $$\lambda(f) \ \in \ H_1(M) \qquad\text{(with integral coefficients understood)}$$ records the homology class of the preimage link $\mathcal L= f^{-1}(*)$ of any regular value $\mathrm{*}$ of $f$ (oriented as explained below), or equivalently the Poincaré dual of the pull-back $f^*(\omega)$ of the orientation class $\omega\in H^2(S^2)$. It is easily shown that two maps have the same primary invariant if and only if they induce the same map on homology.

The secondary invariant $$\nu(f_0,f_1) \ \in \ \mathbb Z_{2d(\lambda)}$$ compares two maps $f_0$ and $f_1$ with the same primary invariant $\lambda$. Here $d(\lambda)$ is the divisibility of $\lambda$ as an element of the free abelian group $H_1(M)/$torsion. Thus $d(\lambda) = 0$ if $\lambda$ is of finite order, and otherwise $d(\lambda)$ is the largest positive integer $d$ for which $\lambda = d\kappa$ for some $\kappa\in H_1(M)$.

For example, if $M$ is the $3$-torus $T^3$, then $\lambda(f) = (p,q,r) \in H_1(T^3) \cong \mathbb Z^3$ where $p$, $q$ and $r$ are the degrees of $f$ restricted to the coordinate $2$-tori, and the divisibility $d(p,q,r)$ is the greatest common divisor of $p$, $q$ and $r$.

In the next few paragraphs, we discuss these invariants $\lambda$ and $\nu$ in more detail, and provide a natural way, in the special case that $M$ is the $3$-torus, to transform $\nu$ from a relative invariant into an absolute one, meaning a function of a single map.

First recall that a *framing* of a smooth link in $M$ is a homotopy class of trivializations of the normal bundle of the link. It can be represented by an orthonormal triple $(\textup{\bf u},\textup{\bf v},\textup{\bf t})$ of vector fields along the link with respect to some Riemannian metric on $M$, where $\textup{\bf t}$ is tangent to the link. We can use this to orient the link by $\textup{\bf t}$ by insisting that the triple give the orientation on $M$. Conversely, if the link is already oriented by $\textup{\bf t}$, then the framing can be specified by a single unit normal vector field $\textup{\bf u}$, as $\textup{\bf v}$ is then determined by the condition that $(\textup{\bf u},\textup{\bf v},\textup{\bf t})$ be an orthonormal frame giving the orientation on $M$. In pictures, therefore, we often indicate a framing on an oriented link by simply drawing a thin parallel push-off of the link, recording the tips of the vectors in $\textup{\bf u}$.

Now given a map $f:M\to S^2$ with regular value $*$, the link $\mathcal L= f^{-1}(*)\subset M$ inherits a framing by pulling back an oriented basis for the tangent space to $S^2$ at $*$, and acquires an orientation from this framing, as above. Equipped with this framing and orientation, $\mathcal L$ will be called the ***Pontryagin link*** of $f$ at $\mathrm{*}$.

Note that any framed oriented link $\mathcal L$ in $M$ arises as the Pontryagin link of some map from $M$ to $S^2$. In particular, the ***Pontryagin--Thom construction*** produces such a map, given by wrapping each normal disk fiber of a tubular neighborhood of $\mathcal L$ around the $2$-sphere by the exponential map, using the framing to identify the fiber with the disk of radius $\pi$ in the tangent space to $S^2$ at $*$, and sending everything outside the neighborhood to the antipode of $*$. This construction provides a one-to-one correspondence $$[M,S^2] \ \longleftrightarrow \ \Omega_1^{\text{fr}}(M)$$ where $[M,S^2]$ is the set of homotopy classes of maps $M\to S^2$, and $\Omega_1^{\text{fr}}(M)$ is the set of framed bordism classes of framed oriented links in $M$ (see e.g. Chapter 7 in Milnor [@Milnor65]).

Now we return to our discussion of the invariants associated with maps $f:M\to S^2$.

An easy argument shows that the primary invariant $\lambda(f)$, the homology class of the oriented link $f^{-1}(*)$, is independent of the choice of regular value $*$, and that $\lambda(f)$ is invariant under homotopies of $f$. Indeed, the preimages $\mathcal L_0$ and $\mathcal L_1$ of any regular values for any pair of maps homotopic to $f$ are bordant in $M\times[0,1]$ (see Milnor [@Milnor65] for a proof). It follows that $\mathcal L_0$ and $\mathcal L_1$ are homologous in $M$. Conversely, homologous links in $M$ are bordant in $M\times[0,1]$ by a standard argument going back to Thom [@Thom].

This shows that the partition of $[M,S^2]$ into subsets $[M,S^2]_\lambda$ according to their primary invariants $\lambda\in H_1(M)$ corresponds to the partition of $\Omega_1^{\text{fr}}M$ into *unframed* bordism classes.

The secondary invariant associated with a pair of bordant framed links measures the obstruction to extending the framings on the links across any bordism between them. More precisely, given $f_0$ and $f_1$ in $[M,S^2]_\lambda$ with Pontryagin links $\mathcal L_0$ and $\mathcal L_1$, and an oriented surface $\mathcal F\subset M\times[0,1]$ with $\partial\mathcal F=  \mathcal L_1\times1 - \mathcal L_0\times0$, the framings on $\mathcal L_0$ and $\mathcal L_1$ combine to give a normal framing of $\mathcal F$ along its boundary. The obstruction to extending this framing across $\mathcal F$ is measured by its relative Euler class $e(\mathcal F)$ in $H^2(\mathcal F,\partial\mathcal F;\pi_1SO(2)) = \mathbb Z$, which in homological terms is the intersection number of $\mathcal F$ with a generic perturbation of itself that is directed by the given framings along $\partial\mathcal F$. This class depends on the choice of the regular values of $f_0$ and $f_1$ used to define the Pontryagin links, and on the choice of the bordism $\mathcal F$ between the links. But the residue class of $e(\mathcal F)$ mod $2d(\lambda)$ does not depend on these choices; see Gompf [@Gompf] and Cencelj, Repovš and Skopenkov [@Cencelj] for details, and also see Auckly and Kapitanksi [@AucklyKapitanski]. This residue class $$\nu(f_0,f_1)  \ = \ e(\mathcal F) \textup{ mod }2d(\lambda) \ \in \ \mathbb Z_{2d(\lambda)}$$ will be referred to as the ***relative Pontryagin $\nu$-invariant*** of $f_0$ and $f_1$.

The task of converting $\nu$ into an *absolute* invariant, that is, changing it from a function of two variables to a function of one variable, requires the choice of a ***base map*** $f_\lambda$ in each subset $[M,S^2]_{\lambda}$ of homotopy classes of maps with primary invariant $\lambda$. One can then define the ***absolute Pontryagin $\nu$-invariant*** by $$\nu(f) \ = \ \nu(f,f_\lambda)$$ for any $f\in[M,S^2]_\lambda$. Whether such choices can be made in a topologically meaningful way depends on the manifold $M$.

For example, Pontryagin [@Pontryagin41 page 356] explicitly cautioned against trying to make this choice when $M=S^1\times S^2$. In this case there are, up to homotopy, exactly two maps to $S^2$ with primary invariant $1\in H_1(S^1\times S^2) = \mathbb Z$, meaning degree $1$ on the cross-sectional $2$-spheres in $S^1\times S^2$. One of these is the projection $f_0(\theta,x)  =  x$ to the $S^2$ factor, and the other is the twist map $f_1(\theta,x)  =  \mathrm{rot}_\theta(x)$ that rotates the $S^2$ factor once while traversing the $S^1$ factor; here $\mathrm{rot}_\theta$ indicates rotation of $S^2$ through an angle $\theta$ about its polar axis. Note that the double twist $f_2(\theta,x)  =  \mathrm{rot}_{2\theta}(x)$ is homotopic to $f_0$.

What Pontryagin observed is that $f_0$ and $f_1$ differ by an automorphism of $S^1\times S^2$, and so there is no natural way to choose which one should serve as the base map for the homology class $[S^1\times S^2,S^2]_1$. More precisely, the automorphism $h$ given by $h(\theta,x)  =  (\theta,\mathrm{rot}_\theta(x))$ satisfies $f_0h=f_1$, while $f_1h=f_2$, which is homotopic to $f_0$. Thus the maps $f_0$ and $f_1$ have equal topological status, and so neither is more basic than the other.

A key feature of this example is the existence of a homotopically nontrivial automorphism of $S^1\times S^2$ that induces the identity on homology. In general, if a $3$-manifold $M$ supports such an automorphism $h$, then $\lambda(fh) = \lambda(f)$ for any map $f:M\to S^2$. Hence the existence of $h$ provides a potential obstruction to the natural choice of base maps in $[M,S^2]_\lambda$ for all $\lambda$. The $3$-torus has no such automorphisms, due to the fact that its higher homotopy groups vanish.

For each triple of integers $p$, $q$ and $r$, we now show how to pick out a specific map $f_{pqr}:T^3\to S^2$ having these preassigned cross-sectional degrees, which can serve in a topologically meaningful way as the base map for the set $[T^3,S^2]_{(p,q,r)}$ of all such maps.

We will describe $f_{pqr}$ by specifying its Pontryagin link $\mathcal L_{pqr}$, as follows. Choose three pairwise disjoint circles $\mathcal C_s$, $\mathcal C_t$ and $\mathcal C_u$ that are cosets of the coordinate circle subgroups $$S^1_s = S^1 \times 0 \times 0 \ , \ S^1_t = 0 \times S^1 \times 0 \ \text{ and } \ S^1_u = 0 \times 0 \times S^1$$ of the $3$-torus (where as usual $S^1=\mathbb R/2\pi\mathbb Z$) with disjoint tubular neighborhoods $\mathcal N_s$, $\mathcal N_t$ and $\mathcal N_u$. Equip these circles with their ***coordinate framings*** induced from the Lie framing $(\partial_s,\partial_t,\partial_u)$ of the tangent bundle of $T^3$, that is, $(\partial_t,\partial_u)$ for $\mathcal C_s$, $(\partial_u,\partial_s)$ for $\mathcal C_t$ and $(\partial_s,\partial_t)$ for $\mathcal C_u$. Then construct $\mathcal L_{pqr}$ from $p$ parallel copies of $\mathcal C_s$ in $\mathcal N_s$ (meaning $p$ distinct cosets of $S^1_s$ lying in $\mathcal N_s$), $q$ copies of $\mathcal C_t$ in $\mathcal N_t$ and $r$ copies of $\mathcal C_u$ in $\mathcal N_u$, all with their coordinate framings, as indicated in Figure [1](#fig:basemaps){reference-type="ref" reference="fig:basemaps"}. Thus $f_{pqr}$ wraps the disk fibers of the tubes $\mathcal N_s$, $\mathcal N_t$ and $\mathcal N_u$ around $S^2$ by maps of degree $p$, $q$ and $r$, and is constant elsewhere.

<figure id="fig:basemaps">
<p><embed src="FigBaseMaps.pdf" style="height:1.66667in" /> (-128,-2)<span><span class="math inline"><em>s</em></span></span> (-76,122)<span><span class="math inline"><em>u</em></span></span> (1,39)<span><span class="math inline"><em>t</em></span></span> (-110,40)<span><span class="math inline"><em>p</em></span></span> (-90,66)<span><span class="math inline"><em>q</em></span></span> (-50,25)<span><span class="math inline"><em>r</em></span></span></p>
<figcaption>Pontryagin link <span class="math inline">ℒ<sub><em>p</em><em>q</em><em>r</em></sub></span> for the base map <span class="math inline"><em>f</em><sub><em>p</em><em>q</em><em>r</em></sub></span></figcaption>
</figure>

Here and below, the $3$-torus is pictured as the cube $[0,2\pi]^3$ in $stu$-space with opposite faces identified. The axes correspond to the coordinate circles $S^1_s$, $S^1_t$ and $S^1_u$, and the coordinate framings are the "blackboard\" framings, i.e. those given by parallel push-offs in the projection shown. The link $\mathcal L_{5\,3\,-2}$ is shown in the figure. Note that by construction $\mathcal L_{000}$ is empty, so $f_{000}$ is constant.

Our goal is to give a simple procedure for computing the Pontryagin $\nu$-invariant of a map $f:T^3\to S^2$ from a "toral diagram\" of its Pontryagin link $\mathcal L$.

By definition, a ***toral diagram*** of $\mathcal L$ consists of

::: indentation
.05em1em

1.  a classical oriented link diagram $\mathcal D$ in the $2$-torus $T^2$ with ***crossings*** $\mathcal C$,

2.  a finite set of signed points in $T^2$, the ***marked points***, partitioned into the ***isolated*** ones $\mathcal M\subset T^2-\mathcal D$, and the ***internal*** ones $\mathcal N\subset\mathcal D-\mathcal C$, []{#markedpoints label="markedpoints"} and

3.  integer ***framings*** for each component of $\mathcal D$ and each point in $\mathcal M$.
:::

For example, the link $\mathcal L_{pqr}$ above is duplicated in Figure [2](#fig:diagrams){reference-type="ref" reference="fig:diagrams"}(a) with its toral diagram beneath it, and another example is given in Figure [2](#fig:diagrams){reference-type="ref" reference="fig:diagrams"}(b).

<figure id="fig:diagrams">
<p><embed src="FigDiagrams.pdf" style="height:2.43056in" /> (-100,24)<span><span class="math inline">3</span></span> (-39,12)<span><span class="math inline">2</span></span> (-300,-20)<span>(a) The link <span class="math inline">ℒ<sub><em>p</em><em>q</em><em>r</em></sub></span> and its diagram</span> (-100,-20)<span>(b) Another example</span></p>
<figcaption>Toral diagrams of framed links in <span class="math inline"><em>T</em><sup>3</sup></span></figcaption>
</figure>

It is understood that $\mathcal L$ should project to $\mathcal D\cup\mathcal M$ under the projection $T^3\to T^2$ sending $(s,t,u)$ to $(s,t)$, and so points in $\mathcal M$ correspond to vertical components $\mathrm{*}\times\mathrm{*}\times S^1$ in $\mathcal L$, oriented up or down according to the signs. The points in $\mathcal N$ correspond to transverse intersections of $\mathcal L$ with the ***horizontal $2$-torus***  $T^2\times0$ -- shaded in the figures -- where the sign $+1$ or $-1$ indicates whether the curve points up or down near the intersection.

To explain the crossings $\mathcal C$, view $T^3$ as the cube $[0,2\pi]^3$ in $stu$-space with opposite faces identified, as before, and $T^2$ as the square $[0,2\pi]^2$ in the $st$-plane with opposite sides identified. Above $\mathcal D-\mathcal N$, the link $\mathcal L$ resides in $T^2\times(0,2\pi)$. At a crossing, the over-crossing strand is the one with the larger vertical $u$-coordinate in the cube.

Finally, the framings specify a push-off of $\mathcal L$ by comparison with the blackboard framing of $\mathcal D\cup\mathcal M$ in $T^2$. These "blackboard\" framings are obtained by pushing $\mathcal D\cup\mathcal M$ off itself in the direction of a normal vector field in $T^2$, and then lifting these push-offs to a collection of framing curves for the components of $\mathcal L$ that we call their *$0$-framings*. For vertical circles, these are just the coordinate framings. Now the $n$-framing on any given component of $\mathcal L$ is the one obtained from the $0$-framing by adding $n$ full twists, right or left handed according as $n$ is positive or negative.

In these figures we typically indicate the framing on the link in $T^3$ by a thin push-off, and use the convention that the unlabeled components of the diagram have framing zero, that is, the blackboard framing. We also denote the positive marked points in the diagram with solid dots, and the negative ones with hollow dots.

We have allowed isolated marked points in the definition above so that projections of links such as $\mathcal L_{pqr}$ will qualify as toral diagrams, and to facilitate our later work. Note, however, that a generic isotopy of $\mathcal L$ will eliminate the set $\mathcal M$ of isolated marked points, converting an $n$-framed isolated marked point -- corresponding to a vertical circle in $\mathcal L$ -- into a small $(n\pm1)$-framed circle with one internal marked point -- corresponding to a spiral perturbation of the vertical circle. More precisely, using the notation above of solid dots for positive marked points and hollow dots for negative ones, we have

$$\includegraphics[height=25pt]{FigIso.pdf}
\put(-250,11){$=$}
\put(-205,11){$=$}
\put(-261,3){\small$n$}
\put(-235,-5){\small$n-1$}
\put(-190,-5){\small$n+1$}
\put(-135,10){and}
\put(-85,10){$=$}
\put(-40,10){$=$}
\put(-93,2){\small$n$}
\put(-66,-6){\small$n+1$}
\put(-24,-6){\small$n-1$}$$ as is readily verified by a suitable picture in the $3$-torus.

Now suppose we are given a toral diagram of a Pontryagin link $\mathcal L$ for a map $f:T^3\to S^2$. We say that the diagram ***represents*** $f$, and seek to compute $\nu(f)$ from it.

First observe that the primary invariant $$\lambda(f) \ = \ (p,q,r) \label{primary}$$ is easily read from the diagram. Indeed $p$ and $q$ (which are the degrees of the projections of $\mathcal L$ to the horizontal circle factors $S^1_s$ and $S^1_t$) are just the intersection numbers of $\mathcal D$ with $S^1_t$ and $-S^1_s$, and $r$ (the degree of the projection of $\mathcal L$ to the vertical circle $S^1_u$ , or equivalently the intersection number of $\mathcal L$ with the horizontal $2$-torus) is the sum of the signs of all the marked points. We call $p$ and $q$ the ***horizontal winding numbers*** of the diagram, and $r$ its ***vertical winding number***. For what follows, we will also need to consider the vertical winding of the individual components of $\mathcal L$. Each such component $\mathcal L_i$ projects either to some subset $\mathcal D_i$ of $\mathcal D$, or to a point $\mathcal M_i$ in $\mathcal M$ (if $\mathcal L_i$ is vertical). In either case, we call this projected image the "$i^\text{th}$ component\" of the diagram, and write $r_i$ for the sum of all the marked points that lie on it. Clearly $r_i$ is just the vertical winding number of $\mathcal L_i$, and $\sum r_i = r$, the total vertical winding number of the diagram.

To compute $\nu(f)$, we will transform $\mathcal L$ by a sequence of framed bordisms into $\mathcal L_{pqr}$ with some extra twists in the framing. The number of twists is by definition $\nu(f)$; counting these twists ultimately yields the simple formula for $\nu(f)$ that will be given in Proposition [\[prop:pontryagin\]](#prop:pontryagin){reference-type="ref" reference="prop:pontryagin"}.

To cleanly state this formula, we assume from the outset that our diagram has no crossings. There is no loss of generality in doing so since the crossings can be eliminated by ***saddle bordisms*** of $\mathcal L$, as illustrated in Figure [3](#fig:crossing){reference-type="ref" reference="fig:crossing"} (viewing $\mathcal L$ from the top, looking down on a crossing in the horizontal torus) which of course do not change $\nu(f)$. Furthermore, we will see that the Pontryagin link of a "generic link\" (to be defined in Section [\[sec:Aprep\]](#sec:Aprep){reference-type="ref" reference="sec:Aprep"}), has a toral diagram without crossings.

<figure id="fig:crossing">
<p><embed src="FigCrossing1.pdf" style="height:0.97222in" /> (-193,28)<span><span class="math inline">∼</span></span> (-201,17)<span>bordism</span> (-87,28)<span><span class="math inline">=</span></span></p>
<figcaption>Using saddles to eliminate crossings</figcaption>
</figure>

Each such saddle bordism is achieved by adding a $1$-handle, as indicated on the left side of Figure [4](#fig:bordism){reference-type="ref" reference="fig:bordism"}, and drawn in full, suppressing one dimension in $T^3$, on the right side.

![The saddle bordism](FigBordism.pdf){#fig:bordism height="80pt"}

The effect of the saddle bordism on the diagram is easy to describe. If it is used to eliminate a self-crossing of an $n_i$-framed component $\mathcal D_i$ (meaning $\mathcal D_i$ is the projection of a component $\mathcal L_i$ of $\mathcal L$) then $\mathcal D_i$ splits into two components whose framings must add up to $n_i\pm1$, depending on the sign of the crossing. Beyond this condition, the framings on the new components can be chosen arbitrarily since twists in the original framing can be shifted along $\mathcal L_i$ at will. If the saddle bordism is used to eliminate a crossing between distinct components $\mathcal D_i$ and $\mathcal D_j$ of $\mathcal D$ with framings $n_i$ and $n_j$, then the result is a single component with framing $n_i+n_j\pm1$.

Once we have a toral diagram *without crossings* representing $f$, the extra data needed to compute $\nu(f)$ is the list of ***vertical winding numbers*** $r_i$ of its components together with one additional integer $n=\sum n_i$, the sum of all the component framings $n_i$, which we call the ***total framing*** and place as a label next to the diagram.

To state the formula efficiently, we will use one more list of numbers that is easily read from the diagram. First pick a basepoint $*$ in $T^2$ away from $\mathcal D\cup\mathcal M$, and then for each $i$, choose an arc $\gamma_i$ that runs from the $i^\text{th}$ component of $\mathcal D\cup\mathcal M$ to $*$. Now define the ***depth*** []{#depth label="depth"} of the $i^\text{th}$ component to be $$d_i \ = \ 2\,\gamma_i\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,\mathcal D\mod{2\gcd(p,q,r)}

\,,$$ that is, twice the intersection number in $T^2$ of the arc $\gamma_i$ with the union $\mathcal D$ of the closed curves in the diagram. This intersection number must be properly interpreted for components of $\mathcal D$. In this case the initial point of $\gamma_i$ lies on $\mathcal D$, contributing $\pm\frac12$ to the intersection number, and thus $\pm1$ to $d_i$. It follows that $d_i$ is always an odd integer for components of $\mathcal D$, and an even integer for components of $\mathcal M$, meaning isolated marked points. An example is shown in Figure [5](#fig:depth){reference-type="ref" reference="fig:depth"}.

<figure id="fig:depth">
<p><embed src="FigDepth.pdf" style="height:1.66667in" /> (-107,87)<span><span class="math inline">𝒟<sub><em>i</em></sub></span></span> (-100,68)<span><span class="math inline"><em>γ</em><sub><em>i</em></sub></span></span> (-26,31)<span><span class="math inline">ℳ<sub><em>j</em></sub></span></span> (-20,57)<span><span class="math inline"><em>γ</em><sub><em>j</em></sub></span></span> (-195,60)<span><span class="math inline">$d_i = 2\cdot2\frac12 = 5$</span></span> (8,47)<span><span class="math inline"><em>d</em><sub><em>j</em></sub> = 2 ⋅  − 1 =  − 2</span></span></p>
<figcaption>Depths of components in the diagram</figcaption>
</figure>

Of course the depth $d_i$ depends on the choice of arc $\gamma_i$, but only modulo $2\gcd(p,q)$, and so it is certainly well defined modulo $2\gcd(p,q,r)$. Furthermore, in the formula for $\nu(f)$ below, the depths appear only as coefficients in the sum $\sum d_ir_i$. It is readily seen that this sum changes by a multiple of $\sum 2r_i = 2r$ when moving the basepoint $*$, and so it is well defined modulo $2\gcd(p,q,r)$, independent of the choices of $*$ and of the arcs $\gamma_i$.

We can now state the main result of this section.

::: proposition
[]{#prop:pontryagin label="prop:pontryagin"} **Let $f:T^3\to S^2$ be a smooth map whose Pontryagin link $\mathcal L$ is represented by a toral diagram in $T^2$ without crossings, with horizontal winding numbers $p$ and $q$, vertical winding number $r$, and total framing $n$. Then the primary and secondary Pontryagin invariants of $f$ are given by $$\begin{aligned}
\lambda(f) \ &= \ (p,q,r) \quad\text{and} \\
\nu(f) \ &= \ n + pq + \textstyle\sum d_ir_i \mod{2\gcd(p,q,r)}
\end{aligned}$$ where $r_i$ and $d_i$ are the vertical winding numbers and depths $($with respect to any chosen basepoint$)$ of the components of the diagram.**
:::

::: proof
*Proof.* The formula for $\lambda(f)$ was derived on page , and the formula for $\nu(f)$ is, as explained above, at least well defined modulo $2\gcd(p,q,r)$, independent of the choice of basepoint. So it remains to verify that this is the correct formula for $\nu(f)$.

First observe that, in the absence of crossings, the integers $r_i$ are all that are needed to recover the link $\mathcal L$ up to *isotopy*. In particular, each nonvertical component of $\mathcal L$ can be taken to wind monotonically around the last circle factor of $T^3$. Furthermore, equipped with the total framing $n$, we can recover the framed link $\mathcal L$ up to *framed bordism*. To see this, note that a pair of saddle bordisms can be used as shown in Figure [6](#fig:framing){reference-type="ref" reference="fig:framing"} to transfer a twist in the framing from any component of $\mathcal L$ to any other, and so we can distribute the framings in any desired way among the components.

<figure id="fig:framing">
<p><embed src="FigFraming.pdf" style="height:1.11111in" /> (-183,32)<span><span class="math inline">∼</span></span> (-117,32)<span><span class="math inline">=</span></span> (-55,32)<span><span class="math inline">∼</span></span></p>
<figcaption>Using saddles to transfer twists</figcaption>
</figure>

We now propose to transform $\mathcal L$ by a sequence of framed bordisms into $\mathcal L_{pqr}$ with some extra twists in the framing. These correspond to homotopies of $f$ and so do not change the Pontryagin invariant $\nu(f)$. We will carry this out on a diagrammatic level, transforming our given toral diagram, with total framing $n$, to the diagram for $\mathcal L_{pqr}$ shown in Figure [2](#fig:diagrams){reference-type="ref" reference="fig:diagrams"}(a) with some total framing, which by definition will equal $\nu(f)$. So we must simply keep track of the change in the total framing as we proceed.

We first use saddle bordisms to replace the vertical winding of each non-vertical component $\mathcal L_i$ by $|r_i|$ zero-framed vertical components, at the cost of adding $r_i$ to the total framing. The new vertical circles are "adjacent\" to $\mathcal D_i$ -- meaning displaced slightly to the *right* of it in the projection -- and oriented up or down according to the sign of $r_i$.

This is illustrated in Figure [7](#fig:winding){reference-type="ref" reference="fig:winding"}. The net effect on the diagram is to reduce all the vertical winding numbers to zero on the components of $\mathcal D$ (i.e. to eliminate the internal marked points $\mathcal N$), to add $\sum|r_j|$ isolated marked points, and to add $\sum r_j$ to the total framing of the diagram, where the sums are only over the non-vertical components of $\mathcal L$.

<figure id="fig:winding">
<p><embed src="FigWinding.pdf" style="height:2.08333in" /> (-102,100)<span><span class="math inline">∼</span></span> (-134,5)<span><span class="math inline"><em>n</em></span></span> (-4,5)<span><span class="math inline"><em>n</em> + 1</span></span></p>
<figcaption>Using saddles to replace vertical winding by vertical circles</figcaption>
</figure>

Since our target is the base link $\mathcal L_{pqr}$ (with extra twists), the vertical circles must be gathered together. This is the purpose of our base point $*$, which will serve as a gathering spot, and the arcs $\gamma_i$, which will serve as the paths in $T^2$ along which to move the vertical circles which at the moment are adjacent to the $\mathcal L_i$. At each intersection of $\gamma_i$ with a component of $\mathcal D$, these vertical circles must cross the corresponding strand of $\mathcal L$. This crossing can be accomplished by a pair of saddle bordisms as indicated in Figure [8](#fig:gathering){reference-type="ref" reference="fig:gathering"}, adding $\pm2$ to the diagram framing. On the diagrammatic level, this can viewed as a two step process, running the bordism shown in Figure [7](#fig:winding){reference-type="ref" reference="fig:winding"} backwards and then forwards, in order to move an isolated marked point across a component of $\mathcal D$, as shown at the bottom of the figure.

<figure id="fig:gathering">
<p><embed src="FigGathering.pdf" style="height:2.08333in" /> (-240,100)<span><span class="math inline">∼</span></span> (-110,100)<span><span class="math inline">∼</span></span> (-275,5)<span><span class="math inline"><em>n</em> − 1</span></span> (-134,5)<span><span class="math inline"><em>n</em></span></span> (0,5)<span><span class="math inline"><em>n</em> + 1</span></span></p>
<figcaption>Using saddles to gather the vertical circles</figcaption>
</figure>

Now it is easy to check that the act of removing the vertical winding of the nonvertical components of $\mathcal L$, and then gathering all the resulting vertical circles (including the original ones corresponding to $\mathcal M$) will add $\sum d_ir_i$ to the total framing of the diagram. Visually, this process can be thought of as a "migration\" to the base point of all the marked points in the diagram.

Next use disk bordisms to remove the null homotopic components of $\mathcal D$ (arranging for them to be $0$-framed by storing their twists elsewhere, as explained above) and similarly use annular bordisms to remove any pair of curves that are parallel but oppositely oriented. The diagram now consists of a $(p,q)$ torus link in $T^2$ (meaning $c$ parallel copies of the $(p',q')$ torus knot, where $p=cp'$ and $q=cq'$ with $p'$ and $q'$ relatively prime) together with $r$ isolated marked points near $*$. The total framing, which was originally equal to $n$, has changed to $n+\sum d_ir_i$.

Finally we transform the $(p,q)$ torus link by using saddle bordisms (reversing the process described above for removing crossings) into $p$ copies of $S^1_s$ and $q$ copies of $S^1_t$, grouped as in $\mathcal L_{pqr}$, at the cost of adding $pq$ to the total framing. Thus we have arrived at $\mathcal L_{pqr}$, having changed the total framing from $n$ to $n+pq + \sum d_ir_i.$ This verifies the stated formula for $\nu(f)$, and completes the proof of Proposition [\[prop:pontryagin\]](#prop:pontryagin){reference-type="ref" reference="prop:pontryagin"}. ◻
:::

The following application will arise in the proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} in Section [\[sec:A\]](#sec:A){reference-type="ref" reference="sec:A"}.

::: example
[]{#ex:basecase label="ex:basecase"}

If $f$ is represented by the $\pm(pq+r)$-framed $(p,q)$ torus link in $T^2$, with one component $K$ of vertical winding number $r$, and the rest of vertical winding number zero, then $\lambda(f)  = (p,q,r)$, and choosing a base point adjacent to $K$, $$\nu(f) \ = \ (pq+r) + pq + (1\cdot r + 0 + 0) \ = \ 2(pq+r) \ = \ 0 \ \in \mathbb Z_{2\gcd(p,q,r)}.$$
:::
