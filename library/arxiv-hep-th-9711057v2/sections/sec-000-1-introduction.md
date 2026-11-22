---
doc_id: arxiv-hep-th-9711057v2
doc_title: "arXiv:hep-th/9711057v2 30 Apr 1998"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9711057v2 30 Apr 1998 — 11 sections: Front matter; Introduction; Random-matrix theory for finite qu"
---
\label{sec1}

The low-lying eigenvalues of the QCD Dirac operator are of great
importance for the understanding of the spontaneous breaking of chiral
symmetry in QCD.  In Euclidean space, the Dirac operator reads
$i\slash D=i\slash\partial+g(\lambda^a/2)\slash A^a$, where $g$ is the
coupling constant, $\lambda^a$ are the generators of SU($N$)-color,
and $A_\mu^a$ are the gauge fields.  The corresponding eigenvalue
equation is $i\slash D \psi_i=\lambda_i \psi_i$ with real eigenvalues
$\lambda_i$.  Because the Dirac operator anticommutes with $\gamma_5$,
the eigenvalues either occur in pairs $\pm\lambda_i$ or are zero.  Let
$\rho(\lambda) = \langle \sum_i\delta(\lambda-\lambda_i)\rangle_A$ be
the eigenvalue density of the Dirac operator averaged over gauge field
configurations.  The Banks-Casher formula,
$\langle\bar\psi\psi\rangle=\pi\rho(0)/V$ \cite{Bank80}, relates the
order parameter of chiral symmetry breaking,
$\langle\bar\psi\psi\rangle$, to the density of eigenvalues of the
Dirac operator near zero virtuality.  Here, it is essential that the
thermodynamic limit be taken before the chiral limit.  Note also that
$\rho(\lambda)$ is normalized to the space-time volume $V$.  In the
real world chiral symmetry is spontaneously broken and
$\langle\bar\psi\psi\rangle\ne 0$.  This implies that the low-lying
Dirac eigenvalues must be spaced like $\sim 1/V$.  Therefore, it is
natural to magnify this region of the spectrum by a factor of $V$.
This was first suggested by Shuryak and Verbaarschot \cite{Shur93} who
introduced the so-called microscopic spectral density defined by
\begin{equation}
  \label{eq1.1}
  \rho_s(z)=\lim_{V\to \infty}\frac{1}{V\Sigma}\;
  \rho\left(\frac{z}{V\Sigma}\right)\:,
\end{equation}
where $\Sigma$ is the absolute value of the chiral condensate.  Based
on an analysis of sum rules derived by Leutwyler and Smilga
\cite{Leut92} for the inverse powers of the Dirac eigenvalues in a
finite volume, Shuryak and Verbaarschot conjectured that the
microscopic spectral density should be a universal quantity which
depends only on global symmetries, the number of flavors $N_f$, and
the topological charge $\nu$.  What is the meaning of universality in
this statement?  In principle, one could compute $\rho_s$ directly
from full QCD.  In practice, of course, the complexity of the QCD
Lagrangian makes this impossible.  However, if $\rho_s$ is universal,
one can try to compute it in another theory which is simpler than QCD
but has the same symmetries.  The simplest theory in which such a
calculation is possible is random-matrix theory (RMT).  Whether the
results obtained in RMT correctly describe the microscopic spectrum of
full QCD is a question that can only be answered by empirical
evidence, most importantly by large-scale lattice QCD simulations.

Let us briefly recall how a chiral random-matrix model is constructed.
In a chiral basis in Euclidean space, the Dirac operator has a block
structure since it only couples states of opposite chirality.  In RMT,
the matrix of the Dirac operator is replaced by a random matrix $W$
with suitable symmetry properties,
\begin{equation}
  \label{eq1.2}
  \left[\matrix{im&i\slash{D}\cr (i\slash{D})^\dagger&im}\right]\to
  \left[\matrix{im&W\cr W^\dagger&im}\right]\:,
\end{equation}
where we have also added a quark mass $m$.  If $W$ has $N+\nu$ rows
and $N$ columns, then the Dirac matrix in (\ref{eq1.2}) (without the
mass term) has $N$ positive and $N$ negative eigenvalues,
respectively, and $\nu$ zero modes (we assume $\nu\ge 0$ and $\nu\ll
N$).  We can identify $\nu$ with the topological charge and
$2N+\nu\approx 2N$ with the volume $V$.  In full QCD with $N_f$
flavors, the weight function used in averaging over gauge field
configurations contains the gluonic action in the form $\exp(-S_{\rm
gl})$ and $N_f$ fermion determinants.  In the random-matrix model, the
gluonic part of the weight function is replaced by a convenient
distribution of the random matrix $W$, usually a Gaussian distribution
of the individual matrix elements (which are uncorrelated).  Since the
fermion determinants can be expressed as products over the Dirac
eigenvalues they can also be taken into account in the random-matrix
model.  The symmetries of $W$ are determined by the anti-unitary
symmetries of the Dirac operator.  They were classified by
Verbaarschot in Ref.~\cite{Verb94a}.  Depending on the number of
colors and the representation of the fermions the matrix elements of
$W$ are real, complex, or quaternion real.  The corresponding
random-matrix ensembles are called chiral Gaussian orthogonal (chGOE),
unitary (chGUE), and symplectic (chGSE) ensemble, respectively.  The
microscopic spectral density has been computed analytically in all
three ensembles for all $N_f$ and $\nu$ in the chiral limit
\cite{Verb93,Verb94d,Naga95}.

Evidence in support of the conjecture that $\rho_s$ is a universal
function has been accumulated in a number of recent studies which we
list here. The moments of $\rho_s$ generate the Leutwyler-Smilga sum
rules \cite{Verb93}.  The result for $\rho_s$ is insensitive to the
probability distribution of the random matrix \cite{Brez96,Nish96}.
Lattice data for the valence quark mass dependence of the chiral
condensate could be understood using the analytical expression for
$\rho_s$ \cite{Chan95,Verb96a}.  The functional form of $\rho_s$ does
not change at finite temperature \cite{Jack96b}.  The analytical
result for $\rho_s$ is found in the Hofstadter model for universal
conductance fluctuations \cite{Slev93}.  For an instanton liquid,
$\rho_s$ shows quite good agreement with the random-matrix result
\cite{Verb94b}.  Recently, a high-statistics lattice calculation
directly demonstrated agreement between the random-matrix results and
lattice data, not only for $\rho_s$ but also for the distribution of
the smallest eigenvalue and for the microscopic spectral two-point
correlator \cite{Berb97a}. (This study was done for gauge group SU(2)
with staggered fermions in the quenched approximation.)  We believe
that the universality of $\rho_s$ is now firmly established.

One of the most interesting and most important problems of present-day
lattice simulations is the inclusion of dynamical fermions.  This is
essential for a realistic description of hadronic properties.
Unfortunately, it is computationally expensive to include the fermion
determinants in a Monte-Carlo simulation.  Moreover, the computational
cost increases with lower quark mass, thus it is extremely difficult
to take the chiral limit on the lattice.  Any analytical insight into
the distribution of the Dirac eigenvalues in the presence of massive
dynamical quarks will therefore be helpful.  It is the purpose of this
work to extend the random-matrix results obtained in the chiral limit
to the general case of massive quarks to be able to compare with
actual lattice calculations.  This issue was first discussed in
Ref.~\cite{Jurk96}.  The most interesting case of QCD with 3 colors
and fermions in the fundamental representation corresponds to the
chGUE of RMT on which we concentrate here.  In what range of the quark
mass can we expect the random-matrix results to be in agreement with
full QCD?  Gasser and Leutwyler \cite{Gass87} have shown that in the
range $1/\Lambda\ll L\ll 1/m_\pi$ the dependence of the finite-volume
QCD partition function on the quark mass $m$ is determined solely by
global symmetries ($\Lambda$ is a typical hadronic scale, $L$ is the
linear size of the Euclidean box, and $m_\pi\sim\sqrt{m\Lambda}$ is
the pion mass).  The partition function was computed for equal quark
masses using an effective Lagrangian in Ref.~\cite{Leut92} and for the
general case of different quark masses in the framework of chiral RMT
in Ref.~\cite{Jack96c}.  The condition $L\ll 1/m_\pi$ sets an upper
limit of $1/\sqrt{V\Lambda^2}$ on the quark mass.  A lower limit of
$1/(V\Lambda^3)$ on the quark mass is set by the requirement that the
chiral condensate be non-zero in a finite volume.  To obtain
non-trivial results for the dependence of the various quantities we
compute on $m$, the quark mass has to be rescaled by the same factor
$1/(V\Sigma)$ as the eigenvalues, cf.~Eq.~(\ref{eq1.1}).  For large
quark masses, our results reduce to those obtained in the quenched
approximation.

This paper is organized as follows.  In Sec.~\ref{sec2} we discuss the
random-matrix model and construct the orthogonal polynomials and the
partition function which are needed in the course of the calculation.
Physical observables such as the microscopic spectral density and the
distribution of the smallest eigenvalue are computed in
Sec.~\ref{sec3}.  Section~\ref{sec4} is a short summary.

After completion of this work we learned that very recently a similar
calculation was performed simultaneously and independently by P.H.
Damgaard and S. Nishigaki \cite{Damg97}.  In this work, the authors
also give a universality proof for more general distributions of the
random matrix and construct spectral sum rules for the massive Dirac
operator (see also Ref.~\cite{Damg97b}) but do not address the
distribution of the smallest eigenvalue.  Wherever the two manuscripts
overlap the results are identical.
