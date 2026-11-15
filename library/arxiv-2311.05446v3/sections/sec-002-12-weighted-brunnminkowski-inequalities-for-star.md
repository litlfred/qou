---
doc_id: arxiv-2311.05446v3
doc_title: "New Brunn--Minkowski and functional inequalities via convexity of entropy"
section_id: sec-002-12-weighted-brunnminkowski-inequalities-for-star
section_title: "Weighted Brunn–Minkowski inequalities for star bodies"
section_number: 1.2
pages: 3-5
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.968
doc_brief: "New Brunn--Minkowski and functional inequalities via convexity of entropy — We study the connection between the concavity properties of a measure ν and the convexity properties of the associated"
---
Despite the difficulties mentioned above when dealing with non-convex sets, in this paper we prove the following theorem:

::: thm
[]{#thm:main-BM intro label="thm:main-BM intro"}Let $V:\mathbb{R}^{n}\to[0,\infty)$ be a $p$-homogeneous convex function for $1<p<\infty$, and let $\nu$ be a measure with density $\frac{\mathrm{d}\nu}{\mathrm{d}x}$ proportional to $e^{-V}$. Let $K_{0},K_{1}\subseteq\mathbb{R}^{n}$ be star bodies. Then for all $0\le t \le1$ we have $$\text{\ensuremath{\nu\left((1-t)K_{0}+t K_{1}\right)^{\frac{p-1}{pn}}\ge(1-t)\nu(K_{0})^{\frac{p-1}{pn}}+ t \nu\left(K_{1}\right)^{\frac{p-1}{pn}}.}}$$
:::

To explain the terminology, we say that $K\subseteq\mathbb{R}^{n}$ is a star body if $K$ is a Borel set such that for all $x\in K$ and $0\le \lambda \le1$ we have $\lambda x\in K$ (i.e. the "star" of $K$ is always assumed to be at the origin). Also recall that $V$ is $p$-homogeneous if $V(\lambda x)=\lambda^{p}V(x)$ for all $x\in\mathbb{R}^{n}$ and $\lambda>0$.

Note that one specific choice, $V(x)=\frac{1}{2}\left|x\right|^{2}$, gives the KolesnikovLivshyts result ([\[eq:gassian-BM-2n\]](#eq:gassian-BM-2n){reference-type="eqref" reference="eq:gassian-BM-2n"}), but this time without the convexity assumption on the sets. For any fixed $p>1$ the exponent $\frac{p-1}{pn}$ is asymptotically (for large $n$) better than the result of [@Livshyts23], and again we need no convexity or symmetry assumptions, but of course our result is only for homogeneous potentials and not for all log-concave measures. Note that as $p\to\infty$ we have $\frac{p-1}{pn}\to\frac{1}{n}$, the optimal exponent. This makes sense since for large $p$ the measure $\nu$ is almost uniform on some convex body, and such uniform measures do satisfy the BrunnMinkowski inequality with exponent $\frac{1}{n}$, applicable to all Borel sets.

As mentioned above, as far as we know none of the previously used techniques can prove a result like Theorem [\[thm:main-BM intro\]](#thm:main-BM intro){reference-type="ref" reference="thm:main-BM intro"}. Our proof will therefore follow completely different lines, using tools of optimal transport and information theory. We lift the problem at hand from the realm of geometry of sets to the realm of geometry of measures, where calculus is sometimes "smoother" than in classical differential geometry. Arguably, even for the Gaussian measure, our proof is simpler than the known arguments.

The theory of optimal transport gives us a natural way to interpolate between two probability measures $\mu_{0}$ and $\mu_{1}$, such that the interpolant $\mu_{t}$ is supported in the Minkowski average $(1-t) \cdot \textnormal{support}(\mu_{0}) + t \cdot \textnormal{support}(\mu_{1})$ of the two supports, thereby playing a role parallel to the Minkowski averaging of sets. Along these interpolations, the relative entropy $D(\cdot \Vert \nu)$ enjoys convexity properties of various degrees depending on $\nu$. The reader will find precise definitions in Section [\[sec: overview\]](#sec: overview){reference-type="ref" reference="sec: overview"}. However, the main point is that a variational formula for $\nu$ can be written in terms of the relative entropy $D(\cdot \Vert \nu)$, $$\label{eq: variationalmeasureIntro}
\sup_{\mu \in \mathcal{P}(K)} e^{- D(\mu \Vert \nu)} = \nu (K),$$ where the supremum runs over all probability measures on $K$ and is attained at the normalized restriction $\nu_{K}$ of $\nu$ to $K$, allowing us to translate convexity properties of the relative entropy into concavity properties of the measure $\nu$.

Since the density $\frac{\textnormal{ d}\nu_{K}}{ \textnormal{ d}\nu}$ is radially decreasing when $K$ is a star body, we will obtain Theorem [\[thm:main-BM intro\]](#thm:main-BM intro){reference-type="ref" reference="thm:main-BM intro"} as a corollary to the following result.

::: thm
[]{#thm:main-entropy label="thm:main-entropy"}Let $V:\mathbb{R}^{n}\to[0,\infty)$ be a $p$-homogeneous convex function for $1<p<\infty$, and let $\nu$ be the probability measure with density proportional to $e^{-V}$. Let $\mu_{0}$, $\mu_{1}$ be Borel probability measures, absolutely continuous with respect to $\nu$, such that $\frac{\mathrm{d}\mu_{0}}{\mathrm{d}\nu}$ and $\frac{\mathrm{d}\mu_{1}}{\mathrm{d}\nu}$ are radially decreasing. Finally, let $\left\{ \mu_{t}\right\} _{t\in[0,1]}$ be the displacement interpolation between $\mu_{0}$ and $\mu_{1}$. Then $$t\mapsto e^{-\frac{p-1}{pn}\operatorname{D}\left(\mu_{t}\middle\Vert\nu\right)}$$ is concave.
:::

It is well known that the behavior of information-theoretic quantities under optimal transport is intimately related to the geometry of the underlying space, which is useful in the context of BrunnMinkowski type inequalities (see for example Remark [\[rem: cdhistory\]](#rem: cdhistory){reference-type="ref" reference="rem: cdhistory"}). There are known proofs of the classical BrunnMinkowski or PrékopaLeindler inequalities along these lines ([@Villani03 Chapter 6]). However, to the best of our knowledge this is the first time such tools are used to prove previously unknown BrunnMinkowski type inequalities for measures on Euclidean space.

To prove Theorem [\[thm:main-entropy\]](#thm:main-entropy){reference-type="ref" reference="thm:main-entropy"} we split the relative entropy $D(\mu \Vert \nu)$ of a measure $\mu$ into its "internal energy" $D(\mu \Vert \textnormal{Vol}_{n})$ and "potential energy" $\int V \textnormal{ d}\mu$ components. We observe that, under the assumptions on $\mu_{0}$ and $\mu_{1}$ as in Theorem [\[thm:main-entropy\]](#thm:main-entropy){reference-type="ref" reference="thm:main-entropy"}, $e^{- \frac{p-1}{n} \int V \textnormal{ d}\mu_{t}}$ is concave in $t$. Theorem [\[thm:main-entropy\]](#thm:main-entropy){reference-type="ref" reference="thm:main-entropy"} is then obtained by combining our observation with a result of Erbar, Kuwada, and Sturm [@ErbarKuwadaSturm15] that $e^{- \frac{1}{n} D(\cdot \Vert \textnormal{Vol}_{n})}$ is concave along all displacement interpolations. The aforementioned convexity property of the potential energy is established locally, that is, by taking two derivatives.
