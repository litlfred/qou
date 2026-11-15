---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-016-41-uniform-bounds-of-the-colored-jones-function
section_title: "Uniform bounds of the colored Jones function"
section_number: 4.1
pages: 10-11
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.792
latex_coverage_ratio: 0.934
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.reductionA}

In this section we will deduce Theorem \ref{thm.boundC3} from estimates
of the degree and the coefficients of the cyclotomic expansion of
the knot. These estimates will be established in Section
\ref{sec.boundsJones}.
By definition $f_{K,n}(\a) = J_{K,n}(e^{\a/n})$, hence equation
\eqref{cyc} gives that
\begin{eqnarray}
\lbl{eq.J2Ca} f_{K,n}(\a) &=& \sum_{k=0}^{n-1} C_{n,k}(e^{\a/n})
H_{K,k}(e^{\a/n}).
\end{eqnarray}

To have upper bounds for $|f_{K,n}(\a)|$ we will need bounds for
$H_{K,k}(e^{\a/n})$ and the ``kernel'' $C_{n,k}(e^{\a/n})$ (the
kernel does not depend on the knot $K$).


\begin{definition}
\lbl{def.l1norm}
For a Laurent polynomial $f(q)=\sum_k a_k q^k$, we define its
$l^1$-norm by
$$
||f||_1=\sum_k |a_k|.
$$
\end{definition}
The proof of the following Theorem, which gives bounds for the
degrees and the $l^1$-norm of $H_{K,n}$, will be given in Section
\ref{sec.boundscyclotomic}.

\begin{theorem}
\lbl{thm.boundC}
{\rm (Proof in Section \ref{sec.boundscyclotomic})}
For every knot $K$, there are positive constants
$A_0, A_1$ (depending on $K$) such that for all $n \in \BN$ we have
\begin{equation}
H_{K,n}(q) = \sum_{j=-A_0n^2}^{A_0n^2} b_{j,n} q^j.
\tag{a}\label{eq1}
\end{equation}
and
\begin{equation}
\lbl{eq.LC} ||H_{K,n}||_1 \leq A_1^n . \tag{b}
\end{equation}
\end{theorem}


The next lemma follows from Theorem \ref{thm.boundC} and an elementary estimate.

\begin{lemma}
\lbl{lem.estimate}
Suppose $|\a| < 1$.
\begin{itemize}
\item[(a)]   For every knot $K$ there is a constant
$A_2$ such that for every $ 0\le k\le n$, we have
$$
|H_{K,k}(e^{\a/n}) | \le (A_2)^k.
$$
\item[(b)]
There is a constant $A_3 >0$ such that every $ 0\le k \leq n$ we
have:
$$
|C_{n,k}(e^{\a/n})| \leq (A_3)^k |\a|^k.
$$
\end{itemize}
\end{lemma}

\begin{proof}
(a) By Theorem \ref{thm.boundC}(a),
$$
H_{K,k}(e^{\a/n}) = \sum_{j=-A_0k^2}^{A_0k^2} b_{j,k} e^{j\a/n}.
$$
From the bounds for $j$ and $k\le n$  one has that $|j/n| \le A_0 k$,
hence $ |e^{j\a/n}| \le \exp (A_0\,  k\, |\Re(\a)|) \le \exp(k \, A_0) $. From
the above equation one has
$$
\left | H_{K,k}(e^{\a/n})\right | \le ||H_{K,k}||_1 \, (\exp A_0)^k.
$$
Using Theorem \ref{thm.boundC}, it is enough to take $A_2 = A_1
\exp(A_0)$.

(b) By definition,
$$
C_{n,k}(e^{\a/n})=\prod_{j=1}^{k} (e^{\a}+e^{-\a}-e^{j\a/n}
-e^{-j\a/n}) = \prod_{j=1}^{k} \left(g(\a) -g(j\a/n)\right),
$$
where $g(z)= e^z + e^{-z}$. One has $g'(z) = e^z -e^{-z}$, hence for
$z$ on the interval connecting $\a$ and $j\a/n$, with $0\le j\le n$,
one has $|g'(z)| \le 2 \exp(|\a|) \le  2e$. By the mean value theorem,
we have, for $0 \le j \le k \le n$,
$$
|g(\a) -g(j\a/n)| \le 2 e |\a -j\a/n| \le  2 e |\a|.
$$
It follows that
$$
|C_{n,k}(e^{\a/n})| \le (2 e)^k |\a|^k.$$ It is enough to take
$A_3=2e$.
\end{proof}



\subsection{Theorem \ref{thm.boundC} implies Theorem \ref{thm.boundC3}}
\lbl{sub.thm.boundC2}

It follows from Lemma \ref{lem.estimate}  that for  $0 \leq k \leq n$
and $|\a|< 1$, we have:
\begin{eqnarray*}
|C_{n,k}(e^{\a/n}) H_{K,k}(e^{\a/n})| & \leq & |\a A_2 A_3|^k.
\end{eqnarray*}

Let us choose $U_K$ to be the disk centered  at the 0, with radius
$1/(2A_2A_3+1)$, then $ |\a A_2 A_3| < 1/2$ for $\a \in U_K$.
Equation \eqref{eq.J2Ca} and the above estimate imply that for all
$n$ and all $\a \in U_K$, we have:
$$
|f_{K,n}(\a)| \le  \sum_{k=0}^{n-1}
\left |C_{n,k}(e^{\a/n}) H_{K,k}(e^{\a/n})\right| \\
\le  \sum_{k=0}^{n-1} (1/2)^k < 2.
$$
which concludes the proof of Theorem \ref{thm.boundC3}, assuming
Theorem \ref{thm.boundC}.
\qed
