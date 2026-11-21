---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-030-84-the-maximum-of-the-r-matrices-at-roots-of-uni
section_title: "The maximum of the R-matrices at roots of unity"
section_number: 8.4
pages: 22-22
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.963
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
Proposition \ref{prop.R} gives the maximum of the growth rate of
$\ev_n(R_+(n;a,b,k))$, as $n\to \infty$. The following proposition
gives the maximum of $\ev_n(R_+(n;a,b,k))$, for a fixed $n$.

\begin{proposition}
\lbl{prop.Rpm} {\rm (Proof in Section \ref{sub.pf71})}
The value of
$|\ev_n(R_+(n;a,b,k))|$ achieves maximum at $a= \lfloor 3n/4
\rfloor$, $b= \lfloor (n-1)/4 \rfloor$, and $k= a-b$. The value of
$|\ev_n(R_-(n;a,b,k))|$ achieves maximum at $a= \lfloor (n-1)/4
\rfloor$, $b= \lfloor 3n/4 \rfloor$, and $k= b-a$. The maximum
value of $|\ev_n(R_+(n;a,b,k))|$ is the same as that of
$|\ev_n(R_-(n;a,b,k))|$. 
\end{proposition}


Note that for these optimal values in the $R_+$ case, $ |a-3n/4| \le
1$, $|b-n/4| \le 1$ and $|k-n/2| \le 1$. The proof of this
proposition will be given in Appendix \ref{CCC}.

From Corollary \ref{87} and Propositions \ref{prop.R+limit},
\ref{prop.R} and \ref{prop.Rpm}, we have the following.

\begin{corollary}\label{86}
The growth rate of the maximum of
$|\ev_n(R_+(n;a,b,k))|$ is given by
$$ \lim_{n\to \infty} \frac{\max_{a, b, k} \log |\ev_n(R_\pm(n;a,b,k))| }{n}
= \frac{v_8}{2 \pi}.
$$
\end{corollary}
