---
doc_id: arxiv-math-0104104v3
doc_title: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds"
section_id: sec-005-6-quatrisson-action-and-intrinsic-derivative
section_title: "Quatrisson action and intrinsic derivative"
section_number: 6
pages: 10-10
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.979
doc_brief: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds — The purpose of this paper is to describe certain natural 4-vector ﬁelds on quaternionic ﬂag manifolds, which geometrically determine"
---
We elaborate on some general notions related to group actions in the
quatrisson context where we recall the notation set forth
in Definition \ref{def:mult-act} and assume that we have a  multiplicative action.
Denoting   the Lie algebra of $H$ by $\hh$, we 
let:
\begin{displaymath} 
	\gamma: \hh\to \Chi(P)
\end{displaymath}
be the usual Lie algebra  anti-homomorphism, and 
recall the \emph{intrinsic derivative} of $\xi$ at $e$:
\begin{displaymath}
	d_e\xi: \hh\to \Wedge^4 \hh.
\end{displaymath}
We also define the $4$-bracket $[\cdot, \cdot, \cdot, \cdot]$ 
on $\hh^*$ to be the dual of $d\xi_e$. 
The next statement and its proof are analogous to Theorem 2.6 of \cite{LW}. 

\begin{Th} 
	In the above situation 
	for each $X\in\hh$ we have:
	\begin{displaymath}
		\LL_{\gamma(X)}\xi = \wedge^4\gamma(d_e\mu)(X).
	\end{displaymath}
	Moreover, for any $1$-forms $\omega_i$ for $1\le i \le 4$ on $P$ we have:
	\begin{displaymath}
		\LL_{\gamma(X)}\xi(\omega_1\wedge \omega_2 \wedge \omega_3 \wedge \omega_4) = 
		<[\zeta_1,\zeta_2,\zeta_3,\zeta_4],X>
	\end{displaymath}
	where $\zeta_i$ is the $\hh^\ast$-valued function on P defined by:
	\begin{displaymath}
		<\zeta_i,X> = <\omega_i,\gamma(X)> 
		\ \   \mbox{for} X \in \hh 
	\end{displaymath}
	and $[\zeta_1,\zeta_2,\zeta_3,\zeta_4]$ 
	denotes the point-wise $4$-bracket in $\hh^\ast$. 
	\label{th004}
\end{Th}
