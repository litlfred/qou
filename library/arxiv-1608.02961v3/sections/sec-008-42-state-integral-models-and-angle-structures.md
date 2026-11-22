---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents"
section_id: sec-008-42-state-integral-models-and-angle-structures
section_title: "State-integral models and angle structures"
section_number: 4.2
pages: 15-20
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.994
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
\label{DI.sec:angle}

When $M= S^3\bs K$ is an oriented hyperbolic knot or link complement (or, more generally, an oriented hyperbolic manifold with non-empty boundary of genus $\geq 1$), there exists a systematic construction of $SL(2,\BC)$ Chern-Simons partition functions $\CalZ[M]_{k,s}$ for all levels $k,s$. The full definition of these partition functions appears in \cite{DIGar-index, DIGHRS-index} for $k=0$, and \cite{DID-levelk, DIAK-complexCS} for $k\neq 0$, respectively. It is a culmination of much previous work, including  \cite{DIhikami-2006,DIDGLZ,DIDimofte-QRS, DIKashAnd, DIAK-new} for $k=1$; \cite{DIDGG-index}  for $k=0$ (and indirectly \cite{DIKim-index, DIIY-index, DIKW-index}); and (indirectly, via 3d-3d correspondence) \cite{DIBNY-lens, DIIMY-fact} for $k> 1$. The definition extends to $SL(N,\BC)$ using techniques of~\cite{DIDGG-Kdec}.


The construction of these partition functions uses a topological ideal triangulation of the three-manifold $M=\cup_{i=1}^N\Delta_i$. This is a tiling of $M$ by truncated tetrahedra $\Delta_i$, as in Figure~\ref{DI.fig:triang}, such that 1) various pairs of large hexagonal faces are glued together; but 2) the small triangles at the truncated vertices are left untouched, and become part of the boundary~$\pd M$.



\begin{figure}[htb]
\centering
\includegraphics[width=5in]{DIadmM}
\caption{Ideal (\DIie\ truncated) tetrahedra, glued together along their large hexagonal faces to form an ideal triangulation of a knot complement $M$. The small triangular faces at truncated vertices become part of the boundary of $M$.}
\label{DI.fig:triang}
\end{figure}


One then proceeds in standard TQFT fashion. For gauge group $SL(2,\BC)$ (or more precisely, $PSL(2,\BC)$), the boundary of each tetrahedron is assigned a Hilbert space $\CalH[\pd\Delta]_{k,s}\simeq L^2(\BR)\otimes \BC^k$. The Hilbert space comes from quantizing an open subset of the space of flat connections on $\pd\Delta$, viewed as a four-punctured sphere; in this case $\CalP[\pd\Delta]^{\rm open}\simeq \BC^*\times \BC^*$, and the quantization of Section \ref{DI.sec:quant} applies in a straightforward manner, with no Weyl quotient. Each tetrahedron is assigned a canonical partition function $\CalZ[\Delta]_{k,s}\in \CalH[\pd\Delta]_{k,s}$, which has the form of a ``quantum dilogarithm'' function; for $|k|\geq 1$, this is

\DIbe \CalZ[\Delta_i]_{k,s}(\mu_i,m_i) = \prod_{r=0}^\infty \frac{1-q^{1+r}z_i^{-1}}{1-\tilde q^{-r} \bar z_i^{-1}}\,, \label{DI.qdl} \DIee

with $q,\tilde q$ as in \eqref{DI.qq} or \eqref{DI.qq-index} and $z_i=e^{\frac{2\pi b}{k}\mu_i-\frac{2\pi i}{k}m_i},\, \bar z_i=e^{\frac{2\pi b^{-1}}{k}\mu_i+\frac{2\pi i}{k}m_i}$ as in \eqref{DI.defxy}. (For $k=0$, see Section \ref{DI.sec:M2}.) 


The partition function $\CalZ[M]_{k,s}$ is then obtained by taking a product $\prod_{i=1}^N \CalZ[\Delta_i]_{k,s}(\mu_i,m_i)$, and integrating out all pairs of variables $(\mu_i,m_i)$ associated to the interior of $M$, leaving behind some variables associated to the boundary. It is slightly tricky to describe this operation in precise terms, because the tetrahedron Hilbert space $\CalH[\pd\Delta]_{k,s}$ does not easily factorize into contributions from the tetrahedron's four large faces.

\footnote{The Hilbert space \emph{can} be factorized by introducing some redundant degrees of freedom \cite{DIKashAnd}, in a manner directly analogous to Kashaev's quantization of Teichm\"uller space \cite{DIKash-Teich}.} 

The right prescription comes from viewing gluing in TQFT somewhat more globally, as a quantum symplectic reduction. It turns out that the combinatorics of ideal triangulations have some fundamental symplectic properties, first discovered by Neumann and Zagier \cite{DINZ, DINeumann-combinatorics}, that allow the quantum symplectic reduction to be defined.

As an example, take $M=S^3\bs K$ to be a knot complement. In this case, there is a canonical ``A-cycle''  on the boundary torus $\pd M=T^2$, defined by a small loop linking the knot $K$ in $S^3$ (called the meridian cycle); and there is a canonical boundary condition for $SL(2,\BC)$ connections, defined by requiring their holonomy along the meridian cycle to have trivial eigenvalues. (Crucially, this does not require the actual holonomy to be trivial; in $SL(2,\BC)$ there are parabolic matrices $\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$ with trivial eigenvalues.)
In the notation of Section \ref{DI.sec:quant}, the boundary condition sets $x=\bar x=1$, or restricts functions $f(\mu,m)\in \CalH[T^2]_{k,s}$ to their values at $\mu=m=0$. Suppose that the knot complement is glued from $N$ tetrahedra $\Delta_i$. The combinatorics of the triangulation define a ``Neumann-Zagier datum''

\DIbe \mb A\,,\; \mb B \;\in \text{Mat}_{N\times N}(\BZ)\,,\qquad \nu\,, \in \BZ^{N} \label{DI.NZ}
\DIee

consisting of two $N\times N$ integer matrices $\mb A,\,\mb B$ (that encode adjacency relations for edges of the tetrahedra and satisfy the symplectic property $\mb A\mb B^T-\mb B\mb A^T=I_{N\times N}$) and a vector $\nu$ of $N$ integers.
 A precise definition is given in \cite{DIDG-quantumNZ}. Then the partition function $\CalZ[M]_{k,s}=\CalZ[M]_{k,s}(0,0)$ with the canonical boundary condition takes the concise form \cite{DIDG-levelk}

\DIbe \CalZ[M]_{k,s} =   \frac{C}{k^N\sqrt{\text{det}{\mb B}}} \sum_{m\in (\BZ/k\BZ)^N} \int d^N\!\mu\,
(-\zeta^{\frac12})^{m\mb B^{-1}\mb A m}e^{-\frac{i\pi}{k}\mu\mb B^{-1}\mb A\mu -\frac{\pi}{k}(b+b^{-1})\mu\mb B^{-1}\nu} \prod_{i=1}^N \CalZ[\Delta]_{k,s}(\mu_i,m_i)\,, \label{DI.knot} \DIee

with $\zeta=e^{\frac{2\pi i}{k}}$. The prefactor $C=\zeta^{\frac14 f\mb B^{-1}\nu}e^{\frac{i\pi}{4k}(b^2-b^{-2})f\mb B^{-1}\nu}$ depends on an integer solution $(f,f'')\in \BZ^{2N}$ to $\mb A f+\mb B f''=\nu$.


There are several things to note about this partition function:
\begin{itemize}
\item It approximately takes the form of a ``state sum'' or ``state integral,'' with the partition function \eqref{DI.qdl} assigned to every tetrahedron building-block. The ``state variables''  $m_i\in \BZ/k\BZ$ and $\mu_i$ are summed/integrated over. The number of sums/integrals is the same as the number of tetrahedra which is also the same as the number of internal edges in the triangulation.

\item As explained in \cite{DID-levelk,DIDG-levelk}, the partition function is only defined up to an overall phase, of the form $\zeta^{\frac a{24}}e^{\frac{i\pi}{12k}(a'b^2+a''b^{-2})}$, $a,a',a''\in \BZ$. This subsumes the standard \emph{framing ambiguity} in complex Chern-Simons theory \cite{DIWitten-cx}, which would modify the partition function by a factor of $e^{-\frac{i\pi}{2k}(b+b^{-1})^2}$ upon shifting the framing of the tangent bundle of $M$.

\item Each tetrahedron building-block manifestly admits a holomorphic-antiholomorphic factorization as in \eqref{DI.fact}. The full partition function is also expected to admit such a factorization; this was demonstrated for some simple examples in \cite{DID-levelk}. (See also \cite{DIBDP-blocks, DIGK-Gg} for $k=0$, $k=1$ examples.)

\item Perhaps most interestingly, the precise definition of the integration contour in \eqref{DI.knot} and the convergence of the integral depends crucially on the existence of a \emph{positive angle structure} on the triangulation being used. This is ultimately what restricts the computation to a particular class of 3-manifolds that includes all hyperbolic ones. It also beautifully makes contact with the three-dimensional superconformal theory $T[M]$ defined combinatorially in \cite{DIDGG} using an ideal triangulation --- the definition of $T[M]$ does not make sense (cannot produce a superconformal theory) unless a positive angle structure exists. We proceed to explain this idea momentarily.

\item Via the 3d-3d correspondence, the integral \eqref{DI.knot} has a dual interpretation as a partition function of $T[M]$ on the lens space $S^3/\BZ_k$. This partition function is computed by localization methods, as in Section 4.1 of B. Willett's article, \volcite{WI}. Each $\CalZ[\Delta]_{k,s}(\mu_i,m_i)$ is the contribution of a chiral multiplet to the partition function, and the additional prefactor comes from background Chern-Simons terms involving flavor and R-symmetries.

\item Changes of ideal triangulations are generated by 2--3 Pachner moves, which replace a pair of tetrahedra glued along a common face by a triplet glued along three common faces and a central edge. The state-integral \eqref{DI.knot} is invariant under 2--3 moves that preserve the positive or non-negative angle structure (as appropriate), due to a 5-term integral identity for the quantum dilogarithm \eqref{DI.qdl}. In the case $k=1$, this identity was first discovered by Faddeev \cite{DIfaddeev-1994} (see also \cite{DIFad-Kash}).


\end{itemize}

An angle structure on a topological ideal triangulation is an assignment of real parameters (``angles'') to the six long edges of each tetrahedron, in such a way that 1) angles on opposite edges are equal (leaving three angles $\alpha_i,\alpha_i',\alpha_i''$ per tetrahedron $\Delta_i$); 2) the sum of angles around any tetrahedron vertex equals $\pi$ (thus $\alpha_i+\alpha_i'+\alpha_i''=\pi$); and 3) the sum of angles around every internal edge in the triangulation equals $2\pi$. 
In terms of the Neumann-Zagier gluing datum \eqref{DI.NZ} for a knot complement, the last condition translates to

\footnote{Technically, only $N-1$ out of the $N$ components of \eqref{DI.NZ-angle} correspond to internal edges; the last component of \eqref{DI.NZ-angle} relates to a boundary condition at $\pd M=T^2$, and can be removed from the angle-structure analysis. We are bypassing such subtleties in this heuristic discussion.}

\DIbe \mb A\alpha + \mb B\alpha'' = \pi\nu\,. \label{DI.NZ-angle}\DIee

The idea of an angle structure is motivated by hyperbolic geometry. In an ideal triangulation by \emph{hyperbolic} tetrahedra, the dihedral angles precisely obey the three conditions above \cite{DIthurston-1980}. 


\begin{figure}[htb]
\centering
\includegraphics[width=4.8in]{DIangle-op}
\caption{Left: dihedral angles assigned to edges of an oriented ideal tetrahedron, obeying $\alpha+\alpha'+\alpha''=\pi$. Right: operators of the tetrahedron theory $T[\Delta]$ assigned to the same edges; these operators have R-charges $\rho,\rho',\rho''$ that obey $\rho+\rho'+\rho''=1$.}
\label{DI.fig:angles}
\end{figure}


A positive (respectively, non-negative) angle structure is one where all angles additionally obey $\alpha_i,\alpha_i',\alpha_i''>0$ ($\geq 0$). An oriented hyperbolic three-manifold with genus-one boundary always admits an triangulation with non-negative dihedral angles, hence there a triangulation with a non-negative angle structure \cite{DIpetronio-2000}. It is conjectured and strongly believed that the same holds for strictly positive angle structures. (As evidence for this, the default triangulations produced by the computer program \texttt{SnapPy} \cite{DISnapPy} for the first few thousand hyperbolic knot complements all admit positive angle structures.)

It was shown in \cite{DIGar-index, DIGHRS-index} that analogue of the partition function \eqref{DI.knot} at $k=0$ (\DIcf\ Section \ref{DI.sec:M2}) is well-defined when the triangulation admits a non-negative angle structure.  Similarly, it was shown in \cite{DIKashAnd} for $k=1$ and \cite{DID-levelk, DIAK-complexCS} for $|k|\geq 1$ that the partition function \eqref{DI.knot} is well defined if the triangulation admits a positive angle structure. In each case, the angle structure specifies a canonical convergent integration contour.


The combinatorial construction of theories $T[M]$ given in \cite{DIDGG} translates the ingredients of the state-integral \eqref{DI.knot} to operations in three-dimensional $\CalN=2$ gauge theories. One starts by associating a theory $T[\Delta_i]$ containing a single chiral multiplet $\Phi_i$ (\DIie\ a free complex boson $\phi_i$ and a complex fermion $\psi_i$) to each tetrahedron.
In addition to the chiral (BPS) operator $\Phi_i$, the theory $T[\Delta_i]$ contains two elementary chiral monopole operators $V_i^\pm$, which exist only in the presence of a monopole background for the flavor symmetry of the theory.

\footnote{One does not usually talk about ``flavor'' monopole operators like $V_i^\pm$, but they are essential in the construction of theories $T[M]$, and the relation between these theories and geometry. They can easily be seen in the generalized index of a free chiral multiplet \cite{DIKW-index}, and can also be understood as ordinary monopole operators if the flavor symmetry of $T[\Delta_i]$ were weakly gauged.} 

Geometrically, the three operators $\Phi_i,V_i^+,V_i^-$ are associated to three pairs of $\Delta_i$, as on the RHS of Figure~\ref{DI.fig:angles}. Moreover, $T[\Delta_i]$ has an R-symmetry

\footnote{This is a global symmetry that does not commute with supersymmetry, and is related to an $SO(2)$ automorphism of the 3d $\CalN=2$ SUSY algebra.} 

$U(1)_R$ that rotates $(\phi_i,\psi_i)$ with charges $(\rho_i,\rho_i-1)$ for some (undetermined) $\rho_i\in \BR$. One usually just says that $\Phi_i$ has R-charge $\rho_i$. The other BPS operators $V_i^+,V_i^-$ have some R-charges $\rho_i',\rho_i''$, subject to a single relation $\rho_i+\rho_i'+\rho_i''=1$.


Even for the theory of a single tetrahedron, R-charges are beginning to look like angles, and it is tempting to identify $\rho_i=\alpha_i/\pi$ (etc.). The analogy persists upon gluing. The theory $T[M]$ of \cite{DIDGG} is defined by taking a tensor product of $N$ tetrahedron theories $\otimes_{i=1}^N T[\Delta_i]$, gauging some flavor symmetries, and (most importantly here) adding superpotential interactions $W = \sum_{E=1}^N \CalO_E$ containing a chiral operator $\CalO_E$ for every internal edge $E$ of the triangulation $M=\cup_{i=1}^N \Delta_i$. If all the tetrahedron edges identified with $E$ are labelled by elementary chiral fields $\Phi_i$, one simply constructs $\CalO_E$ as a product $\prod_i\Phi_i$ of these surrounding fields. For edges identified with monopole operators, the prescription is more subtle. In either case, one finds that the R-charge of $\CalO_E$ is a sum of the R-charges $\rho_i,\rho_i',$ or $\rho_i''$ associated to operators on the tetrahedron edges identified with~$E$. The superpotential breaks $U(1)_R$ R-symmetry unless the charge of every $\CalO_E$ is exactly~$2$.


Now, in order for the gauge theory $T[M]$ to flow (in a straightforward way) to a superconformal theory in the infrared, two conditions are necessary: 1) some $U(1)_R$ R-symmetry must be preserved; and 2) there must exist a choice of $U(1)_R$ symmetry such that the charges of all chiral operators are non-negative, because in a superconformal theory R-charges are proportional to operator dimensions. This means that we must be able to choose $\rho_i,\rho_i',\rho_i''$ for individual tetrahedra in such a way that the sums of these charges around any internal edge $E$ is 2, and all these charges are non-negative. Together with the relation $\rho_i+\rho_i'+\rho_i''=1$, the conditions become equivalent to the existence of a non-negative angle structure.
