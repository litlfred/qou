---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-107-186-twisted-calabi-yau-rings
section_title: "Twisted Calabi-Yau Rings"
section_number: 18.6
pages: 440-447
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
regular rings that is of great importance in recent ring theory. We continue with
Convention 18.1.1. Speciﬁcally,K is a base ﬁeld, and all rings are central overK.
For a ringA, its enveloping ring isAen =A⊗Aop.
Deﬁnition 18.6.1.A ringA is calledhomologically smooth overK ifA is a perfect
complex over the ringAen.
This deﬁnition was proposed by M. Kontsevich, around the year 2000, cf. [154,
Erratum]. Clearly ifA is homologically smooth overK, thenA is a derived pseudo-
ﬁnite complex overAen. Recall (from Example 18.1.14) that the ringA is called
regular if it has ﬁnite global cohomological dimension.
Proposition 18.6.2. If A is homologically smooth overK, then A is a regular
ring.
Proof. By Theorem 14.1.26 there is a quasi-isomorphismρ: P→A in Cstr(Aen),
where P is a bounded complex of ﬁnite projectiveAen-modules. Let d be the
amplitude of P. Given an A-module M, deﬁnePM := P⊗A M, and let ρM :
PM→M be the homomorphism inCstr(A) induced byρ. Since ρis a homotopy
equivalence in Cstr(Aop), it follows thatρM is a quasi-isomorphism. SincePi is a
projective Aen-module, and M is a freeK-module, we see thatPi
M = Pi⊗A M
is a projective A-module (often inﬁnitely generated; cf. Example 18.2.8). The
conclusion is that the projective dimension ofM is at mostd.
A similar consideration shows that everyM′∈M(Aop) has projective dimension
at mostd. So the global homological dimension ofA is at mostd. □
Remark 18.6.3. Suppose A is a ﬁnite type commutativeK-ring. It can be shown
that A is homologically smooth overK if and only if it is smooth overK, in the
sense of [57]. Cf. [108, Proposition 3.24].
Given aK-ring automorphismµof A, we deﬁne theµ-twisted bimoduleA(µ) as
follows: as a leftA-module, A(µ) is the freeA-module A; and the rightA-module
action is twisted byµ. To be explicit, let us denote bya·b the multiplication of the
ringA. Then the left action of a ring elementa∈Aon a bimodule elementb∈A(µ)
440
Derived Categories | Amnon Yekutieli | 14 Apr 2019
is a·µb := a·b∈A(µ); and the right action isb·µa := b·µ(a)∈A(µ). In fancier
notation, a ring elementa1⊗op(a2)∈Aen acts on a bimodule elementb∈A(µ)
from the left like this:(a1⊗op(a2))·µb =a1·b·µ(a2)∈A(µ). The graded version
of this twisting already appeared in Deﬁnition 17.1.7. Ifνis another automorphism
of A, thenA(µ)⊗AA(ν)∼=A(µ◦ν) in M(Aen).
It is possible to twist other bimodules: givenM∈M(Aen) we deﬁne
(18.6.4) M(µ) :=M⊗AA(µ)∈M(Aen).
Let us make explicit the left and right actions of the ringAen on the moduleM(µ),
using formula (18.1.8). The original left and right actions of an elementa∈A on an
elementm∈M are denoted bya·m andm·a. Then an element(a1⊗op(a2))∈Aen
acts on an elementm∈M(µ) from the left and the right by
(18.6.5)
(a1⊗op(a2))·µm =a1·m·µ(a2),
m·µ(a1⊗op(a2)) =a2·m·µ(a1).
Deﬁnition 18.6.6.A ringA is called atwisted CY ringif it has these two prop-
erties:
(i) The ringA is homologically smooth overK.
(ii) There is a natural numbern, called thedimension ofA, and a ring auto-
morphism νof A, called theNakayama automorphism, such that
Exti
Aen(A,A en)∼=
{
A(ν) if i =n
0 if i⁄=n
as A-bimodules.
The ringA is called aCY ringif the third property also holds:
(iii) The automorphismνis inner, so thatA(ν)∼=A as A-bimodules.
In property (ii) theAen-module Exti
Aen(A,A en) should be viewed as a special
case of Exti
B(M,N )∈M(Cop) for M ∈M(B) and N ∈M(B⊗Cop), where we
takeB,C :=Aen, M :=A and N :=Aen, and we use the isomorphism (18.1.5) to
switch from a rightAen-module to a leftAen-module.
The letters “CY” are an abbreviation for “Calabi-Yau”. Most texts use the term
“CY algebra” of course. See Remark 18.6.20 for a discussion of the background of
this deﬁnition. Clearly this is a relative notion: it pertains toA as a centralK-ring.
It is easy to see that the Nakayama automorphismνis unique up to composition
with an inner automorphism.
Here is another deﬁnition, taken from [166].
Deﬁnition 18.6.7.LetA be a noetherian ring with rigid dualizing complexR. If
R∼= A(µ)[n] in D(Aen) for some automorphismµand some integern, then µis
called thedualizing automorphismof A.
Like the Nakayama automorphism, the dualizing automorphism is unique up to
composition with an inner automorphism.
Proposition 18.6.8. Let A be a noetherian ring which is homologically smooth
over K, let n be a natural number, and let νbe an automorphism of A. The
following two conditions are equivalent.
(i) A is a twisted CY ring of dimensionn with Nakayama automorphismν.
(ii) The complexR :=A(ν−1)[n] is a rigid dualizing complex overA.
Thus the dualizing automorphism is the inverse of the Nakayama automorphism.
441
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. The key formula is this: forM,N ∈D(Aen) there are isomorphisms
(18.6.9)
RHomAen(A,M⊗N)∼=1 RHomAen
(
A,A en⊗L
Aen (M⊗N)
{
∼=2 RHomAen(A,A en)⊗L
Aen (M⊗N)
∼=3 N⊗L
A RHomAen(A,A en)⊗L
AM
in D(Aen). The isomorphism ∼=1 is the left unitor. The isomorphism ∼=2 is by
derived tensor-evaluation, and it exists becauseA is a perfect complex overAen;
see Theorem 14.1.22. The isomorphism∼=3 is because the leftAen action onM⊗N
is the outside action, cf. formula (18.2.1).
(i)⇒(ii): By Example 18.1.14 the complexR is dualizing. What is needed is a
rigidifying isomorphism for it. We are given thatRHomAen(A,A en)∼=A(ν)[−n] in
D(Aen). Plugging this andM =N :=R in (18.6.9) gives
RHomAen(A,R⊗R)∼=A(ν−1)[n]⊗L
AA(ν)[−n]⊗L
AA(ν−1)[n]
∼=A(ν−1◦ν◦ν−1)[n−n +n] =A(ν−1)[n] =R,
as required.
(ii)⇒(i): Now we are given thatRHomAen(A,R⊗R)∼=R in D(Aen). Substituting
M =N :=R in (18.6.9) gives
A(ν−1)[n]∼=A(ν−1)[n]⊗L
A RHomAen(A,A en)⊗L
AA(ν−1)[n]
in D(Aen). Therefore A(ν)[−n]∼= RHomAen(A,A en) in D(Aen). This is property
(iii) of Deﬁnition 18.6.6. □
Example 18.6.10.This is a continuation of Example 18.5.10:K has characteristic
0,C is a smooth commutativeK-ring of pure dimensionn, andA =D(C), the ring
of diﬀerential operators. It is known thatA is homologically smooth – in fact, in
this case Aen is a regular noetherian ring, of dimension 4n. According to [166,
Theorem 2.6] the rigid dualizing complex ofA isR =A[2n]. HenceA is a CY ring
of dimension 2n.
AS regular graded rings were introduced in Deﬁnition 15.4.8.
Theorem 18.6.11. LetA be a ring that admits some noetherian connected ﬁltra-
tion F, such that the graded ringGrF (A) is AS regular of dimensionn. Then A
is a noetherian twisted CY ring of dimensionn, with a Nakayama automorphism
νthat respects the ﬁltrationF.
Proof. Let ˜A := ReesF (A) and ¯A := GrF (A). We are given that¯A is AS regular of
dimensionn. According to Theorem 15.4.13(2),˜A is AS regular of dimensionn+1.
Consider the minimal graded-free resolution ˜Q→˜A of ˜A over ˜Aen. We know,
from Theorem 15.4.2 and Proposition 15.3.24, that each˜Qi is a ﬁnite graded-free
˜Aen-module, and ˜Qi = 0 for i< −n−1. Therefore the complex
P :=Aen⊗˜Aen ˜Q∼=Aen⊗L
˜Aen
˜A∈D(Aen)
is perfect. But according to Theorem 18.3.20(2),A is a direct summand ofP in
D(Aen). Thus A is a perfect complex overAen. This is property (ii) of Deﬁnition
18.6.6.
By Corollary 17.3.14 the graded ring˜A has a balanced dualizing complex˜R :=
˜A(˜µ,l)[n + 1], where ˜µis a graded ring automorphism of ˜A, and l is an integer.
Theorem 18.4.5 says that˜R is a graded rigid dualizing complex over˜A.
Lemma 18.4.16 says that for everyp the ˜A-bimodule Hp( ˜R) is a central bimodule
over Cent( ˜A). Butfor p =−n−1wehave H−n−1( ˜R)∼= ˜A(˜µ,l), andthisimpliesthat
442
Derived Categories | Amnon Yekutieli | 14 Apr 2019
˜µacts trivially on the elementt∈Cent( ˜A). Hence ˜µextends to an automorphism
of ˜At, and there is an isomorphism
(18.6.12) Ind( ˜At)en( ˜R)∼= ˜At(˜µ,l)[n + 1]
in D
(
( ˜At)en, gr
{
. Also there is an induced automorphism µof the ring A, and
formula (18.5.1) shows thatµrespects the ﬁltrationF.
According to Theorem 18.4.15 the noetherian ringA has a rigid NC dualizing
complex
R := (RestAen◦Deg0◦Ind( ˜At)en)( ˜R)[−1]∈D(Aen).
From (18.6.12) we see thatR∼= A(µ)[n] in D(Aen). Now use Proposition 18.6.8
with ν:=µ−1. □
Example 18.6.13. Let g be a ﬁnite Lie algebra overK, with rankK(g) = n, and
letA := U(g) be its universal enveloping algebra. The ringA is noetherian twisted
CY of dimensionn. This was worked out in the paper [166], and is outlined below.
The ring A has a standard noetherian connected ﬁltrationF, such that ¯A =
GrF (A) ∼= K[t1,...,tn], the commutative polynomial ring in n variables, all of
degree 1. The ring ¯A is AS regular of dimension n, as explained in Example
17.3.16. The Rees ring here is the homogeneous universal enveloping ring from
Example 15.2.22.
Theorem 18.6.11 says thatA is twisted CY of dimensionn, with a Nakayama
automorphism νthat respects the ﬁltrationF. In case g is an abelian Lie algebra
(i.e. the Lie bracket is zero), thenνis the identity automorphism. Wheng is semi-
simple, Van den Bergh [154] proved thatνis trivial too. So in these extreme cases
the ringA = U(g) is CY (untwisted).
The general case was done in [166]. Consider the character (i.e. rank1 represen-
tation)n(g) of g, then-th exterior power of the adjoint representation. This can
be seen as a Lie algebra homomorphismϵ: g→K. Then the dualizing automor-
phismµis the unique ring automorphism ofA = U(g) such thatµ(v) =v−ϵ(v)·1A
for v∈g⊆F1(A)⊆A. The Nakayama automorphism isν=µ−1.
The comultiplication ofA makes the tensor product ofA-bimodules into a bi-
module. This allows us to expressA(µ) like this:A(µ)∼=A⊗n(g), where the left
action ofA onn(g) is trivial, and the right action is the coadjoint action.
Given an A-bimodule M, its i-th Hochschild homology is the K-module
HHi(A,M ) := TorAen
i (A,M ), and itsi-th Hochschild cohomologyis HHi(A,M ) :=
Exti
Aen(A,M ).
Theorem 18.6.14 (Van den Bergh Duality, [154]). Let A be an n-dimensional
twisted CY ring, with Nakayama automorphismν. For every M ∈M(Aen) and
0≤i≤n there is an isomorphism
HHi(A,M )∼= HHn−i
(
A,M (ν)
{
in M(K), and it is functorial inM.
The theorem does not require the ringsA nor Aen to be noetherian. We need a
lemma ﬁrst.
Lemma 18.6.15.For a complexM∈D(Aen), and an automorphismµofA, there
is an isomorphismA⊗L
Aen M(µ)∼= A(µ)⊗L
Aen M in D(K). This isomorphism is
functorial inM.
Proof. Itsuﬃcestoproduceafunctorialisomorphism ψ:A⊗AenM(µ)
≃
− →A(µ)⊗Aen
M for M∈M(Aen). We deﬁneψon elementsb∈A and m∈M by the formula
ψ(b⊗m) :=µ(b)⊗m. It must be veriﬁed that the relations coming from the action
443
Derived Categories | Amnon Yekutieli | 14 Apr 2019
of the ringAen are respected byψ. Take a ring elementa1⊗op(a2)∈Aen. Then
in the moduleA⊗AenM(µ) we have equalities
(18.6.16)
(a2·b·a1)⊗m = (b·(a1⊗op(a2)))⊗m =
=b⊗((a1⊗op(a2))·µm) =b⊗(a1·m·µ(a2)).
See formula (18.6.5). In the moduleA(µ)⊗AenM we have equalities
(18.6.17)
µ(a2·b·a1)⊗m = (µ(a2)·µ(b)·µ(a1))⊗m =
= (µ(b)·µ(a1⊗op(µ(a2))))⊗m
=µ(b)⊗((a1⊗op(µ(a2)))·m)
=µ(b)⊗(a1·m·µ(a2)).
The isomorphismψsends the ﬁrst (resp. last) term in (18.6.16) to the ﬁrst (resp.
last) term in (18.6.17). □
Proof of Theorem18.6.14. We are given an isomorphism
(18.6.18) A(ν)[−n]∼= RHomAen(A,A en)
in D(Aen). Consider these isomorphisms
(18.6.19)
A⊗L
AenM(ν)[−n]∼=1 A(ν)[−n]⊗L
AenM
∼=2 RHomAen(A,A en)⊗L
AenM
∼=3 RHomAen(A,A en⊗L
AenM)∼=4 RHomAen(A,M )
in D(K). The ﬁrst isomorphism is by Lemma 18.6.15. The isomorphism∼=2 comes
from (18.6.18). The isomorphism∼=3 is by derived tensor-evaluation, and it holds
because A is perfect overAen, see Theorem 14.1.22. The isomorphism∼=4 is clear.
Taking Hi(−) in (18.6.19) we obtain an isomorphism
TorAen
n−i
(
A,M (ν)
{∼= Exti
Aen(A,M )
in M(K). Functoriality is clear. □
Remark 18.6.20. Here is a quick discussion of the evolution of theCalabi-Yau
concept. In algebraic geometry, ann-dimensional smooth proper schemeX over a
ﬁeldKhas thecanonical sheafωX := Ωn
X/K; this is a rank1locally freeOX-module.
In the paper [24] from 1990, A.I. Bondal and M.M. Kapranov introduced theSerre
functor
(18.6.21) S :=ωX[n]⊗OX (−).
This is an auto-equivalence of the derived categoryDb
c(X) = Db
c(ModOX) which
admits a bifunctorial isomorphism
(18.6.22) HomDb
c (X)(M,N )∼= HomDb
c (X)(N, S(M))∗.
Here (−)∗:= HomK(−,K). This is an upgrade of the familiar Serre Duality forX,
which is the special case whereM =OX andN is the translation of a locally free
OX-module.
The Serre functor makes sense on anyK-linear triangulated category D that
has suitable ﬁniteness properties (“smooth” and “proper”). It is a triangulated
auto-equivalence S of D admitting a bifunctorial isomorphism
(18.6.23) HomD(M,N )∼= HomD(N, S(M))∗
in M(K) for M,N ∈D. In [24] it was proved that if a Serre functor exists, then it
is unique. In many situations (where this makes sense) the Serre functor is realized
by tensoring with the rigid dualizing complex. This is true in the geometric context
above, in which the rigid dualizing complex of the schemeX isωX[n]; see formula
444
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(18.6.21). It is also true for a regular ﬁniteK-ring A, as explained in Example
18.6.24 below.
Back in algebraic geometry, a smooth proper schemeX is called Calabi-Yau if
the canonical sheafωX is trivial. (Examples are abelian varieties and K3 surfaces.)
The CY condition implies that the Serre functor S is isomorphic to Tn, the n-
th power of the translation functor ofD = Db
c(X). Thus the dimension ofX is
precisely the ratio between the auto-equivalencesS and T.
Around the year 1994, M. Konstevich began discussingHomological Mirror Sym-
metry, which is a vast and deep program (still not fully understood) relating the
algebraic geometry of a CY schemeX (as above) with thesymplectic geometryof
its mirror partner manifoldY. See [88] for more information on this program.
Among the ideas arising in the discussion by Kontsevich was that of aCalabi-
Yau category. This is a smooth proper K-linear triangulated category D, whose
translation functor T and Serre functor S satisfy the numerical relation S∼= Tn
for some integern, called theCY dimension of A. More generally, if the relation
Sm∼= Tn holds for somem,n ∈Z, then D is called fractionally CY of dimension
(n,m ). By abuse of notation, such a ringA is sometimes called fractionally CY of
dimension n/m.
The concept of CY triangulated categories later showed up in various mathe-
matical areas, including:
•Algebraic geometry (see [91]).
•Conformal ﬁeld theories (see [42]).
•Representation theory of algebras and cluster categories (see [36], [33], [82],
[84], [92] and Example 18.6.24 below).
In the preprint [52] from 2006, V. Ginzburg deﬁnedCalabi-Yau algebras. At
about the same time K. Brown and J.J. Zhang [32] introducedrigid Gorenstein
algebras. These are both precisely the CY rings from Deﬁnition 18.6.6 above.
Eventually the CY terminology was adopted by ring theorists.
In caseA is a noetherian connected graded ring, then it is twisted CY in the
graded sense if and only if it is AS regular; see [123]. More results on graded CY
rings can be found in [124] and its references.
We ﬁnish the subsection (and the book) with an example of a fractionally CY
category.
Example 18.6.24.SupposeA is a ﬁniteK-ring. (Traditional texts would say that
A is a ﬁnite dimensionalK-algebra.) We claim that the rigid dualizing complex of
A isR :=A∗, theK-linear dual ofA. ThatR∈D(Aen) is a NC dualizing complex
over A is very easy to see (cf. Deﬁnition 18.1.12). As for rigidity: in this case it
is just linear algebra. Indeed,R⊗R =A∗⊗A∗∼= (Aen)∗in M(Afour), and hence
there are canonical isomorphisms
SqA(R) = RHomAen(A,R⊗R)∼= HomAen(A, (Aen)∗)∼=A∗=R
in D(Aen).
Now let’s assume thatA is regular, i.e. it has ﬁnite global cohomological dimen-
sion. (If the base ﬁeldK is perfect, one can show thatA is homologically smooth
over it; see [60] and [35].) Then, according to Theorems 14.1.33 and 14.1.22, every
object of Db
f (A) is a compact object ofD(A). This includesR. SoR satisﬁes con-
dition (iii) of Theorem 14.4.16, and therefore it is a tilting complex overA. We see
that the triangulated functor
S :=R⊗L
A (−) : Db
f (A)→Db
f (A)
is an auto-equivalence.
445
Derived Categories | Amnon Yekutieli | 14 Apr 2019
It turns out thatS is a Serre functor ofDb
f (A). Let us prove this. ForM,N ∈
Db
f (A) we have canonical isomorphisms
RHomA(N, S(M)) = RHomA(N,A∗⊗L
AM)
∼=†RHomA(N,A∗)⊗L
AM∼=N∗⊗L
AM
in D(K). The isomorphism∼=†is by derived tensor-evaluation, and it holds because
N is a compact object ofD(A). Therefore we get functorial isomorphisms
(18.6.25)
RHomA(N, S(M))∗∼= (N∗⊗L
AM)∗∼= RHomK(N∗⊗L
AM,K)
∼=♥RHomA(M, RHomK(N∗,K))∼= RHomA(M,N )
in D(K). The isomorphism∼=♥is by adjunction for the ring homomorphismK→A.
Taking H0 in (18.6.25) we obtain a functorial isomorphism
HomDb
f (A)(N, S(M))∗∼= HomDb
f (A)(M,N )
in M(K).
Finally we specialize to the setting of Example 14.5.30. SoA is the ring of upper
triangularn×n matrices overK for somen≥2. As calculated by A. Yekutieli and
E. Kreines in [165], there is an isomorphism
R⊗L
A···⊗L
AR/b∏aceh⋃ipuplef⋃/b∏aceh⋃ipdo⋀⨁∏igh⋃/b∏aceh⋃ipdo⋀⨁lef⋃/b∏aceh⋃ipup∏igh⋃
n+1
∼=A[n−1]
in D(Aen). Since the translation functor ofDb
f (A) is T∼=A[1]⊗L
A (−), we obtain an
isomorphism of functorsSn+1∼= Tn−1. The conclusion is that the categoryDb
f (A)
is fractionally CY of dimension(n−1,n + 1).
446
Derived Categories | Amnon Yekutieli | 14 Apr 2019
