---
doc_id: arxiv-0808.1533v3
doc_title: "On the third order helicity of magnetic fields on invariant domains in S³"
section_id: sec-001-the-milnor-mu-123-invariant-and-the-hopf-degree
section_title: "The Milnor mu-123-invariant and the Hopf degree."
section_number: null
pages: 3-10
source_pdf: 0808.1533v3.pdf
source_sha256: 3e003cc35a4e5711
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.985
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
---
[]{#sec:mu-and-hopf label="sec:mu-and-hopf"}

The $\bar{\mu}$-invariants of $n$-component links in $S^3$ have been introduced by Milnor in [@Milnor54; @Milnor57] as invariants of links up to *link homotopy*. Recall that the link homotopy is a deformation of a link in $S^3$ which allows each component to pass through itself but not through a different component. Clearly, this is a weaker equivalence than the equivalence of links up to *isotopy* where components are not allowed to pass through themselves at all. The fundamental example of a $\bar{\mu}$-invariant is the linking number (denoted by $\bar{\mu}_{12}$) which is a complete invariant of the 2-component links up to link homotopy. In the realm of 3-component links the relevant invariants are the pairwise linking numbers $\bar{\mu}_{12}$, $\bar{\mu}_{23}$, $\bar{\mu}_{32}$, and the third invariant $\bar{\mu}_{123}$ in $\mathbb{Z}_{\text{gcd}(\bar{\mu}_{12}, \bar{\mu}_{23}, \bar{\mu}_{32})}$, which is a well defined integer, if and only if, $\bar{\mu}_{12}=\bar{\mu}_{23}=\bar{\mu}_{32}=0$. In the second part of the paper we will interpret this statement as a topological condition on the invariant set of a vector field. A precise definition of $\bar{\mu}$-invariants is algebraic and involves the Magnus expansion of the lower central series of the fundamental group: $\pi_1(S^3-L)$ of the link complement. We refer the interested reader to the works in [@Milnor54; @Milnor57]. In the remaining part of this section we will prove that $\bar{\mu}_{123}(L)$ is a Hopf degree for an appropriate map associated to the link $L$, provided that the link is *Borromean*, i.e. the pairwise linking numbers are zero (note that the Borromean links are more general then Brunnian links, [@Milnor54]).

Let us review basic facts about the Hopf degree $\mathscr{H}(f)$ of a map $f:S^3\longrightarrow S^2$, (see e.g. [@Bott82]). A well known property of the Hopf degree is that $\mathscr{H}: f\longrightarrow \mathscr{H}(f)$ provides an isomorphism between $\pi_3(S^2)$ and $\mbox{\bbb Z}$. Recall that up to a constant multiple we may express $\mathscr{H}(f)$ as ($M=S^3$) $$\begin{gathered}
\label{eq:hopf-integral}
\mathscr{H}(f)= \int_{M} \alpha\wedge f^\ast\nu=\int_{M} \alpha\wedge \omega=\int_{M} \alpha\wedge d\alpha,
\end{gathered}$$ where $\nu$ is the area 2-form on $S^2$, and $\alpha$ satisfies $\omega=f^\ast\nu=d\alpha$. Notice that $f^\ast\nu$ is always exact since the cohomology of $S^3$ in dimension $2$ vanishes. We may also interpret $\mathscr{H}(f)$ as an intersection number, [@Bott82; @Milnor97]. Namely, consider two regular values $p_1$ and $p_2\in S^2$ of the map $f$, then $l_1=f^{-1}(p_1)$ and $l_2=f^{-1}(p_2)$ form a link in $S^3$, and the integral formula [\[eq:hopf-integral\]](#eq:hopf-integral){reference-type="eqref" reference="eq:hopf-integral"} can be interpreted, as the intersection number of $l_1$ with the Seifert surface spanning $l_2$: $$\begin{gathered}
\label{eq:hopf-intersection}
\mathscr{H}(f)=\text{lk}(l_1,l_2)\ .
\end{gathered}$$ If we replace $S^3$ with an arbitrary closed compact orientable 3-dimensional manifold $M$, we may still obtain an invariant of $f:M\longrightarrow S^2$ this way, provided that the condition $f^\ast\nu=d\alpha$ holds.

::: proposition
[]{#th:hopf-degree-general label="th:hopf-degree-general"} Let $M$ be a closed Riemannian manifold, and $\nu\in \Omega^2(S^2)$ the area form on $S^2$. The formula [\[eq:hopf-integral\]](#eq:hopf-integral){reference-type="eqref" reference="eq:hopf-integral"} provides a homotopy invariant for a map $f:M\longrightarrow S^2$, if the 2-form $f^\ast\nu$ is exact. Up to a constant multiple this invariant can be calculated as an intersection number defined in [\[eq:hopf-intersection\]](#eq:hopf-intersection){reference-type="eqref" reference="eq:hopf-intersection"}, where $l_1=f^{-1}(p_1)$ and $l_2=f^{-1}(p_2)$ form a link in $M$, where both $l_1$ and $l_2$ are null-homologous.
:::

::: proof
*Proof.* Given a homotopy $F:I\times M\mapsto
S^2$, $f_1=F(1,\,\cdot\,)$, $f_0=F(0,\,\cdot\,)$, we define $\hat{\omega}=F^\ast\nu$. We have $$\hat{\omega}  = F^\ast\nu=d\,\hat{\alpha},\qquad 
\omega_1  =  f_1^\ast\nu=i^\ast_1\,F^\ast\nu=d\,\alpha_1,\qquad 
\omega_0  =  f_0^\ast\nu=i^\ast_0\,F^\ast\nu=d\,\alpha_0,$$ where $i_0:M\hookrightarrow M\times I$, $i_0(x)=(x,0)$, $i_1:M\hookrightarrow M\times I$, $i_1(x)=(x,1)$ are appropriate inclusions. Potentials: $\hat{\alpha}\bigl|_{\{0\}\times M}$, $\alpha_0$, and $\hat{\alpha}\bigl|_{\{1\}\times M}$, $\alpha_1$ differ by a closed form $$\hat{\alpha}\bigl|_{\{0\}\times M}-\alpha_0=\beta_0,\quad \hat{\alpha}\bigl|_{\{1\}\times M}-\alpha_1=\beta_1,\quad d\beta_0=d\beta_1=0,$$ therefore the Stokes Theorem immediately implies that Formula [\[eq:hopf-integral\]](#eq:hopf-integral){reference-type="eqref" reference="eq:hopf-integral"} is independent of the choice of the potential. For the proof of invariance under homotopies we revoke the standard argument in [@Bott82 p. 228] $$\begin{split}
 0 & = \int_{F(M\times I)} \nu\wedge\nu
 =\int_{M\times I} \hat{\omega}\wedge \hat{\omega} =  \int_{M\times I} \hat{\omega}\wedge d\,\hat{\alpha}\\
 & = \int_{M\times I} d(\hat{\omega}\wedge \hat{\alpha}) = \int_{\partial(M\times I)} \hat{\omega}\wedge
\hat{\alpha}  =  \int_{M} \omega_1\wedge \alpha_1- \int_{M}
\omega_0\wedge \alpha_0\\
& =  \int_{M} d\alpha_1 \wedge \alpha_1-\int_{M}
d\alpha_0\wedge \alpha_0 =  \mathscr{H}(f_1)-\mathscr{H}(f_0).
\end{split}$$ The interpretation of $\mathscr{H}(f)$ as the intersection number [\[eq:hopf-intersection\]](#eq:hopf-intersection){reference-type="eqref" reference="eq:hopf-intersection"} is the same as in [@Bott82 p. 230]. ◻
:::

Given a 3-component parametrized link $L=\{L_1,L_2,L_3\}$ in $S^3$ we wish to associate a certain map $F_L:S^1\times S^1\times S^1\mapsto S^2$ to it, and interpret its Hopf degree as the Milnor $\bar{\mu}_{123}$-invariant. Recall the definition of the configuration space of $k$ points in $M$: $$\begin{gathered}
 \text{\rm Conf}_k(M):=\{(x_1,x_2,\ldots, x_k)\in (M)^k\,|\,x_i\neq x_j,\text{for}\ i\neq j\}.
\end{gathered}$$ As an introduction to the method we review the Gauss formula for the linking number of a 2-component link $L=\{L_1, L_2\}$ in $\mbox{\bbb R}^3$. Denote parameterizations of components by $L_1=\{x(s)\}$, $L_2=\{y(t)\}$ and consider the map $$\begin{gathered}
 F_L:S^1\times S^1\stackrel{L}{\longrightarrow} \text{\rm Conf}_2(\mbox{\bbb R}^3) \stackrel{r}{\longrightarrow} S^2,\qquad L(s,t)=(x(s), y(t))\ .
\end{gathered}$$ where $r(x,y)=\frac{x-y}{\|x-y\|}$ is a retraction of $\text{\rm Conf}_2(\mbox{\bbb R}^3)$ onto $S^2$. It yields the classical Gauss linking number formula: $$\begin{gathered}
 \bar{\mu}_{12}(L)=\text{lk}(L_1,L_2)=\text{deg}(F_L),\qquad\quad \text{deg}(F_L)=\int_{S^1\times S^1} F^\ast_L(\nu),
\end{gathered}$$ where $\nu\in \Omega^2(S^2)$ is the area form on $S^2$. Consequently, the linking number $\text{lk}(L_1,L_2)$, also known as the Milnor $\bar{\mu}_{12}$-invariant, can be obtained as the homotopy invariant of the map $F_L$ associated to $L$. Observe that homotopy classes $[S^1\times S^1,S^2]$ are isomorphic to $\mbox{\bbb Z}$ and $\text{deg}:F\rightarrow \text{deg}(F)$ provides the isomorphism, we also point out that as sets: $[S^k,\text{\rm Conf}_n(\mbox{\bbb R}^3)]=\pi_k(\text{\rm Conf}_n(R^3))$, and $[S^k,\text{\rm Conf}_n(S^3)]=\pi_k(\text{\rm Conf}_n(S^3))$ (c.f. [@Hatcher02 p. 421]). Thus considering the based homotopies, in context of the link homotopy of Borromean links, and base point free homotopies is equivalent in this setting.

In [@Kohno02; @Koschorke97], authors consider a natural extension of this approach to $n$-component parame-trized links $L$ in $\mbox{\bbb R}^3$ by considering maps $F_L:S^1\times\ldots\times S^1\longrightarrow \text{\rm Conf}_n(\mbox{\bbb R}^3)$ and their homotopy classes, we refer to this type of maps loosely as *link maps*, (c.f. [@Koschorke97]). In particular, Kohno [@Kohno02] proposed specific representatives of cohomology classes of the based loop space of $\text{\rm Conf}_n(\mbox{\bbb R}^3)$ as candidates for appropriate link homotopy invariants of $L$. It has been observed, in [@Deturck-Gluck-Melvin-Shonkwiler08], that in the $3$-component case it is beneficial to consider $\text{\rm Conf}_3(S^3)$, and $L\subset S^3$, since the topology of $\text{\rm Conf}_3(S^3)$ simplifies dramatically (in comparison to $\text{\rm Conf}_3(\mbox{\bbb R}^3)$). We review this simplification in the following paragraph as it is essential for the proof of the main theorem in this section.

<figure id="fig:n-borromean">
<div class="picture">
<p>(380, 150) (0,0)<span><img src="borr" style="width:5.2in" alt="image" /></span> (10,155)<span><span class="math inline"><em>L</em><sub>1</sub></span></span> (155,155)<span><span class="math inline"><em>L</em><sub>2</sub></span></span> (35,10)<span><span class="math inline"><em>L</em><sub>3</sub></span></span> (280,7)<span><span class="math inline">$\mathbf{\Bigl\}}$</span></span> (285,22)<span><span class="math inline"><em>n</em></span></span></p>
</div>
<figcaption>left: <span class="math inline"><em>μ̄</em><sub>123</sub> =  ± 1</span> and right: <span class="math inline"><em>μ̄</em><sub>123</sub> =  ± <em>n</em></span>.</figcaption>
</figure>

Consider a 3-component link $L=\{L_1, L_2, L_3\}$ in $S^3$ parametrized by $\{x(s),y(t),z(u)\}$ and the following map $$\begin{gathered}
\label{eq:F}
 F_L:S^1\times S^1\times S^1\stackrel{L}{\longrightarrow} \text{\rm Conf}_3(S^3)\stackrel{H}{\longrightarrow} S^2,\qquad L(s,t,u)=(x(s), y(t), z(u)),
\end{gathered}$$ where we denote by $H:S^3\times \mbox{\bbb R}^3\times (\mbox{\bbb R}^3\setminus\{0\})\mapsto S^2$ the projection on the $S^2$ factor, first concluding that $\text{\rm Conf}_3(S^3)\subset S^3\times S^3\times S^3$ is diffeomorphic to $S^3\times \text{\rm Conf}_2(\mbox{\bbb R}^3)=S^3\times
\mbox{\bbb R}^3\times (\mbox{\bbb R}^3\setminus\{0\})$, and consequently deformation retracts onto $S^3\times S^2$. Considering $S^3$ as unit quaternions, the map $H$ can be expressed explicitly by the formula, [@Deturck-Gluck-Melvin-Shonkwiler08]: $$\begin{gathered}
\label{eq:hermans-map}
 \text{\rm Conf}_3(S^3) \ni (x,y,z) \stackrel{H}{\longrightarrow}
 \frac{\text{pr}(x^{-1}\cdot y)-\text{pr}(x^{-1}\cdot z)}{\|\text{pr}(x^{-1}\cdot y)-\text{pr}(x^{-1}\cdot z)\|}\in S^2,
\end{gathered}$$ where $\cdot$ stands for the quaternionic multiplication, $\ ^{-1}$ is the quaternionic inverse, and $\text{pr}:S^3\longrightarrow \mbox{\bbb R}^3$ the stereographic projection from $1$. As a result one has the following particular expression for $F_L$: $$\begin{gathered}
\label{eq:F_L}
F_L(s,t,u)=\frac{\text{pr}(x(s)^{-1}\cdot z(u))-\text{pr}(x(s)^{-1}\cdot y(t))}{\|\text{pr}(x(s)^{-1}\cdot z(u))-\text{pr}(x(s)^{-1}\cdot
 y(t))\|}.
\end{gathered}$$

At this point we note that one has a freedom in choosing the deformation retraction $H$ in [\[eq:hermans-map\]](#eq:hermans-map){reference-type="eqref" reference="eq:hermans-map"}, but the above particular formula makes the proof of the main theorem of this section possible. Let $\mathbb{T}=S^1\times S^1\times S^1$ denote the domain of $F_L$, notice that, thanks to [\[eq:F_L\]](#eq:F_L){reference-type="eqref" reference="eq:F_L"}, restricting $F_L$ to the subtorus $\mathbb{T}_{23}$ in the second and third coordinate $(t,u)$ of $\mathbb{T}$, we obtain the usual Gauss map of the 2-component link $\{x^{-1}\cdot L_2,x^{-1} \cdot L_3\}$. Since the diffeomorphism $x^{-1}\cdot$ of $S^3$ is orientation preserving we conclude $\text{\rm deg}(F_L|_{\mathbb{T}_{23}})=\text{lk}(L_2,L_3)$. We claim that for any 2-component sublink $\{L_i,L_j\}$ of $L$: $$\label{eq:linking-numbers}
  \text{\rm deg}(F_L|_{\mathbb{T}_{ij}})=\pm\text{lk}(L_i,L_j),\qquad 1\leq i<j\leq 3,$$ where $i,j$ index the coordinates of $\mathbb{T}$. Indeed, since already true for $i=2$ and $j=3$, the general case follows by applying a permutation $\sigma\in \Sigma_3$ of coordinate factors in $\text{\rm Conf}_3(S^3)\subset (S^3)^3$. Notice that $\sigma$ is a diffeomorphism of $\text{\rm Conf}_3(S^3)\subset (S^3)^3$ either preserving or reversing the orientation (which explains the sign in [\[eq:linking-numbers\]](#eq:linking-numbers){reference-type="eqref" reference="eq:linking-numbers"}). We infer [\[eq:linking-numbers\]](#eq:linking-numbers){reference-type="eqref" reference="eq:linking-numbers"} because $\sigma$ induces an isomorphism on homotopy groups of $\text{\rm Conf}_3(S^3)$.

<figure id="fig:conf1">
<div class="center">
<div class="picture">
<p>(414,140) (30,0)<span><img src="borromean3" alt="image" /></span> (93,120)<span><span class="math inline"><em>L</em><sub>1</sub></span></span> (47,70)<span><span class="math inline"><em>L</em><sub>2</sub></span></span></p>
<p>(75,5)<span><span class="math inline"><em>L</em><sub>3</sub></span></span> (330,80)<span><span class="math inline"><em>A</em><sub>2</sub></span></span> (255,60)<span><span class="math inline"><em>A</em><sub>1</sub></span></span></p>
</div>
</div>
<figcaption>The model of <span class="math inline"><em>L</em><sub>Borr</sub></span> parametrized by <span class="math inline">{<em>L</em><sub>1</sub> = pr(<em>x</em>(<em>s</em>)), <em>L</em><sub>2</sub> = pr(<em>y</em>(<em>t</em>)), <em>L</em><sub>3</sub> = pr(<em>z</em>(<em>u</em>))}</span>. Arc <span class="math inline"><em>A</em><sub>1</sub></span> is a part of the unit circle on <span class="math inline"><em>x</em><em>y</em></span>-plane, <span class="math inline"><em>A</em><sub>2</sub></span> is a part of circle of radius <span class="math inline">1 + <em>ϵ</em></span>.</figcaption>
</figure>

The main theorem of this section is

::: theorem
[]{#th:milnor-hopf label="th:milnor-hopf"} Let $L=\{L_1,L_2,L_3\}$ be a 3-component Borromean link in $S^3$, consider the associated map $F_L$ defined in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}. The Hopf degree of this map satisfies $$\begin{gathered}
   \mathscr{H}(F_L)=\pm 2\,\bar{\mu}_{123},
 
\end{gathered}$$ where the sign depends on the choice of orientations of components of $L$.
:::

::: proof
*Proof.* By the *Borromean rings* we understand any $3$-component link with $\bar{\mu}_{123}=\pm 1$. Every such link is link homotopic to the diagram presented on Figure [1](#fig:n-borromean){reference-type="ref" reference="fig:n-borromean"} (where the sign can be determined from the orientation of components). The proof of the theorem can be reduced to the case of Borromean rings $L^\text{Borr}$, as follows: if $L$ and $L'$ are link-homotopic then $F_{L}$ and $F_{L'}$ are homotopic maps. By the Milnor classification of 3-component links up to link homotopy (see [@Milnor54]), every 3-component link $L$ with zero pairwise linking numbers and $\bar{\mu}_{123}=\pm n$ is represented by the right diagram on Figure [1](#fig:n-borromean){reference-type="ref" reference="fig:n-borromean"}. Consequently, up to homotopy, the associated map $F_L$ can be obtained from $F_{L_\text{Borr}}$ by covering one of the $S^1$ factors in $\mathbb{T}$, $n$-times. Therefore, in order to prove the claim it suffices to show $$\label{eq:hopf=2}
 \mathscr{H}(F_{L^\text{Borr}})=\pm 2\ .$$ According to Proposition [\[th:hopf-degree-general\]](#th:hopf-degree-general){reference-type="ref" reference="th:hopf-degree-general"}, $\mathscr{H}(F_L)$ is well defined for a link $L\subset S^3$ provided $F_L^\ast\nu\in \Omega^2(\mathbb{T})$ is trivial in $H^2(\mathbb{T})$, which is true thanks to [\[eq:linking-numbers\]](#eq:linking-numbers){reference-type="eqref" reference="eq:linking-numbers"} and because the pairwise linking numbers of $L$ are zero. The method of proof relies on a direct calculation of $\mathscr{H}(F_{L^\text{Bor}})$, for a carefully chosen parametrization of $L^\text{Bor}$ in $S^3$. This calculation is achieved by visualization of the link $l_{S,N}=l_S\cup l_N$ in $\mathbb{T}$, and application of Formula [\[eq:hopf-intersection\]](#eq:hopf-intersection){reference-type="eqref" reference="eq:hopf-intersection"}, where $$l_S:=F^{-1}_{L^\text{Bor}}(S),\qquad l_N:=F^{-1}_{L^\text{Bor}}(N)$$ are preimages of the North pole $N=(0,0,1)$ and South pole $S=(0,0,-1)$ in $S^2\subset \mbox{\bbb R}^3$. Notice that $[F_L^\ast\nu]=0$ in $H^2(\mathbb{T})$, if and only if, $[l_S]=0$ and $[l_N]=0$ in $H_1(\mathbb{T})$.

We begin by identifying $S^3$ with the set of unit quaternions in $\mbox{\bbb R}^4$ with standard coordinates: $$(w,x,y,z)=w+x\,\mathbf{i}+y\,\mathbf{j}+z\,\mathbf{k},$$ and choosing a specific parametrization of the Borromean rings $L^\text{Bor}$ in $S^3$. That is, define the $L_1$ component of $L^\text{Bor}$ to be the great circle in $S^3$ through $1$ and $\mathbf{k}$, parametrized as $$x(s)=\cos(s)+\sin(s)\,\mathbf{k},\quad
\bigl(\,x(s)^{-1}=\cos(s)-\sin(s)\,\mathbf{k}\,\bigr).$$

<figure id="fig:4-pos">
<div class="picture">
<p>(300, 120) (0,0)<span><img src="4-pos-reduced" style="height:1.8in" alt="image" /></span> (250,50)<span><span class="math inline">$s=\frac{3\pi}{2}$</span></span> (250,120)<span><span class="math inline"><em>s</em> = <em>π</em></span></span> (0,60)<span><span class="math inline">$s=\frac{\pi}{2}$</span></span> (0,120)<span><span class="math inline"><em>s</em> = 0</span></span></p>
</div>
<figcaption>Four positions corresponding to angles: <span class="math inline">$s=0,\frac{\pi}{2}, \pi, \frac{3\pi}{2}$</span>, small arrows next to <span class="math inline"><em>N</em></span> and <span class="math inline"><em>S</em></span> indicate a motion as <span class="math inline"><em>s</em>↗</span>.</figcaption>
</figure>

Observe that $\text{pr}(x(s))$ parameterizes the $z$-axis in $\mbox{\bbb R}^3$. Figure [2](#fig:conf1){reference-type="ref" reference="fig:conf1"} shows how to define the second and the third component $\{L_2, L_3\}$ of the Borromean rings $L^\text{Borr}$ in $\mbox{\bbb R}^3$ considered as an image of $S^3-\{1\}$ under the stereographic projection $\text{pr}:S^3\subset \mbox{\bbb R}^4\longrightarrow \mbox{\bbb R}^3$ from $1\in S^3$. $L_2$ will bound the annuli with a rounded wedge removed, i.e. an arc $A_1$ of the circle of radius $1$. The arc $A_2$ belongs to the circle of radius $r_\epsilon=(1+\epsilon)$ in the $(x,y)$-plane. The component $L_3$ is chosen to be a vertical ellipse linking with $L_2$.

<figure id="fig:framed-link">
<div class="picture">
<p>(390, 250)(-5,0) (0,0)<span><img src="proj-red-green-dashed-reduced" alt="image" /></span> (-6,182)<span><span class="math inline">$\frac{\pi}{2}$</span></span> (147,182)<span><span class="math inline">$\frac{\pi}{2}$</span></span> (110,215)<span>(A)</span> (263,215)<span>(B)</span> (110,65)<span>(C)</span> (263,65)<span>(D)</span></p>
</div>
<figcaption>Projection of <span class="math inline"><em>l</em><sub><em>S</em>, <em>N</em></sub></span> on the <span class="math inline"><em>s</em><em>u</em></span>-face and <span class="math inline"><em>s</em><em>t</em></span>-face of <span class="math inline">𝕋</span>. The strands <span class="math inline"><em>l</em><sub><em>S</em></sub></span> (solid line) and <span class="math inline"><em>l</em><sub><em>N</em></sub></span> (dashed line) are oppositely oriented since <span class="math inline"><em>l</em><sub><em>S</em></sub></span> and <span class="math inline"><em>l</em><sub><em>N</em></sub></span> are null homologous in <span class="math inline">𝕋</span>.</figcaption>
</figure>

Next we focus on the Formula [\[eq:F_L\]](#eq:F_L){reference-type="eqref" reference="eq:F_L"}, observe that multiplication by $x(s)^{-1}$ has an effect of a rotation by angle $s$ in $(w,z)$-plane and $(x,y)$-plane of $\mbox{\bbb R}^4$, which can be directly calculated: $$\begin{split}
x(s)^{-1}\cdot(w,x,y,z) & = \bigl(\cos(s) w+\sin(s) z, \cos(s) x +\sin(s) y,\\
&  \qquad \cos(s) y-\sin(s) x, \cos(s) z-\sin(s) w\bigr)\ .
\end{split}$$

The flow defined by this $S^1$-action is tangent to the great circles of $S^3$, thus the projected flow on $\mbox{\bbb R}^3$, via the stereographic projection $\text{pr}$, presents the standard picture of the Hopf fibration. Let us call an invariant Hopf torus an $r$-torus, if and only if, it contains a circle of radius $r$ in the $(x,y)$-plane. Without loss of generality we assume that $L_2$ on Figure [2](#fig:conf1){reference-type="ref" reference="fig:conf1"} belongs to the $r_{\epsilon/2}$-Hopf torus. Every point on a $r$-torus traces a $(1,1)$-curve under the $S^1$-action. For sufficiently small $\epsilon$, this motion can be regarded as a composition of the rotation by angle $s$ in both the direction of the meridian and the longitude of a $r$-torus. Therefore, for different values of $s$ the $S^1$-action "rotates" the components $L_2$ and $L_3$, by sliding along the Hopf tori by angle $s$ in the meridian and the longitudinal direction. We denote resulting link components by $$L^s_2(t)=\text{pr}(x^{-1}(s)\cdot y(t)),\qquad \text{and}\qquad  L^s_3(u)=\text{pr}(x^{-1}(s)\cdot z(u)).$$ The unit circle on $(x,y)$-plane is left invariant under this action and therefore can be considered as the "axis of the rotation". This justifies the choice of the particular shape of $L^\text{Borr}$ pictured on Figure [2](#fig:conf1){reference-type="ref" reference="fig:conf1"}. Next, we seek to visualize the projection of $l_{S,N}=l_S\cup l_N$ on the $su$-face and $st$-face of the domain $\mathbb{T}$ of $F_{L^\text{Bor}}$ parameterized by $(s,t,u)\in \mathbb{T}$, (it is convenient to think about $\mathbb{T}$ as a cube in $(s,t,u)$-coordinates, see Figure [4](#fig:framed-link){reference-type="ref" reference="fig:framed-link"}). For example when $s=0$, ($x(0)=1$), a point $(0,t_0,u_0)$ belongs to $l_N$, if and only if, the vector $\mathsf{v}_0=\text{pr}(y(t_0))-\text{pr}(z(u_0))$ points in the direction of $N=(0,0,1)$, analogous condition holds for direction $S=(0,0,-1)$, and $l_S$. In order to determine a diagram of $l_{S,N}$, we must keep track of the "head" and "tail" of the vector $\mathsf{v}_s=L^s_2(t)-L^s_3(u)$, for various values of $s$ and record values of $t$ and $u$ for which $\mathsf{v}_s$ points "North" and "South" (Figure [3](#fig:4-pos){reference-type="ref" reference="fig:4-pos"}). This reads as the following condition $$\label{eq:arrow-eq}
  (s,t,u)\in l_{S,N},\qquad\text{if and only if},\qquad \mathsf{v}_s \parallel S\ \text{or}\ N.$$ Without loss of generality we assume that $L^{s}_2$ is parametrized by the unit $t$-interval, and $L^{s}_3$ is parametrized by the unit $u$-interval. The process of recording values of $u$ and $t$ such that [\[eq:arrow-eq\]](#eq:arrow-eq){reference-type="eqref" reference="eq:arrow-eq"} holds is self-explanatory and is shown on Figure [2](#fig:conf1){reference-type="ref" reference="fig:conf1"} for values $s=0, \frac{\pi}{2}, \pi,
\frac{3\pi}{2}$, which is sufficient to draw projections of $l_S$ and $l_N$ on $st$- and $tu$-faces of $\mathbb{T}$. Collecting the information on Figure [3](#fig:4-pos){reference-type="ref" reference="fig:4-pos"}, we draw the projection of $l_{S,N}$ on the $su$-face of $\mathbb{T}$ represented by square (A) in Figure [4](#fig:framed-link){reference-type="ref" reference="fig:framed-link"}. Analogously, the projection of $l_{S,N}$ on the $st$-face of $\mathbb{T}$ is obtained and pictured in square (B). In order to obtain the diagram of $l_{S,N}$ we resolve the double points of Diagram (A) into crossings. For example, let us resolve the "circled" double point on (A), which occurs at $s=\frac{\pi}{2}$ in the *left* two stands of $l_{S,N}$. It suffices to determine the value of the $t$-coordinate at this point. Diagram (B) tells us that $l_S$ is below $l_N$, because $\mathbb{T}$ is oriented so that the $t$-axis points above the $su$-face (see Figure [4](#fig:framed-link){reference-type="ref" reference="fig:framed-link"}). Resolving the remaining crossings in a similar fashion leads to a diagrams of $l_{S,N}$ presented in squares (C) and (D). Clearly, the linking number of $l_S$ and $l_N$ is equal to $\pm 2$ in Diagram (C), (as the intersection number of e.g. $l_S$ with the obvious annulus on Diagram (C)). This justifies [\[eq:hopf=2\]](#eq:hopf=2){reference-type="eqref" reference="eq:hopf=2"}, and ends the proof. ◻
:::

Results of Theorem [\[th:milnor-hopf\]](#th:milnor-hopf){reference-type="ref" reference="th:milnor-hopf"} and Proposition [\[th:hopf-degree-general\]](#th:hopf-degree-general){reference-type="ref" reference="th:hopf-degree-general"} combined with Formula [\[eq:hopf-integral\]](#eq:hopf-integral){reference-type="eqref" reference="eq:hopf-integral"} allow us to express $\bar{\mu}_{123}(L)$ of a Borromean link $L$ as $$\label{eq:mu-formula}
 \begin{split}
  \bar{\mu}_{123}(L) & =  \int_{\mathbb{T}} F^\ast_L\nu\wedge \alpha=\int_{\mathbb{T}} L^\ast\omega\wedge \alpha,\\
  & \text{for}   \quad F^\ast_L\nu=d\alpha,\quad \omega=H^\ast\nu\in \Omega^2(\text{\rm Conf}_3(S^3)),
  \end{split}$$ where $\nu$ is the area form on $S^2$, and $H:\text{\rm Conf}_3(S^3)\longrightarrow S^2$ is the deformation retraction (as e.g. in [\[eq:hermans-map\]](#eq:hermans-map){reference-type="eqref" reference="eq:hermans-map"}). Alternatively, we may view $\omega$ as a 2-form on $(S^3)^3$ which is singular along the diagonals $\mathbf{\Delta}\subset (S^3)^3$, and the singularity is of order $O(r^2)$, where $r$ is a distance to $\mathbf{\Delta}$. Consequently, $\omega$ is integrable but not square integrable on $(S^3)^3$.

::: remark
[]{#rem:anti-symmetry label="rem:anti-symmetry"} Notice that the integral formula [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} exhibits the following property of $\bar{\mu}_{123}$: $$\bar{\mu}_{123}(L_1,L_2,L_3)=\text{\rm sign}(\sigma)\bar{\mu}_{123}(L_{\sigma(1)},L_{\sigma(2)},L_{\sigma(3)}),\qquad \sigma\in\Sigma_3\ .$$
:::
