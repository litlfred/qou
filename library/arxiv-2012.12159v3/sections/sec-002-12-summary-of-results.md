---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-002-12-summary-of-results
section_title: "Summary of results"
section_number: 1.2
pages: 1-6
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
1.3. Plan of the paper 6
1.4. Acknowledgements 6
2. Preliminaries 7
2.1. Convexity 7
2.2. Projective geometry 7
2.3. Finsler geometry 8
3. A projective outlook on the Funk metric 8
3.1. The projective co-nomadic Finsler structure 8
3.2. The volume in Funk geometry 11
4. Funk billiards and duality 13
5. Integrability of Funk billiard in conics 18
Date: April 23, 2021.
MSC classiﬁcation: 52A40, 37C83, 52A20, 53D25, 51N15, 52A38, 52A10, 52A55.
The research was partially supported by ISF Grant 1750/20.
1
arXiv:2012.12159v3  [math.DG]  22 Apr 2021
2 A Funk perspective on billiards, projective geometry and Mahler volume
6. Sch¨ aﬀer’s dual girth conjecture 21
7. Mahler volumes of every Funk scale 22
8. Maximizing the Funk-Mahler volume 26
9. Regularizing the total Funk volume 34
References 41
1. Introduction
1.1. Funk and Hilbert metrics. The Hilbert metric in the interior of a convex
set K⊂ Rn is given by
dH
K(x,y ) = 1
2 log|ay||xb|
|ax||yb|,
where a,x,y,b appear in that order on the line through x,y with a,b∈ ∂K. It is
evidently invariant under invertible projective maps. Hilbert discovered this metric
while attempting to generalize the Beltrami-Klein model of hyperbolic geometry.
It is moreover a projective metric, meaning that straight segments are geodesic.
Hilbert’s fourth problem [15] asks for a construction of all projective metrics.
A diﬀerent example of a projective metric, which we now recall, was discovered
by Funk [13]. It is given by the non-symmetric distance function
dF
K(x,y ) = log|xb|
|yb|,
where b is the intersection of the ray # »xy with ∂K.
Various problems in Hilbert geometry have been raised and studied, notably
those of volume growth [11, 30, 9, 29] and Gromov hyperbolicity [8]. The Funk
metric, on the other hand, has been for the most part denied the spotlight. In this
paper we attempt to argue that at least from the perspectives of convex geometry
and billiard dynamics, it is the Funk metric that is most natural to study.
Let K⊂ Rn be a convex compact set with non-empty interior, placed in the
aﬃne space Rn. The Funk metric on K is arguably the simplest (non-symmetric)
metric one can deﬁne naturally in its interior. Indeed, it is the non-reversible Finsler
metric whose tangent unit ball at x∈ int(K) is BxK =K⊂TxRn = Rn, namely
K itself with the origin ﬁxed at x.
The Funk and Hilbert metrics are closely related:
dH
K(x,y ) = 1
2(dF
K(x,y ) +dF
K(y,x )).
It is a remarkable fact that the symmetrization of the Funk metric is already projec-
tively invariant. This hints that the Funk metric comes close to being projectively
invariant itself. We shall pursue this idea along several paths.
1.2. Summary of results. IfK⊂ RPn is a convex body with interior, we may ﬁx
a hyperplane at inﬁnity η that is disjoint from K, and consider the corresponding
η-Funk metric on K, denoted Funkη
K. Changing η results in a change to the Funk
metric, but of a very particular type: the Finsler norm is changed by an exact
1-form. This is the core reason behind the projective invariance of many metric
invariants associated to the Funk metric, as follows.
For a submanifold X⊂ int(K), let Funkη
K(X) stand for the Finsler metric that
is induced on X from Funkη
K, that is it is the intrinsic metric induced on X from
3 A Funk perspective on billiards, projective geometry and Mahler volume
the Funk metric. When η is clear from context, e.g. when K belongs to an aﬃne
space, we simply write FunkK(X).
Theorem A. Assume K⊂ Rn is C2-smooth and strictly convex. Let Ω⊂ int(K)
be a smooth k-dimensional submanifold with boundary. The following are invariant
under the action of any invertible projective map g keepingK compact.
i) Thek-dimensional Holmes-Thompson volume of FunkK(Ω), denoted volF
K(Ω).
ii) The geodesics of FunkK(Ω), as well as the length of closed geodesics.
iii) Assume k =n, that is Ω is a smooth domain. Then the Finsler billiard or-
bits in FunkK(Ω), as well as the length of the periodic orbits, are invariant.
Therefore, whenever we discuss any of those invariants, we may assumeK⊂ RPn
is a convex set, without specifying an aﬃne chart. Here and in the following,
smoothness and strict convexity assumptions in statements concerning volumes
can be relaxed through a continuity argument.
The reverse Funk metric is deﬁned similarly to the Funk metric by settingBxK =
ax(K), whereax is the antipodal map with respect tox, or equivalentlydRF
K (x,y ) =
dF
K(y,x ). For K,η as before we denote the corresponding reverse Funk metric on
int(K) by RFunkη
K. Theorem A applies equally to RFunk.
In a sense, those invariants are more natural than the corresponding ones for the
Hilbert metric, which is most clearly manifested by their invariance under projective
duality. Recall that the polar convex body K∨⊂ P∨ = ( RPn)∨ is the closure of
the set of all hyperplanes disjoint from K.
Theorem B. Assume K⊂ int(L) are C2-smooth, strictly convex bodies in RPn.
Then
i) volF
L(K) = volF
K∨(L∨).
ii) The billiard orbits in FunkL(K) and RFunkK∨(L∨) are in a natural bijective
correspondence. Moreover, a periodic orbit corresponds to a periodic orbit,
and they have equal length.
iii) The Holmes-Thompson volumes of FunkL(∂K) and FunkK∨(∂L∨) coincide.
iv) The geodesics of FunkL(∂K) and RFunkK∨(∂L∨) are in a natural bijective
correspondence, and the respective closed geodesics have equal length.
In the limit where K is shrinking to a ﬁxed point inside L through homotheties,
we get corresponding statements for linear spaces with Minkowski norms, as follows.
Let K,L ⊂ V = Rn be ﬁxed convex sets with 0 in their interior, and consider
K⊂ (V,‖•‖L) andLo⊂ (V∗,‖•‖Ko). The ﬁrst statement becomes a tautology, as
both volumes, when properly rescaled, approach the symplectic volume ofK×Lo⊂
V⊕V∗. The second statement is the duality of the Minkowski billiards ( K,L ) and
(Lo,−Ko), ﬁrst established in [14], and which permeates the work of Artstein-
Avidan and Ostrover on the relationship between Minkowski billiards, symplectic
geometry and the Mahler conjecture [6, 5], see also [23] for a survey. It is the
approach of [6] that we take to establish the duality. The third statement was
established in [16] in the particular case of K = L. The fourth statement is the
(non-symmetric) Sch¨ aﬀer dual girth conjecture [26], which can also be understood
as a duality of gliding billiard orbits. It was established in [1] together with the
general case of the third statement.
The ﬁrst statement implies an isomorphic form of duality in Hilbert geometry.
Let volH
K be the Holmes-Thompson volume of the Hilbert metric in K.
4 A Funk perspective on billiards, projective geometry and Mahler volume
Corollary 1. Given K⊂ int(L) in RPn, volH
L (K)≤ 1
2n
(2n
n
)
volH
K∨(L∨). Equality
is attained if and only if K is an ellipsoid, and L is a simplex.
The third statement implies a duality in Hilbert geometry in the projective plane.
Corollary 2. LetK⊂ int(L) be two convex sets in RP2. Then the Hilbert lengths
volH
L (∂K) and volH
K∨(∂L∨) coincide.
It is not hard to verify that for an ellipsoid B⊂ RPn, the Funk billiard (though
not the metric itself) in a domain Ω ⊂ int(B) coincides with that of the Beltrami-
Klein hyperbolic metric. It follows in particular that for an ellipsoid K ⊂ B⊂
RPn, the Funk billiard in K is completely integrable, see [34]. We provide a Funk
perspective and an alternative proof of this result in the projective plane, as follows.
Theorem C. Let K⊂ int(B) be nested ellipses in RP2. Then every orbit of the
B-Funk billiard in K has a caustic, which is a conic in the dual pencil deﬁned by
∂K,∂B . Furthermore, if Q is a caustic for FunkB(K), and ˆQ⊂ P∨ is the caustic of
the dual orbit in RFunkK∨(B∨), then ˆQ∗,∂B,∂K,Q form a harmonic quadruplet
of conics.
HereQ∗⊂ P∨ denotes the dual quadric, consisting of all tangent hyperplanes to
Q⊂ P. For a harmonic quadruplet of quadrics, see Deﬁnition 2.1. In particular,
we can interpret the Poncelet porism of any pair of nested conics in terms of closed
Funk (equivalently, hyperbolic) billiard orbits.
In the second part of this note, we consider the Holmes-Thompson volume of
balls in the Funk metric. Assume K⊂ Rn, and let BF
r (q,K ) denote the outward
r-ball in the Funk metric on K centered at q. Denoting by Kz⊂ (Rn)∗ the dual
body with respect to z, and byωn the volume of the Euclidean unit ball in Rn, one
has volF
K(BF
r (0,K )) = 1
ωn
∫
(1−e−r)K|Kz|dz. We show that for K unconditional
and any r, the volume of BF
r (0,K ) is maximized when K is an ellipsoid, which
translates into the following equivalent systems of aﬃne inequalities.
Theorem D. For an unconditional convex body K⊂ Rn, one has
• For all 0<ρ< 1
∫
ρK
|Kz|dz≤nω2
n
∫ ρ
0
tn−1dt
(1−t2)
n+1
2
.
• For all j≥ 0,
∫
K×Ko
⟨x,ξ⟩2jdxdξ≤ (2π)n
n + 2j
1
(n + 2j)!!(n− 2)!!(2j− 1)!!
( 2
π
) 1−(−1)n
2
.
Equality in each case is attained uniquely by ellipsoids.
Forj = 1, this is a theorem of Ball [7].
In the limit ρ→ 0, which corresponds to Funk balls of inﬁnitesimal radius, the
Blaschke-Santal´ o inequality is recovered:
|K×Ko|≤| Bn× (Bn)o| =ω2
n.
On the other end of the scale, one has the following result of [9].
5 A Funk perspective on billiards, projective geometry and Mahler volume
Proposition 1. AssumeK⊂ Rn isC2-smooth and strictly convex, and 0∈ int(K).
Then as ρ→ 1−, ∫
ρK
|Kz|dz∼ 2−n−1
2
ωn
n− 1
1
(1−ρ)
n−1
2
Ωn(K),
where Ωn(K) is the centro-aﬃne surface area of K.
For the deﬁnition of centro-aﬃne surface area, see eq. (5). Therefore in the limit
of large Funk balls, Theorem D yields the centro-aﬃne isoperimetric inequality:
Ωn(K)≤ Ωn(Bn) =nωn.
Thus Funk geometry interpolates between those two extremes through a continuum
of aﬃne inequalities. As both the Blaschke-Santal´ o and the centro-aﬃne inequali-
ties are valid for arbitrary convex bodies with centroid at the origin, we naturally
conjecture that Theorem D remains true in this generality.
The Colbois-Verovic volume entropy conjecture [11] asserts that the volume
growth entropy of metric balls in Hilbert geometry is maximized by ellipsoids,
or equivalently by smooth strictly convex bodies. This was recently proved by
Tholozan [29] and Vernicos-Walsh [32] using very diﬀerent methods, and previ-
ously established up to dimension 3 in [31]. Theorem D yields yet another proof
of the volume entropy conjecture, albeit only for unconditional bodies. We write
BH
r (q,K ) for the metric ball in the Hilbert metric.
Corollary 3. ForK⊂ Rn a convex unconditional body,
lim sup
R→∞
1
R log volH
K(BH
R (q,K ))≤n− 1.
Theorem D follows from a more general functional form of the same inequalities.
BelowL is the Legendre transform, deﬁned in eq. (1).
Theorem E. For an unconditional Borel function f =e−φ : Rn→ [0,∞), one has
the equivalent systems of inequalities
• For all j≥ 0,
∫
Rn×Rn
⟨x,ξ⟩2je−φ(x)−Lφ(ξ)dxdξ≤ (2π)n (n− 2 + 2j)!!
(n− 2)!!(2j− 1)!!.
• For all 0≤ρ< 1,
∫
Rn×Rn
e−φ(x)−Lφ(ξ)+ρ⟨x,ξ⟩dxdξ≤ (2π)n
(1−ρ2)
n
2
.
Equality in each case is attained uniquely, up to equality a.e., by f that is a multiple
of a gaussian.
In the limit ρ→ 0 we recover the functional Blaschke-Santal´ o inequality for
unconditional functions. For j = 1, this is a theorem of Huang and Li [17]. The
proof we give is inspired by, and largely the same as the proof of the functional
Blaschke-Santal´ o inequality of Lehec [19].
By Proposition 1, the centro-aﬃne surface area of K can be viewed as a regular-
ization of the total Holmes-Thompson volume of K equipped with its Funk metric.
It excels at capturing the volume growth of the metric, but has the drawback of be-
ing dependent on the precise way in which the volume is exhausted, namely through
metric balls centered at a point. As a consequence, it depends on the choice of a
