---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-009-32-cables-of-knots-of-period-at-most-2
section_title: "Cables of knots of period at most 2"
section_number: 3.2
pages: 10-14
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.917
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
\label{period_2}

In this subsection we will study knots with period at most two. Examples of such knots include all the adequate knots and the torus knots. We show that, under a mild hypothesis satisfied by all the known examples, the property of having period at most two is preserved under cabling (Proposition \ref{quasi}). As a  result, if a knot $K \subset S^3$ satisfies the Slope Conjecture and $\pi(K)\leq 2$, then all but at most two cables of $K$ also satisfy the conjecture.



\begin{proposition}
\label{quasi}
Let $K$ be a knot such that for $n \gg 0$ we have
$$
d_+[J_K(n)]=a(n)n^2+b(n)n+d(n)
$$
is a quadratic quasi-polynomial of period $\le 2$, with $b(n) \le 0$. 

Suppose $\frac{p}{q} \notin \{4a(n)\}$. Then for $n \gg 0$ we have
$$d_+[J_{\K}(n)]=A(n)n^2+B(n)n+D(n)$$
is a quadratic quasi-polynomial of period $\le 2$, with $\{A(n)\} \subset \big( \{q^2a(n)\} \cup \{pq/4\} \big)$ and $B(n) \le 0$.
\end{proposition}
 


\begin{proof} 

Since $d_+[J_K(n)]$ is a quadratic quasi-polynomial of period $\le 2$, for $n \gg 0$ we can write

$$d_+[J_K(n)]=\begin{cases} 
a_0 n^2+b_0n+d_0 & \mbox{if } n \mbox{ is even},\\
a_1 n^2+b_1n+d_1 & \mbox{if } n \mbox{ is odd}.\end{cases}$$


 Recall that $K_{p,q}$ is the $(p,q)$-cable of a knot $K$, where $p,q$ are coprime integers and $|q|>1$. It is known that $K_{-p,-q}=\text{r}K_{p,q}$, where $\text{r}K_{p,q}$ denotes $\K$ with the opposite orientation, and that the colored Jones polynomial of a \textit{knot} is independent of the orientation of the knot. Hence, without loss of generality, we will assume that $q > 1$. 
 
 
 
 For $n>0$, let $\CS_n$ be the set of all $k$ such that 
 $$
 |k| \le (n-1)/2 \quad \text{and} \quad k \in \begin{cases} \BZ &\mbox{if } n \text{ is odd}, \\ 
 \BZ+\frac{1}{2} & \mbox{if } n \text{ is even}. \end{cases}
 $$
By \cite{Ve}, for $n>0$ we have
\begin{equation}
\label{cables}
J_{K_{p,q}}(n)= v^{pq(n^2-1)/4} \sum_{k \in \CS_n} v^{-pk(qk+1)} J_K(2qk+1),
\end{equation} 
where it is understood that $J_K(-m)=-J_K(m)$.

In the above formula, there is a sum. Under the assumption of the proposition, we will show that there is a unique term of the sum whose highest degree is strictly greater than those of the other terms. This implies that the highest degree of the sum is exactly equal to the highest degree of that unique term. 


Let $\CS^+_n=\{k \in \CS_n \mid k \ge 0\}$ and $\CS^-_n=\{k \in \CS_n \mid k \le -\frac{1}{2}\}$.  For $k \in \CS_n$ let $$f(k)=d_+[v^{-pk(qk+1)} J_K(2qk+1)].$$
Let $g_i^{\pm}(x)$, for $i \in \{0,1\}$, be the quadratic real polynomials defined by
$$
g_i^{\pm}(x) = ( -pq + 4q^2 a_i ) x^2 + ( -p + 4q a_i \pm 2q b_i ) x +  a_i \pm b_i + d_i.
$$
For $k \in \CS_n$ we have 
$f(k) = -pk(qk+1)+d_+[J_K(|2qk+1|)]$, which gives
\begin{eqnarray*}
 f(k)=
\begin{cases} 
g_0^+(k) &\mbox{if } k \in \CS^+_n \mbox{ and } 2qk+1 \mbox{ is even}, \\
g_0^-(k) &\mbox{if } k \in \CS^-_n \mbox{ and } 2qk+1 \mbox{ is even},\\
g_1^+(k) &\mbox{if } k \in \CS^+_n \mbox{ and } 2qk+1 \mbox{ is odd}, \\
g_1^-(k) &\mbox{if } k \in \CS^-_n \mbox{ and } 2qk+1 \mbox{ is odd}. 
\end{cases}
\end{eqnarray*}

\smallskip

\underline{\textit{Case 1.}}\   Suppose that $q$ is even.
For $k \in \CS_n$, since $2qk+1$ is odd we have $$f(k)= \begin{cases} g_1^+(k) &\mbox{if } k \in \CS^+_n, \\
g_1^-(k) &\mbox{if } k \in \CS^-_n.  \end{cases}$$
\vskip 0.1in

\textit{Subcase 1.1.} Assume  that  $p/q <4a_1$.

Since $-pq + 4q^2 a_1>0$, the quadratic polynomial $g_1^+(x)$ is concave up. Hence, for $n \gg 0$, $g_1^+(k)$ is maximized on $\CS^+_n$ at $k=(n-1)/2$.  Similarly, $g_1^-(k)$ is maximized on $\CS^-_n$ at $k=(1-n)/2$. Note that $$g_1^+ \big( (n-1)/2 \big)-g_1^-  \big( (1-n)/2 \big)=(-p+4qa_1)(n-1)+2b_1>0$$
for $n \gg 0$. Hence $f(k)$ is maximized on the set $\CS_n$ at $k=(n-1)/2$. Since $f \big( (n-1)/2 \big)=g^+_1 \big( (n-1)/2 \big)$, equation \eqref{cables} then implies that  
\begin{eqnarray*}
d_+[J_{K_{p,q}}(n)] &=& pq(n^2-1)/4+g_1^+ \big((n-1)/2 \big)\\
&=& q^2a_1n^2+ \big(qb_1+(q-1)(p-4qa_1)/2 \big)n\\
&& + \, a_1(q-1)^2-(b_1+p/2)(q-1)+d_1
\end{eqnarray*}
for $n \gg 0$. Since we assumed that $q>1$, we have that $B(n) = qb_1+(q-1)(p-4qa_1)/2<0$, and the conclusion follows in this case.
\vskip 0.1in

\textit{Subcase 1.2.} 
Assume that $p/q >4a_1$. 

Since $-pq + 4q^2 a_1<0$, the quadratic polynomial $g_1^+(x)$ is concave down and attains its maximum at 
$$x=x_0:=- \left(\frac{1}{2q}+\frac{b_1}{-p+4qa_1} \right).$$ Since $b_1 \le 0$, we have $x_0 < 0$. This implies that $g_1^+(x)$ is a strictly decreasing function on $[0,\infty)$. Similarly, $g_1^-(x)$ is a strictly increasing function on $(-\infty,-\frac{1}{2}]$.  

First suppose $n$ is even. Then $k \in \BZ+\frac{1}{2}$. In this subcase, $g_1^+(k)$ is maximized on $\CS^+_n$ at $k=\frac{1}{2}$ and $g_1^-(k)$ is maximized on $\CS^-_n$ at $k=-\frac{1}{2}$. Note that $g_1^+(\frac{1}{2})-g_1^-(-\frac{1}{2})=(-p+4qa_1)+2b_1<0$. Hence $f(k)$ is maximized on $\CS_n$ at $k=-1/2$. Since $f(-\frac{1}{2})=g_1^-(-\frac{1}{2})$, equation \eqref{cables} then implies that
$$d_+[J_{K_{p,q}}(n)]=pq(n^2-1)/4+g^-_1(-1/2)$$
for even $n \gg 0$. Similarly, for odd $n \gg 0$ we obtain
$$d_+[J_{K_{p,q}}(n)]=pq(n^2-1)/4+g^+_1(0).$$
Note that $B(n) = 0$ in this case.
\vskip 0.2in


\underline{\textit{Case 2.}} \ Suppose that $q$ is odd. 
As in Case 1 we have the following.
\vskip 0.1in

\textit{Subcase 2.1.}  Suppose that $n$ is even. 

For $k \in \CS_n$, we have $k \in \BZ+\frac{1}{2}$ and $2qk+1$ is even. Hence $f(k)= \begin{cases} g_0^+(k) &\mbox{if } k \in \CS^+_n, \\
g_0^-(k) &\mbox{if } k \in \CS^-_n.  \end{cases}$

If $p/q <4a_0$ then $f(k)$ is maximized on $\CS_n$ at $k=(n-1)/2$. Hence
\begin{eqnarray*}
d_+[J_{K_{p,q}}(n)] &=& pq(n^2-1)/4+g_0^+ \big( (n-1)/2 \big)\\
&=& q^2a_0n^2+ \big(qb_0+(q-1)(p-4qa_0)/2 \big)n\\
&& + \, a_0(q-1)^2-(b_0+p/2)(q-1)+d_0.
\end{eqnarray*}
In this case we have $B(n) = qb_0+(q-1)(p-4qa_0)/2<0$.

If $p/q >4a_0$ then $f(k)$ is maximized on $\CS_n$ at $k=-1/2$. Hence $$d_+[J_{K_{p,q}}(n)]=pq(n^2-1)/4+g^-_0(-1/2).$$
Note that $B(n) = 0$ in this case.

\vskip 0.1in

\textit{Subcase 2.1.}  Suppose that $n$ is odd. 

For $k \in \CS_n$, we have $k \in \BZ$ and $2qk+1$ is odd. Hence $f(k)= \begin{cases} g_1^+(k) &\mbox{if } k \in \CS^+_n, \\
g_1^-(k) &\mbox{if } k \in \CS^-_n.  \end{cases}$

If $p/q <4a_1$ then $f(k)$ is maximized on $\CS_n$ at $k=(n-1)/2$. Hence
\begin{eqnarray*}
d_+[J_{K_{p,q}}(n)] &=& pq(n^2-1)/4+g_1^+ \big( (n-1)/2 \big)\\
&=& q^2a_1n^2+ \big(qb_1+(q-1)(p-4qa_1)/2 \big)n\\
&& + \, a_1(q-1)^2-(b_1+p/2)(q-1)+d_1.
\end{eqnarray*}
In this case we have $B(n) = qb_1+(q-1)(p-4qa_1)/2 < 0$.

If $p/q >4a_1$ then $f(k)$ is maximized on $\CS_n$ at $k=0$. Hence $$d_+[J_{K_{p,q}}(n)]=pq(n^2-1)/4+g^+_1(0).$$
Note that $B(n) = 0$ in this case.

This completes the proof of Proposition \ref{quasi}.
\end{proof}

\begin{remark} (1) Proposition \ref{quasi} generalizes \cite[Lemma 2.2]{RZ}, \cite[Lemma 2.2]{Ru},  \cite[Lemma 3.1]{Tr-AJ-8} and \cite[Lemma 3.2]{Tr}.

(2) When $\pi(K)$ is greater than 2 then determining the highest degree of
 $J_{K_{p,q}}(n)$ in Equation \eqref{cables} becomes harder as there might be more opportunities for cancellation
between terms. This case will be discussed in Section \ref{constant a(n)}.
\end{remark}
 
 Proposition \ref{quasi} and Theorem \ref{main:bs} imply the following.
 
 \begin{theorem}
 \label{thm-quasi}
 Let $K$ be a knot such that for $n \gg 0$ we have
$$
d_+[J_K(n)]=a(n)n^2+b(n)n+d(n)
$$
is a quadratic quasi-polynomial of period $\le 2$, with $b(n) \le 0$. 

Suppose $\frac{p}{q} \notin js_K$. Then for $n \gg 0$ we have
$$d_+[J_{\K}(n)]=A(n)n^2+B(n)n+D(n)$$
is a quadratic quasi-polynomial of period $\le 2$, with $B(n) \le 0$. 
Moreover,  if $js_K \subset bs_K$ we have $js_{\K} \subset bs_{\K}$.

Similarly, let $K$ be a knot such that for $n \gg 0$ we have
$$
d_-[J_K(n)]=a^*(n)n^2+b^*(n)n+d^*(n)
$$
is a quadratic quasi-polynomial of period $\le 2$, with $b^*(n) \ge 0$. 
Suppose $\frac{p}{q} \notin js^*_K$.  
Then for $n \gg 0$ we have
$$d_-[J_{\K}(n)]=A^*(n)n^2+B^*(n)n+D^*(n)$$
is a quadratic quasi-polynomial of period $\le 2$, with $B^*(n) \ge 0$. 
Moreover,  if $js^*_K \subset bs_K$ we have $js^*_{\K} \subset bs_{\K}$.
 \end{theorem}
\begin{proof} The first part of the theorem follows immediately by Proposition  \ref{quasi} and Theorem \ref{main:bs}.
To obtain the second part recall that if ${K^{*}}$ denotes the mirror image of $K$ then
$J_{K^{*}}(n)$ is obtained from $J_K(n)$ by replacing the variable $v$ with $v^{-1}$.
Now the result will follow by applying Proposition \ref{quasi} and Theorem \ref{main:bs} to $K^{*}$.
\end{proof}
 
\smallskip
