---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-004-3-general-results-on-semisimplification-of-tenso
section_title: "General results on semisimplification of tensor categories"
section_number: 3
pages: 8-14
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
categories
3.1. Splitting of the semisimpliﬁcation functor for Tannakian
categories in characteristic zero, reductive envelopes, a nd the
Jacobson-Morozov lemma. For Tannakian categories in character-
istic zero, Andr´ e and Kahn showed that the semisimpliﬁcation funct or
S admits a splitting S∗, and used it to show the existence and unique-
ness (up to conjugation) of the reductive envelope of any aﬃne pr oal-
gebraic group in characteristic zero. In this subsection we review t his
theory (cf. [AK],[S]).
Theorem 3.1. ([AK], Theorem 1, Theorem 2) If char(k) = 0 and C =
RepG is a Tannakian category over k (whereG is an aﬃne proalgebraic
group over k), then the functor S : C →
C admits a splitting S∗ :
C → C , a surjective tensor functor such that S∗(X) ∼
= X for each
indecomposableX ∈ C , and S ◦ S∗ ∼= Id as a symmetric tensor functor.
Now let C be as above and F be the forgetful functor C → Vec.
Then F ◦ S∗ :
C → Vec is a ﬁber functor, so by the Tannakian for-
malism ([DM]), we have C = Rep G, where G := Aut(F ◦ S∗) is a
8
reductive aﬃne proalgebraic group, equipped with a homomorphism
ψG :G →
G (deﬁned up to conjugation in G) giving rise to the functor
S∗. Moreover, since S∗ is surjective, ψG is an inclusion.
Deﬁnition 3.2. ([AK]) The group G equipped with the homomor-
phism ψG (deﬁned up to conjugation) is called the reductive envelope
of G.
Theorem 3.3. ([AK], Theorem 3, Theorem 4) The reductive envelope
G enjoys the following universal property: If φ :G →L is a homomor-
phism from G to a reductive proalgebraic group L, then there exists a
homomorphismφ :G →L such that φ =φ ◦ψG. Moreover, φ is unique
up to conjugation in L by elements commuting with φ(G).
Proof. The morphism φ gives rise to a symmetric tensor functor Φ :
RepL → RepG. Consider the functor Φ ′ := S ◦ Φ. Even though S
may not be exact on any side, the functor Φ ′ is exact since the category
RepL is semisimple (as L is reductive). Thus, Φ ′ : RepL → RepG is
a symmetric tensor functor. Hence, by Tannakian formalism ([DM])
it comes from a homomorphism φ′ :
G → L deﬁned uniquely up to
conjugation in L. Moreover, consider the functor S∗ ◦ Φ ′ = S∗ ◦ S ◦ Φ.
This functor is exact since its source is a semisimple category, so it
is a symmetric tensor functor, and it follows from Proposition 13.7.1
of [AK] that it is naturally isomorphic to Φ as a tensor functor. This
means that the homomorphisms φ and φ′ ◦ψG are conjugate under
L: φ(g) = ℓφ′(ψG(g))ℓ−1 for some ℓ ∈ L and all g ∈ G. Hence,
φ(g) = ~φ(ψG(g)) for all g ∈G, where ~φ(a) := ℓφ′(a)ℓ−1.
Finally, let us show that the homomorphism ~φ in the theorem is
determined uniquely up to conjugation in L (automatically by elements
commuting with φ(G)). To this end, let ~Φ : Rep L → RepG be the
functor deﬁned by ~φ. Then S∗ ◦ ~Φ = Φ, hence, postcomposing with
S, we get ~Φ = S ◦ Φ. Thus, ~Φ is uniquely determined and hence ~φ is
determined up to conjugation, as desired. □
Remark 3.4. A geometric proof of the existence and properties of the
reductive envelope is given in [S].
Example 3.5. Consider the special case G = Ga. In this case the
indecomposable representations of G are unipotent Jordan blocks Jn
of sizes n = 1, 2, 3..., so it is easy to see that
RepG ∼= RepSL(2) (as
the Grothendieck ring of RepG coincides with that of Rep SL(2), and
the dimensions of nonzero objects of RepG are positive). So in this
case the existence of G is easy (namely, G =SL(2)), and the existence
of the splitting S∗ is also straightforward (namely, S∗ is induced by
9
the standard inclusion ψG : Ga֒→SL(2) as upper triangular matrices
with ones on the diagonal). Thus, Theorem 3.3 in this case tells us
that any homomorphism φ : Ga → L for a reductive proalgebraic
group L uniquely (up to conjugacy) factors through a homomorphism
~φ :SL(2) →L. As pointed out in [AK, S], this implies the celebrated
Jacobson-Morozov Lemma:
Proposition 3.6. Let L be a reductive algebraic group over k, and
u ∈ L a unipotent element. Then there exists a homomorphism θ :
SL(2) → L such that θ
(
1 1
0 1
)
= u. Moreover, θ is unique up to
conjugation by the centralizer Zu of u.
Proof. Let G be the 1-parameter unipotent subgroup of L generated
byu, and φ :G →L be the corresponding embedding. Identify G with
Ga by sending u to 1. Then it remains to apply Theorem 3.3 and set
θ = ~φ. □
Note that when G is an algebraic group then
G is typically only a
proalgebraic group (of inﬁnite type), which can be very large. In fa ct,
this is already so when G = G2
a, since the problem of classifying pairs
of commuting matrices is well known to be wild; i.e., the case G = Ga
(leading to the Jacobson-Morozov Lemma) is a rare exception. In o ther
words, the whole category Rep
G is typically unmanageable. However,
it makes sense to consider tensor subcategories of this category gener-
ated by a single object, which are more manageable. Namely, we have
the following corollary.
Corollary 3.7. Let G be an aﬃne algebraic group over k, and V ∈
RepG a faithful representation of G (so that֒→GL(V )). Then
there exists a reductive algebraic group GV ⊂ GL(V ) containing G (a
quotient of
G) such that the subcategory CV of RepG ∼= RepG tensor
generated by V is naturally equivalent to RepGV .
Proof. Let FV : CV → Vec be the restriction of the ﬁber functor of
RepG to CV . Let GV := Aut(FV ). Then GV ⊂ GL(V ) is a reductive
subgroup such that Rep GV = CV . Moreover, GV is a quotient of G,
hence we have a natural homomorphism G → GV , which is obviously
injective, as desired. □
Deﬁnition 3.8. We will call GV the reductive envelope of G inside
GL(V ).
Remark 3.9. 1. Let C = Rep k Z/p , where char( k) = p ≥ 5.
Then a tensor functor S∗ : C → C does not exist, since C = Verp
10
contains objects of non-integer Frobenius-Perron dimension. Als o, if
C = RepGL(n|1) over k of characteristic zero then a symmetric func-
tor S∗ as is Theorem 3.1 does not exist, either. Indeed, if V is the vector
representation of GL(n|1) then ∧n−1S(V ) = 0 (cf. Example 2.7(3)),
while ∧n−1V ⁄= 0 (it is a negligible but nonzero object in C). In fact, it
is clear that a splitting functor S∗ with the properties stated in The-
orem 3.1 cannot exist if C has indecomposable objects of dimension
0.
2. Note that the existence of the group G such that Rep G ∼= RepG
follows from Deligne’s theorem ([D1], Theorem 7.1), since RepG is a
symmetric tensor category over k in which nonzero objects have posi-
tive integer dimensions. This is, in fact, used in the proof of Theorem
3.1 in [AK].
Moreover, using a more general version of Deligne’s theorem for su -
pergroups, [D2], one can see that if G is an aﬃne proalgebraic su-
pergroup over k of characteristic zero and z ∈ G an element of or-
der ≤ 2 acting on O(G) by parity, and Rep( G,z ) is the category of
representations of G on superspaces on which z acts by parity, then
Rep(G,z ) = Rep(G,z) for some reductive proalgebaric supergroup G,
i.e., one whose representation category is semisimple, see [H], Theor em
2.2. In particular, for each V ∈ Rep(G,z ), V generates a category
Rep(GV,z), where GV is a reductive algebraic supergroup (a quotient
of G). This means that the connected component of the identity G0
V
of GV is of the form G′
V/C, where C is a ﬁnite central subgroup and
G′
V =G+
V ×G−
V , where G+
V is a usual reductive group, and Lie G−
V is a
direct sum of Lie superalgebras of type osp(1|2n), see [W].
In fact, as was explained to us by Thorsten Heidersdorf, the symm et-
ric structure of the category is not essential in the Andr´ e-Kahntheorem
on the existence of splitting of the semisimpliﬁcation functor. Namely ,
Theorem 12.1.1 and 13.2.1 of [AK] immediately imply the following
theorem:
Theorem 3.10. Let C be a Karoubian pivotal category as in Theorem
2.6, such that the ideal N (C) of negligible morphisms in C coincides
with the nilpotent radical rad(C) of C (where rad(C)(X,Y ) is the inter-
section of the radical of the algebra End(X ⊕Y ) with HomC(X,Y )); in
other words, C has no nonzero indecomposable objects of zero dimen-
sion. Then the semisimpliﬁcation functor S : C →
C admits a monoidal
splitting S∗ : C → C .
Corollary 3.11. Let C be a Karoubian pivotal category as in Theorem
2.6. Then following conditions are equivalent:
11
(i) Any indecomposable direct summand in a tensor product of two
indecomposable objects of nonzero dimension also has nonze ro dimen-
sion; in other words, indecomposables of nonzero dimension span a full
monoidal subcategory of C.
(ii) The semisimpliﬁcation functor S : C → C admits a monoidal
splitting S∗ : C → C .
Proof. It follows from Theorem 3.10 that (i) implies (ii). To prove that
(ii) implies (i), assume that (i) fails, and let X,Y be simple objects
of nonzero dimension such that X ⊗ Y ∼= Z ⊕ T where Z ⁄= 0 is
indecomposable and has dimension zero. Then S(X) ⊗ S(Y ) ∼= S(T ).
So if there is a monoidal splitting S∗, then applying S∗ to the last
equality, we get X ⊗Y ∼=T . Thus, T ∼=Z ⊕T , which contradicts the
Krull-Schmidt theorem. □
In particular, this implies existence of reductive envelopes for quan -
tum groups. Namely, let H be a Hopf algebra over a ﬁeld k in which
the squared antipode is given by conjugation by a character χ ∈ H ∗
(thereby deﬁning a pivotal structure on Corep( H)), with no inde-
composable ﬁnite dimensional comodules M ⁄= 0 of zero dimension.
Then the category Corep(H) satisﬁes the assumptions of Theorem 3.10.
Therefore, we obtain
Proposition 3.12. There exists a unique universal cosemisimple Hopf
algebra
H with a surjective homomorphism s :H →H (in other words,
any Hopf algebra homomorphism H ′ → H from a cosemisimple Hopf
algebraH ′ uniquely factors throughs). Namely, Corep(H) = Corep(H)
The proof is analogous to the case when H is commutative over
C (i.e., the case of proalgebraic groups). Heuristically writing G =
Spec(H) and G = Spec(H), we may say that the reductive quantum
group G is the reductive envelope of the quantum group G.
Example 3.13. Letq be a transcendental number, or, more generally,
a complex number which is not a root of any polynomial with posi-
tive integer coeﬃcients, say a positive real number or its image unde r
an automorphism of C. Let Bq be the quantum Borel subgroup of
the quantum group Gq attached to a simple complex algebraic group
G. The category Rep( Bq) = Corep( O(Bq)) has a pivotal structure
given by the element q2ρ of the corresponding quantum enveloping al-
gebra. Therefore, the dimension (both left and right) of any nonz ero
representation of Bq is a Laurent polynomial in q with positive integer
coeﬃcients. Thus, this dimension is nonzero. Hence Proposition 3.12
applies, and H := O(Bq) is the quotient of some cosemisimple Hopf
12
algebra H :=O(Bq) for some reductive quantum group Bq, such that
every representation of Bq factors canonically through Bq.
3.2. Compatibility of semisimpliﬁcation with equivariantiza-
tion. Now let C be a tensor category and L be a ﬁnite group acting on
C. Let CL be the L-equivariantization of C ([EGNO], Subsection 4.15).
The following lemma is easy ([EGNO], Exercise 4.15.3).
Lemma 3.14. If
1 →N →G →L → 1
is an exact sequence of groups then L acts naturally on RepkN, and
(RepkN)L ∼= RepkG.
Clearly, any action of L on C descends to its action on the semisim-
pliﬁcation
C.
Proposition 3.15. If |L| ⁄= 0 in k and L preserves the spherical
structure of C thenL-eqiuvariantization commutes with semisimpliﬁca-
tion. In other words, we have a natural equivalence of tensor categories
CL ∼
=
C
L
.
Proof. We have a natural forgetful functor F : CL → C . We claim that
if X,Y ∈ C L and f : X → Y is negligible, then F (f ) is negligible.
Indeed, recall that Hom( F (X),F (Y )) carries a natural action of L,
and that F deﬁnes an isomorphism Hom(X,Y ) ∼= Hom(F (X),F (Y ))L.
Now let h ∈ Hom(F (Y ),F (X)), and let us show that Tr( F (f ) ◦h) = 0.
Leth = |L|−1 ∑
γ∈Lγ(h). Then h =F (g) for a unique g ∈ Hom(X,Y ).
Thus, sinceF (f ) commutes withL and the action of L preserves traces,
we have
Tr(F (f ) ◦h) = Tr(F (f ) ◦h) = Tr(F (f ) ◦F (g)) = 0,
as desired. Thus, the functor F descends to a tensor functor F : CL →
C. Moreover, for any T ∈ CL the object F (T ) has a natural structure
of an L-equivariant object (coming from that of T ), so the functor F
factors naturally through a tensor functor E : CL → C
L
.
Suppose T ∈ CL is simple. Then T = X, where X ∈ C L is an
indecomposable object of nonzero dimension. Thus X = IndL
LZ (ρ ⊗Z),
whereZ is an indecomposable object of C of nonzero dimension, LZ is
the stabilizer of Z in L, and ρ is an irreducible representation of LZ
over k. Then E(T ) = IndL
LZ (ρ ⊗
Z). Thus, E(T ) is simple (since so is
Z, and LZ =LZ).
It remains to show that E is essentially surjective, i.e. every simple
object of C
L
is of the form E(T ). To this end, note that every simple
13
object of C
L
has the form W = Ind L
LV (ρ ⊗V ), where V =
X is a
simple object of C and ρ is an irreducible representation of LV . Since
|LV | ⁄= 0 in k, we have dim ρ ⁄= 0 in k. Hence, W = E(T ), where
T = Ind L
LV (ρ ⊗ X) is a simple object of
CL (as LV = LX ). The
proposition is proved. □
Corollary 3.16. In the setup of Lemma 3.14 assume that |L| ⁄= 0 in
k. Then RepkG ∼= RepkN
L
.
Proof. This follows from Proposition 3.15 and Lemma 3.14. □
Remark 3.17. Similarly to Theorem 2.6, Proposition 3.15 and its
proof generalizes to Karoubian pivotal categories satisfying the a ssump-
tions of Theorem 2.6.
