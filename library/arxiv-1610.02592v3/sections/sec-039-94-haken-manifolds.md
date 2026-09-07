---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-039-94-haken-manifolds
section_title: "Haken manifolds"
section_number: 9.4
pages: 302-311
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
There are two classes of irreducible closed three-manifolds: those that
contain incompressible surfaces, and those that do not. Both classes are very
important and contain a wealth of interesting manifolds.
The manifolds belonging to the ﬁrst class are calledHaken manifoldsand
are somehow easier to study, because they can be cut into balls via a standard
procedure called hierarchy: we cut the manifold along an essential surface,
thenalonganother, andweiterateuntilwegetballs. Westudythesemanifolds
here. We also prove the converse of Proposition 9.3.4, that is that a closed
surface is incompressible if and only if it isπ1-injective, see Theorem 9.4.14.
9.4.1. Introduction. If not otherwise mentioned, all the 3-manifoldsM
we will consider in this section will be connected, compact, oriented and with
(possibly empty) boundary. We introduce a deﬁnition.
Deﬁnition 9.4.1. AHaken manifoldis a compact, connected, oriented 3-
manifoldM with (possibly empty) boundary, which is irreducible,∂-irreducible,
and contains an incompressible and∂-incompressible surface.
The reader should not be frightened by the abundance of adjectives: this
deﬁnition is really clever because it summarises various reasonable hypothesis
in a unique word. The rest of this chapter is mainly devoted to the study of
Haken manifolds. We start by looking at their boundaries.
Proposition 9.4.2. Every boundary componentX of a Haken manifoldM
hasχ(X)⩽ 0 and is incompressible.
Proof. No componentX of∂M is a sphere: if it were so, it would bound
a ballB and we would haveM = B, contradicting Corollary 9.3.13. Hence
χ(X)⩽ 0 andX is incompressible becauseM is∂-irreducible. □
We now prove that there are plenty of Haken manifolds. We start with a
general proposition.
Proposition 9.4.3. Let M be an oriented, compact, irreducible, and∂-
irreducible 3-manifold with (possibly empty) boundary. Every non-trivial ho-
mology classα∈H2(M,∂M ; Z) is represented by a disjoint union of incom-
pressible and∂-incompressible oriented surfaces.
Proof. Every classα is represented by a properly embedded oriented sur-
face S by Proposition 1.7.16. A compression as in Figure 9.8 and 9.9 does
not alter the homology class of the surface: indeed in homology we have
S′−S =∂B whereB =D× [−1, 1] is a tubular neighbourhood of the com-
pressing discD. Hence [S′] = [S] =α.
We compressS until its connected components are either incompressible
and ∂-incompressible surfaces, discs, or spheres. SinceM is irreducible and
9.4. HAKEN MANIFOLDS 295
∂-irreducible, discs and spheres bound balls and are hence homologically trivial,
so they can be removed. □
Corollary 9.4.4.LetM beoriented, compact, irreducible, and∂-irreducible.
IfH2(M,∂M ; Z)⁄={e} thenM is Haken.
Corollary 9.4.5.LetM beoriented, compact, irreducible, and∂-irreducible.
If∂M⁄= ∅ andM⁄=B, thenM is Haken.
Proof. If ∂M contains a sphere, it bounds a ballB and henceM = B.
Otherwise H1(∂M ) has positive rank, and henceH2(M,∂M ) = H1(M) also
has positive rank by Corollary 9.1.5. □
We recall that every compact orientable 3-manifold decomposes along
spheres and disc into irreducible and∂-irreducible pieces. If one such piece has
non-empty boundary then either it is ball, or it is Haken.
The following lemma will be useful soon. It says that every Haken manifold
contains an interesting “spanning” surfaceS, that touches all the boundary
components (the spanning surface need not to be connected).
Lemma 9.4.6. Every Haken manifoldM contains an oriented surfaceS,
whose components are incompressible and∂-incompressible, such that[∂S∩
X]∈H1(X, Z) is non-trivial for every boundary componentX ofM.
Proof. We have∂M =X1⊔...⊔Xk withχ(Xi )⩽ 0 for alli. Proposition
9.1.4 says that the image of
∂ :H2(M,∂M, Z)−→H1(∂M, Z)
is a lagrangian subgroupL of maximal rank. We have
H1(∂M, Z) =⊕k
i=1H1(Xi, Z).
The decomposition is orthogonal with respect to the symplectic intersection
form ω. There is an α ∈ L whose projection to each H1(Xi, Z) is non-
trivial: if not, the space L would be ω-orthogonal to someH1(Xi, Z) and
hence contained in a smaller symplectic subspace, a contradiction sinceL has
maximal rank. Pick any incompressible and∂-incompressible surfaceS such
that∂[S] =α. □
9.4.2. Normal surfaces. On Haken manifolds, incompressible surfaces
are eﬃciently detected by normal surfaces.
Proposition 9.4.7.LetM be Haken andT be a triangulation forM. Every
compact surface S ⊂ M whose components are all incompressible and∂-
incompressible is isotopic to a normal surface.
Proof. We know thatS becomes normal after surgeries as in Figure 9.8 or
Figure 9.9. These surgeries are actually isotopies sinceS is incompressible and
∂-incompressible, andM is irreducible and∂-irreducible (see Figure 9.16).□
296 9. TOPOLOGY OF THREE-MANIFOLDS
Note that in the proof of Proposition 9.4.7, as in many other proofs, it
is crucial thatM be irreducible and∂-irreducible. We can now apply Lemma
9.2.27 to get the following.
Corollary 9.4.8. Let M be a Haken manifold. There is a K > 0 such
that every setS of pairwise disjoint and non-parallel incompressible and∂-
incompressible surfaces inM consists of at mostK elements.
Our aim is now to cut a Haken manifold iteratively along incompressible
and∂-incompressible surfaces. The two-dimensional analogue to keep in mind
is the following: every surfaceSg of genus> 2 can be cut into pairs-of-pants;
a pair-of-pants is a quite simple surface, but we are still not satisﬁed and
we further cut it along three arcs into two discs (two hexagons). We have
constructed a two-step decomposition ofSg into discs: this is what we would
like to extend from two to three dimensions.
9.4.3. Cutting along surfaces.When we cut a 3-manifold along an in-
compressible surface, some nice properties of the manifold are preserved.
Proposition 9.4.9.LetM be compact and irreducible, andS⊂M be either
an essential disc or an incompressible surface. LetM′ be obtained by cutting
M alongS. The following holds:
• the manifoldM′ is irreducible;
• a closed Σ⊂M′ is incompressible inM′⇐⇒it is so inM.
Proof. We prove thatM′ is irreducible. LetΣ⊂M′ be a sphere. SinceM
is irreducible, the sphereΣ bounds a ballB⊂M. The ballB cannot contain
S because all surfaces in a ball are compressible. ThereforeB⊂M′ and M′
is irreducible.
To prove the second assertion, we show thatΣ has a compressing disc
D in M if and only if it has one inM′. If D lies inM′ then of course it lies
also inM. Conversely, supposeD lies inM. PutD in transverse position with
respect toS and pick an innermost intersection circle inD, bounding a disc
D′⊂D. SinceD′ cannot compressS, and sinceM is irreducible, the discD′
can be isotoped away fromS. This simpliﬁesD∩S and after ﬁnitely many
steps we getD∩S = ∅ and henceD⊂M′. □
Corollary 9.4.10.If we cut a Haken 3-manifold along a closed incompress-
ible surface, we get a disjoint union of Haken 3-manifolds.
The following consequence is also interesting.
Corollary 9.4.11. Let M be compact with non-empty boundary. IfM is
irreducible, then either it is a handlebody or it contains a closed incompressible
surface.
9.4. HAKEN MANIFOLDS 297
Proof. The manifoldM decomposes along essential discs into manifolds
M1,...,M k that are irreducible and∂-irreducible. If everyMi is a ball thenM
is a handlebody. IfMi is not a ball, the closed surfaceS =∂Mi is not a sphere
and is incompressible inMi, and hence also inM by Proposition 9.4.9. □
9.4.4. Hierarchies. We want to use incompressible surfaces to cut every
Haken manifold into simpler pieces. The procedure goes as follows.
A hierarchy for a Haken 3-manifoldM is a sequence of 3-manifolds
M =M0
S0
↝M1
S1
↝M2
S2
↝...
Sh−1
↝ Mh
where eachMi+1 is obtained cuttingMi along a properly embedded (possibly
disconnected) surfaceSi⊂Mi, such that the following holds:
• every component of Si is an incompressible and ∂-incompressible
surface or an essential disc, for alli;
• the ﬁnal manifoldMh consists of balls.
The numberh is theheight of the hierarchy. We now show that every Haken
manifold can be “atomised” into balls in three steps.
Theorem 9.4.12.Every Haken manifold has a hierarchy of height3.
Proof. Let S0 be a maximal family of pairwise disjoint and non-parallel
closed incompressible surfaces inM, which exists by Corollary 9.4.8. We cut
M0 =M alongS0 and getM1.
Every connected componentMi
1 of M1 is Haken by Corollary 9.4.10. By
Lemma 9.4.6 for everyi there is a “spanning” surfaceSi
1⊂ Mi
1 made of in-
compressible and∂-incompressible components that intersects every boundary
component ofMi
1. We cutM1 along the spanningS1 =⊔Si
1 and get a new
manifoldM2.
We now prove thatM2 contains no closed incompressible surface. Indeed,
if Σ⊂M2 were closed and incompressible, then it would be so also inM by
Proposition 9.4.9. Since S0 is maximal, the surface Σ would be parallel to
a component ofS0, that is it would cobound aΣ× [0, 1] with it. Since the
spanning surfaceS1 intersects all the boundary components ofM1, a compo-
nent ofS1 would be contained inΣ× [0, 1] and would intersect the boundary
only on the side ofS0: this is excluded by Proposition 9.3.18 (products do
not contain incompressible and∂-incompressible surfaces with boundary only
on one side).
Every component ofM2 is a handlebody by Corollary 9.4.11. We cut it
along a setS2 of essential discs to get balls. □
Hierarchies may be used to prove theorems on Haken manifolds. We will
now use them to prove that incompressible surfaces must beπ1-injective: we
need a preliminary discussion and a lemma.
298 9. TOPOLOGY OF THREE-MANIFOLDS
S2
S0
S1
S2S1
S0
Figure 9.20. The strataS0,S1, andS2 intersect in vertices (left). The
boundary of each ballB⊂ M2 is tessellated into domains belonging to
S0,S 1, orS2. Three of them intersect at a 3-valent vertex (right).
γ γ
D
γ γ
D
γ γ
D
Figure 9.21. Ifγ intersects at most three domains, it bounds a discD
intersecting only these domains, as shown here.
In our hierarchy of height3, the surfaces inS0 are closed, the spanning
surfaces inS1 have boundary, andS2 consists of discs. To simplify notations,
we redeﬁneS0 as∂M∪S0.
It is convenient to consider all the surfacesS0, S1, and S2 inside M,
without cuttingM along them. With this perspective∂S1 is glued toS0 and
∂S2 is glued toS0∪S1, via transverse maps. Every intersectionS0∩S1∩S2
is a vertex as in Figure 9.20-(left). The spaceX = S0∪S1∪S2 is a two-
dimensional cell complex whose complement inM is a union of open balls:
such an objectX is usually called aspine forM.
We say that our hierarchy of height3 is minimal if the essential discs in
S2 are chosen to minimise the total number of vertices. We can of course
suppose that the hierarchy is minimal.
The ﬁnal manifoldM3 is the abstract closure ofM\ (S0∪S1∪S2) and
consists of balls. The boundary of every such ballB is tessellated into domains
belonging toS0, S1, orS2. Three domains intersect at 3-valent vertices as
9.4. HAKEN MANIFOLDS 299
γ γ
D
γ
D
Figure 9.22. By minimality the region inS2 is incident to a single vertex
and we can slideγ through it. Then we resume to thek = 2 case.
in Figure 9.20-(right). We say thatB is essential if every simple closed curve
γ ⊂ ∂B transverse to the tessellation and intersecting⩽ 3 domains is the
boundary of a discD⊂∂B intersecting only these domains: see Figure 9.21.
Lemma 9.4.13. If the hierarchy is minimal, every ball inM3 is essential.
Proof. Let γ ⊂ ∂B intersect k ⩽ 3 domains. The curve γ obviously
bounds a properly embedded discD′ ⊂ B. If k = 1, the curve is entirely
contained inSi for somei. SinceS0 andS1 are incompressible andS2 consists
of discs, the curveγ bounds a discD also inSi. Since S1 is incompressible
and S2 consists of essential discs, the boundary components ofSj with j >i
are not attached in the interior ofD, soD is entirely contained in the domain
containingγ and we are done.
Ifk = 2, the curveγ is contained inSi∪Sj for somei <j. If (i,j ) = (0, 1)
weusethat S1 is∂-incompressibletogetadisc D asinFigure9.21-(top-right).
Ifj = 2, thenγ cuts a disc inS2 into two discsD1∪D2.
We have three half-discsD′,D 1,D 2 intersecting in an arc, all contained
in a handlebodyH⊂M2. Recall thatH\S2 consists of balls. If we replace
D1∪D2 by eitherD1∪D′ orD2∪D′ (say, the ﬁrst) we still get a disc system
that cutsH into balls, and hence another hierarchy. By minimalityD2 =D is
adjacent to no vertices,i.e. it is as in Figure 9.21-(top-right) and we are done.
The casek = 3 is analogous: the curveγ cuts a disc inS2 into two parts
D1∪D2 and we may replace it withD1∪D′. By minimalityD2 is incident
to at most one vertexv: we isotopeγ throughv as in Figure 9.22, and then
conclude using thek = 2 case. □
9.4.5. Dehn’s Lemma.Proposition 9.3.4 says that an orientable con-
nected properly embeddedπ1-injective surfaceS⊂ M with χ(S)⩽ 0 is in-
compressible. We can ﬁnally prove the converse, at least for closed surfaces.
The following result is often proved as a corollary of a famous topological
fact called theDehn Lemma. We do not state Dehn’s Lemma here, and we
prove directly the following using hierarchies.
Theorem 9.4.14.LetM be a compact oriented 3-manifold. A connected
oriented closedS ⊂ M with χ(S)⩽ 0 is incompressible if and only if the
induced mapi∗ :π1(S)→π1(M) is injective.
300 9. TOPOLOGY OF THREE-MANIFOLDS
1
1
2
1
1
1
1
2
2
1
Figure 9.23. The counterimage ofS0∪S1∪S2 alongf. An edge with
label i goes to Si (unlabelled edges go toS0). Here there is a 0-gon
(yellow) and three2-gons (green). The correct notion ofk-gon should be
clear from the picture.
Proof. We know one implication from Proposition 9.3.4; here we suppose
thatS incompressible and prove thati∗ :π1(S)→π1(M) is injective.
The decomposition ofM into irreducible and∂-irreducible factors is made
by cutting M along essential spheres and discs transverse toS. Since S
is incompressible, we may surgerS along these spheres and discs without
altering i∗, so thatS is disjoint from them and hence contained in a single
factor. Therefore we may supposeM is irreducible and∂-irreducible.
NowM containstheincompressible S andishenceHaken. Theorem9.4.12
furnishes a hierarchy of height⩽ 3. We may suppose thatS0 is a maximal
system of closed incompressible surfaces containingS and that the hierarchy
is minimal. The balls inM3 are essential by Lemma 9.4.13.
Suppose by contradiction thati∗ is not injective: there is a loopγ :S1→S
which is homotopically trivial inM but not inS. The triviality inM furnishes
a continuous mapf :D2→M which extendsγ. We homotopef to a smooth
map, transverse to all the strata ofS0∪S1∪S2.
By transversality, the counterimagef−1(S0∪S1∪S2) is a graph inD2 as
in Figure 9.23, which dividesD2 into regions. The graph is itself a hierarchy,
with edges of type 0, 1, 2 attached iteratively. An easy Euler characteristic
argument shows that at least one regionR is ak-gon withk⩽ 3, see Figure
9.23. The regionR is mapped inside a ballB⊂M3, and∂R is mapped to an
immersed curveα⊂∂B intersectingk⩽ 3 domains of the tessellated∂B.
Since B is essential, the curveα is of one of the types shown in Figure
9.24. In all cases we may slide the discf (R) away fromB and decrease the
number of regions inD by destroyingR. After ﬁnitely many homotopies of this
kind we getf (D)∩ (S0∪S1∪S2) = ∅ and hencef (D) is entirely contained
in a ballB⊂M3. Thereforeγ is trivial inS, a contradiction. □
9.4. HAKEN MANIFOLDS 301
α α α
Figure 9.24. The immersed curveα intersects k ⩽ 3 regions and is
hence of one of these types (becauseB is essential).
Corollary 9.4.15.The fundamental group of a Haken manifold is inﬁnite.
Proof. It contains the fundamental group of a closed surface withχ⩽ 0,
which is inﬁnite. □
Corollary 9.4.16.Elliptic 3-manifolds are not Haken.
We will see in the subsequent chapters that every ﬂat 3-manifold is Haken.
Hyperbolic 3-manifolds may or may not be Haken.
9.4.6. Essential surfaces. Topologists sometimes use the term “essen-
tial” to summarise various reasonable notions in a single word. We already
know what an essential disc or sphere is (see Section 9.2.11) and we now turn
to surfaces with non-positive Euler characteristic.
Let M be a compact oriented three-manifold andS⊂ M be a properly
embedded connected compact surface withχ(S) ⩽ 0. We say that S is
essential if it is incompressible,∂-incompressible, and not∂-parallel.
9.4.7. Simple manifolds. Let M be irreducible and ∂-irreducible. We
introduce yet some more deﬁnitions. We say that
• M is atoroidal if it does not contain essential tori,
• M is acylindrical if it does not contain essential annuli.
Finally, the manifoldM is simple if it is atoroidal and acylindrical. We can
summarise this deﬁnition as follows:
Deﬁnition 9.4.17. A compact oriented 3-manifoldM with (possibly empty)
boundary issimple if it does not contain any essential sphere, disc, torus, or
annulus.
Many examples come from elliptic and hyperbolic geometry:
Proposition 9.4.18. Every closed elliptic or hyperbolic 3-manifoldM is
simple.
Proof. We know thatM is irreducible. The manifoldM does not contain
incompressible tori becauseπ1(M) does not containZ×Z: ifM is elliptic then
π1(M) is ﬁnite, if it is hyperbolic we use Corollary 4.2.5. □
302 9. TOPOLOGY OF THREE-MANIFOLDS
The ﬂat geometry is an exception: the three-torusS1×S1×S1 contains
many incompressible tori and is hence not simple. For instance, the two-torus
S1×S1×p is incompressible (because it isπ1-injective).
Our next goal will be to decompose every irreducible and∂-irreducible
manifold M along some canonical set of essential tori and annuli into some
pieces. These pieces will be either simple, or belong to a particular class: the
Seifert manifolds. We introduce this class in the next chapter.
9.4.8. References. The main sources that we have used for this chapter
are an unﬁnished book of Hatcher [26] and Fomenko–Matveev [20]. The proof
of Theorem 9.4.14 through hierarchies is due to Aitchison and Rubinstein [2].
CHAPTER 10
Seifert manifolds
In the previous chapter we have proved various general theorems on three-
manifolds, and it is now time to construct examples. A rich and important
source is a family of manifolds built by Seifert in the 1930s, which generalises
circle bundles over surfaces by admitting some “singular” ﬁbres. The three-
manifolds that admit such kind of ﬁbration are now calledSeifert manifolds.
In this chapter we introduce and completely classify (up to diﬀeomor-
phisms) the Seifert manifolds. In Chapter 12 we will then show how toge-
ometrise them, by assigning a nice Riemannian metric to each. We will show,
for instance, that all the elliptic and ﬂat three-manifolds are in fact particular
kinds of Seifert manifolds.
