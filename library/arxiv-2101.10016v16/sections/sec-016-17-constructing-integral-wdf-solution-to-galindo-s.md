---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-016-17-constructing-integral-wdf-solution-to-galindo-s
section_title: "Constructing integral wdf; solution to Galindo’s problem"
section_number: 17
pages: 117-119
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
17. Constructing integral wdf; solution to Galindo’s problem
In [66] Galindo asks whether a fusion category may admit more than a unitary structure
making it into a unitary tensor category. In [67] the authors solve the problem in some
special cases, e.g. pointed and weakly group theoretical categories, and show in these cases
a stronger property called complete unitarity. A proof has been given by Reutter in [156]
with different methods. The following consequence of Theorem 15.8 gives a positive answer
to Galindo’s question for a wide class of tensor categories with possibly infinitely many
simple objects. Note that we do not assume rigidity. We prove the following Theorem 17.1
stated in the introduction.

118 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Theorem 17.1. Let C1 and C2 be tensor equivalent C
∗
-tensor categories endowed with an
integral weak dimension function (e.g. they are finite semisimple tensor categories). Then
C1 and C2 are also unitarily tensor equivalent.
Proof. It follows from Theorem 15.8 with C1 = C
+ = C, F identity, and C2 = D+. □
In Sect. 5 we have remarked about the role of integral weak dimension functions for
semisimple tensor categories in relation to Tannaka-Krein duality and weak quasi-Hopf
algebras. Moreover in Sect. 15 we have used them to turn C
∗
-categories into tensor C
∗
-
categories. We next show how to construct these functions for a wide classes of categories.
Proposition 17.2. Let C be a semisimple tensor category and d be a positive (symmetric)
weak dimension function on Irr(C) taking values ≥ 1. Then for any integer M ≥ 4,
D(ρ) = M⌊d(ρ)⌋ ρ ∈ Irr(C), ρ ̸= ι, defines an integral (symmetric) weak dimension
function.
Proof. We need to show (7.3) for any pair of non-trivial objects ρ, σ ∈ Irr(C). We have
X
τ∈Irr(C)
D(τ )dim(τ, ρ ⊗ σ) ≤
XM⌊d(τ )⌋dim(τ, ρ ⊗ σ) ≤
XM⌊d(τ )dim(τ, ρ ⊗ σ)⌋ ≤ M⌊d(ρ)d(σ)⌋ ≤ M(⌊d(ρ)⌋ + 1)(⌊d(σ)⌋ + 1) ≤
4M⌊d(ρ)⌋⌊d(σ))⌋ =
4
M
D(ρ)D(σ) ≤ D(ρ)D(σ).
□
Thus all we need to construct integral weak dimension functions is a positive weak
dimension function, and we then ask when such a function exists and how to construct it.
By Prop. 16.1 a necessary condition is that the operators Λρ of left regular representation
of GrC(C) on ℓ
2
(Irr(C)) are bounded. This is also a sufficient condition when GrC(C) is
commutative by Theorem 3.5 in [195]. In the general case, we describe two more classes
of examples.
Theorem 17.3. Any semisimple rigid C
∗
-tensor category or any semisimple rigid tensor
category with amenable fusion ring (e.g. any fusion category) admits a natural positive
symmetric dimension function, and therefore infinitely many integral symmetric weak dimension functions.
Proof. The categories in the statement are all known to admit positive symmetric dimension functions, they are respectively given by the intrinsic dimension [118], the norm of
the left regular representation, see [141] and also Sect 16. Fusion categories are amenable
and the Frobenius-Perron dimension is the unique positive dimension of the representation
ring, cf. Cor. 2.7.8 in [141] and [51]. □
Remark 17.4. The previous result for fusion categories was observed in [125, 165, 82].
More precisely, a semisimple tensor category C with finitely many inequivalent simple
objects always admits positive integral weak dimension functions and when C is a fusion
category then D may be chosen symmetric. An example is given by the function taking

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 119
constant value Maxρ,σ P
τ∈Irr(C)
dim(τ, ρ⊗σ) for non-trivial ξ ∈ Irr(C) [165]. Note that any
other integer larger than the constant value of the previous remark defines another weak
dimension function and this immediately shows that a fusion category admits infinitely
many weak dimension functions.
It follows from Theorem 16.4 that when C is a semisimple rigid tensor category with
amenable fusion ring then every symmetric positive integral weak dimension function
bounds from above the amenable dimension. This interesting bound together with the
results of this section shows the great flexibility of weak quasi-Hopf algebras for this class
of categories.
