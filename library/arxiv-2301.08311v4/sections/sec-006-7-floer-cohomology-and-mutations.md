---
doc_id: arxiv-2301.08311v4
doc_title: "FLOER COHOMOLOGY AND HIGHER MUTATIONS SOHAM CHANDA"
section_id: sec-006-7-floer-cohomology-and-mutations
section_title: "Floer Cohomology and Mutations"
section_number: 7
pages: 65-72
source_pdf: 2301.08311v4.pdf
source_sha256: 385139c69e18f5b0
doc_brief: "FLOER COHOMOLOGY AND HIGHER MUTATIONS — We extend the construction of higher mutation as introduced in [PT20] to local higher mutation, which is applicable to a larger class of monotone Lagrangians."
---
We begin this section with recalling the notion of Lagrangian Intersection Floer cohomology with
local systems. After setting up the conventions and the review of the Floer cohomology, we prove
the invariance of Floer cohomology under mutation. This review follows the exposition in Section 2
of [PT20] and the local system version follows the exposition in [Aur14].
7.1. Floer Cohomology with local system. We explain the construction of Floer cohomology
with local system for monotone Lagrangians. This was first introduced by Oh in [Oh93], [Oh95a].
Let (L,K ) be a monotone pair of compact orientable spin Lagrangians in a compact monotone
symplectic manifold M that transversely intersect where L is locally mutable and K is outside the
mutation neighborhood. Assume the minimal Maslov number of L,K are at least 2. Let EL,EK be
flat C line bundles over L,K with holonomy ρL,ρK. We denote the tuple (L,ρL) and (K,ρK) by
eL, eK. We define the chain complex CF (eL, eK) as follows.
CF (eL, eK) =
M
p∈L∩K
hom(EeL|p,E eK|p)
We explain the relevant moduli spaces of strips that we use to define a coboundary operator.
Fix a t-dependent almost complex structure Jt such that Jt =Jstd in the mutation neighborhood
and makes all the holomorphic strips u : R× [0, 1]→M with u(R×{ 0})⊂L and u(R×{ 1})⊂K
FLOER COHOMOLOGY AND HIGHER MUTATIONS 66
regular by using classical transversality results such as Proposition 3.2 in [Oh93]. We denote the
moduli space of unparameterized (i.e., quotiented by the R translation of the domain) holomorphic
strips byM(L,K ) and we use M(L,K )0 to denote the moduli space of strips of index one. To
ensure that a regular J such that it restricts to the standard Jstd in the mutation neighborhood,
we just note that there are no holomorphic strips or discs contained completely in the mutation
with boundary on L or K. We can also ensure that J0,J 1 are chosen generically such that the
Maslov 2 discs with boundary on L,K are regular. The disc potential of eL is defined as follows. Let
β∈H2(M,L ), we denote the moduli space of Maslov 2 disc in the homology class β byM(L,β ).
These moduli spaces have an evaluation map ev :M(L)→L after choosing a boundary point, and
nβ denotes the degree of the evaluation map.
(7.1.1) W (eL) =
X
β∈M(L,β)
nβ.ρL(∂β)
We can similarly define the disc potentialW (eK) for the Lagrangian K. Given a rigid holomorphic
strip u∈M (L,K )0 such that lims→−∞u(s,t ) =p and lims→∞u(s,t ) =q. We denote the parallel
transport map along u(s, 0) on the line bundle EeL byψL(u) :EeL|p→E eL|q. Similarly, define ψK(u)
to be the parallel transport along u(s, 1).
We now define the Floer coboundary operator. Denote the coboundary operator as∂ :CF (eL, eK)→
CF (eL, eK), we will explain how it acts on an elementη∈ hom(EeL|p,E eK|p) of a summand inCF (eL, eK)
and then extend it linearly.
∂η =
X
u∈M(L,K)0
ψK(u)◦η◦ψL(u)−1
We can check that for a generic choice of J we can arrange ∂2x = (W (eL)−W (eK))x, thus when the
disc potentials are equal, we have that ∂ is an actual differential.
Theorem 7.1 ([Oh93],[Oh95a]). If the disc potentials of the Lagrangians in the monotone pair
match, i.e., W (eL) =W (eK), for a generic choice of Jt we have that ∂2 = 0. We define the Lagrangian
Intersection Floer homology HF of (eL, eK) as the homology of the chain complex (CF (eL, eK),∂ ).
HF (eL, eK) = ker∂
im∂
We explain the properties on the almost complex that we require while counting strips. We call a
t-dependent family Jt of almost complex structure regular for Floer theory if it satisfies the following
properties:
• J0,J1 makes the moduli space of Maslov 2 discs with 1 boundary marking with boundary on
L or K regular and the evaluation at boundary is transverse to L∩K.
• No Chern 1 Jt holomorphic sphere intersects L∩K for all t∈ [0, 1].
• All Maslov index 1 Jt holomorphic strips are regular.
• There are no negative index Jt holomorphic strips.
Although we don’t enforce regularity of index two strips, counting the index one Jt holomorphic
strips for a Jt that is regular for Floer theory gives us a correct Floer coboundary operator ∂. This
follows from the fact that the space of regular Jreg of t-dependent almost complex structures is
dense, and regularity of index one strips imply by a implicit function theorem argument and Gromov
compactness argument that the disc count for Jt is constant for small perturbations.
FLOER COHOMOLOGY AND HIGHER MUTATIONS 67
Remark 7.2. Since the Lagrangian L is exact in the mutation neighborhood, there are no
holomorphic discs or spheres lying completely inside the mutation neighborhood. Thus, we can
choose any almost complex structure in the mutation neighborhood, and then we can assume that
throughout our perturbation scheme, we don’t change the almost complex structure in the mutation
neighborhood. We can also ensure that J0 =J1 since Maslov two discs are simple by [Laz11a] and
the usual transversality arguments for simple holomorphic maps show that for a Baire dense set one
attains regularity.
7.2. Bulk deformed monotone Floer theory with domain dependent perturbations. We
will explain a version of monotone Lagrangian Floer cohomology where we use domain dependent
almost complex structure. In Section 4 and Section 5 we obtain a domain dependent choice of almost
complex structure such that the constrained moduli space of rigid holomorphic strips with markings
going to a nice divisor D are in bijection with rigid broken strips. We will define a deformation of
the Floer coboundary ∂ by counting strips with interior markings going to a nice divisor D and show
that the resulting Floer homology is the same as the usual one which we defined in the previous
subsection. For more details on the construction of domain dependent Lagrangian intersection
theory, see [CW17]
We explain describe domain dependent almost complex structure for marked strips. We define
Ms
k to be the moduli space of strips with k interior markings and Us
k
eπs
k
−→Ms
k be the universal
moduli space. A domain dependent choice of almost complex structure Jk for k≥ 1 is a map
Jk :Us
k→J (M,ω,D ). A collection of domain dependent almost complex structure is said to be
coherent if it satisfies certain properties under gluing and breaking as defined in Definition 3.14
in [CW17]. A map u :Sz→ (M,L,K ) from a k marked strip Sz =fπs
k
−1
([z]) with boundary lying
on L,K and the endpoints going to the intersection points in L∩K, where [ z]∈M s
k is called
holomorphic with respect to the domain dependent almost complex structure J if it satisfies the
domain dependent version of the Cauchy Riemann equation
du(z) +Jk(z, (u(z)))◦du◦jS = 0.
7.2.1. Choosing perturbations. We explain how to choose a domain dependent almost complex
structure to achieve regularity of strips. We choose perturbation scheme P inductively on the
number of interior marked points. For k = 0 marked points, we choose a t−dependent almost
complex structure that is regular for Floer theory and the index 2 strips are also regular. For a disc
with one interior and one boundary marking, we set a domain dependent almost complex structure
that makes the moduli space of discs with boundary on L and K regular and the evaluation map of
interior marked point to D with multiplicity d and boundary marked point going to L∩K regular
for all d. For k = 1 marked strip, the domain dependent perturbations on the boundary strata are
determined from the ones on the disc with one interior marking and the t-dependent Jt chosen for
k = 0. We extend the choice to the whole of Us
1 so that near the end points (input and output) of
the strip,J1(z) =Jt(z) and we require anyJ1 holomorphic strip with the interior marking mapping
to D with multiplicity d regular in the constrained moduli space. This can be attained by following
the treatment of regularity of tangency conditions as done in [CM07]. We proceed inductively to
get a coherent perturbation data P that achieves the following regularity results:
• (R1) Any unbroken strip with the k markings meeting D with differing intersection multi-
plicities is regular in the constrained moduli space where we enforce the intersection numbers
at the markings.
• (R2)Every rigid strip has no tangency to D at the interior markings and is regular.
Using the transversality theorem 4.1 in [CW17] we can show that there is a comeagre set of
coherent perturbation data which achieves the regularity results (R1-2) as given above. Let
FLOER COHOMOLOGY AND HIGHER MUTATIONS 68
MP(M,L,K,D )0 be the moduli space of rigid marked holomorphic strips with respect to a coherent
perturbation dataP that achieves the regularity result (R1-2). Since L,K is a monotone pair of
Lagrangians, there is an upper bound on the energy of index 1 strips, thus by a Gromov compactness
argument we seeMP(M,L,K,D )0 is compact. Thus, regularity enforces that there are only finitely
many rigid strips with interiors marking going to D. From (R2) we also get that any rigid strip
intersectsD transversally.
7.2.2. The ∂P
D coboundary operator. We define a coboundary operator by counting rigid strips with
marked points mapping to a nice divisor. Assume line bundles with flat connection have been chosen
on L,K . We define the chain complex CFP
D (eL, eK)
CFP
D (eL, eK) =
M
p∈L∩K
hom(EeL|p,E eK|p).
It is the same vector space as CF (eL, eK), we will now define the deformed Floer coboundary as
follows
∂P
Dη =
X
u∈MP(M,L,K,D)0
ψK(u)◦η◦ψL(u)−1.
The above expression for ∂P
D is a finite sum because we can apply Gromov compactness to the
set of index 1 strips since (L,K ) is a monotone pair. We define deformed disc potential map WD(eL)
and WD(eK) similar to Equation (7.1.1) by counting Maslov 2 discs with interior marking going to
D. Since our Lagrangians are monotone, we can show that WD =W . We can do so by choosing a
generic path connecting the almost complex structures that gives us a cobordism between the space
of rigid disc, since there is no sphere or disc bubbling owing to monotonicity of the Lagrangians.
Theorem 7.3. If the disc potentials of the Lagrangians in the monotone pair match, i.e. W (eL) =
W (eK), for a generic choice of perturbation scheme domain dependent almost complex structure
P, we have that ∂P
D
2 = 0. We define the bulk D deformed Lagrangian Intersection Floer homology
HFP
D of (eL, eK) as the homology of the chain complex (CF (eL, eK),∂ ).
HFP
D (eL, eK) = ker∂P
D
im∂P
D
Proof. We study the compactified one dimensional moduli space of strips to show when the deformed
disc potentials match, we can define a Floer cohomology. Consider the one dimensional moduli space
MP(M,L,K,D )1, the boundary of this moduli space is obtained by strip breaking or Maslov two
disc bubbling as in the case ofJt strips. Although we have possible disc or sphere bubbling by interior
markings going to boundary, or coming together, these situations can’t occur. Indeed, since the nice
divisor D is disjoint from L∪K any disc bubbling caused by interior marking going to boundary
has to be non-constant on the disc, thus at least Maslov two from monotonicity assumptions. Since
the moduli space of strips with interior markings tangent to D is regular, constant sphere bubbles
formed due to collision of interior marking can’t occur because of index reasons. Thus, we get the
boundary ofMP(M,L,K,D )1 consists of Maslov 2 disc bubbles and strip breaking. The Maslov
two disc bubbles in the boundary gives us the usual relation,
∂P
D
2
=WD(eL)−WD(eK) =W (eL)−W (eK).
When the disc potentials are equal, we define the bulk D deformed Floer homology as HFP
D (eL, eK) =
ker∂P
D
im∂P
D
.
□
FLOER COHOMOLOGY AND HIGHER MUTATIONS 69
7.2.3. Chain homotopy and isomorphism of Floer cohomologies. We will prove that this deformed
Floer cohomology is isomorphic to the usual Lagrangian Floer cohomology. We will show that if we
choose a t dependent almost complex structure Jt that makes evaluation from an interior marked
strip transverse to D and it’s higher jet bundles (equivalent to saying tangency constrained moduli
spaces are regular), the usual ∂ Floer coboundary is chain homotopic to ∂P
D. We can choose such
a Jt because there are countably many constraints and every non-constant strip is s−somewhere
injective as shown in [FHS95] and then countable intersection of comeagre sets are comeagre we get
that all the constraints can be cut out regularly for a comeagre set of t-dependent almost complex
structure. This choice of Jt can be viewed as a coherent perturbation data Pt that is translation
invariant under the R action on the strip, thus ∂Pt
D =∂ since we can just forget the markings that
go to D to get a bijection between the moduli space of rigid Pt strips and Jt strips.
Lemma 7.4. The bulk deformed monotone Lagrangian Floer cohomology is isomorphic to monotone
Lagrangian Floer cohomology as defined in [Oh93] i.e. HFP
D (eL, eK)∼=HF (eL, eK)
Proof. The idea of showing chain homotopy is the same as in the proof of independence of Floer
homology from the choice of almost complex structure Jt. A parameterized strip with k interior
markings and one boundary marking which is a “fake” marking added to parameterize the strip,
intuitively this boundary marking on the strip fixes the 0 in the s coordinate of (s,t )∈ R× [0, 1].
We define a homotopyJh betweenJt andJk such that for s< −1,Jh =Jt and for s> 1,Jh =Jk.
We create a map ϕh :CF (eL, eK)→CFP
D (eL, eK) by counting rigid (Maslov index 0) parameterized
Jh holomorphic strips between intersection points in L∩K. We denote the moduli space of rigid Jh
parameterized strips byMJh
par(M,L,K,D )0. By the usual generic transversality results, we know
that a generic homotopyJh would be enough to achieve regularity.
ϕhη =
X
u∈M
Jhpar(M,L,K,D)0
ψK(u)◦η◦ψL(u)−1
We can check that ϕh is a chain map i.e. ∂P
D◦ϕh = ϕh◦∂ by considering the breaking of 1
dimensional( Maslov index 1) moduli space Jh strips. The only breaking that occurs is when there
is a strip breaking. If the strip breaking occurs near −∞ of, the parameterized strip contributes to
the count in ϕh◦∂ and when strip breaking occurs near +∞ it contributes to the count in ∂P
D◦ϕh.
We define Jh−1 on a parameterized strip by Jh−1(s,t ) = Jh(−s,t ). We can count index 0
solutions to get a map ϕh−1. We can show ϕh◦ϕh−1 is chain homotopic to identity by considering a
twice-parameterized moduli space of holomorphic strips. Twice parameterization refers to choosing
two boundary markings w1,w 2 on a strip such that w1≤w2 in the s−coordinate. In the universal
moduli space of twice parameterized strips with k markings, we define a complex structure Jch
such when w1 =w2,Jch =Jt and at the lower dimensional strata of strip breaking with w1 and w2
lying in different strips,Jch =Jh in the strip component with w1 andJch =Jh−1 in the component
with w2. We now count rigid Jh holomorphic twice parameterized strips (Maslov index -1) to
create a chain homotopy map H :CF (eL, eK)→CF (eL, eK). By considering the breaking of index 0
strips, we get that H◦∂ +∂◦H =ϕh◦ϕh−1−Id. Hence, we get that homologies are the same,
HFP
D (eL, eK)∼=HF (eL, eK).
□
7.3. Proof of Mutation formula. We have now all the materials needed to prove the invariance
of HF under mutation up to a change in the local system.
We recall the notations and conventions we introduced in Section 1.
FLOER COHOMOLOGY AND HIGHER MUTATIONS 70
[C1] M is a compact, monotone, symplectic manifold of dimension 2 n.
[C2] L is a locally mutable, oriented, spin, compact, connected, monotone Lagrangian manifold in
M.
[C3] K is an oriented, spin, compact, connected, monotone Lagrangian manifold in M.
[C4] The Lagrangian K intersectsL transversely but does not intersect a small mutation neighbor-
hood B of L.
[C5] (L,K ) forms a monotone tuple.
[C6] ρL and ρK are local systems on L and K respectively.
[C7] In a mutation neighborhood B, under the identification given by the symplectomorphism ϕ ,
L is equal to the torus segment Tγ.
[C8] x1,...x n−1 is the image of generators of H1(Tγ) under the inclusion map i :Tγ ,→L.
[C9] (x1,x 2,...,x n,y 1,...y l) is a generating set of H1(L) such that xn∩i∗[Tγ] where [Tγ] is the
generator of Hn−1(Tγ). A Poincar´ e duality argument ensures the existence of such anxn.
Given a flat line bundle over L, we denote the holonomies ρ(xi) =zi, ρ(yi) =wi. The mutated
local system on the mutationLµ is equal toρµ(xi) =zi fori<n andρµ(xn) =zn(1+z1 +··· +zn−1)
and ρµ(yi) =wi for all i. We denote the mutated Lagrangian with this local system as fLµ.
Theorem 7.5 (Mutation). The disc potential is invariant under mutation if the local system ρ
is changed to ρµ ie. W (eL) = W (eLµ). Moreover, if W (eL) = W (eK) then the Floer homology is
invariant up to the same change of local system i.e. HF (eL, eK)∼=HF (fLµ, eK).
Proof. We can use a Hamiltonian perturbation on L so that it is identified to the torus segment Tγ′
in the mutation neighborhood such that near 0, γ′ =cγ for a very small c. For any ϵ> 0 we can
choose c small enough that Tγ′ is cylindrical near a contact sphere S2n−1
ϵ of radius ϵ. Thus, we can
do a neck stretching along the hypersurface S2n−1
ϵ . We choose a perturbation scheme P as given in
Theorem 5.20, thus from the Lemma 6.1 and Theorem 6.27 we get that the only rigid broken strips
or rigid broken disc with point constraint have simple discs. We know gluing results in Corollary
4.27 give us a bijection between rigid broken strips and rigid strips of a neck-stretched manifold
MT with boundary on LT or LµT and K. We similarly get a bijection between the rigid broken
disc with point constraints and the rigid unbroken disc with point constraints.
Note that the broken discs with boundaries lying entirely on the outside under mutation do not
change. Thus, we only need to study the broken discs which have inside pieces with boundaries
lying on the Lagrangians.
The classification results in Theorems 6.5 and 6.9 give us that for a fixed Reeb chord ξ of length
π/n, there is one upper disc(simple discs that are sections over the positive half-space) and n lower
discs(simple disc over negative half space) with boundary on Lin. On the other hand, for Lµin there
are n upper discs and 1 lower disc going to the Reeb chord ξ. See Remark 6.14. Thus, there is
a n←→1 and 1←→n correspondence between rigid broken strips with boundary on L and Lµ.
There is a similar correspondence between broken discs.
Applying the gluing result in Corollary 4.27, we get that there is a 1↔n andn↔ 1 correspondence
between the rigid strips with respect to the glued perturbation scheme Pgl in the stretched manifold
MT . Since all the Pgl holomorphic rigid strips are regular, and by monotonicity, there is an upper
bound on energy, we get that for a generic perturbation data eP close toPgl, the count of rigid
strips don’t change. We choose a domain-dependent perturbation as in subsection 7.2.1. A similar
argument works for broken discs with point constraints. Thus, by comparing the homology classes
under the 1↔n and n↔ 1 correspondence we get the invariance of disc potential,
W (eL) =W (eLµ).
FLOER COHOMOLOGY AND HIGHER MUTATIONS 71
L ϕ(L) Lµ
ϕ(L)
Figure 14. Clifford and Chekanov type tori
Similarly, using the 1↔n and n↔ 1 correspondence, and keeping track of the homology classes,
we see that the coboundary operators match up exactly,
(∂
eP
D)(eL, eK) = (∂
eP
D)( fLµ, eK)
where (∂ eP
D)(eL, eK) is the bulk D deformed Floer coboundary for the pair ( eL, eK) and (∂ eP
D)(eL, eK) is the
bulk D deformed Floer coboundary for (fLµ, eK). Thus, we have HFP
D (eL, eK)∼=HFP
D (fLµ, eK). Now
using Lemma 7.4 we get that the Floer homologies are the same.
□
Now, Theorem 1.2 directly follows from Theorem 7.5.
7.4. Applications.
Proof of Corollary 1.5. We will apply Theorem 1.2 to L,ϕ (L) where ϕ(L) is a Hamiltonian pertur-
bation ofL such thatϕ(L)∩L is away from the mutation neighborhood. Such a perturbation always
exists for Clifford type torus in [PT20], see Figure 14. By applying Theorem 1.2 to L,K =ϕ(L).
We have
HF (eL,eϕ(L))∼=HF (eLµ,eϕ(L)).
Now using invariance of HF under Hamiltonian isotopy we have
HF (eL,eL)∼=HF (eLµ,eL).
Thus we have that the Clifford and Chekanov tori are Hamiltonian non-dis placeable. □
Remark 7.6 (Non-Displaceability of Chekanov tori and Real Projective spaces in odd dimensions) .
2
One straightforward generalization of Theorem 1.2 can be obtained by considering Lagrangians
with local-systems coming from F−line bundles, where F is any field. The proof of Theorem 1.2 is
based on comparing moduli space of rigid broken disks. The field C was not essential in any part
2This answers a question raised in Remark 3.2.3 of [KS23].
FLOER COHOMOLOGY AND HIGHER MUTATIONS 72
of the proof, thus we can replace the complex local system with F-local systems defined by the
holonomy map ρL :H1(L)→ F×.
An application of such a generalization would let us show that for odd n, the higher mutation TCh
of the Clifford torus TCl in Pn is non-displaceable from RPn. This follows from the computation of
HF (TCl, RPn) in [Als11] and from using Z2 coefficients in Theorem 1.2 and seeing that the mutation
formula fixes the trivial local system, i.e. (1 , 1,..., 1) = (1, 1,...,n ) mod 2 when n is odd.
