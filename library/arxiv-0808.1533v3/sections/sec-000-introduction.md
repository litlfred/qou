---
doc_id: arxiv-0808.1533v3
doc_title: "On the third order helicity of magnetic fields on invariant domains in S³"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-21
source_pdf: 0808.1533v3.pdf
source_sha256: 3e003cc35a4e5711
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order heli city of a volume preserving vector ﬁeld B, which leads us to a"
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.986
---
A purpose of this paper is to develop a particular formula for the third order helicity on certain invariant sets of a volume preserving vector field $B$. The third order helicity, [@Khesin98], is an invariant of $B$ under the action of volumorphisms isotopic to the identity (denoted here by $\text{\rm SDiff}_0(M)$). Importance of such invariants stems from the basic fact that the evolution of the vorticity in the ideal hydrodynamics or of the magnetic field $B_0$ in the ideal magnetohydrodynamics (MHD), occurs along a path $t\longrightarrow g(t)\in \text{\rm SDiff}_0(M)$, [@Khesin98 p. 176]. Namely, $B(t)=g_\ast(t)B_0$ which is a direct consequence of Euler's equations: $$\label{eq:Eulers-eq}
\frac{d}{dt} B+[v, B]=0,\qquad \frac{d}{dt} g(t)=v .$$ One often says that the magnetic field $B$ is *frozen in* the velocity field $v$ of plasma, and the action by $\text{\rm SDiff}_0(M)$ is frequently referred to as *frozen-in-field* deformations. A fundamental example of such invariant defined for a general class in $\text{\rm SVect}(M)$ is the *helicity* $\mathsf{H}_{12}(B_1,B_2)$ defined for a pair of vector fields $B_1$ and $B_2$ on $M=S^3$ or a homology sphere. Helicity has been first introduced by Woltjer, [@Woltjer58], in the context of magnetic fields, and is a measure of how orbits of $B_1$, and $B_2$ link with each other. This topological interpretation of helicity has been made precise by Arnold, who introduced the concept of the average asymptotic linking number of a volume preserving vector field $B$ on $M$, [@Arnold86]. The subject has been further investigated in [@Akhmetiev05; @Berger90; @Laurence-Stredulinsky00b; @Hornig04] (see [@Khesin98] for additional references), where authors approach *higher helicities* via the Massey products under various assumptions about the vector fields or their domains (work in [@Gambaudo-Ghys97; @Spera06; @Verjovsky94] concerns yet other approaches to the problem). Extensions of the helicity concept to higher dimensional foliations can be found in [@Khesin92; @Riviere02; @Kotschick-Vogel03] and recently in [@Cantarella-Parsley09].

In this paper we present an alternative to these approaches, which is a natural extension of the notion of the linking number as a degree of a map, and exploits relations to the homotopy theory of certain maps associated to the link. The paper has two parts.

In the first part we show how the Milnor $\bar{\mu}_{123}$-invariant: $\bar{\mu}_{123}(L)$ of a parametrized Borromean link $L$ in $S^3$ can be obtained as a Hopf degree of an associated map to the configuration space of three points in $S^3$. The presented approach to link homotopy invariants of 3-component links has been proposed in [@Kohno02] for $n$-component links in $\mbox{\bbb R}^3$, and conveniently simplified for 3-component links in $S^3$ in the joint work [@Deturck-Gluck-Melvin-Shonkwiler08], where the full correspondence between $\bar{\mu}_{123}(L)$ and the Pontryagin-Hopf degree is proved. In Section [1](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"} we present the original proof of this correspondence in the Borromean case, which is sufficient for our purposes.

The second part of the paper is discusses a new definition of the third order helicity denoted here by $\mathsf{H}_{123}(B;\mathcal{T})$, where $B$ is a volume preserving vector field having an invariant unlinked domain $\mathcal{T}\subset S^3$. The simplest of such domains are three invariant handlebodies in $S^3$ which have pairwise unlinked cycles in the first homology. This includes the case of Borromean flux tubes already investigated in [@Berger90; @Laurence-Stredulinsky00b]. In Section [4](#sec:ergodic){reference-type="ref" reference="sec:ergodic"} we develop an ergodic formulation of $\mathsf{H}_{123}(B;\mathcal{T})$ as an average asymptotic $\bar{\mu}_{123}$-invariant, in the spirit of Arnold's average asymptotic linking number, which allows us to extend the definition of the invariant to topologically more complicated unlinked domains. We also derive, in Section [\[sec:energy\]](#sec:energy){reference-type="ref" reference="sec:energy"}, a lower bound for the $L^2$-energy of $B$ in terms of $\mathsf{H}_{123}(B;\mathcal{T})$.

*Acknowledgements:* The inspiration for the presented approach to the link homotopy invariants comes from the paper of Toshitake Kohno [@Kohno02], and I am grateful to him for the valuable e-mail correspondence. I have enjoyed conversations with many colleagues at the University of Pennsylvania, who have influenced this work. I wish to thank Herman Gluck for weekly meetings and his interest in this project, Frederic Cohen, Dennis DeTurck, Charlie Epstein, Paul Melvin, Tristan Rivi$\grave{\rm e}$re, Clay Shonkwiler, Jim Stasheff, David Shea Vick for the valuable input. I am also grateful to my advisor Robert Ghrist who introduced me to the subject long time ago. After posting recent joint results in [@Deturck-Gluck-Melvin-Shonkwiler08] we were informed by Paul Kirk about related works of Urlich Koschorke in [@Koschorke97; @Koschorke04], on homotopy invariants of link maps and Milnor $\bar{\mu}$-invariants. The author acknowledges financial support of DARPA, #FA9550-08-1-0386.

# The Milnor $\bar{\mu}_{123}$-invariant and the Hopf degree. {#sec:mu-and-hopf}

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

# Invariants of volume preserving flows. Helicities. {#sec:invariants-flows}

Given finitely many volume preserving vector fields $B_1$, $B_2$, $\ldots B_k\in \text{\rm SVect}(M)$ on $M=S^3$ or a homology 3-sphere one seeks quantities $\mathsf{I}(B_1,B_2,\ldots,B_k)$ invariant under the action of volumorphisms isotopic to the identity $g\in \text{\rm SDiff}_0(M)$, commonly known as *helicities* or *higher helicities*: $$\begin{gathered}
\label{eq:invariants}
 \mathsf{I}(B_1,B_2,\ldots,B_k)=\mathsf{I}(g_\ast B_1,g_\ast B_2,\ldots,g_\ast B_k),\qquad\quad \text{for all }g\in \text{\rm SDiff}_0(M), 
\end{gathered}$$ where $g_\ast$ is a push-forward by a diffeomorphism $g$. To distinguish the case of a single vector field $B$ (i.e. $B=B_1=\ldots=B_k$) we often refer to $\mathsf{I}(B)=\mathsf{I}(B,B,\ldots,B)$ as *self helicity*. We elucidated in the introduction a fundamental example of such invariant is the ordinary helicity $\mathsf{H}(B_1,B_2)$ of a pair of vector fields. In the remaining part of this section we review well known formulations of the helicity, which will later help us to point out analogies to the proposed formulation of the 3rd order helicity. Let $\mathcal{T}=\mathcal{T}_1\cup \mathcal{T}_2$ represent two invariant subdomains (not necessarily disjoint) under flows of $B_1$ and $B_2$ in $S^3$ and let $$\mathcal{T}=\mathcal{T}_1\times\mathcal{T}_2\subset \text{\rm Conf}_2(M)\subset M\times M.$$ Recall that the formula for $\mathsf{H}(B_1,B_2)$, from [@Khesin05; @Vogel03], specialized to invariant subdomains $\mathcal{T}=\mathcal{T}_1\cup \mathcal{T}_2$ may be expressed as $$\label{eq:helicity}
 \mathsf{H}_{12}(B_1,B_2)=\int_{\mathcal{T}_1\times\mathcal{T}_2} \omega\wedge\iota_{B_1}\mu\wedge\iota_{B_2}\mu,$$ where $\omega$ is known as the linking form on $M\times M$. When $\mathcal{T}=M\times M$ this formula is equivalent to a more commonly known expression: $\mathsf{H}(B_1,B_2)=\int_M \iota_{B_1}\mu\wedge d^{-1}(\iota_{B_2}\mu)$ (because $\omega$ also represents the integral kernel of $d^{-1}$). Philosophically, $\mathsf{H}(B_1,B_2)$ can be derived (c.f. [@Arnold86]) from the linking number of a pair of closed curves, which is expressed by Arnold's Helicity Theorem. For orbits $\{\mathscr{O}^1(x),\mathscr{O}^2(y)\}$ of $B_1$ and $B_2$ through $x, y\in M$, we introduce the following notation for the long pieces of closed up orbits $$\label{eq:orbits}
\begin{split}
 \mathscr{O}^{B_i}_T(x) & =  \{\Phi^i_t(x)\ |\ 0\leq t\leq T\}\subset \mathscr{O}^i(x),\qquad i=1,2\\
 \bar{\mathscr{O}}^i_T(x) & :=  \mathscr{O}^i_T(x)\cup \sigma(x,\Phi^i(x,T)).
\end{split}$$ where $\sigma(x,y)$ denotes a short path, [@Vogel03], connecting $x$ and $y$ in $M$ (see Section [4](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}). Paraphrasing [@Arnold86] we state (for the proof also see [@Vogel03]),

::: theorem
Given $B_1, B_2\in\text{\rm SVect}(M)$, The following limit exists almost everywhere on $M\times M$: $$\begin{gathered}
\label{eq:linking-function}
  \bar{m}_{B_1 B_2}(x,y)=\lim_{T\to \infty} \frac{1}{T^2}\, \text{lk}(\bar{\mathscr{O}}^1_T(x)\times\bar{\mathscr{O}}^2_T(y))\ .
 
\end{gathered}$$ Moreover, $\bar{m}_{B_1 B_2}$ is in $L^1(M\times M)$, and $$\label{eq:helicity-asymp}
 \mathsf{H}_{12}(B_1,B_2)=\int_{M\times M} \bar{m}_{B_1 B_2}(x,y)\, \mu(x)\wedge\mu(y)\ .$$
:::

The function $\bar{m}_{B_1 B_2}$ represents an asymptotic linking number of orbits $\{\mathscr{O}^1(x),\mathscr{O}^2(y)\}$, and the identity [\[eq:helicity-asymp\]](#eq:helicity-asymp){reference-type="eqref" reference="eq:helicity-asymp"} tells us that the helicity $\mathsf{H}_{12}(B_1,B_2)$ is equal to the average asymptotic linking number. In coming paragraphs, we will demonstrate, how this philosophy is applied to obtain the asymptotic $\bar{\mu}_{123}$-invariant for 3-component links and the third order helicity.

# Definition of "$\bar{\mu}_{123}$-helicity" on invariant unlinked handlebodies. {#sec:handlebody}

In this section we apply the formulation of the $\bar{\mu}_{123}$-invariant for the 3-component links in $S^3$, obtained in Section [1](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"}, to define the third order helicity of a volume preserving vector field $B$ on certain invariant sets $\mathcal{T}$ of $B$ in $S^3$. In the following paragraphs as a "warm-up" to a more general case treated in Section [4](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}, we consider the case of three disjoint unlinked handlebodies: $\mathcal{T}=\mathcal{T}_1\cup     \mathcal{T}_2\cup \mathcal{T}_3$ in $S^3$ each of genus $g(\mathcal{T}_i)$. Henceforth, we use "unlinked" to mean "with pairwise unlinked connected components". When $\mathcal{T}$ represents three unlinked tubes (also known as *flux tubes* [@Khesin98]) in $\mbox{\bbb R}^3$, the third order helicity has been developed by several authors [@Berger90; @Mayer03; @Laurence-Stredulinsky00b] via Massey product formula for the $\bar{\mu}_{123}$-invariant, we compare our approach to these known works in Section [\[sec:massey\]](#sec:massey){reference-type="ref" reference="sec:massey"}.

<figure id="fig:invariant-sets">
<div class="picture">
<p>(400,190) (10,30)<span><img src="T-borr-S" style="width:2in" alt="image" /></span> (180,0)<span><img src="T-borr-2-S" style="width:4in" alt="image" /></span> (20,30)<span><span class="math inline">𝒯<sup>Borr</sup></span></span> (60,140)<span><span class="math inline">𝒯<sub>2</sub></span></span> (25,80)<span><span class="math inline">𝒯<sub>3</sub></span></span> (125,70)<span><span class="math inline">𝒯<sub>1</sub></span></span></p>
</div>
<figcaption>The simplest unlinked handlebodies: flux tubes <span class="math inline">𝒯<sup>Borr</sup></span> modeled on the Borromean rings (left), and unlinked genus <span class="math inline">2</span> handlebodies (right).</figcaption>
</figure>

Assume $\mathcal{T}_i$s have smooth boundary and $B$ to be tangent to $\partial \mathcal{T}_i$, we set $$B_i:=B\bigl|_{\mathcal{T}_i},\qquad i=1,2,3,$$ and denote the flow of $B$ on $S^3$ by $\Phi$, and flows of restrictions $B_i$ by $\Phi^i$. Clearly, such $\mathcal{T}$ is an invariant set of $B$. Given any domain $\mathcal{T}$ with three connected components $\{\mathcal{T}_i\}$ we may always associate a product domain in $\text{\rm Conf}_3(S^3)$ as follows $$\label{eq:admissible-domain}
 \mathcal{T}:=\mathcal{T}_1\times \mathcal{T}_2\times \mathcal{T}_3\subset \text{\rm Conf}_3(S^3)\subset S^3\times S^3\times S^3\ .$$ Notice that $\mathcal{T}$ is a domain with corners in $\text{\rm Conf}_3(S^3)$, and we use the same notation for the product of $\mathcal{T}_i$ as for the union in $S^3$. Wherever needed, we also assume that $(S^3)^3$ is equipped with a product Riemannian metric. Let a domain $\mathcal{T}$ defined in [\[eq:admissible-domain\]](#eq:admissible-domain){reference-type="eqref" reference="eq:admissible-domain"}, where $\mathcal{T}_i\cap \mathcal{T}_j=$Ø, $i\neq j$ and each $\mathcal{T}_i$ is a handlebody in $S^3$ be called *unlinked handlebody*, if and only if, the 2-form $\omega\in\Omega^2(\text{\rm Conf}_3(S^3))$ defined in Equation [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} is exact on $\mathcal{T}$, i.e. $\omega$ has a local *potential* $\alpha_\omega\in \Omega^1(\mathcal{T})$: $$\label{eq:omega-exact}
 \omega=d\alpha_\omega\ .$$ Denote a volume preserving vector field $B$ and an unlinked handlebody $\mathcal{T}$ as a pair $(B;\mathcal{T})$.

::: remark
Since $\omega$ is a dual cohomology class to the $S^2$ factor in $\text{\rm Conf}_3(S^3)\cong S^3\times S^2$, $\omega$ does not admit a global potential.
:::

Because each handlebody $\mathcal{T}_i$ has a homotopy type of a bouquet of circles, there is a natural choice of the basis for $H_1(\mathcal{T}_i)$ which consists of cycles $\{L^k_i\}_{k=1,\ldots,g(\partial\mathcal{T}_i)}$ corresponding to the circles. We have the following practical characterization of unlinked handlebodies:

::: lemma
[]{#lem:unlinked-handlebody label="lem:unlinked-handlebody"} $\mathcal{T}$ is an unlinked handlebody, if and only if, $$\label{eq:admissible-condition}
  \text{lk}(L^k_i,L^r_j)  = 0,\qquad \text{for all\ }\, i,j,\qquad i\neq j$$
:::

::: proof
*Proof.* The standard integral pairing, [@Bott82], $H^2(\mathcal{T})\times H_2(\mathcal{T})\longrightarrow \mbox{\bbb R}$ implies that a closed $k$-form is exact, if and only if, it evaluates to zero on all $k$-cycles of the domain. By the K$\ddot{\rm u}$nneth formula $H_2(\mathcal{T})=H_2(\mathcal{T}_1\times \mathcal{T}_2\times \mathcal{T}_3)$ is generated by $L^k_i\otimes L^r_j$, and by [\[eq:linking-numbers\]](#eq:linking-numbers){reference-type="eqref" reference="eq:linking-numbers"}: $$\text{lk}(L^k_i,L^r_j) = \int_{L^k_i\times L^r_j} \omega\qquad  i\neq j.$$ Therefore the condition [\[eq:admissible-condition\]](#eq:admissible-condition){reference-type="eqref" reference="eq:admissible-condition"} is necessary and sufficient for $\omega$ to be exact on $\mathcal{T}$. ◻
:::

We define the $\bar{\mu}_{123}$-helicity of $(B;\mathcal{T})$ denoted by $\mathsf{H}_{123}(B;\mathcal{T})$ or $\mathsf{H}_{123}(B_1,B_2,B_3)$ as follows: $$\label{eq:mu_123-helicity}
\boxed{\mathsf{H}_{123}(B;\mathcal{T})=\mathsf{H}_{123}(B_1,B_2,B_3)\stackrel{\text{def.}}{=}\int_{\mathcal{T}} \bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\wedge \iota_{B_1}\mu_1\wedge \iota_{B_2}\mu_2\wedge \iota_{B_3}\mu_3, }$$ where $\mu_i$ denotes the pull-back of the volume form $\mu$ on $S^3$ under the projection $$\label{eq:projection-i}
\pi_i:S^3\times S^3\times S^3\longrightarrow S^3,\qquad \pi_i(x_1,x_2,x_3)=x_i,$$ and $\iota_{B_i}$ is a contraction by a vector field $B_i$. Our notational convention is to denote by $\iota_{B_i}\mu_i$ both the forms on the base of $\pi_i$ and the pullbacks: $\pi^\ast_i\bigl(\iota_{B_i}\mu_i\bigr)$. Notice that $\mu=\mu_1\wedge\mu_2\wedge\mu_3$ is a volume form on the product: $S^3\times S^3\times S^3$. There are obvious analogies between Formula [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} above, Formula [\[eq:helicity\]](#eq:helicity){reference-type="eqref" reference="eq:helicity"} for $\mathsf{H}_{12}(B;\mathcal{T})$, and the integral formula [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} for the $\bar{\mu}_{123}$-invariant. The $3$-form: $$\gamma_\omega:=\alpha_\omega\wedge d\alpha_\omega=\alpha_\omega\wedge \omega,$$ plays a role of the linking form as $\omega$ in Formula [\[eq:helicity\]](#eq:helicity){reference-type="eqref" reference="eq:helicity"}. The main motivation behind definition [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} is the ergodic interpretation of $\mathsf{H}_{123}(B;\mathcal{T})$ as an average asymptotic $\bar{\mu}_{123}$-invariant of orbits of $B$, which will become apparent in Section [4](#sec:ergodic){reference-type="ref" reference="sec:ergodic"}. Formula [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} can be also regarded as the third order helicity of three distinct vector fields $B_i$, supported on the handlebodies $\mathcal{T}_i$. In Section [\[sec:energy\]](#sec:energy){reference-type="ref" reference="sec:energy"}, we indicate how to construct the potential $\alpha_\omega$ from the basic elliptic theory of differential forms.

::: theorem
[]{#th:invariance-th label="th:invariance-th"} On every unlinked invariant handlebody $\mathcal{T}$ in $S^3$, $\mathsf{H}_{123}(B;\mathcal{T})$ is

-   independent of a choice of the potential $\alpha_\omega$,

-   invariant under the action of $\text{\rm SDiff}_0(S^3)$, i.e. for every $g\in \text{\rm SDiff}_0(S^3)$: $$\begin{gathered}
    \label{eq:invariance}
     \mathsf{H}_{123}(B;\mathcal{T})=\mathsf{H}_{123}(g_\ast B;g(\mathcal{T}))\ .
    \end{gathered}$$
:::

::: proof
*Proof.* To prove $(i)$ observe for every other potential $\alpha'_\omega$ of $\omega$, the difference $\beta=\alpha_\omega-\alpha'_\omega$ is a closed $1$-form on $\mathcal{T}$ (since $\omega=d\alpha_\omega=d\alpha'_\omega$). Therefore, $$\begin{aligned}
 \mathsf{H}_{123}(B;\mathcal{T})-\mathsf{H}_{123}'(B;\mathcal{T}) & = & \int_{\mathcal{T}} (\beta\wedge\omega)\wedge\iota_{B_1}\mu_1\wedge \iota_{B_2}\mu_2\wedge \iota_{B_3}\mu_3\\
 & \stackrel{(1)}{=} & \int_{\mathcal{T}} d\bigl(\beta\wedge \alpha_\omega\wedge\iota_{B_1}\mu_1\wedge \iota_{B_2}\mu_2\wedge \iota_{B_3}\mu_3\bigr)\\
 & = & \int_{\partial\mathcal{T}} \beta\wedge \alpha_\omega\wedge\iota_{B_1}\mu_1\wedge \iota_{B_2}\mu_2\wedge \iota_{B_3}\mu_3 \stackrel{(2)}{=} 0,
\end{aligned}$$ where in (1) we applied $d(\iota_{B_i}\mu_i)=0$ (since $B_i$'s are divergence free), and in (2): $$\iota_{B_i}\mu_i\bigl|_{\partial\mathcal{T}_i}=0,$$ (because each vector field $B_i$ is tangent to the boundary $\partial \mathcal{T}_i$), where $$\partial \mathcal{T}=\bigl(\partial \mathcal{T}_1\times \mathcal{T}_2\times \mathcal{T}_3\bigr)\cup \bigl(\mathcal{T}_1\times \partial\mathcal{T}_2\times \mathcal{T}_3\bigr)\cup \bigl(\mathcal{T}_1\times \mathcal{T}_2\times \partial\mathcal{T}_3\bigr).$$

The proof of $(ii)$ is in the style of [@Berger90; @Mayer03], but adapted to our setting. For any given $g\in \text{\rm SDiff}(S^3)$, by definition, there exists a path $t\longrightarrow g(t)\in \text{\rm SDiff}_0(S^3)$, such that $$g(0)=\text{id}_{S^3},\qquad g(1)=g\ .$$ Denote by $V$ the divergence free vector field on $S^3$, given by $V(x)=\frac{d}{dt} g(t,x)|_{t=0}$, i.e. $g(t)$ is a flow of $V$, and push-forward fields $B_i$ by $$B^t_i:=g(t)_\ast B_i\ .$$ It is well known (see Appendix [\[apx:A\]](#apx:A){reference-type="ref" reference="apx:A"}, or [@Freedman91-2 p. 224]) that 2-forms: $\iota_{B^t_i}\mu$ are frozen in the flow of $V$, i.e. $$\label{eq:forms-frozen-in}
 \frac{d}{dt}\bigl(g(t)^\ast\iota_{B^t_i}\mu\bigr) =(\partial_t+\mathcal{L}_V) \iota_{B^t_i}\mu = 0.$$ We also have a path $\hat{g}(t)=(g(t),g(t),g(t))$ in $\text{\rm SDiff}_0(S^3\times S^3\times S^3)$, which analogously leads to the vector field $\hat{V}=(V,V,V)$. (Recall that a tangent bundle $T(S^3)^3$ has a natural product structure). Equation [\[eq:forms-frozen-in\]](#eq:forms-frozen-in){reference-type="eqref" reference="eq:forms-frozen-in"} implies $$\label{eq:forms-frozen-in2}
(\partial_t+\mathcal{L}_{\hat{V}}) \bigl(\pi^\ast_i\iota_{B^t_i}\mu\bigr)=(\partial_t+\mathcal{L}_{\hat{V}}) \iota_{B^t_i}\mu_i= 0\ .$$ (In the second equation we merely revoke our notational conventions: $\iota_{B^t_i}\mu_i\equiv\pi^\ast_i\bigl(\iota_{g(t)^\ast B_i}\mu\bigr)$).

Let $\mathcal{T}(t)=\hat{g}(t)(\mathcal{T}(0))\subset \text{\rm Conf}_3(S^3)$, we must show $\frac{d}{dt} 
\mathsf{H}_{123}(B^t_1,B^t_2,B^t_3)=0$. Notice that for small enough $\epsilon$ and $t\in (t_0-\epsilon,t_0+\epsilon)$ we can assume, by $(i)$, that $\alpha_\omega$ is a time independent potential obtained from slightly bigger domain $\widetilde{\mathcal{T}}$ which deformation retracts on $\mathcal{T}(t_0)$, and satisfies $$\mathcal{T}(t)\subset\widetilde{\mathcal{T}},\qquad \text{\rm for}\quad t\in (t_0-\epsilon,t_0+\epsilon)\ .$$ Without loss of generality set $t_0=0$, and $\hat{g}(0)=\text{id}_{(S^3)^3}$, at $t_0$ we calculate: $$\begin{aligned}
 \frac{d}{dt} 
 \Bigl(\mathsf{H}_{123}(g(t)^\ast B_1,g(t)^\ast B_2,g(t)^\ast B_3)\Bigr) & = &
 \frac{d}{dt} \int_{\mathcal{T}(t)} \alpha_\omega\wedge d\alpha_\omega\wedge \iota_{B^t_1}\mu_1\wedge \iota_{B^t_2}\mu_2\wedge \iota_{B^t_3}\mu_3\\
 & = & \int_{\mathcal{T}(0)} \frac{d}{dt} \hat{g}(t)^\ast\bigl(\alpha_\omega\wedge d\alpha_\omega\wedge \iota_{B^t_1}\mu_1\wedge \iota_{B^t_2}\mu_2\wedge \iota_{B^t_3}\mu_3\bigr)\\
 & = & \int_{\mathcal{T}(0)} \bigl(\mathcal{L}_{\partial_t+\hat{V}}(\alpha_\omega\wedge d\alpha_\omega)\bigr)\wedge \iota_{B^t_1}\mu_1\wedge \iota_{B^t_2}\mu_2\wedge \iota_{B^t_3}\mu_3,
\end{aligned}$$ where in the last identity we applied [\[eq:forms-frozen-in2\]](#eq:forms-frozen-in2){reference-type="eqref" reference="eq:forms-frozen-in2"} and the product rule for the Lie derivative. Now because $\omega\wedge\alpha_\omega$ is time independent (for $t\in (t_0-\epsilon,t_0+\epsilon)$), Cartan magic formula yields $$\begin{aligned}
 \mathcal{L}_{\partial_t+\hat{V}}(\alpha_\omega\wedge d\alpha_\omega) & = & \mathcal{L}_{\hat{V}}(\alpha_\omega\wedge d\alpha_\omega) = \iota_{\hat{V}} d(\alpha_\omega\wedge d\alpha_\omega)+ d(\iota_{\hat{V}} (\alpha_\omega\wedge d\alpha_\omega))\\
 & =  & d(\iota_{\hat{V}} (\alpha_\omega\wedge d\alpha_\omega)),
\end{aligned}$$ where $d(\alpha_\omega\wedge d\alpha_\omega)=\omega\wedge\omega=0$. Since $B^t_i$ are tangent to the boundary of $\mathcal{T}_i(t)$, the same argument as in the proof of $(i)$ shows that the right hand side of the previous equation vanishes. ◻
:::

::: remark
Notice that the above argument indicates that if we replace $\alpha_{\omega}\wedge d\alpha_\omega$ by virtually any closed 3-form $\eta$ on $\text{\rm Conf}_3(S^3)$ (or $(S^3)^3$) we obtain some invariant under frozen-in-field deformations. If $\eta$ is exact we obtain trivial invariants, therefore the only sensible candidates here are cohomology classes of $\text{\rm Conf}_3(S^3)\cong S^3\times S^2$. In dimension $3$ it leaves us with a dual to the $S^3$ factor in $\text{\rm Conf}_3(S^3)$. Based on the considerations in Section [1](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"} one may argue that an invariant obtained this way is trivial. Indeed, the cohomology class $\eta$ evaluated on any 3-torus obtained from a 3-component link in $S^3$ via the map $L$ in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"} is zero. Therefore, one could apply the ergodic approach of Section [4](#sec:ergodic){reference-type="ref" reference="sec:ergodic"} to show that $\int \eta\wedge\iota_{B}\mu_1\wedge \iota_{B}\mu_2\wedge \iota_{B}\mu_3$ defines a trivial invariant. The crucial obstacle in extending the formula in [\[eq:mu_123-helicity\]](#eq:mu_123-helicity){reference-type="eqref" reference="eq:mu_123-helicity"} to encompass the whole $(S^3)^3$ is the fact that the potential $\alpha_\omega$ cannot be globally defined on $\text{\rm Conf}_3(S^3)$.
:::

# The ergodic interpretation of $\mathsf{H}_{123}(B;\mathcal{T})$ {#sec:ergodic}

The following statement is often seen in literature [@Cantarella-DeTurck-Gluck01; @Cantarella-DeTurck-Gluck-Teytel00]:

> *Helicity measures the extent to which vector fields twist and coil around each other.*

A beauty of Arnold's ergodic approach to the helicity $\mathsf{H}_{12}(B)$ is that it makes this statement precise, by interpreting $\mathsf{H}_{12}(B)$ as an average asymptotic linking number of orbits of $B$. But, it also has a practical application as it allows us to extend our approach to certain invariant sets of $B$. In this section we apply this philosophy to our newly defined invariant $\mathsf{H}_{123}(B;\mathcal{T})$, and interpret it as the average asymptotic $\bar{\mu}_{123}$-invariant of orbits of $B$ in $\mathcal{T}$. Moreover, this ergodic interpretation leads us to an alternative, more intuitive proof of Helicity Invariance Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}.

We begin by observing that given a volume preserving vector field $B$ on $M$ and its flow $\Phi_t$, we may regard $B$ as three vector fields on $(M)^3$. Thus, $(\Phi,\Phi,\Phi)$ induces a natural $\mbox{\bbb R}^3$ action defined as follows: $$\label{eq:R3-action}
 \mathbf{\Phi}:\mbox{\bbb R}^3\times (M)^3\longrightarrow (M)^3,\qquad \bigl((s,t,u),x,y,z\bigr)\stackrel{\mathbf{\Phi}}{\longrightarrow} (\Phi(s,x),\Phi(t,y), \Phi(u,z)).$$ Observe that $\mathbf{\Phi}$ is a volume preserving action on $(M)^3$. Our analysis is rooted in techniques developed in [@Arnold86; @Laurence-Avellaneda93; @Laurence-Stredulinsky00b; @Vogel03], the main tool is the following

::: theorem
[]{#th:multi-ergodic label="th:multi-ergodic"} For any real valued $L^1$-function $F$ on $(M)^3$, the time averages under the action in [\[eq:R3-action\]](#eq:R3-action){reference-type="eqref" reference="eq:R3-action"}: $$\begin{gathered}
\bar{F}(x,y,z)=\lim_{T\to \infty}\frac{1}{T^3}\int^T_0\int^T_0\int^T_0
 F(\Phi(x,s),\Phi(y,t),\Phi(z,u))\,d s\,d t\,d u
\end{gathered}$$ converge almost everywhere. In addition, the limit function $\bar{F}$ satisfies

-   $\|\bar{F}\|_{L^1((M)^3)}\leq \|F\|_{L^1((M)^3)}$,

-   $\bar{F}$ is invariant under the $\mathbf{\Phi}$-action,

-   if $(M)^3$ is of finite volume then $$\begin{gathered}
    \label{eq:ergodic-integrals-equal}
     \int_{(M)^3}\bar{F} =\int_{(M)^3} F\ .
    \end{gathered}$$
:::

::: definition
Define *invariant unlinked domain* $\mathcal{T}$ of $B$ as an arbitrary $\mathbf{\Phi}$-invariant set, with topological closure $\overline{\mathcal{T}}$ which belongs to a larger product of open sets $\widetilde{\mathcal{T}}=\widetilde{\mathcal{T}}_1\times \widetilde{\mathcal{T}}_2\times \widetilde{\mathcal{T}}_3$ in $\text{\rm Conf}_3(S^3)$, satisfying the following

-   $\widetilde{\mathcal{T}}$ admits a *short path system* $\mathcal{S}$,

-   Equation [\[eq:omega-exact\]](#eq:omega-exact){reference-type="eqref" reference="eq:omega-exact"} holds on $\widetilde{\mathcal{T}}$,

where by a system of short paths on $\widetilde{\mathcal{T}}$, [@Vogel03; @Khesin98], we understand a collection of curves $\mathcal{S}=\{\sigma_i(x,y)\}$ on each open set $\widetilde{\mathcal{T}}_i$ such that

-   for every pair of points $x,y \in \widetilde{\mathcal{T}}_i$ there is a connecting curve $\sigma_i(x,y):I\mapsto \widetilde{\mathcal{T}}_i$ in $\mathcal{S}$, $\sigma_i(0)=x$ and $\sigma_i(1)=y$,

-   the lengths of paths in $\mathcal{S}$ are uniformly bounded above by a common constant.
:::

Topologically, every $\mathbf{\Phi}$-invariant set is a union of products of orbits of $B$ in $(S^3)^3$. It is often convenient to think of the orbits $\mathbf{\Phi}$-action as a foliation of $(S^3)^3$. Then $\mathbf{\Phi}$-invariant sets are just union of leaves of this foliation. A fundamental example of an invariant unlinked domain is the case of $\mathbf{\Phi}$-invariant set $\mathcal{T}$ contained in the product $\widetilde{\mathcal{T}}=\widetilde{\mathcal{T}}_1\times \widetilde{\mathcal{T}}_2\times \widetilde{\mathcal{T}}_3$ of disjoint open unlinked handlebodies $\widetilde{\mathcal{T}}_i$. Note that in this case we do not require $B$ to be tangent to $\partial\widetilde{\mathcal{T}}_i$, and $\widetilde{\mathcal{T}}$ always admits a short path system as we describe in the following

::: remark
In [@Vogel03], Vogel shows that on a closed manifold $M$, geodesics always provide a short path system. When $\mathcal{T}$ is contained in the product of unlinked handlebodies $\widetilde{\mathcal{T}}$ we may easily construct such system on $\widetilde{\mathcal{T}}$ as follows Because $\mathcal{\mathcal{T}}_i$ are proper subsets of $S^3$ we generally do not want to use ambient geodesics from $S^3$ as they may not lie entirely in $\mathcal{T}_i$. To obtain $\mathcal{S}$ one puts an artificial Riemannian metric on each $\widetilde{\mathcal{T}}_i$ which makes $\partial\widetilde{\mathcal{T}}_i$ totally geodesic, and choose $\mathcal{S}$ to be geodesics on such Riemannian manifold. Observe that applying a diffeomorphism $g\in \text{Diff}(\widetilde{\mathcal{T}})$ to $\mathcal{S}$ results in the system $g\mathcal{S}$ on $g(\widetilde{\mathcal{T}})$.
:::

The following result is an analog of Arnold's Helicity Theorem in our setting,

::: theorem
[]{#th:ergodic-mu label="th:ergodic-mu"} Given $(B;\mathcal{T})$, the following limit (asymptotic $\bar{\mu}_{123}$-invariant of orbits) exists for almost all $(x,y,z)\in \mathcal{T}$: $$\label{eq:bar-m_B}
 \bar{m}_B(x,y,z)=\lim_{T\to\infty} \frac{1}{T^3}\bar{\mu}_{123}\bigl(\bar{\mathscr{O}}^{B_1}_T(x),\bar{\mathscr{O}}^{B_2}_T(y),\bar{\mathscr{O}}^{B_3}_T(y)\bigr).$$ Moreover, $$\label{eq:H_123-ergodic}
 \mathsf{H}_{123}(B;\mathcal{T})=\int_{\mathcal{T}} \bar{m}_B(x,y,z)\,\mu(x)\wedge\mu(y)\wedge\mu(z)\ .$$
:::

::: proof
*Proof.* The proof is similar to the one in e.g. [@Vogel03]. Before we start, we must point out the following identity (valid for any 3-form $\beta$ on $M\times M\times M$ and vector fields $B_1,B_2,B_3$ on $M$)

$$\label{eq:iota-volume}
 \begin{split}
(\iota_{B_3}\iota_{B_2}\iota_{B_1}\beta)\wedge\mu_1\wedge\mu_2\wedge\mu_3 & =
\beta(B_1,B_2,B_3)\,\mu_1\wedge\mu_2\wedge\mu_3\\
 & =\beta\wedge\iota_{B_1}\mu_1\wedge\iota_{B_2}\mu_2\wedge\iota_{B_3}\mu_3\ .
 \end{split}$$ The first equation follows from the definition, the second one is a consequence of the fact that $\iota_B$ is an antiderivation i.e. $$\label{eq:iota-antiderivation}
  \iota_B(\alpha\wedge\beta)=(\iota_B\alpha)\wedge\beta+(-1)^{|\alpha|}\alpha\wedge(\iota_B\beta),$$ and $\iota_{B_i}\mu_j=0$, for $i\neq j$ (see Appendix [\[apx:A\]](#apx:A){reference-type="ref" reference="apx:A"}). As a result, $$\begin{aligned}
\notag  \mathsf{H}_{123}(B_1,B_2,B_3) & = & \int_{\mathcal{T}} \bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\wedge \iota_{B_1}\mu_1\wedge \iota_{B_2}\mu_2\wedge \iota_{B_3}\mu_3\\
& = & \int_\mathcal{T} \bigl(\iota_{B_3}\iota_{B_2}\iota_{B_1}\bigl(\alpha_\omega\wedge d\alpha_\omega\bigr)\bigr)\,\mu_1\wedge\mu_2\wedge\mu_3\\
\label{eq:m-function}  & = & \int_\mathcal{T} m_{B_1,B_2,B_3}(x,y,z)\,\mu_1\wedge \mu_2\wedge \mu_3,
\end{aligned}$$ where $m_{B_1,B_2,B_3}:=\alpha_\omega\wedge d\alpha_\omega(B_1,B_2,B_3)$. For convenience, let us set (see [\[eq:orbits\]](#eq:orbits){reference-type="eqref" reference="eq:orbits"}): $$\bar{\mathscr{O}}(x,y,z;T):=\bar{\mathscr{O}}^{B_1}_T(x)\times \bar{\mathscr{O}}^{B_2}_T(y)\times\bar{\mathscr{O}}^{B_3}_T(y)\ .$$ Observe that if the orbit $\bar{\mathscr{O}}(x,y,z;T)$ is nondegenerate, it represents a Borromean link and we may apply Formula [\[eq:mu-formula\]](#eq:mu-formula){reference-type="eqref" reference="eq:mu-formula"} to get $$\begin{aligned}
\bar{\mu}_{123}\bigl(\bar{\mathscr{O}}^{B_1}_T(x),\bar{\mathscr{O}}^{B_2}_T(y),\bar{\mathscr{O}}^{B_3}_T(y)\big)
& = & \int_{\bar{\mathscr{O}}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega\\
& = & \int_{\mathscr{O}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega+(I),
\end{aligned}$$ where the term $(I)$ involves integrals over short paths in $\mathcal{S}$, (see Appendix [\[apx:B\]](#apx:B){reference-type="ref" reference="apx:B"}). For degenerate orbits (such as fixed points etc.), the above formula still makes sense because $\bar{\mu}_{123}$ is a homotopy invariant of the associated map as proven in Section [1](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"}. For every $(x,y,z)$ : $$D\mathbf{\Phi}_{(x,y,z)}[\partial_i]=B_i,\quad i=1,2,3,$$ where $\partial_1:=\partial_s$,$\partial_2:=\partial_t$,$\partial_3:=\partial_u$, thus we obtain $$\begin{aligned}
 \mathbf{\Phi}^\ast_{(x,y,z)}(\alpha_\omega\wedge d\alpha_\omega) & = & (\alpha_\omega\wedge d\alpha_\omega(B_1,B_2,B_3)(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\\
 & = & m_{B_1,B_2,B_3}(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\ .
\end{aligned}$$ Therefore, $$\int_{\mathscr{O}(x,y,z;T)}
\alpha_\omega\wedge d\alpha_\omega=\int^T_0\int^T_0\int^T_0 m_{B_1,B_2,B_3}(\Phi^1(x,s),\Phi^2(y,t),\Phi^3(z,u))\,ds\wedge dt\wedge du\ .$$ Function $m_{B_1,B_2,B_3}$ is smooth bounded on $\mathcal{T}$ and hence $L^1$. Because short paths do not contribute to the time average (see Appendix [\[apx:B\]](#apx:B){reference-type="ref" reference="apx:B"}): $$\lim_{T\to\infty} \frac{1}{T^3}(I)=0.$$ Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"} applied to the function $m_{B_1,B_2,B_3}$ yields almost everywhere existence of the limit [\[eq:bar-m_B\]](#eq:bar-m_B){reference-type="eqref" reference="eq:bar-m_B"}. Hence we obtain the invariant $L^1$-function $\bar{m}_B:=\bar{m}_{B_1,B_2,B_3}$ on $\mathcal{T}$. The identity [\[eq:H_123-ergodic\]](#eq:H_123-ergodic){reference-type="eqref" reference="eq:H_123-ergodic"} follows from $(iii)$ of Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"}. ◻
:::

::: theorem
[]{#th:invariance-th-ergodic label="th:invariance-th-ergodic"} On every unlinked domain $\mathcal{T}$ in $S^3$, (i) and (ii) of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"} hold for $\mathsf{H}_{123}(B;\mathcal{T})$.
:::

::: proof
*Proof.* The proof of $(i)$ immediately follows from independence of the limit [\[eq:bar-m_B\]](#eq:bar-m_B){reference-type="eqref" reference="eq:bar-m_B"} of the choice of the potential $\alpha_\omega$. For the proof of $(ii)$ we must show the following $$\int_\mathcal{T} m_{B_1,B_2,B_3}\,\mu_1\wedge \mu_2\wedge \mu_3=\int_{g(\mathcal{T})} m_{g_\ast B_1,g_\ast B_2, g_\ast B_3}\,\mu_1\wedge \mu_2\wedge \mu_3\ .$$ Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"} tells us that $m_{B_1,B_2,B_3}$ and $m_{g_\ast B_1,g_\ast B_2, g_\ast B_3}$ admit $L^1$-averages $\bar{m}_{B_1,B_2,B_3}$ and $\bar{m}_{g_\ast B_1,g_\ast B_2, g_\ast B_3}$, under actions of $B_i$ and $g_\ast B_i$ respectively. It suffices to show the following identity $$\label{eq:m=gm}
 \bar{m}_{B_1,B_2,B_3}(x,y,z)=\bar{m}_{g_\ast B_1,g_\ast B_2, g_\ast B_3}(g(x),g(y),g(z)),\qquad \text{a.e.}$$ then [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"} is an immediate consequence of Equation [\[eq:ergodic-integrals-equal\]](#eq:ergodic-integrals-equal){reference-type="eqref" reference="eq:ergodic-integrals-equal"}, change of variables for integrals, and the fact that $g$ preserves volume (i.e. $\mu_i=g^\ast\mu_i$). Borrowing notation from the previous theorem set $$\begin{aligned}
 g\bar{\mathscr{O}}(x,y,z;T) & := & g(\bar{\mathscr{O}}^{B_1}_T(x))\times g(\bar{\mathscr{O}}^{B_2}_T(y))\times g(\bar{\mathscr{O}}^{B_3}_T(z))\\
 & = & \bar{\mathscr{O}}^{g_\ast B_1}_T(g(x))\times \bar{\mathscr{O}}^{g_\ast B_2}_T(g(y))\times \bar{\mathscr{O}}^{g_\ast B_3}_T(g(z)),
\end{aligned}$$ where the second identity is a consequence of the fact that the flow of $g_\ast B_i$ is obtained as a composition of $g$ and the flow of $B_i$. Since $g$ is isotopic to the identity, $\bar{\mathscr{O}}(x,y,z;T)$ and $g\bar{\mathscr{O}}(x,y,z;T)$ are homotopic as link maps (for nondegenerate orbits they are in fact isotopic Borromean links in $S^3$) and by theorems of Section [1](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"}, we have $$\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))=\bar{\mu}_{123}(g\bar{\mathscr{O}}(x,y,z;T)).$$ As a result of the above identity and [\[eq:bar-m_B\]](#eq:bar-m_B){reference-type="eqref" reference="eq:bar-m_B"} we derive a.e. $$\begin{aligned}
  \bar{m}_{B_1,B_2,B_3}(x,y,z) & = & \lim_{T\to\infty}\frac{1}{T^3}\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))\\
   & = & \lim_{T\to\infty}\frac{1}{T^3}\bar{\mu}_{123}(g\bar{\mathscr{O}}(x,y,z;T))=\bar{m}_{g_\ast B_1,g_\ast B_2, g_\ast B_3}(g(x),g(y),g(z)).
\end{aligned}$$ Notice that in the last equation we used the "pushed forward" short paths system: $g\mathcal{S}$. Since the lengths of paths in $g\mathcal{S}$ are bounded as well, they do not contribute to the limit. This proves the identity [\[eq:m=gm\]](#eq:m=gm){reference-type="eqref" reference="eq:m=gm"}, and consequently [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"}. ◻
:::

Notice that the above argument does not require the Stokes Theorem, and as such may lead to further generalizations. Clearly, for $\mathsf{H}_{123}(B;\mathcal{T})$ to be nontrivial $\mathcal{T}$ must be of nonzero measure.

# Flux formula for $\mathsf{H}_{123}(B;\mathcal{T})$.

The following formula is a well known property of the ordinary helicity $\mathsf{H}_{12}(B;\mathcal{T})$ of the flux tubes $\mathcal{T}$ modeled on a 2-component link $L=\{L_1,L_2\}$ (see e.g. [@Laurence-Avellaneda93; @Cantarella00])

$$\label{eq:helicity12-flux-tubes}
\mathsf{H}_{12}(B;\mathcal{T})=\mathsf{H}_{12}(B_1,B_2)=\text{lk}(L_1,L_2)\,\text{Flux}(B_1)\,\text{Flux}(B_2).$$ Here we show an analogous property for $\mathsf{H}_{123}(B;\mathcal{T})$, when $\mathcal{T}$ is an invariant unlinked handlebody. Recall that $\{L^k_i\}_{k=1,\ldots,g(\partial\mathcal{T}_i)}$ denotes the basis of $H_1(\mathcal{T})$ defined in Lemma [\[lem:unlinked-handlebody\]](#lem:unlinked-handlebody){reference-type="ref" reference="lem:unlinked-handlebody"}.

::: proposition
$\mathsf{H}_{123}(B_1,B_2,B_3)$ on invariant unlinked handlebodies $\mathcal{T}$ satisfies the following formula $$\label{eq:helicity-fluxes}
 \mathsf{H}_{123}(B_1,B_2,B_3)=\sum_{i, j, k} \bar{\mu}_{123}(L^i_1, L^j_2, L^k_3)\,\text{Flux}_{\Sigma_i}(B_1)\,\text{Flux}_{\Sigma_j}(B_2)\,\text{Flux}_{\Sigma_k}(B_3),$$ where $\{L^i_1\otimes L^j_2\otimes L^k_3\}$ is a basis of $H_3(\mathcal{T})$, $\text{Flux}(B_i)$ stands for the flux of $B_i$ through a cross sectional surface $\Sigma_k$ of $\mathcal{T}_i$, which represents the homology Poincar$\acute{\rm e}$ dual of $L^k_i$ in $H_2(\mathcal{T}_i,\partial\mathcal{T}_i)$.
:::

::: proof
*Proof.* Recall that the flux $\text{Flux}_{\Sigma_k}(B_i)$ of a vector field $B_i$ though a cross-sectional surface $\Sigma_k$ in $\mathcal{T}_i$ is given by: $$\label{eq:flux}
 \begin{split}
  \text{Flux}_{\Sigma_k}(B_i) & =  \int_{\Sigma_k} \iota_{B_i}\mu=\int_{\mathcal{T}_i} h_k\wedge\iota_{B_i}\mu\\
  & =  \int_{\mathcal{T}_i} \iota_{B_i}h_k\wedge\mu =\int_{\mathcal{T}_i} h_k(B_i),
  \end{split}$$ where 1-forms $h_k$ represent cohomology Poincar$\acute{\rm e}$ duals of $\Sigma_k$, and we applied [\[eq:iota-antiderivation\]](#eq:iota-antiderivation){reference-type="eqref" reference="eq:iota-antiderivation"} in the third equation. For every closed curve $\gamma\subset \mathcal{T}$ $h_k$ satisfies $$\int_{\gamma} h_k=\#(\gamma,\Sigma_k)=\text{deg}(\gamma, L_k),$$ where $\text{deg}(\gamma, L^j_k)$ measures how many times $\gamma$ "wraps around" the cycle $L^j_k$.

For simplicity, we first assume that $\mathcal{T}$ is modeled on a Borromean link $L=\{L_1,L_2,L_3\}$ (such as $\mathcal{T}^\text{Borr}$ on Figure [5](#fig:invariant-sets){reference-type="ref" reference="fig:invariant-sets"}). Then, $h=h_1\wedge h_2\wedge h_3\in \Omega^3(\mathcal{T})$ is a cohomology class dual to the cycle $L_1\otimes L_2\otimes L_3$ in $H_3(\mathcal{T})$. Define $$H:=\iota_{B_3}\iota_{B_2}\iota_{B_1} h=h(B_1,B_2,B_3),$$ which is a smooth function, and let $\bar{H}$ be the time average of $H$ as in Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"}. It suffices to show $$\label{eq:H-equation}
   \bar{m}_{B_1,B_2,B_3}=\bar{\mu}_{123}(L)\,\bar{H},\qquad \text{a.e.}$$ Analogously, as in the proof of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}, Equation [\[eq:H-equation\]](#eq:H-equation){reference-type="eqref" reference="eq:H-equation"} immediately implies Formula [\[eq:helicity-fluxes\]](#eq:helicity-fluxes){reference-type="eqref" reference="eq:helicity-fluxes"}. Assume the notation of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"}, for given $T$ consider $\bar{\mathscr{O}}(x,y,z;T)$. Thanks to Theorem [\[th:milnor-hopf\]](#th:milnor-hopf){reference-type="ref" reference="th:milnor-hopf"} (see the first paragraph of the proof) we have $$\begin{aligned}
  \bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T)) & = & \bar{\mu}_{123}(L)\,\bigl(\text{deg}(\bar{\mathscr{O}}^{B_1}_T(x),L_1)\,\text{deg}(\bar{\mathscr{O}}^{B_2}_T(y),L_2)\,\text{deg}(\bar{\mathscr{O}}^{B_3}_T(x),L_3)\bigr)\\
  & = & \bar{\mu}_{123}(L)\int_{\bar{\mathscr{O}}(x,y,z;T)} h\ .
 
\end{aligned}$$ Therefore, $$\begin{aligned}
  \bar{m}_{B_1,B_2, B_3}(x,y,z) & = & \lim_{T\to \infty} \frac{1}{T^3}\bar{\mu}_{123}(\bar{\mathscr{O}}(x,y,z;T))\\
  & = & \bar{\mu}_{123}(L)\lim_{T\to \infty} \frac{1}{T^3}\int_{\bar{\mathscr{O}}(x,y,z;T)} H\\
  & =  &\bar{\mu}_{123}(L) \bar{H}(x,y,z),
 
\end{aligned}$$ where the last equality is again the consequence of short paths not contributing to the limit. From the product structure of $\mathcal{T}$ and $(iii)$ of Theorem [\[th:multi-ergodic\]](#th:multi-ergodic){reference-type="ref" reference="th:multi-ergodic"} we get $$\int_\mathcal{T} \bar{H} =\int_\mathcal{T} H=\bigl(\int_{\mathcal{T}_1} h_1(B_1) \bigr)\bigl(\int_{\mathcal{T}_2} h_2(B_2) \bigr)\bigl(\int_{\mathcal{T}_3} h_3(B_3) \bigr),$$ which combined with Equation [\[eq:flux\]](#eq:flux){reference-type="eqref" reference="eq:flux"} for fluxes concludes the proof in the case of Borromean flux tubes. The proof in the case of a general handlebody is analogous, once we show the following

::: lemma
Let $\mathcal{O}=\{\mathcal{O}_1,\mathcal{O}_2, \mathcal{O}_3\}$ be a 3-component link in $S^3$ such that $\mathcal{O}_i\subset \mathcal{T}_i$ for each $i$. Then $\mathcal{O}$ is Borromean and $$\label{eq:mu-in-T}
 \bar{\mu}_{123}(\mathcal{O})=\sum_{i, j, k} \bar{\mu}_{123}(L^i_1, L^j_2, L^k_3)\,\text{deg}(\mathcal{O}_1, L^i_1)\,\text{deg}(\mathcal{O}_2, L^j_2)\,\text{deg}(\mathcal{O}_3, L^k_1)\ .$$
:::

::: proof
*Proof.* Thanks to the interpretation of the $\bar{\mu}_{123}$-invariant in Section [1](#sec:mu-and-hopf){reference-type="ref" reference="sec:mu-and-hopf"}, it is not only a link homotopy invariant, but also a homotopy invariant of the associated map $F_{\mathcal{O}}$ defined in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}. Observe that each component $\mathcal{O}_i$ can be homotoped inside of its handlebody $\mathcal{T}_i$ to become a bouquet of circles $\widehat{\mathcal{O}}_i\cong S^1\vee S^1\vee\ldots\vee S^1$ so that each factor in $\widehat{\mathcal{O}}_i$ is a multiple of the cycle represented by $\{L^j_i\}$in $H_1(\mathcal{T}_i)$. As a result, we obtain the associated map $F_{\widehat{\mathcal{O}}}$, and $$\bar{\mu}_{123}(\mathcal{O})=\frac{1}{2}\mathscr{H}(F_{\widehat{\mathcal{O}}}).$$ Interpreting $\mathscr{H}(F_{\widehat{\mathcal{O}}})$ as the intersection number and summing up intersection numbers we conclude [\[eq:mu-in-T\]](#eq:mu-in-T){reference-type="eqref" reference="eq:mu-in-T"}. ◻
:::

 ◻
:::

In the case of Borromean flux tubes, Formula [\[eq:helicity12-flux-tubes\]](#eq:helicity12-flux-tubes){reference-type="eqref" reference="eq:helicity12-flux-tubes"} reduces to $$\label{eq:helicity12-borro-flux-tubes}
\mathsf{H}_{123}(B_1,B_2,B_3)=\bar{\mu}_{123}(L)\,\text{Flux}_{\Sigma_1}(B_1)
\text{Flux}_{\Sigma_2}(B_2)\text{Flux}_{\Sigma_3}(B_3),$$ where $\Sigma_i$ denotes homology Poincar$\acute{\rm e}$ duals to $L_i$ in $H_2(\mathcal{T}_i,\partial\mathcal{T}_i)$.

Since the fluxes are invariant under frozen-in-field deformations, Formula [\[eq:helicity12-flux-tubes\]](#eq:helicity12-flux-tubes){reference-type="eqref" reference="eq:helicity12-flux-tubes"} is yet another proof of Theorem [\[th:invariance-th\]](#th:invariance-th){reference-type="ref" reference="th:invariance-th"} in the setting of invariant unlinked handlebodies. In [@Laurence-Stredulinsky00b] the authors develop the same formula for the Borromean flux tubes. This clearly must be the case, as we work with the same topological invariants of links via a different approach. Additional advantage of our formulation is that we do not have to separately deal with null points of vector fields as in [@Laurence-Stredulinsky00b].
