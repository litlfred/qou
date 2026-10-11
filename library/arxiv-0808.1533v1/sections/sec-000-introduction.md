---
doc_id: arxiv-0808.1533v1
doc_title: "On the third order helicity of magnetic ﬁelds on invariant domains in S3 R. Komendarczyk ∗"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-23
source_pdf: 0808.1533v1.pdf
source_sha256: 85bb9732afdd70ea
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order heli city of a volume preserving vector ﬁeld B, which leads us to a"
duplicate_of: "arxiv-0808.1533v3"
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.986
---
A purpose of this paper is to develop a particular formula for the third order helicity on certain invariant sets of a volume preserving vector field $X$. The third order helicity, [@Khesin98], is an invariant of $X$ under the action of volumorphisms isotopic to the identity (denoted here by $\text{Diff}^\text{vol}_0(M)$). Importance of such invariants stems from the basic fact that e.g. the evolution of the vorticity in the ideal hydrodynamics or the magnetic field $\mathbf{B}_0$ in the ideal magnetohydrodynamics (MHD), occurs along a path $t\longrightarrow g(t)\in \text{Diff}^\text{vol}_0(M)$, [@Khesin98 p. 176]. Namely, $\mathbf{B}(t)=g_\ast(t)\mathbf{B}_0$ which is a direct consequence of Euler's equations: $$\label{eq:Eulers-eq}
\frac{d}{dt} \mathbf{B}+[\mathbf{v},\mathbf{B}]=0,\qquad \frac{d}{dt} g(t)=\mathbf{v} .$$ One often says that the magnetic field $\mathbf{B}$ is *frozen in* the velocity field $\mathbf{v}$ of plasma, the action by $\text{Diff}^\text{vol}_0(M)$ is often referred to as *frozen-in-field* deformations. The fundamental example of such invariant defined for a general class in $\text{Vect}^\text{vol}(M)$ is the *helicity* $\mathsf{H}_{12}(X_1,X_2)$ defined for a pair of vector fields $X_1$ and $X_2$ on $M=S^3$ or a homology sphere. Helicity has been first introduced by Woltjer, in the context of magnetic fields, and is a measure of how orbits of $X_1$, and $X_2$ link with each other. This topological interpretation of helicity has been made precise by Arnold, who introduced (in [@Arnold86]) the concept of the average asymptotic linking number of orbits for a pair volume preserving vector fields on $M$ and proved that it is equal to their helicity. The subject has been further developed in [@Berger90; @Akhmetiev05; @Hornig04; @Laurence-Stredulinsky00b] (see [@Khesin98] for additional references), where authors approach *higher helicities* via the Massey products under various assumptions about the vector fields or their domains (work in [@Gambaudo-Ghys97; @Verjovsky94] concerns other approaches to the problem). In this paper we present an alternative to these approaches, which is a natural extension the notion of the linking number as a degree of a map, and exploits relations to the homotopy theory of certain maps associated to the link. The paper has two parts:

In the first part we show how the Milnor $\bar{\mu}_{123}$-invariant: $\bar{\mu}_{123}(L)$ of a parametrized borromean link $L$ in $S^3$ can be obtained as a Hopf degree of an associated map to the configuration space of three points in $S^3$. The presented approach to link-homotopy invariants of 3-component links has been proposed in [@Kohno02] for $n$-component links in $\mbox{\bbb R}^3$, and conveniently simplified for 3-component links in $S^3$ in the joint work [@Deturck-Gluck-Melvin-Shonkwiler08], where the full correspondence between $\bar{\mu}_{123}(L)$ and the Pontryagin-Hopf degree is proved. In Section [1](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"} we present the original proof of this correspondence in the borromean case, which is sufficient for our purposes.

The second part of the paper is concerned with a new definition of the third order helicity denoted here by $\mathsf{H}_{123}(X;\mathcal{T})$, where $X$ is a volume preserving vector field having an invariant unlinked domain $\mathcal{T}\subset S^3$. The simplest of such domains are three invariant handlebodies in $S^3$ which have pairwise unlinked cycles in the first homology. This includes the case of borromean flux tubes already investigated in e.g. [@Berger90; @Laurence-Stredulinsky00b]. In Section [4](#sec:ergodic){reference-type="ref" reference="sec:ergodic"} we develop an ergodic formulation of $\mathsf{H}_{123}(X;\mathcal{T})$ as an average asymptotic $\bar{\mu}_{123}$-invariant in the spirit of Arnold's asymptotic linking number, which allows us to extend the definition of the invariant to topologically more complicated unlinked domains. We also indicate that $\mathsf{H}_{123}(X;\mathcal{T})$ provides a lower bound for the $L^2$-energy of $X$.

*Acknowledgements:* My inspiration for the presented approach to the link-homotopy invariants comes from the Toshitake Kohno paper, [@Kohno02], whom I am grateful for the valuable e-mail correspondence. I have enjoyed conversations with many colleagues at the University of Pennsylvania, who have influenced this work. I wish to thank Herman Gluck for weekly meetings and his interest in this project, Frederic Cohen, Dennis DeTurck, Charlie Epstein, Paul Melvin, Tristan Rivi$\grave{\rm e}$re, Clay Shonkwiler, Jim Stasheff, David Shea Vick for the valuable input. I am also grateful to my advisor Robert Ghrist who introduced me to the subject long time ago.

The author acknowledges financial support from DARPA, #FA9550-08-1-0386.

# The Milnor $\bar{\mu}_{123}$-invariant and the Hopf degree. {#sec:mu-and-hopf}

The $\bar{\mu}$-invariants of $n$-component links in $S^3$ have been introduced by Milnor in [@Milnor54; @Milnor57] as invariants of links up to *link-homotopy*, recall that the link homotopy is a deformation of a link in $S^3$ which allows each component of the link to pass through itself but not through a different component. Clearly, this is a weaker equivalence than the equivalence of links up to *isotopy* where components are not allowed to pass through themselves at all. The fundamental example of a $\bar{\mu}$-invariant is the linking number (denoted by $\bar{\mu}_{12}$) which is a complete invariant of the 2-component links up to link homotopy. In the realm of 3-component links the relevant invariants are the pairwise linking numbers $\bar{\mu}_{12}$, $\bar{\mu}_{23}$, $\bar{\mu}_{32}$, and the third invariant $\bar{\mu}_{123}$ in $\mathbb{Z}_{\text{gcd}(\bar{\mu}_{12}, \bar{\mu}_{23}, \bar{\mu}_{32})}$, which is a well defined integer if and only if $\bar{\mu}_{12}=\bar{\mu}_{23}=\bar{\mu}_{32}=0$. In the second part of the paper we will interpret this statement as a topological condition on the invariant set of a vector field. A precise definition of $\bar{\mu}$-invariants is algebraic and involves the Magnus expansion of the lower central series of the fundamental group: $\pi_1(S^3-L)$ of the link complement. We refer the interested reader to the works in [@Milnor54; @Milnor57]. In the remaining part of this section we will prove that $\bar{\mu}_{123}(L)$ is a Hopf degree for an appropriate map associated to the link $L$, provided that the link is *borromean*, i.e. the pairwise linking numbers are zero (note that the borromean links are more general then so called Brunnian links, [@Milnor54]).

Let us review basic facts about the Hopf degree $\mathscr{H}(f)$ of a map $f:S^3\longrightarrow S^2$, (see e.g. [@Bott82]). The well known property of the Hopf degree is that $\mathscr{H}: f\longrightarrow \mathscr{H}(f)$ provides an isomorphism between $\pi_3(S^2)$ and $\mbox{\bbb Z}$. Recall that, up to a constant multiple, we may express $\mathscr{H}(f)$ as ($M=S^3$) $$\begin{gathered}
\label{eq:hopf-integral}
\mathscr{H}(f)= \int_{M} \alpha\wedge f^\ast\nu=\int_{M} \alpha\wedge \omega=\int_{M} \alpha\wedge d\alpha,
\end{gathered}$$ where $\nu$ is the area 2-form on $S^2$, and $\alpha$ satisfies $\omega=f^\ast\nu=d\alpha$. Notice that $f^\ast\nu$ is always exact since the cohomology of $S^3$ in dimension $2$ vanishes (i.e. $H^2(S^3)=0$). We may also interpret $\mathscr{H}(f)$ as an intersection number, [@Bott82; @Milnor97]. Namely, consider two regular values $p_1$ and $p_2\in S^2$ of the map $f$, then $l_1=f^{-1}(p_1)$ and $l_2=f^{-1}(p_2)$ form a link in $S^3$, and the integral formula [\[eq:hopf-integral\]](#eq:hopf-integral){reference-type="eqref" reference="eq:hopf-integral"} can be interpreted, as the intersection number of $l_1$ with the Seifert surface spanning $l_2$: $$\begin{gathered}
\label{eq:hopf-intersection}
\mathscr{H}(f)=\text{lk}(l_1,l_2)\ .
\end{gathered}$$ If we replace $S^3$ with an arbitrary closed compact orientable 3-dimensional manifold $M$, we may still obtain an invariant of $f:M\longrightarrow S^2$ this way, provided that the condition $f^\ast\omega=d\alpha$ holds.

::: proposition
[]{#th:hopf-degree-general label="th:hopf-degree-general"} Let $M$ be a closed Riemannian manifold, and $\nu\in \Omega^2(S^2)$ the area form on $S^2$. The formula [\[eq:hopf-integral\]](#eq:hopf-integral){reference-type="eqref" reference="eq:hopf-integral"} provides a homotopy invariant for a map $f:M\longrightarrow S^2$, if the 2-form $f^\ast\nu$ is exact. Up to a constant multiple this invariant can be calculated as an intersection number defined in [\[eq:hopf-intersection\]](#eq:hopf-intersection){reference-type="eqref" reference="eq:hopf-intersection"}, where $l_1=f^{-1}(p_1)$ and $l_2=f^{-1}(p_2)$ form a link in $M$, where both $l_1$ and $l_2$ are null-homologous.
:::

::: proof
*Proof.* Given a homotopy $F:I\times M\mapsto
S^2$, $f_1=F(1,\,\cdot\,)$, $f_0=F(0,\,\cdot\,)$, we define $\hat{\omega}=F^\ast\nu$. We have $$\begin{aligned}
\hat{\omega} & = & F^\ast\nu=d\,\hat{\alpha},\\
\omega_1 & = & f_1^\ast\nu=i^\ast_1\,F^\ast\nu=d\,\alpha_1,\\
\omega_0 & = & f_0^\ast\nu=i^\ast_0\,F^\ast\nu=d\,\alpha_0,
\end{aligned}$$ where $i_0:M\hookrightarrow M\times I$, $i_0(x)=(x,0)$, $i_1:M\hookrightarrow M\times I$, $i_1(x)=(x,1)$ are appropriate inclusions. The "potentials": $\hat{\alpha}\bigl|_{\{0\}\times M}$, $\alpha_0$, and $\hat{\alpha}\bigl|_{\{1\}\times M}$, $\alpha_1$ differ by a closed form $$\hat{\alpha}\bigl|_{\{0\}\times M}-\alpha_0=\beta_0,\quad \hat{\alpha}\bigl|_{\{1\}\times M}-\alpha_1=\beta_1,\quad d\beta_0=d\beta_1=0,$$ therefore the Stokes Theorem immediately implies that Formula [\[eq:hopf-integral\]](#eq:hopf-integral){reference-type="eqref" reference="eq:hopf-integral"} is independent of the choice of the potential. For the proof of invariance we repeat the standard argument in [@Bott82 p. 228] $$\begin{aligned}
 0 & = & \int_{F(M\times I)} \nu\wedge\nu
 =\int_{M\times I} \hat{\omega}\wedge \hat{\omega} =  \int_{M\times I} \hat{\omega}\wedge d\,\hat{\alpha}\\
 & = &\int_{M\times I} d(\hat{\omega}\wedge \hat{\alpha}) = \int_{\partial(M\times I)} \hat{\omega}\wedge \hat{\alpha}\ .
\end{aligned}$$ Thus, $$\begin{aligned}
0 & = & \int_{\partial(M\times I)} \hat{\omega}\wedge
\hat{\alpha}  =  \int_{M} \omega_1\wedge \alpha_1- \int_{M}
\omega_0\wedge \alpha_0\\
& = & \int_{M} d\alpha_1 \wedge \alpha_1-\int_{M}
d\alpha_0\wedge \alpha_0 =  \mathscr{H}(f_1)-\mathscr{H}(f_0).
\end{aligned}$$ The interpretation of $\mathscr{H}(f)$ as the intersection number [\[eq:hopf-intersection\]](#eq:hopf-intersection){reference-type="eqref" reference="eq:hopf-intersection"} is the same as in [@Bott82 p. 230]. ◻
:::

Given a 3-component parametrized link $L=\{L_1,L_2,L_3\}$ in $S^3$ we wish to associate a certain map $F_L:S^1\times S^1\times S^1\mapsto S^2$ to it, and interpret its Hopf degree as the Milnor $\bar{\mu}_{123}$-invariant. Recall, the definition of the configuration space of $k$ points in $M$: $$\begin{gathered}
 \text{Conf}(M,k):=\{(x_1,x_2,\ldots, x_k)\in (M)^k\,|\,x_i\neq x_j,\text{for}\ i\neq j\}.
\end{gathered}$$ As an introduction to the method we review the Gauss formula for the linking number of a 2-component link $L=\{L_1, L_2\}$ in $\mbox{\bbb R}^3$. Denote parameterizations of components by $L_1=\{\mathsf{x}(s)\}$, $L_2=\{\mathsf{y}(t)\}$ and consider the map $$\begin{gathered}
 F_L:S^1\times S^1\stackrel{L}{\longrightarrow} \text{Conf}(\mbox{\bbb R}^3,2) \stackrel{r}{\longrightarrow} S^2,\qquad L(s,t)=(\mathsf{x}(s), \mathsf{y}(t))\ .
\end{gathered}$$ where $r(x,y)=\frac{x-y}{\|x-y\|}$ is a retraction of $\text{Conf}(\mbox{\bbb R}^3,2)$ onto $S^2$. It yields the classical Gauss linking number formula, up to a constant multiple: $$\begin{gathered}
 \text{lk}(L_1,L_2)=\text{deg}(F_L),\qquad\quad \text{deg}(F_L)=\int_{S^1\times S^1} F^\ast_L(\nu),
\end{gathered}$$ where $\nu\in \Omega^2(S^2)$ is the area form on $S^2$. Consequently, the linking number $\text{lk}(L_1,L_2)$, also known as the Milnor $\bar{\mu}_{12}$-invariant, can be obtained as the homotopy invariant of the map $F_L$ associated to $L$. Notice that homotopy classes $[S^1\times S^1,S^2]$ are isomorphic to $\mbox{\bbb Z}$ and $\text{deg}:F\rightarrow \text{deg}(F)$ provides the isomorphism. In [@Kohno02], Kohno proposed a natural extension of this approach to $n$-component parametrized links $L$ in $\mbox{\bbb R}^3$ by considering maps $F_L:S^1\times\ldots\times S^1\longrightarrow \text{Conf}(\mbox{\bbb R}^3,n)$ and their homotopy classes. More specifically, he proposed specific cohomology classes of the based loop space of $\text{Conf}(\mbox{\bbb R}^3,n)$ as candidates for appropriate link-homotopy invariants of $L$. In [@Deturck-Gluck-Melvin-Shonkwiler08], it has been observed that, in the $3$-component case it is beneficial to consider $\text{Conf}(S^3,3)$, and $L\subset S^3$, since the topology of $\text{Conf}(S^3,3)$ simplifies dramatically (in comparison to $\text{Conf}(\mbox{\bbb R}^3,3)$). We review this simplification in the following paragraph as it is essential for the proof of the next theorem.

Consider a 3-component link $L=\{L_1, L_2, L_3\}$ in $S^3$ parametrized by $\{\mathsf{x}(s),\mathsf{y}(t),\mathsf{z}(u)\}$ and the following map $$\begin{gathered}
\label{eq:F}
 F_L:S^1\times S^1\times S^1\stackrel{L}{\longrightarrow} \text{Conf}(S^3,3)\stackrel{H}{\longrightarrow} S^2,\qquad L(s,t,u)=(\mathsf{x}(s), \mathsf{y}(t), \mathsf{z}(u))\ .
\end{gathered}$$ In order to explain the map $H:\text{Conf}(S^3,3)\longrightarrow S^2$, one must notice that $\text{Conf}(S^3,3)\subset S^3\times S^3\times S^3$ is diffeomorphic to $S^3\times \text{Conf}(\mbox{\bbb R}^3,2)=S^3\times
\mbox{\bbb R}^3\times (\mbox{\bbb R}^3\setminus\{0\})$, and consequently deformation retracts onto $S^3\times S^2$. Denote by $H:S^3\times \mbox{\bbb R}^3\times (\mbox{\bbb R}^3\setminus\{0\})\mapsto S^2$ the projection on $S^2$ factor. Considering $S^3$ as unit quaternions, the map $H$ can be expressed explicitly by the formula, [@Deturck-Gluck-Melvin-Shonkwiler08]: $$\begin{gathered}
\label{eq:hermans-map}
 \text{Conf}(S^3,3) \ni (x,y,z) \stackrel{H}{\longrightarrow}
 \frac{\text{pr}(x^{-1}\cdot y)-\text{pr}(x^{-1}\cdot z)}{\|\text{pr}(x^{-1}\cdot y)-\text{pr}(x^{-1}\cdot z)\|}\in S^2,
\end{gathered}$$ where $\cdot$ stands for the quaternionic multiplication, $\ ^{-1}$ is the quaternionic inverse, and $\text{pr}:S^3\longrightarrow \mbox{\bbb R}^3$ the stereographic projection from $1$. As a result one has the following particular expression for $F_L$: $$\begin{gathered}
\label{eq:F_L}
\notag F_L(s,t,u)=\frac{\text{pr}(\mathsf{x}(s)^{-1}\cdot \mathsf{z}(u))-\text{pr}(\mathsf{x}(s)^{-1}\cdot \mathsf{y}(t))}{\|\text{pr}(\mathsf{x}(s)^{-1}\cdot \mathsf{z}(u))-\text{pr}(\mathsf{x}(s)^{-1}\cdot
 \mathsf{y}(t))\|}.
\end{gathered}$$

At this point we note that one has a freedom in choosing the deformation retraction $H$ in [\[eq:hermans-map\]](#eq:hermans-map){reference-type="eqref" reference="eq:hermans-map"} but this particular formula makes the proof of the main theorem of this section possible. By the *borromean rings* we understand any $3$-component link with $\bar{\mu}_{123}=\pm 1$ link homotopic to a link with diagram presented on Figure [4](#fig:n-borromean){reference-type="ref" reference="fig:n-borromean"} (where the sign can be determined from the orientation of components).

::: theorem
[]{#th:milnor-hopf label="th:milnor-hopf"} Let $L^\text{Bor}=\{L_1,L_2,L_3\}$ be a 3-component link in $S^3$ link homotopic to the Borromean rings, and consider the associated map $F_{L^\text{Bor}}:S^1\times S^1\times S^1\longrightarrow S^2$ defined in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}. Then the Hopf degree of the map $F_{L^\text{Bor}}$ satisfies $$\begin{gathered}
\label{eq:hopf=2}
   \mathscr{H}(F_{L^\text{Bor}})=\pm 2,
 
\end{gathered}$$ where the sign depends on the choice of orientations.
:::

::: proof
*Proof.* According to Proposition [\[th:hopf-degree-general\]](#th:hopf-degree-general){reference-type="ref" reference="th:hopf-degree-general"}, $\mathscr{H}(F_L)$ is well defined for a link $L\subset S^3$ provided $F_L^\ast\nu\in \Omega^2(\mathbb{T})$ is trivial in $H^2(\mathbb{T})$, $\mathbb{T}=S^1\times S^1\times S^1$. This fact will follow from the proof, but we will show in Corollary [\[th:pairwise-linking\]](#th:pairwise-linking){reference-type="ref" reference="th:pairwise-linking"}, that it holds if and only if the pairwise linking numbers of $L$ are zero. The method relies on a direct calculation of $\mathscr{H}(F_{L^\text{Bor}})$, for a carefully chosen parametrization of $L^\text{Bor}$ in $S^3$. This calculation is achieved by visualization of the link $l_{S,N}=l_S\cup l_N$ in $\mathbb{T}$, and application of Formula [\[eq:hopf-intersection\]](#eq:hopf-intersection){reference-type="eqref" reference="eq:hopf-intersection"}, where $$l_S:=F^{-1}_{L^\text{Bor}}(S),\qquad l_N:=F^{-1}_{L^\text{Bor}}(N)$$ are preimages of the North pole $N=(0,0,1)$ and South pole $S=(0,0,-1)$ in $S^2$. Notice that $[F_L^\ast\nu]=0$ in $H^2(\mathbb{T})$ if and only if $[l_S]=0$ and $[l_N]=0$ in $H_1(\mathbb{T})$.

We identify $S^3$ with the set of unit quaternions in $\mbox{\bbb R}^4$ with standard coordinates: $$(w,x,y,z)=w+x\,\mathbf{i}+y\,\mathbf{j}+z\,\mathbf{k},$$ and choose a specific parametrization of the Borromean rings $L^\text{Bor}$ in $S^3$, as follows: define the $L_1$ component of $L^\text{Bor}$ to be the great circle through $1$ in $S^3$, parametrized as $$\mathsf{x}(s)=\cos(s)+\sin(s)\,\mathbf{k},\quad
\bigl(\,\mathsf{x}(s)^{-1}=\cos(s)-\sin(s)\,\mathbf{k}\,\bigr).$$ Notice that $\text{pr}(\mathsf{x}(s))$ parameterizes the $z$-axis in $\mbox{\bbb R}^3$. Because $$\begin{aligned}
\mathsf{x}(s)^{-1}\cdot(w,x,y,z) & = & \bigl(\cos(s) w+\sin(s) z, \cos(s) x +\sin(s) y,\\
& & \ \cos(s) y-\sin(s) x, \cos(s) z-\sin(s) w\bigr),
\end{aligned}$$ we observe that multiplication by $x(s)^{-1}$ is a rotation by angle $s$ in $(w,z)$-plane and $(x,y)$-plane of $\mbox{\bbb R}^4$ , and the flow defined by this $S^1$-action is tangent to the great circles of $S^3$. Consequently, the projected flow on $\mbox{\bbb R}^3$ via the stereographic projection $\text{pr}:S^3\subset \mbox{\bbb R}^4\longrightarrow \mbox{\bbb R}^3$ presents the standard picture of the Hopf fibration, and the $S^1$-action "pushes" points in $\mbox{\bbb R}^3$ along Hopf circles.

<figure id="fig:conf1">
<div class="center">
<div class="picture">
<p>(414,160) (15,0)<span><img src="borromean3" alt="image" /></span> (80,120)<span><span class="math inline"><em>L</em><sub>1</sub></span></span> (35,70)<span><span class="math inline"><em>L</em><sub>2</sub></span></span></p>
<p>(60,5)<span><span class="math inline"><em>L</em><sub>3</sub></span></span> (315,80)<span><span class="math inline"><em>A</em><sub>2</sub></span></span> (240,60)<span><span class="math inline"><em>A</em><sub>1</sub></span></span></p>
</div>
</div>
<figcaption>The model of <span class="math inline"><em>L</em><sub>Borr</sub></span> parametrized by <span class="math inline">{<em>L</em><sub>1</sub> = pr(x(<em>s</em>)), <em>L</em><sub>2</sub> = pr(y(<em>t</em>)), <em>L</em><sub>3</sub> = pr(z(<em>u</em>))}</span>. Arc <span class="math inline"><em>A</em><sub>1</sub></span> is a part of the unit circle on <span class="math inline"><em>x</em><em>y</em></span>-plane, <span class="math inline"><em>A</em><sub>2</sub></span> is a part of circle of radius <span class="math inline">1 + <em>ϵ</em></span>.</figcaption>
</figure>

Let us call a Hopf torus in $\mbox{\bbb R}^3$ the $r$-torus if and only if it contains a circle of radius $r$ in the $(x,y)$-plane and is invariant under the $S^1$-action. Figure [1](#fig:conf1){reference-type="ref" reference="fig:conf1"} shows how to define the second and the third component $\{L_2, L_3\}$ of the Borromean rings $L_\text{Borr}$ in the stereographic projection. $L_2$ will be the annuli with a rounded wedge removed, i.e. an arc $A_1$ of the circle of radius $1$ and $A_2$ arc belongs to the circle of radius $r_\epsilon=(1+\epsilon)$ in the $(x,y)$-plane.

The component $L_3$ is chosen to be a vertical ellipse linking with $L_2$, which belongs to the $r_{\epsilon/2}$-torus, and projects on the $(x,y)$-plane as a segment. Recall that every point on an $r$-torus traces a $(1,1)$-curve under the $S^1$-action. This motion, for sufficiently small $\epsilon$, can be regarded as a composition of the rotation by angle $s$ in both the direction of the meridian and the longitude of an $r$-torus. Therefore for different values of $s$ the $S^1$-action "rotates" the components $L_2$ and $L_3$, by sliding along the Hopf tori by angle $s$ in the meridian and the longitudinal direction, we denote links obtained this way by $$L^s_2(t)=\text{pr}(\mathsf{x}^{-1}(s)\cdot\mathsf{y}(t)),\qquad \text{and}\qquad  L^s_3(u)=\text{pr}(\mathsf{x}^{-1}(s)\cdot\mathsf{z}(u)).$$ Let us collect useful information below

-   The $z$-axis stays invariant under the $S^1$-action.

-   $A_2$ slides, under the $S^1$-action, on the $r_\epsilon$-torus, $A_1$ simply rotates around the $z$-axis in the $(x,y)$-plane.

-   We can disregard the longitudinal rotation (i.e. pretend that the observer sits on the unit circle) the motion of arcs: $L^s_3$, $A^s_2$ together with the connecting segments is simply a full rotation around the unit circle on the $(x,y)$-plane (which can be thought of as the "axis of rotation"). Stages of this motion are pictured on the lower part of Figure [2](#fig:4-pos){reference-type="ref" reference="fig:4-pos"}.

We seek to visualize the projection of $l_{S,N}=l_S\cup l_N$ on the $su$-face and $st$-face of the domain $\mathbb{T}=S^1\times
S^1\times S^1$ of $F_{L^\text{Bor}}$ parameterized by $(s,t,u)\in \mathbb{T}$, (it is convenient to think about $\mathbb{T}$ as a cube in $(s,t,u)$-coordinates, see Figure [3](#fig:framed-link){reference-type="ref" reference="fig:framed-link"}).

For example when $s=0$, ($\mathsf{x}(0)=1$), a point $(0,t_0,u_0)$ belongs to $l_N$, if and only if the vector $\mathsf{v}_0=\text{pr}(\mathsf{y}(t_0))-\text{pr}(\mathsf{z}(u_0))$ "points North", i.e. in the direction of $N=(0,0,1)$, analogous condition holds for $S=(0,0,-1)$, and $l_S$. Thus in order to determine a diagram of $l_{S,N}$, we must keep track of the "head" and "tail" of the vector $\mathsf{v}_s=L^s_2(t)-L^s_3(u)$, for various values of $s$ and record values of $t$ and $u$ for which $\mathsf{v}_s$ points "North" and "South" (Figure [2](#fig:4-pos){reference-type="ref" reference="fig:4-pos"}). We have the following condition $$\label{eq:arrow-eq}
  (s,t,u)\in l_{S,N}\qquad\text{if and only if},\qquad \mathsf{v}_s \parallel S\ \text{or}\ N.$$ An alternative way to view this condition is the following: for a given value of $s$ the coordinates $u$ and $t$ of points in $l_{S,N}$ can be identified with points on $L^s_2$ and $L^s_3$, which come from the intersection points in $\pi(L^s_3\cup L^s_2)$, under the projection $\pi(x,y,z)=(x,y)$, onto the $(x,y)$-plane (see the bottom part of Figure [2](#fig:4-pos){reference-type="ref" reference="fig:4-pos"}). These intersection points are simply crossings in the diagram of the link $\{L^s_2,L^s_3\}$ on the $(x,y)$-plane. Points $N$ and $S$ can be assumed to be regular values of $F_{L_\text{Borr}}$ because $\pi(L^s_2(t))$ and $\pi(L^s_3(u))$ always intersect transversely (bottom of Figure [2](#fig:4-pos){reference-type="ref" reference="fig:4-pos"}), which is persistent under small perturbations of the parametrization of $L_\text{Borr}$.

The main task ahead is to visualize $l_N$ and $l_S$. For a fixed $s=s_0$ we draw arrows: $N$ and $S$ (Figure [2](#fig:4-pos){reference-type="ref" reference="fig:4-pos"}) which lie directly above the crossings of the diagram of $\{L^{s_0}_2,L^{s_0}_3\}$ on the $(x,y)$-plane. Next, we trace each component $L^{s_0}_2$ and $L^{s_0}_3$ and record values of $t$ and $u$ parameter for which the condition [\[eq:arrow-eq\]](#eq:arrow-eq){reference-type="eqref" reference="eq:arrow-eq"} holds, without loss of generality we assume that $L^{s}_2$ is parametrized by the unit $t$-interval, and $L^{s}_3$ is parametrized by the unit $u$-interval.

<figure id="fig:4-pos">
<div class="center">
<div class="picture">
<p>(498, 590) (30,20)<span><img src="4-pos" alt="image" /></span> (30,260)<span><span class="math inline">$s=\frac{3\pi}{2}$</span></span> (30,360)<span><span class="math inline"><em>s</em> = <em>π</em></span></span> (30,460)<span><span class="math inline">$s=\frac{\pi}{2}$</span></span> (30,550)<span><span class="math inline"><em>s</em> = 0</span></span></p>
</div>
</div>
<figcaption>Four positions corresponding to angles: <span class="math inline">$s=0,\frac{\pi}{2}, \pi, \frac{3\pi}{2}$</span>, small arrows next to <span class="math inline"><em>N</em></span> and <span class="math inline"><em>S</em></span> indicate a motion as <span class="math inline"><em>s</em>↗</span>. Several phases of the rotation by <span class="math inline"><em>s</em></span> are pictured on the bottom four drawings.</figcaption>
</figure>

This process is elucidated below for $s=0, \frac{\pi}{2}, \pi,
\frac{3\pi}{2}$, which is sufficient to draw projections of $l_S$ and $l_N$ (each position is pictured on Figure [1](#fig:conf1){reference-type="ref" reference="fig:conf1"}) on $st$ and $tu$-faces of $\mathbb{T}$. We describe each case separately,

-   This is the initial position, where $L^0_3$ is vertical. We mark the initial point $L^0_3(0)$ on the top of $L^0_3$ and orient $L^0_3$ counter-clockwise, the initial point $L^0_2(0)$ on $L^0_2$ is chosen in the middle of the left segment connecting $A_1$ and $A_2$, and the middle point $L^0_2(\frac{1}{2})$ is located the middle of the left segment connecting $A_1$ and $A_2$. Points in $l_S$ are marked by $\times$ and points in $l_N$, are marked by $\bullet$. In this configuration there are four vertical arrows, two pointing North and two South, this gives us four points along the $t$-interval ordered as $NSSN$, ($|-\bullet-\times-\times-\bullet-|$) and four points along the $u$-interval ordered ($|-(\times\bullet)--(\bullet\times)-|$), where $(\times\bullet)$ indicates the "collision" i.e. common value of $u$ for both $l_S$ and $l_N$.

The remaining cases are self-explanatory, see Figure [1](#fig:conf1){reference-type="ref" reference="fig:conf1"},

-   $L^s_3$ is horizontal, and $t$-coordinates of $l_{S,N}$ are colliding ($|-(\bullet\times)-(\times\bullet)-|$). $L^s_2$ is vertical and $u$-coordinates of $l_{S,N}$ are ordered as $(NNSS)$, ($|-\bullet-\times-\times-\bullet-|$).

-   $L^s_3$ is vertical again, and $t$-coordinates of $l_{S,N}$ are ordered : $SNNS$, ($|-\times-\bullet-\bullet-\times-|$). $L^s_2$ is horizontal and $u$-coordinates of $l_{S,N}$ are colliding, ($|-(\bullet\times)--(\times\bullet)-|$).

-   $L^s_3$ is horizontal, and $t$-coordinates of $l_{S,N}$ are colliding ($|-(\times\bullet)-(\bullet\times)-|$). $L^s_2$ is vertical and $u$-coordinates of $l_{S,N}$ are ordered as $(NNSS)$, ($|-\times-\times-\bullet-\bullet-|$).

<figure id="fig:framed-link">
<div class="center">
<div class="picture">
<p>(480, 580) (140,420)<span><img src="cube2-dashed" style="width:3in" alt="image" /></span> (40,20)<span><img src="proj-red-green-dashed" style="width:5in" alt="image" /></span> (30,180)<span><span class="math inline"><em>s</em></span></span> (30,390)<span><span class="math inline"><em>s</em></span></span> (227,180)<span><span class="math inline"><em>s</em></span></span> (227,390)<span><span class="math inline"><em>s</em></span></span> (30,270)<span><span class="math inline">$\frac{\pi}{2}$</span></span> (227,270)<span><span class="math inline">$\frac{\pi}{2}$</span></span> (200,10)<span><span class="math inline"><em>u</em></span></span> (313,8)<span>(D)</span> (115,8)<span>(C)</span> (400,10)<span><span class="math inline"><em>t</em></span></span> (200,220)<span><span class="math inline"><em>u</em></span></span> (115,215)<span>(A)</span> (400,220)<span><span class="math inline"><em>t</em></span></span> (313,215)<span>(B)</span></p>
</div>
</div>
<figcaption>Projection of <span class="math inline"><em>l</em><sub><em>S</em>, <em>N</em></sub></span> on the <span class="math inline"><em>s</em><em>u</em></span>-face and <span class="math inline"><em>s</em><em>t</em></span>-face of <span class="math inline">𝕋</span>. The strands <span class="math inline"><em>l</em><sub><em>S</em></sub></span> and <span class="math inline"><em>l</em><sub><em>N</em></sub></span> are oppositely oriented since <span class="math inline"><em>l</em><sub><em>S</em>, <em>N</em></sub></span> is null homologous in <span class="math inline">𝕋</span>.</figcaption>
</figure>

Collecting this information, we may draw the projection of the link $l_{S,N}$ on the $su$-face of $\mathbb{T}$, which is represented by square (A) in Figure [3](#fig:framed-link){reference-type="ref" reference="fig:framed-link"}. Analogously, the projection of $l_{S,N}$ on the $st$-face of $\mathbb{T}$, is represented by square (B). The dashed line indicates the $l_N$ component of $l_{S,N}$ and the solid line indicates $l_S$. In order to obtain the diagram of $l_{S,N}$ we will resolve the double points on Diagram (A) into crossings, ((B) can be resolved analogously). For example let us resolve the "circled" double point on (A), which occurs for $s=\frac{\pi}{2}$, of the *left* two stands of $l_{S,N}$. It suffices to determine the value of the $t$-coordinate at this point. Diagram (B) tells us that $l_S$ is below $l_N$ because $\mathbb{T}$ is oriented so that the $t$-axis points above the $su$-face (see top of Figure [3](#fig:framed-link){reference-type="ref" reference="fig:framed-link"}). Resolving the remaining crossings in a similar fashion leads to a diagrams of $l_{S,N}$ presented in squares (C) and (D). Diagram (C) is easier to use for the calculation of $\mathscr{H}(F_{L_{\text{Bor}}})=\text{lk}(l_S, l_N)$ as an intersection number of e.g. $l_S$ with a Seifert surface spanning $l_N$. Observe that strands in $l_S$ and $l_N$ are oppositely oriented, which follows from the fact that they are null-homologous in $H^1(\mathbb{T})$, there are an obvious annuli bounding $l_S$ and $l_N$ on Diagram (C). Clearly, the linking number of $l_S$ and $l_N$ is equal to $\pm 2$, since the intersection number of e.g. $l_S$ with the obvious annulus on Diagram (C) is $\pm 2$. This proves [\[eq:hopf=2\]](#eq:hopf=2){reference-type="eqref" reference="eq:hopf=2"}. ◻
:::

<figure id="fig:n-borromean">
<div class="picture">
<p>(380, 150) (0,0)<span><img src="borr" style="width:5.2in" alt="image" /></span> (280,7)<span><span class="math inline">$\mathbf{\Bigl\}}$</span></span> (285,22)<span><span class="math inline"><em>n</em></span></span></p>
</div>
<figcaption>left: <span class="math inline"><em>μ̄</em><sub>123</sub> =  ± 1</span> and right: <span class="math inline"><em>μ̄</em><sub>123</sub> =  ± <em>n</em></span>.</figcaption>
</figure>

::: corollary
[]{#th:general-mu_123 label="th:general-mu_123"} If $L=\{L_1,L_2,L_3\}$ is a 3-component link with vanishing pairwise linking numbers then $$\begin{gathered}
  \mathscr{H}(F_L)=\pm 2\,\bar{\mu}_{123}
 
\end{gathered}$$
:::

::: proof
*Proof.* Clearly, if $L$ and $L'$ are link-homotopic then $F_{L}$ and $F_{L'}$ are homotopic maps. By the Milnor classification of 3-component links up to link homotopy (see [@Milnor54]), every 3-component link $L$ with zero pairwise linking numbers and $\bar{\mu}_{123}=\pm n$ is represented by the right diagram on Figure [4](#fig:n-borromean){reference-type="ref" reference="fig:n-borromean"}. Consequently, up to homotopy, the associated map $F_L$ can be obtained from $F_{L_\text{Borr}}$ by covering one of the $S^1$ factors in $\mathbb{T}$, $n$-times. ◻
:::

::: lemma
We have the following isomorphisms $$\begin{gathered}
\pi_2 (\text{Conf}(\mbox{\bbb R}^3,3))\cong \mbox{\bbb Z}\oplus \mbox{\bbb Z}\oplus \mbox{\bbb Z},\qquad \pi_2
(\text{Conf}(S^3,3))\cong \mbox{\bbb Z},
\end{gathered}$$ and the induced homomorphism $i^\ast:\pi_2 (\text{Conf}(\mbox{\bbb R}^3,3))\mapsto
\pi_2(\text{Conf}(S^3,3))$, from $i:\mbox{\bbb R}^3\mapsto \mbox{\bbb R}^3\cup \{\infty\}\cong S^2$, maps the generators $A_{ij}$, $1\leq i\leq
j\leq 3$, to $\pm\,\alpha$, where $\alpha$ is the single generator of $\pi_2(\text{Conf}(S^3,3))$.
:::

::: proof
*Proof.* The Hurewicz Theorem tells us that $H_2(\text{Conf}(\mbox{\bbb R}^3,3))\cong
\pi_2(\text{Conf}(\mbox{\bbb R}^3,3))$. The 2-skeleton of $\text{Conf}(\mbox{\bbb R}^3,3)$ has a homotopy type of $S^2\vee S^2\vee S^2$ and $H_2(\text{Conf}(\mbox{\bbb R}^3,3))$ is generated by $A_{ij}: S^2\mapsto \text{Conf}(\mbox{\bbb R}^3,3)$, $1\leq i<j\leq 3$ representing each 2-sphere in the 2-skeleton (c.f. [@Cohen02]). The group of permutations $\mathbb{S}_3$ acts on $\text{Conf}(\mbox{\bbb R}^3,3)$ by permuting coordinates. As a consequence of this we obtain the action on generators of $H_2(\text{Conf}(\mbox{\bbb R}^3,3))$ by permutation. We have seen that $\text{Conf}(S^3,3)$ has the homotopy type of $S^3\times S^2$ thus $\pi_2(\text{Conf}(S^3,3))=\mbox{\bbb Z}$, and let us denote the generator by $\alpha$. Now, $i^\ast{A_{ij}}=k\,\alpha$, $k\in \mbox{\bbb Z}$, notice that $i^\ast{A_{23}}=\alpha$ since $i\circ A_{23}=\text{id}_{S^2}$, using the action by permutations we obtain $i^\ast{A_{ij}}=\alpha$. ◻
:::

::: corollary
[]{#th:pairwise-linking label="th:pairwise-linking"} Denote by $F^{kl}_L=F_L\bigl|_{S^1_k\times S^1_l}$ restriction of $F_L$ defined in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"} to the $kl$-torus $k,l\in\{s,t,u\}$, $k\neq l$. Then $$\begin{gathered}
 \text{deg}(F^{kl}_L)=\text{lk}(L_k,L_l),
\end{gathered}$$ where $\text{lk}(L_k,L_l)$ is the linking number between the components parameterized by $k$, and $l$.
:::

::: proof
*Proof.* By definition $$\text{deg}(S_i^1\times S_j^1\stackrel{L_{ij}}{\longrightarrow} \text{Conf}(\mbox{\bbb R}^3,3)\stackrel{\pi_{ij}}{\longrightarrow} \text{Conf}(\mbox{\bbb R}^3,2)\cong S^2)=\text{lk}(L_i,L_j),$$ thus on the cohomology level $\text{lk}(L_i,L_j)=L^\ast_{ij}[A_{ij}]=(F^{ij}_L)^\ast(\alpha)$. ◻
:::

Results of Theorem [\[th:milnor-hopf\]](#th:milnor-hopf){reference-type="ref" reference="th:milnor-hopf"} and Proposition [\[th:hopf-degree-general\]](#th:hopf-degree-general){reference-type="ref" reference="th:hopf-degree-general"} combined with Formula [\[eq:hopf-integral\]](#eq:hopf-integral){reference-type="eqref" reference="eq:hopf-integral"} allow us to express $\bar{\mu}_{123}(L)$ of a borromean link $L$ as $$\begin{aligned}
\label{eq:mu-formula}
  \bar{\mu}_{123}(L) & = & \int_{\mathbb{T}} F^\ast_L\nu\wedge \alpha=\int_{\mathbb{T}} L^\ast\omega\wedge \alpha,\\
  \notag & \text{for} &  \quad F^\ast_L\nu=d\alpha,\quad \omega=H^\ast\nu\in \Omega^2(\text{Conf}(S^3,3)),
 
\end{aligned}$$ where $\nu$ is the area form on $S^2$, and $H:\text{Conf}(S^3,3)\longrightarrow S^2$ is the deformation retraction (as e.g. in [\[eq:hermans-map\]](#eq:hermans-map){reference-type="eqref" reference="eq:hermans-map"}). Alternatively, we may view $\omega$ as a 2-form on $(S^3)^3$ which is singular along the diagonals $\mathbf{\Delta}\subset (S^3)^3$, and the singularity is of order $O(r^2)$, where $r$ is a distance to $\mathbf{\Delta}$. Consequently, $\omega$ is integrable but not square integrable on $(S^3)^3$. We also point out that the 2-form $\omega$ can be replaced with any other cohomologus 2-form in $\text{Conf}(S^3,3)$.

::: remark
[]{#rem:anti-symmetry label="rem:anti-symmetry"} Notice that the integral formula [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} is antisymmetric in the following sense $$\begin{aligned}
   \bar{\mu}_{123}(L_1,L_2,L_3) & = & \int_{S^1_s}\int_{S^1_t}\int_{S^1_u} \omega\wedge\alpha(\dot{\mathsf{x}}(s),\dot{\mathsf{y}}(t),\dot{\mathsf{z}}(u))\,ds\wedge
   dt\wedge du\\
   & = & \int_{S^1_s}\int_{S^1_t}\int_{S^1_u} -\omega\wedge(-\alpha)(\dot{\mathsf{y}}(t),\dot{\mathsf{x}}(s),\dot{\mathsf{z}}(u))\,ds\wedge dt\wedge du\\
   & = & \int_{S^1_t}\int_{S^1_s}\int_{S^1_u} \omega\wedge\alpha(\dot{\mathsf{y}}(t),\dot{\mathsf{x}}(s),\dot{\mathsf{z}}(u))(-\,dt\wedge ds \wedge du)=-\bar{\mu}_{123}(L_2,L_1,L_3)
  
\end{aligned}$$ where in the second identity the potential changes sign because the domain changes orientation.
:::

# Invariants of volume preserving flows. Helicity. {#sec:invariants-flows}

Given finitely many volume preserving vector fields $X_1$, $X_2$, $\ldots X_k\in \text{Vect}^\text{vol}(M)$ on $M=S^3$ or a homology 3-sphere one seeks quantities $\mathsf{I}(X_1,X_2,\ldots,X_k)$ invariant under the action of volumorphisms isotopic to the identity $g\in \text{Diff}^\text{vol}_0(M)$, commonly known as *higher-helicities*: $$\begin{gathered}
\label{eq:invariants}
 \mathsf{I}(X_1,X_2,\ldots,X_k)=\mathsf{I}(g_\ast X_1,g_\ast X_2,\ldots,g_\ast X_k),\qquad\quad \text{for all }g\in \text{Diff}^\text{vol}_0(M), 
\end{gathered}$$ where $g_\ast$ is a push-forward by a diffeomorphism $g$. To distinguish the case of a single vector field $X$ (i.e. $X=X_1=\ldots=X_k$) we often refer to $\mathsf{I}(X)=\mathsf{I}(X_1,X_2,\ldots,X_k)$ as *self-helicity*. We elucidated in the introduction a fundamental example of such invariant is the ordinary helicity $\mathsf{H}(X_1,X_2)$ of a pair of vector fields. In the the remaining part of this section we review well known formulations of the helicity, which will later help us to point out analogies to the proposed formulation of the 3rd order helicity. Let $\mathcal{T}=\mathcal{T}_1\cup \mathcal{T}_2$ represent two invariant subdomains (not necessarily disjoint) under flows of $X_1$ and $X_2$ in $S^3$ and let $$\mathcal{T}=\mathcal{T}_1\times\mathcal{T}_2\subset \text{Conf}(M,2)\subset M\times M.$$ Recall that the formula for $\mathsf{H}(X_1,X_2)$, from [@Khesin05; @Vogel03], specialized to invariant subdomains $\mathcal{T}=\mathcal{T}_1\cup \mathcal{T}_2$ may be expressed as $$\label{eq:helicity}
 \mathsf{H}_{12}(X_1,X_2)=\int_{\mathcal{T}_1\times\mathcal{T}_2} \omega\wedge\iota_{X_1}\mu\wedge\iota_{X_2}\mu,$$ where $\omega$ is so called linking form on $M\times M$. When $\mathcal{T}=M\times M$ this formula is equivalent to a more commonly known expression: $\mathsf{H}(X_1,X_2)=\int_M \iota_{X_1}\mu\wedge d^{-1}(\iota_{X_2}\mu)$ (because $\omega$ also represents the integral kernel of $d^{-1}$).

Philosophically, $\mathsf{H}(X_1,X_2)$ can be derived (c.f. [@Arnold86]) from the linking number of a pair of closed curves, which is expressed by Arnold's Helicity Theorem. For orbits $\{\mathscr{O}^1(x),\mathscr{O}^2(y)\}$ of $X_1$ and $X_2$ through $x, y\in M$, we introduce the following notation for the long pieces of closed up orbits

$$\begin{aligned}
\label{eq:orbits}
 \mathscr{O}^i_T(x) & = & \{\Phi^i_t(x)\ |\ 0\leq t\leq T\}\subset \mathscr{O}^i(x),\qquad i=X, Y,\\
 \bar{\mathscr{O}}^i_T(x) & := & \mathscr{O}^i_T(x)\cup \sigma(x,\Phi^i(x,T)).
\end{aligned}$$ where $\sigma(x,y)$ denotes a short path, [@Vogel03], connecting $x$ and $y$ in $M$ (see Section [4](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}).

::: theorem
Given $X_1, X_2\in\text{Vect}^\text{vol}(M)$, The following limit exists almost everywhere on $M\times M$: $$\begin{gathered}
\label{eq:linking-function}
  \bar{m}_{X_1 X_2}(x,y)=\lim_{T\to \infty} \frac{1}{T^2}\, \text{lk}(\bar{\mathscr{O}}^1_T(x)\times\bar{\mathscr{O}}^2_T(y))\ .
 
\end{gathered}$$ Moreover, $\bar{m}_{X_1 X_2}$ is in $L^1(M\times M)$, and $$\label{eq:helicity-asymp}
 \mathsf{H}_{12}(X_1,X_2)=\int_{M\times M} \bar{m}_{X_1 X_2}(x,y)\, \mu(x)\wedge\mu(y)\ .$$
:::

The function $\bar{m}_{X_1 X_2}$ represents an asymptotic linking number of orbits $\{\mathscr{O}^1(x),\mathscr{O}^2(y)\}$, and the identity [\[eq:helicity-asymp\]](#eq:helicity-asymp){reference-type="eqref" reference="eq:helicity-asymp"} tells us that the helicity $\mathsf{H}_{12}(X_1,X_2)$ is equal to the average asymptotic linking number. We will demonstrate, in coming paragraphs, how this philosophy is applied to obtain the asymptotic $\bar{\mu}_{123}$-invariant for 3-component links and the third order helicity.

# Definition of "$\bar{\mu}_{123}$-helicity" on invariant unlinked handlebodies. {#sec:handlebody}

In this section we apply the formulation of the $\bar{\mu}_{123}$-invariant for the 3-component links in $S^3$, obtained in Section [1](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"}, to define the third order helicity of a volume preserving vector field $X$ on certain invariant domains $\mathcal{T}$ in $S^3$. As a "warm-up" to a more general case presented in Section [4](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}, in the following paragraphs we consider the case of three disjoint unlinked handlebodies: $\mathcal{T}=\mathcal{T}_1\cup    \mathcal{T}_2\cup \mathcal{T}_3$ each of genus $g(\mathcal{T}_i)$ in $S^3$. When $\mathcal{T}$ represents three unlinked tubes (so called *flux tubes*, [@Khesin98]) in $\mbox{\bbb R}^3$, the third order helicity has been developed by several authors [@Berger90; @Mayer03; @Laurence-Stredulinsky00b] via the Massey product formula for the $\bar{\mu}_{123}$-invariant, we compare our approach to these known works in Section [\[sec:massey\]](#sec:massey){reference-type="ref" reference="sec:massey"}.

We consider $\mathcal{T}_i$ to have smooth boundary and the vector field $X$ to be tangent to $\partial \mathcal{T}_i$, set $$X_i:=X\bigl|_{\mathcal{T}_i},\qquad i=1,2,3,$$ denote the flow of $X$ on $S^3$ by $\Phi$, and flows of restrictions $X_i$ by $\Phi^i$. Clearly, $\mathcal{T}$ is an invariant set of $X$. Given for any domain $\mathcal{T}$ with three connected components $\{\mathcal{T}_i\}$ we may always associate a product domain in $\text{Conf}(S^3,3)$ as follows $$\label{eq:admissible-domain}
 \mathcal{T}:=\mathcal{T}_1\times \mathcal{T}_2\times \mathcal{T}_3\subset \text{Conf}(S^3,3)\subset S^3\times S^3\times S^3\ .$$ Notice that $\mathcal{T}$ is a domain with corners in $\text{Conf}(S^3,3)$, and we use the same notation for the product of $\mathcal{T}_i$ as for the union in $S^3$. Wherever needed we also assume that $(S^3)^3$ is equipped with a product Riemannian metric. A domain $\mathcal{T}$ defined in [\[eq:admissible-domain\]](#eq:admissible-domain){reference-type="eqref" reference="eq:admissible-domain"}, where $\mathcal{T}_i\cap \mathcal{T}_j=\O$, $i\neq j$ and each $\mathcal{T}_i$ is a handlebody in $S^3$ is called *unlinked handlebody* if and only if the 2-form $\omega\in\Omega^2(\text{Conf}(S^3,3))$ defined in Equation [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} is exact on $\mathcal{T}$, i.e. $\omega$ has a local *potential* $\alpha_\omega\in \Omega^1(\mathcal{T})$: $$\label{eq:omega-exact}
 \omega=d\alpha_\omega\ .$$ Denote a volume preserving vector field and an unlinked handlebody $\mathcal{T}$ as $(X;\mathcal{T})$.

::: remark
Notice that since $\omega$ is a dual cohomology class to the $S^2$ factor of $\text{Conf}(S^3,3)\cong S^3\times S^2$, thus $\omega$ does not admit a global potential.
:::

Because each handlebody $\mathcal{T}_i$ has a homotopy type of a bouquet of circles $H_1(\mathcal{T}_i)$ is generated by cycles $\{L^k_i\}_{k=1,\ldots,g(\partial\mathcal{T}_i)}$ corresponding to the circles, which we call *basic cycles*. We have the following practical characterization of unlinked handlebodies:

::: lemma
$\mathcal{T}$ is an unlinked handlebody if and only if $$\label{eq:admissible-condition}
  \text{lk}(L^k_i,L^r_j)  = 0,\qquad \forall\, i,j,\qquad i\neq j$$
:::

::: proof
*Proof.* The standard pairing, [@Bott82], $H^2(\mathcal{T})\times H_2(\mathcal{T})\longrightarrow \mbox{\bbb R}$ implies that a closed $k$-form is exact if and only if it evaluates to zero on all $k$-cycles of the domain. By the K$\ddot{\rm u}$nneth formula $H_2(\mathcal{T})=H_2(\mathcal{T}_1\times \mathcal{T}_2\times \mathcal{T}_3)$ is generated by $L^k_i\otimes L^r_j$. Corollary [\[th:pairwise-linking\]](#th:pairwise-linking){reference-type="ref" reference="th:pairwise-linking"} implies (for $i\neq j$) that $$\text{lk}(L^k_i,L^r_j) = \int_{L^k_i\times L^r_j} \omega\ .$$ Therefore the condition [\[eq:admissible-condition\]](#eq:admissible-condition){reference-type="eqref" reference="eq:admissible-condition"} is necessary and sufficient for $\omega$ to be exact on $\mathcal{T}$. ◻
:::

![The simplest unlinked handlebody: flux tubes $\mathcal{T}^\text{Borr}$ modeled on the borromean rings.](borromean-tube2){#fig:invariant-sets width="\\textwidth"}

Let $X$ be a volume preserving vector field on $S^3$ which admits an unlinked domain $\mathcal{T}$ which is invariant under its flow. We define the $\bar{\mu}_{123}$-helicity of $(X;\mathcal{T})$ denoted by $\mathsf{H}_{123}(X;\mathcal{T})$ or $\mathsf{H}_{123}(X_1,X_2,X_3)$ as follows: $$\label{eq:mu_123-helicity}
\boxed{\mathsf{H}_{123}(X;\mathcal{T})=\mathsf{H}_{123}(X_1,X_2,X_3)\stackrel{\text{def.}}{=}\int_{\mathcal{T}} \bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\wedge \iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3, }$$ where $\mu_i$ denotes the pull-back of the volume form $\mu$ on $S^3$ under the projection $$\label{eq:projection-i}
\pi_i:S^3\times S^3\times S^3\longrightarrow S^3,\qquad \pi_i(x_1,x_2,x_3)=x_i,$$ and $\iota_{X_i}$ is a contraction by a vector field $X_i$, our notational convention is to denote by $\iota_{X_i}\mu_i$ both the forms on the base of $\pi_i$ and the pullbacks: $\pi^\ast_i\bigl(\iota_{X_i}\mu_i\bigr)$. Notice that $\mu=\mu_1\wedge\mu_2\wedge\mu_3$ is a natural volume form on the product: $S^3\times S^3\times S^3$.

There are obvious analogies between the formula above, the formula for the helicity $\mathsf{H}_{12}(X;\mathcal{T})$ and the integral formula for the $\bar{\mu}_{123}$-invariant [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"}. Clearly, the 3-form $$\gamma_\omega:=\alpha_\omega\wedge d\alpha_\omega=\alpha_\omega\wedge \omega,$$ plays a role of the linking form as $\omega$ in the formula [\[eq:helicity\]](#eq:helicity){reference-type="eqref" reference="eq:helicity"} for $\mathsf{H}_{12}(X;\mathcal{T})$. The main motivation behind this definition is the ergodic interpretation of $\mathsf{H}_{123}(X;\mathcal{T})$ as an average asymptotic $\bar{\mu}_{123}$-invariant of orbits of $X$, and will become apparent in Section [4](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}. Formula [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} can be also regarded as the third order helicity of three distinct vector fields $X_i$, supported on the handlebodies $\mathcal{T}_i$. In Section [\[sec:energy\]](#sec:energy){reference-type="ref" reference="sec:energy"} we indicate how to construct the potential $\alpha_\omega$ from the basic elliptic theory of differential forms.

::: theorem
[]{#th:invariance-th label="th:invariance-th"} On every unlinked invariant handlebody $\mathcal{T}$ in $S^3$, $\mathsf{H}_{123}(X;\mathcal{T})$ is

-   independent of a choice of the potential $\alpha_\omega$.

-   invariant under the action of $\text{Diff}^\text{vol}_0(S^3)$, i.e. for every $g\in \text{Diff}^\text{vol}_0(S^3)$: $$\begin{gathered}
    \label{eq:invariance}
     \mathsf{H}_{123}(X;\mathcal{T})=\mathsf{H}_{123}(g_\ast X;g(\mathcal{T}))\ .
    \end{gathered}$$
:::

::: proof
*Proof.* To prove $(i)$ observe for every other potential $\alpha'_\omega$ of $\omega$, the difference $\beta=\alpha_\omega-\alpha'_\omega$ is a closed $1$-form on $\mathcal{T}$ (since $\omega=d\alpha_\omega=d\alpha'_\omega$). Therefore $$\begin{aligned}
 \mathsf{H}_{123}(X;\mathcal{T})-\mathsf{H}_{123}'(X;\mathcal{T}) & = & \int_{\mathcal{T}} (\beta\wedge\omega)\wedge\iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3\\
 & \stackrel{(1)}{=} & \int_{\mathcal{T}} d\bigl(\beta\wedge \alpha_\omega\wedge\iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3\bigr)\\
 & = & \int_{\partial\mathcal{T}} \beta\wedge \alpha_\omega\wedge\iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3 \stackrel{(2)}{=} 0,
\end{aligned}$$ where in (1) we applied $d(\iota_{X_i}\mu_i)=0$ (since $X_i$'s are divergence free), and in (2): $$\iota_{X_i}\mu_i\bigl|_{\partial\mathcal{T}_i}=0,$$ (because each vector field $X_i$ is tangent to the boundary $\partial \mathcal{T}_i$), and $$\partial \mathcal{T}=\bigl(\partial \mathcal{T}_1\times \mathcal{T}_2\times \mathcal{T}_3\bigr)\cup \bigl(\mathcal{T}_1\times \partial\mathcal{T}_2\times \mathcal{T}_3\bigr)\cup \bigl(\mathcal{T}_1\times \mathcal{T}_2\times \partial\mathcal{T}_3\bigr).$$

Next we show $(ii)$, the proof is in the style of [@Berger90; @Mayer03], but adapted to our setting. For any given $g\in \text{Diff}^\text{vol}(S^3)$, there exists a path $t\longrightarrow g(t)\in \text{Diff}^\text{vol}_0(S^3)$, such that $$g(0)=\text{id}_{S^3},\qquad g(1)=g\ .$$ Denote by $V$ the divergence free vector field on $S^3$, given by $V(x)=\frac{d}{dt} g(t,x)|_{t=0}$, i.e. $g(t)$ is a flow of $V$, and push-forward fields $X_i$ by $$X^t_i:=g(t)_\ast X_i\ .$$ It is well known (see Appendix B, or [@Freedman91-2 p. 224]) that 2-forms: $\iota_{X^t_i}\mu$ are frozen in the flow of $V$, i.e. $$\label{eq:forms-frozen-in}
 \frac{d}{dt}\bigl(g(t)^\ast\iota_{X^t_i}\mu\bigr) =(\partial_t+\mathcal{L}_V) \iota_{X^t_i}\mu = 0.$$ We also have a path $\hat{g}(t)=(g(t),g(t),g(t))$ in $\text{Diff}^\text{vol}_0(S^3\times S^3\times S^3)$. Analogously for the volume preserving flow $\hat{g}(t)$ we obtain the vector field $\hat{V}=(V,V,V)$ (recall that a tangent bundle $T(S^3)^3$ has a natural product structure). Equation [\[eq:forms-frozen-in\]](#eq:forms-frozen-in){reference-type="eqref" reference="eq:forms-frozen-in"} implies $$\label{eq:forms-frozen-in2}
(\partial_t+\mathcal{L}_{\hat{V}}) \bigl(\pi^\ast_i\iota_{X^t_i}\mu\bigr)=(\partial_t+\mathcal{L}_{\hat{V}}) \iota_{X^t_i}\mu_i= 0\ .$$ (in the second equation we merely revoke our notational conventions: $\iota_{X^t_i}\mu_i\equiv\pi^\ast_i\bigl(\iota_{g(t)^\ast X_i}\mu\bigr)$).

Let $\mathcal{T}(t)=\hat{g}(t)(\mathcal{T}(0))\subset \text{Conf}(S^3,3)$ we must show $\frac{d}{dt} 
\mathsf{H}_{123}(X^t_1,X^t_2,X^t_3)=0$ at every $t=t_0$. Notice that for small enough $\epsilon$ and $t\in (t_0-\epsilon,t_0+\epsilon)$ we can assume, by $(i)$, that $\alpha_\omega$ is a time independent potential obtained from slightly bigger domain $\widetilde{\mathcal{T}}$ which satisfies $$\mathcal{T}(t)\subset\widetilde{\mathcal{T}},\qquad \forall t\in (t_0-\epsilon,t_0+\epsilon),$$ and is a deformation retraction of $\mathcal{T}(t_0)$. Without loss of generality we assume $t_0=0$, $\hat{g}(0)=\text{id}_{(S^3)^3}$, and calculate at $t_0$: $$\begin{aligned}
 \frac{d}{dt} 
 \Bigl(\mathsf{H}_{123}(g(t)^\ast X_1,g(t)^\ast X_2,g(t)^\ast X_3)\Bigr) & = &
 \frac{d}{dt} \int_{\mathcal{T}(t)} \alpha_\omega\wedge d\alpha_\omega\wedge \iota_{X^t_1}\mu_1\wedge \iota_{X^t_2}\mu_2\wedge \iota_{X^t_3}\mu_3\\
 & = & \int_{\mathcal{T}(0)} \frac{d}{dt} \hat{g}(t)^\ast\bigl(\alpha_\omega\wedge d\alpha_\omega\wedge \iota_{X^t_1}\mu_1\wedge \iota_{X^t_2}\mu_2\wedge \iota_{X^t_3}\mu_3\bigr)\\
 & = & \int_{\mathcal{T}(0)} \bigl(\mathcal{L}_{\partial_t+\hat{V}}(\alpha_\omega\wedge d\alpha_\omega)\bigr)\wedge \iota_{X^t_1}\mu_1\wedge \iota_{X^t_2}\mu_2\wedge \iota_{X^t_3}\mu_3,
\end{aligned}$$ where in the last identity we applied [\[eq:forms-frozen-in2\]](#eq:forms-frozen-in2){reference-type="eqref" reference="eq:forms-frozen-in2"} and the product rule for the Lie derivative. Now because $\omega\wedge\alpha_\omega$ is time independent (for $t\in (t_0-\epsilon,t_0+\epsilon)$) by the Cartan magic formula we obtain $$\begin{aligned}
 \mathcal{L}_{\partial_t+\hat{V}}(\alpha_\omega\wedge d\alpha_\omega) & = & \mathcal{L}_{\hat{V}}(\alpha_\omega\wedge d\alpha_\omega) = \iota_{\hat{V}} d(\alpha_\omega\wedge d\alpha_\omega)+ d(\iota_{\hat{V}} (\alpha_\omega\wedge d\alpha_\omega))\\
 & =  & d(\iota_{\hat{V}} (\alpha_\omega\wedge d\alpha_\omega)),
\end{aligned}$$ since $d(\alpha_\omega\wedge d\alpha_\omega)=\omega\wedge\omega=0$. Now, the same argument as in the proof of $(i)$ shows that the right hand side of the previous equation is zero, because $X^t_i$ are tangent to the boundary of $\mathcal{T}_i(t)$. ◻
:::

::: remark
Notice that the above argument shows that if we replace $\alpha_{\omega}\wedge d\alpha_\omega$ by virtually any closed 3-form $\eta$ on $\text{Conf}(S^3,3)$ (or $(S^3)^3$) we obtain some invariant under frozen-in-field deformations. Clearly, if $\eta$ is exact we obtain trivial invariants, therefore the only candidates are cohomology classes of $\text{Conf}(S^3,3)\cong S^3\times S^2$. In dimension $3$, the only candidate cohomology class of $\text{Conf}(S^3,3)$ is a dual of $S^3$. Based on the considerations in Section [1](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"} one may argue that an invariant obtained this way is trivial. Indeed the cohomology class $\eta$ evaluated on any 3-torus obtained from a 3-component link in $S^3$ via the map $L$ in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"} is zero. Therefore one could apply the approach via the Ergodic Theorem (as in Section [4](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}) to show that $\int \eta\wedge\iota_{X}\mu_1\wedge \iota_{X}\mu_2\wedge \iota_{X}\mu_3$ defines a trivial invariant. The crucial obstacle in extending the formula in [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} to encompass the whole $S^3$ is the fact that the potential $\alpha_\omega$ cannot be globally defined on $\text{Conf}(S^3,3)$.
:::

# The ergodic interpretation of $\mathsf{H}_{123}(X;\mathcal{T})$ {#sec:ergodic}

The following statement is often seen in literature [@Cantarella-DeTurck-Gluck01; @Cantarella-DeTurck-Gluck-Teytel00]:

> *Helicity measures the extend to which vector fields twist and coil around each other.*

A beauty of Arnold's ergodic approach to the helicity $\mathsf{H}_{12}(X)$ is that it makes this statement precise, by interpreting $\mathsf{H}_{12}(X)$ as an average asymptotic linking number of orbits of $X$. But it also has a practical application as it allows us to extend our approach to certain invariant sets of $X$. In this section we apply this philosophy to our newly defined invariant $\mathsf{H}_{123}(X;\mathcal{T})$, and interpret it as the average asymptotic $\bar{\mu}_{123}$-invariant of orbits of $X$. Moreover this ergodic interpretation leads us to an alternative, more intuitive proof of Helicity Invariance Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}.

We begin by observing that given a volume preserving vector field $X$ on $M$ and its flow $\Phi_t$, we may regard $X$ as three vector fields on $(M)^3$. Therefore $(\Phi,\Phi,\Phi)$ induces a natural $\mbox{\bbb R}^3$ action defined as $$\label{eq:R3-action}
 \mathbf{\Phi}:\mbox{\bbb R}^3\times (M)^3\longrightarrow (M)^3:\qquad \bigl((s,t,u),x,y,z\bigr)\stackrel{\mathbf{\Phi}}{\longrightarrow} (\Phi(s,x),\Phi(t,y), \Phi(u,z)).$$ Observe that $\mathbf{\Phi}$ is a volume preserving action on $(M)^3$. Our analysis is rooted in techniques developed in [@Arnold86; @Laurence-Avellaneda93; @Laurence-Stredulinsky00b], the main tool is the the following

::: theorem
[]{#th:multi-ergodic label="th:multi-ergodic"} For any real valued $L^1$-function $F$ on $(M)^3$, the time averages under the action in [\[eq:R3-action\]](#eq:R3-action){reference-type="eqref" reference="eq:R3-action"}: $$\begin{gathered}
\bar{F}(x,y,z)=\lim_{T\to \infty}\frac{1}{T^3}\int^T_0\int^T_0\int^T_0
 F(\Phi(x,s),\Phi(y,t),\Phi(z,u))\,d s\,d t\,d u
\end{gathered}$$ converge almost everywhere. Moreover, the limit function $\bar{F}$ satisfies

-   $\|\bar{F}\|_{L^1((M)^3)}\leq \|F\|_{L^1((M)^3)}$,

-   $\bar{F}$ is invariant under the $\mathbf{\Phi}$-action,

-   if $(M)^3$ is of finite volume then $$\begin{gathered}
    \label{eq:ergodic-integrals-equal}
     \int_{(M)^3}\bar{F} =\int_{(M)^3} F\ .
    \end{gathered}$$
:::

We may now define *invariant unlinked domain* $\mathcal{T}$ of $X$ as an arbitrary $\mathbf{\Phi}$-invariant set, with topological closure $\overline{\mathcal{T}}$ which belongs to a larger product of open sets $\widetilde{\mathcal{T}}=\widetilde{\mathcal{T}}_1\times \widetilde{\mathcal{T}}_2\times \widetilde{\mathcal{T}}_3$ in $\text{Conf}(S^3,3)$, satisfying the following

-   $\widetilde{\mathcal{T}}$ admits a *short path system* $\mathcal{S}$,

-   Equation [\[eq:omega-exact\]](#eq:omega-exact){reference-type="eqref" reference="eq:omega-exact"} holds on $\widetilde{\mathcal{T}}$.

By a system of short paths on $\widetilde{\mathcal{T}}$, [@Vogel03; @Khesin98], we understand a collection of curves $\mathcal{S}=\{\sigma(x,y)\}$ on each open set $\widetilde{\mathcal{T}}_i$ such that

-   for every pair of points $x,y \in \widetilde{\mathcal{T}}_i$ there is a curve $\sigma(x,y):I\mapsto \widetilde{\mathcal{T}}_i$ in $\mathcal{S}$, such that $\sigma(0)=x$ and $\sigma(1)=y$,

-   the lengths of paths in $\mathcal{S}$ are uniformly bounded above by a common constant.

Topologically, every $\mathbf{\Phi}$-invariant set is a union of products of orbits of $X$ in $(S^3)^3$, it is often convenient to think of the orbits $\mathbf{\Phi}$-action as a foliation of $(S^3)^3$, then $\mathbf{\Phi}$-invariant sets are just union of leaves of such foliation. A fundamental example of an invariant unlinked domain is the case of $\mathbf{\Phi}$-invariant set $\mathcal{T}$ contained in the product $\widetilde{\mathcal{T}}=\widetilde{\mathcal{T}}_1\times \widetilde{\mathcal{T}}_2\times \widetilde{\mathcal{T}}_3$ of disjoint open unlinked handlebodies $\widetilde{\mathcal{T}}_i$. Notice that we do not require $X$ to be tangent to $\partial\widetilde{\mathcal{T}}_i$ in this case, and $\widetilde{\mathcal{T}}$ always admits a short path system as we describe in the following

::: remark
In [@Vogel03], Vogel shows that on a closed manifold $M$, geodesics always provide a short path system. When $\mathcal{T}$ is contained in the product of unlinked handlebodies $\widetilde{\mathcal{T}}$ we may easily construct such system on $\widetilde{\mathcal{T}}$. Because $\mathcal{\mathcal{T}}_i$ are proper subsets of $S^3$ we generally do not want to use ambient geodesics from $S^3$ as they may not lie entirely in $\mathcal{T}_i$. To obtain $\mathcal{S}$ one may always put an artificial Riemannian metric on each $\widetilde{\mathcal{T}}_i$ which makes it a complete Riemannian manifold (e.g. by making $\partial\widetilde{\mathcal{T}}_i$ totally geodesic) and choose $\mathcal{S}$ to be geodesics on such Riemannian manifold. We also observe that one may apply a diffeomorphism $g\in \text{Diff}(\widetilde{\mathcal{T}})$ to $\mathcal{S}$ which results in the new system $g\mathcal{S}$ on $g(\widetilde{\mathcal{T}})$.
:::

Next theorem shows that the definition of $\mathsf{H}_{123}(X;\mathcal{T})$ in Equation [\[eq:helicity\]](#eq:helicity){reference-type="eqref" reference="eq:helicity"} is valid for invariant unlinked domains of $X$ and is an analog of Arnold's Helicity Theorem in our setting

::: theorem
[]{#th:ergodic-mu label="th:ergodic-mu"} Given $(X;\mathcal{T})$, the following limit (asymptotic $\bar{\mu}_{123}$-invariant of orbits) exists for almost all $(x,y,z)\in \mathcal{T}$: $$\label{eq:bar-m_X}
 \bar{m}_X(x,y,z)=\lim_{T\to\infty} \frac{1}{T^3}\bar{\mu}_{123}\bigl(\bar{\mathscr{O}}^{X_1}_T(x),\bar{\mathscr{O}}^{X_2}_T(y),\bar{\mathscr{O}}^{X_3}_T(y)\bigr).$$ Moreover, $$\label{eq:H_123-ergodic}
 \mathsf{H}_{123}(X;\mathcal{T})=\int_{\mathcal{T}} \bar{m}_X(x,y,z)\,\mu(x)\wedge\mu(y)\wedge\mu(z)\ .$$
:::

::: proof
*Proof.* The proof is similar to the one in e.g. [@Vogel03]. Before we start we must point out the following identity (valid for any 3-form $\gamma$ on $M\times M\times M$ and vector fields $X_1,X_2,X_3$ on $M$) $$(\iota_{X_1}\iota_{X_2}\iota_{X_3}\gamma)\wedge\mu\wedge\mu\wedge\mu=
\gamma(X_1,X_2,X_3)\,\mu\wedge\mu\wedge\mu=\gamma\wedge\iota_{X_1}\mu\wedge\iota_{X_2}\mu\wedge\iota_{X_3}\mu\ .$$ The first equation follows from the definition, the second equation is a consequence of the fact that $\iota_X$ is an antiderivation i.e. $$\label{eq:iota-antiderivation}
  \iota_X(\alpha\wedge\beta)=(\iota_X\alpha)\wedge\beta+(-1)^{|\alpha|}\alpha\wedge(\iota_X\beta),$$ and $\iota_{X_i}\mu_j\equiv 0$ for $i\neq j$. As a result $$\begin{aligned}
\notag  \mathsf{H}_{123}(X_1,X_2,X_3) & = & \int_{\mathcal{T}} \bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\wedge \iota_{X_1}\mu_1\wedge \iota_{X_2}\mu_2\wedge \iota_{X_3}\mu_3\\
& = & \int_\mathcal{T} \bigl(\iota_{X_1}\iota_{X_2}\iota_{X_3}\bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\bigr)\,\mu_1\wedge\mu_2\wedge\mu_3\\
\label{eq:m-function}  & = & \int_\mathcal{T} m_{X_1,X_2,X_3}(x,y,z)\,\mu_1\wedge \mu_2\wedge \mu_3,
\end{aligned}$$ where $m_{X_1,X_2,X_3}:=\alpha_\omega\wedge d\alpha_\omega(X_1,X_2,X_3)$. For convenience let (see [\[eq:orbits\]](#eq:orbits){reference-type="eqref" reference="eq:orbits"}) $$\bar{\mathscr{O}}(x,y,z;T):=\bar{\mathscr{O}}^{X_1}_T(x)\times \bar{\mathscr{O}}^{X_2}_T(y)\times\bar{\mathscr{O}}^{X_3}_T(y)\ .$$ Clearly, every link $\bar{\mathscr{O}}(x,y,z;T)$ is borromean and by Formula [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} we obtain $$\begin{aligned}
\bar{\mu}_{123}\bigl(\bar{\mathscr{O}}^{X_1}_T(x),\bar{\mathscr{O}}^{X_2}_T(y),\bar{\mathscr{O}}^{X_3}_T(y)\big)
& = & \int_{\bar{\mathscr{O}}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega\\
& = & \int_{\mathscr{O}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega+(I)
\end{aligned}$$ where the term $(I)$ involves integrals over short paths in $\mathcal{S}$, (see Appendix B). Next, notice that for every $(x,y,z)$ : $D\mathbf{\Phi}_{(x,y,z)}[\partial_i]=X_i$, $i=s,t,u$ we obtain $$\begin{aligned}
 \mathbf{\Phi}^\ast_{(x,y,z)}(\alpha_\omega\wedge d\alpha_\omega) & = & (\alpha_\omega\wedge d\alpha_\omega(X_1,X_2,X_3)(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\\
 & = & m_{X_1,X_2,X_3}(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\ .
\end{aligned}$$ Thus $$\int_{\mathscr{O}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega=\int^T_0\int^T_0\int^T_0 m_{X_1,X_2,X_3}(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\ .$$ Function $m_{X_1,X_2,X_3}$ is smooth on $\mathcal{T}$ and therefore $L^1$. Because short paths do not contribute to the time average i.e. $$\lim_{T\to\infty} \frac{1}{T^3}(I)=0$$ (see Appendix B), Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"} applied to the function $m_{X_1,X_2,X_3}$ yields almost everywhere existence of the limit [\[eq:bar-m_X\]](#eq:bar-m_X){reference-type="eqref" reference="eq:bar-m_X"} and the invariant $L^1$-function $\bar{m}_X:=\bar{m}_{X_1,X_2,X_3}$ on $\mathcal{T}$. The identity [\[eq:H_123-ergodic\]](#eq:H_123-ergodic){reference-type="eqref" reference="eq:H_123-ergodic"} follows from $(iii)$ of Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"}. ◻
:::

::: theorem
[]{#th:invariance-th-ergodic label="th:invariance-th-ergodic"} On every unlinked domain $\mathcal{T}$ in $S^3$, (i) and (ii) of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"} hold for $\mathsf{H}_{123}(X;\mathcal{T})$.
:::

::: proof
*Proof.* The proof of $(i)$ immediately follows from independence of the limit [\[eq:bar-m_X\]](#eq:bar-m_X){reference-type="eqref" reference="eq:bar-m_X"} on the choice of the potential $\alpha_\omega$. For the proof of $(ii)$ we must show the following $$\int_\mathcal{T} m_{X_1,X_2,X_3}\,\mu_1\wedge \mu_2\wedge \mu_3=\int_{g(\mathcal{T})} m_{g_\ast X_1,g_\ast X_2, g_\ast X_3}\,\mu_1\wedge \mu_2\wedge \mu_3\ .$$ Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"}, tells us that $m_{X_1,X_2,X_3}$ and $m_{g_\ast X_1,g_\ast X_2, g_\ast X_3}$ admit $L^1$-averages $\bar{m}_{X_1,X_2,X_3}$ and $\bar{m}_{g_\ast X_1,g_\ast X_2, g_\ast X_3}$, under actions of $X_i$ and $g_\ast X_i$ respectively. If the following holds: $$\label{eq:m=gm}
 \bar{m}_{X_1,X_2,X_3}(x,y,z)=\bar{m}_{g_\ast X_1,g_\ast X_2, g_\ast X_3}(g(x),g(y),g(z)),\qquad \text{a.e.},$$ then [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"} is an immediate consequence of [\[eq:ergodic-integrals-equal\]](#eq:ergodic-integrals-equal){reference-type="eqref" reference="eq:ergodic-integrals-equal"}, change of variables for integrals, and the fact that $g$ preserves the volume, i.e. $\mu_i=g^\ast\mu_i$. Borrowing notation from the previous theorem we set $$\begin{aligned}
 g\bar{\mathscr{O}}(x,y,z;T) & := & g(\bar{\mathscr{O}}^{X_1}_T(x))\times g(\bar{\mathscr{O}}^{X_2}_T(y))\times g(\bar{\mathscr{O}}^{X_3}_T(z))\\
 & = & \bar{\mathscr{O}}^{g_\ast X_1}_T(g(x))\times \bar{\mathscr{O}}^{g_\ast X_2}_T(g(y))\times \bar{\mathscr{O}}^{g_\ast X_3}_T(g(z)),
\end{aligned}$$ where the second identity is a consequence of the fact that the flow of $g_\ast X_i$ is obtained as a composition of $g$ and the flow of $X_i$. Since $g$ is isotopic to the identity, $\bar{\mathscr{O}}(x,y,z;T)$ and $\bar{\mathscr{O}}(x,y,z;T)$ are isotopic borromean links in $S^3$, and for every $T$: $$\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))=\bar{\mu}_{123}(g\bar{\mathscr{O}}(x,y,z;T)).$$ As a result of the above identity and [\[eq:bar-m_X\]](#eq:bar-m_X){reference-type="eqref" reference="eq:bar-m_X"} we derive a.e. $$\begin{aligned}
  \bar{m}_{X_1,X_2,X_3}(x,y,z) & = & \lim_{T\to\infty}\frac{1}{T^3}\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))\\
   & = & \lim_{T\to\infty}\frac{1}{T^3}\bar{\mu}_{123}(g\bar{\mathscr{O}}(x,y,z;T))=\bar{m}_{g_\ast X_1,g_\ast X_2, g_\ast X_3}(g(x),g(y),g(z)).
\end{aligned}$$ Notice that in the last equation we used in the "pushed forward" short paths system: $g\mathcal{S}$. But since lengths of paths in $g\mathcal{S}$ are bounded as well, they do not contribute to the limit. This proves the identity [\[eq:m=gm\]](#eq:m=gm){reference-type="eqref" reference="eq:m=gm"}, and consequently [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"}. ◻
:::

Notice that the above argument does not require the Stokes Theorem, and thus may lead to further generalizations. Clearly, for $\mathsf{H}_{123}(X;\mathcal{T})$ to be nontrivial $\mathcal{T}$ must be of nonzero measure.

The following formula is a well known property of the ordinary helicity $\mathsf{H}_{12}(X;\mathcal{T})$ of the flux tubes $\mathcal{T}$ modeled on a 2-component link $L=\{L_1,L_2\}$ (see e.g. [@Laurence-Avellaneda93; @Cantarella00])

$$\label{eq:helicity12-flux-tubes}
\mathsf{H}_{12}(X;\mathcal{T})=\mathsf{H}_{12}(X_1,X_2)=\text{lk}(L_1,L_2)\,\text{Flux}(X_1)\,\text{Flux}(X_2).$$ Next we show that an analogous property holds $\mathsf{H}_{123}(X;\mathcal{T})$, for invariant unlinked handlebodies $\mathcal{T}$ investigated in the previous section.

::: proposition
$\mathsf{H}_{123}(X_1,X_2,X_3)$ on invariant unlinked handlebodies $\mathcal{T}$ satisfies the following formula $$\label{eq:helicity-fluxes}
 \mathsf{H}_{123}(X_1,X_2,X_3)=\sum_{i\neq j\neq k} \bar{\mu}_{123}(L^i_1, L^j_2, L^k_3)\,\text{Flux}_{\Sigma_i}(X_1)\,\text{Flux}_{\Sigma_j}(X_2)\,\text{Flux}_{\Sigma_k}(X_3)\ .$$ where $\{L^i_1\otimes L^j_2\otimes L^k_3\}$ is a basis of basic cycles of $H_1(\mathcal{T}_1)\otimes H_1(\mathcal{T}_2)\otimes H_1(\mathcal{T}_3)$, $\text{Flux}(X_i)$ stands for the flux of $X_i$ through a cross sectional surface $\Sigma_k$ of $\mathcal{T}_i$, which represents a homology Poincar$\acute{\rm e}$ dual of $L^k_i$ in $H_2(\mathcal{T}_i,\partial\mathcal{T}_i)$.
:::

::: proof
*Proof.* Recall that a flux $\text{Flux}_{\Sigma_k}(X_i)$ of a vector field $X_i$ though a cross-sectional surface $\Sigma_k$ is given by: $$\begin{aligned}
  \text{Flux}_{\Sigma_k}(X_i) & = & \int_{\Sigma_k} \iota_{X_i}\mu=\int_{\mathcal{T}_i} h_k\wedge\iota_{X_i}\mu\\
  & = & \int_{\mathcal{T}_i} \iota_{X_i}h_k\wedge\mu =\int_{\mathcal{T}_i} h_k(X_i),
 
\end{aligned}$$ where 1-forms $h_k$ represent cohomology Poincar$\acute{\rm e}$ duals of $\Sigma_k$ and we applied [\[eq:iota-antiderivation\]](#eq:iota-antiderivation){reference-type="eqref" reference="eq:iota-antiderivation"} in the third equation. Clearly, $h_i\in \Omega^1(\mathcal{T}_i)$ satisfy $$\int_{\gamma} h_k=\#(\gamma,\Sigma_k)=\text{deg}(\gamma, L_k),$$ where $\text{deg}(\gamma, L^j_k)$ measures how many times $\gamma$ "wraps around" in the cycle $L^j_k$.

For simplicity we first assume that $\mathcal{T}$ is modeled on a borromean link $L=\{L_1,L_2,L_3\}$ (see Figure [5](#fig:invariant-sets){reference-type="ref" reference="fig:invariant-sets"}). Then $h=h_1\wedge h_2\wedge h_3\in \Omega^3(\mathcal{T})$ is a cohomology class dual of the cycle $L=L_1\times L_2\times L_3$ in $\mathcal{T}$. We set $$H:=\iota_{X_1}\iota_{X_2}\iota_{X_3} h=h(X_1,X_2,X_3),$$ which is a smooth function, and let $\bar{H}$ be the time average of $H$ as in Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"}. It suffices to show $$\label{eq:H-equation}
   \bar{m}_{X_1,X_2,X_3}=\bar{\mu}_{123}(L)\,\bar{H},\qquad \text{a.e.}$$ Analogously as in Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}, Equation [\[eq:H-equation\]](#eq:H-equation){reference-type="eqref" reference="eq:H-equation"} immediately implies Formula [\[eq:helicity-fluxes\]](#eq:helicity-fluxes){reference-type="eqref" reference="eq:helicity-fluxes"}. Assume the notation of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}, for given $T$ consider $\bar{\mathscr{O}}(x,y,z;T)$. By the fundamental property of the $\bar{\mu}_{123}$-invariant (see Corollary [\[th:general-mu_123\]](#th:general-mu_123){reference-type="ref" reference="th:general-mu_123"}) we have $$\begin{aligned}
  \bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T)) & = & \bar{\mu}_{123}(L)\,\bigl(\text{deg}(\bar{\mathscr{O}}^{X_1}_T(x),L_1)\,\text{deg}(\bar{\mathscr{O}}^{X_2}_T(y),L_2)\,\text{deg}(\bar{\mathscr{O}}^{X_3}_T(x),L_3)\bigr)\\
  & = & \bar{\mu}_{123}(L)\int_{\bar{\mathscr{O}}(x,y,z;T)} h\ .
 
\end{aligned}$$ Thus we obtain $$\begin{aligned}
  \bar{m}_{X_1,X_2, X_3}(x,y,z) & = & \lim_{T\to \infty} \frac{1}{T^3}\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))\\
  & = & \bar{\mu}_{123}(L)\lim_{T\to \infty} \frac{1}{T^3}\int_{\bar{\mathscr{O}}(x,y,z;T)} H\\
  & =  &\bar{\mu}_{123}(L) \bar{H}(x,y,z),
 
\end{aligned}$$ where the last equality is again the consequence of short paths not contributing to the limit.

Now, from the product structure and $(iii)$ of Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"} we have $$\int_\mathcal{T} \bar{H} =\int_\mathcal{T} H=\bigl(\int_{\mathcal{T}_1} h_1(X_1) \bigr)\bigl(\int_{\mathcal{T}_2} h_2(X_2) \bigr)\bigl(\int_{\mathcal{T}_3} h_3(X_3) \bigr).$$ The proof in the case of a general handlebody is analogous, once we show the following

::: lemma
Let $\mathcal{O}=\{\mathcal{O}_1,\mathcal{O}_2, \mathcal{O}_3\}$ be a 3-component link in $S^3$ such that $\mathcal{O}_i\subset \mathcal{T}_i$ for each $i$. Then $\mathcal{O}$ is borromean and $$\label{eq:mu-in-T}
 \bar{\mu}_{123}(\mathcal{O})=\sum_{i\neq j\neq k} \bar{\mu}_{123}(L^i_1, L^j_2, L^k_3)\,\text{deg}(\mathcal{O}_1, L^i_1)\,\text{deg}(\mathcal{O}_2, L^j_2)\,\text{deg}(\mathcal{O}_3, L^k_1)\ .$$
:::

::: proof
*Proof.* Notice that thanks to our new interpretation, the $\bar{\mu}_{123}$-invariant is not only a link homotopy invariant but a homotopy invariant of the associated map $F_{\mathcal{O}}$ defined in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}. Observe that each component $\mathcal{O}_i$ can be homotopied inside of its handlebody $\mathcal{T}_i$ to be come a bouquet of circles $\widehat{\mathcal{O}}_i\cong S^1\vee S^1\vee\ldots\vee S^1$. Such that each factor in $\widehat{\mathcal{O}}_i$ is a basic cycle in $H_1(\mathcal{T}_i)$. As a result we obtain the associated map $F_{\widehat{\mathcal{O}}}$, and $$\bar{\mu}_{123}(\mathcal{O})=\frac{1}{2}\mathscr{H}(F_{\widehat{\mathcal{O}}}).$$ Interpreting, $\mathscr{H}(F_{\widehat{\mathcal{O}}})$ as the intersection number and summing up intersection numbers we conclude [\[eq:mu-in-T\]](#eq:mu-in-T){reference-type="eqref" reference="eq:mu-in-T"}. ◻
:::

 ◻
:::

In the case of borromean flux tubes modeled on $L$, [\[eq:helicity12-flux-tubes\]](#eq:helicity12-flux-tubes){reference-type="eqref" reference="eq:helicity12-flux-tubes"} reduces to $$\label{eq:helicity12-borro-flux-tubes}
\mathsf{H}_{123}(X_1,X_2,X_3)=\bar{\mu}_{123}(L)\,\text{Flux}_{\Sigma_1}(X_1)
\text{Flux}_{\Sigma_2}(X_2)\text{Flux}_{\Sigma_3}(X_3),$$ where $\Sigma_i$ denotes homology Poincar$\acute{\rm e}$ duals to $L_i$ in $H_2(\mathcal{T}_i,\partial\mathcal{T}_i)$.

Since the fluxes are invariant under frozen-in-field deformations Formula [\[eq:helicity12-flux-tubes\]](#eq:helicity12-flux-tubes){reference-type="eqref" reference="eq:helicity12-flux-tubes"} is yet another proof of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"} in the setting of invariant unlinked handlebodies. In [@Laurence-Stredulinsky00b] the authors develop the same formula for the borromean flux tubes. This clearly must be the case as we deal with the same topological invariants of links via a different approach. Additional advantage of our formulation is that we do not have to separately deal with null points of vector fields as in [@Laurence-Stredulinsky00b]. We also note that in [@Laurence-Stredulinsky00b] the authors prove the helicity invariance only via Formula [\[eq:helicity12-borro-flux-tubes\]](#eq:helicity12-borro-flux-tubes){reference-type="eqref" reference="eq:helicity12-borro-flux-tubes"}.
