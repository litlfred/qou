---
doc_id: arxiv-1501.04614v1
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES"
section_id: sec-003-31-the-highest-degree-and-the-jones-slope
section_title: "The highest degree and the Jones slope."
section_number: 3.1
pages: 9-10
source_pdf: 1501.04614v1.pdf
source_sha256: ebebcae0c1823217
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.938
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES — We continue our study of the degree of the colored Jones polynomial under knot cabling started in [8]."
---
The quantity  $Q(n,k_1,k_2)$ is closely related
to $\delta_K(n)$. According to \cite{GV}  for the 2-fusion knot $K=K(m_1,m_2)$, with $m_2 \notin \{-1, 0\}$, we have the following possibilities:
\vskip 0.04in


\textbf{Case A.} $m_1, m_2 \ge 1$. Then
$$\delta_K(n) = Q(n,k_1,-k_1),$$

\noindent where $$c_1=\frac{1 - m_1 + m_2 + m_2 n}{2 (-1 + m_1 + m_2)},$$ 
and  $k_1$ is of the integers closest to $c_1$ satisfying $k_1 \le n/2$. 

\vskip 0.04in

\textbf{Case B.} $m_1 \le 0, m_2 \ge 1$. There are 2 subcases.

\textbf{(B-1)} ($1 + m_1 + m_2 \le 0$) or ($1 + m_1 + m_2 > 0$ and $1 + 2m_1 + m_2 < 0$). Then
$$\delta_K(n) = Q(n,n,0).$$

\textbf{(B-2)} $1 + m_1 + m_2 > 0$ and $1 + 2m_1 + m_2 \ge 0$. 
 Then
$$\delta_K(n) = Q(n,k_1,k_1-n),$$
\noindent where  $$c_2=\frac{1 - m_1 - m_2 + (1 + m_2) n}{2 (1 + m_1 + m_2)}.$$
and $k_1$ is one of the integers closest to $c_2$.

\textbf{Case C.} $m_2 \le -2$. There are 2 subcases.

\textbf{(C-1)} $m_1 \le -3m_2/2$. Then 
$$\delta_K(n) = Q(n,n,n).$$

\textbf{(C-2)} $m_1 > -3m_2/2$. Let $$c_3=\frac{-3/2 + m_1 + m_2 + (1+m_2 ) n}{1-2m_1-2m_2}$$
and let $k_1$ be one of the integers closest to $c_3$. Then
$$\delta_K(n) = \begin{cases} Q(n,k_1,k_1) &\mbox{if } c_3 \notin \frac{1}{2} + \BZ \\ 
Q(n,k_1,k_1)-(c_3 + 1/2) & \mbox{if } c_3 \in \frac{1}{2} + \BZ \end{cases}$$

We need the following that gives the Jones slopes of 2-fusion knots.

\begin{theorem} \label{a_K}
\cite{DG, GV}
The slope conjecture holds for 2-fusion knot $K=K(m_1,m_2)$. Moreover, we have
$$
 a_K(n) = \begin{cases} m_1 + 2m_2 + \frac{1}{2} + \frac{m_2^2}{4(-1 + m_1 + m_2)} &\mbox{if } (m_1, m_2) \in I_1 \cup I_2, 
\smallskip
\\ 1/2 + 2 m_2   & \mbox{if } (m_1, m_2) \in I_3, 
\smallskip
\\ \frac{3 + 3m_1 + 9m_2}{4} +  \frac{m_1^2}{4(1 + m_1 + m_2)} & \mbox{if } (m_1, m_2) \in I_4, 
\smallskip
\\ 0  & \mbox{if } (m_1, m_2) \in I_5, 
\smallskip
\\ \frac {(2 m_1 + 3 m_2)^2} {2 (-1 + 2 m_1 + 2 m_2)} & \mbox{if } (m_1, m_2) \in I_6.
\end{cases}
$$
\end{theorem}
