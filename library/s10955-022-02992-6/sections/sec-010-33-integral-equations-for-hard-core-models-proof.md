---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions Sabine Jansen 1,2 · Leonid Kolesnikov 1 © The Author(s) 2022"
section_id: sec-010-33-integral-equations-for-hard-core-models-proof
section_title: "Integral Equations for Hard-Core Models: Proof of Theorem 2.6"
section_number: 3.3
pages: 19-22
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions Sabine Jansen 1,2 · Leonid Kolesnikov 1 © The Author(s) 2022 — We prove a new convergence condition for the activity expansion of"
---
In this section we specialize to hard-core systems in the continuum as in Sect. 2.3 and
use capital letters for objects X ∈ X.L e t Dred
n,n+k ⊂ Dn,n+k be the collection of graphs
G ∈ Dn,n+k that have no edges linking any two root vertices i, j ∈{ 1,..., n}.D e ﬁ n e
ψred
n,n+k in a similar way as ψn,n+k but with summation over graphs in Dred
n,n+k . It is not
difﬁcult to check that
ψn,n+k(X1,..., Xn+k) =
∏
1≤i< j≤n
(
1 + f (Xi , X j )
)
ψred
n,n+k(X1,..., Xn+k).
The reduced functions ψred
n,n+k satisfy recurrence relations similar to Lemma 3.5.D e ﬁ n e
g(X1; X2,..., Xn; Y1,..., Yk) :=
k∏
j=1
f (X1, Yj )
∏
1≤i< j≤k
(
1 + f (Yi , Yj )
)
∏
2≤i≤n
1≤ j≤k
(
1 + f (Xi , Yj )
)
. (3.6)
123
33 Page 20 of 47 S. Jansen, L. Kolesnikov
Remember the indicator I from (2.16) and notice
g(X1; X2,..., Xn; Y1,..., Yk) = (−1)k I(X1; X2 ∪···∪ Xn; Y1,..., Yk). (3.7)
Lemma 3.7 For all k, n ∈ N, we have
ψred
n,n+k(X1,..., Xn, Y1,..., Yk)
=
∑
L⊂[k]
g
(
Xs; X′
2,..., X′
n;(Yj )j∈L
)
ψred
n−1+𝓁,n−1+k
(
X′
2,..., X′
n,( Yj )j∈L,( Yj )j∈[k]\L
)
.
The proof is based on combinatorial considerations similar to the proof of Lemma 4.1 in
[14], we leave the details to the reader. The lemma holds true for arbitrary subsets of Rd ,t h e
Xi ’s andYj ’s need not be in X. That applies to our next result as well.
Lemma 3.8 For all k, n ∈ N, we have
ψred
n,n+k(X1,..., Xn, Y1,..., Yk) = ϕT
1+k(X1 ∪···∪ Xn, Y1,..., Yk).
Proof Revisiting the proof of Lemma 3.4, we see that
ψred
n,n+k(X1,..., Xn, Y1,..., Yk)
=
∑
{V1,...,Vr }
r∏
𝓁=1
( ∏
1≤i≤n,
j∈V𝓁
(
1 + f (Xi , Yj )
)
− 1
)
ϕT
|V𝓁|
(
(Yj )j∈V𝓁
)
, (3.8)
where the sum runs over all set partitions{V1,..., Vr } of non-root vertices{n+1,..., n+k}.
For hard-core interactions, the term in parentheses is equal to minus the indicator that D :=
X1 ∪···∪ Xn is intersected by at least one Y j , j ∈ V𝓁. Thus
ψred
n,n+k(X1,..., Xn, Y1,..., Yk) =
∑
{V1,...,Vr }
r∏
𝓁=1
(
−1l{∃ j∈V𝓁: Y j ∩D⁄=∅}
)
ϕT
|V𝓁|
(
(Yj )j∈V𝓁
)
.
Using again (3.8), we deduce
ψred
n,n+k(X1,..., Xn, Y1,..., Yk) = ψ1,1+k(D, Y1,..., Yk) = ϕT
1+k(D, Y1,..., Yk).
⊓⊔
Lemma 3.9 Let k ∈ N and let D0, D1 be two disjoint subsets of Rd , with D0 ⁄= ∅.T h e n
ϕT
1+k(D0 ∪ D1, Y1,..., Yk)
=
∑
L⊂[k]
(−1)𝓁I
(
D0; D1;(Yi )i∈L
)
ϕT
1+k−𝓁
(
D1 ∪
(⋃
i∈L
Yi
)
,( Yj )j∈[k]\L
)
,
where the sum is taken over all subsets L ⊂[ k] and 𝓁denotes the cardinality of L.
Proof The claim of the lemma follows from Eq. ( 3.7), Lemmas 3.7 and 3.8. ⊓⊔
For D ∈ Dε with E1,..., En ∈ Eε and C(D) ={ E1,..., En},l e t
˜T(D; z) := 1 +
∞∑
k=1
1
k!
∫
Xk
⏐⏐ϕT
1+k(D, Y1,..., Yk)
⏐⏐λk
z (dY),
123
Cluster Expansions: Necessary... Page 21 of 47 33
˜T1(D; z) := δn,1({E1,..., En}),a n df o rN ≥ 2,
˜TN
(
D; z
)
:= 1{n≤N} +
N−n∑
k=1
1
k!
∫
Xk
1l{n+∑ k
i=1 |C(Yi )|≤N}
⏐⏐ϕT
1+k(D, Y1,..., Yk)
⏐⏐λk
z (dY).
Although the value of ˜T(D; z) (if the series converges) does not depend on the choice
of the chopping map, notice that the value of ˜TN (D; z) clearly does depend on C(D) =
{E1,..., En} and not only on E1 ∪ ... ∪ En — due to the constraint on the number of
snippets.
A selection rule is a map s from collections of disjoint snippets Dε to Eε such that
s({E1,..., En}) ∈{ E1,..., En},
i.e., s(·) selects one of the snippets. We use the suggestive but somewhat abusive notation Es
for the selected snippet, and let E′
2,..., E′
n be any enumeration of the remaining snippets. If
ξ(·) is a function fromDε to R+ that satisﬁes the measurability assumption from Theorem2.6,
deﬁne a new function ˜κs
z ξ (possibly assuming the value “∞”) by setting
(˜κs
z ξ)
(
D
)
:= 1l{n≥2} ξ
(
E′
2 ∪ ... ∪ E′
n)
+
∞∑
k=1
1
k!
∫
Xk
I(Es; E′
2 ∪···∪ E′
n; Y1,..., Yk)ξ
(
E′
2 ∪ ... E′
n ∪ Y1 ∪ ... ∪ Yk
)
λk
z (dY)
(3.9)
for D ∈ Dε with E1,..., En ∈ Eε and C(D) ={ E1,..., En}. Furthermore, let e(D) :=
δn,1({E1,..., En}) be the indicator that D is a single snippet.
Let z be a non-negative activity such that for every non-empty D ∈ Dϵ the series ˜T
(
D; z
)
converges absolutely. Notice that the topology induced by the Hausdorff distance is equiv-
alent to the myopic topology and the map K ′∋ F ↦→ 1l{F∈K ′| F∩B⁄=∅}(F) =− f (F, B)
is measurable with respect to the myopic topology for all compact subsets B (see [ 21]).
Measurability of K ′ ∋ F ↦→ ˜T(D ∪ F; z) for every D ∈ K ′can be concluded, e.g., by
representing the series ˜T(D ∪ F; z) as in Eq. ( 2.15). Since ˜T(D ∪ F; z) = ˜T(D ∪ F; z) for
every D ∈ Dε, its topological closure D in Rd and every F ∈ K ′(by our assumptions that
the boundaries of snippets are λ-null set), the measurability of K ′∋ F ↦→ ˜T(D ∪ F; z) for
all D ∈ Dε follows.
The next result is an analogue of Proposition 3.6.
Proposition 3.10 We have
˜T
(
·; z
)
= e(·) +˜κs
z ˜T(·; z).
Moreover ˜T1(·; z) = e(·) and for N ≥ 1
˜TN+1
(
·; z
)
= e(·) + (˜κs
z ˜TN )
(
·; z
)
.
The proposition follows from Lemma3.9 by arguments similar to the proof of Proposition3.6,
therefore the proof is omitted.
Proof of Theorem 2.6 To show the implication (ii) ⇒ (i) suppose that T(D; z) is absolutely
convergent and thus ˜T(D; z) is convergent for all non-empty D ∈ Dε. Moreover, ˜T(D; z)
is uniformly bounded from below by 1 and does not depend on the choice of the chopping
map C.W es e t
a(D) := log ˜T(D; z) ≥ 0
123
33 Page 22 of 47 S. Jansen, L. Kolesnikov
for non-empty D ∈ Dε and a(∅) := 0. Furthermore, for D ∈ Dε with E1,..., Em ∈ Eε and
C(D) ={ E1,..., Em},l e t Es ∈ Eε be given by Es({E1,...,Em}) for some selection rule s(·)
and set D′:= D\Es . Exploiting the ﬁxed point equation for ˜T(·; z) from Proposition 3.10,
we get
ea(D′) +
∞∑
k=1
1
k!
∫
Xk
I(Es; D′; Y1,..., Yk)ea(D′∪Y1∪···∪Yk)λk
z (dY) ≤ ea(Es∪D′).
Item (i) of Theorem 2.6 follows upon multiplication with exp(−a(D′)) on both sides (in fact,
we have shown that the inequality from item (i) holds for every choice of s ∈{ 1,..., m}).
The implication (i) ⇒ (ii) follows from Proposition 3.10 by an induction over N similar to
the proof of Theorem 2.1 on p. 20. Indeed, check that for the induction step it is sufﬁcient
that the corresponding system of Kirkwood–Salsburg inequalities holds for all ﬁnite disjoint
unions of snippets (for any choice of the chopping map C, the snippet-size ε> 0a n dt h e
selection rule s). Bound (2.17) is then established using the triangle inequality, the alternating
sign property, and Eq. ( 2.15). ⊓⊔
