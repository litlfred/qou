---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming"
section_id: sec-005-graver-bases-of-n-fold-matrices
section_title: "Graver bases of n-fold matrices"
section_number: null
pages: 11-13
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 1.0
doc_brief: "N-Fold Integer Programming — In this article we study a broad class of integer programming problems in variable dimension."
---
Fix any pair of integer matrices $A$ and $B$ with the same number of columns,
of dimensions $r\times q$ and $s\times q$, respectively. The {\em n-fold
matrix of the ordered pair $A,B$} is the following $(s+nr)\times nq$ matrix,
\[
[A,B]^{(n)} \quad:=\quad ({\bf 1}_n\otimes B)\oplus (I_n\otimes A)\quad=\quad
\left(
\begin{array}{ccccc}
  B & B & B & \cdots & B      \\
  A & 0 & 0 & \cdots & 0      \\
  0 & A & 0 & \cdots & 0      \\
  \vdots & \vdots & \ddots & \vdots & \vdots \\
  0  & 0 & 0      & \cdots & A      \\
\end{array}
\right)\quad .
\]
With this, the generalized n-fold integer programming
problem can be conveniently written as
$$\min\{cx:\ [A,B]^{(n)}x=b,\ x\in\N^{nq}\}\quad.$$
The n-fold of a single matrix $A$, defined in the introduction, is the
special case $A^{(n)}=[A,I_q]^{(n)}$ with $B=I_q$ the $q\times q$ identity,
giving the regular (non-generalized) n-fold integer programming problem.

We now discuss a recent result of \cite{SS} and its extension in
\cite{HS} on the stabilization of Graver bases of n-fold matrices.
Consider vectors $x=(x^1,\ldots,x^n)$ with $x^k\in\N^q$ for $k=1,\dots,n$.
The {\em type} of $x$ is the number $|\{k\,:\,x^k\neq 0\}|$
of nonzero components $x^k\in\N^q$ of $x$. The following result of \cite{HS}
on the stabilization of Graver bases of $[A,B]^{(n)}$ extends
the earlier result for $B=I_q$ from \cite{SS}.

\bp{GraverComplexity}
For every pair of integer matrices $A\in\Z^{r\times q}$ and
$B\in\Z^{s\times q}$, there exists a constant $g(A,B)$
such that for all $n$, the Graver basis of $[A,B]^{(n)}$
consists of vectors of type at most $g(A,B)$.
\ep
The smallest constant $g(A,B)$ possible in the proposition
is called the {\em Graver complexity} of $A,B$.

Using Proposition \ref{GraverComplexity}, we now show that
$\G([A,B]^{(n)})$ can be computed in polynomial time.

\bt{TheoremGraver}
Fix any pair of integer matrices $A\in\Z^{r\times q}$ and $B\in\Z^{s\times q}$.
Then there is a polynomial time algorithm that, given $n$, computes the Graver
basis $\G([A,B]^{(n)})$ of the n-fold matrix $[A,B]^{(n)}$. In particular, the
cardinality and the bit size of $\G([A,B]^{(n)})$ are bounded by a polynomial
function of $n$.
\et
\boproof
Let $g:=g(A,B)$ be the Graver complexity of $A,B$ and consider any $n\geq g$.
We show that the Graver basis of $[A,B]^{(n)}$ is the union of
$n\choose g$ suitably embedded copies of the Graver basis of $[A,B]^{(g)}$.
Consider any $g$ indices $1\leq k_1<\dots <k_g\leq n$ and define a map
$\phi_{k_1,\dots,k_g}$ from $\N^{gq}$ to $\N^{nq}$ by sending
$x=(x^1,\ldots,x^g)$ to $y=(y^1,\ldots,y^n)$ defined by
$y^{k_t}:=x^t$ for $t=1,\dots,g$, and $y^k:=0$ for all other $k$.

We claim that the Graver basis of $[A,B]^{(n)}$ is the union of the images
of the Graver basis of $[A,B]^{(g)}$ under the $n\choose g$ maps
$\phi_{k_1,\dots,k_g}$ for all $1\leq k_1<\dots <k_g\leq n$, that is,
\begin{equation}
\G([A,B]^{(n)})\quad=\quad \bigcup_{1\leq k_1<\dots <k_g\leq n}
\phi_{k_1,\dots,k_g}(\G([A,B]^{(g)}))\quad .
\end{equation}
To see this, recall first that, by definition, the Graver basis of a
matrix $M$ is the set of all $\red$-minimal nonzero dependencies on $M$
(where a dependency on $M$ is a vector $x$ satisfying $Mx=0$).
Thus, if $x=(x^1,\ldots,x^g)\in\G([A,B]^{(g)})$ then $x$ is a
$\red$-minimal nonzero dependency on $[A,B]^{(g)}$, implying that
$\phi_{k_1,\dots,k_g}(x)$ is a $\red$-minimal nonzero dependency
on $[A,B]^{(n)}$ and hence $\phi_{k_1,\dots,k_g}(x)\in\G([A,B]^{(n)})$.
This establishes that the right-hand side of (1) is contained in the
left-hand side. Conversely, consider any $y\in\G([A,B]^{(n)})$. Then,
by Proposition \ref{GraverComplexity}, the type of $y$ is at most $g$,
so there are indices $1\leq k_1<\dots <k_g\leq n$ such that all
nonzero components of $y$ are among those of the reduced vector
$x:=(y^{k_1},\ldots,y^{k_g})$, and therefore $y=\phi_{k_1,\dots,k_g}(x)$.
Now, $y\in\G([A,B]^{(n)})$ implies that $y$ is a $\red$-minimal
nonzero dependency on $[A,B]^{(n)}$, and therefore $x$ is a $\red$-minimal
nonzero dependency on $[A,B]^{(g)}$ and hence $x\in\G([A,B]^{(g)})$,
showing that $y\in\phi_{k_1,\dots,k_g}(\G([A,B]^{(g)}))$. This establishes
that the left-hand side of (1) is contained in the right-hand side.
Thus, the Graver basis of $[A,B]^{(n)}$ is indeed given by (1).

Since $A,B$ are fixed and hence $g=g(A,B)$ is constant, the $g$-fold matrix
$[A,B]^{(g)}$ is also fixed and so the cardinality and bit size of its Graver
basis $\G([A,B]^{(g)})$ are constant as well. It follows from (1) that
$|\G([A,B]^{(n)})|\leq {n\choose g}|\G([A,B]^{(g)})|=O(n^g)$.
Further, each element of $\G([A,B]^{(n)})$ is an $nq$-dimensional vector
$\phi_{k_1,\dots,k_g}(x)$ obtained from some $x\in\G([A,B]^{(g)})$
(of constant bit size) by appending zero components, and therefore is
of linear bit size $O(n)$, showing that the bit size of the entire
Graver basis $\G([A,B]^{(n)})$ is $O(n^{g+1})$. Finally, it is clear that
the ${n\choose g}=O(n^g)$ images  $\phi_{k_1,\dots,k_g}(\G([A,B]^{(g)}))$
and their union $\G([A,B]^{(n)})$ can be computed in
time polynomial in $n$, completing the proof.
\eoproof

\be{Example2}
Consider the matrices $A=[1\ 1]$ and $B=I_2$.
The Graver complexity of the pair $A,B$ is $g(A,B)=2$. The 2-fold matrix
and its Graver basis, consisting of two antipodal vectors only, are
$$
[A,B]^{(2)}\ =\ A^{(2)}
\ =\ \left(
\begin{array}{cccc}
  1 & 0 & 1 & 0 \\
  0 & 1 & 0 & 1 \\
  1 & 1 & 0 & 0 \\
  0 & 0 & 1 & 1 \\
\end{array}
\right)\,,\quad\quad
\G([A,B]^{(2)})
\ =\ \pm \left(
\begin{array}{cccc}
  1 & -1 & -1 & 1 \\
\end{array}
\right)\quad.
$$
By Theorem \ref{TheoremGraver}, the Graver basis of the 4-fold matrix
$[A,B]^{(4)}=A^{(4)}$ can be computed by taking the union of the
images of the $6={4\choose 2}$ maps
$\phi_{k_1,k_2}:\N^{2\cdot 2}\longrightarrow\N^{4\cdot 2}$
for $1\leq k_1<k_2\leq 4$, and we obtain
$$
[A,B]^{(4)}=\left(
\begin{array}{cccccccc}
  1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 \\
  0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 \\
  1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 \\
\end{array}
\right),\ \G([A,B]^{(4)})
=\pm \left(
\begin{array}{cccccccc}
  1 & -1 & -1 & 1 & 0 & 0 & 0 & 0 \\
  1 & -1 & 0 & 0 & -1 & 1 & 0 & 0 \\
  1 & -1 & 0 & 0 & 0 & 0 & -1 & 1 \\
  0 & 0 & 1 & -1 & -1 & 1 & 0 & 0 \\
  0 & 0 & 1 & -1 & 0 & 0 & -1 & 1 \\
  0 & 0 & 0 & 0 & 1 & -1 & -1 & 1 \\
\end{array}
\right)\, .
$$
\ee
