---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-007-33-determinantal-probability-measures
section_title: "Determinantal Probability Measures"
section_number: 3.3
pages: 17-20
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — W e introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polyno mials that amount"
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.973
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


\subsection{Graphs, Laplacians, Spanning Trees and the Random Cluster 
Model}\label{ss-trees}

Let $G=(V,E)$ be a graph with vertex set $V=[n]$ and edge set $E$. Associate 
to each edge $e \in E$ a variable $w_e$. If $e$ connects $i$ and $j$ let 
$A_e$ be the $n \times n$ positive semi-definite matrix with the $ii$-entry 
and 
the $jj$-entry equal to $1$, the $ij$-entry and $ji$-entry equal to $-1$, 
and all other entries equal to $0$. The {\em Laplacian}, $L(G)$,  of $G$ is 
defined by 
$$
L(G)= \sum_{e \in E}w_eA_e.
$$
Let
$$
f_G(z,w)= \det(L(G)+Z).
$$
Thus, by \eqref{pencil}, $f_G$ is a multi-affine real stable polynomial with 
non-negative coefficients.   
The Principal Minors Matrix-Tree Theorem (see, e.g., \cite{Chaiken}) says that 
$$
 f_G(z,w)= \sum_{F}z^{\roots(F)}w^{\edges(F)}, 
$$ 
where the sum is over all rooted spanning forests $F$ in $G$, $\roots(F) 
\subseteq V$ is the set of roots 
of $F$ and $\edges(F) \subseteq E$ is the set of edges used in $F$. 
Alternatively, we may write $f_G$ as 
$$
f_G(z,w)= \sum_{F} w^F \prod_{C \in \mathcal{C}(F)} (\sum_{j \in C}z_j),
$$
where $\mathcal{C}(F)$ is the partition of $V$ whose parts are the vertices 
in the maximal trees in $F$ and the sum is over all forests in $G$.  Since 
the class of stable polynomials is closed under differentiation and 
specialization of  variables at real values (see, e.g., \cite{BBS2}) we have 
that the {\em spanning tree polynomial} $T_G(w)= \sum_Tw^T$, where the sum is 
over all spanning trees, is real stable (which is widely known).  The 
corresponding probability measure is usually called the uniform random 
spanning tree measure and is consequently strongly Rayleigh. Now if 
$\ben$ denotes the vector of all ones as in \S \ref{s2-plet} then 
$$
f_G(\ben,w)= \sum_{F} \omega_G(F)w^F,
$$
where the sum is over all spanning forests (independent sets) in $G$ and 
 $\omega_G(F)$ is the product of the sizes of the connected components of 
$F$. In \cite[Conjecture~5.10]{W} Wagner conjectured that $f_G(\ben,w)$ is a 
Rayleigh polynomial. By the above discussion we have shown that more is 
actually true, namely:

\begin{theorem}\label{t-fg}
For any graph $G$ the polynomial $f_G(\ben,w)$ is real stable.
\end{theorem}

Let $G=(V,E)$ be a graph and let $q>0$ and $0 \leq p \leq 1$ be parameters. 
The {\em random cluster (RC) model}, see \cite{grimmett},  
is the measure $\mu$ on $2^E$ defined 
by 
$$
\mu(F) = \frac 1 {Z_{\text{RC}}} q^{k(F)}p^{|F|}(1-p)^{|E \setminus F|},  
\quad F \subseteq E, 
$$
where $k(F)$ is the number of connected components in the graph $(V,F)$ and 
$Z_{\text{RC}}$ is the appropriate normalizing factor.  
The uniform spanning tree measure can be obtained
from this model by letting $p\to 0$ and $q/p \to 0$, see 
\cite[Section 1.5]{grimmett}. If
$q\geq 1$, the
RC model satisfies PLC and is therefore positively associated. 
If $q\leq1$, NLC is
satisfied, but other negative correlation properties are largely a matter of
conjecture. 
We are interested in properties closed under external fields so we assume 
that $p=1/2$. The generating polynomial of $\mu$ is then a constant multiple 
of the multivariate Tutte polynomial (see \cite{sok}):
$$
Z_G(z,q)= \sum_{F \subseteq E}q^{k(F)}z^F, \quad z=(z_e)_{e\in E}.
$$

If $G=C_n, n \geq 3$, is a cycle and $E=[n]$, then  
$$
Z_G(z,q)= \prod_{j=1}^n(q+z_j) +(q-1)z_1\cdots z_n 
$$
and 
$$
\frac{\partial Z_G}{\partial z_1}\frac{\partial Z_G}{\partial
z_2}-Z_G\frac{\partial^2 Z_G}
{\partial z_1\partial z_2}=  q^2(1-q)\prod_{j=3}^n z_j(q+z_j),
$$
so in this case the RC measure is Rayleigh, but not strongly Rayleigh. 

If $G$ is a tree, then 
$$
Z_G(z,q)= q\prod_{e\in E}(q+z_e),
$$
so the RC model is strongly Rayleigh. 
We conclude that on a
general graph $G$, the RC model is strongly Rayleigh if and only if $G$ is 
acyclic.  

With the help of {\em Mathematica}$^\copyright$, the
third author has verified that the RC model is Rayleigh for all simple 
graphs with at most five vertices.
