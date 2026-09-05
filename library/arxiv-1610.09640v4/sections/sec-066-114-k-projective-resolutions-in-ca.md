---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-066-114-k-projective-resolutions-in-ca
section_title: "K-Projective Resolutions in C(A)"
section_number: 11.4
pages: 200-208
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
(without any vanishing assumption).
Let A♮be the graded ring that we have after forgetting the diﬀerential ofA.
In Subsection 3.8 we introduced the functor Und : C(A)→G(A♮) that forgets
the diﬀerentials of DG modules. We shall now use the abbreviated formM♮:=
Und(M).
Recall that the translation T−i(A) is a DG A-module in which the element
t−i(1A)isindegree i. Thiselementisacocycle, andwhenweforgetthediﬀerentials,
the graded module T−i(A)♮is free over the graded ringA♮, with basis t−i(1A).
Therefore, for every DGA-module M there is a canonical isomorphism
(11.4.1) HomA
(
T−i(A),M
{∼= Ti(M)
in Cstr(K), and canonical isomorphisms
(11.4.2) HomCstr(A)
(
T−i(A),M
{∼= Z0(
HomA(T−i(A),M )
{∼= Zi(M)
in M(K). (Actually, (11.4.1) is an isomorphism inCstr(A), but this uses the DG
A-bimodule structure ofT−i(A).)
We begin with a deﬁnition that is very similar to Deﬁnition 11.3.1.
Deﬁnition 11.4.3.Let P be an object ofC(A).
(1) We say thatP is a free DG A-module if there is an isomorphism P ∼=⨁
s∈S T−is(A) in Cstr(A), for some indexing setS and some collection of
integers{is}s∈S.
(2) A semi-free ﬁltrationonP is a ﬁltrationF ={Fj(P )}j≥−1 ofP in Cstr(A),
such that:
•F−1(P ) = 0.
•Each GrF
j (P ) is a free DGA-module.
•P = limj→Fj(P ).
(3) The DG moduleP is calledsemi-freeif it admits some semi-free ﬁltration.
Note that the direct limit in item (2) is just the union of DG submodules.
There is an alternative description of semi-free ﬁltrations, that is useful for un-
derstanding their structure. We will give it in Deﬁnition 11.4.7 below, after some
combinatorial preliminaries.
The next deﬁnition has already appeared within Example 3.1.23.
Deﬁnition 11.4.4.A graded setis a setS that is partitioned into subsets:S =∐
i∈Z Si. The elements of Si are said to have degreei, so that Si ={s∈S |
deg(s) =i}.
A free DGA-moduleP as in Deﬁnition 11.4.3(1) can be described as follows. The
indexing setS can be made into a graded set by deﬁningSk :={s∈S|is = k}.
In other words,deg(s) =is. We denote byA·s the free DGA-module with basiss,
so that d(s) = 0, and there is an isomorphismA·s
≃
− →T−is(A) in Cstr(A) sending
s↦→t−is(1A). Writing
(11.4.5) A·S :=
⨁
s∈S
A·s
we obtainA·S∼=P as DGA-modules. Note thatA♮·S∼=P♮as gradedA♮-modules.
Deﬁnition 11.4.6.Let S be a graded set. A ﬁltrationon S is a direct system
F =
{
Fj(S)
}
j≥−1 of subsets ofS, such thatF−1(S) =∅ and
jFj(S) = S. The
pair (S,F ) is called aﬁltered graded set.
Note that eachFj(S) is itself a graded set, with degreei component Fj(S)i :=
Fj(S)∩Si.
200
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 11.4.7.LetP be a DGA-module. Asemi-basisofP is a ﬁltered graded
set (S,F ), together with an isomorphismP♮∼= A♮·S of gradedA♮-modules, such
that under this isomorphism we havedP (Fj(S))⊆A♮·Fj−1(S) for everyj≥0.
Proposition 11.4.8. LetP be a DGA-module.
(1) If P has a semi-basis (S,F ), then P has an induced semi-free ﬁltration
{Fj(P )}j≥−1 such thatFj(P )♮=A♮·Fj(S) as gradedA♮-modules for every
j≥−1.
(2) Every semi-free ﬁltration ofP is induced by some semi-basis.
Exercise 11.4.9. Prove Proposition 11.4.8.
Example 11.4.10. IfA is a ring, then a free DGA-module P is a complex of free
A-modules with zero diﬀerential. A semi-free DGA-module P is also a complex of
free A-modules, but there is a diﬀerential on it, and there is a subtle condition on
P imposed by the existence of a semi-free ﬁltration. If the complexP happens to
be bounded above, then it is automatically semi-free, with a ﬁltration like the one
in the proof of Proposition 11.3.5.
Exercise 11.4.11. Find a ringA, and a complexP of freeA-modules, that is not
semi-free. (Hint: Take the ringA =K[ϵ] of dual numbers. Find a complex of free
A-modulesP that is acyclic but not null-homotopic. Now use Theorem 11.4.14 and
Corollary 10.2.14 to deduce thatP is not semi-free.)
Proposition 11.4.12.LetA andB be DG rings, and letP∈C(A) andQ∈C(B)
be semi-free DG modules. ThenP⊗Q∈C(A⊗B) is a semi-free DG module.
Exercise 11.4.13. Prove this proposition. (Hint: let
{
Fj(P )
}
j≥−1 and{
Gk(Q)
}
k≥−1 be semi-free ﬁltrations. Deﬁne
Ej(P⊗Q) :=
j
k=0
(
Fk(P )⊗Gj−k(Q)
{
⊆P⊗Q.
Show that this is a semi-free ﬁltration.)
Theorem 11.4.14. Let P be an object ofC(A). If P is semi-free, then it is K-
projective.
Proof. This is similar to the proof of Theorem 11.3.2.
Step 1. We start by proving that ifP = T−i(A), a translation ofA, then P is
K-projective. This is easy: given an acyclicN∈C(A), we have
HomA(P,N ) = HomA
(
T−i(A),N
{∼= Ti(
HomA(A,N )
{∼= Ti(N)
in Cstr(K), and this is acyclic.
Step 2. NowP is free, sayP∼=⨁
s∈S T−is(A). Then
HomA(P,N )∼=

s∈S
HomA
(
T−is(A),N
{
.
By step 1 and the fact that a product of acyclic complexes inCstr(K) is acyclic, we
conclude that HomM(P,N ) is acyclic.
Step 3. Fix a semi-free ﬁltrationF ={Fj(P )}j≥−1 of P. Here we prove that for
everyj≥−1 the DG moduleFj(P ) is K-projective. This is done by induction on
j≥−1. Forj =−1 it is trivial. Forj≥0 there is an exact sequence
(11.4.15) 0→Fj−1(P )→Fj(P )→GrF
j (P )→0
201
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in the abelian category Cstr(A). Because GrF
j (P ) is a free DG module, it is a
projective object in the abelian categoryGstr(A♮)of graded modules over the graded
ring A♮. Therefore the sequence (11.4.15) is split exact inGstr(A♮).
Let N∈C(A) be an acyclic DG module. Applying the functorHomA(−,N ) to
the sequence (11.4.15) we obtain a sequence
(11.4.16)
0→HomA
(
GrF
j (P ),N
{
→HomA
(
Fj(P ),N
{
→HomA
(
Fj−1(P ),N
{
→0
in Cstr(K). If we forget diﬀerentials this is a sequence inGstr(K). Because (11.4.15)
is split exact inGstr(A♮), it follows that (11.4.16) is split exact inGstr(K). Therefore
(11.4.16) is exact inCstr(K).
BytheinductionhypothesistheDG K-module HomA
(
Fj−1(P ),N
{
isacyclic. By
step 2 the DG moduleHomA
(
GrF
j (P ),N
{
is acyclic. The long exact cohomology
sequence associated to (11.4.16) shows that the DG moduleHomA
(
Fj(P ),N
{
is
acyclic too.
Step 4. We keep the semi-free ﬁltrationF ={Fj(P )}j≥−1 from step 3. Take any
acyclic N∈C(M). By Proposition 1.8.6 we know that
HomA(P,N )∼= lim
←j
HomA
(
Fj(P ),N
{
in Cstr(K). According to step 3 the complexesHomA
(
Fj(P ),N
{
are all acyclic. The
exactness of the sequences (11.4.16) implies that the inverse system{
HomA
(
Fj(P ),N
{}
j≥−1 in Cstr(K) has surjective transitions. Now the Mittag-
Leﬄer argument (Corollary 11.1.8) says that the inverse limit complexHomA(P,N )
is acyclic. □
Here is a result similar to Theorem 11.3.6.
Theorem 11.4.17. Let A be a DG ring. Every M ∈C(A) admits a quasi-iso-
morphism ρ:P→M in Cstr(A) from a semi-free DGA-moduleP.
The proof of this theorem was communicated to us by B. Keller. First we need
a construction and a lemma.
Let us deﬁne the DGA-module
(11.4.18) C := Cone
(
id : T−1(A)→T−1(A)
{
,
the standard cone of the identity automorphism ofT−1(A) in Cstr(A). Since
C = T−1(A)⊕T(T−1(A)) = T−1(A)⊕A
as graded objects, we have the elementse0 := 1A∈A⊆C0 and e1 := t−1(1A)∈
T−1(A)1⊆C1. They satisfydC(e0) =e1. Note that the DG moduleC is semi-free,
with semi-free ﬁltration
(11.4.19) Fj(C) :=



0 if j =−1
T−1(A) if j = 0
C if j≥1.
As a gradedA♮-module, C♮is free, with basis(e0,e 1). Of course the DG module
C is contractible.
Lemma 11.4.20. LetM∈C(A).
(1) There is a homomorphismψ:Q→M in Cstr(A), such thatZ(ψ) : Z(Q)→
Z(M) is surjective, and Q = ⨁
s∈S T−is(A) for a collection of integers
{is}s∈S.
202
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) There is a surjective homomorphismψ′: Q′→M in Cstr(A), such that
Q′:=⨁
s∈S′T−is(C) for some collection of integers{is}s∈S′, whereC is
the DGA-module from formula(11.4.18).
To clarify the notation in the lemma, the collections of integers{is}s∈S and
{is}s∈S′are distinct; namely the functioni :s↦→is is i :S⊔S′→Z.
Proof.
(1) For every cocyclem∈Zi(M) there a homomorphismψm : T−i(A)→M that
sends the elementt−i(1A)∈Zi(T−i(A)) to m. Thus, if{ms}s∈S is a collection of
homogeneous cocycles that generatesZ(M)as aK-module, we get a homomorphism
ψas claimed.
(2) For every elementm∈Mi there is a homomorphismψ′
m : T−i(C)→M in
Cstr(A) that sends t−i(e0)↦→m and t−i(e1)↦→(−1)i·dM(m). Hence, by taking a
collection{ms}s∈S′of homogeneous elements that generatesM as aK-module, we
get a homomorphismψ′as claimed. □
The DGA-module Q in item (1) of the lemma is free. The DGA-module Q′in
item (2) is semi-free, with semi-free ﬁltration induced by that ofC, namely
(11.4.21) Fj(Q′) :=
⨁
s∈S′
T−is(Fj(C))
for j≥−1, whereFj(C) is from (11.4.19).
Proof of Theorem11.4.17. The proof is in several steps.
Step 1. We are going to produce an exact sequence
(11.4.22) ···→Q−2 ∂−2
−−→Q−1 ∂−1
−−→Q0 η
− →M→0
in Cstr(A) with these properties:
(a) The sequence
···→Z(Q−2)
Z(∂−2)
−−−−→Z(Q−1)
Z(∂−1)
−−−−→Z(Q0)
Z(η)
−−−→Z(M)→0
in Gstr(K) is exact.
(b) For everyi≤0 the DGA-module Qi has the following decomposition in
Cstr(A) : Qi = Qi⊕Q′
i, where Qi = ⨁
s∈Si T−js(A) and Q′
i =⨁
s∈S′
i
T−js(C) for some collection of integers{js}s∈Si⊔S′
i
.
This will be done recursively oni≤0.
By Lemma 11.4.20 we can ﬁnd DGA-modules Q0,Q′
0 and homomorphismsψ0 :
Q0→M, ψ′
0 : Q′
0→M, such that both Z(ψ0) and ψ′
0 are surjective. The DG
modules Q0,Q′
0 are of the required form (property (b) withi = 0). We letQ0 :=
Q0⊕Q′
0 and η:=ψ0⊕ψ′
0.
Let N0 := Ker(η). Then the sequence
(11.4.23) 0→N0→Q0 η
− →M→0
in Cstr(A) is exact. The sequence
0→Z(N0)→Z(Q0)
Z(η)
−−−→Z(M)→0
in Gstr(K) is also exact. Indeed, the exactness at Z(N0) and Z(Q0) is because
the functor Z : Cstr(K)→Gstr(K) is left exact (see Proposition 3.8.14), and the
sequence (11.4.23) is exact. The exactness atZ(M) is by the surjectivity ofZ(ψ0) :
Z(Q0)→Z(M).
Next we repeat this procedure withN0 instead ofM, to obtain an exact sequence
(11.4.24) 0→N−1→Q−1 ∂−1
−−→N0→0,
203
Derived Categories | Amnon Yekutieli | 14 Apr 2019
with Q−1 of the required form (property (b) withi =−1), and such that
0→Z(N−1)→Z(Q−1)
Z(∂−1)
−−−−→Z(N0)→0
is also exact. We then splice (11.4.23) and (11.4.24) to get the sequence
0→N−1→Q−1 ∂−1
−−→Q0 η
− →M.
Continuing recursively we obtain an exact sequence (11.4.22) that has properties
(a) and (b).
Step 2. We view the exact sequence (11.4.22) as an acyclic complex with entries in
Cstr(A), that hasQ0 in degree 0. Deﬁne the total DGA-modules
P := Tot⊕(
···→Q−2 ∂−2
−−→Q−1 ∂−1
−−→Q0→0→···
{
and
P aug := Tot⊕(
···→Q−2 ∂−2
−−→Q−1 ∂−1
−−→Q0 η
− →M→0→···
{
.
Because the sequence (11.4.22) and the sequence appearing in property (a) are
exact, we can use Proposition 11.2.16 (with anyj1∈Z). The conclusion is that
the DGA-module P aug is acyclic. Then, by Corollary 11.2.14, the homomorphism
ρ:P→M in Cstr(A) that is induced byηis a quasi-isomorphism.
Step 3. It remains to produce a semi-free ﬁltration{Fj(P )}j≥−1 on the DGA-
module P. Our formula is this:F−1(P ) := 0 of course. Fork≥0 we let
F2·k(P ) :=
(⨁−(k−1)
l=0
T−l(Ql)
{
⊕Tk(
Q−k⊕F0(Q′
−k)
{
,
where F0(Q′
−k) comes from (11.4.21), and
F2·k+1(P ) :=
⨁−k
l=0
T−l(Ql).
We leave it to the reader to verify that this is a semi-free ﬁltration. □
Exercise 11.4.25. Finish step 3 of the proof.
Corollary 11.4.26. Let A be a DG ring. The categoryC(A) has enough K-pro-
jectives.
Proof. Combine Theorems 11.4.14 and 11.4.17. □
Recall that a DG ringA is nonpositive ifAi = 0 for all i > 0. According to
Proposition 7.3.8, whenA is nonpositive the smart truncation functors exist.
Corollary 11.4.27.If the DG ringA is nonpositive, then everyM∈C(A) admits
a quasi-isomorphismρ:P→M in Cstr(A) from a semi-free DGA-moduleP, such
that sup(P ) = sup(H(M)).
Proof. Let i1 := sup(H(M)). If i1 =±∞then there is nothing to prove beyond
Theorem 11.4.17; so let us assume thati1∈Z. DeﬁneM′:= smt≤i1(M). Then
M′→M is a quasi-isomorphism, andsup(M′) = i1. By replacingM with M′we
can now assume thatsup(M) =i1.
Since sup(M)≤i1, in step 1 of the proof of the theorem we can take the DG
module Q0 to be concentrated in degrees≤i1. Another consequence of the fact
that sup(M)≤i1 is that Mi1 = Zi1(M). This means that the homomorphism
ψ0 : Qi1
0 →Mi1 is already surjective; so we don’t need to coverMi1 by Q′
0, and
thus we can takeQ′
0 to be concentrated in degrees≤i1. In this way we can arrange
to have sup(Q0)≤i1. But then we also havesup(N0)≤i1. Thus recursively we
can arrange to havesup(Ql)≤i1 for alll. Therefore in step 2 of the proof we get
sup(P )≤i1.
Finally, becausesup(H(M)) =i1 we must havesup(P ) =i1. □
204
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 11.4.28.Let A be a DG ring. A DGA-module P is called apseudo-
ﬁnite free DGA-module if there are numbersi1∈Z and ri∈N such thatP ∼=⨁
i≤i1 T−i(A)⊕ri in Cstr(A).
Deﬁnition 11.4.29.Let A be a DG ring and letP be a DGA-module.
(1) A pseudo-ﬁnite semi-free ﬁltrationon P is a semi-free ﬁltration F ={
Fj(P )
}
j≥−1 satisfying this ﬁniteness condition: there are numbersi1∈Z
and rj∈N such that GrF
j (P )∼= T−i1+j(A)⊕rj in Cstr(A) for allj∈N.
(2) We callP a pseudo-ﬁnite semi-free DGA-moduleif it admits some pseudo-
ﬁnite semi-free ﬁltration.
Note that in item (1) of the deﬁnition above, for everyj≥−1 we have
(11.4.30) Fj(P )♮∼=
⨁
0≤k≤j
GrF
j (P )♮∼=
⨁
0≤k≤j
T−i1+k(A♮)⊕rk
as gradedA♮-modules.
Proposition 11.4.31. Let P be a DGA-module. The two conditions below are
equivalent.
(i) P is a pseudo-ﬁnite semi-free DGA-module.
(ii) P admits a semi-basis(S,F ) such thatS is bounded above, say byi1∈Z;
each of the setsSi is ﬁnite; and Fj(S) =
i∈[i1−j,i1] for everyj≥−1.
Exercise 11.4.32.Prove Proposition 11.4.31. (Hint: the numbersi1 in Deﬁnition
11.4.29(1) and in condition (ii) are the same.)
A graded A♮-module P♮is called pseudo-ﬁnite freeif there is an isomorphism
of graded A♮-modules P♮∼=
⨁
j≥0 T−i1+j(A♮)⊕rj for some numbersi1 ∈Z and
rj∈N.
Proposition 11.4.33. Let A be a DG ring and letP be a DGA-module. The
following two conditions are equivalent:
(i) The DGA-moduleP is pseudo-ﬁnite semi-free.
(ii) The DGA-module P admits a semi-free ﬁltrationF ={Fj(P )}j≥−1 such
that eachGrF
j (P ) is a pseudo-ﬁnite free DGA-module, and this asymptotic
formula holds: limj→∞sup(GrF
j (P )) =−∞.
If A is nonpositive, the conditions above are equivalent to:
(iii) The gradedA♮-moduleP♮is pseudo-ﬁnite free.
If A is a ring(i.e. Ai = 0 for alli⁄= 0), the conditions above are equivalent to:
(iv) P is a bounded above complex of ﬁnitely generated freeA-modules.
Exercise 11.4.34. Prove the proposition above. (Hint: rephrase these conditions
in terms of semi-bases.)
Remark 11.4.35.Condition (iv) of Proposition 11.4.33 is a hint for the reason we
chose the name “pseudo-ﬁnite” in Deﬁnition 11.4.29, and also the name “pseudo-
noetherian” in Deﬁnitions 11.4.36 and 11.4.37 below (in conjunction with Theorem
11.4.40). Indeed, in [21] and [144], a complex of modules over a ringA is called
pseudo-coherentif it is isomorphic, inD(A), to a bounded above complex of ﬁnite
free A-modules.
For a generalization of the notion of pseudo-coherent complex to DG modules,
see Deﬁnition 12.9.1.
Deﬁnition 11.4.36.A graded ringA is calledleft pseudo-noetherianif it is non-
positive, the ringA0 is left noetherian, and eachAi is a ﬁnitely generated (left)
A0-module.
205
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 11.4.37.Let A be a DG ring.
(1) We callA a cohomologically left pseudo-noetherian DG ringif its cohomol-
ogy H(A) is a left pseudo-noetherian graded ring.
(2) Suppose A is cohomologically left pseudo-noetherian. We denote byDf(A)
the full subcategory ofD(A) on the DG modulesM such that Hi(M) is a
ﬁnitely generatedH0(A)-module for everyi.
Of courseDf(A) is a full triangulated subcategory ofD(A). As usual we combine
indicators: D⋆
f (A) := Df(A)∩D⋆(A).
Example 11.4.38. Suppose A0 is a nonzero noetherian commutative ring. Let
X =∐
i≤0Xi be a nonpositive graded set, such that each graded pieceXi is ﬁnite.
Consider the strongly commutative graded polynomial ringA0[X] := A0⊗K[X]
from Example 3.1.23. The graded ringA0[X] is (left and right) pseudo-noetherian,
but ifX is inﬁnite thenA0[X] is not noetherian (on either side).
Likewise, letY =∐
i<0Yi be a negative graded set, such that each graded piece
Yi is ﬁnite. Take the noncommutative graded polynomial ringA0⟨Y⟩:=A0⊗K⟨Y⟩
from Example 3.1.23 and Deﬁnition 12.8.1. The graded ringA0⟨Y⟩is (left and
right) pseudo-noetherian, but ifY has at least two elements, thenA0⟨Y⟩is not
noetherian (on either side).
Remark 11.4.39. Let A be a DG ring whose cohomologyH(A) is a nonpositive
graded ring. DeﬁneA′:= smt≤0(A), the smart truncation ofA below 0. It is easy
to see thatA′is a DG subring ofA, and the inclusionA′→A is a DG ring quasi-
isomorphism. By Theorem 12.7.2 there is an equivalence of triangulated categories
D(A)→D(A′). This says that for many purposes we can assume thatA itself is a
nonpositive DG ring.
Theorem 11.4.40. Let A be a nonpositive cohomologically left pseudo-noether-
ian DG ring, and letM ∈D−
f (A). Then there is a quasi-isomorphismP →M
in Cstr(A), where P is a pseudo-ﬁnite semi-free DGA-module, and sup(P ) =
sup(H(M)).
Proof. The proof is divided into ﬁve parts.
Part 1. We may assume thatH(M)⁄= 0, so thati1 := sup(H(M))∈Z. We are
going to construct a direct system
0 =F−1(P )⊆F0(P )⊆F1(P )⊆···
of pseudo-ﬁnite semi-free DGA-modules, together with a direct system of DG
A-module homomorphismsFj(ρ) :Fj(P )→M for j≥0, having these properties:
(a) Let j≥0. The homomorphism Hi(Fj(ρ)) : Hi(Fj(P ))→Hi(M) is surjec-
tive for alli, and bijective for alli>i 1−j.
(b) F0(P ) is a pseudo-ﬁnite free DGA-module with sup(F0(P )) =i1.
(c) Let j≥1. There is an isomorphism Fj(P )/Fj−1(P )∼= T−i1+j(A)⊕rj in
Cstr(A), for somerj∈N.
This will be done recursively onj≥0. .
Part 2. Here we deal with the casesj =−1, 0. Forj =−1 we takeF−1(P ) := 0 of
course.
Now we deal withF0(P ). For everyi≤i1 we choose ﬁnitely many generators
of the H0(A)-module Hi(M), and then we lift them to elements ofZi(M). These
choices give rise to a pseudo-ﬁnite free DGA-module F0(P ) and a homomorphism
F0(ρ) :F0(P )→M in Cstr(A), such thatsup(F0(P )) =i1, and the homomorphism
H(F0(ρ)) : H( F0(P ))→H(M) in Gstr(K) is surjective. Condition (a) holds for
j = 0, and so does condition (b). Condition (c) is not applicable here.
206
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Part 3. Suppose thatj≥0, and we have a direct system
0 =F−1(P )⊆F0(P )⊆F1(P )⊆···⊆Fj(P )
of semi-free DGA-modules, together with a direct system of DGA-module homo-
morphisms Fj′(ρ) : Fj′(P )→M for j′∈[0,j ], satisfying conditions (a)-(c) with
index j′instead ofj. In this part we will construct the DGA-module Fj+1(P ).
Let
(11.4.41) ¯N := Ker
(
Hi1−j(Fj(ρ)) : Hi1−j(Fj(P ))→Hi1−j(M)
{
.
BecauseFj(P )isapseudo-ﬁnitesemi-freeDG A-module, andAisacohomologically
left pseudo-noetherian DG ring, it follows that ¯N is a ﬁnitely generatedH0(A)-
module. We choose elements ¯n1,..., ¯nrj+1 ∈¯N that generate ¯N as an H0(A)-
module. Then we lift them to elementsn1,...,nrj+1∈Zi1−j(Fj(P )).
Consider the free DG A-module Q′:= T−i1+j(A)⊕rj+1 with basis (e′
1,...,
e′
rj+1) concentrated in degreei1−j. There is a homomorphismφ:Q′→Fj(P ) in
Cstr(A) with formulaφ(e′
k) :=nk. Deﬁne
(11.4.42) Fj+1(P ) := Cone
(
φ:Q′→Fj(P )
{
,
the standard cone of φ. The DG A-module Fj+1(P ) is pseudo-ﬁnite semi-free.
Condition (b) still holds, becauseF0(P ) did not change. AndFj+1(P )/Fj(P )∼=Q,
where
(11.4.43) Q := T(Q′)∼= T−i1+j+1(A)⊕rj+1,
so condition (c) holds also forj + 1.
Part 4. We continue part 3. Here we construct the homomorphism Fj+1(ρ) :
Fj+1(P )→M in Cstr(A). For everyk∈[1,rj+1] let ek := tQ′(e′
k)∈Qi1−j−1. The
sequence (e1,...,erj+1) is a basis of the free DGA-module Q. We havedQ(ek) = 0
and t−1
Q (ek) =e′
k∈Q′, so by the deﬁnition of the diﬀerential of the cone we have
dFj+1(P)(ek) = dQ(ek) +φ(t−1
Q (ek)) =φ(e′
k) =nk.
Now the cohomology class¯nk of nk belongs to ¯N, so Hi1−j(Fj(ρ))(¯nk) = 0. This
means that the elementFj(ρ)(nk) is a coboundary inM, and we can lift it to an
elementmk∈Mi1−j−1.
By deﬁnition of the cone we haveFj+1(P )♮=Fj(P )♮⊕Q♮as gradedA♮-modules.
We deﬁne the homomorphismFj+1(ρ) : Fj+1(P )♮→M♮in Gstr(A♮) to be the
extension ofFj(ρ) such thatFj+1(ρ)(ek) := mk. Then Fj+1(ρ) : Fj+1(P )→M is
actually a homomorphism inCstr(A).
There is equality Fj+1(P )i = Fj(P )i in all degrees i ≥i1−j. Therefore
Hi(Fj+1(ρ)) = Hi(Fj(ρ)) for alli>i 1−j, and these homomorphisms are bijective
by assumption. The homomorphismZi1−j(Fj(P ))→Zi1−j(Fj+1(P )) is surjective,
and hence Hi1−j(Fj(P ))→Hi1−j(Fj+1(P )) is also surjective. Because the sub-
module ¯N⊆Hi1−j(Fj(P )) goes to zero inHi1−j(Fj+1(P )), we have the following
commutative diagram:
0 // ¯N //

Hi1−j(Fj(P ))
Hi1−j(Fj(ρ)) //
surj

Hi1−j(M) //
id

0
0 // 0 // Hi1−j(Fj+1(P ))
Hi1−j(Fj+1(ρ))// Hi1−j(M) // 0
The top row is exact, by (11.4.41). Therefore the bottom row is exact, i.e.
Hi1−j(Fj+1(ρ)) is bijective. We conclude that condition (a) holds with indexj + 1.
207
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Part 5. DeﬁneP := limj→Fj(P ) and ρ:= limj→Fj(ρ) in Cstr(A). Condition (c)
implies that for everyi the direct system{Fj(Pi)}j≥−1 is eventually stationary.
Hence, by condition (a), the homomorphism Hi(ρ) is bijective. So ρis a quasi-
isomorphism.
By condition (b) and (c) the ﬁltration{Fj(P )}j≥−1 onP satisﬁes condition (ii)
of Proposition 11.4.33. ThereforeP is a pseudo-ﬁnite semi-free DGA-module. □
Example 11.4.44. A special yet very important case of Theorem 11.4.40 is this:
A is a left noetherian ring, andM is a complex ofA-modules with bounded above
cohomology, such that eachHi(M) is a ﬁnitely generatedA-module. Then M has
a resolutionP →M, whereP is a complex of ﬁnitely generated freeA-modules,
and sup(P ) = sup(H(M)). Compare this to Example 11.3.22.
Remark 11.4.45. In Example 11.3.16 we discussed the existence of K-ﬂat res-
olutions of unbounded complexes of sheaves of modules. Here is a more general
assertion.
Consider a DG ringed space (X,A), namely A is a sheaf of DG rings on a
topological spaceX. There are no commutativity or boundedness conditions onA.
By combining the concept of a semi-free DG module from Deﬁnition 11.4.3 with the
concept of a pseudo-free module from Example 11.3.16, we get something new: a
semi-pseudo-free DGA-module. This is a K-ﬂat DGA-module. The arguments in
[179] imply that every DGA-moduleM admits a quasi-isomorphismP→Mfrom
a semi-pseudo-free DGA-moduleP. Therefore C(A) has enough K-ﬂat objects. A
detailed proof of this assertion will be published in the future.
