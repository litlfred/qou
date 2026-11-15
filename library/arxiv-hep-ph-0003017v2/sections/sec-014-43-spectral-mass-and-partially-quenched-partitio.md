---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-014-43-spectral-mass-and-partially-quenched-partitio
section_title: "Spectral Mass and Partially Quenched Partition Function"
section_number: 4.3
pages: 26-27
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.976
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
[]{#SpectralMass label="SpectralMass"}

The Dirac spectrum can be obtained from the resolvent $$\Sigma(z) =\left\langle \frac 1V\: \Tr \frac 1{{\cal D}+z} \right
  \rangle\:,$$ were the spectral mass $z$ is an independent complex variable that does not occur in the average. With purely imaginary eigenvalues the spectral density is given by the discontinuity of the resolvent across the imaginary axis, $$\frac {\rho(\lambda)}V = \lim_{\epsilon\to0}\frac 1{2\pi}
  [ \Sigma(i\lambda +\epsilon) - \Sigma(i\lambda -\epsilon)]\:.
  \label{discon}$$ This follows immediately upon writing the trace as a sum over the eigenvalues of ${\cal D}$. The generating function for the resolvent can be written down easily [@Vminn], $$Z^{\rm sp} = \left \langle \frac {{\det}^{N_f}({\cal D}+m)
      \det({\cal D}+z)}{\det({\cal D}+z')} \right \rangle_{\rm YM}\:,
  \label{Zsp}$$ where we have explicitly displayed the fermion determinant in the measure. The resolvent is then given by $$\Sigma(z) = \left. \frac 1V \partial_z Z^{\rm sp}(z,z')\right|_{z'=z}.
  \label{resol}$$ In QCD, this method was first introduced in order to derive the quenched strong coupling expansion [@Morel]. In nuclear physics and condensed matter physics, this method is known as the supersymmetric method or Efetov method for quenched disorder [@Brezin; @Efetov; @VWZ].

The determinants in the numerator can be written as fermionic integrals whereas the determinant in the denominator can be written as a bosonic integral. The partition function ([\[Zsp\]](#Zsp){reference-type="ref" reference="Zsp"}) is thus invariant under flavor symmetries that mix commuting and anticommuting degrees of freedom. More precisely, for $m=z=z'=0$ the partition function is invariant under the supergroup ${\rm
  Gl}_R(N_f+1|1) \times {\rm Gl}_L(N_f+1|1)$. In order to obtain a consistent effective theory, it is essential to extend the unitary symmetry to the general linear group Gl. We expect, as for the QCD vacuum, that chiral symmetry is spontaneously broken to the diagonal subgroup ${\rm Gl}_{\rm V}(N_f+1|1)$. The mass term explicitly breaks the full symmetry to this subgroup as well.

The effective partition function can be derived in the same way as the regular chiral Lagrangian with one complication. To obtain finite integrals, we must make sure that the integration manifold is Riemannian. This is why we have extended the flavor symmetry to the full general linear group. The integration manifold is then given by the maximum Riemannian submanifold of ${\rm
  Gl}_{\rm A}(N_f+1|1)$. In plain language, this means that we compensate the extra minus sign in the supertrace by complexifying the group parameters. The generating function is thus given by [@OTV] $$\label{zspect}
  Z^{\rm pq}=\hspace*{-17pt}\int\limits_{U\in {\hat {\rm Gl}}(N_f+1|1)} 
  \hspace*{-17pt} DU e^{\int d^4x \left[-\frac
      {F^2}4 \Str \partial_\mu U \partial_\mu U^{-1} -
      \frac{F^2m_0^2}{12}\left(\frac{\sqrt 2 \Phi_0}F  
        - \theta \right )^2 + \frac{ \Sigma}2\:
      \Str (MU + M^\dagger U^{-1})\right]}\:, \nonumber \\$$ where $i\sqrt 2\Phi_0/F = {\rm Str} \log U$. This partition function is also known as the partially quenched effective partition function. It has been used to obtain a better understanding of quenched lattice QCD results [@Maarten; @Sharpe]. The hat on Gl denotes the maximum Riemannian submanifold of ${\rm Gl}(N_f+1|1)$, and Str stands for the supertrace. An example of an explicit parameterization of $U$ will be given in the next subsection. The parameter $m_0^2$ is proportional to the topological susceptibility and results in a mass for the singlet channel that does not vanish in the chiral limit.

The perturbative formulation of this partition function was first given by Bernard and Golterman [@Maarten], and a perturbative calculation of the dependence of the condensate on the spectral mass was first performed in Ref. [@Leung]. In that case, it is acceptable to ignore the convergence properties of the effective partition function and integrate over the unitary supergroup instead.

An alternative generating function would be obtained by replacing the ratio of the two determinants by ${\det}^n({\cal D}+z)$ and putting $n
\rightarrow 0$ after having calculated the resolvent. This procedure, known as the replica trick [@edwards], successfully reproduces the asymptotic expansions of the spectral correlation functions [@asympt; @pourep]. There have been recent claims that it is possible to derive truly nonperturbative results by means of the replica trick [@kamenev; @yurk; @kanrep]. We do not believe that this can be done in general [@critique; @zirnrep; @dalmazi]. As mentioned, because of the compact/noncompact structure of the final answer, the supersymmetric formulation is the natural approach to this problem.
