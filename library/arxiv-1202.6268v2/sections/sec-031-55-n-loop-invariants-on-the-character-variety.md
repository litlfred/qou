---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-031-55-n-loop-invariants-on-the-character-variety
section_title: "n-loop invariants on the character variety"
section_number: 5.5
pages: 35-37
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
mula to general representations ρ∈ XM in Section 4, we may now generalize the entire
state integral. The basic result for the higher invariants ST ,n is that their formulas remain
completely unchanged. The shapes zi simply become functions of the representation ρ, and
satisfy deformed gluing equations ( 4.5)–(4.6). One must also make sure to use a generalized
ﬂattening whenever it occurs, just as in Section 4.
We note that, for a hyperbolic knot complement M = S3\K, the generalized Chern-
Simons state integralZM (u; ℏ) is expected to match the asymptotic expansion of the colored
Jones polynomials JN (K;q). Speciﬁcally, one should consider the limit
(5.22) N→∞ , ℏ→ 0, q N =eN ℏ =e2u ﬁxed,
where m =eu is the meridian eigenvalue for a geometric representation ρm in the neighbor-
hood of the discrete faithful. This is the full Generalized Volume Conjecture of [ Guk05].
To see how formulas for the generalized invariants ST ,n , n≥ 0, come about, consider the
state integral at general meridian eigenvalue m =eu. From ( C.23) of Appendix C, we ﬁnd
ZT (u; ℏ) =
√
8π
ℏ3 det B
∫ dNZ
(2πℏ)N/ 2
N∏
i=1
ψℏ(Zi)e− 1
2ℏ Z·B−1AZ
×e
1
ℏ
[
2u·DB−1u+(2πi +ℏ)f ·B−1u+ 1
2
(
iπ + ℏ
2
) 2
f ·B−1ν−Z·B−1
(
2u+
(
iπ + ℏ
2
)
ν
) ]
,(5.23)
where u := (0,..., 0,u ) and D is the block appearing in any completion of the Neumann-
Zagier matrices ( A B) to ( A B
C D )∈Sp(2N, Q), such that the bottom row D of D appears in
the longitude gluing equation C·Z +D·Z ′′ =v + 2πiνλ (Section
4.4). Indeed, since we are
contracting with u, only this bottom row of D really matters in ( 5.23).
The critical points of the state integral are now given by
(5.24) AZ + BZ ′′ = 2u +iπν,
36 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
with Z ′′ :=−~Li1(e−Z). As expected, this is the logarithmic form of the deformed gluing
equation (
4.5). Thus, all critical points correspond to representations ρ = ρm∈ XM . The
multivalued nature of this equation must be carefully studied to make sure desired solutions
actually exist. However, for example, representations on the geo metric component X geom
M
always exist in a neighborhood of the discrete faithful representa tion, if we choose u = logm
to be close to zero (and use a regular triangulation).
We then start expanding the state integral around a critical point , setting
(5.25) ZT (u; ℏ)∼ ℏ− 3
2 exp
[ 1
ℏST , 0(u) +ST , 1(u) + ℏST , 2(m) + ℏ2ST , 3(m) +...
]
.
The leading contribution ST , 0(ρ) is given, following some standard manipulations using the
generalized ﬂattening, by
(5.26) ST , 0(u) = uv (u)− 1
2 (Z−iπf )· (Z ′′ +iπf ′′) +
N∑
i=1
~Li2(e−Z)
(
mod π2
6
)
.
Here we write ST , 0 as a function of the logarithmic meridian eigenvalue u, though a ﬁxed
choice of representation ρ will implicitly ﬁx the choice of longitude eigenvalue v = log(−ℓ) as
well. Expression ( 5.26) is a holomorphic version of the complex volume of a cusped manifold
with deformed cusp. Explicitly,
(5.27) ST , 0(u) = i(VolM (u) +iCSM (u))− 2vℜ(u).
This is the correct form of the complex volume to use in the Generalize d Volume Conjecture,
cf. [
GM08].
At ﬁrst subleading order, we re-derive the generalized torsion for mula. The calculation is
identical to that of Section 5.3, with the exception of the correction ( 5.13) coming from the
ℏ0 part of the exponential. This correction now becomes
(5.28) exp
[
f· B−1u + iπ
2 f· B−1ν− 1
2Z· B−1ν
]
.
To simplify this correction, we must use Af + Bf ′′ = ν and a deformed gluing equation
AZ + BZ ′′ = 2 u +iπν. The u-dependent part of the gluing equation cancels the new
u-dependent term in ( 5.28), ultimately leading to the same result
exp
[
f· B−1u + iπ
2 f· B−1ν− 1
2Z· B−1ν
]
=
(
zf ′′
z′′−f) −1/ 2
,
and therefore the same torsion 8
(5.29) τT = 4πe−2ST , 1 = 1
2 det
(
A∆ z′′ + B∆ −1
z
)
zf ′′
z′′−f.
Finally, we can produce a generalized version of the Feynman rules of Section 5.4. We
note, however, that the u-dependent terms in ( 5.23) do not contribute to either the vacuum
energy Γ (0) (at order ℏ1 or higher), the propagator, or the vertex factors Γ (k)
i . Therefore,
8The normalization of the torsion here diﬀers from the torsion at the discrete faithful by a factor of π 2.
In fact, we intentionally changed the normalization of the entire sta te integral ( 5.23) by π 2. This is because
we wanted the state integral to match the asymptotics of the colo red Jones polynomials exactly, and the
asymptotics happen to jump by π 2 when u⁄= 0, cf. [GM08].
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 37
the Feynman rules must look exactly the same. The only diﬀerence is t hat the critical
point equation ( 5.24) requires us to use shape parameters that satisfy the generalize d gluing
equations.
5.6. Example: 4 1 completed. We may demonstrate the power of the Feynman-diagram
approach by computing the ﬁrst two subleading corrections ST , 2 andST , 3 for the ﬁgure-eight
knot complement.
We can use the same Neumann-Zagier datum described in Section
2.6, along with the
generalized ﬂattening of Section 4.6. Let us specialize to representations ρm on the geometric
component of the character variety. Then the two shapes z, ware expressed as functions on
the A-polynomial curve,
(5.30) z =−m2−m−2
1 +m2ℓ , w = m2 +ℓ
m2−m−2 ,
as in ( 4.21).
The 2-loop invariant is explicitly given in ( 1.19) of the Introduction. Evaluating this
expression in Mathematica, we ﬁnd
S41, 2 =−w3(z + 1) +w2((11− 8z)z− 4) +w(z− 1)(z(z + 12)− 5) + (z− 2)(z− 1)2
12(w +z− 1)3 .
Upon using ( 5.30) to substitute rational functions for z and w, the answer may be most
simply expressed as
(5.31) ~S41, 2 = S41, 2 + 1/8
τ 3
41
=− 1
192
(
m−6−m−4− 2m−2 + 15− 2m2−m4 +m6)
,
where we have divided by a power of the torsion as suggested in ( 1.14) of the Introduction.
(We have also absorbed a constant 1/8, recalling that our formula is only well deﬁned modulo
Z/24.
In a similar way, we may calculate the 3-loop invariant, ﬁnding unambigu ously
(5.32) ~S41, 3 = S41, 3
τ 6
41
= 1
128
(
m−6−m−4− 2m−2 + 5− 2m2−m4 +m6)
.
These answers agree perfectly with the ﬁndings of [ DGLZ09], and the comparison there
to the asymptotics of the colored Jones polynomials at general u. Moreover, at the discrete
faithful representation we obtain
(5.33) S41, 2 = 11i
72
√
3 =− 11
192τ 3
41
, S 41, 3 =− 1
54 = 1
128τ 6
41
,
in agreement with known asymptotics of the Kashaev invariant.
