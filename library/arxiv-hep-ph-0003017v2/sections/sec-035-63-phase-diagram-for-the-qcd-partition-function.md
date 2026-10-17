---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-035-63-phase-diagram-for-the-qcd-partition-function
section_title: "Phase Diagram for the QCD Partition Function"
section_number: 6.3
pages: 46-50
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.988
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

## Random Matrix Triality at $\mu \ne 0$

In previous sections, we have shown that the pattern of chiral symmetry breaking and the correlations of the Dirac eigenvalues are related to the anti-unitary symmetries of the Dirac operator. Since the chemical potential occurs only in the combination $\partial_0 + \mu$, the anti-unitary symmetries at $\mu \ne 0$ are the same as for zero chemical potential. Thus for QCD with two colors and fermions in the fundamental representation the Dirac operator is real ($\beta =1$), whereas for QCD with adjoint fermions the Dirac operator is quaternion real ($\beta =4$). In the first case, the Dirac operator has the structure [@Osbornmu] $${\cal D} = \mat 0 & W+ \mu \\ -W^T +\mu & 0 \emat \quad \hbox{with
  $W$ real}.$$ In the second case, ${\cal D}$ is given by $${\cal D} = \mat 0 & W+ \mu \\ -W^\dagger +\mu & 0 \emat \quad 
  \hbox{with $W$ quaternion real}.$$ In this case, the quaternion real matrix elements of $W$ satisfy the reality relation $W_{kl}^* =\sigma_2 W_{kl} \sigma_2$. In both cases, it is easy to show that the fermion determinant is real. Furthermore, because of $$\begin{aligned}
  {\det}^{N_f} W\,{\det}^{N_f} W^T = {\det}^{2N_f} W &&
  \hbox{for $\beta = 1$},\\
  {\det}^{N_f} W\,{\det}^{N_f} W^\dagger = {\det}^{2N_f} W &&
  \hbox{for $\beta = 4$},
\end{aligned}$$ the flavor symmetry group is enhanced to U($2N_f$) in both cases (for $\nu=0$).[^1] The full flavor symmetry is broken spontaneously to Sp($2N_f$) and O($2N_f$), respectively, and is broken in the same way by the mass term. The chemical potential breaks the symmetry according to ${\rm U}(2N_f) \rightarrow {\rm U}(N_f)\times {\rm U}(N_f)$ in both cases. For both $\beta =1$ and $\beta=4$ the pseudoreality of the Dirac operator leads to Goldstone modes with a nonzero baryon number in the same way we have seen for the phase quenched partition function. An exact low-energy effective partition function valid to lowest order in $m$ and $\mu^2$ can be written down [@KSTVZ]. For an elaborate discussion of the symmetries, their breaking pattern, and the low-energy effective theory in both cases, see Ref. [@KSTVZ].

For an even number of flavors, dynamical Monte Carlo simulations are possible for $\beta =1$ and $\beta =4$, though not for $\beta=2$. However, quenched simulations have been performed for all three classes. A cut along the imaginary axis below a cloud of eigenvalues was found in instanton liquid simulations [@Thomas] for $N_c =2$ at $\mu \ne 0$, which corresponds to $\beta =1$. In lattice QCD simulations with staggered fermions for $N_c = 2$ [@baillie], a depletion of eigenvalues along the imaginary axis was observed, whereas for $N_c=3$ the eigenvalue distribution did not show any pronounced features [@everybody].

<figure id="fig:scatter">
<div class="center">

</div>
<figcaption>Scatter plot of the real (<span class="math inline"><em>x</em></span>) and imaginary (<span class="math inline"><em>y</em></span>) parts of the eigenvalues of the random matrix Dirac operator at nonzero chemical potential. The values of <span class="math inline"><em>β</em></span> and <span class="math inline"><em>μ</em></span> are given in the figures. Full curves show the analytical result for the boundary. The line along the imaginary axis for <span class="math inline"><em>β</em> = 1</span> represents the accumulation of eigenvalues on this axis. (From Ref. <span class="citation" data-cites="Osbornmu"></span>.)</figcaption>
</figure>

A chiral random matrix model for the Dirac operator at $\mu \ne 0$ in each symmetry class is obtained by drawing the matrix elements of $W$ from a Gaussian probability distribution. In the quenched approximation, the spectral properties of the random matrix Dirac operator of Eq. ([\[diracopmu\]](#diracopmu){reference-type="ref" reference="diracopmu"}) can easily be studied numerically by diagonalizing a set of matrices with the probability distribution of Eq. ([\[zrandommu\]](#zrandommu){reference-type="ref" reference="zrandommu"}). Figure [2](#fig:scatter){reference-type="ref" reference="fig:scatter"} shows results [@Osbornmu] for the eigenvalues of a few $100\times 100$ matrices for $\mu = 0.15$ (dots). The solid curves represent the analytical result for the boundary of the domain of eigenvalues derived in Ref. [@Misha] for $\beta =2$. However, the analysis can be extended [@Osbornmu] to $\beta = 1$ and $\beta
=4$, and with the proper scale factors, the solution is identical.

For $\beta =1$ and $\beta = 4$ we observe exactly the same structure as in the previously mentioned (quenched) QCD simulations. There is an accumulation of eigenvalues on the imaginary axis for $\beta = 1$ and a depletion of eigenvalues along this axis for $\beta = 4$. The depletion can be understood as follows. For $\mu = 0$ all eigenvalues are doubly degenerate. This degeneracy is broken at $\mu\ne 0$, which produces the observed repulsion between the eigenvalues.

The number of purely imaginary eigenvalues for $\beta = 1$ scales as $\sqrt N$ and is thus not visible in a leading-order saddle-point analysis. Such a $\sqrt N$ scaling is typical for the regime of weak non-Hermiticity first identified by Fyodorov et al. [@fyodorov]. Using the supersymmetric method of RMT, Efetov [@Efetovnh] obtained the $\sqrt N$ dependence analytically. The case $\beta=4$ was also analyzed analytically [@efetovsym], with results that are in complete agreement with the numerical simulations. Obviously, more work is needed in order to arrive at a complete characterization of universal features [@fyodorovpoly] of the spectrum of non-Hermitian operators.

[^1]: For $\beta=4$ and $\mu=0$, the Dirac operator satisfies the relation $(C{\cal D})^T=-C{\cal D}$ whereas $(C\mu\gamma_0)^T=C\mu\gamma_0$ (with $C$ the charge conjugation matrix). Therefore, for $\beta =4$ and $\mu \ne 0$, the Pfaffian of the Dirac operator is not defined and the fermion determinant ${\det}^{N_f/2}({\cal D}+\mu\gamma_0)$ cannot be expressed as an integral over $N_f$ Majorana fermions with flavor symmetry U($N_f$), as discussed in Sec. [\[anti-unitary\]](#anti-unitary){reference-type="ref" reference="anti-unitary"}. Instead, we write ${\det}^{N_f}({\cal D}+\mu\gamma_0)$ as an integral over $N_f$ Dirac fermions with flavor symmetry U($2N_f$).
