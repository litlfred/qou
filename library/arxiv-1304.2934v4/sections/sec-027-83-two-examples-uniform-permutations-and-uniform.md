---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-027-83-two-examples-uniform-permutations-and-uniform
section_title: "Two examples: uniform permutations and uniform set-partitions"
section_number: 8.3
pages: 67-68
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
ample that ﬁlls in this framework is the number of disjoint cycles Xn of a uniform
random permutation in S(n). As mod-convergence of Xn has already been discussed
in this article (Example 2.3), we will skip details. Using Feller’s coupling, it is easily
seen that
Pn(t) =
n
∏
i=1
t + i− 1
1 + i− 1.
Moreover, a straight-forward computation yieldsµn = Hn + O(1), σ2
n = Hn + O(1) and
L3
n = Hn + O(1), where Hn is the n-th harmonic number as in Example 2.3. Theorem 8.1
implies that (Xn− Hn)/(Hn)1/3 converges in the mod-Gaussian sense, as established
at the end of Example 2.3. Note however that Theorem 8.1 does not give the stronger
mod-Poisson convergence of (Xn)n∈N without renormalization.
The second and more interesting example is the number of blocks in a random uni-
form set-partition of [n]. By deﬁnition, a set-partition of [n] is a set of disjoint non-
empty subsets of [n], whose union is [n]. These subsets are called blocks or parts of the
set-partition. For instance,{{2, 4},{1},{3}} is a set-partition of [4] with 3 blocks. We
denote Q(n) the set of all set-partitions of [n]. For each integer n≥ 0, we then consider
a random uniform set-partition in Q(n), and denote Xn its number of blocks.
It was proved by Harper [Har67, Lemma 1] that the probability generating function
of Xn has only real non-negative roots. Moreover, the asymptotic behaviour of µn =
E[Xn] and σ2
n = Var(Xn) are known — see e.g. [CDKR15, Theorem 2.1] —
µn = n
log n (1 + o(1)), σ2
n = n
(log n)2 (1 + o(1)).
We will prove in next subsection that
L3
n = 2n
(log n)3 (1 + o(1)).
Since Mn = 1 and
√σn = O
(
n1/4
(log n)1/2
)
≪ Ln = O
(
n1/3
log n
)
≪ σn = O
(
n1/2
log n
)
,
we can apply Theorem 8.1: the variables (Xn− µn)/Ln converge in the mod-Gaussian
sense with parameter tn = σ2
n/L2
n = ( n
4 )1/3 (1 + o(1)) and limiting function ψ(z) =
exp(z3/6). As a corollary, applying Theorem 4.3 and Proposition 4.14 yields the fol-
lowing precise deviation result.
68 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
Proposition 8.3. Let X n be the number of blocks in a uniform set-partition of [n]. Deﬁne
µn, σn, L n and t n as above. Then the random variable Xn−µn
σn converges towards a Gaussian
law, with a normality zone of size o (n1/6). Moreover, at the edge of this normality zone, the
deviation probabilities are given by: for any ﬁxed x > 0,
P
[ Xn− µn
Ln
≥ tnx
]
= exp(−tn x2
2 )
x√2πtn
exp
( x3
6
)
(1 + o(1));
P
[ Xn− µn
Ln
≤− tnx
]
= exp(−tn x2
2 )
x√2πtn
exp
(
− x3
6
)
(1 + o(1)).
