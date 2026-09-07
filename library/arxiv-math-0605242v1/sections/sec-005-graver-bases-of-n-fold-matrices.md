---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming Jesús A. De Loera∗ Raymond Hemmecke † Shmuel Onn ‡ Robert Weismantel §"
section_id: sec-005-graver-bases-of-n-fold-matrices
section_title: "Graver bases of n-fold matrices"
section_number: null
pages: 11-13
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
doc_brief: "N-Fold Integer Programming Jesús A. De Loera∗ Raymond Hemmecke † Shmuel Onn ‡ Robert Weismantel § — In this article we study a broad class of integer programming problem s in variable dimension."
---
Fix any pair of integer matrices A and B with the same number of columns, of dimensions r × q and
s × q, respectively. The n-fold matrix of the ordered pair A, B is the following ( s + nr) × nq matrix,
[A, B ](n) := ( 1n ⊗ B) ⊕ (In ⊗ A) =


B B B · · · B
A 0 0 · · · 0
0 A 0 · · · 0
... ... . . . ... ...
0 0 0 · · · A


.
With this, the generalized n-fold integer programming prob lem can be conveniently written as
min{cx : [ A, B ](n)x = b, x ∈ Nnq} .
The n-fold of a single matrix A, deﬁned in the introduction, is the special case A(n) = [A, I q](n) with
B = Iq the q × q identity, giving the regular (non-generalized) n-fold int eger programming problem.
We now discuss a recent result of [19] and its extension in [13 ] on the stabilization of Graver bases
of n-fold matrices. Consider vectors x = ( x1, . . . , x n) with xk ∈ Nq for k = 1 , . . . , n . The type of x is
the number |{k : xk ⁄= 0 }| of nonzero components xk ∈ Nq of x. The following result of [13] on the
stabilization of Graver bases of [ A, B ](n) extends the earlier result for B = Iq from [19].
Proposition 4.1 For every pair of integer matrices A ∈ Zr×q and B ∈ Zs×q, there exists a constant
g(A, B ) such that for all n, the Graver basis of [A, B ](n) consists of vectors of type at most g(A, B ).
The smallest constant g(A, B ) possible in the proposition is called the Graver complexity of A, B .
Using Proposition 4.1, we now show that G([A, B ](n)) can be computed in polynomial time.
Theorem 4.2 Fix any pair of integer matrices A ∈ Zr×q and B ∈ Zs×q. Then there is a polynomial
time algorithm that, given n, computes the Graver basis G([A, B ](n)) of the n-fold matrix [A, B ](n). In
particular, the cardinality and the bit size of G([A, B ](n)) are bounded by a polynomial function of n.
Proof. Let g := g(A, B ) be the Graver complexity of A, B and consider any n ≥ g. We show that the
Graver basis of [ A, B ](n) is the union of
( n
g
)
suitably embedded copies of the Graver basis of [ A, B ](g).
Consider any g indices 1 ≤ k1 < · · · < k g ≤ n and deﬁne a map φ k1,...,kg from Ngq to Nnq by sending
x = (x1, . . . , x g) to y = (y1, . . . , y n) deﬁned by ykt := xt for t = 1, . . . , g , and yk := 0 for all other k.
11
We claim that the Graver basis of [ A, B ](n) is the union of the images of the Graver basis of [ A, B ](g)
under the
( n
g
)
maps φ k1,...,kg for all 1 ≤ k1 < · · · < kg ≤ n, that is,
G([A, B ](n)) =
⋃
1≤k1<···<kg≤n
φ k1,...,kg (G([A, B ](g))) . (1)
To see this, recall ﬁrst that, by deﬁnition, the Graver basis of a matrix M is the set of all ⊑-minimal
nonzero dependencies on M (where a dependency on M is a vector x satisfying M x = 0). Thus,
if x = ( x1, . . . , x g) ∈ G ([A, B ](g)) then x is a ⊑-minimal nonzero dependency on [ A, B ](g), implying
that φ k1,...,kg (x) is a ⊑-minimal nonzero dependency on [ A, B ](n) and hence φ k1,...,kg (x) ∈ G ([A, B ](n)).
This establishes that the right-hand side of (1) is containe d in the left-hand side. Conversely, consider
any y ∈ G ([A, B ](n)). Then, by Proposition 4.1, the type of y is at most g, so there are indices
1 ≤ k1 < · · · < k g ≤ n such that all nonzero components of y are among those of the reduced vector
x := (yk1, . . . , y kg ), and therefore y = φ k1,...,kg(x). Now, y ∈ G ([A, B ](n)) implies that y is a ⊑-minimal
nonzero dependency on [ A, B ](n), and therefore x is a ⊑-minimal nonzero dependency on [ A, B ](g) and
hence x ∈ G ([A, B ](g)), showing that y ∈ φ k1,...,kg (G([A, B ](g))). This establishes that the left-hand side
of (1) is contained in the right-hand side. Thus, the Graver b asis of [ A, B ](n) is indeed given by (1).
Since A, B are ﬁxed and hence g = g(A, B ) is constant, the g-fold matrix [ A, B ](g) is also ﬁxed
and so the cardinality and bit size of its Graver basis G([A, B ](g)) are constant as well. It follows from
(1) that |G([A, B ](n))| ≤
( n
g
)
|G([A, B ](g))| = O(ng). Further, each element of G([A, B ](n)) is an nq-
dimensional vector φ k1,...,kg (x) obtained from some x ∈ G ([A, B ](g)) (of constant bit size) by appending
zero components, and therefore is of linear bit size O(n), showing that the bit size of the entire Graver
basis G([A, B ](n)) is O(ng+1). Finally, it is clear that the
( n
g
)
= O(ng) images φ k1,...,kg (G([A, B ](g)))
and their union G([A, B ](n)) can be computed in time polynomial in n, completing the proof. □
Example 4.3 Consider the matrices A = [1 1] and B = I2. The Graver complexity of the pair A, B
is g(A, B ) = 2. The 2-fold matrix and its Graver basis, consisting of tw o antipodal vectors only, are
[A, B ](2) = A(2) =


1 0 1 0
0 1 0 1
1 1 0 0
0 0 1 1


, G([A, B ](2)) = ±
(
1 −1 −1 1
)
.
By Theorem 4.2, the Graver basis of the 4-fold matrix [ A, B ](4) = A(4) can be computed by taking
12
the union of the images of the 6 =
( 4
2
)
maps φ k1,k2 : N2·2 − →N4·2 for 1 ≤ k1 < k 2 ≤ 4, and we obtain
[A, B ](4) =


1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 1 0 0 0 0 0 0
0 0 1 1 0 0 0 0
0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 1


, G([A, B ](4)) = ±


1 −1 −1 1 0 0 0 0
1 −1 0 0 −1 1 0 0
1 −1 0 0 0 0 −1 1
0 0 1 −1 −1 1 0 0
0 0 1 −1 0 0 −1 1
0 0 0 0 1 −1 −1 1


.
