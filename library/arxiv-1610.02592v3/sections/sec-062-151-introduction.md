---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-062-151-introduction
section_title: "Introduction"
section_number: 15.1
pages: 451-458
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
It sometimes happens in three-dimensional topology, that a topological or
geometric property of a manifold is preserved under Dehn ﬁllings, with only
few exceptions. For instance, the Dehn ﬁlling of a Seifert manifold is again a
Seifert manifold, with only one exception (a ﬁbre-parallel Dehn ﬁlling gives a
connected sum of Seifert manifolds, see Corollary 10.3.44).
The most striking appearance of this phenomenon is the Hyperbolic Dehn
ﬁlling Theorem, proved by Thurston at the end of the 1970s. This theorem
says roughly that “most” Dehn ﬁllings of a cusped hyperbolic manifold are still
hyperbolic.
15.1.1. GeneralisedDehnﬁllingparameters. Inallthischapter,wecon-
sider a compact oriented three-manifoldN with∂N =T1⊔...⊔Tc consisting
of tori, and we ﬁx generatorsmi,li for everyπ1(Ti ).
Let a generalised Dehn ﬁlling parameters = (s1,...,s c) be a sequence
where eachsi is either the symbol∞or a rationally related pair of real numbers
(p,q ) = ( kp′,kq′) = k(p′,q′) where k > 0 is real and (p′,q′) are coprime
integers. We think atsi as lying in the two-sphereS2 = R2∪{∞}.
443
444 15. HYPERBOLIC DEHN FILLING
A generalised Dehn ﬁlling parameters determines a Dehn ﬁllingNﬁll ofN
as follows: for everyi, ifsi =k(p′,q′) we ﬁllTi by killing the slopep′mi +q′li,
while ifsi =∞ we do nothing. The result is a new compact manifold, that
may be closed (if there are no∞ in s) or be bounded by some tori. We also
mark the cores of the ﬁlled solid tori with the labelαi = 2π
k > 0.
15.1.2. The Hyperbolic Dehn ﬁlling Theorem.This chapter is mainly
devoted to the proof of the following theorem.
Theorem 15.1.1. Let M = int(N) be a complete orientable ﬁnite-volume
cusped hyperbolic three-manifold. There is a neighbourhoodU of (∞,..., ∞)
inS2×... ×S2 such that for every generalised Dehn ﬁlling parameters∈U
the interiorMﬁll of the manifoldNﬁll obtained by Dehn ﬁllingN alongs admits
a ﬁnite-volume complete hyperbolic structure with cone angles.
The cores of the ﬁlling solid tori are closed geodesics with cone anglesαi.
The singular locus ofMﬁll consists of the core geodesics withαi⁄= 2π.
Ifs∈U is an ordinary (not extended) Dehn ﬁlling parameter (see Section
14.2.1), that is ifsi is either∞ or a coprime pair(p,q ) for alli, thenαi = 2π
and Nﬁll is a hyperbolic manifold without cone angles: this is of course the
case of most interest.
Corollary 15.1.2. Let M = int(N) be a complete orientable ﬁnite-volume
hyperbolic three-manifold. For everyi = 1,...,c there is a ﬁnite setSi of
slopes inTi such that for every Dehn ﬁlling parameters withsi⁄∈Si for alli,
the ﬁlled manifoldMﬁll = int(Nﬁll) is hyperbolic.
WhenM has one cusp, the corollary may be stated simply as follows.
Corollary 15.1.3. If M is a complete orientable ﬁnite-volume hyperbolic
three-manifold with one cusp, all but ﬁnitely many Dehn ﬁllingsMﬁll are hy-
perbolic.
To appreciate the power of these theorems, consider for instance a hyper-
bolic linkL⊂ S3 (recall thatL⊂ S3 is hyperbolic ifS3\L admits a ﬁnite-
volume complete hyperbolic metric). By the hyperbolic Dehn ﬁlling theorem,
there is a ﬁnite subsetS⊂ Q such that every surgery onL with coeﬃcients
in Q\S produces a closed hyperbolic manifold.
15.1.3. Examples. Wedescribeacoupleofclarifyingexamples. Weknow
that the ﬁgure eight knotK⊂S3 is hyperbolic: by the Dehn ﬁlling Theorem,
there is an open neighbourhoodU⊂S2 of∞ such that every Dehn surgery
onK with parameters∈U produces a hyperbolic cone manifold.
We will prove in the next section that the subsetU shown in Figure 15.1
fulﬁls this requirement. The only coprime pairs(p,q ) that are not contained
inU are those withp
q equal to one of the following
(21) − 4,−3,−2,−1, 0, 1, 2, 3, 4,∞.
15.1. INTRODUCTION 445
0
(-4,-1) (4,-1)
(-4,1) (4,1)
(-5,0) (5,0)
U
Figure 15.1. Hyperbolic Dehn ﬁllings on the ﬁgure-eight knot complement.
p
q manifold
0 T( 3 1
−1 0
)
±1
(
S2, (2, 1), (3, 1), (7,−6)
)
±2
(
S2, (2, 1), (4, 1), (5,−4)
)
±3
(
S2, (3, 1), (3, 1), (4,−3)
)
±4
(
D, (2, 1), (2, 1)
)⋃(0 1
1 0
)(
D, (2, 1), (3, 1)
)
Table 15.1.The non-hyperbolic Dehn surgeries of the ﬁgure-eight knot.
WegetatorusbundlewithAnosovmonodromyandhenceof Solgeometry,
three Seifert manifolds of~SL2 geometry, and a graph manifold that splits
into two Seifert manifolds via a map that interchanges the ﬁbres and the
boundarysectionsofthetwoportions(themapisheredenotedbyamatrix
in the section-ﬁbre basis).
Every other surgery onK yields a closed hyperbolic three-manifold. For in-
stance, the manifold Vol2 from Table 14.5 can be obtained withp
q =±5
(there is a symmetry ofK sending p
q to−p
q).
On the other hand, ap
q surgery from the list (21) does not produce a
hyperbolic manifold: see Table 15.1, taken from Martelli – Petronio [38].
More generally, a parameterk(p,q ) ∈ U produces a hyperbolic closed
manifold with a core geodesic of cone angle2π
k , which may be interpreted as
an orbifold whenk∈ N. In particular, if(p,q ) = (1, 0) the closed manifold is
just S3, because an∞-surgery on a knot inS3 gives S3 back. Therefore by
looking at Figure 15.1 we discover that for everyk> 5 there is a hyperbolic
structure onS3 with cone angle2π
k on the ﬁgure-eight knotK.
We now consider a link with two components. The Whitehead link L
shown in Figure 14.10 is hyperbolic: it is hard to determine an explicit open
446 15. HYPERBOLIC DEHN FILLING
P R
F
J
P R
J
F
I
V
III VII
VIII
IV
VI II
2
2 3
3
1
1 2
2 3
3
1
1
3
1 2
3
1 2
3
1 2
3
1 2
3
1 2
3
1 2
3
1 2
3
1 2
Figure 15.2. We truncate the tetrahedra and ﬂatten their boundary.
We assign a modulusz and w to them. The edge numberedi = 1, 2, 3
has moduluszi (on the left tetrahedron) orwi (on the right tetrahedron).
I III
II IV VI VIII
V VIIm
l
z1 z2
z3
z1 z2
z3
z3 z1
z2
z3 z1
z2
w1 w3
w2
w1 w3
w2
w2 w1
w3
w2 w1
w3
Figure 15.3. The triangulated boundary is a torus obtained by identify-
ing the opposite edges of this parallelogram. The triangulationT has two
edges, that we colour in red and white. Their endpoints are shown here.
set U⊂ S2×S2 in this case, but a careful computer-aided analysis carried
with SnapPy [15] shows the following, see [38].
Theorem 15.1.4.A surgery on the Whitehead link with coeﬃcients(p
q, r
s )
produces a closed hyperbolic manifold, unless one of the following holds:
• p
q or r
s belongs to the set{0, 1, 2, 3, 4,∞},
• up to permutation the pair
(p
q, r
s
)
belongs to the set
{
(−4,−1), (−3,−1), (−2,−2), (−2,−1),
( 3
2, 5
)
,
( 4
3, 5
)( 5
2, 7
2
)}
.
The proposition is symmetric in the two coeﬃcients because the link itself
has a symmetry that interchanges the two components. All the Dehn ﬁlling
parameters listed in the theorem indeed produce non-hyperbolic manifolds. For
instance, if p
q∈{ 1, 2, 3} we get a Seifert manifold ﬁbering over the disc with
two singular ﬁbres, see [38].
We ﬁrst prove Theorem 15.1.1 for the ﬁgure-eight knot, where the com-
binatorics is so simple that everything can be veriﬁed by hand. We will then
prove the theorem in general in Section 15.2 using more sophisticated tools.
15.1. INTRODUCTION 447
15.1.4. The ﬁgure-eight knot example.We now discuss in detail the
standard example: the ﬁgure-eight knot complement, one of the very few
cases where the consistency and completeness equations can be solved by
hand. This part will not be needed in the proof of Theorem 15.1.1, so the
reader may wish to skip it and go directly to Section 15.1.5.
LetT be the triangulation with two tetrahedra shown in Figure 14.7. The
truncated version is in Figure 15.2. We assign the complex variablez and w
to the left and right tetrahedron, respectively. We set
z1 =z, z 2 = 1
1−z, z 3 = z− 1
z
and deﬁnew1,w 2,w 3 similarly. Recall that
(22) z1z2z3 =w1w2w3 =−1.
The modulus of an edge in Figure 15.2 labeled withi∈{ 1, 2, 3} is zi or wi
depending on the tetrahedron. With some patience one sees that the boundary
triangulated surface is a torusT as in Figure 15.3. The triangulationT has
two edges shown in Figure 14.7, each yielding a consistency equation. Figure
15.3 shows that the consistency equations are
z 2
2z3w 2
2w3 = 1, z 2
1z3w 2
1w3 = 1.
Using (22) we see that the equations are both equivalent to
z2w2 =z1w1,
that is
(23) z(1−z)w (1−w ) = 1.
We now look at the boundary torusT. Letm andl be the generators ofπ1(T )
shown in Figure 15.3. We have
(24) µ(m) =−z1z3w1 =w (1−z), µ (l) =z 2
2z 2
3w 4
1w 2
2w 2
3 = z 2
w 2.
The completeness equations are
(25) w (1−z) = 1, z 2 =w 2.
Exercise 15.1.5. The only solution to (23) and (25) isz =w =e
πi
3 .
We have conﬁrmed that the ﬁgure-eight complementM has a complete
hyperbolicstructureobtainedbyrepresentingbothtetrahedrawithidealregular
hyperbolic tetrahedra. We now investigate the non-complete solutions of the
consistency equations.
The two ideal tetrahedra have moduliw andz and the consistency equa-
tions reduce to one equation (23) which we rewrite as
z 2−z + 1
w (1−w ) = 0.
448 15. HYPERBOLIC DEHN FILLING
0 1
i
i2
complete 0
(-4,-1) (4,-1)
(-4,1) (4,1)
(-5,0) (5,0)
R s
d
Figure 15.4. Every w ∈ R determines a hyperbolic structure forM
(left). The Dehn ﬁlling generalised invariantsd mapR onto a neighbour-
hood of∞ (right).
The solutions are
z =
1±
√
1− 4
w(1−w)
2 .
Weareonlyinterestedinsolutionswith ℑz,ℑw >0. Foreveryw withℑw >0
there is a unique solutionz withℑz >0, except when∆∈ R>0.
Exercise 15.1.6. We have∆ = 1− 4
w(1−w)∈ R>0 if and only ifw belongs
to the half-lines =
{ 1
2 +yi withy>
√
15
2
}
, see Figure 15.4-(left).
We deﬁne the open region
R ={w∈ C|ℑw >0}\ s.
Everyw∈R determines a hyperbolic structure forM. The complete structure
is obtained atw0 = 1
2 +
√
3
2 , see Figure 15.4-(left).
The manifoldM is a knot complement and hence the boundary torusT is
equipped with its natural meridian/longitude basism′,l′, see Section 11.3.1.
Using SnapPea we ﬁnd out that
m′ =m, l ′ =l + 2m.
From (24) we get
(26) ˜µ(m′) =w (1−z), ˜µ(l′) = z 2
w 2w 2(1−z)2 =z 2(1−z)2.
We ﬁxm′,l′ as generators forπ1(T ). We deﬁned in Section 14.2.7 the gen-
eralised Dehn surgery invariant(p,q ) =d(w ) for every non-complete solution
w∈R\{w0}. This gives a continuous map
d :R−→S2
that sendsw0 to∞.
Proposition 15.1.7. The imaged(R) contains the coloured region shown
in Figure 15.4-(right).
15.1. INTRODUCTION 449
Proof. The domainR is an open disc and its abstract closure¯R is home-
omorphic to the closed disc. We show thatd extends to a continuous map
¯R→S2 which sends∂R to the almost-rectangle shown in Figure 15.4.
The invariantsd(w ) = (p,q ) are such that
(27) wp(1−z)p+2qz 2q =e2πi.
The regionR has two involutions (determined in fact by isometries ofM):
• the involutionτ(w ) =z =
1±
√
1− 4
w(1−w)
2 . This involution sendsµ(m)
toµ(m)−1 =µ(m−1), henced(τ(w )) =−d(w );
• the involutionσ(w ) = 1−w: using (26) we getd(σ(w )) =d(w ).
Now we note that whenw tends to a point in the linel+ = [1, +∞] then z
tends to a point inl− = [−∞, 0]. Therefore the argument ofw,z, 1−z tends
respectively to 0,π, 0. Equation (27) implies thatq→ 1.
Ifw→ 1thenz→−∞ and (27) implies thatp+2q+2q =p+4q→ 0, so
(p,q )→ (−4, 1). Ifw→ +∞ thenz→ 0 and equationz(1−z)w (1−w ) = 1
implies that|z||w|2→ 1; here (27) gives|w|p−4q→ 1, hencep− 4q→ 0, so
(p,q )→ (4, 1). We have proved thatd maps [1, +∞] onto the segment
(−4, +1), (+4, +1).
Using the involutionτ we deduce thatd maps [−∞, 0] onto the segment
(+4,−1), (−4,−1).
When w is near the right side of the half-lines, the numberz tends to the
segment (0, 1
2]. Therefore the arguments ofz and 1−z tend to 0 and (27)
implies that the argument ofwp tends to 2π. When w∈s the argument of
w is at leastarctan
√
15 = 1.31811607... and hencep is at most 2π
arctan
√
15 =
4.374... < 5. This implies that we can connect (4, 1) and (4,−1) while
staying inside the image ofd with a curve as in Figure 15.4. □
15.1.5. A road map.The rest of this chapter is mostly devoted to the
proof of Theorem 15.1.1. Here is our plan: we ﬁrst study the combinatorial
properties of an arbitrary ideal triangulationT forM, and we prove that the
solutions to the consistency equations form a complex manifoldDef(M,T )
of (complex) dimensionc equal to the number of cusps ofM. The manifold
Def(M,T ) is nicely parametrized by the holonomies on anyc ﬁxed curves at
diﬀerent cusps.
The manifold Def(M,T ) is often empty, but sinceM is hyperbolic we
expect that there should be some ideal triangulationT for which Def(M,T )
is not empty and contains a solutionz that also satisﬁes the completeness
equations (we are unfortunately not able to prove this in general, and this
will be a technical issue). The generalised Dehn ﬁlling invariants deﬁned in
Section 14.2.7 furnish a local diﬀeomorphismd : Def(M,T )→S2×... ×S2
thatsends z to (∞,..., ∞). Inparticularthismapisopenanditsimagecovers
450 15. HYPERBOLIC DEHN FILLING
a neighbourhoodU of (∞,..., ∞). We conclude thanks to the discussion of
Section 14.2.7.
