---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-028-65-mapping-class-group
section_title: "Mapping class group"
section_number: 6.5
pages: 193-199
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Fix two essential multicurvesµ andη as in Figure 6.25. The ﬁgure easily
generalises to any genusg, and the reader may check thatµ andη subdivide
the surface into hexagons (or a single square wheng = 1). The important
point is thatSg\ (µ∪η) consists of polygons, none of which is a bigon.
By hypothesisϕ is homotopic to the identity, so the image multicurves
ϕ(µ) and ϕ(η) are curve by curve homotopic toµ and η. By Proposition
6.3.22 the multicurveϕ(µ) is isotopic toµ, andϕ(η) is isotopic toη.
The curvesµ and η are in minimal position because there are no bigons.
The imagesϕ(µ) and ϕ(η) are also in minimal position becauseϕ is a dif-
feomorphism. By Proposition 6.3.24 the supportsµ∪η and ϕ(µ∪η) are
ambiently isotopic, so we may suppose that they coincide.
The graphµ∪η is made of vertices (the intersectionsµ∩η) and edges.
The components ofµ andη are pairwise non-homotopic simple closed curves,
henceϕsendsnecessarilyeverycomponenttoitself, anditdoessoorientation-
preservingly by Proposition 6.3.6. This implies easily that vertices and edges
are sent to themselves byϕ. Hence ϕ = id on vertices and after an isotopy
we may suppose thatϕ = id on edges too.
After an isotopy we may also suppose thatϕ = id on a regular neigh-
bourhood U ofµ∪η, obtained by thickening the cellularisation ofµ∪η to a
handle decomposition with 0- and 1-handles. The complement ofU consists
of discs (the hexagons). Consider one such discD, enlarged a bit so that
∂D⊂ int(U). The mapϕ sends D to itself and is the identity on a collar of
∂D. By Theorem 6.4.1 and Remark 6.4.4 there is an isotopy connectingϕ to
id on every such discD that ﬁxes pointwise this collar, so we can extend it
constantly on the rest ofU and get a global isotopy onSg connectingϕ and
id. □
This theorem has important consequences in dimensions two and three.
6.5. Mapping class group
We have just proved that two self-diﬀeomorphisms ofSg are homotopic
if and only if they are isotopic. We have also seen that wheng = 0 there are
only two self-diﬀeomorphisms up to isotopy: the identity and a reﬂection. Do
we get a more complicated picture wheng> 1? Yes, we get an interesting
group, called themapping class groupof Sg. The group is naturally deﬁned
on all ﬁnite-type surfacesSg,b,p.
6.5.1. Deﬁnition.Recall that the ﬁnite-type orientable surfaceSg,b,p has
genusg, it hasb boundary components, andp punctures.
Deﬁnition 6.5.1. Themapping class groupofSg,b,p is the group
MCG(Sg,b,p ) = Diﬀeo +(Sg,b,p )/∼
186 6. SURFACES
where Diﬀeo+(Sg,b,p ) indicates the group of all orientation-preserving diﬀeo-
morphisms Sg,b,p → Sg,b,p that ﬁx pointwise the boundary andϕ∼ ψ if ϕ
andψ are connected by an isotopy that ﬁxes the boundary pointwise at every
level.
Example 6.5.2. The groupsMCG(S2) and MCG(D2) are trivial by Theo-
rems 6.4.1 and 6.4.5.
The group MCG(Sg,b,p ) acts onH1(Sg,b,p, Z) since homotopic functions
induce the same maps in homology. We get a group homomorphism
MCG(Sg,b,p )−→Aut+(
H1(Sg,b,p, Z)
)
= Aut+(
Zn)
= SLn(Z)
withn = 2g + max{b +p− 1, 0}. This homomorphism is neither injective nor
surjective in general. Its kernel is called theTorelli groupofSg,b,p.
The mapping class group of a sphere is trivial, so we look at the torus.
6.5.2. The torus. The mapping class group of the torus is a familiar
group of 2× 2 matrices.
Proposition 6.5.3. The Torelli group of the torusT is trivial and
MCG(T )∼= Aut+(H1(T )) = SL 2(Z).
Proof. Fix a meridianm and longitudel of T. A diﬀeomorphismϕ of T
that acts trivially onH1(T ) =π1(T ) = Z2 sendsm andl to two simple closed
curvesϕ(m) andϕ(l) homotopic and hence isotopic tom andl: the proof of
Theorem 6.4.7 shows thatϕ is isotopic to the identity. Therefore the Torelli
group is trivial.
A matrixA∈ SL2(Z) acts linearly onR2 preserving the orientation and the
lattice Z2 and hence descends to a self-diﬀeomorphism ofT = R2/Z2. This
shows that the mapMCG(T )→ Aut+(H1(T )) = SL 2(Z) is surjective. □
The mapping class group of a surfaceSg of genusg> 2 is not isomorphic
toafamiliargroupofmatrices, atleastasfarasweknow: indeed(exceptsome
low-genus cases) it is still unknown whetherMCG(Sg,b,p ) is linear, i.e. isomor-
phic to a subgroup ofGL(n, C) for some integern.
For the moment we content ourselves with a concrete description of some
particularly simple elements ofMCG(Sg,b,p ) called Dehn twists.
6.5.3. Dehn twists. Let γ be a non-trivial simple closed curve in the
interior ofSg,b,p. The Dehn twistalong γ is the elementTγ∈ MCG(Sg,b,p )
deﬁned as follows.
Pick a tubular neighbourhood ofγ orientation-preservingly diﬀeomorphic
to S1× [−1, 1] where γ lies asS1×{ 0}. Let f : [−1, 1]→ R be a smooth
function which is zero in
[
−1,− 1
2
]
and 2π on
[ 1
2, 1
]
. Let
Tγ :Sg,b,p−→Sg,b,p
6.5. MAPPING CLASS GROUP 187
Figure 6.26. A Dehn twist along a curveγ maps a transverse arcµ
onto an arc which makes a complete left turn.
be the diﬀeomorphism that acts on the tubular neighbourhood asTγ(eiα,t ) =
(ei(α+f (t)),t ) and on its complementary set inSg,b,p as the identity. We may
visualise Tγ by noting that it gives a complete left turn to any arcµ that
intersectsγ as in Figure 6.26.
Proposition 6.5.4. The element Tγ ∈ MCG(Sg,b,p ) is well-deﬁned and
depends only on the isotopy class ofγ.
Proof. In the deﬁnition ofTγ we have chosen a tubular neighbourhood for
γ and a smooth functionf. Tubular neighbourhoods are ambiently isotopic,
and functions with ﬁxed extremes are isotopic too: these facts imply easily
that the isotopy class ofTγ is well-deﬁned and depends only on the isotopy
class ofγ. □
Remark 6.5.5. To deﬁneTγ we needed the orientation ofSg,b,p, but not
an orientation forγ. A bit surprisingly, if we change the orientation ofγ the
elementTγ remains unaﬀected.
The inverseT−1
γ transforms every curveµ crossingγ via a completeright-
turn and is sometimes called anegative Dehn twist.
We construct some examples in the torusT. Let m and l be some ﬁxed
meridian and longitude on the orientedT forming a positive basis, so that
m·l = +1 and we get an identiﬁcationMCG(T ) = SL 2(Z).
Proposition 6.5.6. The Dehn twistsTm andTl are
Tm =
(1 −1
0 1
)
, T l =
(1 0
1 1
)
.
Proof. In homology we ﬁnd
Tm(m) =m, T m(l) =l−m, T l (l) =l, T l (m) =m +l.
The proof is complete. □
By Exercise 6.3.4 there is a unique non-separating simple closed curveγ
in Sg up to self-diﬀeomorphism for everyg≥ 1. Therefore the Dehn twists
Tγ along non-separating curves inSg are all conjugate inMCG(Sg). In the
torus case these can be easily identiﬁed algebraically.
188 6. SURFACES
a
b Ta Tb
Figure 6.27. Two curvesα(red) andβ (green) intersecting in one point
are related: we getα =Tβ(Tα(β)).
(1) (2)
a
b
g g
a
b
a
b
a
b
2g1
Figure 6.28. Pick two consecutive points inα (green) that intersectβ
(red). We can ﬁnd a third non-separating curveγ (blue) intersectingα
andβ in<k points. There are two cases (1) and (2): in (1) the curveγ
intersectsβ in one point and is hence non-separating, in (2) we have two
possibilitiesγ1,γ 2, and one is certainly non-separating sinceβ is.
Corollary 6.5.7. An element A ∈ SL2(Z) = MCG( T ) is a (positive or
negative) Dehn twist⇐⇒it is primitive andtrA = 2.
Proof. Every such matrix inSL2(Z) is conjugate to
(1±1
0 1
)
. □
Exercise 6.5.8. The Dehn twistsTm andTl generate MCG(T ).
We have seen that Dehn twists generateMCG(T ), while many elements
A∈ MCG(T ) are neither Dehn twists nor powers of Dehn twists (those with
trA⁄= 2). These two facts extend to higher-genus surfacesSg; we start by
generalising the ﬁrst.
6.5.4. Dehntwistsgenerate. Dehntwistsarebasicelementsinthemap-
ping class group, and we now prove that they generate the whole group. We
restrict ourselves for simplicity to compact surfacesSg,b.
Theorem 6.5.9.The group MCG(Sg,b) is generated by Dehn twists.
To prove the theorem we will need some preliminary facts. We say that
two non-separating simple closed curves in the interior ofSg,b are related if
there is a combination of isotopies and Dehn twists transforming the ﬁrst into
the second.
Lemma 6.5.10. The non-separating curves inSg,b are all related.
6.5. MAPPING CLASS GROUP 189
(2)
(1)
(3)
a
b
a
b
a
b
Figure 6.29. The arcsα(red) andβ (green) intersect at their endpoints
and maybe at somek interior points. Ifk = 0 and they are oriented as in
(1), a Dehn twist alongγ transformsβ intoα. If they are oriented as in
(2), a negative Dehn twist alongγ transforms this conﬁguration into (1).
Ifk >0 we look at the ﬁrst intersection point inα. If the orientations are
coherent as in (3) a Dehn twist alongγ decreases k. It the orientations
are not coherent we change them as in (2).
Proof. Let α and β be two non-separating curves. Up to isotopy they
intersect transversely into some k points. If k = 1 they are related by
a couple of Dehn twists as shown in Figure 6.27. If k = 0 , since they
are both non-separating, one sees easily that there is another curveγ with
i(α,γ ) = i(β,γ ) = 1 : hence α and β are both related toγ, so they are
related themselves. Ifk> 2 we can ﬁnd a curveγ intersectingα andβ trans-
versely into<k points as shown in Figure 6.28 and we proceed by induction
onk. □
We now considerSg,b with b> 2 and ﬁx two pointsp,q in two distinct
boundary components ofSg,b. We consider all the properly embedded arcs
in Sg,b with endpoints atp and q. As above, we say that two such arcs are
related if there is a combination of Dehn twists and isotopies transforming the
ﬁrst into the second.
Lemma 6.5.11.The arcs inSg,b with endpoints atp andq are all related.
Proof. Pick two arcsα andβ and put them into transverse position: they
intersect at their endpointsp and q and maybe transversely at somek other
points. Figure 6.29 shows that after isotopies and Dehn twists we getα =
β. □
190 6. SURFACES
We can ﬁnally prove Theorem 6.5.9.
Proof of Theorem 6.5.9. Letϕ be a self-diﬀeomorphism ofSg,b ﬁxing
pointwise the boundary. We prove thatϕ is generated by isotopies and Dehn
twists.
Weﬁrstprovethecase g = 0 byinductionon b. Weknowthat MCG(S0,1)
is trivial, so we supposeb> 2. Letp,q be points in distinct boundary compo-
nents ofS0,b, andα be an arc connecting them. All the arcs with endpoints
inp andq are related, and henceα andϕ(α) are. Therefore up to composing
with Dehn twists and isotopies we may suppose thatϕ is the identity ofα and
hence also on a tubular neighbourhood ofα. We cut S0,b along α and get
S0,b−1, withϕ transformed into a self-diﬀeomorphism ofS0,b−1. By induction
on b the newϕ is generated by Dehn twists and isotopies, so the originalϕ
also is.
We prove the caseg >0 by induction ong. Let α be a non-separating
simple closed curve. Since these are all related, up to isotopies and Dehn
twists we may suppose thatϕ is the identity onα; as above we can cutSg,b
alongα, getSg−1,b+2 and conclude by induction ong. □
6.5.5. Actiononsimpleclosedcurves. Wenowshowthateveryelement
ϕ∈ MCG(Sg) is determined by the way it permutes the (isotopy classes of)
simple closed curves inSg.
Proposition 6.5.12.The action ofϕ∈ MCG(Sg) on the isotopy classes of
simple closed curves is faithful.
Proof. TheproofofTheorem6.4.7showsthatif ϕﬁxestheisotopyclasses
of two essential multicurvesµ and η as in Figure 6.25 then it is isotopic to
the identity. □
Recall that every simple closed curve is oriented by assumption: if we
considered unoriented simple closed curves the proposition would be false,
because in low genus there are someϕ that send every curve to its inverse:
this happens for instance with the map−I∈ SL2(Z) = MCG(T ).
6.5.6. References. The main source for this chapter is the book of Farb
– Margalit [18], which contains a lot more information on the mapping class
group of surfaces. We have also consulted Benedetti – Petronio [4] and Thur-
son’s notes [56] and book [57], in particular for Smale’s Theorem, that was
originally proved in [54].
CHAPTER 7
Teichmüller space
We have discovered in Chapter 6 that every surfaceSg of genusg> 2
can be equipped with a hyperbolic metric, and we have already noticed that
this metric is not unique: this chapter is entirely devoted to studying this
non-uniqueness phenomenon.
It turns out thatSg admits a continuous family of non-equivalent hyper-
bolic metrics, that form altogether a nice topological space called theTe-
ichmüller space of Sg. We prove in his chapter that the Teichmüller space
of Sg is homeomorphic to an open ball of dimension6g− 6. To prove this
fact we will introduce and study concepts likelength functions, earthquakes,
and Fenchel–Nielsen coordinates. The simple closed curves and their geodesic
representatives will play a fundamental role in all the discussion.
