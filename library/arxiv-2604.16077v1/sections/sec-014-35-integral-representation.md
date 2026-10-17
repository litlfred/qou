---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-014-35-integral-representation
section_title: "Integral representation"
section_number: 3.5
pages: 33-34
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.88
latex_coverage_ratio: 0.941
doc_brief: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement — We compute the real part of the semi-classical limit of the sequence of quantum hyperbolic invariants (QHI) of"
---
\label{INTREPEST} As we are going to consider the functions in \eqref{form1} when $N\rightarrow +\infty$, we re-introduce now the hidden dependence on $N$ in the notations, thus letting $(\bu_N)_N:=((\bu_{0,N},\bu_{1,N},\bu_{2,N}))_N$ be a sequence of triples of quantum shape parameters on $\Delta^0$ as in Section \ref{4_1}. Contrary to the more general situation considered in Section \ref{ASYWEIGHTS}, here we assume that $\bu_{k,N}^N$ is constant. Thus, as in \eqref{qshapeuvoct25} we write \begin{equation}\label{recapuvarmars25} \bu_{k,N} = \exp(\bl_{k,N}),\ \bl_{k,N}:= \frac{1}{N}(\Log(u_{k}) +\pi ia_{k}) + \pi i a_k, a_{k}\in \mz.\end{equation}
Using the formula \eqref{relomS0} one can write \eqref{sumS} as
\begin{equation}
\Sigma_N(\bu_{0,N},\bu_{1,N}) = 1 + \frac{1}{\hat S_N(\bl_{0,N})}\sum_{\beta=1}^{N-1} e^{\frac{2\pi i}{N} \beta^2 -\bl_{1,N}\beta} \textstyle \hat S_N(\bl_{0,N}+2\beta i\pi/N).\label{int01}
\end{equation}
Note that for $\beta\in \mz$ we have $e^{\bl_{1,N}\beta} = e^{(\bl_{1,N}+2i\pi k)\beta}$ for any $k \in \mz$, so the formula \eqref{int01} is invariant under translation of $\bl_{1,N}$ by $2i\pi$. In fact, because the QHI solely depend on the quantum shape parameters $\bu_{k,N}$ and $\bv_{k,N}$, by adding even integers to $a_0$ or $a_1$ if necessary we can assume that in the above formula we have
\begin{equation}\label{situation2}
\forall N,\ \mathfrak{I}(\bl_{0,N})\in ]-2\pi,0]\ ,\ \mathfrak{I}(\bl_{1,N})\in ]0,2\pi].
\end{equation}

Recall that the poles of $\hat S_N(z)$ are the points $z=2i\pi+2pi\pi/N$, $p\in \mn$, the simple poles being those with $p\in \{0,\ldots,N-1\}$ (see \eqref{PP1}). On another hand the poles of $\coth(Nz/2)$ are the points $z=2i\pi \beta/N$, $\beta\in \mz$, and they are all simple poles, with residue $2/N$. Because $\mathfrak{I}(\bl_{0,N})\subset ]-2\pi,0]$, it follows that the function
$$\textstyle\phi\colon z\mapsto \hat S_N(\bl_{0,N}+z)\coth(\frac{Nz}{2})\frac{N}{2}$$
is meromorphic in the half-space $\{\textstyle \mathfrak{I}(z) < 2\pi\}$, and has poles $\textstyle z_\beta:=2i\pi \beta/N$ where $\beta\in\mz$, $\beta\leq N-1$. These poles are simple, and ${\rm Res}(\phi,z_\beta) =\hat S_N(\bl_{0,N}+2\beta i\pi/N)$. 

Let $C_N$ be the boundary of a rectangle with counter clockwise orientation, sides parallel to the real and imaginary axes, containing the segment $\textstyle i[\frac{2\pi}{N},2\pi-\frac{2\pi}{N}]$ in its interior, and close to it so that we have constants $\varepsilon>0$ and $s_N^-,s_N^+\in ]0,\textstyle \frac{2\pi}{N}[$ satisfying  
\begin{equation}\label{choiceCN}
C_N \subset \{\vert \mathfrak{R}(z) \vert \leq \varepsilon\}\cap \{s_N^-\leq \mathfrak{I}(z) \leq 2\pi-s_N^+\}\ . \end{equation}
See Figure \ref{fig:contours:CN+-}. An immediate application of Cauchy's residue theorem gives:
\begin{lem}\label{lemintrep} Assuming \eqref{situation2} and \eqref{choiceCN}, we have
\begin{equation}\label{int1}
\Sigma_N(\bu_{0,N},\bu_{1,N}) =1+ \frac{1}{\hat S_N(\bl_{0,N})} \frac{N}{4i\pi}\int_{C_N} e^{\frac{N}{2i\pi}(z^2 - \bl_{1,N}z)}\hat S_N(\bl_{0,N} + z)\textstyle \coth(\frac{Nz}{2})dz.
\end{equation}
\end{lem}
