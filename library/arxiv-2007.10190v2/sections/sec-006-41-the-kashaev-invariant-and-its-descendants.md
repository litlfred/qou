---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-006-41-the-kashaev-invariant-and-its-descendants
section_title: "The Kashaev invariant and its descendants"
section_number: 4.1
pages: 7-8
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.921
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
\label{sub.k41}

The series $\Phi_{\s_1} (\tau)$ appearing in the saddle-point
expansion of the state integral appeared originally in the asymptotic
expansion of the Kashaev invariant \cite{K95}. In the case of the
$4_1$ knot, the Kashaev invariant is given by

\begin{equation}
\label{J41}
\J^{(4_1)}(q) = \sum_{n=0}^\infty (q;q)_n (q^{-1};q^{-1})_n \,.
\end{equation}
The above expression can be evaluated when $q$ is a root of unity. The
Volume Conjecture of Kashaev~\cite{kas-volume} (and its extension to all orders \cite{gukov}) 
asserts that $\J^{(4_1)}(\re^{2 \pi \ri/N})$ has
an asymptotic expansion for $N$ large of the form

\begin{equation}
\label{J41Phi}
\J^{(4_1)}(\re^{2 \pi \ri/N}) \sim N^{3/2}\,
\Phi_{\s_1}\left(\frac{1}{N}\right). 
\end{equation}














We now explain a relation discovered in~\cite{GZ:kashaev} 
between the formula for the Kashaev invariant~\eqref{J41} and the
algebraic equation~\eqref{41xi}.

Following~\cite{GZ:kashaev}, we define the descendants
$\J^{(4_1)}_m(q)$ of the Kashaev invariant of the $4_1$ knot by
\begin{equation}
\label{J41m}
\J^{(4_1)}_m(q) = \sum_{n=0}^\infty (q;q)_n (q^{-1};q^{-1})_n \, q^{m n},
\qquad (m \in \BZ) \,.
\end{equation}
Then, the sequence $\J^{(4_1)}_m(q)$ is a solution to a linear $q$-difference
equation
\begin{equation}
\label{qdiffJ}
q^{m+1} \J_m(q) + (1-2q^m)\J_m(q) + q^{m-1} \J_{m-1}(q) =1,
\qquad (m \in \BZ) \,.
\end{equation}
This can be seen as follows: let
\begin{equation}
\label{anm41}
a_{n,m}(q)=
(q;q)_n (q^{-1};q^{-1})_n q^{m n}
\end{equation}
denote the summand of~\eqref{J41m}. It follows that
\begin{subequations}
  \begin{align}
    \label{ap1}
    a_{n+1,m}(q) &= (1-q^{-n-1})(1-q^{n+1}) \,a_{n,m}(q) \\
    \label{ap2}
    &= q^m(2-q^{n+1}-q^{-n-1}) \, a_{n,m}(q) \\
    \label{ap3}
  &= q^m(2-q \, a_{n,m+1}(q)-q^{-1} a_{n,m-1}(q)) \,.
\end{align}
\end{subequations}
Summing over $n \geq 0$ and taking into account the boundary term
$a_{0,m}(q)=1$ on the left hand side of the above equation concludes the
proof of Equation~\eqref{qdiffJ}.

Using the operators $E$ and $Q$ that act on sequences $(y_m)$ by
\begin{equation}
\label{EQ}
(Ey)_m=y_{m+1}, \qquad (Qy)_m=q^m y_m, \qquad EQ=qQE
\end{equation}
it follows that we can write~\eqref{qdiffJ} in the form
\begin{equation}
\label{qdiffJ2}
( Q(1-qE)(1-q^{-1}E^{-1}) - I) \J_m(q) = 1 \,.
\end{equation}
The homogeneous part of the above operator can be obtained by
replacing $x$ in the left hand side of Equation~\eqref{41xi} $x$ by
$qE$, and replacing the right hand side of Equation~\eqref{41xi} by
$Q^{-1}$.
