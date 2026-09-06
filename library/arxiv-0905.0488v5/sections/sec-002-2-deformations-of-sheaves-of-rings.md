---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-002-2-deformations-of-sheaves-of-rings
section_title: "Deformations of Sheaves of Rings"
section_number: 2
pages: 15-19
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
In this section we recall material from the companion papers [Ye7] and [Ye9]. For
the rest of the paper we work over a base ﬁeldK of characteristic 0. All algebras
are by defaultK-algebras, and all homomorphisms are by default overK. Further
conventions are that associative algebras are unital, and commutative algebras are
associative (and unital). For K-modules M,N we writeM⊗N := M⊗KN and
Hom(M,N ) := HomK(M,N ).
Deﬁnition 2.1.Aparameter K-algebraisacompletelocalnoetheriancommutative
K-algebraR, with maximal idealm and residue ﬁeldR/m = K. We sometimes say
that (R, m) is a parameter K-algebra. For i≥0 we letRi := R/mi+1. The K-
algebra homomorphismR→K is called the augmentation ofR.
By homomorphism of parameter algebrasR→R′we mean aK-algebra homo-
morphism (it is automatically a local homomorphism).
Note thatR can be recovered fromm, sinceR = K⊕m as K-modules, with the
obvious multiplication.
Example 2.2. The most important parameter algebra in deformation theory is
K[[ℏ]], the ring of formal power series in the variableℏ. A K[[ℏ]]-deformation (see
below) is sometimes called a “1-parameter formal deformation”.
Remark 2.3. Some of the deﬁnitions and results in the paper hold for a ﬁeldK
of arbitrary characteristic. (A few of them hold even for any commutative ringK
and any commutativeK-algebraR.) A rule of thumb is that whenever exponential
functionsoccur, weneedcharacteristic 0. Forthesakeofclaritywerestrictattention
to a ﬁeld of characteristic0 and parameter algebras over it.
16 AMNON YEKUTIELI
Let (R, m) be a parameter algebra, and letM be an R-module. The m-adic
completion ofM is theR-module ˆM := lim←i (Ri⊗RM). The moduleM is called
m-adically completeif the canonical homomorphismM→ˆM is bijective. SinceR
is noetherian, the m-adic completion of anyR-module is m-adically complete; see
[Ye5, Corollary 3.5]. (This may be false whenR is not noetherian.)
Given aK-module V and anR-module M, we letMˆ⊗V := ˆM⊗V, the m-adic
completion of theR-module M⊗V.
Let X be a topological space. Recall that a sheafM of R-modules on X is
called ﬂatif for every pointx∈X the stalkMx is a ﬂatR-module. The m-adic
completion ofM is the sheafˆM := lim←i (Ri⊗RM). The sheafM is called m-
adically completeif the canonical sheaf homomorphismM→ˆMis an isomorphism.
We need some properties of sheaves onX. SupposeU ={Uk}k∈K is a collection
of open sets inX. Fork0,...,km∈K we writeUk0,...,km :=Uk0∩···∩Ukm.
Deﬁnition 2.4.LetN be a sheaf of abelian groups on a topological spaceX.
(1) An open setU ⊂X will be calledN-acyclic if the derived functor sheaf
cohomology satisﬁesHi(U,N ) = 0 for alli> 0.
(2) Now suppose U ={Uk}k∈K is a collection of open sets inX. We say
that the collectionU isN-acyclic if all the ﬁnite intersectionsUk0,...,km are
N-acyclic.
(3) We say thatthere are enoughN-acyclic open setsif for any open setU⊂X,
and any open coveringU ofU, there exists anN-acyclic open coveringU′
of U which reﬁnesU.
Example 2.5. Here are a few typical examples of a topological spaceX, and a
sheafN, such that there are enoughN-acyclic open sets.
(1) X is an algebraic variety over the ﬁeldK (i.e. an integral ﬁnite type sepa-
rated K-scheme), withstructuresheafOX, andN isacoherent OX-module.
Then any aﬃne open setU isN-acyclic.
(2) X is a complex analytic manifold, with structure sheafOX, andN is a
coherentOX-module. Here we takeK = C of course. Then any Stein open
set U isN-acyclic.
(3) X is a diﬀerentiable manifold, with structure sheafOX, andN is anyOX-
module. The ﬁeld isK = R. Then any open setU isN-acyclic.
(4) X is a diﬀerentiable manifold, andN is a locally constant sheaf of abelian
groups. Then any suﬃciently small simply connected open setU isN-
acyclic.
In order to get a good behavior ofm-adically complete sheaves, we shall consider
deformations in the following setup:
Setup 2.6. K is a ﬁeld of characteristic0; (R, m) is a parameterK-algebra; X is
a topological space; andOX is a sheaf of commutativeK-algebras onX. Moreover
X has enoughOX-acyclic open sets.
As Example 2.5 shows this covers many instances. We assume Setup 2.6 for the
rest of this section.
Deﬁnition 2.7.An associativeR-deformation ofOX is a sheafA of ﬂatm-adically
complete associativeR-algebras onX, together with an isomorphism of sheaves of
K-algebras ψ: K⊗RA→OX, called anaugmentation.
LetA andA′be associative R-deformations ofOX. A gauge transformation
g :A→A′is an isomorphism of sheaves ofR-algebras that commutes with the
augmentations toOX.
TWISTED DEFORMATION QUANTIZATION 17
Similarly, given a commutativeK-algebraC, anassociativeR-deformation ofC
is a ﬂatm-adically complete associativeR-algebraA, together with an isomorphism
of K-algebras K⊗RA∼=C.
Observe that we do not impose a condition that an associative deformationA
should be “locally diﬀerential”; see Remarks 3.7 and 3.8 for a discussion.
Recall that a Poisson bracket on a commutativeR-algebra A is an R-bilinear
pairing{−,−}: A×A →A which is a Lie bracket, and is a biderivation (a
derivation in each variable). The pair(A,{−,−}) is called aPoisson R-algebra. A
homomorphism of PoissonR-algebras A→A′is an algebra homomorphism that
respects the Poisson brackets. All of this makes sense also for sheaves ofR-algebras.
Deﬁnition2.8.WeviewOX asasheafofPoisson K-algebraswiththezerobracket.
A Poisson R-deformation ofOX is a sheafA of ﬂatm-adically complete Poisson
R-algebras onX, together with an isomorphism of sheaves of PoissonK-algebras
ψ: K⊗RA→OX, called anaugmentation.
LetA andA′be Poisson R-deformations ofOX. A gauge transformationg :
A→A′is an isomorphism of sheaves of PoissonR-algebras that commutes with
the augmentations toOX.
Similarly, given a commutativeK-algebra C, a Poisson R-deformation ofC is
a ﬂatm-adically complete PoissonR-algebra A, together with an isomorphism of
Poisson K-algebras K⊗RA∼=A.
According to [Ye9, Proposition 4.5], ifA is an associative (resp. Poisson)R-
deformation ofOX, andU⊂X is anOX-acyclic open set, thenA := Γ(U,A) is an
associative (resp. Poisson)R-deformation ofC := Γ(U,OX). The important fact is
that A is a ﬂat andm-adically completeR-module.
LetA be an associative (resp. Poisson)R-deformation ofOX. It has an R-
bilinear Lie bracket[−,−] on it. In the associative case let⋆denote the multipli-
cation. Given local sectionsa1,a 2∈A, their bracket is[a1,a 2] :=a1⋆a2−a2⋆a1.
In the Poisson case we take the Poisson bracket:[a1,a 2] := {a1,a 2}. Note that
[A,A]⊂mA. According to [Ye9, Corollary 3.8], for everyj≥0 the sheaf mjA is
m-adically complete. Thus we obtain a sheaf of pronilpotent groups
(2.9) Exp(mjA) := lim
←i
Exp(mjA/mj+iA),
and an isomorphism of sheaves of sets
(2.10) exp : mjA
≃
− →Exp(mjA).
In particular we have a sheaf of pronilpotent groups
(2.11) IG(A) := Exp(mA)
that we call thesheaf of inner gauge groupsofA. A gauge transformationg :A→
A′induces a group isomorphism
(2.12) IG(g) : IG(A)→IG(A′).
Consider a local section α∈mA. Let adA(α) : A → Abe the operator
adA(α)(a′) := [α,a′], where [−,−] is the Lie bracket. Then to the group element
a := exp(α)∈IG(A) we can associate the operator
(2.13) ig(a) := exp(adA(α))
onA. It turns out thatadA(α) is a derivation of the algebraA, and henceig(a) is
a gauge transformation ofA. In the associative case the groupIG(A) is canonically
identiﬁed with the kernel of the augmentation homomorphismψ:A×→O×
X, and
then ig(a) becomes conjugation by the invertible elementa. In the Poisson case we
call ig(a) a formal hamiltonian ﬂow. See [Ye9, Section 5] for details.
18 AMNON YEKUTIELI
Deﬁnition 2.14.We denote byAssDef(R,OX) (resp. PoisDef(R,OX)) the crossed
groupoid P = (P1, P2, AdP1↷P2, D) described as follows:
•The objects of P are the associative (resp. Poisson)R-deformationsA of
OX.
•The 1-morphisms, i.e. the elements of the sets P1(A,A′), are the gauge
transformations g :A→A′.
•The groups of2-morphisms are P2(A) := Γ(X, IG(A)).
•The twisting by a1-morphism g is AdP1↷P2(g) := IG(g).
•The feedback D : P2(A)→P1(A) is D(a) := ig(a).
According to [Ye9, Proposition 5.7] these are indeed crossed groupoids.
In the next two propositions we write P(R,X ) for either AssDef(R,OX) or
PoisDef(R,OX); etc.
Proposition 2.15. Let U′⊂U be open subsets ofX, andR→R′a homomor-
phism of parameter algebras. There is a morphism of crossed groupoidsP(R,U )→
P(R′,U′), sendingA to (R′ˆ⊗RA)|U′.
Proof. ForR→R′this is [Ye9, Proposition 5.8]. ThatA|U′is a deformation of
OU′is trivial. □
Proposition 2.16. The assignmentU↦→P(R,U ) is a stack of crossed groupoids
on X.
Proof. By Proposition 2.15 we have a morphism of crossed groupoids
restV/U : P(R,OU)→P(R,OV )
for every inclusionV ⊂U of open sets. So the local objects and local1-morphisms
form a split prestack of groupoids, say P1. Since the property of being an R-
deformation ofOX is local, and gauge transformations between deformations are
local, it follows that P1 is a stack. Finally, we know that the local2-morphisms
form sheaves of groups (these are the sheavesIG(A)). □
Deﬁnition 2.17. (1) The stack of crossed groupoidsU ↦→AssDef(R,OU) is
called thestack of associativeR-deformations ofOX, and it is denoted by
AssDef(R,OX).
(2) The stack of crossed groupoidsU↦→PoisDef(R,OU) is called thestack of
Poisson R-deformations ofOX, and it is denoted byPoisDef(R,OX).
We now discuss ﬁrst order brackets. SupposeA is an R-deformation ofOX.
SinceA is ﬂat overR, and we have the augmentationψ: K⊗RA
≃
− →OX, there is
an induced K-linear isomorphism mA/m2A∼= (m/m2)⊗OX. This gives rise to a
homomorphism of sheavesψ+ : mA→(m/m2)⊗OX.
Suppose A is an associative deformation, with multiplication ⋆. Given local
sections a1,a 2∈A, the commutator satisﬁesa1⋆a2−a2⋆a1∈mA. Hence we get
(2.18) ψ+(a1⋆a2−a2⋆a1)∈(m/m2)⊗OX.
Likewise ifA is a Poisson deformation, with Poisson bracket{−,−}, then we have
ψ+({a1,a 2})∈(m/m2)⊗OX.
Proposition 2.19. LetA be associative (resp. Poisson) R-deformation ofOX.
There is a uniqueK-bilinear sheaf morphism
{−,−}A :OX×OX→(m/m2)⊗OX
having the following property. Given local sectionsc1,c 2∈OX, choose local liftings
a1,a 2∈Arelative to the augmentationψ:A→OX, i.e.ci =ψ(ai). Then
{c1,c 2}A =ψ+(1
2(a1⋆a2−a2⋆a1)
{
TWISTED DEFORMATION QUANTIZATION 19
or
{c1,c 2}A =ψ+({a1,a 2}),
as the case may be.
Proof. This is a variant of the usual calculation in deformation theory. The only
thing to notice is that it makes sense for sheaves. □
Deﬁnition 2.20.The ﬁrst order bracketofA is the K-bilinear sheaf morphism
{−,−}A in the proposition above.
Proposition 2.21. (1) The ﬁrst order bracket is gauge invariant. Namely if
A and B are gauge equivalent R-deformations ofOX, then {−,−}A =
{−,−}B.
(2) The bracket{−,−}A is a biderivation ofOX-modules.
(3) Suppose R = K[[ℏ]]. Using the isomorphism ℏ−1 : m/m2 ≃
− →K, we get a
bilinear function
{−,−}A :OX×OX→OX.
Then this is a Poisson bracket onOX.
Proof. All these statements are easy local calculations. □
