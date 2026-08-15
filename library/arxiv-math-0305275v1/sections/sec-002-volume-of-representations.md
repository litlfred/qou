---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds Stefano Francaviglia12"
section_id: sec-002-volume-of-representations
section_title: "Volume of representations"
section_number: null
pages: 9-15
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds Stefano Francaviglia12 — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2"
---
For this section we ﬁx an ideally triangulated manifold M and a representa-
tion ρ :π1(M) → Isom+(H3).
In this section we recall the notion of volume of an equivariant map fr om
~M to H3. We prove that if we restrict to the class of pseudo-developing
maps, then the volume of ρ is well-deﬁned. Namely the volume does not
depend neither on the pseudo-developing map nor on the product s tructure
of the cusps. Such a volume can be calculated using a straightening o f any
pseudo-developing map and it is exactly the algebraic sum of the volum es of
the straightened tetrahedra.
Deﬁnition 4.1 (Volume of pseudo-developing map) LetDρ be a pseu-
do-developing map for ρ. Let ω be the volume form of H3 and let D∗
ρω be
9
the pull-back of ω. Since Dρ is equivariant, then D∗
ρω projects to a 3-form,
that we still call D∗
ρω, on M. The volume vol( Dρ) of Dρ is deﬁned by:
vol(Dρ) =
∫
M
D∗
ρω.
Remark 4.2 We will see below that for pseudo-developing maps the vol-
ume is always ﬁnite. The same deﬁnition of volume does not work for an y
equivariant map from ~M to H3 because if the pull-back of the volume form
is not in L1, then the volume is not well-deﬁned.
Deﬁnition 4.3 (Straight volume) Let Dρ be a pseudo developing map
for ρ. Let {∆ i} be the set of the tetrahedra of the ideal triangulation of M
and { ~∆ i} be a set of lifts of the ∆ ′
is. Let vi = 0 if Str( ~∆ i) is a degenerate
tetrahedron, and let vi be the algebraic volume of Str( ~∆ i) otherwise.
We deﬁne the straight volume of ( Dρ) as Strvol(Dρ) = ∑
ivi.
Remark 4.4 Let ∆ 1,..., ∆ n be the tetrahedra of τ . Let z = (z1,...,z n) ∈
{C \ {0, 1}}n be a solution of Thurston’s hyperbolicity equations (see [BP],
[F], [NZ], [PP], [PW], [Th1]). Then there exists a developing map Dz : ~M →
H3 for z that is a pseudo-developing map for some holonomy ρ(z). Such a
map is already straight and we have Strvol( Dz) = vol(Dz) = ∑ vi = vol(z),
where vi is the volume of the geodesic ideal tetrahedron of modulus zi.
Let Cp = Tp × [0, ∞]/∼ be a cusp of M and let N~p = P~p × [0, ∞]/∼
be one of its lifts in ~M. Then we can identify π1(Cp) with Stab( ~p). Let
f : P~p × {0} → H3 be a Stab( ~p)-equivariant map, let ξ ∈ ∂H3 be a ﬁxed
point of ρ(Stab(~p)) and let F : N~p :→
H
3
be the cone-map obtained by
coning f to ξ. As above, let F ∗ω be the pull-back of the volume-form on
Cp. Similarly we can pull-back the metric. We call Ap
t the area of the torus
Tp × {t}.
Lemma 4.5 In the previous setting, for t>r we have:
Ap
t ≤Ap
re−(t−r) and
∫
Tp×[t, ∞)
|F ∗ω| ≤ Ap
t.
Proof. Let (x,y ) be local coordinates on P~p. Choose the half-space model
C × R+ of H3 and assume that ξ = ∞. In such a model the hyperbolic
metric at the point ( z,s ) is the Euclidean one rescaled by the factor 1 /s. It
10
follows that, called α +iβ and h the complex and real components of F , we
have
α(x,y,t ) +iβ(x,y,t ) = α(x,y,r ) +iβ(x,y,r ) h(x,y,t ) = h(x,y,r )e(t−r).
The element of area at level t isdσt(x,y ) =
√
det(TJF t ·H ·JF t), where
Ft is the restriction of F to P~p × {t} and H(x,y,t ) = 1
h2 Id is the matrix of
the hyperbolic metric. From direct calculations it follows that dσt(x,y ) ≤
dσr(x,y )e−t+r and the ﬁrst inequality follows.
Now note that the volume element |F ∗ω| at the point ( x,y,t ) ∈ Cp is
bounded by the area element of the torus Tp × {t} multiplied by the length
element of the ray {(x,y )} × [0, ∞]. Since the parameter t is exactly the
arc-length, then the length element is exactly dt. It follows that
∫
Tp×[t, ∞)
|F ∗ω| ≤
∫ ∞
t
Ap
sds ≤
∫ ∞
t
Ap
te−(s−t)ds =Ap
t.
This completes the proof.
✷
Remark 4.6 From Lemma 4.5 it follows in particular that
∫
Tp×[t, ∞) |F ∗ω| ≤
Ap
0e−t. This means that we have an estimate of
∫
Tp×[0, ∞) |F ∗ω| not depending
on the point ξ =F (p) but only on the area of Tp × {0}.
Remark 4.7 From Lemma 4.5 it follows that vol( Dρ) is ﬁnite for any pseu-
do-developing map Dρ.
The following lemma is proved in [D].
Lemma 4.8 If Dρ and Fρ are two pseudo-developing maps for ρ that agree
on the ideal points, then vol(Dρ) = vol(Fρ).
This is because any two pseudo-developing maps are equivariantly homotopic.
The fact that they coincide on the ideal points allows one to constru ct a
homotopy h that respects the cone structures of the cusps. Namely, for
each ideal point ~p of ~M we choose any equivariant homotopy between the
restrictions of Dρ andFρ toP~p ×{¯t}, where ¯t = max{tDρ,t Fρ }, we cone such a
homotopy toDρ(~p) along geodesic rays, and we extend the homotopy outside
the cusps in any equivariant way. For such a homotopy h we can use the
Stokes theorem on M × [0, 1] for h∗ω to obtain the thesis. More precisely,
11
let Kt be M \ ∪p(Tp × (t, ∞)), where p varies on the set of the ideal points;
then we have
0 =
∫
Kt×[0, 1]
d(h∗ω) =
∫
∂ (Kt×[0, 1])
h∗ω =
∫
Kt
(D∗
ρω −F ∗
ρω) +
∫
∂K t×[0, 1]
h∗ω
and, as in Lemma 4.5, we can prove that the last integral goes to zer o as
t → ∞.
We now prove that the claim of Lemma 4.8 is true in general.
Theorem 4.9 Let Dρ and Fρ be two pseudo-developing maps for ρ. Then
vol(Dρ) = vol(Fρ).
Proof. Fort ∈ [0, ∞), let Dt
ρ be the map constructed as follows: Dt
ρ coincides
with Dρ until the level t of each cusp. Then for each cusp Np we complete
Dt
ρ by coning D|Pp×{t} to Fρ(p) along geodesic rays in such a way that the
arc-length is the parameter s −t, where s ∈ [t, ∞). Now, Dt
ρ is a pseudo-
developing map that agrees with Fρ on the ideal points. Thus by Lemma 4.8
vol(Dt
ρ) = vol( Fρ). Since Dt
ρ and Dρ agree outside the cusps and where
they diﬀer they are cones on the same basis (and diﬀerent vertices ), from
Lemma 4.5 we get
|vol(Dρ) − vol(Dt
ρ)| ≤ 2
∑
p
Ap
t ≤ 2(
∑
p
Ap
0)e−t
where p varies on the set of ideal points and Ap
t is the area of the torus
Tp × {t}. As t → ∞ we get the thesis.
✷
Similar techniques actually allow to prove the following theorem.
Theorem 4.10 For any pseudo-developing map Dρ forρ we have vol(Dρ) =
Strvol(Dρ).
Before proving Theorem 4.10, we give the following deﬁnition.
Deﬁnition 4.11 Let f,g be two maps from a set X respectively to Hn and
H
n
. For t ∈ [0, ∞] the convex combination Φ t from f to g is deﬁned by:
Φ t(x) =
{ γx(t) t ≤ dist(f (x),g (x))
g(x) t ≥ dist(f (x),g (x))
where γx is the geodesic from f (x) and g(x), parametrized by arc-length.
12
Remark 4.12 In Deﬁnition 4.11, if X is a topological space and f and g
are continuous, then the convex combination from f to g is continuous on
X×[0, ∞] because the function dist(f (x),g (x)) is well-deﬁned and continuous
from X to [0, ∞].
Proof of 4.10. For the proof assume that tDρ = 0. We start by ﬁxing a
suitable homotopy h between Dρ and Str(Dρ). Deﬁne h : ~M × [0, ∞] → H3
outside the cusps to be the convex combination from Dρ to Str(Dρ) and then
for each cusp N~p extendh by coning h((x, 0),s ) to Dρ(~p) along geodesic rays
in such a way that the parameter t ∈ [0, ∞) of the cusp is the arc-length.
Let Ds(x) = h(x,s ). By Lemma 4.8 we have that
∫
M
D∗
ρω =
∫
M
D∗
sω for s ∈ (0, ∞).
So we only have to prove that
∫
MD∗
sω → Strvol(Dρ) as s → ∞ . Clearly, it
suﬃces to prove that for any tetrahedron ∆ we have
∫
∆ D∗
sω → v where v
is the volume of Str(∆). If ∆ does not collapse in the straightening, t hen
the distance from Dρ and Str(Dρ) is bounded outside the cusps and so Ds =
Str(Dρ) for s >>0; since Str( Dρ) is a homeomorphism on ∆, then
∫
∆ D∗
sω
is exactly the volume of the straight version of ∆.
If ∆ collapses in the straightening, then we have to show that
∫
∆ D∗
sω → 0.
This follows from direct calculations. We give only the lead-line of them b e-
cause they are involved but use elementary techniques. Moreover , in the next
section, we will give an alternative proof of this theorem (see Theor em 5.1
and Remark 5.9).
Given the convex combination Φ t from a map f to a map g, it is possible
to calculate the Jacobian of Φ t as a function of the derivatives of f and g,
the time t and the distance between f and g. This is not completely trivial,
for example think of a tetrahedron as a convex combination of two s egments:
the segments have zero area but in the middle we have quadrilaterals with
non-zero area. Using these calculations, we can estimate |D∗
sω| outside the
cusps, showing that its integral goes to zero as s goes to inﬁnity. Looking
inside the cusps, by Lemma 4.5 we reduce the estimate to the same es timate
as above, made with 2-dimensional objects (the bases of the cusp s).
✷
Remark 4.13 Since vol(Dρ) = Strvol( Dρ) it follows that such a volume
does not depend on the chosen cone structure of the cusps. Mor eover, by
Theorem 4.9, vol(Dρ) does not depend on the developing map, but only on
ρ. This allows us to give the following deﬁnition.
13
Deﬁnition 4.14 The volume vol(ρ) of ρ is the volume of any pseudo-devel-
oping map for ρ.
As the following corollary shows, for hyperbolic manifolds the volume o f
the holonomy is exactly the hyperbolic volume.
Corollary 4.15 Let M be a complete hyperbolic manifold of ﬁnite volume.
If ρ is the holonomy of the hyperbolic structure then vol(ρ) = vol(M).
Proof. Consider H3 as the universal cover of M and choose the arc length
as the cone parameter of the cusps. Clearly the identity of H3 is a pseudo-
developing map for ρ. Obviously we have
∫
M Id∗(ω) = vol(M).
✷
Corollary 4.16 Let zi be the modulus induced by a pseudo-developing map
Dρ on the i th tetrahedron and letvi be the volume of a hyperbolic ideal geodesic
tetrahedron of modulus zi. Then we have vol(ρ) = ∑ vi.
Remark 4.17 Even if ∑ vi depends only on ρ, the moduli zi induced by a
pseudo-developing map Dρ actually can depend on Dρ. Namely, any ideal
pointp is mapped to a ﬁxed point of ρ(Stab(p)) and, if this is not a parabolic
group, we have more than one possibility for Dρ(p). Conversely, if each
ρ(Stab(p)) is a non-trivial parabolic group, then by Remark 2.8 it follows
that the moduli zi are uniquely determined by ρ.
Proposition 4.18 Letg be a reﬂection of H3 and let
ρ be the representation
g ◦ρ ◦g−1. Then vol(ρ) = −vol(ρ).
Proof. If Dρ is a pseudo-developing map for ρ, then g ◦Dρ is a pseudo-
developing map for ρ and it is easily checked that vol( g ◦Dρ) = −vol(Dρ).
✷
We recall here two facts proved in [D].
Proposition 4.19 Suppose that ρt : π1(M) → Isom+(H3), t ∈ [0, 1] is a
smooth one parameter family of representations. Then vol(ρ0) = vol(ρ1).
This can be proved by using the one-parameter family ρt to construct a
one-parameter family of pseudo-developing maps. Some estimates on the
derivative along the t-direction of the volume of such maps are needed.
14
Proposition 4.20 Suppose that ρ factors through the fundamental group of
a Dehn ﬁlling N of M. Then the volume of ρ w.r.t. N coincides with the
volume of ρ w.r.t. M.
Theorem 4.10 extends from ideal to “classical” triangulations, name ly to
genuine triangulations T of M . Consider such a T as a triangulation of M
with some simplices at inﬁnity (those in ∂M ). Given a pseudo-developing
map Dρ for ρ, deﬁne a straightening of Dρ relative to T , exactly as in Sec-
tion 3, by considering the convex hulls of the images of the vertices o f T .
Then, one can give the deﬁnition of the straight volume relative to T of a
developing map Dρ exactly as in Deﬁnition 4.3, with the unique diﬀerence
that one has to use the tetrahedra of T instead of the ideal tetrahedra of an
ideal triangulation of M. Call such a volume Strvol T (Dρ).
Finally, exactly as in Theorem 4.10, one can prove the following fact:
Proposition 4.21 Let T be a triangulation of M and Dρ be a pseudo-
developing map for ρ. Then vol(ρ) = Strvol T (Dρ).
