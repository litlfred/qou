---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming"
section_id: sec-003-some-packing-problems
section_title: "Some packing problems"
section_number: null
pages: 6-8
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.984
doc_brief: "N-Fold Integer Programming — In this article we study a broad class of integer programming problems in variable dimension."
---
\label{Applications2}

\vskip.5cm\noindent{\sc Minimum cost shipment}

\vskip.2cm\noindent
The minimum cost shipment problem concerns the shipment of a large stock
of items of several types, using various vessels, with minimum possible cost.
More precisely, the data is as follows. There are $t$ types of items.
The weight of each item of type $j$ is $w_j$ and there are $n_j$ items
of type $j$ to be shipped. There are $v$ available vessels, where vessel
$k$ has maximum weight capacity $u_k$. The cost of shipping one item of
type $j$ on vessel $k$ is $p_{j,k}$. We now formulate this as an n-fold
integer programming problem. We set $n:=v$, $p:=1$, $q:=t+1$.
The defining matrix is the row vector $A=(A_j):=(w_1,w_2,\dots,w_t,1)$.
The variables vector is $x=(x^1,\dots, x^n)$
with $x^k=(x^k_1,\dots,x^k_t,x^k_q)$, where $x^k_j$ represents the number
of items of type $j$ to be shipped on vessel $k$ for $j=1,\dots,t$, and
$x^k_q$ is an extra slack variable representing the unused weight capacity
in vessel $k$. The cost vector is $c=(c^1,\dots, c^n)$ with
$c^k=(c^k_1,\dots,c^k_t,c^k_q)$, where $c^k_j:=p_{j,k}$ for $j=1,\dots,t$,
and $c^k_q:=0$. Finally, the demand vector is $b=(b^0,b^1,\dots,b^n)$ \break
with  $b^k:=u_k$ for $k=1,\dots,n$, and
$b^0:=(n_1,\dots,n_t,\sum_{k=1}^v u_k-\sum_{j=1}^t n_jw_j)$.
Then the resulting n-fold integer programming problem,
$\min\{cx:\ A^{(n)}x=b,\ x\in\N^{nq}\}$,
can be written in scalar form as follows:
\begin{eqnarray*}
\min & & \sum_{j=1}^q \sum_{k=1}^n c^k_j\,x^k_j
    \ = \  \sum_{j=1}^t \sum_{k=1}^v p_{j,k}\,x^k_j \\
s.t. & & \sum_{k=1}^n x^k_j=b^0_j=n_j\,,\quad\quad\ j=1,\dots, t \\
     & & \sum_{k=1}^n x^k_q=b^0_q=\sum_{k=1}^v u_k-\sum_{j=1}^t n_jw_j \\
     & & \sum_{j=1}^q A_j\,x^k_j = \sum_{j=1}^t w_j\,x^k_j + x^k_q
            = b^k = u_k \,,\quad\quad\ k=1,\dots, n\\
     & & x^k_j\in\N\,,\quad\quad\quad\quad j=1,\dots, q\,,\quad k=1,\dots, n\ .
\end{eqnarray*}
Assume that the number $t$ of types is fixed, but the numbers $n_j$ of items
of each type may be very large: this is a reasonable assumption in applications
(for instance, several types of automobiles to be shipped overseas, or several
types of appliances to be shipped on ground). Then we obtain the following
striking corollary of Theorem \ref{Main}, showing that the problem is
polynomial time solvable, where the input size is $v$ plus the bit size of
the integer numbers $n_j, u_k, p_{j,k}$ constituting the data.
Note that this result is {\em much stronger} than the standard
results on the {\em pseudo-polynomial time} solvability of this kind of
packing and knapsack-type problems using dynamic programming: our algorithm
can handle {\em very large} $n_j$ and $u_k$, possibly exponential
in the dimensional parameter $v$.

\bc{Shipment}
For any fixed number $t$ of types and type weights $w_j$, the minimum cost
shipment problem is solvable in time which is polynomial in the number $v$
of vessels and in the bit size of the integer numbers $n_j$ of items of each
type to be shipped, vessel capacities $u_k$, and shipment costs $p_{j,k}$.
\ec


\vskip.5cm\noindent{\sc The cutting stock problem}

\vskip.2cm\noindent
This is a classical manufacturing problem, where the usual setup is as follows:
a manufacturer supplies rolls of material (such as scotch-tape or band-aid)
in one of $t$ different widths $w_1,\dots,w_t$. The rolls are all cut out
from standard rolls of common large width $u$, coming out of the production line.
Given orders by customers for $n_j$ rolls of width $w_j$, the problem facing
the manufacturer is to meet the orders using the smallest possible number
of standard rolls. This is almost a direct special case of the minimum
cost shipment problem discussed above, with sufficiently many identical
vessels, say $v:=\sum_{j=1}^t\lceil n_j / \lfloor u / w_j \rfloor \rceil$,
of capacity $u_k:=u$ each, playing the role of the standard rolls, and with
cost $p_{j,k}:=w_j$ for each roll of width $w_j$ regardless of the standard
roll from which it is being cut out. The only correction needed is that
each slack variable $x^k_q=x^k_{t+1}$, measuring the unused width of
the $k$th standard roll, has cost of one unit instead of zero,
so that the total cost becomes the number of standard rolls used.
Thus the formulation as an n-fold program is with
$n:=\sum_{j=1}^t\lceil n_j / \lfloor u/w_j \rfloor \rceil$, $p:=1$, $q:=t+1$,
$A:=(w_1,w_2,\dots,w_t,1)$, variables $x^k_j$ representing the number
of rolls of width $w_j$ cut out of the $k$th roll for $j=1,\dots,t$
and $x^k_q$ representing the unused width of the $k$th standard roll,
costs $c^k_j:=w_j$ for $j=1,\dots,t$ and $c^k_q:=1$, and demands
$b^k:=u$ for $k=1,\dots,n$ and $b^0:=(n_1,\dots,n_t,nu-\sum_{j=1}^t n_jw_j)$.

Again, quite surprisingly, we get the following useful
corollary regarding this classical problem.

\bc{CuttingStock}
For any fixed $t$ and widths $w_1,\dots,w_t$,
the cutting stock problem is solvable in time polynomial in
$\sum_{j=1}^t\lceil n_j / \lfloor u / w_j \rfloor \rceil$ and in
the bit size of the numbers $n_j$ of orders and raw roll width $u$.
\ec

One common approach to the cutting stock problem makes use of so-called
{\em cutting patterns}, which are feasible solutions of the knapsack
problem $\{y\in\N^t\,:\,\sum_{j=1}^t w_jy_j\leq u\}$. This is useful
when the width $u$ of the standard rolls is of the same order of magnitude
as the demand widths $w_j$. However, when $u$ is much larger than the $w_j$,
the number of cutting patterns becomes prohibitively large to handle.
But then the values $\lfloor u/w_j\rfloor$ are large and hence
$n:=\sum_{j=1}^t\lceil n_j / \lfloor u/w_j \rfloor \rceil$
is small, in which case the result of Corollary \ref{CuttingStock}
using $n$-fold integer programming becomes particularly appealing.
