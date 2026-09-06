---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements FRANC¸ OIS GUÉRITAUD APPENDIX BY DA VIDFUTER"
section_id: sec-014-10-a-numerical-example
section_title: "A numerical example"
section_number: 10
pages: 25-28
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
---
In this section we ﬁx two large enough integers N and M and investigate the behavior
of the angles for Ω = RNLM : the angles made positive by the previous computations
will turn out to be very small. We will directly construct a Euclidean realization of
Figure 4, automatically unique up to isometry. Since N and M are large, there exist
small complex numbers a, a′, b, b′ such that
(6)
{ sin a = i tan b cos b′
sin a′ = −i tan b′ cos b where
{ b = (π− 2a)/N
b′ = (π− 2a′)/M.
Geometry &Topology 10 (2006)
1264 Franc ¸ois Gu´eritaud and David Futer
A way to compute a, a′ is to set a0 = a′
0 = 0 and to deﬁne inductively
as+1 = arcsin
(
i tanπ− 2as
N cosπ− 2a′
s
M
)
and a similar expression for a′
s+1, with a change of sign. The sequences as, a′
s converge
exponentially fast to a, a′. The constants a, a′ become arbitrarily small for large
enough N, M, hence b∼π/N and b′∼π/M. So plugging into (6), a∼ iπ/N and
a′∼− iπ/M. Using the Landau symbol O(A, B) in the sense of O(max{A, B}), this in
turn yields
(7)
b = π
N− 2iπ
N2 +O( 1
N3, 1
M3 )
b′ = π
M + 2iπ
M2 +O( 1
N3, 1
M3 )
a = iπ
N + 2π
N2 +O( 1
N3, 1
M3 )
a′ = −iπ
M + 2π
M2 +O( 1
N3, 1
M3 ).
(In fact a, a′, b, b′ are analytic functions of 1
N, 1
M , by the Implicit Function Theorem.)
Proposition 10.1 The fan which corresponds to RN can be embedded into C with
nodes at complex coordinates ± cot b and intermediary vertices cot(a + sb) where
−1≤ s≤ N + 1; similarly, the fan corresponding to LM can be embedded into C
(possibly with a different scaling factor) with nodes± cot b′ and intermediary vertices
cot(a′ + sb′) where−1≤ s≤ M + 1 (see Figure 11).
/NUL cot b0
cot AN
cot b
cot A0
1
/NUL cot b
cot A/NUL 1
As WD a C sb
cot A0
M /NUL 1
cot A0
2
cot A0
M C1
cot AN /NUL 1
A0
s WD a0 C sb 0
cot A0
0
cot A1
cot A2
cot AN C1
cot b0
cot A0
/NUL 1
cot A0
M
cot A0
Figure 11
Proof There are several things to check. First, the congruence of pairs of triangles
inside each fan follows from the identity of complex ratios
(8) cot(As + b)− cot b
cot(As + b)− cot As
= cot(As− b) + cot b
cot(As− b)− cot As
= sin2 As
sin2 b
Geometry &Topology 10 (2006)
Canonical triangulations 1265
where As = a + sb for 0≤ s≤ N , and an identical relation for a′, b′.
Next, each fan, when stripped of two of its four limiting (grey) triangles, is a parallelo-
gram. This follows from cot(a + Nb) = cot(π− a) =− cot a, and the same for a′. In
particular, each fan admits a center of symmetry.
Furthermore, these two parallelograms are congruent. To see this, letα,α′,β,β ′ denote
the squared cotangents of a, a′, b, b′. Raising (6) to the power−2, we get
{ 1 +α = −β(1 +β′−1)
1 +α′ = −β′(1 +β−1) hence α
α′ = β +β/β′ + 1
β′ +β′/β + 1 = β
β′,
so cot a/ cot b =± cot a′/ cot b′, the correct sign being minus by the estimates (7).
Further yet, the limiting (grey) triangles of the two fans have the same shape: by
(8) their complex ratios are sin2 a/ sin2 b and sin2 b′/ sin2 a′, both equal by (6) to
− cos2 b′/ cos2 b.
Finally, all triangles are positively oriented, that is, Im(sin2 As/ sin2 b) > 0 for all
0≤ s≤ N . We ﬁrst check this for s = 0 (the case s = N will follow by symmetry): we
have sin2 a/ sin2 b =−(cos2 b′/ cos2 b) =−((1− sin2 b′)/(1− sin2 b)). In the latter
expression, both the numerator and denominator are∼ 1, but their imaginary parts are
equivalent to−4π2/M3 and 4π2/N3 respectively (with an O(N−4, M−4) error), by (7).
Therefore, the ratio does lie above the real line, and the “pinched” angles of the limiting
(grey) triangles in Figure 11 are both roughly
2π2(N−3 + M−3) radians.
Very pinched, but not ﬂat!
To check that arg(sin As/ sin b) lies in (0,π/ 2) for all other 0 ≤ s≤ N , we need to
draw the level curves of z↦→ arg(sin z) in C. This is done in Figure 12, in the case
0≤ Re (z)≤ π: the curves fall into 4 symmetric families (“quadrants” meeting at
π/2∈ C), and it is an easy exercise to check that the families above (resp. below) the
real axis are made of convex (resp. concave) curves. The authorized region for the
As = a + sb is in grey (with a narrow collar nearπ/2); the forbidden regions are left in
white. The segment [ A0AN] clearly stays in the grey region, which implies the result.
By the same argument, the triangles in the fan of LM are well-oriented, too. Therefore
we may tile the plane with parallelograms (or fans) congruent to those in Figure 11 to
get a Euclidean realization of Figure 4.
Finally, notice that the Kleinian group associated to the embedding of the left fan in
Figure 11 contains the M¨obius transformation z↦→ (z cos b− sin b/(z sin b + cos b)) (it
Geometry &Topology 10 (2006)
1266 Franc ¸ois Gu´eritaud and David Futer
AN
a C sb
0
a

Figure 12: Level curves of z↦→ arg(sin z)
sends each tetrahedron sitting above a triangle in the left half of the fan to the tetrahedron
sitting above the similar triangle in the right half). Therefore, 2 ib (and similarly−2ib′)
are the complex lengths of very short closed geodesics in the hyperbolic manifold Vϕ.
A consequence of Theorem 1.1 is that the volume of any angle structure (deﬁned by
Figure 5, where (3) holds) is a lower bound for the volume of the manifold Vϕ. One
gets bounds which are sharp in terms of distances in the Farey graph; see Section B.1.
