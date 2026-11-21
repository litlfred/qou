---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-027-66-the-local-asymptotics-for-the-weighted-bergma
section_title: "The local asymptotics for the weighted Bergman kernel: the corrective algorithm"
section_number: 6.6
pages: 18-20
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.958
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
[]{#subsec-5.6 label="subsec-5.6"}

We recall from Subsection [\[subsec-5.3\]](#subsec-5.3){reference-type="ref" reference="subsec-5.3"} that the kernel $M_m(z,w)$ given by [\[eq-Mm\]](#eq-Mm){reference-type="eqref" reference="eq-Mm"} is a local reproducing kernel $\mathrm{mod}(\mathrm{e}^{-\delta_0 m})$ (see Proposition [\[negliprop\]](#negliprop){reference-type="ref" reference="negliprop"}). The kernel $M_m(z,w)$ is automatically holomorphic in $z\in{\mathbb D}(z_0,r)$, and we would like to correct it so that it becomes conjugate-holomorphic in $w$, while maintaining the approximate reproducing property. In view of the negligible amplitude calculation [\[nablanegli\]](#nablanegli){reference-type="eqref" reference="nablanegli"}, the approximate reproducing property (with a worse precision) will be kept if we replace $M_m$ by the kernel $$K^{\langle k\rangle}_{m}(z,w):=\Lfun^{\langle k\rangle}(z,w)\,\mathrm{e}^{2mQ(z,w)},$$ where $$\Lfun^{\langle k\rangle}:=m\Lfun_0+\Lfun_1+\cdots+m^{-k+1}
\Lfun_k
\label{eq-Lfunexp1}$$ is a finite asymptotic expansion (where each term $\Lfun_j$ is independent of $m$), with $$\Lfun^{\langle k\rangle}=
\frac{2m}{\pi}\bar\partial_w \theta + \bar\partial_w\theta \, 
[\boldsymbol{\nabla}X]^{\langle k\rangle}.  
\label{negliampeq}$$ Here, $X\sim X_0+m^{-1}X_1+m^{-2}X_2+\ldots$ is an asymptotic expansion in $m$ (where every $X_j$ is independent of $m$), and each $X_j(z,w)$ should be holomorphic in $z$ and $C^\infty$-smooth in $w$. Then $K^{\langle k\rangle}_{m}(z,w)$ is a local reproducing kernel $\text{mod}(m^{-k})$ as a result of perturbing by the abschnitt of a negligible amplitude (multiplied by $\mathrm{e}^{2mQ(z,w)}$). We want to add the condition that $\Lfun^{\langle k\rangle}(z,w)$ be conjugate-holomorphic in $w$, to obtain a local Bergman kernel $\text{mod}(m^{-k})$. This amounts to asking that $\Lfun_j(z,w)$ is holomorphic in $\bar w$. The way this will enter into the algorithm is that such functions are uniquely determined by their diagonal restrictions.

It is convenient to express [\[negliampeq\]](#negliampeq){reference-type="eqref" reference="negliampeq"} is the form $$\frac{\Lfun^{\langle k\rangle}}{\bar\partial_w \theta}=
\frac{2m}{\pi}+[\boldsymbol{\nabla}X]^{\langle k\rangle}.  
\label{negliampeq1.1}$$ For convenience of notation, we think of $\Lfun^{\langle k\rangle}$ as the abschnitt of an asymptotic expansion $\Lfun\sim m\Lfun_0+\Lfun_1+
m^{-1}\Lfun_2+\ldots$. Proposition [\[prop-neglampl1\]](#prop-neglampl1){reference-type="ref" reference="prop-neglampl1"} tells us how to solve [\[negliampeq1.1\]](#negliampeq1.1){reference-type="eqref" reference="negliampeq1.1"}: we just apply the diffusion operator ${\mathbf S}$ to both sides and check that the abschnitts coincide along the diagonal $z=w$. More concretely, $\Lfun^{\langle k\rangle}$ solves [\[negliampeq1.1\]](#negliampeq1.1){reference-type="eqref" reference="negliampeq1.1"} for some $X$ if and only if $$\bigg\{{\mathbf S}\bigg[\frac{\Lfun}{\bar\partial_w \theta}
\bigg]-\frac{2m}{\pi}\bigg\}^{\langle k\rangle}\in{\mathbf M}_{z-w}{\mathfrak R}_1,$$ which is the same as $$\bigg\{{\mathbf S}\bigg[\frac{m^{-1}\Lfun}{\bar\partial_w \theta}
\bigg]\bigg\}^{\langle k+1\rangle}-\frac{2}{\pi}\in{\mathbf M}_{z-w}{\mathfrak R}_1.  
\label{Scond}$$ When we expand the condition [\[Scond\]](#Scond){reference-type="eqref" reference="Scond"}, we find that it is equivalent to having $$\frac{\Lfun_0}{\bar\partial_w \theta}-\frac{2}{\pi}\in{\mathbf M}_{z-w}{\mathfrak R}_1,
\label{Scond1}$$ and $$\sum_{i=0}^{j}\frac{1}{i!2^i}({\pmb{\partial}}_w{\pmb{\partial}}_\theta)^i
\Bigg\{\frac{\Lfun_{j-i}}{\bar\partial_w \theta}\Bigg\}\in{\mathbf M}_{z-w}{\mathfrak R}_1,
\qquad j=1,\ldots,k.
\label{Scond2}$$ From the Taylor expansion [\[eq-4.19.1\]](#eq-4.19.1){reference-type="eqref" reference="eq-4.19.1"}, we see that $$\bar\partial_w\theta(z,w)-\partial_z\bar\partial_w Q(z,w)\in{\mathbf M}_{z-w}
{\mathfrak R}_1,$$ so that [\[Scond1\]](#Scond1){reference-type="eqref" reference="Scond1"} is equivalent to $$\Lfun_0(z,w)-\frac{2}{\pi}\partial_z\bar\partial_w Q(z,w)\in{\mathbf M}_{z-w}{\mathfrak R}_1.$$ Taking the restriction to the diagonal, we obtain that $\Lfun_0(z,z)=\frac{2}{\pi}\varDelta Q(z)$, and as the diagonal $z=w$ is a uniqueness set for functions that are holomorphic in $(z,\bar w)$, the only possible choice is $$\Lfun_0(z,w):=\frac{2}{\pi}\partial_z\bar\partial_w Q(z,w).$$ The rest of the functions $\Lfun_j$ are obtained in explicit form using [\[Scond2\]](#Scond2){reference-type="eqref" reference="Scond2"}. To illustrate how this works, we show how to obtain $\Lfun_1$. By [\[Scond2\]](#Scond2){reference-type="eqref" reference="Scond2"} with $j=1$, we have $$\frac{\Lfun_{1}}{\bar\partial_w\theta}+\frac12{\pmb{\partial}}_w{\pmb{\partial}}_\theta
\Bigg\{\frac{\Lfun_{0}}{\bar\partial_w \theta}\Bigg\}\in{\mathbf M}_{z-w}{\mathfrak R}_1.
\label{eq-5.29}$$ We plug in the expression for $\Lfun_0$ which we obtained above, and restrict [\[eq-5.29\]](#eq-5.29){reference-type="eqref" reference="eq-5.29"} to the diagonal $z=w$: $$\frac{\Lfun_{1}(z,z)}{\varDelta Q(z,z)}=-\frac12{\pmb{\partial}}_w{\pmb{\partial}}_\theta
\Bigg\{\frac{\frac{2}{\pi}\partial_z\bar\partial_w Q(z,w)}
{\bar\partial_w \theta}
\Bigg\}\Bigg|_{w:=z}.$$ After some necessary simplifications, this leads to the formula $$\Lfun_{0}(z,z)=\frac{1}{2\pi}\varDelta\log\varDelta Q(z),$$ and the only possible choice for $\Lfun_{0}(z,w)$ which is holomorphic in $(z,\bar w)$ is the polarization of the above, $$\Lfun_{0}(z,w)=\frac1{2\pi}
\partial_z\bar\partial_w\log[\partial_z\bar\partial_w 
Q(z,w)].$$ We note that the expressions for $\Lfun_{j}(z,w)$ are well-defined and holomorphic in $(z,\bar w)$ on the bidisk ${\mathbb D}(z_0,r)\times{\mathbb D}(z_0,r)$, at least for $j=0$ and $j=1$. This will be the case for all other indices $j$ as well, because the expressions for $\Lfun^{1}_{j}(z,w)$ will only involve polynomial expressions in some derivatives of $\partial_z\bar\partial_wQ(z,w)$ possibly divided by a positive integer power of $\partial_z\bar\partial_wQ(z,w)$. This allows us to work with the local Bergman kernel $K^{\langle k\rangle}(z,w)$ in the context of the bidisk ${\mathbb D}(z_0,r)\times{\mathbb D}(z_0,r)$.
