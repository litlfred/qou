---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-010-112-algebro-geometric-quotient
section_title: "Algebro-geometric quotient"
section_number: 1.1.2
pages: 17-19
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
The action of the group SL2(k) on R(Γ) induces a natural action on its algebra
of functions k[R(Γ)] by pre-composition. The sub-algebra of invariant functions
k[R(Γ)]SL2 is known to be ﬁnitely generated, although this is a delicate problem
ﬁrst answered by Hilbert in the late nineteenth century. There is an amount of good
references on the topic, let us just mention [MFK93] and [KP96].
16
Recall that any ﬁnitely generatedk-algebraA is the quotient of an algebra of poly-
nomials, in other words there is an exact sequence0→I→k[X1,...,X n]→A→ 0.
By Hilbert’s basis theorem, the idealI is ﬁnitely generated, henceA deﬁnes an al-
gebraic setV (I)⊂ kn, namely the zero-locus of any generating set of polynomials
for I. Up to isomorphism, this set does not depend on the presentation ofA, hence
we denote bySpec(A) the aﬃne algebraic variety deﬁned byA.
Remark 1.1.3. In general, the use of the term variety is reserved to irreducible
and reduced algebraic sets. Anirreducible set is a set which is not a reunion of two
proper closed subsets. An irreducible component is a maximal irreducible subset.
Given a ringR, Spec(R) is said to bereduced if R does not contain any nilpotent
element. In particular, by mean of an irreducible component we will assume it to be
reduced. We will call many algebraic objects varieties despite they have no reason
to be irreducible, nor reduced.
Deﬁnition 1.1.4.We deﬁne thecharacter variety X(Γ) = R(Γ)//SL2(k) as the
spectrum Spec(k[R(Γ)]SL2) of the sub-algebra of invariants.
It is usually called the algebro-geometric quotient ofR(Γ) by SL2(k), let us list
without proof some of its properties :
— It comes with a projection mapπ :R(Γ)→X(Γ) that satisﬁes the following
universal property : for any SL2-invariant morphismf : R(Γ)→ Y, with
Y an algebraic variety, there is an unique mapf′ : X(Γ)→ Y such that
f =f′◦π.
— Thek-points of this quotient are in bijection with the closed orbits ofSL2(k)
acting onR(Γ), or with conjugacy classes of semi-simple (or completely redu-
cible) representations ofΓ into SL2(k). In other words, orbits whose closure
intersect inR(Γ) are identiﬁed inX(Γ).
— It is the biggest Hausdorﬀ quotient of the topological quotientR(Γ)/ SL2(k).
Example 1.1.5. Back to Γ = Z, recall that the SL2(k)-orbit of ρ1 : 1 ↦→ ( 1 1
0 1 )
contains the trivial representationρ0 in its closure. We are going to see how the
theory of algebraic quotients solves this problem.
Since the varietyR(Z) is isomorphic to SL2(k), what we want is to compute the
subalgebra of invariant of the algebrak[SL2] = k[X1,1,X1,2,X2,1,X2,2]/(X1,1X2,2−X1,2X2,1−1).
Assume f∈ k[SL2] is an invariant. Then for any diagonalizableA∈ SL2(k), there
is some λ∈ k∗ and g∈ SL2(k) such thatA = g
(λ 0
0 λ−1
)
g−1 hence f(A) = p(λ)
for some polynomialp∈k[t,t−1] that does not depend onA. Moreover, the matrix
17
(λ 0
0 λ−1
)
is conjugated to
(
λ−1 0
0 λ
)
hencep∈k[t+t−1]. Since diagonalizable matrices
form a dense subset ofSL2(k), we conclude thatf∈ k[X1,1+X2,2]/(X1,1X2,2−1), that is
f∈k[Tr]. Reciprocally, it is clear that the trace function is an invariant, hence the
algebra of invariant is isomorphic tok[Tr].
In other words, any representationρ : Z→ SL2(k) is equivalent to1↦→
(λ 0
0 λ−1
)
for
λ∈k∗, such thatλ +λ−1 = Tr(ρ(1)). In particular{ρt}t∈k∗ and ρ0 are identiﬁed in
X(Z), which is isomorphic tok.
Itshouldbeclearfromthisexamplethatthecomputationofthealgebraofinvariants
is in general somewhat diﬃcult, on the other hand it provides a motivation to pay
attention on a particular kind of functions, namely trace functions, which will play
a key role in the next paragraph, and in the rest of this thesis.
Notation. When Γ is the fundamental group of a manifoldM, its character variety
will be denoted byX(M) instead ofX(Γ).
