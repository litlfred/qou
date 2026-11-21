---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-034-63-phase-diagram-for-the-qcd-partition-function
section_title: "Phase Diagram for the QCD Partition Function"
section_number: 6.3
pages: 46-48
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.972
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
The random matrix models at nonzero temperature and nonzero chemical potential introduced in the previous sections can be merged into a single schematic chRMT model for the chiral phase transition [@phase], $$Z = \int DW {\det}^{N_f} \left ( \begin{array}{cc} m & iW + iC\\
      iW^\dagger +iC& im \end{array}\right )
  e^{-\frac12N\Sigma^2\Tr WW^\dagger}\:,
  \label{Zmut}$$ where $C$ is a diagonal matrix with $C_{kk}= t -i\mu$ for one half of the diagonal elements and $C_{kk}=-t-i\mu$ for the other half. In the following, we set $\Sigma=1$ for simplicity.

This random matrix partition function can be rewritten as a $\sigma$-model. For the case $N_f = 1$ it is given by $$Z(t,\mu) = \int d\sigma e^{-\frac{N}{2}\Tr\Omega (\sigma)}\:,$$ where $$\begin{aligned}
  \Omega(\sigma) &\!\!\!=\!\!\!& \sigma \sigma^* 
  -\frac12\log [(\sigma+m)(\sigma^* + m) - (\mu+it)^2]\nonumber \\
  &&\phantom{\sigma \sigma^*}-\frac12\log [(\sigma+m)(\sigma^* + m) 
  - (\mu-it)^2]\:.
\end{aligned}$$ For $t = 0$ this is exactly the $\sigma$-model discussed in Sec. [\[RMMmu\]](#RMMmu){reference-type="ref" reference="RMMmu"}. At the saddle point, the chiral condensate is given by the expectation value of $\sigma$. For $m= 0$ the saddle-point equation is of fifth order in $\sigma$, $$\sigma[\sigma^4 - 2(\mu^2 -t^2 +\frac 12)\sigma^2 
  + (\mu^2+t^2)^2 +\mu^2 -t^2] =0\:.
  \label{saddlemut}$$ The critical points occur where one of the solutions of the quartic equation merges with the solution $\sigma = 0$, i.e. along the curve $(\mu^2+t^2)^2 +\mu^2 -t^2 =0$. At the tricritical point, three solutions merge. This happens if in addition $\mu^2 -t^2 +\frac 12=0$.

<figure id="fig:3dRM">
<div class="center">

</div>
<figcaption>Phase diagram of QCD with two light flavors of mass <span class="math inline"><em>m</em></span> as calculated from the random matrix model. The almost parallel curves on the wing surface are cross sections of this surface with <span class="math inline"><em>m</em>=</span>constant planes. (From Ref. <span class="citation" data-cites="phase"></span>.)</figcaption>
</figure>

Figure [1](#fig:3dRM){reference-type="ref" reference="fig:3dRM"} shows the phase diagram in the $\mu t
m$-space. In the $m=0$ plane, we observe a line of second-order phase transitions and a line of first-order phase transitions. They join at the tricritical point. Also joining at the tricritical point is a line of second-order phase transitions in the $m$-direction, which is the boundary of the plane of first-order transitions in $\mu
tm$-space. This line is the collection of end points of lines of first-order phase transitions. We expect that the critical exponents for such a liquid-gas transition are given by the three-dimensional Ising model. The tricritical point was also found in a Nambu--Jona-Lasinio model [@italians; @krish3].

Because the saddle-point equation ([\[saddlemut\]](#saddlemut){reference-type="ref" reference="saddlemut"}) is of fifth order in $\sigma$, the critical properties of the random matrix model ([\[Zmut\]](#Zmut){reference-type="ref" reference="Zmut"}) are very similar to those of a $\phi^6$-theory. The critical dimension at the tricritical point of such theories is three, so that mean field theory, and therefore RMT, describes the correct critical behavior at this point. This random matrix model can be considered as the matrix equivalent of a Landau-Ginzburg functional. The advantage over using the standard Landau-Ginzburg theory is that in this case the spectrum of the Dirac operator is also accessible. This allows us to study the critical properties of the Dirac eigenvalues. For example, for $\mu = 0$ we have found that the distribution of the smallest nonzero eigenvalue of the Dirac operator may serve as an order parameter for the chiral transition [@JV].
