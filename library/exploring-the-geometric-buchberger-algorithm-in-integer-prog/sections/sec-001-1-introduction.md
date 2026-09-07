---
doc_id: exploring-the-geometric-buchberger-algorithm-in-integer-prog
doc_title: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br"
section_id: sec-001-1-introduction
section_title: "INTRODUCTION"
section_number: 1
pages: 1-1
source_pdf: Exploring the Geometric Buchberger Algorithm in Integer Programming.pdf
source_sha256: 73854bc5e3bcffb0
doc_brief: "Exploring the Geometric Buchberger Algorithm in Integer Programming Gabriel Mattos Langeloh gmlangeloh@inf.ufrgs.br — The Geometric Buchberger algorithm is a specialization of the clas- sical"
---
Integer programming, that is, finding an optimal solution to IP4,(b)
min{c? x | Ax = b, x € Z”} is an NP-hard computational problem
with many applications in graph theory, combinatorial optimization
and other areas. Conti and Traverso [4] showed that this problem
can be solved by computing Grébner bases of toric ideals. Although
at first this approach may seem counter-productive due to the dou-
bly exponential degree bound of Grébner basis elements by Mayr
and Meyer [23] when compared to previously known exponential
algorithms for integer programming, such as the branch-and-bound
method, a singly exponential degree bound for Grébner bases of
toric ideals is also known [29]. Furthermore, more recent results
[3] have shown that the Grébner basis approach is Fixed-Parameter
Tractable (FPT) with respect to a parameter related to the sparsity
of the constraint matrix A of the integer program.

Various connections of Grébner bases of toric ideals to the the-
ory of integer programming are known. For example, [30, 33] show
that sensitivity analysis for integer programming can be done via
Grébner basis methods, while [15-17, 34] relate these methods to

Publication rights licensed to ACM. ACM acknowledges that this contribution was
authored or co-authored by an employee, contractor or affiliate of a national govern-
ment. As such, the Government retains a nonexclusive, royalty-free right to publish
or reproduce this article, or to allow others to do so, for Government purposes only.
Request permissions from owner/author(s).

ISSAC '24, July 16-19, 2024, Raleigh, NC, USA

© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0696-7/24/07

https://doi.org/10.1145/3666000.3669706

334

(extended) group relaxations of integer programs. The latter connec-
tion is particularly relevant for current Grébner basis algorithms
and will be detailed in Section 2.

Grébner basis computations for integer programming were fur-
ther improved by Thomas’ Geometric Buchberger Algorithm [32],
the use of truncated Grébner bases [35], the GRIN implementation
of Grébner bases for integer programming [14] and the project-and-
lift algorithm to find initial generating sets of toric ideals [21, 22],
among others [20, 36], leading to the state-of-the-art implemen-
tation 4ti2 [1]. However, the practical use of these techniques in
integer programming remains limited, since the classical methods
for this problem, based on the branch-and-bound algorithm, are
more efficient on the vast majority of cases, essentially because
they are able to avoid a large part of the search space of this type
of optimization problem. Of particular note are uses of Grébner
basis methods to solve problems related to integer programming
that include additional complications, making them less tractable
by classical methods. Examples of this situation are applications
to optimization problems with non-linear constraints [10, 11], to
problems with stochastic constraints [31] and to multiobjective
integer programming [2, 12, 18], where the Grébner basis meth-
ods are competitive because they are able to efficiently solve all
problems in the family IP4,(b) for varying b.

The main goals of this paper are to further improve Grébner
basis methods for integer programming, especially when there are
many binary variables, as is the case in many common combinato-
rial optimization problems, and to evaluate their performance in
these problems to strengthen their use in applications where solv-
ing multiple problems in an integer programming family is useful.
Although such experimental analyses have been done before in the
literature [36], Grébner basis methods for toric ideals have been
significantly improved since then. Additionally, we are not aware of
any previous work specializing Grébner basis techniques to binary
variables in integer programming, despite the relative importance
of this particular case. We assume familiarity with the theory of
Grébner basis of arbitrary ideals and Buchberger’s algorithm in this
context, but no familiarity with the integer programming special
case.
