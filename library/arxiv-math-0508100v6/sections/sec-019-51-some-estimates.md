---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-019-51-some-estimates
section_title: "Some estimates"
section_number: 5.1
pages: 12-13
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.684
latex_coverage_ratio: 0.901
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
The following is a higher order version of Lemma \ref{lem.estimate}.
The proof is similar.


\begin{lemma}
\lbl{lem.estimate2}
Suppose $|\a| < 1$.
\begin{itemize}
\item[(a)]  For $1\le k \le n$, $0\le l$,  and $y$ on
the interval from 0 to $\a/n$ we have
$$
\left |\frac{\partial^l}{\partial y^l} c_k(\a,y)
\right| < (A_3)^k  |\a|^{k-l}\, k^{2l}.
$$
\item[(b)]
For any $y \in \BC, |y| < 1/n$ and $1\le k\le n$ we have
$$
\left |\frac{\partial^l}{\partial y^l}H_{K,k}(e^y)\right
| <(A_2)^k\, (A_0)^l \, k^{2l}.
$$
\end{itemize}
\end{lemma}

\begin{proof}
(a) We have $c_k(\a,y) = \prod_{j=1}^k g_j$, where
$$
g_j = e^\a + e^{-\a} -e^{jy} - e^{-jy}.
$$
\newcommand{\bl}{{\mathbf l}}
By the Leibniz rule, the $l$-th derivative (with
respect to $y$) of $c_k$ is the sum
\begin{equation}
\lbl{form}
\frac{\partial^l}{\partial y^l} c_k(\a,y) = \sum_{|\bl|=l} \binom {l}{l_1,\dots,l_k}\, t(\bl),
\quad \text{where} \quad
t(\bl)=\prod_{j=1}^k g_j^{(l_j)}.
\end{equation}

Here $\bl=(l_1,\dots,l_k), |\bl|:= \sum_{j=1}^k l_j$, $l_j \ge 0$.
 We will estimate each term $t(\bl)$. Fix $\bl= (l_1,\dots,l_k)$. We
consider two cases, $l_j=0$ and $l_j>0 $.

Suppose $l_j=0$. Then $g_j^{(l_j)} = g_j = e^\a + e^{-\a} - e^{jy}
- e^{-jy}$. Since $j \le k \le n$, the interval connecting $\a$ and
$jy$ lies totally in the disk of radius $|\a|$ (remember that $|y|
\le |\a|/n$). As in the proof of Lemma \ref{lem.estimate}, we have
\begin{equation}
\lbl{1}
|g_j|=|(e^{\a} + e^{-\a}) - (e^{jy} + e^{-jy})| \le (2e)|\a|.
\end{equation}




Now suppose $l_j >0$. Then
$$
g_j^{(l_j)} =  - e^{jy}j^{l_j} - e^{-jy}(-j)^{l_j}.$$

It is clear $|e^{\pm \a}| < e$. Since $|j|\le |k|$ and $|jy| < |\a|$,
we have $|e^{\pm jy}(\pm j)^{l_j}| < e k^{l_j}$. Hence

\begin{equation}
\left |g_j^{(l_j)}\right| <  (2e)\, k^{l_j}.
\label{2}
\end{equation}
Taking the product over $j$, using \eqref{1}, \eqref{2} and $\sum l_j =l$,
we get

$$
\begin{aligned} |t(\bl)| & < (2e)^k\,  k^l\,  |\a|^{\#\{l_j =0 \}} \\
        & < (2e)^k\,  k^l\,  |\a|^{k-l} \quad
\text{because} \quad |\al| <1 \quad \text{and} \quad \#\{l_j =0 \} \ge k-l
\end{aligned}
$$
Since $\sum_{|\bl|=l} \binom {l}{l_1,\dots,l_k} =k^l$, from \eqref{form}  and the above estimate for $t(\bl)$, we get the result with
$A_3=2e$.

(b) By Theorem \ref{thm.boundC}(a),

$$
\frac{\partial^l}{\partial y^l}H_{K,k}(e^{y}) =
\sum_{j=-A_0k^2}^{A_0k^2} b_{j,k} e^{jy} j^l.
$$
From the bounds for $j$ and $k\le n$  one has $ |e^{jy}| \le \exp
(A_0 k )$ and $|j^l | \leq (A_0k^2)^l$. From the above equation one has

$$
\left| \frac{\partial^l}{\partial y^l} H_{K,k}(e^{y})\right| \le ||H_{K,k}||_1
\, (\exp A_0)^k (A_0k^2)^l.
$$
Using Theorem \ref{thm.boundC}, it is enough to take $A_2 = A_1
\exp(A_0)$.
\end{proof}

\begin{corollary}
\lbl{14}
For every knot $K$ there are positive constants $A_4, A_5$ such
that
\begin{itemize}
\item[(a)] for $0\le k$, $0\le N$,  and  $|\a| <1$ and $y$  on the
interval from $0$ to $\a/k$, we have
$$ \left |   \frac{\partial^N}{\partial y^N}h_{K,k}(\a,y) \right |
< |\a A_4|^{k-N} (A_5 k^2)^N.
$$
\item[(b)] for $0\le k$, $0\le N$, and  $|\a| <1$  and every positive
integer $n$, we have
$$ \left | h_{K,k}(\a, \a/n) - \sum_{p=0}^{N-1} d_{k,p}(\a) \,
 (\a/n)^p \right|  < \frac{1}{N!}
\left( \frac{\a}{n} \right)^N \, |\a A_4|^{k-N} (A_5 k^2)^N.
$$
\end{itemize}

\end{corollary}

\begin{proof} (a) The $N$-th derivative of $h_{K,k}(\a,y)$, which is
the product of $c_k(\a,y)$ and $H_{K,k}(e^y)$, is the sum of $2^N$
terms, each  of the form

$$
\frac{\partial^l}{\partial y^l} c_k(\a,y) \, \frac{\partial^{N-l}}{\partial
y^{N-l}}H_{K,k}(e^y).
$$

Using  Lemma \ref{lem.estimate2}, the absolute value of the above
term is bounded by $|\a|^{k-l} (A_2A_3)^k (A_0)^{N-l} k^{2N}$, which,
in turn, is less than  $|\a|^{k-N} (A_2A_3)^k (A_0)^{N} k^{2N}$. Hence,
multiplied by $2^N$ we get

$$ \left| \frac{\partial^l}{\partial y^l} h_{K,k}(\a,y) \right| < 2^N
\times |\a|^{k-N} (A_2A_3)^k (A_0)^{N} k^{2N} = (\a A_2A_3)^{k-N}
(2A_0A_2A_3 k^2)^N.
$$
It is enough to take $A_4=A_2A_3$ and $A_5= 2A_0A_2A_3$.

(b) By Taylor's Theorem,
$$
\left | h_{K,k}(\a, \a/n) - \sum_{p=0}^{N-1} d_{k,p}(\a) \,
 (\a/n)^p \right|  < \frac{1}{N!} \left( \frac{\a}{n} \right)^N
 \,\max \left|\frac{\partial^N}{\partial y^N}h_{K,k}(\a,y)\right
 |,
$$
where $\max$ is taken when $y$ is on the interval connecting 0 and
$\a/n$.
Using the  estimate of part (a), we get the result.
\end{proof}



\subsection{Theorem  \ref{thm.boundC} implies Theorem \ref{thm.1}}
\lbl{sub.thm1proof}

To simplify notation, let us define, for a knot $K$,
\begin{equation}
\lbl{eq.simplifynot}
f_{K,n}^{[N]}(z):=J_{K,n}(e^{z/n})-\sum_{k=0}^{N-1}
\frac{P_{K,k}(e^{z})}{\D_K(e^{z})^{2k+1}}
\left(\frac{z}{n}\right)^k.
\end{equation}

Theorem \ref{thm.1} follows from Theorem \ref{thm.Zrat},  Lemma
\ref{lem.complex} and the following uniform bound.


\begin{theorem}
\lbl{thm.boundC4}

For every knot $K$ there exists an open neighborhood $\tilde U_K$ of
$0 \in \BC$ such that for every $N \geq 0$ there exists a positive
number $M_N$ such that for $\a \in \tilde U_K$, and all $n \geq 0$, we
have:
$$
\left|\left( \frac{n}{\a} \right)^N
f_{K,n}^{(N)}(\a) \right| < M_N.
$$
\end{theorem}

\begin{proof}(of Theorem \ref{thm.boundC4}, assuming Theorem
\ref{thm.boundC})
We have the following identities, where the second follows from
\eqref{11} and \eqref{12}:

$$\begin{aligned}
f_{K,n}^{[N]}(\a) & = f_{K,n}(\a) -
\sum_{p=0}^{N-1}
R_{K,p}(\a) \, \left (\frac{\a}{n} \right)^p \\
&= \sum_{k=0}^\infty h_{K,k}(\a,\frac{\a}{n}) - \sum_{p=0}^{N-1}
\left( \sum_{k=0}^\infty d_{k,p}(\a) \right) \left (\frac{\a}{n}
\right)^p
\\ &= \sum_{k=0}^\infty \left [h_{K,k}(\a,\frac{\a}{n}) - \sum_{p=0}^{N-1}
d_{k,p}(\a) \left (\frac{\a}{n} \right)^p \right]
\end{aligned}$$

Using the estimate in Corollary \ref{14}, we see that

$$ \left |\left (\frac{n}{\a}\right)^N f_{K,n}^{[N]}(\a)\right| < \frac{1}{N!}
\sum_{k=0}^\infty \, |\a A_4|^{k-N}\,  (A_5 k^2)^N.
$$
 If
$|\a A_4 | < 1$, the series of the right hand side is absolutely
convergent. It is enough to take $\tilde U_K$ to be the disk centered
at 0 with radius $1/(2A_4+1)$. This proves Theorem
\ref{thm.boundC4}, assuming Theorem \ref{thm.boundC}.
\end{proof}
