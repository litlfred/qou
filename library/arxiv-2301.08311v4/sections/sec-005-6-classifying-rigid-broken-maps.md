---
doc_id: arxiv-2301.08311v4
doc_title: "FLOER COHOMOLOGY AND HIGHER MUTATIONS"
section_id: sec-005-6-classifying-rigid-broken-maps
section_title: "Classifying Rigid Broken Maps"
section_number: 6
pages: 54-65
source_pdf: 2301.08311v4.pdf
source_sha256: 385139c69e18f5b0
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND HIGHER MUTATIONS — We extend the construction of higher mutation as introduced in [PT20] to local higher mutation, which is applicable to a larger class of monotone Lagrangians."
---
The aim of this section is to classify combinatorial types of rigid broken strips or rigid broken
discs with the choice of perturbation scheme as done in Section 5. We will show that any rigid
broken strip has only two levels and all the inside pieces are either punctured spheres or discs with
one boundary puncture that is asymptotic to a Reeb chord of length π/n.
Lemma 6.1. If (u, D) is a regular vertically constrained broken strip that is also rigid, it has at
most two levels and the inside piece does not intersect the critical locus crit(πm). Similarly, if (u, D)
is a regular vertically constrained broken disc with point constraint, it has at most two levels and the
inside piece does not intersect the critical locus crit(πm).
Proof. We have already chosen a perturbation scheme on the outside piece to make the moduli
space of broken strips transversally cut out. If (u, D) is a rigid broken strip, the only deformations
of the broken map u are the ones obtained by the action of the automorphism group of the domain,
i.e., by reparameterizing the broken strip. If u has more than two levels, there will be a non-trivial
neck piece ui, (recall that any neck level should have a non-trivial map from the definition of a
broken strip). Since ui is a non-trivial map, translation of ui by the R action on R × S2n−1 produces
FLOER COHOMOLOGY AND HIGHER MUTATIONS
55
neck maps which have the same asymptotic Reeb chords and orbits, so there is a one dimensional
deformation of u obtained by replacing ui by its translates. Notice that this deformation cannot be
obtained by a reparameterization, as the map ui is not a trivial strip or a cylinder. Thus, we get a
contradiction to the assumption that u is rigid.
Now assume that uin touches the critical locus, since it is regular as a vertically constrained broken
strip, we have that Ind( eDvc
u ) < Ind( eDu), we see that u is of high index and thus cannot be rigid.
□
6.1. Elementary discs. We will now classify the moduli space of single punctured discs with
boundary on an asymptotically cylindrical Lagrangian manifold.
The heuristic of classifying
elementary discs by showing they are sections over the fibration is inspired from [Sei01]. Recall, we
can define a torus segment over any simple path in the punctured complex plane. Thus, we have a
Lagrangian TR+iϵ for the path γ : R →C∗given by γ(s) = s + iϵ.
TR+iϵ = {(z1, . . . , zn)|πm(z) ∈R + iϵ, |z1| = · · · = |zn|}.
Note that this Lagrangian is asymptotically close to the cylindrical Lagrangian TR\{0}.
Definition 6.2 (Elementary disc in Cn ). A map u : H →Cn such that the restriction u|R lies on
the Lagrangian TR+iϵ or Tγ for a cylindrical γ and u is asymptotic to a trivial strip over a Reeb
chord of length π
n is called a elementary disc. We denote the set of elementary discs with Reeb
chord ζ at infinity with boundary on TR+iϵ and Tγ by Mζ(R + iϵ), Mζ(γ) respectively.
In this subsection, we will classify single punctured discs with boundary on TR+iϵ that have a
minimal length Reeb chord at its puncture. After classifying such discs, we will use a Gromov-
compactness and regularity argument to conclude a classification of elementary discs provide us a
classification of discs that occur as interior pieces of rigid broken strips and discs.
Lemma 6.3. An elementary disc u with boundary on TR+iϵ can be viewed as sections of πm over the
upper half-space H+iϵ or the lower half-space −H+iϵ i.e. ∃ϕu, a biholomorphism from H →±H+iϵ
and a section su : ±H + iϵ →Cne such that u = su ◦ϕu.
Proof. It is enough to show that ϕu = πm ◦u is a biholomorphism to ±H + iϵ, then su = u ◦ϕ−1
u
will
be the required section. As the map u = (u1, . . . , un) is asymptotic to a trivial strip from Lemma
3.12, let’s denote the trivial strip by
uζ(z) = (z1/nl1, . . . , z1/nln),
over a Reeb chord
ζ(t) =
1
√n|l1|(eitl1, . . . , eitln),
of length π
n in S2n−1, where we have |li| = |lj| for all i, j since the boundary of u lies on TR+iϵ. The
idea of the proof is to show that since asymptotically all the coordinates ui are away from 0, we get
that the product u1.u2 . . . .un is asymptotic to a trivial strip over a Reeb chord of length π and thus
essentially, a linear map.
Note that u can be extended to a map from the closed disc to Pn such that
u(∞) = [l1 : · · · : ln : 0] ∈TCliff ⊂Pn−1
∞,
where Pn−1
∞
= [z0 : · · · : zn−1 : 0]. The fact that u(∞) is a point in the torus TCliff follows from the
fact that the boundary of u lies on TCliff from the definition of TR+iϵ.
By checking the S2n−1 component of the metric, we know that in limit dcyl(u(z), uζ(z)) →0
as |z| →∞. We can arrange for
u(z)
|u(z)| to lie in a small neighborhood N of the Reeb chord ζ in
the unit sphere S2n−1, such that πm(N) lies in a small neighborhood Nζ around πm(ζ) for large
FLOER COHOMOLOGY AND HIGHER MUTATIONS
56
|z|. We can also assume that the distance from origin to Nζ has a lower bound ϵ0 for some fixed
ϵ0 > 0 . This implies that we can extend πm ◦u to a map from the closed disc to P1 by defining
πm ◦u(∞) = [1 : 0].
Since the boundary of πm ◦u lies on R + iϵ and it extends to a map to P1, after applying the
Schwarz reflection principle and classification of maps from the disc D to P1 with boundary on R
we see that
πm ◦u = pR(z) + iϵ,
where pR is a polynomial with real coefficients. Now, using the fact that dcyl(u(z), uζ(z)) goes to 0,
by checking the R component of the metric, we have
lim
|z|→∞
|u(z)|
|z1/n|∥(l1, . . . , ln)∥= 1.
Thus, we can conclude that
lim
|z|→∞
|πm ◦u(z)|
|z||l1. . . . .ln| = 1
Thus combining the fact πm ◦u = pR +iϵ with the limit above, we see that pR is a non-constant linear
polynomial and thus a biholomorphism. If pR = az +b with a > 0 we get πm ◦u is a biholomorphism
to the upper half space H + iϵ , or else if a < 0, it is a biholomorphism to the lower half-space
−H + iϵ.
□
Remark 6.4. Using Lemma 6.3 we can reduce the problem of classifying elementary discs to the
problem of classifying sections. As we have πm(z) = −πm(zξ) for an nth root of unity ξ, a section
su over −H + iϵ is given by a section over H −iϵ and then multiplying it with ξ. Thus, it is enough
to classify sections over H ± iϵ for ϵ > 0. Also note that the phase action of T n−1 on Cn defined
by (θ1, . . . θn−1).(z1, . . . , zn) = (eiθ1z1, . . . , eiθn−1zn−1, e−i(P θj)zn) induces a free action on the set of
sections of πm over H ± iϵ.
Theorem 6.5 (Classification of sections). Let ϵ > 0.
(1) There is a unique T n−1 orbit of sections with finite Hofer energy over H + iϵ with boundary
on R + iϵ given by sθ = θ.(z1/n, . . . , z1/n) for θ ∈T n−1.
(2) There are n disjoint T n−1 orbits of sections with finite Hofer energy over H−iϵ with boundary
on R −iϵ given by
sk
θ = θ.((z + 2iϵ)1/n, . . . ,
z
z + 2iϵ(z + 2iϵ)1/n
|
{z
}
kth coordinate
, . . . , (z + 2iϵ)1/n)
Proof. (1). Let the section be eu = (f
u1, f
u2, . . . , f
un). Thus f
u1(z) . . . f
un(z) = z and |u1| = . . . |un|
on R + iϵ. As the domain of definition is in a complex plane with the negative imaginary axis
removed, C \ [0, −i∞), we can define an nth root in this domain. Let uk =
f
uk
z1/n . Thus u1. . . . .un = 1
on H + iϵ and |uk| = 1 on R + iϵ , so we can extend uk to C by Schwarz reflection by defining
uk(z) =
1
uk(z+2iϵ). Note that EH(eu) < ∞implies that u is asymptotic to a trivial strip over a Reeb
chord. From |f
uk(z)| = |z|1/n for z ∈R + iϵ, we conclude that u is asymptotic to a trivial strip over
a Reeb chord of length π/n. Thus, we have uk is bounded near ∞. Since uk can be extended to an
entire function, we have by Liouville’s theorem that uk is constant. Now, from f
u1(z) . . . f
un(z) = z
and |u1| = . . . |un| on R + iϵ we see that eu = θ.(z1/n, . . . , z1/n) for some θ ∈T n−1.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
57
(2). Let the section be eu = (f
u1, f
u2, . . . , f
un). From πm ◦eu(0) = 0 we have that at least one of
euk is 0 at 0, without loss of generality assume eu1(0) = 0. Thus, in a neighborhood around 0, we
have f
u1(z) = zh(z) which implies hf
u2 . . . f
un = 1 and f
u2, . . . , f
un are non-vanishing on H −iϵ. Define
uk =
f
uk
(z+2iϵ)1/n , for k̸ = 1 we have uk is non-vanishing and |uk(z)| = 1 for z ∈R −iϵ, thus we can do
a Schwarz reflection as above to see that uk extends to an entire function. From EH(eu) < ∞and
|f
uk| = |z|1/n on R −iϵ we have that uk is bounded near infinity for k̸ = 1. Thus, from Liouville’s
theorem, we have uk is constant for k̸ = 1. Now from πm ◦eu(z) = z and the definition of uk, we
have that f
u1 =
z
z+2iϵ(z + 2iϵ)1/n. Thus, eu = θ.(
z
z+2iϵ(z + 2iϵ)1/n, (z + 2iϵ)1/n, . . . , (z + 2iϵ)1/n) for
some θ ∈T n−1. This gives one of n T n−1 orbits. The other orbits are obtained from the cases
uk(0) = 0 where k̸ = 1. Using a similar technique as above, by writing uk(z) = zh(z), one can show
that the section would be of the form sk
θ.
□
Corollary 6.6. For a Reeb chord ζ of angle π/n from T+ to T−we have that for ϵ > 0 |Mζ(R+iϵ)| =
1 and |Mζ(R −iϵ)| = n
Theorem 6.7. The sections classified in Theorem 6.5 are transversally cut out, that is, the linearized
Cauchy-Riemann operator eDu is surjective for all the sections u classified in Theorem 6.5.
Proof. This follows from Theorems 5.5 and 5.7.
□
6.2. Flattening the curve: R + iϵ to a cylindrical γ. We will now show that the count of
elementary discs with boundary on Tγ for an admissible cylindrical γ is the same as the disc count
we obtained in Corollary 6.6. We will assume ϵ > 0 hereon. We will compactify the rigid discs to
discs in CPn and prove bijection between the compactified discs. Recall that the closure of TR+iϵ is a
self-clean intersecting Lagrangian. A compactified elementary disc will map the boundary puncture
mapping to the self-clean intersection at the infinity divisor T n−1
Cliff ,→CPn−1
∞
,→CPn.
Later we will use a Lagrangian isotopy coming from a family of asymptotically cylindrical paths.
We explain the process of compactifying elementary discs with boundary on Tγt for an asymptotically
cylindrical path γt . We can compactify elementary discs to discs in CPn. Given any elementary
disc u : D2 \ {1} with boundary on TR±iϵ or Tγt we can extend u to u that maps 1 to a point in the
Clifford torus T n−1
Cliff in the infinity divisor CPn−1
∞
,→CPn. The Clifford torus is the self-intersection
locus of the Lagrangians T R±iϵ (and T γt), thus given any holomorphic map v : D2 →CPn with
boundary on T R±iϵ (or T γt) such that v−1(CPn−1
∞) = {1}, we have that v : D2 \ {1} →Cn is
asymptotic to a Reeb chord with boundary on T±. Similar to Step 5 in the proof of asymptotic
convergence in Theorem 3.5, by using Theorem 3.2 of [Sch16] the length of the Reeb chord is the
same as the eigenvalue of the leading order eigenfunction. We define the moduli space of discs in
CPn that restrict to elementary discs in Cn when restricted to D \ {1} as elementary discs in Cn.
Definition 6.8 (Elementary disc in CPn). A map u : D →CPn with boundary on the Lagrangian
T R+iϵ or T γ for a cylindrical γ is called elementary when u−1(CPn−1
∞) = {1} and the eigenvalue
of the leading order eigenfunction of u as in Theorem 3.2 of [Sch16] is π/n. We denote the set of
elementary discs that maps 1 7→p ∈T n−1
Clif and boundary on T R+iϵ or T γ by Mp(R + iϵ), Mp(γ)
respectively.
Note that for each p ∈T n−1
Cliff there are 2n Reeb chords ζi in S2n−1 of length π/n with boundary
on T± that descend to p. From the definition of elementary discs we have the following bijections
Mp(R ± iϵ) ↔∪2n
i=1Mζi(R ± iϵ)
FLOER COHOMOLOGY AND HIGHER MUTATIONS
58
Mp(γ) ↔∪2n
i=1Mζi(γ).
We denote the collection of discs in Mp(R ± iϵ) that converges to the Reeb chord ζ in cylindrical
coordinates as
Mζ
p(R ± iϵ),
the notation Mζ
p(γ) is defined similarly. Clearly we have the following bijections by extending and
restricting the maps,
Mζ
p(R ± iϵ) ↔Mζi(R ± iϵ)
Mζ
p(γ) ↔Mζi(γ).
We will now prove the main theorem of the subsection, which states that there is a bijection
between the moduli spaces of rigid discs if we ‘flatten the curve’. More precisely, if we flatten R + iϵ
to an admissible path γ0, counts of elementary discs don’t change.
Theorem 6.9. For each ϵ > 0 and Reeb chord ζ of length π/n with boundary on T±, the moduli
space of elementary disc with Reeb asymptote ζ and with boundary on Tγ for an admissible cylindrical
γ is in bijection with the moduli space of elementary discs with Reeb asymptote ζ with bounding
TR+iϵ
Mζ(γ) ↔Mζ(R + iϵ)
For a mutated admissible cylindrical γ′, we have a similar bijection,
Mζ(γ′) ↔Mζ(R −iϵ)
We collect some results about regularity and area computation here before proceeding to the
proof of Theorem 6.9
Remark 6.10 (Regularity for compactified elementary discs bounding T γt). We collect some
regularity results here that allows us to obtain a cobordism. From Theorem 6.7 we have that any
elementary disc in Cn is cut out regularly, i.e., the linearized Cauchy-Riemann operator at any
elementary disc u , Du is surjective. Consider the extension to the elementary disc u in CPn, this
is a holomorphic disc that maps a boundary point to the self-clean intersection locus. We can set
up the moduli problem of discs with boundary on T R±iϵ or T γ similar to the treatment of moduli
space of strips with boundary on cleanly intersecting Lagrangians as done by Schm¨aschke in [Sch16].
The linearization of the ∂section in this setting is denoted as follows,
Du : W k,p,δ(u∗TCPn, ∂u∗TT R+iϵ) →W k−1,p,δ(Hom(TH, u∗TCPn))
The following lemma shows that u is regular for any elementary disc u.
We begin by comparing the formal adjoints. Note that these formal adjoints D∗
u and D∗
u are defined
through different metrics, the first one is defined through a hermitian metric on CPn and the second
one is defined through a cylindrical hermitian metric on Cn. The cylindrical hermitian structure
on Cn at z is given by ⟨, ⟩0
|z|2 where ⟨, ⟩0 is the standard Hermitian metric on Cn The hermitian
metric on CPn is given by hCPn( , ) = gCPn( ) −gCPn( , J ) where gCPn = dr2/r4 + λ2
0/r2 + π∗gFS
in the cylindrical end R × S2n−1 of Cn. The subscripts refer to the projection along the splitting
T(R × S2n−1) = TR ⊕R⟨R⟩⊕ξ, where R is the Reeb field and ξ is the contact structure on S2n−1
to write sections as a sum of 3 projections. Consider the following rescaling of sections,
FLOER COHOMOLOGY AND HIGHER MUTATIONS
59
S1 : Γ(u∗TCn) →Γ(u∗TCn)
S1(ηr + ηR + ηξ) = r2(ηr + ηR) + ηξ
S2 : Γ(Hom(TΣ, u∗TCn)) →Γ(Hom(TΣ, u∗TCn))
S2(αr + αR + αξ) = r2(αr + αR) + αξ.
For these rescalings we have the following relation between the cylindrical and CPn metric
(6.2.1)
⟨α, Siβ⟩CPn = ⟨Siα, β⟩CPn = ⟨α, β⟩cyl.
Using these rescalings we have,
D∗
u = S2D∗
uS−1
2 .
(6.2.2)
Lemma 6.11. For any elementary disc u in CPn with boundary on T γt , the linearization Du is
surjective.
Proof. It will be enough to show that the kernel of the formal adjoint D∗
u is trivial. Let η be an
element in the kernel of the formal adjoint D∗
u, thus it is an element in W k,p,−δ(Hom(TH, u∗TCPn)).
From Equation (6.2.2) we have that S−1
2 η will be an element in kernel of D∗
u. Since we have η ∈
W k,p,−δ(Hom(TH, u∗TCPn)), we have ∥η(s, t)∥CPn ∈O(eδs), which implies that ∥S−1
2 η∥cyl ∈O(eδs)
thus S−1
2 η ∈W k,p,−δ(Hom(TH, u∗TCn)). But we have already proved that for any elementary disc
u, the linearization Du is surjective in Theorem 6.7, thus S−1
2 η = 0, hence we have η = 0. Thus, the
kernel of D∗
u is trivial, hence Du is surjective.
□
Remark 6.12 (Area computations). We calculate some symplectic areas that will be required for
dealing with bubbling. Recall that Cn with the Fubini-Study, ωFS is symplectomorphic to the unit
ball B1(0), ω0 by the following rescaling symplectomorphism ϕFS : B1(0) →Cn,
ϕFS((z1, z2, . . . , zn)) 7→
1
1 −P
i |zi|2 (z1, . . . , zn).
It is clear that ϕ−1
FS(Tγ) = Teγ for some eγ : [0, 1] →C∗. Given a elementary disc ut in CPn with
boundary on T γt, we can calculate it’s symplectic area by using the symplectomorphism ϕFS. Note
that from convergence to Reeb chords, we can extend the map ϕ−1
FS ◦un by adding a Reeb chord of
length π/n. Recall from Lemma 2.14 and Remark 2.15 that Teγ is an exact Lagrangian. Moreover,
for the primitive feγ of λ0,i.e. λ0|Teγ = dfeγ, we have that feγ is constant over the fiber T n−1, in other
words, there is a f eγ such that feγ = πm ◦f eγ. Now we can use Stoke’s theorem to calculate the
symplectic area of un as follows,
R
un ωFS =
R
ϕ−1
F S◦un ω0 = π/n ± (f eγ(eγ(1)) −f eγ(eγ(0))).
Now we can proceed to the proof of Theorem 6.9.
Proof of 6.9. The proof is based on a cobordism argument. Fix a family γt of paths in C∗such that
the compactification γt in CP1 is a C2 isotopy from γ to R + iϵ. This induces a Lagrangian isotopy
of T γ to T R+iϵ.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
60
Consider the parameterized moduli space f
M(ζ) of triples (t, Σ, u) where u is a J0 holomorphic
map from the one-marked-disc Σ to CPn with boundary on T γt which takes the marked point to
the Reeb chord ζ. This is a cobordism between Mζ(γ) and Mζ(R + iϵ).
From Remark 6.12 we see that there is no bubbling in this moduli space. Indeed, from exactness
of Tγt in Cn, we have that any possible disc or sphere bubble has to touch the infinity divisor CPn−1
∞.
One can use the area computations from Remark 6.12 to conclude that there can’t be a bubble
touching the infinity divisor. From Lemma 6.11 we get that the parametrized moduli space f
M(ζ) is
a regularly cut-out manifold with boundary of dimension one. The Lemma 6.11 also proves that the
natural projection map f
M(ζ) →[0, 1] is a submersion.
Thus, we get that f
M(ζ) is a trivial cobordism between the zero-dimensional manifolds Mζ(γ)
and Mζ(R + iϵ). Hence we get the required bijection Mζ(γ) ↔Mζ(R + iϵ). A similar cobordism
argument works for mutated admissible paths by choosing a family γ′
t interpolating between γ′ and
R −iϵ.
□
Remark 6.13 (Theorem 6.9 for longer Reeb chords). The proof technique for Theorem 6.9 gives
us a bijection between single punctured holomorphic discs with higher multiplicity Reeb chords as
well. Let k > 0 be a natural number. We denote the moduli space of single punctured holomorphic
discs with boundary on TR+iϵ, that is asymptotic to a Reeb chord ζ of length kπ/n, as
Mζ(R + iϵ).
We similarly denote the moduli space of single punctured disc with boundary on Tγ with Reeb
asymptote ζ as
Mζ(γ).
A trivial cobordism argument as above shows that we get a bijection (more precisely, a diffeomor-
phism)
Mζ(R + iϵ) ↔Mζ(γ).
Remark 6.14. The results of this subsection should be interpreted as a 1 ←→n correspondence
between elementary discs with fixed Reeb chords under mutation. Let ζ+ be a Reeb chord of minimal
length starting on T+ and ζ−be a Reeb chord of minimal length starting on T−. From Remark
6.4 and Theorems 6.5 and 6.9 we get the following disc counts. For the pre-mutated Lagrangian
boundary Tγ, there is exactly one elementary disc with Reeb chord ζ+ and exactly n elementary
discs with Reeb chord ζ−. For the mutated Lagrangian boundary Teγ, the disc count gets reversed.
There are exactly n elementary discs with Reeb chord ζ+ and exactly one elementary disc with
Reeb chord ζ−.
6.3. Classifying inner piece maps with boundary on TR+iϵ. We will use a similar argument
as in Theorem 6.5 to classify all possible holomorphic punctured discs. We only need classification
of single punctured disks for this article, we add this subsection for the sake of completion.
6.3.1. Case 1: Disc with only boundary punctures. Up to an automorphism, a punctured disc is
equal to the upper half-plane with punctures on the real line. Assume that we have k + 2 punctures
on the real line, at the points 0, 1, r1, . . . , rk, we denote it by Hk+2. Let
u : Hk+2 →Cn
be a disc with boundary on TR+iϵ. Since near the punctures , the disc u is asymptotic to Reeb
chords starting on the tori T±, we have that πm ◦u has poles at the punctures. Thus, πm ◦u is a
FLOER COHOMOLOGY AND HIGHER MUTATIONS
61
meromorphic map from H with boundary lying on R + iϵ. The usual Schwarz reflection trick gives
us that
πm ◦u = p
q + iϵ,
where p, q are real polynomials such that degree of p is strictly bigger than that of q. Here q(z) is a
polynomial of the form
zm0(z −1)m1(z −r1)m2 . . . (z −rk)mk+2
where m0, . . . mk+2 are the multiplicities of the limiting Reeb chords at the punctures. Assume that
{u1, . . . , ul} are roots of πm ◦u in H, the roots here can have repetitions to accommodate roots with
multiplicities. Let f be a rational function defined as follows
f(z) = πm ◦u(z) × Πl
j=1
z −uj
z −uj
.
From construction of f, we see that all the roots of f lie in the lower half plane, and the poles of
f are on the real line. Thus, we can take a nth root of f by taking nth root of each factor. This
construction can be generalized for any rational function on H, we define it below.
Definition 6.15 (Cleaning of rational functions). Let p/q be a rational function on H, with zeroes at
{u1, . . . , ul} and poles at {ζ1, . . . ζo}. Here the roots are poles repeat according to its multiplicitiesx.
We call f to be a cleaning of the rational function of p/q if
f(z) = p(z)
q(z) × Πl
j=1
z −uj
z −uj
× Πo
j=1
z −ζj
z −ζj
.
Definition 6.16 (Weight Matrix). We call a n × l matrix B a weight matrix if each column is a
standard basis vector ei of Cn.
ei =


0
...
0
1
0
...
0


Definition 6.17. Let W be the set of all possible n × l weight matrices. We define an assignment
function as follows,
A : W × Cl →Cn
A(B, (z1, . . . , zl)) = (zb11
1 zb21
2
. . . zbn1
n , zb12
1 zb22
2
. . . zbn2
n , . . . , zb1l
1
. . . zbnl
n )
Example 6.18. If B =


0
1
1
0
0
0

, then A(B, (x, y)) = (y, x, 1).
A quick counting argument shows that there are nl weight matrices of size n × l. We can now state
the classification theorem.
Theorem 6.19. Let u : Hk+2 →Cn be a holomorphic disc with boundary on TR+iϵ. Assume the
zeroes of πm ◦u, counted with multiplicity, are {x1, . . . , xl}. Let f be the cleaning of the rational
function πm ◦u. Then,
u(z) = θ.f1/n(z)A

B,
z −x1
z −x1
, . . . z −xl
z −xl

where B is a weight matrix and θ is an element of T n−1 acting on Cn by the phase action.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
62
Proof. Let u = (u1, . . . , un). We know that u1u2 . . . un has roots at {x1, . . . xl}, thus each root is
from some component ui. If ui has roots {y1, . . . yh} we define
eui = Πh
j=1
z −yj
z −yj
× ui.
In case ui doesn’t have any roots, then we set eui = ui. Denote the product eu1 . . . eun by f. Note
that from the construction f is actually the cleaning of the rational function πm ◦u. Thus, the nth
root f1/n is a well-defined meromorphic function on H. Also, since |r −z| = |r −z| for any real
number r, we have
|eui(r)| = |euj(r)|
for any i, j and real number r. Since near the punctures u is asymptotic to a Reeb chord starting on
the Legendrian tori T±, the holomorphic function
eui
f1/n extends over the punctures. Since |eui| = |f1/n|
on R, from the Schwarz reflection argument in Theorem 6.5 we have that
eui
f1/n is a constant function,
thus
eui = eiθif1/n.
Thus we have
ui = eiθiΠh
j=1
z −yj
z −yj
f1/n.
The appearance of the weight matrix in the result comes from distributing l Blaschke factors z−xi
z−xi
into n coordinates. Depending on the vanishing of each coordinate functions ui, we can choose a
weight matrix B such that
u(z) = θ.f1/n(z)A

B,
z −x1
z −x1
, . . . z −xl
z −xl

.
□
Proposition 6.20. Let c be a Reeb chord with boundary on T±, then there is a single punctured
holomorphic disc with boundary on TR+iϵ with the puncture asymptotic to c.
Proof. Recall that we have a transitive T n−1 action on the space of Reeb chords. Thus, it is enough
to show that there is a single punctured disk asymptotic to a Reeb chord c± where c± is Reeb chord
starting at T± of length equal to the length of c.
Let the length of c be an l multiple of the length of the smallest Reeb chord (i.e. length of c is
lπ
n ). Let f± be a cleaning of the polynomial ±zl + iϵ and {x1, . . . , xm} be the set of zeroes of
±zl + iϵ : H →C.
Then
u±(z) = f1/n
± (z)
z −x1
z −x1
. . . z −xm
z −xm
T
,
is a single punctured disk satisfying the required properties.
□
Remark 6.21. Note that in Proposition 6.20 the number of roots in H is ⌊l
2⌋if the Reeb chord
starts at T+ or else it is ⌈l
2⌉.
Remark 6.22. Using Remark 6.13 we see that Proposition 6.20 holds for the boundary condition
Tγ for a cylindrical path γ.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
63
6.3.2. Case 2: Disc with interior punctures. The classification result for discs with interior punctures
( in other words, domains with cylindrical ends) follows a similar proof strategy, except that there is
more combinatorial freedom.
We illustrate the combinatorial freedom by considering a neighborhood of an interior puncture.
Let p ∈D2 be an interior puncture and u is a holomorphic disc with boundary on the Lagrangian
TR+iϵ which is asymptotic to a Reeb orbit near the puncture p. We can’t read off information about
the Reeb orbit by looking at πm ◦u near p. This stems from the fact that the Reeb orbits can have
some zero coordinates, so πm ◦u can be any of the following:
(1) finite at p.
(2) vanish at p
(3) have a pole at p.
Thus to account for all the cases, we need to embed the orders of vanishing and poles of the
coordinates of u in the hypothesis of the classification theorem.
We define the notion of negative degree of vanishing to mean the order of the pole and negative
order of pole to mean the degree of vanishing. e.g. the map z2 has a pole of order −2 at 0 and the
map 1/z3 vanishes to the degree −3 at 0. We also define the degree of a function at a point to be 0
if the evaluation of the function at the point is in C∗.
Theorem 6.23. Fix a finite set P of punctures in D2. Let u = (u1, u2, . . . , un) : D2
P →Cn be a
holomorphic disc from the punctured disc D2
P with boundary lying on TR+iϵ. Assume that for each
puncture p ∈P, the coordinates ui have orders of vanishing pi. Let
ef(z) = πm ◦u(z) × Πn
p∈P,i=1
z −p
z −p
pi
.
Assume ef has zeroes, counted with multiplicities, at {x1, . . . , xl}. Let f be the cleaning of ef. Then
there is a weight matrix B such that
u(z) = θ.f1/n


Πp∈P
  z−p
z−p
p1
0
0 . . .
0
Πp∈P
  z−p
z−p
p2
0 . . .
0
...
...
0
...
0
. . .
Πp∈P
  z−p
z−p
pn


B
z −x1
z −x1
. . . z −xl
z −xl
T
Proof. The idea of the proof is exactly the same as Theorem 6.19 after we factor out the zeroes
and poles from the interior puncture. Define eui = ui × Πn
p∈P

z−p
z−p
pi
. Define eu as the function
(eu1, . . . , eun) and applying the same argument as in Theorem 6.19 gives us the result.
□
6.4. Only elementary discs show up in rigid things. We now prove the main result of this
section : the only possible interior pieces for a rigid broken strip or a disc, is an elementary disc.
The idea of the proof is to utilize monotonicity of the Lagrangian pair.
Definition 6.24 (Maslov index for 2-level broken maps). Let (u, D) be a 2-level broken disc (or a
broken strip) with boundary on L (and on K). The Maslov index µ(u) is defined to be the Maslov
index of a T-gluing uT . Since the homotopy type of the glued map does not depend on the gluing
parameter T, the Maslov index for 2-level broken maps is well-defined.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
64
Lemma 6.25. Any regular broken strip u has Maslov index at least 1. A regular rigid broken strip
has Maslov index 1.
Proof. From Theorem 4.24, we know that for a large gluing parameter T, there is a regular
holomorphic glued strip uT whose limit as T →∞is u. As uT is regular, the Maslov index is at
least one. Thus, Maslov index of u is at least one.
From Theorem 4.25, we know there is a large gluing parameter T such that gluing gives a bijection
between rigid broken strips and rigid unbroken strips. Thus, the gluing uT is rigid, hence Maslov
index is one.
□
Lemma 6.26. Any regular broken disc u has Maslov index at least 2. A regular rigid broken disc
with point constraint has Maslov index 2.
Proof. The broken disc analog can be proved by a similar gluing argument as done in the proof of
Theorem 6.25.
□
Theorem 6.27. Each disc component of the inside piece of a rigid broken strip (u, D) or a rigid
broken disc with point constraint is a elementary disc.
Proof. Since the Lagrangian pair is monotone, there is an upper limit of energy of rigid broken discs
and strips. From Remark 6.12 we see that the symplectic area of an inside disc increases as the
number of punctures increase. Similarly, we see that the symplectic area of an inside disc increases
if the Reeb chord length at any of the punctures increases. Assume we are doing a neck-stretching
around the boundary sphere of a Darboux ball of radius R. Thus, there is an upper limit ku > 0
such that any rigid broken strip or disc has Reeb chord asymptote of length at most kuπ
n .
Since the torus segment Tγ is exact, and the punctures map to Reeb orbits or chords, from the
Stokes’ theorem argument in Remark 6.12 we see that the symplectic area is a sum of contributions
from the punctures. Each boundary puncture contributes at least cR(π/n −|fγ(0) −fγ(1)|) > 0
area and each interior puncture contributes cRπ > 0 where cR depends continuously on the radius
R.
Assume that the inner piece of a rigid strip (u, D) has a disc u with more than one punctures.
Only one of the boundary punctures of u matches with a boundary puncture of the strip piece lying
outside. Denote the boundary puncture on the strip piece by p. We can replace u with a single
boundary punctured disc eu that matches with the Reeb chord limit of uout at p. Repeat this for
each multiple punctured disc inside, and forget some punctured spheres or discs on the outside to
obtain a broken strip eu. The total symplectic area of eu is less than that of u. Since the Lagrangians
L, K form a monotone pair, we know that there is a cx,y for each x, y ∈L ∩K such that there is an
action-index relation for any strip u from x to y,
Iω(u) = λIµ(u) + cx,y.
Thus, since eu has smaller area, it will have smaller Maslov index. We have that
µ(eu) < µ(u).
Since u is a rigid disc, from Lemma 6.25 we have that it’s Maslov index is one. Thus we have
µ(eu) < 1,
which contradicts that eu is regular. As we have fixed a regularization scheme which makes every
broken map of index at most one regular, we have a contradiction.
Thus, we know for any rigid strip u, every inner piece disc has exactly one puncture. From index
computation in Remark 5.4 we see that if the Reeb chord at boundary puncture is not of minimal
FLOER COHOMOLOGY AND HIGHER MUTATIONS
65
u
C
B
A
eu
A′
Figure 13. Creating eu by replacing the disc A with A′ and removing the outside
pieces B and C
length ( i.e., π/n), the dimension Min is larger than the dimension of the matching condition RC.
Thus, for non-minimal Reeb chords, there is a non-trivial kernel of the evaluation map
evin : Min →RC,
hence such configurations cannot arise in rigid broken strips. This ends the proof for rigid broken
strips. For rigid broken discs, exactly the same argument would work.
□
