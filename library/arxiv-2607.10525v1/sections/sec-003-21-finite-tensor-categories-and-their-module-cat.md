---
doc_id: arxiv-2607.10525v1
doc_title: "Fiber Functors of Equivariantizations of Finite Tensor Categories"
section_id: sec-003-21-finite-tensor-categories-and-their-module-cat
section_title: "Finite tensor categories and their module categories"
section_number: 2.1
pages: 4-7
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
toc_source: outline
doc_brief: "Fiber Functors of Equivariantizations of Finite Tensor Categories — Let G be a finite group acting on a finite tensor category C."
---
egory is a finite abelian category equipped with a rigid monoidal structure, bilinear
tensor product, and simple unit [EO04, Section 2.2]; a fusion category is a semisimple
finite tensor category.
A left C-module category is a finite abelian category M with an exact bilinear
action ⊗: C × M →M and the usual associativity and unit constraints. It is exact
if P⊗M is projective whenever P is projective in C, and indecomposable if it is not a
direct sum of two nonzero module categories. A C-module functor F : M →N is an
exact functor equipped with coherent natural isomorphisms
F(X⊗M)
∼−→X⊗F(M).
We write FunC(M, N) for the category of module functors and module natural trans-
formations.
Remark 2.1. If M is indecomposable and exact, then
C∗
M := FunC(M, M)
is a finite tensor category [EO04, Theorem 3.27]. We use reverse composition, F ⊗
G := G ◦F, so that evaluation gives the right action M ◁F = F(M) and the double-
dual equivalence (C∗
M)∗
M ≃C. In this situation C and C∗
M are Morita equivalent.
2.2. Equivariant tensor categories and their module categories.
FIBER FUNCTORS OF EQUIVARIANTIZATIONS
5
2.2.1. Group actions on tensor categories. Let G be the strict monoidal category
associated with a group G. An action of G on a tensor category C is a monoidal
functor
G −→Aut⊗(C).
By the coherence theorem for tensor categories with G-action [Gal17, Theorem 2.4],
we may and do assume that the G-action is strict. We write g∗for the tensor au-
toequivalence attached to g, so that g∗h∗= (gh)∗and e∗= idC. Equivariant module
categories will not be strictified; their coherence maps are retained below.
2.2.2. The semidirect product. For a tensor category C with a strict G-action, the
semidirect product C ⋊G is the monoidal category
C ⋊G =
M
g∈G
Cg,
where each homogeneous component Cg is a copy of C [Tam01, Nik08]. We write
[X, g] for the object X ∈C placed in degree g. The tensor product and unit are
(1)
[X, g] ⊗[Y, h] = [X ⊗g∗(Y ), gh],
1C⋊G = [1, e],
with associativity and unit constraints induced from those of C. When G is finite,
C ⋊G is a finite tensor category. For an arbitrary subset S ⊆G, we use the notation
(C ⋊G)S :=
M
s∈S
Cs.
If S is a subgroup, this is the tensor subcategory C ⋊S. If S = gK is a left coset, then
(C⋊G)gK is naturally a ((C⋊G)gKg−1, C⋊K)-bimodule category under tensor product.
This notation will also be used for arbitrary faithfully graded tensor categories.
2.2.3. H-equivariant module categories. We follow [Gal11, ENO11] for equivariant
module categories and their use in constructing module categories over equivarianti-
zations.
Let H ⊆G be a subgroup acting on a finite tensor category C. Given a C-module
category M, we twist the module structure by any element g ∈H.
For each g ∈H, let Mg be the category with the same underlying abelian category
as M and with C-action
X⊗gM := g∗(X)⊗M.
The associativity and unit constraints are those induced from the module structure
of M and the tensor structure of g∗. Since the action on C is strict, (Mg)h = Mgh
as C-module categories.
We now make explicit the monoidal category that records twisted module autoe-
quivalences. Let AutH
C (M) be the groupoid whose objects are pairs (g, F), where
g ∈H and
(F, cF) : M −→Mg
6
C. GALINDO, C. GALLEGO, AND Y. MORALES
is a C-module equivalence.
There are no morphisms between objects of different
degrees, and morphisms in degree g are C-module natural isomorphisms. If (g, F)
and (h, E) are objects, define
(g, F) ⊗(h, E) := (gh, F ◦E),
where the C-module constraint on the composite is
(2)
cF◦E
X,M : F(E(X⊗M))
F(cE
X,M)
−−−−−−→F(h∗(X)⊗E(M))
cF
h∗(X),E(M)
−−−−−−−−→(gh)∗(X)⊗F(E(M)).
With the usual horizontal product of module natural isomorphisms, composition
makes this a strict monoidal groupoid with unit (e, idM). The degree map
π1 : AutH
C (M) −→H,
(g, F) 7−→g,
is a strict monoidal functor.
An H-equivariant C-module category is a C-module category M together with a
strong monoidal section
ρ : H −→AutH
C (M),
π1 ◦ρ = idH .
We work with normalized sections. Explicitly, the data consist of C-module equiva-
lences
(Uh, ch) : M −→Mh,
h ∈H,
and module natural isomorphisms
µg,h : UgUh
∼−→Ugh
such that
(3)
(µgh,k)M ◦(µg,h)Uk(M) = (µg,hk)M ◦Ug((µh,k)M)
for all g, h, k ∈H and M ∈M, and such that each µg,h is a module natural transfor-
mation, equivalently
(4)
(id(gh)∗(X) ⊗(µg,h)M) ◦cg
h∗(X),Uh(M) ◦Ug(ch
X,M)
= cgh
X,M ◦(µg,h)X⊗M
for all X ∈C and M ∈M. Normalization means
(5)
Ue = idM,
ce = id,
µe,h = µh,e = idUh .
Every strong monoidal section is monoidally isomorphic to a normalized one, so this
convention does not change the equivalence classes under consideration.
Under these conventions, normalized H-equivariant C-module structures on M
are equivalent to (C ⋊H)-module structures extending the original C-action. The
correspondence is given explicitly by
(6)
[X, h]⊗M := X⊗Uh(M).
The associativity constraint for this action is built from ch and µg,h; conversely, the
action of [1, h] recovers Uh, and the module associativity recovers ch and µg,h.
FIBER FUNCTORS OF EQUIVARIANTIZATIONS
7
An H-equivariant C-module category will be called indecomposable when its un-
derlying C-module category is indecomposable.
