---
doc_id: arxiv-1501.04614v1
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES"
section_id: sec-001-2-jones-slopes-of-cable-knots
section_title: "Jones slopes of cable knots"
section_number: 2
pages: 3-7
source_pdf: 1501.04614v1.pdf
source_sha256: ebebcae0c1823217
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.985
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES — We continue our study of the degree of the colored Jones polynomial under knot cabling started in [8]."
---
Let $K_{p,q}$ be the $(p,q)$-cable of a knot $K$, where $q > 1$. For $n>0$, let $\CS_n$ be the set of all $k$ such that 
 $$
 |k| \le (n-1)/2 \quad \text{and} \quad k \in \begin{cases} \BZ &\mbox{if } n \text{ is odd}, \\ 
 \BZ+\frac{1}{2} & \mbox{if } n \text{ is even}. \end{cases}
 $$
By \cite{Ve}, for $n>0$ we have
\begin{equation}
\label{cables11}
J_{K_{p,q}}(n)= v^{pq(n^2-1)/4} \sum_{k \in \CS_n} v^{-pk(qk+1)} J_K(2qk+1),
\end{equation} 
where it is understood that $J_K(-m)=-J_K(m)$.

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

\begin{proof} Fix $n \gg 0$. Recall the cabling formula \eqref{cables11} of the colored Jones polynomial
$$J_{K_{p,q}}(n)= v^{pq(n^2-1)/4} \sum_{k \in \CS_n} v^{-pk(qk+1)} J_K(2qk+1).$$
In the above formula, there is a sum. Under the assumption of the proposition, we will show that there is a unique term of the sum whose highest degree is strictly greater than those of the other terms. This implies that the highest degree of the sum is exactly equal to the highest degree of that unique term. 

For $k \in \CS_n$ let $$f(k) := d_+ [v^{-pk(qk+1)} J_K(2qk+1)] = -pk(qk+1)+d_+[J_K(|2qk+1|)].$$
The goal is to show that $f(k)$ attains its maximum on $\CS_n$ at a unique $k$. 

Since $d_+[J_K(n)]$ is a quadratic quasi-polynomial, $f(k)$ is a piece-wise quadratic polynomial. The above goal will be achieved in 2 steps. In the first step we show that $f(k)$ attains its maximum on each piece at a unique $k$. Then in the second step we show that the maximums of $f(k)$ on all the pieces are distinct.

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
Note that, as in the proof of \cite[Proposition 3.2]{Effie-Anh-slope}, we use the assumption that $b(i) \le 0$ when $(p - 4qa)\ve > 0$. Moreover we have 
$$ \begin{cases}  |k_{n,\ve,i}|  \to \infty \mbox{ as }  n \to \infty, &\mbox{if } p - 4qa < 0 \\
 |k_{n,\ve,i}|  \le \pi, &\mbox{if } p - 4qa > 0.  \end{cases}$$

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

\smallskip

\textit{Case 1:} $p - (4a - M_1)q <0 $. In particular, we have $p - 4qa <0$. There are 2 subcases.

\underline{Subcase 1.1:} $\ve_1 = \ve_2$. Since $k_1$ and $k_2$ have the same sign, we have 
$$|q(k_1+k_2)+1| - |2qk_2+1| = 2q (|k_1| - |k_2|) \ge 0.$$
Hence
\begin{eqnarray*}
|\sigma'| &\ge& \big| (-p+4qa) \big( q(k_1+k_2)+1 \big) + 2qb(i_1)\ve_1 \big| - \big| \big( b(i_1) - b(i_2) \big) \big( q(k_1+k_2)+1 \big) \big| \\
&\ge& \big( -p + 4qa - |b(i_1) - b(i_2)| \big) |q(k_1+k_2)+1| + 2q b(i_1).
\end{eqnarray*}
Since $|q(k_1+k_2)+1| \to \infty$ as $n \to \infty$, and $$-p + 4qa - |b(i_1) - b(i_2)| \ge -p + 4qa - M_1 >0$$ 
we get $|\sigma'| \to \infty$ as $n \to \infty.$

\smallskip

\underline{Subcase 1.2:} $\ve_1 \not= \ve_2$. Since $k_1$ and $k_2$ have opposite signs, we have 
$$(q|k_1-k_2| + 1) - |2qk_2+1| \ge 2q (|k_1| - |k_2|)  \ge 0.$$
Hence
\begin{eqnarray*}
|\sigma'| &\ge& \big|  (-p+4qa)(k_1 - k_2) + 2b(i_1)\ve_1 \big| -  | b(i_1) - b(i_2)| \, ( q|k_1 - k_2| + 1) \\
&\ge& \big( -p + 4qa - q |b(i_1) - b(i_2)| \big) |k_1 - k_2| -  | b(i_1) - b(i_2)|  + 2 b(i_1).
\end{eqnarray*}
Since $|k_1 - k_2| \to \infty$ as $n \to \infty$, and $$-p + 4qa - q |b(i_1) - b(i_2)| \ge -p + 4q a  - q M_1 >0,$$ we get $|\sigma'| \to \infty$ as $n \to \infty.$

\medskip 

\textit{Case 2:} $p- (4a + M_1)q > \max\{0, M_2\}$. There are 2 subcases.

\underline{Subcase 2.1:} $\ve_1 = \ve_2$. Note that $q(k_1+k_2)+1$ and $\ve_1$ have the same sign. Moreover, both $-p+4qa$ and $2qb(i_1)$ are non-positive. As in subcase 1.1 we have 
\begin{eqnarray*}
|\sigma'| &\ge& \big| (-p+4qa) \big( q(k_1+k_2)+1 \big) + 2qb(i_1)\ve_1 \big| - \big| \big( b(i_1) - b(i_2) \big) \big( q(k_1+k_2)+1 \big) \big| \\
&=& \big( p - 4qa - |b(i_1) - b(i_2)| \big) \, |q(k_1+k_2)+1| - 2q b(i_1).
\end{eqnarray*}
Since $p - 4qa - |b(i_1) - b(i_2)|  \ge p - 4qa - M_1 > \max \{0, M_2\}$, we get 
$$|\sigma'| > M_2  -2 q b(i_1) \ge |d(i_1) - d(i_2)|.$$

\underline{Subcase 2.2:} $\ve_1 \not= \ve_2$. Note that $k_1 - k_2$ and $\ve_1$ have the same sign. Moreover, both $-p+4qa$ and $2qb(i_1)$ are non-positive. As in subcase 1.2 we have
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

\begin{remark} The proof of Proposition \ref{quasi-constant} can be slightly modified to give the following.

Let $K$ be a knot such that for $n \gg 0$ we have
$$
d_+[J_K(n)]=a(n)n^2+b(n)n+d(n)
$$
where $a(n)$, $b(n)$ and $d(n)$ are periodic functions with $b(n) \le 0$. Let
$$a_M = \max\{a(n)\}, \quad a_m = \min\{a(n)\} $$
and
\begin{eqnarray*}
M_1 &=&  \max\{|b(i)-b(j)| : i  \equiv j \pmod{2} \},\\
M_2 &=& \max\{2b(i) + |b(i) - b(j)| +|d(i)-d(j)| : i \equiv j \pmod{2}\}.
\end{eqnarray*}

(1) Suppose $p- (4 a_m -M_1)q < 0$. Then for $n \gg 0$ we have
$$d_+[J_{\K}(n)]=A(n)n^2+B(n)n+D(n)$$
where $A(n)$, $B(n)$ and $D(n)$ are periodic functions with $\{A(n)\} \subset \{q^2 a(n)\}$ and $B(n) < 0$.

(2) Suppose $\{a(n)\}$ has period at most $2$ and  $p- (4a_M + M_1)q > \max\{0,M_2\}$. Then for $n \gg 0$ we have
$$d_+[J_{\K}(n)]=pqn^2/4+O(1).$$
\end{remark}

We now recall the following result about the behavior of the boundary slopes under knot cabling in \cite{Effie-Anh-slope}.

\begin{theorem} \cite{Effie-Anh-slope}
\label{bdry slope}
 For every knot $K \subset S^3$ and  $(p, q)$ coprime  integers
we have 
 $$\left( q^2 bs_K \cup \{pq\} \right) \subset bs_{K_{p,q}}.$$
\end{theorem}

\no{
Here we study knots for which $d_+[J_K(n)]$ has a unique  Jones slope. We have provided conditions under which
if a number $a\in \QQ$ is a Jones slope of a mono-sloped knot $K$ then $q^2a$ is a Jones slopes of the cable knot $\K$.}

Proposition \ref{quasi-constant} and Theorem \ref{bdry slope} imply Theorem \ref{thm-quasi-constant} stated in the introduction.

\begin{example}  

\label{3-knots}

 Theorem \ref{thm-quasi-constant} applies to the non-alternating knots $8_{20}, 9_{43}, 9_{44}$ (of period $3$) in Section 4 of \cite{Ga-slope}. 
 
 For $K=8_{20}$ we have
 \begin{eqnarray*}
d_+[J_K(n)] &=& \begin{cases} 2n^2/3 - n/2 - 1/6 &\mbox{if } n \not\equiv 0 \pmod{3}\\ 
2n^2/3 - 5n/6 -1/2 & \mbox{if } n \equiv 0 \pmod{3}.\end{cases} 

\end{eqnarray*}
Hence $K_{p,q}$ satisfies Conjectures \ref{conj}  and  \ref{slope} if $p-\frac{7}{3}q<0$ or $p-3q > 0$.


For $K=9_{43}$ we have
 \begin{eqnarray*}
d_+[J_K(n)] &=& \begin{cases} 8n^2/3 - n/2 - 13/6 &\mbox{if } n \not\equiv 0 \pmod{3}\\ 
8n^2/3 - 5n/6 -7/2 & \mbox{if } n \equiv 0 \pmod{3}.\end{cases}

\end{eqnarray*}
Hence $K_{p,q}$ satisfies Conjectures \ref{conj}  and  \ref{slope} if $p-\frac{31}{3}q<0$ or $p - 11q>\frac{2}{3}$.


For $K=9_{44}$ we have
\begin{eqnarray*}
d_+[J_K(n)] &=& \begin{cases} 7n^2/6 - n - 1/6 &\mbox{if } n \not\equiv 0 \pmod{3}\\ 
7n^2/6 - 4n/3 -1/2 & \mbox{if } n \equiv 0 \pmod{3}.\end{cases}

\end{eqnarray*}
Hence $K_{p,q}$ satisfies Conjectures \ref{conj}  and  \ref{slope} if $p-\frac{13}{3}q<0$ or $p - 5q > 0 $.

\end{example}
