---
doc_id: arxiv-2607.10525v1
doc_title: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES"
section_id: sec-008-5-fiber-functors-on-gaugings
section_title: "Fiber functors on gaugings"
section_number: 5
pages: 18-21
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
doc_brief: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES — LetGbe a finite group acting on a finite tensor categoryC."
---
We now apply the classification to gaugings. LetBbe a braided fusion category
and let
E=
M
g∈G
Eg
be a faithfulG-crossed braided fusion category with neutral componentEe =B. We
denote byρthe crossed action ofGonE. Following the formulation of gauging
in [CGPW16], based on the extension theory of [ENO10], the gauging determined by
theG-crossed extensionEis the equivariantization
EG.
The crossed braiding makesEG a braided fusion category, but the fiber-functor prob-
lem below uses only the underlying tensor categoryEtogether with the actionρ.
Definition 5.1.For a subgroupS⊆G, setE S =L
s∈SEs. AClifford datumforE
is a triple(S,N, eN), whereNis an indecomposable semisimpleB-module category
and eNis an indecomposable semisimpleE S-module category on the same underlying
finite semisimple category, whose restriction toBis equivalent to the givenB-module
structure onN. We call eNanE S-extension ofN.
Given a Clifford datum(S,N, eN), put
Ind(S, eN) := IndE
ES(eN)≃E⊠ ES
eN.
The result is an indecomposableE-module category. Conversely, by Clifford theory
for graded fusion categories, every indecomposableE-module category is of this form.
Letd= (S,N, eN)be a Clifford datum and leth∈G. We define itsh-twist by
dh = (h−1Sh,N h, eN h),
where eN h is the same underlying category aseN, regarded as anEh−1Sh-module cat-
egory by
X⊗hN:=ρ h(X)⊗N, X∈E h−1Sh, N∈ eN,
andN h is its restriction toB=E e. Then
Ind(S, eN)h≃Ind(h−1Sh, eN h)
asE-module categories.
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 19
Definition 5.2.Letd= (S,N, eN)be a Clifford datum. AnH-equivariant Clifford
liftofdis a choice, for everyh∈H, of an equivalence of inducedE-module categories
Φh : Ind(S, eN)
∼
− →Ind(h−1Sh, eN h),
together with coherence isomorphisms making the corresponding functors
Ind(S, eN)−→Ind(S, eN)h
anH-equivariant structure in the sense of Section 2.
Remark5.3.For each fixedh∈H, the equivalence criterion for induced module cat-
egories over graded fusion categories [MCnM20, Definition 5.10 and Proposition 5.12]
tests the existence ofΦh by asking for an elementah∈Gsuch that
S=a h(h−1Sh)a−1
h
and, writing
Eah(h−1Sh) :=
M
u∈ah(h−1Sh)
Eu
for the corresponding(E S,Eh−1Sh)-bimodule category, an equivalence ofES-module
categories
Eah(h−1Sh) ⊠Eh−1Sh
eN h≃ eN.
It remains to require these equivalences, ashvaries, to satisfy the equivariant coher-
ence.
Theorem 5.4.LetE= L
g∈GEg be a faithfulG-crossed braided fusion category with
neutral componentB=E e. Fiber functors onEG correspond to equivalence classes of
tuples
(H,S,N, eN,u)
satisfying:
(1)HandSare subgroups ofG;
(2)(S,N, eN)is a Clifford datum forE;
(3)uis anH-equivariant Clifford lift of(S,N, eN);
(4)forM= Ind(S, eN), the induced action ofHonIrr(M)is transitive;
(5)for some, hence every, simple objectX∈M, the stabilizer cocycle
[αX]∈H 2(StH(X),k×)
is nondegenerate.
Two tuples are identified when their associated equivariantE-module categories are
conjugate in the sense of Definition2.3.
Proof.Apply Theorem 3.6 to the crossed actionρ:G→Aut ⊗(E). By Clifford the-
ory for graded fusion categories [Gal12, MCnM20], every indecomposableE-module
category has the form
M≃Ind E
ES(eN)≃E⊠ ES
eN
20 C. GALINDO, C. GALLEGO, AND Y. MORALES
for a Clifford datum(S,N,eN). Transporting theH-equivariant structure onMgives
u.
Conversely, such a tuple produces anH-equivariant indecomposable exact semisim-
pleE-module category. Items (4)–(5) and Theorem 3.6 give a fiber functor. The
equivalence relation is exactly the conjugacy relation of Theorem 2.4.□
Corollary 5.5.LetG=C p =⟨τ⟩be cyclic of prime order, and letE= L
g∈GEg be
a faithfulG-crossed braided fusion category with neutral componentB. Then the data
of Theorem 5.4 reduce to the following possibilities.
(1)H={e},S=G, and eNis a rank-oneE-module category. These fiber functors
are theG-orbits of fiber functors onEunder the crossed action.
(2)H=G, andM= Ind(S, eN)carries aG-equivariant Clifford lift whose gen-
erator acts onIrr(M)as a singlep-cycle. This has two subcases:
(a)S={e}, eN=N, and
M=E⊠ BN=
M
g∈G
Mg,M g :=E g ⊠BN,
where everyM g has rank one and the generator ofGacts on theirp
simple objects as a singlep-cycle.
(b)S=G, and eNis anE-module category withpsimple objects, equipped
with aG-equivariant structure whose generator acts as ap-cycle.
Proof.The only subgroups ofCp are{e}andG, andH 2(L,k×) = 0for both. Hence
Corollary 3.7 applies: the stabilizer condition in Theorem 5.4 is equivalent to freeness
of theH-action onIrr(M).
IfH={e}, freeness and transitivity mean thatMhas one simple object. If
S={e}, the restriction ofInd(S, eN)toBhas one nonzero component for each
element ofG; hence its rank is at leastp. Thus rank one forcesS=G.
IfH=G, a free transitive action of the cyclic group of orderpis exactly a single
p-cycle. The two alternatives forSare the only possible ones. ForS={e}, Clifford
theory gives a decomposition
M=
M
g∈G
Mg,M g =E g ⊠BN,
into non-zero indecomposableB-module subcategories; see [Gal12, Proposition 4.1].
Consequently,
# Irr(M) =
X
g∈G
# Irr(Mg)≥p,
and equality holds ifand only ifeveryMg has rankone. In particular, equality implies
thatN=M e has rank one. This argument does not require an invertibleB-bimodule
category to preserve rank. The caseS=Gis immediate fromM= eN.□
Remark5.6.Two layers of data are not visible from the neutral-component module
category alone. First,Nmust extend fromBtoE S. In the obstruction theory
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 21
of [MM12], ifN≃Mod B(A), this requiresS-stability and a splitting of
1−→Aut B(N)−→Λ−→S−→1,
whereΛconsists of invertibleA-A-bimodules supported inE S. After a splitting is
chosen, anobstructioninH 3(S,k×)governsassociativemultiplicationontheresulting
graded algebra eA= L
s∈SAs. Second, the inducedE-module category must be
equivalent to itsh-twists forh∈H, with compatible coherence. Thus the practical
inputs are theB-module category, itsES-extension, and the equivariant lift; the rank-
one test is then supplied by Theorem 5.4.
