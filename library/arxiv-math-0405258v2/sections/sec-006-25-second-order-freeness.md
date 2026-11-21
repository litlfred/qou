---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-006-25-second-order-freeness
section_title: "Second order freeness"
section_number: 2.5
pages: 7-10
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.955
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
In \cite{MSp1}, we introduced the concept of second order freeness
which is intended to capture the structure of the fluctuation
functionals for random matrices arising in the limit $N\to\infty$,
in the same way as the usual freeness captures the structure of the
expectation of the trace in the limit. We recall the relevant
notations and definitions.

\begin{definition}
A \emph{second order non-commutative probability space}
$(\cA,\ab \ff_1,\ff_2)$ consists of a unital algebra $\cA$, a
tracial linear functional
$$\ff_1:\cA\to\CC \qquad\text{with}\qquad
\ff(1)=1$$ and a bilinear functional
$$\ff_2:\cA\times\cA\to\CC,$$
which is tracial in both arguments and which satisfies
$$\ff_2(a,1)=0=\ff_2(1,b)\qquad\text{for all $a,b\in\cA$.}$$
\end{definition}

\begin{notation}
Let unital subalgebras $\cA_1,\dots,\cA_r\subset\cA$ be given.
\\
1) We say that a tuple $(a_1,\dots,a_n)$ ($n\geq 1$) of elements
from $\cA$ is \emph{cyclically alternating} if, for each $k$, we
have an $i(k)\in\{1,\dots,r\}$ such that $a_k\in \cA_{i(k)}$ and, if
$n\geq 2$, we have $i(k)\not= i(k+1)$ for all $k=1,\dots,n$. We
count indices in a cyclic way modulo $n$, i.e., for $k=n$ the above
means $i(n)\not=i(1)$. Note that for $n=1$, we do not impose any
condition on neighbours.
\\
2) We say that a tuple $(a_1,\dots,a_n)$ of elements from $\cA$ is
\emph{centered} if we have
$$\ff_1(a_k)=0\qquad\text{for all $k=1,\dots,n$.}$$
\end{notation}


\begin{definition}\label{free}
Let $(\cA,\ff_1,\ff_2)$ be a second order non-commutative
probability space. We say that unital subalgebras
$\cA_1,\dots,\cA_r\subset \cA$ are \emph{free with respect to
$(\ff_1,\ff_2)$} or \emph{free of second order}, if they are free
(in the usual sense \cite{VDN}) with respect to $\ff_1$ and if the
following condition for $\ff_2$ is satisfied. Whenever we have, for
$n,m\geq 1$, tuples $(a_1,\dots,a_n)$ and $(b_m,\dots, b_1)$ from
$\cA$ such that both are centered and cyclically alternating then we
have
\begin{enumerate}
\item If $n\not=m$, then
$$\ff_2(a_1\cdots a_n, b_m\cdots b_1)=0.$$
\item If $n=m=1$ and $a\in\cA_i$, $b\in\cA_j$, with $i\not= j$,
then
$$\ff_2(a,b)=0.$$
\item If $n=m\geq2$, then
$$\ff_2(a_1\cdots a_n, b_n\cdots b_1)=
\sum_{k=0}^{n-1} \ff_1(a_1b_{1+k})\cdot\ff_1(a_2b_{2+k})\cdots
\ff_1(a_nb_{n+k}).$$
\end{enumerate}
For a visualization of this formula, one should think of two
concentric circles with the $a$'s on one of them and the $b$'s on
the other. However, whereas on one circle we have a clockwise
orientation of the points, on the other circle the orientation is
counter-clockwise. Thus, in order to match up these points modulo a
rotation of the circles, we have to pair the indices as in the sum
above.

\end{definition}

Recall that in the combinatorial description of freeness \cite{NSp},
the extension of $\ff_1$ to a multiplicative function on
non-crossing partitions plays a fundamental role. In the same way,
second order freeness will rely on a suitable extension of $\ff_2$.

\begin{notation}\label{extension}
Let $(\cA,\ff_1,\ff_2)$ be a second order non-commutative
probability space. Then we extend the definition of $\ff_1$ and
$\ff_2$ as follows:
\begin{align*}
\ff_1:\bigcup_{n=1}^\infty\bigl(S_n\times \cA^n)&\to\CC\\
(\pi,a_1,\dots,a_n)&\mapsto \ff_1(\pi)[a_1,\dots,a_n]
\end{align*}
is, for a cycle $\pi=(i_1, i_2,\dots, i_r)$, given by
$$\ff_1(\pi)[a_1,\dots,a_n]:=\ff_1(a_{i_1}a_{i_2}a_{i_3}\cdots
a_{i_r})$$ and extended to general $\pi\in S_n$ by multiplicativity
$$\ff_1(\pi_1\times\pi_2)[a_1,\dots,a_n]=
\ff_1(\pi_1)[a_1,\dots,a_n]\cdot \ff_1(\pi_2)[a_1,\dots,a_n].$$ In a
similar way,
\begin{align*}
\ff_2:\bigcup_{m,n=1}^\infty\bigl(S_m\times S_n\times
\cA^m\times \cA^n)&\to\CC\\
(\pi_1,\pi_2,a_1,\dots,a_m,b_1,\dots,b_m) &\mapsto
\ff_2(\pi_1,\pi_2)[a_1,\dots,a_m;b_1,\dots,b_n]
\end{align*}
is defined, for two cycles $\pi_1=(i_1, i_2, \dots, i_p)$ and
$\pi_2=(j_1, j_2, \dots,\ab j_r)$, by
$$\ff_2(\pi_1,\pi_2)[a_1,\dots,a_m;b_1,\dots,b_n]:=
\ff_2(a_{i_1}a_{i_2}\cdots a_{i_p},b_{j_1}b_{j_2}\cdots b_{j_r})$$
and extended to the general situation by the derivation
property
\begin{multline}\label{leftderivation}
\ff_2(\pi_1\times\pi_2,\pi_3)[a_1,\dots,a_m;b_1,\dots,b_n]
\\=\ff_2(\pi_1,\pi_3)[a_1,\dots,a_m;b_1,\dots,b_n]\cdot
\ff_1(\pi_2)[a_1,\dots,a_m,b_1,\dots,b_n]
\\+
\ff_2(\pi_2,\pi_3)[a_1,\dots,a_m;b_1,\dots,b_n]\cdot
\ff_1(\pi_1)[a_1,\dots,a_m,b_1,\dots,b_n].
\end{multline}
and
\begin{multline}\label{rightderivation}
\ff_2(\pi_1,\pi_2\times\pi_3)[a_1,\dots,a_m;b_1,\dots,b_n]
\\=\ff_2(\pi_1,\pi_2)[a_1,\dots,a_m;b_1,\dots,b_n]\cdot
\ff_1(\pi_3)[a_1,\dots,a_m,b_1,\dots,b_n]
\\+
\ff_2(\pi_1,\pi_3)[a_1,\dots,a_m;b_1,\dots,b_n]\cdot
\ff_1(\pi_2)[a_1,\dots,a_m,b_1,\dots,b_n].
\end{multline}
\end{notation}


\begin{remark}\label{associativity}
Let $(A_i)_{i \in I}$ be a family of unital subalgebras of
the second order probability space $(A, \ff_1, \ff_2)$ which are
free of second order. Suppose that for each $i$ we have
$(B_{i,j})_{j\in K_i}$ a family of unital subalgebras of $A_i$
which are free of second order. By \cite[Prop. 2.5.5 (iii)]{VDN}
$(B_{i,j})_{j \in \cup_i K_i}$ are free of first order. We leave
as an exercise for the reader to show that the proof of
\cite{VDN} can be adapted to show that  $(B_{i,j})_{j \in \cup_i
K_i}$ are free of second order. \end{remark}
