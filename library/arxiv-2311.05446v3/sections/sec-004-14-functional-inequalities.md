---
doc_id: arxiv-2311.05446v3
doc_title: "New Brunn--Minkowski and functional inequalities via convexity of entropy"
section_id: sec-004-14-functional-inequalities
section_title: "Functional Inequalities"
section_number: 1.4
pages: 6-8
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.967
doc_brief: "New Brunn--Minkowski and functional inequalities via convexity of entropy — We study the connection between the concavity properties of a measure ν and the convexity properties of the associated"
---
While we cannot answer Question [\[qstn: poincare\]](#qstn: poincare){reference-type="ref" reference="qstn: poincare"} in full generality, the case where $\mu_0$ or $\mu_1$ is $\gamma$ itself does suffice to prove several fundamental functional inequalities.

The HWI inequality, originally introduced by Otto and Villani in [@OttoVillani00], asserts a relationship between the three elemental quantities--- $D(\cdot \Vert \gamma), \mathscr{W}_{2}(\cdot, \gamma)$, and $I(\cdot \Vert \gamma)$. The "H" in HWI stands for relative entropy (as it is sometimes denoted), "W" is for the Wasserstein distance, and "I" for Fisher information. Recall that, if $P^{\ast}_{s} \mu$ denotes the evolution of the measure $\mu$ under the Ornstein--Uhlenbeck process at time $s$, then the Fisher information is $I(\mu \Vert \gamma) = - \left. \frac{\textnormal{ d}}{\textnormal{ d}s} D(P^{\ast}_{s} \mu \Vert \gamma) \right|_{s=0}$. Using the methods from [@ErbarKuwadaSturm15], we obtain the following strengthening of the Gaussian HWI inequality for even strongly log-concave measures as a consequence of our results.

::: thm
[]{#thm: HWIintro label="thm: HWIintro"} Let $\mu$ be an even strongly log-concave probability measure on $\mathbb{R}^n$. Suppose $\{ \mu_{0}, \mu_{1} \} = \{ \mu , \gamma \}$. Then, $$\label{eq: HWIintro}
        e^{\frac{D(\mu_{0} \Vert \gamma)}{n} - \frac{D(\mu_{1} \Vert \gamma)}{n}} \leq \cos \left( \sqrt{\frac{2}{n}}\mathscr{W}_{2}(\mu_{0}, \mu_{1}) \right) + \frac{1}{\sqrt{2n}} \sin \left(  \sqrt{\frac{2}{n}} \mathscr{W}_{2}(\mu_{0}, \mu_{1}) \right) \sqrt{I(\mu_{0} \Vert \gamma)}.$$
:::

The original HWI inequality of Otto--Villani ([@OttoVillani00 Theorem 3]) for the Gaussian measure, which is valid without symmetry or log-concavity assumptions on $\mu$, states that $$\label{eq: originalHWI}
D(\mu_{0} \Vert \gamma) - D(\mu_{1} \Vert \gamma) \leq \mathscr{W}_{2}(\mu_{0}, \mu_{1}) \sqrt{I(\mu_{0} \Vert \gamma)} - \frac{1}{2} \mathscr{W}_{2}^{2} (\mu_{0}, \mu_{1}).$$ To compare our inequality [\[eq: HWIintro\]](#eq: HWIintro){reference-type="eqref" reference="eq: HWIintro"} with the original HWI inequality [\[eq: originalHWI\]](#eq: originalHWI){reference-type="eqref" reference="eq: originalHWI"}, the reader may raise both sides of [\[eq: HWIintro\]](#eq: HWIintro){reference-type="eqref" reference="eq: HWIintro"} to the power $n$ and send $n \to \infty$. A key feature of HWI type inequalities, perhaps even the motivation behind it in [@OttoVillani00], is that they unify two other important families of inequalities. At one end, by setting $\mu_{0} = \mu$ and $\mu_{1} = \gamma$ in Theorem [\[thm: HWIintro\]](#thm: HWIintro){reference-type="ref" reference="thm: HWIintro"}, after some elementary manipulations, we get a refinement of the Gaussian Logarithmic Sobolev inequality. Although first popularized in the mathematical community through a contribution of Gross ([@Gross75]), the Gaussian Logarithmic Sobolev inequality had previously appeared in the work of Federbush ([@Federbush69]) and even earlier as an information-theoretic uncertainty principle by Stam ([@Stam59]).

::: cor
Let $\mu$ be an even strongly log-concave probability measure on $\mathbb{R}^n$. Then, $$4 D(\mu \Vert \gamma) \leq 2n \left( e^{\frac{2}{n}D(\mu \Vert \gamma)} - 1 \right) \leq I( \mu \Vert \gamma).$$ Therefore, $$D(P^{\ast}_{t} \mu \Vert \gamma ) \leq e^{-4t} D(\mu_{0} \Vert \gamma).$$
:::

On the other hand, with $\mu_{0} = \gamma$ and $\mu_{1} = \mu$, the transportation cost-information inequality of Talagrand ([@Talagrand96]) is improved for even strongly log-concave probability measures.

::: cor
Let $\mu$ be an even strongly log-concave probability measure on $\mathbb{R}^n$. Then, $$\mathscr{W}_{2}^{2} (\mu , \gamma) \leq - n \log \cos \left( \sqrt{\frac{2}{n}} \mathscr{W}_{2}(\mu, \gamma) \right) \leq D(\mu \Vert \gamma).$$
:::

The original inequalities assert $2D (\mu \Vert \gamma) \leq I(\mu \Vert \gamma)$ and $\frac{1}{2} \mathscr{W}_{2}^{2}(\mu, \gamma) \leq D(\mu \Vert \gamma)$, respectively, for all probability measures $\mu$. Thus, even if we completely ignore the dimensional improvements that we have obtained, both the Gaussian Logarithmic Sobolev and the Talagrand inequalities show an improvement by a multiplicative factor of $2$ when restricted to even strongly log-concave measures. From examples presented in the main body of the text (see Examples [\[exmpl: betterlsineedsslc\]](#exmpl: betterlsineedsslc){reference-type="ref" reference="exmpl: betterlsineedsslc"} and [\[exmpl: bettertalagrandneedsslc\]](#exmpl: bettertalagrandneedsslc){reference-type="ref" reference="exmpl: bettertalagrandneedsslc"}), the reader will see that both assumptions--- central symmetry and strong log-concavity of the measure, are essential for this improvement. Dimensional improvements in Gaussian functional inequalities have been pursued before, for example, in the works of Bakry and Ledoux ([@BakryLedoux06]), Bobkov, Gozlan, Roberto, and Samson ([@BobkovGozlanRobertoSamson14]), and more recently, Bolley, Gentil, and Guillin ([@BolleyGentilGuillin18]). However, none of these results gives the multiplicative improvement we get by restricting to even strongly log-concave measures. Readers interested in dimension-dependent functional inequalities may also consult [@BakryBolleyGentil12; @BakryBolleyGentil17; @EskenazisShenfeld24; @Shenfeld24].

The rest of this paper is organized as follows. In Section [\[sec: overview\]](#sec: overview){reference-type="ref" reference="sec: overview"} we give the necessary background on optimal transport and describe the previous works on displacement concavity of entropy. In Section [\[sec: dimconhomo\]](#sec: dimconhomo){reference-type="ref" reference="sec: dimconhomo"} we give the relatively short proofs of Theorems [\[thm:main-BM intro\]](#thm:main-BM intro){reference-type="ref" reference="thm:main-BM intro"} and [\[thm:main-entropy\]](#thm:main-entropy){reference-type="ref" reference="thm:main-entropy"}.

Then, in Section [\[sec: gaussian\]](#sec: gaussian){reference-type="ref" reference="sec: gaussian"} we restrict our attention to the case $\nu=\gamma$, to discuss potential improvements to convexity properties of $D(\cdot \Vert \gamma)$ beyond those established in Section [\[sec: dimconhomo\]](#sec: dimconhomo){reference-type="ref" reference="sec: dimconhomo"}. In particular we prove Theorem [\[thm: gaussianentintro\]](#thm: gaussianentintro){reference-type="ref" reference="thm: gaussianentintro"}. Finally, in Section [\[sec: gaussianapp\]](#sec: gaussianapp){reference-type="ref" reference="sec: gaussianapp"} we apply our findings from the previous section to prove functional inequalities such as Theorem [\[thm: HWIintro\]](#thm: HWIintro){reference-type="ref" reference="thm: HWIintro"} and its corollaries.
