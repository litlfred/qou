---
doc_id: arxiv-1112.5179v1
doc_title: "Prepared for submission to JHEP 3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA "
section_id: sec-012-46-tentacles-and-vacua
section_title: "Tentacles and vacua"
section_number: 4.6
pages: 37-42
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA 2Trinity College, Cambridge CB2 1TQ, UK — We"
---
Some interesting physical consequences of the diﬀerence equations (4.35) result from the fact
that they control the behavior of the index at large charges (m,e ), in a fairly simple manner.
There are actually two ways to send m and/or e to inﬁnity: we can either keep |q| < 1
ﬁxed, or simultaneously send m→∞ and q→ 1 ( ℏ→ 0) so that qm stays ﬁxed. In the
latter case, the index IM diverges, with leading asymptotics governed by the volume of M.
Mathematically, this is a familiar phenomenon, closely related to the “Volume Conjecture”
for Chern-Simons partition function. Physically, it seems closely related to Z-extremization
[2], though the precise connection is still not well understood.
We will mention some aspects of theq→ 1 limit at the end of this section. For now, let’s
instead consider the less familiar limit ( m,e )→∞ with|q|< 1 ﬁxed. The leading behavior
of the index 19 in this limit is simply governed by the classical LagrangianLM(x,p ) (4.36),
and turns out to detect the presence of unconstrained chiral operators in the theory TM.
Equivalently, the leading behavior can detect when TM has a moduli space of vacua.
In order to make a more precise statement, note that superconformal theories TM (and
more generally theories in class R) should have an index IM(m,e ;q) such that the powers
of q appearing at ﬁxed ( m,e ) are bounded from below ( cf. Section 2). Then we can deﬁne
leadM(m,e ) to be the lowest power ofq the appears inIM(m,e ;q) — this is the ﬁrst nontrivial
R + j3
2 contribution of an operator with charge e in the presence of ﬂux m. We claim that
leadM(m,e ) generically grows quadratically as m,e→∞ , but that restricted to special rays
in charge space it may instead grow linearly. These are exactly the rays along which the
“amoeba” of LM has a “tentacle.” Moreover, when we are in an Sp(2N, Z) duality frame
such that a ray/tentacle lies in a purely electric direction, the theory TM should have an
unconstrained chiral operator O that prodces the leading contribution to the index, and
parametrizes a 3d moduli space of vacua.
We will try to motivate these statements physically and mathematically. To begin, let
us recall the formal deﬁnition of an amoeba [63]. Given an algebraic variety in ( C∗)2N, say
with coordinates (xi,pi), the amoeba is its projection to the real subspace spanned by the
magnitudes
ReXi = log|xi|, RePi = log|pi|. (4.47)
19The leading behavior is all we will look at here. It would be very interesting to also consider subleading
corrections and their physical implications.
– 36 –
∼− e
∼− m
∆
Re(P)
Re(X)
31
Re(P)
Re(X)
41
Re(P)
Re(X)
Figure 7. Amoebas for the tetrahedron, trefoil, and ﬁgure-eight knot Lagrangians.
For example, the classical LagrangiansLM for the tetrahedron, trefoil, and ﬁgure-eight knot,20
L∆ = p +x−1− 1 = 0, (4.48a)
L31 = p−x3 = 0, (4.48b)
L41 = p−1 + (x−2−x−1− 2−x +x2) +p = 0, (4.48c)
have the amoebas shown in Figure 7. A salient feature of the amoebas is that they extend
asymptotically along a ﬁnite collection of semi-inﬁnite rays, or tentacles. These tentacles occur
whenever there is a solution to the deﬁning equations ofLM in the limit (|x|,|p|) = (enr,ens),
n→∞ , for some nontrivial integer slope vector ( r,s ).
The tentacles of amoebas in LM actually arise physically as parameter spaces of vacua
for the 3d theories TM in ﬂat R3. One indirect but instructive way to see this is to recall
from [9] or [19] that the entire complex Lagrangian LM is the SUSY parameter space for TM
compactiﬁed on (untwisted) R2×S1
R. This eﬀective 2d N = (2, 2) theory has a complex,
periodic twisted mass associated to each U(1) global symmetry, obtained by complexifying
the 3d real mass with the Wilson line of the background U(1) gauge ﬁeld. We can multiply
this mass by the radius R to make it dimensionless, and express it as
X =Rm 3d +i
∮
S1
R
A. (4.49)
The 2d theory also has a complexiﬁed, periodic FI parameter (or moment map), naturally
obtained by combining the 3d FI parameter ξ3d and the 2d background θ-angle:
P =Rξ 3d +iθ. (4.50)
20It is easy to see that these are classical q→ 1 limits of the corresponding operators in Section 4.5, with
x =M and p =−𝓁 in the case of knot complements. For the ﬁgure-eight knot, one must throw out an extra
factor of (x2− 1) that only arises in (4.46) as a quantum correction. Evidently, this factor is not relevant for
analyzing vacua or ﬂat directions in the index.
– 37 –
The 2d twisted superpotential preserves supersymmetry when
exp
(
∂~W
∂X
)
= exp(P ) (4.51)
(put diﬀerently, the FI parameter P contributes toW as XP ), and it was argued in [9, 19]
that (4.51) are just the deﬁning equations for LM.
To lift back up to a SUSY parameter space in 3d, we can ﬁrst restrict to the real parts
of X and P , and then send R→∞ . The ﬁrst operation projects LM onto its amoeba, and
the second scales the amoeba so that only the tentacles — a collection of semi-inﬁnite rays —
are left. Suﬃciently far along these rays, Re X and ReP (or rather m3d and ξ3d) are the 3d
masses and FI parameters consistent with SUSY. Near the origin, quantum corrections may
still play an interesting role, which will not aﬀect the current story. 21 We emphasize that the
tentacles map onto a parameter space of vacua. However, if any of the tentacles happen to
align with the P axis (or plane) at X = 0, an actual SUSY moduli space in TM also opens
up. This is because the eﬀective background FI parameter Re P (ξ3d) is a real moment map
for a U(1) symmetry. Then, for example, SUSY requires that ξ3d sets the vev for a sum
of chiral ﬁelds ∑
jQj|φj|2, where Qj are the U(1) charges. Preserving SUSY at any value
of ReP∼ ξ3d while simultaneously having zero mass Re X∼ m3d means there must be an
inﬁnite ﬂat direction in dynamical ﬁeld space.
This phenomenon is simple to illustrate in the tetrahedron theory. Its amoeba does have
a tentacle on the negative Re P axis (or |p|→ 0). Correspondingly, T∆ has a free chiral
operator φZ charged under the single global U(1), whose vev parametrized a moduli space.
We have|φZ|2 +ξ3d = 0, or |φZ|2∼− ξ3d∼− ReP . The other tentacles of the amoeba lie
along|x|→∞ and|p|→∞ ,|x|→ 0. In either case, we can happily preserve SUSY, though
the ﬁeld φZ becomes massive. If we apply a Tk∈ Sp(2, Z) transformation to T∆ to shift
the Chern-Simons level by k, the story remains essentially the same; we clearly still get a
moduli space, while the amoeba gets “skewed” horizontally without lifting its tentacle from
theP -axis. (Recall that Sp(2, Z) simply acts by multiplication on the symplectic vector
(X
P
)
,
so Tk :
(X
P
)
↦→
( X
P +kX
)
.) On the other hand, generic Sp(2, Z) images of T∆ have no moduli
space at all.
Now, let us return to the index. Suppose that TM has a moduli space corresponding to a
tentacle ofLM at ReX = 0, along a ray in the Re P plane pointing in direction s (with s an
N-dimensional vector of coprime integers). The direction s selects a U(1) symmetry inside
U(1)N whose moment map can be nonzero. We would then expect that the moduli space is
parametrized by the vev of a chiral operator O with electric charge e =−s. This operator
and its powersOn can potentially contribute to the index. It is not completely clear that the
contribution will be the dominant one (at leading order in q), but if it is, then
lead(0,−ns) = RO
2 n, n ≫ 0, (4.52)
21In 2d, quantum corrections are responsible for smoothing the asymptotic regions of the parameterLM into
a connected algebraic variety. Otherwise,LM would be a collection of “cigars” centered around each tentacle.
– 38 –
whereRO is the R-charge ofO. This behavior should at east hold true for suﬃciently large n.
Thus the index (potentially) develops an asymptotically “ﬂat” direction along the tentacles
of the amoeba.
Figure 8 . Graph of the leading exponent
lead(m,e ) for the ﬁgure-eight index.
Here we used the presence of a moduli space
to argue for linear growth of lead( m,e ) in a dis-
tinguished electric direction — corresponding to a
tentacle in the P plane. However, an Sp(2N, Z)
transformation could be used to align any tenta-
cle with the P plane. Since Sp(2N, Z) acts co-
variantly on the index, preserving the growth of
lead(m,e ), this implies that we could actually ex-
pect linear growth along every tentacle, in any di-
rection. Explicitly, if a tentacle extends in direc-
tion (r,s ), so that (|x|,|p|)∼ (enr,ens), n→∞ ,
lies inLM, then
lead(−rn,−sn)∼ n, n →∞ . (4.53)
It is easy to see from Figure 1 that this holds for
T∆: ﬂat directions (anti)align with tentacles. In Figure 8, we similarly plot lead 41(m,e ) for
the ﬁgure-eight knot. 22 For the trefoil, (4.53) holds in a trivial way: the index I31 = δe,3m
vanishes except right on the tentacles, where it is constant.
The behavior (4.53) is (roughly) predicted mathematically by the general structure of the
diﬀerence equations ˆLM, and the fact that they are quantizations of the classical Lagrangian
LM. The simple property that the operators ˆLM are polynomials in ˆx±, ˆp±, andq, along with
the assumption that indices IM(m,e ;q) are q-series bounded from below, implies that the
generic growth of lead(m,e ) is quadratic ( cf. [64]). This is essentially because the operators
ˆx±, ˆp± only involve linear factors q
m
2 and q
e
2 , and can also only generate other linear factors
when shifting m ande in quadratic parts of the index. For example, ˆx+·qe2
= (q
m
2−2e−1)qe2
.
All these linear factors then enable cancellations between diﬀerent terms in the equations
ˆLMIM = 0.
Nevertheless, linear growth of the index is permitted along directions (anti)parallel to
tentacles of the amoeba ofLM. The tentacles are normal vectors to boundary surfaces of the
Newton polygon of LM, and also (roughly) the Newton polygon of ˆLM. This allows extra
cancellations to happen in the diﬀerence equations, along these distinguished directions. A
more detailed, albeit heuristic, explanation is given in Appendix D.
One potential application of the observed growth rates of the index is to shed some light
on the convergence of sums (4.6) that deﬁne IM. Speciﬁcally, suppose that we start with a
triangulation ofM and ﬁrst construct a product indexI{∆i},{Πi} =I∆1×···×I ∆N . We then
22The tentacles and ﬂat directions of knot complements always occur back-to-back, due to the Z2 Weyl
symmetry (4.15). This is nicely illustrated in Figures 7 and 8.
– 39 –
transform this to a polarization ~Π, in which all internal edges of M are electric. If we chose
a reﬁned, “easy” triangulation — so that it properly deﬁnes a theory TM — there must be
a chiral operator OI associated to every internal edge, and charged under the edge coordi-
nate’s U(1) symmetry. Moreover, before doing the ﬁnal index sum (4.6), we shift R-charge
so that every OI has ROI = 2. In this aﬃne Sp(2N, Z) frame, we know that the leading
exponent function lead{∆i},˜Π(m,e ) of the product indexI{∆i},˜Π(m,e ) should grow linearly in
any electric directioneI corresponding to the charge ofOI, with slope ROI/2. In the negative
direction−eI, we generically expect quadratic growth instead. To compute the ﬁnal index
IM, we set magnetic charges mI→ 0 (just like in the analysis above), and sum along both
positive and negative eI directions. We would then expect the sum not only to converge, but
to do so “uniformly”: in order to compute IM(m,e ) at ﬁxed external charges ( m,e ) to nth
order in q, we should need to sum only from about −neI to neI in each direction. This has
certainly been observed in examples.
To close this discussion, let us also return to the other, ’t Hooft-like, asymptotic limit of
the index. Rather than taking ( m,e )→∞ along a ray, with|q|< 1, we send both m→∞
andq→ 1 (ℏ→ 0) with qm held ﬁxed. Working in an electric fugacity basis, we can use ζ to
complexify the naturally real number qm, and set
x =qmζ (4.54)
as in (3.6). Then, just as we found in Section 3 that the tetrahedron index is dominated
approximately by the hyperbolic volume of a tetrahedron,
I∆(m;q,ζ ) ∼ exp
( 2
iℏV∆(z) +...
)
, V ∆(z) =−Im Li2(z−1), (4.55)
we now ﬁnd that the index IM is dominated approximately by the hyperbolic volume 23 of
M,
IM(m;q,ζ ) ∼ exp
( 2
iℏVM(x) +...
)
. (4.56)
Note that this volume depends on boundary conditions x. For example, the volume depends
on the external dihedral angles of a geodesic boundary, or on the metric (or SL(2, C)) holon-
omy around a cusp boundary ofM. It diﬀers very slightly from the actual hyperbolic volume,
but the diﬀerence is easy to correct: the actual volume is
VolM(x) =VM(x) + (ImP )· (ReX), (4.57)
where (x,p ) = (eX,eP ) is a point on the LagrangianLM (a solution to the deﬁning equations
forLM at ﬁxed x). Note that while VM(x) and Im P have branch cuts, VolM(x) should be
well deﬁned.
23IfM does not admit a deformed hyperbolic structure with speciﬁed boundary conditions, the formula still
holds, but “volume” means volume of a ﬂat SL(2, C) connection.
– 40 –
Figure 9. The Kinoshita-Terasaka (left) and Conway (right) knots, related by a nontrivial mutation
operation.
One way to check (4.56), up to a constant, is to note that the leading asymptotics of the
index must be governed by the classical ℏ→ 0 (q→ 1) limit of the diﬀerence operators ˆLM.
In particular, the point (X, P= ∂VM
∂X ) must lie on the classical LM. This property is known
to characterize volumes of 3-manifolds [23]. Physically, the asymptotics (4.56) are extremely
familiar from the study of ellipsoid partition functions Zb[TM] and twisted R2×S1 partition
functions of TM, both of which are very closely related to the index. We will discuss the
relations further in Section 6.3.
