---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.893
latex_coverage_ratio: 0.992
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
Chern-Simons theory with complex gauge group came to prominence in the late 80's, partly as a tool for understanding three-dimensional gravity with a negative cosmological constant \cite{DIAT-CSgrav, DIWitten-gravCS, DIWitten-top, DIWitten-cx}.
Many early developments were due to Witten.
Since then, it has found a multitude of applications and deep connections with many parts of theoretical physics and mathematics. A highly incomplete list includes:

\begin{itemize}
\item Many further applications of $SL(2,\BC)$ Chern-Simons theory (and its $SL(2,\BR)\times SL(2,\BR)$ cousin) to three-dimensional quantum gravity and AdS/CFT.
Similarly, $SL(N,\BC)$ Chern-Simons at large $N$ has been used to describe higher-spin theories of gravity~\cite{DICFPT-spin3, DIGaberdielGopakumar}.


\item Chern-Simons theory with gauge group $SL(N,\BC)$ can naturally be embedded in string/M-theory, opening up many powerful perspectives and techniques for analyzing the former.
As a notable example, the compactification of $N$ M5 branes on the product of an ellipsoidally deformed lens space $L(k,1)_b\simeq S^3_b/\BZ_k$ and a three-manifold $M$ (with a topological twist along $M$) leads equivalently to $SL(N,\BC)$ Chern-Simons theory at level $k$ on $M$ \cite{DICJ-S3, DILY-S2, DIYagi-S2} or an $\CalN=2$ supersymmetric theory $T_N[M]$ on the lens space \cite{DIDGH, DIDG-Sdual, DIYamazaki-3d, DIDGG}. This duality, known as the 3d-3d correspondence, fits into a series of dualities involving the compactification of five-branes on various $d$-dimensional manifolds $M^d$, including the AGT correspondence \cite{DIAGT} and the duality of Gukov-Gadde-Putrov relating Vafa-Witten partition functions on $M^4$ and elliptic genera \cite{DIGGP-4d}. 




\item There is a multitude of applications to three-dimensional geometry and topology. Fundamentally, partition functions of complex Chern-Simons theory on three-manifolds $M$ provide new topological invariants, generalizing the famous invariants (including knot polynomials) associated with compact Chern-Simons theory \cite{DIWit-Jones, DIResh-Tur}. As yet, a systematic computation of the complex invariants only exists for certain classes of manifolds (\DIeg\ hyperbolic ones \cite{DIKashAnd, DIDGG-index, DIAK-complexCS, DID-levelk}), though new tools to attack the general case are under development \cite{DIGukovPei, DIPeiKe}.

The perturbative expansion of $SL(2,\BC)$ Chern-Simons theory on a three-manifold $M$ encodes various topological invariants of $M$, such as its hyperbolic volume and twisted analytic torsion. In the case that $M=S^3\backslash K$ is a knot complement in $S^3$, it was conjectured by Gukov \cite{DIgukov-2003} that this expansion agrees with a (highly nontrivial) asymptotic limit of colored Jones polynomials of $K$, providing physical motivation for a mathematical statement known as the Volume Conjecture \cite{DIkashaev-1997, DIMur-Mur}. The relation between complex Chern-Simons theory and knot polynomials is essentially a result of analytic continuation, albeit a subtle one \cite{DIWit-anal}.

The perturbative expansion of $SL(2,\BC)$ Chern-Simons theory on knot complements has been successfully reproduced  \cite{DIDF, DIGS-quant, DIBorotEynard} using the topological recursion of Eynard-Orantin \cite{DIEO}, a far-reaching formalism for the quantization of spectral curves.

The study of five-brane systems related to complex Chern-Simons theory recently led to a vast generalization of the Volume Conjecture, involving asymptotic limits of colored HOMFLY polynomials and their categorification \cite{DIFGS-VC}.


\item There are several hints that complex Chern-Simons theory has quasi-modular properties, \DIcf\ \cite{DIDG-Sdual, DIGPV}, though a complete physical characterization of these properties is still missing. The asymptotic expansions of $SL(2,\BC)$ Chern-Simons theory around various singular points in the space of coupling constants (levels) \cite{DIDG-levelk},
related by an action of the modular group, provide evidence for the Quantum Modularity Conjecture of Zagier \cite{DIQMF}.

\item There are close connections between complex Chern-Simons theory and the mathematical theory of cluster algebras, \DIcf\ \cite{DITY-cluster, DIDGG-Kdec}. Cluster algebras play an essential role in the (local) description and quantization of phase spaces that complex Chern-Simons theory attaches to two-dimensional boundaries, \DIcf\ \cite{DIFockChekhov, DIKash-Teich, DIFG-cluster}, and Chern-Simons theory on three-manifolds is associated with cluster-algebra morphisms.


\item Very recently, $SL(2,\BC)$ Chern-Simons theory at integer levels (in terms of \eqref{DI.action} below, this means $k\in \BZ$ and $is\in \BZ$)  has been proposed as an effective theory of quantum Hall systems \cite{DIVafa-FQHE}. Excitingly, this may lead to tests of complex Chern-Simons theory in the lab.

\end{itemize}



In this short review, we will only be able to touch upon a few of these topics and connections.
We will actually begin in Section \ref{DI.sec:quant} with some basic concepts in complex Chern-Simons theory, including the definition of the Hilbert spaces $\CalH[\Sigma]$ assigned to two-dimensional oriented manifolds. One of the most prominent distinctions between Chern-Simons theory with complex and compact gauge groups is that, in the complex case, these Hilbert spaces are infinite-dimensional. As an illustrative example, we will outline the simple quantization of the torus Hilbert space $\CalH[T^2]$ for gauge group $SL(2,\BC)$, and its dependence on the coupling constants or ``levels'' of the theory. We also review some features of the refined or \emph{equivariant} quantization of Hilbert spaces recently developed by Gukov and Pei \cite{DIGukovPei}.

This prepares us in Section \ref{DI.sec:TQFT} to discuss one of the most fundamental \emph{open} problems in complex Chern-Simons theory: defining the theory as a full TQFT. In essence, this means being able to assign Hilbert spaces $\CalH[\Sigma]$ to any oriented surface and wavefunctions $\CalZ[M]\in \CalH[\pd M]$ to any oriented three-manifold, in such a way that the standard cutting-and-gluing axioms of Atiyah and Segal are obeyed \cite{DIatiyah-1990}. As we shall review, the difficulty with cutting and gluing in complex Chern-Simons theory stems from the infinite-dimensional nature of Hilbert spaces, and the fact that, naively, wavefunctions often vanish or diverge. Some very promising routes to overcoming these difficulties are suggested by embedding complex Chern-Simons theory in string/M-theory, and using additional symmetries to regulate zeroes or infinities  \cite{DICDGS, DIGukovPei, DIPeiKe}. Interestingly, these symmetries are related to categorification of Chern-Simons theory.

In the second half of this review, we then discuss a few relations between complex Chern-Simons theory and the topology and geometry of three-manifolds.
In each case, we view these relations in light of string/M-theory and the 3d-3d correspondence.
In Section \ref{DI.sec:topol}, we will discuss 1) asymptotic expansions of $SL(N,\BC)$ Chern-Simons partition functions, their relation to hyperbolic volumes, and their behavior at large $N$ \emph{vis \`a vis} holography of five-brane systems; 2) state-sum/integral models for $SL(N,\BC)$ Chern-Simons theory, their relation to positive angle structures on ideal triangulations of three-manifolds, and the corresponding implication for positivity of operator dimensions in theories $T[M]$ built from ideal triangulations; 3) the interpretation of the $SL(N,\BC)$ partition function at level $k=0$ as counting surfaces in a three-manifold $M$, BPS operators in $T[M]$, and BPS M2 branes ending on wrapped M5 branes in M-theory (related to recent mathematical work \cite{DIGHHR}). In Section \ref{DI.sec:QM}, we will state some of the observations and conjectures about ``quantum'' modularity in Chern-Simons theory.

We emphasize that the 3d-3d correspondence provides the main link between complex Chern-Simons theory and localization methods in supersymmetric gauge theories, which are the focus of this collection of articles. Particularly relevant are the reviews of T. Dumitrescu (\volcite{DU}) and B. Willett (\volcite{WI}). The basic idea is that whenever $T[M]$ can be explicitly described as (say) a gauge theory, its partition function on spaces such as $S^3$ or $S^3/\BZ_k$ is readily computed by supersymmetric localization. This has led to new formulations and refinements of Chern-Simons partition functions on $M$, which in turn produce invariants of 3-manifolds,

\DIbe
\raisebox{-.4in}{\includegraphics[width=4.5in]{DI3drel}}
\DIee


Unfortunately, we will not say very much about connections of complex Chern-Simons theory to cluster algebras, topological recursion, categorification, gravity, or many other fascinating topics. We hope that some of the references above will guide readers interested in these subjects.
