---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.77
latex_coverage_ratio: 0.839
doc_brief: "N-Fold Integer Programming — In this article we study a broad class of integer programming problems in variable dimension."
---
The integer programming problem is the following discrete
optimization problem, where $\N$ denotes the set of nonnegative
integers, $A$ is an integer matrix and $b,c$ are integer vectors of
suitable dimensions:
$$
\min\, \{cx:\ Ax=b,\ x\in\N^q\}.
$$
It is well known to be generally NP-hard but polynomial time
solvable in fixed dimension $q$, see \cite{Sch}.

In this article, motivated by applications to high-dimensional
transportation problems and contingency tables and by the recently
discovered striking universality theorem for rational polytopes
\cite{DO2} (see Section \ref{Applications}), we study the following
class of integer programming problems in variable dimension.

\vskip.2cm\noindent
{\bf The n-fold integer programming problem}. Fix a $p\times q$
integer matrix $A$. Given positive integer $n$ and integer vectors
$b=(b^0,b^1,\dots,b^n)$ and $c=(c^1,\dots,c^n)$, where
$b^0\in\Z^q$, and $b^k\in \Z^p$ and $c^k\in\N^q$ for $k=1,\dots,n$,
find a nonnegative integer vector $x=(x^1,\dots,x^n)$, where $x^k\in\N^q$
for $k=1,\dots,n$, which minimizes $cx=\sum_{k=1}^n c^k x^k$ subject to
the equations $\sum_{k=1}^n x^k=b^0$ and $Ax^k=b^k$ for $k=1,\dots,n$.

\vskip.2cm\noindent
The term ``n-fold integer programming" refers to the problem being
almost separable into $n$ similar programs
$\min\{c^k x:\ Ax^k=b^k,\ x^k\in\N^q\}$ in fixed dimension; however, the
constraint $\sum_{k=1}^n x^k=b^0$ binds these programs together, and the
result is an integer program in large variable dimension $nq$.

\vskip.2cm\noindent
Let the {\em n-fold matrix} of $A$ be the following
$(q+np)\times nq$ matrix, with $I_q$ the $q\times q$ identity matrix:

$$A^{(n)}\quad:=\quad ({\bf 1}_n\otimes I_q)\oplus (I_n \otimes A)\quad=\quad
\left(
\begin{array}{ccccc}
  I_q    & I_q    & I_q    & \cdots & I_q    \\
  A  & 0      & 0      & \cdots & 0      \\
  0  & A      & 0      & \cdots & 0      \\
  \vdots & \vdots & \ddots & \vdots & \vdots \\
  0  & 0      & 0      & \cdots & A      \\
\end{array}
\right)\quad .
$$
\vskip.2cm\noindent
Then the n-fold integer programming problem can be
conveniently written in matrix form as
$$\min\{cx:\ A^{(n)}x=b,\ x\in\N^{nq}\}\quad.$$

In this article we establish the following theorem. Naturally,
the input size is $n$ plus the bit size of the integer objective vector
$c\in\Z^{nq}$ and the integer right-hand side vector $b\in\Z^{q+np}$.

\bt{Main}
Fix any integer matrix $A$. Then there is a polynomial time
algorithm that, given any $n$ and any integer vectors $b$ and $c$,
solves the corresponding n-fold integer programming problem.
\et

\noindent
The proof of this theorem involves two heavy ingredients. First, it makes
use of the equivalence of the linear optimization problem and the directed
augmentation problem, recently introduced and studied in \cite{SW}.
Second, it uses recent results of \cite{HS} and \cite{SS}
on the stabilization of certain Graver bases.

One important consequence of Theorem \ref{Main} is a polynomial time
algorithm for the $3$-way transportation problem for long tables,
settling its computational complexity;
see Section \ref{Applications} for details.

\vskip.2cm\noindent{\bf Corollary \ref{Threeway}\ }
Fix any $r,s$. Then there is a polynomial time algorithm that, given
$l$, integer objective vector $c$, and integer line-sums $(u_{i,j})$,
$(v_{i,k})$ and $(w_{j,k})$, solves the integer transportation problem
$$\min\{\,cx\ :\ x\in\N^{r\times s\times l}\,,\ \sum_i x_{i,j,k}=w_{j,k}
\,,\ \sum_j x_{i,j,k}=v_{i,k}\,,\ \sum_k x_{i,j,k}=u_{i,j}\,\}\ .$$

The n-fold integer programming problem
and theorem can be generalized as follows.

\vskip.2cm\noindent
{\bf Generalized n-fold integer programming}. Fix integer matrices $A,B$
of sizes $r\times q$ and $s\times q$, respectively. Given positive
integer $n$ and integer vectors $b=(b^0,b^1,\dots,b^n)$ and
$c=(c^1,\dots,c^n)$, with $b^0\in\Z^s$, and $b^k\in \Z^r$ and $c^k\in\N^q$
for $k=1,\dots,n$, find $x=(x^1,\dots,x^n)$ with $x^k\in\N^q$ for
$k=1,\dots,n$, which minimizes $cx=\sum_{k=1}^n c^k x^k$ subject to
$\sum_{k=1}^n Bx^k=b^0$ and $Ax^k=b^k$ for $k=1,\dots,n$.

\vskip.2cm\noindent
We have the following more general result, from which
Theorem \ref{Main} is deduced in the case $B=I_q$.

\vskip.2cm\noindent
\bt{Generalized} Fix any pair of integer matrices $A,B$ of compatible sizes.
Then there is a polynomial time algorithm that solves the generalized
n-fold integer programming problem on any input $n,b,c$.
\et

The article is organized as follows. In Section \ref{Applications} we discuss
applications of Theorem \ref{Main} to multiway transportation problems
and to some packing problems, as follows. In \ref{Applications1} we obtain
the aforementioned Corollary \ref{Threeway} which provides a polynomial time
solution to $3$-way integer transportation problems for long tables,
contrasting the recent universality theorem of \cite{DO2} for slim tables.
We also extend this result to $d$-way transportation problems for long
tables of any dimension (Corollary \ref{Multiway}). In \ref{Applications2}
we describe applications to a certain shipment problem
(Corollary \ref{Shipment}) and to the classical cutting stock problem
(Corollary \ref{CuttingStock}). In Sections 3 -- 4 we develop the
necessary ingredients for our n-fold integer programming algorithm,
as follows. In Section 3 we discuss Graver bases and augmentation.
We show (Lemma \ref{Graver}) that the Graver basis allows to solve the
directed augmentation problem introduced recently in \cite{SW}, and,
combining this with the results of \cite{SW}, show that any feasible solution
to an integer program can be augmented to an optimal one in polynomial time
provided the Graver basis is part of the input (Theorem \ref{GraverAug}).
In section 4 we discuss the stabilization of Graver bases discovered recently
in \cite{HS,SS}, and use it to show that Graver bases of n-fold matrices
can be computed in polynomial time (Theorem \ref{TheoremGraver}). Finally, in
Section 5, we combine all the ingredients from Sections 3 and 4, and prove our
main result Theorem \ref{Generalized} and its specialization Theorem \ref{Main}.
