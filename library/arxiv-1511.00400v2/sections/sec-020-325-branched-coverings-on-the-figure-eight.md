---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-020-325-branched-coverings-on-the-figure-eight
section_title: "Branched coverings on the figure eight"
section_number: 3.2.5
pages: 25-26
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.969
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
[]{#sssection:branched label="sssection:branched"}

We next consider another family of examples. We consider it only for the figure eight knot, but it generalizes to other manifolds.

Consider $M_ n^3$ the n-th cyclic branched covering of $S^3$, branched along the figure eight knot. It is hyperbolic for $n\geq 4$. Its torsion may be computed by means of the twisted Alexander polynomial, by using the formula à la Fox, Proposition [\[prop:Fox\]](#prop:Fox){reference-type="ref" reference="prop:Fox"}, due to Turaev [@Turaev86], see also [@DY12; @Porti04; @SW02; @Raimbault12; @Yamaguchi12]. More precisely, this polynomial is $$p_{\chi}( t )=t^2-2\chi(m) t + 1,$$ by [\[eqn:tor82t\]](#eqn:tor82t){reference-type="eqref" reference="eqn:tor82t"}, cf. [@Kitano-Morifuji2012]. Notice that its value at $1$ agrees with Example [\[ex:fig8sl2\]](#ex:fig8sl2){reference-type="ref" reference="ex:fig8sl2"}. The holonomy of $M_ n^3$ extends to a holonomy of the quotient orbifold $M_ 
n^3/ 
(\mathbb{Z}/n\mathbb{Z})$ in $\mathrm{PSL}_2(\mathbb{C})$. It induces a representation of the exterior of the not $S^3-\mathcal K$ that lifts to $\mathrm{SL}_2(\mathbb{C})$, that we denote by $\rho_n$. Since a rotation of angle $2\pi /n$ has trace $\pm 2\cos ( \pi/n)$, we have $$\chi_{\rho_n}(m)= \operatorname{tr}(\rho_n(m))= \pm 2 \cos ( \pi/n).$$ Using Proposition [\[prop:Fox\]](#prop:Fox){reference-type="ref" reference="prop:Fox"}, if $\Sigma_n\subset M_n$ is the lift of the branching locus, then $$\operatorname{tor}(M_n^3-\Sigma_n,\sigma)=\prod_{k=0}^{n-1} p_{\chi_n}( e^{2\pi i\frac{k}{n}})  =
 \prod_{k=0}^{n-1} \left( e^{4\pi i\frac{k}{n}}\mp 4\cos({\pi}/{n} ) 
e^{2\pi i\frac{k}{n}}+1\right).$$ By the surgery formula (Proposition [\[prop:SF\]](#prop:SF){reference-type="ref" reference="prop:SF"}) and knowing that the complex length of the core geodesic is $\approx  \frac{\sqrt{3}\,\pi}n + O\left(\frac{1}{n^3}\right)$ (Remark [\[rem:length\]](#rem:length){reference-type="ref" reference="rem:length"}), $$\label{eq:foxsurgery}
 \operatorname{tor}(M_n^3,\sigma)= \frac{1/2}{1-\cosh \left( \frac{\sqrt{3}\,\pi}n  + 
O\left(\frac{1}{n^3}\right) \right)} 
  \prod_{k=0}^{n-1} \left( e^{4\pi i\frac{k}{n}}\mp 4\cos( {\pi}/{n} ) 
e^{2\pi i\frac{k}{n}}+1\right).$$ In particular, $$\label{eqn:limlog/n}
\lim_{n\to\infty} \frac{\log\vert \operatorname{tor}(M_n^3,\sigma)\vert}{n}= 
 \lim_{n\to\infty} \frac{1}{n} \sum_{k=0}^{n-1} \log \left\vert  e^{4\pi 
i\frac{k}{n}}\pm 4\cos( {\pi}/{n} ) e^{2\pi i\frac{k}{n}}+1 \right\vert.$$ Here we used that $\lim_{x\to 0^+}  x\log x =0$ to get rid of the first term, outside the product, in [\[eq:foxsurgery\]](#eq:foxsurgery){reference-type="eqref" reference="eq:foxsurgery"}. As $t^2 \mp 4 t + 1$ has no roots in the unit circle, the limit [\[eqn:limlog/n\]](#eqn:limlog/n){reference-type="eqref" reference="eqn:limlog/n"} converges to $$\frac{1}{2\pi}\int_{\vert z\vert =1} \log\vert z^2\pm  4 z +1 \vert .$$ Thus by Jensen's formula $$\lim_{n\to\infty} \frac{\log\vert \operatorname{tor}(M_n^3,\sigma)\vert}{n}
 = \log\vert 2+\sqrt{3}\vert .$$

This approach uses the ideas on Mahler measure of [@SW02]. It applies to a hyperbolic knot provided that the torsion polynomial has no roots in the unit circle. It is easy to prove that the roots of the polynomial are not roots of the unity, but this does not discard roots in the unit circle. For the adjoint representation, the nonexistence of roots in the unit circle has been proved by Kapovich [@Kapovich98].
