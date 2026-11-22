---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-035-77-the-local-asymptotics-for-the-weighted-bianal
section_title: "The local asymptotics for the weighted bianalytic Bergman kernel: the corrective algorithm I"
section_number: 7.7
pages: 25-28
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.956
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
[]{#subsec-I label="subsec-I"}

The implementation of the corrective algorithm is rather analogous to the holomorphic situation of Subsection [\[subsec-5.6\]](#subsec-5.6){reference-type="ref" reference="subsec-5.6"}. However, since there are certain differences, we explain everything in rather great detail. We recall from Subsection [\[subsec-6.2\]](#subsec-6.2){reference-type="ref" reference="subsec-6.2"} that the kernel $M_{2,m}$ given by [\[eq-6.104\]](#eq-6.104){reference-type="eqref" reference="eq-6.104"} is a local bi-reproducing kernel $\mathrm{mod}(m\mathrm{e}^{-\delta_0m})$; see Proposition [\[neglipropbi\]](#neglipropbi){reference-type="ref" reference="neglipropbi"}. If we correct $M_{2,m}$ by adding a bi-negligible amplitude, then it remains a local bi-reproducing kernel $\mathrm{mod}(m\mathrm{e}^{-\delta_0m})$, in view of [\[bianalnegliampli2\]](#bianalnegliampli2){reference-type="eqref" reference="bianalnegliampli2"}. That is, we replace $M_{2,m}$ by the kernel $$K^{\langle k\rangle}_{2,m}(z,w):=\Lfun^{\langle 2,k\rangle}(z,w)\mathrm{e}^{2mQ(z,w)},$$ where $$\Lfun^{\langle 2,k\rangle}:=m^2\Lfun^{2}_0+m\Lfun^{2}_1+\cdots+m^{-k+1}
\Lfun^{2}_{k+1}
\label{eq-Lfunexp1.b}$$ is a finite asymptotic expansion (where each term $\Lfun^{2}_j$ is independent of $m$), with $$\Lfun^{\langle 2,k\rangle}=
- \frac{4m^2}{\pi}
|z-w|^2 (\bar \partial_w \theta)^2
+\frac{4m}{\pi}\bar\partial_w\theta - \frac{2m}{\pi}
(\bar z-\bar w)\bar\partial_w^2 \theta+\bar\partial_w\theta \, 
[\boldsymbol{\nabla}{\mathbf M}_{\bar\partial_w\theta}\boldsymbol{\nabla}X]^{\langle k\rangle}.  
\label{negliampeq.b}$$ Here, $X\sim X_0+m^{-1}X_1+m^{-2}X_2+\ldots$ is some asymptotic expansion in $m$ (where every $X_j$ is independent of $m$), where each $X_j(z,w)$ should be bi-holomorphic in $z$ and $C^\infty$-smooth in $w$. Then $K^{\langle k\rangle}_{2,m}(z,w)$ is a local bi-reproducing kernel $\text{mod}(m^{-k})$ as a result of perturbing by the abschnitt of a negligible amplitude (multiplied by $\mathrm{e}^{2mQ(z,w)}$). We want to add the condition that $\Lfun^{\langle 2,k\rangle}(z,w)$ be bi-holomorphic in $\bar w$, to obtain a local weighted bianalytic Bergman kernel $\text{mod}(m^{-k})$. If we write $$\Rfun^{(2)}:= -\frac{4m^2}{\pi}
|z-w|^2 (\bar \partial_w \theta)^2
+\frac{4m}{\pi}\bar \partial_w \theta-\frac{2m}{\pi}
(\bar z-\bar w)\bar\partial_w^2 \theta,$$ so that the kernel $M_{2,m}$ in [\[eq-6.104\]](#eq-6.104){reference-type="eqref" reference="eq-6.104"} may be written as $$\label{eq-RfunM}
M_{2,m}(z,w)=\Rfun^{(2)}(z,w)\,\mathrm{e}^{2mQ(z,w)},$$ then the relation [\[negliampeq.b\]](#negliampeq.b){reference-type="eqref" reference="negliampeq.b"} may be expressed in condensed form: $$\bigg[\frac{\Lfun^{(2)}-\Rfun^{(2)}}{\bar\partial_w\theta}\bigg]
^{\langle k\rangle}=
[\boldsymbol{\nabla}{\mathbf M}_{\bar\partial_w\theta}\boldsymbol{\nabla}X]^{\langle k\rangle}.  
\label{negliampeq2.b}$$ Here, $\Lfun^{(2)}\sim m^2\Lfun^{2}_0+m\Lfun^{2}_1+\Lfun^{2}_2+\ldots$ is the asymptotic expansion with abschnitt $\Lfun^{\langle 2,k\rangle}$. This now puts us in a position to apply Proposition [\[binegliprop\]](#binegliprop){reference-type="ref" reference="binegliprop"}, which says that [\[negliampeq2.b\]](#negliampeq2.b){reference-type="eqref" reference="negliampeq2.b"} holds for some $X$ if and only if $$\bigg\{
{\mathbf S}\bigg[\frac{\Lfun^{(2)}-\Rfun^{(2)}}{\bar\partial_w\theta}\bigg]
\bigg\}^{\langle k\rangle}\in{\mathbf M}_{z-w}{\mathfrak R}_2\quad\text{and}\quad
{\mathbf S}'\bigg[\frac{\Lfun^{(2)}-\Rfun^{(2)}}{\bar\partial_w\theta}\bigg]
\bigg\}^{\langle k\rangle}\in{\mathbf M}_{z-w}{\mathfrak R}_2.
\label{negliampeq3.b}$$ Also, Remark [\[rem-7.3\]](#rem-7.3){reference-type="ref" reference="rem-7.3"} tells us how to recover the corresponding abschnitt of $X$: $$\label{eq-recoverX}
X^{\langle k+2\rangle}=(2m)^{-2}\bigg\{
{\mathbf S}^{-1}{\mathbf N}{\mathbf S}'\bigg[\frac{\Lfun^{(2)}-\Rfun^{(2)}}{\bar\partial_w\theta}\bigg]
\bigg\}^{\langle k\rangle}.$$ This formula is valuable when we need to estimate the contribution from the bi-negligible amplitude using [\[bianalnegliampli2\]](#bianalnegliampli2){reference-type="eqref" reference="bianalnegliampli2"}.

It remains to see how [\[negliampeq3.b\]](#negliampeq3.b){reference-type="eqref" reference="negliampeq3.b"} helps us determine the asymptotic expansion $\Lfun^{(2)}$. A first remark is that it no longer will be enough to determine $\Lfun^{(2)}(z,w)$ along the diagonal $z=w$, as functions which are biharmonic in each of the variables $(z,\bar w)$ need not be uniquely determined by their diagonal restrictions (e.g., consider the function $\bar z w-z\bar w$).

Before we carry on to analyze the relations [\[negliampeq3.b\]](#negliampeq3.b){reference-type="eqref" reference="negliampeq3.b"} further,

we recall the Taylor expansions [\[eq-4.19\]](#eq-4.19){reference-type="eqref" reference="eq-4.19"}, [\[eq-4.19.1\]](#eq-4.19.1){reference-type="eqref" reference="eq-4.19.1"}, and [\[eq-4.19.2\]](#eq-4.19.2){reference-type="eqref" reference="eq-4.19.2"}, and rewrite [\[eq-4.19.1\]](#eq-4.19.1){reference-type="eqref" reference="eq-4.19.1"} in the form $$\bar\partial_w\theta=
\partial_z\bar\partial_w Q(z,w)
\bigg\{1+\sum_{j=1}^{+\infty}\frac{1}{(j+1)!}(w-z)^{j}
\frac{\partial_z^{j+1}\bar\partial_w Q(z,w)}{\partial_z\bar\partial_w Q(z,w)}\bigg\},
\label{eq-4.19.3}$$ It follows from [\[eq-4.19.2\]](#eq-4.19.2){reference-type="eqref" reference="eq-4.19.2"} and [\[eq-4.19.3\]](#eq-4.19.3){reference-type="eqref" reference="eq-4.19.3"} that $$\frac{\partial_w\theta}{\bar\partial_w\theta}-
\frac12\frac{\partial_z^2Q(z,w)}{\partial_z\bar\partial_w Q(z,w)}\in{\mathbf M}_{z-w}{\mathfrak R}_1.
\label{eq-4.19-ratio}$$ A more refined version of [\[eq-4.19-ratio\]](#eq-4.19-ratio){reference-type="eqref" reference="eq-4.19-ratio"} is $$\frac{\partial_w\theta}{\bar\partial_w\theta}-
\frac12\frac{\partial_z^2Q(z,w)}{\partial_z\bar\partial_w Q(z,w)}
-(w-z)\bigg\{\frac13\frac{\partial_z^3Q(z,w)}{\partial_z\bar\partial_wQ(z,w)}
-\frac14\frac{[\partial_z^2Q(z,w)][\partial_z^2\bar\partial_wQ(z,w)]}
{[\partial_z\bar\partial_w Q(z,w)]^2}\bigg\} 
\in{\mathbf M}_{z-w}^2{\mathfrak R}_1.
\label{eq-4.19-ratio2}$$ We now return to the corrective algorithm, which takes the criteria [\[negliampeq3.b\]](#negliampeq3.b){reference-type="eqref" reference="negliampeq3.b"} as its starting point. We express $\Rfun^{(2)}$ in terms of the differential operators ${\pmb{\partial}}_w$ and ${\pmb{\partial}}_\theta$, using that ${\pmb{\partial}}_\theta\bar w=1/\bar\partial_w\theta$: $$\frac{\Rfun^{(2)}}{\bar\partial_w\theta}={\mathbf M}_{{\pmb{\partial}}_\theta \bar w}[\Rfun^{(2)}]

=-\frac{4m^2}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}
+\frac{4m}{\pi}-\frac{2m}{\pi}(\bar z-\bar w)\,
{\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}.
\label{eq-initial1.1}$$

We first rewrite the criteria [\[negliampeq3.b\]](#negliampeq3.b){reference-type="eqref" reference="negliampeq3.b"} in the more appropriate form $$\big\{
{\mathbf S}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[
\Lfun^{(2)}-\Rfun^{(2)}]
\big\}^{\langle k\rangle}\in{\mathbf M}_{z-w}{\mathfrak R}_2\quad\text{and}\quad
\big\{{\mathbf S}'{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[\Lfun^{(2)}-\Rfun^{(2)}]
\big\}^{\langle k\rangle}\in{\mathbf M}_{z-w}{\mathfrak R}_2.
\label{negliampeq4.b}$$

In view of the asymptotic expansion for $\Lfun^{(2)}$ (see [\[eq-Lfunexp1.b\]](#eq-Lfunexp1.b){reference-type="eqref" reference="eq-Lfunexp1.b"}) and the definition [\[Sdef\]](#Sdef){reference-type="eqref" reference="Sdef"} of the operator ${\mathbf S}$, it follows that $$\big\{{\mathbf S}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[\Lfun^{(2)}]\big\}^{\langle k\rangle}
=\sum_{j=0}^{k+1}m^{2-j}\sum_{i=0}^{j}
\frac{2^{-i}}{i!}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^i{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{j-i}.
\label{eq-firstcond1}$$ We would also like to calculate the corresponding expression involving the operator ${\mathbf S}'$ in place of ${\mathbf S}$ (see [\[eq-defS\'\]](#eq-defS'){reference-type="eqref" reference="eq-defS'"}). In a first step, we get that $$\big\{{\mathbf S}^{-1}{\mathbf N}{\mathbf S}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[\Lfun^{(2)}]\big\}^{\langle k\rangle}
=\sum_{j=0}^{k+1}m^{2-j}\sum_{i_2=0}^{j}\sum_{i_1=0}^{i_2}
\frac{(-1)^{i_2-i_1}2^{-i_2}}{i_1!(i_2-i_1)!}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_2-i_1}
{\mathbf N}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_1}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{j-i_2},$$ and, in a second step, we obtain (since ${\mathbf M}_{{\pmb{\partial}}_\theta\bar w}={\mathbf M}_{\bar\partial_w\theta}^{-1}$) $$\begin{gathered}
\big\{{\mathbf S}'{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[\Lfun^{(2)}]
\big\}^{\langle k\rangle}
=\big\{{\mathbf S}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf S}^{-1}{\mathbf N}{\mathbf S}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[\Lfun^{(2)}]
\big\}^{\langle k\rangle}





\\
=\sum_{j=0}^{k+1}m^{2-j}\sum_{i_3=0}^{j}\sum_{i_2=0}^{i_3}
\sum_{i_1=0}^{i_2}
\frac{(-1)^{i_2-i_1}2^{-i_3}}{i_1!(i_2-i_1)!(i_3-i_2)!}
({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_3-i_2}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}
({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_2-i_1}{\mathbf N}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_1}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{j-i_3}.
\label{eq-6.6.11}
\end{gathered}$$ We also need to calculate the corresponding expressions for $\Rfun^{(2)}$. First, we find that (see [\[eq-initial1.1\]](#eq-initial1.1){reference-type="eqref" reference="eq-initial1.1"}) $$\begin{gathered}
\big\{{\mathbf S}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[\Rfun^{(2)}]\big\}^{\langle k\rangle}

=\bigg\{{\mathbf S}\bigg[-\frac{4m^2}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}
+\frac{4m}{\pi}-\frac{2m}{\pi}(\bar z-\bar w)\,
{\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}\bigg]\bigg\}^{\langle k\rangle}
\\
=\frac{4m}{\pi}
-\frac{4m^2}{\pi}
\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}-\sum_{j=1}^{k+1}\frac{(2m)^{2-j}}{j!\pi}
({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{j-1}\bigg\{j(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}
{{\pmb{\partial}}_\theta\bar w}
+{\pmb{\partial}}_w{\pmb{\partial}}_\theta\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\},
\label{eq-6.6.12}
\end{gathered}$$

and, consequently, $$\begin{gathered}
\big\{{\mathbf N}{\mathbf S}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[\Rfun^{(2)}]\big\}^{\langle k\rangle}





=-\frac{4m^2}{\pi}
\frac{\bar z-\bar w}{{\pmb{\partial}}_\theta \bar w}
\\
-\sum_{j=1}^{k+1}\frac{(2m)^{2-j}}{j!\pi}{\mathbf N}
({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{j-1}\bigg\{j(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}
{{\pmb{\partial}}_\theta\bar w}
+{\pmb{\partial}}_w{\pmb{\partial}}_\theta\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\}
\\
=-\sum_{j=0}^{k+1}\frac{(2m)^{2-j}}{j!\pi}{\mathbf N}
\bigg\{j({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{j-1}{\mathbf M}_{\bar z-\bar w}\,
{\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}
+({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^j\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\},
\label{eq-6.6.12.1}
\end{gathered}$$ where we interpret the term for $j=0$ is the natural fashion. By expansion of the operators involved, it is clear that, formally, $${\mathbf S}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf S}^{-1}
=\sum_{j=0}^{+\infty}(2m)^{-j}\sum_{i=0}^{j}
\frac{(-1)^{i}}{i!(j-i)!}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{j-i}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i},$$ which we apply to [\[eq-6.6.12.1\]](#eq-6.6.12.1){reference-type="eqref" reference="eq-6.6.12.1"}: $$\begin{gathered}
\big\{{\mathbf S}'{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[\Rfun^{(2)}]\big\}^{\langle k\rangle}
=\big\{{\mathbf S}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf S}^{-1}
{\mathbf N}{\mathbf S}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[\Rfun^{(2)}]\big\}^{\langle k\rangle}
=-\frac{1}{\pi}\sum_{j=0}^{k+1}(2m)^{2-j}\sum_{i_2=0}^{j}
\sum_{i_1=0}^{i_2}\frac{(-1)^{i_2-i_1}}{i_2!i_1!(i_2-i_1)!}
\\
\times
({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_1}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_2-i_1}{\mathbf N}
\bigg\{(j-i_2)({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{j-i_2-1}{\mathbf M}_{\bar z-\bar w}
{\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}
+({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{j-i_2}\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\}.
\label{eq-6.6.13.1}
\end{gathered}$$ We may now apply the criterion [\[negliampeq4.b\]](#negliampeq4.b){reference-type="eqref" reference="negliampeq4.b"} for each power of $m$ separately. The first part of the criterion, which involves ${\mathbf S}$,

says (for $j=0$) $$\frac{4}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}
+{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}\in{\mathbf M}_{z-w}{\mathfrak R}_2, 
\label{eq-4.13'}$$ and (for $j=1$)

$$-\frac{4}{\pi}+\frac{2}{\pi}(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}

+\frac{2}{\pi}{\pmb{\partial}}_w{\pmb{\partial}}_\theta\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}

+{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{1}
+\frac12{\pmb{\partial}}_w{\pmb{\partial}}_\theta{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}
\in {\mathbf M}_{z-w}{\mathfrak R}_2, 
\label{eq-4.14}$$ while (for $j=2,3,4,\ldots$) $$\begin{gathered}
\frac{2^{2-j}}{j!\pi}
({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{j-1}\bigg\{j(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}
{{\pmb{\partial}}_\theta\bar w}
+{\pmb{\partial}}_w{\pmb{\partial}}_\theta\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\} 
+\sum_{i=0}^{j}
\frac{2^{-i}}{i!}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^i{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{j-i}
\in{\mathbf M}_{z-w}{\mathfrak R}_2.
\label{eq-4.15}
\end{gathered}$$ As for the second part of the criterion [\[negliampeq4.b\]](#negliampeq4.b){reference-type="eqref" reference="negliampeq4.b"}, which involves ${\mathbf S}'$, it says that (use [\[eq-6.6.11\]](#eq-6.6.11){reference-type="eqref" reference="eq-6.6.11"} and [\[eq-6.6.13.1\]](#eq-6.6.13.1){reference-type="eqref" reference="eq-6.6.13.1"}) for $j=0,1,2,\ldots$, $$\begin{gathered}
\sum_{i_3=0}^{j}\sum_{i_2=0}^{i_3}
\sum_{i_1=0}^{i_2}
\frac{(-1)^{i_2-i_1}2^{-i_3}}{i_1!(i_2-i_1)!(i_3-i_2)!}
({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_3-i_2}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}
({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_2-i_1}{\mathbf N}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_1}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{j-i_3}
\\
+\frac{2^{2-j}}{\pi}\sum_{i_2=0}^{j}
\sum_{i_1=0}^{i_2}\frac{(-1)^{i_2-i_1}}{i_2!i_1!(i_2-i_1)!}
\\
\times
({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_1}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{i_2-i_1}{\mathbf N}
\bigg\{(j-i_2)({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{j-i_2-1}{\mathbf M}_{\bar z-\bar w}
{\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}
+({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^{j-i_2}\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\}
\in{\mathbf M}_{z-w}{\mathfrak R}_2.
\label{eq-4.17.1}
\end{gathered}$$ For $j=0$, the condition [\[eq-4.17.1\]](#eq-4.17.1){reference-type="eqref" reference="eq-4.17.1"} reads $$\frac{4}{\pi}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf N}\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}
+{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf N}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}\in{\mathbf M}_{z-w}{\mathfrak R}_2, 
\label{eq-4.16.1}$$ and for $j=1$, $$\begin{gathered}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf N}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{1}
+\frac12{\pmb{\partial}}_w{\pmb{\partial}}_\theta{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf N}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}
-\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}^{-1}{\pmb{\partial}}_w{\pmb{\partial}}_\theta{\mathbf N}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}
\\
+\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf N}{\pmb{\partial}}_w{\pmb{\partial}}_\theta{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}
+\frac{2}{\pi}{\pmb{\partial}}_w{\pmb{\partial}}_\theta{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf N}\bigg[
\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg]
-\frac{2}{\pi}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\pmb{\partial}}_w{\pmb{\partial}}_\theta{\mathbf N}\bigg[
\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg]
\\
+\frac{2}{\pi}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf N}{\pmb{\partial}}_w{\pmb{\partial}}_\theta\bigg[
\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg]+
\frac{2}{\pi}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf N}
\bigg[(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}\bigg]
\in{\mathbf M}_{z-w}{\mathfrak R}_2.
\label{eq-4.16.2}
\end{gathered}$$ As the function $1/{\pmb{\partial}}_\theta\bar w$ is in ${\mathfrak R}_1$, we may rewrite [\[eq-4.16.1\]](#eq-4.16.1){reference-type="eqref" reference="eq-4.16.1"} in the form $${\mathbf N}\bigg[\frac{4}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}+{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}
\Lfun^2_{0}\bigg]
\in{\mathbf M}_{z-w}{\mathfrak R}_2.
\label{eq-4.16.3}$$ and we may reorganize [\[eq-4.16.2\]](#eq-4.16.2){reference-type="eqref" reference="eq-4.16.2"}:

$$\begin{gathered}
{\mathbf N}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{1}
+{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}^{-1}{\pmb{\partial}}_w{\pmb{\partial}}_\theta{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\mathbf N}
\bigg[\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+\frac{2}{\pi}
\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg]
-{\pmb{\partial}}_w{\pmb{\partial}}_\theta{\mathbf N}
\bigg[\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+
\frac{2}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg]
\\
+{\mathbf N}{\pmb{\partial}}_w{\pmb{\partial}}_\theta
\bigg[\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+\frac{2}{\pi}
\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg]
+\frac{2}{\pi}{\mathbf N}\bigg[(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}\bigg]
\in{\mathbf M}_{z-w}{\mathfrak R}_2.
\label{eq-4.16.4}
\end{gathered}$$ In terms of the usual commutator $\boldsymbol{\lfloor}{\mathbf A}\boldsymbol{,}{\mathbf B}\boldsymbol{\rfloor}
:={\mathbf A}{\mathbf B}-{\mathbf B}{\mathbf A}$,

we may express [\[eq-4.16.4\]](#eq-4.16.4){reference-type="eqref" reference="eq-4.16.4"} as $$\begin{gathered}
{\mathbf N}\bigg[
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}[\Lfun^2_{1}]
+{\pmb{\partial}}_w{\pmb{\partial}}_\theta\bigg\{\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+
\frac{2}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\}
-\frac{4}{\pi}+\frac{2}{\pi}(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}
\bigg]
\\
+{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}^{-1}{\boldsymbol{\Big\lfloor}}
{\pmb{\partial}}_w{\pmb{\partial}}_\theta\boldsymbol{,}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\boldsymbol{\Big\rfloor}}
{\mathbf N}\bigg[\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+\frac{2}{\pi}
\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}\bigg]
\in{\mathbf M}_{z-w}{\mathfrak R}_2.
\label{eq-4.16.5}
\end{gathered}$$
