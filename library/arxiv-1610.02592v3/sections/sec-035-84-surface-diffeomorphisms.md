---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-035-84-surface-diffeomorphisms
section_title: "Surface diffeomorphisms"
section_number: 8.4
pages: 266-277
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
The mapφ is injective: given two metricsm,m′, if the ﬁrst components
ofφ(m),φ (m′) are equal thenq(m) =λq(m′), and if the second components
are equal we getλ = 1.
By similar methods one proves that the image ofφ is open and the inverse
there is continuous. The set W× [0, 1] embeds in H since W embeds in
R6g−7. □
Corollary8.3.29. Thespace Teich(Sg)isatopologicalmanifoldwithbound-
ary∂Teich(Sg).
8.3.18. Conclusion. We have discovered that Teich(Sg) is a compact
topological manifold with boundary, and we now invoke Theorem 1.7.18 to
deduce that it is a disc. We have ﬁnally completed the proof of the following
theorem, which is the main achievement of the whole chapter.
Theorem 8.3.30. The closure Teich(Sg) of Teich(Sg) in PC is homeo-
morphic to the closed discD6g−6. Its interior isTeich(Sg) and its boundary
contains S as a dense subset.
Thurston’s original compactiﬁcation theorem embeds everything inRS
instead of C. We can easily deduce it from Theorem 8.3.30.
Proof of Theorem 8.1.5. The natural mapC → RS induced by the in-
tersection formi is continuous sincei is, and it induces a continuous map
ϕ: PC→ P(RS ) on their projective spaces.
The Teichmüller space is embedded in both projective spaces andϕ re-
stricts to a homeomorphism between the two embeddings, and to a continuous
surjective map from their compactiﬁcations. The map on compactiﬁcations
is actually injective sinceϕ|PML is (intersections with simple closed curves
distinguish laminations) and is hence a homeomorphism. □
8.4. Surface diﬀeomorphisms
WehavediscoveredthatThurston’scompactiﬁcation Teich(Sg)oftheTe-
ichmüller space is homeomorphic to a closed disc. The mapping class group
MCG(Sg) acts on it naturally. We can now apply Brouwer’s ﬁxed point the-
orem to every elementϕ∈ MCG(Sg), and characteriseϕ according to the
position of its ﬁxed points, much similarly as we did for the isometries ofHn.
8.4.1. The torus case. As usual, the ﬂat torus case is very instructive
because everything can be written explicitly.
We know from Proposition 7.1.5 thatMCG(T ) acts on Teich(T ) like the
Möbius transformations PSL2(Z) do on the hyperbolic half-planeH2. The
action of course extends to the compactiﬁcationH2 = H2∪ R∪{∞} and
every non-trivial isometry A ∈ PSL2(Z) is elliptic, parabolic, or hyperbolic
according to the position of its ﬁxed points.
8.4. SURFACE DIFFEOMORPHISMS 259
As an integral matrix, the isometryA has also more properties that are
easy to check: if it is elliptic, it has ﬁnite order becausePSL2(Z) is discrete;
if it is parabolic, it is conjugate inPSL2(Z) to a matrix
(1n
0 1
)
for somen⁄= 0
and is thus then-th power of a Dehn twist; if it is hyperbolic, it is conjugate
in PSL2(R) to a diagonal matrix
(λ 0
0 λ−1
)
for someλ >1, with some basis of
eigenvectors v,w . The two foliations ofR2 into lines parallel tov or w are
both preserved byA and descend to foliations inT = R2/Z2 that are preserved
byA. The two foliations are both irrational (becauseλ is), that is every leaf
is dense inT, andA stretches one foliation byλ and contracts the other by
1/λ. One such diﬀeomorphism ofT is calledAnosov.
Summing up, the non-trivial elements inMCG(T ) either have ﬁnite order,
or preserve a simple closed curve, or are Anosov. We now deﬁne an analogous
trichotomy for the elements inMCG(Sg) when g> 2, where the foliations
are replaced by measured geodesic laminations, and the measure is there to
encode stretchings and contractions.
8.4.2. The trichotomy. Let Sg have genusg> 2. The mapping class
group MCG(Sg) acts naturally on the whole spaceC of currents and in par-
ticular on the compactiﬁcationTeich(Sg)∼=D6g−6 of the Teichmüller space.
Let ϕ∈ MCG(Sg) be a non-trivial element. By Brouwer’s ﬁxed point
theorem,ϕ ﬁxes at least one point inTeich(Sg). We say thatϕ is:
(1) ﬁnite orderif it ﬁxes a hyperbolic metricm∈ Teich(Sg);
(2) reducible if it ﬁxes a multicurveµ∈ M;
(3) pseudo-Anosov in all the other cases.
We now analyse the three cases individually.
8.4.3. Finite order elements.We must ﬁrst explain the terminology.
Proposition 8.4.1. A non-trivial elementϕ∈ MCG(Sg) is ﬁnite order if
and only if it has indeed ﬁnite order inMCG(Sg).
Proof. Suppose thatϕ preserves the isotopy class[m]∈ Teich(Sg) of a
hyperbolic metricm in Sg. We can choose a representative forϕ that ﬁxes
m. This representative is an isometry form. Since the isometry group of a
closed hyperbolic manifold is ﬁnite (see Corollary 4.3.8) we haveϕn = id for
somen> 1 andϕ has indeed ﬁnite order inMCG(Sg).
Conversely, letϕ be an element having ﬁnite order inMCG(Sg). The
subgroup⟨ϕ⟩ generated byϕ cannot act freely onTeich(Sg)∼= R6g−6, other-
wise it would quotientR6g−6 to an aspherical manifold with ﬁnite fundamental
group, contradicting Theorem 1.7.10. Therefore some non-trivial power ofϕ
has a ﬁxed point inTeich(Sg).
If ϕ has prime order we easily conclude that alsoϕ has a ﬁxed point and
we are done. However, ifϕ has orderp1··· ps for some primespi, we need to
do more work. By induction,ϕ′ =ϕp1···ps−1 has a ﬁxed point[m]∈ Teich(Sg)
260 8. SURFACE DIFFEOMORPHISMS
and is hence represented by an isometry forSg with metricm. The isometry
ϕ′ quotientsSg to a hyperbolic orbifold, and the ﬁxed pointsFix(ϕ′) ofϕ′ in
Teich(Sg) can be identiﬁed naturally with the (suitably deﬁned) Teichmüller
space of this orbifold, which is homeomorphic toRN for someN >0 like in
the surface case (exercise).
Sinceϕ andϕ′ commute, the ﬁrst act as a mapping class onFix(ϕ′) with
order p1··· ps−1: we conclude by induction ons that ϕ has a ﬁxed point in
Teich(Sg). □
We get in particular the following corollary, which is far from obvious be-
cause MCG(Sg) does not act itself onSg, and algebraic relations inMCG(Sg)
do not translate into algebraic relations between representatives, except in
some very lucky cases.
Corollary 8.4.2.Ifϕ∈ MCG(Sg) has orderk, it may be represented by a
diﬀeomorphismϕ:Sg→Sg such thatϕk = id.
Proof. The classϕ has a representativeϕ:Sg→Sg that is an isometry
for some hyperbolic metric; the isometryϕk is isotopic to the identity and is
hence the identity by Corollary 4.3.7. □
8.4.4. Reducible elements. We must explain the terminology also in this
case. If ϕ ﬁxes a multicurveµ, one can cutSg along µ and look at the re-
striction ofϕ to the resulting pieces: after extending all the theory to surfaces
with boundary (that we have not done here for simplicity), we can hence study
inductively each piece, and this explains the wordreducible.
The cases (1) and (2) are not exclusive: there are isometries of hyperbolic
surfaces that preserve some multicurve. On the other hand, there are ﬁnite
order elements that are not reducible (exercise) and reducible mapping classes
that are not of ﬁnite order: for instance, Dehn twists.
8.4.5. The action on ML. The mapping class groupMCG(Sg) of Sg
acts on the currents spaceC and hence on the “light cone” subspaceML of
allmeasuredgeodesiclaminations, whichcontainsthespace M ofmulticurves.
The action of MCG(Sg) on ML can be seen concretely insideSg. It
suﬃces to considerML as the space of all measuredtopological laminations
(deﬁned in Section 8.3.11) considered up to isotopy and collapsing of parallel
closedleaves. Nowϕ∈ MCG(Sg)actson MLsimplybysendingthemeasured
topological laminationµ toϕ(µ).
We now prove that ifϕ ﬁxes a non-trivial point inML we fall back into
one of the two cases already considered.
Proposition 8.4.3. If ϕ(µ) = µ for some non-trivialµ∈ ML, thenϕ is
either ﬁnite order or reducible.
8.4. SURFACE DIFFEOMORPHISMS 261
Proof. We ﬁx a hyperbolic metric onSg and representµ as a measured
geodesic lamination there.
By Proposition 8.3.5 there are ﬁnitely many complementary regions inSg\
µ. Ifµ is not full, some region is not an ideal polygon and hence deformation-
retracts onto a subsurfaceS′ ⊂ Sg, whose boundary components∂S′ are
non-trivial simple closed curves inSg. The union of all such curves∂S′ asS′
varies produces a multicurve preserved byϕ, which is hence reducible.
If µ is full, all the complementary regions are ideal polygons, and after
substituting ϕ with a ﬁnite power we can suppose that each region is ﬁxed
(not pointwise) byϕ, together with each of its boundary components. We
consider the preimage˜µ⊂ H2 and note that its complementary regions inH2
are still ideal ﬁnite polygons, the lifts of the ones inSg.
The diﬀeomorphismϕ lifts to a homeomorphism˜ϕ: H2→ H2 that ﬁxes
˜µ, and we may suppose that it ﬁxes (not pointwise) a complementary polygon
and each of its boundary lines. In particularϕ ﬁxes orientation-preservingly a
linel⊂ ˜µ.
Remember that G is the set of all lines inH2. We now prove that, if˜ϕ
ﬁxes (orientation-preservingly) a linel⊂ ˜µ⊂ G, then it ﬁxes (still orientation-
preservingly) all the lines in˜µ contained in some neighbourhood ofl∈ G. This
is done as follows: since the boxes form a neighbourhood system forG, and
˜ϕ acts via homeomorphisms onG, there are two boxesB⊂B′ containing l
such that ˜ϕ(B)⊂ B′. Now B∩ ˜µ⊂ B′∩ ˜µ consists of some parallel lines,
which look likeJ× R⊂J′× R for some measured ordered setJ′ and some
subsegmentJ⊂J′: the mapϕ sendsJ toJ′ preserving both the ordering and
the measure, and ﬁxing the point corresponding tol: hence it is the identity.
On the other hand, every complementary region of˜µ is a ﬁnite ideal poly-
gon: hence if˜ϕ ﬁxes (orientation-preservingly) one side of the polygon, it ﬁxes
all the others.
Thetwopropertiesjustlistedtogethereasilyimplythat, since l isﬁxed, the
whole of ˜µ is. Since the lines are ﬁxed orientation-preservingly, their endpoints
are ﬁxed: the map˜ϕ ﬁxes all the endpoints of all lines in˜µ, and since these
endpoints form a dense subset of∂H2 the map ˜ϕ ﬁxes∂H2 pointwise and
henceϕ is trivial inMCG(Sg) by Proposition 6.5.12. □
The previous proposition shows in particular that pseudo-Anosov elements
act freely on ML\{ 0}. We now investigate more closely these mysterious
mapping classes.
8.4.6. Pseudo-Anosov elements. A pseudo-Anosov elementϕ is by def-
inition neither ﬁnite order nor reducible. We have just seen thatϕ acts freely
on ML\{ 0}, but this does not prevent it from having some ﬁxed points in
262 8. SURFACE DIFFEOMORPHISMS
Figure 8.16. The appropriate lift ˜ϕ acts on∂H2 with 2k ﬁxed points
that are alternatively attractive and repelling. By joining the repelling
points we ﬁnd another laminationµu ﬁxed byϕ. Herek = 5.
PML; indeed we now show that there are two ﬁxed points there, one at-
tracting and the other repelling, so thatϕ looks very much like a hyperbolic
isometry on the hyperbolic space.
Theorem 8.4.4. Let ϕ∈ MCG(Sg) be a pseudo-Anosov element. There
are two measured geodesic laminationsµs,µu∈ ML and a real numberλ> 1
such that
ϕ(µs) =λµs, ϕ (µu) = 1
λµu.
The laminationsµs andµu are full, and they altogether ﬁllSg.
Proof. By Brouwer’s ﬁxed point theorem, a pseudo-Anosov elementϕ has
a ﬁxed point inTeich(Sg)∼= D6g−6 which is (by deﬁnition) neither a metric
nor a multicurve. Thereforeϕﬁxes a projective measured lamination[µ]which
is full (otherwiseϕ would be reducible: see the proof of Proposition 8.4.3).
Since [µ] is a projective class, we haveϕ(µ) = λµ for some real number
λ >0. Up to replacingϕ with its inverseϕ−1 we may suppose thatλ> 1,
and Proposition 8.4.3 shows thatλ> 1. We denote thisµ byµs.
We now constructµu. As in the proof of Proposition 8.4.3, we consider
the preimage ˜µs⊂ H2 ofµs, and after replacingϕ with a ﬁnite power we may
choose a lift˜ϕ ofϕ that ﬁxes a complementary polygonal regionR of ˜µs and
its sides, hence in particular the vertices ofR, see Figure 8.16.
Thek vertices ofR divide∂H2 into ˜ϕ-invariant arcsI1,...,I k, correspond-
ing to the sidess1,...,s k ofR, see Figure 8.16. Sinceµs is full, eachsi is the
limit of a sequence of leaves in˜µs with both endpoints inIi converging to the
endpoints ofsi but distinct from them by Proposition 8.3.10. Sinceλ >1,
the map ˜ϕ pushes these leaves towardssi, so in particular the vertices ofR
are local attractors for the action of˜ϕ on∂H2, see Figure 8.16.
8.4. SURFACE DIFFEOMORPHISMS 263
Since the endpointsp andq ofli are attractors, the map˜ϕ ﬁxes at least
one point in the interior ofIi, and we show that it cannot ﬁx two: if˜ϕ ﬁxesr
ands in the interior ofIi, then it ﬁxes the box[p,r ]× [s,q ] that has non-zero
measure, a contradiction sinceλ> 1. There is a single ﬁxed point inli, and
it must be repulsive.
The dynamics of ˜ϕ on ∂H2 is described in Figure 8.16. The closure of
the projection of thek green lines is another invariant geodesic laminationµu,
which must be full becauseϕ is pseudo-Anosov.
We now prove thatµu admits some (non unique) transverse measure and
can hence be considered as an element ofML. The dynamics shows that for
some curveγ∈ S the supports ofϕ−k(γ) tend to that ofµu. The sequence
ϕ−k([γ])∈ PML hence converges on a subsequence to a projective measured
geodesic lamination with supportµu.
In principle, the measure supported byµu needs not to be unique, not
even up to rescaling: hence the element[µu] may not be uniquely determined
and we cannot conclude that it is ﬁxed byϕ, unfortunately. However, distinct
measures on the same support form obviously a convex cone in the current
space C and hence a closed disc inPC, the classϕ acts on this disc and
therefore has a ﬁxed point there by Brouwer’s ﬁxed point theorem again.
We haveϕ(µu) = λ′µu for someλ′. It is clear thatµu and µs ﬁllSg
altogether, and in particulari(µu,µs)> 0. Therefore
0<i (µu,µs) =i(ϕ(µu),ϕ (µs)) =λλ′i(µu,µs)
givesλ′ = 1
λ. The proof is complete. □
The laminations µs and µu are the stable and the unstable measured
geodesic laminations ﬁxed byϕ, andλ is thedilatation ofϕ. We now prove a
converse to Theorem 8.4.4.
Proposition 8.4.5. Ifϕ∈ MCG(Sg) is such thatϕ(µ) = λµ for some full
µ∈ ML andλ> 1, thenϕ is pseudo-Anosov.
Proof. We need to prove thatϕ is neither ﬁnite order nor reducible, that
is thatϕ ﬁxes no non-trivial currentα∈ Teich(Sg)∪ M. We have
i
(
ϕk(α),µ
)
=i
(
α,ϕ−k(µ)
)
=λ−ki
(
α,µ )→ 0
ask→ +∞. Thereforeϕ(α)⁄=α unlessi(α,µ ) = 0, which is excluded since
µ is full. □
8.4.7. Examples. We now construct plenty of pseudo-Anosov diﬀeomor-
phisms. We need a bit of simple linear algebra.
We say that a matrix or vector ispositive if all its entries are. A square ma-
trixM with non-negative integral entries isPerron-Frobenius ifMk is positive
for somek >0.
264 8. SURFACE DIFFEOMORPHISMS
a
b
a
b
a
b b'
a'
Figure 8.17. We smoothenα∪β to a bigon track that contains both
α andβ (left). The bigon track may have some bigons as complementary
regions (right).
Proposition 8.4.6.Every Perron-Frobenius integral matrixM has apositive
eigenvectorv with some eigenvalueλ> 1.
Proof. The matrixM has non-negative entries and hence preserves the
standard simplex∆ ={xi> 0,∑xi = 1}, so by Brouwer’s ﬁxed point theorem
it has a ﬁxed pointv∈ ∆ there. Since Mk > 0 and v is an eigenvector for
Mk, we getv >0. SinceMk is integral we getλk > 1 and henceλ> 1. □
The following examples were constructed by Penner in 1988. Recall that
a multicurveα in Sg is essential if it contains no parallel components: this
holds for instance ifα is a simple closed curve or a pants decomposition.
Theorem 8.4.7.Letα andβ be two essential multicurves that altogether
ﬁllSg. Let ϕ∈ MCG(Sg) be any composition of Dehn twistsT +1
a and T−1
b
wherea andb vary among the curves inα andβ. If every componenta,b of
α,β occurs at least once, thenϕ is pseudo-Anosov.
The Dehn twists may occur in any order, for instanceϕ =T 2
aT−3
b T−1
b′ Ta′.
Proof. We putα andβ in minimal position and smoothen the transverse
intersections as in Figure 8.17-(left) to get abigon trackτ. A bigon track is
like a train track, except that it may contain some complementary bigon as in
Figure 8.17-(right). The straightening procedure described in Section 8.3.12
works also in this case (exercise), so every weight system onτ determines a
measured geodesic lamination inSg. (Diﬀerent weight systems may determine
the same geodesic laminations because of the bigons.)
We haveα =a1⊔... ⊔am andβ =b1⊔... ⊔bn. Eachai andbj may be
represented by assigning weights 1 or 0 to the edges ofτ, and these weights
formm+n independent (exercise) vectorsv1,...,v m+n in the weights space of
τ. LetV be the(m +n)-dimensional sub-cone of the weights space generated
byv1,...,v m+n via combinations with non-negative coeﬃcients. Every vector
inV models a measured geodesic lamination inSg.
8.4. SURFACE DIFFEOMORPHISMS 265
Let Ω be them +n square matrix Ωij = i(vi,vj ). We have Ω =
( 0 H
K 0
)
.
The crucial point here is that bothTaj andT−1
bk
act onV like the matrix
Qi =I +Di Ω
where I is the identity andDi has 1 on thei-th entry of the diagonal and 0
everywhere else. The mapϕ therefore acts onV as a productM =Qi1··· Qih
of non-negative matrices. Since eachi = 1,...,m +n occurs at least once as
an index, we may deduce (exercise) thatM is Perron-Frobenius. ThereforeM
has a positive eigenvectorv with eigenvalueλ> 1.
The positive eigenvectorv determines an elementµ∈ ML such that
ϕ(µ) = λµ. We leave to the reader the proof thatµ is full, and we conclude
using Proposition 8.4.5. □
8.4.8. References. The material contained in this chapter is well known
to experts, but it is hard to ﬁnd a source in the literature that contains ev-
erything in a fully self-contained way. The whole theory was presented by
Thurston in a very nice and readable paper [55] that however contained no
proof. The most complete book on the subject is then Fathi – Laudenbach –
Poénaru [19], and this is also the main source that we have used for writing
this chapter. Another important source is Casson – Bleiler [12].
We have chosen to describe the whole theory using Bonahon’s geodesic
currents, that originated in the papers [6, 7]. To this purpose we have also
consultedMcMullen[ 39], Aramayona–Leininger[3], andCalegari[9]. Wealso
borrowed some arguments on train tracks and measured geodesic laminations
from a nice and self-contained paper of Hatcher [27]. The proof of Proposition
8.4.1 was taken from [18, Theorem 6.1]. Theorem 8.4.7 was proved by Penner
in [44].
Part 3
Three-manifolds
CHAPTER 9
Topology of three-manifolds
The three-manifolds world is topologically much richer than the surfaces
realm, while yet not so crazy as the four-manifolds universe. In dimension two
a simple homological invariant (the Euler characteristic) suﬃces to classify
topologically all the closed orientable manifolds: at the complete opposite,
the closed four-manifolds cannot be classiﬁed in any reasonable sense. The
three-manifolds lie in the middle: we do not have yet a complete satisfactory
picture, but we understand them a good deal.
The rest of this book is devoted to three-manifolds, more speciﬁcally to
compact orientable three-manifolds, possibly with boundary (the orientability
assumption is not essential, but it helps to simplify many arguments). We
split their study into some parts. First, we state some universal topological
facts, mostly concerning the way surfaces can be contained in three-manifolds.
Then we construct some classes of three-manifolds, focusing mostly on Seifert
manifolds. After classifying the Seifert manifolds topologically, we assign a
geometry to each: there are eight interesting geometries in dimension three,
and we introduce them with some care. Finally, we concentrate on the most
interesting and beautiful of the eight: hyperbolic geometry.
Inthischapterwestarttostudythetopologyofthree-manifolds. Webegin
