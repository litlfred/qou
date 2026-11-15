---
doc_id: arxiv-2301.08311v4
doc_title: "FLOER COHOMOLOGY AND HIGHER MUTATIONS"
section_id: sec-003-4-constructing-moduli-space-of-broken-maps
section_title: "Constructing Moduli Space of Broken Maps"
section_number: 4
pages: 30-44
source_pdf: 2301.08311v4.pdf
source_sha256: 385139c69e18f5b0
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND HIGHER MUTATIONS — We extend the construction of higher mutation as introduced in [PT20] to local higher mutation, which is applicable to a larger class of monotone Lagrangians."
---
4. Constructing Moduli Space of Broken Maps
In this section, we describe the construction of moduli space of broken strips and broken discs
as zero sets of a Fredholm map between Banach manifolds. From this section on wards, we will
focus on the broken manifold obtained from performing a neck-stretching along the boundary of a
mutation neighborhood of a manifold M.
We recall the notation from Subsection 3.1 and the spaces which show up in the broken manifold
after stretching along the boundary of a mutation neighborhood. The contact hypersurface Z is
S2n−1 and the Legendrian Λ is diffeomorphic to a disjoint union of two n −1 dimensional tori. The
broken manifold (as defined in Subsection 3.1.3) produced by neck-stretching across the contact
sphere S2n−1 is the collection,
c
Min = Cn, R × S2n−1, . . . , c
Mout
The broken mutable Lagrangian is the collection,
bLin = Tγ, R × (T n−1
+
⊔T n−1
−
), . . . , bLout
where the curve γ is a cylindrical extension of the curve determining L in the mutation neighborhood.
The analysis for setting up moduli spaces of broken discs with boundary on Lagrangian that do
not meet the neck has already been developed in the literature, see e.g. [CW15]. In the situation
where the Lagrangian does not meet the neck, the puncture nodes in the broken maps occur only
in the interior. In this subsection, we will deal with the case of broken discs and strips where the
puncture nodes occur only on the boundary and refer the reader to [CW15] for the case of the
interior puncture nodes.
4.1. Constructing Map spaces. We describe a Banach manifold structure on a subspace of
continuous maps from punctured discs to Cn or Cn \ {0} with boundary lying on the torus-segment
Lagrangian. We aim to construct a Banach manifold such that any punctured holomorphic disc
with boundary on the relevant torus segments. We construct the space of maps by starting with
continuous maps that are trivial strips over Reeb chords near the punctures. Then we use geodesic
flow exponentiation to define open sets around the maps with trivial strips.
4.1.1. Continuous maps with strip-like ends. We begin by describing the cylindrical structure on
the domain near punctures. Let P be a finite set of points on the boundary of the unit disc, let ΣP
denote the punctured disc with punctures at P i.e. ΣP = D \ P. From now on, we assume that the
set of punctures P has l elements and is equal to {pi}l
i=0. We label each puncture with either + or
−. We fix holomorphic charts ϕ±
p on Up, a neighborhood of the puncture p, the sign ± is determined
by the label of the puncture p, such that for a large Mp > 0 we have the following biholomorphisms
ϕp,+ : Up \ {p} →[Mp, ∞) × [0, 1]
ϕp,−: Up \ {p} →(−∞, −Mp] × [0, 1],
and ϕp,± maps the boundary of Σ to R×{0, 1}.We can compose this chart map with the biholomorphic
map z 7→e∓2πz from the strip R × [0, 1] to the punctured upper half-space H \ {0} to get new charts
e∓2πϕ±
p , assume that these charts extend to charts from Up where p 7→0. The neighborhoods Up
under the coordinates ϕ±
p are hereafter called strip-like ends of Σ . We fix a volume form dΣ on Σ
that is equal to the translation invariant volume form dsdt on the strip-like ends.
We define a space of continuous maps that are equal to trivial strips near boundary punctures.
The set of continuous maps from Σ to Cn \ {0} ∼= R × S2n−1 that satisfies the Lagrangian boundary
condition on Tγ where γ is cylindrical path and restrict to trivial Reeb-strips,
uc (s, t) =

kπ
ns, cR(kt)

,
FLOER COHOMOLOGY AND HIGHER MUTATIONS
31
on the strip-like ends for non-zero integer k and Reeb chord cR on S2n−1 with boundary on the
Legendrian tori is denoted as Maps0(ΣP , Cn, Tγ) i.e.
Maps0(ΣP , Cn, Tγ) :=

u ∈C0(Σ, Cn, Tγ)

∃K, m, Ru > 0, cR a Reeb chord,
such that
u ◦ϕ−1
p,±(s, t) = Ke±mscR(±mt)
for |s| > Ru

.
We now define the weighted Sobolev space that we will use to define charts for our space of maps.
Let β ∈C∞(R) be a non-decreasing bump function that is equal to 1 on [1, ∞) and equal to 0 on
(−∞, 0]. First we describe a function κδ
Σ that we use to define weighted Sobolev norm.
κδ
Σ : Σ →R
κδ
Σ(z) = 0 for z ∈Σ \ ∪iUpi
κδ
Σ(ϕ−1
p (s, t)) = δβ(|s| −Mp) for p ∈P
Let gcyl be the cylindrical metric on Cn obtained from renormalizing the standard Riemannian
metric g0 i.e. gcyl = g0/r2. Let u ∈Maps0
strip(ΣP , Cn, Tγ), we define the δ weighted Sobolev space of
sections of TCn over u with boundary on TTγ and k, p regularity with kp > 2 using the cylindrical
metric gcyl as follows,
W k,p,δ(u∗TCn, ∂u∗TTγ) =

η ∈W k,p
loc (u∗TCn)

Z
(|η|p + |∇η|p+
. . . |∇kη|p)epκδ
Σ)dΣ < ∞,
η(z) ∈TTγ for z ∈∂Σ

.
where W k,p
loc denotes the set of sections of the bundle u∗TCn that under any trivialization of the
bundle u∗TCn is in the Sobolev space W k,p
loc and ∇refers to the weak derivative taken with respect
to the standard connection on TCn. We define the (k, p, δ) norm on sections as follows
∥η∥p
k,p,δ =
Z
(|η|p + |∇η|p + . . . |∇kη|p)epκδ
Σ)dΣ.
4.1.2. Choosing domain dependent metric. We will use geodesic exponentiation to obtain a sub-basis
for the topology on the subspace of maps. We now choose a metric to exponentiate along to construct
the sub-basis. See section 5.3 [Mau08] for an expansive treatment of domain-dependent metric in the
context of quilts. Let RM(Cn) be the space of metrics on Cn. For a map u ∈Maps0
strip(ΣP , Cn, Tγ)
choose R > 0 such that u(s, t) is cylindrical on all the strip-like ends and the image of [R, ∞) × [0, 1]
lies the cylindrical end Tγ \ BR(0) of the Lagrangian Tγ. Choose a metric gu on Cn that makes the
Lagrangian Tγ ∩BR+1(0) totally geodesic. We can choose such a metric from corollary 3.2 in [Abo12]
or by using Frauenfelder’s metric, see Lemma 4.3.4 [MS12]. Let gu
Σ be a domain dependent choice of
metrics that interpolates between the metric gu and standard cylindrical metric gcyl = g0/r2 where
r is the radial coordinate as follows
FLOER COHOMOLOGY AND HIGHER MUTATIONS
32
gu
Σ : Σ →RM(Cn)
gu
Σ(z) = gu for z ∈Σ \ ∪iUpi
gu
Σ(ϕ−1
p (s, t)) = (1 −β(|s| −Mp))gu + β(|s| −Mp)gcyl for p ∈P
For η ∈W k,p,δ(u∗TCn, ∂u∗TTγ) we can define the map expu(η) where we do point-wise geodesic
exponentiation with respect to the domain dependent metric gu
Σ
expu(η)(z) = expu(z),g(z)(η(z))
Notice that our choice of domain-dependent metric ensures that expu η is a map that preserves the
Lagrangian boundary condition expu η(∂Σ) ∈Tγ. This follows from the fact that on the cylindrical
end of Tγ, the Legendrian tori T+, T−are totally geodesic with the round metric on the sphere.
4.1.3. Constructing the set of W k,p,δ maps. We now describe the set of maps on which we will give
a Banach manifold structure. We define the map space Mapsk,p
δ (ΣP , Cn, Tγ) from which we cut out
the moduli space of parameterized holomorphic maps as follows
Mapsk,p
δ (ΣP , Cn, Tγ) :=

expu0(X)

 u0 ∈Maps0
strip(ΣP , Cn, Tγ),
X ∈W k,p,δ(u0∗TCn, ∂u0∗TTγ)

.
We show that any finite Hofer energy punctured holomorphic disc with correct boundary conditions
lie in the space of maps we defined above. Let u be a holomorphic map on the domain Σ to Cn
with boundary lying on the torus segment Tγ which has finite Hofer energy EH(u) < ∞. We
have exponential convergence (of decay rate at least e−πs/n) to trivial Reeb strips on its strip-like
ends from Theorem 3.5. Thus, for some u0 ∈Maps0
strip(ΣP , Cn, Tγ), we have u = expu0(η) for
some η ∈W k,p,δ(u∗TCn, ∂u∗TTγ) where the geodesic exponentiation is done based on the domain
dependent metric gu0
Σ and δ < π
n. This proves that any finite Hofer energy punctured disc u can be
written as a geodesic exponentiation of a W k,p,δ vector field on a map u0 ∈Maps0
strip(ΣP , Cn, Tγ).
4.1.4. Banach structure on Mapsk,p
δ (ΣP , Cn, Tγ). Now we will describe a Banach manifold structure
on the space of maps by prescribing a generating set for an atlas. Let V be the space generated by
the n −1 independent vector fields Xi on Cn where
Xk(z1, . . . , zn) = (0, . . . , 0, izk, 0, . . . , −izn).
Let H be the one dimensional space generated by the radial vector field Xrad on Cn where β is the
bump function we chose before and R > 0 such that Tγ \ BR(0) is cylindrical.
Xrad(z) = β(|z|/R)z
We can check that all the sections of V ⊕H restrict to vector fields on Tγ under the restriction of
the sections to Tγ. Given a puncture p and a map u ∈Mapsk,p
δ (ΣP , Cn, Tγ), for any v ∈V , h ∈H
we can define vu,p, hu,p to be sections on u∗TCn which are equal to v, h in the strip-like end at p
and extended to Σ by a bump function so that vu,p, hu,p = 0 on Σ \ Up
We describe charts on the space of maps now. The Banach charts on Mapsk,p
δ (ΣP , Cn, Tγ) at
u0 ∈Maps0
strip(ΣP , Cn, Tγ) are given by geodesic exponentiation
FLOER COHOMOLOGY AND HIGHER MUTATIONS
33
(4.1.1)
expu0 : W k,p,δ(u0∗TCn, ∂u0∗TTγ) ⊕V |P| ⊕H|P| →Mapsk,p
δ (ΣP , Cn, Tγ)
expu0(w, v1, . . . , vl, h1, . . . , hl) = expu0(w +
l
X
i=1
(vi,u0,pi + hi,u0,pi))
Since the choice of domain dependent metric differ only on compact sets, the transition func-
tions expu0 ◦exp−1
u1 are maps between the corresponding Banach tangent spaces at u0, u1 ∈
Maps0
strip(ΣP , Cn, Tγ). Following the traditional notation in treatments of J−holomorphic maps,
we denote Mapsk,p
δ (ΣP , Cn, Tγ) as B when we want to view it as a Banach manifold.
We describe a Banach bundle over the space of maps, and show that the space of holomorphic
maps can be viewed as the zero locus of a certain section of the bundle. Define a Banach vector
bundle E over B as follows
E =
[
u∈B
W k−1,p,δ(Hom(TΣ, u∗TCn))
where W k−1,p,δ(Hom(TΣ, u∗TCn)) is the space of (0, 1) forms on Σ with finite weighted norm as
before,
∥η∥p
k−1,p,δ =
Z
(|η|p + |∇η|p + . . . |∇k−1η|p)epκδ
Σ)dΣ.
The almost complex structure J is chosen such that in the cylindrical ends (ie. away from a
compact domain) J = J0 where J0 is the standard complex structure on Cn. The moduli space of
J-holomorphic punctured discs is then given by the zero set of the Cauchy-Riemann F section.
F : B →E,
u 7→∂J(u)
The moduli space of parameterized punctured discs f
MΣ can be described as F−1(0) and the
unparameterized moduli space MΣ is the quotient f
MΣ/Aut(Σ). Note that the automorphism
group of Σ can be atmost 2 dimensional and the infinitesimal action of it on g
MΣ lies in the Banach
tangent space.
4.1.5. Space of Reeb chords and evaluation at puncture. From Section 3 we know the asymptotic
behavior near a puncture of a holomorphic map with finite Hofer energy is modelled on a Reeb
chords or orbit. Thus, one can define an evaluation map at the punctures, taking values in the
space of Reeb chords or orbits. We denote the space of Reeb chords in Z with boundary on Λ by
RC(Z, Λ). In our situation where the Reeb field is generated by a free S1 action on Z, the space
RC can be easily described in terms of the length of the Reeb chord and starting point of the Reeb
chord. Note that the length of the Reeb chord has to be an integer multiple of π/n and the starting
point has to lie on either of the two T n−1 in Λ, thus
RC =
(lπ
n , w


l ∈N, w ∈Λ
)
.
We can define evaluation at puncture p ∈P from the moduli space of parameterized holomorphic
discs to S2n−1 that maps the holomorphic map u which is asymptotic to the Reeb chord ζ at the
puncture to the starting point ζ(0) of the Reeb chord.
evp : f
MΣ →RC,
evp(u) = (kπ/n, ζp(0))
FLOER COHOMOLOGY AND HIGHER MUTATIONS
34
Here ζp is the Reeb chord of length kπ/n such that u is asymptotic to the trivial strip over ζp at
the strip-like end at p. We can also define an evaluation map on the charts of the Banach space of
maps B as given in (4.1.1) as follows
EVp : W k,p,δ(u0∗TCn, ∂u0∗TTγ) ⊕V |P| ⊕H|P| →V
EVp(w, v1, . . . , vp, . . . , vl, h1, . . . , hp, . . . , hl) = (vp).
Remark 4.1. We can similarly define a space Mapsk,p
δ (ΣP , R × Z, R × Λ) for cylindrical manifolds
and Mapsk,p
δ (ΣP , c
W, bL) for manifolds with cylindrical ends over contact hypersurface.
4.2. Linearization of Cauchy-Riemann map and Fredholmness. In this subsection we show
that the Cauchy-Riemann section is a Fredholm map near zeroes of the section . More precise, we
show that the vertical derivative at the points where the section F vanishes is a Fredholm map
of Banach spaces. One can linearize F at a holomorphic map u as usual in the classical case by
choosing a connection on E induced from a connection ( cylindrical in our case ) on Cn. We assume
that the punctures are non-removable ie. the punctures go to Reeb chords. Since we have already
established exponential convergence to Reeb-strips, we first obtain an expression for linearization
for trivial Reeb strip, uγ where γ is a Reeb chord in S2n−1. This will be an analog of Proposition
6.24 in [Wen16].
Before we begin stating the result, we will define some terms so that it is consistent with Wendl’s
proposition. Wendl deals with a cylindrical manifold R × Z with framed Hamiltonian structure
(ω, λ). In our case, the cylindrical manifold is obtained by setting M = S2n−1 and the Hamiltonian
structure is given the standard contact form λ = λ0 on the sphere, where ξ is the contact structure.
The Reeb field on M is denoted by R. T(R × Z) is split into direct sum of two bundles, ϵ ⊕ξ where
ϵ is generated by R and TR. Λ denotes the two disjoint Legendrian tori, which gives the boundary
condition. One can define an asymptotic operator associated to Reeb chords with boundary on
Λ similar to asymptotics associated to Reeb orbits. For Reeb orbits of period T, the asymptotic
operator Aγ was given by the hessian of the action functional Aω on the space of loops in M, see
section 6.1.1 page 149 in [Wen16] . In the case of Reeb chords, T denotes the ‘length’ of the Reeb
chords, i.e.
R
γ∗λ . The connection ∇is chosen to be the Levi-Civita connection induced from the
round metric on the sphere. We define Aγ : Γ(γ∗ξ, Tγ(0)Λ, Tγ(1)Λ) →Γ(γ∗ξ) as follows
Aγ(η) = −J(∇tη −T∇ηR).
We can ignore the projection πξ as we are working with a contact hypersurface instead of stable
Hamiltonian structure.
Lemma 4.2 (Analog of Wendl’s 6.24 [Wen16]). The J-holomorphic trivial strip uγ : R×[0, 1] →R×Z
for a Reeb chord γ of length T with boundary on R × Λ has linearized Cauchy-Riemann operator
Duγ : Γ(u∗
γϵ ⊕u∗
γξ, ∂u∗
γTR ⊕∂u∗
γTΛ) →Ω0,1(R × [0, 1], u∗
γϵ ⊕u∗
γξ) given by
(Duγη)∂s = ∂sη +

i∂t
0
0
−Aγ

η.
Proof. Wendl’s proof by splitting Duγ into blocks given by the splitting ϵ ⊕ξ works the same almost
verbatim. The main difference is the boundary condition. Define the contact action functional
for chords with boundary on Legendrian Λ by Aλ(γ) =
R
γ∗λ. We can check that the Hessian
of this action functional, computed at a Reeb chord γ with respect to ∇, is −J(∇tη −T∇ηR)
where T is the length of γ. The only change from Wendl’s proof is that we are dealing with chords
instead of orbits, so anytime an integration by parts is used one might encounter boundary terms
λ(η(1)) −λ(η(0)) but they vanish since η(0), η(1) lie on TΛ ,→ker λ.
□
FLOER COHOMOLOGY AND HIGHER MUTATIONS
35
Consider the Banach space isomorphisms E : W k,p,δ →W k,p given by f 7→eδsf. We have a
slight abuse of notation here since E is a map from W 1,p,δ(u∗
γT(R × Z), ∂u∗
γT(R × Λ)) and of
Ω0,1
δ (u∗
γT(R × Z)). With this notation, we have
EDuγE−1 = ∂s +

i∂t + δ
0
0
−Aγ + δ

.
Lemma 4.3. For any δ < π
n, we have that EDuγE−1 is an operator of form ∂s + A on the space of
Sobolev sections W 1,p where A is a non-degenerate operator.
Proof. Note that the eigenvalues of

i∂t
0
0
−Aγ

are given by eigenvalue of i∂t and Aγ. The eigenvalue
of Aγ can be explicitly computed to be πZ, notice since we are dealing with a Morse-Bott situation,
0 is actually an eigenvalue. Note that Aγ = −J ˆ∇t where ˆ∇is the unique symplectic connection for
which parallel transport is the linearized Reeb flow , (see [Wen16] ), we have that eigenfunction
for eigenvalue λe is given by η(t) = (ϕt)∗(eiλetη(0)) where ϕ is the Reeb flow. Thus, to satisfy the
boundary conditions we need λe ∈πZ. The eigenvalues for i∂t are a subset of π
nZ since the smallest
θ such that eiθΛ ,→Λ is π
n. Thus, if we choose δ in the given range, we’d have EDuγE−1 = ∂s + A
where A is non-degenerate.
□
4.2.1. Trivialization. We explain the choice of trivialization of bundles we make to simplify the
linearization. We need a suitable trivialization under which Du is equal to ∂s + J0∂t + A. We state
a version of Lemma 2.13 in [Sch16] to create a family of trivialization, we leave the proof to the
reader since it follows the idea in [Sch16] very closely.
Lemma 4.4. For any p ∈LY and R > 0, there is an open set V in Y such that the tangent bundle
of U = π−1
Y (V ) has the following trivialization
Φ : [R, ∞) × [0, 1] × U × R2n →T(R × Z)|U,
(s, t, q, v) 7→Φs,t(q)v ∈Tq(R × Z)
that satisfies the following
• Js,t(q)Φs,t(q) = Φs,tJ0,
• gcyl(Φs,t(q)ξ, Φs,t(q)ξ′) = g0(ξ, ξ′),
• Tq(R × Λ) = ϕs,k(Rn ⊕{0}) for all q ∈R × Λ ∩U and k = 0, 1,
where J0, g0 are the standard complex structure and metric on R2n.
Recall when B is a subbundle of A and D is a subbundle of C, then by an isomorphism F of the
pair of bundles F : (A, B) →(C, D) refers to an isomorphism F : A →C such that its restriction
to B is an isomorphism to D. Let’s assume that πY ◦u converges to the point p ∈LY ⊂Y as
s →∞and choose a trivialization Φ as in Lemma 4.4. Using this trivialization, we get the following
trivialization of the pair of bundles over the half-strip [R, ∞) × [0, 1].
eΦ : (u∗T(R × Z), ∂u∗T(R × Λ)|[R,∞)×[0,1]) →([R, ∞) × [0, 1] × R2n,
(4.2.1)
[R, ∞) × {0, 1} × (Rn ⊕{0}))
4.2.2. Semi-Fredholmness by local estimates on cylindrical ends. We call a linear map semi-fredholm
if it has closed image and finite dimensional cokernel. In this subsection, we will show that the
linearization of the Cauchy-Riemann section is semi-fredholm by combining local estimates.
We will use the following classic lemma to prove that Du is Fredholm. This has been proved in
numerous textbooks and classical references, e.g., see Lemma A.1.1 in [MS12].
FLOER COHOMOLOGY AND HIGHER MUTATIONS
36
Lemma 4.5. If K is a compact operator, T is a bounded operator, and c > 0 such that
|x| ≤c(|Tx| + |Kx|)
then T is semi-fredholm.
If the domain surface Σ were compact, by standard methods in [MS12] one has
|x|W 1,p(Σ) ≤c(|Dux|Lp(Σ) + |x|Lp(Σ)),
and by the Rellich-Kondrachov compact embedding, we have that the inclusion of W 1,p(Σ) ,→Lp(Σ)
is compact for a compact surface Σ with smooth boundary. The argument goes as follows, from
Proposition B.4.9 in [MS12] we have a local estimate, which is then patched together for a finite
covering of the compact space. This argument is outlined in Proposition C.2.1 in the book.
The above approach will not directly work when the domain is non-compact. We will show a
stronger inequality in the cylindrical setting to avoid the use of Rellich-Kondrachov theorem. We
will use the approach in [Wen16] to show a similar inequality for a compact subdomain away from
the strips and on the strips we will show there is an inequality (see Lemma 4.18 in [Wen16])
(∗)
||x||W 1,p(R×[0,1]) ≤c||Dux||Lp(R×[0,1]).
We will use the above estimate while patching local estimates on the whole domain. From
exponential convergence we have that u converges to uγ on a strip-like end of Σ for some Reeb
chord γ, thus it is enough to prove (∗) for uγ. To verify this, notice trivialization of u∗
γT(R × Z)
and u∗T(R × Z) as given in equation (4.2.1) is exponentially close to each other that contributes
to an exponentially decaying 0th order term. Now we use the fact that for δ > 0, the inclusion
W k,p,δ →W k−1,p is a compact operator and thus the difference is a compact operator.
Lemma 4.6. Let D = ∂s + A(t) be an operator of functions over the strip such that A is an
unbounded self-adjoint and non-degenerate operator on W 1,p([0, 1], Cn, Rn−1 × λeR+, Rn−1 × R+),
the Sobolev space of functions from [0, 1] to Cn with given boundary conditions.Then
D : W 1,p(R × [0, 1], Cn, Rn−1 × λeR+, Rn−1 × R+) →Lp(R × [0, 1], Cn)
is an isomorphism. Here λe = ekπ/n for some k.
Proof. This lemma is a version of Proposition 8.7.3 in [ADE14], Lemma 2.4 in [Sal99].
The
proof runs the same, except the fact in the special case of p = 2 we’d need to use density of
W 1,p(Cn, Rn−1 × λR+, Rn−1 × R+) inside L2(Cn). To verify the density, one can check that C3
maps from [0, 1] to Cn with the boundary conditions on the given subspaces is dense in C3([0, 1], Cn)
with L2 metric. Clearly we have that C3([0, 1], Cn) is a subspace of W 1,p, thus density of smooth
functions in L2 gives us that W 1,p(Cn, Rn−1 × λR+, Rn−1 × R+) is dense inside L2(Cn). The other
steps in the proof of the lemma run exactly the same as that given in the references.
□
Corollary 4.7. If u is a holomorphic strip R × [0, 1] →R × Z that exponentially converges to a
trivial Reeb strip uγ (i.e., satisfies equation (3.2.1)), we have that for all δ < π
n there exists a c > 0
such that
||x||W 1,p,δ(R×[0,1]) ≤c||Dux||Lp,δ(R×[0,1]).
Proof. Note that since we have exponential convergence, it is enough to check for Duγ. We know
uγ(s, t) = e
kπ
n (s+it)(x1, . . . , xn) for some xi ∈C such that x1.x2. . . . xn ∈R̸=0. Thus, we see that we
can choose a trivialization of u∗
γTCn such that we get the boundary conditions as in Lemma 4.6.
Now letting D′ = EDuγE−1, from Lemma 4.3 we have that D′ fits the hypothesis in Lemma 4.6.
The fact that D′ is an isomorphism gives us the inequality
||η||W 1,p ≤c||D′η||Lp.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
37
Since E is a Banach isomorphism from the weighted to unweighted Sobolev spaces, we have
||η||W 1,p,δ ≤c||Duγη||Lp,δ,
for a possibly different c.
□
Theorem 4.8. Du : TuB →Eu is semi-fredholm when δ < π
n.
Proof. Define E similar to as 4.3, but now on the whole Σ by choosing a function f : Σ →R that is
equal to δs on the strip-like ends and zero away from them. This defines Banach isomorphism
(4.2.2)
E : W k,p,δ(u∗TCn) →W k,p(u∗TCn)
η 7→efη.
As E is a Banach isomorphism, it is enough to show D′ := EDuE−1 is semi-fredholm.
We will use Lemma 4.5 to claim semi-fredholmness. We can cover Σ by finitely many charts away
from the punctures, call the union of the charts Σo and use Proposition B.4.9 (ii) in [MS12] to get
an estimate
||η|| ≤c(||η||W 0,p(Σo)|| + ||Du(η)||W 0,p(Σo))
∀η ∈W 1,p
0 ((Σo)).
This gives us an estimate for D′ as on Σo for a possibly different c, E is just multiplying by a
bounded function.
(*)
||η|| ≤c(||η||W 0,p(Σo)|| + ||D′(η)||W 0,p(Σo))
∀η ∈W 1,p
0 ((Σo)).
We can assume that the strip-like ends in Σ \ Σo under the fixed chart is biholomorphic to
[R + 1, ∞) × [0, 1] for some fixed R > 0. For each puncture q, let Zq
R be the strip neighborhood
[R, ∞) × [0, 1] under the fixed charts. From Corollary 4.7 and Lemma 4.3 we see that
(**)
||η||W 1,p(R×[0,1]) ≤c′
q||D′η||Lp(R×[0,1])
∀η ∈W 1,p
0 (Zq
R).
Here we extend η by 0 over the whole strip before using Corollary 4.7. Now a standard argument
of using bump function β that is supported on Σo, for any η ∈W 1,p(u∗T(R × Z)), we can use βη
and (1 −β)η in inequalities (*) and (**) to get
||η||W 1,p(Σ) ≤C(||D′(η)||W 0,p(Σ) + ||η||W 1,p(Σo)).
Since closure of Σo in Σ is compact with smooth boundary, we have that W 1,p(Σo) ,→W 0,p(Σo) is
a compact inclusion, thus the restriction on η 7→η|Σo is a compact operator. Thus, from 4.5 we
have that D′ is semi-fredholm, thus Du is semi-fredholm for the given choice of δ
□
4.2.3. Fredholmness. In this subsection, we will use a similar argument as in subsection 4.2.2 to the
adjoint of the linearization and show that the linearization is a Fredholm operator. To show that Du
is Fredholm, it is enough to show D′ = EDuE−1 is Fredholm where E is from equation (4.2.2). We
use a Hermitian structure hcyl = gcyl( , ) −igcyl( , J ) on TCn induced from the cylindrical metric
gcyl to define a formal adjoint D′∗and show that D′∗is semi-Fredholm. This idea has been widely
used in literature to prove Fredholmness of Cauchy-Riemann operators coming out of linearizations,
see [Wen16], [MS12] . We define C0,Tγ(Hom(TΣ, u∗TCn)) as follows
FLOER COHOMOLOGY AND HIGHER MUTATIONS
38
C0,Tγ(Hom(TΣ, u∗TCn)) =

α ∈Γ(Hom(TΣ, u∗TCn))

α(T∂Σ) ⊂∂u∗TTγ,
α has compact support

.
We use a Hermitian metric to define an adjoint of the linearization. The Hermitian structure hcyl
induces an L2 pairing on the space of sections Γ(u∗TCn, ∂u∗TCn) and Γ(Hom(TΣ, u∗TCn)) given
by the following integral,
⟨η, ξ⟩:= Re
Z
Σ
⟨η, ξ⟩dΣ.
The formal adjoint D′∗is defined as the unique operator on the Sobolev completion W k,p
Tγ (u∗Hom(TΣ, u∗TCn))
that satisfies
⟨D′α, β⟩= ⟨α, D′∗β⟩for all α ∈Γ0(u∗TCn, ∂u∗TCn),
β ∈C0,Tγ(Hom(TΣ, u∗TCn)).
Remark 4.9. Another approach of defining the formal adjoint D∗
u is to define it on the space
W k,p,−δ
Tγ
(Hom(TΣ, u∗TCn)), where we use a negative Sobolev weight. We can define isomorphism
E′ similar to E, but with negative weight such that E′D∗
uE′−1 = D′∗.
We can follow the same proof as in Proposition 4.32 in [Wen16] to get the following lemma about
D∗
u which finishes the proof of Fredholmness.
Lemma 4.10. D′∗is semi-Fredholm and we have the following isomorphisms coker D′ = ker D′∗,
coker D′∗= ker D′.
As a corollary of the previous lemma, we have the following theorem
Theorem 4.11. The linearization Du of ∂at any holomorphic map u is a Fredholm operator.
4.3. Domain dependent almost complex structure on the outside. In practice, attaining
regularity is not possible without allowing some perturbation of the almost complex structure. We
see in Section 5 that one can achieve regularity for the inside and neck pieces for the standard almost
complex structure J0 in Cn, but we need to allow perturbations of the outside piece to achieve
regularity of the broken discs and strips. We use the perturbation scheme of domain dependent
almost complex structures as initially done in [CM07] for the closed case and later generalized to
the open case with boundary on Lagrangian in [CW17],[CW15].
Notice that we can identify c
Mout with M \ {p} where p is the center of the Darboux ball whose
boundary we do the neck-stretching along. In this identification, bLout corresponds to the Lagrangian
Tγ obtained by the path γ(t) = t for t ∈(−ϵ, ϵ) \ {0} in the Darboux chart. The closure of bLout is
denoted by Lsing, it is locally a conical manifold, a double cone over the torus T n−1 given by T(−ϵ,ϵ).
We need to stabilize the components in the outside domain that have boundary lying on Lout so that
we can use domain dependent perturbation on these components. We follow the scheme of obtaining
marking by intersection with a divisor similar to [CM07] ,[CW17],[CW15]. The treatment of domain
dependent perturbations presented here assumes some familiarity with the idea of coherent choice
of perturbation datum for Lagrangian intersection Floer theory as done in [CW17].
FLOER COHOMOLOGY AND HIGHER MUTATIONS
39
Definition 4.12 (Nice divisor adapted to J). Given a pair of transversely intersecting Lagrangians
L, K of M such that L is locally mutable, a submanifold D of codimension two that doesn’t intersect
L ∪K ∪Lsing is called a “ nice divisor” if M \ D is exact symplectic manifold and Lsing is exact
Lagrangian in M \ D. A nice divisor is called “adapted” to a complex structure J if the tangent
bundle TD is preserved by J.
Remark 4.13. In Pn, if we take L to be the Clifford torus, then there is a nice divisor D adapted
to the standard J0. We can take two fibers of the map πm in some standard affine chart of Pn and
perturb them to obtain a smooth divisor in Pn that makes L exact in the complement.
From now on, we assume the existence of a nice divisor. If u is a non-constant holomorphic map
in the outside piece with boundary on Lout, then it must intersect D as otherwise exactness of Lsing
would imply symplectic area of u is 0.
Definition 4.14 (Stabilizing combinatorial type of broken strip). Given combinatorial type Γ of
a broken strip where each outside piece stable, we define the stabilized type Γst by forgetting all
the inner and neck pieces that are not stable along with the puncture nodes that connected the
unstable piece to a stable piece. If removing such a puncture node renders an otherwise stable piece
into an unstable piece, we forget that as well in Γst.
We will now define the notion of domain dependent perturbation of almost complex structure.
Let k ≥1 be natural number, we define Mk to be the moduli space of nodal strips with k interior
markings and Uk
eπk
−→Mk is the universal moduli space whose fiber over S ∈Mk is the set by pairs
(S, z) where z is a point on S. Fix an almost complex structure Jfix on c
Mout that is equal to the
cylindrical almost complex structure J0 on the cylindrical end. We denote Jcyl(c
Mout, ω, D) to be
the set of almost complex structures satisfying the following,
(1) compatible with the symplectic form ω on c
Mout,
(2) equal to J0 in the cylindrical end of c
Mout,
(3) D is adapted to it.
Definition 4.15 (Domain dependent almost complex structure for broken strips ). A domain
dependent almost complex structure of a strip with k interior markings is a smooth map Jk : Uk →
Jcyl(c
Mout, ω, D) such that near the puncture nodes, the almost complex structure is equal to Jfix,
i.e., there is an open neighborhood U in Uk near the locus of puncture nodes such that Jk(w) = Jfix
for w ∈U .
Now we describe glued domain dependent almost complex structures. Given a domain dependent
almost complex structure on a stabilized combinatorial type of broken strip Γst such that near the
puncture nodes Jk is equal to Jfix, we can get a domain dependent almost complex structure on
the unbroken T-stretched manifold MT by gluing Γst at the puncture nodes. A T−gluing across
a puncture node, where T > 0 is a parameter measuring the “length of the neck”, is obtained
by identifying truncated neighborhoods (deleting (T, ∞) from positive end and (−∞, −T) from
negative end) of the strip/cylinder coordinate near both sides of the puncture node.
We explain the gluing construction more precisely in the case where there is only one puncture
node, the general construction is done similarly. Fix a parameter T > 0. For now, assume Γst
has only one puncture node. Let Γst
gl be the combinatorial type obtained from gluing Γst across a
puncture node. Thus, the moduli space of strips MΓst of type Γst is a lower dimensional stratum
in the compactified moduli space MΓst
gl. We can choose a chart of MΓst
gl near the strata MΓst by
first choosing strip-like parameterization of the surfaces near the puncture node and then gluing
the strips. Let [s] ∈MΓst, and C[s] be the surface corresponding to [s], let p be the puncture node
FLOER COHOMOLOGY AND HIGHER MUTATIONS
40
lying between the components C−, C+ of C[s]. Let U± be neighborhoods of p in C± such that we
can choose charts ϕ± on them as follows,
ϕ−: U−→(−∞, 0] × [0, 1]
ϕ+ : U+ →[0, ∞) × [0, 1].
We obtain the T-glued domain CT
[s] by removing ϕ−((−∞, −T) × [0, 1]) and ϕ+((T, ∞) × [0, 1]) from
the components C± of C[s] and gluing the remnant surfaces by the relation (s, t) ∼(s + T, t).
We now explain how to glue domain dependent almost complex structure. Since Jk is equal to
Jfix near the locus of the puncture node, we can choose a strip-like neighborhood U± as above, so
that Jk restricted to U± is equal Jfix. Recall that we do not perturb the almost complex structure
on the inside piece. We define a T-glued domain dependent almost complex structure JT
k on the
T-glued domain CT
[s],by defining JT
k (z) to be equal to the T-stretched almost complex structure in
the JT neck region for all z and for z ∈the neck region of the domain, define Jk(z) to be equal to
Jfix on the outside piece of MT .
JT
k (z)(m) =





Jin
if m ∈Min
J0
if m ∈[−T × T] × Z
Jk(z)(m)
if m ∈Mout
Definition 4.16 (Coherent families of perturbation data for broken strips). We call the set
P = {Jk}∞
k=0 where in the k = 0 case we choose a t−dependent complex structure, and for
k ≥1, Jk is a domain dependent almost complex structure for broken strips, a coherent family of
perturbation data if the T−glued domain dependent almost complex structure forms a coherent
family of perturbation for MT as in Definition 3.14 in [CW17] for any T > 0.
We explain the notion of being holomorphic with respect to a domain dependent choice of almost
complex structure. A map u : Sz →c
Mout from a k marked strip Sz = eπ−1
k ([z]) where [z] ∈Mk is
called holomorphic with respect to the domain dependent almost complex structure J if it satisfies
the domain-dependent version of the Cauchy Riemann equation
du(z) + Jk(z, (u(z))) ◦du ◦jS = 0.
We show that the expected dimension of moduli space of holomorphic maps with respect to
domain-dependent choice almost complex structure is equal to domain independent almost complex
structure if we add divisor constraints on the marked point. Recall, for a fixed complex structure,
the expected dimension of the moduli space of discs or strips at a point u depended solely on
the topological data of u. We show that the same formula can be applied to the moduli space of
holomorphic broken strips with respect to a domain-dependent perturbation, with the constraint of
interior markings mapping to a nice divisor D. Denote the expected dimension of the moduli space
at a point u that is of homology class A by vir(A). Given a (relative) homology class A, the expected
dimension of Mdd
k (c
Mout) at any element u that is of the homology class A is vir([A]) + dim(Mk). If
we require the interior markings to map to D to create a constrained moduli space Mk(Mout, D), the
expected dimension of Mk(Mout, D) at u of homology class A is vir(A) + dim(Mk) −2k = vir(A).
We introduce some notations regarding domain-dependent almost complex structures.
We
denote the space of coherent perturbation datum P(c
Mout, D). We denote the moduli space of Jk
holomorphic maps by Mdd
k (c
Mout) and the moduli space of broken strips or broken disc with point
constraint with respect to a coherent perturbation data P with the constraint of interior markings
going to a nice divisor D as MBr,P(M[l], L[l], K, D) and MBr,P(M[l], L[l], p, D). In Subsection 5.3
FLOER COHOMOLOGY AND HIGHER MUTATIONS
41
we prove that there is a choice of a coherent perturbation datum that makes every rigid broken
strip and rigid broken strip with point constraint regular.
4.4. Moduli space of broken strips and discs. Now that we have dealt with the analysis of the
space of maps and Fredholmness of the Cauchy-Riemann section, we will now describe the moduli
space of broken discs and strips. In this subsection, we will explain how the moduli space of broken
strips and discs can be cut out as a zero set of a section similar to moduli space of holomorphic
discs. Let D = (Din, D1, . . . , Dout) denote a nodal disk or strip with l levels as in Definition 3.3. We
denote the set of nodes between two components of different label as P and for all p ∈P, we use
p± to view p as an element in the two different components. The moduli space of broken strips
with domain D to the broken manifold M[l] with boundary on the broken Lagrangian L[l] and
some boundary components of Dout mapping to the compact Lagrangian K in Mout is denoted by
MBr(D, M[l], L[l], K) and the moduli space of broken discs is denoted by MBr(D, M[l], L[l]).
Assume Γst is the stabilized combinatorial type of the domain, see Definition 4.14. Let C denote
the nodal surface D regarded as a smooth surface with nodes. Let Ci denote the surface in ith piece
of the domain, Di, regarded as a smooth manifold with nodes and let
(4.4.1)
UΓst
i ,l →MΓst
i ,l × Ci
be a collection of trivializations, indexed by l, of the universal moduli space of Riemann surfaces of
type Γ. These trivializations induce a family of complex structures on the fibers of the universal
space
(4.4.2)
MΓst
i ,l →J (Ci),
m →j(m).
Let Ei denote the bundle of (0, 1) forms over the space Mapsk,p
δ (Σi, Mi, R × Λ), i.e. the fiber Ei over
a map ui is
Ei,u := W k,p
δ
(Hom(TΣi, u∗
i TMi)).
In the equation below, the notation MΓ stands for a choice of a complex structure on the domain
C induced from the choice of trivializations we made in equations (4.4.1) and (4.4.2). We can define
the following map by setting it to ∂j(m),Ji on each component
∂
strip
Br
: MΓst × Mapsk,p
δ (Σin, Cn, Tγ) × Mapsk,p
δ (Σ1, R × S2n−1, R × Λ)
× . . . Mapsk,p
δ (Σout, c
Mout, Lout, K) →Ein × . . . Eout.
Note that the linearization of ∂Br is a Fredholm operator because we know that linearization of ∂is
Fredholm from Theorem 4.11 and MΓ is finite dimensional. The set ∂
−1
Br(0) consists of holomorphic
maps from a broken domain D of combinatorial type Γ with the correct Lagrangian boundary
condition but at the nodes between two levels, the maps might not match up correctly ie. they might
be asymptotic to different Reeb chords. Recall that we have an evaluation map at each puncture to
the space of Reeb chords RC, we collect such evaluation maps to create a “big evaluation map”
evbig : ∂
strip
Br
−1(0) →(RC−× RC+)|P|.
The space ev−1
big(∆|P|) where ∆is the diagonal manifold in RC−× RC+ is precisely the moduli space
MBr(Γ, M[l], L[l], K). The linearization of evbig is obtained by collecting EV−× EV+ for each node
between two levels.
Similar to broken strips, we can obtain the moduli space of broken discs as a fiber product
obtained from a zero section. The only modification we need to do is define the following ∂section :
FLOER COHOMOLOGY AND HIGHER MUTATIONS
42
∂
disc
Br : MΓ × Mapsk,p
δ (Σin, Cn, Tγ) × Mapsk,p
δ (Σ1, R × S2n−1, R × Λ)
× . . . Mapsk,p
δ (Σout, c
Mout, Lout) →Ein × . . . Eout
where Eout is the obvious bundle of (0, 1)-forms over the space Mapsk,p
δ (Σout, c
Mout, Lout).
We collect some definitions below. In all the following definitions, we work with a fixed combi-
natorial type Γ and the domains are allowed to vary only in the strata of the associahedra of the
moduli of domains determined by the type Γ.
Definition 4.17 (Regular broken strip). We call a broken strip u ∈MBr(Γ, M[l], L[l], K) regular
if the linearizations of ∂Br is surjective at u and the evaluation map, evbig, is transverse to the
diagonal ∆|P|.
Assuming transversality of everything, the expected dimension of the moduli spaces MBr(Γ, M[l], L[l], K)
and MBr(Γ, M[l], L[l]) at a point u is Ind( eDu) −|P|(n −1) where eDu is the linearization of ∂
strip
Br
or ∂
disc
Br at (D, u).
Definition 4.18 (Virtual dimension). For a broken strip or a disc (u, D), the virtual dimension is
given by the formula
vir(u) = Ind( eDu) −|P|(n −1) −dim aut(D).
Definition 4.19 (Rigid broken strip). We call a broken strip u rigid if vir(u) = 0. The moduli
space of rigid strips is denoted as MBr(Γ, M[l], L[l], K)0.
Definition 4.20 (High-index broken strip). We call a broken strip u high-index if vir(u) > 0.
In the unbroken compact case, the moduli space Maslov 2 discs with a boundary constraint of
passing through a fixed point is of expected dimension 0 and contributes to the disc potential. We
define a notion of point constrained broken disc so that we can later compare counts of Maslov two
discs passing through a point of the unbroken Lagrangian L with the broken Lagrangian L. Given
a point p ∈Lin that is not in the cylindrical part of the Lagrangian Lin, we define the notion of
broken disc with point constraint, the choice of p is not relevant since L is assumed to be connected.
Definition 4.21 (Broken disc with point constraint). Let q be a boundary marking on one of the
interior pieces of D which gives us an evaluation map evq with values in Lin. The moduli space of
broken discs with point constraint, MBr(M[l], L[l], p) is defined as the space ev−1
q (p).
The expected dimension of the point constrained moduli space at a broken disc (u, D) is vir(u) −n.
Definition 4.22. We say a broken disc with point constraint is rigid if vir(u) = n.
Definition 4.23 (Compactified energy). For a two-level broken strip (u, D) = ((uin, uout), D). The
compactified energy Ec(u) is defined as
Ec(u) = E(uin) + E(uout)
where uin, uout are compactifications obtained by extending the maps to the compactified targets
Min, Mout obtained by symplectic cutting.
4.5. Gluing broken things. In this section, we will discuss how to obtain unbroken maps from
broken discs and strip. Given a broken strip or disc (u, D) in a broken manifold M with boundary
on broken (or unbroken) Lagrangians L or K, we want to investigate if this broken map can be
viewed as a limit of a neck-stretching process. More precisely, by “gluing” a broken disc u, we mean
obtaining a family of holomorphic discs uτ in a τ−stretched manifold Mτ such that uτ →u as
FLOER COHOMOLOGY AND HIGHER MUTATIONS
43
τ →∞. We state some gluing results from [PW19] without proof, since there is no change in the
proof for the case of broken strips. We refer the reader to the op. cit. article for the case of broken
discs. The gluing method in [PW19] is similar to gluing discs with Lagrangian boundary conditions,
as done in [Abo12].
We recall the notation relevant to gluing from [PW19]. Given a nodal domain S with k puncture
nodes, and gluing parameters δ1, . . . δk > 0, we define the glued domain Sδ1,...,δk by gluing strip-like
(−L, L) × R × [0, 1] or cylindrical necks (−L, L) × S1 of length 2L = | ln(δi)| at the ith puncture
node. Given a l−broken manifold M, we can similarly define Mδ1,...,δl by gluing necks of appropriate
length. Note that the notational convention we choose is to use subscript to denote parameters of a
glued broken manifold while superscript is used to denote a stretched manifold.
Theorem 4.24 (Theorem 6.8 in [PW19]). Let (u, S) be a regular broken strip with boundary
on broken Lagrangian L and unbroken Lagrangian K with limiting eigenvalues λ1, . . . λk of Reeb
chords or orbits. Then, there exists δ0 such that for each δ ∈(0, δ0) there exists an unbroken strip
uδ : Sδ/λ1,...,δ/λk →Mδ such that uδ →u as δ →0.
The theorem above shows that for any regular broken strip, we can view it as an SFT-limit of
unbroken strips. InSection 5 we show that we can choose a perturbation scheme on the outer pieces
of broken strips so that any broken strip is regular. From now on, until the end of this subsection,
we assume that all broken strips are either high index or regular. The next theorem we state from
[PW19] shows that once we arrange regularity for all the broken strips, the gluing construction
in Theorem 4.24 would provide bijection of set of rigid broken disc with rigid unbroken disc in a
neck-stretched manifold.
In Section 6, from the proof of Lemma 6.1 we see that any regular rigid broken strip has at
most two levels. Hence, in the following theorem we consider only two level rigid strips. We use
M<E
Br (Γ, M[l], L[l], K)0 to denote the moduli space of rigid broken strips with compactified energy at
most E and constraint of interior markings going to the nice divisor D and MEHor<E(Mδ, L, K, D)0
to denote rigid holomorphic strips with respect to the glued coherent perturbation data with
boundary on L, K with at most E horizontal energy and constraint of interior markings going to D.
Theorem 4.25 (Theorem 6.10 in [PW19]). Let M be a broken symplectic manifold with 2 levels
and L be a broken Lagrangian with 2 levels . Assume perturbations have been chosen so that every
strip in M<E
Br,P(M[l], L[l], K, D)0 is regular. There exists δ0 such that for δ < δ0 the correspondence
u 7→uδ from Theorem 4.24 defines a bijection between the moduli spaces M<E
Br,P(M[l], L[l], K, D)0
and MEHor<E(Mδ, L, K, D)0.
M<E
Br,P(M[l], L[l], K, D)0 ↔MEHor<E(Mδ, L, K, D)0
Remark 4.26. The proof of 4.25 involves an application of the SFT compactness theorem. Note
that we apply SFT Compactness to a sequence of maps with bounded horizontal energy due to
Lemma 9.2 in [BEH+03].
If (L, K) is a monotone pair, then from the action-index relation we get that there is an energy
bound E0 such that any index-1 strip has energy less than E0. Thus, as a corollary of Theorem
4.25 we have the following result.
Corollary 4.27. If (L, K) is a monotone pair and a perturbation scheme is chosen that makes
every broken strip either high-index or regular and all the elements in M<E
Br,P(M[l], L[l], K, D)0 is
regular, then there is a δ0 such that for 0 < δ < δ0, there is a bijection between the rigid broken
holomorphic strips and the unbroken holomorphic strips in Mδ and all the rigid unbroken strips in
Mδ are regular.
FLOER COHOMOLOGY AND HIGHER MUTATIONS
44
MBr(M[l], L[l], K)0 ↔M(Mδ, L, K, D)0
Proof. By using E = E0 in Theorem 4.25 and the fact that any index 1 strip has energy less than
E0 we directly get the bijection. The fact that the unbroken strips are regular follows from the
Floer’s Picard Lemma used in the gluing construction of Theorem 4.24, see [PW19] for details.
□
