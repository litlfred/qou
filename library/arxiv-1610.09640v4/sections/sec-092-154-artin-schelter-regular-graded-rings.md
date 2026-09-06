---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-092-154-artin-schelter-regular-graded-rings
section_title: "Artin-Schelter Regular Graded Rings"
section_number: 15.4
pages: 345-351
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
an important class of graded rings: theArtin-Schelter regular graded rings. These
are connected graded noncommutative rings, that homologically are similar to com-
mutative polynomial rings. A great deal of noncommutative ring theory and ho-
mological algebra grew out of the study of this class of rings. See Remark 15.4.23
for some historical notes.
We continue with Conventions 15.1.17 and 15.2.1. Thus all graded rings are
central over the base ﬁeldK.
Suppose A is a connected graded ring. Recall that the augmentation ideal ofA
is denoted bym. The opposite ring ofA isAop, and the enveloping ring isAen. We
view A/m∼=K as a gradedAen-module.
345
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 15.4.1.Let A be a noetherian connected graded ring.
(1) The graded ringAis called aregular graded ringif it has ﬁnite graded global
cohomological dimension; namely if there is a natural numberd such that
Exti
A(M,N ) = 0 and Exti
Aop(M′,N′) = 0 for alli > d, M,N ∈M(A, gr)
andM′,N′∈M(Aop, gr). The smallest such natural numberd is called the
graded global dimensionof the ringA.
(2) The graded ringA is called aGorenstein graded ringif the graded bimodule
Ahas ﬁnite graded injective dimension overAand overAop; namely if there
is a natural numberd such thatExti
A(M,A ) = 0 and Exti
Aop(M′,A ) = 0 for
all i > d, M∈M(A, gr) and M′∈M(Aop, gr). The smallest such natural
numberd is called thegraded injective dimensionof the ringA.
Recall that the graded projective dimension of a gradedA-moduleM is smallest
generalized integerd∈N∪{±∞}such that Exti
A(M,N ) = 0 for all integersi>d
and allN∈M(A, gr).
The minimal graded-free resolution of a graded module was introduced in Deﬁ-
nitions 15.3.14 and 15.3.17.
Theorem 15.4.2. Let A be a noetherian connected graded ring, and letd be a
natural number. The following ﬁve conditions are equivalent.
(i) The graded ringA is regular, of graded global dimensiond.
(ii) The graded projective dimension of the gradedA-moduleK is d.
(iii) The gradedK-modules TorA
i (K,K) vanish for alli>d , but not fori =d.
(iv) The gradedK-modules Exti
A(K,K) vanish for alli>d , but not fori =d.
(v) LetP→A be the minimal graded-free resolution of the gradedAen-module
A. Then the gradedAen-modulesP−i vanish for alli>d , but not fori =d.
Observe that in this theorem, conditions (i), (iii) and (v) are op-symmetric, but
not conditions (ii) and (iv).
Proof. Consider the minimal graded-free resolutionρ:P→A of A overAen. We
express the graded-freeAen-module P−i, fori≥0, as
(15.4.3) P−i =Aen⊗Vi∼=A⊗Vi⊗A
with Vi∈Mf(K, gr). The ﬁniteness of the gradedK-modules Vi is by Proposition
15.3.24. In formula (15.4.3) the ringAen acts on itself from the left, and it acts on
A⊗Vi⊗A by the outside action, i.e.
(a1⊗op(a2))·(b1⊗v⊗b2) = (a1·b1)⊗v⊗(b2·a2)
for a1⊗op(a2)∈Aen and b1⊗v⊗b2∈A⊗Vi⊗A.
As explained in the proof of Proposition 15.3.24, in the category
Cstr(Aop, gr) the homomorphism ρ: P →A is a homotopy equivalence. Hence,
taking a module M ∈M(A, gr), and writing QM := P⊗A M, we get a quasi-
isomorphism
τM :=ρ⊗idM :QM =P⊗AM→A⊗AM∼=M
in Cstr(A, gr). BecauseM is a graded-freeK-module, it follows that every
Q−i
M =P−i⊗AM∼=A⊗Vi⊗M
is also a graded-freeA-module. In this way we obtain a (functorial) graded-free
resolution τM :QM→M in Cstr(A, gr).
Assume now that condition (v) holds. This means thatVi = 0 for all i > d,
and Vd⁄= 0. The graded-free resolutionQM has lengthd for every nonzeroM∈
M(A, gr). We see that
Exti
A(M,N )∼= Hi(
HomA(QM,N )
{
= 0
346
Derived Categories | Amnon Yekutieli | 14 Apr 2019
for allN∈M(A, gr) andi>d . By the op-symmetry of condition (v), it also follows
that Exti
Aop(M′,N′) = 0 for allM′,N′∈M(Aop, gr) andi>d . This says that the
graded global dimension ofA is at mostd. To get equality, we test forM =N =K.
In this case we know thatQK is a minimal graded-free resolution ofK overA (see
the proof of Proposition 15.3.24), so the complexK⊗AQK has trivial diﬀerential.
Therefore
(15.4.4)
Exti
A(K,K)∼= Hi(
HomA(QK,K)
{
∼= Hi(
HomK(K⊗AQK,K)
{∼= HomK(Vi,K).
This is nonzero fori = d. Likewise over Aop. We have thus veriﬁed conditions
(i), (ii) and (iv). Condition (iii) is veriﬁed similarly: the resolutionQK shows that
TorA
i (K,K)∼=Vi as gradedK-modules.
Let us prove the implication (i)⇒(v): since Exti
A(K,K) = 0 for all i > d,
equations (15.4.4) and (15.4.3) say thatP−i = 0 in this range. On the other hand,
there is some pairM,N ∈M(A, gr) such thatExtd
A(M,N )⁄= 0, and this says that
P−d⁄= 0.
Theotherimplicationsareprovedsimilarly, andweleavethemasanexercise. □
Exercise 15.4.5. Finish the proof of Theorem 15.4.2.
The next condition ﬁrst appeared in the paper [6] by M. Artin and W. Schelter.
Throughout, “AS” is an abbreviation for “Artin-Schelter”.
Deﬁnition 15.4.6.Let A be a noetherian connected graded ring. We say thatA
satisﬁes theAS conditionif there are integersn and l such that
Extn
A(K,A )∼= Extn
Aop(K,A )∼=K(l)
as gradedK-modules, and
Exti
A(K,A )∼= Exti
Aop(K,A )∼= 0
for alli⁄=n. The numbern is called theAS dimensionof A, and the numberl is
called theAS indexof A.
In derived category terms, the AS condition says that
(15.4.7) RHomA(K,A )∼= RHomAop(K,A )∼=K(l)[−n]
in D(K, gr),
Deﬁnition 15.4.8.Let A be a noetherian connected graded ring.
(1) We say thatA is an AS regular graded ringof dimensionn if it is a reg-
ular graded ring (Deﬁnition 15.4.1(1)), and it satisﬁes theAS condition
(Deﬁnition 15.4.6) with AS dimensionn.
(2) We say thatA is an AS Gorenstein graded ringof dimension n if it is a
Gorenstein graded ring (Deﬁnition 15.4.1(2)), and it satisﬁes theAS con-
dition (Deﬁnition 15.4.6) with AS dimensionn.
As we shall see later, in Subsection 16.5, the AS condition implies that the local
cohomology of graded A-modules behaves as though A is commutative. In the
paper [10] by Artin and J.J. Zhang, subsequent to [6], this behavior was formalized
as theχcondition; see Deﬁnition 16.5.14 below.
Some texts do not make the assumption that the connected graded ringA is
noetherian, as we did in Deﬁnition 15.4.8. However, without this assumption the
theory is not as rich.
It is natural to ask whether the AS dimension of the ringA coincides with its
graded global dimension (in the AS regular case), or with its graded injective di-
mension (in the AS Gorenstein case). The next propositions say that these numbers
agree.
347
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proposition 15.4.9. LetA be an AS regular graded ring. Then the AS dimension
of A equals its graded global dimension.
Proof. Let n be the graded global dimension ofA. Let P →A be the minimal
graded-free resolution of the gradedAen-module A. By Theorem 15.4.2 we know
that the graded Aen-modules P−i vanish for alli > n, but not fori = n. Let
QK→K be the induced graded-free resolution of theA-moduleK from the proof
of Theorem 15.4.2. Then the complexQK is concentrated in cohomological degrees
[−n, 0], and Q−n
K ⁄= 0. Also, as shown there, QK→K is a minimal graded-free
resolution ofK overA.
Now letT := HomA(QK,A )∈C(Aop, gr), so RHomA(K,A )∼=T in D(K, gr). A
quick calculation shows thatT is a minimal complex of graded-freeAop-modules.
Thiscomplexisconcentratedincohomologicaldegrees [0,n ], andTn⁄= 0. Therefore
Extn
A(K,A )∼= Hn(T )⁄= 0. A similar calculation shows thatExtn
Aop(K,A )⁄= 0. We
see that the AS dimension ofA is n. □
Proposition 15.4.10. Let A be an AS Gorenstein graded ring. Then the AS
dimension ofA equals its graded injective dimension.
Proof. This is an immediate consequence of [72, Theorem 4.5]. □
In Examples 17.3.15 and 17.3.16 we will present some important kinds of AS
regular rings.
Deﬁnition 15.4.11.Let A be a nonzero graded ring. A central elementa of A is
called aregular central elementif it is not a zero-divisor; i.e.a·b = 0 impliesb = 0.
If the elementa∈A is not central, then we have to distinguish between left and
right regularity ofa.
The next two theorems discuss the relation between the ringsA andB from the
following setup.
Setup 15.4.12. Let A be a noetherian connected graded ring, and leta∈A be
a homogeneous regular central element of positive degree. Deﬁne the connected
graded ringB :=A/(a).
Theorem 15.4.13. Assume Setup15.4.12.
(1) If B is a regular graded ring of graded global dimensionn−1, thenA is a
regular graded ring of graded global dimensionn.
(2) Moreover, ifB is an AS regular graded ring of dimensionn−1, thenA is
an AS regular graded of dimensionn.
Proof.
(1) By Theorem 15.4.2, to prove thatA is a regular graded ring of graded global
dimension n, it is enough to show that the cohomology of the complexK⊗L
AK∈
D(K, gr) has concentration [−n, 0]. Because a graded-free resolution ofK over A
is also a free resolution in the ungraded sense, and because we are only interested
in the vanishing of cohomology, we can forget the algebraic grading, and just look
at the complexK⊗L
AK∈D(K). Similarly, becauseB is a regular graded ring of
graded global dimensionn−1, we know that the complexK⊗L
BK∈D(K) satisﬁes
(15.4.14) con
(
H(K⊗L
BK)
{
= [−n + 1, 0].
Let ˜B := K(A,a ) be the Koszul complex on the regular central elementa∈A;
namely
˜B =
(
···→0→A
a·(−)
− −−− →A→0→···
{
,
concentrated in cohomological degrees−1 and 0. This is a DG ring: as a cohomo-
logically graded ring we have˜B :=A⊗K[x], whereK[x]is the strongly commutative
348
Derived Categories | Amnon Yekutieli | 14 Apr 2019
polynomial ring on the variablex that has cohomological degree−1 (see Examples
3.1.23 and 3.3.9). The diﬀerential isd(x) := a. The canonical DG ring homomor-
phism ˜B→B is a quasi-isomorphism. Also ˜B is semi-free DG module overA and
overAop. According to Theorem 12.7.2(2) there is an isomorphism
(15.4.15) K⊗L
BK∼=K⊗L
˜BK
in D(K).
By the associativity of the derived tensor product, and becauseK is a DGA-
module via the DG ring homomorphismA→˜B, there are isomorphisms
(15.4.16) K⊗L
AK∼=K⊗L
A ( ˜B⊗L
˜BK)∼= (K⊗L
A ˜B)⊗L
˜BK
in D(K). Now the image of the elementa inK is zero, so we obtain these isomor-
phisms
K⊗L
A ˜B∼=K⊗A ˜B∼=
(
K
0·(−)
−−−→K
{∼=K[1]⊕K
in D( ˜Bop). Substituting this into (15.4.16) we get
K⊗L
AK∼=
(
K[1]⊕K
{
⊗L
˜BK∼= (K⊗L
˜BK)[1]⊕(K⊗L
˜BK)
in D(K). Hence
(15.4.17) Hi(
K⊗L
AK
{∼= Hi+1(
K⊗L
BK
{
⊕Hi(
K⊗L
BK
{
asK-modules. This, together with (15.4.14), imply thatcon
(
H(K⊗L
AK)
{
= [−n, 0],
as required.
(2) NowB is an AS regular graded ring of dimensionn−1. As explained in part
(1) of the proof, we may neglect the algebraic grading, and we only need to prove
that
(15.4.18) RHomA(K,A )∼=K[−n]
in D(K).
Let ˜B be the DG ring from above. BecauseK is a DGA-module via the DG
ring homomorphismA→˜B, there is an adjunction isomorphism
(15.4.19) RHomA(K,A )∼= RHom ˜B
(
K, RHomA( ˜B,A )
{
in D(K). Now ˜B is a semi-free DG module overA, so
RHomA( ˜B,A )∼= HomA( ˜B,A )∼=
(
A
(−)·a
− −−− →A
{∼=B[−1]
in D( ˜B). Substituting this into (15.4.19), and using Theorem 12.7.2(2), we get
RHomA(K,A )∼= RHom ˜B
(
K,B [−1]
{∼= RHomB(K,B )[−1]
in D(K). The AS condition forB says that RHomB(K,B )∼=K[−n + 1] in D(K).
Hence the isomorphism (15.4.18) holds. □
Remark 15.4.20. The proof of the theorem above can actually yield more, with
some modiﬁcations. If we were to make the DG ring˜B into a bigraded object, with
both algebraic and cohomological grading, then we would obtain an isomorphism
(15.4.15) in the derived categoryD( ˜B, gr) of bigraded DG˜B-modules. The problem
is that we did not develop this kind of theory in the book...
The outcome of this more reﬁned construction would be that formula (15.4.17) is
an isomorphism inM(K, gr). This would give the ability to compare the AS indexes
ofA andB. As can be guessed (cf. the easy case of Example 17.3.16, takinga to be
one of the variables), if the AS index ofA isl, then the AS index ofB isl−deg(a).
Theorem 15.4.21. Assume Setup15.4.12.
(1) If A is a Gorenstein graded ring of graded injective dimensionn, thenB is
a Gorenstein graded ring of graded injective dimension at mostn−1.
349
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) Moreover, ifA is an AS Gorenstein graded ring of dimensionn, thenB is
an AS Gorenstein graded ring of dimensionn−1.
Exercise 15.4.22. Prove Theorem 15.4.21. (Hint: Study the proof of Theorem
15.4.13.)
Remark 15.4.23.Herearesomehistoricalnotesonthematerialinthissubsection.
Around 1985, M. Artin and W. Schelter [6] began a systematic study of connected
graded noncommutative rings (better known as graded algebras), with the hope of
obtaining a classiﬁcation in low dimensions, in analogy to the commutative pro-
jective geometry of curves and surfaces. This is how the concept ofArtin-Schelter
regular graded ringswas born. Closely related concepts areSklyanin algebrasand
Koszul algebras.
The area of research initiated by Artin and Schelter is often calledNC algebraic
geometry. Indeed, in 1994 Artin and J.J. Zhang [10] introduced the concept ofNC
projective scheme. Given a noetherian connected graded ringA, let Mtor(A, gr)⊆
M(A, gr) be the full subcategory on them-torsion modules. The quotient abelian
category M(A, gr)/Mtor(A, gr) is viewed as the category of quasi-coherent sheaves
on an imaginary schemeProj(A). Note that ifA happens to be commutative, then,
by the famous theorem of J.P. Serre, this quotient category is canonically equivalent
to QCohX, whereX = Proj(A) is the genuine projective scheme. The geometric
metaphor of Artin and Zhang turned out to be very useful in predicting “geometric
properties” of connected graded rings, that were later proved algebraically, working
in M(A, gr) or its derived categoryD(A, gr).
For AS regular graded rings of dimension≤3 generated in degree1, the classiﬁ-
cation was pretty much complete by 1991, in papers by Artin, jointly with J. Tate
and M. Van den Bergh; see the papers [8] and [9], and the survey [145]. Research
on AS graded rings of higher dimensions, and with generators in various degrees,
was later conducted by J.T. Staﬀord, S.P. Smith, Zhang, and their students and
collaborators.
In2006, V.Ginzburgpublishedthehighlyinﬂuentialpreprint[52]onCY(Calabi-
Yau) algebras. Since then, the research on AS regular rings and their relatives
has merged with the research on CY rings and categories. (It turns out that for
connected graded rings, the twisted CY rings are precisely the AS regular rings.)
See Remark 18.6.20 for more on CY theory. Two of the latest papers on graded
CY rings are [123] and [124].
Inthesubsequentsectionsofthebookweshalldealwithafewideasthatemerged
as by-products of the Artin school of NC algebraic geometry: the χcondition,
balanced dualizing complexes and rigid dualizing complexes.
350
Derived Categories | Amnon Yekutieli | 14 Apr 2019
