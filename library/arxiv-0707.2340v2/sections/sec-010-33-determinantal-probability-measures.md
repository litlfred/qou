---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-010-33-determinantal-probability-measures
section_title: "Determinantal Probability Measures"
section_number: 3.3
pages: 17-18
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.985
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{ss-det-m}

In \cite{Lyons} Lyons defined a {\em determinantal probability measure} 
on $2^{[n]}$ to 
be a measure $\mu\in\fP_n$ such that
there is an $n \times n$ matrix $A$ so that for any subset $S$ of 
$[n]$ one has 
\begin{equation}\label{det-me}
\mu(\{T: S \subseteq T\}) = \det(A[S]),
\end{equation}
where as before $A[S]$ denotes the principal submatrix of $A$ whose rows and 
columns are indexed by $S$. As discussed in e.g.~\cite{BKPV,Lyons}, such 
measures have important applications ranging from 
fermionic processes/continuous scaling limits of discrete point 
processes \cite{DVJ,Lyons-Steif} to the distribution of eigenvalues of 
random matrices and zeros of the Riemann zeta function \cite{Con}, 
transfer current matrices \cite{BP}, 
non-intersecting random walks \cite{Joh2}, 
Poissonized versions of the Plancherel
measure on partitions \cite{BOO}
and Young diagrams \cite{OR}, discrete orthogonal polynomial 
ensembles \cite{Joh}, etc.

Recall that a square matrix $A$ is said to be a {\em contraction} 
if $||A||\le 1$, where $||\cdot||$ denotes the supremum (operator) norm. 
Clearly, a positive semi-definite matrix is a contraction if and only
if all its eigenvalues are in the interval $[0,1]$. Such matrices were
called {\em positive contractions} in \cite{Lyons}. 

\begin{theorem}\label{contract}
Suppose that  $\mu$ is a determinantal measure on $2^{[n]}$ whose
corresponding matrix is a positive contraction. Then $\mu$ is $\CNA+$.
\end{theorem}

This is one of the main results of \cite{Lyons} 
(cf.~\cite[Theorem 8.1]{Lyons}), where 
exterior (Grassmann) algebra methods were used to investigate determinantal 
probability measures and, in particular, to prove the above theorem.
As noted in {\em loc.~cit.}, Theorem~\ref{contract} provides a powerful tool 
for studying determinantal probability measures, comparable to the FKG theorem
in the theory of positive association, and is crucial to most of the results
in e.g.~\cite{Lyons-Steif}. 

Let us show that Theorem \ref{contract} actually follows from 
Theorem \ref{stab-NA} of \S \ref{s-sna} and the fact that determinantal 
measures induced by positive contractions are strongly Rayleigh: 

\begin{proposition}\label{det-stab}
Suppose that  $\mu$ is a determinantal measure on $2^{[n]}$ whose
corresponding matrix is a positive contraction. Then $\mu$ is strongly 
Rayleigh.
\end{proposition}

\begin{proof}
Since positive definite matrices are dense in the set of all positive 
semi-definite matrices, by Proposition \ref{pro-rs} (3) it is enough to prove 
the statement for invertible
positive contractions. Elementary computations show that 

$$g_\mu(z_1,\ldots,z_n)=\det(I-A+AZ)=\det(A)\cdot \det(A^{-1}-I+Z),$$ 
where $Z=\text{diag}(z_1,\ldots,z_n)$. 
Since $A$ is an invertible positive contraction, $A^{-1}-I$ is positive 
semi-definite and
$\det(A)>0$, so by \eqref{pencil} the polynomial $g_\mu$ is 
real stable. 
\end{proof}

Another main result of \cite{Lyons} is that if $A$ and $B$ are commuting 
positive contractions and $A \leq B$, 
then the measure corresponding to $B$ stochastically dominates
the one corresponding to $A$ (Definition \ref{d-stoc}). In 
\S \ref{ss-trunc} we extend this result using the theory of stability and 
strongly Rayleigh measures and we prove that the condition 
$[A,B]=0$ (where $[\cdot,\cdot]$ denotes the Lie bracket)
can be dropped from the hypothesis.
