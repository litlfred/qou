---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-013-42-leutwyler-smilga-sum-rules
section_title: "Leutwyler-Smilga Sum Rules"
section_number: 4.2
pages: 25-26
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.983
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
For masses in the domain of Eq. ([\[range\]](#range){reference-type="ref" reference="range"}), we can equate the mass dependence of the QCD partition function and the mass dependence of the effective partition function. Equating the coefficients of the expansion in powers of the mass then gives us the so-called Leutwyler-Smilga sum rules [@Leut92]. The QCD partition function can be expanded as $$\label{ZQCDnu}
  {Z^{\rm QCD}_\nu(m)} = \frac {\langle 
    m^{|\nu|} \prod_k'(m+i\lambda_k) \rangle}
  {\langle\prod_k' i\lambda_k\rangle}
  = m^{|\nu|}\Bigl( 1 + m^2 \Bigl\langle\sum_{\lambda_k > 0 }\frac
    1{\lambda_k^2}\Bigr\rangle +\ldots\Bigr)\:,$$ where the prime indicates that the product is over nonzero eigenvalues only. The effective partition function can be expanded in a power series in $m$ as well. From the U(1) part of the group integral, it is clear that $Z_\nu^{\rm eff}(m) \propto m^{|\nu|}$. Thus, $$\label{Zeffnu}
  Z_\nu^{\rm eff}= m^{|\nu|}(a_0 + a_1 m^2 + \ldots)\:,$$ where the coefficients $a_i$ are obtained by calculating the group integrals. Let us consider two examples. The simplest example is $N_f
=1$, for which $$Z_\nu^{\rm eff} = \frac 1{2\pi}
  \int d\theta\: e^{-i\nu \theta} e^{mV \Sigma \cos \theta}
  =I_\nu(mV\Sigma)\:.$$ The series expansion of the modified Bessel function is given by $$I_\nu(x) = \frac{1}{\nu!}\left (\frac x2\right )^\nu+ \frac 1{(\nu + 1)!} 
  \left (\frac x2\right )^{\nu+2} + \ldots$$ for $\nu\ge0$. We also have $I_{-\nu}(x)=I_\nu(x)$. Matching the normalizations of Eqs. ([\[ZQCDnu\]](#ZQCDnu){reference-type="ref" reference="ZQCDnu"}) and ([\[Zeffnu\]](#Zeffnu){reference-type="ref" reference="Zeffnu"}) and equating the coefficients of the $O(m^2)$ terms, we find $$\left\langle\frac 1{V^2} \sum_{\lambda_k > 0} \frac
  1{\lambda_k^2}\right\rangle= \frac{\Sigma^2}{4(|\nu|+1)}\:.$$ A second example is the case of $\nu = 0$ and arbitrary $N_f$. In this case, we use the group integral $$\int DU \:U_{ij} U^\dagger_{kl} = \frac 1{N_f} \delta_{jk} \delta_{il}$$ to derive the result $$\left\langle\frac 1{V^2} \sum_{\lambda_k > 0}\frac
    1{\lambda_k^2}\right\rangle = \frac{\Sigma^2}{4N_f}\:.$$ Since asymptotically for large $\lambda$ the spectral density is proportional to $V\lambda^3$, the sum over the eigenvalues has to be regularized. As discussed above in Sec. [\[diracspectrum\]](#diracspectrum){reference-type="ref" reference="diracspectrum"}, a finite result is obtained by taking the thermodynamic limit before removing the cutoff.

What do we learn from these sum rules? Since the total number of eigenvalues is of order $V$, the obvious interpretation is that the smallest eigenvalues are of order $1/V$. Indeed, this is in agreement with the Banks-Casher formula. What is more important, however, is that in the derivation of the sum rules we have relied only on the chiral symmetry of the partition function and its spontaneous breaking by the formation of a chiral condensate. Therefore any theory with the same pattern of chiral symmetry breaking as QCD should obey the same spectral sum rules. In particular, the eigenvalues distributed according to the chRMT introduced in the previous section should obey the same sum rules. In fact, all Leutwyler-Smilga sum rules can be derived systematically from the joint eigenvalue chRMT probability distribution in Eq. ([\[zeig\]](#zeig){reference-type="ref" reference="zeig"}) using the known Selberg integrals [@sell]. In addition to these sum rules, it is possible to derive massive sum rules [@lsmass]. A relation between sum rules and partially quenched effective theories was considered in Ref. [@zyab]. Spectral sum rules for Ginsparg-Wilson fermions on the lattice were considered in Ref. [@Farc99c]. Inverse moments of the small Dirac eigenvalues in generalized chiral perturbation theory were derived in Ref. [@Desc99].

We have seen that chRMT allows us to calculate the correlations of the smallest eigenvalues of the Dirac operator on the scale of the average level spacing. This raises the question of whether it is possible to derive the microscopic properties of the eigenvalues from the low-energy effective partition function. The answer is no. The spectral density cannot be derived from the mass dependence of the chiral condensate, $$\Sigma(m) =\left \langle\frac 1V \sum_k \frac
    1{i\lambda_k+m}\right\rangle,$$ because the average contains the fermion determinant with the same mass. As we show in the next section, this problem can be circumvented by the introduction of a spectral mass.
