---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-001-11-differential-topology
section_title: "Differential topology"
section_number: 1.1
pages: 17-23
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Figure 1.2. The tangent space inx may be deﬁned as the set of all
curves γ with γ(0) = x seen up to an equivalent relation that identiﬁes
two curves having (in some chart) the same tangent vector atx. This
condition is chart-independent.
Deﬁnition 1.1.3. A mapf : M→ M′ between diﬀerentiable manifolds is
smooth if it is smooth when read locally through charts. This means that for
everyp∈M there are two charts(Ui,ϕi ) ofM and (U′
j,ϕ′
j ) ofN withp∈Ui
andf (p)∈U′
j such that the compositionϕ′
j◦f◦ϕ−1
i is smooth wherever it is
deﬁned.
A diﬀeomorphismis a smooth mapf : M → M′ that admits a smooth
inverse g : M′→ M. A curve in M is a smooth mapγ : I→ M deﬁned on
some open intervalI of the real line, which may be bounded or unbounded.
Deﬁnition 1.1.4. A diﬀerentiable manifold isoriented if it is equipped with
an atlas where all transition functions are orientation-preserving (that is, the
determinant of their diﬀerential at any point is positive).
A manifold which can be oriented is calledorientable.
1.1.2. Tangent space. Let M be a diﬀerentiable manifold of dimension
n. We may deﬁne for every pointp∈M a n-dimensional vector spaceTpM
called thetangent space.
Thespace TpM maybedeﬁnedbrieﬂyasthesetofallcurves γ : (−a,a )→
M suchthat γ(0) =panda> 0isarbitrary,considereduptosomeequivalence
relation. The relation is the following: we identify two curves that, read on
some chart (Ui,ϕi ), have the same tangent vector atϕi (p). The deﬁnition
does not depend on the chart chosen.
AchartidentiﬁesTpM withtheusualtangentspace Rn atϕi (p)intheopen
setVi =ϕi (Ui ). Two distinct chartsϕi andϕj provide diﬀerent identiﬁcations
with Rn, which diﬀer by a linear isomorphism: the diﬀerentialdϕji of the
transition map ϕij. The structure of TpM as a vector space is then well-
deﬁned, while its identiﬁcation withRn is not.
10 1. PRELIMINARIES
Every smooth mapf :M→N between diﬀerentiable manifolds induces at
each pointp∈M a linear mapdfp :TpM→Tf (p)N between tangent spaces
in the following simple way: the curveγ is sent to the curvef◦γ.
Deﬁnition 1.1.5. A smooth mapf :M→N is alocal diﬀeomorphismat
a point p ∈ M if there are two open setsU ⊂ M and V ⊂ N containing
respectivelyp andf (p) such thatf|U :U→V is a diﬀeomorphism.
The inverse function theorem inRn implies easily the following fact, that
demonstrates the importance of tangent spaces.
Theorem 1.1.6. Let f : M→ N be a smooth map between manifolds of
the same dimension. The map is a local diﬀeomorphism atp∈M if and only
if the diﬀerentialdfp :TpM→Tf (p)N is invertible.
In this theorem a condition satisﬁed at a single point (diﬀerential invertible
atp) implies a local property (local diﬀeomorphism). Later on, we will see that
in Riemannian geometry a condition satisﬁed at a single point may also imply
a global property.
If γ : I→ M is a curve, itsvelocity γ′(t) in t∈ I is the tangent vector
γ′(t) = dγt(1). Here “1” means the vector 1 in the tangent spaceTtI = R.
We note that the velocity is a vector and not a number: the modulus of a
tangent vector is not deﬁned in a diﬀerentiable manifold (because the tangent
space is just a real vector space, without a norm).
1.1.3. Diﬀerentiable submanifolds.Let N be a diﬀerentiable manifold
of dimensionn.
Deﬁnition 1.1.7. A subsetM⊂N is adiﬀerentiable submanifoldof dimen-
sion m⩽n if everyp∈M has an open neighbourhoodU⊂N diﬀeomorphic
to an open setV ⊂ Rn via a mapϕ:U→V that sendsU∩M onto V∩L,
whereL is a linear subspace of dimensionm.
The pairs{(U∩M,ϕ|U∩M)}form an atlas forM, which inherits a structure
of m-dimensional diﬀerentiable manifold. At every pointp∈ M the tangent
spaceTpM is a linear subspace ofTpN.
1.1.4. Fibre bundles. We introduce an important type of smooth maps.
Deﬁnition 1.1.8. Asmooth ﬁbre bundleis a smooth map
π :E−→B
such that every ﬁbreπ−1(p) is diﬀeomorphic to a ﬁxed manifoldF and π
looks locally like a projection. This means thatB is covered by open setsUi
equipped with diﬀeomorphismsψi :Ui×F→π−1(Ui ) such thatπ◦ψi is the
projection on the ﬁrst factor.
1.1. DIFFERENTIAL TOPOLOGY 11
Themanifolds E andB arecalledthe total andbasemanifold, respectively.
The manifoldF is theﬁbreof the bundle. Asection of the bundle is a smooth
map s : B→ E such thatπ◦s = idB. Two ﬁbre bundlesπ : E→ B and
π′ :E′→B are isomorphic if there is a diﬀeomorphismψ :E→E′ such that
π =π′◦ψ.
1.1.5. Vector bundles.A smooth vector bundleis a smooth ﬁbre bundle
where every ﬁbreπ−1(p) has the structure of a n-dimensional real vector
space which varies smoothly withp. Formally, we require thatF = Rn and
ψi (p,·) :F → π−1(p) be an isomorphism of vector spaces for everyψi as
above.
The zero-section of a smooth vector bundle is the sections :B→E that
sendsp tos(p) = 0, the zero in the vector spaceπ−1(p). The images(B) of
the zero-section is typically identiﬁed withB vias.
Two vector bundles areisomorphic if there is a diﬀeomorphismψ as above,
which restricts to an isomorphism of vector spaces on each ﬁbre. As every
manifold here is diﬀerentiable, likewise every bundle will be smooth and we will
hence often omit this word.
1.1.6. Tangent and normal bundle.LetM be a diﬀerentiable manifold
of dimensionn. The union of all tangent spaces
TM =
⋃
p∈M
TpM
is naturally a diﬀerentiable manifold of double dimension2n, called thetangent
bundle. The tangent bundleTM is naturally a vector bundle overM, the ﬁbre
overp∈M being the tangent spaceTpM.
LetM⊂N be a smooth submanifold ofN. The normal spaceat a point
p∈M is the quotient vector spaceνpM =TpN/TpM. Thenormal bundleνM
is the union
νM =
⋃
p∈M
νpM
and is also naturally a smooth vector bundle overM. The normal bundle is not
canonically contained inTN like the tangent bundle, but (even more usefully)
it may be embedded directly inN, as we will soon see.
1.1.7. Vector ﬁelds.A vector ﬁeldX on a smooth manifoldM is a sec-
tion of its tangent bundle. A point p and a vector v ∈ TpM determine
an integral curve α: I → M starting fromv, that is a smooth curve with
α(0) = p,α′(0) = v, and α′(t) = X(α(t)) for allt ∈ I. The curve α is
unique if we require the intervalI to be maximal. It depends smoothly onp
andv.
12 1. PRELIMINARIES
1.1.8. Immersionsandembeddings. Asmoothmap f :M→N between
manifolds is animmersion if its diﬀerential is everywhere injective: note that
this does not imply thatf is injective. The map is anembedding if it is a
diﬀeomorphism onto its image: this means thatf is injective, its image is a
submanifold, andf :M→f (M) is a diﬀeomorphism.
Theorem 1.1.9. IfM is compact, every injective immersionf :M→N is
an embedding.
1.1.9. Isotopy and ambient isotopy.LetX andY be topological spaces.
We recall that ahomotopy between two continuous mapsϕ,ψ :X→Y is a
continuous mapF : X× [0, 1]→ Y such thatF0 = ϕ and F1 = ψ, where
Ft =F (·,t ).
LetM andN be diﬀerentiable manifolds. Asmooth isotopybetween two
embeddingsϕ,ψ :M→N is a smooth homotopyF between them, such that
every mapFt is an embedding. Again, we will shortly use the wordisotopy to
mean a smooth isotopy. We note that many authors do not require an isotopy
to be smooth, but we do.
Being isotopic is an equivalence relation for smooth mapsM→ N: two
isotopiesFt andGu can be glued ifF1 =G0, and since we want a smooth map
we priorly modifyF and G so that they are constant neart = 1 and u = 0.
This can be done easily by reparametrisingt andu.
An ambient isotopy on N is an isotopy betweenidN and some other dif-
feomorphism ϕ: N → N, such that every level is a diﬀeomorphism. Two
embeddings ϕ,ψ : M→ N are ambiently isotopic if there is an ambient iso-
topyF ofN such thatψ =F1◦ϕ.
Theorem 1.1.10. If M is compact, two embeddingsϕ,ψ : M → N are
isotopic if and only if they are ambiently isotopic.
1.1.10. Tubular neighbourhood. Let M ⊂ N be a diﬀerentiable sub-
manifold. A tubular neighbourhood of M is an open subsetU ⊂ N with a
diﬀeomorphismνM→U sending identically the zero-section ontoM.
Theorem 1.1.11. Let M⊂ N be a closed diﬀerentiable submanifold. A
tubular neighbourhood forM exists and is unique up to an isotopy ﬁxingM
and up to pre-composing with a bundle isomorphism ofνM.
If we are only interested in the open setU and not its parametrisation, we
can of course disregard the bundle isomorphisms ofνM.
Vectorbundlesarehenceuseful(amongotherthings)tounderstandneigh-
bourhoods of submanifolds. Since we will be interested essentially in manifolds
of dimension at most 3, two simple cases will be important.
Proposition 1.1.12. A connected compact manifoldM has a unique line
bundleE→M up to isomorphism with orientable total spaceE.
1.1. DIFFERENTIAL TOPOLOGY 13
The orientable line bundle onM is a productM× R precisely whenM
is also orientable. IfM is not orientable, the unique orientable line bundle is
indicated byM×∼ R.
Proposition 1.1.13. For everyn, there are exactly two vector bundles of
dimensionn overS1 up to isomorphism, one of which is orientable.
Again, the orientable vector bundle isS1× Rn and the non-orientable one
is denoted byS1×∼ Rn. These simple facts allow us to fully understand the
possibleneighbourhoodsofcurvesinsurfaces, andofcurvesandsurfacesinside
orientable 3-manifolds.
1.1.11. Manifolds with boundary.Let adiﬀerentiable manifoldM with
boundary be a topological space with charts on a ﬁxed half-space ofRn instead
of Rn, forming a smooth atlas. (By deﬁnition, maps from subsets ofRn are
smooth if they locally admit extensions to smooth functions deﬁned on open
domains.)
The points corresponding to the boundary of the half-space form a subset
of M denoted by∂M and calledboundary. The boundary of an-manifold is
naturally a(n− 1)-dimensional manifold without boundary. Theinterior ofM
isM\∂M.
We can deﬁne the tangent spaceTpM at a pointp∈∂M as the set of all
curves inM starting from or arriving top, with the same equivalence relation
as above. The space TpM is a vector space that contains the hyperplane
Tp∂M. Most of the notions introduced for manifolds extend in an appropriate
way to manifolds with boundary. Asubmanifold of a manifold with boundary
M is the image of an embeddingN ↪→M, whereN is another manifold with
boundary.
The most important manifold with boundary is certainly thedisc
Dn =
{
x
⏐⏐‖x‖⩽ 1
}
⊂ Rn.
Moregenerally, adisc ina n-manifoldN isasubmanifold D⊂N withboundary
diﬀeomorphic toDn. Since a disc is in fact a (closed) tubular neighbourhood
of any point in its interior, the uniqueness of tubular neighbourhoods implies
the following.
Theorem 1.1.14 (Cerf – Palais).Let N be connected and oriented. Two
orientation-preserving embeddingsf,g :Dn→ int(N) are ambiently isotopic.
Aboundary componentN ofM is a connected component of∂M. Acollar
for N is an open neighbourhood diﬀeomorphic toN× [0, 1). As for tubular
neighbourhoods, every compact boundary component has a collar, unique up
to isotopy.
A closed manifoldis a compact manifold without boundary.
14 1. PRELIMINARIES
1.1.12. Cut and paste. If M ⊂ N is a closed and orientable(n− 1)-
submanifold in the interior of an orientablen-manifold N, it has a tubular
neighbourhood diﬀeomorphic toM× R. The operation ofcutting N alongM
consists of the removal of the portionM× (−1, 1). The resulting manifoldN′
has two new boundarycomponentsM×{−1}andM×{1}, both diﬀeomorphic
to M. By the uniqueness of the tubular neighbourhood, the manifold N′
depends (up to diﬀeomorphisms) only on the isotopy class ofM⊂N.
LetM andN be connected. The submanifoldM is separating if its com-
plement consists of two connected components. The cut manifold has two or
one components depending on whetherM is separating or not.
Conversely, letM andN ben-manifolds with boundary, and letϕ:∂M→
∂N be a diﬀeomorphism. It is possible toglue M andN alongϕ and obtain a
newn-manifold as follows.
A naïve approach would consist in taking the topological spaceM⊔N and
identifyp withϕ(p) for allp∈∂M. The resulting quotient space is indeed a
topological manifold, but the construction of a smooth atlas is not immediate.
A quicker method consists of taking two collars∂M× [0, 1) and ∂N× [0, 1)
of the boundaries and then consider the topological space
(M\∂M )⊔ (N\∂N ).
Now we identify the points(p,t ) and (ϕ(p), 1−t) of the open collars, for all
p∈∂M and allt∈ (0, 1). Having now identiﬁed twoopen subsets ofM\∂M
andN\∂N, a diﬀerentiable atlas for the new manifold is immediately derived
from the atlases ofM andN.
Proposition 1.1.15.The resulting smooth manifold depends (up to diﬀeo-
morphism) only on the isotopy class ofϕ.
1.1.13. Connected sum. We introduce an important cut-and-paste op-
eration. The connected sum of two connected orientedn-manifolds M and
M′ is a newn-manifold obtained by choosing twon-discs D⊂ int(M) and
D′⊂ int(M′) and an orientation-reversing diﬀeomorphismϕ:D→ D′. The
new manifold is constructed in two steps: we ﬁrst remove the interiors ofD
and D′ from M⊔M′, thus creating two new boundary components∂D and
∂D′, and then glue these boundary components alongϕ|∂D. See Figure 1.3.
We denote the resulting manifold by M#M′. Since ϕ is orientation-
reversing, themanifoldM#M′ isorientedcoherentlywith M andM′. Theorem
1.1.14 implies the following.
Proposition 1.1.16. The oriented smooth manifoldM#M′ depends (up
to diﬀeomorphism) only onM and M′. The connected sum operation # is
commutative, associative, andSn serves as the identity element.
We can invert a connected sum as follows. Suppose a n-manifold M
contains a separating (n− 1)-sphere N⊂ int(M). We ﬁx a diﬀeomorphism
