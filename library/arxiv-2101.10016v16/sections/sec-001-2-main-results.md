---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-001-2-main-results
section_title: "Main results"
section_number: 2
pages: 11-19
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
2. Main results
In this section we state some of our main results that we prove in this paper regarding
Problems 1, 2, 3, 4, 5, 6.
2.1. Unitarizability of fusion categories: The Kirillov and Galindo conjectures.
Let g be a complex simple Lie algebra and let Uq(g) be the Drinfeld-Jimbo quantum group
specialized at the root of unity q = e
iπ/ℓ, with ℓ a positive integer divisible by d, the ratio
of the square lengths of the long and the short roots, and ℓ/d larger than the dual Coxeter
number h
∨ of g. Let C(g, q, ℓ) denote the associated fusion category. Let us define the level
k associated to ℓ by
ℓ = d(h
∨ + k).
Using general Tannakian methods for weak quasi-Hopf algebras, we develop a main
unitarizability criterion for braided tensor categories, Theorem 15.8. A main consequence
is the solution of Kirillov’s Problem 3 given in Theorem 21.2. The proof is based on the
general theorem to the original Finkelberg’s theorem [55], [56] and Wenzl’s unitarity result
of C(g, q, ℓ) [185].
Theorem 2.1. Under the same assumptions as in Finkelberg’s theorem 21.1, O˜
ℓ becomes
a unitary modular fusion category with Kirillov’s Hermitian structure.
Another consequence of Theorem 15.8 is the first positive answer to Galindo’s question
Problem 6 for a wide class of tensor categories with possibly infinitely many simple objects,
the proof is in Sect. 17, see Theorem 17.1. Another proof has been given by Reutter in
[156] with different methods.
Theorem 2.2. Let C1 and C2 be tensor equivalent C
∗
-tensor categories endowed with an
integral weak dimension function (e.g. they are finite semisimple tensor categories). Then
C1 and C2 are also unitarily tensor equivalent.
These theorems are interesting especially taking into consideration the fact that the
abstract theorem 15.8 on which they rely uses only the choice of an integral weak dimension
function on the affine Lie algebra fusion category. This category naturally admits such a
dimension function given by representations of the simple Lie algebra g and no inner
structure is needed in detail, other than the two cited milestone theorems.
Theorem 2.1 is, in other words, a strong motivation to refine our Tannakian methods
compatibly with the inner structure of the categories. This leads us to seek a direct proof
of the equivalence between quantum group fusion categories and CFT fusion categories.
To get a deeper understanding of our unitarizability criterion for affine Lie algebra fusion

12 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
categories, we need to examine their inner structures and utilize their naturally arising
integral dimension functions.
2.2. Lie algebra and level set up. Our framework relies on the setup in [185], which
applies to all simple Lie algebras, whether simply laced or non-simply laced. The fundamental representation V of g is defined in [185] for each Lie type. We also denote by V
the corresponding quantized counterpart of Uq(g), q = e
iπ/ℓ, and the associated object of
C(g, q, ℓ).
The minimal level for which the fundamental representation belongs to the Weyl alcove
is k = 1 for all types g ̸= E8, and k = 2 for g = E8. Accordingly, we assume throughout
this paper that k ≥ 1 if g ̸= E8 and k ≥ 2 if g = E8.
Remark 2.3. The case g = E8 at level k = 1 yields a trivial pointed braided category,
and it is the only case.
Remark 2.4. The sole exception to the constraints in 2.2 is part (c) of Theorem 2.11,
which establishes the equivalence of our structure with the Huang–Lepowsky braided tensor
structure.
Our strategy to prove part (c) of Theorem 2.11 can be viewed as a wide generalization of
the classification of braided tensor structures for pointed categories case (examples of such
categories are described in Subsect. 25.1 for the type A level k = 1 case). To this aim,
we develop a classification of braided tensor structures in a semisimple pre-tensor category
endowed with a generating object, see Theorems 8.13 and 8.21.
By the main result of [185], C(g, q, ℓ) is a unitary ribbon braided rigid tensor category
with natural unitary representation of the braid group.
2.3. Construction of the weak Hopf algebras AW (g, q, ℓ) (global quantum gauge
groups). The weak Hopf algebras AW (g, q, ℓ) summarized in this subsection will be the
solution of Doplicher-Roberts Problem 1 for the braided tensor categories associated to
the WZW model by Corollary 2.9 and Theorem 2.11.
Starting from [185], in Sect. 31 we recall the construction of a strict braided tensor
category G˜
q with objects the fusion tensor powers of V , and we recall an equivalence from
G˜
q to C(g, q, ℓ) with an embedding full functor. Wenzl identified a natural linear functor
W : G˜
q → Hilb.
In Sect. 9 we introduce the new definition of weak Hopf algebra and Theorem 9.10 gives
a categorical characterization by weak tensor functors in the semisimple case.
Moreover, motivated by the hermitian structure of Uq(g) at q = e
iπ/ℓ, the specialization
of Drinfeld coboundary matrix R of the generic Uh(g) [47] and its explicit relation with
the hermitian structure of Uq(g) detailed by Wenzl in [185], we introduce the definition of
compatible unitary coboundary weak quasi-Hopf algebra in Def. 30.1, which replicates the
properties as for the hermitian structure of the non-semisimple Uq(g) in a unitary setting.
We give a new construction extended to all Lie types and levels of such algebras AW (g, q, ℓ)
associated to Wenzl’s functor W.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 13
Theorem 2.5. Wenzl functor W admits a natural weak tensor structure making AW (g, q, ℓ) :=
Nat(W) into a unitary coboundary weak Hopf C
∗
-algebra with Ω-involution and ribbon tensor structure compatible with C(g, q, ℓ), and with antipode of Kac type. There is a natural
epimorphism of ∗-algebras
π : Uq(g) → AW (g, q, ℓ)
that has support the simple representations of Uq(g) in the Weyl alcove Λ
+(q) and that
satisfies
P π ⊗ π(∆U(a)) = ∆(π(a)) = π ⊗ π(∆U(a))P, P = ∆(I). (2.1)
The unitary coboundary matrix R
AW (g,q,ℓ)
of AW (g, q, ℓ) arises naturally from the (nonsemisimple) Hermitian coboundary matrix R
U
for Uq(g) through Tannakian reconstruction
via
R
AW (g,q,ℓ)
= π ⊗ π(R
U
)∆(I), (2.2)
where R
U
has been constructed in Theorem 31.9. This is a 2-cocycle for AW (g, q, ℓ) as
defined in Def. 9.12. A similar relation holds for the corresponding R-matrices.
The definition of weak tensor functor is given in 4.8. Axioms of unitary coboundary
weak (quasi-)Hopf algebras, their categorical characterization, their main properties are
introduced and studied in Sects. 28, 29, 30. These are special kind of Ω-involutive weak
quasi-Hopf algebras in the sense of Sect. 11, with Ω explicitly associated to the R-matrix
and the ribbon structure. The notion of antipode of Kac type extending a notion used
in the setting of compact quantum groups [141] to the Ω-involutive case, is given in Def.
11.19. Theorem 2.5 will be proved in Sect. 32.
Establishing the stated properties for AW (g, q, ℓ) is not immediately linked to the properties of Uq(g) because the ideal of this algebra defining AW (g, q, ℓ) is not a co-ideal.
2.4. Classification of type A braided fusion categories. The following result is our
first application of the weak Hopf algebras AW (slN , q, ℓ) (first constructed in [25]) to the
study of Problems 4–5. It gives an equivalence between fusion categories in type A with
different methods, by classifying ribbon fusion categories with the same fusion rules as
C(slN , q, ℓ) by their ribbon structure. The Grothendieck ring of C(slN , q, ℓ) is denoted by
RN,ℓ.
To establish equivalences between the fusion categories of vertex operator algebras
(which are not inherently unitary) and those of quantum groups or conformal nets, we
replace the unitarity assumption with the weaker condition of pseudounitarity, see Sect.
25.
Theorem 2.6. Let C and C
′
be pseudo-unitary ribbon fusion categories with ribbon structures θ and θ
′
, assumed positive for N even, and with based Grothendieck rings isomorphic
to RN,ℓ with N + 1 ≤ ℓ < ∞. Let f : Gr(C) → Gr(C
′
) be a based ring isomorphism such
that for each irreducible ρ ∈ C, θ
′
ρ
′ = θρ where ρ
′
is an irreducible in C
′
in the class of f[ρ].
Then there is an equivalence of ribbon braided tensor categories F : C → C
′
inducing f. If
the categories are unitary, F may be chosen unitary.

14 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
The previous result is based on Kazhdan-Wenzl theory [110]. The main conceptual
argument of proof consists of Theorem 2.6 in extending an analogous result by Neshveyev
and Yamashita [140] in the setting of compact quantum groups to our weak Hopf algebras.
This result is a first important step in our study of determining braided tensor structures
of categories related to conformal field theory, in that is gives an insight of how the braided
symmetry determines the associator, a feature that will emerge again in our next results
with more direct methods with the uniqueness Theorems 8.13 and 8.21 for braided tensor
structures in a semisimple category with a tensor product bifunctor, a generating object
admitting a positive integer valued weak dimension function.
Remark 2.7. Theorem 25.1 applies to establish in particular equivalence of the categories
C(slN , q, ℓ) and Rep(V(slN )k) giving an alternative proof of KLF theorem in the type A case.
The proof gives information on the structure of the equivalence. The theorem applies also
to other approaches to braided tensor structures in categories motivated by conformal field
theory, provided they have the prescribed fusion rules and ribbon structure.
Kazhdan-Wenzl theory classifies all the ribbon fusion categories with prescribed Grothendieck rings of type A up to a twist of the associativity morphisms. These twists
have been classified by Kazhdan and Wenzl in [110], see also Sect. 25 for more details.
It follows that the categories in the statement correspond to representation categories of
the weak Hopf algebra AW (slN , q, ℓ) up to a twist. Then as anticipated by extending an
argument by Neshveyev and Yamashita to our weak Hopf algebra we prove that the twist
of the associativity morphisms is trivialized by the presence of the braided symmetry. It
is remarkable that their arguments in the setting of compact quantum groups extend to
weak Hopf algebras, because our algebras are not co-associative, strictly speaking. This
contributes to the idea that their lack of co-associativity is limited. We take the opportunity
to note that similar phenomena also occurred in the development of the theory of weak
Hopf algebras Sects. 9, 14, and in the study of amenability in the setting of weak quasiHopf algebras and weak Hopf algebras, see Sect. 16. Moreover, the relevance of weak Hopf
algebras that first emerged in the proof of Theorem 2.6, it emerged again in the direct
proof of Theorem 2.8.
Moreover, Neshveyev and Yamashita proved in the same paper that the categories with
twisted associator in the case where q is real, correspond to compact quantum groups,
and classified these groups, as deformation of the defining compact quantum group. An
analogue of this result for the fusion categories C(slN , q, ℓ) and our weak Hopf algebras
AW (slN , q, ℓ) has been studied in [71].
2.5. Vertex operator algebras and the KLF equivalence. Let Rep(Vgk) be the module category of the affine vertex operator algebra Vgk
at positive integer level k. Let A(Vgk)
be the Zhu algebra.
To connect with the vertex operator algebra fusion category, we develop an analogue
of Drinfeld-Kohno Theorem, see Theorem 30.4, which leaves the structure of compatible
unitary cobundary weak quasi-Hopf algebra invariant. We apply this theorem to our

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 15
AW (g, q, ℓ) to connect to the Zhu algebra A(Vgk
) via Wenzl continuous de-quantization
curve described in [185].
The following result solves Frenkel-Zhu Problem 4 for affine vertex operator algebras at
positive integer levels. This problem has roots in the question by Moore and Seiberg in
conformal field theory, see Problem 2.
Theorem 2.8. With the same notation as above, with q = e
iπ/ℓ with ℓ = d(h∨ + k), we
have:
(a) the Zhu algebra A(Vgk
) admits a canonical structure of compatible unitary coboundary weak quasi-Hopf C
∗
-algebra. The C
∗
structure of A(Vgk
), regarded as a quotient
of U(g), is induced by the classical compact real form of g. The weak quasi-bialgebra
structure is induced by a weak quasi-tensor structure (F0, G0) for Zhu forgetful ∗-
functor
Z : Rep(A(Vgk
)) → Hilb
obtained via a natural isomorphism with Wenzl functor W and a Drinfeld twist.
More in detail, the triple (Z, F0, G0) enriched over the category of Hilbert spaces,
is obtained by transferring the untwisted structure of AW (g, q, ℓ) via Drinfeld-Kohno
theorem 30.4 and Wenzl continuous path on the arc Tq,1 connecting q to 1 clockwise
through Kashiwara-Lusztig specialized canonical bases (Cor. 31.4), that is there is
an isomorphism ϕ and twist T such that
A(Vgk) ≃
ϕ
(AW (g, q, ℓ))T .
(b) The structure in (a) satisfies the strong unitarity property F
∗
0 = G0 on pairs (Vλ, V )
and (V, Vλ)where Vλ is a simple representation and V is the fundamental representation (cf. part b) of Theorem 30.4).
We have used the same notation V and Vλ for the representations of the vertex operator
algebra Vgkand of the Zhu algebra A(Vgk) corresponding to the irreducible objects of the
quantum group fusion categories. Parts (a) and (b) of Theorem 2.8 will be proved in
Subsect. 33.2.
The following result is a consequence of Theorem 2.8 and a combination of our previous
Tannakian constructions and of the general unitarizability and tensor category constructions Sect 15 applied to Zhu’s linear equivalence.
Corollary 2.9. For any complex simple Lie algebra g and all the positive integer levels k
(with k ≥ 2 for g = E8), the linear category Rep(Vgk) becomes a unitary modular tensor
category RepT(Vgk) with the structure induced by Zhu’s linear equivalence
Z : Rep(Vgk) → RepT(A(Vgk)),
where RepT(A(Vgk)) is endowed with the unitary modular fusion category structure induced
by the structure of A(Vgk
) constructed in Theorem 2.8 (a) via the Drinfeld twist T and
Wenzl’s continuous curve. Therefore these constructions give unitary ribbon braided tensor
equivalences
RepT(Vgk)
Z
−→ RepT(A(Vgk)) 2.8,(a)−−−→ Rep(AW (g, q, ℓ)
TK ribbon equiv
−−−−−−−−−−→ C(g, q, ℓ). (2.3)

16 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
The middle equivalence in (2.3) is application of the explicit symmetry provided by
our analogue of Drinfeld-Kohno theorem 30.4 described in Theorem 2.8 (a). The twist T
described by that theorem and the categorical counterpart given by the middle equivalence
above is given by a Drinfeld twist explicitly defined by the action of the R-matrix, more
precisely by the braided and ribbon structure in the two settings, that allow to see in the
vertex operator algebra setting the same structure as that in the quantum group setting,
via the naturally isomorphic algebras AW (g, q, ℓ) and A(Vgk
).
Remark 2.10. Before proceeding further we explicitly notice that Corollary 2.9 gives a
self-contained structure of unitary rigid ribbon braided tensor category on the module
category RepT(Vgk
) of the affine vertex operator algebra Vgk
for all Lie types and levels,
equivalence with the quantum group fusion category by direct construction.
In particular, we have considered both simply laced and non-simply laced Lie types in
a uniform way. Furthermore, we do not use the Knizhnik-Zamolodchikov equations. Our
proof of rigidity of RepT(Vgk
) does not depend on the Verlinde formula.
2.6. Comparing our braided tensor structure of RepT(Vgk
) with Huang-Lepowsky
braided tensor structure RepHL(Vgk). Let us next endow the linear category Rep(Vgk) of
modules of the vertex operator algebra with the ribbon braided tensor structure RepHL(Vgk
)
introduced by Huang and Lepowsky [84]–[93]. The following result, compares the structures of RepHL(Vgk
) and RepT(Vgk), is our solution to Huang’s Problem 5.
Theorem 2.11. We have that:
(a) The representation category Rep(A(Vgk)) admits a natural structure of rigid ribbon
braided tensor category RepHL(A(Vgk)) obtained by transporting Huang-Lepowsky
structure to Rep(A(Vgk)). In this way, Zhu’s linear equivalence
Z : RepHL(Vgk) → RepHL(A(Vgk))
admits a natural structure of ribbon braided tensor equivalence.
(b) Let A(Vgk) be endowed with the twisted unitary compatible coboundary weak quasiHopf structure following Theorem 2.8 (a), and let, as before, RepT(A(Vgk
)) be endowed with the corresponding unitary rigid ribbon braided tensor structure. Then
Z : RepHL(Vgk) → RepT(A(Vgk))
preserves the ribbon for all objects.
Moreover RepT(A(Vgk)) and RepHL(A(Vgk)) have the same tensor product bifunctor. The equivalence structure maps of Z as in (a) w.r.t. the modified structure
for the target category satisfy the braided tensor equivalence equations for the braid
morphisms for pairs (Vλ, V ) and (Vλ, V ), and the associativity morphisms for triples
(Vλ, V, V ), (V, Vλ, V ), (V, V, Vλ)
with Vλ an arbitrary irreducible object.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 17
(c) If g is of one of the Lie types A, B, C, D, G2 then Zhu’s equivalence in (b) is a
ribbon braided tensor equivalence. It follows that the composition
RepHL(Vgk
)
Z
−→ RepT(A(Vgk
)) 2.8,(a)−−−→ Rep(AW (g, q, ℓ)) TK ribbon equiv−−−−−−−−−−→ C(g, q, ℓ) (2.4)
is a ribbon braided tensor equivalence by application of the indicated theorems.
Theorem 2.11 establishes the equivalence with Huang-Lepowsky structure for simply
laced and non simply laced Lie types. By bypassing the analytic monodromy of the KZ
equations entirely and the Verlinde formula, we establish an alternative construction of
the Huang–Lepowsky braided tensor structure.
Our proof starts with the the work of Wenzl [185] alongside the description of the primary
fields by Wassermann [181] for the minimum energy functor of affine Lie algebras in the
type A case. This leads to the description by Frenkel and Zhu of the fusion rules for the
affine vertex operator algebras [61]. The comparison of the two tensor product befunctprs
results in the tensor product Theorem 34.7. Connection between the work by Frenkel and
Zhu with the basic tensor product bifunctor by Huang and Lepowsky is given in Theorem
33.3. The comparison led us to apply the description of the primary fields and also of
the braided symmetry studied by Toledano Laredo in [169]. For the connection with the
vertex operator algebra setting, see Remark 38.16. Part (a) is proved in Sect. 37. The
corresponding abstract result is explicitly stated in Sect. 15, see also Sect. 7 of [149]. The
rest of part (b) summarizes the comparison on the associators described in Theorems 33.4
and 37.24 and of the braiding morphisms Theorems 33.11, 35.1, Remark 38.16.
In part (c), one needs to extend the coincidence of the braiding and associativity morphisms from the special cases considered in part (b) to all such morphisms. Establishing
this result for a given Lie algebra allows one to pass from local to global coincidence
between our analytic tensor structure and the Huang-Lepowsky structure. Because the
corresponding quantum group fusion category is known to be rigid, this global coincidence
provides a new, direct proof of rigidity for the Huang-Lepowsky braided tensor category.
To prove part (c), we establish our main abstract uniqueness theorem, Theorem 8.21 (a
generalization of Theorem 8.13) for braided tensor structures within a category equipped
with a common tensor product bifunctor and a multiplicative generating object (which, in
our application, is the fundamental representation). This theorem operates via cohomological reduction: by exploiting the pentagon and hexagon equations, we show that the global
braided tensor structure is completely and uniquely determined by its values on a subclass
of special objects, directly treatable in the application. The hypotheses of the theorem are
specifically formulated to match the explicit data available in our setting. Consequently,
our final equivalence between our quantum group based structure and Huang-Lepowsky
structure, holds for all classical Lie types and G2, driven by state-of-the-art results concerning the generalized Schur-Weyl dualities between the fundamental representation and the
braid group within the quantum group fusion category. Ultimately, this approach yields
an independent, algebraic derivation of the Huang-Lepowsky braided tensor structure that
entirely bypasses the historical analytic difficulties of the KZ equations and the Verlinde
formula.

18 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Building on the results established in part (b), in this paper we verify the hypotheses of
Theorem 8.21 concerning direct comparison between the braiding and associativity morphisms on the side of the quantum group fusion category for its original structure and for
the Huang-Lepowsky structure transferred to the Zhu algebra, via our Drinfeld twist. The
further verification regarding the duality property of the braid group (i.e. the braid group
generates the morphism spaces between tensor powers of the fundamental representation)
is performed on the quantum group side on the algebra AW (g, q, ℓ). This requires separate verification across the various Lie types. To accomplish this, we compare the original
ribbon braided tensor category structure of the quantum group fusion category with the
untwisted braided tensor category structure coming from the Zhu algebra endowed with
Huang-Lepowsky structure. We do this untwist operation applying the same twist as before
on the module category of the Zhu algebra equipped with the Huang-Lepowsky braided
tensor structure from part (a). At this stage, the final assumption of Theorem 8.21 is the
requirement that the centralizer algebras of the truncated tensor powers of the generating representation V in the quantum group fusion category C(g, q, ℓ) are generated by the
representation of the braid group. For the classical Lie types and G2, this verification is
detailed in Section 11 of [149]. It relies on well-known extensions of quantum Schur-Weyl
duality for types A and C, alongside more recent results concerning the generators and
relations of the centralizer algebras for the vector representation in types B, D, and G2.
The detailed proof of Theorems 8.13 and 8.21 and verification of the duality between the
fundamental representation and the braid group is deferred to [149].
Remark 2.12. Theorem 23.10 gives a unitarizability result for RepHL(Vgk). The proof
is based on our approach to KLF Theorem 2.11 for Huang-Lepowsky ribbon braided tensor structure, proved in later sections. This unitarizability result is further specified by
Corollary 2.9 combined with Theorem 2.11 as follows.
Specifically, Corollary 2.9 is obtained as an application of the general unitarizability and
tensor category construction criterion given in Theorem 15.7 for linear C
∗
-categories. To
apply this theorem we choose C
+ to be the linear C∗
-category of unitary representations
of Vgkregarded as a unitary vertex operator algebra (see [73] and references therein for
the notion of unitary representations of unitary vertex operator algebras), A = A(Vgk),
the unitary compatible weak quasi-Hopf algebra structure of the Zhu algebra given by
Theorem 2.8, and C = Rep(A(Vgk)) regarded as endowed with the ribbon braided tensor
structure induced by A(Vgk). The linear C
∗
-structure of Rep(A(Vgk)) is compatible with
that of C
+ via Zhu’s linear equivalence E+ = Z and its inverse S+ obtained by Zhu [197],
since it corresponds to the classical compact real form of g. Theorem 15.7 then applies and
makes C
+ into a unitary tensor category with tensor product bifunctor described in the
proof of 15.7 via the pair (E
+, S+). The unitary tensor category structure obtained in this
way defines RepT(Vgk
) and is also rigid and unitary ribbon braided as so is Rep(A(Vgk
)).
Thanks to the ribbon braided tensor equivalence between RepT(Vgk) and RepHL(Vgk)
by (c) of Theorem 2.11 for the specified Lie types, the unitarizability then holds also for
Huang-Lepowsky ribbon braided tensor category RepHL(Vgk
).

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 19
Applicative aspects of hermitian forms of vertex operator algebras and connections with
hermitian forms on the Zhu algebra are discussed in Sect. 23, see in particular the general
criterion given in Theorem 23.9. More examples of unitarization of module categories of
vertex operator algebras fulfilling the needed assumptions are discussed in conclusion of
the same section.
