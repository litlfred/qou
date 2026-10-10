---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-002-3-outline-of-the-paper
section_title: "Outline of the paper"
section_number: 3
pages: 19-23
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
3. Outline of the paper
The first part of the present work is a presentation of the general theory of tensor categories and weak quasi-Hopf algebras, and general Tannakian results both in the algebraic
and C
∗
setting, with or without braiding and ribbon structures. These topics are the
content of Sects. 4–7, 9–14.
Section 9 is dedicated to developing the notion of weak Hopf algebra in a new sense, as
the Hopf algebra counterpart of Mack-Schomerus weak quasi-Hopf algebras. Our definition
differs from the usual notion of weak Hopf algebra, because the coproduct is not strictly
coassociative, but the defining fiber functor is weakly monoidal and the associator explicitly
depends only on the weakness of the coproduct. This includes our previous examples
AW (slN , q, ℓ) of [25] and the new examples AW (g, q, ℓ) constructed later in this paper, in
a general theoretical context.
In Sects. 4, 5 we review tensor categories and their functors. Because CFT fusion
categories are unitary, and are equipped with unitary representations of the braid group,
any reconstruction of quantum gauge group must be equipped with a compatible C
∗
-
structure, which requires considering a new and general notion of an Ω-involution.
Sects 6, 7, 9–13 are devoted to Tannakian duality theorems, both in the algebraic and
unitary case. We introduce a general notion of Ω-involutions for weak Hopf or weak quasiHopf algebras extending and developing the case of quasi-Hopf algebras considered by
Gould and Lekatsas [72].
The notion of Ω-involution describes the unitary structure of our first examples in [25]
in the type A case, with a specific positive matrix Ω explicitly associated to the ribbon
structure and the braiding of AW (slN , q, ℓ), describing positivity of the inner product of
tensor product of representations, and it induces unitary representations of the braid group.
This special kind of Ω-involution is a main interest in later sections of our paper.
Sect. 11 is dedicated to the development of a theory of weak (quasi-)Hopf C
∗
-algebras
with general Ω-involutions, which turns out to unify the theory of the discrete duals of
of the compact quantum groups, where Ω is trivial and the coproduct is unital, with
the unitary structure of the quantum group fusion category C(g, q, ℓ) studied by Wenzl,
associated to the hermitian form of Uq(g) at roots of unity [185].
Ω-involutions arise in Tannakian constructions of quasi-Hopf or weak quasi-Hopf algebras
from tensor C
∗
-categories when the structure maps are not unitary. This property is
inherited by tensor categories equivalent to tensor C
∗
-categories with such maps.
Sects. 14, 15, 26 study unitarizability of braided tensor categories with methods of the
associated weak quasi-Hopf algebras.

20 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
The main result of Sect. 15 is Theorem 15.8, giving a method for unitarizing braided
tensor categories knowing that the category is tensor equivalent to a unitary braided tensor
category.
Section 16 regards amenability, its extends to weak quasi-Hopf algebras known results
from several sources. A main result establishes that when the categorical dimensions are
not integer and the unitary category corresponds to the representation category of a weak
Hopf algebra then necessarily the corresponding Ω-involution can not be trivial. Thus in
cases where one has a trivial Ω-involution then the corresponding algebra can not be a
weak Hopf algebra, see Corollary 16.8.
A main application of the abstract unitarizability results of Sect. 15 is the first solution
to the problem posed by Galindo on uniqueness of the unitary structure, Theorem 2.2 in
Section 17.
We analyse different natural integral weak dimension functions in Sect.18. We apply
Tannakian results to the unitary quantum group fusion categories in Sect. 20. These results
are formulated fixing the choice of an integral weak (i.e. submultiplicative) dimension
functions.
The second main application of the unitarizability criterion 15.8, is Theorem 21.2, giving
the unitarization of the Beilinson-Feigin-Mazur category O˜
ℓ
for all the cases where it is
known that Finkelberg’s equivalence with C(g, q, ℓ) holds [55], [56]. This theorem relies on
Wenzl’unitarity result of C(g, q, ℓ) in [185].
The proof of the unitarizability of O˜
ℓ
, Theorem 21.2, depends on the Finkelberg equivalence, and this was our original motivation to look for a direct proof. We do this in the
rest of the paper.
We discuss our unitarization results of module categories Rep(Vgk) of affine vertex operator algebras at positive integer levels k as a first result on the subject, see Sect. 23.
The preceding Sect. 22 is dedicated to preliminaries on vertex operator algebras and their
modules. This result depends on our main result Theorem 2.11.
Section 24 deals with weak quasi-Hopf algebras obtained via Tannakian duality and
conformal nets, along the same lines.
In the rest of the work we develop direct, canonical constructions of weak quasi-Hopf
algebras naturally associated to the inner fusion structure of the categories via their coproduct.
To approach our study of a direct proof of KLF equivalence theorem, we first study the
type A case, from a classification perspective thanks to Kazhdan-Wenzl theory [110].
We do this in Sect. 25 that can be read independently of the rest of the paper, and the
result is both interesting in its own and quite enlightening for the rest of the paper because
Kazhdan-Wenzl methods are abstract, and thus may be applied to concrete examples
beyond quantum groups, including the case of vertex operator algebras. The main result
is stated as Theorem 2.6 that gives a classification of these fusion categories in terms of
the representation ring and the ribbon structure.
Thanks to the braided symmetry, the emerging categories from the classification can
only correspond to to C(slN , q, ℓ). In particular, the proof shows how any associativity
morphism when realized over C(slN , q, ℓ) becomes trivial thanks to the constraint given

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 21
by the braided symmetry. This result extends a remarkable result by Neshveyev and
Yamashita in the setting of compact quantum groups, Prop. 4.4 in [140]. In our case, we
apply their arguments to the weak Hopf algebras AW (slN , q, ℓ) of [25]. The result highlights
how the presence of the braided symmetry determines the associator and trivializes it for
the quantum group fusion category, setting up the framework for the arbitrary Lie types
handled at the very end of the paper with a mixture of direct comparison, cohomological
reduction, and quantum Schur-Weyl duality.
Our study for the general Lie types beyond type A is starts from Sects. 19 and occupies
the rest of the paper (with the exception of Sect. 25 as said).
To make our approach to unitarization of module categories of affine vertex operator
algebras useful, we first need to understand KLF equivalence in the setting of HuangLepowsky tensor product structure. Our main result is Theorem 2.11 and its proof is a
main aim of this paper.
Sects. 27, 28, 29, 30 develop central categorical and algebraic notions of unitary coboundary weak quasi-Hopf algebras and their compatible and hermitian counterparts. While hermiticity is a weakening of unitarity to the case where the ∗
-involution is not a C
∗
-algebra
involution, and is useful to include Uq(g) as the main example, the mentioned compatibility property is a strengthening to the notion of hermitian/unitary coboundary weak
quasi-Hopf algebra, to the case where, just like Uq(g), the coproduct anticocommutes with
the ∗-involution. The weaker case admits a nice Tannakian characterization established
in Sect. 29 extending to the coboundary symmetry the symmetry property of functors
between symmetric tensor categories, a property envisaged for a long time in our previous
work.
Sect. 32 is devoted to the construction of canonical unitary compatible coboundary
weak Hopf C
∗
-algebras AW (g, q, ℓ) for all the Lie types associated to C(g, q, ℓ), which, as
∗
-algebras, are semisimple quotients of Uq(g), by an ideal which is not a coideal. Their
coproduct naturally arises from the fusion tensor product of C(g, q, ℓ). We study their
naturally arising Ω-involution associated to their coboundary matrices R, extending those
considered in [25], [26] for the type A case with different methods.
Similarly to the type A case, the equivalence between C(g, q, ℓ) and the corresponding
Rep(Vgk) relies on these algebras AW (g, q, ℓ), but in these cases we adopt a direct comparison. Similarly to the type A case, the interplay between the braiding and the associativity
morphisms are relevant. But differently from the type A case, we develop an abstract cohomological reduction for the pentagon and hexagon equations of a braided tensor category
with. a generating object, reminding the classification of braided pointed fusion categories
[50]. We shall be able to explain structural properties of our unitarization of Rep(Vgk) and
its deep symmetry with the quantum group fusion category by the end of the paper.
In Sect. 33 we use these canonical unitary coboundary weak Hopf C
∗
-algebras AW (g, q, ℓ)
to transport, via the construction of a Drinfeld twist of AW (g, q, ℓ), the unitary structure
to Rep(Vgk). To describe this unitary structure, we pass through the Zhu algebra A(Vgk),
which becomes a unitary coboundary weak quasi-Hopf algebra with 3-coboundary associator, by our analytic analogue of the Drinfeld-Kohno theorem 30.4. Up to this point we
have constructed, via transport from the Zhu algebra and Zhu’s linear equivalence and

22 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
its inverse [197], the structure of a rigid unitary modular category on Rep(Vgk
) for all
the Lie types and positive integer levels, with fusion multiplicities transported from the
quantum group fusion category via AW (g, q, ℓ) and the Drinfeld twist. These constitutes
parts (a), (b) of Theorem 2.8. We are left to compare our ribbon braided structure with
Huang-Lepowsly structure.
Thus we pass to introduce Huang-Lepowsky tensor structure in generality, following
historical presentation starting from the setting of affine Lie algebras, where one can see the
first connections between primary fields with the Verlinde fusion structure of corresponding
quantum groups at roots of unity. This is the content of Sects. 34–38 which also contains
the proof of parts (a), (b) Theorem 2.11.
Historically, the comparison between the fusion tensor product of quantum groups and
of affine Lie algebras has roots primary fields, see e.g. [150], or Appendix A in [149]. This
connection emerges in the works by Tsuchiya and Kanie, Kohno, Wassermann and relation
with the work of Wenzl [170], [116], [185], [181].
The notion of primary field and its relation to quanto groups plays a central role in
our proof. Sect. 34 introduces these fundamental notion of primary field in the setting of
loop groups or affine Lie algebras. It gives a central Theorem 34.7 based on the work by
Fenkel and Zhu [61] and our construction of weak quasi-Hopf algebra on the Zhu algebra.
This is the first connection between our truncated tensor product bifunctor ⊠ and what
will later correspond to Huang-Lepowsky bifunctor ⊠HL, via a known connection between
intertwining operators in the setting of vertex operator algebras and primary fields. This
section also contains Corollary 35.1 that is a reduction of the final result to the associator,
using work by Toledano-Laredo [169].
The methods that we have used so far (mainly our version of Drinfeld-Kohno theorem
30.4) to prove parts (a) and (b) of Theorem 2.8 and a direct comparison to prove parts
(a), (b) Theorem 2.11, show coincidence of the two tensor product bifunctors, of the ribbon structure, and the braiding for certain special pairs of variables where one of them
is the fundamental representation V . We also know that special associativity morphisms
coincide when two out of the three variables are the fundamental representation, by direct
verification. We call these special associativity morphisms of CFT type, and we develop an
abstract cohomology theory in Sect. 8 to determine the remaining braiding and associativity morphisms uniquely using the pentagon and hexagon equations. The main results
are Theorems 8.13 and 8.21, whose proofs are deferred to [149].
This general comological reduction applies to the case where the category has a generating object in a given linear category with a tensor product bifunctor, with braiding
morphisms that generate the centralizer algebras of tensor powers of the generating object.
This applies to the quantum group fusion categories for the classical Lie types ABCD and
G2, by results known in the literature on generalization of Schur-Weyl duality, see [24] for
the classical vector representation, and due to Wenzl and his collaborators for the considered fundamental representations. This application is discussed in Sect. 11 in [149] as
well.
In summary, our approach systematically bridges quantum groups with the analytical
realities of conformal field theory. By substituting strict coassociativity with our weak

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 23
quasi-Hopf framework, we bypass the historical reliance on the analytic monodromy of the
Knizhnik–Zamolodchikov equations, passage to negative shifted levels, use of the Verlinde
formula to establish rigidity, use of rigidity to establish braided tensor equivalence. We
also expand our results to all positive integer levels and to all Lie types for our UMFC
structure on RepT(Vgk
) and to the classical Lie types and G2 for the Huang-Lepowsky
structure. This also allows us to uniformly establish the uniqueness of unitary structures
across tensor categories (Theorem 2.2) and settle the long-standing unitarization problem
for the Beilinson–Feigin–Mazur category (Theorem 21.2), together with the other problems
mentioned in Subsect. 1.3 for the WZW model. When classification is unavailable from
the outset, we utilize the weaker condition of pseudounitarity alongside Kazhdan–Wenzl
theory to fully classify Type A ribbon fusion categories and complete the operator-algebraic
proof of the Kazhdan–Lusztig–Finkelberg equivalence.
Perspectives for future research have been discussed in [150]. Among them, the extension
of the theory of quantum homogeneous spaces [146] and induced representations [147] of
Woronowicz compact quantum groups [189, 190, 192] to unitary coboundary weak Hopf
C
∗
-algebras, to study extensions of the WZW model in the setting of vertex operator
algebras and conformal nets.
