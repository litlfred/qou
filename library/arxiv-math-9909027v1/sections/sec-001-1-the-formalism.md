---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I"
section_id: sec-001-1-the-formalism
section_title: "The Formalism"
section_number: 1
pages: 13-25
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
doc_brief: "Planar Algebras, I — We introduce a notion of planar algebra, the simplest example of which is a vector space of tensors, closed under planar contractions."
---
Deﬁnition 1.1. If k is a non-negative integer, the standard k-box, Bk,
is {(x, y) ∈R2 | 0 ≤x ≤k+1, 0 ≤y ≤1}, together with the 2k marked
points, 1=(1, 1), 2=(2, 1), 3 = (3, 1), . . ., k = (k, 1), k + 1 = (k, 0), k + 2 =
(k −1, 0), . . ., 2k = (1, 0).
Deﬁnition 1.2. A planar network N will be a subset of R2 consisting
of the union of a ﬁnite set of disjoint images of Bk’s (with k varying) under
smooth orientation-preserving diﬀeomorphisms of R2, and a ﬁnite number
of oriented disjoint curves, smoothly embedded, which may be closed (i.e.
isotopic to circles), but if not their endpoints coincide with marked points
of the boxes.
Otherwise the curves are disjoint from the boxes.
All the
marked points are endpoints of curves, which meet the boxes transversally.
The orientations of the curves must satisfy the following two conditions.
a) A curve meeting a box at an odd marked point must exit the box at
that point.
b) The connected components of R2\N may be oriented in such a way
that the orientation of a curve coincides with the orientation induced
as part of the boundary of a connected component.
Remark. Planar networks are of two kinds according to the orientation
of the unbounded region.
Let Li, i = 1, 2, . . . be sets and L = `
i Li be their disjoint union. L will
be called the set of “labels”.
13
Deﬁnition 1.3. A labelled planar network (on L) will be a planar network
together with a function from its k-boxes to Lk, for all k with Lk̸ = ∅.
If the labelling set consists of asymmetric letters, we may represent the
labelling function diagrammatically by placing the corresponding letter in its
box, with the understanding that the ﬁrst marked point is at the top left.
This allows us to ignore the orientations on the edges and the speciﬁcation
of the marked points. In Fig. 1.4 we give an example of a labelled planar
network with L1 = {P}, L2 = {R}, L3 = {Q}. Here the unbounded region
is positively oriented and, in order to make the conventions quite clear, we
have explicitly oriented the edges and numbered the marked points of the
one 3-boxes labelled Q.
P
R
R
Q
6
4
5
1
2
3
Figure 1.4
Note that the same picture as in Fig. 1.4, but with an R upside down, would
be a diﬀerent labelled planar tangle since the marked points would be diﬀer-
ent. With or without labels, it is only necessary to say which distinguished
boundary point is ﬁrst.
Remark 1.5. By shrinking each k-box to a point as in Fig. 1.6 one
obtains from a planar network a system of immersed curves with transversal
14
multiple point singularities.
Figure 1.6
Cusps can also be handled by labelled 1-boxes. To reverse the procedure
requires a choice of incoming curve at each multiple point but we see that
our object is similar to that of Arnold in [A]. In particular, in what follows
we will construct a huge supply of invariants for systems of immersed curves.
It remains to be seen whether these invariants are of interest in singularity
theory, and whether Arnold’s invariants may be used to construct planar
algebras with the special properties we shall describe.
Deﬁnition 1.7. A planar k-tangle T (for k = 0, 1, 2, . . .) is the intersec-
tion of a planar network N with the standard k-box Bk, with the condition
that the boundary of Bk meets N transversally precisely in the set of marked
points of Bk, which are points on the curves of N other than endpoints.
The orientation induced by N on a neighborhood of (0,0) is required to be
positive. A labelled planar k-tangle is deﬁned in the obvious way.
The connected curves in a tangle T will be called the strings of T.
The set of smooth isotopy classes of labelled planar k-tangles, with iso-
topies being the identity on the boundary of Bk, is denoted Tk(L).
Note. T0(L) is naturally identiﬁed with the set of planar isotopy classes
of labelled networks with unbounded region positively oriented.
Deﬁnition 1.8. The associative algebra Pk(L) over the ﬁeld K is the
vector space having Tk(L) as basis, with multiplication deﬁned as follows. If
T1, T2 ∈Tk(L), let ˜T2 be T2 translated in the negative y direction by one unit.
After isotopy if necessary we may suppose that the union of the curves in T1
and ˜T2 deﬁne smooth curves. Remove {(x, 0) | 0 ≤x ≤k + 1, x̸ ∈Z} from
T1 ∪˜T2 and ﬁnally rescale by multiplying the y-coordinates 1
2, then adding 1
2.
15
The resulting isotopy class of labelled planar k-tangles is T1T2. See Figure
1.9 for an example.
T1 =
, T2 =
, T1T2 =
Q
Q
R
R
Figure 1.9
Remark. The algebra Pk(L) has an obvious unit and embeds unitally in
Pk+1(L) by adding the line {(k + 1, t) | 0 ≤t ≤1} to an element of Pk(L).
Since isotopies are the identity on the boundary this gives an injection from
the basis of Pk(L) to that of Pk+1(L).
If there is no source of confusion we will suppress the explicit dependence
on L.
Deﬁnition 1.10. The universal planar algebra P(L) on L is the ﬁltered
algebra given by the union of all the Pk’s (k = 0, 1, 2, . . .) with Pk included
in Pk+1 as in the preceding remark.
A planar algebra will be basically a ﬁltered quotient of P(L) for some L,
but in order to reﬂect the planar structure we need to impose a condition of
annular invariance.
Deﬁnition 1.11. The j−k annulus Aj,k will be the complement of the
interior of Bj in (j + 2)Bk −( 1
2, 1
2). So there are 2j marked points on the
inner boundary of Aj,k and 2k marked points on the outer one. An annular
j −k tangle is the intersection of a planar network N with Aj,k such that
the boundary of Aj,k meets N transversally precisely in the set of marked
points of Aj,k, which are points on the curves of N other than endpoints.
16
The orientation induced by N in neighborhoods of (−1
2, −1
2) and (0, 0) are
required to be positive. Labeling is as usual.
Warning. The diagram in Fig. 1.11(a) is not an annular 2–1 tangle,
whereas the diagram in Fig. 1.11 (b) is.
(a)
Q
Q
(b)
Figure 1.11
The set of all isotopy classes (isotopies being the identity on the boundary)
of labelled annular j−k tangles, A(L) = S
j,k Aj,k(L) forms a category whose
objects are the sets of 2j-marked points of Bj. To compose A1 ∈Aj,k and
A2 ∈Ak,ℓ, rescale and move A1 so that its outside boundary coincides with
the inside boundary of A2, and the 2k boundary points match up. Join the
strings of A1 to those of A2 at their common boundary and smooth them.
Remove that part of the common boundary that is not strings. Finally rescale
the whole annulus so that it is the standard one. The result will depend only
on the isotopy classes of A1 and A2 and deﬁnes an element A2A1 in A(L).
Similarly, an A ∈Aj,k(L) determines a map πA : Tj(L) →Tk(L) by
surrounding T ∈Tj(L) with A and rescaling. Obviously πAπB = πAB, and
the action of A(L) extends to P(L) by linearity.
Deﬁnition 1.12 A general planar algebra will be a ﬁltered algebra P =
∪kPk, together with a surjective homomorphism of ﬁltered algebras, Φ :
P(L) →P, for some label set L, Φ(Pk) = Pk, with ker Φ invariant under
A(L) in the sense that, if Φ(x) = 0 for x ∈Pj, and A ∈Aj,k then Φ(πA(x)) =
0, we say Φ presents P on L.
Note. Deﬁnition 1.12 ensures that A(L) acts on P via πA(Φ(x))
def
=Φ(πA(x)).
In particular A(∅) (∅= emptyset) acts on any planar algebra.
17
The next results show that this action extends multilinearly to planar
surfaces with several boundary components.
If T is a planar k-tangle (unlabelled), number its boxes b1, b2, . . ., bn. Then
given labelled tangles T1, . . . , Tn with Ti having the same number of bound-
ary points as bi, we may form a labelled planar k-tangle πT(T1, T2, . . . , Tn)
by ﬁlling each bi with Ti — by deﬁnition bi is the image under a planar dif-
feomorphism θ of Bj (for some j), and Ti is in Bj, so replace bi with θ(Ti)
and remove the boundary (apart from marked points, smoothing the curves
at the marked points). None of this depends on isotopy so the isotopy class
of T deﬁnes a multilinear map πT : Pj1 × Pj2 × . . . × Pjn →Pk. Though
easy, the following result is fundamental and its conclusion is the deﬁnition
given in the introduction of planar algebras based on the operad deﬁned by
unlabeled planar tangles.
Proposition 1.13 If P is a general planar algebra presented on L, by Φ, πT
deﬁnes a multilinear map Pj1 × Pj2 × . . . × Pjn →Pk.
Proof. It suﬃces to show that, if all the Ti’s but one, say i0, are ﬁxed
in Pji, then the linear map α : Pji0 →Pk, induced by πT, is zero on ker Φ.
By multilinearity the Ti’s can be supposed to be isotopy classes of labelled
tangles. So ﬁll all the boxes other than the i0’th box with the Ti. Then we
may isotope the resulting picture so that bi0 is the inside box of a ji0 −k
annulus. The map α is then the map πA for some annular tangle A so ker
Φ ⊆ker πA by Deﬁnition 1.12.
□
Proposition 1.14 Let P be a general planar algebra presented on L by Φ.
For each k let Sk be a set and α : Sk →Pk be a function. Put S = `
k Sk.
Then there is a unique ﬁltered algebra homomorphism ΘS : P(S) →P with
ker ΘS invariant under A(S), intertwining the A(∅) actions and such that
ΘS( R ) = α(R) for R ∈S.
Proof. Let T be a tangle in P(S) with boxes b1, . . . , bn and let f(bi) be
the label of bi. We set ΘS(T) = πT(α(f(b1)), α(f(b2)), . . ., α(f(bn)) with πT
as in 1.13. For the homomorphism property, observe that πT1T2 and πT1 · πT2
are both multilinear maps agreeing on a basis. For the annular invariance
of ker ΘS, note that ΘS factors through P(L), say ΘS = Φ ◦θ, so that
18
ΘS(x) = 0 ⇐⇒θ(x) ∈ker Φ. Moreover, if A ∈A(S), θ◦πA is a linear
combination of πA′’s for A′ in A(L). Hence Φ(θ(πA(x)) = 0 if θ(x) ∈ker Φ.
Finally we must show that ΘS is unique. Suppose we are given a tangle
T ∈P(S). Then we may isotope T so that all its boxes occur in a vertical
stack, as in Figure 1.15.
R1
R2
R3
R4
Figure 1.15
In between each box cut horizontally along a level for which there are
no critical points for the height function along the curves. Then the tangle
becomes a product of single labelled boxes surrounded by A(∅) elements. By
introducing kinks as necessary, as depicted in Figure 1.16, all the surrounded
boxes may be taken in Pk(S) for some large ﬁxed k.
cut
cut
cut
cut
Figure 1.16
19
Since ΘS is required to intertwine the A(∅) action and is an algebra ho-
momorphism, it is determined on all the surrounded boxes by its value on
{ R
: R ∈S}, and their products. The beginning and end of T may involve
a change in the value of k, but they are represented by an element of A(∅)
applied to the product of the surrounded boxes. So ΘS is completely deter-
mined on T.
□
Deﬁnition 1.17. Let P 1, P 2 be general planar algebras presented by
Φ1, Φ2 on L1, L2 respectively.
If α : L1
k →P 2
k , as in 1.14, is such that
ker Θα ⊇ker Φ1, then the
resulting homomorphism of ﬁltered algebras Γα : P 1 →P 2 is called a planar
algebra homomorphism. A planar subalgebra of a general planar algebra is the
image of a planar algebra homomorphism. A planar algebra homomorphism
that is bijective is called a planar algebra isomorphism. Two presentations
Φ1 and Φ2 of a planar algebra will be considered to deﬁne the same planar
algebra structure if the identity map is a planar algebra homomorphism.
Remarks. (i) It is obvious that planar algebra homomorphisms inter-
twine the A(∅) actions.
(ii) By 1.14, any presentation of a general planar algebra P can be altered
to one whose labelling set is the whole algebra itself, deﬁning the same planar
algebra structure and such that Φ( R ) = R for all R ∈P. Thus there is a
canonical, if somewhat unexciting, labelling set. We will abuse notation by
using the same letter Φ for the extension of a labelling set to all of P. Two
presentations deﬁning the same planar algebra structure will deﬁne the same
extensions to all of P as labelling set.
Proposition 1.18 Let P be a general planar algebra, and let Cn ⊆Pn be
unital subalgebras invariant under A(∅) (i.e., πA(Cj) ⊆Ck for A ∈Aj,k(∅)).
Then C = ∪Cn is a planar subalgebra of P.
Proof. As a labelling set for C we choose C itself. We have to show
that ΘC(P(C)) ⊆C. But this follows immediately from the argument for the
uniqueness of ΘS in 1.14. (Note that Cn ⊆Cn+1 as subalgebras of Pn+1 is
automatic from invariance under A(∅).)
□
20
The deﬁnition of isomorphism was asymmetric. The next result shows
that the notion is symmetric.
Proposition 1.19 If Γα : P 1 →P 2 is an isomorphism of planar algebras, so
is (Γα)−1.
Proof. Deﬁne α−1 : L2
k →P 1
k
by α−1(R) = (Γα)−1(Φ2( R ). Then
Γα ◦Θα−1 is a ﬁltered algebra homomorphism intertwining the A(∅) actions
so it equals Φ1 by 1.14. Thus ker Φ2 ⊆ker Θα−1 and Γα−1 = (Γα)−1.
□
The deﬁnitions of planar algebra homomorphisms, etc., as above are a
little clumsy. The meaning of the following result is that this operadic def-
inition of the introduction would give the same notion as the one we have
deﬁned.
Proposition 1.20 If Pi, Φi, Li for i = 1, 2 are as in Deﬁnition 1.17, then
linear maps Γ : P 1
k →P 2
k deﬁne a planar algebra homomorphism iﬀ
πT(Γ(x1), Γ(x2), . . . , Γ(xn)) = Γ(πT(x1, x2, . . . , xn))
for every unlabelled tangle T as in 1.13.
Proof. Given Γ, deﬁne α : L1 →P 2 by α(R) = Γ(Φ1( R )). Then
Θα = Γ◦Φ1 by the uniqueness criterion of 1.14 (by choosing T appropriately
it is clear that Γ is a homomorphism of ﬁltered algebras intertwining A(∅)-
actions). On the other hand, a planar algebra isomorphism provides linear
maps Γ which satisfy the intertwining condition with πT.
□
Deﬁnition 1.21. For each j, k = 0, 1, 2, . . . with j ≤k, Pj,k(L) will
be the subalgebra of Pk(L) spanned by tangles for which all marked points
are connected by vertical straight lines except those having x coordinates
j + 1 through k. (Thus P0,k = Pk.) If B is a general planar algebra, put
Pj,k = Φ(Pj,k) for some, hence any, presenting map Φ.
Deﬁnition 1.22. A planar algebra will be a general planar algebra P
with dim P0 = 1 = dim P1,1 and Φ(
), Φ(
) both nonzero.
21
A planar algebra P, with presenting map Φ : P(L) →P, deﬁnes a planar
isotopy invariant of labelled planar networks, N 7→ZΦ(N ) by ZΦ(N )id =
⊕( N ) ∈P′ if the unbounded region of N is positively oriented (and N
is moved inside B0 by an isotopy), and ZΦ(N )id = Φ(
N ) ∈P1,1 in the
other case (N has been isotoped into the right half of B1). The invariant Z
is called the partition function. It is multiplicative in the following sense.
Proposition 1.23 Let P be a planar algebra with partition function Z. If T
is a labelled tangle containing a planar network N as a connected component,
then
Φ(T) = Z(N )Φ(T ′)
where T ′ is the tangle T from which N has been removed.
Proof. If we surround N by a 0-box (after isotopy if necessary) we see
that T is just N
to which a 0 −k annular tangle has been applied. But
Φ( N ) = Z(N )Φ(
), so by annular invariance, Φ(T) = Z(N )T
□
A planar algebra has two scalar parameters, δ1 = Z(
) and δ2 = Z(
)
which we have supposed to be non-zero.
We present two useful procedures to construct planar algebras. The ﬁrst
is from an invariant and is analogous to the GNS method in operator algebras.
Let Z′ be a planar isotopy invariant of labelled planar networks for some
labelling set L. Extend Z′ to P0(L) by linearity. Assume Z′ is multiplicative
on connected components and that Z′(
)̸ = 0, Z′(
)̸ = 0. For each k let
Jk = {x ∈Pk(L) | Z′(A(T))=0 ∀A ∈Ak,0}. Note that Z′ (empty network)
=1.
Proposition 1.24 (i) Jk is a 2-sided ideal of Pk(L) and Jk+1 ∩Pk(L) = Jk.
(ii) Let Pk = Pk(L)/Jk and let Φ be the quotient map. Then P = ∪Pk
becomes a planar algebra presented by Φ with partition function ZΦ = Z′.
(iii) If x ∈Pk then x = 0 iﬀZΦ(A(x))=0
∀A ∈Ak,0.
Proof. (i) If T1 and T2 are tangles in Pk(L), the map x 7→T1xT2 is given
by an element T of Ak,k(L), and if A ∈Ak,0 then Z′(A(Tx)) = Z′(AT)(x)) =
0 if x ∈Jk. Hence Jk is an ideal.
22
It is obvious that Jk ⊂Jk+1∩Pk(L). So suppose x ∈Jk+1∩Pk. Then for
some y ∈Pk, x =
y
, the orientation of the last straight line depending
on the parity of k. We want to show that y ∈Jk. Take an A ∈Ak,0 and
form the element ˜A in Ak+1,0 which joins the rightmost two points, inside
the annulus, close to the inner boundary. Then ˜A(x) will be A(y) with a
circle inserted close to the right extremity of
y . So by multiplicativity,
Z′( ˜A(x)) = Z′(
)Z′(A(y)). Since Z′(
)̸ = 0, Z′(A(y)) = 0 and y ∈Jk.
(ii) By (i) we have a natural inclusion of Pk in Pk+1. Invariance of the
Jk’s under A is immediate. To show that dim P0 = 1 = dim P1,1, deﬁne
maps U : P0 →K (K = the ﬁeld) and V : P1,1 →K by linear extensions of
U( N ) = Z′(N ) and V ( N
M ) = Z′(N )Z′(M). Observe that U(J0) = 0
and if Ni, Mi, λi(∈K) satisfy Z′(P
i λiA(Ni Mi ) = 0 for all A ∈A1,0, then
by multiplicativity, Z′(
)(P λiZ(Ni)Z(Mi)) = 0, so that U and V deﬁne
maps from P0 and P1,1 to K, respectively. In particular both U and V are
surjective since U(
) = 1, V ( ↑) = 1. We need only show injectivity. So
take a linear combination P λi Ni with P λiZ′(Ni) = 0. Then if A ∈A0,0,
Z′(P λi · A( Ni )) = 0 by multiplicativity so P λi · Ni ∈J′. Similarly for
P
i λiA(Ni Mi ) ∈P1,1.
Thus dim P0 = 1 = dim P1,1 and by construction, Z = Z′.
(iii) This is the deﬁnition of Jk (and ZΦ = Z′).
□
Remark. If one tried to make the construction of 1.24 for an invariant
that was not multiplicative, one would rapidly conclude that the resulting
algebras all have dimension zero.
Deﬁnition 1.25. A planar algebra satisfying condition (iii) of 1.24 will
be called non-degenerate.
The second construction procedure is by generators and relations. Given
a label set L and a subset R ⊆P(L), let Jj(R) be the linear span of
[
T ∈R
T ∈Pk(L)
Ak,j(L)(T). It is immediate that Jj+1(R)∩Pj(L) = Jj(R) (just apply
23
an element of A(∅) to kill oﬀthe last string), and Jj(R) is invariant under
A(L) by construction.
Deﬁnition 1.26. With notation as above, set Pn(L, R) = Pn(L)
Jn(R). Then
P(L, R) = ∪nPn(L, R) will be called the planar algebra with generators L
and relations R.
This method of constructing planar algebras suﬀers the same drawbacks
as constructing groups by generators and relations. It is not clear how big
Jn(R) is inside Pn(L). It is a very interesting problem to ﬁnd relation sets
R for which 0 < dim Pn(L, R) < ∞for each n. Knot theory provides some
examples as we shall see.
Deﬁnition 1.27.
A planar algebra is called spherical if its partition
function Z is an invariant of networks on the two-sphere S2 (obtained from
R2 by adding a point at inﬁnity).
The deﬁnition of non-degeneracy of a planar algebra involves all ways of
closing a tangle. For a spherical algebra these closures can be arranged in a
more familiar way as follows.
Deﬁnition 1.28. Let P be a planar algebra with partition function Z.
Deﬁne two traces trL and trR on Pk by
trL( R ) = Z(
R )
and
trR( R ) = Z( R
).
Note. For a spherical planar algebra P, δ1 = δ2 and we shall use δ for
this quantity. Similarly TrL = TrR and we shall use Tr. If we deﬁne tr(x) =
1
δnTr(x) for x ∈Pn then tr is compatible with the inclusions Pn ⊆Pn+1 (and
tr(1)=1), so deﬁnes a trace on P itself.
Proposition 1.29 A spherical planar algebra is nondegenerate iﬀTr deﬁnes
a nondegenerate bilinear form on Pk for each k.
Proof. (⇐) The picture deﬁning Tr is the application of a particular
element A of Ak,0 to x ∈Pk.
24
(⇒) It suﬃces to show that, for any A ∈Ak,0(L) there is a y ∈Pk such
that Tr(xy) = Z(A(x)). By spherical invariance one may arrange A(x) so
that the box containing x has no strings to its left. The part of A(x) outside
that box can then be isotoped into a k-box which contains the element y.
□
Remark 1.30. One of the signiﬁcant consequences of 1.29 is that, for
nondegenerate P, if one can ﬁnd a ﬁnite set of tangles which linearly span
Pk, the calculation of dim Pk is reduced to the ﬁnite problem of calculating
the rank of the bilinear form deﬁned on Pk by Tr. Of course this may not be
easy!
Corollary 1.31 A nondegenerate planar algebra is semisimple.
