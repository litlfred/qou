---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-012-4-cabling-knots-with-constant-an
section_title: "Cabling knots with constant a(n)"
section_number: 4
pages: 18-22
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.979
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
\label{constant a(n)}

In Section 3 we studied the behavior of $d_+[J_K(n)]$ under knot cabling for knots of period at most two. In this section we study knots with period greater than two under the additional hypothesis
that, for $n \gg 0$ we have $a(n)=a$, where $a$ is a constant.
In this case, by abusing the terminology, we will say that $a(n)$ is constant. The main result in this section is the following.

 \begin{theorem}
 \label{thm-quasi-constant}
 Let $K$ be a knot such that for $n \gg 0$ we have
$$
d_+[J_K(n)]=an^2+b(n)n+d(n)
$$
where $a$ is a constant, $b(n)$ and $d(n)$ are periodic functions with $b(n) \le 0$. Let \begin{eqnarray*}
M_1 &=&  \max\{|b(i)-b(j)| \, : \,  i \equiv j \pmod{2}\},\\
M_2 &=& \max\{2b(i) + |b(i)-b(j)| + |d(i)-d(j)| \, : \, i \equiv j \pmod{2}\}.
\end{eqnarray*}

Suppose $p- (4a-M_1)q < 0$ or $p- (4a + M_1)q > \max\{0,M_2\}$. Then for $n \gg 0$ we have
$$d_+[J_{\K}(n)]=An^2+B(n)n+D(n)$$
where $A$ is a constant, and $B(n), D(n)$ are periodic functions with $B(n) \le 0$. Moreover, if $js_K \subset bs_K$ then $js_{\K} \subset bs_{\K}$.
 \end{theorem}
 
 As a corollary of Theorem \ref{thm-quasi-constant} and Theorem \ref{main:bs}  we obtain the following result which implies, in particular, that for knots with constant $a(n)$ the Slope Conjecture 
 is closed under cabling for infinitely many pairs $(p, q)$.
 \begin{corollary} \label{cables-a}
 Let $K$ be a knot such that for $n \gg 0$ we have
$$
d_+[J_K(n)]=an^2+b(n)n+d(n)
$$
where $a$ is a constant, $b(n)$ and $d(n)$ are periodic functions with $b(n) \le 0$. Let $M_1, M_2$
be as in the statement of Theorem \ref{thm-quasi-constant}.
If $K$ satisfies the Slope Conjecture,  then
$\K$ satisfies the conjecture  provided that  $p- (4a-M_1)q < 0$ or $p- (4a + M_1)q > \max\{0,M_2\}$. 
 \end{corollary}
\smallskip
 
 \begin{example}  

\label{3-knots} As an illustration we apply 
 Theorem \ref{thm-quasi-constant} and Corollary \ref{cables-a}  to the knots  $8_{20}, 9_{43}, 9_{44}$.  By  \cite[Section 4]{Ga-slope},
 these are the only  knots, with at most nine crossings, that have Jones period larger than 2. Indeed,
 the period of these knots is  $3$. Another application of Theorem \ref{thm-quasi-constant} will be illustrated in Example \ref{example-pretzel}.
 
 For $K=8_{20}$ we have
 \begin{eqnarray*}
d_+[J_K(n)] &=& \begin{cases} 2n^2/3 - n/2 - 1/6 &\mbox{if } n \not\equiv 0 \pmod{3}\\ 
2n^2/3 - 5n/6 -1/2 & \mbox{if } n \equiv 0 \pmod{3}.\end{cases} 
\end{eqnarray*}
Hence $K_{p,q}$ satisfies the Slope Conjecture if $p-\frac{7}{3}q<0$ or $p-3q > 0$.

For $K=9_{43}$ we have
 \begin{eqnarray*}
d_+[J_K(n)] &=& \begin{cases} 8n^2/3 - n/2 - 13/6 &\mbox{if } n \not\equiv 0 \pmod{3}\\ 
8n^2/3 - 5n/6 -7/2 & \mbox{if } n \equiv 0 \pmod{3}.\end{cases}
\end{eqnarray*}
Hence $K_{p,q}$ satisfies the Slope Conjecture if $p-\frac{31}{3}q<0$ or $p - 11q>\frac{2}{3}$.


For $K=9_{44}$ we have
\begin{eqnarray*}
d_+[J_K(n)] &=& \begin{cases} 7n^2/6 - n - 1/6 &\mbox{if } n \not\equiv 0 \pmod{3}\\ 
7n^2/6 - 4n/3 -1/2 & \mbox{if } n \equiv 0 \pmod{3}.\end{cases}
\end{eqnarray*}
Hence $K_{p,q}$ satisfies the Slope Conjecture if $p-\frac{13}{3}q<0$ or $p - 5q > 0 $.
\end{example}

Theorem \ref{thm-quasi-constant} follows from Theorem \ref{bdry slope} and the following proposition.

\begin{proposition}
\label{quasi-constant}
Let $K$ be a knot such that for $n \gg 0$ we have
$$
d_+[J_K(n)]=an^2+b(n)n+d(n)
$$
where $a$ is a constant, $b(n)$ and $d(n)$ are periodic functions with $b(n) \le 0$. Let
\begin{eqnarray*}
M_1 &=&  \max\{|b(i)-b(j)| : i  \equiv j \pmod{2} \},\\
M_2 &=& \max\{2b(i) + |b(i)-b(j)| + |d(i)-d(j)| : i \equiv j \pmod{2}\}.
\end{eqnarray*}

Suppose $p- (4a-M_1)q < 0$ or $p- (4a + M_1)q > \max\{0,M_2\}$. Then for $n \gg 0$ we have
$$d_+[J_{\K}(n)]=An^2+B(n)n+D(n)$$
where $A$ is a constant with $A \in \{q^2a, pq/4\}$, and $B(n), D(n)$ are periodic functions with $B(n) \le 0$.
\end{proposition}

\begin{proof} Fix $n \gg 0$. Recall the cabling formula \eqref{cables} of the colored Jones polynomial
$$J_{K_{p,q}}(n)= v^{pq(n^2-1)/4} \sum_{k \in \CS_n} v^{-pk(qk+1)} J_K(2qk+1).$$
In the above formula, there is a sum. As in the proof of Proposition \ref{quasi} we will show that, under the assumption of the proposition, there is a unique term of the sum whose highest degree is strictly greater than those of the other terms. This implies that the highest degree of the sum is exactly equal to the highest degree of that unique term. 

For $k \in \CS_n$ let $$f(k) := d_+ [v^{-pk(qk+1)} J_K(2qk+1)] = -pk(qk+1)+d_+[J_K(|2qk+1|)].$$
The goal is to show that $f(k)$ attains its maximum on $\CS_n$ at a unique $k$. 

Since $d_+[J_K(n)]$ is a quadratic quasi-polynomial, $f(k)$ is a piece-wise quadratic polynomial. The above goal will be achieved in 2 steps. In the first step we show that $f(k)$ attains its maximum on each piece at a unique $k$. Then in the second step we show that the maximums of $f(k)$ on all the pieces are distinct.
\smallskip

\textbf{Step 1.} Let $\pi$ be the period of $d_+[J_K(n)]$. For $\ve \in \{\pm 1\}$ and $0 \le i < \pi$, let $h_i^{\ve}(x)$ be the quadratic real polynomial defined by
$$
h_i^{\ve}(x) := ( -pq + 4q^2 a ) x^2 + ( -p + 4q a + 2q b(i) \ve ) x +  a + b(i) \ve + d(i).
$$
For each $k \in \CS_n$, we have $f(k)= h^{\ve_k}_{i_k}(k)$
for a unique pair $(\ve_k, i_{k})$. Let
$$I_n := \{ (\ve_k,i_{k}) \mid k \in \CS_n\}.$$
Then $f(k)$ is a piece-wise quadratic polynomial of exactly $|I_n|$ pieces, each of which is associated with a unique pair $(\ve, i)$ in $I_n$.

For each $(\ve,i) \in I_n$, let $$\CS_{n,\ve,i} := \{ k \in \CS_n \mid (\ve_k, i_k) = (\ve,i)\}$$
which is the set of all $k$ on the piece associated with $(\ve,i)$. 

The quadratic polynomial $h_i^{\ve}(x)$ is concave up if $p-4qa<0$, and concave down if $p-4qa>0$.  Hence, for $n \gg 0$, $h_i^{\ve}(k)$ is maximized on the set $\CS_{n,\ve,i}$ at a unique $k=k_{n,\ve,i}$, where
$$ k_{n,\ve,i} := \begin{cases} \max \CS_{n,\ve,i} &\mbox{if } (p - 4qa)\ve < 0, \\
\min \CS_{n,\ve,i} &\mbox{if } (p - 4qa)\ve > 0.  \end{cases}$$
Note that, as in the proof of Proposition \ref{quasi}, we use the assumption that $b(i) \le 0$ when $(p - 4qa)\ve > 0$. Moreover we have 
$$ \begin{cases}  |k_{n,\ve,i}|  \to \infty \mbox{ as }  n \to \infty, &\mbox{if } p - 4qa < 0 \\
 |k_{n,\ve,i}|  \le \pi, &\mbox{if } p - 4qa > 0.  \end{cases}$$
\smallskip

\textbf{Step 2.} Let 
$$\text{Max}_n := \max \{f(k) \mid k \in \CS_n\}.$$
From step 1 we have $\text{Max}_n =  \max \{ h_{i}^{\ve}(k_{n, \ve, i}) \mid (\ve, i) \in I_n \}.$ We claim that $$h_{i_1}^{\ve_1}(k_{n,\ve_1,i_1}) \not= h_{i_2}^{\ve_2}(k_{n,\ve_2,i_2})$$
for $(\ve_1,i_1) \not= (\ve_2,i_2)$. 

Indeed, let $k_1:=k_{n,\ve_1,i_1}$ and $k_2:=k_{n,\ve_2,i_2}$. Note that $k_1 \not= k_2$. Moreover, $k_1$ and $k_2$ are both in  $\BZ$ or $\frac{1}{2} + \BZ$. As a result we have $k_1 \pm  k_2 \in \BZ$, and $i_1 - i_2 \equiv 2q (k_1 - k_2) \equiv 0 \pmod{2}$. Let
$$\sigma := h_{i_1}^{\ve_1}(k_1) - h_{i_2}^{\ve_2}(k_2).$$

Without loss of generality, we can assume that $|k_1| \ge |k_2|$. Then we write $\sigma = \sigma' + d(i_1) - d(i_2)$ where
$$
\sigma' := \begin{cases} (k_1 - k_2) \Big( (-p+4qa) \big( q(k_1+k_2)+1 \big) + 2qb(i_1)\ve_1 \Big) \\ \qquad \qquad \qquad + \, \big( b(i_1) - b(i_2) \big) \ve_1 (2qk_2 + 1) &\mbox{if } \ve_1 = \ve_2, \\
\Big( (-p+4qa)(k_1 - k_2) + 2b(i_1)\ve_1 \Big) \big( q(k_1+k_2)+1 \big) 
\\ \qquad \qquad \qquad - \, \big( b(i_1) - b(i_2) \big) \ve_1 (2qk_2 + 1) &\mbox{if } \ve_1 \not= \ve_2.  \end{cases}
$$
We consider the following 2 cases.
\medskip

\textit{Case 1:} Suppose that $p - (4a - M_1)q <0 $. In particular, we have $p - 4qa <0$. There are 2 subcases.
\smallskip

\underline{Subcase 1.1:} We have $\ve_1 = \ve_2$. Since $k_1$ and $k_2$ have the same sign, we have 
$$|q(k_1+k_2)+1| - |2qk_2+1| = 2q (|k_1| - |k_2|) \ge 0.$$
Hence
\begin{eqnarray*}
|\sigma'| &\ge& \big| (-p+4qa) \big( q(k_1+k_2)+1 \big) + 2qb(i_1)\ve_1 \big| - \big| \big( b(i_1) - b(i_2) \big) \big( q(k_1+k_2)+1 \big) \big| \\
&\ge& \big( -p + 4qa - |b(i_1) - b(i_2)| \big) |q(k_1+k_2)+1| + 2q b(i_1).
\end{eqnarray*}
Since $|q(k_1+k_2)+1| \to \infty$ as $n \to \infty$, and $$-p + 4qa - |b(i_1) - b(i_2)| \ge -p + 4qa - M_1 >0$$ 
we get $|\sigma'| \to \infty$ as $n \to \infty.$

\smallskip

\underline{Subcase 1.2: } We have $\ve_1 \not= \ve_2$. Since $k_1$ and $k_2$ have opposite signs, we have 
$$(q|k_1-k_2| + 1) - |2qk_2+1| \ge 2q (|k_1| - |k_2|)  \ge 0.$$
Hence
\begin{eqnarray*}
|\sigma'| &\ge& \big|  (-p+4qa)(k_1 - k_2) + 2b(i_1)\ve_1 \big| -  | b(i_1) - b(i_2)| \, ( q|k_1 - k_2| + 1) \\
&\ge& \big( -p + 4qa - q |b(i_1) - b(i_2)| \big) |k_1 - k_2| -  | b(i_1) - b(i_2)|  + 2 b(i_1).
\end{eqnarray*}
Since $|k_1 - k_2| \to \infty$ as $n \to \infty$, and $$-p + 4qa - q |b(i_1) - b(i_2)| \ge -p + 4q a  - q M_1 >0,$$ we get $|\sigma'| \to \infty$ as $n \to \infty.$

\medskip 

\textit{Case 2:} Suppose that $p- (4a + M_1)q > \max\{0, M_2\}$. There are 2 subcases.
\smallskip

\underline{Subcase 2.1:} We have $\ve_1 = \ve_2$. Note that $q(k_1+k_2)+1$ and $\ve_1$ have the same sign. Moreover, both $-p+4qa$ and $2qb(i_1)$ are non-positive. As in subcase 1.1 we have 
\begin{eqnarray*}
|\sigma'| &\ge& \big| (-p+4qa) \big( q(k_1+k_2)+1 \big) + 2qb(i_1)\ve_1 \big| - \big| \big( b(i_1) - b(i_2) \big) \big( q(k_1+k_2)+1 \big) \big| \\
&=& \big( p - 4qa - |b(i_1) - b(i_2)| \big) \, |q(k_1+k_2)+1| - 2q b(i_1).
\end{eqnarray*}
Since $p - 4qa - |b(i_1) - b(i_2)|  \ge p - 4qa - M_1 > \max \{0, M_2\}$, we get 
$$|\sigma'| > M_2  -2 q b(i_1) \ge |d(i_1) - d(i_2)|.$$
\smallskip

\underline{Subcase 2.2:} We have $\ve_1 \not= \ve_2$. Note that $k_1 - k_2$ and $\ve_1$ have the same sign. Moreover, both $-p+4qa$ and $2qb(i_1)$ are non-positive. As in subcase 1.2 we have
\begin{eqnarray*}
|\sigma'| &\ge& \big|  (-p+4qa)(k_1 - k_2) + 2b(i_1)\ve_1 \big| -  | b(i_1) - b(i_2)| \, ( q|k_1 - k_2| + 1) \\
&=& \big( p - 4qa - q |b(i_1) - b(i_2)| \big) |k_1 - k_2| - | b(i_1) - b(i_2)|  - 2 b(i_1).
\end{eqnarray*}
Since $p - 4qa - q |b(i_1) - b(i_2)| \ge p - 4qa - q M_1 > \max\{0, M_2\}$, we get $$|\sigma'| > M_2 -  | b(i_1) - b(i_2)|  -2 b(i_1) \ge |d(i_1) - d(i_2)|.$$

In all cases, for $n \gg 0$ we have $|\sigma'| > |d(i_1)-d(i_2)|.$ Hence $$\sigma = \sigma' + d(i_1) - d(i_2) \not= 0.$$
We have proved that $f(k)$ attains its maximum on $\CS_n$ at a unique $k$. More precisely, there exists a unique $(\ve_n, i_n) \in I_n$ such that $h_{i_n}^{\ve}(k_{n, \ve_n, i_n}) = \text{Max}_n$. 

Equation \eqref{cables} then implies that  
\begin{eqnarray*}
d_+[J_{K_{p,q}}(n)] &=& pq(n^2-1)/4 + h^{\ve_n}_{i}(k_{n,\ve_n,i_n}).
\end{eqnarray*}

If $p - 4qa < 0$ then $k_{n,\ve_n,i_n} = \ve_n (n/2 + s_n)$, where $s_n$ is a periodic sequence and $s_n \le -1/2$. We have
\begin{eqnarray*}
d_+[J_{K_{p,q}}(n)] &=& q^2a n^2 + \big( (-p + 4qa) (q s_n + \ve_n /2) + qb(i_n) \big) n -  pq/4 \\
&& + \, (-p + 4qa)s_n (q s_n + \ve_n) + 2q b(i_n) s_n+  a + b(i_n) \ve_n + d(i_n).
\end{eqnarray*}
In this case we have $$B(n)=(-p + 4qa) (q s_n + \ve_n /2) + qb(i_n) < 0,$$ since $q s_n + \ve_n /2 \le -q/2 + 1/2 <0$ and $b(i_n) \le 0$.

If $p - 4qa > 0$ then $k_{n,\ve_n,i_n} = s_n$, where $s_n$ is a periodic function. We have
\begin{eqnarray*}
d_+[J_{K_{p,q}}(n)] &=& pq (n^2-1)/4 
+ (-p + 4qa)s_n (q s_n + 1) + 2q b(i_n) \ve_n s_n\\
&& + \,  a + b(i_n) \ve_n + d(i_n).
\end{eqnarray*}
In this case we have $B(n)=0$.

This completes the proof of Proposition \ref{quasi-constant}.
\end{proof}
