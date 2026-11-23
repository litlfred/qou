---
doc_id: arxiv-1506.06747v3
doc_title: "Cottingham formula and nucleon polarizabilities"
section_id: sec-040-d-a-new-causal-representation
section_title: "D A new causal representation"
section_number: null
pages: 27-28
source_pdf: 1506.06747v3.pdf
source_sha256: c44709743db78865
toc_source: outline
doc_brief: "Cottingham formula and nucleon polarizabilities — The diﬀerence between the electromagnetic self-energies of proton and neutron can be calculated with the Cottingham formula, which expresses the"
---
Consider the product of two retarded propagators
tret(p, q) =
1
µ2
1 −(q0 + iǫ)2 + q2
×
1
µ2
2 −(p0 + q0 + iǫ)2 + (p + q)2 .
(D.50)
The Fourier transform of this amplitude,
˜tret(p, x) =
Z
d4qe−ix·qtret(p, q) ,
(D.51)
is given by the convolution of the two propagators in
coordinate space. Since these vanish outside the for-
ward light-cone, the same is also true of the convo-
lution: ˜tret(p, x) diﬀers from zero only in the forward
light-cone, x2 ≥0, x0 ≥0.
This
reﬂects
the
properties
of
the
integrand
in (D.51), which contains four poles
tret(p, q) =
1
(q0 −ω1 + iǫ)(q0 + ω1 + iǫ)
×
1
(q0 + p0 −ω2 + iǫ)(q0 + p0 + ω2 + iǫ) ,
ω1 =
q
µ2
1 + q2 ,
ω2 =
q
µ2
2 + (q + p)2 .
(D.52)
All of these occur in the lower half of the q0-plane.
The path of integration can therefore be deformed into
a segment from −∞to −R, a semi-circle of radius R
and a segment from R to +∞. If x0 < 0, the factor
e−iq0x0 suppresses the integrand if R is taken large,
except for the segments where the imaginary part of q0
is not large. But there, tret(p, q) is small, of order 1/R4.
Since the length of these segments is of order R, their
contributions also tend to zero if R is taken large. Since
the integral is path-independent, it vanishes for x0 < 0.
The quantity ˜tret(p, x) is Lorentz invariant. The
time component of the vector x depends on the frame
chosen, but for any point outside the forward light-cone,
there is a frame where the time component is negative.
This conﬁrms that ˜tret(p, x) vanishes outside the for-
ward light-cone.
The advanced version of the amplitude only diﬀers
in the sign of the iǫ prescription. Like the advanced
propagators in coordinate space, the Fourier transform
of tadv(p, q) is diﬀerent from zero only in the backward
light-cone, x2 ≥0, x0 ≤0. The diﬀerence between the
two,
v(p, q) =
1
2πi(tret(p, q) −tadv(p, q)) ,
(D.53)
is therefore causal: the Fourier transform of v(p, q) van-
ishes outside the light-cone. Since tadv(p, q) is the com-
plex conjugate of tret(p, q), the function v(p, q) is real.
For space-like momenta, v(p, q) picks up a contribu-
tion only from the poles at q0 = −p0 ± ω2:
v(p, q) =
1
µ2
1 −q2 δ((p + q)2 −µ2
2) ,
q2 ≤0 , ν ≥0 .
(D.54)
This demonstrates that any function which for space-
like momenta can be represented as
V (ν, q2) =
Z ∞
0
da
Z ∞
0
db ρ(a, b)
a −q2
× {δ(q2 + 2νm −b) −δ(q2 −2νm −b)} ,
(D.55)
admits a causal continuation into the time-like region
(we have replaced µ2
1 and µ2
2 by a = µ2
1, b = µ2
2 −m2,
respectively and imposed the condition b ≥0, which
ensures that, for space-like momenta, the support of
V (ν, q2) is contained in the physical region, Q2 ≤
2m|ν|). There is only one continuation that is free of
ﬁxed poles. The corresponding time-ordered amplitude
is given by
T (ν, q2) =
Z ∞
0
da
Z ∞
0
db
ρ(a, b)
a −q2 −iǫ
×
(
1
b −q2 + 2νm −iǫ
+
1
b −q2 −2νm −iǫ
)
.
(D.56)
This representation, in particular, yields a causal de-
scription of the elastic contributions discussed in sec-
tion 3. Since the form factors are analytic functions of
t, the coeﬃcients vel
1 , vel
2 introduced in (10) do admit a
representation of the form
vel
i (q2) =
Z ∞
0
da
σi(a)
a −q2 −iǫ ,
(D.57)
so that the spectral functions ρi(a, b) = σi(a)δ(b) in-
deed generate the elastic contributions.
