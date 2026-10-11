---
doc_id: arxiv-hep-lat-9912004v2
doc_title: "Microscopic Universality and the Chiral Phase Transition in two Flavor QCD F. Farchioni"
section_id: sec-002-i-introduction
section_title: "INTRODUCTION"
section_number: I
pages: 1-2
source_pdf: 9912004v2.pdf
source_sha256: 7033719ec7a8a0bc
doc_brief: "Microscopic Universality and the Chiral Phase Transition in two Flavor QCD F. Farchioni — 9 sections: Hip; B. Lang; INTRODUCTION"
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.997
---
It is inherent to the lattice approach to quantum field theory, that one has to extrapolate from finite lattices, finite statistics and non-critical coupling parameters to infinite lattices, infinite statistics and critical points. Since the result supposedly is a non-trivial, non-perturbatively defined quantum field theory, this process is plagued by uncertainties. A typical example of such a situation, where all these aspects combine, is the study of the thermal transition in QCD for small quark masses. One is interested in the continuum limit (gauge coupling $g\to 0$), small or vanishing fermion masses ($m\to 0$), close to critical temperature ($T\to T_c$) in the thermodynamic limit ($L_x\to
\infty$) --- a formidable problem.

The extrapolations are always based on assumptions on the asymptotic behavior. Well known examples are scaling functions based on renormalization group and chiral perturbation theory --- an expansion around a ground state with Goldstone bosons. Here we will examine another such approach, which should allow the extrapolation to infinite volume and vanishing fermion mass: Chiral Random Matrix Theory (chRMT).

## Chiral Random Matrix Theory

RMT attempts to identify universal features of ensembles of (random) matrices with common symmetry properties. Its chiral version, if successful, allows to separate two aspects of a theory like QCD: the general universal properties shared with other theories from the model-specific "dynamical" content of the theory. Microscopic eigenvalue distribution shapes are an example for the first aspect, expectation values of the fermion condensate for the second.

The limitations for validity of the chRMTconsiderations (for a given $T$ in the phase of broken chiral symmetry) are set by [@LeSm92; @ShVe93] $$\label{QCDrange}
\frac{1}{\Lambda_{QCD}} \ll L_x \ll \frac{1}{m_\pi} \; ,$$ where $L_x$ is the linear size of the system and $m_\pi$ is the mass of the lightest (pseudo-)Goldstone boson. The second restriction imposes that the pion does not fit into the space-time volume and it therefore appears to be unphysical. However, various correlators in the Dirac operator spectrum can be computed precisely in this limit.

chRMThas been proven to give exact analytical predictions for the spectrum of the Dirac operator in the microscopic limit [@AkDaMa97]. The microscopic scaling region is simply a blowup of the origin in the spectrum. To be specific, one considers eigenvalues $\lambda$ on the scale $\frac{\pi}{V
\Sigma}$ where $\Sigma$ is the chiral condensate, related to the spectral density per unit volume $\rho(\lambda)$ via the Banks-Casher [@BaCa80] relation, $\Sigma = \lim_{\lambda\to 0}\lim_{V\to\infty} \pi \rho(\lambda)$. This regime is, by definition, only well defined in the spontaneously broken phase where $\rho(0)\not=0$. In the phase with restored symmetry the scale of interest is set by the density of states in the vicinity of the onset of $\rho(\lambda)$.

Here we present a study of the microscopic correlators in the spectrum of the staggered Dirac operator in SU(3) gauge theory with dynamical fermions at finite temperature. Specifically we examine the low lying eigenvalue statistics at temperatures below, near, and above the critical temperature of the chiral phase transition.

Our analysis is based on the evaluation of the MILC collaboration's gauge configurations [@MILC96; @MILCNERSC]. We therefore concentrate on the new aspects connected to RMT ideas for the spectral correlators of the Dirac operator. In particular for $T>T_c$ we study the singularity at the inner endpoint of the spectral density.

## Temperature transition

Strictly speaking, in the continuum limit $a\to 0$, non-zero temperature is realized for lattices $n_x^3\times n_t$ with $T=1/(n_t\,a(\beta_g))$ and $n_t/n_x\to 0$. In that limit, for vanishing quark mass $m$, one expects a phase transition at $T_c$. In [@MILC96] the critical temperature was estimated to lie between 143 and 154 MeV. For $T<T_c$ chiral symmetry is broken spontaneously, with massless pseudoscalars and $\left\langle\overline{\psi}\psi\right\rangle\neq 0$; above $T_c$ we expect restoration of this symmetry. Whereas for pure Yang-Mills theory the deconfinement transition is associated with a breaking of the center-symmetry with the Polyakov loop as order parameter, this symmetry is explicitly broken by the fermion action. Nevertheless, remnants of the original breaking feature of the Polyakov loop persist even for small fermion masses.

The nature of the chiral phase transition depends on the number of flavors $N_f$. An argument based on a 3D $\sigma$-models analysis [@PiWi84] predicts a first order phase transition for $N_f\ge 3$. For $N_f=2$ one expects a second order phase transition with $SU(2)\times SU(2)\simeq O(4)$ scaling behavior. However, even first order behavior may be arguable [@Wi92; @RaWi93; @Ra95]. For staggered fermions at non-vanishing lattice spacing the correct counting of flavors is unclear since flavor symmetry is restored only in the continuum limit. Staggered fermions (as simulated by MILC with the hybrid R-algorithm [@GoLiRe87]) correspond to the case $N_f=2$ in the continuum limit. On coarse lattices the so defined fermions should show at least $U(1)\simeq O(2)$ scaling behavior. For a discussion of the various scenarios cf. [@La98; @DeTar98; @BeDeGo99].

It is unclear whether the phase transition at $T_c$ extends towards $m>0$ or whether, when moving from lower to higher temperature, one just observes crossover-like behavior. Some evidence points towards this second scenario [@AoFuHa98; @La98]. In the following, we denote the crossover (phase transition) position by $T_c(m)$ or simply $T_c$.
