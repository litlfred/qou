---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-026-72-the-bound-for-the-l1-norm-of-hkn
section_title: "The bound for the l1-norm of HK,n"
section_number: 7.2
pages: 17-18
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.904
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
Multiply both sides of \eqref{33}  by $\{2n+2\}!$,
then use  \eqref{31} and Theorem \ref{95}, we see that there is a constant
$A_7$ such that

\begin{equation}
\lbl{eq.L1C} ||\{2n+2\}!H_{K,n}(q)||_1 \leq  (A_7)^n.
\end{equation}
The polynomials
$$
\tH_{K,n}(q) := q^{A_0n^2} H_{K,n}(q) \qquad
\text{and} \qquad  g(q):=\tH_{K,n}(q) \prod_{j=1}^{2n+2}(1-q^j)
$$
have only non-negative degrees in $q$, with $\maxdeg(\tH_{K,n}) \le
2A_0n^2$:

\begin{equation}
\tH_{K,n}(q) = \sum_{k=0}^{2A_0n^2} a_k q^k
\end{equation}
 Since $g(q)$ is the product of the polynomial on the left hand
side of \eqref{eq.L1C} and a power of $q$, we have

\begin{equation}
 ||g(q)||_1 \leq (A_7)^n.
\label{41}
\end{equation}
There are estimates of $l^1$-norm using Mahler measure \cite{Mahler}.
However, the estimate \eqref{41} is weak: the  inequalities of Mahler
imply an exponential upper bound on the Mahler measure of $H_{K,n}(q)$,
and a doubly exponential upper bound on the $l^1$-norm of $H_{K,n}(q)$. The
following estimate, which does not follow from Mahler
measure considerations, was communicated to us by D. Boyd. Since


$$
\tH_{K,n}(q) = g(q) \frac{1}{\prod_{k=j}^{2n+2} (1-q^j)},
$$
we have that
$$
a_k=\sum_{i=0}^k b_i c_{k-i}, \quad \text{where} \quad g(q) =
\sum_{k} b_k q^k \quad \text{and} \quad \frac{1}{\prod_{k=1}^{2n+2}
(1-q^k)}=\sum_{k=0}^\infty c_k q^k.
$$
Note that $c_k$ is the number of partitions of $k$ of length $\le
2n+2$. Hence $0\le c_{k-1} \le c_k$, and $c_k\le p_k$, where $p_k$
is the number of partitions of $k$. Using the growth rate of $p_k$
(see \cite{An}), we see that there is a constant $A_8$ such that
\begin{equation}
p_k < (A_8)^{\sqrt k}.\label{42}
\end{equation}
The crucial part of the above inequality is the exponent
$\sqrt{k}$. Now we can easily
obtain the desired upper bounds for $||\tH_{K,n}||_1$.
Since $ a_k=\sum_{i=0}^k b_i c_{k-i}$  we have

$$
\begin{aligned}
|a_k| & \le \sum_{i=0}^k |b_i| c_{k-i} \le \left( \sum_{i=0}^k
|b_i|\right) c_{k} \le ||g(q)||_1 c_k\\
&\le (A_7)^n (A_8)^{n \sqrt {2A_0}}  \qquad \text{by \eqref{41},
\eqref{42}  and $k \le 2A_0 n^2 $}
\end{aligned}
$$
It follows that, for $n \ge 1$,

$$
||\tH_{K,n}||_1 \le \sum_{k=0}^{2A_0n^2} |a_k|
\le 2A_0n^2 (A_7)^n (A_8)^{n \sqrt
{2A_0}} \le (A_1)^n,
$$
for appropriate $A_1$. This completes the
proof of Theorem \ref{thm.boundC}.
