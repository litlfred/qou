---
doc_id: funaba-2014-j-phys-conf-ser-544-012019
doc_title: "Conference Series"
section_id: sec-000-1-introduction-and-main-result
section_title: "Introduction and main result"
section_number: 1
pages: 2-4
source_pdf: Funaba_2014_J._Phys.__Conf._Ser._544_012019.pdf
source_sha256: c95b283a122d67e4
---
Recently Fernando C. Marques and Andr´ e Neves (Marques & Neves) proved the Willmore
conjecture, namely, they showed the following. Let Σ be an immersed torus in R3. Let κ1
and κ2 be principal curvatures. The Willmore functional is given by
W(Σ) =
∫
Σ
(κ1 +κ2
2
)2
dΣ =
∫
Σ
(κ1−κ2
2
)2
dΣ,
where the second equation is the consequence of the Gauss-Bonnet theorem. It is known to be
invariant under M¨ obius transformations ofR3. Then the Willmore conjecture, now the theorem
of Marques and Neves, asserts that W(Σ)≥ 2π2 and that the equality holds if and only if Σ is
a torus of revolution whose generating circle has radius 1 and center at distance
√
2 from the
axis of revolution up to a M¨ obius transformation, in other words, if and only if Σ is the image
of a stereographic projection of the Cliﬀord torus
{
(z1,z 2)∈ C× C
⏐⏐⏐|z1| =|z2| = 1/
√
2
}
⊂S3 =
{
(z1,z 2)∈ C× C
⏐⏐⏐|z1|2 +|z2|2 = 1
}
.
In this paper, we give another characterization of the Cliﬀord torus using the surface energy
introduced by David Auckly and Lorenzo Sadun ((1)), which is also invariant under M¨ obius
transformations. To be precise, we have not yet succeeded in proving that the Cliﬀord torus
gives the minimum energy among all the immersed tori 1. We only show that it gives the
minimum energy among one-parameter family of tori of revolution. Since the energy we use is
conformally invariant, it follows that the Cliﬀord torus gives the minimum energy among Dupin
cyclides. As the surface energy that we use in this paper is generelization of knot energy, we
start with the review of it.
Energy of knots was introduced in (5) motivated to give a functional on the space of knots
that can produce a representative conﬁguration of a knot for each knot type as an embedding
1 To show it, it suﬃce to show that the Cliﬀord torus gives the minimum energy among all the embedded tori,
since the energy blows up if a torus has a double point
Flux in QCS IOP Publishing
Journal of Physics: Conference Series 544 (2014) 012019 doi:10.1088/1742-6596/544/1/012019
Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence. Any further distribution
of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.
Published under licence by IOP Publishing Ltd 1
that minimizes the energy in the knot type. Let K be a knot and x be a point on it. Deﬁne
V (x;K) = lim
ε→0
(∫
K\Bε(x)
dy
|x−y|2− 2
ε
)
, and E(K) =
∫
K
V (x;K)dx, (1)
where Bε(x) is a ball with center x and radius ε. Let us call a process as in the deﬁnition
of V (x;K) in (1) the renormalization in this paper. In general, when we are interested in a
diverging integral, we ﬁrst restrict the integration to the complement of an ε-neighbourhood of
the set where the integrand blows up, then expand the result in a Laurent series in ε, and ﬁnally
take the constant term. In the case of a knot, the integrand ofV in (1) blows up at the one-point
set{x}. There are two ways to deﬁne an ε-neighbourhood of it, according to the choice of the
distance between a pair of points on the knot; either the chord length as in (1) or the arc-length
along the knot as in (5). Both types of the renormalization give the same result ((6)).
The energy E(K) in (1) was proved to be invariant under M¨ obius transformations by
Freedman, He, and Wang ((2)), which is the reason why it is sometimes called the M¨ obius
energy of knots.
After this energy was found, it has been generalized to functionals that can measure geometric
complexity of knots, surfaces, and in general, submanifolds ((1), (3), et al.). Among several ways
of generalization to surface energy, in this paper we study the one by Auckly and Sadun that
uses a similar renormalization process as in (1).
Let S be an embedded surface in R3 without boundary and x be a point in S. Deﬁne the
renormalizedr−4-potentialV and the renormalizedr−4-potential energy E by
V (x;S) = lim
ε→0
(∫
S\Bε(x)
d2y
|x−y|4− π
ε2 + π∆(x)
16 log
(
∆(x)ε2)
+ πK(x)
4
)
,
E(S) =
∫
S
V (x;S)d2x,
(2)
where d2y and d2x mean the volume element of S, ∆(x) is given by ∆( x) = (κ 1(x)−κ2(x))2,
and K(x) is the Gauss curvature; K = κ1κ2. This energy E(S) was proved to be invariant
under M¨ obius transformations in (1). It blows up asS degenerates to an immersed surface with
double points.
As was pointed out in (1), the choice of the log-term in (2) is not the unique reasonable one.
The reason why there is a factor ∆(x) in the log-term is to make the resulting energy scale
invariant, butc∆(x) (c⁄= 0) also has the same eﬀect. Thus there is ambiguity in the deﬁnition
of the renormalized potential.
In (1), Auckly and Sadun has computed the energy of spheres and planes and the potentials
V of an inﬁnitely long straight cylinder and a surface called dimple. In this article we compute
the energies of one-parameter family of tori of revolution.
Theorem: Let TR be a torus of revolution whose generating circle has radius 1 and center at
distanceR (R> 1) from the axis of revolution. Then the renormalized potential energy is given
by
E(TR) = π3
2
√
R2− 1
(
R2 (3 log 2− 1) + 2− 2
R2
)
.
Corollary: Among tori of revolution, a stereographic projection of the Cliﬀord torus gives the
minimum energy.
Flux in QCS IOP Publishing
Journal of Physics: Conference Series 544 (2014) 012019 doi:10.1088/1742-6596/544/1/012019
2
Proof of Corollary : Since
d
dRE(TR) = π3(R2− 2)
(
(R2− 2)2 + 3R4 log (4/e)
)
4R3 (R2− 1)3/2 ,
the energy takes the minimum value π3(6 log 2− 1)/2 when R =
√
2. □
Problem: (1) Does T√
2 give the minimum energy among all the embedded tori in R3, hence
among all the immersed tori in R3?
(2) When we change the power of |x−y| in the denominator in (2) from 4 to any number
λ, we obtain a new potential energy Er−λ after suitable renormalization. It is no longer scale
invariant when λ⁄= 4. What is R =R(λ) that makes TR give the minimum energy Er−λ after
rescaling to have area 1?
