---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-031-b2-useful-corollaries
section_title: "B.2 Useful corollaries."
section_number: null
pages: 25-28
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
For proving the main transformation formula which allows us to get from (2.17) the expression
(2.28) we need following corollaries.
Corollary 1.
I(µ) = Sb(µ5 + µ6)Sb(2Q −
6
X
i=1
µ6)
Y
1≤i<j≤4
Sb(µi + µj)I(ν),
(B.6)
26
where we deﬁne the integral I(µ) as
I(µ) = 1
2
Z i∞
−i∞
Q6
i=1 Sb(µi ± u)
Sb(±2u)
du.
(B.7)
Here we have
[ν1, ν2, ν3, ν4, ν5, ν6] = [µ1 + ξ, µ2 + ξ, µ3 + ξ, µ4 + ξ, µ5 −ξ, µ6 −ξ]
and
2ξ = Q −
4
X
i=1
µi .
Later it will be convenient to write 6 variables µ in the following way
[µ] =
 µ1
µ2
µ3
µ4
µ5
µ6

.
Corollary 2. :
J(µ, ν) =
3
Y
i=1
Sb(µi + ν4)Sb(νi + µ4)I(ρ),
(B.8)
with
J(µ, ν) =
Z i∞
−i∞
4
Y
i=1
Sb(µi −u)Sb(νi + u)du,
(B.9)
which has U(1) gauge symmetry, and the balancing condition P4
i=1(µi + νi) = 2Q. Here we
have
[ρ1, ρ2, ρ3, ρ4, ρ5, ρ6] = [µ1 + ξ, µ2 + ξ, µ3 + ξ, ν1 −ξ, ν2 −ξ, ν3 −ξ]
and
2ξ = Q −ν4 −
3
X
i=1
µi = −Q + µ4 +
3
X
i=1
νi.
Again it is useful to have the following notation
[µ, ν] =
 µ1
µ2
µ3
µ4
ν1
ν2
ν3
ν4

,
The inversion of Corollary 2 is the following
Corollary 3.
I(ρ) =
Y
1≤i<j≤3
Sb(ρi + ρj)Sb(ρi+3 + ρj+3)J(µ, ν),
(B.10)
27
and the balancing condition P4
i=1 µi + νi = 2Q. Here we have
 µ1
µ2
µ3
µ4
ν1
ν2
ν3
ν4

=
 ρ1 −x
ρ2 −x
ρ3 −x
Q −ρ456 −x
ρ4 + x
ρ5 + x
ρ6 + x
Q −ρ123 + x

,
where ρ123 = ρ1 + ρ2 + ρ3, ρ456 = ρ4 + ρ5 + ρ6, and x is arbitrary.
Corollary 4. :
I(µ) = Sb(2Q −
6
X
i=1
µi)
Y
1≤i<j≤6
Sb(µi + µj)I(Q/2 −µ).
(B.11)
To get the desired transformation formulas one should use the following asymptotic formulas
when some of the parameters go to inﬁnity
lim
u→∞e
πi
2 B2,2(u)Sb(u)
=
1,
for arg b < arg u < arg 1/b + π,
lim
u→∞e−πi
2 B2,2(u)Sb(u)
=
1,
for arg b −π < arg u < arg 1/b.
By taking different restrictions for the parameters one can get lots of identities from the integral
identity (B.5). Let us take
µ1 →µ1 + µ;
µ5 →µ5 −µ
with the following limit µ →∞. The left hand-side of (B.5) gives
Ih(µ2, µ3, µ4, µ6, µ7, µ8) = 1
2
Z i∞
−i∞
Q4
i=2 Sb(µi ± z)Sb(µi+4 ± z)
Sb(±2z)
dz,
(B.12)
without any restrictions for parameters µ2, µ3, µ4, µ6, µ7, µ8 and in the right hand-side one needs
to shift the integration variable z →z −µ/2 and afterwards taking the limit µ →∞which
gives
Y
2≤i<j≤4
Sb(µi + µj)Sb(µi+4 + µj+4)
(B.13)
×
Z i∞
−i∞
dz Sb(ξ + z + (µ1 + µ5)/2)Sb((µ1 + µ5)/2 −ξ −z)
×
4
Y
i=2
Sb(µi + ξ −(µ1 + µ5)/2 −z)Sb(µi+4 −ξ + (µ1 + µ5)/2 + z)dz,
and 2ξ = Q −P4
i=2 µi.
Inverting now the equality (B.12)=(B.13) one gets Corollary 3. To get Corollary 1 one takes
the limit µ7, µ8 →∞such that µ7 −µ8 = O(1) in (B.5).
28
Application of (B.2) twice and thrice gives new integral transformations formulas for (B.1)
while further application of (B.2) does not lead to new integral transformations. It can be shown
[S08]
V (s1, . . . , s8) =
Y
1≤i<j≤8
Γ(sisj; p, q) V
√pq
s1
, . . . ,
√pq
s8

,
(B.14)
the reduction to the hyperbolic level of which brings to Corollary 4.
In [SV11] other reductions of V -functions were considered in connections with the so-called
state integral for 41 knot [Hi1] and with the kernel of S-move [T03].
