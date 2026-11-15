---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-033-625-quenched-dirac-spectra
section_title: "QUENCHED DIRAC SPECTRA"
section_number: 6.2.5
pages: 44-46
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.963
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
A chRMT for quenched QCD at nonzero chemical potential is obtained by replacing the determinant in Eq. ([\[zrandommu\]](#zrandommu){reference-type="ref" reference="zrandommu"}) by its absolute value. This model can be solved analytically in the large-$N$ limit [@Misha]. However, we will follow a different approach by analyzing the corresponding effective theory [@many1]. The advantage of this approach is that the effective theory is as valid for quenched QCD as it is for the quenched chiral random matrix model.

For non-Hermitian matrices, the eigenvalues are scattered in the complex plane. Using the fact that $$\partial_{z^*} \frac 1z = \pi \delta^2(z) \:,$$ where the complex delta function is defined as $\delta^2(z) =
\delta(\Re z)\delta(\Im z)$, we find that the two-dimensional spectral density is (up to a normalization constant) given by $$\rho(\lambda) = \left .\frac 1\pi \partial_{z^*} G(z)\right
  |_{z=\lambda} \:. 
  \label{BCC}$$ The resolvent is defined as $$G(z) = \frac 1{N_f V} \partial_{z} \log Z\:,
  \label{Gz}$$ and the quenched result is obtained in the limit $N_f = 0$ of the partition function $$Z=\left\langle {\det}^{N_f}({\cal D}(\mu)+z) {\det}^{N_f}
  ({\cal D}^\dagger(\mu) + z^*)\right\rangle \:.
  \label{zpart}$$ The product in Eq. ([\[zpart\]](#zpart){reference-type="ref" reference="zpart"}) can be written as $${\det}^{N_f}({\cal D}(\mu)+z) {\det}^{N_f}( {\cal D}^\dagger(\mu) + z^*) = 
  \det \mat iW{\bf 1}_{2N_f} +B_R& \zeta \\ \zeta & iW^\dagger {\bf 1}_{2N_f}
    +B_L \emat$$ with $$B\equiv B_R=B_L = \mat \mu{\bf 1}_{N_f} & 0 \\ 0 & -\mu{\bf 1}_{N_f} 
\emat \quad {\rm and} \quad
  \zeta = \mat z{\bf 1}_{N_f} & 0 \\ 0 & z^*{\bf 1}_{N_f} \emat\:,$$ where we have displayed the degeneracy in flavor space by means of the identity matrices ${\bf 1}_{2N_f}$ and ${\bf 1}_{N_f}$. For $z=\mu
=0$, the quenched partition function is thus invariant under ${\rm
  SU}_R(2N_f)\times {\rm SU}_L(2N_f)$. This symmetry is broken spontaneously to the diagonal subgroup, ${\rm SU}_V(2N_f)$. At low energies, the effective partition function is therefore given by a partition function of Goldstone modes parameterized by matrices $U\in{\rm SU}(2N_f)$. The static effective Lagrangian is obtained from the requirement that it should have the same symmetries as the underlying microscopic partition function. The mass term was discussed in Sec. [\[Finite-Volume\]](#Finite-Volume){reference-type="ref" reference="Finite-Volume"}. The chemical potential term remains invariant under ${\rm SU}(2N_f)\times{\rm SU}(2N_f)$ transformations if at the same time $B_R$ and $B_L$, now considered as independent matrices, are transformed as $$B_R \rightarrow  U_R B_R U_R^{-1} \:, \qquad B_L \rightarrow U_L B_L
  U_L^{-1}\:.$$ The matrices $U$ in the Goldstone manifold transform as $U \to U_R U
U_L^{-1}$. To lowest nontrivial order in $\mu$, we can write two invariant combinations, $$\Tr U B_L U^{-1} B_R \qquad {\rm and} \qquad \Tr BB\:.$$ The coefficients follow from the conditions that the critical chemical potential is equal to one third of the mass of the lightest baryon and that the baryon density should vanish below $\mu_c$. For the static limit of the effective partition function, we find $$Z = \int_{U\in {\rm SU}(2N_f)} DU e^{-\frac {F^2 V}4\Tr[ U, B]
    [ U^{-1}, B] + \frac12\Sigma V \Tr (MU + M^\dagger U^{-1})}\:,
\label{zeffspec}$$ with the mass matrix given by $$M = \mat z {\bf 1}_{N_f} & 0 \\ 0 & z^* {\bf 1}_{N_f} \emat\:.$$ This partition function can be derived more elegantly by means of a local gauge invariance principle [@KST; @KSTVZ]. For real masses $z$ the Dirac operator satisfies the relation ${\rm det}({\cal D}^\dagger(\mu) + z^*)=
{\rm det}({\cal D}(-\mu) + z)$, so that the partition function defined in Eq. ([\[zpart\]](#zpart){reference-type="ref" reference="zpart"}) and the corresponding low-energy effective partition function given in Eq. ([\[zeffspec\]](#zeffspec){reference-type="ref" reference="zeffspec"}) can be interpreted as the partition function of QCD at finite isospin density [@misha-son].

Below the critical chemical potential, $\mu < m_\pi/2$, only the vacuum state contributes to the partition function, so that $$Z = e^{\Sigma V N_f(z+z^*)}\:.$$ In terms of the effective theory, the saddle point is at $U =\bf 1$. The resolvent ([\[Gz\]](#Gz){reference-type="ref" reference="Gz"}) is given by $$\label{Gzconstant}
  G(z) = \frac 1{N_f V} \partial_{z} \log Z = \Sigma\:.$$ Since $G(z)$ does not depend on $z^*$, it follows from Eq. ([\[BCC\]](#BCC){reference-type="ref" reference="BCC"}) that the spectral density is zero in the region where ([\[Gzconstant\]](#Gzconstant){reference-type="ref" reference="Gzconstant"}) holds. Because $m_\pi^2=(z+z^*)\Sigma/F^2$, see Eqs. ([\[Gmass1\]](#Gmass1){reference-type="ref" reference="Gmass1"}) through ([\[Gmass3\]](#Gmass3){reference-type="ref" reference="Gmass3"}), the condition $\mu <
m_\pi/2$ means that the spectral density vanishes everywhere except in a strip $$|\Re z| < \frac{2\mu^2 F^2}\Sigma\:.$$ For $z$ inside this strip, the Goldstone modes contribute to the partition function. In terms of the effective partition function, the saddle point rotates away from $U=\bf 1$, leading to a nonvanishing diquark condensate. The rotation of the saddle point is a generic feature of low-energy effective partition functions of non-Hermitian field theories [@supernonh; @Efetovnh; @KST; @KSTVZ; @efetovrot].

These results are in qualitative agreement with spectra of the quenched lattice QCD Dirac operator at $\mu \ne 0$ [@everybody]. The correlations of the complex eigenvalues are not so well understood, but the first lattice QCD calculations [@Tilomu] seem to confirm the theoretical expectations [@Ginibre; @fyodorov; @fyodorovpoly; @Forrestc].
