---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-023-92-t-system
section_title: "T-system"
section_number: 9.2
pages: 70-70
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.8
latex_coverage_ratio: 1.0
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
\label{subsubsec: T-system} In this subsection, we  recall the {\em $T$-system} among the (unipotent) quantum minors for later use
(see \cite{KNS11} for $T$-system).

\begin{prop} [{\cite[Proposition 3.2]{GLS}}] \label{prop: the ses}
Assume that the Kac-Moody algebra $\g$ is of symmetric type. Assume that $u,v \in W$ and $i \in I$ satisfy $u < us_i$ and $v <
vs_i$. Then
\begin{align*}
& \Delta(us_i\varpi_i,vs_i\varpi_i)\Delta(u\varpi_i,v\varpi_i) =
q^{-1}\Delta(u  s_i \varpi_i,v\varpi_i)\Delta( u\varpi_i, v s_i\varpi_i)
 +\Delta(u\lambda,v\lambda),   \\

& \Delta(u\varpi_i,v\varpi_i)\Delta(us_i\varpi_i,vs_i\varpi_i) =
q\Delta( u\varpi_i\ ,vs_i\varpi_i)\Delta(u  s_i  \varpi_i,v\varpi_i) +
 \Delta(u\lambda,v\lambda)

\end{align*}
and
\begin{align*}
& q^{(vs_i\varpi_i,v\varpi_i-u\varpi_i)}\D(us_i\varpi_i,vs_i\varpi_i)\D(u\varpi_i,v\varpi_i) \allowdisplaybreaks\\
& \hspace{5ex} = q^{-1+(v\varpi_i,vs_i\varpi_i-u\varpi_i)}\D(us_i\varpi_i,v\varpi_i)\D(u\varpi_i,vs_i\varpi_i)  +\D(u\lambda,v\lambda)
\allowdisplaybreaks\\
& \hspace{5ex} = q^{-1+(vs_i\varpi_i,v\varpi_i-us_i\varpi_i)}\D(u\varpi_i,vs_i\varpi_i)\D(us_i\varpi_i,v\varpi_i) + \D(u\lambda,v\lambda),
\allowdisplaybreaks\\
& q^{(v\varpi_i,vs_i\varpi_i-us_i\varpi_i)}\D(u\varpi_i,v\varpi_i)\D(us_i\varpi_i,vs_i\varpi_i) \allowdisplaybreaks\\
& \hspace{5ex} = q^{1+(vs_i\varpi_i,v\varpi_i-us_i\varpi_i)}\D(u\varpi_i,vs_i\varpi_i)\D(us_i\varpi_i,v\varpi_i) + \D(u\lambda,v\lambda)
\allowdisplaybreaks\\
& \hspace{5ex} = q^{1+(v\varpi_i,vs_i\varpi_i-u\varpi_i)}\D(us_i\varpi_i,v\varpi_i)\D(u\varpi_i,vs_i\varpi_i) + \D(u\lambda,v\lambda),
\end{align*}
where  $\lambda=s_i\varpi_i+\varpi_i$. 
\end{prop}
 Note that the difference of $\la$ and $\displaystyle-\sum_{j \ne i}a_{j,i}\varpi_j$ are $W$-invariant.
Hence we have
$\displaystyle \D(u\lambda,v\lambda) = \prod_{j \ne i}\D(u\varpi_j,v\varpi_j)^{-a_{j,i}}$ from Corollary \ref{cor:Duv},
 by disregarding  a power of $q$.
