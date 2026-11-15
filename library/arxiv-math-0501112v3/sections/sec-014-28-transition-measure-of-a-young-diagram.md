---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-014-28-transition-measure-of-a-young-diagram
section_title: "Transition measure of a Young diagram"
section_number: 2.8
pages: 8-9
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.887
latex_coverage_ratio: 0.955
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
[]{#subsec:transitionanalytic label="subsec:transitionanalytic"} To any generalized Young diagram $\omega$ we can assign the unique probability measure $\mu^{\omega}$ on ${\mathbb{R}}$, called transition measure of $\omega$, the Cauchy transform of which $$\label{eq:Cauchy} G_{\mu^{\omega}}(z)= \int_{{\mathbb{R}}} \frac{1}{z-x} d
\mu^{\omega}(x)$$ is given by $$\label{eq:definicja3} \log G_{\mu^{\omega}}(z)= -\frac{1}{2}
\int_{{\mathbb{R}}} \log(z-x)  \omega''(x) dx = -\frac{1}{2} \int_{{\mathbb{R}}}
\frac{1}{z-x} \omega'(x) dx$$

for every $z\notin{\mathbb{R}}$. For a Young diagram $\lambda$ we will write $\mu^{\lambda}$ as a short hand of $\mu^{\omega^{\lambda}}$. This definition may look artificial but it turns out [@Kerov1993transition; @OkounkovVershik1996; @Biane1998; @Okounkov2000randompermutations] that it is equivalent to natural representation-theoretic definitions which arise by studying the representation $\rho_q$ together with the inclusion $S_q\subset
S_{q+1}$.

For $p>0$ and a Young diagram $\lambda$ we consider the rescaled (generalized) Young diagram $\omega^{p \lambda}$ given by $\omega^{p
\lambda}:x \mapsto p \omega^{\lambda}\big( \frac{x}{p} \big)$. Informally speaking, the symbol $p \lambda$ corresponds to the shape of the Young diagram $\lambda$ geometrically scaled by factor $p$ (in particular, if $\lambda$ has $q$ boxes then $p \lambda$ has $p^2
q$ boxes). It is easy to see that [\[eq:definicja3\]](#eq:definicja3){reference-type="eqref" reference="eq:definicja3"} implies that the corresponding transition measure $\mu^{p \lambda}$ is a dilation of $\mu^{\lambda}$: $$\label{eq:skalowanie} \mu^{p \lambda}= D_p \mu^{\lambda}.$$ This nice behavior of the transition measure with respect to rescaling of Young diagrams makes it a perfect tool for the study of the asymptotics of symmetric groups $S_q$ as $q\to\infty$.
