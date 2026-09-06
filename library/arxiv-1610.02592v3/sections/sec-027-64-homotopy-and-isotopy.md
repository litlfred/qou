---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-027-64-homotopy-and-isotopy
section_title: "Homotopy and isotopy"
section_number: 6.4
pages: 189-193
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
objects or to prove statements which turn outa posteriori not to depend on
the chosen metric. We will employ this strategy many times in Chapter 8.
6.4. Homotopy and isotopy
We have proved that “homotopy implies isotopy” for non-trivial simple
closed curves inSg, and now we want to prove an analogous result for dif-
feomorphisms ofSg. A crucial ingredient is the following theorem proved by
Smale in the 1950s, which considers the self-diﬀeomorphisms of the discD2.
Theorem 6.4.1. Two diﬀeomorphismsϕ,ψ : D2→ D2 that coincide on
∂D 2 are isotopic, via an isotopy that ﬁxes∂D 2 pointwise.
There is a proof of Theorem 6.4.1 in the topological category that is
surprisingly easy and works in any dimension.
6.4.1. The Alexander trick.The proof of the following fact is so imme-
diate, that it has a name: it is usually called theAlexander trick.
Proposition 6.4.2 (Alexander trick).Two homeomorphismsϕ, ψ :Dn→
Dn that coincide on∂Dn are continuously isotopic, via an isotopy that ﬁxes
∂Dn pointwise.
Proof. We considerf = ϕ◦ψ−1 and idDn and deﬁne an isotopy that
transformsf into idDn ﬁxing∂Dn. The following function does the job:
F (x,t ) =
{ x if‖x‖>t,
tf
(x
t
)
if‖x‖⩽t.
The proof is complete. □
Unfortunately this proof does not work in the smooth category, because
the functionF is not smooth (and not smoothable) at(0, 0). Of course, as
every continuous map, ourF may be approximated by smooth functions, but
the injectivity of the slicesF (·,t ) can be lost in the approximation.
Moreover, the statement in the smooth category is just false in dimension
n> 7: there are self-diﬀeomorphisms ofDn that arenot smoothly isotopic to
idDn inhighdimension, andthisisconnectedtotheexistenceof exoticspheres,
diﬀerentiable manifolds that are homeomorphic but not diﬀeomorphic toSn.
6.4.2. Self-diﬀeomorphisms of the disc.After this very brief excursion
in the topological world, we turn back to the smooth category: every map
considered so far is smooth by assumption like in the rest of the book.
We prove here Theorem 6.4.1. We need a fact on planar ﬁelds.
Proposition 6.4.3. On a nowhere-vanishing vector ﬁeld onR2, a maximal
integral curve is never trapped in a compact set.
182 6. SURFACES
p
(1) (2) (3) (4)
Figure 6.23. At a pointp, after a local diﬀeomorphism we may suppose
that the vector ﬁeld is constantly vertical (1). Ifp is a limit point of an
integral curveα we may ﬁnd a closed curve that bounds a disc (2). If such
a disc existed, we could rotate it and inverse all arrows (3) and glue the
two portions to form a nowhere-vanishing vector ﬁeld on the sphere (4).
Figure 6.24. A self-diﬀeomorphismϕ ofD2 ﬁxing∂D 2 pointwise (left).
To get an isotopy ﬁxing∂D 2 pointwise we need to rescale via a diﬀeo-
morphism that maps each arc as in the right ﬁgure to itself, and varies
smoothly from id tof−1
t from bottom to top (right).
Proof. Suppose by contradiction that a maximal integral curveα:I→ R2
lies in a compact setK for allt >t0. Its ω-limit ω(α)⊂K is the set of all
pointsx∈K to whichγ accumulates, that is the intersection of the closures
of α(t0,∞) for allt0∈ I. The ω-limit is the intersection of a ﬁltration of
compact sets and is hence non-empty. Pick a pointp∈ω(α).
Up to a local diﬀeomorphism, the vector ﬁeld nearp is constant vertical
as in Figure 6.23-(1). The integral curves nearp are vertical. Sincep∈ω(α),
the curveα contains inﬁnitely many of them that tend to the one containing
p. Two subsequent ones determine a closed curve as in Figure 6.23-(2), that
bounds a disc by the Jordan curve theorem.
We prove that such a disc cannot exist. If it existed, we could reverse all
arrows and rotate it to obtain another disc as in Figure 6.23-(3), and by gluing
the two discs we would construct as in Figure 6.23-(4) a nowhere-vanishing
vector ﬁeld on the sphere. Such a ﬁeld of course does not exist since the
sphere has non-zero Euler characteristic. □
We can now prove Theorem 6.4.1.
6.4. HOMOTOPY AND ISOTOPY 183
Proof of Theorem 6.4.1. After composing withψ−1 we can suppose that
ψ = id. Now ϕ|S1 is the identity. Every self-diﬀeomorphism of any compact
manifold that ﬁxes the boundary is isotopic to one which is the identity on a
collar of the boundary: hence we can suppose thatϕ = id on a collar ofS1.
We sketchϕ in Figure 6.24-(left): vertical lines are transformed into paths
with the same endpoints. We want to construct an isotopy betweenϕ and
idD2 that “straightens” smoothly these lines, and we start by straightening their
tangent vector ﬁelds.
Consider the constant unitary vertical vector ﬁeldX0 = (0, 1) onD2 and
let X1 be its image along the diﬀeomorphismϕ. It is easy to construct a
homotopyXt betweenX0 andX1 through non-vanishing vector ﬁelds: we see
both X0 and X1 as mapsD2→ C∗, we lift them to mapsD2→ C via the
universal cover exp : C→ C∗, we make a convex combination and we project
it back toC∗. By construction the vectorsXt are constantly(0, 1) on a collar
ofS1.
We now carefully integrate the homotopyXt of vector ﬁelds to an iso-
topy of diﬀeomorphisms. LetS1
+ and S1
− be the upper and lower hemisphere
of S1. The vectors Xt at S1
− point inside and those atS1
+ point outside
D2. By Proposition 6.4.3 the integral curveγt
x of Xt starting from a point
(x,−
√
1−x 2)∈S1
− exits at some point inS1
+ after some timeTt
x that varies
smoothly inx andt.
The pointγt
x (u) is deﬁned foru∈ [0,T t
x ] and varies smoothly onx,t,u .
We obviously haveT 0
x = 2
√
1−x 2 and also T 1
x = T 0
x since γ1
x = ϕ◦γ0
x.
HoweverTt
x may not be constant int, so we rescale the integral curves as
˜γt
x (u) =γt
x
(
u· Tt
x
2
√
1−x 2
)
.
The new curve˜γt
x is deﬁned in the interval
[
0, 2
√
1−x 2]
not depending ont.
We can now deﬁne
ϕt
(
x,−
√
1−x 2 +u
)
= ˜γt
x (u).
The diﬀeomorphismϕt :D2→D2 furnishes an isotopy betweenid = ϕ0 and
ϕ =ϕ1. However, the diﬀeomorphismϕt does not ﬁx the points inS1
+ since
the endpoint of˜γt
x has a ﬁrst coordinateft(x) which might be distinct fromx
when 0<t < 1 (but varies smoothly ont andx).
To ﬁx that it suﬃces to compose eachϕt with a diﬀeomorphism ofD2
that maps each arc as in Figure 6.24-(right) to itself and varies smoothly from
id tof−1
t from bottom to top. □
Remark 6.4.4. Ifϕ: D2→ D2 is the identity on a collar ofS1, we can
easily transform the isotopyϕt so that it is the identity on this collar for allt.
This will be useful to glue isotopies.
184 6. SURFACES
Figure 6.25. Two essential multicurves (blue and red) in minimal posi-
tion, which subdivide the surface into hexagons.
6.4.3. Homotopy and isotopy of diﬀeomorphisms.We are now ready
to promote homotopies to isotopies of diﬀeomorphisms. We start with the
easier sphere case, which is a simple consequence of Theorem 6.4.1.
Theorem 6.4.5. Two diﬀeomorphismsϕ,ψ : S2→ S2 are isotopic⇐⇒
they are homotopic⇐⇒they are co-oriented.
Proof. We suppose thatϕ andψ are co-oriented and we must prove that
they are isotopic. Pick any discD⊂ S2. Both ϕ and ψ send D to some
disc inS2. Theorem 1.1.14 furnishes an ambient isotopy relating these maps,
so we may suppose thatϕ and ψ coincide onD. The closed complement is
another disc and we conclude by Theorem 6.4.1.
More precisely, we pick a smaller closed discD′⊂ int(D) and consider the
closed complementD′′ =S2\ int(D′). The diﬀeomorphismsϕ and ψ of D′′
coincide on a collar of∂D′′ and Theorem 6.4.1 together with Remark 6.4.4
furnishes an isotopy that is the identity on that collar. We extend this isotopy
as the identity onD\D′′ and we are done. □
The theorem has a very important three-dimensional application.
Corollary 6.4.6 (Smale’s Theorem).Every self-diﬀeomorphism ofS2 ex-
tends to a self-diﬀeomorphism ofD3.
Proof. Every self-diﬀeomorphism ofS2 is isotopic either to the identity or
to a reﬂection by Theorem 6.4.5. We map a collar ofS2 to itself using this
isotopy, then extend to the rest ofD3 using the identity or the reﬂection.□
We can ﬁnally promote homotopies to isotopies on a general genus-g
surface Sg. The proof uses many of the techniques introduced in the last
sections: we employ multicurves to cut the surface into discs, and then use
Theorem 6.4.1 individually on each disc.
Theorem 6.4.7. Two diﬀeomorphismsϕ, ψ :Sg→Sg are isotopic if and
only if they are homotopic.
Proof. We have seen the caseg = 0, so we supposeg> 1. By composing
withψ−1 we can suppose thatψ = id.
