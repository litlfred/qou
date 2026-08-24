---
doc_id: arxiv-2301.08311v4
doc_title: "FLOER COHOMOLOGY AND HIGHER MUTATIONS SOHAM CHANDA"
section_id: sec-004-5-regularity
section_title: "Regularity"
section_number: 5
pages: 43-54
source_pdf: 2301.08311v4.pdf
source_sha256: 385139c69e18f5b0
doc_brief: "FLOER COHOMOLOGY AND HIGHER MUTATIONS — We extend the construction of higher mutation as introduced in [PT20] to local higher mutation, which is applicable to a larger class of monotone Lagrangians."
---
in Theorem 4.24 would provide bijection of set of rigid broken disc with rigid unbroken disc in a
neck-stretched manifold.
In Section 6, from the proof of Lemma 6.1 we see that any regular rigid broken strip has at
most two levels. Hence, in the following theorem we consider only two level rigid strips. We use
M<E
Br (Γ, M[l], L[l],K )0 to denote the moduli space of rigid broken strips with compactified energy at
mostE and constraint of interior markings going to the nice divisor D andMEHor<E(Mδ,L,K,D )0
to denote rigid holomorphic strips with respect to the glued coherent perturbation data with
boundary on L,K with at most E horizontal energy and constraint of interior markings going to D.
Theorem 4.25 (Theorem 6.10 in [PW19]). Let M be a broken symplectic manifold with 2 levels
and L be a broken Lagrangian with 2 levels . Assume perturbations have been chosen so that every
strip inM<E
Br,P(M[l], L[l],K,D )0 is regular. There exists δ0 such that for δ <δ0 the correspondence
u7→uδ from Theorem 4.24 defines a bijection between the moduli spaces M<E
Br,P(M[l], L[l],K,D )0
andMEHor<E(Mδ,L,K,D )0.
M<E
Br,P(M[l], L[l],K,D )0↔M EHor<E(Mδ,L,K,D )0
Remark 4.26. The proof of 4.25 involves an application of the SFT compactness theorem. Note
that we apply SFT Compactness to a sequence of maps with bounded horizontal energy due to
Lemma 9.2 in [BEH +03].
If (L,K ) is a monotone pair, then from the action-index relation we get that there is an energy
bound E0 such that any index-1 strip has energy less than E0. Thus, as a corollary of Theorem
4.25 we have the following result.
Corollary 4.27. If (L,K ) is a monotone pair and a perturbation scheme is chosen that makes
every broken strip either high-index or regular and all the elements in M<E
Br,P(M[l], L[l],K,D )0 is
regular, then there is a δ0 such that for 0 < δ < δ0, there is a bijection between the rigid broken
holomorphic strips and the unbroken holomorphic strips in Mδ and all the rigid unbroken strips in
Mδ are regular.
FLOER COHOMOLOGY AND HIGHER MUTATIONS 44
MBr(M[l], L[l],K )0↔M (Mδ,L,K,D )0
Proof. By using E =E0 in Theorem 4.25 and the fact that any index 1 strip has energy less than
E0 we directly get the bijection. The fact that the unbroken strips are regular follows from the
Floer’s Picard Lemma used in the gluing construction of Theorem 4.24, see [PW19] for details. □
5. Regularity
We prove that under a generic perturbation of complex structure, every broken disc or strip
with only puncture nodes (the nodes between two levels) are either regular or high-index. As a
consequence of this regularity, we will see in Section 6 that the only rigid broken strip or rigid
broken disc with point constraint has two levels, and the inner level consists of simple discs.
From the construction of moduli space of broken discs and strips, we know that broken maps
are fiber products of moduli spaces of levels under the evaluation maps at the punctures. Thus,
it is enough to show each level is regular, and the evaluation maps are transverse, we will take
this approach to prove regularity. We will prove that the standard complex structure J0 of Cn is
enough to ensure the inner and neck pieces to be transversally cut out. Finally, we use a domain
dependent choice of almost complex structure on the outside level to cut the last layer of evaluation
fiber product transversally.
Here is an outline of this section :
• In the first subsection, we will focus on the interior pieces. A short exact sequence argument
shows that when we forget about the matching condition at Reeb chord/orbits, discs in
the interior piece are transversally cut out when they don’t touch the critical locus (set of
critical points) of the fibration πm (see Equation (1.2.1) for definition). As for when the
discs touch the critical locus, we show that we can obtain a stronger regularity result. We
show that a constrained moduli space of discs that touch the critical locus is transversely
cut out.
• In the second subsection we will focus on the neck piece and show that all of them are
regular and the evaluation map at any of the puncture is a surjective map to the Legendrian
torus.
• In the third subsection, we will use domain dependent perturbation to regularize the outside
component. Notice that using domain dependent perturbations, we can cut out any matching
condition coming from the necks transversally. Thus, we can choose domain dependent
perturbation to make the evaluation map of the outer pieces transverse to the matching
conditions coming from the inside and neck pieces.
• In the fourth subsection, we explain how to obtain the fiber product under the matching
condition of Reeb chords between the levels transversally cut out.
Remark 5.1 (Transversality of punctured spheres) . We leave the details of transversality of
punctured spheres with cylindrical ends in the broken maps, since it has already been well studied
in the literature. See subsection 7.5 in [CW15] for details, specifically Lemma 7.20 proves all the
required transversality result needed for spheres. Thus, from now on we will deal with transversality
of pieces with nonempty boundary.
5.1. Interior piece. In this subsection, we show that with the standard almost complex structure,
we can obtain regularity of the moduli space of punctured discs in the interior piece Cn of the
broken manifold M. We prove a stronger result that the constrained moduli space where the points
that touch the critical locus are constrained to be on a particular subspace in crit(πm) is regularly
FLOER COHOMOLOGY AND HIGHER MUTATIONS 45
cut out. This shows that the moduli space of discs that touch the critical locus is regular, and of
high index.
5.1.1. When discs don’t touch the critical locus. We show regularity of discs that don’t touch the
critical locus. Let u be a map from a punctured disc Σ with l boundary punctures to Cn with
boundary on the Lagrangian torus Tγ. If we assume that u never touches a point where dπm is 0,
we can obtain the following short exact sequence of 2 – chains where Di refers to the corresponding
linearization of ∂ and the boundary conditions are suppressed from the notation for clarity.
0 0 0
0 W 1,p,δ(u∗TvCn)⊕Vl W 1,p,δ(u∗T Cn)⊕Vl⊕Hl W 1,p,δ+π
n ((πm◦u)∗T C)⊕Hl 0
0 W 0,p,δ(Hom(T Σ,u∗TvCn) W 0,p,δ(Hom(T Σ,u∗T Cn) W 0,p,δ+π
n (Hom(T Σ, (πm◦u)∗T C) 0
0 0 0
i
D1
dπm
D2 D3
i dπm
Since the above is a short exact sequence, to prove D2 is surjective, it is enough to prove that
D1,D 3 are surjective. We show that eD2, the parameterized version of D2 that takes into account
the moduli space of domains Γ in. We need the domain perturbations to prove eD3 is surjective. To
proveD1 is surjective, one approach is to directly show that index of D1 is n− 1 and kernel is of
dimension n− 1. We outline another approach to show regularity using a splitting argument similar
to Lemma 3.3.2 in [MS12].
5.1.2. Compactifying along the ends and index computations. The index problem and regularity of
Cauchy Riemann operators on bundles over discs have been well understood in the literature, see
Appendix C of [MS12]. We aim to extend our bundles to the closed disc so that we can use the
results of appendix C in [MS12]. We can compactify u∗TvCn to a holomorphic vector bundle over
the closed disc such that ∂u∗TvTγ compactifies to a real sub-bundle. Notice that near the ends,
u∗TvCn is holomorphically trivial such that on the boundary since it is isomorphic to the bundle
Tv((πm◦u)∗Cn) where (πm◦u)∗Cn is the pullback of the fibration πm : Cn→ C. We can take the
pullback of the fibration πm since near the ends u doesn’t hit the critical locus as the map u is close
to a trivial strip over a Reeb chord or a trivial cylinder over a Reeb orbit. We compactify u∗TvCn
by gluing a trivial bundle at the ends, we denote this bundle as ( u∗TvCn)comp. Similarly, πm◦u
extends to a holomorphic map πm◦u from the closed disc to CP1 with boundary on γ. We can
compactify (πm◦u)∗T C by (πm◦u)∗T CP1. We denote the linearization of the Cauchy-Riemann
section ∂ at πm◦u as Dc
i . We can check that the restriction of Dc
i to (πm◦u)∗T C equal to Di by a
direct computation.
We can identify the kernel and cokernel of the compactified problem with the cylindrical problem
by adding constraints. Since we are using the standard complex structure, the linearizations Di are
just ∂, we can use Taylor series expansion to identify the kernel and cokernel of the uncompactified
linearized problems with the kernel and cokernel of the compactified problem with constraints. See
Proposition 5.9 in [PW19] for a proof of isomorphism between the (co)kernels of the cylindrical and
compactified linearized operator.
Lemma 5.2. kerDi∼= kerDc
i and cokerDi∼= cokerDc
i where the compactified problem for D2 with
constraint of having sections that vanish at points mapping to ∞ at the same order as πm◦u.
We now use Lemma 5.2 to compute indices. From the short exact sequence, we know that
Ind(D2) = Ind(D1) +Ind(D3). The index of D1 isn− 1 by an index gluing argument applied to the
FLOER COHOMOLOGY AND HIGHER MUTATIONS 46
vertical index of the fibration (πm◦u)∗Cn where we pinch off the singular fibers. Note that for index
computation, we can perturb any u smoothly over a compact region while preserving the Fredholm
index, thus even if u passes through the critical locus, we can assume that after small perturbation
over a compact region, u misses the critical locus. Thus we still get a short exact sequence whose D1
has index n− 1. The index of Dc
2 without any constraints is given directly by the Riemann-Roch
formula as 1 +µ(πm◦u) where µ is the Maslov index, and with the constraint of vanishing at the
same order as πm◦u, the index is 1 + µ(πm◦u)−πm◦u−1
weighted(∞) where πm◦u−1
weighted(∞) is a
weighted sum of intersection of πm◦u with∞ where interior intersections are weighted with 2 and
boundary intersections are weighted with 1. Thus, we have the following index formula :
Lemma 5.3. LetDu denote the linearization of the ∂ operator at u in the cylindrical setting, then
Ind(Du) =n +µ(πm◦u)−πm◦u−1
weighted(∞).
Remark 5.4. As a quick application of the index formula, we compute the index of a disc with
only one boundary puncture. The index of a disc u : H→ (Cn,Tγ) that is asymptotic to a Reeb
chord of length kπ/n is n +k. We can also prove the surjectivity of D2 at this stage by using the
identification of kernel and cokernel with compactified problem.
Theorem 5.5 (Horizontal Transversality). coker eD3 ={0}.
Proof. From the identification of the cokernels in Lemma 5.2, it is enough to check that coker eDc
3 is
0 with the appropriate constraints. Since this is a one dimensional problem, a modification of the
automatic transversality result in [Sei08] proves transversality in this case. The only modification
to Lemma 13.1 and 13.2 in [Sei08] which we need for our case is working with marked points
in the interior. See the proof of horizontal transversality in Theorem 5.14 below for a detailed
explanation. □
5.1.3. Splitting of holomorphic bundles over disc. We show that a Cauchy Riemann operator on
a holomorphic bundle over a closed disc with totally real boundary conditions can be split using
results of Oh in [Oh95b]. Any holomorphic bundle over the closed disc is holomorphically trivial
by applying the Oka-Grauert principle to an extension of the bundle to a slightly larger open
disc. Thus, a pair ( eE, eF ) of holomorphic bundle with real sub-bundle on the boundary of a disc
is holomorphically isomorphic to the pair of bundles ( D× Cn,F ) where F is a real sub-bundle of
S1× Cn. In [Oh95b], Oh proves that a linearized Cauchy-Riemann problem with boundary for the
standard complex structure splits into a direct sum of 1 dimensional problems (see Theorem 1 in
[Oh95b] and Corollary 5.19 in [PW19] for adaptation to the cylindrical setting). Applying Oh’s
splitting result to the vertical part, we have the following:
Lemma 5.6 (Splitting Lemma). The Cauchy-Riemann problem,
Dc
1 :Wk,p(u∗TvCn,∂u∗TvTγ)comp→Wk−1,p(Hom(T D, (u∗TvCn)comp),
splits into direct sum of n− 1 one dimensional problem under a change of trivialization,
Dc
1 :⊕n−1
i=1Wk,p(Ei,Fi)→⊕ n−1
i=1Wk−1,p(Hom(T D,Ei))
where⊕Ei∼=u∗TvCn and⊕Fi∼=∂u∗TvTγ.
We can apply Lemma 5.6 to obtain the following transversality result.
Theorem 5.7. (Vertical Transversality) cokerD1 = 0
Proof. From the splitting Lemma, we have that cokerD1 =⊕n−1
i=1 cokerD1|i where D1|i is the
restriction of D1 to the bundle pair (Ei,Fi). Thus, it is enough to show that each of the coker are
FLOER COHOMOLOGY AND HIGHER MUTATIONS 47
0. We also know that for 1 dimensional Cauchy-Riemann problem with boundary condition, either
the kernel or the cokernel is non-zero. Thus it is enough to show that kerD1|i is non-zero for all i.
Note that there is a Tn−1 action on the space of maps given by
(θ1,...θ n−1).(u1,...,u n) = (eiθ1u1,eiθ2u2...,e −i Pθjun),
and this action preserves the projection of the map under the map πm. This action restricts to an
action on the space of holomorphic maps, thus taking the infinitesimal action at u, we get a map
tn−1→ kerD1∼=Dc
1. Also note that if we compose tn−1→ kerD1∼= kerDc
1 with the evaluation map
evq for a point q on ∂Σ, we have an isomorphism of vector spaces tn−1 ∼− →u∗TvCn|q. This proves
that kerD1|i is non-zero for all i as otherwise we wouldn’t get an isomorphism since ⊕Ei∼=u∗TvCn.
Thus coker D1 = 0 □
5.1.4. When discs touch the critical locus. In this section, we show that discs that touch the critical
locus are regular. Moreover, we prove that a constrained moduli space is regularly cut out. When a
disc u touches the critical locus of πm at the points{ζ1,...ζ i}, we lose the vertical bundle which
helped us prove regularity. The vertical bundle still exists over D\{ζ1,...ζ i}. We will show that
the vertical bundle can be holomorphically extended over the points ζj and then use a splitting
argument with domain dependent perturbations to prove transversality of a “vertically constrained””
problem where we put high codimension constraints to the extension of the vertical bundle. This
allows us to show that broken strips that touch the critical locus are high index, hence can’t be
rigid.
The primary obstruction to defining a vertical bundle when a disc touches the critical locus is that
the dimension of the kernel jumps up at the critical points. When p∈ Cn\ crit(πm), the vertical
direction is
Tv
p Cn = ker⟨[p2...p n p1p3...p n p1...p n−1], ⟩,
where⟨,⟩ is the complex bilinear dot product. Define the rational map ϕ as follows
ϕ : Cn99K Pn−1
(z1,...,z n)7→ [z2z3...z n :z1z3...z n :··· :z1...z n−1].
The vertical fiber over a point p is equal to ker⟨ϕ(p), ⟩ since the kernel of the dot product is
invariant under scaling by C∗. We will show that this rational map, ϕ, can be lifted to a smooth
map.
Theorem 5.8. There exists a complex manifold eCn obtained by iterated blow up of Cn along complex
subspaces and a smooth map eϕ :eCn→ Pn−1 such that the following diagram commutes,
eCn Pn−1
Cn
eϕ
eπ ϕ
whereeπ is a composition of blowdown maps.
Now,ϕ can be extended to a map eϕ :eC→ Pn−1 by doing an inductive iterated blowup. Now the
vertical subbundle of u∗T Cn overz is defined by kereϕ◦eu(z) where eu is the lift of the disc to the
blowup. Because the disc u maps to trivial cylinders (or strips) over Reeb orbits (or chords) near
the punctures, we can check that there is an extension of eϕ◦eu to the whole disc.
FLOER COHOMOLOGY AND HIGHER MUTATIONS 48
Proof. The iterated blowup is constructed by first blowing up the origin in Cn to obtain eCn
0
π0
−→Cn,
then blowing up the lift of the lines C⟨ei⟩ in Cn generated by the standard basis vector {e1,...,e n}
of Cn to obtain eCn
1
π1
−→eCn
0. We continue this process of blowing up and stop at the ( n− 2)th step
where we have blown up all (lifts of) the standard subspaces of complex dimension ≤n− 2 in Cn to
obtain a chain of blowups as follows
(5.1.1) eCn
n−2
πn−2
−−−→eCn
n−3
πn−3
−−−→... eCn
0
π0
−→Cn
We denote the n− 2 iterated blown up space as
eCn πtot
−−→Cn.
Note that the map ϕ factors as ψ◦pr where pr : Cn\{ 0}→ Pn−1 is the standard projection map
to the projective space and
ψ : Pn−199K Pn−1
[z1 :··· :zn]7→ [z2z3...z n :z1z3...z n :··· :z1...z n−1].
LetePn−1 be the space obtained by a similar construction as in (5.1.1), ( n− 2) times iterated
blowups of Pn−1 along the standard coordinate projective subspaces. We can check that eCn is a C∗
bundle overePn−1. To get a lift of ϕ, it is enough to show that the rational map ψ lifts to a smooth
map eψ onePn−1. Indeed, we can define
eϕ(z) = eψ(epr(z))
where epr is the projection map from eCn→ePn−1.
We use an inductive process to lift the map. When the dimension is two, we can define the map
eψ to be just ψ. Assume eψ has been defined for dimension n and thus eϕ is defined for dimension
n + 1. We can define eψ for dimension n + 1 by taking a standard Cn+1 chart near the vertex of the
moment polytope of Pn and extending the map ψ to eCn+1 by eϕ that has already been defined. For
example, take the chart Cn+1→ Pn+1 given by z7→ [1 :z], then we define, under the identification
of the domain using this chart,
eψ(z) := [0 :eϕ(z)]
on the exceptional divisors of eCn+1. We can do this for all the vertices of the moment polytope
of Pn+1 and check that we get a well-defined map eψ :ePn+1→ Pn+1 which is a smooth lift of the
rational map ψ.
□
Corollary 5.9. Letu : Σ→ Cn be a holomorphic punctured disc with boundary on a torus segment
Tγ, such that u−1(crit(πm)) ={ζ1,...,ζ l}. Then the pullback bundle u∗T Cn splits as
u∗T Cn = eV⊕ eH
where eV is a subbundle that matches with the vertical bundle V = kerdπm

Σ\{ζi} on away from the
critical points Σ\{ζ1,...ζ l}.
Proof. We use the lifted map to obtain extension of vertical sub-bundles over the critical points in a
disc. From the lifting property of blowup, the holomorphic map u to Cn extends toeu, a holomorphic
map to the blowup eCn. We have a map eϕ◦eu to Pn−1, thus we can define a holomorphic sub bundle
eV ofu∗T Cn by defining eVz = ker⟨eϕ◦eu(z), ⟩. We can then define a quotient line bundle u∗T Cn/eV
FLOER COHOMOLOGY AND HIGHER MUTATIONS 49
over the disc after compactifying the bundles, and since any short exact sequence of holomorphic
bundles over a closed disc split, we get a splitting
u∗T Cn = eV⊕ eH
where eH denotes the quotient bundle.
□
The previous corollary lets us split the Cauchy-Riemann operator. Denote the split operator as
follows,
Du =DV⊕DH.
We now compute the index of DV . For simplicity of notation, let u be a map from a punctured disc
that touch the critical locus critπm only at 0 and assume
u(0) = (0, 0,...,p k+1,...,p n),
where pi̸= 0. Thus, we have,
ui(z) =zmi + higher order terms
for some positive integers mi, we can assume without loss of generality that mi≤mi+1. We will
prove that the index of DV is n− 1 + 2(Pk−1
i=1 mi). Consider the holomorphic sections,
Xi(z) = (0,...,u i(z),..., −uk(z),..., 0),
then the sections X1,...,X k−1,Xk+1,...,X n forms a frame of eV over D2\{ 0} and the boundary
condition of the bundle pair ( eV,∂u ∗TvTγ) is just iRn−1. Note that Xk+1(0),...,X n(0) are linearly
independent and the Xi(z) vanishes at the order mi for i < k. Thus these sections give an
isomorphism of eV near 0 with the twisted trivial bundle ⊕k−1
i=1O(mi), thus from a gluing argument
we have
Ind(DV ) =n− 1 + 2c1(⊕k−1
i=1O(mi)) =n− 1 + 2(
k−1X
i=1
mi).
Assume the map u that touches the critical locus at ( ζ1,...,ζ i) and kl is the number of 0’s in u(ζl)
for 1≤l≤i. Let ml1≤ml2≤...m lkl
be the order of the vanishing of the coordinates of u at ζl.
We define the critical multiplicity mc of the map u as
mc(u) =
iX
l=1
kl−1X
q=1
mlq.
Lemma 5.10. If u touches the critical points of πm, the index of the vertical linearized operator
DV is n− 1 + 2mc(u) and the horizontal index is 1 +µ(πm◦u)−πm◦u−1
weighted(∞)− 2mc(u)
Ind(DV ) =n− 1 + 2mc(u)
Ind(DH) = 1 +µ(πm◦u)−πm◦u−1
weighted(∞)− 2mc(u)
Proof. By using an index-gluing argument we can generalize the discussion to obtain the required
index formula. □
We will now relate the kernel and cokernel of the linearized operators with a linearized operator
of a constrained problem on.
Lemma 5.11. kereDH∼= kereDconst
πm◦u and coker eDH∼= coker eDconst
πm◦u
FLOER COHOMOLOGY AND HIGHER MUTATIONS 50
Proof. Let Dconst
πm◦u be the linearization of ∂ of the constrained Cauchy Riemann problem at πm◦u
with the constraint of vanishing atζl to the orderPkl−1
q=1 mq wherem1≤m2≤...m kl are the orders
of vanishing of the coordinates of u at ζl. The push-forward dπm, maps kerDH isomorphically
to kerDconst
πm◦u. This follows from the fact that dπm has this order of vanishing at ζl. Since dπm is
isomorphism on fibers of eH except over ζi, we see that the map kerDH
dπm
−−→kerDconst
πm◦u is injective.
By checking the order of vanishing at ζi we see that this map is also surjective. We also know that
Ind(DH) = Ind(Dconst
πm◦u), thus, their cokernels are also isomorphic. We can use the fact that since
dπm is complex linear and the linearizations D we deal with are ∂ under holomorphic frames to see
that the kernels of the parameterized linear operators eDH and eDconst
πm◦u are isomorphic, and the index
argument shows that the cokernels are isomorphic. □
Definition 5.12 (Level Structure). We can define a level structure on the set crit(πm) by defining
a point (p1,...,p n)∈ crit(πm) to be of level k if exactly k of the pi’s are 0. Thus, every critical
point has a level ranging from 2 to n.
We will now define the notion of being vertically constrained at the critical points and the notion
of point constrained.
Definition 5.13 (Vertically Constrained moduli space) . Let u be a holomorphic map from a
punctured disc to Cn with boundary on Tγ that meets the critical locus crit(πm) at the points
{ζ1,...,ζ i}. Assume that the level of u(ζj) is kj. The family of punctured holomorphic discs with
the constraint of touching a critical point of levelki at the pointζi is called the vertically constrained
moduli space.
We denote the linearization of ∂ at u of the vertically constrained problem by Dvc
u . By using the
splitting of u∗T Cn into eV⊕ eH as before, we get a splitting of Dvc
u =Dvc
V ⊕Dvc
H , where Dvc
H =DH
since the constraints are only on the subbundle eV . We denote the linearized operator including
domain parameterization by eDvc
u . From Lemma 5.10 we have the following,
Ind(Dvc
u ) = Ind(Du)− 2
iX
j=1
kj.
If a disc doesn’t meet the critical locus, then by definition, being vertically constrained would impose
no constraints on the linearized Cauchy-Riemann problem. We denote the moduli space of vertically
constrained discs in Cn with boundary on Tγ asMvc
in.
Recall that the disc potential is obtained by count of rigid discs with point constraints. We
define the notion of point constrained moduli space of broken discs. The notion of point constrained
interior moduli space is defined similar to the notion of broken disc with point constraint. Given a
point p in Lin, the moduli space of discs with constraint at p is defined to be the subspace of the
moduli of discs that pass through p. The moduli space with point constraint can be realized as
ev−1
q (p) where q is a point on the boundary of a disc and evq is the evaluation map at q.
Theorem 5.14. For any disc u touching crit (πm), the parameterized vertically constrained moduli
space of discs with point constraint preserving the level structure of the critical points is regularly
cut out, i.e. eDvc
u is a surjective map.
Proof. First, we split the operator eDvc
u =Dvc
V ⊕eDH. Since the action of Tn−1 as defined in Theorem
5.7 on the space of maps preserves the level structure of the critical points, the action descends
to the vertically constrained problem and gives transversality of Dvc
V . From Lemma 5.11, we see
that it is enough to prove that linearization of ∂ at πm◦u with the constraint of vanishing at
the critical points ζi is surjective. From the proof of Lemma 4.3.2 of [Wen10] we see that for any
FLOER COHOMOLOGY AND HIGHER MUTATIONS 51
smooth vector field X that vanishes at the points ζis, we have that d(πm◦u)X is a smooth vector
field that satisfies the constraint of vanishing at ζi to the correct order since d(πm◦u) has order of
vanishing 1 less than that of π◦u and X has an order of vanishing at least 1 at the points ζi. Thus,
we can apply the result Lemma 4.3.2 in our case to conclude that image of Dconst
πm◦u doesn’t change
if we expand our domain to Wk,p(End(T Σ))⊕W
k,p,δ+π
n
const ((πm◦u)∗T C,∂ (πm◦u)∗Tγ ). Now since
πm◦u is a non-constant map to one dimensional manifold, we can use the argument of automatic
transversality as done in Lemma 13.2 in [Sei08] to get that eDconst
H is surjective. We finally use the
vertical and horizontal transversality to show that p is a regular value of the evaluation map evq to
prove the regularity of the point constraint. □
Corollary 5.15. The moduli spaceMin of vertically constrained discs in Cn with boundary on Tγ
is a smooth manifold and the evaluation map evp at any boundary puncture p that takes a map u to
the starting point of the Reeb chord u is asymptotic to at the puncture p,
evp :Mvc
in→T±,
is a submersion to the Legendrian torus.
Proof. Theorem 5.14 shows thatMvc
in is a manifold. The submersion to the Legendrian torus follows
from the Tn−1 action. □
5.2. Neck Pieces. In this subsection, we show that regularity of maps in the neck piece can be
obtained without perturbing the standard complex structure. The treatment of the neck piece is
very similar to the treatment of the interior piece, albeit a bit easier.
We use a similar splitting trick as in Subsection 5.1 to split the Cauchy-Riemann operator. Let u
be a disc mapping to the neck piece Cn\{ 0} with boundary on TR∗. Using [Oh95b], we get that
(u∗T Cn,∂u∗TT R∗) splits into 1 dimensional bundle pairs ⊕n
i=1(Ei,Fi). We can show regularity of
Du by showing that the kernel of the restriction, kerD|i is non-zero for all i since these are one
dimensional problems.
Theorem 5.16. If u is map to the neck-piece with boundary on the cylindrical Lagrangian TR∗,
then coker Du ={0}
Proof. In the neck piece, there is an action of R×Tn−1 where the R action is by translation andTn−1
action is same as in the interior piece. The infinitesimal action provides a mapR×tn−1→ kerDu such
that under the evaluation map at a boundary point q, we have an isomorphism R× tn−1 ∼− →Tu(q)TR∗.
A similar argument as in Theorem 5.7 gives us coker Du ={0}. □
Let p be a boundary puncture. Let evp denote the evaluation map at p that takes values in the
space of Reeb chords. Specifically, evp(u) is the starting point of the Reeb chord the map u is
asymptotic to at the puncture p. As a corollary of Theorem 5.16, we have the following result,
Corollary 5.17. The moduli spaceMneck of discs in the neck piece is a smooth manifold and the
evaluation map evp
evp :Mneck→T±,
is a submersion to the Legendrian torus.
Proof. Same argument as in proof of Corollary 5.15. □
FLOER COHOMOLOGY AND HIGHER MUTATIONS 52
5.3. Outer Piece. We will now show that we can choose a domain dependent perturbation data
on broken strips and broken discs to form a coherent perturbation data that attains our goal of
showing every broken strip is either regular or of high index. For any combinatorial type Γ st of
stable connected nodal strip with k markings, the smooth components of Γ st can be divided into
the following collections
• strip piece,
• discs without interior marked points,
• discs with interior markings.
Given a stabilized combinatorial type Γst of broken disc with k intersections with the nice divisor D,
we will show that we can choose generic domain dependent complex structure to obtain regularity
for all outside pieces along with regularity of the matching condition at the contact S2n−1 and
Legendrian T±. The matching conditions between the last neck piece and outside piece is given
by countably many images of smooth maps coming the interior pieces given by evaluating at the
positive puncture of last level. For a broken strip with l neck pieces, the smooth map it contributes
is
evl+ :Mvc
in×evin,ev1−M1×ev1+,ev2−···× evl−1+,evl−Ml.
The choice will be made such that it satisfies the following properties on each type of smooth
component.
• (P1) On strips, Jk will be only t dependent and equal to Jout at the boundaries .
• (P2) On discs without interior marked points, Jk will be the constant almost complex
structure Jout.
• (P3) On discs with interior marked points, Jk is a domain dependent almost complex
structure that is equal to Jout on the boundary .
Once we set such a perturbation dataP, given any combinatorial type Γ of a broken strip or a broken
disc, we define the notion of domain dependent broken holomorphic strip by using the standard
complex structure on the inside and neck pieces and the domain dependent complex structure on
Γst.
Theorem 5.18 (Outside Transversality). There is a coherent family of perturbation data P
satisfying the properties (P1-3) which makes moduli space of strips Mdd
k (cMout,Lout,K,D ) or the
moduli space of discs with Mdd
k (cMout,Lout,D ) regular and the evaluation map at the cylindrical
punctures transversely intersecting with the matching condition coming from the inside and neck
pieces.
Proof. For satisfying the coherence conditions we inductively choose the perturbations based on the
number of interior marked points. After choosing perturbations for at most k− 1 markings, we
use the perturbations of M<k to define perturbation on lower dimensional strata of Mk. Since the
space of almost complex structures we care about is contractible, we can extend the perturbations
from the lower dimensional strata of Mk to the whole of Mk.
Fork = 0 markings, there is no stable combinatorial type of strip. The only possible broken type Γ
without any outside interior marking mapping to D is the case when the outside piece is just a strip
with punctures going to Reeb chords or orbits. Let S be a strip with punctures and u :S→ cMout
with boundary on Lsing and K where the u is asymptotically a trivial strip or cylinder over a Reeb
chord or orbit, a similar proof as Theorem 4.3 in [FHS95] shows that the set R(u) of regular points
that are somewhere injective in the s−direction (notation from [FHS95] ) is open dense in the
strip S. Thus, by constructing a universal moduli space and usual generic transversality arguments
we can see that for a generic t dependent family of almost complex structure, the moduli space
FLOER COHOMOLOGY AND HIGHER MUTATIONS 53
Mt(cMout) of Jt holomorphic punctured strips in cMout with boundary on Lout and K is a smooth
manifold and the evaluation maps at the punctures are transverse to countably many matching
conditions. The important fact of generic transversality we use here is that the set of regular Jt
families for which each evaluation map is transverse forms a comeagre/Baire set hence countable
intersection of such comeagre sets is also comeagre.
Fork = 1, we first define a domain dependent almost complex structure on a punctured disc with
1 marking where the punctures go to Reeb orbits or chords so that the holomorphic punctured discs
are regular and the evaluation at the punctures are transverse to the evaluation from the inside and
neck pieces and the evaluation at the interior marking is transverse to D. This is obtained by the
usual technique of creating a universal moduli space of pairs ( Jk,u ) of domain-dependent almost
complex structure and holomorphic map, showing that it is a Banach manifold and then using
Sard-Smale. See proof of Theorem 4.1 in [CW17] The boundary strata of a strip with 1 marked
point have strip breaking due to the marking escaping to infinity or disc bubbling when the interior
marking goes to the boundary. The domain from the strip breaking will not have any holomorphic
maps from it since the ends of the strip go to Lout∩K and the interior marking goes to D but
D∩ (Lout∪K) =∅. By choosing domain-dependent almost complex structure on the punctured
disc with 1 marking and a t dependent Jt on the strip without any markings, we force the choice of
domain dependent almost complex structure at the boundary strata obtained by disc bubbling.
In the case of k = 2 we first encounter a situation where the lower dimensional strata will have a
disc without any marking. This combinatorial type can only occur as a domain of a holomorphic
strip when the disc without marking is in the neck piece or the map is constant on the disc, as Lout
is exact inMout\D. In either of those cases, we know that such discs are Jneck or Jout regular.
We continue this method of choosing domain dependent perturbation inductively by extending the
pre-determined choice of almost complex structure on lower dimensional strata of Mk to choose
a coherent perturbation data which makes the moduli space of outer piece regular such that the
matching condition with the inside pieces are transversely cut out. □
5.4. Moduli space of broken discs and strips. At this stage, we know that the moduli space
of maps to the blow-up of interior, neck and outer piece are regularly cut out and the evaluation
map at the punctures are submersions when the complex structure on the blown-up interior and
neck piece is the standard complex structure and the complex structure on the outer piece is a
domain-dependent perturbation, JΓout, of the complex structure Jout. We will show that for such
a choice of complex structure, any holomorphic broken disc that avoids the critical locus in the
interior is regular in the sense of Definition 4.17.
We define the notion of a vertically constrained broken strip by constraining the inner piece of
the broken strip to be vertically constrained. We denote the moduli space of such broken strips by
Mvc
Br(Γ, M[l], L[l],K ).
Similar to strips, we can add vertical constraints to broken discs with point constraints. We
denote the moduli space of broken discs with point and vertical constraints by
Mvc
Br(Γ, M[l], L[l],p ).
We will show that for any combinatorial type Γ = (Γ in, Γ1,..., Γout), any ( Jstd,...,J Γout)-
holomorphic broken strip (u, D) is regularly cut out as a fiber product. We illustrate an inductive
method which ensures that
Mvc
in×evin,ev1M1×ev1,ev2···× evl−1,evlMl
is a smooth fiber product.
FLOER COHOMOLOGY AND HIGHER MUTATIONS 54
Lemma 5.19. There is a coherent perturbation datum P such that every l− broken strip (u, D)∈
MBr(Γ, M[l], L[l],K ) or broken disc (u, D)∈ Mvc
Br(Γ, M[l], L[l],p ) where there are no multiply
covered pieces and the only nodes are puncture nodes that map asymptotically to Reeb orbit or chord
is regular where the standard complex structure of Cn is chosen in the neck pieces and inner pieces.
Proof. From Corollaries 5.15, 5.17 and Theorem 5.18, we get that for any holomorphic (uin,u 1,...,u l)
satisfying the matching condition, it is regular in the moduli space of (vertically constrained)
punctured discs to the inside and neck pieces respectively. The corollaries also show that the
evaluation map at a puncture is a submersion at the matching condition, thus by an inductive
argument we see that (uin,u 1,...,u l) is a regular broken strip with an inner piece and l neck pieces
since the transversality of the evaluation maps at the puncture nodes among these levels can be
ensured by using the submersion of the evaluation map at a single puncture as illustrated above.
ThusMvc
in×evin,ev1M1×ev1,ev2···× evl−1,evlMl is a smooth manifold and we have an evaluation
mapevmedium from it to T±,→S2n−1, we use a domain dependent perturbation on Dout as shown in
Theorem 5.18 to achieve regularity of Mout and to ensure the evaluation map evout is transversely
intersecting with evmedium, hence the total fiber product that produces the moduli of broken strips
is transversely cut out. □
Using Lemma 5.19, we can now prove the main transversality theorem of this section.
Theorem 5.20. There is a coherent perturbation datum such that every broken strip or a broken
disc with point constraint is either regular or high-index.
Proof. Once we have attained regularity for broken strips with only puncture nodes, we can conclude
that the only possible non-regular broken strips are of high index by using monotonicity of M and
L,K . Given a broken strip, after replacing multiple covered components by the underlying simple
and forgetting nodal components to obtain a single nodal strip with only puncture nodes, we get a
holomorphic broken strip which is regular by Lemma 5.19 hence non-negative index. Removing
non-constant nodal components reduces the total energy, by an index gluing argument we see that
monotonicity implies that removing nodal components reduces the index. Replacing multiple covers
by single covers also cause the index to decrease. Thus, we have attained our goal of showing that
either the broken strip is of high index or is regular. □
