---
doc_id: arxiv-2301.08311v4
doc_title: "FLOER COHOMOLOGY AND HIGHER MUTATIONS SOHAM CHANDA"
section_id: sec-001-2-local-mutation
section_title: "Local Mutation"
section_number: 2
pages: 6-14
source_pdf: 2301.08311v4.pdf
source_sha256: 385139c69e18f5b0
doc_brief: "FLOER COHOMOLOGY AND HIGHER MUTATIONS — We extend the construction of higher mutation as introduced in [PT20] to local higher mutation, which is applicable to a larger class of monotone Lagrangians."
---
isotopy classes of Lagrangians.
1.4. Outline of the chapter. The proof of Theorem 1.2 is modelled on the neck-stretching
argument in Charest-Woodward [CW15]. The idea of the proof is to study “broken holomorphic
maps” (also known as holomorphic buildings in the literature), which are the limits of a Symplectic
Field Theory (SFT) neck-stretching process. We perform a neck-stretching along a small contact
sphere in a small Darboux neighborhood in the mutation neighborhood. This setup of the neck-
stretching process separates the mutation neighborhood from the rest of the manifold. Finally, we
make a local comparison in the stretched mutation neighborhood to obtain the mutation formula.
In Section 2 we explain the construction of local higher mutations. We prove that mutations
preserve the monotonicity of a Lagrangian.
In Section 3 we explain the SFT neck-stretching process with boundary conditions and prove
SFT compactness. [BEH +03] proves the SFT compactness theorem for limits of closed curves
with Morse-Bott Reeb orbit dynamics. The analysis required for maps with Lagrangian boundary
FLOER COHOMOLOGY AND HIGHER MUTATIONS 7
conditions proved so far in the literature has assumed non-degeneracy of Reeb chord dynamics, see
[Abb14], [Can21]. These results do not apply to the neck-stretching in our setting since Reeb chords
come in families and are always degenerate. We prove Theorem 3.13, a version of SFT compactness
that applies to our setting. The presentation here is an expanded version of the method outlined
in [PW19]. In [OW13], there is a different approach to proving exponential convergence to Reeb
orbits, which is an important step for proving the SFT compactness. It was indicated to the author
by Oh that similar methods can be applied to the Morse-Bott type Reeb chord dynamics as well.
In Section 4 we explain the construction of moduli space of broken maps as the intersection of a
∂ section with the zero-section of a Banach bundle. We prove that the linearization of ∂ in this
setting is a Fredholm operator. We also introduce notation for domain-dependent perturbations of
the almost complex structure, which we require to prove regularity of broken maps.
In Section 5 we show that the moduli space of rigid (expected dimension zero) broken maps with
boundary on L,K is transversely cut out for a generic choice of domain-dependent perturbation
away from the mutation neighborhood.
In Section 6 we prove that the only possible rigid broken maps have no “neck-pieces” and the
only possible configuration that can occur in the stretched mutation neighborhood can be classified
explicitly. This classification result is very similar to the classification of rigid objects already
found in the literature, e.g., Lemma 2.16 in horizontal sections in Lefschetz fibration in [Sei01],
classification of curves with boundary on transversely intersecting Lagrangians and surgeries as in
Theorem 60.26 in [FOOO07] and Proposition 5.13 in [PW19].
In Section 7 we prove that we can use broken maps to define Lagrangian intersection Floer
cohomology in the monotone case and that it is the same as the usual monotone Floer theory as
introduced in [Oh93]. Finally we prove the main theorem at the end of this section.
2. Local Mutation
In this section, we begin by constructing local higher mutations. Subsequently, we gather some
symplectic properties of the objects involved in the construction and prove that local mutations
preserve monotonicity of Lagrangians.
2.1. Construction of Local Higher Mutation. Similar to defining a Lagrangian torus over a
closed loop in C∗ as in (1.2.2) we can define a Lagrangian over a simple open path in C∗.
Definition 2.1. Let γ : [0, 1]→ C∗ be a path that does not intersect itself. Assume γ(0)̸=γ(1).
We defineTγ, a torus segment overγ, as follows,
(2.1.1) Tγ =

(z1,z 2,...z n)∈ Cn

πm(z1,z 2,...z n)∈γ,|z1| =|z2| =... |zn|

.
For a non-intersecting path γ, the torus segment Tγ is diffeomorphic to the product of a ( n− 1)
dimensional torus and a closed interval of the real line.
Definition 2.2 (Admissible Path). We call a path γ : (−t,t )→ C∗ admissible if there exists an
ϵ> 0 such that
(1) γ(x) =x for x∈ (−t,−ϵ)∪ (ϵ,t ),
(2) image of γ|(−t+ϵ,t−ϵ) lies in the disc D(t−ϵ) of radius t−ϵ ,
(3) γ lies completely inside the upper half plane.
FLOER COHOMOLOGY AND HIGHER MUTATIONS 8
γ
Tγ
Cn
C0
πm
Figure 2. Torus segmentTγ over a path γ
Rγ 0
Figure 3. Admissible path γ
Definition 2.3 (Locally mutable). We call a LagrangianL,→ (M,ω ) locally mutable if the following
hold:
(1) There is an open set B in M that is symplectomorphic via ϕ to an open ball B(0) around
0∈ Cn such that ϕ(B∩L) =Tγ for some admissible path γ in C.
(2) i∗ :H1(B∩L),→H1(L) is a split injection, i.e., 0 →H1(Tγ)→H1(L) extends to split short
exact sequence. Here i∗ is induced from i :ϕ−1(Tγ)→L.
(3) L\B is connected.
Example 2.4. Note that we can use a Hamiltonian isotopy (with respect to ωn) to map a circle in
the complex plane that does not pass through 0 to a curve γ that has an arc which is admissible.
Thus, a similar argument as Lemma 2.16 shows that the Clifford and Chekanov tori are locally
mutable.
Remark 2.5. For dimension 2, [Hau20] proves that if there is an isotropic surgery disc D whose
boundary cleanly intersects a Lagrangian L, then L satisfies condition (1) of Definition 2.3.
Definition 2.6 (Mutation neighborhood). The open set B in Definition 2.3 is called the mutation
neighborhood.
Now we can define local higher mutations. Intuitively, Local Higher Mutation is a cut-paste
construction where we cut out a torus segment over a path and replace it with another torus segment
over “flipped” curve that goes around 0 in the opposite direction. We need to replace the curve
while preserving some symplectic area so that eventually we preserve monotonicity of Lagrangians.
Definition 2.7. We define λn as the 1-form on C∗ given by λn = xdy−ydx
2(x2+y2)
n−1
n
. The form λn is
obtained by pulling back the 1-form λ0 =P
ixidyi−yidxi, on Cn, under the diagonal nth-root map,
z7→ (z1/n,...,z 1/n).
Definition 2.8 (Local Higher Mutation). Given a locally mutable Lagrangian L, the local higher
mutationLµ ofL is the Lagrangian obtained by removing ϕ−1(Tc) for an arc c ofγ i.e. c : (−r,r )→
C∗ and c(x) =γ(x) and gluing back ϕ−1(Tc′) for a curve c′ such that,
FLOER COHOMOLOGY AND HIGHER MUTATIONS 9
M
B
L ϕ
Tγ
Cn
π
γR
iR
C
Figure 4. Locally mutable L in M
(1) there is an ϵ> 0 such that c(x) =c′(x) for x∈ (−r,−r +ϵ)∪ (r−ϵ,r ),
(2) the glued curve c∪c′ is homotopic to the unit circle around 0 ,
(3) the resulting curve γ′ = (γ\c)∪c′ is smooth,
(4)
R
cλn =
R
c′λn.
Definition 2.9 (Mutated admissible path). Given an admissible path γ, we call the curve γ′ as
constructed in Definition 2.8 the mutated admissible path of γ.
Remark 2.10. For dimension 2, Lagrangian mutation is the same as performing an anti-surgery as
defined in [Hau20] followed by a Lagrangian surgery.
γ γ′
Mutation
Figure 5. Mutation of paths
We will show that the monodromy of the fiber torus around the origin is trivial in the mapping
class group. In Definition 2.8, condition (1) implies replacing c withc′ does not change the topology
of the Lagrangian L. We will also show that condition (3) implies that the symplectic areas of the
discs remain the same after local higher mutation and Lemma 2.16 implies all such choices of paths
c′ produces Hamiltonian isotopic Lµ.
FLOER COHOMOLOGY AND HIGHER MUTATIONS 10
The construction of higher mutation is related to an example of special Lagrangian fibration
that appears in [Joy02]. When γ is the real axis, Tγ is the Harvey-Lawson cone when k is odd (see
example 3.5 in [Joy02]). Consider the Harvey-Lawson Lagrangian fibration in dimension 3
ρ : C3→ R3
ρ(z1,z 2,z 3) = (Im(z1z2z3),|z2
1|−| z2
2|,|z2
1|−| z2
3|).
The singular Lagrangian ρ−1(0) is the Harvey-Lawson cone. The Clifford and Chekanov type tori
can be Hamiltonian isotoped so that they match the Harvey-Lawson fibers locally near 0. In this
setting, higher mutation can be thought of as replacing ρ−1(ϵ, 0, 0) with ρ−1(−ϵ, 0, 0) locally and
gluing it back appropriately.
2.2. Monodromy of the fiber Lagrangian torus. We will use symplectic parallel transport
of the fibration πm (see Equation (1.2.1) for definition of πm) to obtain various properties of the
Lagrangians we have been considering so far. One way to verify the manifold Tγ is a Lagrangian, is
by showing it is obtained by a symplectic parallel transport of a Lagrangian in a fiber. Notice that
πm is a fibration over C∗. The standard symplectic form ω0 in Cn induces a symplectic horizontal
distribution, which allows us to parallel transport between fibers such that the parallel transport
maps are symplectomorphisms of the fiber.
We describe how a symplectic fibration provides us a splitting of the tangent bundle of the total
space of the fibration. The tangent bundle of Cn splits into vertical and horizontal components
under the fibration πm. Away from the locus of critical points of πm, the vertical bundle V of the
fibration is sub bundle obtained as the kernel bundle kerdπm i.e. over a point z∈ Cn, the fiber
Vz of the vertical bundle is given as V|z = kerdπm(z). The horizontal bundle H is defined as the
symplectic complement Vω of the vertical bundle V . We can explicitly compute kerdπm at a point
z = (z1,...z n)∈ Cn to obtain Vz. For a point z such that πm(z)̸= 0, we have that
Vz = SpanC(X1(z),...,X n−1(z)),
where Xi(z) = (0,... 0, z i|{z}
ith spot.
, 0,..., −zn).
A direct computation can be done to obtain symplectic complement to the vertical bundle over any
z such that πm(z)̸= 0. We have the following relation.
(2.2.1) Hz = SpanC
  z1
|z1|2,... zn
|zn|2

Definition 2.11. We defineTz, the Lagrangian torus in the fiber over z∈ C∗ to be the torus given
by the relations|z1| =··· =|zn| in the fiber π−1
m (z).
Lemma 2.12. The manifold Tγ is a Lagrangian submanifold of Cn equipped with the standard
symplectic structure and Tγ is diffeomorphic to a torus.
Proof. Note that when|z1| =··· =|zn| for some z = (z1,...,z n)∈ Cn, from equation (2.2.1) we
have that the horizontal distribution at z is just C.z. The torus Tz is a Lagrangian submanifold
in π−1
m (z) by a direct computation and the manifold Tγ is the union of tori Tγ(t) for all t, i.e.
∪tTγ(t). A simple check shows that the map z 7→ (z
1
nz1,...,z
1
nzn) is a horizontal section for
(z1,...,z n)∈π−1
m (1) such that|z1| =··· =|zn|. This proves that the symplectic parallel transport
from the fiber over the point a to the fiber over the point b maps the Lagrangian torus Ta to the
torus Tb. Thus Tγ is a Lagrangian.
FLOER COHOMOLOGY AND HIGHER MUTATIONS 11
From the proof above one gets that the monodromy obtained from a circle around origin T1→T1
is multiplication by an nth root of unity ξ on all factors, thus Tγ is a trivial bundle over γ hence a
torus. □
Remark 2.13. The proof above also shows that torus segments are Lagrangian submanifolds.
Lemma 2.14. The torus segment Tγ is an exact Lagrangian for any smooth, non-intersecting path
γ : [0, 1]→ C∗ .
Proof. The standard symplectic form ω0 has a standard primitive λ0 =Pn
i=1
1
2(xidyi−yidxi). The
restriction of λ0 to Tγ is closed because Tγ is a Lagrangian. Now, to show that it is exact, it is
enough to show that line integrals ofλ0 over the generators ofH1(Tγ) is 0. Clearly the torus segment
Tγ retracts onto Tp for any p on γ thusH1(Tγ)∼= Zn−1. The generators are given by the standard
n− 1 loops S1→Tp,θ7→ (p1,...,e iθpi,...,e −iθpn) where (p1,...,p n)∈Tp . Using Stokes’ theorem
and the fact that|pi| =|pn|, we see that the line integral λ0 over the n− 1 generators is 0. Thus Tγ
is exact.
□
Lemma 2.15. For any path c to the Lagrangian torus in the fiber over p, i.e. c : [0, 1]→Tp, we
have
R
cλ0 = 0.
Proof. From 2.14, the one form λ0 restricted to the Lagrangian, Tγ is exact. Thus, we have that the
line integral
R
cλ0 depends solely on the end points c(0),c (1). Now choose a path from c(0) to c(1)
that is a composition of arcs from the standard n− 1 loops defined above. Since λ0 is rotationally
invariant, a direct computation shows that the integral of λ0 over any arc of the standard n− 1
loops is 0. Thus, we have that
R
cλ0 = 0.
□
2.3. Hamiltonian isotopy. In this subsection, we study the Hamiltonian isotopy classes of the
family of Lagrangians Tγ based on properties of the path γ. We follow the approach of Corollary
2.5 in [LM14] to provide a condition on paths γ and γ′ that is sufficient to make the torus segments
Tγ and T′
γ Hamiltonian isotopic. We study the case of smoothly isotoping the path γ0 : [0, 1]→ C∗
to another path γ1 where γs is fixed in a small neighborhood of 0 and 1, i.e., there is an ϵ such that
γs(t) =γ0(t) for t∈ [0,ϵ )∪ (1−ϵ, 1]. Call γ(0) =a , γ(1) =b.
Lemma 2.16. Letγs be an isotopy of paths that is constant on endpoints as described above, such
that
R
γs
λn is constant, Tγ0 is Hamiltonian isotopic to Tγ1
Proof. The isotopy γ : [0, 1]× [0, 1]→ C∗, of paths γs :=γ(s, ), from the curve γ0 to γ1, lifts to
an isotopy of embedded manifolds (with boundary) from the torus segment Tγ0 to Tγ1 via torus
segments. Since we know that each torus segment is a Lagrangian manifold, we have a Lagrangian
isotopy betweenTγ0 toTγ1. An equivalent condition to Lagrangian isotopy being a result of ambient
Hamiltonian isotopy is that the Lagrangian isotopy is exact, see Section 6.1 [Pol01]. To deal with an
isotopy of manifolds with boundary, we use the relative de Rham model to define exactness. In our
setting, being exact turns out to be the same as having the integral
R
cs
λ0 for an isotopy (induced
from the Lagrangian isotopy) of curves cs∈H1(Tγs,Ta∪Tb) invariant of isotopy in the s-direction.
Here c is a homotopy of paths lying on the isotopy of the torus segments over γ with boundary on
the torii Ta,Tb i.e. cs :=c(s, ) is a path (or loops) in Tγs such that the boundary (if any) ∂cs lies
on the boundary Ta∪Tb of the torus segment. We have observed that the torus segment Tγ is an
exact Lagrangian in Lemma 2.14 and that the integrals of λ0 are 0 on paths that lie in a single fiber
Tz in Lemma 2.15. Thus, it is enough to check whether
R
cs
λ0 is invariant of s for a family of curves
FLOER COHOMOLOGY AND HIGHER MUTATIONS 12
cs that descend to the path γs. A candidate for such a lift is cs(t) = (γs(t)1/n,...,γ s(t)1/n). ClearlyR
cs
λ0 =
R
γs
λn from the definition of λn. From the hypothesis of the lemma, we see that
R
cs
λ0 is
invariant ofs. Thus, we have proved the Lemma.
□
Corollary 2.17. If γ0 and γ1 are two admissible paths that are equal near the ends and
R
γ0
λn =R
γ1
λn then Tγ0 is Hamiltonian isotopic to Tγ1.
Proof. Lemma 2.16 reduces the problem of finding a Hamiltonian isotopy of the Lagrangian Tγ for
admissible paths γ to finding an isotopy of γ that keeps the line integral with respect to λn constant.
Assume that γ0 and γ1 are two admissible paths that are equal near the ends, are isotopic to each
other and
R
γ0
λn =
R
γ1
λn. We can ‘close up’ γ0 and γ1 to an embedded circle with the same area
by attaching a path γu that lies in the upper half plane. Lemma 2.3 of [LM14] show that γ0∪γu is
Hamiltonian isotopic with respect to the symplectic form ωn =dλn to γ1∪γu where the isotopy is
constant on γu. Thus we get an isotopy γs of γ0 to γ1 such that
R
γs
λn is constant. Thus, using
Lemma 2.16 we finish the proof of our corollary. □
We define a cylindrical version of the Lagrangian Tγ when the path γ is chosen to be cylindrical.
The construction depends on choosing a path on C that lies on the real line away from a compact
set.
Definition 2.18 (Cylindrical path). A cylindrical path is defined as a map γ : R→ C∗ such that
γ(r)∈ R when|r|>M for some M >0 and the following have the following limits
lim
r→±∞
γ(r) =±∞.
Definition 2.19 (Asymptotically cylindrical path). A path γ : R→ C∗ is defined to asymptotically
cylindrical if there is an ϵ̸= 0 such that γ(r)∈ R +iϵ when|r| > M for some M > 0 and the
following have the following limits
lim
r→±∞
γ(r) =±∞.
Definition 2.20 (Cylindrical extension). Let γ : (−t,t ) be an admissible path. From the definition
of admissible path, we know there is an ϵ >0 such that γ(x) = x for x∈ (−t,t )\ (−ϵ,ϵ ). The
cylindrical extension γe is defined as
γe(x) =x for x ∈ R\ (−ϵ,ϵ )
γe(x) =γ(x) otherwise.
We conclude this subsection with the definition of a cylindrical version of torus segments, that
shows up in the later sections as a result of neck stretching. We define a Lagrangian Tγ over a
cylindrical path γ similarly as we define a torus-segment in Definition 2.1. We can similarly define
Tγ for an asymptotically cylindrical path γ.
Since the path γ lies on the real axis near its ends, the Lagrangian Tγ has cylindrical ends in
the sense that for large R> 0, Tγ\BR(0) = [M,∞)× Λ for some M >0 in cylindrical coordinates
R×S2n−1 of Cn\{ 0} where Λ is the disjoint union of two Legendrian tori T+,T− in the unit sphere
S2n−1 given by the equations
(2.3.1) T± =

(z1,...,z n)∈S2n−1

|z1| =|z2| =.. =|zn|,z 1.z2.....z n∈ R±

.
FLOER COHOMOLOGY AND HIGHER MUTATIONS 13
2.4. Mutation preserves monotonicity. In this subsection, we will describe which Lagrangians
can be locally mutated and explain the construction of local mutations and show that monotonicity
of Lagrangians is preserved under the operation of mutation.
Lemma 2.21. If L is a locally mutable monotone Lagrangian, then its mutation Lµ is also monotone.
Proof. To fix notation, we use B to denote the mutation neighborhood of L, γ to denote the curve
that determines Tγ as in Definition 2.3 and γ′ to denote the path for the mutation. For any disc
uµ with boundary on Lµ, we will construct a disc with boundary on L, u, with the same area and
Maslov number as uµ, which would prove that Lµ is monotone. Since L =Lµ outside the mutation
neighborhood, we need to modify uµ only where it enters the mutation neighborhood. Let ∂uµ
denote the restriction of the disc uµ to the boundary circle and assume that on the domain interval
[p,q ], ∂uµ is a map to the mutation neighborhood i.e. ∂uµ : [p,q ]→B. We can choose points p,q
on the circle so that the [ p,q ] is a maximal subset of the boundary circle with this property. There
can be two cases,
(1) ∂uµ(p) and ∂uµ(q) lie on the same end of Tγ, i.e. πm(∂uµ(p)) =πm(∂uµ(q)) =:z,
(2) ∂uµ(p) and ∂uµ(q) lie on the opposite ends of Tγ, i.e. πm(∂uµ(p))̸=πm(∂uµ(q)).
For case (1), we can homotope the path ∂uµ over [p,q ] through paths in Lµ while fixing the end
points to a path that lies completely on a single torus fiber Tz⊂Tγ. We can use this homotopy
to extend uµ so that the boundary on [p,q ] lies on Tz, call the extended map upre. Note that this
doesn’t change the area since the homotopy of paths lied in a Lagrangian, also, it doesn’t change
the Maslov number of the boundary. Since ∂upre maps the boundary [p,q ] to Tz, using the fact that
z∈γ we get that ∂upre([p,q ])⊂L since L =Tγ in the mutation neighborhood.
For case (2), as a preliminary step, we homotope∂uµ to a path onTγ′ such that on (p+e,q−e) for
smalle,∂uµ is a horizontal section of γ′. We then attach horizontal sections over the discs bounding
γ∪γ′ and not containing 0 to extend uµ to uprepre so that the boundary lies on Tγ. We need to
deal with the case of discs containing 0 carefully, note that since the horizontal section is given by
taking the nth root, it can’t be defined in a neighborhood of 0, but only on a slit neighborhood, i.e.,
after removing a half-line starting at 0. We can remove a ray R+ from the neighborhood and then
attach two copies of a line to the neighborhood to get a domain topologically looking like a radial
sector removed from a disc. Call the two newly attached lines as l1,l 2. Refer to figure (6). We
can continuously define an nth root map over this domain (colored yellow in the figure), and then
attach a sector ( colored green in the figure) of 0 symplectic area that lies on TR+ and is a homotopy
between the two branches of the horizontal section over l1,l 2. Use this homotopy to extend uprepre
to upre. The boundary of upre on [p,q ] lies on L. Note that, as before, the symplectic area of upre
is the same as that of uµ from the fact that the area contributions from the horizontal sections
cancel out from condition (4) in Definition 2.8. Also, the Maslov number doesn’t change since the
generators of H1(Tz) have Maslov number 0.
After extending uµ as shown in the last two paragraphs for every maximal domain [ p,q ] on the
boundary where ∂uµ is a map to the mutation neighborhood, we can get a map u that has the
following properties,
• the boundary of the map lies on L,
• the Maslov number is Im(uµ),
• the symplectic area is ω(uµ).
SinceL is monotone, we get that Im(uµ) =λω(uµ). The constant λ doesn’t depend on uµ we began
with. Thus, by repeating this construction for each uµ∈π2(M,Lµ) we see that Lµ is monotone.
□
FLOER COHOMOLOGY AND HIGHER MUTATIONS 14
Disc with removed sector
Sector
Figure 6. Disc used in creating homotopy from uprepre to upre
Definition 2.22. (Monotone tuple of Lagrangians, Definition 4.1.2 in [WW10]) A pair of Lagrangians
(L1,L 2) is called a monotone pair if there is a there exists a τ for which we have the following
an action-index relation for maps with boundary on Li. Let u : Σ→ M where ∂Σ ={Ci} and
u(Ci)⊂Li, then we have
2
Z
u∗ω =τµ(u).
We can use the method of Lemma 2.21 to prove that monotonicity of a Lagrangian pair is preserved
when one of the Lagrangians is mutated.
Lemma 2.23. If (L,K ) is a monotone pair of Lagrangians and L is locally mutable, then the pair
(Lµ,K ) is also a monotone pair.
