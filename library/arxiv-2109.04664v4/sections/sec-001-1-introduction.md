---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
Let N ≥ 2 be an integer.
In [10], R. Kashaev introduced a link invariant ⟨K⟩N for a knot K in the three-
sphere S3 by using the so-called quantum dilogarithm. In [11], he studied its
asymptotic behavior when N → ∞ for several hyperbolic knots and conjectured
that it would determine its hyperbolic volume for any hyperbolic knot, where a knot
is called hyperbolic if its complement possesses a complete hyperbolic s tructure with
ﬁnite volume. More precisely he conjectured
Conjecture 1.1 (Kashaev’s conjecture). LetH be a hyperbolic knot in S3. Then
the following equality holds.
(1.1) lim
N →∞
log |⟨H⟩N |
N = V
(
S3 \H
)
2π ,
where V
(
S3 \H
)
is the hyperbolic volume.
LetJN (K;q) be the colored Jones polynomial associated with the N -dimensional
irreducible representation of the Lie algebra sl(2; C) [12, 32]. We normalize it so that
JN (U ;q) = 1 for the unknot U , and that J2(K;q) is the ordinary Jones polynomial
[9]. In [23], J. Murakami and the ﬁrst author proved that Kashaev’s invariant ⟨K⟩N
coincides with the N -dimensional colored Jones polynomial JN (K;q) evaluated at
q =e2π √−1/N . They also generalized Kashaev’s conjecture for general knots:
Conjecture 1.2 (Volume Conjecture). For any knot K ⊂S3, we have
(1.2) lim
N →∞
log
⏐
⏐
⏐JN
(
K;e2π √
−1/N
) ⏐
⏐
⏐
N = Vol
(
S3 \K
)
2π .
Here, Vol(S3 \K) is the simplicial volume, also known as the Gromov norm [6] ( see
also [33]), which is normalized so that Vol
(
S3 \H
)
= V
(
S3 \H
)
ifH is hyperbolic.
Date: August 17, 2022.
2020 Mathematics Subject Classiﬁcation. Primary 57K16 57K14 57K10.
Key words and phrases. colored Jones polynomial, ﬁgure-eight knot, volume conjec ture,
Chern–Simons invariant, Reidemeister torsion.
The ﬁrst author is supported by JSPS KAKENHI Grant Numbers JP 16H03927, JP22H01117,
JP20K03601, JP20K03931. The second author is supported by g rants from the Simons Foundation
(#354595 and #708778).
1
2 HITOSHI MURAKAMI AND ANH T. TRAN
Kashaev’s conjecture was complexiﬁed by T. Takata, J. Murakami, M. Okamoto,
Y. Yokota and the ﬁrst author in [24] by dropping the absolute value symbol (and
replacing ⟨H⟩N with JN
(
H;e2π √−1/N
)
) in (1.1).
Conjecture 1.3 (Complexiﬁcation of Kashaev’s conjecture). For a hyperbolic knot
H, we have
(1.3) lim
N →∞
logJN
(
H;e2π √−1/N
)
N = V
(
S3 \H
)
+ √−1 CS(S3 \H)
2π ,
where CS is the SO(3) Chern–Simons invariant of H associated with the Levi-Civita
connection [16].
More detailed asymptotic formulas are known for several knots [1, 28, 30]:
⟨H⟩N ∼
N →∞
ω (H)N 3/ 2 exp
( N
2π CV(H)
)
,
where CV( H) := Vol
(
S3 \H
)
+ √−1 CS(S3 \ H) is the complex volume and
2√−1ω (H)2 is the adjoint (cohomological) Reidemeister torsion twisted by the
holonomy representation of π1(S3 \H) to SL(2; C) [29].
It was also generalized by replacing 2 π √−1 with another complex number ξ
[2, 21].
Conjecture 1.4 (Generalized Volume Conjecture) . Let ξ ⁄= 2π √
−1 be a complex
number close to 2π √−1, and H a hyperbolic knot. Then we have
(1.4) JN
(
H;eξ/N
)
∼
N →∞
C
sinh(ξ) ×τ(ξ)1/ 2
( N
ξ
) d
exp
( N
ξS(ξ)
)
with d a constant. Here S(ξ) and τ(ξ) are related to the SL(2; C) Chern–Simons
invariant and the adjoint Reidemeister torsion, respectiv ely, both associated with a
certain representation of π1(S3 \H) to SL(2; C).
In this paper, we are mainly interested in the ﬁgure-eight knot. We ﬁ rst list
known results for the asymptotic behavior of the colored Jones po lynomial of the
ﬁgure-eight knot E.
We deﬁne a function ϕ as
ϕ (ξ) := arccosh
(
cosh(ξ) − 1
2
)
for a complex number ξ, where we use the following branch of arccosh:
arccosh(x) := log
(
x −
√
−1
√
1 −x2
)
,
and we choose the branch cut of log as ( −∞, 0). Note that ϕ (0) = −π √−1/ 3 and
ϕ (κ) = 0, where κ := log
(
3+
√
5
2
)
. We also deﬁne
S(ξ) := Li 2(e−ξ−ϕ (ξ)) − Li2(e−ξ+ϕ (ξ)) +ξϕ (ξ),
˜S(ξ) := Li 2(e−ξ−ϕ (ξ)) − Li2(e−ξ+ϕ (ξ)) + (ξ − 2π
√
−1)(ϕ (ξ) + 2π
√
−1),
T (ξ) := 2√
(2 cosh(ξ) + 1)(2 cosh(ξ) − 3)
,
where
Li2(z) := −
∫ z
0
log(1 −x)
x dx
is the dilogarithm function, where we choose the branch cut as (1 , ∞). Note that
S(0) = ˜S(2π √−1) = Li 2(eπ √−1/ 3) − Li2(e−π √−1/ 3) = √−1 × 2. 02988... .
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 3
The quantities S(ξ), ˜S(ξ), and T (ξ) are related to the Chern–Simons invariant
and the adjoint Reidemeister torsion associated with a certain repr esentation of
π1
(
S3 \E
)
to SL(2; C). See Section 5 for details.
(1) ξ = 2π √−1:
This corresponds to the case of the Volume Conjecture. Kashaev
sketched a proof of (1.2) in [11], and then T. Ekholm gave a detailed pr oof of
(1.2). See for example [27, Section 3.2] for Ekholm’s proof. Later, J .E. An-
dersen and S.K. Hansen [1, Theorem 1] followed Kashaev’s method to prove
the following asymptotic formula.
JN
(
E;e2π √−1/N
)
∼
N →∞
2π 3/ 2
( N
2π √−1
) 3/ 2
T (2π
√
−1)1/ 2 exp
( N
2π √−1
˜S(2π
√
−1)
)
.
Since S(0) = √−1 Vol
(
S3 \E
)
, this reﬁnes the Volume Conjecture for the
ﬁgure-eight knot.
(2) ξ is close to 2 π √−1 and not purely imaginary:
Y. Yokota and the ﬁrst author proved the following formula [26].
(1.5) lim
N →∞
logJN (E;eξ/N )
N =
˜S(ξ)
ξ .
(3) ξ is purely imaginary with 5 π/ 3< |ξ|< 7π/ 3, and 2π/ |ξ| is irrational with
ﬁnite irrationality measure:
In [17] (see [22] for correction), the ﬁrst author proved the follo wing
formula.
lim
N →∞
logJN (E;eξ/N )
N =
˜S(ξ)
ξ .
See also [19, 6.2.2].
(4) ξ is of the form 2 π √−1 +u for a real number u with 0 < |u|<κ :
The ﬁrst author proved the following asymptotic formula [21, Theo-
rem 1.4]:
(1.6) JN
(
E;eξ/N
)
∼
N →∞
√−π
2 sinh(u/ 2)T (ξ)1/ 2
( N
ξ
) 1/ 2
exp
( N
ξ
˜S(ξ)
)
.
Note that this reﬁnes (1.5) when ξ is as above.
(5) ξ satisﬁes the inequalities |2 coshξ − 2|< 1 and | Imξ|<π/ 3:
In this case, JN
(
E;eξ/N )
converges. In fact, we have
lim
N →∞
JN
(
E;eξ/N
)
= 1
∆( E;eξ),
where ∆( E;t) = −t + 3 −t−1 is the normalized Alexander polynomial of
the ﬁgure-eight knot E [18, Theorem 1.1].
See [5] for general knots.
(6) ξ = ±κ:
In this case, JN
(
E;eκ/N )
grows polynomially. More precisely, we have
JN
(
E;eκ/N
)
∼
N →∞
Γ(1/ 3)
(3κ)2/ 3N 2/ 3,
where Γ(z) is the Gamma function [8, Theorem 1.1].
(7) ξ is real and |ξ|>κ :
The ﬁrst author proved the following formula [17, Theorem 8.1] (see also
[20, Theorem 3.2] and [19, Lemma 6.7]).
(1.7) lim
N →∞
logJN (E;eξ/N )
N = S(ξ)
|ξ| .
