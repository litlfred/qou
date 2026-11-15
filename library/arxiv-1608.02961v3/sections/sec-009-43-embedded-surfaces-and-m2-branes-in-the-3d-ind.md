---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents"
section_id: sec-009-43-embedded-surfaces-and-m2-branes-in-the-3d-ind
section_title: "Embedded surfaces and M2 branes in the 3d index (k=0)"
section_number: 4.3
pages: 20-22
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.997
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
\label{DI.sec:M2}

The partition function of complex Chern-Simons theory at level $k=0$ is rather special. Via the 3d-3d correspondence, it takes the form of a supersymmetric index \cite{DIDGG-index}. Schematically:

\DIbe \CalZ[M]_{k=0,s} = \CalZ[\text{$T[M]$ on $S^2\!\times_q\!S^1$}] = \text{Tr}_{\CalH[\text{$T[M]$ on $S^2$}]} (-1)^Rq^{\frac{R}{2}+J_3}\,, \label{DI.index} \DIee

with $q=\exp\frac{4\pi}{2}$ as usual.
Here $S^2\!\times_q\!S^1$ denotes a geometry that is fibered over $S^1$, in such a way that $S^2$ rotates around an axis (by an amount $\pi/s$) as $S^1$ is traversed. Just as in our discussion around \eqref{DI.tr}, the partition function of any quantum field theory in such a geometry can be expressed as a trace. In this case, it becomes a trace over the Hilbert space of $T[M]$ on $S^2$, weighted by the spin ($J_3$) and R-charge ($R$) of states. Due to the factor $(-1)^R$, this trace behaves like an Euler character (physically, a Witten index \cite{DIWitten-constraints}). In particular, only ``BPS states'' in the cohomology of a particular supercharge contribute. While the ``BPS sector'' of the Hilbert space containing such states is infinite-dimensional, it is expected to have finite $q$-graded dimension when $M$ is sufficiently nice (\DIeg\ hyperbolic), so that \eqref{DI.index} produces a well-defined formal Laurent series in $q$.
Less obviously, if $T[M]$ is a superconformal theory, then superconformal symmetry requires the existence of an R-charge assignment such that only non-negative powers of $q$ appear in \eqref{DI.index} \cite{DIDGG-index}.

In the case that $T[M]$ is superconformal, one can also use the state-operator correspondence to recast the RHS or \eqref{DI.index} as a sum over BPS \emph{operators} of $T[M]$ rather than states.
Then the index counts the number of operators with given spin and R-charge. 
Combining this perspective with the 3d-3d correspondence really makes the geometry of $M$ come to life, in the following way. 


Recall that for gauge group $G_\BC=SL(N,\BC)$, the theory $T[M]$ is the effective theory of $N$ M5 branes wrapped on $M\times \BR^3$ inside the eleven-dimensional background $T^*M\times \BR^5$. From this perspective, at least some of the BPS operators in $T[M]$ should come from M2 branes that end on the stack of M5 branes, such that their boundary $\pd$(M2)$=\Sigma\times\{0\} \subset M\times \BR^3$ wraps a surface in $M$. One might therefore expect that

\DIbe \text{The index $\CalZ[M]_{k=0,s}$ ``counts'' surfaces in $M$.} \label{DI.counts} \DIee

Alternatively, we may think of $T[M]$ as the effective theory obtained by compactifying the 6d $(2,0)$ theory of type $A_{N-1}$ on $M$. The local BPS operators of $T[M]$ can come from 1) local operators of the 6d theory; or 2) surface operators in the 6d theory, corresponding to the boundaries of M2 branes in the M-theory picture above. Thus, a more refined statement of \eqref{DI.counts} would be that the index counts surfaces in $M$ decorated by local operators.


The first hint that \eqref{DI.counts} could be true came in work of Gukov, Gadde, and Putrov \cite{DIGGP-walls}. They investigated the index for knot complements $M=S^3\backslash K$, and found contributions from boundary-incompressible surfaces. These are incompressible surfaces $\Sigma$ whose boundary $\pd \Sigma = S^1\subset \pd M$ wraps a particular nontrivial cycle on the torus boundary of $M$. The corresponding operators $\CalO_\Sigma$ and all of their powers $\CalO_\Sigma^2$, $\CalO_\Sigma^3$,...  (corresponding to multiply-wrapped surfaces) are expected to contribute to the index, and this is exactly what \cite{DIGGP-walls} found.

To make a more precise statement, we should recall that the index $\CalZ[M]_{k=0,s}(m,n)$ of a knot complement  depends on two integers $m,n$, as in \eqref{DI.index-fmn}. On one hand, these integers are magnetic and electric (flavor) charges in the space of local BPS operators of $T[M]$. On the other hand, these charges label homology classes $(m,n)\in H_1(\pd M,\BZ)$.
For an operator $\CalO_\Sigma$ corresponding to a surface in $M$, the charges $(m_\Sigma,n_\Sigma)$ measure the homology class of the boundary curve $\pd \Sigma\subset \pd M$.

In the case of a boundary-incompressible surface $\Sigma$, the expectation is that the operator $\CalO_\Sigma$  preserves not one but two supercharges. This implies that if $\CalO_\Sigma$ has $\frac R2+J_3=Q_\Sigma$, so that it contributes $q^{Q_\Sigma}$ to the index in some charge sector $(m_\Sigma,n_\Sigma)$, then the $d$-th power $\CalO_\Sigma^d$ has $\frac R2+J_3=dQ_\Sigma$ and contributes $q^{dQ_\Sigma}$ to the index in charge sector $(dm_\Sigma,dn_\Sigma)$. One can therefore detect the presence of such operators in the index because they force the minimal power of $q$ appearing in $\CalZ[M]_{k=0,s}(dm,dn)$ to grow linearly as $d\to \infty$ whenever $(m,n)$ coincides with the charge $(m_\Sigma,n_\Sigma)$ of an incompressible surface.
In contrast, for generic $(m,n)$, the growth of $\CalZ[M]_{k=0,s}(dm,dn)$ as $d\to \infty$ is quadratic.

\footnote{Similar behavior appears in certain stable limits of the Jones polynomial \cite{DIGaroufalidis-slopes}. In both cases, the behavior can partially be explained by observing that 1) one is studying $q$-series that are solutions to recursion relations coming from the $A$-polynomial of a knot \cite{DIgukov-2003, DIgaroufalidis-2004, DIDGG-index}; and 2) boundary slopes of the $A$-polynomial are related to boundary slopes of incompressible surfaces \cite{DIcooper-1994}. See \cite[App. D]{DIDGG-index} for further remarks.} 

Famously, the set of possible charges of incompressible surfaces $(m_\Sigma,n_\Sigma)$ is finite \cite{DIHatcher-bdy}. 

The simplest example of such behavior occurs not for a knot complement but for a single ideal tetrahedron $M=\Delta$. The index $\CalZ[\Delta]_{k=0,s}(m,n)$ is defined by

\DIbe \sum_{n\in \BZ} \CalZ[\Delta]_{k=0,s}(m,n)\, \zeta^n = \prod_{r=0}^\infty \frac{1-q^{1+r}x^{-1}}{1-q^r \tilde x^{-1}}\,, \label{DI.tet-index} \DIee

where $x=q^{\frac m2}\zeta$ and $\tilde x=q^{\frac m2}\zeta^{-1}$ (\DIcf\ \eqref{DI.index-fmz}). Explicitly,

\DIbe \CalZ[\Delta]_{k=0,s}(m,n) = \sum_{r=(-n)_+}^\infty \frac{q^{-\big(r+\frac12n\big)m}}{\prod_{i=1}^r(1-q^{-i})\prod_{j=1}^{r+n}(1-q^j)}\,, \DIee

where $(-n)_+=\text{max}(-n,0)$.
There are three rays in the $(m,n)$ lattice along which the leading power of $q$ grows linearly: $\gamma=(0,-d)$, $\gamma'=(d,0)$, and $\gamma''=(-d,d)$ for $d\geq 0$. In terms of the theory $T[\Delta]$, these three rays correspond to powers of the three operators $\Phi,V^+,V^-$ that were discussed at the end of Section \ref{DI.sec:angle}. Geometrically, they correspond to the three ``local'' incompressible surfaces shown in Figure \ref{DI.fig:surface}. (These surfaces are boundary-incompressible if the boundary of the ideal tetrahedron is understood as a four-punctured sphere. They are the basic building blocks of what are known as normal surfaces in three-manifold topology~\cite{DIRubinstein-S3}.)


\begin{figure}[htb]
\centering
\includegraphics[width=5in]{DIsurface}
\caption{Three incompressible surfaces inside an ideal tetrahedron, corresponding to three unconstrained operators in the theory $T[\Delta]$.}
\label{DI.fig:surface}
\end{figure}

The boundary-incompressible surfaces in $M$ lead to very special operators that are unconstrained, in the sense that all their powers contribute to the index, with purely additive $\frac R2+J_3$ charge.
In general, one might expect to find operators whose powers do obey various relations, and do not have additive charges.  Excitingly, in recent mathematical work \cite{DIGHHR}, 
 Hodgson, Hoffman, Garoufalidis, and Rubinstein found that it was possible to rewrite the \emph{entire} index 
 $\CalZ[M]_{k=0,s}$ of a knot complement as a sum over surfaces,
 
 \DIbe \CalZ[M]_{k=0,s}(m,n)\; = \hspace{-.2cm}\sum_{\text{$\Sigma$ s.t. $[\pd \Sigma]=(m,n)$}} \hspace{-.2cm}
 w_\Sigma(q)\,, \DIee
 
 where the sum is over all normal surfaces in a given triangulation of $M$, making the expected relation \eqref{DI.counts} true in a precise sense.
 The main contribution to the weights $w_\Sigma(q)$ looks like a product of tetrahedron indices, corresponding to the tetrahedra in the triangulation. It would be very interesting to understand these weights in terms of local operators of the 6d $(2,0)$ theory, bound to the surface $\Sigma$.
