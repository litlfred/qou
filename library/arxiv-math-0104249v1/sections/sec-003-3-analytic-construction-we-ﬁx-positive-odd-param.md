---
doc_id: arxiv-math-0104249v1
doc_title: "IRRA TIONALITY OF V ALUES OF ZET A-FUNCTION W. Zudilin 1. Introduction. The irrationality of values of the zeta-function ζ(s) at odd integers s ≥ 3 is one of the most attractive pr"
section_id: sec-003-3-analytic-construction-we-ﬁx-positive-odd-param
section_title: "Analytic construction. We ﬁx positive odd parameters a,b,c such thatc ≥ 3,"
section_number: 3
pages: 2-4
source_pdf: 0104249v1.pdf
source_sha256: c2fcdefc73b8df24
doc_brief: "IRRATIONALITY OF VALUES OF ZETA-FUNCTION W. Zudilin 1. Introduction. The irrationality of values of the zeta-function ζ(s) at odd integers s ≥ 3 is one of the most attractive problems in number theory"
---
a>b (c − 1), and for each positive integer n consider the rational function
R(t) = Rn(t) :=
(
(t ± (n + 1)) · · ·(t ±cn)
) b
(
t(t ± 1) · · ·(t ±n)
) a · (2n)!a+b−bc
= (−1)n ·
( sinπt
π
) b
· Γ( ±t +cn + 1)bΓ(t −n)a+b
Γ(t +n + 1)a+b · (2n)!a+b−bc,
(3)
where the record ‘ ±’ means that the product contains factors corresponding bot h to
a sign ‘+’ and to a ‘ −’. To the function (3) assign the inﬁnite sum
I =In :=
∞∑
t=n+1
1
(b − 1)!
db−1R(t)
dtb−1 ; (4)
the series on the right-hand side of (4) converges absolutel y since R(t) = O(t−2) as
t → ∞ . Decomposing the function (3) in a sum of partial fractions a nd using its
oddness, we deduce that
I =
∑
s is odd
b<s<a+b
Asζ(s) −A0 (5)
(see (10) below), where denominators of the rational number s As = As,n grow not
faster than exponentially (cf. [R1], lemmes 1, 5). By Dn denote the least common
multiple of numbers 1 , 2,...,n ; the prime number theorem yields
lim
n→∞
logDn
n = 1.
IRRATIONALITY OF ZETA-V ALUES 3
Lemma 1. For each odd integer c ≥ 3 there exists a sequence of integers Π n =
Π n,c ≥ 1, n = 1, 2,... , such that the numbers Π −b
n Da+b−1
2n As,n are integral and the
limit relation
̟c := lim
n→∞
log Π n,c
n = −
(c−1)/ 2∑
l=1
(
2ψ
( 2l
c − 1
)
+ 2ψ
( 2l
c
)
+ 2c − 1
l
)
+ 2(c − 1)(1 −γ)
(6)
holds; here γ ≈ 0.57712 is Euler’s constant and ψ(x) is the logarithmic derivative of
the gamma-function.
Proof. Let
Π n =
∏
√
(c+1)n<p≤2n
pν p, where νp = min
k=0, ±1,..., ±n
{
ordp
(cn +k)! (cn −k)!
(n +k)!c(n −k)!c
}
.
(7)
Then for rational functions
G(t) = Gn(t) := (t ± (n + 1)) · · ·(t ±cn)
(
t(t ± 1) · · ·(t ±n)
) c−1, H (t) = Hn(t) := (2n)!
t(t ± 1) · · ·(t ±n)
we have the inclusions
Π −1
n · Dj
2n
j!
dj
dtj
(
G(t)(t +k)c−1) ⏐
⏐
⏐
⏐
t=−k
∈ Z, Dj
2n
j!
dj
dtj
(
H(t)(t +k)
) ⏐
⏐
⏐
⏐
t=−k
∈ Z,
k = 0, ±1,..., ±n, j = 0, 1, 2,...
(8)
(a proof of the inclusions (8) for the function G(t) needs a certain generalization of
the arithmetic scheme of Nikishin–Rivoal). Now, represent ing the initial function (3)
in the form R(t) = G(t)bH(t)a+b−bc and applying Leibniz’s rule for the diﬀerentiation
of a product, by (8) we obtain
Π −b
n Dj
2nBk,j ∈ Z, where Bk,j = 1
j!
dj
dtj
(
R(t)(t +k)a) ⏐
⏐
⏐
⏐
t=−k
,
k = 0, ±1,..., ±n, j = 0, 1,...,a − 1.
(9)
These relations yield the desired inclusions Π −b
n Da+b−1
2n As ∈ Z since
As = (−1)b−1
( s − 1
b − 1
) n∑
k=−n
Bk,a +b−s−1, s is odd, b<s<a +b,
A0 = (−1)b−1
n∑
k=−n
k+n∑
l=1
(( a +b − 2
b − 1
) Bk, 0
la+b−1 + · · · +
( b
b − 1
) Bk,a −2
lb+1 + Bk,a −1
lb
)
.
(10)
By (7), for each prime number p>
√
(c + 1)n there holds
νp = min
|k|≤n
ϕc
( n
p,k
p
)
,
