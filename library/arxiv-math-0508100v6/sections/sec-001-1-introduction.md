---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
1.1. Asymptotics of the colored Jones function of a knot 2
1.2. The generalized volume conjecture 4
1.3. The Generalized Volume Conjecture near 2 πi 5
1.4. Upper bounds for the generalized volume conjecture 5
1.5. Relation with hyperbolic geometry, and asymptotically sharp bou nds 5
1.6. The main ideas and organization of the paper 7
1.7. Acknowledgment 8
2. Weak versus strong convergence 8
2.1. A lemma from complex analysis 8
2.2. The main diﬃculty for uniform bounds 8
3. Two expansions of the colored Jones polynomial 8
3.1. The loop expansion 8
3.2. The cyclotomic expansion 9
3.3. Comparing the cyclotomic and the loop expansion 10
4. A reduction of Theorem 2.2 to estimates of the cyclotomic function 10
4.1. Uniform bounds of the colored Jones function 10
4.2. Theorem 4.2 implies Theorem 2.2 11
5. A reduction of Theorem 1.6 to estimates of the cyclotomic function 12
5.1. Some estimates 12
5.2. Theorem 4.2 implies Theorem 1.6 13
6. Bounds for the degree and coeﬃcients of the colored Jones fun ction 14
6.1. Bounds for the degree 14
6.2. Bounds for the coeﬃcients 14
Date: August 26, 2011.
The authors were supported in part by National Science Found ation.
1991 Mathematics Classiﬁcation. Primary 57N10. Secondary 57M25.
Key words and phrases: hyperbolic volume conjecture, color ed Jones function, Jones polynomial, R-matrices, regular
ideal octahedron, weave, hyperbolic geometry, Catalan ’s c onstant, Borromean rings, cyclotomic expansion, loop expa nsion,
asymptotic expansion, WKB, q-diﬀerence equations, asymptotics, perturbation theory, Kontsevich integral.
1
2 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
6.3. Proof of Theorem 1.12 16
7. Proof of Theorem 4.2 16
7.1. The bound for degrees of HK,n 16
7.2. The bound for the l1-norm of HK,n 17
8. Growth rates of R-matrices and the Lobachevsky function 18
8.1. The Lobachevsky function 18
8.2. Asymptotics of the R-matrix using ideal octahedra 19
8.3. The maximum of the growth rate of the R-matrix 21
8.4. The maximum of the R-matrices at roots of unity 22
8.5. Proof of Theorem 1.13 22
9. The generalized volume conjecture near α = 2πi 22
10. The q-holonomic point of view 23
10.1. Bounds on l1-norm of q-holonomic functions 23
10.2. Bounds for higher rank groups 24
11. Some physics 24
11.1. A small dose of physics 24
11.2. The WKB method 25
Appendix A. The volume conjecture for the Borromean rings 25
Appendix B. Proof of Proposition 8.9 27
B.1. Preliminary estimates 27
B.2. Proof of Proposition 8.9 28
References 30
1. Introduction
1.1. Asymptotics of the colored Jones function of a knot. To a knot K in 3-space, one can associate
a sequence of Laurent polynomials
JK,n (q) ∈ Z[q±1]
for n ∈ N = {1, 2, 3, . . .}. JK, 1(q) = 1 and JK, 2(q) is the famous Jones polynomial of K introduced by
Jones in [ Jon87], and JK,n (q) are roughly speaking the Jones polynomials of ( n − 1)-parallels of the knot.
More precisely, JK,n (q) is the quantum group invariant of K using the n-dimensional irreducible sl2(C)
representation, normalized by Junknot,n (q) = 1 for all n; see [ RT90, Tur94]. The sequence {JK,n (q)}n is often
called the colored Jones function of the knot K.
The paper is concerned with the asymptotic growth of the colored J ones function. More precisely, ﬁx a
knot K and consider the sequence of holomorphic functions:
fK,n : C − →C, f K,n (z) := JK,n (ez/n )
for n ∈ N. In other words, we are evaluating the n-th polynomial JK,n (q) at a complex n-th root of ez. We
will be concerned with strong and weak convergence of the sequen ce fK,n , for n ∈ N. Let us explain what
we mean by that. Fix an open subset U of C containing 0.
Deﬁnition 1.1. (a) A sequence of holomorphic functions fn : U − → C strongly converges in U to a
holomorphic function f : U − →C (and write slim n→∞fn(z) = f (z)) if fn(z) converges to f (z) uniformly on
any compact subset of U .
(b) A sequence of holomorphic functions fn : U − →C weakly converges to a holomorphic function f : U − →C
(and write wlim n→∞fn(z) = f (z)) if the Taylor series of fn(z) at z = 0 coeﬃcient-wise converges to the
Taylor series of f (z). In other words, for every k ≥ 0, we have:
lim
n→∞
dkfn
dzk
⏐
⏐
⏐
z=0
= dkf
dzk
⏐
⏐
⏐
z=0
.
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 3
It is easy to see that strong convergence of holomorphic function s implies weak convergence. The converse
is not true (see however, Lemma 2.1 below).
The Melvin-Morton-Rozansky (MMR, in short) Conjecture, which w as settled by Bar-Natan and the
ﬁrst author in [ BNG96], compares the function fK,n of a knot K with the Alexander polynomial ∆ K of K,
normalized by ∆ K(t−1) = ∆ K (t) and ∆ K(1) = 1.
Theorem 1.2. (The MMR conjecture) [ BNG96] For every knot K we have
wlimn→∞ fK,n (z) = 1
∆ K(ez) .
Our sample result is the following analytic form of the MMR Conjecture , which has application in the
Generalized Volume Conjecture.
Theorem 1.3. (Proof in Section
2.1) For every knot K there exists an open neighborhood UK of 0 ∈ C such
that in UK, we have
slimn→∞fK,n (z) = 1
∆ K(ez) .
Given Theorem 1.3 one may ask for a full asymptotic expansion of fK,n (z) in terms of powers of 1 /n. In
order to formulate our results, let us introduce the notion of stro ng and weak asymptotic expansions.
Deﬁnition 1.4. Fix an open set U of C, and holomorphic functions fn : U − →C and Rn : U − →C.
(a) We will say that the sequence fn is strongly asymptotic in U to the series ∑ ∞
k=0 Rk(z)
(z
n
) k
, and write
(1) fn(z) ∼s
n→∞
∞∑
k=0
Rk(z)
(z
n
) k
if for every N ≥ 0 we have:
(2) slim n→∞
(n
z
) N
(
fn(z) −
N −1∑
k=0
Rk(z)
(z
n
) k
)
= RN (z).
(b) Likewise, we will say that the sequence fn is weakly asymptotic in U to the series ∑ ∞
k=0 Rk(z)
(z
n
) k
, and
write
(3) fn(z) ∼w
n→∞
∞∑
k=0
Rk(z)
(z
n
) k
if for every N ≥ 0 we have:
(4) wlim n→∞
(n
z
) N
(
fn(z) −
N −1∑
k=0
Rk(z)
(z
n
) k
)
= RN (z).
Usually, sequences of holomorphic functions fn(z) do not have asymptotic expansions (or even a limit, as
n → ∞). However, sequences that appear in perturbative expansions o f Quantum Field Theory are generally
expected to have asymptotic expansions. In fact asymptotic exp ansions are generally easier to deﬁne (via
Feynman diagram techniques) than the partition functions fK,n (z) themselves. Even when the partition
functions can be deﬁned, the asymptotic expansions is a numerically useful way to approximate them.
In [ Roz98], Rozansky discovered that the sequence fK,n (z) has a weak asymptotic expansion, where the
terms are rational functions in the variable ez. More precisely, Rozansky proved the following result.
Theorem 1.5. [Roz98] For every knot K there exists a sequence PK,k (q) ∈ Q[q±1] of Laurent polynomials
with PK, 0(q) = 1 such that
(5) fK,n (z) ∼w
n→∞
∞∑
k=0
PK,k (ez)
∆ K(ez)2k+1
(z
n
) k
.
4 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
A diﬀerent proof, valid for all simple Lie groups, was given in [ Gar], using work of [ GK04]. Our result is
strong version of Theorem 1.5.
Theorem 1.6. (Proof in Section 5.2) For every knot K there exists an open neighborhood ˜UK of 0 ∈ C such
that in ˜UK, we have
(6) fK,n (z) ∼s
n→∞
∞∑
k=0
PK,k (ez)
∆ K(ez)2k+1
(z
n
) k
.
