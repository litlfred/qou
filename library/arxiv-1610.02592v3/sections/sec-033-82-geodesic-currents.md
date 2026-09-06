---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-033-82-geodesic-currents
section_title: "Geodesic currents"
section_number: 8.2
pages: 230-246
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
For the moment we content ourselves with checking that this projective
embedding strategy works at least on the much simpler ﬂat torus case.
8.1.3. The torus. The Teichmüller space of the torusT is described in
Section 7.2.4 and needs no further comment; nevertheless, we prove here that
the projective embedding strategy works forT, just as a sanity check before
approaching the more complicated higher genus surfaces.
Proposition 8.1.6. The space Teich(T ) embeds in P(RS ) and its closure
thereishomeomorphictoacloseddisc D2. Theinteriorofthisdiscis Teich(T )
and its boundary containsS as a dense subset.
Proof. Everything can be written explicitly by identifyingTeich(T ) with
the half-planeH2 and S with the setQ∪{∞}⊂ ∂H 2. Exercise 6.3.14 and
Proposition 7.2.5 give
i
(p
q,r
s
)
=
⏐⏐⏐⏐det
(p r
q s
)⏐⏐⏐⏐ =|ps−qr| =|s|·
⏐⏐⏐p−qr
s
⏐⏐⏐,
𝓁
p
q (z) =|p +qz|√
ℑz .
Therefore the images of r
s ∈ S and z ∈ H2 = Teich(T ) in P(RS ) are
respectively the functionals
p
q↦−→
⏐⏐⏐p−qr
s
⏐⏐⏐ if s⁄= 0 and|q| if s = 0,
p
q↦−→|p +qz|.
We could remove the constants|s| and
√
ℑz because we are considering func-
tionals in P(RS ) rather than inRS. We deﬁne for allz∈H2 the functional
fz : p
q↦−→|p +qz| if z⁄=∞,
f∞ : p
q↦−→|q|.
and we get a continuous immersionz↦→fz ofH2 into P(RS ). The immersion
is closed because it sends a compact space to a Hausdorﬀ space, hence it is
a homeomorphism onto its image. The image is the closure ofTeich(T ) and
its boundary containsS as a dense set. □
8.2. GEODESIC CURRENTS 223
8.2. Geodesic currents
We will prove Thurston’s compactiﬁcation Theorem 8.1.5 using a slightly
diﬀerent perspective. We are guided by the analogy with the hyperbolic space:
when we embed (actually, deﬁne) the spaceHn in Rn+1, we make an essential
use of the lorentzian form⟨,⟩ in Rn+1, so thatHn consists of some pointsv
with⟨v,v⟩ =−1, and∂Hn may be identiﬁed with the light cone rays, that is
the rays spanned by vectorsv with⟨v,v⟩ = 0.
It would be nice to have a similar nice bilinear form⟨,⟩ on RS, with the
propertythat Teich(Sg)and S consistofpointswith ⟨v,v⟩ =k and⟨v,v⟩ = 0
respectively, for some ﬁxedk⁄= 0. Unfortunately we are not able to deﬁne
such a bilinear form inRS, and in order to get one we now substituteRS
with a similar (but more structured) inﬁnite-dimensional space, the space of
geodesic currents.
In geometric measure theory, acurrent is a measure on some space, which
generalises the notion ofm-dimensional submanifold in an-manifold. A ge-
odesic current is a similar tool introduced by Bonahon in 1988 speciﬁcally
designed for geodesics on hyperbolic surfaces.
We will see that the geodesic currents are indeed equipped with a bilinear
form, which generalises beautifully both the intersection numberi(α,β ) of
curves and the length functions𝓁γ on the Teichmüller space.
8.2.1. Geodesics. From now on, and through all the rest of this chapter,
we will consider geodesics only as subsets, neglecting their parametrisation.
More precisely, letM a complete hyperbolic manifold. We indicate by
G (M)the set of the supports of all the complete non-trivial geodesicsR→M.
With a little language abuse, we call an element ofG (M) a geodesic.
A geodesic in G (M) is closed if it is the support of a closed geodesic
S1→M, that is if it is compact; otherwise, it isopen. We say that a geodesic
is simple if it has a simple geodesic parametrisation, either as an open geodesic
R→M or as a closed oneS1→M.
We are particularly interested in the setG = G (H2) of lines inH2. A line
is determined by its extremes, hence there is a natural bijection
G←→
(
∂H2×∂H2\ ∆
)
/∼
where ∆ ={(a,a )| a∈∂H2} is the diagonal and(a,b )∼ (b,a ). We assign
to G the topology of
(
∂H2×∂H2\ ∆
)
/∼.
Exercise 8.2.1. The space G is homeomorphic to an open Möbius strip.
The lines intersecting a compact setK⊂ H2 form a compact subset ofG.
The isometries ofH2 act naturally onG by homeomorphisms.
Proposition 8.2.2.IfS = H2/Γ is a complete hyperbolic surface there is a
natural bijection
G (S)←→ G/Γ.
224 8. SURFACE DIFFEOMORPHISMS
Proof. Every geodesic inS lifts to aΓ-orbit of lines inH2. □
It is typically more comfortable to lift objects fromS to the universal
cover H2, and to study them there: we will often see a geodesicγ∈ G (S) as
a Γ-orbit of lines inH2.
Wewillsincenowconsideronlyclosedsurfaces Sg ofgenus g> 2. Wenow
prove the crucial fact thatG (Sg) depends only mildly on the chosen hyperbolic
metric forSg. An isomorphism between two pairs (G1, Γ1) and (G2, Γ2) of
groups Γi acting on topological spaces Gi is an isomorphism ψ : Γ 1 → Γ2
together with aψ-equivariant homeomorphismG1→ G2.
Proposition 8.2.3. Let g> 2 and Sg = H2/Γ have a hyperbolic metric.
Thepair (G, Γ)doesnotdepend(uptocanonicalisomorphisms)onthechosen
hyperbolic metric.
Proof. Letm,m′ betwohyperbolicstructureson Sg,inducingtwodiﬀerent
coveringsπ,π′ : H2→Sg. The identity mapSg→Sg lifts to a mapH2→ H2
thatextendstoanequivarianthomeomorphism ∂H2→∂H2 byTheorem5.2.1.
This induces an equivariant homeomorphismG→ G. □
Here and in the next sections, the hyperbolic metric onSg has only an
auxiliary role: we need it to identifySg with H2/Γ and to deﬁne and study
some geometric objects likeG (Sg) = G/Γ, but most of our discoveries will be
independent a posterioriof the auxiliary hyperbolic metric.
Let Sg = H2/Γ be a hyperbolic surface. We note that Γ does not act
properly discontinuously onG.
Proposition 8.2.4. The Γ-orbit of a linel∈ G is discrete if and only ifl
projects to a closed geodesic inSg.
Proof. Letπ(l)⊂Sg be the projection ofl in Sg. Since Sg is compact,
the projectionπ(l) is not a closed geodesic⇔ there is a small discD⊂ Sg
intersectingπ(l) into inﬁnitely many distinct segments⇔ there is a small disc
D⊂ H2 intersecting inﬁnitely many lines of theΓ-orbit ofl⇔ the Γ-orbit is
not discrete. □
The linesl⊂ H2 that project to closed geodesics inSg are precisely the
axis of the hyperbolic isometriesϕ in Γ, and the Γ-orbit of one such axisl
consists of the axis of all the isometries inΓ conjugate toϕ. Two such axis
are either incident or ultraparallel by Corollary 4.2.3, and the closed geodesic
inSg is simple if and only if all the distinct axis in theΓ-orbit are ultraparallel.
Proposition 8.2.4 implies in particular that theΓ-orbit ofl is discrete only
for countably many linesl∈ G.
Recall from Corollary 4.1.14 that every homotopically non-trivial closed
curve inSg is homotopic to a unique closed geodesic.
8.2. GEODESIC CURRENTS 225
8.2.2. Geodesic currents. We now introduce a measure-theoretical no-
tion which is at ﬁrst sight unrelated with everything we have seen up to now;
we will later show that, on the contrary, it generalises many of the geometric
objects that we have encountered in the last pages. The basic notions of
measure theory that we will need are summarised in Section 1.3.
Deﬁnition 8.2.5. LetSg = H2/Γ be a hyperbolic surface. A geodesic
current onSg is a locally ﬁniteΓ-invariant Borel measure onG = G (H2).
We denote byC = C (Sg) the set of all the geodesic currents inSg. It is a
subset of the spaceM (G ) of all the locally ﬁnite Borel measures onG, closed
with respect to sums and products with non-negative scalars, and it inherits
its topology, see Section 1.3.3.
The currents spaceC is independent of the auxiliary hyperbolic metric on
Sg up to canonical isomorphisms, since the pair(G, Γ) is.
8.2.3. Closed geodesics. We now introduce a fundamental example of
geodesic current.
Example 8.2.6 (Closed geodesics). A closed geodesicγ onSg = H2/Γ lifts
by Proposition 8.2.4 to a discreteΓ-orbit of lines inH2. The Dirac measure on
this discrete set is locally ﬁnite andΓ-invariant, hence it is a geodesic current.
We can therefore interpret every closed geodesic inSg as a particular
geodesic current with discrete support. In particular we get an embedding
S ↪→ C
of the set S of all (isotopy classes of) unoriented non-trivial simple closed
curves inSg into C. The embedding is deﬁned by taking the geodesic rep-
resentative of each curve. Recall that the hyperbolic metric plays only an
auxiliary role.
The following proposition implies that – conversely – every current sup-
ported on a discrete set is a linear combination of closed geodesics.
Proposition 8.2.7. If l∈ G is an atomic point for a geodesic currentµ,
that is ifµ({l})> 0, thenl projects to a closed geodesic inSg.
Proof. Sincel is atomic andµ is Γ-invariant and locally ﬁnite, theΓ-orbit
ofl in G is discrete. We conclude thanks to Proposition 8.2.4. □
It is an important aspect of the theory that atomic points may be only of
a very speciﬁc type. We remind that many closed geodesics are not simple.
8.2.4. Pencils. We have determined the 0-dimensional subsets ofG that
may have positive mass, and we now look at some natural 1-dimensional ones.
Let apencil p⊂ G of lines centred ata∈∂H2 be some Borel set of lines all
having one endpoint ata, as in Figure 8.1-(left).
226 8. SURFACE DIFFEOMORPHISMS
a a
b
c
d
Figure 8.1. A pencil and a box (in the Klein model).
We note that a pencil may contain at most one axis of some hyperbolic
transformationin Γ,becausetwoaxisareneverasymptoticallyparallelbyCorol-
lary 4.2.3.
Proposition 8.2.8.Letµ be a geodesic current. The mass of a pencilp is
zero, unless it contains the axis of some non-trivial element inΓ.
Proof. It suﬃces to consider the case wherep contains no axis, and
consists of all lines with one endpoint ina and another in some segment
[b,c ]⊂∂H2 not containinga.
As the lines inp point toa, they project inSg to a narrow beam of lines
that go on running forever and exponentially-narrowing inSg but never close
up. There is a discD⊂ Sg intersecting them inﬁnitely many times, hence
a liftD⊂ H2 intersects inﬁnitely many disjointΓ-translates ofp. The lines
intersectingD form a compact subset ofG, henceµ(p) = 0. □
8.2.5. Boxes. We now investigate some natural 2-dimensional subsets of
G. Let a,b,c,d ∈ ∂H2 be four distinct counterclockwise-ordered points as
in Figure 8.1-(right): these determine two disjoint arcs[a,b ], [c,d ]⊂ ∂H2
and hence a compact setB = [a,b ]× [c,d ]⊂ G consisting of all lines with
endpoints in[a,b ] and [c,d ], see Figure 8.1-(right). We call this compact set
B a box.
The topological boundary∂B of a boxB has four sides: the four pencils of
lines inB with one endpoint ina,b,c , ord. We say that the boxB is generic
if no linel∈ ∂B projects to a closed geodesic,i.e. no l∈ ∂B is the axis of
some hyperbolic transformation inΓ. This is indeed a generic condition: if
neither ofa,b,c,d is the endpoint of some axis, thenB is certainly generic,
and recall that there are only countably many axis overall.
We equip the currents spaceC with the weak-* topology introduced in
Section 1.3.3. We now prove that a converging sequence of currents behave
well on generic boxes.
Proposition 8.2.9.Ifµi ⇀µ is a converging sequence of geodesic currents
andB is a generic box, thenµi (B)→µ(B).
8.2. GEODESIC CURRENTS 227
Figure 8.2. The boxB containingl and the sub-boxesB′ andB′′ (left).
A linel∈Uγ parametrised by the pair(t,θ ) (right).
Proof. By Proposition 1.3.8 it suﬃces to prove thatµ(∂B) = 0, and this
follows from Proposition 8.2.8. □
8.2.6. Rigidity of atoms.We now use boxes to prove that the atomic
points in C are somehow rigid.
Proposition 8.2.10. The closed geodesics form a discrete subset inC.
Proof. Letµ∈ C be a closed geodesic,i.e it is the Dirac measure on the
Γ-orbit of an axisl⊂ H2 of some hyperbolic transformationϕ∈ Γ.
Let B = [a,b ]× [c,d ] be a small generic box containingl and no other
Γ-translate ofl, so thatµ(B) = 1 . Up to substitutingϕ with ϕ−1 we may
suppose thatϕ([a,b ]) = [a′,b′]⊂ [a,b ]. Consider the sub-boxesB′ = [a,a′]×
[c,d ] and B′′ = [b′,b ]× [c,d ] shown in Figure 8.2-(left). Sinceϕ contracts
[a,b ] and expands [c,d ], we have
(4) B\p⊂
∞⋃
i=1
ϕi (B′⊔B′′).
wherep is the pencil containingl and other lines with one endpoint varying in
[b,c ]. Note thatp contains no axis ofΓ other thanl. If necessary, we move
a′ and b′ slightly farther froma and b to ensure thatB′ and B′′ (and hence
all theirϕ-translates) are generic while (4) still holds.
We haveµ(B′⊔B′′) = 0 and we deﬁne an open neighbourhoodU ofµ in
the current spaceC as follows:
U =
{
η∈ C |η(B′⊔B′′)<ε, η(B)> 1−ε
}
for some ﬁxed0<ε< 1. This is indeed an open set becauseB,B′, and B′′
are generic. We now prove thatU contains no closed geodesic exceptµ.
By contradiction, supposeU contains a closed geodesicη. Sinceη(B)>
1−ε> 0, at least one atoml′ ofη is contained inB. Ifl′ =l thenη =µ and
wearedone. Otherwise, theline l′ iscontainedin B\p andhencein ϕi (B′⊔B′′)
for somei. This is impossible since this set has measureε< 1. □
228 8. SURFACE DIFFEOMORPHISMS
We have classiﬁed the elements inC supported on discrete sets, and it is
now time to introduce some geodesic currents supported on the whole ofG.
8.2.7. The Liouville measure. There is a continuous measure onG =
G (H2)thatisinvariantundertheactionofthewholeisometrygroup Isom(H2).
This measure is called theLiouville measure, and is deﬁned as follows.
Letγ : R→ H2 be a geodesic parametrised by arc length, andUγ⊂ G be
the open set consisting of all the lines intersectingγ, exceptγ itself. We can
parametriseUγ via the homeomorphism
R× (0,π )→Uγ
that sends (t,θ ) to the linel that intersectsγ at the pointγ(t) with angleθ,
see Figure 8.2-(right). We deﬁne a volume 2-form onUγ by setting:
Lγ = 1
2 sinθdt ∧dθ.
Since G is non-orientable, we cannot hope to deﬁne a global area form on
G. However all these local forms match up to sign and hence give rise to a
measure.
Proposition 8.2.11. The chartsUγ form a diﬀerentiable atlas forG. The
2-formsLγ match up to sign and hence deﬁne a measureL on G.
Proof. Every line inH2 intersects some other line, hence the charts cover
G. We consider a liner∈Uγ∩Uγ′. The chartsUγ and Uγ′ have parametri-
sations (t,θ ) and (t′,θ′) and 2-forms
Lγ = 1
2 sinθdt∧dθ, L γ′ = 1
2 sinθ′dt′∧dθ′.
We consider the jacobianJ = ∂(t′,θ′)
∂(t,θ) and recall that
dt′∧dθ′ = detJ·dt∧dθ
so we need to show that
(5) detJ =± sinθ
sinθ′.
We can reparametriseγ at our please, since this may changeLγ only by a sign.
We may suppose thatγ and γ′ are asymptotically parallel, because any two
linesγ,γ′ intersectingr are connected by a pathγ =γ1,...,γ k =γ′ of lines
intersectingr, such that any two subsequent linesγi,γi+1 are asymptotically
parallel (actuallyk = 3 suﬃces).
We represent the linesγ,γ′, andr in the half-plane modelH2⊂ R2 as in
Figure 8.3. Up to isometries and reparametrisations we have
γ(t) = (0,et), γ ′(t′) = (1,et′
).
The line r is a Euclidean half-circle with center at some pointC ∈ R and
with some radiusR >0. It intersectsγ and γ′ at some heightset and et′
,
8.2. GEODESIC CURRENTS 229
0 1
g
C
g'
r
u
u'
R
Figure 8.3. The two asymptotic linesγ,γ′ in the half-space modelH2
and the liner intersecting both.
with some anglesθ andθ′. We now calculate the determinant ofJ = ∂(t′,θ′)
∂(t,θ) .
Figure 8.3 shows that
R = et
sinθ = et′
sinθ′
C =−et cotθ, 1−C =et′
cotθ′.
Now
∂(C,R )
∂(t,θ ) =
(−et cosθ sin−1θ e t sin−2θ
et sin−1θ −et cosθ sin−2θ
)
whose determinant is−e2t sin−1θ =−R sinθ, and we get the same formula
for ∂(C,R)
∂(t′,θ′). Therefore
det∂(t′,θ′)
∂(t,θ ) = det∂(t′,θ′)
∂(C,R )· det∂(C,R )
∂(t,θ ) = (−R sinθ′)−1· (R sinθ) = sinθ
sinθ′
and we ﬁnally obtain (5), as required. □
The measureL on G is called theLiouville measureand is clearly invariant
by the action ofIsom(H2). The renormalising factor 1
2 in the deﬁnition was
chosen to get the following property, which nicely characterisesL.
Proposition 8.2.12. Let s⊂ H2 be a geodesic segment of lengthl. The
lines in H2 intersectings form a set of measurel.
Proof. The set has measure
∫ π
0
∫ l
0
1
2 sinθdtdθ =l
∫ π
0
1
2 sinθdθ =l.
The proof is complete. □
The Liouville measureL is supported on the whole ofG.
Exercise 8.2.13. The Liouville measure of a boxB = [a,b ]× [c,d ] is
L(B) =
⏐⏐ logβ(a,b,c,d )
⏐⏐
whereβ is the cross-ratio of the four points.
230 8. SURFACE DIFFEOMORPHISMS
8.2.8. The Liouville current. Let nowSg = H2/Γ be equipped with a
hyperbolic metric. The Liouville measure onG is Isom(H2)-invariant: in par-
ticular it is Γ-invariant and hence deﬁnes a currentL∈ C (Sg), called the
Liouville current.
It is important to note that the space of currentsC = C (Sg) does not
depend on the given hyperbolic metric forSg, but the Liouville current does!
Every metricm∈ Teich(Sg) induces a Liouville currentLm∈ C, and in this
way we get aLiouville map
Teich(Sg)−→ C
that sendsm toLm. We will soon see that this map is injective: as promised,
we have mapped bothS and Teich(Sg) inside the currents spaceC.
Remark 8.2.14. We constructed the Liouville currentLm by assigning to
G a diﬀerentiable atlas – hence a smooth structure – and a 2-form deﬁned up
to sign. We note that the smooth structure onG also depends crucially on
m, because the boundary extension of Theorem 5.2.1 is not guaranteed to be
a diﬀeomorphism.
The crucial feature that makesC preferable to P(RS ) as a comfortable
ambient space for bothS and Teich(Sg) is the existence of a nice bilinear
form in C that extends both the length and the geometric intersection of
closed geodesics. We now introduce this bilinear form.
8.2.9. The projective frame bundle.We denote by I ⊂ G× G the
open subset consisting of all the pairs ofincident distinct lines inH2. We give
I the topology induced byG× G, henceI is an open topological 4-manifold.
Since two distinct incident lines intersect in a single pointp∈ H2, the setI
can be interpreted as the set of triples(p,l 1,l 2) with p∈ H2 and l1,l 2 two
distinct vector lines in the tangent planeTpH2.
Let nowSg = H2/Γ be equipped with a hyperbolic metric. The action of
Γ on G is not properly discontinuous, but the diagonal action ofΓ on I is, as
the following shows.
Proposition 8.2.15. The map I→ I/Γ is a topological covering.
Proof. The group Γ acts freely and properly discontinuously onH2, and
hence it does soa fortiorion the triples(p,l 1,l 2). □
In particular I/Γ is a four-manifold, and it is naturally a bundle overSg,
whose ﬁbre abovep∈Sg consists of the ordered pairs of distinct vector lines
l1,l 2 inTpSg. Recall that theframe bundleon a manifoldM is a bundle whose
ﬁbre abovep∈M is the set of allframes (i.e. basis) inTpM. The spaceI/Γ
can be seen as some projective quotient of the frame bundle onSg.
8.2. GEODESIC CURRENTS 231
8.2.10. Intersection form. Two geodesic currentsα,β ∈ C = C (Sg)
induce a Γ-invariant product measureα×β on G× G and hence onI. This
measure descends via the coveringI→ I/Γ to a measure onI/Γ which we
still indicate byα×β, see Section 1.5.4.
Deﬁnition 8.2.16. Theintersectioni(α,β ) of two geodesic currents is the
total volume ofI/Γ in the measureα×β.
The intersectioni(α,β )does not depend on the auxiliary hyperbolic metric
forSg. The ﬁniteness ofi(α,β ) is not immediate sinceI/Γ is not compact,
and it deserves a proof.
Proposition 8.2.17. The intersectioni(α,β ) is ﬁnite.
Proof. LetD be a compact fundamental domain forSg = H2/Γ. SinceD
is compact, the lines intersectingD form a compact subsetX⊂ G which has
ﬁnite measuresα(X)andβ(X). The projection sends(X×X)∩I surjectively
onto I/Γ. Thereforei(α,β ) = (α×β)(I/Γ)<α (X)·β(X). □
The formi is clearly bilinear and symmetric.
8.2.11. Geometric intersection and length of closed geodesics.We
now show that this abstract-looking intersection form generalises both the
geometric intersection and the length of simple closed geodesics. We consider
as usual the setS of simple closed curves as a subset ofC. The following
proposition explains why we employed the notationi for the intersection form
of two geodesic currents.
Proposition 8.2.18. If α,β ∈ S, the number i(α,β ) is the geometric
intersection of the simple closed curvesα andβ.
Proof. Representα andβ as simple closed geodesics. The measureα×β
is the Dirac measure with support the pairs of incident lines inH2 that cover
respectivelyα andβ. The Γ-orbits of these pairs are in natural bijection with
the transverse intersection points inα∩β. Hence the volume ofI/Γ is the
cardinality ofα∩β, except whenα =β and in this case we get zero. □
We note in particular thati(α,α ) = 0 for everyα∈ S, hence the setS is
contained in the “light cone” consisting of all the currentsα withi(α,α ) = 0.
(Of coursei(α,α )> 0 for every geodesic currentα.) We now consider the
Liouville currentLm∈ C determined by some hyperbolic metricm onSg.
Proposition 8.2.19. Ifα∈ S theni(Lm,α ) = 𝓁α(m) is the length of the
geodesic representative ofα in the metricm.
Proof. Representα as a simple closed geodesic in the metricm, of length
𝓁α(m). The measure Lm×α has its support on the pairs(l,l′) of incident
lines wherel is arbitrary andl′ is a lift ofα.
232 8. SURFACE DIFFEOMORPHISMS
Any segments′⊂l′ of length𝓁α(m) in a ﬁxed liftl′ ofα is a fundamental
domain for the action ofΓ on the lifts ofα. Thereforei(Lm,α ) is the volume
of the pairs (l,l′) where l′ is ﬁxed, andl is arbitrary and intersectss′. By
Proposition 8.2.12 these pairs have volume𝓁α(m). □
Theintersectionform i on C generalisesboththegeometricintersectionof
curvesandthelengthfunctionsonTeichmüllerspace, twoapparentlyunrelated
objects! As promised, we can easily deduce thatTeich(Sg) embeds in C.
Corollary 8.2.20.The Liouville mapTeich(Sg)→ C is injective.
Proof. Ifm⁄=m′ there is a curveγ∈ S with𝓁γ(m)⁄=𝓁γ(m′) by Propo-
sition 7.3.4 and hencei(Lm,γ )⁄=i(Lm′,γ ). ThereforeLm⁄=Lm′. □
We will since now consider bothTeich(Sg) and S as subsets ofC. We
know the geometric meaning of the intersection of two curves, and of a curve
and a hyperbolic metric. What is the intersection of two hyperbolic metrics?
When they coincide, we get a positive constant.
Proposition 8.2.21. Ifm∈ Teich(Sg) we havei(Lm,Lm) =−π2χ(Sg).
Proof. The metricm produces a smooth structure onG and hence onI,
and Lm is induced by aΓ-invariant 2-form onG deﬁned up to sign, that we
also denote asLm. We need to integrate the 4-formLm×Lm on I/Γ.
Recall that I/Γ may be interpreted as a bundle overSg. We make a
ﬁrst-order computation on a very small region ofSg, which we may suppose
to be Euclidean: a very thin rectangleR in Sg of sidesl and a with a≪ l.
We compute the volume of the portion of bundle lying aboveR.
We integrateLm×Lm on all the pairs of segments intersecting in some
point inR, and we consider only segments with both endpoints on the bigl
sides, neglecting the smalla sides. A segment meeting thel sides at angleθ
has lengthL(θ) =a/ sinθ. By Proposition 8.2.12 theLm×Lm volume of the
portion of I aboveR is (at a ﬁrst order) equal to
∫ π
0
∫ l
0
1
2 sinθ·L(θ)dtdθ ∼ 1
2l
∫ π
0
sinθ· a
sinθ = π
2la.
The ﬁrst-order contribution of a small region is henceπ
2 times its area.
Since the volume is induced by a diﬀerentiable form, by taking the limit we
ﬁnd that the contribution of any region is preciselyπ
2 its area and we conclude
by the Gauss-Bonnet theorem. □
We have already noted thati is symmetric and bilinear. As we mentioned,
there is an evident analogy between the embeddingsTeich(Sg) ↪→ C and
Hn ↪→ Rn+1, since there is a bilinear form on both spacesC and Rn+1, and
Teich(Sg) is also contained in a “hyperboloid” consisting of vectorsv with
i(v,v ) = k for some ﬁxedk⁄= 0. On the other handS is contained in the
“light cone” formed by all vectorsv withi(v,v ) = 0.
8.2. GEODESIC CURRENTS 233
We may compactifyHn by projecting the hyperboloid to the Klein model
Kn⊂ RPn. NowKn is an open disc, whose boundary is the image of the light
cone. Wewouldliketoapplythesamecompactiﬁcationstrategyto Teich(Sg).
Before doing that, we need to prove a slightly technical fact: that the bilinear
formi is continuous.
8.2.12. Continuity of the intersection form.LetSg = H2/Γ be a closed
hyperbolic surface. The following theorem is not obvious becauseI is not
compact: the proof relies on the fact that closed geodesics form a discrete
rigid set in C and therefore atomic points cannot “escape to inﬁnity” on a
converging sequence of currents.
Theorem 8.2.22.The formi : C× C→ R is continuous.
Proof. Letβ1,β 2 be two currents converging toα1,α 2. We need to prove
that i(β1,β 2) converges toi(α1,α 2). The bundle I/Γ is not compact and
we need to control that no mass escapes to inﬁnity: the inﬁnity here is the
diagonal ∆⊂ G× G, so our aim is to cover∆ with small boxes and prove that
they contribute very little toi(β1,β 2). For any boxB, we deﬁne
Ψ(B) =
(
(B×B)∩ I
)
/Γ.
We show that for everyε> 0 there are ﬁnitely many small generic boxesBi
whose Γ-translates cover G, such that
(β1×β2)(∪i Ψ(Bi ))<ε
as soon asβ1,β 2 are suﬃciently close toα1,α 2. Since the Γ-translates of
∪i (Bi×Bi ) form an open neighbourhood of∆, the set(I/Γ)\ (∪i Ψ(Bi )) is
compact with zero-measure boundary (because the boxesBi are generic) so
its contribution toi(β1,β 2) tends to that toi(α1,α 2) ifβ1,β 2 are suﬃciently
close, and the theorem is proved.
It remains to construct the boxesBi. We ﬁrst ﬁx ﬁnitely many generic
boxesBi whose Γ-translates cover G. LetK >0 be bigger than the totalα1
andα2-mass of the boxes.
We now pick a small number 0 < ε′ < ε/2K and subdivide each box
Bi into ﬁnitely many generic sub-boxes (which we still callBi) such that the
following holds for eachi and eachj = 1, 2:
(1) eitherαj (Bi )<ε′, or
(2) there is an atomic pointl∈Bi withαj (l)>ε′ andαj (Bi\l)<ε′.
If the second case holds for bothj = 1, 2, we also requirel∈ Bi to be the
same line forj = 1, 2. We note that the totalα1 andα2-mass of the boxes is
still smaller thanK after the subdivision. We have
(β1×β2)(Ψ(B))⩽β1(B)·β2(B)
so ifβ1,β 2 are suﬃciently close toα1,α 2 the boxesBi that are of the ﬁrst kind
for at least one value ofj = 1, 2 contribute toi(β1,β 2) less than 2ε′K <ε.
234 8. SURFACE DIFFEOMORPHISMS
We are left to consider the boxesBi containing a linel whose α1 and
α2-mass are both bigger thanε′. This is a potentially bad situation since the
point (l,l )∈ G× G is atomic and contained in the frontier ofI, and could
enter inside I abruptly for some arbitrarily small perturbations ofα1 andα2.
We show that this cannot happen because atomic points are rigid, as noted in
Proposition 8.2.10.
As in the proof of Proposition 8.2.10, we setBi =B = [a,b ]× [c,d ] and
construct B′ = [a,a′]× [c,d ],B′′ = [b′,b ]× [c,d ] whose ϕ-translates cover
B\p wherep is a pencil containingl. We note that
(β1×β2)(Ψ(B))⩽β1(B′⊔B′′)·β2(B) +β2(B′⊔B′′)·β1(B)
is smaller thanε′(β1(B) +β2(B)) and hence by summing on theBi we get
again a contribution smaller than2ε′K <ε. □
8.2.13. Filling geodesic currents.We now deﬁne an interesting class of
currents, whose importance will be evident in the next section.
We say that a geodesic currentα∈ C (Sg) ﬁllsthe surfaceSg = H2/Γ
if every line inH2 intersects transversely at least one line in the support of
α. For instance, a Liouville measure ﬁllsSg since its support is the whole of
G. We say thatk closed geodesicsγ1,...,γ k ﬁllSg if the geodesic current
γ1 +... +γk does.
Proposition8.2.23. Letγ1,...,γ k beclosedgeodesics. If Sg\(γ1∪···∪ γk)
consists of polygons, the curves ﬁllSg.
Proof. Every geodesic inSg intersects these curves. □
As an example, we can pick two multicurvesη andµ inSg that intersect
transversely forming only polygons but no bigons. By the bigon criterionη and
µ are in minimal position and by Proposition 6.3.24 their geodesic representa-
tives have the same conﬁguration asη∪µ, so they ﬁllSg.
It is a bit more diﬃcult to construct a single (non-simple) closed geodesic
that ﬁllsSg. The following remark is straightforward.
Remark 8.2.24. Letα andβ be currents. We havei(α,β )> 0 if and only
if there are two lines in the supports ofα andβ that intersect in a point.
Corollary 8.2.25.Ifα ﬁllsSg theni(α,β )> 0 for every non-trivialβ∈ C.
8.2.14. A compactness criterion. We now state a simple and general
compactness criterion for subsets ofC that has various nice (and apparently
unrelated) geometric consequences.
Proposition 8.2.26 (Compactness criterion).If α∈ C ﬁllsSg, the set of
allβ∈ C withi(α,β )⩽M is compact, for allM >0.
8.2. GEODESIC CURRENTS 235
Proof. Let C ⊂ C be the set of allβ with i(α,β )⩽ M. It is closed
becausei is continuous.
Letl be a line inH2. By hypothesis there is another linel′ in the support
of α which intersectsl in a point. LetB′, B be two suﬃciently small boxes
neighbourhoods of l′,l in G, so thatB′×B ⊂ I and B′×B is mapped
injectively into I/Γ. Ifβ∈C we have
α(B′)β(B) = (α×β)(B′×B)⩽ (α×β) (I/Γ) =i(α,β )⩽M.
Therefore every linel in H2 has a box neighbourhoodB such that
β(B)⩽Kl ∀β∈C
for some constant Kl = M/α(B′) that depends only on l. The set C is
relatively compact by Theorem 1.3.9, and hence compact since it is closed.
The proof is complete. □
We now state some corollaries. The ﬁrst concerns the immersion of
Teich(Sg) in C.
Corollary 8.2.27.The Liouville mapTeich(Sg)↪→ C is proper and a home-
omorphism onto its image.
Proof. We prove that the map is proper: ifmj∈ Teich(Sg) is a diverging
sequence of metrics, we know from Proposition 7.3.14 that there is a closed
curveγ∈ S such that𝓁γ(mj ) = i(mj,γ )→∞ on a subsequence. Sincei is
continuous, the sequencemj diverges also inC.
We denote the Liouville map byL. We should now prove thatL is con-
tinuous, but we prefer to consider the inverse mapL−1 : L(Teich(Sg)) →
Teich(Sg). The map L−1 is continuous becausei is and Teich(Sg) has the
weakest topology where the length functions are continuous. We show that
L−1 is proper. Let γ1,...,γ k be simple closed curves that ﬁllSg. If L(mi )
is a diverging sequence, by Proposition 8.2.26 we havei(L(mi ),∑
tγt)→∞
and hencei(L(mi ),γt)→∞ for somet. Therefore mi is divergent also in
Teich(Sg).
NowL−1 is continuous and proper and hence a homeomorphism by Corol-
lary 7.3.11. □
A second immediate corollary is a general compactness criterion for the
Teichmüller space.
Corollary 8.2.28.Letγ1,...,γ k be some closed geodesics that ﬁllSg. The
metricsm∈ Teich(Sg) with𝓁γi (m)⩽M form a compact subset ofTeich(Sg),
for allM >0.
We can similarly deduce the following.
Corollary 8.2.29.Letγ1,...,γ k be some simple closed curves that ﬁllSg.
For everyM there are only ﬁnitely manyα∈ S withi(γi,α )<M for alli.
236 8. SURFACE DIFFEOMORPHISMS
Exercise 8.2.30. Use the compactness criterion to re-prove that on a hy-
perbolicclosedsurfacethereareonlyﬁnitelymanyclosedgeodesicsofbounded
length.
We are ﬁnally ready to construct Thurston’s compactiﬁcation of the Te-
ichmüller space, using Bonahon’s geodesic currents.
8.2.15. Projective currents. As usual, we pick a hyperbolic closed sur-
face Sg = H2/Γ. The currents space C is equipped with a multiplication by
positive scalars, hence we can deﬁne its projectivisation
π : C\ 0−→ PC
where PC = (C\ 0)/∼ withα∼λα for allλ> 0. We givePC the quotient
topology.
Proposition 8.2.31. The space PC is compact.
Proof. Pick anα∈ C that ﬁllsSg. By the compactness criterion the
set C ={β∈ C | i(α,β ) = 1} is compact. By Corollary 8.2.25 we have
i(α,β )> 0 for allβ, henceλβ∈C for someλ> 0. Therefore π(C) = PC
and PC is compact. □
We now want to embed bothTeich(Sg) and S in PC.
Proposition 8.2.32. The composition S→ C\ 0→ PC is injective.
Proof. Letγ1,γ 2∈ S be distinct. There is always a closed curveη∈ S
withi(γ1,η )⁄= 0 andi(γ2,η ) = 0. □
Proposition 8.2.33.The compositionTeich(Sg)→ C\0→ PC is injective
and a homeomorphism onto its image.
Proof. Wesee Teich(Sg)alreadyproperlyembeddedin C. Sincei(m,m ) =
−π2χ(Sg) is constant onTeich(Sg), the composition is injective. The restric-
tionπ : Teich(Sg)→π(Teich(Sg)) is also continuous, and we now prove that
it is proper (note that we need to restrict the codomain to get this).
Consider a diverging sequencemj ∈ Teich(Sg). By compactness of PC
the sequence [mj ]∈ PC converges on a subsequence to some[α]∈ PC. For
each j there is aλj > 0 such that λjmj → α in C. Since mj diverges in
Teich(Sg) and hence inC we getλj→ 0. We get
i(α,α ) = lim
j→∞
i(λjmj,λjmj ) =−π2χ(Sg) lim
j→∞
λ2
j = 0.
In particular [α]⁄∈ π(Teich(Sg)). Therefore the restrictionπ : Teich(Sg)→
π(Teich(Sg)) is proper and hence a homeomorphism. □
We will since now consider bothS and Teich(Sg) embedded in PC.
8.2. GEODESIC CURRENTS 237
8.2.16. Thurston’scompactiﬁcation.Weconsidertheclosure Teich(Sg)
of Teich(Sg) inside PC. This closure is compact sincePC is, and it is called
the Thurston compactiﬁcationof Teichmüller space. We deﬁne itsboundary
simply as
∂Teich(Sg) = Teich(Sg)\ Teich(Sg).
Our aim is now to identify the topology of the Thurston boundary. The proof
of Proposition 8.2.33 already shows the following.
Proposition 8.2.34.The Thurston boundary consists of projective currents
[α] withi(α,α ) = 0.
We will later prove that the Thurston boundary actually consists ofall the
projective currents[α]withi(α,α ) = 0. For the moment we content ourselves
with some examples.
8.2.17. Weighted pants decompositions.We construct some geodesic
currents based on geodesic pants decompositions. We will need the following.
Exercise8.2.35. LetP beahyperbolicgeodesicpair-of-pants. Everysimple
geodesicγ in the interior ofP is open and has both ends that converge to∂P,
winding around it.
Hint. DecomposeP into two right-angled hexagons. □
Let aweighted pants decompositionforSg be a pants decompositionµ =
γ1⊔... ⊔γ3g−3 equipped with some real numbersλ1,...,λ 3g−3 > 0. A
weighted pants decomposition deﬁnes a geodesic currentµ = λ1γ1 +... +
λ3g−3γ3g−3 such thati(µ,µ ) = 0.
We will soon prove that[µ] lies in the Thurston boundary ifµ⁄= 0. We
will need the following lemma that characterises the positively weighted pants
decompositions among all currents.
Lemma 8.2.36. Let µ =∑λiγi be a weighted pants decomposition with
all positive weightsλi > 0. A currentα∈ C hasi(α,α ) =i(α,µ ) = 0 if and
only ifα =∑λ′
iγi for some weightsλ′
i> 0.
Proof. Ifα =∑λ′
iγi, then clearlyi(α,α ) = i(α,µ ) = 0. Conversely, let
α be a current withi(α,α ) = i(α,µ ) = 0. Sinceλi > 0, the support ofµ is
the preimage inH2 of the geodesic pants decomposition. Sincei(α,µ ) = 0,
the support ofα consists of lines that are either contained or disjoint from
that ofµ.
By Exercise 8.2.35 a linel of the latter type has both its endpoints at the
endpoints of some line ofµ, so there are only countably many of them overall;
they are not atomic since their projection inSg is not closed and hence have
zero mass. So such linesl do not occur. The support ofα is hence contained
in that ofµ and the proof is complete. □
238 8. SURFACE DIFFEOMORPHISMS
We now characterise simple closed curves.
Lemma 8.2.37. Let γ ∈ S be a simple closed curve andµ∈ C be a
non-trivial current. If i(γ,α ) = 0 implies i(µ,α ) = 0 for allα∈ S, then
[µ] = [γ].
Proof. Extendγ =γ1 to a geodesic pants decompositionβ =∑
iγi. The
previous lemma implies thatµ =∑
iλiγi and by letting the pants decomposi-
tion vary we getµ =λ1γ1. □
8.2.18. Pinching and twisting.How can we construct sequences of hy-
perbolic metrics onSg that converge to some point at inﬁnity? We can do
this quite easily bypinching a simple geodesic, or bytwisting along it.
To deﬁne the former, we need to ﬁx some Fenchel–Nielsen coordinates
(li,θi ) for Teich(Sg) based on a pants decompositionµ = γ1⊔... ⊔γ3g−3.
Fix a metric (li,θi )∈ Teich(Sg). A pinching along γ = γ1 is any sequence
of metrics where the ﬁrst length coordinatel1 tends to zero and all the other
coordinates are kept bounded (from above and below).
Proposition 8.2.38. The limit of a pinching is[γ].
Proof. By the Collar Lemma 7.3.7, the length of a closed geodesicα
in the pinched metrics tends to inﬁnity ifi(γ,α ) > 0 and stays bounded if
i(γ,α ) = 0. Therefore the pinched metrics tend inPC to a class[µ] such that
i(γ,α ) = 0⇒i(µ,α ) = 0 for allα∈ S. Lemma 8.2.37 gives[µ] = [γ]. □
Letm∈ Teich(Sg) be any metric andγ be a closed geodesic. We denoted
bymγ
θ the metric obtained fromm via an earthquake of angleθ alongγ, see
Section 7.2.1.
Proposition 8.2.39. The limit ofmγ
θ asθ→±∞ is [γ].
Proof. By Proposition 7.2.10 the length of a closed geodesicα tends to
inﬁnity ifi(γ,α ) > 0 and is constant ifi(γ,α ) = 0 . We conclude as above
that the metrics tend to[γ]. □
To appreciate the qualitative diﬀerence between pinching and twisting
alongγ, recall the explicit torus case from Section 7.2.4: if we pinch alongγ,
the sequence of metrics converge to[γ]∈∂H2 roughly like a geodesic pointing
to [γ], while if we twist alongγ it does so along a horosphere centred at[γ].
We have discovered in particular that the setS is entirely contained in
Thurston’s boundary. To fully identify the Thurston boundary, we now analyse
the geodesic currentsαlying in the “light cone”, that is those withi(α,α ) = 0.
We already know that the weighted pants decompositions are there, but there
is more: we will soon see that the light cone contains many new fascinating
