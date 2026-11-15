---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-019-appendix-c-a-combinatorial-counting-of-structure
section_title: "Appendix C. A combinatorial counting of structures"
section_number: null
pages: 20-22
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
In this section we consider structures on a set [k] = {1, . . ., k}, and their combinatorial countings.
Deﬁnition C.1. Let k be a positive integer. A k-structure is a pair S = (A, B) such that
• A = (A1, . . . , Al), B = (B1, . . . , Bl) for some l, Ai, Bi ⊂[k], Ai̸ = ∅for all i,
• A is a partition of {1, . . . , k} such that for every i < j, x ∈Ai, y ∈Aj we have x < y.
• Bi ⊂∪j<iAj. In particular B1 = ∅.
• B is monotonic. That is, if x ∈Bj ∩Ai then for each j ≥j′ > i, x ∈Bj′,
Lemma C.2. The number of k-structures S such that |Ai| = ai and |Bi| = bi for i = 1, . . . , l is
lY
i=2
ai−1 + bi−1
bi

.
Proof. Bi is an arbitrary subset of Ai−1 ∪Bi−1 of bi elements.
□
Deﬁnition C.3. Let S be a k-structure, v ∈{0, . . ., n −1}{1,...,k} and i ∈Ax for some x ≤l.
• We let |S| = (a, b), where a = (|A1|, . . . , |Al|) and b = (|B1|, . . . , |Bl|).
• We let m(|S|, i) be the number of j ∈Ax ∪Bx such that j < i. Note that m(|S|, i) equals bi plus
the number of elements of Ax that are smaller than i and hence it depends only on |S|.
• We denote by def1(S, v, i) the number of j ∈Ax ∪Bx such that j < i and vj < vi,
• we denote by def2(S, v, i) the number of j ∈Bd(i)+1 such that vj < vi; d(i) is the minimum index so
that d(i) ≥i and i /∈Bd(i)+1.
Deﬁnition C.4. Let S be a k-structure. We let V (S, n) = {v ∈{0, . . ., n −1}{1,...,k}; if {i, j} ⊂Am ∪Bm
for some m then vi̸ = vj}.
The following Theorem follows by comparing the deﬁnitions.
Theorem 9. Let f be a ﬂow on arc-graph GK.
Recall that fr(v) = P f(e) over all red edges of GK
terminating in vertex v of GK, and fb(v) is deﬁned analogously for the blue edges. We consider set Fr
linearly ordered, ﬁrst by the terminal vertices, and then by ordering ≺which induces a linear ordering on
the set ∪F(e), over red edges e entering the same vertex (see Deﬁnition 6.5).
There is a natural bijection between ACn(f) and the set of all pairs (S, v) where S is an |Fr|-structure,
|S| = ((fr(1), . . . , fr(r))(fb(1), . . . , fb(r))) and v ∈V (S, n).
Theorem 10.
X
S:|S|=(a,b)
X
v∈V (S,n)
k
Y
i=1
tvi−def1(S,v,i)−def2(S,v,i) =
k
Y
i=1
(n −m(i))t
l−1
Y
i=1
ai + bi
bi+1

t−1.
In the proof we will use the following proposition.
Proposition C.5. Let S be a k-structure. Then
X
v∈V (S,n)
k
Y
i=1
tvi−def1(S,v,i) =
k
Y
i=1
(n −m(|S|, i))t.
Proof. Use induction on k. The inductive step follows from the following claim:
Claim: Let m(k) < n and ﬁx diﬀerent numbers v1, . . . , vm(k) between 0 and n −1. Then
•
X
vk:vk̸=vi,i≤m(k)
tvk−def1(v,k) = A −B + C,
where A = P
vk:vk̸=vi,i≤m(k) tvk, B = Pm(k)
i=1 tn−i, and C = Pm(k)
i=1 tvi.
20
• A + C = P
0≤z≤n−1 tz and A −B + C = 1−tn−m(k)
1−t
.
Note that the second part is simply true.
Let v′
1 < · · · < v′
m(k) be a reordering of v1, . . . , vm(k). We may write v′
1 = n−i1, . . . , v′
m(k) = n−im(k), 1 ≤
im(k) < · · · < i1. The LHS becomes
A −tn−i1+1 −· · · −tn−i2−1 −tn−i2+1 −· · · −tn−im(k)−1 −tn−im(k)+1 −· · · −tn−1
+tn−i1 + · · · + tn−i2−2 + tn−i2−1 + · · · + tn−m(k)−1.
This equals to the RHS of the equality we wanted to show.
The Proposition simply follows from the
Claim.
□
Proof. (of Theorem 10)
We let a′
i = P
j≤i ai.
X
S:|S|=(a,b)
X
v∈V (S,n)
k
Y
i=1
tvi−def1(S,v,i)−def2(S,v,i) =
X
B2⊂A1
X
v1,...,va1
a1
Y
i=1
tvi−def1(v,i)−def2(B2,v,i) ×
X
B3,...,Bl
X
va1+1,...,vk
k
Y
i=a1+1
tvi−def1(v,i)−def2(B3,...,Bl,v,i) =
X
v1,...,va1
a1
Y
i=1
tvi−def1(v,i)
X
B2⊂A1
a1
Y
i=1
t−def2(B2,v,i) ×
X
B3,...,Bl
X
va1+1,...,vk
k
Y
i=a1+1
tvi−def1(v,i)−def2(B3,...,Bl,v,i) =
X
v1,...,va1
a1
Y
i=1
tvi−def1(v,i)
X
B2⊂A1
a1
Y
i=1
t−def2(B2,v,i) × · · · ×
X
va′
l−2+1,...,va′
l−1
a′
l−1
Y
i=a′
l−2+1
tvi−def1(v,i) X
Bl
a′
l−1
Y
i=a′
l−2+1
t−def2(Bl,v,i) ×
X
va′
l−1+1,...,vk
k
Y
i=a′
l−1+1
tvi−def1(v,i).
The last sum may be expressed using Proposition C.5, and we get
X
v1,...,va1
a1
Y
i=1
tvi−def1(v,i)
X
B2⊂A1
a1
Y
i=1
t−def2(B2,v,i) × · · · ×
X
va′
l−2+1,...,va′
l−1
a′
l−1
Y
i=a′
l−2+1
tvi−def1(v,i) X
Bl
a′
l−1
Y
i=a′
l−2+1
t−def2(Bl,v,i) ×
k
Y
i=a′
l−1+1
(n −m(i))t =
k
Y
i=a′
l−1+1
(n −m(i))t
X
v1,...,va1
a1
Y
i=1
tvi−def1(v,i)
X
B2⊂A1
a1
Y
i=1
t−def2(B2,v,i) × · · · ×
a′
l−1
Y
i=a′
l−2+1
(n −m(i))t
al−1 + bl−1
bl

t−1
=
k
Y
i=1
(n −m(i))t
l−1
Y
i=1
ai + bi
bi+1

t−1.
□
21
