---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-002-12-triangulation-version-of-theorem
section_title: "Triangulation-version of Theorem"
section_number: 1.2
pages: 5-6
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.967
doc_brief: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement — We compute the real part of the semi-classical limit of the sequence of quantum hyperbolic invariants (QHI) of"
---
\label{QHIintro2} Again denote $M:=S^3 \setminus 4_1$, the figure-eight knot complement. Let $(T,b)$ be its usual geometric triangulation with two tetrahedra $U$ and $V$, and with a \textit{branching} $b$ (i.e. an orientation of edges without cycles) as shown in Figure \ref{Teight}.

\begin{figure}[ht]
	\begin{center}
		\includegraphics[width=8cm]{Teight.eps}
		\caption{\label{Teight} The face and edge identifications of a geometric branched ideal triangulation of the figure eight knot complement.}
	\end{center}
\end{figure}

For the following notations, see Section \ref{QGVsec} for details. Denote by $u=(u_0,u_1,u_2)$ and $v=(v_0,v_1,v_2)$ triples of complex shape parameters of ideal hyperbolic tetrahedra associated to the edges of $U$ and $V$, respectively (so $u_i\in \mc_*$, $u_{i+1} = (1-u_i)^{-1}$, and similarly for the $v_i$'s, with indices mod $3$). Assume that they satisfy Thurston's gluing equations along the edges of $T$. Denote by $\rho\colon \pi_1(M)\rightarrow PSL(2,\mc)$ the holonomy defined by $(u,v)$. For each odd integer $N \geqslant 3$, we take $N$-th roots $\bu_{j,N}$ and $\bv_{j,N}$ of $u_{j}$ and $v_{j}$, respectively, thus getting new triples $\bu_N:=(\bu_{0,N},\bu_{1,N},\bu_{2,N})$ and $\bv_N=(\bv_{0,N},\bv_{1,N},\bv_{2,N})$. These $N$-th roots satisfy certain compatibility conditions. 

The invariant $\Hh_{N}(M,\rho,h_\rho,k_c)$ in Theorem \ref{asyinvteo} can be computed as the evaluation at some point $(\bu_N,\bv_N)$ of a rational function $\Hh_{N,(T,b,c)}$ on $\mc^6$. This function results from a {\it state sum} associated to $(T,b)$, {\it i.e.}, the total contraction of a tensor network, whose tensors correspond to the tetrahedra $U$, $V$ (as is common in quantum topology) and are made of quantum dilogarithms. The function $\Hh_{N,(T,b,c)}$ depends on a so-called charge $c$, which is a tuple of integers associated to the pairs of opposite edges of the tetrahedra $U$ and $V$, again satisfying certain compatibility conditions. All these ``certain compatibility conditions'' are fixed by the choices of $h_\rho$ and $k_c$ in Theorem \ref{asyinvteo}. We can thus write 
$$ \Hh_{N}(M,\rho,h_\rho,k_c) = \Hh_{N,(T,b,c)}(\bu_N,\bv_N).$$
For details on $\Hh_{N,(T,b,c)}$ the most computation-oriented readers may want to look at the formulas \eqref{ssumrednonred} (where the charge $c$ has been fixed to some specific value), \eqref{functomegadef} and \eqref{form1}. 
\smallskip

We will see that Theorem \ref{asyinvteo} can be reduced to the following result, which will be our main objective:

\begin{teo}[Triangulation-version of Theorem \ref{asyinvteo}]\label{thm:main_triang}
	Let $(\bu_N)_{N}$ and $(\bv_N)_{N}$ be sequences as above. 	Then, for every charge $c$ the state sum $\Hh_{N,(T,b,c)}$ satisfies:
	\smallskip
	
	\noindent (a) If $\lim_{N\ra +\infty}\bu_{1,N}=-1$ and $\lim_{N\ra +\infty}\bv_{1,N}=-1$, then
	$$\lim_{N\ra +\infty} \frac{2\pi}{N} \Log \vert \Hh_{N,(T,b,c)}(\bu_N,\bv_N)\vert = {\rm Vol}(M).$$ 
	(b)  If $\lim_{N\ra +\infty}\bu_{1,N}=1$ and $\lim_{N\ra +\infty}\bv_{1,N}=1$, then
	$$\lim_{N\ra +\infty} \frac{2\pi}{N} \Log \vert \Hh_{N,(T,b,c)}(\bu_N,\bv_N)\vert = 0.$$
	Moreover, (a) and (b) are the only two possibilities.
\end{teo}
