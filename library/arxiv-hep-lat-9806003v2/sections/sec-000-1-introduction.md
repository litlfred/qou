---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.997
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 14 sections: Front matter; Introduction; Complete Dirac spectra in SU(2) ga"
---
\label{sec1}
It is now well established that Random Matrix Theory (RMT) accurately
models spectral fluctuations in an abundant variety of different
systems, such as chaotic, disordered and many--body systems, see the
review in Ref.~\cite{guhr97}. In recent years, RMT has in addition
been successfully introduced into the study of certain aspects of
Quantum Chromodynamics (QCD). The interest focuses on the spectral
properties of the Euclidean Dirac operator.  The eigenvalue equation
under consideration reads
\begin{equation}
i\slash D[A]\psi_k=\lambda_k[A]\psi_k \ ,
\label{eq1}
\end{equation}
where $i\slash D[A]=i\slash\partial+g\slash A^at^a$ is the massless
Euclidean Dirac operator. The coupling constant is denoted by $g$ and
the $t^a$ are the generators of the gauge group. The distribution of
the color gauge fields $\slash A^a$ is given by the Euclidean QCD
partition function. As these gauge fields vary over the ensemble of
gauge field configurations, the eigenvalues fluctuate about their
average positions. The average spectral density is defined as
\begin{equation}
\rho(\lambda)=\left\langle\sum\nolimits_k\delta(\lambda-\lambda_k[A])
   \right\rangle_A \;.
\label{eq2}
\end{equation}
The average has to be performed over all gauge field configurations.

In contrast to most other systems, however, there are two
different regimes in QCD spectra which can be addressed in an RMT
approach, the microscopic region and the bulk region. 
Since the Dirac operator only couples states of opposite chirality,
the eigenvalues are pairwise positive and negative. This is the reason
why two types of spectral fluctuations can be distinguished, namely
spectral fluctuations in the microscopic limit near zero virtuality,
$\lambda=0$, and in the bulk of the spectrum. 
 
Concerning the microscopic region, chiral Random Matrix Theory (chRMT)
\cite{shuryak93} incorporates the global symmetry properties, in
particular chiral symmetry, of $i\slash D$. It predicts level
repulsion between positive and negative eigenvalues which results in a
distinct behavior of the eigenvalue density and correlations near the
origin.  It is possible to calculate spectral correlators analytically
in the microscopic limit \cite{verbaar93,forr93,nagao95}, and to
compare the predictions of chRMT with complete spectra of the lattice
QCD Dirac operator on reasonably large lattices.  Indeed, remarkable
agreement is found~\cite{bitsch97a,bitsch97b,ma97,verbaar96,verbaar97}
at the edge of the spectrum.

Sufficiently far away from the origin, however, the repulsion of
negative and positive eigenvalues should become unimportant.
Therefore the chiral structure of the theory is not expected to be of
relevance in the bulk of the spectrum.  This is the region we will
address on in this work. By comparing with lattice data, it has
already been shown that conventional RMT properly models these
fluctuations in the bulk \cite{halasz95,halasz97,verbaar97}.  It is
important to go beyond these statistical analyses made so far in order
to see to what scales RMT does apply. The identification of such
scales gives a fundamental insight into a system. Investigations of
this type have been performed in great detail in disordered systems
and in many--body systems.  There, the Thouless energy $E_c$ or the
spreading width $\Gamma$ determine the scale $E_c/D$ where $D$ is the
level spacing, in which the fluctuation are of RMT type
\cite{thou75,thou77}.  Beyond this scale, deviations from the RMT
behavior occur, see Ref.\cite{guhr97} for a detailed discussion and
further references.

Recently, theoretical studies \cite{stern98,osborn98,janik98}
established a link between disordered systems and QCD. The range of
validity of RMT, $\lambda_{\rm RMT}$, was introduced as an equivalent
of a Thouless energy $E_c$. A scaling $\lambda_{\rm RMT}/D \propto
\sqrt{V}$ was proposed where $V$ is the four--volume of the system.
Indeed, such a scaling behavior was found very recently in the
microscopic region \cite{bitsch98} for deviation from RMT behavior. As
argued in \cite{osborn98} a corresponding effect should also be seen
in the bulk of the spectrum. This is what we will investigate.

The identification of this scale $\lambda_{\rm RMT}/D$ in QCD spectra
could lead to an improved understanding of certain features of QCD and
allows us to separate the stochastic noise of the short range
fluctuations from the true dynamics of the QCD vacuum. Eventually, it
could be possible to set up effective models or simplify the presently
used simulation algorithms in lattice gauge theories.  In this work,
we search for such a universal scale $\lambda_{\rm RMT}/D$ in the bulk
region by analyzing lattice data.  In contrast to the microscopic
region, the bulk of the spectrum is expected to have a translation
invariant analogue of the Thouless energy.  We emphasize that our
analysis is self--consistent. Advantageously, it does not depend on
any model that aims at an explanation for the occurrence of this
universal scale.

The high amount and quality of the data sets which exceed the
existing ones by far enable us to considerably extend the energy
range for our analysis.  Moreover, the wealth of data makes it
possible to directly address bare correlation functions which cannot
be analyzed in most systems. Furthermore, in doing so we discuss some
technical aspects, which are of general interest for the investigation
of spectral fluctuations.

This paper is organized as follows: In Sec.~\ref{sec2} the data under
investigation is presented.  A detailed analysis of the statistical
properties is given in Sec.~\ref{sec3}. This includes the introduction
of the numerical unfolding approaches, a statistical analysis of the
nearest neighbor spacing distribution, two--point spectral
correlations and higher order spectral correlations. Deviations from
the RMT predictions are found and interpreted. Summary and discussion
are given in Sec.~\ref{sec4}.
