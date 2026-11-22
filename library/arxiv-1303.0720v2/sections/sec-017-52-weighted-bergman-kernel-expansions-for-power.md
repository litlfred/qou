---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-017-52-weighted-bergman-kernel-expansions-for-power
section_title: "Weighted Bergman kernel expansions for power weights"
section_number: 5.2
pages: 10-11
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.993
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We should observe first that the above setting of power weights $\omega=\mathrm{e}^{-2mQ}$ has a natural extension to the setting of line bundles over (usually compact) complex manifolds in one or more dimensions. As the Bergman kernel is of geometric importance, it has been studied extensively in the line bundle setting (see, e.g., [@mm]). To make matters more precise, suppose we are given a (compact) complex manifold $\mathcal{X}$ and a holomorphic line bundle $L$ over $\mathcal{X}$ supplied with an Hermitian metric $h$, where in our above simplified setting $h\sim \mathrm{e}^{-2Q}$ is a local representation of the metric $h$. Next, if $m$ is a positive integer, the weight $\mathrm{e}^{-2mQ}$ appears when as the local metric associated with the tensor power $L^{\otimes m}$ of the line bundle $L$. This is often done because the initial line bundle $L$ might have admit only very few holomorphic sections.

To be even more precise, the one-variable analogue of the weight which is studied in the context of general complex manifolds is $\mathrm{e}^{-2mQ}\varDelta Q$, and it is clearly necessary to ask that $\varDelta Q$ is nonnegative.

Here, we shall stick to the choice of weights $\omega=\mathrm{e}^{-2mQ}$ which seems more basic.

It is -- as mentioned previously -- generally speaking a difficult task to obtain the weighted Bergman kernel explicitly. Instead, we typically need to resort to approximate formulae. Provided that the potential $Q$ is sufficiently smooth with $\varDelta Q>0$, the weighted Bergman kernel has an asymptotic expansion (up to an error term of order $\mathrm{O}(m^{-k})$) $$K_m(z,w) \sim \Lfun^{\langle k\rangle}(z,w)\mathrm{e}^{2mQ(z,w)} 
=\{m \Lfun_{0}(z,w) + \Lfun_{1}(z,w) + \dots + m^{-k+1} 
\Lfun_{ k}(z,w) \}\, \mathrm{e}^{2mQ(z,w)} 

\label{eq-asexp1.01}$$ near the diagonal $z=w$.

Here, the function $Q(z,w)$ is a local polarization of $Q(z)$, i.e., it is an almost holomorphic function of $(z,\bar w)$ near the diagonal $z=w$ with $Q(z,z) = Q(z)$. For details on local polarizations, see, e.g., [@bbs], [@ahm3]. It is implicit in [\[eq-asexp1.01\]](#eq-asexp1.01){reference-type="eqref" reference="eq-asexp1.01"} that $$\Lfun^{\langle k\rangle}(z,w)
=m \Lfun_{0}(z,w)+\Lfun_{1}(z,w)+\cdots +m^{-k+1}\Lfun_{k}(z,w),   
\label{eq-asexp1.02}$$ where each term $\Lfun_{j}(z,w)$ is holomorphic in $(z,\bar w)$ near the diagonal $z=w$. The asymptotic expansion [\[eq-asexp1.01\]](#eq-asexp1.01){reference-type="eqref" reference="eq-asexp1.01"} was developed in the work of Tian [@tian], Yau [@yau], Zelditch [@zel], and Catlin [@cat]. We should mention that in a different but related setting, some of the earliest results on asymptotic expansion of Bergman kernels were obtained by Hörmander [@horm] and Fefferman [@feff]. As for the asymptotics [\[eq-asexp1.01\]](#eq-asexp1.01){reference-type="eqref" reference="eq-asexp1.01"}, various approaches have been developed, see e.g. [@tian], [@mm], [@liulu], [@bbs], [@dougklev]. In [@lu], Lu worked out the first four terms explicitly using the peak section method of Tian.

Later, Xu [@xu] obtained a closed graph-theoretic formula for the general term of the expansion.
