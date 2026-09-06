---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-003-3-reduction-and-lifting
section_title: "Reduction and Lifting"
section_number: 3
pages: 16-19
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — We consider commutative DG rings (better known as nonpositive stronglycommutativeassociativeunitalDGalgebras)."
---
Recall that by default all DG modules are left DG modules, and all DG rings
are nonpositive (Convention 1.4). In this section we study the canonical DG ring
homomorphism A→ ¯A, and the corresponding reduction functorD(A)→ D( ¯A),
M↦→ ¯A⊗L
A M. We do not make any ﬁniteness assumptions on the cohomology
modules Hi(M).
A triangulated functorF is calledconservative if for any objectM, F(M) = 0
implies M = 0;orequivalently,ifforanymorphism φ, F(φ)isanisomorphismim-
plies φisanisomorphism. Cf.[KaSc,Section1.4]. Thefollowingresultisanalogous
to the Nakayama Lemma (cf. Remark 7.24).
Proposition 3.1. Let A be a DG ring. The reduction functor
¯A⊗L
A− : D−(A)→ D−( ¯A)
is conservative.
Proof. Take M∈ D−(A)notisomorphicto 0,andlet i1 := sup(H(M)). Wecanﬁnd
a K-ﬂat resolution (e.g. a semi-free resolution)P→ M over A such thatsup(P) =
i1. Then ¯A⊗L
A M∼= ¯A⊗A P, and (by the “Künneth trick”)
Hi1 ( ¯A⊗L
A M)∼= Hi1 ( ¯A⊗A P)∼= ¯A⊗A Hi1 (P)∼= Hi1 (M)
is nonzero. Hence ¯A⊗L
A M is nonzero. □
Given a homomorphismφ : P→ Q in C(A), we denote bycone(φ) the corre-
sponding cone, which is also an object ofC(A).
Lemma 3.2. Suppose φ : P → Q is a homomorphism inC(A), where P and Q are
pseudo-ﬁnite(resp. ﬁnite) semi-free DG modules. Thencone(φ) is a pseudo-ﬁnite(resp.
ﬁnite) semi-free DG module.
Proof. Clear from Proposition 1.15. □
Proposition 3.3. Let M∈ D−(A). We write ¯M := ¯A⊗L
A M∈ D−( ¯A).
COMMUTATIVE DG RINGS 17
(1) If ¯Misisomorphicin D( ¯A)to ¯A⊕r forsomecardinalnumber r,then Misisomor-
phic inD(A) to A⊕r.
(2) If ¯M is isomorphic inD( ¯A) to a semi-free DG¯A-module ¯P of semi-free lengthd,
then M is isomorphic inD(A) to a semi-free DGA-module P of semi-free length
d.
ObservethattheDG ¯A-module ¯Pin(2)aboveisnothingbutaboundedcomplex
of free ¯A-modules; cf. Proposition 1.15. The semi-free length was introduced in
Deﬁnition 1.14.
Proof. Step1. InviewofProposition3.1wecanassumethat ¯Aand Marenonzero.
Deﬁnei1 := sup(H(M)). By replacing M with a suitable resolution of it, we can
assume thatM is a K-ﬂatDGA-module satisfyingsup(M) = i1. After that wecan
also assume that ¯M = ¯A⊗A M. The Künneth formula says that
Hi1 ( ¯M)∼= Hi1 ( ¯A⊗A M)∼= ¯A⊗A Hi1 (M)∼= Hi1 (M)
as ¯A-modules. Thereforesup(H( ¯M)) = sup( ¯M) = i1.
We are given an isomorphism¯φ : ¯P → ¯M in D( ¯A0), where ¯P is a bounded
complex of free ¯A-modules. Since ¯P is K-projective, we can assume that the iso-
morphism ¯φ : ¯P→ ¯M in D( ¯A) is in fact a quasi-isomorphism inC( ¯A). The proof
continues by induction onj := amp( ¯P)∈ N. Note that in item (1) we havei1 = 0,
¯P = ¯A⊕r and j = 0.
Step 2. In this step we assume thatj = 0. This means that the only nonzero term
of ¯P is in degreei1, and it is the free module¯Pi1∼= ¯A⊕r1 for some cardinal number
r1. In other words,¯P∼= ¯A[−i1]⊕r1 in C( ¯A). So Hi1 ( ¯M)∼= ¯Pi1, andHi( ¯M) = 0 for
all i⁄= i1. Recall the isomorphism of¯A-modules Hi1 ( ¯M)∼= Hi1 (M) from Step 1.
There are canonical surjectionsMi1→ Hi1 (M) and ¯Mi1→ Hi1 ( ¯M). We can write
the quasi-isomorphism ¯φ as ¯φ : ¯A[−i1]⊕r1→ ¯M.
Considerthenonderivedreductionfunctor F : C(A)→ C( ¯A), F(−) := ¯A⊗A−.
Let P := A[−i1]⊕r1, a free DGA-module satisfying F(P) ∼= ¯P. There exists a
homomorphism φ : P→ M in C(A) that lifts the quasi-isomorphism¯φ : ¯P→ ¯M,
namely ¯φ = F(φ). Now the DG modulesP and M are K-ﬂat, so¯φ = LF(φ). Since
¯φ is an isomorphism, and since the functorLF is conservative, we conclude thatφ
is an isomorphism. This proves item (1).
Step 3. Here we suppose thatj≥ 1. Let i2 := sup( ¯P), which is of course≥ i1.
Say ¯Pi2∼= ¯A⊕r2 for some natural numberr2. Deﬁne DG modules¯P′ := ¯A[−i2]⊕r2
and P′ := A[−i2]⊕r2; these satisfy¯P′∼= ¯A⊗A P′. The inclusion ¯Pi2⊆ ¯P is viewed
as a DG module homomorphism¯α : ¯P′→ ¯P. We also have a quasi-isomorphism
¯φ : ¯P → ¯M and an equality ¯M = ¯A⊗A M in C( ¯A). In this way we obtain a
homomorphism ¯ψ : ¯P′→ ¯M, ¯ψ := ¯φ◦ ¯α. Because P′ is a free DGA-module, there
is a homomorphismψ : P′→ M in C(A) lifting ¯ψ, namely ¯ψ = F(ψ), where F is
the functor ¯A⊗A−.
Let M′′∈ C(A) be the cone ofψ, so there is a distinguished triangle
(3.4) P′ ψ
− →M
χ
− →M′′− →P′[1]
in D(A). Deﬁne ¯M′′ := F(M′′) and ¯χ := F(χ), which are an object and a mor-
phism inC( ¯A), respectively. Since all three DG modules in this triangle are K-ﬂat,
it follows that
¯P′ ¯ψ
− →¯M
¯χ
− →¯M′′− →¯P′[1]
18 AMNON YEKUTIELI
is a distinguished triangle inD( ¯A). On the other hand, let¯P′′ be the cokernel of
the inclusion ¯α : ¯P′→ ¯P. So there is a distinguished triangle
¯P′ ¯α− →¯P
¯β
− →¯P′′− →¯P′[1]
in D( ¯A). Consider the diagram of solid arrows inD( ¯A) :
¯P′ ¯α //
=

¯P
¯β //
¯φ

¯P′′ //
¯φ′′

¯P′[1]
=

¯P′ ¯ψ // ¯M
¯χ // ¯M′′ // ¯P′[1]
Thesquareontheleftiscommutative, andthereforeitextendstoanisomorphism
of distinguished triangles. So there is an isomorphism¯φ′′ : ¯P′′→ ¯M′′ in D( ¯A).
Finally, the complex¯P′′ is a bounded complex of ﬁnite free¯A-modules, of am-
plitude j− 1≥ 0. According to the induction hypothesis (step 2 forj > 1, and
step 1 forj = 1) there is an isomorphismφ′′ : P′′ ≃− →M′′ in D(A) for some ﬁnite
semi-free DGA-module P′′. From (3.4) we obtain a distinguished triangle
P′ ψ
− →M
ψ
− →P′′ γ
− →P′[1]
in D(A). Wecanassumethat γisahomomorphismin C(A). Turningthistriangle
we get a distinguished triangle
P′′[−1]
−γ[−1]
−−−−→P′ ψ
− →M ∆− →.
DeﬁneP to be the cone on the homomorphism−γ[−1] : P′′[−1] → P′. Then
P∼= M in D(A), and by Lemma 3.2,P is a ﬁnite semi-free DGA-module. □
WelearnedthenextpropositionfromB.AntieauandJ.Lurie. Cf.[Lu1,Corollary
7.2.2.19] for a more general statement.
Proposition 3.5. Let ¯P be a projective ¯A-module. Then there exists a DGA-module P
with these properties:
(i) P is a direct summand, inD(A), of a direct sum of copies ofA.
(ii) ¯A⊗L
A P∼= ¯P in D( ¯A).
Proof. Say ¯Pisadirectsummand,in Mod ¯A,ofafree ¯A-module ¯F. So ¯Pistheimage
of an idempotent endomorphism¯φ : ¯F→ ¯F. Let F be the direct sum inC(A) of
copies of A, as many as there are copies of¯A in ¯F. There is a canonical surjection
F → ¯F. Choose any homomorphism φ : F → F in C(A) lifting ¯φ. Note that
manysuch φexist;andtheyaren’tnecessarilyidempotents. Let Pbethehomotopy
colimit construction onφ. Namely we let
Φ :
⨁
i∈N F →
⨁
i∈N F
be the homomorphism
Φ(a0, a1, a2, ...) := ( a0, a1− φ(a0), a2− φ(a1), ...)
in C(A), and then we deﬁneP := cone(Φ)∈ C(A). Because P is K-ﬂat overA, we
see that ¯A⊗L
A P∼= ¯A⊗A P∼= cone( ¯Φ), where
¯Φ :
⨁
i∈N
¯F →
⨁
i∈N
¯F
is the homotopy colimit construction on¯φ. An easy calculation, using the fact that
¯φ is an idempotent with image¯P, shows thatcone( ¯Φ)∼= ¯P in D( ¯A). This proves
(ii).
COMMUTATIVE DG RINGS 19
As for (i): say ¯Q is the other direct summand of¯F in Mod ¯A. We can lift it to
a DG A-module Q as above. Now ¯P⊕ ¯Q∼= ¯F in D( ¯A). By Proposition 3.3(1) we
deduce thatP⊕ Q∼= F in D(A). □
