---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-002-2-cohomological-dimension
section_title: "Cohomological Dimension"
section_number: 2
pages: 11-16
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — We consider commutative DG rings (better known as nonpositive stronglycommutativeassociativeunitalDGalgebras)."
---
WecontinuewiththeconventionsofSection1,namelyourDGringsarenonpos-
itive,andtheDGmodulesareacteduponfromtheleft. Theconcentration con(M)
of a graded moduleM was introduced in Deﬁnition 1.10.
Deﬁnition 2.1.Let A and B be DG rings, and letE⊆ D(A) be a full subcategory.
(1) Let F : E → D(B) be an additive functor, and let[d0, d1] be an integer
interval. We say thatF has cohomological displacement at most[d0, d1] if
con
(
H(F(M))
)
⊆ con
(
H(M)
)
+ [d0, d1]
for everyM∈ E.
(2) Let F : Eop→ D(B) be an additive functor, and let[d0, d1] be an integer
interval. We say thatF has cohomological displacement at most[d0, d1] if
con
(
H(F(M))
)
⊆− con
(
H(M)
)
+ [d0, d1]
for everyM∈ E.
(3) Let Fbeasinitem(1)or(2). The cohomologicaldisplacementof Fisthesmall-
est integer interval[d0, d1] for whichF has cohomological displacement at
most [d0, d1]. Ifd0∈ Z(resp. d1∈ Z,resp. d0, d1∈ Z)then Fissaidtohave
boundedbelow (resp.boundedabove,resp. bounded)cohomologicaldisplacement.
12 AMNON YEKUTIELI
(4) Let [d0, d1] be the cohomological displacement ofF. The cohomological di-
mension of F is d := d1− d0∈ N∪{ ∞}. If d∈ N, then F is said to have
ﬁnite cohomological dimension.
Notethatif E′⊆ E,and F hascohomologicaldisplacementatmost [d0, d1],then
F|E′ also has cohomological displacement at most[d0, d1].
Example 2.2. Consider a commutative ringA = B, and letE := D(A). For the
covariant case (item (1) in Deﬁnition 2.1) take a nonzero projective moduleP, and
let F := HomA(P⊕ P[1],−). Then F has cohomological displacement[0, 1]. For
the contravariant case (item (2)) take a nonzero injective moduleI, and letF :=
HomA(−, I⊕ I[1]). Then F has cohomological displacement[−1, 0]. In both cases
the cohomological dimension ofF is 1.
Remark 2.3. Suppose A and B are rings. If E = D+(A) and F = RF0 (or E =
D−(A) and F = LF0) for some additive functorF0 : Mod A→ Mod B, then the
cohomological dimension ofF is the usual cohomological dimension ofF0.
Assume that E = D(A) and F is a triangulated functor. The functor F has
bounded below (resp. above) cohomological displacement iﬀ it is way-out right
(resp. left), in the sense of [RD, Section I.7].
Deﬁnition 2.4.Let A be a DG ring, letM∈ D(A), and let[d0, d1] be an integer
interval of lengthd := d1− d0.
(1) Given a full subcategoryE⊆ D(A), we say thatM has projective concentra-
tion [d0, d1] and projective dimensiond relative toE if the functor
RHomA(M,−) : E→ D(Z)
has cohomological displacement−[d0, d1] relative toE.
(2) Givenafullsubcategory E⊆ D(A),wesaythat Mhasinjectiveconcentration
[d0, d1] and injective dimensiond relative toE if the functor
RHomA(−, M) : Eop→ D(Z)
has cohomological displacement[d0, d1] relative toE.
(3) Given a full subcategoryE⊆ D(Aop), we say thatM has ﬂat concentration
[d0, d1] and ﬂat dimensiond relative toE if the functor
−⊗ L
A M : E→ D(Z)
has cohomological displacement[d0, d1] relative toE.
Example 2.5.Continuing with the setup of Example 2.2, the DG moduleP⊕ P[1]
(resp. I⊕ I[1])hasprojective(resp.injective)concentration [−1, 0]relativeto D(A).
Example2.6. Let AbeaDGring,andconsiderthefreeDGmodule P := A∈ D(A).
The functor
F := RHomA(P,−) : D(A)→ D(Z)
isisomorphictotheforgetfulfunctor restA/Z,soithascohomologicaldisplacement
[0, 0]andcohomologicaldimension 0relativeto D(A). ThustheDGmodule Phas
projective concentration [0, 0] and projective dimension0 relative to D(A). Note
however that the cohomologyH(P) could be unbounded below.
The interval of generation of a DG module was introduced in Deﬁnition 1.16.
Proposition 2.7. Let M∈ D(A). Assume there is an isomorphismP∼= M in D(A),
where P is a K-ﬂat(resp. K-projective) DG A-module generated in the integer interval
[d0, d1]. ThenMhasﬂat(resp.projective)concentrationatmost [d0, d1]relativeto D(Aop)
(resp. D(A)).
COMMUTATIVE DG RINGS 13
Proof. First consider the K-ﬂat case. Take anyN∈ D(Aop). After applying smart
truncation, we can assume thatcon(N) = con(H(N)). Now N⊗L
A M∼= N⊗A P,
and by Proposition 1.17 the bounds onN⊗A P are as claimed.
Next consider the K-projective case. Take anyN ∈ D(A). As above, we can
assumethat con(N) = con(H(N)). Weknowthat RHomA(M, N)∼= HomA(P, N).
The bounds on the DG moduleHomA(P, N) are as claimed, by Proposition 1.17.
□
Proposition 2.8. If M ∈ D[d0,d1](A), then M has projective concentration at most
[−∞, d1] relative toD(A), injective concentration at most[d0, ∞] relative toD(A), and
ﬂat concentration at most[−∞, d1] relative toD(Aop).
Proof. First let’s assume thatM⁄= 0 and d1 < ∞. We know thatM admits a semi-
free resolutionP→ M with sup(P) = sup(H(M))≤ d1. Now we can use Propo-
sition 2.7 for the ﬂat and projective concentrations.
Now let’s assume thatM⁄= 0 and d0 >−∞. By Proposition 1.19 there is a K-
injective resolutionM→ I with inf(I) = inf(H(M))≥ d0. For anyN∈ D(A) we
have RHomA(N, M)∼= HomA(N, I),andhencetheboundontheinjectiveconcen-
tration. □
Remark 2.9. Let us write <att> for either of the attributes projective, injective or
ﬂat. When A is a ring,E = D0(A) ≈ Mod A and M ∈ Mod A, we recover the
usual deﬁnition of <att> dimension of modules in ring theory. Furthermore, in
the ring case, a DGA-module M has <att> concentration in a bounded integer
interval [d0, d1]relativeto D0(A),iﬀ Misomorphicin D(A)toacomplex Pof<att>
A-modules withcon(P)⊆ [d0, d1]. This implies thatM has ﬁnite <att> dimension
relativeto D(A). Wedonotknowifthis–namelythe<att>dimensionof Mrelative
to D(A) is the same as that relativeD0(A) – is true whenA is a genuine DG ring.
The next two theorems are variations of the opposite (in the categorical sense)
of [RD, Proposition I.7.1], the “Lemma on Way-Out Functors”. The canonical ho-
momorphism A→ ¯A lets us view any¯A-module as a DGA-module.
Theorem 2.10. Let A and B be DG rings, letF, G : D(A)→ D(B) be triangulated
functors, and letη : F→ G be a morphism of triangulated functors. Assume thatηM :
F(M)→ G(M) is an isomorphism for everyM∈ Mod ¯A.
(1) The morphismηM is an isomorphism for everyM∈ Db(A).
(2) If F and G have bounded above cohomological displacements, thenηM is an iso-
morphism for everyM∈ D−(A).
(3) If F and G have ﬁnite cohomological dimensions, thenηM is an isomorphism for
every M∈ D(A).
Proof. (1) The proof is by induction onj := amp(H(M)). If j = 0 then M is iso-
morphic to a shift an object of¯A, so ηM is an isomorphism. Ifj > 0, then using
smart truncation we obtain a distinguished triangleM′→ M→ M′′ ∆− →in D(A)
such thatamp(H(M′′)) < j and amp(H(M′)) < j. Since ηM′′ and ηM′ are isomor-
phisms, so isηM.
(2) Here we assume that F and G have cohomological displacements at most
[−∞, d1] for some integerd1. Take any M∈ D−(A). In order to prove thatηM
is an isomorphism it suﬃces to show that
Hi(ηM) : H i(F(M))→ Hi(G(M))
is bijective for everyi∈ Z.
14 AMNON YEKUTIELI
Fix an integeri. Let M′→ M→ M′′ ∆− →be a distinguished triangle such that
sup(H(M′))≤ i− d1− 2and inf(H(M′′))≥ i− d1− 1. Thiscanbeobtainedusing
smart truncation.
The cohomologies ofF(M′) and G(M′) are concentrated in the degree range
≤ i− 2. Thedistinguishedtriangleinducesacommutativediagramof ¯A-modules
with exact rows:
Hi(F(M′)) //
Hi(ηM′ )

Hi(F(M)) //
Hi(ηM)

Hi(F(M′′)) //
Hi(ηM′′ )

Hi+1(F(M′))
Hi+1(ηM′ )

Hi(G(M′)) // Hi(G(M)) // Hi(G(M′′)) // Hi+1(G(M′)) .
The four terms involvingM′ are zero. Since M′′ has bounded cohomology, we
know by part (1) thatHi(ηM′′ ) is an isomorphism. ThereforeHi(ηM) is an isomor-
phism.
(3)Hereweassumethat Fand Ghaveﬁnitecohomologicaldimensions. So Fand G
havecohomologicaldisplacementsatmost [d0, d1]forsome d0≤ d1 in Z. Takeany
M∈ D(A),andﬁx i∈ Z. Wewanttoshowthat Hi(ηM)isanisomorphism. Using
smart truncations ofM we obtain a distinguished triangleM′ → M→ M′′ ∆− →
in D(A), such thatsup(H(M′))≤ i− d0 + 1 and inf(H(M′′))≥ i− d0 + 2. The
cohomologies ofF(M′′) and G(M′′) are concentrated in degrees≥ i + 2. We have
a commutative diagram of¯A-modules with exact rows:
Hi−1(F(M′′)) //
Hi−1(ηM′′ )

Hi(F(M′)) //
Hi(ηM′ )

Hi(F(M)) //
Hi(ηM)

Hi(F(M′′))
Hi(ηM′′ )

Hi−1(G(M′′)) // Hi(G(M′)) // Hi(G(M)) // Hi(G(M′′))
Thefourtermsinvolving M′′ arezerohere. Since M′ hasboundedabovecohomol-
ogy, we know by part (2) thatHi(ηM′ ) is an isomorphism. ThereforeHi(ηM) is an
isomorphism. □
Theorem 2.11. Let A and B be DG rings, letF, G : D(A)→ D(B) be triangulated
functors, and letη : F→ G be a morphism of triangulated functors. Assume thatA is
cohomologically left pseudo-noetherian, andηA : F(A)→ G(A) is an isomorphism.
(1) If F and G have bounded above cohomological displacements, thenηM : F(M)→
G(M) is an isomorphism for everyM∈ D−
f (A).
(2) If Fand Ghaveﬁnitecohomologicaldimensions,then ηM : F(M)→ G(M)isan
isomorphism for everyM∈ Df(A).
Proof. Step1. ConsideraﬁnitefreeDG A-module P,i.e. P∼=
⨁r
k=1 A[−ik]in C(A)
for some i1, . . . , ir∈ Z. Because the functorsF, G are triangulated, andηA is an
isomorphism, it follows thatηP is an isomorphism.
Step2. Nowlet Pbeaﬁnitesemi-freeDG A-module,withﬁnitesemi-freeﬁltration
{νj(P)} of length j1 (see Deﬁnition 1.13). We prove thatηP is an isomorphism by
induction onj1. For j1 = 0 this is step 1. Now assumej1≥ 1. WriteP′ := νj1−1(P)
and P′′ := grν
j1
(P), so there is a distinguished triangleP′→ P→ P′′ ∆− →in D(A).
According to step 1 and the induction hypothesis, the morphismsηP′′ and ηP′ are
isomorphisms. Hence ηP is an isomorphism.
Step 3. Here we assume thatF and G have cohomological displacements at most
[−∞, d1]forsomeinteger d1. Takeany M∈ D−
f (A). Inordertoprovethat ηM isan
COMMUTATIVE DG RINGS 15
isomorphism it suﬃces to show that
Hi(ηM) : H i(F(M))→ Hi(G(M))
is bijective for everyi∈ Z.
We may assume thatM is nonzero. Leti1 := sup(H(M)), which is an integer.
There exists a pseudo-ﬁnite semi-free resolutionP→ M such that sup(P) = i1;
see Proposition 1.19. We will prove thatHi(ηP) is an isomorphism for everyi. Fix
a pseudo-ﬁnite semi-free ﬁltration{νj(P)} of P.
Takeaninteger j,anddeﬁne P′ := νj(P)and P′′ := P/νj(P). Sothereisadistin-
guished triangleP′→ P→ P′′ ∆− →in D(A). The DG moduleP′′ is concentrated in
thedegreerange ≤ i1− j− 1,andhencesoisitscohomology. Thusthecohomolo-
gies of F(P′′) and G(P′′) are concentrated in the degree range≤ i1− j− 1 + d1,
or in other wordsHi(F(P′′)) = Hi(G(P′′)) = 0 for alli > i1− j− 1 + d1. On the
other hand the DG moduleP′ is ﬁnite semi-free. The distinguished triangle above
induces a commutative diagram of¯A-modules with exact rows:
(2.12) Hi−1(F(P′′)) //
Hi−1(ηP′′ )

Hi(F(P′)) //
Hi(ηP′ )

Hi(F(P)) //
Hi(ηP)

Hi(F(P′′))
Hi(ηP′′ )

Hi−1(G(P′′)) // Hi(G(P′)) // Hi(G(P)) // Hi(G(P′′))
For any i > i1 + d1− j the modules in this diagram involvingP′′ are zero. By
step 2 we know thatHi(ηP′ ) is an isomorphism for everyi. ThereforeHi(ηP) is an
isomorphism for everyi > i1 + d1− j. Since j can be made arbitrarily large, we
conclude thatHi(ηP) is an isomorphism for everyi.
Step 4. Here we assume thatF and G have ﬁnite cohomological dimensions. SoF
and G have cohomological displacements at most[d0, d1] for some d0≤ d1 in Z.
This step is very similar to the proof of Theorem 2.10(3).
Take anyM∈ Df(A). Fix i∈ Z. We want to show thatHi(ηM) is an isomor-
phism. Using smart truncations ofM, we obtain a distinguished triangleM′→
M→ M′′ ∆− →in Df(A), such thatM′∈ D[−∞,i−d0+1]
f (A) and M′′∈ D[i−d0+1,∞]
f (A).
Wegetacommutativediagramlike(2.12). Themodules Hi−1(F(M′′)), Hi(F(M′′)),
Hi−1(G(M′′)) and Hi(G(M′′)) are zero. Since M′ ∈ D−
f (A), step 3 says that
Hi(ηM′ ) is an isomorphism. ThereforeHi(ηM) is an isomorphism. □
The next theorem is a variant of the opposite of [RD, Proposition I.7.3]. For a
boundedness condition⋆, we denote by−⋆ the opposite boundedness condition.
Thus ifD⋆ denotes eitherD, D+, D− or Db, thenD−⋆ denotes eitherD, D−, D+ or
Db respectively.
Theorem 2.13.Let Aand BbeDGrings, andlet F : D(A)op→ D(B)beatriangulated
functor. Assume thatA and B are cohomologically left pseudo-noetherian, andF(A)∈
D+
f (B).
(1) If F has bounded below cohomological displacement, thenF(M) ∈ D+
f (B) for
every M∈ D−
f (A).
(2) If F has ﬁnite cohomological dimension, thenF(M)∈ D−⋆
f (B) for every M∈
D⋆
f (A).
Proof. The proof is very similar to that of Theorem 2.11. We just outline the neces-
sary changes.
16 AMNON YEKUTIELI
Steps 1-2. P is a ﬁnite semi-free DGA-module. By induction on the lengthj1 of a
semi-free ﬁltration, we prove thatF(P)∈ D+
f (B).
Step 3. HereF has cohomological displacement[d0, ∞] for somed0∈ Z, andM∈
D−
f (A). Let P→ M be a pseudo-ﬁnite semi-free resolution, withsup(P) = i1.
Take anyj∈ Z, and consider the distinguished triangleP′→ P→ P′′ ∆− →where
P′ := νj(P). There is an exact sequence of¯B-modules
(2.14) Hi−1(F(P′′)) // Hi(F(P′)) // Hi(F(P)) // Hi(F(P′′)).
By step 2 we know thatHi(F(P′))∈ Modf ¯B for every i. If i≤ d0− i1 + j then
Hi−1(F(P′′)) = Hi(F(P′′)) = 0. Therefore Hi(F(P))∈ Modf ¯B. But j can be made
arbitrarily large. This proves thatF(M)∈ Df(B). But on the other hand we know
that Hi(F(M)) = 0 for alli <−i1 + d0. We conclude thatF(M)∈ D+
f (B).
Step4. Here Fhascohomologicaldisplacementatmost [d0, d1]forsome d0≤ d1 in
Z, M∈ Df(A), andi∈ Z. We truncateM to obtain a distinguished triangleM′→
M→ M′′ ∆− →in Df(A), such thatM′∈ D[−∞,j+1]
f (A) and M′′ ∈ D[j+1,∞]
f (A) for
j := i− d1− 3. Wegetanexactsequencelike(2.14). Themodules Hi−1(F(M′′))and
Hi(F(M′′)) are zero, andHi(F(M′))∈ Modf ¯B by step 3. ThereforeHi(F(M))∈
Modf ¯B. The condition on the boundedness ofH(F(M)) is established like in step
3. □
