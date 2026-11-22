---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-031-623-zero-temperature-limit
section_title: "ZERO TEMPERATURE LIMIT"
section_number: 6.2.3
pages: 42-44
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.935
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
The random matrix model discussed in the previous section has attracted a great deal of interest, and more sophisticated versions of this model have been proposed [@Feinnh; @Halaszyl; @Osbornmu; @Nowak; @glasgow]. One problem of the model ([\[zrandommu\]](#zrandommu){reference-type="ref" reference="zrandommu"}) is that the chiral condensate is $\mu$-dependent below the critical value of the chemical potential. The correct zero temperature limit, with a chiral condensate that remains constant up to the critical value of the chemical potential, is obtained if all Matsubara frequencies are taken into account. We illustrate this with a one-dimensional lattice QCD model.

Writing the Dirac operator as $${\cal D}(\mu) = \gamma_0 (\partial_0+\mu) + R\:, 
  \label{Dmur}$$ the $\mu$-dependence of the fermion determinant can be gauged away by means of a time-dependent gauge transformation, i.e. $$\gamma_0 (\partial_0+\mu) + R = e^{-\mu\tau}
  \left [\gamma_0\partial_0  + R \right ] e^{\mu\tau}\:.$$ The $\mu$-dependence is now in the boundary conditions, but for $T\to0$ we expect that they are not important and that the partition function becomes independent of $\mu$. The lesson is that in order to obtain a condensate that is $\mu$-independent, one must treat the time derivative exactly, or, in other words, all Matsubara frequencies have to be taken into account. This was first worked out in detail for lattice QCD models at nonzero chemical potential [@matstone]. Let us discuss the strong coupling limit of a one-dimensional SU($N_c$) lattice QCD model with Kogut-Susskind fermions [@Bilic]. In that case, the matrix elements of the discretized Dirac operator are given by $${\cal D}_{kl} = \delta_{k,l-1} U_{kl} e^{\mu} -
  \delta_{k,l+1} U^\dagger_{kl} e^{-\mu} \:,$$ where the indices are modulo $N$, the number of lattice sites. Antiperiodic boundary conditions result in an extra minus sign for the matrix elements ${\cal D}_{1N}$ and ${\cal D}_{N1}$. The matrices $U_{kl}$ are independent SU($N_c$) matrices. By using gauge invariance, one can reduce this partition function to a single SU($N_c$) integral, which can be performed analytically, resulting in the partition function $$Z_N = 2 \cosh(N_c N \mu) +
  \frac{\sinh [(N_c +1) N \sinh^{-1}m]}{\sinh[ N \sinh^{-1} m]}\:.$$ The number of lattice sites $N$ can be interpreted as the total number of Matsubara frequencies. A sharp transition is obtained in the limit $N \rightarrow \infty$. For example, the chiral condensate is given by [@Bilic] $$\lim_{N\to\infty}\frac 1N \partial_m \log Z_N = \left\{
    \begin{array}{cl}
      N_c/\sqrt{1+m^2} & \hbox{for $\sinh \mu <m$}\:,\\
      0 & \hbox{for $\sinh \mu  > m$}\:.
    \end{array}\right.$$ Similar results have been derived for a large-$d$ strong coupling expansion of lattice QCD at finite density [@strong] (with $d$ the Euclidean dimensionality). The failure of the quenched approximation has been reproduced in such lattice models. The effect of including all Matsubara frequencies has also been investigated in a random matrix model obtained by replacing the remainder $R$ in Eq. ([\[Dmur\]](#Dmur){reference-type="ref" reference="Dmur"}) by a chiral random matrix. After ensemble averaging, one obtains a similar partition function with similar conclusions [@papp].
