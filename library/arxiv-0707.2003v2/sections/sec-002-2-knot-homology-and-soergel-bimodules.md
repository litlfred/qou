---
doc_id: arxiv-0707.2003v2
doc_title: "A geometric model for Hochschild homology of Soergel bimodules"
section_id: sec-002-2-knot-homology-and-soergel-bimodules
section_title: "Knot homology and Soergel bimodules"
section_number: 2
pages: 5-7
source_pdf: 0707.2003v2.pdf
source_sha256: 0b8fe37aabeee412
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 1.0
doc_brief: "A geometric model for Hochschild homology of Soergel bimodules — An important step in the calculation of the triply graded link homology theory of Khovanov and Rozansky is the determination of the"
---
[]{#sec:knot-homol-soerg label="sec:knot-homol-soerg"}

While Soergel bimodules merit study simply by being connected so much delightful mathematics, we have applications in knot theory in mind, as we will now briefly describe. The interested reader can find more details in the papers of Khovanov [@Kho05], Rasmussen [@Ras06], and Webster [@Web06a].

The braid group $B_G$ of $G$ is a finitely presented group, with generators $\si_s$ for each simple reflection $s\in W$, which is defined by the presentation $$\begin{aligned}
 \si_s\si_t&=\si_t\si_s & \big(\text{when }(st)^2=e\big)\\
 \si_s\si_t\si_s&=\si_t\si_s\si_t & \big(\text{when }(st)^3=e\big)\\
(\si_s\si_t)^2&=(\si_t\si_s)^2 & \big(\text{when }(st)^4=e\big)\\
(\si_s\si_t)^3&=(\si_t\si_s)^3 & \big(\text{when }(st)^6=e\big)
\end{aligned}$$ Note that if $G=\SL n$, then $B_n=B_G$ is the standard braid group familiar from knot theory.

There are several natural weak actions of the braid group on category $\mc O$ by families of functors (see, for example, [@AS; @KM]), which have an avatar on the bimodule side of the picture in the form of a complex of bimodules attached to each braid group element. The description of these bimodule complexes can be found in various sources, for example [@Kho05], or for general Coxeter groups in [@Rou04].

Define the complexes of $S$-bimodules: $$\begin{aligned}
  F(\si_s)&=\cdots\longrightarrow \HT[-1]\longrightarrow \S{s}\longrightarrow  \hspace{2.5mm}0 \hspace{2.5mm}\longrightarrow \cdots\\
  F(\si_s^{-1})&=\cdots\longrightarrow \hspace{4mm}0 \hspace{4mm}\longrightarrow \S{s}\longrightarrow \HT[1]\longrightarrow \cdots
\end{aligned}$$ where the maps between non-zero spaces are the unique (up to scalar) non-zero maps of degree 0. These maps are defined by (respectively) the pushforward and pullback in $\BB$-equivariant cohomology for the inclusion $B\hookrightarrow \overline{BsB}$.

::: thm
The shuffling complex $$F(\si)=F(\si_{i_1}^{\ep_1})\otimes_{\HT}\cdots \otimes_{\HT}F(\si_{i_m}^{\ep_m})$$ of a braid $\si=\si_{i_1}^{\ep_1}\cdots\si_{i_m}^{\ep_m}$ (where $\ep_i=\pm 1$) depends up to homotopy only on $\si$ not its factorization. In particular, $$F(\si\si')=F(\si)\otimes_{\HT}F(\si'),$$ so $F$ defines a categorification of $B_G$.
:::

The maps in this complex also have a geometric interpretation: each degree is a direct sum of Bott-Samelson modules for subsequences of $\Bi$, and the "matrix coefficients" of the differential between these are induced by pullback or pushforward maps on $\BB$-equivariant cohomology for inclusions $\BS{\Bi'}\to\BS{\Bi''}$ of Bott-Samelson spaces where $\Bi'$ and $\Bi''$ are subsequences of $\Bi$ which differ by a single index.

Even better, this complex can be used to find a knot invariant, as was shown by Khovanov [@Kho05]. Let $\HH_*(\S{})$ be the Hochschild homology of $\S{}$, which can be defined (using the standard equivalence between $\HT-\HT$-bimodules with $\HT\otimes\HT^{op}$) by $$\HH_i(\S{})=\Tor^i_{\HT\otimes\HT^{op}}(\HT,\S{}).$$ This can be calculated by the Hochschild complex of $\HT$ (which is often used as a definition), or by the Koszul complex, both of which are free resolutions of $\HT$ as an $\HT\otimes\HT^{op}$-module.

In the case where $G=\SL n$, Hochschild homology is a categorification of the trace on the braid group defined by Jones [@Jon87]. Remarkably, combining these creates a categorification of knot polynomials, which had previously been defined by Khovanov and Rozansky.

::: thm
(Khovanov, [@Kho05]) As a graded vector space, the homology $\KR(\bar\si)$ of the complex $\HH_i(F( \si))$ is depends only on the knot $\bar\si$, and in fact, is precisely the triply graded homology defined by Khovanov and Rozansky in [@KR05].
:::

Applying Theorem [\[sec:introduction-1\]](#sec:introduction-1){reference-type="ref" reference="sec:introduction-1"} to our remarks above, we can understand the differentials of the complex $\HH_i(F( \si))$ in terms of pullback and pushforward on $B$-equivariant cohomology.
