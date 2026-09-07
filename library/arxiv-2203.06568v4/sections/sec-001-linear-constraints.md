---
doc_id: arxiv-2203.06568v4
doc_title: "Semidefinite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-001-linear-constraints
section_title: "linear constraints"
section_number: null
pages: 8-10
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
doc_brief: "Semidefinite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
(i) x0,0
0,0,0,0 = 1;
(ii) 0 ≤ xt,t′
i,j,i′,j′ ≤ x0,0
i,0,i′,0;
(iii) x0,0
i,0,i′,0 + x0,0
0,j,0,j′ ≤ 1 + xt,t′
i,j,i′,j′ ;
(iv) xt,t′
i,j,i′,j′ = xc,c′
a,b,a′,b′ if ((i, i′), (j, j′), (i + j − 2t, i′ + j′ − 2t′));
is a permutation of ((a, a′), (b, b′), (a + b − 2c, a′ + b′ − 2c′)),
(v) xt,t′
i,j,i′,j′ = 0 if {i + i′, j + j′, (i + i′) + (j + j′) − 2(t + t′)} ∩ {1, . . . , d− 1} ⁄= ∅.
(14)
Constraints (i) and (iv) come from the deﬁnition of xt,t′
i,j,i′,j′ . Constraints (ii) and (iii) are because of the positive semi deﬁ-
niteness of R and R′. Constraint (iv) is the requirement of the minimum distance .
The split distance distribution of C with respect to the partition {T1, T2} is {Ai,j}, where
Ai,j = 1
|C| |{(a, b) ∈ C × C | |a∆ b ∩ T1| = i, |a∆ b ∩ T2| = j}|.
It has been shown that generalized Delsarte’s inequalities on Ai,j hold [Sim95].
Corollary 9. [Sim95, Generalized Delsarte’s inequalities]
∑
i,j
Ai,jK n1
p (i)K n2
q (j) ≥ 0, (15)
for p = 0, . . . , n1 and q = 0, . . . , n2, where
K n
k (x) =
k∑
y=0
(−1)y
(x
y
)(n − x
k − y
)
is the binary Krawchuk polynomial.
We can show that the generalized Delsarte’s inequalities on {Ai,j} can be derived from the positive semideﬁniteness of Rs
and R′
s in Proposition 7.
Lemma 10. If Rs and R′
s are positive semideﬁnite, then (15) holds.
Proof. Deﬁne a matrix
Ds = Rs + 2n − |C|
|C| R′
s =
∑
i,j,i′,j′,t,t′
x0,0
i+j−2t,0,i′ +j′−2t′,0M t,t′
i,j,i′,j′ ,
which is a nonnegative linear combination of positive semid eﬁnite matrices Rs and R′
s, and hence is positive semideﬁnite. We
can rewrite Ds as
Ds =
∑
k,k′
x0,0
k,0,k′,0Mk,k′ ,
where
(Mk,k′ )X,Y =
{
1, if |X∆ Y ∩ T1| = k, |X∆ Y ∩ T2| = k′;
0, otherwise.
Deﬁne matrices Dm
a for 0 ≤ a, m ≤ n with entries
(Dm
a )X,Y =
{
1, if |X∆ Y | = a;
0, otherwise,
for indexes X, Y in the power set of {1, . . . , m}. Notice that {Dm
a } forms a basis for the Bose–Mesner algebra of the
Hamming scheme with length m. Using the isomorphism in Lemma 4, one ﬁnds that Mk,k′ is isomorphic to Dn1
k ⊗ Dn2
k′ . By
[Del73], we learn that Krawchuk polynomials K m
a (p) are eigenvalues of the matrices {Dm
a } for 0 ≤ p ≤ m and, moreover, the
matrices {Mk,k′} are commutative. Consequently, to diagonalize Ds, we simply have to diagonalize Mk,k′ and the semideﬁnite
conditions become ∑
k,k′
x0,0
k,0,k′,0K n1
k (p)K n2
k′ (q) ≥ 0, (16)
for p ∈ {0, . . . , n1} and q ∈ {0, . . . , n2}. Recall that the Krawchuk polynomial obeys the following sy mmetric relation [MS77]:
(m
a
)
K m
b (a) =
(m
b
)
K m
a (b).
9
Thus the inequality (16) becomes
∑
k,k′
(n1
k
)(n2
k′
)
x0,0
k,0,k′,0
(n1
p
)(n2
q
)
K n1
k (p)K n2
k′ (q) ≥ 0,
which implies the result.
Let Nk be the collection of codes S ⊂ P with minimum distance at least d and |S| ≤ k. Schrijver’s SDP can be generalized
by considering the k-points relation of codewords. The generalized version is a s follows [GMS12].
Proposition 11. [GMS12, Generalized SDP bound] For S ∈ N k, deﬁne
N (S) = {S′ ⊂ P : S ⊂ S′, |S| + 2|S′ \ S| ≤ k}.
Let x = {xi}i∈Nk ⊂ R be a set of non-negative numbers. Deﬁne the |N (S)| × |N (S)| matrix indexed by N (S) as
(MS(x))S′,S′′ =
{
xS′∪S′′, if S′ ∪ S′′ has minimum distance at least d;
0, otherwise,
for S′, S′′ ∈ N (S). Then,
A(n, d) ≤ Ak(n, d) = max
{∑
i∈P
x{i} : x∅ = 1, xS ≥ 0 and MS(x) is positive semideﬁnite for each S ∈ N k
}
. (17)
It can be shown that the generalized Schrijver’s SDP constra ints with k = 4 induces our positive semideﬁnite constraint on
Rs.
Proposition 12. The positive semideﬁnite constraints in the quadruple semi deﬁnite program in (17) imply the positive
semideﬁniteness of Rs.
Proof. Let C be a code of length n and minimum distance d. Consider S = {∅, u} ∈ N 4, where u has 1 in the ﬁrst n1
positions and 0 in the other n2 positions, which is a subset of C. Let x be deﬁned as xi = 1 if i ⊂ C and xi = 0 for the other
cases. Observe that there is an one-to-one correspondence b etween N (S) = {S ∪ {v} : v ∈ P} and P by sending S ∪ {v} to
v. Thus, MS(x) can be indexed by P and
(MS(x))v,w =
{
1, if {v, w} ⊂ C;
0, otherwise.
Notice that MS(x) = χC (χC )T is positive semideﬁnite and
Ru
s = 1
|Π us |
∑
(π1,π2)∈Π us
χ(π1,π2)(C)(χ(π1,π2)(C))T .
We observe that each χ(π1,π2)(C)(χ(π1,π2)(C))T is similar to MS(x) = χC (χC )T by changing the order of the basis. Thus,
Ru
s is semideﬁnite.
IV. S EMIDEFINITE PROGRAM
In this section, we provide an SDP that gives an upper bound on the size of an (n, d) code C ⊂ P . We include the known
linear constraints in the literature, which are critical in the SDP . We observe that an SDP with semideﬁnite constraints based
on quadruple distances [GMS12] does not improve the upper bo unds of A(18, 4) and A(19, 4). In fact, the bounds obtained
with only Schrijver’s semideﬁnite constraints are even wor se than the bounds with linear constraints [Del73], [Bes80] in some
cases. For instance, A(18, 4) ≤ 6552 can be obtained by certain linear constraints, while the SDP gives us an upper bound of
6553.
A. linear constraints
The distance distribution Aj of C in (1) can be represented in terms of xt,t′
i,i′,j,j′ as
Aj =
∑
i+i′=j
(n1
i
)(n2
i′
)
x0,0
i,0,i′,0.
Furthermore, the propagation rule A(n − 1, 2e − 1) = A(n, 2e) [MS77] implies that we need to consider only even distance j.
10
Lemma 13. [Bes80, Lemma 7] n∑
i=0
(n − i
k
)
Ai ≤
(n
k
)
A(n − k, d). (18)
Lemma 14. [MEL02, Theorem 9]
An− d
2
+
⌊ 2n
d
⌋ ∑
i<⌊ d
2 ⌋
An−i ≤
⌊ 2n
d
⌋
. (19)
Our SDP also beneﬁts from bounds on A(n, d, w), the maximum size of a length- n code with minimum distance d and
constant weight w.
Lemma 15. [Bes80, Lemma 5] Let P = A(n − 1, d, 1
2 d + 1), Q = A(n − 1
2 d, d, 1
2 d + 1), R = A(n − 1
2 d + 2, d, 1
2 d + 2), then
( 1
2 d + 2)An− 1
2 d−2 + 1
2 d(P − Q)An− 1
2 d + (nP − ( 1
2 d + 2)R)An− 1
2 d+2 + nP
n∑
i=n− 1
2 d+3
Ai ≤ nP. (20)
Lemma 16. [MEL02, Theorem 10] For i = 1, . . . , d
2 − 1,
An− d
2 −i+(A(n, d, d
2 + i) − A(n − d
2 + i, d, d
2 + i))An− d
2 +i + A(n, d, d
2 + i)
∑
j>i
An− d
2 +j ≤ A(n, d, d
2 + i). (21)
Lemma 17. [Sch05, (25)] For i = 0, . . . , n,
Ai ≤ A(n, d, i). (22)
We also have additional linear constraints from doubly cons tant-weight codes. Let T (w1, t1, w2, t2, d) be the maximum
possible size of a doubly constant-weight code, which is a (t1 + t2, d, w1 + w2) constant-weight code such that every codeword
has exactly w1 and w2 ones on the ﬁrst t1 and next t2 coordinates, respectively.
Lemma 18. [KT13, Theorem 3] For i, j, t ∈ {0, . . . , n}, we have
xt
i,j ≤ T (t, i, j − t, n − i, d)(i
t
)(n−i
j−t
) x0
i,0. (23)
B. Semideﬁnite program for binary codes
Collecting all the mentioned linear and semideﬁnite constr aints, we have the following SDP on A(n, d) with variables
xt,t′
i,j,i′,j′ ∈ C:
maximize
n∑
a=0
∑
i+i′=a
(n1
i
)(n2
i′
)
x0,0
i,0,i′,0.
subject to positive semideﬁniteness of (2), (3), (12), (13) (24)
(4), (9), (10), (14)
(18), (19), (20), (21), (22), (23).
As mentioned in the previous section, the generalized Delsa rte’s inequalities (15) are implicitly included in the SDP .
