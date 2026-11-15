---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-011-35-low-crossing-knots-with-period-two
section_title: "Low crossing knots with period two"
section_number: 3.5
pages: 17-18
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.968
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
Theorem \ref{thm-quasi} applies to several non-alternating knots with 8 and 9 crossings.  The Jones slopes of all non-alternating prime knots with up to nine crossings were calculated by Garoufalidis in Section 4 of \cite{Ga-slope}.
According to \cite{Ga-slope} the knots of 
 period two are the ones shown in Table 1. 
The remaining knots, which are $8_{20}, 9_{43}, 9_{44}$, have periods 3 and they will be treated in Section \ref{constant a(n)}.





\begin{table}[]
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline
$K$& $js_K \cup js^*_K $ & $b(n)$ & $b^*(n)$ \\
\hline
$8_{19}$ &$ \{12,0\}$ &  $0$ & $5/2$ \\
\hline
$8_{21}$ & $\{1,-12\}$ & $-1$ & $3/2$ \\
\hline
$9_{42}$  & $\{6,-8\}$ & $-1/2$ & $5/2$ \\
\hline
$9_{45}$  & $ \{1,-14\}$ & $-1$ & $2$ \\
\hline
$9_{46}$  & $ \{2,-12\}$ & $-1/2$ & $5/2$ \\
\hline
$9_{47}$  & $ \{9,-6\}$ & $-1$ & $2$\\
\hline
$9_{48}$ & $\{11,-4\}$ & $-3/2$ & $3/2$\\
\hline
$9_{49}$ & $ \{15,0\}$ & $-3/2$ & $3/2$\\
\hline
 \end{tabular}
\vskip 0.3in 
\caption{ The knots up to nine crossings of period two.}

\end{center}
\end{table}
\begin{corollary} \label{low} Let $K$ be any knot of Table 1 and let $K'$ be an iterated cable of $K$.
Then $K'$ satisfies the Slope Conjecture.
\end{corollary}

\begin{proof}
Due to different conventions and normalizations of the colored Jones polynomial, $d_+[J_K(n)]$ (resp. $d_-[J_K(n)]$) in our paper is different from $\delta_K(n)$ (resp. $\delta_K^*(n)$) in \cite{Ga-slope}. For $n>0$ we have
\begin{eqnarray*}
d_+[J_K(n)] &=&  \delta_K(n-1) + (n-1)/2,\\
d_-[J_K(n)] &=&  \delta_K^*(n-1) + (1-n)/2.
\end{eqnarray*}
 
Consider the non-alternating knot $K=8_{19}$. By \cite[Section 4]{Ga-slope} we have
\begin{eqnarray*}
d_+[J_K(n)] &=& 3n^2-\big( 13+(-1)^n \big)/4,\\
d_-[J_K(n)] &=& 5(n-1)/2.
\end{eqnarray*} 
Moreover, $js_K = \{12\} \subset bs_K$ and $js^*_K = \{0\} \subset bs_K$.  In particular, the Jones slopes are integers and we have
$b(n) \le 0$ and $b^{*}(n) \ge 0$.  Similar analysis applies to the knots of Table 1.

Now given a cable $\K$ of $K$, since $\abs{q}>1$, $p/q$ is not a Jones slope of $K$.
 Theorem \ref{thm-quasi}  implies that $js_{\K} \subset bs_{\K}$  and that $js^*_{\K} \subset bs_{\K}$. In particular, $\K$ satisfies the Slope Conjecture. Applying this argument repeatedly we obtain the result for iterated cables.
\end{proof}
