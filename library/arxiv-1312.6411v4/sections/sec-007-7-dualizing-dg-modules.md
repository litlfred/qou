---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-007-7-dualizing-dg-modules
section_title: "Dualizing DG Modules"
section_number: 7
pages: 35-43
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — We consider commutative DG rings (better known as nonpositive stronglycommutativeassociativeunitalDGalgebras)."
---
Recall that all our DG rings are now commutative (Convention 4.2), and¯A =
H0(A). In this section we concentrate on cohomologically pseudo-noetherian DG
rings (Deﬁnition 1.18).
Here is a generalization of Grothendieck’s deﬁnition of dualizing complex.
When A is a ring, this is identical to the deﬁnition in [RD, Section V.2].
Deﬁnition 7.1.Let A be a cohomologically pseudo-noetherian DG ring. A DG
A-module R is called adualizingif it satisﬁes these three conditions:
(i) Each Hi(R) is a ﬁnite¯A-module.
(ii) R has ﬁnite injective dimension relative toD(A).
(iii) Theadjunctionmorphism A→ RHomA(R, R)in D(A)isanisomorphism.
In other words, condition (i) says thatR∈ Df(A); condition (ii) says that the
functor RHomA(−, R) has ﬁnite cohomological dimension relative toD(A), as in
Deﬁnitions 2.1 and 2.4(2); and condition (iii) says that the canonical graded ring
homomorphism
H(A)→
⨁
k∈Z
HomD(A)(R, R[k])
36 AMNON YEKUTIELI
is bijective.
Proposition 7.2. Suppose R is a dualizing DG module overA, and consider the functor
D := RHomA(−, R) : D(A)→ D(A).
Let D⋆ denote eitherD, Db, D+ or D−; and correspondingly letD−⋆ denote eitherD, Db,
D− or D+.
(1) For anyM∈ D⋆
f (A) we haveD(M)∈ D−⋆
f (A). In particular,R∈ D+
f (A).
(2) For any M∈ Df(A) the canonical morphismM→ D(D(M)) in Df(A) is an
isomorphism.
(3) The functor
D : D⋆
f (A)op→ D−⋆
f (A)
is an equivalence of triangulated categories.
Proof. (1)Thefunctor Dhasﬁnitecohomologicaldimension,sowecanapplyThe-
orem 2.13(2). SinceA∈ D−
f (A), we getR = D(A)∈ D+
f (A).
(2)Thereisamorphismoftriangulatedfunctors η : id Df(A)→ D◦ D. Bothfunctors
have ﬁnite cohomological dimensions, andηA is an isomorphism. We can apply
Theorem 2.11(2).
(3) Combine items (1) and (2). □
Corollary 7.3. Let A be a cohomologically pseudo-noetherian DG ring, and letR be a
dualizing DGA-module. The following two conditions are equivalent:
(i) The DG ringA is cohomologically bounded.
(ii) The DG moduleR is cohomologically bounded.
Proof. This is by Proposition 7.2, sinceR∼= D(A) and A∼= D(R). □
In Example 7.26 we demonstrate the unbounded option.
Given a homomorphismf : A→ B of DG rings, we denote by¯f := H0( f ) the
induced ring homomorphism.
Deﬁnition 7.4.Let f : A → B be a homomorphism between cohomologically
pseudo-noetherian DG rings. We say thatf is acohomologically pseudo-ﬁnite homo-
morphism if ¯f : ¯A→ ¯B is a ﬁnite ring homomorphism, i.e.¯f makes ¯B into a ﬁnite
¯A-module.
Clearly iff is cohomologically ﬁnite, thenrest f sends D⋆
f (B) into D⋆
f (A), where
⋆ is either+,−, bor blank.
Proposition 7.5. Let f : A → B be a cohomologically pseudo-ﬁnite homomorphism
between cohomologically pseudo-noetherian DG rings.
(1) If RA is a dualizing DGA-module, thenRB := RHomA(B, RA) is a dualizing
DG B-module.
(2) If f is a quasi-isomorphism andRB is a dualizing DGB-module, then RA :=
rest f (RB) is a dualizing DGA-module.
Proof. (1) The proof is almost the same as in the case of a ring; see [RD, Propo-
sition V.2.4]. Viewing B as an object ofD−
f (A), Proposition 7.2(1) tells us that
RB∈ D+
f (A); and henceRB∈ D+
f (B). For anyN∈ D(B) we have
RHomB(N, RB)∼= RHomA(N, RA)
by adjunction, and hence the injective dimension ofRB relative toD(B) is at most
the injective dimension of A relative toD(A), which is ﬁnite. And ﬁnally
RHomB(RB, RB)∼= RHomA
(
RHomA(B, RA), RA
)∼= B
COMMUTATIVE DG RINGS 37
by Proposition 7.2(2). These isomorphisms are actually insideD(B), and they are
compatible with the canonical morphism fromB.
(2)Thisisbecausehere rest f : D(B)→ D(A)isanequivalence,preservingbound-
edness and ﬁniteness of cohomology. □
In commutative ring theory, many good properties of a ringA can be deduced
ifitis“notfar”froma“nice”ringK(suchasaﬁeld). Thisistheunderlyingreason
for the next deﬁnition.
Recallthataringhomomorphism A→ Biscalledof essentiallyﬁnitetypeifitcan
befactoredas A→ Bft→ B,where A→ Bftisﬁnitetype(i.e. Bisﬁnitelygenerated
as A-ring), and Bft→ B is the localization at some multiplicatively closed subset
of Bft.
Deﬁnition 7.6.Let K be a noetherian ring, letA be a cohomologically pseudo-
noetherianDGring,andlet u : K→ AahomomorphismofDGrings. Wesaythat
u is ofcohomologically essentially ﬁnite type, and thatA is acohomologically essentially
ﬁnite type DGK-ring, if the ring homomorphism¯u : K→ ¯A is of essentially ﬁnite
type.
Deﬁnition 7.7.A DG ring A is called tractable if it is cohomologically pseudo-
noetherian, and there exists a cohomologically essentially ﬁnite type homomor-
phism K→ A from some ﬁnite dimensional regular noetherian ringK. Such a
homomorphism K→ A is called atractionfor A.
Lemma7.8. Let AbeaDGring,let Kbeanoetherianring,andsupposethereisacohomo-
logically essentially ﬁnite type homomorphismu : K→ A. Then there is a commutative
diagram of DG rings
K u //
v

A π //
f

¯A
Aeft
g // Aloc
==
suchthat πisthecanonicalhomomorphism ; f and garequasi-isomorphism;and K→ A0
eft
is essentially ﬁnite type.
Proof. Let S := π−1( ¯A×)∩ A0, namely s∈ S iﬀπ(s) is invertible in the ring¯A.
Deﬁne the DG ringAloc := ( S−1· A0)⊗A0 A. Then π factors via f, and f is a
quasi-isomorphism.
Since K→ ¯Aisessentiallyﬁnitetype, thereisapolynomialring K[t]inﬁnitely
many variables of degree0, and a homomorphismh : K[t]→ ¯A which is essen-
tially surjective, i.e. it is surjective after a localization. Thus, lettingT := h−1( ¯A×)
⊆ K[t], and deﬁningA0
eft := T−1· K[t], the homomorphism hT : A0
eft → ¯A is
surjective.
Now the ringA0
eft is noetherian. The homomorphismhT : A0
eft→ ¯A factors via
a homomorphism g0 : A0
eft → A0
loc, and the composed homomorphismA0
eft →
H0(Aloc) is surjective. Since the the modulesHi(Aloc) are ﬁnite overA0
eft, we can
extend A0
efttoaDGring Aeft,andsimultaneouslyextend g0toaquasi-isomorphism
g : Aeft→ Aloc, by inductively introducing ﬁnitely many new variables (free ring
generators) in negative degrees. The process is the same as in the proof of [YZ1,
Proposition 1.7(2)]. □
Theorem 7.9. Let A be a tractable DG ring. ThenA has a dualizing DG module.
Proof. Let K→ Abeatractionfor A. Considerthediagramofhomomorphismsin
Lemma 7.8. SinceA→ Aloc is a quasi-isomorphism, andA0
eft→ Aeft→ Aloc are
38 AMNON YEKUTIELI
cohomologicallypseudo-ﬁnite,itsuﬃces(byProposition7.5)toshowthat A0
eft has
a dualizing DG module (which is the same as a dualizing complex over this ring,
in the sense of [RD]). But the ring homomorphismK→ A0
eft can be factored into
K→ K[t]→ B→ A0
eft, whereK[t] is a polynomial ring inn variables, K[t]→ B
is surjective, andB→ A0
eft is a localization. Thus, using [RD, Theorem V.8.3] and
Proposition 7.5(1) above, the DG module
A0
eft⊗B RHomK[t](B, Ωn
K[t]/K[n])
is a dualizing DG module overA0
eft. □
Theorem 7.10. Let A be a cohomologically pseudo-noetherian DG ring, and letR be a
dualizing DG module overA.
(1) If P is a tilting DG module, thenP⊗L
A R is a dualizing DG module.
(2) If R′isadualizingDGmodule,then P := RHomA(R, R′)isatiltingDGmodule,
and R′∼= P⊗L
A R in D(A).
(3) If P is a tilting DG module, and ifR∼= P⊗L
A R in D(A), thenP∼= A in D(A).
This issimilar to[RD, Theorem V.3.1], and thestrategy of theproof isthe same;
cf. also [Ye2, Theorem 4.5].
Proof. (1) Assume P is a tilting DG module, and letR′ := P⊗L
A R. According
to Corollary 6.8 the functorP⊗L
A− is an auto-equivalence ofD(A), it has ﬁnite
cohomological dimension, and it preservesD+
f (A). Therefore the DG moduleR′
is dualizing.
(2)Deﬁnetheobjects P := RHomA(R, R′)and P′ := RHomA(R′, R),andthefunc-
tors D := RHomA(−, R), D′ := RHomA(−, R′), F := P⊗L
A− and F′ := P′⊗L
A−.
We know that the functorsD, D′, D′◦ D, D◦ D′ have ﬁnite cohomological dimen-
sionsrelativeto D(A); theDGmodules P, P′∈ D−
f (A); and thefunctorsF, F′ have
boundedabovecohomologicaldisplacementsrelativeto D(A). Forany M∈ D(A)
there is a canonical morphism
RHomA(R, R′)⊗L
A M→ RHomA(RHomA(M, R), R′),
so we get a morphism of triangulated functorsη : F→ D′◦ D. By deﬁnitionηA
is an isomorphism, and Theorem 2.11(1) says thatηM is an isomorphism for every
M∈ D−
f (A). Likewise there is an isomorphismη′
M : F′(M)→ (D◦ D′)(M) for
every M∈ D−
f (A).
Let us calculateP⊗L
A P′ :
P⊗L
A P′∼= F(P′)∼= (D′◦ D)(P′)
∼= (D′◦ D)(F′(A))∼= (D′◦ D◦ D◦ D′)(A)∼= A.
This provesP is tilting. And
P⊗L
A R∼= F(R)∼= (D′◦ D)(D(A))∼= D′(A)∼= R′.
(3) IfP is tilting andR∼= P⊗L
A R, then
A∼= RHomA(R, R)∼= RHomA(P⊗L
A R, R)
∼=∗ RHomA(P, RHomA(R, R))∼= RHomA(P, A),
where the isomorphism∼=∗ is by adjunction. But then
P∼= A⊗L
A P∼= RHomA(P, A)⊗L
A P∼=† RHomA(P, P)∼=†† A,
where the isomorphism∼=† is by a combination of Theorems 6.5 and 5.20, and the
isomorphism∼=†† is by Theorem 6.5. □
COMMUTATIVE DG RINGS 39
Corollary 7.11. Assume A has some dualizing DG module. The formulaR↦→ P⊗L
A R
induces a simply transitive action of the groupDPic(A) on the set of isomorphism classes
of dualizing DGA-modules.
Proof. Clear from the theorem. □
Corollary 7.12. Assume A has some dualizing DG module(e.g. A is tractable). The
formula R↦→ RHomA( ¯A, R) induces a bijection
{dualizing DGA-modules}
isomorphism
≃− →{dualizing DG ¯A-modules}
isomorphism .
Proof. By Corollary 7.11 the actions of the groupsDPic(A) and DPic( ¯A) on these
two sets, respectively, are simply transitive. And by Theorem 6.14 the group ho-
momorphism DPic(A)→ DPic( ¯A) induced byP↦→ ¯A⊗L
A P is bijective. Thus it
suﬃces to prove that the function induced byR↦→ RHomA( ¯A, R) is equivariant
for the action ofDPic(A). Here is the calculation:
RHomA( ¯A, P⊗L
A R)∼=‡ P⊗L
A RHomA( ¯A, R)
∼= ( ¯A⊗L
A P)⊗L
¯A RHomA( ¯A, R).
The isomorphism∼=‡ comes from Lemma 7.13 below, noting that the tilting DG
module P satisﬁes condition (∗) of the lemma, since it is perfect. □
We say that a DGA-module N has bounded below generationif it is generated in
the integer interval[i0, ∞] for some integeri0; see Deﬁnition 1.16.
Lemma 7.13. Let L∈ D−
f (A) and M, N∈ D+(A). Assume thatN satisﬁes this condi-
tion:
(∗) There is a covering sequence(s1, . . . , sn) of ¯A, and for everyi there is an isomor-
phism Asi⊗A N ∼= ˜Ni in D(Asi ), where ˜Ni is a K-ﬂat DGAsi-module with
bounded below generation.
Then the canonical morphism
ψL,M,N : RHom A(L, M)⊗L
A N→ RHomA(L, M⊗L
A N)
in D(A), from formula(5.5), is an isomorphism.
Proof. Step 1. Here we assume thatN∼= ˜N in D(A), where ˜N is a K-ﬂat DGA-
module of bounded below generation. Using smart truncation if needed, we can
assume that the DGB-module M is bounded below. Let ˜L → L be a pseudo-
ﬁnite semi-free resolution overA (see Proposition 1.19). The morphismψL,M,N is
represented by the homomorphism
˜ψ ˜L,M, ˜N : Hom A( ˜L, M)⊗A ˜N→ HomA( ˜L, M⊗A ˜N)
in C(A). Because the semi-free DGA-module ˜L is bounded above and has ﬁnitely
manybasiselementsineachdegree,andboth Mand M⊗A ˜N areboundedbelow,
we see that˜ψ ˜L,M, ˜N is bijective.
Step 2. HereN satisﬁes condition (∗). We claim that the obvious morphisms
(7.14)
(
RHomA(L, M)⊗L
A N
)
⊗A0 A0
si→ RHomA(L, M)⊗L
A ˜Ni
and
(7.15) RHomA(L, M⊗L
A N)⊗A0 A0
si→ RHomA(L, M⊗L
A ˜Ni)
40 AMNON YEKUTIELI
in D(A), that come from the given isomorphismsAsi⊗A N ≃− →˜Ni, are isomor-
phisms. That (7.14) is an isomorphism is trivial. As for the morphism (7.15): con-
dition (∗) implies thatM⊗L
A N belongs toD+(A). Since A0
si is a K-ﬂat DG module
over A0 generated in degree0, we can use Step 1.
Step 3. Now we are in the general situation. Letψi be the morphism gotten from
ψL,M,N bythelocalization A0
si⊗A0−,so ψi goesfromtheﬁrstobjectin(7.14)tothe
ﬁrst object in (7.15). Since¯A→ ∏i ¯Asi is faithfully ﬂat, it suﬃces to prove that all
the ψi are isomorphisms. But by step 2 it suﬃces to show that
ψL,M, ˜Ni : RHom A(L, M)⊗L
A ˜Ni→ RHomA(L, M⊗L
A ˜Ni)
is an isomorphism. Since˜Ni is a K-ﬂat DGA-module with bounded below gener-
alization, we can use step 1. □
Corollary 7.16. If the ring ¯A is local, then any two dualizing DGA-modules R and R′
satisfy R′∼= R[m] for some integerm.
Proof. By Corollary 6.17 we haveDPic(A) ∼= Z, generated by the class ofA[1].
Now use Corollary 7.11. □
Proposition7.17. Let AbeacohomologicallynoetherianDGring,andlet Rbeadualizing
DG A-module. Assume A is cohomologically bounded. ThenR is dualizing in the sense
of [FIJ, Deﬁnition 1.8].
Proof. There are four conditions in [FIJ, Deﬁnition 1.8]. Condition (1) – the exis-
tence of resolutions – is trivial in our commutative situation. Condition (2) says
that if M∈ Db
f (A) then RHomA(M, R)∈ Db
f (A); and this is true by Proposition
7.2(1). Condition (3) requires that for anyM∈ Db
f (A), letting N be either M or
M⊗L
A R, the adjunction morphisms
N→ RHomA
(
RHomA(N, R), R
)
are isomorphisms. Now by Corollary 7.3 we know thatR∈ Db
f (A). A combina-
tionofProposition2.8andTheorem2.13(1)tellsusthat M⊗L
A R∈ D−
f (A). Thusin
bothcases N∈ D−
f (A),andaccordingtoProposition7.2(2)themorphisminques-
tion is an isomorphism. Condition (4) is part of condition (3) in the commutative
situation. □
Deﬁnition7.18.AcohomologicallynoetheriancohomologicallyboundedDGring
A is calledGorensteinif the DG moduleA has ﬁnite injective dimension relative to
D(A).
Proposition 7.19. Let A be a cohomologically noetherian cohomologically bounded DG
ring. The following conditions are equivalent:
(i) A is Gorenstein.
(ii) The DGA-module A is dualizing.
Proof. Since conditions (i) and (iii) of Deﬁnition 7.1 are automatic forR := A, this
is clear. □
Remark 7.20. For DG rings that are not cohomologically bounded, a comparison
likeinProposition7.17doesnotseemtoworknicely. Corollary7.16isverysimilar
to [FIJ, Theorem III]; but of course the assumptions are not the same.
We do not know a reasonable deﬁnition of Gorenstein DG rings that are not
cohomologically bounded.
Here is a rather surprising result, that was pointed out to us by Jørgensen.
COMMUTATIVE DG RINGS 41
Theorem 7.21. Let A be a DG ring, which is cohomologically bounded and cohomologi-
cally essentially ﬁnite type over some noetherian ringK. If ¯A is a perfect DGA-module,
then the canonical homomorphismA→ ¯A is a quasi-isomorphism.
Example 7.26 shows that the assumption thatA is cohomologically bounded is
really needed.
Proof. We will prove that¯Ap⊗ ¯A Hi(A) = 0 for everyi < 0 and everyp∈ Spec ¯A.
Fix such i and p. Because the assertion is invariant under DG ring quasi-iso-
morphisms, we may assume, by Lemma 7.8 (replacingA with Aeft), that A0 is a
noetherian ring. Consider the ringA0
p := ˜S−1· A0, whereπ : A→ ¯A is the canon-
ical homomorphism,S := ¯A− p, and ˜S := π−1(S)∩ A0. Next deﬁne the DG ring
Ap := A0
p⊗A0 A. Then A0
p→ ¯Ap is surjective, andA0
p is a noetherian local ring.
By Proposition 5.3(2) the DGAp-module ¯Ap∼= Ap⊗A ¯A is perfect; and by Theo-
rem 5.20 this is a compact object ofD(Ap). Also ¯Ap is nonzero. According to [Jo,
Theorem 0.2] we haveamp(H(Ap))≤ amp(H( ¯Ap)) = 0. Therefore Hi(Ap) = 0
for alli < 0. ButHi(Ap)∼= ¯Ap⊗ ¯A Hi(A). □
We conclude this section with several examples and remarks.
Example 7.22. Suppose A is a Gorenstein noetherian ring, anda = ( a1, . . . , an)
is a sequence of elements inA. Let B := K(A; a), the Koszul complex, which is
cohomologically noetherian and cohomologically bounded. The DG ring homo-
morphism A→ B is cohomologically pseudo-ﬁnite,RA := A[n] is a dualizing DG
A-module,andhence RB := RHomA(B, RA)isadualizingDG B-module. ButBis
semi-free as DGA-module, and therefore
RB = RHomA(B, A[n])∼= HomA(B, A[n])∼= B
in D(B). We see thatB is Gorenstein, in the sense of Deﬁnition 7.18.
Example 7.23. Here is a comparison to Hinich’s notion of dualizing DG mod-
ule from [Hi1]. LetA be a noetherian local ring, with maximal idealm. For the
sake of simplicity, let us assume thatA contains a ﬁeldK, such thatK→ A/m
is ﬁnite. Leta = ( a1, . . . , an) be a sequence of elements inA that generates an
m-primary ideal, and letB := K(A; a) be the associated Koszul complex. Thus
K→ B is a cohomologically pseudo-ﬁnite homomorphism of DG rings, and ac-
cordingtoProposition7.5theDG B-module RB := HomK(B, K)isdualizing. Now
HomK
(
H(RB), K
) ∼= H(B) as graded H(B)-modules, so RB is a dualizing DG
module in the sense of Hinich. Taking Corollary 7.16 into consideration, we see
thatanydualizingDG B-module R(inoursense)satisﬁestheconditionofHinich.
Remark 7.24. The results in our paper so far suggest an analogy between the fol-
lowing two scenarios:
(dg) The DG scenario: a cohomologically pseudo-noetherian DG ringA, with
reduction ¯A := H0(A).
(ad) The adic scenario: a noetherian ringA, a-adically complete w.r.t. an ideala,
with reduction ¯A := A/a.
Werefertothisasthe DGvs.adicanalogy . Thisanalogyrestrictstothe“degenerate
cases” in these scenarios:
(dg) The cohomologyH(A) is bounded.
(ad) The deﬁning ideala is nilpotent.
Of course, this observation is not new (cf. [Lu1], [Lu2], [TV] and [AG]).
The DG vs. adic analogy holds also for “ﬁnite homomorphisms”:
42 AMNON YEKUTIELI
(dg) A cohomologically pseudo-ﬁnite homomorphismf : A→ B between co-
homologically pseudo-noetherian DG rings (Deﬁnition 7.4).
(ad) Aformallyﬁniteorpseudo-ﬁnitehomomorphism f : A→ Bbetweenadically
complete noetherian rings, as in [Ye1] and [AJL2] respectively.
There is a further analogy between “dualizing objects” in the two scenarios:
(dg) A dualizing DG moduleR over a cohomologically pseudo-noetherian DG
ring A (Deﬁnition 7.1).
(ad) A t-dualizing complexR over an adically complete noetherian ringA, as in
[Ye1] and [AJL1].
The analogies above raise two questions:
(1) Is there a DG analogue of thec-dualizing complexof [AJL1]?
(2) Is there a DG analogue of theGM Dualityof [AJL1] and theMGM Equiva-
lenceof [PSY]?
Remark 7.25. Recall that a noetherian ringA of ﬁnite Krull dimension is regular
(i.e. all its local ringsAp are regular) iﬀ it has ﬁnite global cohomological dimen-
sion.
Now suppose A is a cohomologically pseudo-noetherian DG ring. By “Krull
dimension” we could mean that of¯A, but “regular local ring” has no apparent
meaning here. Hence we propose this deﬁnition:A is calledregular if it hasﬁnite
global cohomological dimension. By this we mean that there is a natural numberd,
such that ifM∈ C(A) is generated in the integer interval[i0, i1], then M has pro-
jective dimension at mostd + i1− i0; cf. Deﬁnitions 1.16 and 2.4, and Examples
2.5 and 2.6. According to Theorem 5.11, we see that anyM∈ Db
f (A), including
M = ¯A, is perfect.
Now assume thatA is a regular DG ring, but withbounded cohomology. Then,
taking M = ¯A, Theorem 7.21 says thatA→ ¯A is a quasi-isomorphism. The con-
clusion is thatthe only regular DG rings with bounded cohomology are the regular rings
(up to quasi-isomorphism).
Under the DG vs. adic analogy of Remark 7.24, this corresponds to an adic ring
A with a nilpotent deﬁning ideala. If A is regular, then it cannot have nonzero
nilpotent elements. Thereforea = 0 here, andA→ ¯A is bijective.
Example7.26. Takeaﬁeld K,andlet A := K[t],thepolynomialringinavariable t
of degree−2. We viewA as a DG ring with zero diﬀerential, soH(A)∼= A, and it
is cohomologically noetherian, but not cohomologically bounded below. The DG
ring homomorphismK→ A is cohomologically pseudo-ﬁnite. Hence the DGA-
module R := HomK(A, K) is dualizing. This DG module is not bounded above.
Notethathere ¯A∼= KisaperfectDG A-module. Toshowthis,weshallproduce
a ﬁnite semi-free resolution of¯A. The DG moduleA≤−2, which is both the stupid
andthesmarttruncationof Aat−2, isfree, sinceA≤−2∼= A[2]asDG A-modules.
Let φ : A≤−2→ A be the inclusion, and letP := cone(φ). There is an obvious
quasi-isomorphism P→ ¯A.
The adic analogue is the ring of formal power seriesA := K[[t]], with ideal of
deﬁnitiona := ( t). Thecorrespondingt-dualizingcomplexis R := Homcont
K (A, K),
which is an artinianA-module of inﬁnite length.
Remark7.27. OurdeﬁnitionofdualizingDGmodules,Deﬁnition7.1,mightseem
an almost straightforward generalization of Grothendieck’s original deﬁnition in
[RD]. Howeverthereareatleasttwosubtlepoints: (a)Findingthecorrectnotionof
injective dimension of a DG module (condition (ii) of Deﬁnition 7.1). (b) Allowing
a dualizing DG module to have unbounded above cohomology (condition (i) of
Deﬁnition 7.1; cf. Corollary 7.3 and Remark 7.24).
COMMUTATIVE DG RINGS 43
All results in this section, up to and including Corollary 7.11, might also seem
to be straightforward generalizations of Grothendieck’s corresponding results in
[RD]. Butthetechnicaldiﬃculties(mainlywhen Aiscohomologicallyunbounded)
cannot be neglected.
We should mention that Theorem 7.9 can be made a bit stronger, by replacing
the condition thatA is tractable with the weaker condition that there is a cohomo-
logically essentially ﬁnite type homomorphismK→ A, whereK is a noetherian
ring with a dualizing complex. Theorem 7.21 can be similarly strengthened.
Some earlier papers, notably [Hi1] and [FIJ], had adopted other deﬁnitions of
dualizing DG modules; see Example 7.23 and Proposition 7.17 respectively. These
deﬁnitions are not consistent with our deﬁnition in general, and there does not
appear to be a well-developed theory for them.
In[Lu2,Deﬁnition4.2.5],Luriegivesadeﬁnitionofadualizing E∞ moduleover
an E∞ ring. Now any DG ringA can be viewed as anE∞ ring, and DGA-modules
canbeviewed E∞ A-modules. Underthiscorrespondence,itseemsthatadualizing
DG A-module, in the sense of Deﬁnition 7.1 above, becomes a dualizing module
in the sense of [Lu2]. (We are being careful, because a precise comparison of the
deﬁnitions is not so easy.) Thus our results in this section, up to and including
Corollary 7.11, might be viewed as special instances of Lurie’s statements. Still, an
attempttoproduceafullproofofourresultsbasedonthecorrespondingresultsin
[Lu2](e.g.deducingourTheorem7.9from[Lu2,Theorem4.3.14],ordeducingour
Theorem7.10from[Lu2, Proposition4.2.9])mightbenontrivial, andmostlikelyit
would be longer than our own direct proofs. This is because, as far as we know,
theredonotexistfullcomparisonresultsforthemonoidaloperationsbetweenthe
E∞ and the DG setups.
OurCorollary7.12appearstobetotallynew. Wecouldnotﬁndanythingresem-
blingitinLurie’spapers,norelsewhereintheliterature. LikewiseforTheorem7.21
(except for Jørgensen’s original local result).
Remark 7.28.AresultthatisnoticeablymissingfromourpaperisaDGanalogue
of[Lu2,Theorem4.3.5]. TranslatedtotheDGterminology,itstatesthatifthering ¯A
admitsadualizingDGmodule,thentheDGring AadmitsadualizingDGmodule.
We do not know whether this result can be proved within the DG framework; this
is a question that we ﬁnd interesting.
Note however that the corresponding result in the adic case, namely whenA is
acomplete a-adicringextensionof ¯A(cf.Remark7.24),wasprovedalongtimeago
byFaltings[Fa]. Theproofofthenilpotentcasein[Fa]isquiteeasy;butthepassage
tothecompleteadiccaseissomewhatinvolvedthere. Theproofcanbegreatlysim-
pliﬁed by ﬁrst proving the existence of a t-dualizing complexR′
A over A, and then
applying derived completion to obtain a c-dualizing complexRA := LΛa(R′
A).
See [Ye1] [AJL1], [AJL2] and [PSY] for information on derived completion, and on
dualizing complexes over adic rings.
