---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-004-comparison-with-simplicial-volume
section_title: "Comparison with simplicial volume"
section_number: null
pages: 15-21
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.984
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2, C)."
---
[]{#s qua label="s qua"}

Here we generalize the argument used to prove Theorem [\[t vsd\]](#t vsd){reference-type="ref" reference="t vsd"} to compare ${\rm vol}(\rho)$ with the simplicial volume of $M$, obtaining exactly the expected inequality.

Let $||(\overline M,\partial \overline M)||$ be the simplicial volume of $\overline M$ relative to the boundary (see [@BP], [@G], [@Ku], [@Th1] for more details), and let $v_3$ be the volume of a regular straight ideal tetrahedron of $\ensuremath{\mathbb H}^3$.

::: teo
[]{#t sv label="t sv"} For any representation $\rho:\pi_1(M)\to$ Isom$^+(\ensuremath{\mathbb H}^3)$ we have $$|{\rm vol}(\rho)|\leq v_3\cdot||(\overline M,\partial \overline M)||.$$
:::

  For the proof we fix a representation $\rho:\pi_1(M)\to{\rm Isom}^+(\ensuremath{\mathbb H}^3)$ and a pseudo-developing map $D_\rho$ for $\rho$.

Let $c=\sum_i\lambda_i\sigma_i$ be a smooth singular chain in $\overline M$; here each simplex $\sigma_i$ is a piecewise smooth map from the standard tetrahedron $\Delta^3$ to $\overline M$. The simplicial volume of $c$ is defined as $||c||=\sum|\lambda_i|$. The relative simplicial volume of $(\overline M,\partial \overline M)$ is defined as

$$||(\overline M,\partial \overline M)||=\inf\{||c||:\, [c]=[\overline M]\in
H_3(\overline M,\partial \overline M)\}.$$

The proof has two main steps:

1.  []{#stp1 label="stp1"} Given a smooth cycle $c=\sum_i \lambda_i\sigma_i$ representing $[\overline M]$, show that ${\rm vol}(\rho)=\sum_i\int_{\Delta^3} \lambda_i
    \sigma_i^*(D_\rho^*\omega)$, where $\omega$ is the volume form of $\ensuremath{\mathbb H}^3$.

2.  []{#stp3 label="stp3"} By replacing $c$ with its straightening, show that ${\rm vol}(\rho)=\sum_i \lambda_iv_i$, where $v_i$ is the volume of a straight version of $\sigma_i$.

From Step [\[stp3\]](#stp3){reference-type="ref" reference="stp3"} it follows that $$|{\rm vol}(\rho)|\leq\sum_i|\lambda_i|\cdot|v_i|\leq v_3\cdot||c||.$$ Theorem [\[t sv\]](#t sv){reference-type="ref" reference="t sv"} follows taking to the infimum over all $c$'s representing $[\overline M]$.

1ex. Since a pseudo-developing map has the cone property on the cusps, the $3$-form $D_\rho^*\omega$ defined on $M$ extends to a $3$-form on $\overline M$ that vanishes at the boundary. So we can consider the class $[D_\rho^*\omega]\in
H^3(\overline M,\partial \overline M)$. Since $[c]=[\overline M]$, then $${\rm vol}(\rho)=\int_M D_\rho^*\omega=\langle [D_\rho^*\omega],
[\ensuremath{\overline{M}}]\rangle=\langle 
[D_\rho^*\omega],[c]\rangle=\sum_i\int_{\Delta^3}
\lambda_i\sigma_i^*(D_\rho^*\omega)
.$$

1ex. The idea is the following. Consider a lift $\ensuremath{\widetilde{c}}$ of $c$ to $\ensuremath{\widehat{\ensuremath{\widetilde{M}}}}$. Let $\ensuremath{\overline{c}}=(D_\rho)_*\ensuremath{\widetilde{c}}$ be the push-forward of $\ensuremath{\widetilde{c}}$ to $\ensuremath{\mathbb H}^3$ via $D_\rho$ and let ${\rm Str}(\ensuremath{\overline{c}})$ be a straightening of $\ensuremath{\overline{c}}$. Since the straightening is homotopic to the identity, then there exists a chain-homotopy of degree one *i.e.* a map $H$ from $k$-chains to $(k+1)$-chains such that ${\rm Str} - {\rm Id}=H\circ\partial - \partial\circ H$. Then we have $$\begin{array}{lcl}
{\rm vol}(\rho)&=&\langle D_\rho^*\omega,\ensuremath{\widetilde{c}}\rangle=
\langle\omega, (D_\rho)_*\ensuremath{\widetilde{c}}\rangle= 
\langle\omega,\ensuremath{\overline{c}}\rangle\\&=&
 \langle\omega,\textrm{Str}(\ensuremath{\overline{c}})\rangle +
\langle\omega,\partial H\ensuremath{\overline{c}}\rangle-
 \langle\omega,H\partial \ensuremath{\overline{c}}\rangle\\ &=&
\displaystyle{\sum_i}\lambda_iv_i+\langle d\omega,H\ensuremath{\overline{c}}\rangle- 
\langle\omega,H \partial \ensuremath{\overline{c}}\rangle.\end{array}$$ The last two summands are zero because $d\omega=0$ and, even if $\partial \ensuremath{\overline{c}}\neq0$, everything can be made $\rho$-equivariantly so that the action of $\rho$ cancels out in pairs the contributions of $\langle\omega,H \partial \ensuremath{\overline{c}}\rangle$.

We formalize now this argument. Let $C_k(X)$ denote the real vector space of finite singular, piecewise smooth $k$-chains in a space $X$. Consider the projection $\ensuremath{\overline{M}}\to\ensuremath{\widehat{M}}$ obtained by collapsing each boundary torus to a point. Given a relative cycle $c=\sum_i\lambda_i\sigma_i$ in $C_k(\ensuremath{\overline{M}})$ *i.e.* a chain $c$ such that $\partial c\in C_{k-1}(\partial \ensuremath{\overline{M}})$, we also call $c$ the chain induced on $C_k(\ensuremath{\widehat{M}})$ with $\partial
c\in C_k($ideal points$)$. We call $\ensuremath{\widetilde{c}}$ a lift of $c$ to $\ensuremath{\widehat{\ensuremath{\widetilde{M}}}}$, that is $\ensuremath{\widetilde{c}}=\sum_i\lambda_i\ensuremath{\widetilde{\sigma}}_i\in C_k(\ensuremath{\widehat{\ensuremath{\widetilde{M}}}})$ where each $\ensuremath{\widetilde{\sigma}}_i$ is a lift of $\sigma_i$.

::: remark
[]{#r remA label="r remA"} The chain $\ensuremath{\widetilde{c}}$ in general is not a relative cycle. Nevertheless, since $c$ is a relative cycle, assuming $\partial \ensuremath{\widetilde{c}}=\sum_jl_j\eta_j$, there exists a family $\{\alpha_j\}$ of elements of $\pi_1(M)$ such that $$\sum_jl_j\cdot\alpha_{j*}(\eta_j)\in C_k(\textrm{ideal points})$$ where $\pi_1(M)$ acts on $\ensuremath{\widetilde{M}}$ via deck transformations and $\alpha_{j*}(\eta_j)$ is the composition of $\alpha_j$ with $\eta_j$.
:::

We set $\ensuremath{\overline{\sigma}}_i=(D_{\rho})_*(\ensuremath{\widetilde{\sigma}}_i)$ and $\ensuremath{\overline{c}}=\sum_i\lambda_i\ensuremath{\overline{\sigma}}_i=(D_{\rho})_*(\ensuremath{\widetilde{c}})\in C_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$. We restrict now the class of simplices we want to use.

::: defi
We call a $k$-simplex $\sigma:\Delta^k\to\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$ *admissible* if for any sub-simplex $\eta$ of $\sigma$, if the interior of $\eta$ touches $\partial \ensuremath{\mathbb H}^3$ then $\eta$ is constant. A chain is admissible if its simplices are admissible.
:::

::: lemma
[]{#l lemB label="l lemB"} Let $c'=\sum_i\lambda_i\sigma_i'$ be a relative cycle in $C_k(\ensuremath{\overline{M}})$. Then there exists a cycle $c=\sum_i\lambda_i\sigma_i$ (with the same $\lambda_i$'s) such that $[c']=[c]\in H_k(\ensuremath{\overline{M}},\partial \ensuremath{\overline{M}})$ and such that $\ensuremath{\overline{c}}$ is admissible.
:::

  For any chain $\beta\in C_k(\ensuremath{\overline{M}})$, define span$(\beta)$ as the set of all the subsimplices of $\beta$ (of any dimension). Given the chain $c'$, construct $c$ as follows: near $\partial \ensuremath{\overline{M}}$ push $c'$ a little inside $M$, keeping fixed only the simplices of span$(\partial
c')$. This operation can be made via an homotopy, so $[c]=[c']$. Moreover, the only simplices of $c$ that touch $\partial
\ensuremath{\overline{M}}$ are the ones of span$(\partial c)$. Finally, $c$ is admissible because, if $\ensuremath{\overline{\sigma}}_i(x)\in\partial \ensuremath{\mathbb H}^3$, then from the definition of pseudo-developing map it follows that $\sigma_i(x)$ is an ideal point. Thus $x$ lies on a face $F$ of $\sigma_i$ such that the simplex $\eta=(\sigma_i)|_{F}$ belongs to ${\rm span}(\partial c)$. It follows that $\ensuremath{\widetilde{\eta}}$ is a constant map and then also $\ensuremath{\overline{\eta}}$ is constant.\

We call $\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$ the vector space of admissible chains. Note that the boundary operator is well-defined on $\oplus_k\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$ (The boundary of an admissible cycle is admissible).

::: defi
For any admissible simplex $\sigma:\Delta^k\to\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$, a straightening ${\rm Str}(\sigma):\Delta^k\to\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$ is a simplex agrees with $\sigma$ on the $0$-skeleton, moreover we require ${\rm Str}(\sigma)$ to be a standard map whose image is the convex hull of its vertices. For any chain $c=\sum_i\lambda_i\sigma_i$ a straightening of $c$ is a chain ${\rm Str}(c)=\sum_i\lambda_i{\rm Str}(\sigma_i)$.
:::

A straightening of a simplex is admissible because any straight simplex is admissible. The straightening of a simplex is not unique in general. Nevertheless, as the following lemma shows, it is possible to choose a straightening for any simplex compatibly with the boundary operator of $\oplus_k\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$.

::: lemma
There exists a chain-map ${\rm Str} :\oplus_k\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)
\to\oplus_k\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$ that maps each simplex to one of its straightenings and such that for any isometry $\gamma$ of $\ensuremath{\mathbb H}^3$, $\gamma_*\circ{\rm Str}={\rm Str} 
\circ\,\gamma_*$.
:::

  Let $K$ be the set of pairs $\{(B,f)\}$ where $B$ is a sub-space of $\oplus_k\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$ and $f:B\to\oplus_k\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$ is a linear map, such that:

-   $\partial(B)\subset B$.

-   $\forall\gamma\in{\rm Isom}(\ensuremath{\mathbb H}^3),\ \gamma_*(B)\subset B$.

-   $\forall \sigma\in B$, $f(\sigma)$ is a straightening of $\sigma$.

-   $\forall \gamma\in$ Isom$(\ensuremath{\mathbb H}^3)$, $f\circ\gamma_*=\gamma_*\circ f$.

-   $f\circ\partial=\partial\circ f$.

Note that $K$ is not empty because each $0$-simplex is admissible and it is itself its unique straightening, so that $(\ensuremath{\overline{C}}_0(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3),Id)\in K$. We order $K$ by inclusion (*i.e.* $(B,f)\prec(C,g)$ iff $B\subset C$ and $g|_{B}=f$) and use Zorn's lemma. Let $\{(B_\xi,f_\xi)\}$ be an ordered sequence in $K$. Clearly $$(B_\infty=\cup_{\xi} B_\xi,f_\infty=
\cup_{\xi} f_\xi)$$ is an upper bound for $\{(B_\xi,f_\xi)\}$. It follows that there exists a maximal element $(\ensuremath{\overline{B}},\ensuremath{\overline{f}})\in K$. We claim that $\ensuremath{\overline{B}}=\oplus_k\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$. Suppose the contrary. Let $k=\min\{n\in\ensuremath{\mathbb N}: \ensuremath{\overline{C}}_n(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)\not\subset\ensuremath{\overline{B}}\}$ and let $\sigma$ be a simplex of $\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)\setminus \ensuremath{\overline{B}}$. If $k=0$, set $B_1$ the space spanned by $\ensuremath{\overline{B}}$ and $\displaystyle{\bigcup_{\gamma\in{\rm Isom}(\ensuremath{\mathbb H})^3}
  \gamma_*(\sigma)}$, define $\ensuremath{\overline{f}}(\sigma)=\sigma$, $\ensuremath{\overline{f}}(\gamma_* (\sigma))=\gamma_*(\ensuremath{\overline{f}}(\sigma))$ and extend $\ensuremath{\overline{f}}$ on $B_1$ by linearity. Then $$(\ensuremath{\overline{B}},\ensuremath{\overline{f}})\prec(B_1,\ensuremath{\overline{f}})$$ contradicting the maximality of $(\ensuremath{\overline{B}},\ensuremath{\overline{f}})$. If $k>0$, then $\ensuremath{\overline{f}}$ is defined on $\partial\sigma$ and, as $\ensuremath{\overline{f}}(\partial \sigma)$ is standard, it is not hard to show that it extends to a standard map $\ensuremath{\overline{f}}(\sigma)$ defined on the whole $\Delta^k$. Then define $B_1$ and extend $\ensuremath{\overline{f}}$ to $B_1$ as above. Again we have $(\ensuremath{\overline{B}},\ensuremath{\overline{f}})\prec(B_1,\ensuremath{\overline{f}})$, that contradicts the maximality of $(\ensuremath{\overline{B}},\ensuremath{\overline{f}})$.

Thus $\ensuremath{\overline{B}}=\oplus_k\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$ and $\ensuremath{\overline{f}}$ is the requested chain map Str.\

::: lemma
[]{#l lemC label="l lemC"} There exists a homotopy operator $H:\oplus_k\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)\to\oplus_k\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$ between Str and the identity such that $H\circ\gamma_*=\gamma_*\circ H$ for any isometry $\gamma$ of $\ensuremath{\mathbb H}^3$.
:::

  A homotopy operator between ${\rm Str}$ and ${\rm Id}$ is a chain map of degree $1$, *i.e.* a map $H:\ensuremath{\overline{C}}_k(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)\to \ensuremath{\overline{C}}_{k+1}(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$, such that $$\textrm{Str} -Id =\partial \circ H- H\circ\partial.$$ For any admissible $\sigma:\Delta^k\to\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$, let $h_\sigma(t,x)$ be the homotopy constructed as follows: $h_\sigma(t,x)$ is the convex combination from $\sigma(x)$ to ${\rm Str}(\sigma)(x)$ if $\sigma(x)\notin\partial
\ensuremath{\mathbb H}^3$ and $h_\sigma(t,x)=\sigma(x)$ otherwise. Note that from the admissibility of $\sigma$ it follows that $h_\sigma(\infty,x)={\rm
  Str}(\sigma)(x)$ for any $x$. So the $h_\sigma$ actually is a homotopy between $\sigma$ and ${\rm
  Str}(\sigma)$.

As $h_\sigma$ is a map $h_\sigma:\Delta^k\times[0,\infty]\to\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$, up to triangulating $\Delta^k\times[0,\infty]$, it is a chain in $C_{k+1}(\ensuremath{\overline{\ensuremath{\mathbb H}}}^3)$. Fix a canonical triangulation of $\Delta^k\times[0,\infty]$ and define $H(\sigma)$ as $h_\sigma$. Since $$\partial(\Delta^k\times[0,\infty])=
\Delta^k\times\{\infty\}- 
\Delta^k\times\{0\}+
\partial\Delta^k\times[0,\infty]$$ then $\partial \circ H={\rm Str}- Id+H\circ\partial$.

Since $h_\sigma$ is constructed using geodesic rays, then for every isometry $\gamma$ we have $h_{\gamma\circ\sigma}=\gamma\circ h_\sigma$. It follows that $H\circ\gamma_*= \gamma_*\circ H$.

Finally, admissibility of $h_\sigma$ follows from admissibility of $\sigma$.\

::: lemma
[]{#l lemD label="l lemD"} Let $c=\sum_i\lambda_i\sigma_i$ be a chain in $C_k(\ensuremath{\overline{M}})$. Let $\{\gamma_j\}$ be a finite set of isometries and let $A$ be the hyperbolic convex hull in $\ensuremath{\mathbb H}^3$ of $$\bigcup_{i,j} \gamma_j({\rm Im}(\ensuremath{\overline{\sigma}}_i)).$$ Then $A$ has finite volume.
:::

  Since $D_\rho$ has the cone property on the cusps and since $c$ is a finite sum of simplices, then $A$ is contained in a geodesic polyhedron with a finite number of vertices, and such a polyhedron has finite volume.\

We are now ready to complete the proof of Theorem [\[t sv\]](#t sv){reference-type="ref" reference="t sv"}. Let $c=\sum_i\lambda_i\sigma_i$ be a relative cycle in $C_3(\ensuremath{\overline{M}})$ such that $[c]=[\ensuremath{\overline{M}}]$ in $H_3(\ensuremath{\overline{M}},\partial \ensuremath{\overline{M}})$. By Lemma [\[l lemB\]](#l lemB){reference-type="ref" reference="l lemB"} we can suppose that $c$ is admissible. Assume $\partial \ensuremath{\widetilde{c}}=\sum_jl_j\eta_j$. By Remark [\[r remA\]](#r remA){reference-type="ref" reference="r remA"}, there exists a finite set $\{\alpha_j\}\subset\pi_1(M)$ such that $\sum_jl_j\cdot\alpha_{j_*}\eta_j\in C_2($ideal points$)$.

Let $A$ be as in Lemma [\[l lemD\]](#l lemD){reference-type="ref" reference="l lemD"}, where we use $\{\rho(\alpha_j)\}\cup\{{\rm Id}\}$ as the set of isometries. Since $A$ has finite volume, then the volume form $\omega$ of $\ensuremath{\mathbb H}^3$ is an element of $H^3(A)$. Moreover, the straightening of any admissible simplex in $\ensuremath{\overline{C}}_k(A)$ is contained in $\ensuremath{\overline{C}}_k(A)$ and, since the homotopy operator $H$ is constructed using convex combinations, then $H$ is well-defined on $\oplus_k\ensuremath{\overline{C}}_k(A)$. Called $v_i$ the volume of the straight version of $\sigma_i$, we have $$\begin{array}{lcl}
{\rm vol}(\rho)&=&\langle D_\rho^*\omega,\ensuremath{\widetilde{c}}\rangle =
\langle\omega,(D_\rho)_*(\ensuremath{\widetilde{c}})\rangle =
\langle\omega,\ensuremath{\overline{c}}\rangle\\
&=& \langle\omega,\textrm{Str}\ensuremath{\overline{c}}\rangle+ \langle\omega,H\partial\ensuremath{\overline{c}}\rangle- \langle\omega,\partial H \ensuremath{\overline{c}}\rangle\\
&=&
\sum_i\lambda_iv_i+\langle\omega,H\partial \ensuremath{\overline{c}}\rangle- \langle d\omega,H\ensuremath{\overline{c}}\rangle=\sum_i\lambda_iv_i+\langle\omega,H\partial \ensuremath{\overline{c}}\rangle
\end{array}$$ By Lemma [\[l lemC\]](#l lemC){reference-type="ref" reference="l lemC"} we have $\rho(\alpha_j)_*H=H\rho(\alpha_j)_*$. Moreover, the volume form is invariant by isometries. It follows that $$\begin{array}{lcl}
\langle\omega,H\partial \ensuremath{\overline{c}}\rangle&=&
\langle\omega,H\sum_jl_j(D_\rho)_*\eta_j\rangle=
\sum_jl_j\langle\omega,H(D_\rho)_*\eta_j\rangle\\
&=&
\sum_jl_j\langle\rho(\alpha_j)^*\omega,H(D_\rho)_*\eta_j\rangle=
\sum_jl_j\langle \omega,\rho(\alpha_j)_*H(D_\rho)_*\eta_j\rangle\\
&=&
\sum_jl_j\langle \omega,H\rho(\alpha_j)_*(D_\rho)_*\eta_j\rangle
=\sum_jl_j\langle \omega,H(D_\rho)_*\alpha_{j*}\eta_j\rangle\\&=&
\langle \omega,H(D_\rho)_*\sum_jl_j\alpha_{j*}\eta_j\rangle.
\end{array}$$ The last product is zero because $D_{\rho*}\sum_jl_j\alpha_{j*}\eta_j$ lies on the ideal points of $A$, where $H$ is fixed and $\omega$ vanishes.

This completes the proof of Theorem [\[t sv\]](#t sv){reference-type="ref" reference="t sv"}.\

::: remark
[]{#r difp label="r difp"} Theorem [\[t sv\]](#t sv){reference-type="ref" reference="t sv"} applies when the cycle $c$ is an ideal triangulation. So it implies Theorem [\[t vsd\]](#t vsd){reference-type="ref" reference="t vsd"}.
:::

::: cor
[]{#c vg label="c vg"} Let $M$ be a graph $3$-manifold. Then for all representations $\rho:\pi_1(M)\to{\rm Isom}^+(\ensuremath{\mathbb H}^3)$ we have ${\rm vol}(\rho)=0$.
:::

 This is because for each graph manifold $M$ we have $||(M,\partial M)||=0$ (see [@G], [@Ku]).\

::: cor
[]{#c df label="c df"} Let $M$ be a complete hyperbolic $3$-manifold of finite volume. Then for all representations $\rho:\pi_1(M)\to{\rm Isom}^+(\ensuremath{\mathbb H}^3)$ we have $|{\rm vol}(\rho)|\leq$ ${\rm vol}(M)$.
:::

 This follows from the fact that for complete hyperbolic $3$-manifold we have ${\rm vol}(M)=v_3||(M,\partial M)||$ (see [@G], [@Ku]).\

In [@D] it is proved that, for compact manifolds, equality holds if and only if $\rho$ is discrete and faithful. In the next section we show that this is true in general for manifolds of finite volume.
