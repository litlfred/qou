---
doc_id: arxiv-2304.12545v1
doc_title: "HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF WALTER NEUMANN"
section_id: sec-001-2-volumes-and-dehn-surgeries
section_title: "Volumes and Dehn surgeries"
section_number: 2
pages: 3-7
source_pdf: 2304.12545v1.pdf
source_sha256: bfc3c2be395b1b2d
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
---
As already stated, the original main purpose of [31] was to study the arithmetic of the set
of volumes of all hyperbolic 3-manifolds. It had been observed by Thurston, using earlier
work of Jørgensen, that this volume spectrum is a well-ordered subset of the positive reals. In
other words, there is a smallest volume (which is known), a second smallest, a third smallest,
. . . , then a smallest limit point, a second smallest limit point, . . . , then limits of these, and
so on. The proof of well-orderedness shows that these simple and higher-order limit points
4 STA VROS GAROUF ALIDIS AND DON ZAGIER
arise by “closing up” one or more of the cusps of a non-compact hyperbolic 3-manifold M by
Dehn surgeries to obtain a countable collection of manifolds with fewer cusps whose volumes
tend from below to that of M. The object of [31] was to study the speed with which these
volumes converge.
Before studying the eﬀect of surgeries, we must understand the volume of a single hyper-
bolic 3-manifold M. Clearly it can be given as the sum of the volumes of the tetrahedra
of any ideal triangulation, so the ﬁrst step is to understand these. An (oriented and non-
degenerate) ideal tetrahedron can be parametrized either by a shape parameter z in the
complex upper half-plane, as explained in the preceding section, or, in case z is in the upper
half plane, by the three angles α, β, γ(positive and with α +β +γ = π) of the Euclidean
triangle that one “sees” by looking at the tetrahedron from any of its four cusps. When
Im(z)> 0, the angles and the shapes are related by (α,β,γ ) = (arg(z), arg(z′), arg(z′′)) with
z′ and z′′ as above.
According to Chapter 7 of Thurston’s notes, written by Milnor, the volume of this tetra-
hedron when Im(z)> 0 is given in terms of these two parametrizations by the two formulas
Vol(∆(z)) = D(z) = Л(α) + Л(β) + Л(γ), (4)
the equality of the two being an identity due to Kummer. (Both formulas are actually true
for all z⁄= 0, 1, but the sum of α, β and γ is−π if z is in the lower half-plane.) Here D(z)
and Л(θ) are the Bloch-Wigner dilogarithm (cf. Section 3) and the Lobachevsky function,
deﬁned respectively by
D(z) = Im
(
Li2(z) + log|z| log(1−z)
)
,
Л(θ) = −
∫ θ
0
log|2 sint|dt = 1
2
∞∑
n=1
sin(2nθ)
n2 = 1
2D
(
e2iθ)
. (5)
Thus the volume of a hyperbolic manifold M triangulated byN ideal tetrahedra with shape
parameters zi is given in terms of the dilogarithm function by
Vol(M) =
N∑
j=1
D(zj). (6)
Now let M be a 3-manifold with h cusps. It has a unique complete hyperbolic structure
as a quotient H 3/Γ for some lattice Γ ⊂ PSL2(C) isomorphic to π1(M), the corresponding
shape parameters z0 = (z0
1,...,z 0
N) being a solution of all N + 2h equations (1) and (2). A
small deformation of this hyperbolic structure will have a nearby shape parameter vector
z = (z1,...,z N) satisfying only (1). By the result of Thurston mentioned earlier, the space
of all such deformations has the structure of a smooth complex manifold of dimension h, so
is isomorphic to a small neighborhood U of 0 in Ch. Thus each zi depends holomorphically
on u∈ U andzi(0) =z0
i . To make this more visible, and to choose nice coordinates ui on U,
we have to look more closely at the structure of the cusps on M and at Dehn surgeries.
Each cusp has the structure [0,∞)×T 2, whereT 2 is a totally geodesically embedded torus
in M and has a ﬂat Euclidean metric, unique up to homothety, induced by the hyperbolic
metric on M. More concretely, the cusps of M = H 3/Γ are indexed by P∈ P 1(C) whose
stabilizer ΓP is free abelian of rank 2. After conjugation we can place P at∞, in which
HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF W ALTER NEUMANN 5
case Γ∞ has the form±
(1 Λ
0 1
)
for some lattice Λ ⊂ C, unique up to homothety, and then
we can identify Λ with H1(T 2) and T 2 with C/Λ. There is a canonical quadratic form on Λ
deﬁned as the square of the length of a vector divided by the volume of T 2. If we choose
an oriented basis (µ,λ ) of H1(T 2) (“meridian” and “longitude”) to identify Λ with Z2, then
this quadratic form is given by Q(p,q ) =|pτ +q|2/Im(τ) if we rescale Λ after homothety to
be Zτ + Z for some τ in the complex upper half-plane.
On the other hand, each element of Λ = H1(T 2) can be identiﬁed with an isotopy class
of closed curves on T 2. Doing a ( p,q ) Dehn surgery at a cusp, once the basis of H1(T 2)
has been chosen, means removing T 2× [0,∞) from M and replacing it by a solid torus in
such way that the curve on T 2 corresponding to the class pµ +qλ bounds in the solid torus.
Here we assume that the integers p and q are coprime, but we also allow “ ∞” as a value
for (p,q ), meaning that we leave this cusp untouched. The Dehn surgeries on M are then
described by tuples κ = ((p1,q 1),..., (ph,qh))∈ (Z2∪{∞} )h. Thurston’s theorem [32] tells
us that if all ( pi,qi) are near enough to ∞ (meaning that (pi,qi) =∞ or p2
i +q2
i is large),
the surgered manifold Mκ is hyperbolic, in which case both the shape parameters z1,...,z N
and the volume Vol(Mκ) become functions of κ. Explicitly, the deformed shape parameters
z(κ) = z(p, q) that tend to z0 as all the pairs ( pi,qi) tend to inﬁnity are given by adding
to the original gluing equations (1) the h new equations given by the product of the pi-th
power of the ﬁrst expression by the qi-th power of the second one in (2), and then Vol( Mκ)
is given by (6) with zj replaced by zj(κ).
We now get two real numbers at each cusp: the value Qi(pi,qi) of the quadratic form
corresponding to that cusp at the pair ( pi,qi) (with the convention Qi(∞) = ∞) and the
length Li =Li(κ) of the short geodesic on Mκ which is the core of the solid torus added by
the Dehn surgery (or 0 if the ith cusp has not been surgered). They are related by
Li = 2π
Qi(pi,qi) + O
( h∑
i=1
1
p4
i +q4
i
)
(7)
([31], Prop. 4.3) as all κi = (pi,qi) tend to inﬁnity. The main volume result of [31], proved
by using (6) and analyzing the changes of the dilogarithms under small changes of the z’s,
is then given by the pair of asymptotic formulas
Vol(Mκ) = Vol( M) −
h∑
i=1
( π2
Qi(pi,qi) + O
( 1
p4
i +q4
i
))
(8a)
= Vol(M) −
h∑
i=1
(πLi
2 + O
(
L2
i
))
(8b)
(Theorems 1A and 1B in [31]), which are equivalent to one another by virtue of (7). These
volumes, as κ = (p, q) ranges over all h-tuples of suﬃciently large pairs of coprime integers
or the symbol ∞ meaning unsurgered, all belong to the hyperbolic volume spectrum, and
equation (8a) has as an immediate corollary a description of the local structure of this volume
spectrum near its limit point, because the asymptotics of the number of lattice points, or of
6 STA VROS GAROUF ALIDIS AND DON ZAGIER
primitive lattice points, in a large ellipse, is well-known. The precise asymptotic statement,
which we will not repeat here, is formulated explicitly as a Corollary to Theorem 1A in [31].
All of this is only for integral (and coprime) values of pi and qi. However, as is explained
in [31] in detail, the shape parameterszj(κ) and the lengthsLi(κ) are deﬁned forp andq real
rather than just integral and coprime in pairs, and equations (7) and (8) still remains true.
The only point is that in the deﬁnition of the zj’s we had to take the pith and qith powers
of the equations in (2), and one cannot in general take real powers of complex numbers in a
well-deﬁned way, but since the left-hand sides of the expressions in (2) are near to 1 for small
deformations of the original value z = z0 and since a complex number near 1 has a well-
deﬁned logarithm near 0, there is no problem. When the pi andqi are not integral, we are no
longer “ﬁlling in” the cusp by gluing on a solid torus, but are simply changing the hyperbolic
structure on the original open topological manifold M, with the new hyperbolic structures
in general being incomplete. If we now deﬁne 2 h complex numbers u = ( u1,..., uh) and
v = (v1,..., vh) by
ui =
N∑
j=1
(
M′
ij log zj
z0
j
+ M′′
ij log 1−zj
1−z0
j
)
, vi =
N∑
j=1
(
L′
ij log zj
z0
j
+ L′′
ij log 1−zj
1−z0
j
)
,
then from the symplectic properties of the gluing equations it follows that [28, Lem.4.1]
piui + qivi = 2πi (i = 1,...,h ),
and we can take u as canonical coordinates for the above-mentioned neighborhood U of
0∈ Ch, in which case each vi becomes an odd power series in the u’s with linear term τiui
and we can write Li(u) and Vol(u) instead of Li(κ) and Vol(Mκ). We should mention that u
and v can be deﬁned invariantly, without using any triangulation, as follows: the deformed
hyperbolic structure on M corresponds to a homomorphism ρ : Γ→ PSL2(C) near to the
inclusion map, and then u and v are simply the logarithms of the ratios of the eigenvalues
of the images under ρ of the meridians and longitudes, respectively.
In terms of the new coordinates, equation (8b) becomes
Vol(u) = Vol( M) − π
2
h∑
i=1
Li(u) + ε(u), (9)
with ε(u) = O(||u||4) as u tends to 0 in Ch. Theorem 2 of [31] was the statement that
the function ε(u) deﬁned by (9) is harmonic, and hence is the real part of a holomorphic
function f(u) near 0 (uniquely determined if we ﬁx f(0) = 0). Theeorem 3, proved using
equation (3), said that ∂vi/∂uj is symmetric in i and j, which implies that there is a single
function Φ(u) with∂Φ/∂ui = 2vi for alli, and that f is given in terms of Φ by 4f = Φ− u· v
(or equivalently by−8f = (E− 2)Φ, where E =∑ ui∂/∂ ui is the Euler operator), so that
the volume correction ε(u) in (9) is given by
ε(u) = Im
(
f(u)
)
, f (u) := 1
4
∫ u
0
( h∑
i=1
(vidui− uidvi)
)
. (10)
The function f is now often called the Neumann-Zagier potential function, although this
name was used in the original paper for Φ instead. It should perhaps also be mentioned that
HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF W ALTER NEUMANN 7
simpler proofs of the last results described could probably have been obtained by using the
second rather than the ﬁrst volume formula in (4).
There is one more important point about volumes. Another insight by Thurston was
that the volume of a hyperbolic 3-manifold, which is a positive real number, is actually in a
natural way the imaginary part of a complexiﬁed volume whose real part is the Chern-Simons
invariant, an important topological invariant taking values in R/4π2Z whose deﬁnition we
omit here. It was conjectured in [31], and proved soon afterwards by Yoshida [34], that the
above formulas remain true with the volumes replaced by their complexiﬁed versions, the
functions Li(u) also lifted suitably from R to C, and ε(u) replaced by f(u). Later, in [28],
Walter showed how to lift (6) to an explicit and computable expression for the complexiﬁed
volume of Mp,q in terms of the complex dilogarithm.
