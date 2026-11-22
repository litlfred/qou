---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-006-7-some-counterexamples
section_title: "Some counterexamples"
section_number: 7
pages: 17-19
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.945
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 9 sections: Front matter; Introduction and statement of main; The Hecke algebra and permutation"
---
\label{SecCounterEx}

Let $R = \Z[q,q^{-1}]$. We write the $m^\th$ cyclotomic polynomial in
$q$ as $\Phi_m = \Phi_m(q)$.

Andersen remarked that in general the Gram matrix $G(\lambda)$ is not
diagonalizable \cite[Remark~5.11]{Andersen:Tilting}. We give two
examples of this kind.

Note that $G(\lambda)$ is divisibly diagonalizable over
$\Z_{(p)}[q,q^{-1}]$ for all but finitely many primes $p$. In fact, it
suffices to exclude the primes occurring in the denominators of the
entries of the matrices used to diagonalize $G(\lambda)$ over
$\Q[q,q^{-1}]$.

We record the elementary divisors in ``jump notation''. That is, we write
\[
\lraa{f_1} m_1 \lraa{f_2} m_2 \lraa{f_3} m_3 \lraa{f_4} \cdots \lraa{f_s} m_s
\]
to indicate that the matrix has the elementary divisor $f_1$ with
multiplicity $m_1$, the elementary divisor $f_1 f_2$ with multiplicity
$m_2$, \dots, and the elementary divisor $f_1\cdots f_s$ with
multiplicity $m_s$. 

\begin{Example}
\rm
Let $\lambda = (3,3,2)$. The elementary divisors of $G(3,3,2)$ over $\Q[q,q^{-1}]$ are given by
\[
\lraa{\Phi_2^2} 1 \lraa{\Phi_4} 20\lraa{\Phi_3\Phi_5} 20 \lraa{\Phi_4} 1\; ;
\]
over $\F_2[q,q^{-1}]$ they are given by
\[
\lraa{\Phi_2^3} 1 \lraa{\Phi_2} 20\lraa{\Phi_3\Phi_5} 20 \lraa{\Phi_2} 1\; ;
\]
and, putting $q = 1$, over $\Z$ they are given by
\[
\lraa{2^3} 21\lraa{3\cdot 5} 21 \; .
\]
We claim that $G(3,3,2)$ is not diagonalizable over
$\Z_{(2)}[q,q^{-1}]$. To see this suppose that it is diagonalizable.
Then, considered as an element of $\Z_{(2)}[q,q^{-1}]$, any resulting
diagonal entry must contain the factor $(q+1)$ with exponent $2$.
Considered as an element of $\F_2[q,q^{-1}]$ the factor $(q+1)$ can
occur only with even exponent in such a diagonal entry. But this is
not the case, so we have a contradiction.

This claim in particular implies that $G(3,3,2)$ is not diagonalizable
over $\Z[q,q^{-1}]$.

We remark that the comparison of the elementary divisors over $\Q[q,q^{-1}]$ and over 
$\Z$ yields a contradiction to diagonalizability over $\Z_{(2)}[q,q^{-1}]$, too.
\end{Example}

\begin{Example}
\rm
Let $\lambda = (4,2,1,1)$. The elementary divisors of $G(4,2,1,1)$ over $\Q[q,q^{-1}]$ are given by
\[
\lraa{\Phi_2} 14\lraa{\Phi_2} 1 \lraa{\Phi_4} 30\lraa{\Phi_7} 30\lraa{\Phi_4} 1 \lraa{\Phi_2} 14\; ;
\]
over $\F_2[q,q^{-1}]$ they are given by
\[
\lraa{\Phi_2} 14\lraa{\Phi_2^2} 1 \lraa{\Phi_2} 30\lraa{\Phi_7} 30\lraa{\Phi_2} 1 \lraa{\Phi_2^2} 14\; ;
\]
over $\F_3[q,q^{-1}]$ they are given by
\[
\lraa{\Phi_2} 13\lraa{\Phi_2} 2 \lraa{\Phi_4} 30\lraa{\Phi_7} 30\lraa{\Phi_4} 2 \lraa{\Phi_2} 13\; ;
\]
and, putting $q = 1$, over $\Z$ they are given by
\[
\lraa{2} 14\lraa{2^2} 31 \lraa{7} 31\lraa{2^2} 14\; .
\]
We claim that $G(4,2,1,1)$ is not diagonalizable over
$\Z_{(2)}[q,q^{-1}]$. Again, by way of contradiction suppose that it
is diagonalizable. In $\F_2[q,q^{-1}]$, $14$ of the resulting diagonal
entries contain the factor $(q+1)$ with exponent $1$. Therefore, in
$\Z_{(2)}[q,q^{-1}]$, $14$ of them contain the factor $(q+1)$ with
exponent $1$ and the factor $(q^2 + 1)$ with exponent $0$. Similarly,
in $\F_2[q,q^{-1}]$, $14$ of the resulting diagonal entries contain
the factor $(q+1)$ with exponent $7$. Thus in $\Z_{(2)}[q,q^{-1}]$,
$14$ of them contain the factor $(q+1)$ with exponent $3$ and the
factor $(q^2 + 1)$ with exponent $2$. Hence in $\F_2[q,q^{-1}]$, no
other diagonal entry can contain $(q+1)$ with odd exponent. But in
$\F_2[q,q^{-1}]$, there is a diagonal entry containing $(q+1)$ to the
power $3$ and another containing it to the power $5$ so, again, we have a
contradiction.

We claim that $G(4,2,1,1)$ is not diagonalizable over $\Z_{(3)}[q,q^{-1}]$. Assume it to be diagonalizable. In $\Z_{(3)}[q,q^{-1}]$, $14$ of the resulting
diagonal entries contain $(q+1)$ with exponent $1$. This contradicts the fact that in $\F_3[q,q^{-1}]$, only $13$ of them contain $(q+1)$ with 
exponent $1$.

Both claims independently imply that $G(4,2,1,1)$ is not diagonalizable over $\Z[q,q^{-1}]$.

We remark that the comparison of the elementary divisors over $\Q[q,q^{-1}]$ and over 
$\Z$ yields a contradiction to diagonalizability over $\Z_{(2)}[q,q^{-1}]$, too.
\end{Example}

Finally, we give a (non-exhaustive) list of elementary divisors of
some divisibly diagonalizable Gram matrices for non-hooks, calculated
using {\sc Gap 3} \cite{Gap} and {\sc Magma} \cite{Magma}. We omit the
respective conjugate partition; compare (\ref{CorDiagbar}).

\begin{footnotesize}
$$\begin{array}{lll}\toprule
n& \lambda&\text{Elementary divisors of\ } G(\lambda) \\\midrule
4&(2,2)   &\lraa{\Phi_2} 1\lraa{\Phi_3} 1 \\[4pt]\hline
5&(3,2)   &\lraa{1} 1\lraa{\Phi_3} 3\lraa{\Phi_4} 1 \\[4pt]\hline
6&(4,2)   &\lraa{1} 4\lraa{\Phi_4} 1 \lraa{\Phi_2} 3\lraa{\Phi_5} 1 \\ 
 &(3,3)   &\lraa{\Phi_2} 1\lraa{\Phi_3} 3\lraa{\Phi_4} 1 \\
 &(3,2,1) &\lraa{1} 4\lraa{\Phi_3} 4\lraa{\Phi_5} 4\lraa{\Phi_3} 4 \\[4pt]\hline
7&(5,2)   &\lraa{1} 8\lraa{\Phi_5} 5\lraa{\Phi_3\Phi_6} 1 \\
 &(4,3)   &\lraa{1} 1\lraa{\Phi_3} 7\lraa{\Phi_4} 5\lraa{\Phi_5} 1 \\
 &(3,3,1) &\lraa{\Phi_2} 6 \lraa{\Phi_3} 2\lraa{\Phi_5} 12\lraa{\Phi_4} 1\\[4pt]\hline
8&(6,2)   &\lraa{1} 13\lraa{\Phi_3\Phi_6} 1 \lraa{\Phi_2} 5\lraa{\Phi_7} 1 \\
 &(5,3)   &\lraa{1} 8\lraa{\Phi_4} 6\lraa{\Phi_2} 7\lraa{\Phi_5} 6\lraa{\Phi_6} 1 \\
 &(4,4)   &\lraa{\Phi_2} 1\lraa{\Phi_3} 7\lraa{\Phi_4} 5\lraa{\Phi_5} 1 \\[4pt]\hline
9&(7,2)   &\lraa{1} 19 \lraa{\Phi_7} 7 \lraa{\Phi_4\Phi_8} 1 \\
 &(6,3)   &\lraa{1}21\lraa{\Phi_5}19\lraa{\Phi_6} 1 \lraa{\Phi_3} 6\lraa{\Phi_7} 1\\
 &(5,4)   &\lraa{1} 1\lraa{\Phi_3} 15\lraa{\Phi_4} 18\lraa{\Phi_5} 7\lraa{\Phi_6} 1 
\\[4pt]\bottomrule
\end{array}$$
\end{footnotesize}

We do not know an example of a Gram matrix $G(\lambda)$ that is diagonalizable over
$\Z[q,q^{-1}]$, but not divisibly diagonalizable.

For a general partition $\lambda$, we can not decide whether
$G(\lambda)$ is diagonalizable over $\Z[q,q^{-1}]$.
