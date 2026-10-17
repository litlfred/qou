---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-005-21-the-quantum-gluing-varieties
section_title: "The quantum gluing varieties"
section_number: 2.1
pages: 9-10
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.965
doc_brief: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement — We compute the real part of the semi-classical limit of the sequence of quantum hyperbolic invariants (QHI) of"
---
\label{QGVsec} These form the parameter spaces of the QHI state sum formulas. 


\subsubsection{Quantum $3$-simplices} (see \cite{AGT}, Section 3)\label{sec:q3Delta} A {\it quantum $3$-simplex} is a tuple $(\Delta,b,\bw)$ where:
\begin{itemize}
\item $(\Delta,b)$ is an oriented tetrahedron with ordered vertices, say $v_0,\ldots,v_3$. The letter ``$b$'' denotes the system of edge orientations, called {\it branching}, which encodes the vertex ordering and is defined by the rule: an edge with endpoints $v_i$ and $v_j$ points towards $v_j$ if $j>i$. 

\noindent We call $(\Delta,b)$ a {\it branched tetrahedron}. It has a natural {\it $b$-orientation}, defined by the ordered triple of oriented edges $(v_0v_1)$, $(v_0v_2)$ and $(v_0v_3)$. We encode this $b$-orientation by a sign $*_b(\Delta)\in \{-1,+1\}$: $*_b(\Delta)=+1$ if the $b$-orientation coincides with the given orientation of $\Delta$, $*_b(\Delta)=-1$ otherwise.
\item $\bw:=(\bw_0,\bw_1,\bw_2)\in \mc^*$ satisfies the following requirements: 
\smallskip

\noindent (a) $w:=(w_0,w_1,w_2) := (\bw_0^N,\bw_1^N,\bw_2^N)\in (\mc_*)^3$, and we have the relations
\begin{equation}\label{cyclicshapeoct25}
w_{i+1}=\frac{1}{1-w_i}\quad {\rm (indices\ mod}(3));
\end{equation}
 \noindent (b) We have
 \begin{equation}\label{tetrelbasique}
 \bw_0\bw_1\bw_2 =e^{-*_b(\Delta)\frac{\pi i}{N}}.
 \end{equation}
 We call $w_i$ and $\bw_i$ a {\it shape parameter} and a {\it quantum shape parameter}, respectively.
 \end{itemize} 
 
One can regard $w_0,w_1,w_2$ as the three cross ratios of a $4$-tuple of points in $\mc\mathbb{P}^1=\partial_\infty \mh^3$, ordered up to even permutations. The triple $(w_0,w_1,w_2)$ up to cyclic permutations parametrizes the equivalence class of the $4$-tuple up to the action of Moebius transformations on $\mc\mathbb{P}^1$; equivalently, $(w_0,w_1,w_2)$ up to cyclic permutations parametrizes an orientation preserving isometry class of $3$-dimensional hyperbolic ideal tetrahedra (see {\it e.g.} \cite[Chapter E.6-i]{BP}). Each shape parameter is naturally assigned to a specific pair of opposite edges of $(\Delta,b)$: $w_0$ to the edges $(v_0v_1)$ and $(v_2v_3)$, $w_1$ to the edges $(v_1v_2)$ and $(v_0v_3)$, and $w_2$ to the edges $(v_0v_2)$ and $(v_1v_3)$. This way, e.g., $w_0$ computes the dilation coefficient of the loxodromic element in $PSL(2,\mc)$ fixing $v_0$ and $v_1$ and mapping $v_2$ to $v_3$.

Therefore a quantum $3$-simplex $(\Delta,b,\bw)$ encodes an hyperbolic ideal $3$-simplex up to isometry, plus a choice of $N$-th root $\bw_i$ of each shape parameter $w_i$, assigned to the same pair of opposite edges of $(\Delta,b)$, as described above. 
\medskip

Let $(\Delta,b,\bw)$ be a quantum $3$-simplex. We can write the quantum shape parameters in the form  
\begin{equation}\label{ecoldef}\bw_k = \exp\left(\frac{1}{N}(\Log(w_k) +2\pi i e_k)\right),
\end{equation}
where $e_0,e_1,e_2\in \mz/N$ satisfy
\begin{equation}\label{etetcol}
\sum_{k=0,1,2} (\Log(w_k) +2\pi i e_k) = -*_b\! (\Delta)\pi i\quad {\rm mod}(2\pi i N).
\end{equation}
We call $e_k$ a {\it (edge) $N$-color}. Alternatively, since $N$ is odd the map $\mz \rightarrow \mz/N\mz$, $d\mapsto \textstyle \overline{\frac{(N+1)}{2} d}$, is well-defined and surjective. Therefore it is also possible to write
\begin{equation}\label{coldef}\bw_k = \exp\left(\frac{1}{N}\left(\Log(w_k) +\pi i (N+1)d_k\right)\right),
\end{equation}
where $d_k \in \mz$ and 
\begin{equation}\label{tetcol}
\sum_{k=0,1,2} (\Log(w_k) +\pi i d_k) = -*_b\! (\Delta)\pi i.
\end{equation}
The usefulness of the expression \eqref{coldef} will be explained in Remark \ref{defflatcharge}. We call $d_k$ a {\it (edge) color}, and $\Log(w_k) +\pi i d_k$ a {\it log-parameter}. Since the shape parameters $w_k$ have imaginary parts of the same sign and $\textstyle \sum_{k=0,1,2} \Log(w_k) = {\rm sign}(\mathfrak{I}(w_0))\pi i$, we have
\begin{equation}\label{sumdeven}
d_0+d_1+d_2 = -*_b\! (\Delta)- {\rm sign}(\mathfrak{I}(w_0))\in \{-2,0,2\}.
\end{equation}
