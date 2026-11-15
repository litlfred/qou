---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-004-41-the-kashaev-invariant-and-its-descendants
section_title: "The Kashaev invariant and its descendants"
section_number: 4.1
pages: 7-9
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.917
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


\subsection{The $q$-series $(G^0_0,G^1_0)$ and their
  descendants}
\label{sub.gG41}

We now discuss an appearance of the formal power series $\Phi(\tau)$
in the radial asymptotics of some $q$-series, following~\cite{GZ:qseries}.

By $q$-series we mean formal Laurent series in a variable $q$ with
integer coefficients, i.e., elements of $\BZ((q))$.  All the
$q$-series below will define holomorphic functions in the punctured
unit disk with (perhaps) a pole at the origin.  We now recall how the
radial asymptotics of the $q$-series $(G^0_0,G^1_0)$ is given by
$\Phi(\tau)$. The first series $G^0_0(q)$ was found quite by accident
to have radial asymptotics expressed in terms of the series
$\Phi(\tau)$~\cite{GZ:qseries}, whereas the second series was found
systematically by expressing the state integral invariant of the $4_1$
knot in terms of products of $q$-series and
$\tq$-series~\cite{GK:qseries}.

Below, we will use capital letters for $q$-series and small letters
for the corresponding functions on the upper half-plane, e.g.,
$g^0_m(\tau)=G^0_m(q)$ for $q=\re^{2\pi
  \ri\tau}$. In~\cite{GZ:qseries} it was observed that we have an
asymptotic expansion

\begin{equation}
\label{gGtau}
\begin{pmatrix} \frac{1}{\sqrt{\tau}} g^0_0(\tau) \\
  \sqrt{\tau} g^1_0(\tau)
\end{pmatrix} \sim \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}
  \Phi( \tau) 
\end{equation}

to all orders in $\tau$, as $\tau$ tends to $0$ along a ray in the
first quadrant of the upper half-plane. The above asymptotic expansion
requires some explanation since on a fixed ray in the first quadrant,
$\Phi_{\s_1}( \tau)$ is exponentially larger than
$\Phi_{\s_2}(\tau)$. Nonetheless, the asymptotic
expansion~\eqref{gGtau} makes sense theoretically and computationally
if we use a refined optimal truncation explained in detail
in~\cite{GZ:kashaev} and applied in~\cite{GZ:qseries}. The numerical
computations of~\cite{GZ:qseries} hinted that the matrix in
Equation~\eqref{gGtau} is the constant term of a matrix of $\tq$
series.

Given the definition of $G^0_0(q)$ and $G^1_0(q)$ from~\cite{GZ:qseries}
and~\cite{GK:qseries}, it was relatively straightforward to add the
variable $q^{m n}$ and arrive to formulas~\eqref{gm} and~\eqref{Gm}
which define the descendants of the pair $(G^0_0(q),G^1_0(q))$.
