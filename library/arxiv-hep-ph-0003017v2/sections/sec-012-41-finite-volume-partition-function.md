---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-012-41-finite-volume-partition-function
section_title: "Finite-Volume Partition Function"
section_number: 4.1
pages: 23-25
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.965
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
[]{#Finite-Volume label="Finite-Volume"} As we have seen before, chiral symmetry is spontaneously broken by the QCD vacuum. According to Goldstone's theorem, this leads to the appearance of massless modes. The Lagrangian describing the dynamics of these modes can be obtained solely from the symmetries of the QCD partition function. Goldstone modes corresponding to the symmetry-breaking pattern ${\rm SU}_R(N_f) \times {\rm SU}_L(N_f)
\rightarrow {\rm SU}_V(N_f)$ can be parameterized as $$U =  U_R U_L^{-1}$$ with $U_R \in {\rm SU}_R(N_f)$ and $U_L \in {\rm SU}_L(N_f)$. The chiral Lagrangian is constructed by the requirement that it should have the same invariance properties as the QCD Lagrangian. In particular, for $m=0$ the Lagrangian should be both Lorentz invariant and invariant under ${\rm SU}_R(N_f) \times {\rm SU}_L(N_f)$. To lowest order in the momenta (or derivatives), the kinetic term in the effective Lagrangian is uniquely given by [@Weinberg; @GaL] $$\label{Lkin}
  {\cal L}_{\rm kin} = \frac {F^2}4 \Tr \partial_\mu U \partial_\mu
  U^{-1}\:.$$ The parameter $F$ is the pion decay constant. The mass term in the QCD Lagrangian breaks the full flavor symmetry. However, the full symmetry can be restored if the mass matrix is transformed as well, $$M \rightarrow U_L M U_R^{-1}\:.$$ We require that the mass term in the effective Lagrangian satisfies this extended symmetry. To lowest order in $M$, it is therefore uniquely given by $$\label{Lmass}
  {\cal L}_m = -\frac 12\Sigma\: \Tr (MU + M^\dagger U^{-1})\:.$$ For a diagonal mass matrix, the action is therefore minimized by $U = {\bf 1}$. The normalization of the mass term is such that the mass derivative of the partition function according to Eq. ([\[massder\]](#massder){reference-type="ref" reference="massder"}) is equal to the chiral condensate $\Sigma$. The chiral Lagrangian is valid in the domain $$\label{domain1}
  m\ll \Lambda\qquad{\rm and}\qquad p \ll \Lambda\:,$$ where $p$ is the momentum and $\Lambda$ is a typical hadronic mass scale.

We will study the effective Lagrangian at finite volume in a box of volume $L^4$. Then the smallest nonzero-momentum modes are of the order $$p \sim 1/L\:.$$ The fluctuations of the zero-momentum modes, the constant fields, are not affected by the kinetic term and are limited only by the mass term. Comparing Eqs. ([\[Lkin\]](#Lkin){reference-type="ref" reference="Lkin"}) and ([\[Lmass\]](#Lmass){reference-type="ref" reference="Lmass"}), we see that in a domain where $$\label{domain2}
  \frac {m\Sigma}{F^2} \ll \frac 1{L^2}\:,$$ the fluctuations of the zero-momentum modes completely dominate the fluctuations of the nonzero-momentum modes. The mass-dependence of the effective partition function is then given by [@GL; @Leut92] $$Z(m,\theta) = \int_{U\in {\rm SU}(N_f)} DU\: e^{V\Sigma\,
    \Re\Tr Ume^{i\theta/N_f}}\:,
  \label{ZFV}$$ where we have set $M=m{\bf 1}$ and have introduced the $\theta$-dependence by the substitution $m \rightarrow
m\exp(i\theta/N_f)$ just as for the QCD partition function. Combining the conditions ([\[domain1\]](#domain1){reference-type="ref" reference="domain1"}) and ([\[domain2\]](#domain2){reference-type="ref" reference="domain2"}), we find that the finite volume partition function is valid in the domain [@GL; @Leut92] $$m \ll \frac{1}{\Lambda L^2} \ll \Lambda\:.
  \label{range}$$

The partition function for a given topological charge can be extracted from its $\theta$-dependence. Since $$Z(m,\theta) = \sum_\nu e^{i\nu\theta} Z_\nu(m)\:,$$ we obtain $Z_\nu$ by Fourier inversion. Thus, the finite volume partition function in the sector of topological charge $\nu$ is $$Z_\nu(m) = \frac 1{2\pi}\int d\theta \:e^{-i\nu\theta}Z(m,\theta) 
  =\int_{U\in {\rm U}(N_f)}DU\:{\det}^\nu U
  \:e^{V\Sigma\: \Re\Tr m U}\:,
\label{ZFVnu}$$ which coincides with Eq. ([\[Znum\]](#Znum){reference-type="ref" reference="Znum"}). The partition function ([\[ZFVnu\]](#ZFVnu){reference-type="ref" reference="ZFVnu"}) can be evaluated for arbitrary masses. The integrals were first calculated in the context of one-plaquette lattice QCD models [@brower] but later rederived by means of Itzykson-Zuber integrals [@Russian; @Guhr; @seneru].
