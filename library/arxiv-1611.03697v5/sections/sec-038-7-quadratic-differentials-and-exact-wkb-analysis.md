---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-038-7-quadratic-differentials-and-exact-wkb-analysis
section_title: "Quadratic differentials and exact WKB analysis"
section_number: 7
pages: 33-35
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.99
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{in}

The only examples of CY$_3$ categories where the full stability space is understood come from quivers with potential associated to triangulated surfaces. The associated stability spaces can be identified with moduli spaces of meromorphic quadratic differentials on Riemann surfaces \cite{BS}, and the associated BPS invariants then count finite-length trajectories of these differentials. It turns out that the corresponding Riemann-Hilbert problems are closely related to the exact WKB analysis of  time-independent Schr{\"o}dinger equations. We give a brief and sketchy treatment of this connection here; we hope to return to this subject in future papers.



\subsection{Quadratic differentials}

For more details on the contents of this section see \cite{BS}.
Let us start by fixing data
\[g\geq 0, \quad m=\{m_1,\cdots,m_k\}, \quad k\geq 1,\  m_i\geq 2,\]
and  consider the space
$\Quad(g,m)$ consisting of equivalence classes of pairs $(S,q)$, where $S$ is a compact Riemann surface of genus $g$ and $q$ a meromorphic quadratic differential on $S$ with simple zeroes, and poles of multiplicities $m_i$.
It is a complex orbifold of dimension
\[n=6g-6+\sum_i (m_i+1).\]

Associated to a point $(S,q)$ is a double cover
$\pi\colon \Hat{S}\to S$
branched at the zeroes and odd-order poles of $q$. We denote by $\hS^\circ\subset \hS$ the complement of the inverse image of the poles of $q$, and define the hat-homology group
 \[\Gamma=H_1(\hS^{\circ};\bZ)^-, \]
where the superscript denotes the $-1$ eigenspace under the action of the covering involution of $\pi\colon \Hat{S}\to S$. The intersection form defines a skew-symmetric form
\[\<-,-\>\colon \Gamma \times \Gamma \to \bZ.\]
The groups $\Gamma$ form a local system over $\Quad(g,m)$.

The meromorphic abelian differential $\sqrt{q}$ is well-defined on the double cover $\hS$, and holomorphic on $\hS^\circ$. It defines a de Rham cohomology class in $H^1(\hS^\circ;\bC)^-$ and can be viewed as a group homomorphism $Z\colon \Gamma\to \bC$
\[Z(\gamma)=\int_\gamma \sqrt{q}.\]
It was proved in \cite{BS} that the period map
\[\pi\colon \Quad(g,m) \to \Hom_\bZ(\Gamma,\bC)\isom \bC^n.\]
is a local analytic isomorphism.





By a trajectory of a differential $(S,q)$ we mean a path in $S$ along which $\sqrt{q}$ has constant phase $\theta$. A finite-length trajectory is of one of two types:
\begin{itemize}
\item[(a)] a saddle connection connects two zeroes of the differential (not necessarily distinct);
\item[(b)] a closed trajectory: any such moves in an annulus of  trajectories called a ring domain.
\end{itemize}
Any finite-length trajectory  can be lifted to a closed cycle in $\hS$ which defines an associated class $\gamma\in \Gamma$. All trajectories in a ring domain have the same class, so we can also talk about the class associated to the ring domain.

 Let us assume that our quadratic differential is generic in the sense that if $\gamma_1,\gamma_2$ are two finite-length trajectories of the same phase, then their classes are  proportional in $\Gamma$.
We then define the BPS invariants of $q$ by
\[\Omega(\gamma)=\#\big\{\mbox{saddle connections of class $\gamma$}\big\} - 2\cdot \#\big\{\mbox{ring domains of class $\gamma$}\big\}.\]
The reason for the coefficient $-2$ is that a ring domain leads to a moduli space of stable objects isomorphic to $\bP^1$.  See \cite[Theorem 1.4]{BS}. In physical terms saddle connections represent hypermultiplets, whereas ring domains represent vector multiplets.


\begin{claim}
The data $(\Gamma, Z,\Omega)$ described above defines a miniversal variation of  convergent BPS structures over the orbifold $\Quad(g,m)$.
\end{claim}

\noindent{\it Sketch proof.}
To check  the wall-crossing formula one can use the results of \cite{BS} to view $\Quad(g,m)$ as an open subset of a space of stability conditions on a CY$_3$ triangulated category defined by a quiver with potential, and then apply the theory of wall-crossing for generalised  DT invariants \cite{JS,KS1}.  

The fact that the BPS structures are convergent should follow from the results of \cite[Section 5]{BS}. The basic point is that the only non-finiteness in the BPS spectrum arises from finitely many ring domains. Each of these contributes an infinite collection of saddle connections with classes of the form $\gamma+n\alpha$, where $\alpha$ is the class of the ring domain. But for sufficiently large $R>0$ these saddle connections give a finite contribution to the sum \eqref{concon}.
\qed \smallskip
