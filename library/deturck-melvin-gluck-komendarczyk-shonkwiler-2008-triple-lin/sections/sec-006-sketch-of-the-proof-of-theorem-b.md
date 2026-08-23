---
doc_id: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-006-sketch-of-the-proof-of-theorem-b
section_title: "Sketch of the proof of Theorem B"
section_number: null
pages: 23-25
source_pdf: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-linking-numbers.pdf
source_sha256: db149864ce367da2
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
---
Let L be a 3-component link in S3 with pairwise linking numbers p, q
andr all zero. We saw in Theorem A that these numbers are the degrees
of the characteristic map gL : T 3→ S2 on the 2-dimensional coordinate
subtori. Thus gL is homotopic to a map which collapses the 2-skeleton of
T 3, and so is in effect a map of S3→S2. The Hopf invariant of this map,
which we will regard as the Hopf invariant of gL, is equal to Pontryagin’s
ν-invariant comparinggL to the constant map, and we will denote this by
ν(gL).
To calculate this Hopf invariant, we adapt J. H. C. Whitehead’s integral
formula for the Hopf invariant of a map from S3→ S2 to the case of a
map from T 3→S2, and show how to make the calculation explicit.
Using Hopf’s definition of his invariant of a map f : S3→ S2 as the
linking number between the inverse images of two regular values, White-
head [1947] expressed this as follows. Let ω be the area 2-form on S2,
normalized so that
R
S2ω = 1. Then its pullback f∗ω is a closed 2-form
on S3 which is exact because H2(S3; R) = 0. Hence f∗ω = dα for some
1-form α on S3, and Whitehead showed that
Hopf(f) =
Z
S3
α∧f∗ω,
the integral being independent of the choice of α.
We recast Whitehead’s formula in terms of vector fields by letting Vf
be the vector field on S3 corresponding in the usual way to the 2-form
f∗ω. Then Vf is divergence-free, since f∗ω is closed, and is in fact in the
image of curl since f∗ω is exact. Thus Vf =∇× W for some vector field
W on S3, and the integral formula for the Hopf invariant becomes
Hopf(f) =
Z
S3
W  Vf d(vol),
independent of the choice of W .
To make Whitehead’s formula more explicit, one needs a way to produce
a vector fieldW whose curl isVf. On R3 this can be done by viewingVf as
274 DETURC, GLUCK, KOMENDARCZYK, MEL VIN et al
a flow of electric current and then calculating the corresponding magnetic
field BS(Vf) using the classical formula of Biot and Savart [1820]:
BS(Vf) = −∇× Gr(Vf),
where Gr is the Green’s operator that inverts the vector Laplacian. Then
∇× BS(Vf) =Vf
by Ampere’s Law. The justification for these statements, and a nice ex-
planation, can be found in Chapter 5 – Magnetostatics in Griffiths [1989].
The explicit formula for the Green’s operator on R3 is given by con-
volution with the fundamental solution φ(r) = −1/(4πr) of the scalar
Laplacian, and hence
BS(Vf)(y) =
Z
R3
Vf(x)×∇yφ (∥y−x∥) dx,
assuming that V is compactly supported, to guarantee that the integral
converges. The corresponding formula on S3 was given by DeTurck and
Gluck [2008] and by Kuperberg [2008].
We can summarize the calculation of the Hopf invariant in the single
formula
Hopf(f) =
Z
S3
BS(Vf)  Vf d(vol)
which was Woltjer’s original expression for the helicity of the vector field
Vf.
A routine check shows that the above formula, with the integration over
T 3 instead ofS3, yields the value of the Hopf invariant of the characteristic
map gL :T 3→S2. This provides a formula for Pontryagin’s ν-invariant,
and portrays it as the helicity of the associated vector field VgL, which for
simplicity we denote by VL:
ν(gL) = Hopf(gL) = Hel(VL) =
Z
T 3
BS(VL)  VL d(vol). (‡)
A straightforward calculation shows that
VL = Ft×Fu  F
4π∥F∥3 ∂/∂s + Fu×Fs  F
4π∥F∥3 ∂/∂t + Fs×Ft  F
4π∥F∥3 ∂/∂u,
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS 275
where F : T 3→ R3−{ 0} is the map defined in Section 3, and where
subscripts denote partial derivatives.
Therefore, to make the integral formula (‡) explicit, it remains to obtain
an explicit formula for the Biot-Savart operator on the 3-torus. As in the
case of R3, this depends on having an explicit formula for the fundamental
solution of the scalar Laplacian.
