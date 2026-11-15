---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-030-622-a-random-matrix-model-for-qcd-at-finite-dens
section_title: "A RANDOM MATRIX MODEL FOR QCD AT FINITE DENSITY"
section_number: 6.2.2
pages: 41-42
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.975
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
[]{#RMMmu label="RMMmu"}

A random matrix model for QCD at nonzero chemical potential model is obtained by writing the Dirac operator as [@Misha] $${\cal D}(\mu) = \mu \gamma_0 + {\cal R}$$ and replacing ${\cal R}$ by a chiral random matrix ensemble. The partition function is thus given by $$Z_{N_f}(m) = \int DW  {\det}^{N_f}({\cal D} +m)
  e^{-\frac12N\Sigma^2 \Tr(W^\dagger W)}
  \label{zrandommu}$$ with a Dirac operator given by $${\cal D} = \left (\begin{array}{cc} 0 & iW +\mu\\
      iW^\dagger +\mu& 0 \end{array} \right )\:.
  \label{diracopmu}$$ For QCD with three or more colors (chUE) this Dirac operator has no Hermiticity properties. Therefore, the fermion determinant in Eq. ([\[zrandommu\]](#zrandommu){reference-type="ref" reference="zrandommu"}) has a complex phase, and the partition function cannot be simulated by Monte Carlo methods.

The partition function with Dirac operator ([\[diracopmu\]](#diracopmu){reference-type="ref" reference="diracopmu"}) can be rewritten in terms of a $\sigma$-model. For $N_f= 1$, the partition function is particularly simple, $$Z(\mu) =\int d\sigma d\sigma^* [(\sigma+m)(\sigma^*+m) - \mu^2]^n
  e^{-n|\sigma|^2}\:, 
\label{zmusig}$$ where we have set $\Sigma=1$ for ease of notation. For $n=N/2\rightarrow
\infty$ the integrals can be evaluated by a saddle-point approximation. In the chiral limit, we find that [@Misha] $$\bar \sigma = \left\{
    \begin{array}{ccccl}
      0 & {\rm for} & \mu >\mu_c & \Rightarrow & Z = \mu^{2n} \\
      \sqrt{1+\mu^2} & {\rm for} & \mu < \mu_c & \Rightarrow & 
      Z = e^{-n(\mu^2 + 1)}
    \end{array}\right.$$ with $\mu_c$ given by the point where the two partition functions are equal, i.e. $\mu_c^2 = \exp(-1-\mu_c^2)$, which is solved by $\mu_c
\approx 0.53$. The vacuum properties of this partition function depend on $\mu$ for $\mu \le \mu_c$. The reason for this unphysical result is discussed below in Sec. [\[failure\]](#failure){reference-type="ref" reference="failure"}. As was demonstrated in Ref. [@Vanderheyden99] for $\beta =2$, this model does not show diquark condensation. However, a random matrix model that does show diquark condensation was formulated in Ref. [@Vanderheyden00].

The QCD partition function ([\[zrandommu\]](#zrandommu){reference-type="ref" reference="zrandommu"}) is a polynomial in $m$ and $\mu$ with coefficients that can be obtained analytically [@Halaszyl]. Its properties can be analyzed by means of its zeros in the complex chemical potential plane and the complex mass plane. Figure [1](#ylfig){reference-type="ref" reference="ylfig"} shows a first-order phase transition at $\mu
\approx 0.53$. In the chirally restored phase, the cut on the imaginary $m$ axis is no longer present. The figure also shows the points (stars) where two solutions of the saddle-point equations of the $\sigma$-model coincide. Indeed, the cuts end on these branch points.

<figure id="ylfig">
<div class="center">

</div>
<figcaption>Zeros of the partition function in the complex <span class="math inline"><em>μ</em></span> and <span class="math inline"><em>m</em></span> plane. (From Ref. <span class="citation" data-cites="Halaszyl"></span>.)</figcaption>
</figure>

In lattice QCD at finite density, the zeros of the QCD function in the complex $\mu$ plane can be studied by means of the Glasgow method [@Barbourqed]. This method has been analyzed in terms of the above random matrix model [@glasgow] with the conclusion that it requires an exponentially large number of gauge field configurations to obtain statistically significant results.
