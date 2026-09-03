---
doc_id: s00209-021-02825-4
doc_title: "Mathematische Zeitschrift (2022) 300:1359–1400 A representation theoretic explanation of the Borcea–Brändén characterization Jonathan Leake 1 © The Author(s) 2021"
section_id: sec-026-acknowledgements
section_title: "Acknowledgements"
section_number: null
pages: 34-41
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
---
polynomials and linear stability preservers. We would also like to thank an anonymous referee for a thorough
reading of this paper and many helpful comments.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if changes were made. The images or other third party material in this article are included in the
article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is
not included in the article’s Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder.
To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/ .
A Tensor product decomposition of SL 2(C) representations
In this appendix, we discuss in detail the decomposition of inner tensor products of SL 2(C)
and (SL2(C))m representations. The results given here are for the most part standard, and
they are typically presented via the theory of Lie groups and algebras (e.g., in [ 6]a n d[10]).
Here though, we discuss these results in terms of the polynomial spaces V(n) and V(λ).
That said, the ﬁrst results we state demonstrate the importance of V(n) and V(λ) in the
representation theory of SL 2(C). In fact, these representations are precisely the irreducible
representations of SL 2(C) and (SL2(C))m , respectively (see Lecture 11 of [ 6], and also
Proposition 2.3.23 of [11]). We will not make full use of this fact but will need the following
simpler results.
Proposition A.1 For all n∈ N0, we have that V(n) is an irreducible representation ofSL2(C)
of dimension n + 1.
Proposition A.2 For allλ ∈ Nm
0 , we have that V(λ) ∼= V(λ1)⊠ ··· ⊠ V(λm) is an irreducible
representation of (SL2(C))m of dimension ∏
i(λi + 1).
In particular, outer tensor products of irreducible representations of SL2(C) are irreducible
representations of (SL2(C))m . On the other hand, inner tensor products are not irreducible
and their decomposition leads to a natural deﬁnition of the apolarity form (see Sect. 3.2).
We now set out to compute these decompositions, which are often given as exercises in the
literature (see, e.g., Exercise 11.11 of [ 6]).
A.1 Decomposition of V(n) ⊗ V(m)
Fix n, m ∈ N0. We now consider the representation of SL 2(C) given by the inner tensor
product, V(n)⊗V(m). The importance of the tensor product comes from the fact that it relates
to consideration of SL2(C)-invariant bilinear forms like the apolarity form. In particular, the
decomposition of the tensor product as a sum of irreducible representations (PropositionA.7)
will show us exactly how the D map (see Proposition 3.1) can be used to deﬁne the apolarity
form in the representation theoretic context (Deﬁnition 3.3).
We begin with an important SL 2(C)-invariant map.
123
A representation theoretic explanation... 1393
Proposition A.3 Let x and y denote the linear maps deﬁned on V (k) via multiplication
by x and y, respectively. The linear map U := (x ⊗ y − y ⊗ x) : V(n) ⊗ V(m) →
V(n + 1) ⊗ V(m + 1) is SL2(C)-invariant.
Proof Straightforward computation, e.g., on simple tensors. ⊓⊔
We then use this U m a pt os h o wt h a tDk is not the zero map when k ≤ m, n.
Lemma A.4 For k ≤ m ≤ n, consider the map DU k : V(n − k)⊗ V(m − k) → V(n − 1)⊗
V(m − 1).W eh a v e :
DU k = Uk D + k(n + m − k + 1)Uk−1
Proof Follows from the fact that (∂x x − x∂x)p = p and (∂y y − y∂y)p = p. ⊓⊔
Corollary A.5 For k ≤ m ≤ n, consider the map D kUk : V(n − k) ⊗ V(m − k) →
V(n − k) ⊗ V(m − k).W eh a v e :
DkUk(xn−k ⊗ xm−k) = k!(n + m − k + 1)!
(n + m − 2k + 1)! (xn−k ⊗ xm−k) ⁄= 0
In particular, xn−k ⊗ xm−k is in the image of Dk : V(n) ⊗ V(m) → V(n − k) ⊗ V(m − k).
Proof Apply the previous lemma k times, and use the fact that D(xn−k ⊗ xm−k) = 0. ⊓⊔
We will use this fact about the image ofDk to determine the decomposition ofV(n)⊗V(m)
into irreducible components. We will also need the following fundamental representation
theory result.
Lemma A.6 (Schur’s Lemma) Let V , V′, W be representations of a group G, and suppose
V, V′are irreducible. Then:
(i) Any G-invariant map π : W → V is either surjective or the zero map.
(ii) Any G-invariant map ι : V → W is either injective or the zero map.
(iii) Any G-invariant map ψ : V → V′is either an isomorphism or the zero map.
Further, if V, V′are vector spaces over an algebraically closed ﬁeld, thenψ is unique up to
scalar.
Applying Schur’s lemma to each of the r th transvectants (discussed at the end of Sect.
3.2) yields the desired representation decomposition.
Proposition A.7 Let m ≤ n. We have the following decomposition of V (n) ⊗ V(m),a sa
representation of SL2(C), into irreducible components.
V(n) ⊗ V(m) ∼=
⨁
r≤m
V(n + m − 2r)
In particular, V(n) ⊗ V(n) ∼= V(2n) ⊕ V(2n − 2) ⊕···⊕ V(2) ⊕ V(0).
Proof For each r ∈ N0, ≤ m, consider the SL 2(C)-invariant r th transvectant map:
V(n) ⊗ V(m)
Dr
−→ V(n − r) ⊗ V(m − r)
×
−→ V(n + m − 2r)
By Corollary A.5, this map is not the zero map, as xn−r · xm−r = xn+m−2r is in its image.
Since V(n + m − 2r) is irreducible by Proposition A.1, Schur’s lemma implies this map is
123
1394 J. Leake
surjective. This in turn implies V(n) ⊗ V(m) ∼= V(n + m − 2r) + Wr (as a representation)
for some subspace Wr . Since this holds for all r ≤ m, we actually have
V(n) ⊗ V(m) ∼= W +
⨁
r≤m
V(n + m − 2r)
for some subspace W . The sum of irreducible components here is direct, as any two distinct
irreducible components must intersect trivially. To show that we can set W = 0, we use the
following dimension argument:
m∑
r=0
dim(V(n + m − 2r)) =
m∑
r=0
(n + m − 2r + 1) = (n + 1)(m + 1) = dim(V(n) ⊗ V(m))
This completes the proof. ⊓⊔
Along with the stated decomposition, we also obtain something else: the r th transvectant
is a projection from V(n) ⊗ V(m) onto the irreducible component V(n + m − 2r). Schur’s
lemma and the tensor product decomposition then imply this projection is actually unique
up to scalar. In a similar way, Schur’s lemma also implies D and U must restrict to either a
unique isomorphism or the zero map on each irreducible component of V(n)⊗ V(m).I nt h e
following, we determine exactly what happens on each component.
Theorem A.8 Consider the decomposition V (n) ⊗ V(m) ∼= V(n + m) ⊕ V(n + m − 2) ⊕
···⊕ V(n − m + 2) ⊕ V(n − m). The maps
U : V(n) ⊗ V(m) → V(n + 1) ⊗ V(m + 1)
D : V(n + 1) ⊗ V(m + 1) → V(n) ⊗ V(m)
restrict to SL2(C)-invariant isomorphisms from V (n + m − 2r) to V (n + m − 2r) for all
0 ≤ r ≤ m ≤ n. Additionally, D restricts to the zero map on V (n + m + 2).
Proof By Schur’s lemma, the claim immediately follows ifU is injective and D is surjective.
That D is surjective follows from the fact that the transvectant maps ×◦ Dr are projections
onto each of the irreducible components ofV(n)⊗V(m) for 1 ≤ r ≤ m+1. ThatU is injective
follows from the fact that U(v) = 0 implies v = 0. One can see this by lexicographically
ordering the basis {x j yn− j ⊗ xk ym−k : 0 ≤ j ≤ n, 0 ≤ k ≤ m} and considering the highest
component of a given v ∈ V(n) ⊗ V(m). ⊓⊔
Our main application of this theory is given as follows. Consider the nth transvectant map
×◦ Dn : V(n) ⊗ V(n) → V(0) ∼= C, which is nonzero by the previous theorem. This
map can be interpreted as an SL 2(C)-invariant bilinear form on V(n). It turns out that the
apolarity bilinear form used in Grace’s theorem also has this property, and this justiﬁes the
following deﬁnition.
Deﬁnition 3.3 We call the nth transvectant
V(n) ⊗ V(n)
Dn
−→ V(0) ⊗ V(0)
×
−→ V(0) ∼= C
the apolarity form of V (n).
Corollary A.9 The apolarity form is the unique(up to scalar)nondegenerateSL2(C)-invariant
bilinear form on V (n).
123
A representation theoretic explanation... 1395
A.2 Decomposition of V(/NAK) ⊗ V(/SYN)
Fix λ,μ ∈ Nm
0 ,a n dl e tV(λ) and V(μ) denote the irreducible representations of (SL2(C))m
given by the outer tensor products:
V(λ) ∼= V(λ1) ⊠ ··· ⊠ V(λm) V(μ) ∼= V(μ1) ⊠ ··· ⊠ V(μm)
We next generalize the above results to the inner tensor product of these two representations,
V(λ)⊗V(μ). In particular, we determine the decomposition of this tensor product and deﬁne
a multivariate apolarity form. Note that these statements strictly generalize the previous
analogous statements.
Proposition A.10 (c.f. Proposition A.7) Let μ ≤ λ. We have the following decomposition of
V(λ) ⊗ V(μ), as a representation of (SL2(C))m , into irreducible components.
V(λ) ⊗ V(μ) ∼=
⨁
α≤μ
V(λ + μ − 2α)
Proof We compute:
V(λ) ⊗ V(μ) ∼=
(
V(λ1) ⊠ ··· ⊠ V(λm)
)
⊗
(
V(μ1) ⊠ ··· ⊠ V(μm)
)
∼=
(
V(λ1) ⊗ V(μ1)
)
⊠ ··· ⊠
(
V(λm) ⊗ V(μm)
)
∼=
( ⨁
α1≤μ1
V(λ1 + μ1 − 2α1)
)
⊠ ··· ⊠
( ⨁
αm≤μm
V(λm + μm − 2αm)
)
∼=
⨁
α≤μ
V(λ + μ − 2α)
The last step uses the distributive law for sums and tensor products of representations. ⊓⊔
Theorem A.11 (c.f. Theorem A.8) For anyβ ∈ Nm
0 , deﬁne Uβ := Uβ1 ⊠ ··· ⊠ Uβm . Deﬁne
Dβ similarly. For anyμ ≤ λ ∈ Nm
0 , the maps
Uβ : V(λ) ⊗ V(μ) → V(λ + β) ⊗ V(μ + β)
Dβ : V(λ + β) ⊗ V(μ + β) → V(λ) ⊗ V(μ)
restrict to SL2(C)-invariant isomorphisms on the components of V (λ) ⊗ V(μ) ∼=⨁
α≤μ V(λ + μ − 2α). Finally, Dβ restricts to the zero map on the other irreducible com-
ponents of V (λ + β) ⊗ V(μ + β).
Proof Follows by induction on β,u s i n gT h e o r e mA.8. ⊓⊔
Deﬁnition 3.4 (c.f. Deﬁnition 3.3) We call the map
V(λ) ⊗ V(λ)
Dλ
−→ V(0m) ⊗ V(0m)
×
−→ V(0m) ∼= C
the apolarity form of V (λ).
Corollary A.12 (c.f. Corollary A.9) The apolarity form is the unique(up to scalar) nondegen-
erate (SL2(C))m -invariant bilinear form on V(λ).
123
1396 J. Leake
B The Grace–Walsh–Szeg ˝o coincidence theorem
A classical result in the representation theory of SL2(C) is the fact that V(n) ∼= Symn(V(1)).
Here, Symn(V(1)) denotes the set of symmetric tensors in V(1)⊗n , or alternatively, the set of
symmetric elements in V(1n). That is, there is some SL2(C)-invariant injection from V(n) to
V(1)⊗n , and by our conceptual thesis this map should transfer stability information. In fact,
this idea is formalized in the Grace–Walsh–Szeg˝ o coincidence theorem, and the injective
map is known as the polarization map.
B.1 Polarization and projection
For polynomials of degree m ≤ n, the degree- n polarization map is deﬁned on monomials
as follows and is extended linearly.
/Pi1↑
n : Cn[x]→ C(1n)[x1,..., xn]
xk ↦→ 1
n!
∑
σ∈Sn
k∏
j=1
xσ( j)
This deﬁnition can be extended to homogeneous polynomials in V(n) by composing with
Hmg−1
n and Hmg(1n).T h em a p/Pi1↑
n has a left inverse /Pi1↓
n , called the projection map, which
we deﬁne as follows.
/Pi1↓
n : C(1n)[x1,..., xn]→ Cn[x]
f (x1, x2,..., xn) ↦→ f (x, x,..., x)
That is,/Pi1↓
n ◦/Pi1↑
n is the identity map. Similarly, this deﬁnition can be extended to homogeneous
polynomials by composing with Hmg −1
(1n) and Hmgn .
It is well-known that /Pi1↑
n is an injective linear map onto the subspace of symmetric multi-
afﬁne polynomials. This fact then extends to homogeneous polynomials, where the terms
symmetric and multi-afﬁne each refer to pairs of homogeneous variables. Further, one can
deﬁne multivariate polarization and projection maps via composition:/Pi1↑
λ := /Pi1↑
λm ◦···◦ /Pi1↑
λ1
and /Pi1↓
λ := /Pi1↓
λm ◦···◦ /Pi1↓
λ1 . Injectivity then automatically extends to /Pi1↑
λ ,a n d/Pi1↓
λ ◦ /Pi1↑
λ is
the identity map.
These two maps arise naturally in the theory of polynomials in general, and play an
important role in the theory of stability, via the Grace–Walsh–Szeg˝ o coincidence theorem
as well as in the proof of the Borcea–Brändén characterization of linear operators. The next
result shows they also have represention theoretic importance.
Proposition B.1 Fixλ ∈ Nm
0 , and view V(λ) ∼= V(λ1)⊠··· ⊠ V(λm) and V(1λ) ∼= V(1)⊗λ1 ⊠
··· ⊠ V(1)⊗λm as representations of (SL2(C))m . The maps /Pi1↑
λ : V(λ) → V(1λ) and
/Pi1↓
λ : V(1λ) → V(λ) are (SL2(C))m -invariant.
Proof Note that by proving the result for /Pi1↑
n and /Pi1↓
n with m = 1, the general result follows
since /Pi1↑
λ and /Pi1↓
λ are compositions of such maps. To prove it for m = 1, note that the set of
symmetric elements in V(1)⊗n ∼= V(1n) is invariant under the diagonal action of SL 2(C).
Further, since V(n) is irreducible of dimension n + 1a n d V(1)⊗n has a single irreducible
component of dimension n + 1, Schur’s lemma implies the result. ⊓⊔
123
A representation theoretic explanation... 1397
This result then has a few corollaries which will help to shed light on results related to
polarization and the apolarity form. The ﬁrst will be useful in elucidating the representation
theoretic ties to the Grace–Walsh–Szeg˝o coincidence theorem below.
Lemma B.2 Fix λ ∈ Nm
0 . Then the apolarity form commutes with polarization up to scalar.
That is:
Dλ = D(1λ) ◦ (/Pi1↑
λ ⊗ /Pi1↑
λ)
Proof The map D(1λ) ◦ (/Pi1↑
λ ⊗ /Pi1↑
λ) : V(λ) ⊗ V(λ) → C is an (SL2(C))m -invariant bilinear
form on V(λ). By uniqueness (see Corollary A.12), this then must equal Dλ up to scalar. ⊓⊔
The content of this result is that fact that we have commutativity even though D(1λ) is
a priori the apolarity form with respect to a different group action than that of Dλ (i.e.,
(SL2(C))|λ| instead of (SL2(C))m ). That said, it should be noted that the analogous commu-
tativity statement with the projection map /Pi1↓
λ does not hold (unless of course, one restricts
to the image of /Pi1↑
λ ).
The purpose of this result is then to demonstrate the connection between a polynomial and
its polarization. In particular, if Grace’s theorem gives stability information via the apolarity
form, then the previous result shows that the polarizations of those polynomials will have the
same stability information. We prove this rigorously in Corollary B.5.
Proposition B.1 also leads to one of the crucial results used in the proof of the Borcea–
Brändén characterization of linear operators (Lemma 2.5 in [1]). It relies on the notion of “the
polarization of an operator”, given by T ↦→ /Pi1↑
α ◦ T ◦ /Pi1↓
λ ( s e e§ 2 . 2i n[1]). We do not make
explicit use of this result, but we state it here to demonstrate that operator polarization has a
representation theoretic interpretation similar to that of the usual polynomial polarization.
Proposition B.3 The symbol of the polarization of an operator T is the polarization of the
symbol of T .
Proof Using Proposition B.1 and Deﬁnition 3.6, it is straightforward to see that all the maps
involved are injective (SL2(C))2m -invariant linear maps (i.e., polarization of polynomials,
polarization of operators, the Symb map). The result then follows from a dimension argument
and Schur’s lemma, in a way similar to that of the proof of Proposition B.1. ⊓⊔
B.2 The coincidence theorem
The Grace–Walsh–Szeg˝o coincidence theorem has strong ties to Grace’s theorem, and most
books and surveys on the subject state the two results side by side. Some books (e.g., [ 15])
even go so far as to demonstrate their equivalence, perhaps with other results involving typical
polynomial convolutions. Here, we will state and prove the general multivariate version of
the theorem in terms of homogeneous polynomials, making use of evaluation symbols and
Grace’s theorem (Theorem 5.1).
First though, consider the following corollary to the symbol lemma (Lemma 3.7)w h i c h
is similar in spirit to the evaluation symbol lemma (Lemma 5.10). Note that when applied
to p ∈ V(n) with m = 1, this result has the following intuitive statement as a corollary:
Dn(q ⊗ p) is equal to the evaluation of /Pi1↑
n p at the roots of q .
123
1398 J. Leake
Lemma B.4 Fix λ ∈ Nm
0 ,p ∈ V(λ), and any (a : b) ∈ (CP1)|λ|, more explicitly deﬁned as
follows:
(a : b) ≡
(
(a1,1 : b1,1) ,...,( a1,λ1 : b1,λ1 ) ,...,( am,1 : bm,1) ,...,( am,λm : bm,λm )
)
∈ (CP1)λ1+···+λm
We have the following:
(/Pi1↑
λ p)(a, b) = Dλ
(
/Pi1↓
λ
(
Symb(ev(a,b))
)
⊗ p
)
= Dλ
⎛
⎝
m∏
k=1
λk∏
j=1
(bk, j xk − ak, j yk) ⊗ p
⎞
⎠
Proof We ﬁrst prove the case of m = 1a n d p ∈ V(n), given as follows:
(/Pi1↑
n p)(a, b) = Dn
(
/Pi1↓
n
(
Symb(ev(a,b))
)
⊗ p
)
= Dn
⎛
⎝
n∏
j=1
(bj x − a j y) ⊗ p
⎞
⎠
The second equality follows immediately from the deﬁnition of /Pi1↓
n and of ev(a,b) (Deﬁnition
5.9). For the ﬁrst equality, Lemma B.2 implies:
Dn
(
/Pi1↓
n
(
Symb(ev(a,b))
)
⊗ p
)
= D(1n)
(
/Pi1↑
n ◦ /Pi1↓
n
(
Symb(ev(a,b))
)
⊗ /Pi1↑
n p
)
By deﬁnition of /Pi1↑
n , both /Pi1↑
n ◦ /Pi1↓
n
(
Symb(ev(a,b))
)
and /Pi1↑
n p are symmetric in pairs of
variables. Further, we can explicitly compute:
/Pi1↑
n ◦ /Pi1↓
n
(
Symb(ev(a,b))
)
= 1
n!
∑
σ∈Sn
n∏
j=1
(bj xσ( j) − a j yσ( j))
This expression and the fact that /Pi1↑
n p is symmetric then imply:
D(1n)
(
/Pi1↑
n ◦ /Pi1↓
n
(
Symb(ev(a,b))
)
⊗ /Pi1↑
n p
)
= 1
n!
∑
σ∈Sn
D(1n)
⎛
⎝
n∏
j=1
(bj xσ( j) − a j yσ( j)) ⊗ /Pi1↑
n p
⎞
⎠
= D(1n)
⎛
⎝
n∏
j=1
(bj x j − a j yj) ⊗ /Pi1↑
n p
⎞
⎠
The last expression is then equal to (/Pi1↑
n p)(a, b) by the evaluation symbol lemma (Lemma
5.10).
For the general case of p ∈ V(λ), the same argument applies with a few tweaks. The
key change is that /Pi1↑
λ ◦/Pi1↓
λ
(
Symb(ev(a,b))
)
and /Pi1↑
λ p are no longer fully symmetric in pairs
of variables, but instead invariant under the action of Sλ1 ×···× Sλm on the |λ| pairs of
variables.
⊓⊔
Generally speaking, the above lemma demonstrates the strong connection between the
apolarity form and the polarization map. We now utilize this to prove the coincidence theorem.
123
A representation theoretic explanation... 1399
Corollary B.5 (Grace–Walsh–Szeg˝o) Fix λ ∈ Nm
0 ,p ∈ V(λ), and any disjoint Grace pair
(C1×···× Cm, B1×···× Bm).I fpi s (C1×···× Cm)-stable, then/Pi1↑
λ pi s(Cλ1
1 ×···× Cλm
m )-
stable.
Proof So as to prove the contrapositive, suppose /Pi1↑
λ p is not (Cλ1
1 ×···× Cλm
m )-stable. That
is, suppose (/Pi1↑
λ p)(a, b) = 0f o rs o m e(a, b) = (a1, b1,..., am,λm , bm,λm ) ∈ C2|λ| such that
(a j,k : bj,k) ∈ C j for all j ∈[ m] and k ∈[ λj ]. By the previous lemma, this implies:
Dλ
(
/Pi1↓
λ
(
Symb(ev(a,b))
)
⊗ p
)
= 0
By disjointness of C j and Bj for all j ∈[ m],w et h e nh a v et h a t(a j,k : bj,k)/∈ Bj for all
j, k. Therefore Symb(ev(a,b)) is (Bλ1
1 ×···× Bλm
m )-stable (see Deﬁnition 5.9). This implies
/Pi1↓
λ
(
Symb(ev(a,b))
)
is (B1 ×···× Bm)-stable. Since Dλ
(
/Pi1↓
λ
(
Symb(ev(a,b))
)
⊗ p
)
= 0,
the deﬁnition of Grace pair (Deﬁnition 5.2) then implies p must not be(C1×···× Cm)-stable.
⊓⊔
By Theorem 5.7, this implies the coincidence theorem for circular regions when m > 1
and for any projectively convex regions when m = 1. Notice that there is no reference made
to degree or convexity restrictions (compare this to Theorems 1.1 and 1.2 in [2]). As discussed
above, this is one of the main beneﬁts of using homogeneous polynomials and interpreting
zeros as lying in CP1 and (CP1)m .
