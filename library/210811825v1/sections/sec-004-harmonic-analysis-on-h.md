---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-004-harmonic-analysis-on-h
section_title: "Harmonic analysis on H"
section_number: null
pages: 47-52
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
Harmonic analysis on H
2.3.1
Disks
Here we take “disk” to mean a general disk in hyperbolic space rather than the Poincaré
disk model. Due to the radial symmetry of the disk, it is possible to give an explicit
formula for the eigenfunctions. From these, we can calculate the eigenvalues of the disk
and use them to bound the eigenvalues of a domain in our surface from below. First,
we introduce a more convenient polar co-ordinate system, known as the geodesic polar
co-ordinates. Recall the diﬀerent forms that a group action in Isom+(H) can take (for
example, reﬂection or rotation matrices). An element g ∈Isom+(H) can be written as
g = k(ϕ)a(e−r)k(θ), where
k(ϕ) =
 
cos(ϕ)
sin(ϕ)
−sin(ϕ)
cos(ϕ)
!
,
0 ≤ϕ < π,
a(e−r) =
 
e−r/2
0
0
er/2
!
,
r ≥0,
and k(θ) is a rotation by angle 2θ around i.
This way of expressing g is known as
Cartan’s decomposition [38]. Given a point z ∈C such that z = x + yi, in geodesic polar
co-ordinates, z = k(ϕ)e−ri and we use the following to deﬁne the change of co-ordinates:
y = (cosh(r) + sinh(r) cos(2ϕ))−1,
37
x = y sinh(r) sin(2ϕ).
The Riemannian measure and length element in terms of (r, ϕ) are now
ds2 = dr2 + (2 sinh(r))2dϕ2,
dz = (2 sinh r)dr dϕ.
These give us formulae for the area of a disk D:
Area(D) = 4π sinh2 r
2

,
and circumference of its boundary
l(∂D) = 2π sinh(r),
where we normalize the disk to be centred at i and take r as above to be its radius. The
Laplacian takes the form
∆= −
 ∂2
∂r2 +
1
tanh r
∂
∂r +
1
(2 sinh r)2
∂2
∂ϕ2

,
and eigenfunctions are Legendre p functions
P−s(cosh(r)) = 2F1

s, 1 −s; 1; 1 −cosh(r)
2

,
where
2F1(a, b; c; z) =
∞
X
k=0
(a)k(b)k
(c)kk! zk,
(s)k = s · · · (s + k −1)
is the hypergeometric function and λ = s(1 −s) are the eigenvalues. The full derivation
of these eigenfunctions is given in [38].
2.3.2
Cylinders
Not all domains in hyperbolic surfaces satisfy the isoperimetric inequality. It may still
be desirable to investigate the eigenvalues of such regions; we will see a particular case
of this when we look at the Bolza surface in Section 3.4. One region that does not,
in general, satisfy the isoperimetric inequality is the hyperbolic cylinder. We take the
deﬁnition from [57].
Deﬁnition 2.31 (Hyperbolic Cylinder) A hyperbolic cylinder C, with core geodesic γ
of length l, is the quotient of H by a hyperbolic isometry
τ =
 
el/2
0
0
e−l/2
!
,
l > 0.
The core geodesic is the image of the axis of τ under the quotient map H/⟨τ⟩.
38
C
Cw
θ
ρ
γ
Figure 2.3: Collar Cw contained in hyperbolic cylinder C
We use Fermi coordinates to describe a point p ∈C. Denote by l the length of γ,
parametrized with constant speed. ρ is the signed distance of p from γ and θ is the
projection of p onto γ. For example, in Figure 2.3, the Fermi coordinates of the point on
the boundary of Cw at the end of the arrow are (ρ, θ).
Deﬁnition 2.32 (Collar) The collar Cw, for w ≥l is
Cw = {(ρ, θ) ∈C | l cosh(ρ) < w, 0 ≤θ ≤2π}.
Remark 2.33 Note that Cw is diﬀeomorphic to a annulus Ωof constant width ρ, with
two boundary components of length w. In particular, for such an annulus, we have the
following formulae for its area and the length of its boundary:
A(Ω) =2l sinh(ρ),
l(∂Ω) =2l cosh(ρ),
where again, l is the length of the core geodesic, and ρ is the constant distance from the
core geodesic to the boundary.
With respect to the Fermi coordinates, C has the metric
ds2 = dρ2 + l2 cosh2 ρ
4π2
dθ2.
The Laplacian on C is given by
∆= −
 d2
dρ2 + tanh ρ d
dρ +
4π2
l2 cosh2(ρ)
d2
dθ2

.
39
There is a fundamental system of even and odd eigenfunctions; these are given and
analyzed in [11]. With respect to the core geodesic γ, the even function is
φeven
k
(s; ρ) = (cosh(ρ))
2πik
l
2F1
s
2 + πik
l , 1 −s
2
+ πik
l ; 1
2; −sinh2(ρ)

and the odd function is
φodd
k (s; ρ) = sinh(ρ)(cosh(ρ))
2πik
l
2F1
1 + s
2
+ πik
l , 2 −s
2
+ πik
l ; 3
2; −sinh2(ρ)

where, once again, the corresponding eigenvalues are λ = s(1 −s).
Although annuli in hyperbolic cylinders do not satisfy the isoperimetric inequality
in Deﬁnition 1.13, Mondal proved that hyperbolic cylinders satisfy a similar geometric
isoperimetric inequality. First we need the notion of symmetrization:
Deﬁnition 2.34 (Symmetrization) Let Ωbe an essential annulus with core geodesic
γ. The symmetrization of Ωis the annulus Ω0 of constant width that is symmetric with
respect to the core geodesic γ and has the same area as Ω.
Then we have the following:
Lemma 2.35
[57, Lemma 2.2.3] Let Ωbe an essential annulus with piecewise smooth
boundary and Ω0 be the symmetrisation of Ω. Then l(∂Ω) ≥l(∂Ω0).
Proof:
The proof is a partial reproduction of that in [57]. Let Ωbe an essential annulus
in a cylinder C with core geodesic γ of length k, and Ω0 its symmetrisation. Lemma 2.35
is proved in two parts; ﬁrst, when ∂Ωis graph over γ, and the more general case when
∂Ωis arbitrary. The two parts of the proof are similar, so here we just reproduce the
ﬁrst part.
Since ∂Ωis a graph over γ, we can take two piecewise functions r1 and r2 to map γ to
the boundary in the positive and negative directions respectively (recall that the distance
in Fermi coordinates is signed). Formally, for i ∈{1, 2},
ri : [0, k] →R,
ri(0) = ri(k),
and ∂Ωis parametrised in Fermi coordinates as
{(t, ri(t)) | t ∈[0, k]}.
Without loss of generality, we can assume r1(t) > r2(t) for t ∈[0, k]. We integrate with
respect to the hyperbolic cylinder metric (see Section 2.3.2) to calculate
A(Ω) =
Z k
0
Z r2(t)
r1(t)
cosh (r)drdt =
Z k
0
(sinh (r2(t)) −sinh (r1(t))) dt
40
and
l(∂Ω) =
Z k
0
(r′
1(t) + 1)
1
2 cosh (r1(t))dt +
Z k
0
(r′
2(t) + 1)
1
2 cosh (r2(t))dt.
Note that
l(∂Ω) ≥
Z k
0
(cosh (r1(t)) + cosh (r2(t)))dt,
and let L denote the expression on the right hand side of this inequality. For the symmetri-
sation Ω0, the functions from the core geodesic to the boundary are constant, for example
equal to ±ρ, where ρ = sinh−1 
A(Ω)
2k

. Taking such a ρ ensures that A(Ω) = A(Ω0). Here,
recall the simpler formulae
l(∂Ω0) = 2|k| cosh(ρ)
and
A(Ω0) = 2|k| sinh(ρ).
To prove the lemma, we show that
l(∂Ω)2 −A(Ω)2 ≥l(∂Ω0)2 −A(Ω0)2.
The result follows from the equality of the surface areas. First, note that
l(∂Ω)2 −A(Ω)2 ≥(L + A(Ω))(L −A(Ω)).
Let us consider the two factors on the right hand side of this inequality:
L + A(Ω) =
Z k
0
((cosh (r2(t)) + sinh (r2(t))) + (cosh(r1(t)) −sinh (r1(t))))dt
=
Z k
0
(exp(r2(t)) + exp(−r1(t)))dt
and
L −A(Ω) =
Z k
0
(exp(−r2(t)) + exp(r1(t)))dt.
By Hölder’s inequality,
(L + A(Ω))(L−A(Ω)) ≥
Z k
0

(exp(r2(t)) + exp(−r1(t)))
1
2(exp(−r2(t)) + exp(r1(t)))
1
2

dt
2
=
Z k
0
(2 + 2 cosh (r1(t) + r2(t)))
1
2 dt
2
≥4k2,
since cosh(t) ≥1. On the other hand, 4k2 is precisely the value of
l(∂Ω0)2 −A(Ω0)2.
Therefore, Lemma 2.35 is proved for Ωwith ‘nice’ boundary.
□
41
