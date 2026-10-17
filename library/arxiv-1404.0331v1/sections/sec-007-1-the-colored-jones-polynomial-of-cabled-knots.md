---
doc_id: arxiv-1404.0331v1
doc_title: "THE STRONG AJ CONJECTURE FOR CABLES OF TORUS KNOTS"
section_id: sec-007-1-the-colored-jones-polynomial-of-cabled-knots
section_title: "The Colored Jones polynomial of cabled knots"
section_number: 1
pages: 3-4
source_pdf: 1404.0331v1.pdf
source_sha256: 53d7ce3afaf405e1
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.926
doc_brief: "THE STRONG AJ CONJECTURE FOR CABLES OF TORUS KNOTS — The AJ conjecture, formulated by Garoufalidis, relates the A-polynomial and the colored Jones polynomial of a knot in the 3-sphere."
---
\label{cjp}

By \cite{Mo}, the formula for the colored Jones polynomial of the $(r,s)$-cabled knot $K^{(r,s)}$ over a knot $K$ is given by
\begin{equation}
\label{cjp-cable}
J_{K^{(r,s)}}(n)= t^{-rs(n^2-1)} \sum_{j=-\frac{n-1}{2}}^{\frac{n-1}{2}} t^{4rj(js+1)} J_K(2sj+1).
\end{equation}

\begin{lemma}
\label{J_C}
One has
\begin{eqnarray*}
&& J_{K^{(r,s)}}(n+2) - t^{-4rs(n+1)} J_{K^{(r,s)}}(n) \\
&=& t^{-2rs(n+1)} \left( t^{2r(n+1)}J_{K}(s(n+1)+1) - t^{-2r(n+1)}J_{K}(s(n+1)-1) \right).
\end{eqnarray*}
\end{lemma}

\begin{proof}
From Eq. \eqref{cjp-cable} we have
\begin{eqnarray*}
&& J_{K^{(r,s)}}(n+2) - t^{-4rs(n+1)} J_{K^{(r,s)}}(n) \\
&=& t^{-rs((n+2)^2-1)} \sum_{j=-\frac{n+1}{2}}^{\frac{n+1}{2}} t^{4rj(sj+1)} J_K(2sj+1)  - t^{-4rs(n+1)} t^{-rs(n^2-1)} \sum_{j=-\frac{n-1}{2}}^{\frac{n-1}{2}} t^{4rj(js+1)} J_K(2sj+1) \\
&=&t^{-rs((n+2)^2-1)}  \left( t^{r(n+1)(s(n+1)+2)}J_K(s(n+1)+1)+t^{r(n+1)(s(n+1)-2)} J_K(-s(n+1)+1) \right).
\end{eqnarray*}
The lemma follows since $J_K(-s(n+1)+1)=-J_{K}(s(n+1)-1)$.
\end{proof}

\begin{lemma}
\label{J_Cs_2}
One has
$$J_{K^{(r,2)}}(n+1) + t^{-2r(2n+1)}J_{K^{(r,2)}}(n) =  t^{-2rn}J_K(2n+1).$$
\end{lemma}

\begin{proof}
By Eq. \eqref{cjp-cable} we have
\begin{eqnarray*}
J_{K^{(r,2)}}(n+1)=t^{-2r((n+1)^2-1)} \sum_{k=-\frac{n}{2}}^{\frac{n}{2}} t^{4rk(2k+1)} J_K(4k+1).
\end{eqnarray*}
Set $k=-(j+\frac{1}{2}).$ Then
\begin{eqnarray*}
J_{K^{(r,2)}}(n+1) &=& t^{-2r((n+1)^2-1)} \sum_{j=\frac{n-1}{2}}^{-\frac{n+1}{2}} t^{4rj(2j+1)} J_K(-(4j+1))\\
      &=& t^{-2r((n+1)^2-1)} \Big( -\sum_{j=-\frac{n-1}{2}}^{\frac{n-1}{2}} t^{4rj(2j+1)} J_K(4j+1)+t^{2rn(n+1)} J_K(2n+1) \Big)\\
      &=&-t^{-2r(2n+1)} J_{K^{(r,2)}}(n)+t^{-2rn} J_K(2n+1).
\end{eqnarray*}
This proves Lemma \ref{J_Cs_2}.
\end{proof}

\begin{remark}
The proofs of Lemmas \ref{J_C} and \ref{J_Cs_2} are similar to those of Lemmas 1.1 and 1.5 in \cite{Tr}. See also Propositions 3 and  5 in \cite{Hi}, and Lemma 3.1 and Section 6.1 in \cite{RZ}.
\end{remark}
