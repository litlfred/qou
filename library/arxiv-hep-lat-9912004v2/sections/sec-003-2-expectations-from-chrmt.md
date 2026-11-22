---
doc_id: arxiv-hep-lat-9912004v2
doc_title: "arXiv:hep-lat/9912004v2 9 Mar 2000"
section_id: sec-003-2-expectations-from-chrmt
section_title: "Expectations from chRMT"
section_number: 2
pages: 2-3
source_pdf: 9912004v2.pdf
source_sha256: 7033719ec7a8a0bc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.997
doc_brief: "arXiv:hep-lat/9912004v2 9 Mar 2000 — 11 sections: Front matter; Chiral Random Matrix Theory; Introduction"
---
[]{#SecRMT label="SecRMT"}

According to the nature of the elements in the random matrix, chRMT appears in three universality classes. In this paper we consider the SU(3) gauge theory with quarks in the fundamental representation, which belongs to the universality class of the chiral unitary ensemble (chUE). The partition function under study is [@ShVe93; @JaVe96; @WeScWe96] $$\begin{aligned}
{\mathcal Z}^{(N_f)}(\{m\})&=&
\int {\rm d}M \,e^{-N{\rm Tr} U(M^2)}\nonumber\\
\label{Z}
 &&\times \prod_{f=1}^{N_f}\det(M+T+im_f) \;,
\end{aligned}$$ where $M$ is a $2N\times2N$ block hermitian matrix (the elements of $W$ being random complex numbers), and $T$ is a deterministic, i.e. not-random, off-diagonal block matrix $$\label{Tmodel}
M=\left(\begin{array}{cc} 0 & W \\ W^\dagger & 0 \end{array} \right) \qquad , 
\qquad   
T=\left(\begin{array}{cc} 0 & t \\ t & 0 \end{array} \right) \; .$$ Here d$M$ denotes the Haar measure, $U(x)$ is an analytic function.

The predictions from chRMTconcern the correlations between the eigenvalues $\lambda$ of $D\equiv M+T$ on the scale of individual eigenvalues in the thermodynamic limit $N\to\infty$. The matrix $D$ is the analogue of the massless Dirac operator in QCD. The chiral phase transition within chRMTis identified through the value of the spectral density of the eigenvalues of $D$ near zero, i.e. using the Banks-Casher relation.

Modeling the chiral phase transition in chRMTamounts to driving a depletion of eigenvalues of $D$ near the origin by means of some temperature parameter. Two separate approaches have been examined in the literature. First, the unitary invariant chRMT[@ShVe93; @AkDaMa97], corresponding to ([\[Z\]](#Z){reference-type="ref" reference="Z"}) with $T=0$, in which the chiral phase transition is driven by tuning $U(M^2)$. Second, the non-unitary invariant chRMT [@JaVe96; @WeScWe96; @SeWeGu98], corresponding to ([\[Z\]](#Z){reference-type="ref" reference="Z"}) with $U(M^2)=M^2$, where the deterministic block matrix $T$ mimics the effect of the temperature. In this paper we do not need to distinguish between the two approaches as they are consistent for the quantities measured here.

Below $T_c$, i.e. when $\rho(0)\not=0$, chRMTpredicts [@NiDaWe98] the probability distribution for the smallest eigenvalue (for the trivial topological sector) $$\label{Pmin}
P(z,\{\mu\})=\frac{z}{2}\,e^{-z^2/4}\,\frac{\det_{1\leq i,j\leq
    N_f}C_{ij}(\{\sqrt{\mu^2+z^2}\})}{\det_{1\leq i,j\leq
    N_f}A_{ij}(\{\mu\})} \ ,$$ with $$\begin{aligned}
A_{ij}(\{\mu\})&\equiv&\mu_i^{j-1}I_{j-1}(\mu_i)\;, \nonumber\\
C_{ij}(\{\mu\})&\equiv&\mu_i^{j-1}I_{j+1}(\mu_i)\;, \nonumber\\
z&=&2\,\pi\,\lambda\,\rho(0)\,N\;, \;\textrm{and}\;\;
\mu_f=2\,\pi\,m_f\,\rho(0)\,N\;.
\end{aligned}$$ where $\rho(0)$ is the spectral density at the origin for the *massless* situation (i.e. when $m_f=0$ in ([\[Z\]](#Z){reference-type="ref" reference="Z"})). $I_j$ denotes the $j$'th modified Bessel function. This result is universal in the chRMTcontext, that is, the analytic form of $P(z,\{\mu\})$ does not change under deformations of $U(M^2)$ provided that $\rho(0)\not=0$. After the identification $V\equiv
2\,N$ ($V$ is the physical volume in lattice units), ([\[Pmin\]](#Pmin){reference-type="ref" reference="Pmin"}) allows to extract $\Sigma=\pi\,\rho(0)$ (the fermion condensate in the chiral limit) from finite-volume Dirac spectra. Of course, in this the mild condition ([\[QCDrange\]](#QCDrange){reference-type="ref" reference="QCDrange"}) must be satisfied.

Above $T_c$, when there is a finite gap in the spectral density, the repulsion between the eigenvalue pair $\pm\lambda_{\rm min}$ becomes negligible; chRMThence predicts a *soft* inner edge, known as the Airy-solution [@Fo93; @TrWi94].

At $T_c$ --- signaled in chRMTby a power-like behavior of the spectral density at small $\lambda$ --- $\rho(\lambda) \propto
\lambda^{\frac{1}{\delta}}$, the prediction from chRMTis not unique. It turns out that the spectral correlators depend on the value of $\delta$ [@AkDaMa98].

The distribution of the smallest eigenvalue is a spectral one-point correlation function and is quite sensitive to statistical fluctuations (see below). As an additional measure we also study a two-point correlator: the level spacing distribution $P(s)$. Note that the level spacings, $s=s_{i+1}-s_i$, are determined in the unfolded spectrum $\{s_i\}_{i=1}^{2N}$. Unfolding separates the fluctuation properties of the spectrum from the supposedly smooth background behavior. The unfolded variable is defined in terms of the eigenvalue spectrum and the local average spectral density by $$s_i=\int_{0}^{\lambda_i}\langle\rho(\lambda)\rangle{\rm d}\lambda \ .
\label{defUnf}$$ The RMT prediction for the level spacing distribution is well approximated by the unitary Wigner surmise $$P(s)=\frac{32}{\pi^2}\,s^2\,e^{-\frac{4\,s^2}{\pi}} \ .
\label{WUE}$$ The level spacing distribution is not expected to be affected by temperature and masses in chRMT, see e.g. [@PuRaWe98].

chRMTmakes predictions for average spectral correlators in sectors with definite topological charge $\nu$, i.e. derived assuming exact zero modes (these are not included in the predicted distributions; cf. [@Da99] for the result of the weighted summation of all topological sectors). For Ginsparg-Wilson fermions [@GiWi82], which realize chiral symmetry on the lattice, one may identify exact zero modes as resulting from topological excitations according to the Atiyah-Singer index theorem (for Wilson fermions one can hypothesize that zero modes are replaced by real modes). This is not the case for staggered fermions, where exact zero modes are absent away from the continuum limit [@SmVi87] and even gauge configurations with non-vanishing topological charge do not give zero eigenvalues. Exact zero modes are here replaced by "almost" zero modes which accumulate to the origin in the continuum limit. In the strong coupling region the microscopic staggered Dirac spectra summed over all topological sectors show [@DaHeNi99; @BeMeWe98] good agreement with the analytical prediction for the topologically neutral, $\nu=0$, sector from chRMT. However, approaching weaker coupling observations contradicting this scenario have been found in a two-dimensional context [@FaHiLa99].

Before turning to the numerical studies, let us comment on the validity of the chRMTpredictions. The condition for application of chRMTin lattice analyses is well established when $T\sim 0$: The range in the unfolded spectrum over which the chRMTcorrelations dominate is $|\lambda|\le
\frac{f^2_\pi}{\langle\bar{\psi}\psi\rangle L_x^2}$ [@JaNoPa98; @OsVe98a], where $f_\pi$ is the pion decay constant. An equivalent statement for $T\geq
T_c$ is not known and no stringent tests of the low-lying eigenvalue statistics have been carried out so far.

Let us emphasize that even though the larger part of the studies of chRMThave been focused on the situation where $\rho(0)\not=0$, there is nothing wrong from first principles in using chRMTwhen $\rho(0)=0$.
