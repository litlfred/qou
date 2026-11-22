---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming"
section_id: sec-004-graver-bases-and-directed-augmentation
section_title: "Graver bases and directed augmentation"
section_number: null
pages: 8-11
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.996
doc_brief: "N-Fold Integer Programming — In this article we study a broad class of integer programming problems in variable dimension."
---
Consider the following family $\IP_A$ of integer programs in
standard form, with arbitrary demand vector $b\in\Z^m$ and
arbitrary objective vector $c\in\Z^n$, sharing the same constraint
matrix $A\in\Z^{m\times n}$,
\[
\IP_A(b,c):\quad \min\{cx:\ Ax=b,\ x\in\N^n\}.
\]
A {\em universal test set} for the family $\IP_A$ is a {\em finite} subset
$G$ of the lattice $\L(A):=\{x\in\Z^n:\ Ax=0\}$ of dependencies on $A$
such that whenever $x$ is
feasible but not optimal for $\IP_A(b,c)$ (where $b:=Ax$), there is an
{\em improving direction} $g\in G$, namely such that $x-g$ is feasible
and better, that is, $x-g\in\N^n$ and $cg>0$. Thus, a universal
test set enables the solution of the following augmentation problem.

\vskip.2cm\noindent{\bf Augmentation problem.}
Given $A\in\Z^{m\times n}$, $x\in\N^n$ and $c\in\Z^n$, either find an
improving direction $g\in\Z^n$, namely one with
$x-g\in \{y\in\N^n\,:\,Ay=Ax\}$ and $cg>0$, or assert that no such $g$ exists.

\vskip.2cm\noindent
An {\em augmentation oracle for a matrix $A$} is one that solves the
augmentation problem, that is, when queried on $x\in\N^n$ and $c\in\Z^n$,
it either returns an improving direction $g$ or asserts that none exists.
Clearly, an explicit universal test set $G$ for $A$ enables the efficient
realization of an augmentation oracle for $A$ by simply searching for
an improving direction $g\in G$. An oracle solving the augmentation problem,
and in particular, an explicit universal test set $G$, enable the following
simple iterative procedure that, for any program $\IP_A(b,c)$ in $\IP_A$ with
bounded objective function, converts any feasible $x$ to an optimal one:
``while there exists an improving direction $g$ set $x:=x-g$ and repeat''.

In 1975, Graver \cite{Graver:75} constructed, for \emph{every}
integer matrix $A$, a canonical universal test set. The {\em Graver basis}
${\cal G}(A)$ of $A$ can be defined as follows. First, we need to
extend the partial ordering $\leq$ from $\N^n$ to $\Z^n$. For
$u,v\in\Z^n$ we say that $u$ is {\em conformal} to $v$, denoted $u\red v$,
if $|u_i|\leq |v_i|$ and $u_iv_i\geq 0$ for $i=1,\ldots,n$,
that is, $u$ and $v$ lie in the same orthant of $\R^n$ and each component
of $u$ is bounded by the corresponding component of $v$ in absolute value.
With this, ${\cal G}(A)$ consists precisely of all $\red$-minimal vectors in
$\L(A)\setminus\{0\}$. For a more detailed introduction of Graver
bases we refer to \cite{Hemmecke:PSP}. The currently fastest algorithm
to compute Graver bases, based on a completion procedure and a
project-and-lift approach, is described in \cite{Hemmecke:SymmGraver}
and implemented in the software package \FourTiTwo\ \cite{4ti2}.

The Graver basis, being a universal test set, provides an augmentation oracle
and hence enables to convert any feasible solution to an optimal one for any
$\IP_A(b,c)$ by the iterative augmentation procedure above. But this in
itself is not enough to guarantee an {\em efficient} (polynomial time)
solution: a major remaining question is how many augmentation steps
are needed to reach an optimal solution.

Recently, in \cite{SW}, a directed version of the augmentation problem
was introduced; quite remarkably, it was shown that the number
of {\em directed} augmentation steps needed to reach optimality is polynomial.
We discuss this next. First, we define the directed augmentation problem.


\vskip.2cm\noindent{\bf Directed augmentation problem.}
Given $A\in\Z^{m\times n}$, $x\in\N^n$ and $c',c''\in\Z^n$, either
find $g=g^+-g^-\in\Z^n$ satisfying $x-g\in\{y\in\N^n\,:\,Ay=Ax\}$
and $c'g^+-c''g^->0$, or assert that none exists.

\vskip.2cm\noindent
Here and throughout, $g^+,g^-\in\N^n$ denote the {\em positive} and
{\em negative} parts of $g\in\Z^n$, defined by $g^+_i:=\max\{g_i,0\}$
and $g^-_i:=-\min\{g_i,0\}$ for $i=1,\dots,n$. Thus, the directed
augmentation problem involves {\em two} objective function vectors:
$c'$ controls the cost of the positive part of $g$ and $c''$
controls the cost of the negative part of $g$.
The usual augmentation problem occurs as the special case $c'=c''=c$.
A {\em directed augmentation oracle for $A$} is one that solves
the directed augmentation problem, i.e. when queried on $x\in\N^n$,
$c',c''\in\Z^n$, it either returns an improving direction $g$ or
asserts that none exists.


\vskip.2cm\noindent
In \cite{SW}, it was assumed that the input includes an upper bound vector
$u\in\N^n$ on the variables, so that the actual feasible set is
$\{y\in\N^n\,:\,Ay=Ax,\ y\leq u\}$. Under this assumption, the feasible
region is always bounded and there is always an optimal solution.
Further, the complexity estimates in \cite{SW} depended on the
bit size of $u$ and $b:=Ax$. However, this is not really needed.
Consider the integer program $\IP_A(b,c)\,:\ \min\{cy:\ Ay=b,\ y\in\N^n\}$
with $b=Ax$. Its objective function is bounded
(and hence there is an optimal solution) if and only if it is bounded for
the corresponding LP-relaxation $\min\{cy:\ Ay=b,\ y\in\R_+^n\}$,
which can be checked in polynomial time by linear programming.
Furthermore, whenever $\IP_A(b,c)$ has an optimal solution, it has one of bit
size polynomially bounded in the size of $A$ and $b=Ax$; this basically
follows from Cramer's rule, see e.g. \cite[Section 17.1]{Sch}.
Therefore, it is possible to compute an upper bound $u$ in terms of $A$
and $x$ only, and plug it into the analysis of \cite{SW}; for instance,
$u_k:=m!\,n(n+1)(\max|x_j|)(\max|A_{i,j}|)^m$ for $k=1,\dots,n$ will do.

With this, the results of \cite{SW} imply the following.
\bp{DAP}
There is a polynomial oracle time algorithm that, given $A\in\Z^{m\times n}$,
$x\in\N^n$, $c\in\Z^n$, solves the integer program $IP_A(b,c)$ with $b:=Ax$
by querying a directed augmentation oracle for $A$.
\ep
Here, as usual, {\em solving} the (feasible) integer program means that the
algorithm either returns an optimal solution or asserts that the objective
function is unbounded; and {\em polynomial oracle time} means that the number
of arithmetic operations, the number of calls to the oracle, and the size
of the numbers occurring throughout the algorithm are polynomially bounded
in the size of the input $A,x,c$.

It is not hard to see that if the matrix $A$ is totally unimodular, in
particular the incidence matrix of a directed graph, then a directed
augmentation oracle for $A$ can be realized using linear programming.
However, in general it is not clear which matrices $A$ admit
efficient directed augmentation.

As explained above, the Graver basis of a matrix $A$ yields an
augmentation oracle for $A$. We now show that, moreover, it enables the
realization of a directed augmentation oracle for $A$ as well.

\bl{Graver}
Let $\G(A)$ be the Graver basis of $A\in\Z^{m\times n}$. For any $x\in\N^n$ and
$c',c''\in\Z^n$, there is a $g\in\Z^n$ with $x-g\in\{y\in\N^n\,:\,Ay=Ax\}$
and $c'g^+-c''g^->0$ if and only if there is such $g\in \G(A)$.
\el

\boproof
Suppose $g$ is an improving direction. Then $g\in \L(A)\setminus\{0\}$
and hence can be written as a {\em conformal sum} of
(not necessarily distinct) elements of the Graver basis of $A$,
that is, $g=\sum g^i$ with $g^i\red g$ and $g^i\in\G(A)$ for all $i$.
To see this, recall that $\G(A)$ is the set of $\red$-minimal elements
in $\L(A)\setminus\{0\}$ and note that $\red$ is a well-ordering; if
$g\in\G(A)$, we are done; otherwise there is an $h\in\G(A)$ with
$h\sqsubset g$ in which case, by induction on $\red$, there is a
conformal sum $g-h=\sum g^i$ giving $g=h+\sum g^i$.

Now, $g^i\red g$ is equivalent to $(g^i)^+\leq g^+$ and $(g^i)^-\leq g^-$, so
the conformal sum $g=\sum g^i$ gives corresponding sums of the positive
and negative parts $g^+=\sum (g^i)^+$ and $g^-=\sum (g^i)^-$. Consequently,
\[
0\ <\ c'g^+ - c''g^- \ =\  c'\sum (g^i)^+ - c''\sum (g^i)^-
\ = \ \sum (c'(g^i)^+ - c''(g^i)^-)\ ,
\]
which implies that there is some $g^i$ in this sum with
$c'(g^i)^+ - c''(g^i)^->0$. Now, $g^i\in\G(A)\subset \L(A)$ so $Ag^i=0$
and hence $A(x-g^i)=Ax$. Finally we show that $x-g^i\geq 0$:
if $g^i_j\leq 0$ then $x_j-g^i_j\geq x_j\geq 0$; and if $g^i_j>0$ then
$g^i\red g$ implies $g^i_j\leq g_j$ and thus $x_j-g^i_j \geq x_j - g_j \geq 0$,
the last inequality holding because $g$ is an improving direction.
So $g^i\in\G(A)$ is an improving direction in the Graver basis.
\eoproof

As an immediate corollary of Proposition \ref{DAP}
and Lemma \ref{Graver}, we get the following statement.

\bt{GraverAug}
There is a polynomial time algorithm that, given any matrix $A\in\Z^{m\times n}$
along with its Graver basis $\G(A)$, and vectors $x\in\N^n$ and $c\in\Z^n$,
solves the integer program $IP_A(b,c)$ with $b:=Ax$.
\et

\noindent
While Theorem \ref{GraverAug} holds for any matrix, its complexity bound
depends on the size of the Graver basis which is part of the input.
Typically, the Graver basis is very large and its cardinality may be
exponential in $n$. However, in the next section we show that for a broad
and useful class of matrices, we can tame the behavior of the Graver basis,
leading to an efficient algorithm in terms of $A,x,c$ only.
