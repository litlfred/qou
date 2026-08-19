---
doc_id: arxiv-0911.4494v2
doc_title: "The geometry of Markov traces Ben Webster Geordie Williamson"
section_id: sec-003-3-hecke-algebras-and-geometry
section_title: "Hecke algebras and geometry"
section_number: 3
pages: 4-9
source_pdf: 0911.4494v2.pdf
source_sha256: 1ba1c79686b12d98
doc_brief: "The geometry of Markov traces Ben Webster Geordie Williamson — We give a geometric interpretation of the Jones-Ocneanu tra ce on the Hecke algebra, using the equivariant cohomology of shea ves on"
---
G denote a split semi-simple algebraic group over Fq with ﬁxed split maximal torus
T and Borel subgroup B. If Γdenotes the Dynkin diagram of the root system of G,
then we may canonically identify WΓwith the Weyl group of G. Given any w∈ WΓ
we denote by ˙w a representative in G for w∈ WΓ. Consider the corresponding Bruhat
decomposition
G(Fq) =
⨆
w∈WΓ
B(Fq)· ˙w· B(Fq).
1 Recall that if B is an A-algebra (for a A a commutative ring), and M an A-module, then a trace on B
with values in M is a map φ : B→ M of A-modules such that φ(b1b2) = φ(b2b1) for all b1, b2∈ B.
4
Ben Webster & Geordie Williamson
A classical theorem of Iwahori identiﬁes the convolution al gebra of B(Fq)× B(Fq)-
invariant C-valued functions on G(Fq) with HΓ, where q
1/2 is specialized at a ﬁxed
square root of|Fq|∈ C. Under this identiﬁcation the element σi∈ HΓcorresponds to the
characteristic function of the orbit B(Fq)· ˙si· B(Fq) multiplied by q−1/2.
The fact that the Hecke algebra arises as a convolution algeb ra suggests a natural
categoriﬁcation using Grothendieck’s function-sheaf dic tionary . Fix a prime ℓ diﬀerent
from the characteristic of Fq and let /CZ denote an algebraic closure of the ﬁeld of ℓ-adic
numbers.
We denote by Db
B×B(G) the bounded B× B-equivariant derived category of mixed
constructible
/CZ -sheaves on G (see, for example [SGA73], [Del77], [BBD82] and [BL94]),
often referred to as the Hecke category . There is a convolution product on Db
B×B(G)
which we denote by ⋆ (see [Spr82]). We ﬁx a square root q
1/2 of q in
/CZ , which allows
us to deﬁne a square root ( 1/2) of the Tate twist (1). We denote by ⟨m⟩the shift-twist
functor [m](m/2) (note that⟨m⟩preserves weight).
Deﬁnition 3. Let ICw denote the intersection cohomology complex corresponding to the B× B
orbit B ˙wB, normalized so that the restriction of ICw to B ˙wB is /CZ
B ˙wB⟨ℓ(w)/2⟩.
That is, we normalize intersection cohomology complexes so that the induced sheaf
on G/B is perverse and pure of weight 0.
Finally , letDB×B(G)0 denote the subcategory of Db
B×B(G) consisting of objects isomor-
phic to direct sums of ICw⟨m⟩for w∈ WΓand m∈ Z and KB×B(G)0 its split Grothendieck
group. We have:
• The category DB×B(G)0 is preserved under convolution (by the Decomposition
theorem), and ⋆ induces a ring structure on KB×B(G)0.
• The assignment q1/2↦→⟨−1⟩makes KB×B(G)0 into an algebra over Z[q1/2, q−1/2].
The following result is well-known:
Theorem 4 (See [Spr82]). The Hecke algebra HΓcan be identiﬁed with KB×B(G)0. Under this
identiﬁcation the Kazhdan-Lusztig basis element C ′
w corresponds to the class of the intersection
cohomology complex [ICw].
For example, if s is a simple reﬂection, then C′
s = σs + q−1/2 corresponds to
/CZ
Ps
⟨1⟩, the
shift-twist of the constant sheaf on the minimal parabolic s ubgroup Ps = BsB.
The relationship between these sheaves and the Hecke algebr a was an important
ingredient in the Kazhdan-Lusztig conjecture [KL79, KL80] .
Alternatively , one can consider the B× B-equivariant cohomology of ICw. This is
an indecomposable Soergel bimodule H∗
B×B(G; ICw) = Sw (for more background on
Soergel bimodules and their connections to geometry , see the original paper [Soe92] of
Soergel or authors’ earlier paper [WW08]).
4. A categoriﬁed trace. Let B∆⊂ B× B be the diagonal subgroup. Then we can asso-
ciate to ICw and Sw bigraded vector spaces H∗
B∆
(ICw) and H H∗(Sw), the B∆-equivariant
cohomology and Hochschild homology respectively .
The bigrading on H H∗(Sa) is easy to describe: one grading, which we call the t-
grading, is given by the homological grading on H H∗ and one is given by the fact
that Sa is a graded bimodule over polynomials, with linear polynomi als in degree 2.
5
The geometry of Markov traces
For reasons of knot theory , we follow the convention of [MSV] with respect to the
grading on Hochschild homology: we normalize the gradings s o that the di ﬀerential
on Hochschild homology has bidegree (1 , 1).
The bigrading on H∗
B∆
(ICw) is of geometric origin, but less obvious than the algebraic
grading. What we must use is the weight grading on cohomology . By previous work
of the authors [WW08, Theorem 1.4], there is an isomorphism H∗
B∆
(ICw) /simequalH H∗(Sw),
which sends the q-grading to the usual cohomological grading and the t-grading to the
weight plus cohomological grading, i.e. that given by the no rm of the eigenvalue of
Frobenius.
Thus, we let Hi; j
B∆
(G; ICw) be subspace of Hi
B∆
(G; ICw) of weight j. In all situations
encountered below, Frobenius will always act semi-simply v ia powers of our ﬁxed q
1/2
and hence Hi; j
B∆
(G; ICw) is equal to the q
j/2-eigenspace of Hi
B∆
(G; ICw) for the action of
Frobenius.
Deﬁnition 5. Given a sheafF∈ Db
B∆
(G), its mixed Poincar´ e seriesis
PF (q, t) = dimq,t H∗
B∆
(G;F ) =
∑
i, j
dim Hi; j
B∆
(G;F )q
i/2
t j−i.
We will always consider equivariant mixed Poincar´ e polynomials, and only specify
the group if there is danger of confusion. Note that
(1) PF⟨−i⟩(q, t) = q
i/2
PF (q, t).
As before, Γis a Dynkin diagram, and we let Γ′ = Γ−{ v} for a single vertex v, and
ι : HΓ′→ HΓis the induced inclusion.
Theorem 6. The linear extension of the function TrΓ(C′
w) = dimq,t H∗
B∆
(ICw) = PICw(q, t) only
depends on the root system of G and is a trace on HΓ. Furthermore, for each vertex v, we have
Tr∅(1) = 1 Tr Γ(σvι(a)) =−t· TrΓ′(a)
TrΓ(ι(a)) = 1 + q
1/2t
1− q · TrΓ′(a) Tr Γ(σ−1
v ι(a)) = q−1/2
· TrΓ′(a)
In particular, when Γ =An, this trace coincides with that of Jones-Ocneanu. Furtherm ore, in
the case where Γ =Bn, Cn, Dn, it is the trace Tr−t
Γ given in Proposition 2, where y =−t.
This establishes that this trace pulled back to the braid gro up provides a knot invari-
ant (up to normalization), called the HOMFLYPT polynomial i n the type A case, and
an invariant of knots in the solid torus in type B, by the “cylindrical Markov theorem”
(see [GL97]).
Proof of Theorem 6. We ﬁrst show that our trace only depends on the root system of t he
semi-simple group G, and not on its root datum. To this end let
φ : ~G→ G
denote a central isogeny and set ~B := φ−1(B). We denote by ~ICw the intersection
cohomology complex on ~G, normalized as in Deﬁnition 3. We claim there is a canonical
6
Ben Webster & Geordie Williamson
isomorphism:
H∗
B∆
(G, ICw) /simequalH∗
~B∆
(~G, ~ICw).
First note that ( φ∗, φ∗) give an equivalence
Db
~B×~B(~G)
∼
→ Db
~B×B(G)
and hence the adjunction morphism F → φ∗φ∗F is an isomorphism for any F ∈
Db
~B×B
(G). It follows that
H∗
~B∆
(G, ICw)
∼
→ H∗
~B∆
(~G, φ∗ICw) = H∗
~B∆
(~G, ~ICw)
Lastly H∗
~B∆
(G, ICw) = H∗
B∆
(G, ICw) because K = ker φ is a ﬁnite group and our coeﬃcients
are of characteristic zero.
Our deﬁnition yields a trace since for sheaves F ,F′∈ Db
B×B(G) we have
H∗
B∆
(G;F ⋆F′) /simequalH∗
B×B(G× G;F ⊠F′) /simequalH∗
B∆
(G;F′ ⋆F ).
where the B× B-action on G× G in the equation above is given by
(b1, b2)· (g1, g2) = (b1g1b−1
2 , b2g2b−1
1 ).
It follows that Tr∅(1) = 1 since if Γ =∅ then G is the trivial group.
It remains to verify the behaviour of our trace under an inclu sion ι. To do this we
give a geometric interpretation of ι. By the above considerations we may assume that
G is of adjoint type. Now let ∆⊂ R denote the based root system of ( G, B, T). The
inclusion Γ⊂ Γ′ determines a based root system ∆′⊂ R′ with an inclusion into ∆⊂ R
such that ∆ = ∆′∪{ α} where α is the simple root corresponding to the new vertex v of
Γ.
Now let G′ denote the closed subgroup of G generated by root subgroups and
cocharacters corresponding to roots in R′, and let ~G′ = G′T. Then G′ is a semi-simple
algebraic group with root system R′ and ~G′ /simequalG′× Gm, because we have assumed that
G is adjoint. If we set
T′ := T∩ G′, ~T′ := T, B′ := B∩ G′ and ~B′ := B∩ ~G′
then T′ and ~T′ (respectively B′ and ~B′) are split maximal tori (respectively Borel sub-
groups) of G′ and ~G′.
The projection and inclusion maps
G′ p
← ~G′ i
֒→G
induce functors
p∗ : Db
B′×B′(G)→ Db
~B′× ~B′(G′) and i∗ : Db
~B′× ~B′(G′)→ Db
~B′× ~B′(G).
We deﬁne
I∗ : Db
B′×B′(G′)−→ Db
B×B(G)
F↦−→ indB×B
~B′× ~B′i∗p∗F .
7
The geometry of Markov traces
If w′∈ WΓ′ and w denotes its image under the natural inclusion WΓ′֒→WΓthen one
has I∗(ICw′) /simequalICw because B/~B′ is isomorphic to an a ﬃne space. Hence I∗ categoriﬁes
the inclusion ι : HΓ′→ HΓ′ under the identiﬁcations in Theorem 4.
Now, let P⊂ G be the minimal standard parabolic corresponding to α∈ ∆. Given
F∈ Db
B′×B(G′)0 it remains to calculate the Poincar´ e series of the cohomology groups
H∗
B∆
(
/CZ
B ⋆ I∗F ) /simequalH∗
B∆
(I∗F ) and H∗
B∆
(
/CZ
P ⋆ I∗F )
in terms of H∗
B′
∆
(F ). It will be easier to work instead with T∆-equivariant cohomology ,
which is equivalent because B∆/T∆is isomorphic to an a ﬃne space.
First note that, as ~G′ /simequalG′× Gm we have, by the K ¨ unneth formula,
(2) H∗
T∆
(I∗F ) /simequalH∗
T′
∆
(F )⊗ H∗
Gm
(Gm)
(where Gm acts trivially on Gm in the second factor).
It remains to calculate H∗
B∆
(
/CZ
P ⋆ I∗F ). Set Z := (ker α)0 and let L = CG(Z) be its
centralizer in G. We can write T /simequalZ× Tv, with Gm /simequalTv via the fundamental coweight
corresponding to α (which belongs to the cocharacter lattice because G is of adjoint
type).
Now we have a Levi decomposition P = LU, where U denotes the unipotent radical
of P. Hence we have a T× T-equivariant map P→ L with ﬁbers isomorphic to a ﬃne
spaces. Moreover, H := L/Z is a semi-simple group of rank 1. It follows that we have
an acyclic T× T-equivariant map
P×T ~G′→ H× G′.
Moreover, the induced conjugation actions of Z (resp. Tv) on H (resp. G′) are trivial.
Hence
(3) H∗
T∆
(G,
/CZ
P ⋆ I∗F ) /simequalH∗
(Tv)∆
(H)⊗ H∗
Z∆
(G′,F )
Taking Poincar´ e series in the equations (2,3), we get the relations
Tr(ι(a)) = dimq,t H∗
B∆
(I∗F ) = 1 + q
1/2t
1− q Tr(a)
Tr(C′
vι(a)) = dimq,t H∗
T∆
(G,
/CZ
P ⋆ I∗F⟨1⟩) = q−1/2 + qt
1− q Tr(a)
This establishes one of our conditions. For the others, we ﬁr st observe that σv = C′
v−q−1/2
and σ−1
v = C′
v− q
1/2. This shows that
Tr(σvι(a)) = qt− t
1− q· Tr(a) Tr( σ−1
v ι(a)) = q−1/2− q
1/2
1− q · Tr(a)
=−t· Tr(a) = q−1/2
· Tr(a).
Finally , we must establish our claim that
TrBn+1(Tnι(a)) =−t· TrBn(a)
This follows from Corollary 13, which shows that our trace co incides with that con-
sidered by Gomi and from [Gom06, §4.4 & 4.5] where Gomi shows that his trace
8
Ben Webster & Geordie Williamson
corresponds to that constructed by Geck and Lambropoulou, w hich has this property
by [GL97, Proposition 4.5]. □
Question 1. The above proof uses the Gomi’s algebraic calculations to de duce that our
trace satisﬁes all the conditions in Deﬁnition 2 for y =−t. We do not know whether the
extra conditions in types B, C and D have a geometric explanation.
