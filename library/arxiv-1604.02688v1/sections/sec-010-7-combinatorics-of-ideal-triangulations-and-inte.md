---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-010-7-combinatorics-of-ideal-triangulations-and-inte
section_title: "Combinatorics of ideal triangulations and integer normal surface theory"
section_number: 7
pages: 16-19
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
theory
The work of Kang-Rubinstein and Luo-Tillmann, described above, shows that the edge
solutions and tetrahedral solutions span the real vector spaceN(T; R)⊂ R3n of closed normal
classes, and that these together with the peripheral curve solutions span the real vector space
Q(T; R)⊂ R3n ofall Q-normalclasses. However, overtheintegersthesituationismoresubtle
— the integer linear combinations of edge and tetrahedral solutions generally give only a
ﬁnite index submodule ofN(T; Z) and the integer linear combinations of edge, tetrahedral
and peripheral curve solutions give a ﬁnite index submodule ofQ(T; Z). In this section we
give a precise description of these integer classes. It turns out that this is a consequence of
the results of Neumann [Neu92] on combinatorics of ideal triangulations.
Weregarda Q-normalclassasalinearcombinationofquadsin T satisfyingthe Q-matching
equations of Tollefson [Tol98]. Explicitly, letZE∼= Zn and Z□∼= Z3n denote the free Z-
modules with bases given by the (unoriented) edge classes and quad types inT respectively.
Given a quadqσ in an oriented tetrahedronσ of T we associate a sign±1 to each of the
edges ofσ meetingqσ as shown in ﬁgure 8. (These signs give the shear parameters along the
edges as explained in Section 6.1.) Adding these contributions gives a linear map
F : Z□→ ZE (21)
whose kernel is the submoduleQ(T; Z) of Q-normal classes.
Figure 8. Each quad can be replaced by a twisted square or twisted octagon.
Kang-Rubinstein [KR04] observed that for each edge class inT, the sum of all quad types
facing the edges in this class gives an “edge solution” inQ(T; Z); this gives a linear map
G : ZE→ Z□ (22)
with image contained inQ(T; Z). Further, the sum of the three quad types in a tetrahedron
in T gives a “tetrahedral solution” inQ(T; Z). We let E, T⊂ Q(T; Z)⊂ Z□ denote the
THE 3D-INDEX AND NORMAL SURF ACES 17
Z-submodules spanned by the edge solutions and tetrahedral solutions respectively, and let
Q0(T; Z) denote the submoduleE + T⊂Q(T; Z).
Next we associate two important homology (or cohomology) classes with anyQ-normal
class. First observe that any quadrilateral in a tetrahedron can be replaced by a ‘twisted
square’ meeting the same edges, or by a ‘twisted octagon’ in the corresponding truncated
tetrahedron with its four external edges oriented as shown in Figure 8 (compare [Neu92,
Figures 9, 10]). Note that the arrow on each external edge goes from an internal edge
labelled +1 to an internal edge labelled−1.
Each spun normal classS∈ Q(T; Z) is a linear combination of quads, so we can replace
this by a linear combinationS′ of twisted octagons. It follows from theQ-matching equations
that S′ represents a mod 2 homology class[S]2∈H2(M,∂M ; Z/2Z). Here and throughout
the paper, we will use[ ]2 to indicate aZ/2Z homology (or co-homology) class. Further, the
boundary edges ofS′, oriented as above, represent a homology class[∂S]∈ H1(M; Z). In
particular, the kernel of the boundary mapS↦→ [∂S] is precisely the submoduleN(T; Z)⊂
Q(T; Z) of closed normal classes.
WhenS gives an embedded spun normal surface,[∂S] agrees with boundary map deﬁned
by Tillmann in [Til08] (up to sign), and describes the boundary components of the spun
normal surface and the direction of spiralling of the spun normal surface around∂M. (With
the orientation convention given in Figure 8, the ends of a spun normal surface spiral up
into the cusp to theright of the oriented boundary curve, as viewed from the cusp.)
SinceS′ gives a 2-chain mod 2 whose boundary represents the reduction of[∂S] mod 2, it
follows that
([S]2, [∂S])∈{ (a,b )∈H2(M,∂M ; Z/2Z)×H1(∂M ; Z) :∂∗a =b mod 2}
where∂∗ :H2(M,∂M ; Z/2Z)→H1(∂M ; Z/2Z) is the connecting homomorphism in the long
exact sequence of the pair(M,∂M ). Hence, [∂S]∈ K = Ker(H1(∂M ; Z)→H1(M; Z/2Z)),
by the long exact sequence of the pair(M,∂M ) with Z/2Z coeﬃcients.
Theorem 7.1.The homomorphism
H :Q(T; Z)→H2(M,∂M ; Z/2Z)×H1(∂M ; Z), S↦→ ([S]2, [∂S])
has image
ImH ={(a,b )∈H2(M,∂M ; Z/2Z)×H1(∂M ; Z) :∂∗a =b mod 2}
and kernel
KerH =Q0(T; Z) = E + T.
In particular, the homomorphism
H0 :N(T; Z)→H2(M,∂M ; Z/2Z), S↦→ [S]2
has image
ImH0 = Ker(H2(M,∂M ; Z/2Z)→H2(∂M ; Z/2Z)) = Im(H2(M; Z/2Z)→H2(M,∂M ; Z/2Z))
and kernel
KerH0 =Q0(T; Z) = E + T.
18 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Proof. This essentially follows from Neumann [Neu92, Theorem 5.1] together with Poincaré
duality. To match Neumann’s notation from sections 4–6 of [Neu92] we letK denote the
oriented pseudo-manifold given by the triangulationT with its ideal vertices included. Thus
K is homeomorphic to the end compactiﬁcationˆM of the intM, obtained by collapsing each
component of∂M to a separate point. Truncating the corners of the tetrahedra inK gives
a cell complexK0 homeomorphic toM with boundary∂K0 homeomorphic to∂M.
Let C0 = ZV ∼= Zr,C 1 = ZE∼= Zn,J = Z□∼= Z3n be the free Z-modules with bases
given by the cusps, (unoriented) edge classes, and quad types in T respectively, and let
E, T⊂ Z□ denote theZ-submodules spanned by the edge solutions and tetrahedral solutions
respectively. Then Neumann deﬁnes a chain complex
0→C0
α
− →C1
β
− →J
β∗
−→C1
α∗
−→C0→ 0
where J = Z□/T∼= Z2n, α gives the sum of all edges incident to a vertex,α∗ is a map that
associates to an edge the sum of its endpoints, andβ andβ∗ are deﬁned so that the following
diagram commutes:
J = Z□
π

F
’’
C1 = ZE
G
77
β ’’
C1 = ZE
J = Z□/T
β∗
77
Here, π : Z□→ Z□/T is the quotient map.
To relate this to integerQ-normal surface theory we observe thatKerβ∗ =Q(T; Z)/T and
Imβ = (E + T)/T.
Now Neumann’s Theorem 5.1 gives an isomorphism fromKerβ∗/ Imβ =Q(T; Z)/(E + T)
to
{(f,g )∈H1(M; Z/2Z)×H1(∂M ; Z) :i∗f =g mod 2}
where i∗ : H1(M; Z/2Z) → H1(∂M ; Z/2Z) is induced by the inclusion mapi : ∂M →
M. In other words, this is the set of pairs (f,g ) with f ∈ Hom(H1(M), Z/2Z), g ∈
Hom(H1(∂M ), Z), such that f(γ) = g(γ) mod 2 for all γ ∈ H1(∂M ), where we write
H1(∂M ) =H1(∂M ; Z) and H1(M) =H1(M; Z).
Now we have a commutative diagram
H1(M,∂M ; Z/2Z)
j∗
−−−→ H1(M; Z/2Z)
i∗
−−−→H1(∂M ; Z/2Z)↓∼=
↓∼=
↓∼=
H2(M; Z/2Z)
j∗
−−−→H2(M,∂M ; Z/2Z)
∂∗
−−−→H1(∂M ; Z/2Z)
where the vertical maps are the isomorphisms given by Poincaré duality. This gives an
isomorphism
Q(T; Z)/(E + T)∼={(a,b )∈H2(M,∂M ; Z/2Z)×H1(∂M ; Z) :∂∗a =b mod 2}
THE 3D-INDEX AND NORMAL SURF ACES 19
where∂∗ :H2(M,∂M ; Z/2Z)→H1(∂M ; Z/2Z) is the connecting homomorphism in the long
exact sequence of the pair(M,∂M ). A careful examination of Neumann’s work shows that
this isomorphism is given by the homology mapH :S↦→ ([S]2, [∂S]) deﬁned above. □
Remark 7.2. Using Poincaré duality and the Mayer-Vietoris sequence it follows that
ImH0 = Im(H2(M; Z/2Z)→H2(M,∂M ; Z/2Z))
∼= Ker(H1(M; Z/2Z)→H1(∂M ; Z/2Z))∼=H1( ˆM; Z/2Z).
where ˆM is the pseudo-manifold given by the triangulationT with its ideal vertices included;
thus ˆM is homeomorphic toM with a cone attached over each boundary torus.
Remark 7.3. When M has no non-peripheral Z/2Z homology (for example, ifM is a knot
or link exterior in aZ/2Z homology sphere), thenQ0(T; Z) =N(T;Z) consists of all closed
normal classes. Further,K = Ker(H1(∂M ; Z)→H1(M; Z/2Z)) is a subgroup of index2r in
H1(∂M ; Z) where r is the number of components of∂M.
In general,Q0(T; Z) is a ﬁnite index submodule ofN(T;Z), and for any normal surface
class S∈N(T;Z) its “double”2S lies inQ0(T; Z).
