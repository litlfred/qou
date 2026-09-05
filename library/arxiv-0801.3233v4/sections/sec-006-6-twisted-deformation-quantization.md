---
doc_id: arxiv-0801.3233v4
doc_title: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli"
section_id: sec-006-6-twisted-deformation-quantization
section_title: "Twisted Deformation Quantization"
section_number: 6
pages: 7-9
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
doc_brief: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0."
---
The above can be sheaﬁﬁed: to a deformationA ofOX we assign the sheaf of
groups IG(A), etc.
Let us ﬁx an aﬃne open covering{U0,...,Um}of X. We write
Ui,j,...:=Ui∩Uj∩···.
Deﬁnition 5.1.A twisted associative(resp. Poisson) deformation A ofOX con-
sists of the following data:
(1) For anyi, a deformationAi ofOUi.
(2) For anyi<j , a gauge equivalence
gi,j :Ai|Ui,j→Aj|Ui,j.
(3) For anyi<j <k , an element
ai,j,k∈Γ
(
Ui,j,k, IG(Ai)
{
.
The conditions are:
(i) For anyi<j <k one has
g−1
i,k◦gj,k◦gi,j = ig(a−1
i,j,k).
(ii) For anyi<j <k <l one has
a−1
i,j,l·ai,k,l·ai,j,k =g−1
i,j (aj,k,l).
Condition (i) says that the 2-cochain{ai,j,k}measures the failure of the 1-
cochain{gi,j}to be a cocycle. This tells us whether the collection{Ai}of local
deformations can be glued into a global deformation ofOX.
Condition (ii) – usually called the tetrahedron equation – says that the2-
cochain{ai,j,k}satisﬁes a twisted cocycle condition.
See Figure 1 for an illustration.
Example 5.2. IfA is a usual deformation ofOX, then we obtain a twisted defor-
mation A by takingAi :=A|Ui, gi,j := 1 and ai,j,k := 1.
In this way we can view usual deformations as twisted deformations.
There is a notion oftwisted gauge equivalenceA→A′between twisted asso-
ciative (resp. Poisson) deformations ofOX.
Let A be a twisted deformation. We sayA is really twistedif it is not twisted-
equivalent to any usual deformationA′.
Example 5.3. It is easy to construct an example of a commutative twisted asso-
ciative deformation A ofOX that is really twisted. Take an algebraic varietyX
with nonzero cohomology classc∈H2(X,OX). Let U be an aﬃne open covering
of X, and let{ci,j,k}be a Čech2-cocycle representing c on this covering. Now
consider the data
(
{Ai},{gi,j},{ai,j,k}
{
withAi :=OUi[[ℏ]], gi,j := 1 and
ai,j,k := exp(ℏci,j,k).
This twisted deformationA has obstruction classc in the ﬁrst order central exten-
sion (in the sense of [Ye6]). This implies thatA is really twisted.
Remark 5.4. For a twisted associative deformation A there is a well deﬁned
abelian category Coh A of “coherent leftA-modules”, which is a deformation of
the abelian categoryCohOX. See the work of Lowen and Van den Bergh [LV].
8 AMNON YEKUTIELI
Figure 1.
Indeed, there is a geometric Morita theory, which says that twisted associative
deformations ofOX are the same as deformations ofCohOX. This is explained in
the last chapter of the book [KS1] by Kashiwara and Schapira.
We do not know of a similar interpretation of twisted Poisson deformations.
6. Twisted Deformation Quantization
Justasinthecaseofusualdeformations, givenatwisted(associativeorPoisson)
deformation A ofOX, we can deﬁne the ﬁrst order bracket{−,−}A onOX. The
ﬁrst order bracket is invariant under twisted gauge equivalence.
Let A be a twisted Poisson deformation, and letB be a twisted associative
deformation. We say thatB is atwisted quantizationof A if
{−,−}B ={−,−}A.
The next theorem is inﬂuenced by ideas of Kontsevich (from [Ko3] and private
communications).
Theorem 6.1 ([Ye5]). Let K be a ﬁeld containingR, and let X be a smooth
algebraic variety overK. There is a canonical bijection
tw.quant :{twisted Poisson deformations ofOX}
twisted gauge equivalence
≃
−→{twisted associative deformations ofOX}
twisted gauge equivalence ,
called the twisted quantization map, which is a twisted quantization in the sense
above.
TWISTED DEFORMATION QUANTIZATION 9
Asbefore, by“canonical”wemeanthatthetwistedquantizationmapcommutes
with étale morphismsX′→X.
The proof of Theorem 6.1 relies on a rather complicated calculations involv-
ing Maurer-Cartan equations in cosimplicial DG Lie algebras, and cosimplicial2-
groupoids. See Appendices C and D.
The results on pronilpotent gerbes from [Ye6] tell us that whenH1(X,OX) = 0
and H2(X,OX) = 0, there are no really twisted deformations. Thus Theorem 6.1
implies:
Corollary 6.2.Assume the cohomology groupsH1(X,OX) and H2(X,OX) vanish.
Then the functiontw.quant of the theorem gives a bijection
quant :{Poisson deformations ofOX}
gauge equivalence
≃
−→{associative deformations ofOX}
gauge equivalence .
As we already mentioned, ifH1(X,TX) = 0, then all twisted Poisson deforma-
tions are sheaf theoretically trivial. Likewise, ifH1(X,DX) = 0, then all twisted
associative deformations are sheaf theoretically trivial. Hence:
Corollary 6.3. Assume the cohomology groups H1(X,OX), H2(X,OX),
H1(X,TX) and H1(X,DX) vanish. Then the function tw.quant of the theorem
gives a bijection
quant :{formal Poisson brackets onOX[[ℏ]]}
gauge equivalence
≃
−→{star products onOX[[ℏ]]}
gauge equivalence .
The conditions of Corollary 6.3 are satisﬁed, for instance, whenX = Pn
K (n-
dimensional projective space overK).
Let me ﬁnish this survey with a question. Given a varietyX, with Poisson
bracket{−,−}1 onOX, we can form the Poisson deformationA :=OX[[ℏ]] with
bracket ℏ{−,−}1, as in Example 2.2. By viewingA as a twisted Poisson defor-
mation (cf. Example 5.2), and applying Theorem 6.1, we get a twisted associative
deformation B := quant(A).
Question 6.4. Does there exist a varietyX, with a symplectic Poisson bracket
{−,−}1, such that the corresponding twisted associative deformationB is really
twisted?
My feeling is that the answer is positive. And moreover, an example should
be whenX is any Calabi-Yau surface, and{−,−}1 is any nonzero Poisson bracket
on X. It might be possible to settle this question with an explicit (yet very hard)
calculation, since there are explicit formulas for the twisted quantization map.
