---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming"
section_id: sec-002-high-dimensional-transportation-problems
section_title: "High dimensional transportation problems"
section_number: null
pages: 3-6
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.966
doc_brief: "N-Fold Integer Programming — In this article we study a broad class of integer programming problems in variable dimension."
---
\label{Applications1}

A {\em $d$-way transportation polytope} is the set of all
$m_1\times\cdots\times m_d$ nonnegative arrays $x=(x_{i_1,\dots,i_d})$
such that the sums of the entries over some of their lower dimensional
subarrays ({\em margins}) are specified. For simplicity of exposition, we shall
concentrate here only on $d$-way {\em line-sum polytopes}, of the form
$$T =  \left\{\,x\in\R_+^{m_1\times\cdots \times m_d}
\, : \, \sum_{i_1} x_{i_1,\dots,i_d}=u_{i_2,\dots, i_d}\,,
\ \sum_{i_2} x_{i_1,\dots,i_d}=u_{i_1,i_3,\dots, i_d}\,,
\ \dots\,,\ \sum_{i_d} x_{i_1,\dots,i_d}=u_{i_1,\dots,i_{d-1}}\,\right\}\,.$$
Transportation polytopes and their integer points (called
contingency tables by statisticians), have been studied and
used extensively in the operations research literature and in
the context of secure statistical data disclosure by public agencies
such as the census bureau and the national center for health statistics.
In the operations research literature, one is typically interested in the
integer and linear transportation problems, which are the integer and
linear programming problems over the transportation polytope, see
e.g. \cite{BR,KW,OR,QS,Vla,YKK} and references therein. In the statistics
community, one is often interested in the values an entry can attain
in all tables with fixed margins, related to the security of the entry
under margin disclosure, and in the construction of a Markov basis
allowing a random walk on the set of tables with fixed margins, see e.g.
\cite{AT,Cox1,Cox2,DO3,DFKPR,IJ} and references therein.

It is well known that the system defining a $2$-way transportation polytope
is totally unimodular. This implies that all the above problems are easy in
this case. However, already $3$-way transportation problems are much harder.
Consider the problem of deciding if a given $3$-way line-sum polytope of
$r\times s \times l$ arrays (with $r$ rows, $s$ columns and $l$ layers)
contains an integer point: the computational complexity of this problem
provides useful indication about the difficulty of the problems mentioned above.
If $r,s,l$ are all fixed, then the problem is solvable in
polynomial time by integer programming in fixed dimension $rsl$.
On the other hand, if $r,s,l$ are all variable part of the input,
then the problem is NP-complete \cite{IJ}. The in-between cases are
much more delicate. The case of two parameters $r,s$ variable and
one parameter $l$ fixed was recently resolved in \cite{DO1}, where it was
shown to be NP-complete, strengthening \cite{IJ}. Moreover, very recently,
in \cite{DO2}, the following striking universality result was shown.
\bp{Transportation}
Any rational polytope $P=\{y\in\R_+^n:Ay=b\}$ is polynomial time
representable as a $3$-way line-sum transportation polytope
of size $r\times s\times 3$ for some (polynomially bounded) $r$ and $s$,
$$T\quad=\quad\{\,x\in\R_+^{r\times s\times 3}\ :\ \sum_i x_{i,j,k}=w_{j,k}\,,\
\sum_j x_{i,j,k}=v_{i,k}\,,\ \sum_k x_{i,j,k}=u_{i,j}\,\}\ .$$
\ep
Here representable means that there is a coordinate-erasing projection from
$\R^{r\times s\times 3}$ onto $\R^n$ providing a bijection between $T$ and
$P$ and between the sets of integer points $T\cap\Z^{r\times s\times 3}$
and $P\cap\Z^n$. Thus, {\em any} rational polytope is an
$r\times s\times 3$ line-sum polytope, and {\em any} integer (respectively,
linear) programming problem is equivalent to an integer (respectively, linear)
$r\times s\times 3$ line-sum transportation problem. This result led to the
solution of several open problems from \cite{Vla} and \cite{YKK} and had
several implications on the complexity of Markov bases and the entry
security problem, see \cite{DO2} and \cite{DO3} for more details.

However, the last case, of two parameters $r,s$ fixed and one
parameter $l$ variable, has remained open and intriguing.
Here, as a consequence of Theorem \ref{Main}, we are able to
resolve this problem and show that both the decision and
optimization problems are polynomial time solvable.

\bc{Threeway}
Fix any $r,s$. Then there is a polynomial time algorithm that, given
$l$, integer objective vector $c$, and integer line-sums $(u_{i,j})$,
$(v_{i,k})$ and $(w_{j,k})$, solves the integer transportation problem
$$\min\{\,cx\ :\ x\in\N^{r\times s\times l}\,,\ \sum_i x_{i,j,k}=w_{j,k}
\,,\ \sum_j x_{i,j,k}=v_{i,k}\,,\ \sum_k x_{i,j,k}=u_{i,j}\,\}\ .$$
\ec
\boproof
We formulate the $3$-way integer transportation problem as an n-fold
integer program with $n:=l$, $p:=r+s$, and $q:=r\cdot s$.
Reindex the variables as $x^k_{i,j}:=x_{i,j,k}$ so that the variables
vector is $x=(x^1,\dots,x^n)$ with $x^k=(x^k_{i,j})\in\N^{r\times s}$
a $2$-way $r\times s$ table - the $k$th layer of the $3$-way table $x$.
Similarly write $c=(c^1,\dots,c^n)$ with $c^k\in\Z^{r\times s}$
for the objective vector. Next, put $b:=(b^0,b^1,\dots,b^n)$, with
$b^0\in\N^{rs}$ defined by $b^0:=(u_{i,j})$, and $b^k\in\N^{r+s}$
defined by $b^k:=((v_{i,k}),(w_{j,k}))$ for $k=1,\dots,n$.
Finally, let $A$ be the $p\times q=(r+s)\times r\cdot s$ matrix of
equations for the usual $2$-way transportation polytope, forcing
row-sums and column-sums on each of the $r\times s$ layers $x^k$
by $Ax^k=b^k$, $k=1,\dots,n$. Then the equations $Ax^k=b^k$ force the
line-sums $v_{i,k}$ and $w_{j,k}$, and the additional n-fold integer
program binding constraint $\sum_{k=1}^n x^k=b^0$
forces the ``long" line-sums $u_{i,j}$. This completes the encoding.
Since $r,s$ are fixed, so are $p,q$, and $A$, and therefore,
the corollary follows from Theorem \ref{Main}.
\eoproof
\be{Example1}
Consider the case $r=s=3$ (the smallest where the problem is
genuinely $3$-dimensional). Then $p=6$, $q=9$, and writing
$x^k=(x^k_{1,1},x^k_{1,2},x^k_{1,3},x^k_{2,1},x^k_{2,2},x^k_{2,3},
x^k_{3,1},x^k_{3,2},x^k_{3,3})$, the matrix $A$ which defines the
n-fold program providing the formulation of the
$3\times 3\times l$ transportation problem is
$$A\quad=\quad\left(
\begin{array}{ccccccccc}
  1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 \\
  1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 \\
  0 & 1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 \\
  0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 1 \\
\end{array}
\right)\quad.
$$
Already for this case, of $3\times 3\times l$ tables, the only polynomial
time algorithm for the corresponding line-sum integer transportation problem
we are aware of is the one guaranteed by Corollary \ref{Threeway} above.
\ee

Corollary \ref{Threeway} extends to transportation problems
of any dimension $d$, for {\em long} tables, namely, of size
$m_1\times\cdots\times m_{d-1}\times l$, where $m_1,\dots, m_{d-1}$
are fixed and only the length $l$ is variable, as follows.
\bc{Multiway}
Fix $d,m_1,\dots,m_{d-1}$. Then there is a polynomial time algorithm that,
given $l$, integer objective $c$, and line-sums
$(u_{i_2,\dots, i_d}),\dots, (u_{i_1,\dots, i_{d-1}})$,
solves the long multiway transportation problem
$$\min \{c x\ :\ x\in\N^{m_1\times\cdots \times m_{d-1}\times l}
\, : \, \sum_{i_1} x_{i_1,\dots,i_d}=u_{i_2,\dots, i_d}\,,
\ \dots\,,\ \sum_{i_d} x_{i_1,\dots,i_d}=u_{i_1,\dots,i_{d-1}}\,\}\,.$$
\ec
\boproof
The long multiway transportation problem can be encoded as an
n-fold integer program with $n:=l$, $p:=\sum_{i=1}^{d-1}m_i$, and
$q:=\prod_{i=1}^{d-1}m_i$, by reindexing the variables as
$x^{i_d}_{i_1,\dots,i_{d-1}}:=x_{i_1,\dots,i_d}$, letting $A$ be the
matrix of equations of line-sums of $(d-1)$-way transportation polytope
of $m_1\times\cdots\times m_{d-1}$ arrays, and proceeding in direct
analogy to the proof of Corollary \ref{Threeway}. The details are omitted.
\eoproof
