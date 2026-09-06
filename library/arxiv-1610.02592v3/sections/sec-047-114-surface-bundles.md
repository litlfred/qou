---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-047-114-surface-bundles
section_title: "Surface bundles"
section_number: 11.4
pages: 367-372
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
This theorem reveals in particular that it is fairly easy to construct plenty
of simply connected four-manifolds with boundary. Note that the simply con-
nected four-manifolds constructed in this way are not contractible: indeed
the following proposition shows that they have a non-trivial second homology
group.
Proposition 11.3.17. A four-manifold with one 0-handle and k 2-handles
is homotopy equivalent to a bouquet ofk two-spheres.
Proof. We ﬁrst deformation retract the two-handles over their core discs,
and then we shrink the whole 0-handle to a point. □
To construct contractible four-manifolds, we need to employ 1-handles.
11.3.7. Three-manifolds with boundary.The Lickorish-Wallace Theo-
rem extends to compact manifolds with boundary, in the appropriate way.
Proposition 11.3.18.Every compact orientable 3-manifoldM with bound-
ary is obtained fromS3 as follows: pickL⊔C⊂S3 where L is a link andC
is a 1-complex; remove an open regular neighbourhood ofC and perform an
integral surgery onL.
Proof. Cap oﬀ the boundary ofM by adding handlebodiesHg, to get a
closedmanifold M′. Choosea1-complex C⊂M′ whoseregularneighbourhood
consists of these handlebodies, so that by removingC we getM back.
Now M′ is obtained fromS3 via integral surgery along some linkL, and
by general position we may suppose thatC is disjoint from the cores of the
surgered solid tori, so that we can see bothC andL disjointly inS3. □
If∂M consists of tori we may suppose thatC is also a link.
11.4. Surface bundles
Seifert manifolds have base orbifolds of dimension 2 and smooth ﬁbres of
dimension 1. We now introduce a complementary construction where the base
orbifolds have dimension 1 and the smooth ﬁbres have dimension 2. These are
called surface bundles.
11.4.1. Surface bundles.Asurface bundle overS1 is a ﬁbre bundleM→
S1 of a compact orientable 3-manifoldM (possibly with boundary) over the
circle, whose ﬁbreΣ is a connected compact orientable surface. IfM has
boundary, thenΣ also has, and∂M consists of tori ﬁbering overS1.
Proposition 11.4.1.Every surface bundle overS1 is constructed by taking
Σ× [0, 1] and glueing Σ× 0 to Σ× 1 via an orientation-preserving diﬀeomor-
phismψ.
360 11. CONSTRUCTIONS OF THREE-MANIFOLDS
Proof. One such glueing clearly gives rise to a surface bundle overS1.
Conversely, by cutting a surface bundle overS1 along a ﬁbre we get a surface
bundle over the interval, which is a productΣ× [0, 1]. □
The diﬀeomorphismψ is themonodromy of the surface bundleMψ. Since
isotopic glueings produce diﬀeomorphic manifolds, the three-manifoldMψ de-
pends only of the class ofψ in the mapping class groupMCG(Σ) on Σ. More
than that, it actually depends only on its conjugacy class:
Proposition 11.4.2. If ψ and φ are conjugate inMCG(Σ), thenMψ and
Mφ are diﬀeomorphic.
Proof. The diﬀeomorphismg : Σ → Σ that conjugates them extends to
Σ× [0, 1] and gives a diﬀeomorphismMψ→Mφ. □
The manifoldsMψ andMψ−1 are (orientation-reversingly) diﬀeomorphic.
11.4.2. Properties. We now start to investigate the topological proper-
ties of surface bundles. LetM→S1 be a surface bundle with ﬁbreΣ.
Exercise 11.4.3. The mapsΣ→M→S1 induce an exact sequence
0−→π1(Σ)−→π1(M)−→π1(S1)−→0.
This implies in particular thatπ1(M) surjects onto Z and therefore:
Corollary 11.4.4.We haveb1(M)> 1.
In other terms, the surface ﬁbreΣ is non-separating and hence [Σ] ∈
H2(M,∂M )isnon-trivial(andhasinﬁniteorder,sincethereisnotorsionthere).
Note that there is an obvious degree-n regular coveringMψn→ Mψ for
every n and an inﬁnite regular coveringΣ× R→Mψ induced by the normal
subgroupπ1(Σ)◁π 1(M).
Proposition 11.4.5. The ﬁbreΣ is an essential surface. Ifχ(Σ)> 0 then
M is diﬀeomorphic toD×S1 orS2×S1. Ifχ(Σ)⩽ 0 the universal cover of
int(M) is R3 andM is Haken.
Proof. Ifχ(Σ)> 0then MCG(Σ)is trivial and we are done, so we suppose
χ(Σ)⩽ 0. The ﬁbreΣ is incompressible becauseπ1(Σ) injects, and is also
∂-incompressible by a doubling argument (the doubleDM ﬁbres toS1 with
incompressible ﬁbreDΣ, henceΣ is∂-incompressible). The ﬁbre is clearly not
∂-parallel, hence it is essential.
The manifoldM is covered byΣ×R, whose interior is covered byR2×R =
R3: henceM is irreducible. It is also∂-irreducible because its double also ﬁbres
and hence is irreducible. ThereforeM is Haken. □
11.4. SURFACE BUNDLES 361
11.4.3. Semi-bundles. The Seifert ﬁbrations are circle bundles over two-
dimensional orbifolds, and likewise it is natural to consider surface bundles
over 1-orbifolds. The compact 1-orbifolds areS1 and the closed segment with
mirrored endpoints. We have already considered the S1 case and we now
deﬁne some surface bundles over the closed segment, calledsemi-bundles.
Let Σ be a non-orientable surface, with orientable double coverp : ˜Σ→ Σ
and deck transformationτ that gives Σ = ˜Σ/τ. We have
Σ×∼ (−1, 1) =
( ˜Σ× (−1, 1)
)
/(τ,ι)
with ι(x) = −x. A local semi-bundle is the mapΣ×∼ (−1, 1)→ [0, 1) that
sends (p,x ) to|x|. The ﬁbre over0 is Σ, that overx∈ (0, 1) is ˜Σ.
A semi-bundle M→ [−1, 1] is a map which is a local semi-bundle when
restricted to [−1, 1−ε) and (ε, 1]. The ﬁbre over±1 is Σ and the ﬁbre of
x∈ (−1, 1) is ˜Σ. We should think about this object as a surface bundle over
the segment orbifold[−1, 1] with mirror points±1.
Exercise 11.4.6. Every semi-bundle is constructed by gluing two copies of
Σ×∼ [−1, 1] along their boundaries via some diﬀeomorphism.
Set I = [−1, 1]. LetM→I be a semi-bundle with ﬁbresΣ and ˜Σ. Note
thatI = R/Γ where Γ< Isom(R) is generated by the reﬂections at the points
±1. The orbifold fundamental group ofI is
π1(I) = Γ = Z/2Z∗ Z/2Z.
Exercise 11.4.7. The maps˜Σ→M→I induce an exact sequence
0−→π1( ˜Σ)−→π1(M)−→π1(I)−→0.
Proposition 11.4.8.Ifχ(Σ)> 0 thenM is diﬀeomorphic toRP2×∼ S1. If
χ(Σ)⩽ 0 the orientable ﬁbre˜Σ is essential, the universal cover ofint(M) is
R3, andM is Haken.
Proof. Same proof as in the standard bundle case. □
Exercise 11.4.9. An orientable 3-manifoldM has a (semi-)bundle structure
if and only if there is an orientableΣ⊂M that cutsM into interval bundles.
Let M→ I be a semi-bundle. We may pull-back the semi-bundle along
the orbifold double coverS1→I and get an ordinary surface bundle˜M→S1,
so that the following diagram commutes:
˜M //

M

S1 //I
Every semi-bundle is thus covered by an ordinary bundle.
362 11. CONSTRUCTIONS OF THREE-MANIFOLDS
11.4.4. Seifert manifolds. We now classify the Seifert manifolds that
have a surface (semi-)bundle structure.
Proposition 11.4.10. A Seifert manifoldM has a (semi-)bundle structure
if and only if one of the following holds:
• ∂M⁄= 0,
• e(M) = 0,
• M =
(
T, (1,e )
)
or
(
K, (1,e )
)
,
• M =
(
S2, (2, 1),(2, 1),(2, 1),(2, 2q +1)
)
or
(
RP2, (2, 1),(2, 2q +1)
)
.
The manifolds in the last line occur only as semi-bundles.
Proof. If∂M⁄= ∅ ore(M) = 0 thenM→S has an orientable sectionΣ,
which cutsM into interval bundles: henceΣ is a ﬁbre of a (semi-)bundle (see
Exercise 11.4.9).
LetS be one of the orbifolds
T, K, (S2, 2, 2, 2, 2), (RP2, 2, 2).
It contains a circle that splitsS into one or two annuli, Möbius strips, or
(D, 2, 2). Every circle ﬁbering over these pieces is an interval bundle by Propo-
sition 10.3.33. Therefore every ﬁberingM→S contains a vertical torus that
splitsM into interval bundles and is hence a (semi-)bundle.
Conversely, ifM has a (semi-)bundle structure the orientable ﬁbre is es-
sential and is hence either horizontal or vertical: we get one of the types
listed. □
11.4.5. Torusbundles. Atorusbundle isofcourseasurfacebundle M→
S1 with ﬁbre a torusT. We ﬁx a basis forπ1(T ), so thatMCG(T ) = SL 2(Z).
By what said above, every matrixA∈ SL2(Z) deﬁnes a torus bundleMA with
monodromyA. We want to understand whenMA is a Seifert manifold.
Exercise 11.4.11. For everye∈ Z there are diﬀeomorphisms
M(1e
0 1
)∼=
(
T, (1,e )
)
, M (−1 e
0 −1
)∼=
(
K, (1,e )
)
.
The classiﬁcation of torus bundles reduces to linear algebra.
Proposition 11.4.12. Two torus bundlesMA andMA′ are diﬀeomorphic if
and only ifA′ is conjugate toA±1 in SL2(Z).
Proof. LetMA∼=MA′ be a diﬀeomorphism. Consider the toriT andT′ of
the two ﬁbrations both insideMA and minimise their transverse intersection.
If T∩T′ = ∅, by Proposition 9.3.18 the tori are parallel and the two
ﬁbrations are isotopic: henceA′ is conjugate toA±1. Otherwise by the same
propositionT′ decomposesintoﬁberedannuliintheproductlinebundle MA\T.
One such ﬁbered annulus identiﬁes a circleγ⊂T preserved byA. Therefore
A is conjugate to
(1e
0 1
)
or
(−1 e
0 −1
)
, andA′ is conjugate to
(1e′
0 1
)
or
(−1 e′
0 −1
)
for
the same reason. Exercise 11.4.11 implies thatA′ =A±1. □
11.4. SURFACE BUNDLES 363
Exercise 11.4.13. A matrix A ∈ SL2(Z) has ﬁnite order if and only if
A =±I or|trA|< 2. Every ﬁnite-orderA is conjugate to one of
(1 0
0 1
)
,
(−1 0
0 −1
)
,
(−1 1
−1 0
)
,
(0 −1
1 0
)
,
(1 −1
1 0
)
.
These matrices have order 1, 2, 3, 4, 6.
Hint. Use Proposition 2.3.9. □
We can easily determine whether a torus bundle is Seifert by looking at its
monodromyA.
Proposition 11.4.14. Let M = MA be a torus bundle with monodromy
A⁄=±I. The following holds:
• if|trA|< 2 thenM is a Seifert manifold withe = 0 andχ = 0,
• if|trA| = 2 thenM is a Seifert manifold withe⁄= 0 andχ = 0,
• if|trA|> 2 thenM is not a Seifert manifold.
Proof. ConsiderT× [−1, 1] foliated by lines{x}× [−1, 1]. The foliation
extendsto MA. IfAhasﬁniteorder, thenMA isﬁnitelycoveredby MI =T×S1
and hence all ﬁbers are compact. ThereforeMA is Seifert ﬁbered and covered
byT×S1, and we gete =χ = 0.
If|trA| = 2 then A is conjugate to
(±1 e
0 ±1
)
and we use Exercise 11.4.11.
Proposition 11.4.10 easily shows that all the Seifert manifolds that are torus
bundles are realised with|trA|⩽ 2, hence if|trA|> 2 the manifoldM is not
Seifert by Proposition 11.4.12. □
When|trA|> 2 we say that the monodromyA is Anosov.
11.4.6. Bundles withχ(Σ)< 0. Proposition 11.4.12 does not extend to
surfacebundleswith χ(Σ)< 0; indeeditmayhappenthatnon-conjugatemon-
odromies in MCG(Σ) give rise to diﬀeomorphic manifolds and understanding
when this happens is a hard problem.
Proposition 11.4.14 extends nevertheless and reﬂects the trichotomy of
mapping classes. Let Σ be a closed orientable surface withχ(Σ) < 0. Re-
call from Section 8.4 that every elementψ∈ MCG(Σ) is either ﬁnite order,
reducible, or pseudo-Anosov.
Proposition 11.4.15. Let Mψ be a surface bundle with ﬁbreΣ and mon-
odromyψ∈ MCG(Σ). The following holds:
• ifψ has ﬁnite order, thenMψ is Seifert withχ< 0 ande = 0,
• ifψ is reducible, thenMψ contains an essential torus,
• ifψ is pseudo-Anosov, thenMψ is simple and not Seifert.
Proof. Same proof as Proposition 11.4.14. Ifψ has ﬁnite order, it is an
isometry for some hyperbolic metric onΣ, and the line ﬁbration ofΣ× [−1, 1]
glues to a Seifert ﬁbration forMψ.
364 11. CONSTRUCTIONS OF THREE-MANIFOLDS
Ifψ is reducible there are disjoint essential simple closed curvesγ1,...,γ k
with ψ(γi ) = γi+1 cyclically; by gluing the annuliγi× [−1, 1] we get a torus
T⊂Mψ. It is essential because by cutting along it we still get a ﬁbration over
S1 with ﬁbers havingχ⩽ 0.
Ifψ ispseudo-Anosovtherearenoessentialtori T⊂Mψ, forbyminimising
T∩ Σ then Mψ\T would consist of essential annuli of typeγ× [−1, 1] and
henceψ would be reducible. The manifoldMψ is not Seifert because the ﬁbre
Σ would become a horizontal surface: thenM would be covered byΣ×S1
and henceψ would be of ﬁnite order. □
