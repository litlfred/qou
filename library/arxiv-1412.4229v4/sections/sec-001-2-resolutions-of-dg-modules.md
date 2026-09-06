---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-001-2-resolutions-of-dg-modules
section_title: "Resolutions of DG Modules"
section_number: 2
pages: 12-16
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — Let A → B be a homomorphism of commutative rings."
---
Let A be a DG ring. We already mentioned thatM(A) = DGModA is a DG
category, equipped with a translation automorphismT. The homotopy category of
DGModA is ˜K(DGModA), where by deﬁnition
(2.1) Hom˜K(DGModA)(M,N ) := H0(
HomA(M,N )
{
.
This is a triangulated category. The derived category˜D(DGModA) is gotten from
˜K(DGModA) by inverting the quasi-isomorphisms. The localization functor (iden-
tity on objects) is
(2.2) Q : DGModA→˜D(DGModA).
If A is a ring, i.e. A = A0, with module category ModA, then DGModA =
C(ModA), ˜K(DGModA) = K(ModA) and ˜D(DGModA) = D(ModA). Here are
THE SQUARING OPERATION 13
some references for the derived category of DG modules: [BL, Section 10], [Ke1,
Section 2], and [SP, Section 09KV]. Another reference is our course notes [Ye4],
but there (in Sections 4 and 9) the DG categoryC(M), associated to an abelian
category M, should be replaced by the DG categoryDGModA.
Deﬁnition 2.3.We shall use the following abbreviations for the triangulated cat-
egories related to a DG ringA: K(A) := ˜K(DGModA) and D(A) := ˜D(DGModA).
Let us recall a few facts about resolutions of DGA-modules. A DG moduleN is
called acyclic ifH(N) = 0. A DGA-moduleP (resp.I) is calledK-projective(resp.
K-injective) if for any acyclic DGA-module N, the DG Z-module HomA(P,N )
(resp. HomA(N,I )) is also acyclic. The DG moduleP is calledK-ﬂatif for every
acyclic DGAop-module N, the Z-module N⊗AP is acyclic. As in the “classical”
situation, K-projective implies K-ﬂat. These deﬁnitions were introduced in [Sp]. In
[Ke1, Section 3] it is shown that “K-projective” is the same as “having property
(P)”, and “K-injective” is the same as “having property (I)”. EveryM ∈M(A)
admits K-projective resolutionsP →M and K-injective resolutionsM→I. See
also [BL], [BN], [AFH] and [SP, Chapter 09JD]. (Semi-free DG modules will be
discussed in Section 3.)
Recall that a diagram
M
φ0
$$
φ1
::N
in M(A) is called commutative up to homotopyif the homomorphismsφ0 and φ1
are homotopic. Or in other words, if the corresponding diagram inK(A) is com-
mutative.
The next proposition is essentially a standard fact. We state it here because it
will play a key role, especially in Section 5.
Proposition 2.4. Let P,I ∈M(A). Assume either P is K-projective orI is K-
injective.
(1) The additive homomorphism
Q : HomM(A)(P,I )→HomD(A)(P,I )
is surjective, and its kernel is the groupB0(HomA(P,I )) of null-homotopic
homomorphisms.
(2) Let ψ: P →I be a morphism in D(A). There exists a homomorphism
φ:P→I in M(A), unique up to homotopy, such thatQ(φ) =ψ.
(3) Let φ0,φ1 : P→I be homomorphisms in M(A). The homomorphisms φ0
and φ1 are homotopic iﬀQ(φ0) = Q(φ1) in D(A).
In other words, item (2) says that given a morphismψin D(A), as in the ﬁrst
diagram below, there exists a homomorphism φin M(A) making that diagram
commutative; and suchφis unique up to homotopy. Item (3) says that the second
diagram below, in M(A), is commutative up to homotopy, iﬀ the third diagram
below, in D(A), is commutative.
P
ψ
##
Q(φ)
;;I P
φ0
!!
φ1
==I P
Q(φ0)
!!
Q(φ1)
==I
14 AMNON YEKUTIELI
Proof. (1) According to [Sp, Propositions 1.4 and 1.5], the additive homomorphism
HomK(A)(P,I ) = H0(HomA(P,I ))→HomD(A)(P,I )
is bijective. Note that in [Sp]Ais a ring; but the deﬁnitions and proofs pass without
change to the case of a DG ring.
(2, 3) These are immediate from (1). □
A DG ring homomorphismu : A→B induces the forgetful (or restriction of
scalars) functor Foru : M(B)→M(A), which is exact, and hence gives rise to a
triangulated functor Foru : D(B)→D(A). We usually do not mention the functor
Foru explicitly, unless it is important for the discussion at hand.
Ifu :A→B is a quasi-isomorphism thenForu : D(B)→D(A) is an equivalence,
with quasi-inverseM↦→B⊗L
AM. For anyM0∈D(Aop) andM1,M 2∈D(A) there
are bi-functorial isomorphismsM0⊗L
AM1∼= M0⊗L
B M1 and RHomA(M1,M 2)∼=
RHomB(M1,M 2) in D(Z); cf. [YZ2, Proposition 1.4].
Here is a result that will be used a lot in our paper. The restriction functors are
suppressed in it. The easy proof is left to the reader.
Proposition 2.5.LetA0
u1
−→A1
u2
−→A2 andB0
v1
−→B1
v2
−→B2 be homomorphisms
in DGR. Fork = 0, 1, 2 let Mk∈M(Bk⊗ZAk) and Nk∈M(Bk); and fork = 1, 2
let ζk :Mk−1→Mk and θk :Nk→Nk−1 be homomorphisms inM(Bk−1⊗ZAk−1)
and M(Bk−1) respectively.
(1) The abelian groupHomB0(M0,N 0) is a DGAop
0 -module, with action
(φ·a)(m) :=φ(a·m)
for φ∈HomB0(M0,N 0), a∈A0 and m∈M0.
(2) The function
Homv1(ζ1,θ1) : HomB1(M1,N 1)→HomB0(M0,N 0),
with formula
Homv1(ζ1,θ1)(φ) :=θ1◦φ◦ζ1
for φ∈HomB1(M1,N 1), is a homomorphism inM(Aop
0 ).
(3) There is equality
Homv1(ζ1,θ1)◦Homv2(ζ2,θ2) = Homv2◦v1(ζ2◦ζ1,θ1◦θ2).
(4) Say ζ′
1 : M0 →M1 and θ′
1 : N1 →N0 are also homomorphisms in
M(B0⊗ZA0) and M(B0) respectively, and there are homotopiesζ1⇒ζ′
1 and
θ1⇒θ′
1 in M(B0⊗ZA0) and M(B0) respectively. Then there is a homotopy
Homv1(ζ1,θ1)⇒Homv1(ζ′
1,θ′
1)
in M(Aop
0 ).
Item (2) of the proposition is illustrated here:
M0
ζ1 //
Homv1(ζ1,θ1)(φ)

M1
φ

N0 N1
θ1oo
Proposition 2.6. Letv :A′→A be a quasi-isomorphism between DG rings. Let
Q,I ∈M(A), P ∈M(Aop), Q′,I′∈M(A′) and P′∈M(A′op). Let φ: P′→P
be a quasi-isomorphism inM(A′op), and letψ: Q′→Q and χ: I→I′be quasi-
isomorphisms in M(A′).
THE SQUARING OPERATION 15
(1) If ((P is K-ﬂat overAop orQ is K-ﬂat overA) and (P′is K-ﬂat overA′op
or Q′is K-ﬂat overA′)) then
φ⊗vψ:P′⊗A′Q′→P⊗AQ
is a quasi-isomorphism.
(2) If ((Q is K-projective orI is K-injective overA) and (Q′is K-projective
or I′is K-injective overA′)) then
Homv(ψ,χ) : HomA(Q,I )→HomA′(Q′,I′)
is a quasi-isomorphism.
Proof. This is implicit in the proof of [YZ2, Proposition 1.4]. Here is a detailed
proof.
(1) By the symmetry of the situation we can assume that eitherP′andP are K-ﬂat
(over the respective DG rings), or thatQ′andP are K-ﬂat. We begin by reducing
the second case to the ﬁrst case. Choose a K-ﬂat resolutionµ: ˜P′→P′. Then
˜P′⊗A′Q′→P′⊗A′Q′is a quasi-isomorphism, and it suﬃces to prove that
(φ◦µ)⊗vψ: ˜P′⊗A′Q′→P⊗AQ
is a quasi-isomorphism, which is the ﬁrst case.
Now we assume thatP′andP are K-ﬂat. Consider the homomorphismφ·idA :
P′⊗A′A→P, (φ·idA)(p′⊗a) :=φ(p′)·a. We claim this is a quasi-isomorphism.
Toseewhy, letuslookattheﬁrstcommutativediagrambelow. Thehomomorphism
idP′⊗v is a quasi-isomorphism sincev is a quasi-isomorphism andP′is K-ﬂat;
the homomorphism idP′·idA′is an isomorphism; andφis a quasi-isomorphism;
therefore φ·idA is a quasi-isomorphism.
P′⊗A′A′idP′·idA′
//
idP′⊗v

P′
φ

P′⊗A′A
φ·idA //P
P′⊗A′Q′φ⊗vψ //
idP′⊗ψ

P⊗AQ
P′⊗A′Q λ //P′⊗A′A⊗AQ
(φ·idA)⊗idQ
OO
Next look at the second commutative diagram above. The homomorphismλ,
deﬁned byλ(p′⊗q) :=p′⊗1⊗q, is an isomorphism. The homomorphismidP′⊗ψ
is a quasi-isomorphism because ψis a quasi-isomorphism and P′is K-ﬂat; and
(φ·idA)⊗idQ is a quasi-isomorphism becauseφ·idA a quasi-isomorphism between
K-ﬂat DGAop-modules. Thereforeφ⊗vψis a quasi-isomorphism.
(2) Choose K-projective resolutionsα: ˜Q→Q and α′: ˜Q′→Q′, and K-injective
resolutions β: I →˜I and β′: I′→˜I′, in M(A) and M(A′) respectively. By
Proposition 2.4, we can liftψandχto quasi-isomorphisms ˜ψand ˜χ, such that the
diagrams
˜Q′
α′

˜ψ // ˜Q
α

Q′ψ //Q
˜I
˜χ // ˜I′
I
β
OO
χ //I′
β′
OO
in M(A′) are commutative up to homotopy. We get a diagram
(2.7) HomA(Q,I )
Homv(ψ,χ) //
Homid(α,β)

HomA′(Q′,I′)
Homid(α′,β′)

HomA( ˜Q, ˜I)
Homv( ˜ψ,˜χ) // HomA′( ˜Q′, ˜I′)
16 AMNON YEKUTIELI
in M(Z) that is commutative up to homotopy. Now let us examine the commutative
diagram
HomA(Q,I )
Homid(α,idI) //
Homid(idQ,β)

Homid(α,β)
((
HomA( ˜Q,I )
Homid(id ˜Q,β)

HomA(Q, ˜I)
Homid(α,id ˜I) // HomA( ˜Q, ˜I)
in M(Z). The homomorphisms Homid(α,id˜I) and Homid(id ˜Q,β) are both quasi-
isomorphisms. Atleastoneofthehomomorphisms Homid(idQ,β)and Homid(α,idI)
is a quasi-isomorphism. It follows that the diagonal homomorphismHomid(α,β)
is a quasi-isomorphism. A similar argument shows thatHomid(α′,β′) is a quasi-
isomorphism. Going back to diagram (2.7), we see that it is enough to prove that
Homv( ˜ψ,˜χ) is a quasi-isomorphism.
Let λ: ˜I→HomA′(A, ˜I′) be the homomorphismλ(i)(a) := ˜χ(a·i) in M(A). It
ﬁts into a commutative diagram
˜I λ //
˜χ

HomA′(A, ˜I′)
Homid(v,id)

˜I′ HomA′(A′, ˜I′)canoo
in M(A′), where can is the canonical isomorphism. Because ˜χand v are quasi-
isomorphisms, and ˜I′is K-injective, we see thatλis a quasi-isomorphism.
Finally, consider the commutative diagram
HomA( ˜Q, ˜I)
Homv( ˜ψ,˜χ) //
Homid(id,λ)

HomA′( ˜Q′, ˜I′)
HomA( ˜Q, HomA′(A, ˜I′))
adj // HomA′( ˜Q, ˜I′)
Homid( ˜ψ,id)
OO
in M(Z), where adj is the adjunction isomorphism. Since λand ˜ψare quasi-
isomorphisms, ˜Q is K-projective, and ˜I′is K-injective, it follows thatHomv( ˜ψ,˜χ)
is a quasi-isomorphism. □
