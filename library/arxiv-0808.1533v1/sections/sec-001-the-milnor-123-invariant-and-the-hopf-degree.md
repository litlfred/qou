---
doc_id: arxiv-0808.1533v1
doc_title: "On the third order helicity of magnetic ﬁelds on invariant domains in S 3"
section_id: sec-001-the-milnor-123-invariant-and-the-hopf-degree
section_title: "The Milnor 123-invariant and the Hopf degree."
section_number: null
pages: 2-12
source_pdf: 0808.1533v1.pdf
source_sha256: 85bb9732afdd70ea
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.99
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
duplicate_of: "arxiv-0808.1533v3"
---
[]{#sec:mu-and-hopf label="sec:mu-and-hopf"}

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
