---
doc_id: arxiv-math-0405126v1
doc_title: "ASYMPTOTIC BEHA VIORS OF THE COLORED JONES POL YNOMIALS OF A TORUS KNOT HITOSHI MURAKAMI"
section_id: sec-003-4-hitoshi-murakami
section_title: "HITOSHI MURAKAMI"
section_number: 4
pages: 4-5
source_pdf: 0405126v1.pdf
source_sha256: 713498dbe80f7319
doc_brief: "ASYMPTOTIC BEHAVIORS OF THE COLORED JONES POLYNOMIALS OF A TORUS KNOT HITOSHI MURAKAMI — W e study the asymptotic behaviors of the colored Jones polyn o- mials of torus knots."
---
=
∫
C ′
eN fa,b,r(z)τa,b (z) dz +
∑
k
Res
(
eN fa,b,r(z)τa,b (z); z = kπ
√
− 1/ (ab)
)
.
We will apply the saddle point method (or the method of steepest des cent) to
know the asymptotic behavior of the integral on C′. See for example [14, Theorem
7.2.9]. On C′ we have
fa,b,r
(
se(θ/ 2+π/ 4)√−1 + πr
√
− 1
)
= − s2
2π |r| + πr √ − 1
2 .
So Im fa,b,r (z) is constant on C′ and Re fa,b,r (z) takes its unique maximum at
z = πr √ − 1 (when s = 0) on C′. (Note that this is also true if we change C′
slightly near a pole of τa,b .) Therefore from the saddle point method we have
∫
C ′
eN fa,b,r(z)τa,b (z) dz
∼
N →∞
√
2πτa,b (πr √ − 1)
√
N
√
− d2fa,b,r (z)/dz 2
⏐
⏐
z=πr √
−1
eN fa,b,r(πr √−1)
= π
√
2r
abN eπ √−1/ 4τa,b (πr
√
− 1)eN abπr √−1/ 2.
We also have
Res
(
eN fa,b,r(z)τa,b (z); z = kπ
√
− 1/ (ab)
)
= eN kπ √−1(1− k
2abr ) Res
(
τa,b (z); z = kπ
√
− 1/ (ab)
)
= (− 1)k 2 sinh(kπ √ − 1/a ) sinh(kπ √ − 1/b )
ab eN kπ √−1(1− k
2abr ).
Therefore we have∫
C
eN fa,b,r(z)τa,b (z) dz
∼
N →∞
π
√
2r
abN eπ √−1/ 4τa,b (πr
√
− 1)eN abπr √−1/ 2
+
∑
k
(− 1)k 2 sinh(kπ √ − 1/a ) sinh(kπ √ − 1/b )
ab eN kπ √−1(1− k
2abr ).
(2.2)
Now we want to know the biggest real part of the exponents in (2.2) . We have
max
{
Re
( abπr √ − 1
2
)
, max
k
Re
(
kπ
√
− 1
(
1 − k
2abr
))}
= max
{
− abπ Im r
2 , max
k
− k2π Im r
2ab|r|2
}
=









π Im r
2ab max
k
{
− a2b2, − k2
|r|2
}
if Im r > 0
− π Im r
2ab max
k
{
a2b2, k2
|r|2
}
if Im r < 0
.
Since 1 < h (θ) when 0 < θ < π/ 2, |r| > 1/ (ab), and k runs over positive integers
less than ab|r|h(θ) > 1, we have
max
k
{
− a2b2, − k2
|r|2
}
= − 1
|r|2
THE COLORED JONES POLYNOMIALS OF A TORUS KNOT 5
if Im r > 0. Since 0 < h(θ) < 1 when − π/ 2 < θ < 0, 0 < k < ab |r|h(θ) < ab |r|. So
we have
max
k
{
a2b2, k2
|r|2
}
= a2b2
if Im r < 0.
Therefore if Im r < 0
∫
C
eN fa,b,r(z) τa,b (z)dz ∼
N →∞
π
√
2r
abN eπ √−1/ 4τa,b (πr
√
− 1)eN abπr √−1/ 2
and if Im r > 0
∫
C
eN fa,b,r(z)τa,b (z) dz ∼
N →∞
− 2 sinh(π √ − 1/a ) sinh(π √ − 1/b )
ab eN π √−1(1− 1
2abr ).
Since
Φ a,b,r (N ) ∼
N →∞
ga,b,r
√
N e−N abrπ √−1/ 2,
we have
JN
(
T (a, b ); e2πr √−1)
∼
N →∞
− 2 sinh(π √ − 1/a ) sinh(π √ − 1/b )ga,b,r
ab
√
N eN π √−1
(
1−abr/ 2−1/ (2abr)
)
if Im r > 0 and
JN
(
T (a, b ); e2πr √−1)
∼
N →∞
sinh(arπ √ − 1) sinh(brπ √ − 1)
sinh(abrπ √ − 1) sinh(rπ √ − 1)
if Im r < 0.
Since the Alexander polynomial ∆
(
T (a, b ); t
)
of T (a, b ) is (tab/ 2−t−ab/ 2)(t1/ 2−t−1/ 2)
(ta/ 2−t−a/ 2)(tb/ 2−t−b/ 2)
(see for example [13, Page 119]), we have
lim
N →∞
JN
(
T (a, b ); e2πr √−1/N
)
= 1
∆
(
T (a, b ); e2πr √−1)
if Im r < 0. If Im r > 0 we have
lim
N →∞
log JN
(
T (a, b ); e2πr √−1/N
)
N =
(
1 − 1
2abr − abr
2
)
π
√
− 1.
This completes the proof of Theorem 1.1.
