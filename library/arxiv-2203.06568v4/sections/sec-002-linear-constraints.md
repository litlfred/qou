---
doc_id: arxiv-2203.06568v4
doc_title: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-002-linear-constraints
section_title: "linear constraints"
section_number: null
pages: 8-9
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
toc_source: outline
---
(i)
x0,0
0,0,0,0 = 1;
(ii)
0 ≤xt,t′
i,j,i′,j′ ≤x0,0
i,0,i′,0;
(iii)
x0,0
i,0,i′,0 + x0,0
0,j,0,j′ ≤1 + xt,t′
i,j,i′,j′;
(iv)
xt,t′
i,j,i′,j′ = xc,c′
a,b,a′,b′ if ((i, i′), (j, j′), (i + j −2t, i′ + j′ −2t′));
is a permutation of ((a, a′), (b, b′), (a + b −2c, a′ + b′ −2c′)),
(v)
xt,t′
i,j,i′,j′ = 0 if {i + i′, j + j′, (i + i′) + (j + j′) −2(t + t′)} ∩{1, . . ., d −1}̸ = ∅.
(14)
Constraints (i) and (iv) come from the deﬁnition of xt,t′
i,j,i′,j′. Constraints (ii) and (iii) are because of the positive semideﬁ-
niteness of R and R′. Constraint (iv) is the requirement of the minimum distance.
The split distance distribution of C with respect to the partition {T1, T2} is {Ai,j}, where
Ai,j =
1
|C||{(a, b) ∈C × C | |a∆b ∩T1| = i, |a∆b ∩T2| = j}|.
It has been shown that generalized Delsarte’s inequalities on Ai,j hold [Sim95].
Corollary 9.
[Sim95, Generalized Delsarte’s inequalities]
X
i,j
Ai,jKn1
p (i)Kn2
q (j) ≥0,
(15)
for p = 0, . . . , n1 and q = 0, . . . , n2, where
Kn
k (x) =
k
X
y=0
(−1)y
x
y
n −x
k −y

is the binary Krawchuk polynomial.
We can show that the generalized Delsarte’s inequalities on {Ai,j} can be derived from the positive semideﬁniteness of Rs
and R′
s in Proposition 7.
Lemma 10. If Rs and R′
s are positive semideﬁnite, then (15) holds.
Proof. Deﬁne a matrix
Ds = Rs + 2n −|C|
|C|
R′
s =
X
i,j,i′,j′,t,t′
x0,0
i+j−2t,0,i′+j′−2t′,0M t,t′
i,j,i′,j′,
which is a nonnegative linear combination of positive semideﬁnite matrices Rs and R′
s, and hence is positive semideﬁnite. We
can rewrite Ds as
Ds =
X
k,k′
x0,0
k,0,k′,0Mk,k′,
where
(Mk,k′)X,Y =
(
1, if |X∆Y ∩T1| = k, |X∆Y ∩T2| = k′;
0, otherwise.
Deﬁne matrices Dm
a for 0 ≤a, m ≤n with entries
(Dm
a )X,Y =
(
1, if |X∆Y | = a;
0, otherwise,
for indexes X, Y in the power set of {1, . . ., m}. Notice that {Dm
a } forms a basis for the Bose–Mesner algebra of the
Hamming scheme with length m. Using the isomorphism in Lemma 4, one ﬁnds that Mk,k′ is isomorphic to Dn1
k ⊗Dn2
k′ . By
[Del73], we learn that Krawchuk polynomials Km
a (p) are eigenvalues of the matrices {Dm
a } for 0 ≤p ≤m and, moreover, the
matrices {Mk,k′} are commutative. Consequently, to diagonalize Ds, we simply have to diagonalize Mk,k′ and the semideﬁnite
conditions become
X
k,k′
x0,0
k,0,k′,0Kn1
k (p)Kn2
k′ (q) ≥0,
(16)
for p ∈{0, . . . , n1} and q ∈{0, . . ., n2}. Recall that the Krawchuk polynomial obeys the following symmetric relation [MS77]:
m
a

Km
b (a) =
m
b

Km
a (b).
9
Thus the inequality (16) becomes
X
k,k′
n1
k
n2
k′

x0,0
k,0,k′,0
n1
p
n2
q

Kn1
k (p)Kn2
k′ (q) ≥0,
which implies the result.
Let Nk be the collection of codes S ⊂P with minimum distance at least d and |S| ≤k. Schrijver’s SDP can be generalized
by considering the k-points relation of codewords. The generalized version is as follows [GMS12].
Proposition 11.
[GMS12, Generalized SDP bound] For S ∈Nk, deﬁne
N(S) = {S′ ⊂P : S ⊂S′, |S| + 2|S′ \ S| ≤k}.
Let x = {xi}i∈Nk ⊂R be a set of non-negative numbers. Deﬁne the |N(S)| × |N(S)| matrix indexed by N(S) as
(MS(x))S′,S′′ =
(
xS′∪S′′,
if S′ ∪S′′ has minimum distance at least d;
0,
otherwise,
for S′, S′′ ∈N(S). Then,
A(n, d) ≤Ak(n, d) = max
(X
i∈P
x{i} : x∅= 1, xS ≥0 and MS(x) is positive semideﬁnite for each S ∈Nk
)
.
(17)
It can be shown that the generalized Schrijver’s SDP constraints with k = 4 induces our positive semideﬁnite constraint on
Rs.
