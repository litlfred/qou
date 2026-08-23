---
doc_id: arxiv-math-0405126v1
doc_title: "ASYMPTOTIC BEHAVIORS OF THE COLORED JONES POLYNOMIALS OF A TORUS KNOT"
section_id: sec-002-2-proof
section_title: "Proof"
section_number: 2
pages: 2-4
source_pdf: 0405126v1.pdf
source_sha256: 713498dbe80f7319
doc_brief: "ASYMPTOTIC BEHAVIORS OF THE COLORED JONES POLYNOMIALS OF A TORUS KNOT — W e study the asymptotic behaviors of the colored Jones polyn o- mials of torus knots. Contrary to the works by R. Kashaev, O."
---
When t = e2πr √
−1/N for r ∈ C \ Z, JN
(
T (a, b ); e2πr √−1/N
)
can be given by the
following integral form [11, Lemma 1].
JN
(
T (a, b ), e 2πr √−1/N
)
= Φ a,b,r (N )
∫
C
eN fa,b,r(z)τa,b (z)dz.
Here
Φ a,b,r (N ) := ga,b,r
√
N e−(ab(N 2−1)+a/b +b/a )πr √−1/ (2N )
with ga,b,r :=
√
ab
2π
√
2reπ √−1/ 4 sinh
(
πr √ − 1
) ,
fa,b,r (z) := ab
(
z − z2
2πr √ − 1
)
,
THE COLORED JONES POLYNOMIALS OF A TORUS KNOT 3
τa,b (z) := 2 sinh(az) sinh(bz)
sinh(abz) ,
and C is the line
(2.1) C := {seϕ √−1 |s ∈ R}
with Re
(
r√ − 1e−2ϕ √−1
)
> 0. (We will choose ϕ later.)
Let P be the set of the poles of τa,b (z), that is , we put
P :=
{ kπ √ − 1
ab
⏐
⏐k ∈ Z, a ∤ k, b ∤ k
}
.
We will show that the result follows if r / ∈ R, Re r > 0, and |r|> 1
ab .
Put θ := arg r (− π/ 2 < θ < π/ 2) so that r = |r|eθ√−1. Put also ϕ := θ/ 2 + π/ 4
in (2.1). Note that Re
(
r√ − 1e−2ϕ √−1
)
= Re |r|> 0 and that 0 < ϕ < π/ 2.
Let C′ be the line parallel to C that passes through the point πr √ − 1. (We change
C′ slightly near P to avoid poles of τa,b (z) if necessary.) For a positive number
R, let D+ (D−, respectively) be the segment of the line Re z = R (Re z = − R,
respectively) between C and C′ oriented upward (downward, respectively). We see
that C′ and D± are parameterized as follows.
C′ =
{
se(θ/ 2+π/ 4)√−1 + πr
√
− 1
⏐
⏐
⏐ s ∈ R
}
,
D± =
{
± R + s
√
− 1
⏐
⏐ ± R tan (θ/ 2 + π/ 4) ≤ s ≤ ± R tan (θ/ 2 + π/ 4) + π |r|h(θ)
}
,
where h(θ) := cos θ + sin θ tan(θ/ 2 + π/ 4) Note that C′ crosses the imaginary axis
at π |r|h(θ)√
− 1.
Then by the residue theorem∫
C
eN fa,b,r(z)τa,b (z) dz
=
∫
C ′
eN fa,b,r(z) τa,b (z) dz +
∑
k
Res
(
eN fa,b,r(z)τa,b (z); z = kπ
√
− 1/ (ab)
)
−
∫
D+
eN fa,b,r(z)τa,b (z) dz −
∫
D−
eN fa,b,r(z)τa,b (z) dz,
where Res( F (z); z = ζ) is the residue of F (z) around z = ζ, C (C′, respectively)
is the segment in C (C′, respectively) bounded by D± oriented from left to right,
and k runs over integers that are not multiples of a or b such that kπ √ − 1/ab is
between C and C′, that is, 0 < k < ab |r|h(θ).
Since it is not hard to see that on D±
⏐
⏐
⏐eN fa,b,r(z)
⏐
⏐
⏐ < e abN(c2R2+c1R+c0)
for some ci with c2 < 0 if R is suﬃciently large, and that
|τa,b (z)|=
⏐
⏐(eaz − e−az)
(
ebz − e−bz) ⏐
⏐
|eabz − e−abz|
≤
⏐
⏐e(a+b)z⏐
⏐+
⏐
⏐e(a−b)z⏐
⏐+
⏐
⏐e(b−a)z⏐
⏐+
⏐
⏐e−(a+b)z⏐
⏐
⏐
⏐|eabz| − |e−abz|
⏐
⏐
= e±(a+b)R + e±(a−b)R + e±(b−a)R + e∓(a+b)R
|e±abR − e∓abR| ,
the integrals on D± vanish when R → ∞ . Therefore we have
∫
C
eN fa,b,r(z)τa,b (z) dz
