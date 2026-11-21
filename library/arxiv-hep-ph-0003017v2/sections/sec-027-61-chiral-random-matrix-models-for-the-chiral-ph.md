---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-027-61-chiral-random-matrix-models-for-the-chiral-ph
section_title: "Chiral Random Matrix Models for the Chiral Phase Transition at Nonzero Temperature"
section_number: 6.1
pages: 39-41
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.979
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
[]{#modelT label="modelT"}

The original motivation for introducing chiral random matrix models was to obtain a better understanding of the QCD Dirac spectrum for temperatures around the critical temperature for the chiral phase transition [@JV; @tilot]. The idea is to split the Dirac operator into the time derivative and a remainder that will be replaced by a chRMT, $${\cal D} = \gamma_0 \partial_0 + R\:.$$ In a chiral basis with time dependence given by $\exp [i(2n+1)\pi
T\tau]$, where $\tau$ is the Euclidean time, the first term in ${\cal
  D}$ is diagonal and is given by a direct sum of Matsubara frequencies $\omega_n = (2n+1)\pi T$. The simplest model for ${\cal
  D}$ is obtained by replacing the diagonal matrix with positive Matsubara frequencies by the identity matrix times an effective Matsubara frequency $t$, and replacing the diagonal matrix with negative Matsubara frequencies by the opposite effective Matsubara frequency. After a suitable basis change, this model can be written (in the sector of zero topological charge) as [@JV; @tilot] $$Z_{N_f}(m) = \int DW {\det}^{N_f}({\cal D}+m) 
  e^{-\frac12 N\Sigma^2 \Tr (W^\dagger W)}\:,
  \label{zrandomt}$$ where $${\cal D} = \left (\begin{array}{cc} 0 & iW +it\\
      iW^\dagger +it& 0 \end{array} \right )\:.
  \label{diracop}$$ We restrict ourselves to the unitary case ($\beta =2$) with a complex matrix $W$ of dimension $N/2$. The integral is over the real and imaginary parts of the matrix elements of $W$. For simplicity, we consider only a Gaussian probability distribution. The normalization is such that the parameter $\Sigma$ is equal to the magnitude of the chiral condensate at zero temperature, $$\Sigma=\lim_{m\to0}\lim_{N\to\infty}\frac 1{NN_f} 
  \partial_m \left.\log Z_{N_f}(m) \right|_{t=0}\:.$$

It can be shown that the effect of the fermion determinant on the macroscopic spectral density is subleading in $N_f/N$, so that $\rho(\lambda)$ can be calculated in the quenched limit. By expanding the resolvent of the Dirac operator, defined by $$G(z) = \frac 1N\:\Tr \left \langle  \frac 1{z-{\cal D}}
  \right\rangle\:,$$ in a geometric series of the random matrix, it can be shown that $g=G/\Sigma^2$ satisfies a cubic equation [@JV; @senert; @mishat], $$g^3 -2zg^2 +g(z^2-t^2 + 1/\Sigma^2) - z/\Sigma^2 = 0\:.
  \label{cubic}$$ A variant of the method by which this equation was derived in Refs. [@JV; @senert] is sometimes referred to as the Blue's function method [@zeeblue]. The spectral density, obtained from the discontinuity of the resolvent, is shown in Fig. [1](#mishaspants){reference-type="ref" reference="mishaspants"}. We observe that chiral symmetry is broken up to $t = 1/\Sigma$ with a chiral condensate given by $$\label{squareroot}
  G(T,z\rightarrow 0) = \Sigma\sqrt{1-(\Sigma t)^2}\:.$$ Above this temperature, the spectrum splits into two disconnected regions.

<figure id="mishaspants">
<div class="center">

</div>
<figcaption>The spectral density of the QCD Dirac operator as a function of an effective Matsubara frequency <span class="math inline"><em>t</em></span> that models the effect of temperature. (From Ref. <span class="citation" data-cites="mishat"></span>.)</figcaption>
</figure>

Since this model has no spacetime dependence, it should not be a surprise that all critical exponents are given by their mean field values. From Eq. ([\[squareroot\]](#squareroot){reference-type="ref" reference="squareroot"}), we see that $\beta
=1/2$. For $t\to1/\Sigma$, we find $$G \propto z^{1/3}\:,$$ resulting in another critical exponent $\delta = 3$. The spectral density at the critical point follows by taking the discontinuity of $G$ across the imaginary axis, see Eq. ([\[discon\]](#discon){reference-type="ref" reference="discon"}), and is thus given by $$\rho(\lambda) = \frac{N}{\pi} \lambda^{1/3}\:.$$ The unfolded eigenvalues in this case are given by $$x_k = \frac {3N}{4\pi} \lambda_k^{4/3}\:,$$ and a nontrivial scaling limit at $t=1/\Sigma$ is obtained by introducing the microscopic variable [@Hikami-Brezin; @Jani98a] $$z = \lambda N^{3/4}\:.
  \label{scalingt}$$ Starting from the exact analytical result derived in Ref. [@senert], it is possible to take the limit $N\rightarrow \infty$ with the scaling relation ([\[scalingt\]](#scalingt){reference-type="ref" reference="scalingt"}) and to obtain an analytical result for the microscopic spectral density at the critical point [@Hikami-Brezin; @Jani98a]. We emphasize that this result is based on mean field critical exponents and is thus not applicable to QCD with nontrivial critical exponents (see also the discussions in Secs. [\[UniversalityProofs\]](#UniversalityProofs){reference-type="ref" reference="UniversalityProofs"} and [\[sec:chphtr\]](#sec:chphtr){reference-type="ref" reference="sec:chphtr"}).

As a last application of the partition function ([\[zrandomt\]](#zrandomt){reference-type="ref" reference="zrandomt"}), we mention the explanation of the observation [@Chan95] that the temperature at which chiral symmetry is restored is higher for gauge field configurations with a nonzero $Z_3$-phase than for gauge field configurations with zero $Z_3$-phase. The explanation in terms of the random matrix model ([\[zrandomt\]](#zrandomt){reference-type="ref" reference="zrandomt"}) is that the lowest Matsubara frequency for the nonzero $Z_3$-phases is shifted to a lower value by the phase of the Polyakov loop, and thus the critical temperature is higher [@mishat].
