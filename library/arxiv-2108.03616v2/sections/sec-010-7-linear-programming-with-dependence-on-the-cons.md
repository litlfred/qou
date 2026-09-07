---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-010-7-linear-programming-with-dependence-on-the-cons
section_title: "Linear programming with dependence on the constraint matrix only"
section_number: 7
pages: 24-25
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
trix only
Recent years have seen tremendous progress in the developme nt of more eﬃcient LP algo-
rithms using interior point methods, see e.g. [ CLS19, LS19, vdBLN+20, vdBLL+21] and refer-
ences therein. These algorithms are weakly polynomial, i.e., their running time depends on the
encoding length of the input ( A,b,c ) of LP(A,b,c ).
A fundamental open problem is the existence of a strongly polynomial LP algorithm; this was
listed by Smale as one of the key open problems in mathematics for the 21st century [ Sma98].
The number of arithmetic operations of such an algorithm wou ld be polynomial in the number
n of variables and m of constraints, but independent of the input length.
Towards this end, there is a line of work on developing algori thms with running time depend-
ing only on the constraint matrix A, while removing the dependence on b and c. This direction
was pioneered by Tardos’s 1985 paper [ Tar86], giving an algorithm for LP(A,b,c ) with integral
A that has runtime poly( m,n, log ∆ A).
A breakthrough work by Vavasis and Ye [ VY96] introduced a Layered Least Squares Interior-
Point Method that solves LP(A,b,c ) withinO(n3.5 log( ¯χA +n)) iterations, each requiring to solve
a linear system. Recall from Theorem 4.2 that log( ¯χA +n) = Θ(log( κA +n)); also recall from
Proposition 3.2 that κA≤ ∆ A.
Recently, [ DHNV20] improved the Vavasis–Ye bound to O(n2.5 log(n) log( ¯χ∗
A +n)) linear
system solves, where ¯χ∗
A is the optimized version of ¯ χA, analogous to κ∗
A deﬁned in Section 5.
The key insight of this work is using the circuit imbalance me asureκA as a proxy to ¯χA. These
results are discussed in Section 7.2.
Section 7.1 exhibits another recent paper [ DNV20] that extends Tardos’s black-box frame-
work to solve LP in runtime poly( m,n, log(¯κA +n)), based on the proximity results in Section 6.
We note that using an initial rescaling as in Theorem 5.1, we can obtain poly( m,n, log(¯κ∗
A +n))
runtimes from these algorithms.
24
