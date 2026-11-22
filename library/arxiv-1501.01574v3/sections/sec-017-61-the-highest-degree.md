---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-017-61-the-highest-degree
section_title: "The highest degree."
section_number: 6.1
pages: 26-27
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.81
latex_coverage_ratio: 1.0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
The quantity  $Q(n,k_1,k_2)$ is closely related
to the degree $\delta_K(n)$. According to \cite{GV}  for the 2-fusion knot $K=K(m_1,m_2)$, with $m_2 \notin \{-1, 0\}$, we have the following possibilities:
\vskip 0.04in


\textbf{Case A.} Suppose that $m_1, m_2 \ge 1$. Then
$$\delta_K(n) = Q(n,k_1,-k_1),$$

\noindent where $$c_1=\frac{1 - m_1 + m_2 + m_2 n}{2 (-1 + m_1 + m_2)},$$ 
and  $k_1$ is of the integers closest to $c_1$ satisfying $k_1 \le n/2$. 

\vskip 0.04in

\textbf{Case B.} Suppose that $m_1 \le 0, m_2 \ge 1$. There are 2 subcases.

\textbf{(B-1)} We have ($1 + m_1 + m_2 \le 0$) or ($1 + m_1 + m_2 > 0$ and $1 + 2m_1 + m_2 < 0$). Then
$$\delta_K(n) = Q(n,n,0).$$

\textbf{(B-2)}  We have $1 + m_1 + m_2 > 0$ and $1 + 2m_1 + m_2 \ge 0$. 
 Then
$$\delta_K(n) = Q(n,k_1,k_1-n),$$
\noindent where  $$c_2=\frac{1 - m_1 - m_2 + (1 + m_2) n}{2 (1 + m_1 + m_2)}.$$
and $k_1$ is one of the integers closest to $c_2$.

\textbf{Case C.} Suppose that  $m_2 \le -2$. There are 2 subcases.

\textbf{(C-1)} We have $m_1 \le -3m_2/2$. Then 
$$\delta_K(n) = Q(n,n,n).$$

\textbf{(C-2)} We have $m_1 > -3m_2/2$. Let $$c_3=\frac{-3/2 + m_1 + m_2 + (1+m_2 ) n}{1-2m_1-2m_2}$$
and let $k_1$ be one of the integers closest to $c_3$. Then
$$\delta_K(n) = \begin{cases} Q(n,k_1,k_1) &\mbox{if } c_3 \notin \frac{1}{2} + \BZ, \\ 
Q(n,k_1,k_1)-(c_3 + 1/2) & \mbox{if } c_3 \in \frac{1}{2} + \BZ. \end{cases}$$
