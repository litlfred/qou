---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-019-324-torsion-for-dehn-fillings
section_title: "Torsion for Dehn fillings"
section_number: 3.2.4
pages: 23-25
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.993
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
Let $\vert p\vert +\vert q\vert$ be sufficiently large and let $\sigma$ be a spin structure on $M^3$ extensible to $M_{p/q}^3$. Let $\rho_{p/q,\sigma}$ denote the lift of the holonomy of the restriction to $M^3$ of the hyperbolic structure on $M_{p/q}^3$, and $\chi_{p/q,\sigma}$ the corresponding character. Let $\lambda_{p/q}$ denote the complex length of the soul of the filling torus. There is a surgery formula:

::: prop
[]{#prop:SF label="prop:SF"} Let $M^3$ be as above. For $\vert p\vert +\vert q\vert$ sufficiently large: $$\tau(M_{p/q}^3,\sigma)=  \frac{\mathbb{T}_{M}(\chi_{p/q,\sigma} )}{ 2 
(1-\cosh(\lambda_{p/q}/2 ) ) }.$$
:::

This proposition can be proved using Mayer-Vietoris (Proposition [\[prop:MV\]](#prop:MV){reference-type="ref" reference="prop:MV"}) to the pair $(M^3, D^2\times S^1 )$. The proof can be found for instance in [@Kitano15] for the figure eight knot, and in [@Tran15] for twist knots, but it applies to every cusped manifold, and it is essentially done too in [@Memoirs Proposition 4.10]. The only computation required is the torsion of the solid torus added by Dehn filling, or its core geodesic, which is (by Example [\[ex:circle\]](#ex:circle){reference-type="ref" reference="ex:circle"}): $$\frac{1}{
\det \left( \begin{pmatrix}
            1 & 0 \\
            0 & 1
           \end{pmatrix}
           -
           \begin{pmatrix}
            e^{\lambda_{p/q}/2} & 0 \\
            0 & e^{-\lambda_{p/q}/2}
           \end{pmatrix}
      \right) }= \frac1{2 (1-\cosh(\lambda_{p/q}/2 ))}.$$

::: remark
[]{#rem:2pi label="rem:2pi"} The complex length $\lambda_{p/q}$ is defined up to addition of a term in $2\pi i \mathbb{Z}$. The spin structure (or equivalently a choice of lift of the holonomy) determines $\lambda_{p/q}$ up to $4\pi i\mathbb{Z}$, as the holonomy of this curve is conjugate to $$\begin{pmatrix}
 e^{\lambda_{p/q}/2} & 0 \\ 0 & e^{-\lambda_{p/q}/2}
\end{pmatrix}.$$
:::

::: cor
[]{#cor:differentspin label="cor:differentspin"} There exist closed hyperbolic manifolds $N^3$ with two spin structures $\sigma$ and $\sigma'$ so that $\tau(N^3,\sigma)\neq \tau(N^3,\sigma')$.
:::

::: proof
*Proof.* The manifolds are obtained by Dehn filling on the figure eight knot. Consider the sequence $p_n/ q_n= 2 n$ so that both spin structures on the figure eight knot exterior $M^3$ extend to $M^3_{p_n/q_n}$, i.e. $H_1(M^3_{2 n} ; \mathbb{Z}/2\mathbb{Z})\cong \mathbb{Z}/2\mathbb{Z}$. The corresponding lifts differ on the sign of the trace of the meridian. As the core of the solid torus is homologous to the meridian, the sign of the traces of these cores differ. Hence for one of the lifts the complex length (modulo $4\pi i\mathbb{Z}$) is $\lambda_{2n}$, for the other one it is $\lambda_{2n}+ 2\pi i$ by Remark [\[rem:2pi\]](#rem:2pi){reference-type="ref" reference="rem:2pi"}. By Remark [\[rem:length\]](#rem:length){reference-type="ref" reference="rem:length"}, one may approximate $$\label{eqn:approx}
 \lambda_{2n}=\frac{2\pi i}{2n}+ O\left(\frac{1}{n^2}\right).$$ The goal is to show that the limit $$\label{eqn:limit}
 \lim_{n\to+\infty} \frac{\vert \tau(M_{2 n},\sigma )\vert }{ \vert \tau(M_{2 n},\sigma' )\vert}$$ is not $1$. By Proposition [\[prop:SF\]](#prop:SF){reference-type="ref" reference="prop:SF"} it is the product of the limits: $$\label{eqn:limitlambdas}
 \lim_{n\to\infty}\frac{1-\cosh( \lambda_{2n}/2 ) }{ 1-\cosh( (\lambda_{2n} + 2\pi i)/2) }
=\lim_{n\to\infty}\frac{1-\cos\frac{\pi} {2n}}{1+\cos\frac{\pi} {2n}} = 0$$ (using the approximation [\[eqn:approx\]](#eqn:approx){reference-type="eqref" reference="eqn:approx"}) and $$\label{eqn:limitfunctions}
 \lim_{n\to\infty}  
 \frac{\mathbb{T}_M(\chi_{2n,\sigma} 
)}{\mathbb{T}_M(\chi_{2n,\sigma'} )}
=
\frac{\tau(M^3,\sigma)}{\tau(M^3,\sigma')}.$$ As for one of the spin structures the trace of the meridian is $2$ and for the other $-2$, by Example [\[ex:fig8sl2\]](#ex:fig8sl2){reference-type="ref" reference="ex:fig8sl2"}, the limit in [\[eqn:limitfunctions\]](#eqn:limitfunctions){reference-type="eqref" reference="eqn:limitfunctions"} is $(2-2\cdot(-2))/(2-2\cdot2)=-3$. Thus the limit [\[eqn:limit\]](#eqn:limit){reference-type="eqref" reference="eqn:limit"} vanishes, hence it is not $1$. ◻
:::

The previous argument applies to any knot exterior, the precise value of the torsion is not needed. Corollary [\[cor:differentspin\]](#cor:differentspin){reference-type="ref" reference="cor:differentspin"} holds true also for cusped manifolds, by applying an analogous formula for partial surgery.

::: cor
[]{#cor:dense label="cor:dense"} The set of modules of the torsions $\left\vert \tau(M^3_{p/q},\sigma)\right\vert$ obtained by Dehn filling on $M^3$, so that the spin structure $\sigma$ on $M^3$ extends to $M^3_{p/q}$, is dense in $$\left[\frac14{\vert \tau(M^3,\sigma)\vert},+\infty\right).$$
:::

::: proof
*Proof.* By the surgery formula, Proposition [\[prop:SF\]](#prop:SF){reference-type="ref" reference="prop:SF"}, it suffices to show that $$\left\vert 1- \cosh( 
  {\lambda_{p/q}}/2)\right\vert$$ is dense in the interval $[0,2]$. Let $r, s\in\mathbb{Z}$ be such that $p s-q r = 1$, by Remark [\[rem:length\]](#rem:length){reference-type="ref" reference="rem:length"}, $\lambda_{p/q}= 2\pi i \frac{r}p+\frac up$ and $u\to 0$. Then the result follows from the density of $\cos(\pi \frac{r}{p})$ in $[-1,1]$. Notice that extendibility of $\sigma$ is just determined by a condition $a\, p + b\, q\equiv 0 \mod 2$, for $a, b\in \mathbb{Z}/2\mathbb{Z}$ depending on $\sigma$. ◻
:::

As the surgery formula shows, this density is a consequence of the contribution of the core geodesics. Notice that in Theorem [\[thm:BV\]](#thm:BV){reference-type="ref" reference="thm:BV"} the hypothesis require the length of geodesics to be bounded below away from zero.
