---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-026-65-a-formal-diffusion-operator-and-the-character
section_title: "A formal diffusion operator and the characterization of negligible amplitudes"
section_number: 6.5
pages: 16-18
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.954
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
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
