---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-039-43-depoissonization-and-proof-of-theorem-4-fix-s
section_title: "Depoissonization and proof of Theorem 4. Fix some m ="
section_number: 4.3
pages: 33-36
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
1, 2, . . . and denote by Fn the distribution function of λ1, . . . , λm under
the Plancherel measure Mn
Fn(x1, . . . , xm) = Mn ({λ | λi < x i , 1 ≤ i ≤ m}) .
Also, set
F (θ, x) = e−θ
∞∑
k=0
θk
k! Fk(x).
This is the distribution function corresponding to the meas ure M θ .
34 A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
The measures Mn can be obtained as distribution at time n of a
certain random growth process of a Young diagram, see e.g. [3 8]. This
implies that
Fn+1(x) ≤ Fn(x) , x ∈ Rm .
Also, by construction, Fn is monotone in x and similarly
F (θ, x) ≤ F (θ, y) , x i ≤ yi , i = 1, . . . , m .(4.17)
We shall use these monotonicity properties together with th e following
lemma.
Lemma 4.7 (Johansson, [14]) . There exist constants C > 0 and n0 >
0 such that for any nonincreasing sequence {bn}∞
n=0 ⊂ [0, 1]
1 ≥ b0 ≥ b1 ≥ b2 ≥ b3 ≥ · · · ≥ 0,
and its exponential generating function
B(θ) = e−θ
∞∑
k=0
θk
k! · bk
we have for all n > n 0 the following inequalities:
B(n + 4
√
n ln n) − C
n2 ≤ bn ≤ B(n − 4
√
n ln n) + C
n2 .
This lemma implies that for all x ∈ Rm
F (n + 4
√
n ln n, x) − C
n2 ≤ Fn(x) ≤ F (n − 4
√
n ln n, x) + C
n2 .(4.18)
Set
¯
1 = (1 , . . . ,1) .
Theorem 5 asserts that
F
(
θ, 2θ
1
2 ¯
1 + θ
1
6 x
)
→ F (x), θ → +∞, x ∈ Rm,(4.19)
where F (x) is the corresponding distribution function for the Airy en -
semble. Note that F (x) is continuous.
Denote n± = n ± 4
√
n ln n. Then for i = 1, . . . , m
2n
1
2
± + n
1
6
± xi = 2n
1
2 + n
1
6 xi + O((ln n)1/ 2) .
Hence, for any ε > 0 and all suﬃciently large n we have
2n
1
2
+ + n
1
6
+ (xi − ε) ≤ 2n
1
2 + n
1
6 xi ≤ 2n
1
2
− + n
1
6
− (xi + ε) ,
ASYMPTOTICS OF PLANCHEREL MEASURES 35
for i = 1, . . . , m. By (4.17) this implies that
F
(
n+, 2n
1
2 ¯
1 + n
1
6 x
)
≥ F
(
n+, 2n
1
2
+ ¯
1 + n
1
6
+ (x − ε ¯
1)
)
F
(
n−, 2n
1
2 ¯
1 + n
1
6 x
)
≤ F
(
n−, 2n
1
2
− ¯
1 + n
1
6
− (x + ε ¯
1)
)
.
From this and (4.18) we obtain
F
(
n+, 2n
1
2
+ ¯
1 + n
1
6
+ (x − ε ¯
1)
)
− C
n2
≤ Fn
(
2n
1
2 ¯
1 + n
1
6 x
)
≤
F
(
n−, 2n
1
2
− ¯
1 + n
1
6
− (x + ε ¯
1)
)
+ C
n2 .
From this and (4.19) we conclude that
F (x − ε ¯
1) + o(1) ≤ Fn
(
2n
1
2 ¯
1 + n
1
6 x
)
≤ F (x + ε ¯
1) + o(1)
as n → ∞. Since ε > 0 is arbitrary and F (x) is continuous we obtain
Fn
(
2n
1
2 ¯
1 + n
1
6 x
)
→ F (x), n → ∞, x ∈ Rm,
which is the statement of Theorem 4.
Appendix A. General properties of determinantal point
processes
In this Appendix, we collected some necessary facts about de termi-
nantal point processes, their correlation functions, Fred holm determi-
nants, and convergence of trace class operators.
Let X be a countable set, let Conf( X) = 2 X be the set of subsets of
X and denote by Conf( X)0 ⊂ Conf(X) the set of ﬁnite subsets of X.
We call elements of Conf( X) conﬁgurations. Let L be a kernel on X,
that is, a function on X × X also viewed as a matrix of an operator in
H = ℓ2(X).
By a determinantal point process on X (in [10] such processes are
called fermion point processes) we mean a probability measu re on
Conf(X)0 such that
Prob(X) =
det
[
L(xi, xj)
]
xi∈X
det(1 + L) , X ∈ Conf(X)0 .
Here the determinant in the numerator is the usual determina nt of
linear algebra, whereas the determinant in the denominator is, in gen-
eral, a Fredholm determinant. Some suﬃcient conditions und er which
det(1 + L) makes sense are described in the following subsection.
36 A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
A.1. Fredholm determinants and determinantal processes. Let
H be a complex Hilbert space, L(H) be the algebra of bounded opera-
tors in H, and L1(H), L2(H) be the ideals of trace class and Hilbert–
Schmidt operators, respectively.
Assume we are given a splitting H = H+ ⊕ H−. According to this
splitting, write operators A ∈ L(H) in block form A =
[
