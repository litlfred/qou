---
doc_id: arxiv-math-0602138v1
doc_title: "Non-Commutative Formal Groups in Positive Characteristic"
section_id: sec-000-poisson-algebras-with-internal-symmetry
section_title: "Poisson Algebras with Internal Symmetry"
section_number: null
pages: 2-12
source_pdf: 0602138v1.pdf
source_sha256: ed9ade66a774c93e
toc_source: outline
doc_brief: "Non-Commutative Formal Groups in Positive Characteristic — We describe geometric non-commutative formal groups in ter ms of a ge- ometric commutative formal group with a Poisson structure o n its"
---
In this section, we generalize the algebraic relationship as indicated in (Eqn. 1)
for a Lie algebra g over R. Choosing any R-module basis g = R⟨Xi⟩i∈I , one
can view Sg as the tensor product of the one dimensional algebras S{Xi}. It
is from this vantage point that we wish to generalize. We will be looking a t S,
a commutative algebra, which has a ﬁxed identiﬁcation as the tensor product
S = ⨂
i∈I Ai of commutative sub-algebras Ai for i in some indexing set I.
We then desire a non-commutative algebra U for which there is a PBW-type
isomorphism between S and U , and an algebra T for which both U and S are
2
quotients by appropriate commutator relations:
T
S ∼−
PBW
✲✛ U.
✲
Speciﬁcally, we desire that S be the quotient of T by ideal of relations generated
by f g − gf for f, g ∈ T . We recall that a Poisson structure on an algebra A is
a skew-symmetric bi-derivation π which satisﬁes the Jacobi identity.
Deﬁnition 1.1.
1.1.1. Let I be an indexing set and for each i ﬁx a commutative algebra Ai. We
deﬁne the splay of the Ai to be the following diagram T in the category
of algebras:
Ai
⊂ ιi✲ ∐
i∈I
Ai.
We call T := ∐
i Ai, the co-product of the Ai, the splay algebra of T
and we call the Ai the coordinate algebras of T .
1.1.2. Let T (resp. T
′
) be a splay with coordinate algebras Ai for i ∈ I (resp.
Bj for j ∈ J). A morphism of splays T
Φ✲ T
′
is an algebra morphism
T
Φ✲ T ′ of the respective splay algebras such that if for every i ∈ I
there is some ji ∈ J and some Ai
Φ ji✲ Bj such that Φ is the map induced
from the UMP of the co-product T as follows:
Ai
⊂
ιi✲ ∐
Ai
Bji
Φ ji ❄
∐
i
Bj
ιji ❄✛
∃!
1.1.3. Let π be a Poisson structure on an algebra A, and suppose that the
Ai are sub-algebras. Then we say that π has internal symmetry (with
respect to the Ai) if π (Ai, A i) = 0. If T is a splay with coordinate algebras
Ai, then a Poisson structure π on T is a Poisson structure π on T with
internal symmetry with respect to the Ai’s.
1.1.4. Let T and T ′ be splay algebras equipped with Poisson structures π and
π ′ respectively. We say that a morphism of splays T
Φ✲ T
′
is a Poisson
morphism if Φ ◦ π = π ′ ◦(Φ ⊗ Φ). If T = T ′ as splays, then we say
that π and π ′ are equivalent Poisson structures and that Φ gives an
equivalence between π and π ′.
3
1.1.5. Let A be an algebra and π a Poisson structure on A. We say that π
vanishes on constants if for all a ∈ A we have π (1, a ) = 0 = π (a, 1).
1.1.6. Suppose that A = ⋃
n≥0 A(n) is a ﬁltered algebra and π is a Poisson
structure on A. We say that π is strongly ﬁltered if:
π (A(m), A (n)) ⊆ A(m+n−1).
We will assume for the remainder of this paper that all Poisson struc tures vanish
on constants.
Example 1.2. For an algebra A one has the canonical Poisson structure
deﬁned by:
πc(a, b ) := ab − ba
for a, b ∈ A. The fact that it is a Poisson structure follows from the associativit y
of the algebra A. As we have assumed that A has no quasi-zeros, clearly πc
vanishes if and only if A is a commutative algebra, so that πc is a measure of
the non-commutativity of A.
Remark 1.3. Looking ahead, the Poisson structures π on the splay algebras
measure the non-commutativity of the algebras U . In our motivating example
of g one takes T = Tg, S = Sg, and U = Ug. One usually considers the
Kostant-Kirilov-Souriau π KKS Poisson bracket which is a Poisson bracket on Sg
rather than Tg (c.f. [9]). However, one may may also form a Poisson bracket ˜ π
on Tg by extending the Lie bracket by the bi-derivation law. Working modulo
the commutator relations ηζ − ζη for η, ζ ∈ g we have for all f ∈ Tg that:
˜π (ηζ − ζη, f ) ≡ η˜π (ζ, f ) + ˜π (η, f )ζ
−ζ˜π (η, f ) − ˜π (ζ, f )η
≡ 0
so that ˜π on Tg descends to π KKS on Sg.
We cannot hope to have such a nice situation in general. For example,
suppose that R is a Z/m Z-algebra for some m ≥ 2, and suppose that we have
a relation of the form f m = g in S. Then in order for a Poisson structure π on
T to descend to S we would need for all h ∈ T that:
0
REQ
≡ π (f m − g, h )
≡ m!f m−1π (f, h ) − π (g, h )
≡ − π (g, h )
so that we must have either g = 0 or π (g, h ) = 0. Although this will not
happen in general, we will see below that S = Dist(Gn
a ), over any Fp-algebra
R, falls into the former case, and thus a Poisson structure on the sp lay of some
Dist(Ga)’s will descend.
4
There are two main types of PBW proofs. One makes use of the theo ry of
Gr¨ obner bases as in [15] and [4]. The other is from the viewpoint of deformations
of Koszul algebras as in [1] and [5]. Below, we generalize the Gr¨ obner basis
setting.
Remark 1.4.
1.4.1. Let X be a set and suppose that there is a map X
deg✲ Z≥1. Suppose
that < is a total ordering on the set X . Then if A is either SX or TX , we
obtain a monomial ordering in the sense of [12] and [11] on A by using the
graded lexicographic ordering where for a monomial m = x1 · · · xn with
xi ∈ X , we deﬁne its degree and length by:
deg(m) :=
∑
1≤i≤n
deg(xi)
len(m) := n.
We deﬁne:
A(n) := R⟨m | deg(m) ≤ n⟩ ⊆ A
to be the R-span of monomials of degree at most n, we see that A is a
ﬁltered algebra. A is in fact graded algebra where:
An := R⟨m | deg(m) = n⟩ ⊆ A
A =
⨁
n≥0
An.
If, in particular, we take X
deg✲ Z≥1 to be the constant function 1, then
deg(m) = len(m) and we recover the usual grading on SX and TX . If
J is an ideal in A and B := A/ J , then B inherits a ﬁltration from A:
B =
⋃
n≥0
B(n) B(n) := q(A(n))
where A
q✲ B is the quotient map. We will assume below that all
algebras constructed in this manner are equipped with this ﬁltration .
1.4.2. Let I be an indexing set, and for each i ∈ I suppose we have sets Xi,
and suppose that for each i ∈ I we have an ordering <i on Xi. Deﬁne
X :=∐
i∈I Xi. Then we have an embedding:
SXi
⊂ ιi✲ TXi
⊂ ✲ TX (2)
given by writing any monomial m of length n in Xi as:
m = x1x2x3 · · ·xn
where xi ∈ X i and x1 ≤i x2 ≤i · · · ≤i xn, and we deﬁne:
ιi(m) := x1x2x3 · · · xn ∈ TXi.
5
The map from SXi is then the R-linear extension of this map. By abuse
of notation, we denote ιi(m) simply by m and the composite map of (Eqn.
2) also by ιi.
Lemma 1.5. Let T be a splay with coordinate algebras Ai over a ﬁeld k. Sup-
pose that each Ai has a ﬁxed presentations:
Si
⊂ ✲ SXi ✲ ✲Ai
for some set Xi and ideal of relations Si. Suppose that for each i there is a map:
degi : Xi ✲ Z≥1
and an ordering <i on Xi such that for some indexing set Ji there is a collection
of polynomials {fi,j | j ∈ Ji} which forms a Gr¨ obner basis for the ideal Si with
respect to the graded lexicographic ordering on SXi induced by <i and degi.
Then the splay algebra T has a k basis of elements of the form:
a1a2 · · · ak
where for each 1 ≤ j ≤ k there is some ij ∈ I such that ij ⁄= ij+1 and such that
aj = aj, 1 · · · aj,n j are non-decreasing monomials of length nj ≥ 1 in Xij which
are not leading monomial ideal of the ideal Sij ,
Proof. Adopting the notation of (Rmk. 1.4.2), one may exhibit ∐
i Ai as:
T = TX / R
where R =∑
i Ri and Ri is the ideal generated by Si and the relations sa,a ′ :=
aa′ − a′a for a, a ′ ∈ Ai.
The statement now reduces to showing that the set:
⋃
i∈I
{fi,j | j ∈ Ji} ∪
⋃
i∈I
{sa,a ′ | a > i a′ ∈ X i}
is a Gr¨ obner basis for the ideal R for some monomial ordering on TX . This
follows readily from the graded lexicographic ordering given by deg and an
ordering ≪ as follows. As X is the co-product in sets of the Xi, the maps degi
induce a map X
deg✲ Z≥1. In concrete terms, if m = m1 · · · mn is a monomial
in TX with the mj monomials in Xij for some ij ∈ I, then we have:
deg(m) :=
∑
1≤j≤n
degij (mj).
Let xi ∈ X i ⊆ X and xi′ ∈ X i′ ⊆ X we deﬁne:
xi ≪ xi′ if



i < i ′,
OR
i = i′ and xi <i xi′ .
6
Remark 1.6.
1.6.1. By the results in [11], we may easily extend (Lem. 1.5) to the case of
a general ring R as long as we assume that the leading coeﬃcients of the
fi,j are units of R.
1.6.2. Under the assumptions of (Lem. 1.5) and the ordering ≪ introduced in
its proof, we obtain an R-linear map:
T ⊂
ι≪ ✲ TX
such that q ◦ ι≪ is the identity map on T where q is the quotient map
TX
q✲ ✲T . If J is an ideal of T , we denote by ˜J≪ the ideal of T X
generated by image of ι≪(J ).
Suppose now that π is a Poisson structure on a splay T . Then we obtain
a Poisson structure on TX , denoted by ˜π , by applying the bi-derivation
law to the following map:
X × X ✲ A ⊂
ι≪ ✲ TX
(xi, x i′ ) ✲ π (xi, x ′
i) ✲ ι≪ ◦ π (xi, x i′ ).
Lemma 1.7. Let T be a splay over a ﬁeld k with coordinate algebras Ai which
satisfy the conditions of the (Lem. 1.5). Suppose that π Poisson structure on T
Denote by J the T ideal:
J = (aa′ − a′a − π (a, a ′)) .
Let ˜π≪ and ˜J≪ be as in (Rmk. 1.6.2) and R be as in the proof of (Lem. 1.5).
Then:
• The Poisson structure ˜π≪ descends to π .
• Suppose that f, g ∈ TX , then
f g − gf ≡ ˜π≪(f, g )
(
mod R + ˜J≪
)
.
• π descends to the canonical Poisson structure on U := T / J .
Proof. The ﬁrst statement is clear by the construction of ˜ π≪. The third state-
ment follows readily from the second. For the second, by k-linearity, we may
assume that f and g are monomials. In which case, we proceed by induction
on the sum of their lengths L := len(f ) + len(g). For L ≤ 2 it is trivial by
deﬁnition of ˜π≪. Suppose now that we have proved it for all L′ ≤ L. Let x ∈ X
and consider f ′ = f x where len(f ) ≤ L′. Then, we have:
f ′g − gf ′ ≡ f xg − gf x
≡ (f ˜π≪(x, g ) + f gx) − (f gx + ˜π≪(g, f )x)
≡ f ˜π≪(x, g ) + ˜π≪(f, g )x
≡ ˜π≪(f x, g ) ≡ ˜π≪(f ′, g ).
A similar statement for ˜π≪(g, f ′) gives the desired result.
7
Remark 1.8. Let T (resp. T
′
) be a splay with Poisson structure π (resp. π ′)
and suppose that T
Φ✲ T
′
is a Poisson morphism. Let U (resp. U ) be as in
(Lem. 1.7). Then it is clear that Φ descends to an algebra morphism U
Φ✲ U ′.
If Ai for i ∈ I (resp. A′
j for j ∈ J) are the coordinate algebras of T (resp. T
′
),
then we have the following commutative diagram:
Ai
⊂
ιi ✲ T ✲ ✲U
A′
ji
Φ ji ❄
⊂
ιji ✲ T ′ ✲ ✲U ′.
Φ❄
We now prove a PBW-type theorem. In the case of a Lie algebra g this reduces
to the usual PBW theorem where one has chosen an ordered basis f or the Lie
algebra (c.f. [16], [15], [4]). Again, we may extend (Lem. 1.7) and (Rmk. 1.9)
to the case of a general ground ring R as long as the leading coeﬃcients of the
fi,j ’s are units.
Theorem 1.9. Suppose T is a splay over a ﬁeld k with coordinate algebras Ai
which satisfy the conditions of (Lem. 1.5). Suppose that π is a strongly ﬁltered
Poisson structure on T , and let J be as in (Lem. 1.7). Then, ﬁxing the choice
of a total ordering < on I, U is isomorphic as a k-module to S :=⨂
i Ai.
Proof. It is now enough to show that the set:
Y := {fi,j |i ∈ I, j ∈ Ji} ∪ {ga,b | a ≫ b ∈ X }
is a Gr¨ obner basis of R + ˜J≪ with respect to deg and the ordering ≪ as in
the proof of (Lem. 1.5).
We ﬁrst show that Y generates R+ ˜J≪. By k-linearity of the Poisson bracket,
and as R =∑
i Ri where Ri ⊆ TXi has a Gr¨ obner basis in TXi given by the
fi,j ’s and the ga,b = ab − ba for a > i b ∈ X i, it is enough to show that for all
monomials m and n of TX , we may write mn − nm − ˜π (m, n ) =∑
r µ rgar,b r ηr
for some µ r, η r ∈ TX and some ar ≫ br ∈ X . The statement then follows from
repeated application of the bi-derivation law. Indeed, writing m = m′m′′, we
have that:
m′m′′n − nm′m′′ − ˜π (m′m′′, n )
= m′m′′n − nm′m′′ − m′˜π (m′′, n ) − ˜π (m′, n )m′′
= m′(m′′n − ˜π (m′′, n )) − (nm′ + ˜π (m′, n ))m′′
= m′(m′′n − ˜π (m′′, n )) − m′nm′′ + m′nm′′ − (nm′ + ˜π (m′, n ))m′′
= m′(m′′n − nm′′ − ˜π (m′′, n )) + (m′n − nm′ − ˜π (m′, n ))m′′
which allows us to continually reduce the length of the monomials under con-
sideration, so that we may assume that m and n both have length 1, i.e.
8
that they may be identiﬁed as elements of X . Then we may write either
mn − nm − ˜π = gm,n if m ≫ n or otherwise mn − nm − ˜π = −gn,m .
We now show that this is indeed a Gr¨ obner basis. Without loss of gene rality,
we may assume that the leading coeﬃcient fi,j is LC(fi,j ) = 1. Recalling that
the fi,j are polynomials in SXi
⊂ ✲ TXi, we may write their leading monomials
as:
LM(fi,j ) =: xi,j = xi,j, 1xi,j, 2 · · · xi,j,n j
where the xi,j,k ∈ X i satisfy xi,j, 1 ≤i xi,j, 2 ≤i · · · ≤ i xi,j,n j . For the polyno-
mials gy,x with y > x ∈ X , the strong ﬁltration property on π ensures that
LM(gy,x ) = yx. Now it suﬃces to check the vanishing of the following “S-
polynomials”:
S1 = g(xk, x i,j, 1)xi,j, 2 · · ·xi,j,n j − xkfi,j
with xk ≫ xi,j, 1 in X :
S2 = xi,j, 1xi,j, 2 · · · xi,j,n j −1g(xi,j,n j , x k) − fi,j xk
with xi,j,n j ≫ xk in X , and:
S3(k, j, i ) = g(xk, x j )xi − xkg(xj, x i)
with xk ≫ xj ≫ xi in X .
Let us write fi,j = xi,j − hi,j . We have two possibilities in showing that S1
vanishes. The ﬁrst case is for xk ∈ X i, in which we have for all 1 ≤ r ≤ nj:
g(xk, x 1,j,r ) = xkxi,j,r − xi,j,r xk
by internal symmetry. From this, the vanishing of S1 follows easily. The second
case is for xk ⁄∈ Xi, but as xk ≫ xi,j, 1, this means that xk ∈ X i′ for some i′ > i,
so that xk ≫ xi,j, 1 ≫ gi,j 2 · · · ≫xi,j,n j . We also note that as ˜ π descends to π on
A we necessarily have that for all h ∈ TX we have that:
0 = ˜π (fi,j , h ) = ˜π (xi,j − hi,j , h ).
Now as ˜π is a bi-derivation, it follows that:
∑
1≤r≤nj
xi,j, 1 · · · xi,j,r −1 ˜π (xi,j,r , h )xi,j,r +1 · · ·xi,j,n j = ˜π (hi,j , h )
With these observations, we may now compute S1 as follows:
S1 = −xi,j, 1xkxi,j, 2 · · ·xi,j,n j − ˜π (xk, x i,j, 1)xi,j, 2 · · · xi,j,n j + xkhi,j
= −xi,j, 1xi,j, 2xkxi,j, 3 · · · xi,j,n j − xi,j, 1 ˜π (xk, x i,j, 2)xi,j, 3 · · · xi,j,n j
−˜π (xk, x i,j, 1)xi,j, 2 · · · xi,j,n j + xkhi,j
...
= −xi,j, 1 · · · xi,j,n j xk + xkhi,j
−
∑
1≤r≤nj
xi,j, 1 · · · xi,j,r −1, ˜π (xk, x i,j,r )xi,j,r +1 · · · xi,j,n j
= −hi,j xk − ˜π (xk, x i,j ) + xkhi,j
= ˜ π (xk, h i,j ) − ˜π (xk, x i,j ) = 0
9
The vanishing of S2 is similar.
The vanishing of S3 proceeds similarly to the case of the Gr¨ obner basis for
the PBW theorem of a Lie algebra. Indeed, we have:
S3 = −xkxixj − xk ˜π (xj , x i) + xjxkxi + ˜π (x, x j )xi
= −xixkxj − ˜π (xk, x i)xj − xk ˜π (xj, x i) + xjxixk
+xj ˜π (xk, x i) + (xk, x j )xi
= −xixjxk − xi ˜π (xk, x j) − ˜π (xk, x i)xj − xk(xk, x i) + xixjxk
+˜π (xk, x i)xk + xj ˜π (xk, x i) + ˜π (xk, x j )xi
= ˜ π (˜π (x, x j ), x i) + ˜π (xj , ˜π (xk, x i)) + ˜π (˜π (xj, x i), x k)
= 0
where the last equality follows from skew-Symmetry along with the Ja cobi iden-
tity.
Remark 1.10.
1.10.1. We have injective maps Ai
⊂ ιi✲ T = ∐
i Ai, and it is clear that the
composite maps Ai
q ◦ ιi✲ U is injective, so that Ai is a k-sub-algebra of
U .
1.10.2. Let g be a Lie algebra over k and choose a basis g = k⟨Xi⟩i∈I . Take
for Ai the free commutative algebra generated by xi. Then T = Tg, and
U = Tg/ J = Ug, the universal enveloping algebra, and we may identify
S =⨂ Ai = Sg. Choosing an ordering < on I, we recover the usual PBW
theorem.
1.10.3. More generally, let g be a Lie algebra where we may write g = ⊕i∈I hi
where the hi are abelian Lie sub-algebras. Taking Ai = Shi = Uhi, then
we have:
T = Tg/ R.
Here, R is the ideal R =∑
i Ri where Ri is the ideal generated by the
elements aa′ − a′a for a, a ′ ∈ Ai. Then, the Lie algebra structure on g
induces a Poisson bracket on T , and as the hi are abelian sub-algebras,
we see that the Poisson bracket has internal symmetry with respe ct to
the Ai. We may identify U = Ug, and we may view the Ai = Shi as
sub-algebras of U . Identifying S =⨂ Ai = Sg, and choosing an ordering
on the indexing set I as well as an ordered basis for each of the hi’s, we
again recover the usual PBW theorem.
Deﬁnition 1.11. Let T be a splay with coordinate algebras Ai for i ∈ I and
suppose that T has a strongly ﬁltered Poisson structure π . Denote the multi-
plication of S := ⊗Ai be ·. Let < be an ordering on I. Then we say that a map
T
∆✲ T ⊗ T is strongly multiplicative (with respect to <) if:
∆ π = (· ⊗ π + π ⊗ · + π ⊗ π ) ◦(1 1⊗ τ ⊗ 1 1)◦ ∆ .
10
Here, 1 1 is the identity map, and· denotes, by abuse of notation, the map induced
by on TX by:
X × X
·✲ SX ⊂ι≪✲ T X .
Remark 1.12.
1.12.1. Suppose that we are in the situation of (Def. 1.11). Then if η, ζ ∈ X we
have η · ζ = ζ · η. Moreover, if η > ζ we have by construction of T that:
ζη = ζ · η = η · eta
1.12.2. Let us continue the example given by a Lie algebra g with the choice of
an ordered basis, where Tg
∆✲ Tg ⊗ Tg is map induced by the diagonal
map on g. Then, one has that the π ⊗ π term of the strong multiplicativity
condition automatically vanishes when applied to elements of g ⊆ T =
Tg and, thus, what remains is the usual multiplicativity condition (c.f.
[13]). Moreover, one can view the multiplicativity condition as exactly
the condition that is needed to ensure that ∆ descends to an algebr a map
Ug
∆✲ Ug ⊗ Ug.
In view of the previous remark, we note the following:
Proposition 1.13. Let T be a splay with Poisson structure π and coordinate
algebras Ai for i ∈ I satisfy the conditions of (Lem. 1.5). Suppose that for each i
we have algebra maps Ai
∆ i✲ Ai ⊗ Ai, such that the induced map T
∆✲ T ⊗ T
is strongly multiplicative. Then ∆ descends to an algebra map U
∆✲ U ⊗ U ,
where U is as in (Thm. 1.9).
Proof. Let us ﬁx an ordering on the index set I. In the proof of (Thm. 1.9)
we realized U as the quotient of TX by R + ˜J≪ for which we have exhibited a
Gr¨ obner basis forR + ˜J≪ given in terms of the fi,j ’s and gy,x ’s for y ≫ x ∈ X .
Let us write π instead of ˜π by abuse of notation. Since ∆ is induced from the
∆ i, it is enough to show that ∆ vanishes on the gy,x ’s. Let us suppose that
y ∈ X j and x ∈ X i. If i = j, then gy,x = yx − xy and the assertion is trivial. If
i ⁄= j, then j > i as y ≫ x. As ∆ was induced from the ∆ i’s, we may write:
∆( x) = ∆ i(x) =
∑
r
λ rx′
r ⊗ x′′
r
∆( y) = ∆ j(y) =
∑
s
µ sy′
s ⊗ y′′
s .
Here, the x′
r, x ′′
r are monomials in Xi, and the y′
s, y ′′
s are monomials in Xj . We
11
compute modulo the ideal ( R + ˜J≪) ⊗ TX + TX ⊗ (R + ˜J≪) in that:
∆( yx − xy) ≡
∑
r,s
λ rµ s (y′
sx′
r ⊗ y′′
s x′′
r − x′
ry′
s ⊗ x′′
r y′′
s )
≡
∑
r,s
λ rµ s ((x′
ry′
s + π (y′
s, x ′
t)) ⊗(x′′
r y′′
s + π (y′′
s , x ′′
r )) − x′
ry′
s ⊗ x′′
r y′′
s )
≡
∑
r,s
λ rµ s
(
π (y′
s, x ′
r) ⊗ x′′
r y′′
s + x′
ry′
s ⊗ π (x′′
r , y ′′
s )
+π (y′
s, x ′
r) ⊗ π (y′′
s , x ′′
r )
)
≡ (π ⊗ · + · ⊗ π + π ⊗ π ) ◦(1 ⊗ τ ⊗ 1) ◦(∆ ⊗ ∆)( y ⊗ x)
≡ ∆ ◦ π (y, x )
which yields the desired result.
