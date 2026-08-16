---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-006-8-hitoshi-murakami-and-anh-t-tran
section_title: "HITOSHI MURAKAMI AND ANH T. TRAN"
section_number: 8
pages: 8-10
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
Therefore we have from (2.1)
JN
(
E; exp(ξ/N )
)
=
exp
(
TN
(
ξ
2π √−1 (1 + 1
2N )
))
exp
(
TN
(
ξ
2π √−1 (1 − 1
2N )
))
×
N −1∑
k=0
e−kξ
exp
(
TN
(
ξ
2π √−1 (1 − 2k+1
2N )
))
exp
(
TN
(
ξ
2π √−1 (1 + 2k+1
2N )
)) .
We use the following lemma, a proof of which is given in Section 6.
Lemma 3.1. We have
exp
(
TN
(
ξ
2π √−1 (1 + 1
2N )
))
exp
(
TN
(
ξ
2π √−1 (1 − 1
2N )
)) = 1
1 −eξ = −e−ξ/ 2
2 sinh(ξ/ 2).
Now we deﬁne
fN (z) := 1
N
(
TN
( ξ(1 −z)
2π √−1
)
−TN
( ξ(1 +z)
2π √−1
))
−ξz + 2π
√
−1z
so that
(3.1) JN
(
E; exp(ξ/N )
)
= 1
2 sinh(ξ/ 2)
N −1∑
k=0
exp
(
N ×fN
( 2k + 1
2N
))
.
Since TN (z) is deﬁned for z with 0 < Re(zeθ√−1) < cosθ, the function fN (z) is
deﬁned for z with ⏐
⏐
⏐
⏐
Imz
tanθ + Rez
⏐
⏐
⏐
⏐< 1
from the assumption tan θ< π
ξ .
From Proposition 2.8, fN (z) converges to the following function:
F (z) := 1
ξ
(
L2
( ξ(1 −z)
2π √−1
)
− L2
( ξ(1 +z)
2π √−1
))
−ξz + 2π
√
−1z
in the region
{
z ∈ C
⏐
⏐
⏐
⏐
⏐
⏐
⏐
Imz
tanθ + Rez
⏐
⏐
⏐
⏐ ≤ 1 − 2πν
ξ sinθ, | Rez| ≤ 2πM
ξ − 1
}
.
Since Im
(
ξ(1±z)
2π √−1
)
= −ξ
2π (1 ± Rez),
F (z) = 1
ξ
(
Li2
(
e−ξ(1+z)
)
− Li2
(
e−ξ(1−z)
))
+ξz
when −1< Rez <1 from (2.4).
Remark 3.2. When x is real and −1<x< 1, then F (x) is also real.
From Lemma 2.9, the ﬁrst and the second derivatives of F (z) are given as follows:
F ′(z) = L1
( ξ(1 −z)
2π √−1
)
+ L1
( ξ(1 +z)
2π √−1
)
−ξ + 2π
√
−1,
F ′′(z) = ξ
2π √−1
(
L0
( ξ(1 −z)
2π √−1
)
− L0
( ξ(1 +z)
2π √−1
))
= ξ(e−ξz −eξz )
eξ +e−ξ −eξz −e−ξz.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 9
Note that when −1< Rez <1, we have
F ′(z) = log(1 −e−ξ(1−z)) + log(1 −e−ξ(1+z)) +ξ
= log(eξ +e−ξ −eξz −e−ξz )
(3.2)
from (2.3), since Im
(
ξ(1±z)
2π √−1
)
= − ξ
2π (1 ± Rez).
We assume that ξ >κ, where κ := arccosh(3/ 2) = log( 3+
√
5
2 ) = 0. 962... . Put
ϕ (ξ) := arccosh
(
cosh(ξ) − 1
2
)
= log
(
cosh(ξ) − 1
2 + 1
2
√
(2 cosh(ξ) − 1)2 − 4
)
.
Note that since ξ > κ, we have cosh( ξ) > cosh(ϕ (ξ)) and cosh( ξ) > cosh(κ) = 3
2 .
So we have 0 < ϕ(ξ) < ξ. Note also that this deﬁnition is the same as that in
Section 1.
Since 0 <ϕ (ξ)<ξ , we have
F (ϕ (ξ)/ξ ) = 1
ξ
(
Li2(e−ξ−ϕ (ξ)) − Li2(e−ξ+ϕ (ξ))
)
+ϕ (ξ),(3.3)
F ′(ϕ (ξ)/ξ ) = 0,(3.4)
F ′′(ϕ (ξ)/ξ ) = −ξ
√
(2 cosh(ξ) − 1)2 − 4.(3.5)
The second equality follows since
eϕ (ξ) +e−ϕ (ξ) =eξ +e−ξ − 1.
Put
S(ξ) := ξF (ϕ (ξ)/ξ ) = Li 2(e−ξ−ϕ (ξ)) − Li2(e−ξ+ϕ (ξ)) +ξϕ (ξ).
Since
dS (ξ)
dξ = (1 + ϕ ′(ξ)) log(1 −e−ξ−ϕ (ξ)) − (1 −ϕ ′(ξ)) log(1 −e−ξ+ϕ (ξ))
+ϕ (ξ) +ξϕ ′(ξ)
= log eϕ (ξ) −e−ξ
1 −e−ξ+ϕ (ξ) +ϕ ′(ξ) log
(
eξ +e−ξ −eϕ (ξ) −e−ϕ (ξ)
)
= log eϕ (ξ) −e−ξ
1 −e−ξ+ϕ (ξ) > 0
and S(κ) = 0, S(ξ)> 0 for ξ >κ.
Recalling that F (x) ∈ R when x is real and −1<x< 1, we have the following
lemma.
Lemma 3.3. As a function of a real variable x, the real-valued function F (x)
takes its maximum S(ξ)/ξ atx =ϕ (ξ)/ξ in the half open interval [0, 1). Moreover,
it is strictly increasing (decreasing, respectively) when x < ϕ(ξ)/ξ (x > ϕ(ξ)/ξ ,
respectively).
Proof. Since we have
F ′(x) = log(eξ +e−ξ −eξx −e−ξx),
we see that F ′(x) is strictly decreasing. Since F (0) = 0 and F ′(x) becomes 0 when
x =ϕ (ξ)/ξ < 1, the lemma follows. □
We have the following corollary.
Corollary 3.4. For any c− and c+ with 0 < c− < ϕ(ξ)/ξ < c+ < 1, there exists
δ >0 such that F (x)<S (ξ)/ξ −δ if x<c − or x>c +.
