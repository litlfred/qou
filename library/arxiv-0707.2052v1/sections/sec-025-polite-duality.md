---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-025-polite-duality
section_title: "Polite duality."
section_number: null
pages: 31-38
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
Recall from Section 2.2 that for every space X there is the Serre kernel
ΣX: X→ X such that for spaces X and Y the functor
ΣY ◦ − ◦ ΣX: HomV ar(X, Y)→ HomV ar(X, Y)
is a Serre functor for the category HomV ar(X, Y).
31
Deﬁnition. If Φ : X→ Y and Φ† : Y → X are kernels then a polite du-
ality between them, denoted Φ
∨
←→Φ†, consists of adjunctions as follows
(numbered as shown)
Φ† ◦ ΣY ⊣1 Φ ⊣2 ΣX ◦ Φ†,
Φ ◦ ΣX ⊣3 Φ† ⊣4 ΣY ◦ Φ,
such that the following compatibility relations hold.
(1+2). For kernels Θ : Z→ X and Ψ : Z→ Y, the diagram of iso-
morphisms below commutes:
Hom(Ψ, Φ ◦ Θ)
1
→ Hom(Φ† ◦ ΣY ◦ Ψ, Θ)
Hom(Φ ◦ Θ, ΣY ◦ Ψ ◦ ΣZ)∨
Serre
↓
2
→ Hom(Θ, ΣX ◦ Φ† ◦ ΣY ◦ Ψ ◦ ΣZ)∨ .
Serre↓
(2+3). The composite map
Hom(Θ, Φ†◦Ψ) ∼−→
3
Hom(Φ◦ΣX◦Θ, Ψ) ∼−→
2
Hom(ΣX◦Θ, ΣX◦Φ†◦Ψ)
is the one induced by composition with ΣX.
(3+4). Same as (1+2), but for adjunctions 3 and 4.
(1+4). Same as (2+3), but for adjunctions 1 and 4.
It is useful to think of this deﬁnition in terms of string diag rams. For
each of the four adjunctions we get a unit and a counit. Denoti ng Φ by an
upward oriented line and Φ† by a downward oriented line, we can draw the
units and counits as follows.
η1: η2: η3: η4:
ǫ1 : ǫ2 : ǫ3: ǫ4 :
Relation (2+3) can be represented graphically in the follow ing way: for
any α ∈ Hom(Θ, Φ† ◦ Ψ) we have
Ψ 
α 
Θ 
=
α 
Ψ 
Θ 
.
From this we can deduce the equality
= ,
32
so we deﬁne the following diagram to be this common morphism:
γΦ : .
Similarly we can deduce that the counits ǫ2 and ǫ3 are equal, and we deﬁne
the following diagram to be the common morphism:
ǫ
Φ : .
Likewise, using the relation (1+4), from the units η1 and η4, and the counits
ǫ1 and ǫ4 we obtain the common morphisms denoted as follows.
γΦ ∨ :
ǫ
Φ ∨ :
So the four units and four counits are obtained from these two M-shaped
and two Y-shaped morphisms.
Relations (1+2) and (3+4) in the deﬁnition of polite duality are essen-
tially equivalent to the invariance of the Serre trace under a partial trace
in the following sense. Given a polite duality Φ
∨
←→Φ† and a morphism
α ∈ Hom(Φ◦Θ, Σ◦Φ◦Ψ) we can deﬁne the left partial trace in Hom(Θ, Σ◦Ψ)
with respect to Φ† as drawn below.
Θ 
α 
Ψ 
Similarly we can deﬁne a right partial trace when the Φ is on the right
rather than on the left. So the following diagram is the right partial trace
with respect to Φ and Φ† of a morphism α ′ ∈ Hom(Θ ′ ◦ Φ, Ψ′ ◦ Φ ◦ Σ).
Θ ′
α ′
Ψ ′
Theorem 17. If Φ and Φ† form a politely dual pair of kernels, then the
Serre trace is invariant under partial trace with respect to Φ:
Tr


Ψ 
α 
Ψ 

 = Tr


Ψ 
α 
Ψ 
 ; Tr


Ψ ′
α ′
Ψ ′ 
 = Tr

 α ′
Ψ ′
Ψ ′ 
 .
33
Proof. We will just prove the left partial trace case. Relation (1+2 ) says
that for β ∈ Hom(Ψ, Φ ◦ Θ) and γ ∈ (Θ, Σ ◦ Φ† ◦ Σ ◦ Ψ ◦ Σ) we have the
equality
Tr


Θ 
Ψ 
β
γ
Ψ 


= Tr


Θ 
Ψ 
β
γ
Ψ 


.
Applying this with
β :=
Ψ 
and γ :=
Ψ 
α 
Ψ 
we obtain the equality
Tr


α 
Ψ 
Ψ 


= Tr


Ψ 
Ψ 
α 


.
The result follows from the commutativity property of the Se rre trace,
namely that Tr(β ◦v α) = Tr(S(α) ◦v β).
Proposition 18. Polite dualities Φ
∨
←→Φ† and Ψ
∨
←→Ψ† for two kernels
Φ : X→ Y and Ψ : Y→ Z canonically induce a polite duality
Ψ ◦ Φ
∨
←→Φ† ◦ ΣY ◦ Ψ†.
Proof. The required adjunctions are constructed in the obvious fas hion, us-
ing the fact that the composition, in reverse order, of adjoi nts (left or right)
of composable functors is naturally an adjoint (in the same d irection) of
the composition of the functors. The compatibilities requi red by the polite
duality follow from straight forward checks.
Adjunctions are intrinsic parts of a polite duality. Conver sely, the fol-
lowing proposition shows that any adjunction induces a poli te duality in a
natural way.
Proposition 19. Given an adjunction Ψ ⊣ Φ, deﬁne Φ† := Ψ ◦ Σ− 1
Y . Then
there exists a polite duality Φ
∨
←→Φ† where the adjunction ⊣1 is the given
one Ψ ⊣ Φ.
Proof. As ΣX ◦ Φ† = ΣX ◦ Ψ ◦ Σ− 1
Y , compatibility relation (1+2) yields an
adjunction
Φ ⊣2 ΣX ◦ Φ†.
34
Similarly, relations (1+4) and (2+3) force adjunctions
Φ ◦ ΣX ⊣3 Φ† ⊣4 ΣY ◦ Φ,
and it is easy to see that relation (3+4) is then automaticall y satisﬁed.
Proposition 20. Let Φ ∈ D(X × Y) be a kernel, and let Φ∨ ∈ D(Y × X) be
the dual R HomX×Y(Φ, OX×Y), regarded as a kernel from Y to X. Then there
exists a canonical polite duality Φ
∨
←→Φ∨ .
Proof. For kernels Θ ∈ D(Z × X) and Ψ ∈ D(Z × Y) consider the sequence
of isomorphisms
HomD(Z×Y)(Ψ, Φ ◦ Θ)
∼= HomD(Z×Y)(Ψ, πZY ,∗(π∗
ZXΘ ⊗ π∗
XYΦ))
∼= HomD(Z×X)(πZX,!(π∗
ZYΨ ⊗ π∗
YXΦ∨ ), Θ)
= HomD(Z×X)(πZX,∗(π∗
ZYΨ ⊗ π∗
YX(Φ∨ ⊗ ωY[dim Y])), Θ)
= HomD(Z×Y)((Φ∨ ◦ ΣY) ◦ Ψ, Θ).
Taking Z = Y, Θ = Φ∨ ◦ ΣY and Ψ = IdY yields a morphism of kernels
IdY→ Φ ◦ Φ∨ ◦ ΣY;
in a similar fashion we obtain a morphism
Φ∨ ◦ ΣY ◦ Φ→ IdX.
These two morphisms satisfy the identities needed to make Φ∨ ◦ ΣY the left
adjoint of Φ. Proposition 19 gives the result.
A.2 Reﬂexively polite kernels.
We still need to address one more compatibility between the d ualities con-
structed above. Given a kernel Φ, the previous proposition yields a polite
duality
Φ
∨
←→Φ∨ .
Given any polite duality Φ
∨
←→Φ†, we get, symmetrically, a polite duality
Φ† ∨
←→Φ by switching the adjunctions 1 and 3 and the adjunctions 2 and
4. Thus there is a natural polite duality
Φ∨ ∨
←→Φ.
On the other hand, applying Proposition 20 to the kernel Φ∨ we get a polite
duality Φ∨ ∨
←→Φ∨∨ and then, using the canonical identiﬁcation Φ∨∨ ∼= Φ,
we get another polite duality
Φ∨ ∨
←→Φ.
The fundamental question is whether these two polite dualit ies are the same.
35
Deﬁnition. Let Φ : X→ Y be a kernel. We shall say that Φ is reﬂexively
polite if the two dualities above are equal.
Immediately we get the following result.
Proposition 21. If a kernel Φ is reﬂexively polite then so is Φ∨ .
Proposition 22. If Φ : X→ Y and Ψ : Y→ Z are reﬂexively polite kernels
then so is Ψ ◦ Φ.
Proof. This follows at once from the fact that the adjunctions deﬁne d in
Proposition 18 are canonical.
Proposition 23. Suppose that Φ : X→ Y and Ψ : X ′→ Y ′ are reﬂexively
polite kernels then so is Φ ⊠ Ψ : X × X ′→ Y × Y ′, the kernel deﬁned by
Φ ⊠ Ψ := π∗
XYΦ ⊗ π∗
X′Y ′Ψ.
Proof. This is obvious once one realises that all operations decomp ose with
respect to the box product operation, and the canonical bund le of a product
of spaces is the box product of the canonical bundles of the fa ctors.
Proposition 24. Let ∆ : X→ X × X denote the diagonal map, let E be an
object in D(X), then the kernel ∆∗E : X→ X is reﬂexively polite.
Proof. The dual (∆∗E )∨ of ∆∗E is naturally identiﬁed with
∆∗(E ∨ ⊗ ω− 1
X [− dim X]).
The result now follows from Proposition 2 and the fact that th e functor
given by tensoring with an object of the derived category is l eft and right
adjoint to the one obtained by tensoring with the dual object .
Proposition 25. Let X be a space, then the kernel OX considered as a kernel
X→ pt is reﬂexively polite, and so also is O ∨
X : pt→ X.
Proof. First, observe that checking reﬂexive duality amounts to ch ecking the
equality of two quadruples of adjunctions. In each quadrupl e, any one of
the adjunctions determines the remaining three, and thus in order to check
the equality it suﬃces to check that one of the compatibiliti es (1+2), (1+3),
etc. holds with one adjunction chosen from one duality, and t he other one
from the second duality.
Furthermore, adjunctions are completely determined by the ir respective
units and counits, and these are determined by considered fu nctors between
derived categories of the form
Φ ◦ − : D(Z × X) =: HomV ar(Z, X)→ HomV ar(Z, pt) := D(Z),
and analogues for Φ∨ ◦− , for various choices of the space Z. Thus, if we argue
that the desired equality holds for the adjunctions between these induced
36
functors (for arbitrary choice of Z), we will have argued that Φ is reﬂexively
polite.
For ease of notation, write Φ for the kernel OX: X→ pt. For a given
space Z, let πZ: X × Z→ Z denote the projection. The functors Φ ◦ −
and Φ∨ ◦ − are then naturally identiﬁed with πZ,∗ and π∗
Z, respectively.
Adjunctions 1 and 2 from the polite duality Φ
∨
←→Φ∨ correspond to the
classical adjunctions
π∗
Z ⊣ πZ,∗ ⊣ π!
Z,
while the same ones from the polite duality Φ∨ ∨
←→Φ∨∨ correspond to
πZ,! ⊣ π∗
Z ⊣ πZ,∗.
Indeed, the standard way (see [6, Theorem 4.6]) to deﬁne the a djunctions
πZ,∗ ⊣ π!
Z and πZ,! ⊣ π∗
Z is to require them to satisfy the analogue of condi-
tion (1+2) from the deﬁnition of a polite duality.
The condition of polite duality can now can be stated as the st atement
that the composite isomorphism
HomX×Z(Θ,π∗
ZΨ) ∼= HomZ(πZ,!Θ, Ψ) = HomZ (πZ,∗S(Θ), Ψ)
∼= HomX×Z
(
S(Θ), π!
ZΨ
)
= HomX×Z (S(Θ), S(π∗
ZΨ))
is the one induced by the functor S(−) = − ⊗π∗
XωX[dim X], where πX denotes
the projection from X × Z to X. This fact corresponds to the fact that the
diagram marked (!) below commutes
Hom(Θ, π∗Ψ)
∼
Hom(S− 1π∗SΘ, Ψ)
∼
Hom(π∗SΘ, SΨ)
∼
Hom(SΘ, Sπ∗Ψ)
Serre (!) Serre
Hom(π∗Ψ, SΘ)
∨
∼
∼
Hom(Ψ, π∗SΘ)
∨
∼
= = =Hom(Ψ, π∗SΘ)
∨
∼
∼
Hom(π∗Ψ, Θ)
∨
.
∼
Proposition 26. Let πX: X × Y→ X be the projection, and (abusing nota-
tion) denote by πX,∗ : X × Y→ X and π∗
X: X→ X × Y the kernels represented
in D(X × X × Y) by the structure sheaf of the graph of πX. Then πX,∗ and
π∗
X are reﬂexively polite.
Proof. Both kernels are of the form O∆ X ⊠ OY, and the result then follows
from Propositions 25, 24, and 23.
Theorem 27. Every kernel is reﬂexively polite.
Proof. With notation as in Proposition 26, any kernel Φ : X→ Y decomposes
as
Φ = πY ,∗ ◦ (− ⊗ Φ) ◦ π∗
X.
Since the claim of the theorem holds for each individual kern el in the decom-
position (Propositions 26 and 24), the result follows from P roposition 18.
37
