---
doc_id: arxiv-2607.10525v1
doc_title: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
doc_brief: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES — LetGbe a finite group acting on a finite tensor categoryC."
---
LetCbe a finite tensor category over an algebraically closed fieldkof characteristic
zero. Afiber functoronCis ak-linear exact faithful tensor functorF:C→Vec k.
Classical neutral Tannakian duality reconstructs affine group schemes from symmetric
tensor categories equipped with a fiber functor [SR72, DM82]. In the non-symmetric
setting relevant here, Tannaka–Krein reconstruction instead produces a Hopf alge-
bra [JS91, Sch92, BV07]: for every fiber functorFon a finite tensor categoryC, there
is a finite-dimensional Hopf algebraAF withC≃Rep(A F ), under whichFbecomes
the forgetful functor [EGNO15, Theorem 5.3.12]. The fiber-functor problem is thus
the problem ofHopf realization: deciding when a finite tensor category is the repre-
sentation category of a finite-dimensional Hopf algebra, and counting the realizations
arising from inequivalent forgetful functors.
For group-theoretical fusion categories this problem has a concrete answer in terms
of finite groups and cohomology. Recall that a fusion category is calledgroup-
theoreticalif it is categorically Morita equivalent toVec ω
G, the category of finite-
dimensionalG-graded vector spaces with associativity constraint defined by a3-
cocycleω∈Z 3(G,k×). In this case fiber functors are described by subgroup and
2020Mathematics Subject Classification.18M05, 18M20, 16T05.
Key words and phrases.finite tensor category, equivariantization, fiber functor, module category,
gauging.
1
arXiv:2607.10525v1  [math.QA]  12 Jul 2026
2 C. GALINDO, C. GALLEGO, AND Y. MORALES
cochain data [Ost03, Nik08]. Equivariantizations give a different source of exam-
ples. If a finite groupGacts on a tensor categoryC, thenC G is the category of
objects ofCequipped with compatibleG-equivariant structures, and is again a finite
tensor category. Equivariantizations of Tambara–Yamagami categories, the fusion
categories with simple objectsA∪{m}and fusion rulem⊗m= L
a∈Aa, give
non-group-theoretical semisimple Hopf algebras [Nik08, TY98], answering [ENO05,
Question 8.45]. Thus non-group-theoretical fusion categories may still admit fiber
functors; consequently, the group-theoretical classification does not cover the gen-
eral fiber-functor problem. Our first result classifies fiber functors on an arbitrary
equivariantization.
Theorem 1.1.LetGbe a finite group acting on a finite tensor categoryC. Fiber
functors onCG are classified by conjugacy classes of pairs(H,M), whereH⊆Gis a
subgroup andMis anH-equivariantC-module category whose underlyingC-module
category is indecomposable, exact, and semisimple, satisfying:
(1)Hacts transitively onIrr(M);
(2)for some, and hence every, simple objectX∈M, the stabilizer cocycle
[αX]∈H 2(StH(X),k×)
is non-degenerate.
This is Theorem 3.6; the relevant notion of conjugacy is Definition 2.3. In this
form, the theorem turns the fiber-functor problem forCG into a rank-one condition
for equivariant module categories; via Tannaka–Krein reconstruction it also covers
Hopf realizations outside the semisimple setting. Structurally, the simple objects of
MH are obtained fromH-orbits inIrr(M)together with projective representations of
stabilizers. HenceM H has rank one exactly when theH-action is transitive and the
twisted group algebrakαX[StH(X)]of a stabilizer is simple. When the relevant second
cohomology groups vanish, for instance whenever every subgroup ofGis cyclic, the
description reduces to freeness and transitivity of theH-action onIrr(M).
The proof combines three known facts. Fiber functors correspond to rank-one exact
module categories [EGNO15, Proposition 7.3.3 and Example 7.4.6]. Exact module
categories over equivariantizations come from equivariant module categories over the
original category [GM12]. Finally, simple objects in equivariant semisimple categories
are governed by projective representations of stabilizers. Combining these facts gives
Theorem 1.1.
Here and throughout,Cn denotes the cyclic group of ordern.
OurfirstapplicationconcernsafamilyofsemisimpleHopfalgebrasduetoNikshych.
Theorem 1.2.Letpbe an odd prime, and letH p be Nikshych’s semisimple Hopf
algebra of dimension4p2 constructed in[Nik08]. ThenRep(H p)has one equivalence
class of fiber functors ifp≡3 (mod 4), and two equivalence classes of fiber functors
ifp≡1 (mod 4).
This is Theorem 4.4. In Nikshych’s construction,Hp is reconstructed from theC2-
equivariantization of the Tambara–Yamagami categoryTY(Cp×C p,χp,p−1), where
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 3
χp is the standard hyperbolic form andC2 acts by interchanging the two factors. This
Tambara–Yamagami category has exactly two fiber functors, corresponding to the or-
dered decompositionsCp×Cp =L 1×L 2 andC p×Cp =L 2×L 1, whereL1 =C p×{0}
andL 2 ={0}×C p. The involution used in the construction ofHp interchanges them;
hence they give one equivalence class on the equivariantization. The remaining possi-
bility left by Theorem 1.1, namely a fiber functor coming fromH=C2, is controlled
by the rank-two module categories over this Tambara–Yamagami category described
in [Nik08]: it is impossible forp≡3 (mod 4), and contributes one additional class
forp≡1 (mod 4).
Our second application concerns gaugings. A gauging of a braided fusion cat-
egoryBis an equivariantizationE G, whereE= L
g∈GEg is a faithfulG-crossed
braided fusion category with neutral componentEe =B[CGPW16, ENO10]. Com-
bining Theorem 1.1 with Clifford theory for module categories over graded fusion
categories [Gal12, MCnM20], we reduce the module-category input fromEto module
categories over the neutral componentB, together with extension and equivariant-lift
data; this is Theorem 5.4. For prime cyclic gaugings the description is especially
explicit: ifG=C p, the relevant second cohomology groups vanish, and Corollary 5.5
says that a fiber functor either comes from a rank-one module category overE, or
from aC p-equivariantE-module category withpsimple objects. In the latter case,
the module category is either induced from aB-module categoryNfor which every
componentE g ⊠BNhas rank one, or is already anE-module category of rankp; in
both subcases the generator acts on simple objects as a singlep-cycle.
We apply this to the small radical gaugings classified in [GN25]. There the Tan-
nakian radical is the subcategoryRep(G)being gauged, and the mantle is the braided
fusion categoryBappearing as the neutral component. The non-pointed, non-
degenerate entries are canonical gaugings of their mantles by their radicals. We
reproduce the relevant table as Table 1, whereC(A,q)denotes the pointed mod-
ular category attached to ametric group(A,q), that is, a finite abelian groupA
with a non-degenerate quadratic formq, and add the fiber-functor conclusion. Since
a non-degenerate braiding onRep(H)corresponds to a factorizable quasitriangular
structure on the semisimple Hopf algebraH, deciding which entries admit a fiber
functor is the same as deciding which are realized by finite-dimensional semisimple
factorizable Hopf algebras.
Corollary 1.3.Apart from pointed categories, the entries from the small-dimensional
list in[GN25]considered in Table 1 that admit realizations as representation categories
of finite-dimensional semisimple factorizable Hopf algebras are exactly:
(1)the ordinary dihedral doublesRep(D(Dr));
(2)the hyperbolic prime-cyclic twisted-double rowsRep(D ω(Cr ⋊C p)), withp|
r−1, for every cohomology class[ω]∈H 3(Cr ⋊Cp,k×).
All remaining non-pointed entries in that table have no such realization.
This is Corollary 5.18. Its proof draws on several distinct obstructions. The rows
containing Ising categories, metaplectic categories, and centers of elliptic Tambara–
Yamagami categories are excluded by integrality. For the dihedral twisted doubles,
4 C. GALINDO, C. GALLEGO, AND Y. MORALES
the group-theoretical description of fiber functors, Goursat’s lemma, and the explicit
cocycle representatives of [CGR00] show that only the trivial cohomology class sur-
vives. The odd elliptic prime-cyclic rows are excluded using the prime-cyclic gauging
description, the non-group-theoreticality theorem of [GPR24], and the Hopf-algebra
obstruction of [JL09]. The dimension36row requires instead a separate invariant-
Lagrangian computation for theF4 extension, together with the same Hopf-algebra
obstruction.
The paper is organized as follows. Section 2 fixes conventions on finite tensor
categories, equivariantizations, and equivariant module categories, and records the
conjugacy theorem for equivariantized module categories, Theorem 2.4. Section 3
proves the main classification, Theorem 3.6. Section 4 proves Theorem 4.4. Section 5
establishes the Clifford-theoretic description of fiber functors on gaugings and applies
it to the table of [GN25].
