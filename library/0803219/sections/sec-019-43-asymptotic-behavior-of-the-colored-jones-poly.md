---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-019-43-asymptotic-behavior-of-the-colored-jones-poly
section_title: "Asymptotic behavior of the colored Jones polynomial. First of all,"
section_number: 4.3
pages: 28-29
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
---
the volume conjecture for torus knots is proved by Kashaev an d Tirkkonen [25].
In fact J. Dubois and Kashaev [9] proved a stronger result.
Theorem 4.1 ([25]). Let T (a, b ) be the torus knot of type (a, b ). Then we have
the following asymptotic equality for large N .
JN
(
T (a, b ); exp(2π
√
− 1/N )
)
= exp
((
ab − a
b − b
a
) π √ − 1
2N
)
×



exp
(
π √ −1
4
)
4
√
2ab
N 3/ 2 exp
(− abN π √ − 1
2
)
ZN
(
T (a, b )
)
+ 1
4
∞∑
k=1
ak
(
T (a, b )
)
k!
(π √ − 1
2abN
)k−1}
,
where
ZN
(
T (a, b )
)
:=
ab−1∑
j=1
(− 1)(N −1)j j2 4
ab sin
(jπ
a
)
sin
(jπ
b
)
exp
(− j2N π √ − 1
2ab
)
.
and ak (T (a, b )) is a ﬁnite type invariant for every k. See [9] for a topological
interpretation of each term of ZN
(
T (a, b )
)
.
Observe that the limit of (2.1) always exists but that that of (2.2) does not
unless ( a, b ) = (2 , 3) or ( a, b ) = (3 , 2).
Next we review the results in [43] and [19].
Theorem 4.2. Let θ be a complex number with |θ |> 2π/ (ab).
• If Re(θ ) > 0, then we have
lim
N →∞
JN
(
T (a, b ); exp(θ/N )
)
= 1
∆
(
T (a, b ); exp(θ )
).
• If Re(θ ) < 0, then we have
lim
N →∞
log JN
(
T (a, b ); exp(θ/N )
)
N =
(
1 − π √ − 1
abθ − abθ
4π √ − 1
)
π
√
− 1.
Remark 4.3. In [43], the author only proved the case where Im( θ ) > 0. But
taking the complex conjugate we have a similar formula for th e other case. This
was pointed out by A. Gibson.
Putting u := θ − 2π √ − 1, we have
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 247
Corollary 4.4. Let u be a complex number with |u + 2π √ − 1|> 2π/ (ab).
• If Re(u) > 0, then we have
lim
N →∞
JN
(
T (a, b ); (u + 2π
√
− 1)/N )
)
= 1
∆
(
T (a, b ); exp(u)
).
• If Re(u) < 0, then we have
(u + 2π
√
− 1) lim
N →∞
log JN
(
T (a, b ); exp((u + 2π √ − 1)/N )
)
N
= − 1
4ab
{
ab(u + 2π
√
− 1) − 2π
√
− 1
} 2
.
For small θ , Garoufalidis and Lˆ e proved the following.
Theorem 4.5 ([11, Theorem 1]) . For any knot K, there exists a neighborhood
U of 0 such that if θ ∈ U then
lim
N →∞
JN
(
K; exp(θ/N )
)
= 1
∆( K; exp(θ )) .
As in the case of the ﬁgure-eight knot when exp( θ ) is a zero of the Alexander
polynomial, we can prove that the colored Jones polynomial g rows polynomially.
Theorem 4.6 ([19, Theorem 1.2]) . We have
JN
(
T (a, b ); exp
(
± 2π
√
− 1/ (abN )
))
∼
N →∞
e∓π √ −1/ 4 sin(π/a ) sin(π/b )√
2 sin(π/ (ab)) N 1/ 2.
