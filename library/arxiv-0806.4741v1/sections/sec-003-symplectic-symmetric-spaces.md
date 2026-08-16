---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane P. Bieliavsky G´ eom´ etrie et Physique math´ ematique Universit´ e Catholique de Louvain 2, Chemin du Cyclotron, B-1348 Louva"
section_id: sec-003-symplectic-symmetric-spaces
section_title: "Symplectic symmetric spaces"
section_number: null
pages: 4-7
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
doc_brief: "The deformation quantizations of the hyperbolic plane P. Bieliavsky Géométrie et Physique mathématique Université Catholique de Louvain 2, Chemin du Cyclotron, B-1348 Louvain-la-Neuve, Belgium — We"
---
expressed as an oscillatory integral, analogous to the oscillatory integral formulation (8) of Weyl’s composi-
tion. In [33], A. Weinstein suggested a beautiful geometrical interpretation of the asymptotics of the phase
S =S(x,y,z ) occurring in the oscillatory kernel in terms of the area of a geodesic triangle admitting points
x,y and z as midpoints of its geodesic edges. In section (3.7), we illustrate this by establishing an exact
formula for the kernel in terms of a speciﬁc geometrical quantity of three points hereafter denoted by Scan,
in accord with Weinstein’s asymptotics.
2 Symplectic symmetric spaces
2.1 Deﬁnitions and elementary properties
Everything in this subsection is entirely standard and can be found e.g. in [34] and references therein. A
symplectic symmetric space is a triple (M,ω,s ) where M is a connected smooth manifold endowed with a
non-degenerate two-form ω and where
s :M×M→M : (x,y )↦→s(x,y ) =:sxy
is a smooth map such that for all pointx inM, the partial map: sx :M→M is an involutive diﬀeomorphism
ofM (i.e. s2
x = idM) which preserves the two-form ω (i.e. s⋆
xω =ω) and which admits x as an isolated ﬁxed
point. On furthermore requires the following property:
sxsysx = ssxy
4
to hold for any pair of points ( x,y ) in M×M. In this situation, the space M is endowed with a preferred
aﬃne connection. Indeed, for every triple of tangent vector ﬁelds X,Y and Z on M, the following formula:
ωx(∇XY , Z) := 1
2Xx.ω(Y + sx⋆Y , Z)
deﬁnes1 a torsion-free aﬃne connection ∇ on M that enjoys the properties of being preserved by every
symmetry sx as well as being compatible with ω in the sense that:
∇ω = 0.
This last fact implies in particular that ω is closed, turning it into a symplectic form on M.
An important class of symplectic symmetric spaces is constituted by the non-compact Hermitean symmetric
spaces. Such a space is a coset space M = G/K of a non-compact simple Lie group G by a maximal
compact subgroup K that admits a non-discrete center Z(K). The ﬁrst example being the hyperbolic plane
D := SL2(R)/SO(2). The compactness of K implies in particular that a Hermitean symmetric space admits
a G-invariant Riemannian metric for which the connection ∇ is the Levi-Civita connection.
However, in general a symplectic symmetric space needs not to be Riemannian, even not pseudo-Riemannian,
in the sense that there is in general no metric tensor g on M such that∇g = 0. In this sense a symplectic
symmetric space is a purely symplectic object. In the problem we are concerned with in the present work,
such a “non-metric” symplectic symmetric space will play a central role.
Two symplectic symmetric spaces (Mi,s (i),ω (i)) (i = 1, 2) are saidisomorphic is there exists a diﬀeomorphism
ϕ :M1→M2 that is symplectic i.e. such thatϕ⋆ω(2) =ω(1) and that intertwines the symmetries:ϕs(1)
x ϕ−1 =
s(2)
ϕ(x) for all x inM(1). Given a symplectic symmetric space (M,ω,s ), its automorphism group Aut(M,ω,s )
therefore turns out to be the intersection of the diﬀeomorphism group of aﬃne transformation of ( M,∇)
with the symplectic group of (M,ω ):
Aut(M,ω,s ) = Aﬀ( ∇)∩ Symp(ω). (12)
The latter group is therefore a (ﬁnite dimensional) Lie group of transformations of M. One then shows that
since it contains the symmetries {sx}x∈M its action on M is transitive, turning (M,ω ) into a homogeneous
symplectic space. In particular, every symplectic symmetric space is a coset space.
Up to isomorphism, the list of homogeneous spaces underlying simply connected 2-dimensional symplectic
symmetric spaces is the following:
1. the ﬂat plane : R2
2. the hyperbolic plane : D := SL2(R)/SO(2)
3. the universal covering space of the anti-de Sitter surface : ~AdS2 := ~SL2(R)/SO(1, 1)
4. the sphere : S2 :=SO(3)/SO(2)
5. the universal covering space of the Galileo coset : ~SO(2)× R2/R
6. the Poincar´ e coset :M :=SO(1, 1)× R2/R.
Items 5 and 6 provide the ﬁrst examples of non-metric symplectic symmetric spaces.
A old classical result independently due to Kirilov and Kostant [35, 36] asserts that every simply connected
homogeneous symplectic space is isomorphic to the universal covering space of a co-adjoint orbit of some Lie
group. In our situation of symplectic symmetric spaces this can be easily visualized. Indeed, ﬁxing a base
point o∈M the conjugation
˜σ : Aut(M,ω,s )→ Aut(M,ω,s ) :g↦→ ˜σ(g) :=sogso (13)
1See [34] and appendix A for an explicit computation in the case of generic coadjoint orbits of the Poincar´ e (1,1) group.
5
deﬁnes an involutive automorphism of the group Aut( M,ω,s ). Its diﬀerential at the unit element therefore
yields an involutive automorphism at the Lie algebra level:
σ := ˜σ⋆e : aut(M,ω,s )→ aut(M,ω,s ) (14)
where aut(M,ω,s ) denotes the Lie algebra of the automorphism group. The latter Lie algebra therefore
decomposes into a direct sum of (±1)-eigenspaces for σ:
aut(M,ω,s ) = k⊕ p. (15)
Note that the diﬀerential at e of the coset projection: π : Aut(M,ω,s )→ M when restricted to the (−1)-
eigensubspace p provides a linear isomorphism with the tangent space at o:
π⋆e|p : p ˜−→To(M). (16)
The pull back of the symplectic structure at o therefore deﬁnes a symplectic bilinear two-form on p:
Ω := ( π⋆e|p)⋆ωo . (17)
When extended by zero to the entire aut(M,ω,s ) the element Ω is easily seen to be a Chevalley 2-cocycle in
the sense that:
Ω([X,Y ],Z ) + Ω([Z,X ],Y ) + Ω([Y,Z ],X ) = 0. (18)
The 2-cocycle Ω needs in general not to be exact at the level of the automorphism algebra aut(M,ω,s ). That
is there does not always exist a linear form ξo on aut(M,ω,s ) such that
Ω(X,Y ) = ξo[X,Y ]. (19)
Note nevertheless that the only 2-dimensional non-exact case corresponds to the ﬂat plane R2.
We now adopt the notation
G := Aut(M,ω,s ) ; g := aut(M,ω,s ). (20)
Denoting by K the stabilizer subgroup of G of the base point o, one gets the G-equivariant identiﬁcation
G/K−→M :gK↦→go, (21)
where the symmetry map reads
sgK(g′K) = g˜σ(g−1g′)K . (22)
It turns out that the 2-cocycle Ω is exact if and only if the action of G on (M,ω ) is Hamiltonian in the
sense that, endowing C∞(M) with the Lie algebra structure deﬁned by the Poisson bracket associated to
the symplectic structure ω, there exists a Lie algebra map
λ : g−→C∞(M) :X↦→λX (23)
that satisﬁes the following property:
{λX,f}(x) = d
dt|t=0f(exp(−tX)x) =: X⋆
x.f (24)
for all function f∈C∞(M). Note that the map λ is then necessarily G-equivariant in the sense that
λAd(g)X(x) = λX(gx) (25)
for all g∈G, X∈ g and x∈M.
When Hamiltonian, one may choose:
ξo(X) := λX(o). (26)
In that case, denoting by O the co-adjoint orbit of the element ξo∈ g⋆, the moment mapping:
J :M−→O⊂ g⋆ :x↦→ [J(x) : g→ R :X↦→λX(x)] (27)
6
realizes a G-equivariant covering from M onto the co-adjoint orbit O. Note that the co-adjoint orbit O is
itself endowed with a canonical symplectic structure ωO deﬁned at the level of the fundamental vector ﬁelds
for the co-adjoint action by
ωO
ξ (X⋆,Y ⋆) := ξ[X,Y ] ( ξ∈O ). (28)
With respect to the latter structure the moment map J :M→O is symplectic.
When non-exact, a passage to a central extension of g yields an entirely similar situation. Indeed, the
transvection group (generated by all the sx◦sy and forming a normal subgroup of Aut( M) ) does not
act in a strongly Hamiltonian manner on M. However, one may consider the (non-split) central extension
0→ RZ→ ˜g := g⊕ RZ→ g→ 0 deﬁned by [X,Y ]∼ := [X,Y ]⊕Ω(X,Y )Z, mimicking the passage from R2n
to the Heisenberg algebra in the ﬂat situation. In this new set-up, M may now be realized as a coadjoint
orbit of the extended group and the above results remain valid under essentially the same form [34].
To close this subsection, we observe that when the co-adjoint orbit O is simply connected the moment
mapping J : M→O is then necessarily a global G-equivariant symplectomorphism. This turns out to be
the case in items 1, 2, 4 and 6 in the above list of 2-dimensional spaces.
