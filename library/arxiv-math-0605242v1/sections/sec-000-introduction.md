---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming Jesús A. De Loera∗ Raymond Hemmecke † Shmuel Onn ‡ Robert Weismantel §"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
doc_brief: "N-Fold Integer Programming Jesús A. De Loera∗ Raymond Hemmecke † Shmuel Onn ‡ Robert Weismantel § — In this article we study a broad class of integer programming problem s in variable dimension."
---
The integer programming problem is the following discrete o ptimization problem, where N denotes the
set of nonnegative integers, A is an integer matrix and b, c are integer vectors of suitable dimensions:
min {cx : Ax = b, x ∈ Nq}.
It is well known to be generally NP-hard but polynomial time s olvable in ﬁxed dimension q, see [20].
In this article, motivated by applications to high-dimensi onal transportation problems and con-
tingency tables and by the recently discovered striking uni versality theorem for rational polytopes [6]
(see Section 2), we study the following class of integer prog ramming problems in variable dimension.
∗ Supported in part by NSF grant DMS-0309694, a 2003 UC-Davis C hancellor’s fellow award, and the Alexander von
Humboldt foundation.
† Supported in part by the European network ADONET 504438 and b y grant FOR 468 of the Deutsche Forschungs-
gemeinschaft.
‡ Supported in part by a grant from ISF - the Israel Science Foun dation, by the Technion President Fund, and by the
Jewish Communities of Germany Research Fund.
§ Supported in part by the European network ADONET 504438 and b y grant FOR 468 of the Deutsche Forschungs-
gemeinschaft.
1
The n-fold integer programming problem . Fix a p × q integer matrix A. Given positive integer n
and integer vectors b = (b0, b 1, . . . , b n) and c = (c1, . . . , c n), where b0 ∈ Zq, and bk ∈ Zp and ck ∈ Nq for
k = 1, . . . , n , ﬁnd a nonnegative integer vector x = (x1, . . . , x n), where xk ∈ Nq for k = 1, . . . , n , which
minimizes cx = ∑ n
k=1 ckxk subject to the equations ∑ n
k=1 xk = b0 and Axk = bk for k = 1, . . . , n .
The term “n-fold integer programming” refers to the problem being almost separable into n similar
programs min {ckx : Axk = bk, x k ∈ Nq} in ﬁxed dimension; however, the constraint ∑ n
k=1 xk = b0
binds these programs together, and the result is an integer p rogram in large variable dimension nq.
Let the n-fold matrix of A be the following ( q + np) × nq matrix, with Iq the q × q identity matrix:
A(n) := ( 1n ⊗ Iq) ⊕ (In ⊗ A) =


Iq Iq Iq · · · Iq
A 0 0 · · · 0
0 A 0 · · · 0
... ... . . . ... ...
0 0 0 · · · A


.
Then the n-fold integer programming problem can be convenie ntly written in matrix form as
min{cx : A(n)x = b, x ∈ Nnq} .
In this article we establish the following theorem. Natural ly, the input size is n plus the bit size of
the integer objective vector c ∈ Znq and the integer right-hand side vector b ∈ Zq+np.
Theorem 1.1 Fix any integer matrix A. Then there is a polynomial time algorithm that, given any
n and any integer vectors b and c, solves the corresponding n-fold integer programming prob lem.
The proof of this theorem involves two heavy ingredients. Fi rst, it makes use of the equivalence of the
linear optimization problem and the directed augmentation problem, recently introduced and studied
in [21]. Second, it uses recent results of [13] and [19] on the stabilization of certain Graver bases.
One important consequence of Theorem 1.1 is a polynomial tim e algorithm for the 3-way trans-
portation problem for long tables, settling its computatio nal complexity; see Section 2 for details.
Corollary 2.2 Fix any r, s . Then there is a polynomial time algorithm that, given l, integer objective
vector c, and integer line-sums ( ui,j), ( vi,k) and ( wj,k), solves the integer transportation problem
min{ cx : x ∈ Nr×s×l ,
∑
i
xi,j,k= wj,k,
∑
j
xi,j,k= vi,k,
∑
k
xi,j,k= ui,j } .
2
The n-fold integer programming problem and theorem can be ge neralized as follows.
Generalized n-fold integer programming . Fix integer matrices A, B of sizes r × q and s × q,
respectively. Given positive integer n and integer vectors b = (b0, b 1, . . . , b n) and c = (c1, . . . , c n), with
b0 ∈ Zs, and bk ∈ Zr and ck ∈ Nq for k = 1, . . . , n , ﬁnd x = (x1, . . . , x n) with xk ∈ Nq for k = 1, . . . , n ,
which minimizes cx = ∑ n
k=1 ckxk subject to ∑ n
k=1 Bxk = b0 and Axk = bk for k = 1, . . . , n .
We have the following more general result, from which Theore m 1.1 is deduced in the case B = Iq.
Theorem 1.2 Fix any pair of integer matrices A, B of compatible sizes. Then there is a polynomial
time algorithm that solves the generalized n-fold integer p rogramming problem on any input n, b, c .
The article is organized as follows. In Section 2 we discuss a pplications of Theorem 1.1 to multiway
transportation problems and to some packing problems, as fo llows. In 2.1 we obtain the aforementioned
Corollary 2.2 which provides a polynomial time solution to 3 -way integer transportation problems for
long tables, contrasting the recent universality theorem o f [6] for slim tables. We also extend this
result to d-way transportation problems for long tables of any dimensi on (Corollary 2.4). In 2.2 we
