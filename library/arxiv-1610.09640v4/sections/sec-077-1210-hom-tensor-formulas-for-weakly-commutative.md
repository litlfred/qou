---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-077-1210-hom-tensor-formulas-for-weakly-commutative
section_title: "Hom-Tensor Formulas for Weakly Commutative DG Rings"
section_number: 12.10
pages: 248-253
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
subsection we assume that all DG rings are weakly commutative (see Deﬁnition
3.3.4). For such a DG ringA, its 0-th cohomology H0(A) is a commutative ring.
Proposition 12.10.1. For a weakly commutative DG ringA, the categoryD(A)
is H0(A)-linear.
Proof. Thisistruealreadyforthehomotopycategory. Indeed, forany M,N ∈C(A)
theK-module H0(
HomA(M,N )
{
is an H0(A)-module; and composition inK(A) is
H0(A)-bilinear. □
Let A be a DG ring. There is a canonical isomorphismu : A
≃
− →Aop to its
opposite. The formula is u(a) := (−1)i·a for a∈Ai. This implies that every
left DG A-module can be made into a right DGA-module, and vice-versa. The
formula relating the left and right actions ism·a = (−1)i·j·a·m for a∈Ai and
m∈Mj. On the level of categories we obtain an isomorphism of DG categories
C(A)∼= C(Aop), which is the identity functor on the underlying DGK-modules.
Weak commutativity makes the tensor and Hom functors A-bilinear (in the
graded sense), and therefore their derived functors have more structure: they are
H0(A)-bilinear triangulated bifunctors
(12.10.2) (−⊗L
A−) : D(A)×D(A)→D(A)
and
(12.10.3) RHomA(−,−) : D(A)op×D(A)→D(A).
When the DG rings in Theorem 12.7.2 are weakly commutative, this result can
be ampliﬁed:
Proposition 12.10.4. In the situation of Theorem12.7.2, assume thatA and B
are weakly commutative.
(1) The restriction functorRestu : D(B)→D(A) is an equivalence ofH0(A)-
linear triangulated categories, with quasi-inverseLIndu.
248
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) For everyM,N ∈D(B) there is an isomorphismM⊗L
AN
≃
− →M⊗L
BN in
D(A). This isomorphism is functorial inM and N.
(3) For every M,N ∈D(B) there is an isomorphism RHomA(M,N )
≃
− →
RHomB(M,N ) in D(A). This isomorphism is functorial inM and N.
Proof.
(1) The ring homomorphismH0(u) : H0(A)→H0(B) makes D(B) into an H0(A)-
linear category, and thenRestu : D(B)→D(A) becomes an H0(A)-linear functor.
(2,3) Going over the steps in the proof of Theorem 12.7.2, we see that all the moves
are A-linear (in the graded sense). □
Suppose A→B is a DG ring homomorphism. For everyM∈C(A) and N∈
C(B), their tensor productM⊗AN is a DGB-module, via the action onN. Thus
we get a DG bifunctor
(12.10.5) (−⊗A−) : C(A)×C(B)→C(B).
There is an isomorphism
(12.10.6) M⊗AN
≃
− →N⊗AM
in Cstr(B), that uses the Koszul sign rulem⊗n↦→(−1)i·j·n⊗m for homogeneous
elementsm∈Mi and n∈Nj.
Proposition 12.10.7.LetA→B be a homomorphism of weakly commutative DG
rings. The DG bifunctor(12.10.5) has a left derived bifunctor
(−⊗L
A−) : D(A)×D(B)→D(B).
This is anH0(A)-bilinear triangulated bifunctor.
Proof. The left derived bifunctor exists by Theorem 9.3.16, using K-ﬂat resolutions
in the ﬁrst argument (i.e. inCstr(A)). As for theH0(A)-bilinearity: this is already
comes in the homotopy category level, namely for the bifunctor
(−⊗A−) : K(A)×K(B)→K(B). □
Similarly we have anH0(A)-bilinear triangulated bifunctor
(−⊗L
A−) : D(B)×D(A)→D(B).
When A =B these operations coincide with (12.10.2).
Proposition 12.10.8 (Symmetry). Let A→B be a homomorphism of weakly
commutative DG rings. For everyM∈D(A) and N∈D(B) there is an isomor-
phism M⊗L
AN∼= N⊗L
AM in D(B). This isomorphisms is functorial inM and
N.
Proof. Use the isomorphism (12.10.6). □
Proposition 12.10.9 (Associativity). Let A1 →A2 →A3 be homomorphisms
between weakly commutative DG rings. For eachi let Mi∈D(Ai). There is an
isomorphism
(M1⊗L
A1M2)⊗L
A2M3∼=M1⊗L
A1 (M2⊗L
A2M3)
in D(A3). This isomorphisms is functorial in theMi.
Proof. Choose K-ﬂat resolutionsPi→Mi in C(Ai). Then we have isomorphisms
(M1⊗L
A1M2)⊗L
A2M3∼= (P1⊗A1P2)⊗A2P3
∼=†P1⊗A1 (P2⊗A2P3)∼=M1⊗L
A1 (M2⊗L
A2M3)
in D(A3). The isomorphism∼=†is due to the usual associativity of⊗. □
249
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Suppose A→B is a DG ring homomorphism. For everyM∈C(A) and N∈
C(B), theDGK-module HomA(N,M )hasaDG B-modulestructure, viatheaction
on N. Thus we get a DG bifunctor
(12.10.10) HomA(−,−) : C(B)op×C(A)→C(B).
Proposition 12.10.11. Let A→B be a homomorphism of weakly commutative
DG rings. The DG bifunctor(12.10.10) has a right derived bifunctor
RHomA(−,−) : D(B)op×D(A)→D(B).
This is anH0(A)-bilinear triangulated bifunctor.
Proof. The right derived bifunctor exists by Theorem 9.3.11, using K-injective res-
olutions in the second argument (i.e. inCstr(A)). □
Proposition 12.10.12 (Hom-Tensor Adjunction). Let A1→A2→A3 be homo-
morphisms between weakly commutative DG rings. For eachi let Mi ∈D(Ai).
There is an isomorphism
RHomA2
(
M3, RHomA1(M2,M 1)
{∼= RHomA1
(
M2⊗L
A2M3,M 1)
in D(A3). This isomorphisms is functorial in theMi.
Proof. Choose a K-ﬂat resolutionP2→M2 in C(A2), and a K-injective resolution
M1→I1 in C(A1). An easy adjunction calculation show that HomA1(P2,I 1) is
K-injective in C(A2). Then we have isomorphisms
RHomA2
(
M3, RHomA1(M2,M 1)
{∼= HomA2
(
M3, HomA1(P2,I 1)
{
∼=†HomA1(P2⊗A2M3,I 1)∼= RHomA1
(
M2⊗L
A2M3,M 1)
in D(A3). The isomorphism∼=†is due to the usual Hom-tensor adjunction. □
Remark 12.10.13. It is not hard to show that D(A) is a closed symmetric
monoidal category, with monoidal operation(−⊗L
A−) and monoidal unit objectA.
It needs just a bit more than Propositions 12.10.9, 12.10.8 and 12.10.12.
For a noncommutative version of this monoidal structure see Remark 14.3.23
and Deﬁnition 15.3.13.
We end this subsection with a weakly-commutative variant of Theorem 12.9.10.
Cohomologically pseudo-noetherian nonpositive DG rings were introduced in Deﬁ-
nition 11.4.37. DG modules with derived bounded below tensor displacement were
deﬁned in Deﬁnition 12.9.5.
Theorem 12.10.14.LetA→B be a homomorphism between weakly commutative
DG rings, and let L ∈D(A) and M,N ∈D(B) be DG modules. There is a
morphism
evR,L
L,M,N : RHomA(L,M )⊗L
BN→RHomA(L,M⊗L
BN)
in D(B), calledderived tensor-evaluation, which is functorial in these DG modules.
Moreover, if conditions(i)-(iii) below hold, thenevR,L
L,M,N is an isomorphism.
(i) The DG ringA is nonpositive and cohomologically pseudo-noetherian, and
L∈D−
f (A).
(ii) The DGB-moduleM is in D+(B).
(iii) The DGB-moduleN has derived bounded below tensor displacement.
Proof. Choose a K-projective resolutionP→L in Cstr(A) and a K-ﬂat resolution
Q→N in Cstr(B). Consider the obvious homomorphism
evP,M,Q : HomA(P,M )⊗BQ→HomA(P,M ⊗BQ)
250
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in Cstr(B). We takeevR,L
L,M,N := Q(evP,M,Q) in D(B). The morphismevR,L
L,M,N does
not depend on the choices, and hence it is functorial.
Now assume that conditions (i)-(iii) hold. Because the restriction functor
D(B)→D(K) is conservative, it is enough to show thatevR,L
L,M,N is an isomor-
phism in D(K). According to Theorem 11.4.40, L is a derived pseudo-ﬁnite DG
A-module (cf. Example 12.9.2). Now we can use Theorem 12.9.10. □
251
Derived Categories | Amnon Yekutieli | 14 Apr 2019
