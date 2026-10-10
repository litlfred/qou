---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-034-7-quadratic-differentials-and-exact-wkb-analysis
section_title: "Quadratic differentials and exact WKB analysis"
section_number: 7
pages: 33-35
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
text_source: latex
latex_prose_ratio: 0.695
latex_coverage_ratio: 0.977
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
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


\subsection{Voros symbols}
The weak Riemann-Hilbert problem (see Remark \ref{oh}(iii)) defined by the above BPS structures  can be solved using exact WKB analysis of an associated Schr{\"o}dinger equation.  This was  essentially proved by Iwaki and Nakanishi \cite{IN} following Gaiotto, Moore and Neitzke \cite{GMN2}.


Suppose given a quadratic differential $(S,q)$ as above. Let us also choose 
 a projective structure  on the Riemann surface $S$.\footnote{ If the quadratic differential $q$ has a double pole at a point $p\in S$ one should assume that this projective structure (represented in \cite{IN} by the term $Q_2(z)$) also has a pole of a particular form \cite[Assumption 2.5]{IN}.}
We can then invariantly consider the holomorphic Schr{\"o}dinger equation
\[\hbar^2 \frac{d^2}{dz^2} y(z,\hbar) = q(z)\cdot y(z,\hbar),\]
where $z$ is a co-ordinate in the chosen projective structure.
The WKB method involves substituting
\[y(z_1,\hbar)=\exp\Big( \int_{z_0}^{z_1} T(z)\,dz \Big), \qquad T(z)=\sum_{k\geq 0} T_k(z) \cdot \hbar^{k-1},\]
and then solving for $T_j(z)$ order by order. This gives rise to a recursion
\[\frac{dT_{k-1}}{dz}+\sum_{i+j=k} T_i(z) T_j(z)=0,\quad k>0,\]
together with the initial condition $T_{0}(z)^2 =q(z)$. Depending on the choice of square-root taken to define $T_0(z)$ one then obtains two systems of solutions $T_k^{\pm}(z)$. The differences
\[\omega_k(z)=\frac{1}{2} \big(T^+_k(z) -T^-_k(z)\big) dz\]
are single-valued meromorphic one-forms on the spectral cover $\hS$, which vanish unless $k$ is even. One has $\omega_0=\sqrt{q(z)} \, dz$.

The formal cycle Voros symbol associated to a class $\gamma\in \Gamma$ is the formal sum
\begin{equation}\exp(V_\gamma)= \exp\Big(\frac{1}{\hbar} \int_\gamma \omega_0\Big)\cdot \exp\Big(\sum_{g\geq 1} \hbar^{2g-1} \int_\gamma \omega_{2g} \Big).\end{equation}



Iwaki and Nakanishi, relying on analytic results of \cite{KoSc},  show that if $\rr\subset \bC^*$ is a non-active ray for the BPS structure defined by $(S,q)$, then the sum over $g\geq 1$ in the above formal expressions can be Borel summed in the direction $\rr$. This results in Voros symbols which are holomorphic functions of $t=\hbar$ defined in a neighbourhood of $0$ in the half-plane $\bH_\rr$. They also compute the wall-crossing behaviour for these Borel sums as one varies the active ray $\rr\subset \bC^*$.
 


\begin{claim}
Given a quadratic differential $(S,q)$ as above,  the Borel sums of the cycle Voros symbols  give a solution to the corresponding weak Riemann-Hilbert problem  with $t=\hbar$.
\end{claim}
\smallskip

\noindent{\it Sketch proof.}
For the definition of the weak Riemann-Hilbert problem see Remark \ref{oh}(iii). The claim should follow from  the work of Iwaki and Nakanishi \cite{IN}, although a careful proof would require additional continuity arguments to take care of differentials with multiple saddle connections. See particularly Theorem 2.18, Theorem 3.4 and formula (2.21). \qed
\smallskip

It is interesting to ask whether given a suitable choice of base projective structure, the Voros symbols in fact give solutions to the full Riemann-Hilbert problem as stated in Section \ref{real}.  Another interesting topic for further research is the connection with topological recursion \cite{ey}, which is known to be closely related to exact WKB analysis. In particular, it is interesting to ask whether the $\tau$-function computed by topological recursion gives a $\tau$-function in the sense of this paper.








\begin{appendix}
