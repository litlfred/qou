---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-033-75-the-characterization-of-bi-negligible-amplitu
section_title: "The characterization of bi-negligible amplitudes"
section_number: 7.5
pages: 23-24
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.96
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We need to find the bianalytic analogue of Proposition [\[prop-neglampl1\]](#prop-neglampl1){reference-type="ref" reference="prop-neglampl1"}, so that we can tell when we have a bi-negligible amplitude. To formulate the criterion, we first need to define the operator ${\mathbf N}$. We note that a function $f\in{\mathfrak R}_2$ has a unique decomposition $f(z,w)=f_1(z,w)+\bar z f_2(z,w)$, where $f_1$ and $f_2$ are holomorphic in in $z$ and $C^\infty$-smooth in $w$ (near the diagonal $z=w$). For such $f\in{\mathfrak R}_2$, we put $${\mathbf N}[f](z,w):=\frac{f_1(z,w)-f_1(w, w)}{z-w}+\bar z\,
\frac{f_2(z,w)-f_2(w, w)}{z-w}.$$ Then ${\mathbf N}{\mathbf M}_{z-w}$ is the identity operator. Second, we need the (formal) operator ${\mathbf S}'$ given by $${\mathbf S}' : = {\mathbf S}{\mathbf M}^{-1}_{\bar \partial_w \theta} {\mathbf S}^{-1} {\mathbf N}{\mathbf S}.  
\label{eq-defS'}$$

::: prop
[]{#binegliprop label="binegliprop"} Fix an integer $k=1,2,3,\ldots$. Suppose $a$ has an asymptotic expansion $a\sim m^2 a_0+m a_1+a_2+m^{-1}a_3
+\ldots$, where the functions $a_j\in{\mathfrak R}_2$ are all independent of $m$. Then the following are equivalent:

There exist two finite asymptotic expansions $\alpha=m^2\alpha_0+m\alpha_1+\alpha_2+\cdots+
m^{-k+1}\alpha_{k+1}$ and $\alpha'=m^2\alpha'_0+m\alpha'_1+\alpha_2'+\cdots+
m^{-k+1}\alpha'_{k+1}$, where each $\alpha_j,\alpha_j'\in{\mathfrak R}_2$ is independent of $m$, such that $[{\mathbf S}a]^{\langle k\rangle}={\mathbf M}_{z-w}\alpha$ and $[{\mathbf S}' a]^{\langle k\rangle}={\mathbf M}_{z-w}\alpha'(z,w)$.

There exists an asymptotic expansion $A\sim A_0+m^{-1}A_1+m^{-2}A_2+\ldots$, with $A_j\in{\mathfrak R}_2$ independent of $m$, such that $$a^{\langle k\rangle}=[\boldsymbol{\nabla}{\mathbf M}_{\bar \partial_w \theta}\boldsymbol{\nabla}A]
^{\langle k\rangle}.$$
:::

::: proof
*Proof.* We first show the implication $\mathrm{(i)}\Rightarrow\mathrm{(ii)}$. We recall the abschnitt properties [\[eq-abschn1\]](#eq-abschn1){reference-type="eqref" reference="eq-abschn1"} and [\[eq-abschn2\]](#eq-abschn2){reference-type="eqref" reference="eq-abschn2"}, which will be used repeatedly. We put $\beta:=[{\mathbf S}^{-1}\alpha]^{\langle k\rangle}$, to obtain $$^{\langle k\rangle}={\mathbf M}_{z-w}\alpha=[{\mathbf M}_{z-w}{\mathbf S}\beta]^{\langle k\rangle}, 
\label{bianaleq1}$$ and, consequently, by [\[Snabla\]](#Snabla){reference-type="eqref" reference="Snabla"}, we have $$a^{\langle k\rangle} = [{\mathbf S}^{-1}{\mathbf M}_{z-w}{\mathbf S}\beta]^{\langle k\rangle} 
= [(2m)^{-1}\boldsymbol{\nabla}\beta]^{\langle k\rangle}.

\label{bianaleq2}$$ Moreover, we see from [\[bianaleq1\]](#bianaleq1){reference-type="eqref" reference="bianaleq1"} and the definition [\[eq-defS\'\]](#eq-defS'){reference-type="eqref" reference="eq-defS'"} of ${\mathbf S}'$ that $$^{\langle k\rangle} = 
[{\mathbf S}{\mathbf M}^{-1}_{\bar \partial_w \theta} {\mathbf S}^{-1} {\mathbf N}{\mathbf S}a]^{\langle k\rangle} 
=[{\mathbf S}{\mathbf M}^{-1}_{\bar\partial_w\theta}{\mathbf S}^{-1}{\mathbf N}{\mathbf M}_{z-w}{\mathbf S}\beta]^{\langle k\rangle}

=[{\mathbf S}{\mathbf M}^{-1}_{\bar\partial_w\theta}\beta]^{\langle k\rangle}, 
\label{eq-6.5.5}$$ where we used that ${\mathbf N}{\mathbf M}_{z-w}$ is the identity. Next, we put $\beta':=[{\mathbf S}^{-1}\alpha']^{\langle k\rangle}$, so that $\alpha'=[{\mathbf S}\beta']^{\langle k\rangle}$, so that in view of the second condition in (i) and [\[eq-6.5.5\]](#eq-6.5.5){reference-type="eqref" reference="eq-6.5.5"}, we get that $${\mathbf M}_{z-w}[{\mathbf S}\beta']^{\langle k\rangle}={\mathbf M}_{z-w}\alpha'=
[{\mathbf S}' a]^{\langle k\rangle}=
[{\mathbf S}{\mathbf M}^{-1}_{\bar\partial_w\theta}\beta]^{\langle k\rangle}.$$ We solve for $\beta$, using [\[Snabla\]](#Snabla){reference-type="eqref" reference="Snabla"}: $$\beta=[{\mathbf M}_{\bar \partial_w \theta} {\mathbf S}^{-1} {\mathbf M}_{z-w} {\mathbf S}\beta']^{\langle k\rangle}
= [(2m)^{-1}{\mathbf M}_{\bar \partial_w \theta}\boldsymbol{\nabla}\beta']^{\langle k\rangle}.


\label{eq-6.5.6}$$ By putting the relations [\[bianaleq2\]](#bianaleq2){reference-type="eqref" reference="bianaleq2"} and [\[eq-6.5.6\]](#eq-6.5.6){reference-type="eqref" reference="eq-6.5.6"} together, we now see that $$a^{\langle k\rangle}=[(2m)^{-2}\boldsymbol{\nabla}
{\mathbf M}_{\bar \partial_w \theta}\boldsymbol{\nabla}\beta']^{\langle k\rangle},$$ which means that (ii) holds with $A^{\langle k+2\rangle}=(2m)^{-2}\beta'$.

Finally, we turn to the reverse implication $\mathrm{(ii)}\Rightarrow\mathrm{(i)}$. This time we have $A$, and just need to find $\alpha$ and $\alpha'$ with the given properties. Inspired by the calculations we carried out for the forward implication, we put

$\alpha':=[(2m)^2{\mathbf S}A]^{\langle k\rangle}$ and

$\alpha:=

[2m{\mathbf S}{\mathbf M}_{\bar \partial_w \theta}\boldsymbol{\nabla}A]^{\langle k\rangle}$. It remains to verify that (i) holds with these choices $\alpha$ and $\alpha'$. We first check with the help of [\[Snabla\]](#Snabla){reference-type="eqref" reference="Snabla"} and (ii) that $${\mathbf M}_{z-w}\alpha=
[2m{\mathbf M}_{z-w}{\mathbf S}{\mathbf M}_{\bar \partial_w \theta}\boldsymbol{\nabla}A]^{\langle k\rangle}
=[{\mathbf S}\boldsymbol{\nabla}{\mathbf M}_{\bar \partial_w \theta}\boldsymbol{\nabla}A]^{\langle k\rangle}
=[{\mathbf S}a]^{\langle k\rangle},$$ so the first relation in (i) holds. Second, we check using (ii), [\[eq-defS\'\]](#eq-defS'){reference-type="eqref" reference="eq-defS'"}, and [\[Snabla\]](#Snabla){reference-type="eqref" reference="Snabla"}, that $$\begin{gathered}
^{\langle k\rangle}=
[{\mathbf S}'\boldsymbol{\nabla}{\mathbf M}_{\bar \partial_w \theta}\boldsymbol{\nabla}A]^{\langle k\rangle}
=[{\mathbf S}{\mathbf M}^{-1}_{\bar \partial_w \theta} {\mathbf S}^{-1} {\mathbf N}{\mathbf S}
\boldsymbol{\nabla}{\mathbf M}_{\bar \partial_w \theta}\boldsymbol{\nabla}A]^{\langle k\rangle}  
\\
=[2m{\mathbf S}{\mathbf M}^{-1}_{\bar \partial_w \theta} {\mathbf S}^{-1} {\mathbf N}
{\mathbf M}_{z-w}{\mathbf S}{\mathbf M}_{\bar \partial_w \theta}\boldsymbol{\nabla}A]^{\langle k\rangle}
=[2m{\mathbf S}{\mathbf M}^{-1}_{\bar \partial_w \theta}
{\mathbf M}_{\bar \partial_w \theta}\boldsymbol{\nabla}A]^{\langle k\rangle}
\\
=[2m{\mathbf S}\boldsymbol{\nabla}A]^{\langle k\rangle}
=[(2m)^2{\mathbf M}_{z-w}{\mathbf S}A]^{\langle k\rangle}={\mathbf M}_{z-w}\alpha',
\end{gathered}$$ and the second relation in (i) holds as well. Note that in the above calculation we used that ${\mathbf N}{\mathbf M}_{z-w}$ is the identity. The proof is complete. ◻
:::

::: rem
[]{#rem-7.3 label="rem-7.3"} (a) It is clear that a bi-negligible amplitude is automatically a negligible amplitude, since $\boldsymbol{\nabla}{\mathbf M}^{-1}_{\bar \partial_w \theta}\boldsymbol{\nabla}A=
\boldsymbol{\nabla}B$, with $B:={\mathbf M}^{-1}_{\bar \partial_w \theta}\boldsymbol{\nabla}A$. The first part of condition (i) of Proposition [\[binegliprop\]](#binegliprop){reference-type="ref" reference="binegliprop"} captures this observation. But it is of course harder for amplitude to be bi-negligible than to be negligible. The second part of condition (i), which involves ${\mathbf S}'$, expresses that difference.

In the context of the proof of Proposition [\[binegliprop\]](#binegliprop){reference-type="ref" reference="binegliprop"}, the relation $$A^{\langle k+2\rangle}=(2m)^{-2}\beta'=(2m)^{-2}[{\mathbf S}^{-1}\alpha']^{\langle k\rangle}
=(2m)^{-2}[{\mathbf S}^{-1}{\mathbf N}{\mathbf S}' a]^{\langle k\rangle}$$ tells us how to obtain $A^{\langle k+2\rangle}$ starting from a given $a^{\langle k\rangle}$.

Proposition [\[binegliprop\]](#binegliprop){reference-type="ref" reference="binegliprop"} is stated for bi-negligible amplitudes (i.e., where $q=2$). However, it is rather clear how to formulate the corresponding result for general $q$. In (i), we get $q$ operators ${\mathbf S},\ldots,{\mathbf S}^{(q-1)}$ instead of ${\mathbf S},{\mathbf S}'$, and in (ii), we get a product of $q$ copies of the operator $\boldsymbol{\nabla}$ interlaced with $q-1$ copies of the multiplication operator ${\mathbf M}_{\bar\partial_w\theta}$.
:::
