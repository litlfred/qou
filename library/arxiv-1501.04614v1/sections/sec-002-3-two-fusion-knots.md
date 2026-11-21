---
doc_id: arxiv-1501.04614v1
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES"
section_id: sec-002-3-two-fusion-knots
section_title: "Two-fusion knots"
section_number: 3
pages: 7-9
source_pdf: 1501.04614v1.pdf
source_sha256: ebebcae0c1823217
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 1.0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES — We continue our study of the degree of the colored Jones polynomial under knot cabling started in [8]."
---
The family of 2-fusion knots is a two-parameter family  of closed 3-braids denoted
by
$$\{ K(m_1, m_2)  \mid  m_1, m_2\in \ZZ\}.$$
For the precise definition and description see \cite {GV, DG}. 

Note that $K(m_1, m_2)$ is a torus knot if $m_2 \in \{-1,0\}$. In fact, $K(m_1, 0) = T(2, 2m_1 + 1)$ and $K(m_1, -1) = T(2, 2m_1 -3)$. It is known that $K(m_1, m_2)$ is hyperbolic if $m_1 \notin \{0, 1\}$, $m_2 \notin \{-1,0\}$ and $(m_1, m_2) \not= (-1,1)$. See \cite{GV}. Note that $K(-1,1) = T(2,5)$.

From now on we consider $m_2 \notin \{-1,0\}$ only. Let 
\begin{eqnarray*}
I_1 &=& \{(m_1, m_2) : m_2 \ge 1 \text{ and } m_1 \ge 2\}, \smallskip \\
I_2 &=& \{(m_1, m_2) : m_2 \ge 1 \text{ and } m_1 = 1\}, \smallskip \\
I_3 &=& \{(m_1, m_2) : m_2 \ge 1 \text{ and } m_1  \le -(m_2 + 1)\} \\
&& \cup \, \{(m_1, m_2) : m_2 \ge 1 \text{ and } -(m_2 + 1)/2 > m_1 > -(m_2 + 1)\},\smallskip\\
I_4 &=& \{(m_1, m_2) : m_2 \ge 1 \text{ and } 0 \ge m_1 \ge - (m_2 + 1)/2\}, \smallskip\\
I_5 &=& \{(m_1, m_2) : m_2 \le -2 \text{ and }  m_1 \le -3m_2/2\}, \smallskip\\
I_6 &=& \{(m_1, m_2) : m_2 \le -2 \text{ and } m_1 > -3m_2/2\}.
\end{eqnarray*}
and let $\CS_{m_1, m_2}$ be the set of coprime pairs $(p,q)$, with $q>1$, such that

\begin{itemize}

\item  If $ (m_1, m_2) \in I_1$, then   $p- \left( 4m_1 + 8m_2 + 2 + \frac{m_2^2}{ m_1 + m_2 - 1} \right) q < 0$ or 

$p- \left( 4m_1 + 8m_2 + 2 + \frac{m_2^2}{ m_1 + m_2 - 1} \right) q > \frac{(1 - m_1 + m_2)^2}{4(m_1 + m_2 -1)}$.

\smallskip

\item  If $ (m_1, m_2) \in I_2$,  then $p- ( 9 m_2 + 6) q > \frac{3m_2}{4} \mbox{ or } p- ( 9 m_2 + 6) q < 0$.





\smallskip

\item If $ (m_1, m_2) \in I_4$, then $p-\left( 3m_1 + 9m_2 + 3 + \frac{m_1^2}{m_1 + m_2+1} \right) q < 0$ or 

$p- \left( 3m_1 + 9m_2 + 3 + \frac{m_1^2}{m_1 + m_2+1} \right) q > \max\{  \frac{m_1 + m_2 -1}{4} + \frac{m_1 (m_2 - 1)}{m_1 + m_2 + 1}, 0\}$.






\smallskip

\item If $(m_1, m_2) \in I_6$, then
$p- \frac {2(2 m_1 + 3 m_2)^2 + m_2 + 1} {2 m_1 + 2 m_2-1}  q < 0$ or

$p- \frac {2(2 m_1 + 3 m_2)^2 - (m_2 + 1)} {2 m_1 + 2 m_2-1}  q > \max\{ \frac{2m_1 + 2m_2 -1}{8} + \frac{(2m_1-6) (m_2+1)}{2m_1 + 2m_2 - 1}, 0\}$.
\end{itemize}

\begin{theorem}
\label{thm:slope-cable} Let $K=K(m_1, m_2)$ be a  2-fusion knot. Then, 

\begin{enumerate}
\item Conjectures  \ref{conj} and \ref{slope}  hold  for $K$.
\item Conjectures \ref{conj} and \ref{slope} hold true for $(p,q)$-cables of the 2-fusion knot $K(m_1, m_2)$, where $(p,q) \in \CS_{m_1,m_2}$.
\end{enumerate}
\end{theorem}

Due to different conventions and normalizations of the colored Jones polynomial, the degree $d_+[J_K(n)]$ in our paper is different from $\delta_K(n)$ in \cite{GV}. For $n>0$ we have $$d_+[J_K(n)] =  \delta_K(n-1) + (n-1)/2.$$




For $n \in \BN$ and $k_1, k_2 \in \BZ$ such that $0 \le k_1 \le n$ and $|n-2k_1| \le n+2k_2 \le n+2k_1$, let
\begin{eqnarray*}
Q(n,k_1,k_2)&=& \frac{k_1}{2} - \frac{3 k_1^2}{2} - 3 k_1 k_2 - k_2^2 - k_1 m_1 - k_1^2 m_1 - k_2 m_2 - k_2^2 m_2 - 6 k_1 n \\ 
& & - \, 3 k_2 n + 2 m_1 n + 4 m_2 n - k_2 m_2 n - 2 n^2 + m_1 n^2 + 2 m_2 n^2 \\ 
& & + \, \frac{1}{2} \left( (1 + 8 k_1 + 4 k_2 + 8 n) \min\{l_1,l_2,l_3\} - 3 \min\{l_1,l_2,l_3\}^2\right)
\end{eqnarray*}
where
$$
l_1=2 k_1 + n, \qquad l_2=2 k_1 + k_2 + n, \qquad l_3=k_2 + 2 n.
$$
