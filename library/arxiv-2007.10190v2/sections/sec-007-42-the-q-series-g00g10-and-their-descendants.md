---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-007-42-the-q-series-g00g10-and-their-descendants
section_title: "The q-series (G00,G10) and their descendants"
section_number: 4.2
pages: 8-9
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.951
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
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
