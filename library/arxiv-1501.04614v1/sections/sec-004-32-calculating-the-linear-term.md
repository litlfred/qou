---
doc_id: arxiv-1501.04614v1
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES"
section_id: sec-004-32-calculating-the-linear-term
section_title: "Calculating the linear term"
section_number: 3.2
pages: 10-13
source_pdf: 1501.04614v1.pdf
source_sha256: ebebcae0c1823217
toc_source: outline
text_source: latex
latex_prose_ratio: 0.872
latex_coverage_ratio: 0.958
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES — We continue our study of the degree of the colored Jones polynomial under knot cabling started in [8]."
---
\begin{theorem}

\label{prop:b}

For the 2-fusion knot $K=K(m_1,m_2)$, with $m_2 \notin \{-1,0\}$, we have
$$
b_K(n) = \begin{cases} \frac{m_2(1-m_1)}{2(-1+m_1+m_2)} &\mbox{if } (m_1, m_2) \in I_1 \cup I_2, 
\smallskip
\\ 1 + m_1  & \mbox{if } (m_1, m_2) \in I_3, 
\smallskip
\\ \frac{m_1(m_2-1)}{2(1+m_1+m_2)}   & \mbox{if } (m_1, m_2) \in I_4, 
\medskip
\\ 5/2 + m_1 + 3 m_2  & \mbox{if } (m_1, m_2) \in I_5, 
\smallskip
\\ \frac {(-5 + 2m_1)(1 + m_2)} {2 (-1 + 2 m_1 + 2 m_2)} & \mbox{if } (m_1, m_2) \in I_6 \mbox{ and } \frac {-1+(1 + m_2)(n-1)} {-1 + 2 m_1 + 2 m_2} \notin  \BZ,
\medskip
\\ \frac {(-3 + 2m_1)(1 + m_2)} {2 (-1 + 2 m_1 + 2 m_2)} & \mbox{if } (m_1, m_2) \in I_6\mbox{ and } \frac {-1+(1 + m_2)(n-1)} {-1 + 2 m_1 + 2 m_2} \in  \BZ.
\end{cases}
$$
In particular we have $b_K(n) \le 0$. Moreover $b_K(n) = 0$ if and only if $m_1 \in \{0,1\}$ and $m_2 \ge 1$, or $(m_1, m_2) = (-1,1)$.
\end{theorem}

\begin{proof} As in the previous subsection, there are 3 cases.

\vskip 0.04in

\textbf{Case A.} $m_1, m_2 \ge 1$. Recall that $$c_1=\frac{1 - m_1 + m_2 + m_2 n}{2 (-1 + m_1 + m_2)}$$ 
and $k_1$ is one of the integers closest to $c_1$ satisfying $k_1 \le \frac{n}{2}$. We have
\begin{eqnarray*}
\delta_K(n) = Q(n,k_1,-k_1)
&=& (1-m_1-m_2) k_1^2 + ( 1 - m_1 + m_2 + m_2 n) k_1 \\
&& + \, 2 m_1 n + 4 m_2 n  + m_1 n^2 + 2 m_2 n^2 + \frac{n}{2} + \frac{n^2}{2}.
\end{eqnarray*}

Write $k_1 = c_1 + r_n$ where $r_n$ is a periodic sequence with $\begin{cases} |r_n| \le 1/2 &\mbox{if } m_1 \ge 2, 
\\ r_n \in \{-1/2, -1\}  & \mbox{if } m_1 = 1. 
\end{cases}$ We have
$$
\delta_K(n) = Q(n,c_1+r_n,-c_1-r_n) = Q(n,c_1,-c_1) + (1-m_1-m_2) r_n^2
$$
and
\begin{eqnarray*}
Q(n,c_1,-c_1) &=& 2 m_1 n + 4 m_2 n  + m_1 n^2 + 2 m_2 n^2 + \frac{n}{2} + \frac{n^2}{2} -\frac{( 1 - m_1 + m_2 + m_2 n)^2}{4(1-m_1-m_2)} \\
&=& \left( m_1 + 2m_2 + \frac{1}{2} + \frac{m_2^2}{4(-1 + m_1 + m_2)} \right) n^2 \\
&& + \,  \left( 2m_1 + 4m_2 + \frac{1}{2} + \frac{m_2(1-m_1+m_2)}{2(-1 + m_1 + m_2)} \right) n - \frac{( 1 - m_1 + m_2)^2}{4(1-m_1-m_2)}.
\end{eqnarray*} 

Since $d_+[J_K(n)] = \delta_K(n-1) + (n-1)/2$ we obtain
\begin{eqnarray*}
d_+[J_K(n)] &=& \left( m_1 + 2m_2 + \frac{1}{2} + \frac{m_2^2}{4(-1 + m_1 + m_2)} \right) n^2 + \frac{m_2(1-m_1)}{2(-1+m_1+m_2)} n\\
&& - \, \left( m_1 + 2m_2 + \frac{1}{2} - \frac{(1-m_1)^2}{4(-1 + m_1 + m_2)} \right) + (1-m_1-m_2) r^2_{n-1}.
\end{eqnarray*} 

\textbf{Case B.} $m_1 \le 0, m_2 \ge 1$.  There are 2 subcases.

\textbf{(B-1)} ($1 + m_1 + m_2 \le 0$) or ($1 + m_1 + m_2 > 0$ and $1 + 2m_1 + m_2 < 0$). Then
$$\delta_K(n) = Q(n,n,0)=\left( \frac{1}{2} + 2 m_2 \right) n^2 + \left( \frac{3}{2} + m_1 + 4 m_2 \right) n.$$
Hence $$
d_+[J_K(n)] = \left( \frac{1}{2} + 2 m_2 \right) n^2 + (1 + m_1) n - \left( \frac{3}{2} + m_1 + 2 m_2 \right).
$$

\textbf{(B-2)} $1 + m_1 + m_2 > 0$ and $1 + 2m_1 + m_2 \ge 0$. Recall that $$c_2=\frac{1 - m_1 - m_2 + (1 + m_2) n}{2 (1 + m_1 + m_2)}$$
and $k_1$ is one of the integers closest to $c_2$. We have 
\begin{eqnarray*}
\delta_K(n) = Q(n,k_1,k_1-n)
&=& (-1-m_1-m_2) k_1^2 + ( 1 - m_1 - m_2 + (1 + m_2) n) k_1 \\
&& + \, 2 m_1 n + 5 m_2 n  + m_1 n^2 + 2 m_2 n^2 + \frac{n}{2} + \frac{n^2}{2}.
\end{eqnarray*}
Write $k_1 = c_2 + r_n$ where $r_n$ is a periodic sequence with $|r_n| \le 1/2$.  As in Case A we have 
$$\delta_K(n) = Q(n,c_2,c_2-n) + (-1-m_1-m_2)r_n^2$$
and
\begin{eqnarray*}
Q(n,c_2,c_2-n) &=&  2 m_1 n + 5 m_2 n  + m_1 n^2 + 2 m_2 n^2 + \frac{n}{2} + \frac{n^2}{2} - \frac{( 1 - m_1 - m_2 + (1 + m_2) n)^2}{4(-1-m_1-m_2)} \\
&=& \left( \frac{3}{4} + \frac{3m_1}{4} + \frac{9m_2}{4} +  \frac{m_1^2}{4(1 + m_1 + m_2)} \right) n^2  \\
&& + \,  \left( 1 + 2m_1 + \frac{9m_2}{2}  - \frac{m_1}{1 + m_1 + m_2} \right) n - \frac{( 1 - m_1 - m_2)^2}{4(-1-m_1-m_2)}.
\end{eqnarray*} 
Hence 
\begin{eqnarray*}
d_+[J_K(n)] &=& \left( \frac{3}{4} + \frac{3m_1}{4} + \frac{9m_2}{4} +  \frac{m_1^2}{4(1 + m_1 + m_2)} \right) n^2 + \frac{m_1(m_2-1)}{2(1+m_1+m_2)} n\\
&& - \,  \left( \frac{3}{4} + \frac{3m_1}{4} + \frac{9m_2}{4} - \frac{(m_2 - 1)^2}{4(1 + m_1 + m_2)}\right) + (-1-m_1-m_2)r_n^2.
\end{eqnarray*}

\textbf{Case C.} $m_2 \le -2$. There are 2 subcases.

\textbf{(C-1)} $m_1 \le -3m_2/2$. Then 
$$\delta_K(n) = Q(n,n,n)=(2 + m_1 + 3 m_2) n.$$
Hence $$d_+[J_K(n)] = (5/2 + m_1 + 3 m_2) (n-1).$$ 

\textbf{(C-2)} $m_1 > -3m_2/2$. Recall that $$c_3=\frac{-3/2 + m_1 + m_2 + (1+m_2 ) n}{1-2m_1-2m_2}$$
and let $k_1$ be one of the integers closest to $c_3$. We have
$$\delta_K(n) = \begin{cases} Q(n,k_1,k_1) &\mbox{if } c_3 \notin \frac{1}{2} + \BZ \\ 
Q(n,k_1,k_1)-(c_3 + 1/2) & \mbox{if } c_3 \in \frac{1}{2} + \BZ \end{cases}$$
and
\begin{eqnarray*}
Q(n,k_1,k_1)
&=& \left( 1/2-m_1-m_2 \right) k_1^2 - \left( -3/2 + m_1 + m_2 + (1+m_2 ) n \right) k_1 \\
&& + \, 2 m_1 n + 4 m_2 n  + m_1 n^2 + 2 m_2 n^2 + \frac{n}{2} + \frac{n^2}{2}.
\end{eqnarray*}

Write $k_1 = c_3 + r_n$ where $r_n$ is a periodic sequence with $|r_n| \le 1/2$. As in Case A we have 
$$Q(n,k_1,k_1) = Q(n,c_3,c_3) + \left( 1/2-m_1-m_2 \right) r_n^2$$
and
\begin{eqnarray*}
Q(n,c_3,c_3) &=&  2 m_1 n + 4 m_2 n  + m_1 n^2 + 2 m_2 n^2 + \frac{n}{2} + \frac{n^2}{2} - \frac{\left( -3/2 + m_1 + m_2 + (1+m_2 ) n \right)^2}{4(1/2-m_1-m_2)} \\
&=& \frac {(2 m_1 + 3 m_2)^2} {2 (-1 + 2 m_1 + 2 m_2)} n^2 + \left( \frac{1}{2} + 2 m_1 + \frac{9m_2}{2} + \frac {-3 + 2 m_1} {2 (-1 + 2 m_1 + 2 m_2)} \right) n\\
&& - \, \frac{\left( -3/2 + m_1 + m_2  \right)^2}{4(1/2-m_1-m_2)} .
\end{eqnarray*} 
Hence 
\begin{eqnarray*}
d_+[J_K(n)] &=& \frac {(2 m_1 + 3 m_2)^2} {2 (-1 + 2 m_1 + 2 m_2)} n^2 + 
\begin{cases} \frac {(-5 + 2m_1)(1 + m_2)} {2 (-1 + 2 m_1 + 2 m_2)} n &\mbox{if } \frac {-1+(1 + m_2)(n-1)} {-1 + 2 m_1 + 2 m_2}  \notin \BZ \medskip \\ 
\frac {(-3 + 2 m_1)(1 + m_2)} {2(-1 + 2 m_1 + 2 m_2)}n & \mbox{if } \frac {-1+(1 + m_2)(n-1)} {-1 + 2 m_1 + 2 m_2}  \in  \BZ \end{cases} \\
&& - \, \left( \frac{1}{2} + m_1 + 2m_2 - \frac{\left( 2m_1 -5  \right)^2}{8(2m_1 + 2m_2 -1)} \right) + \left( 1/2-m_1-m_2 \right) r_{n-1}^2.
\end{eqnarray*}
This completes the proof of Theorem \ref{prop:b}.
\end{proof}


The proof of Theorem \ref{prop:b} implies the following.

\begin{lemma} \label{M}
For the 2-fusion knot $K=K(m_1, m_2)$ we have
$$
M_1 = \begin{cases}  0  & \mbox{if } (m_1, m_2) \notin I_6, 
\\ \frac {1 + m_2} {-1 + 2 m_1 + 2 m_2} & \mbox{if } (m_1, m_2) \in I_6,
\end{cases}
$$
and 
$$
\max\{0, M_2\} = \begin{cases} \frac{(1 - m_1 + m_2)^2}{4(m_1 + m_2 -1)} &\mbox{if } (m_1, m_2) \in I_1, 
\smallskip\\
3m_2/4 &\mbox{if } (m_1, m_2) \in I_2, 
\smallskip
\\ 0  & \mbox{if } (m_1, m_2) \in I_3, 
\smallskip
\\ \max \big\{  \frac{m_1 + m_2 -1}{4} + \frac{m_1 (m_2 - 1)}{m_1 + m_2 + 1}, 0 \big\}   & \mbox{if } (m_1, m_2) \in I_4, 
\smallskip
\\ 0  & \mbox{if } (m_1, m_2) \in I_5, 
\smallskip
\\ \max \big\{ \frac{2m_1 + 2m_2 -1}{8} + \frac{(2m_1-6) (m_2+1)}{2m_1 + 2m_2 - 1}, 0 \big\} & \mbox{if } (m_1, m_2) \in I_6.
\end{cases}
$$
\end{lemma}
 

\subsection{Proof of Theorem \ref{thm:slope-cable}} 
Theorem \ref{prop:b} implies that Conjecture \ref{conj} holds true for 2-fusion knots: The fact that $b_K(n)\leq 0$ is clear by the statement
of Theorem \ref{prop:b}.  This, together with Theorem \ref{a_K}, proves Theorem \ref{thm:slope-cable} part $(1)$.
Moreover, $b_K(n) = 0$ if and only if $m_1 \in \{0,1\}$ and $m_2 \ge 1$, or $(m_1, m_2) = (-1,1)$.
As noted in \cite{GV}  we have
$K(1, m_2)= K^*(0, -m_2-1)$. On the other hand, by definition 
the knot $K(0, m_2)$ is a torus  knot. Finally  $K(-1, 1)$ is the torus knot $T(2,5)$.
Thus if $b_K(n)=0$, and $K=K(m_1, m_2)$, then $K$ is a torus knot.
By combining Theorem \ref{thm-quasi-constant}, Theorem \ref{a_K} and Lemma \ref{M} we get Theorem \ref{thm:slope-cable} part $(2)$.\qed
 
\begin{example} 
Consider the 2-fusion knot $K(m, 1)$, also known as the $(-2,3,2m+3)$-pretzel knot. It is known that $K(m,1)$ is $B$--adequate if $m \le -2$ and is $A$--adequate if $m \ge -1$. Moreover $K(m,1)$ is a torus knot if $|m| \le 1$, and $K(-2,1)$ is the twist knot $5_2$ which is an adequate knot. Hence we consider the two cases $m \ge 2$ and $m \le -3$ only. 

Note that $K(m_1,m_2)$ is the mirror image of $K(1-m_1, -1-m_2)$. In particular, $K(m,1)$ is the mirror image of $K(1-m, -2)$.

\textit{Case 1:} $m \ge 2$. From the proof of Theorem \ref{prop:b} we have
$$
d_+[J_{K(m, 1)}(n)] = \left( \frac{5}{2} + m + \frac{1}{4m} \right) n^2 + \left( \frac{1}{2m} - \frac{1}{2} \right) n - \left( 3 + \frac{3m}{4} - \frac{1}{4m} \right) - m r^2_{n-1}
$$
where $r_n$ is a periodic sequence with $|r_n| \le 1/2$.

Hence, by Corollary \ref{cables}, the $(p,q)$-cable of $K(m,1)$ satisfies Conjectures \ref{conj} and \ref{slope} if $$p-\left( 10 + 4m + \frac{1}{m} \right)q <0 \quad \text{or} \quad p-\left( 10+ 4m + \frac{1}{m} \right)q > \frac{m}{4} + \frac{1}{m} - 1.$$

\textit{Case 2:} $m \le -3$. From the proof of Theorem \ref{prop:b} we have
$$d_+[J_{K(1-m, -2)}(n)] = -\frac {2(m+2)^2} {2m+3} \, n^2 + b(n) n + (6m+17)/8 + (m + 3/2) r^2_{n-1}$$
where $r_n$ is a periodic sequence with $|r_n| \le 1/2$, and $b(n) = \begin{cases} -\frac{1}{2}   &\mbox{if } (2m+3) \nmid n, \medskip \\ 
-\frac {2m+1} {2( 2m+3)} & \mbox{if } (2m+3) \mid n. \end{cases}$

\smallskip

Hence, by Corollary \ref{cables}, the $(p,q)$-cable of $K(1-m, -2) = (K(m,1))^*$ satisfies Conjectures \ref{conj} and \ref{slope} if $$p + \left( 10 + 4m + \frac{1}{2m + 3} \right)q < 0 \quad \text{or} \quad p + \left( 10+ 4m + \frac{3}{2m+3} \right)q > - \left( \frac{m}{4} + \frac{1}{2m+3}+ \frac{11}{8} \right).$$
\end{example}



 

\no{ Similarly, let $K$ be a knot such that for $n \gg 0$ we have
$$
d_-[J_K(n)]=a^*n^2+b^*(n)n+d^*(n)
$$
where $a^*$ is a constant, $b^*(n)$ and $d^*(n)$ are periodic functions, and $b^*(n) \ge 0$. Let
\begin{eqnarray*}
M^*_1 &=&  \max\{|b^*(i)-b^*(j)|\},\\
M^*_2 &=& \max\{-2b^*(i) + |b^*(i) - b^*(j)| +|d^*(i)-d^*(j)|\}.
\end{eqnarray*}

Suppose $p - (4a^* + M^*_1)q > 0$, or $p - (4a^* - M^*_1)q < - M^*_2$ and $p - 4a^*q <0$. Then for $n \gg 0$ we have
$$d_-[J_{\K}(n)]=A^*n^2+B^*(n)n+D^*(n)$$
where $A^*$ is a constant, and $B^*(n), D^*(n)$ are periodic functions, and $B^*(n) \ge 0$. Moreover, if $js^*_K \subset bs_K$ then $js^*_{\K} \subset bs_{\K}$.
}
 

\bibliographystyle{hamsplain}
