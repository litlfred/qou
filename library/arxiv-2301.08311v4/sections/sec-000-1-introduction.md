---
doc_id: arxiv-2301.08311v4
doc_title: "FLOER COHOMOLOGY AND HIGHER MUTATIONS SOHAM CHANDA"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 2301.08311v4.pdf
source_sha256: 385139c69e18f5b0
doc_brief: "FLOER COHOMOLOGY AND HIGHER MUTATIONS — We extend the construction of higher mutation as introduced in [PT20] to local higher mutation, which is applicable to a larger class of monotone Lagrangians."
---
2. Local Mutation 7
3. SFT Compactness 14
4. Constructing Moduli Space of Broken Maps 30
5. Regularity 44
6. Classifying Rigid Broken Maps 54
7. Floer Cohomology and Mutations 65
References 72
1. Introduction
A natural question about Lagrangian submanifolds is how their invariants change if one locally
modifies a Lagrangian. We describe a local modification for Lagrangians that contain a torus
segment and study the behavior of Lagrangian Floer cohomology under the change. We call this
modification a local higher mutation . Intuitively, a local higher mutation is a surgery operation,
it removes a torus segment from a Lagrangian and replaces with an opposite torus segment. This
modification of a Lagrangian is a local change inspired by Pascaleff-Tonkonog’s higher mutation in
[PT20].
Mutations come up naturally in the context of almost toric fibrations of symplectic 4-manifolds.
One obtains a mutation of a smooth toric fiber in an almost toric fibration by varying the location
of the singular fiber so that it crosses the smooth fiber, see [LS10]. Auroux [Aur07] describes a
relation between the disc potentials of two families of Hamiltonian non-isotopic Lagrangian tori that
are mutations of each other. Seidel [Sei13] shows that the Floer homology of a pair of mutated tori
in dimension two is non-zero only when the local system over the tori satisfies a certain algebraic
relation. The algebraic relations that occur between the potentials also occur in the theory of cluster
algebras as algebraic mutations. Pascaleff-Tonkonog [PT20] generalizes the mutation construction
to higher dimensional tori and establishes a wall-crossing formula for their disc-potential.
Key words and phrases. Floer Cohomology, Disc Potential, Neck-Stretching, Higher Mutation.
1
arXiv:2301.08311v4  [math.SG]  17 Sep 2024
FLOER COHOMOLOGY AND HIGHER MUTATIONS 2
Mutations of two-dimensional Lagrangians can be viewed from the perspective of surgery. La-
grangian surgery, introduced by Polterovich in [Pol91], is a version of classical surgery technique.
Mutation of two-dimensional Lagrangians arise from different resolutions of a singular Lagrangian
with transverse double intersection by Lagrangian surgery. Fukaya-Oh-Ohta-Ono [FOOO07] studies
the effect of Lagrangian surgery on the moduli space of discs with boundaries on the Lagrangian.
Woodward-Palmer [PW19] proves the invariance of the disc potential and Floer homology under
Lagrangian surgery.
1.1. Main result. The main result in this chapter is an invariance of Floer cohomology, up to a
change in local system. In spirit, this result is similar to the invariance result in [PW19] which
proves a similar result for Lagrangian surgery.
We begin with a quick recap of Lagrangian intersection Floer cohomology with local systems.
For a more detailed discussion, see Section 7. Let L′,K′ be two transversely intersecting, orientable,
spin, compact Lagrangians in a compact monotone symplectic manifold M′. Assume that (L′,K′)
forms a monotone tuple. Let EL′,EK′ be flat complex line bundles over L′,K′ with holonomies
ρL′,ρK′. Define the chain complex CF ((L′,ρL′), (K′,ρK′)) as follows,
CF ((L′,ρL′), (K′,ρK′)) =
M
p∈L′∩K′
hom(EL′|p,EK′|p),
whereEK′|p,EL′|p refers to the fibers of the line bundles over the point p. The differential ∂ on
CF ((L′,ρL′), (K′,ρK′)) is defined by counting rigid holomorphic strips weighted by the holonomies.
Oh [Oh95a] shows that if all Maslov two discs are simple and the disc potentials WL′ and WK′
match, then ∂2 = 0. Later, from structural results of images of pseudoholomorphic discs proved in
[KO00], [Laz11a], it was established that all Maslov two discs with boundary on orientable monotone
Lagrangians are simple. The cohomology of the complex CF ((L′,ρL′), (K′,ρK′) is denoted as
HF ((L′,ρL′), (K′,ρK′)), which we call the Lagrangian Floer cohomology.
Now we get back to stating the main result. We describe relevant notations and assumptions in
the following list.
[C1] M is a compact, monotone, symplectic manifold of dimension 2 n.
[C2] L is a locally mutable, oriented, spin, compact, connected, monotone Lagrangian manifold in
M. See Definition 2.3 for the definition of locally mutable.
[C3] K is an oriented, spin, compact, connected, monotone Lagrangian manifold in M.
[C4] The Lagrangian K intersectsL transversely but does not intersect a small mutation neighbor-
hood B of L. See Definition 2.6 for the definition of mutation neighborhood.
[C5] (L,K ) forms a monotone tuple. See Definition 2.22 for the definition of monotone tuple of
Lagrangians.
[C6] ρL and ρK are local systems on L and K respectively.
[C7] In a mutation neighborhood B, under the identification given by the symplectomorphism ϕ, L
is equal to the torus segment Tγ. See Definitions 2.1 for the definition of torus segment.
[C8] x1,...x n−1 is the image of generators of H1(Tγ) under the inclusion map i :Tγ ,→L. From
Definition 2.3, we know that the induced map i∗ :H1(Tγ)→H1(L) is injective.
[C9] (x1,x 2,...,x n,y 1,...y l) is a generating set of H1(L) such that xn∩i∗[Tγ] where [Tγ] is the
generator of Hn−1(Tγ). A Poincar´ e duality argument ensures the existence of such anxn.
Denote the evaluation of the holonomy ρL on H1(L) as follows,
ρL(xi) =zi(1.1.1)
ρL(yi) =wi
FLOER COHOMOLOGY AND HIGHER MUTATIONS 3
Definition 1.1. The mutated local system ρLµ on the mutated Lagrangian Lµ for the pair (L,ρL)
is given by
ρLµ(xi) =zi for i<n(1.1.2)
ρLµ(xn) =zn(1 +z1 +··· +zn−1)
ρLµ(yi) =wi.
To obtain regularity of certain moduli spaces, we use domain-dependent perturbations. This
paradigm of transversality was introduced in [CM07] for closed curves and extended to discs with
boundary on Lagrangians in [CW17], [CW15]. One key step in this model is to stabilize domains by
adding mark points coming from intersections with a Donaldson divisor. We assume the existence
of such a divisor, which we call nice divisor, see Definition 4.12, which helps us in the regularization
of broken maps. One can prove that such divisors do exist by modifying Auroux’s argument in
Theorem 3.3 of [PT20] if the symplectic form is rational and the Lagrangian L satisfies certain
geometric conditions. We now state the main result of the chapter.
Theorem 1.2 (Invariance under mutation) . Let M,L,K be manifolds as described in C[1-9].
Assume that there is a nice divisor D in M. Let Lµ be a local higher mutation of L. Let ρL, ρK be
choices of local systems on L,K such that ρL is given as in equation (1.1.1). Let ρLµ be the mutated
local system as in equation (1.1.2). Then, we have an isomorphism between the disc potentials of
the Lagrangians,
WL(ρL)∼=WLµ(ρLµ)
Moreover, if WL(ρL) =WK(ρK), then we have isomorphism of the vector spaces
HF ((Lµ,ρLµ), (K,ρK))∼=HF ((L,ρL), (K,ρK))
Remark 1.3. The algebraic relation between the local systems in Theorem 1.2 matches with the
mutation formulae present in the literature. When n = 2, this formula matches with the expected
change in the local system needed for invariance under Lagrangian surgery as done in [Aur07], [Sei13],
[PW19]. For higher dimensions, it agrees with the mutation formula for monotone Lagrangian torus
in [PT20], see the relation (1.2.3).
Remark 1.4. We need the existence of a divisor to stabilize the disc components in the outside
piece of a broken manifold. Usually, one would not require domain dependent perturbation of J
when the Lagrangian pair is monotone because Maslov 2 discs are simple from results in [KO00]
and [Laz11b]. To regularize holomorphic buildings, we would require a version of structural results
in [Laz11b,KO00] which works for manifolds with cylindrical ends. To avoid this technicality, we
are assuming the existence of a divisor to regularize our holomorphic buildings.
Corollary 1.5. LetLµ be a higher mutation of a monotone toric fiber L in (M,ω ) as constructed in
[PT20]. Equip the Lagrangians with local systems ρL,ρLµ which are related by the mutation formula
1.1.2 and denote the Lagrangian branes as eL,eLµ. Then we have,
HF (eLµ,eL)∼=HF (eL,eL).
In particular, by choosing ρ to be a critical point of WL, we know that HF is non-vanishing. Thus,
we have that the Clifford and Chekanov-type tori are Hamiltonian non-displaceable from each other.
1.2. Higher toric mutation. Higher-dimensional toric mutation, as described by Pascaleff-
Tonkonog [PT20], is a non-Hamiltonian transformation of the monotone Lagrangian torus fiber in
a monotone toric manifold. We describe the simplest example of such higher mutation here. Let
M0 = (Cn,ω 0), where w0 is the standard symplectic form Pn
i=1dxi∧dyi on Cn∼= R2n. Consider
the fibration given by the multiplication map
(1.2.1) πm :M0→ C, πm(z1,...z n) =z1z2...z n.
FLOER COHOMOLOGY AND HIGHER MUTATIONS 4
Given a simple closed curve γ :S1→ C∗, we can define an embedded Lagrangian torus
(1.2.2) Tγ ={(z1,z 2,...z n)∈ Cn|πm(z1,z 2,...z n)∈γ(S1),|z1| =|z2| =... |zn|}.
Tγ
π−1
m (p)
Cn
πm
C
γ
p
Figure 1. The Lagrangian torus Tγ
The Hamiltonian isotopy class of the Lagrangian Tγ depends on geometric properties of the curve
γ. For a fixed area enclosed by the curve γ, with respect to a symplectic form dλn (see Definition
2.7), there are at most two Hamiltonian isotopy classes depending on whether the curve γ encloses
0 inside it. We elaborate on constructing Hamiltonian isotopies of Tγ in Subsection 2.3. When the
curve γ encloses 0, we say that the torus is of Clifford type, and if it does not, we say that it is
of Chekanov type. The process of interchanging between Clifford and Chekanov type tori is the
simplest occurrence of mutation. See [CS10] for a slightly different construction of the Chekanov
tori. Pascaleff-Tonkonog use the local model ( M0,Tγ) to define higher toric mutations in a toric
manifold in [PT20]. We briefly discuss Pascaleff-Tonkonog’s higher toric mutation now. Assume
that X is a monotone toric manifold with Delzant polytope ∆, whose barycenter is 0. Let I be
a line joining a vertex w of ∆ with 0. The toric fibration, over a neighborhood of the line I, is
symplectomorphic ( as total spaces, not fibrations ) to the fibration πm over a neighborhood of the
unit circle γ(θ) =eiθ attached with the line segment S joining the point 0 with the point −1 such
that the monotone torus is mapped to Clifford-type Tγ. Choose a curve γ′ in a neighborhood of the
union of curves γ∪S, such that the area enclosed by the curve γ′ is the same as that of γ and the
Lagrangian torus Tγ′ is of Chekanov-type. Tγ′ is the mutation of the monotone torus with respect
to the vertex w.
We recall the definition of monotonicity. Let ( M,ω ) be a symplectic manifold. Let Iω be the
symplectic area functional and Ic be the first Chern class defined on π2(M).
FLOER COHOMOLOGY AND HIGHER MUTATIONS 5
Iω :π2(M)→ R
Iω(u) =
Z
u
ω
Ic :π2(M)→ Z
Ic(u) =c1(u)
Floer [Flo89] defines the concept of a monotone symplectic manifold. A symplectic manifold ( M,ω )
is called a monotone symplectic manifold if there exists an α> 0 such that Ic =αIω. This relation
between the symplectic area and first Chern class allowed Floer to control sphere bubbling. Oh
[Oh93] extends the concept of monotonicity to Lagrangians and constructs Lagrangian intersection
Floer cohomology. Let L be a Lagrangian in (M,ω ) and µL be the Maslov index functional for discs
with boundary on L. In addition, let Iω be the symplectic area functional on the homotopy classes
of discs with boundary on L.
Iω :π2(M,L )→ R
µL :π2(M,L )→ Z
A Lagrangian L is said to be a monotone Lagrangian if there is a λ > 0 such that there is a
area-index relation Iω =λµL. This area-index relation allows control of disc bubbling. Initially, the
construction of Lagrangian intersection Floer cohomology was based on the assumption that the
minimal Maslov numbers of the Lagrangians are at least three. An addendum, [Oh95a], extends the
construction to Lagrangians with minimal Maslov index two if the disc potential of the Lagrangians
matched. The disc potential of a Lagrangian L is the number of Maslov two discs passing through a
generic point on L.
We follow Pascaleff-Tonkonog’s exposition of disc potential with a choice of a local system. Let
ρ :H1(L)→ C∗ be a local system on L. We define the disc potential WL(ρ) by counting Maslov
two discs with boundary on L. Let Tor be the torsion subgroup of H1(L). Fix a generating set
(e1,...,e m)
of H1(L, Z)/ Tor∼= Zm. Let (x1,...,x m) be the image of (e1,...,e m) under the holonomy map ρ.
The choice,
(x1,...,x m)∈ (C∗)m,
specifies the holonomy of a flat C∗ line bundle over L uniquely. Thus we can view ( C∗)m as the
space of flat line bundles over L. The disc potential is a Laurent polynomial in x1,...,x m, which
we interpret as a function on the space of holonomies of flat line bundles over L.
WL : (C∗)m→ C
WL(x1,...,x m) =
X
u|µ(u)=2
nu.x∂u
(1) u is a J-holomorphic disc with a boundary marking.
(2) µ is the Maslov index.
(3) nu is the degree of the evaluation map at the boundary marking ev :MJ(L,u )→L.
(4) ∂u is considered as an element of Zm∼=H1(L, Z)/ Tor.
(5) xl for l = (l1,...,l m) denotes xl1
1xl2
2 ...x lm
m .
FLOER COHOMOLOGY AND HIGHER MUTATIONS 6
Now we restrict our attention to the disc potential of the Lagrangian torus Tγ in a monotone
toric manifold. The first homology H1(Tγ) is isomorphic to Zn. Choose a basis ([ e1],..., [en]) of
H1(Tγ) such that e1,...,e n−1 are cycles on a torus over a single fiber of πm and that en is a cycle
that descends to the curve γ. Pascaleff-Tonkonog [PT20, p. 62] shows that the disc-potential of Tγ′
can be obtained from that of Tγ by replacing xi in WL with the following method, see equation
(5.17) in [PT20],
xi−→xi for i<n(1.2.3)
xn−→xn(1 +x1··· +xn−1).
1.3. Motivation. Mutations in symplectic 4-manifolds have played a crucial role in symplectic
geometry. Vianna [dVV16] proves that there are infinitely many Hamiltonian isotopy classes of
monotone Lagrangians in the projective space CP2 by doing iterated mutations and comparing the
disc potentials. Mutations also have emerged to be important in mirror symmetry, see [STW16a],
[HK20], [HK21].
Strominger-Yau-Zaslow [SYZ96] conjectures that mirror Calabi-Yau manifolds carry dual torus
fibration, thus one approach to constructing mirror manifolds is to understand torus fibrations.
Higher mutations come up naturally in examples of singular special Lagrangian fibrations. See
[BM09][Gro98], [Gro97] for examples of such singular fibrations in higher dimensions.
The approach of obtaining the mutation formula presented in this chapter uses the paradigm of
neck-stretching in Symplectic Field Theory (SFT) whereas [PT20] uses Liouville neighborhoods of
the Lagrangian tori. One advantage of using SFT neck-stretching is that, it allows us to obtain
mutation formulas for Lagrangians that are not necessarily diffeomorphic to tori. The construction
of local higher mutations enlarges the class of Lagrangian manifolds that can be mutated. Thus,
understanding the relationship between the Floer theoretic invariants might allow us to understand
finer details about mirror symmetry. For example, we can apply Theorem 1.2 to Lagrangian surfaces
of higher genus. Although as stated, the theorem requires the ambient symplectic manifold to
be compact, the same proof would be applicable to exact Lagrangians in non-compact symplectic
manifolds. Thus, we can recover cluster-algebraic relations in the Floer theoretic invariants of exact
Lagrangian surfaces under mutation, which are similar to the relations in the microlocal sheaves as
found by Shende, Treumann and Williams [STW16b].
Another feature of local higher mutations is that they preserve the diffeomorphism type of
Lagrangians, while potentially changing the Hamiltonian isotopy class. Thus, the change in Floer
