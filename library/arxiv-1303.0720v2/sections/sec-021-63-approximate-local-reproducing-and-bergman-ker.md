---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-021-63-approximate-local-reproducing-and-bergman-ker
section_title: "Approximate local reproducing and Bergman kernels"
section_number: 6.3
pages: 14-18
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.968
---
[]{#subsec-5.3 label="subsec-5.3"} In [@bbs], the point of departure is an approximate reproducing identity for functions in $\mathrm{A}^2_m$. To state the result, we define the kernel $$M_m(z,w) := \frac{2m}{\pi} \mathrm{e}^{2mQ(z,w)}\bar\partial_w\theta(z,w).
\label{eq-Mm}$$ This kernel is for obvious reasons only defined in some fixed neighborhood of the diagonal. We shall be concerned with the (small) bidisk ${\mathbb D}(z_0,r)\times{\mathbb D}(z_0,r)$ where $M_m(z,w)$ is well-defined, by our assumptions (A:i)--(A:iv) above.To extend the kernel beyond the bidisk, we multiply by a smooth cut-off function $\chi_0(w)$, and think of the product as $0$ off the support of $\chi_0$ (also where $M_m(z,w)$ is undefined). The function $\chi_0(w)$ is $C^\infty$-smooth with $0\le\chi_0\le1$ throughout ${\mathbb C}$, and vanishes off ${\mathbb D}(z_0,\frac34r)$, while it has $\chi_0=1$ on $\mathbb{D}(z_0, \frac23 r)$, and is a function of the distance $|w-z_0|$. We ask in addition that the norm $\|\bar\partial\chi_0\|_{L^2(\Omega)}$ is bounded by an absolute constant, which is possible to achieve. We will use the simplified notation $$\|u\|_{m}:=\|u\|_{L^2(\Omega,\mathrm{e}^{-2mQ})}=\bigg\{\int_\Omega|u|^2\mathrm{e}^{-2mQ}
\mathrm{d}A\bigg\}^{1/2}.
\label{eq-norm1}$$

::: prop
[]{#negliprop label="negliprop"} We have that for all $u\in\mathrm{A}^2_m$, $$u(z)=\int_{\Omega}u(w)\chi_0(w)M_m(z,w)\,\mathrm{e}^{-2mQ(w)}\mathrm{d}A(w) 
+\mathrm{O}(r^{-1}\|u\|_{m} \mathrm{e}^{mQ(z)-m\delta_0}),
\qquad z\in \mathbb{D}(z_0,\tfrac13 r),$$ where we write $\delta_0:=\frac{1}{18}r^2\epsilon_0>0$. The implied constant is absolute.
:::

To develop the necessary intuition, we supply the easy proof.

::: proof
*Proof of Proposition [\[negliprop\]](#negliprop){reference-type="ref" reference="negliprop"}.* Since the Cauchy kernel $1/(\pi z)$ is the fundamental solution to $\bar\partial$, we have by Cauchy-Green theorem (i.e., integration by parts) that $$\begin{gathered}
u(z) =\chi_0(z)u(z)=\int_{\Omega} \frac{1}{\pi(z-w)} \bar \partial_w \Big( u(w) 
\chi_0(w)\,\mathrm{e}^{2m(z-w)\theta(z,w)} \Big) \mathrm{d}A(w) 
\\
= \int_{\Omega} u(w) \chi_0(w) M_m(z,w) \,\mathrm{e}^{-2mQ(w)} \mathrm{d}A(w)  
\\
+ \frac{1}{\pi}\int_{\Omega} u(w) \frac{ \bar \partial_w \chi_0(w)}{z-w}
\mathrm{e}^{2m(z-w) \theta(z,w)}\mathrm{d}A(w),\qquad z\in{\mathbb D}(z_0,\tfrac13 r).
\label{reproeq1}
\end{gathered}$$ It will be enough to show that the last term on the right-hand side of [\[reproeq1\]](#reproeq1){reference-type="eqref" reference="reproeq1"} (the one which involves $\bar \partial_w \chi$) belongs to the error term. By [\[Qtaylor2\]](#Qtaylor2){reference-type="eqref" reference="Qtaylor2"} and the Cauchy-Schwarz inequality, we have that $$\begin{gathered}
\frac{1}{\pi}\int_{\Omega}\bigg|u(w) \frac{\bar\partial_w \chi_0(w)}{z-w}
\mathrm{e}^{2m(z-w)\theta}  \bigg|\mathrm{d}A(w) 
\leq  
\int_{\Omega} \bigg| u(w) \frac{\bar\partial_w \chi_0(w)}{z-w}\bigg| 
\,\mathrm{e}^{mQ(z)- mQ(w)- \frac12 m \varDelta Q(z) |w-z|^2} \mathrm{d}A(w) 
\\
\leq \|u\|_{m}\mathrm{e}^{mQ(z)} 
\bigg\{\int_{\Omega}\bigg|\frac{\bar\partial_w\chi_0(w)}{z-w} 
\bigg|^2 
\mathrm{e}^{-m\varDelta Q(z)|w-z|^2} \mathrm{d}A(w) \bigg\}^{1/2} 

\leq \frac{3}{r}\|\bar\partial\chi_0\|_{L^2(\Omega)} \|u\|_{m}
\mathrm{e}^{mQ(z)}\mathrm{e}^{-\frac{1}{18}m r^2\varDelta Q(z)}, 
\end{gathered}$$ again for $z\in{\mathbb D}(z_0,\frac13 r)$, and the desired conclusion is immediate. ◻
:::

We will interpret Proposition [\[negliprop\]](#negliprop){reference-type="ref" reference="negliprop"} as saying that the function $M_m(z,w)$ is an local reproducing kernel $\text{mod}(\mathrm{e}^{-\delta m})$, with $\delta=\delta_0>0$. More generally, a function $L_m(z,w)$ defined on ${\mathbb D}(z_0,r)$ and holomorphic in $z$ is a *a local reproducing kernel* $\text{mod}(\mathrm{e}^{-\delta m})$ if $$u(z)=\int_{\Omega}u(w)\chi_0(w)L_m(z,w)\,\mathrm{e}^{-2mQ(w)}\mathrm{d}A(w) 
+\mathrm{O}(\| u \|_{m} \mathrm{e}^{mQ(z)-m\delta}),
\qquad z\in \mathbb{D}(z_0,\tfrac13 r),$$ holds for large $m$ and all $u\in\mathrm{A}^2_m$. Here and in the sequel, it is implicit that $\delta$ should be positive. Analogously, a function $L_m(z,w)$ defined on ${\mathbb D}(z_0,r)$ and holomorphic in $z$ is a *a local reproducing kernel* $\text{mod}(m^{-k})$ if $$u(z)=\int_{\Omega}u(w)\chi_0(w)L_m(z,w)\,\mathrm{e}^{-2mQ(w)}\mathrm{d}A(w) 
+\mathrm{O}(\| u \|_{m} m^{-k}\mathrm{e}^{mQ(z)}),
\qquad z\in \mathbb{D}(z_0,\tfrac13 r),$$ holds for large $m$ and all $u\in\mathrm{A}^2_m$. We speak of *approximate local reproducing kernels* when it is implicit which of the above senses applies. The Bergman kernel $K_m(z,w)$ is of course an approximate local reproducing kernel in the above sense (no error term!), and it has the additional property of being holomorphic in $\bar w$. This suggests the term *approximate local Bergman kernel* for an approximate local reproducing kernel, which is holomorphic in $\bar w$. Starting with the local reproducing kernel $M_m$, Berman, Berndtsson, and Sjöstrand supply an algorithm to correct $M_m$ and obtain as a result an approximate local Bergman kernel $\text{mod} (m^{-k})$ for any given positive integer $k$. It is a nontrivial step -- which actually requires additional assumptions on the potential $Q$ -- to show that the approximate local Bergman kernels obtained algorithmically in this fashion are indeed close to the Bergman kernel $K_m$ near the diagonal. This is achieved by an argument based on Hörmander's $L^2$-estimates for the $\bar\partial$-operator. In this section, we only present the corrective algorithm.

## A differential operator and negligible amplitudes

The corrective algorithm involves the differential operator $$\boldsymbol{\nabla}:= 
\frac{1}{\bar\partial_w\theta} \bar \partial_w + 2m{\mathbf M}_{z-w}
\label{nabladef}$$ and a (formal) diffusion operator ${\mathbf S}$ which will be described in detail later on. In [\[nabladef\]](#nabladef){reference-type="eqref" reference="nabladef"} and more generally in the sequel, ${\mathbf M}$ with a subscript stands for the operator of multiplication by the function in the subscript. The differential operator $\boldsymbol{\nabla}$ has the property that for smooth functions $A$ on ${\mathbb D}(z_0,r)\times{\mathbb D}(z_0,r)$, $$\frac{1}{\bar\partial_w\theta}
\bar\partial_w \big\{ A(z,w) \,\mathrm{e}^{2m(z-w) \theta(z,w)} \big\}
=\mathrm{e}^{2m(z-w) \theta(z,w)}\boldsymbol{\nabla}A(z,w),
\label{eq-fundid0}$$ which we may express in the more abstract (intertwining) form $${\mathbf M}_{\bar\partial_w\theta}
\boldsymbol{\nabla}={\mathbf M}_{\mathrm{e}^{-2m(z-w)\theta}}\bar\partial_w {\mathbf M}_{\mathrm{e}^{2m(z-w)\theta}}.
\label{eq-fundid0.1}$$ It follows from [\[eq-fundid0\]](#eq-fundid0){reference-type="eqref" reference="eq-fundid0"} that if $u$ is a holomorphic function on ${\mathbb D}(z_0,r)$, then $$\begin{gathered}
\label{nablanegli}
\int_{\Omega} u(w) \chi_0(w) [\bar\partial_w \theta(z,w)] 
[\boldsymbol{\nabla}A(z,w)]\, \mathrm{e}^{2m(z-w) \theta(z,w)} \mathrm{d}A(w) 
\\
= \int_{\Omega} u(w) \chi_0(w) \bar \partial_w 
\big\{ A(z,w) \,\mathrm{e}^{2m(z-w)\theta(z,w)} \big\} \mathrm{d}A(w) 
=\int_{\Omega} u(w) A(z,w) \,\mathrm{e}^{2m(z-w)\theta(z,w)} \bar\partial\chi_0(w)\mathrm{d}A(w) 
\end{gathered}$$ which we may estimate using [\[Qtaylor2\]](#Qtaylor2){reference-type="eqref" reference="Qtaylor2"}: $$\begin{gathered}
\label{nablanegli1.1}
\bigg|\int_{\Omega} u(w) \chi_0(w) [\bar\partial_w \theta(z,w)] 
[\boldsymbol{\nabla}A(z,w)]\, \mathrm{e}^{2m(z-w) \theta(z,w)} \mathrm{d}A(w) \bigg|
\\
\le
\mathrm{e}^{mQ(z)-\delta_0m}\int_{\Omega} |u(w) A(z,w)| \,\mathrm{e}^{-mQ(w)}|\bar\partial\chi_0(w)|\mathrm{d}A(w) 
\\
\le\mathrm{e}^{mQ(z)-\delta_0m}\|A\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\|u\|_m
\|\bar\partial\chi_0\|_{L^2(\Omega)} =
\mathrm{O}\big(\mathrm{e}^{mQ(z)-\delta_0m}\|A\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\|u\|_m\big),
\qquad z\in{\mathbb D}(z_0,\tfrac13r),
\end{gathered}$$ where the implied constant is absolute. Here, $\delta_0=\frac{1}{18}r^2\epsilon_0$ as before, and the norm of $A$ is the supremum norm on the bidisk ${\mathbb D}(z_0,\tfrac34r)^2=
{\mathbb D}(z_0,\tfrac34r)\times{\mathbb D}(z_0,\tfrac34r)$. Compared with the typical size $\mathrm{O}(\mathrm{e}^{mQ(z)})$, this means that we have exponential decay in $m$.

For this reason functions of the form ${\mathbf M}_{\bar\partial_w\theta}
\boldsymbol{\nabla}A$ are called *negligible amplitudes*.

## A formal diffusion operator and the characterization of negligible amplitudes

Next, to define the diffusion operator ${\mathbf S}$, we need the two differential operators $${{\pmb{\partial}}}_w=\partial_w-\frac{\partial_w\theta}{\bar\partial_{w}\theta}
\bar\partial_{w},\qquad
{\pmb{\partial}}_\theta=
\frac{1}{\bar\partial_{w}\theta}\bar\partial_{w}.
\label{eq-coordch1}$$ These operators come from the change of variables $(z,w, \bar w) \to (z, w, \theta)$, but this is of no real significance to us here. What is, however, important is the property that they commute (${\pmb{\partial}}_w{\pmb{\partial}}_\theta={\pmb{\partial}}_\theta{\pmb{\partial}}_w$), and the formula for the commutator of ${\pmb{\partial}}_w$ and ${\mathbf M}_{z-w}$ (see [\[eq-commutator1\]](#eq-commutator1){reference-type="eqref" reference="eq-commutator1"} below). In terms of the above differential operators, $\boldsymbol{\nabla}$ simplifies: $$\boldsymbol{\nabla}={\pmb{\partial}}_\theta+2m{\mathbf M}_{z-w}.
\label{nabladef1.1}$$ The diffusion operator ${\mathbf S}$ is defined (rather formally) by $${\mathbf S}:= \mathrm{e}^{(2m)^{-1} {\pmb{\partial}}_w {\pmb{\partial}}_\theta} = \sum_{j=0}^{\infty} 
\frac{1}{j!(2m)^j}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^j .  
\label{Sdef}$$ The relation with diffusion comes from thinking about ${\pmb{\partial}}_w {\pmb{\partial}}_\theta$ as a generalized Laplacian, so that ${\mathbf S}$ is the $1/(2m)$ forward time step for the corresponding generalized diffusion (or heat) equation. Our analysis will not require the series expansion [\[Sdef\]](#Sdef){reference-type="eqref" reference="Sdef"} to converge in any meaningful way. It is supposed to act on asymptotic expansions of the type $$a(z,w) \sim m a_0(z,w) + a_1(z,w) + m^{-1} a_{2}(z,w)+ m^{-2} a_{3}(z,w)+\ldots,
\label{eq-asseries1}$$ in the obvious fashion. Here, the functions $a_j(z,w)$ are assumed not to depend on the parameter $m$. As for the meaning of an asymptotic expansion like [\[eq-asseries1\]](#eq-asseries1){reference-type="eqref" reference="eq-asseries1"}, we should require that $$a(z,w)=\sum_{j=0}^{k} m^{-j+1} a_j(z,w)+\mathrm{O}(m^{-k}).$$

Actually, we may even think that the left hand side represents the right-hand side more abstractly in the sense of the *abschnitts* (partial sums) $$a^{\langle k\rangle}(z,w)=\sum_{j=0}^{k} m^{-j+1} a_j(z,w),$$ so that $a(z,w)$ need not be a well-defined function, it would just be a stand-in for the sequence of abschnitts $a^{\langle k\rangle}(z,w)$, $k=1,2,3,\ldots$. In this sense, the meaning of ${\mathbf S}a$ clarifies completely. We observe from the way ${\mathbf S}$ is defined that $$^{\langle k\rangle}=
[{\mathbf S}a]^{\langle k\rangle}.
\label{eq-abschn1}$$ and likewise for its inverse $$^{\langle k\rangle}=
[{\mathbf S}^{-1} a]^{\langle k\rangle}.
\label{eq-abschn2}$$ Here, the inverse operator ${\mathbf S}^{-1}$ is given by the (rather formal) expansion $${\mathbf S}^{-1}:=\mathrm{e}^{-(2m)^{-1} {\pmb{\partial}}_w {\pmb{\partial}}_\theta} =\sum_{j=0}^{\infty} 
\frac{(-1)^j}{j!(2m)^j}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^j .  
\label{Sdefinv}$$

The important property of ${\mathbf S}$, which is verified by a simple algebraic computation, is that $${\mathbf S}\boldsymbol{\nabla}= 2m{\mathbf M}_{z-w}{\mathbf S}. 
\label{Snabla}$$ We include the calculation which gives [\[Snabla\]](#Snabla){reference-type="eqref" reference="Snabla"}, as it is elegant and quite simple. First, we note that $${\pmb{\partial}}_w^j{\mathbf M}_{z-w}{\pmb{\partial}}_{\theta}^j
=-j\,{\pmb{\partial}}_\theta({\pmb{\partial}}_\theta{\pmb{\partial}}_w)^{j-1}+{\mathbf M}_{z-w}({\pmb{\partial}}_\theta{\pmb{\partial}}_w)^j,
\qquad j=1,2,3,\ldots,$$ which follows from the calculation $${\pmb{\partial}}_w^j{\mathbf M}_{z-w}=-j\,{\pmb{\partial}}_w^{j-1}+{\mathbf M}_{z-w}{\pmb{\partial}}_w^j,\qquad
j=1,2,3,\ldots.
\label{eq-commutator1}$$ Finally, we expand ${\mathbf S}\boldsymbol{\nabla}$: $$\begin{gathered}
{\mathbf S}\boldsymbol{\nabla}=\mathrm{e}^{(2m)^{-1}{\pmb{\partial}}_\theta{\pmb{\partial}}_w}\boldsymbol{\nabla}
=\mathrm{e}^{(2m)^{-1}\,{\pmb{\partial}}_\theta{\pmb{\partial}}_w}({\pmb{\partial}}_{\theta}+2m{\mathbf M}_{z-w})\\
=\sum_{j=0}^{+\infty}\frac{1}{j!(2m)^j}\,{\pmb{\partial}}_w^j{\pmb{\partial}}_\theta^j({\pmb{\partial}}_{\theta}
+2m{\mathbf M}_{z-w})
={\pmb{\partial}}_{\theta}\,\mathrm{e}^{(2m)^{-1}{\pmb{\partial}}_\theta{\pmb{\partial}}_w}+
\sum_{j=0}^{+\infty}\frac{1}{j!(2m)^{j-1}}\,
{\pmb{\partial}}_w^j\,{\mathbf M}_{z-w}\,{\pmb{\partial}}_{\theta}^j
\\
={\pmb{\partial}}_\theta\,\mathrm{e}^{(2m)^{-1}{\pmb{\partial}}_\theta{\pmb{\partial}}_w}
-\sum_{j=1}^{+\infty}\frac{1}{(j-1)!(2m)^{j-1}}\,
{\pmb{\partial}}_\theta({\pmb{\partial}}_\theta{\pmb{\partial}}_w)^{j-1}
+\sum_{j=1}^{+\infty}\frac{1}{j!(2m)^{j-1}}\,{\mathbf M}_{z-w}({\pmb{\partial}}_\theta{\pmb{\partial}}_w)^{j}
\\
=2m{\mathbf M}_{z-w}\,\mathrm{e}^{m^{-1}{\pmb{\partial}}_\theta{\pmb{\partial}}_w}=2m{\mathbf M}_{z-w}{\mathbf S},
\end{gathered}$$ as needed.

The reason why we consider the diffusion operator ${\mathbf S}$ is outlined in the following proposition (see [@bbs]). As for notation, let ${\mathfrak R}_1$ denote the algebra of all functions $f(z,w)$ that are holomorphic in $z$ and $C^\infty$-smooth in $w$ (near the diagonal $z=w$).

::: prop
Fix an integer $k=1,2,3\ldots$. Suppose $a(z,w)$ has the asymptotic expansion [\[eq-asseries1\]](#eq-asseries1){reference-type="eqref" reference="eq-asseries1"}, i.e., $a\sim m a_0 + a_1 +m^{-1}a_{2}+m^{-2}a_3+\ldots$, where the functions $a_j\in{\mathfrak R}_1$ are all independent of $m$. Then the following are equivalent:

We have that

$$[{\mathbf S}a]^{\langle k\rangle} \in{\mathbf M}_{z-w}{\mathfrak R}_1.$$ We have that

$$a^{\langle k\rangle} = [\boldsymbol{\nabla}A]^{\langle k\rangle},$$ for some function $A(z,w) = \sum_{j=0}^{k} m^{-j} A_j(z,w)$, where each $a_j\in{\mathfrak R}_1$ is independent of $m$.

[]{#prop-neglampl1 label="prop-neglampl1"}
:::

::: proof
*Proof.* Suppose first that (ii) holds. Then, by [\[eq-abschn1\]](#eq-abschn1){reference-type="eqref" reference="eq-abschn1"} and [\[Snabla\]](#Snabla){reference-type="eqref" reference="Snabla"}, we have that $$^{\langle k\rangle}=[{\mathbf S}a^{\langle k\rangle}]^{\langle k\rangle}
= [{\mathbf S}[\boldsymbol{\nabla}A]^{\langle k\rangle}]^{\langle k\rangle}
=[{\mathbf S}\boldsymbol{\nabla}A]^{\langle k\rangle}={\mathbf M}_{z-w}[2m{\mathbf S}A]
^{\langle k\rangle}=2m{\mathbf M}_{z-w}[{\mathbf S}A]^{\langle k+1\rangle},  
\label{eq-calc1}$$ and (i) follows.

Next, we suppose instead that (i) holds, so that $[{\mathbf S}a]^{\langle k\rangle}=
{\mathbf M}_{z-w}\alpha$ for some function $\alpha(z,w)=\sum_{j=0}^{k}m^{1-j}
\alpha_j(z,w)$, where the $\alpha_j(z,w)$ are independent of $m$, and holomorphic in $z$ and $C^\infty$-smooth in $w$ near the diagonal $z=w$. We would like to find an $A$ of the form prescribed by (ii). In view of the calculation [\[eq-calc1\]](#eq-calc1){reference-type="eqref" reference="eq-calc1"}, it is clear that if $A$ can be found, then we must have $\alpha=[2m{\mathbf S}A]^{\langle k\rangle}=
2m[{\mathbf S}A]^{\langle k+1\rangle}$. Finally, by [\[eq-abschn2\]](#eq-abschn2){reference-type="eqref" reference="eq-abschn2"}, we realize that $A=(2m)^{-1}[{\mathbf S}^{-1}\alpha]^{\langle k\rangle}$. Finally, we plug in $A:=(2m)^{-1}[{\mathbf S}^{-1}\alpha]^{\langle k\rangle}$ and check that it is of the right form, with $[\boldsymbol{\nabla}A]^{\langle k\rangle}=a^{\langle k\rangle}$.

Indeed, we see by applying ${\mathbf S}^{-1}$ from the left and the right on both sides of [\[Snabla\]](#Snabla){reference-type="eqref" reference="Snabla"} using [\[eq-abschn1\]](#eq-abschn1){reference-type="eqref" reference="eq-abschn1"} and [\[eq-abschn2\]](#eq-abschn2){reference-type="eqref" reference="eq-abschn2"} that $$\boldsymbol{\nabla}{\mathbf S}^{-1} = 2m{\mathbf S}^{-1}{\mathbf M}_{z-w}, 
\label{Snabla3}$$ so that $$[\boldsymbol{\nabla}A]^{\langle k\rangle}=
[(2m)^{-1}\boldsymbol{\nabla}{\mathbf S}^{-1}\alpha]^{\langle k\rangle}
=[{\mathbf S}^{-1}{\mathbf M}_{z-w}\alpha]^{\langle k\rangle}=[{\mathbf S}^{-1}{\mathbf S}a]^{\langle k\rangle}
=a^{\langle k\rangle},$$ as needed. ◻
:::
