---
doc_id: arxiv-1105.1998v3
doc_title: "A Connection Formula of the Hahn-Exton q-Bessel Function"
section_id: sec-004-3-the-limit-of-the-connection-formula
section_title: "The limit of the connection formula"
section_number: 3
pages: 6-11
source_pdf: 1105.1998v3.pdf
source_sha256: daf3bffad8eb2749
doc_brief: "A Connection Formula of the Hahn-Exton q-Bessel Function — We show a connection formula of the Hahn–Exton q-Bessel function around the origin and the infinity."
---
In this section, we show that the limit p → 1− of the connection formula gives a connection
formula of the Bessel function. At first, we assume that 0 < p < 1 and 0 < √
p < 1. For the
Bessel function, we set the Hankel function of the first and t he second kind H (1)
ν (z) and H (2)
ν (z).
Deﬁnition 3. The Hankel function of the first kind is given by
H (1)
ν (z) := Γ
(1
2 − ν
)
πi √π
(z
2
)ν∫ (1+)
1+∞ i
eizt(
t2 − 1
)ν− 1
2 dt, −π < arg z < 2π.
The Hankel function of the second kind is defined by
H (2)
ν (z) := Γ
(1
2 − ν
)
πi √π
(z
2
)ν∫ (− 1− )
− 1+∞ i
eizt(
t2 − 1
)ν− 1
2 dt, −2π < arg z < π.
The contour for H (1)
ν (z) is a path starting from t = +1 + ∞i, rounding the circle around
t = 1 counterclockwise, and going back to t = +1 + ∞i. Moreover, the contour for H (2)
ν (z) is
a path starting from t = −1 + ∞i, rounding the circle around t = 1 clockwise, and going back
to t = −1 + ∞i.
The Hankel functions can be written by Jν (z):
H (1)
ν (z) = ie− νπi
sin νπ
{
Jν (z) − eνπi J− ν (z)
}
, (8)
H (2)
ν (z) = − ieνπi
sin νπ
{
Jν (z) − e− νπi J− ν (z)
}
. (9)
The Hankel functions have asymptotic expansions around z = 0 [4]:
H (1)
ν (z) ∼
( 2
πz
)1
2
eiζ∑
s≥ 0
is As(ν)
zs , −π + δ ≤ arg z ≤ 2π − δ,
H (2)
ν (z) ∼
( 2
πz
)1
2
e− iζ∑
s≥ 0
(−i)s As(ν)
zs , −2π + δ ≤ arg z ≤ π − δ,
as z → ∞. Here, δ is an any small constant,
As(ν) = (4ν2 − 12)(4ν2 − 32) · · ·
{
4ν2 − (2s − 1)2}
s!8s
and
ζ = z − 1
2 νπ − 1
4 π.
In this sense, (8) and (9) considered as connection formula o f the Bessel equation.
A Connection Formula of the Hahn–Exton q-Bessel Function 7
3.1 Limit of the connection formula
We rewrite the connection formula in Theorem 1 in order to tak e a limit p → 1− . We set new
functions hν (t; p) and J ±
ν (x; p). We set hν (t; p) := ( p1/ 2, p 1/ 2; p)∞ z(t). For any x ∈ C∗ \ [−λ; p]
and λ ∈ C∗, J +
ν,λ (x; p) is
J +
ν,λ (x; p) := (pν+1; p)∞
(p; p)∞
θp
(
λp ν
x
)
θp
(λ
x
) 1ϕ 1
(
0; p1+2ν ; p, x
)
.
Similarly, J −
ν,λ (x; p) is
J −
ν,λ (x; p) := (pν+1; p)∞
(p; p)∞
θp
(
λp ν
x
)
θp
(λ
x
) 1ϕ 1
(
0; p1+2ν ; p, p 2ν x
)
.
We remark that the function θp(λp ν /x )/θ p(λ/x ) satisfies the following q-difference equation
u(px) = pν u(x),
which is also satisfied by the function u(x) = xν . We remark that the pair ( J +
ν,λ (x; p), J −
− ν,λ (x; p))
gives a fundamental system of solutions of equation (6) if ν ⁄∈Z. We set the function C +
ν (λ, t ; p)
and C −
ν (λ, t ; p) as follow:
Deﬁnition 4. For any λ ∈ C∗, C +
ν (λ, t ; p) is
C +
ν (λ, t ; p) := (p
1
2 , p
1
2 ; p)∞
(pν+1, p − 2ν ; p)∞
θp(−p2ν+2t)
θp(−pν+2t)
θp(λt)
θp(λp ν t) .
Similarly, the function C −
ν (λ, t ; p) is
C −
ν (λ, t ; p) := (p
1
2 , p
1
2 ; p)∞
(p− ν+1, p 2ν ; p)∞
θp(−p2t)
θp(−pν+2t)
θp(λt)
θp(λp − ν t) .
Then, C +
ν (λ, t ; p) and C −
ν (λ, t ; p) are single valued as a function of t. The function C +
ν (λ, t ; p)
and C −
ν (λ, t ; p) are the p-elliptic functions. By using these new functions, our conn ection formula
is rewritten by
hν
(1
x ; p
)
= C +
ν
(
λ, 1
x ; p
)
J +
ν (x; p) + C −
ν
(
λ, 1
x ; p
)
J −
− ν,λ (x; p).
Theorem 2. For any x ∈ C∗ \ (−∞, 0] where arg x ∈ (−π, π ), we have
lim
p→ 1−
hν
( 1
(1 − p)2x ; p
)
= −ie− νπi H (2)
2ν (2√x).
Here, H (2)
2ν (·) is the Hankel function of the second kind.
The aim of this section is to give a proof of the theorem above.
By the definition, hν
(
1/ {(1 − p)2x}; p
)
can be described as follows
hν
( 1
(1 − p)2x ; p
)
=
{
(p
1
2 , p
1
2 ; p)∞
(p− 2ν , p ; p)∞
(1 − p)2ν
} 


θp
(
− p2ν +2
x(1− p)2
)
θp
(
− pν +2
x(1− p)2
)(1 − p)− 2ν


 .
×
{
1ϕ 1
(
0; p1+2ν ; p, (1 − p)2x
)}
8 T. Morita
+
{
(p
1
2 , p
1
2 ; p)∞
(p2ν , p ; p)∞
(1 − p)− 2ν
} 


θp
(
− p2
x(1− p)2
)
θp
(
− pν +2
x(1− p)2
)(1 − p)2ν



×
{
1ϕ 1
(
0; p1− 2ν ; p, p − 2ν (1 − p)2x
)}
. (10)
We consider the limit of each part {·}.
Lemma 4. For any ν ∈ C∗ \ Z, we have
lim
p→ 1−
(p
1
2 , p
1
2 ; p)∞
(p− 2ν , p ; p)∞
(1 − p)2ν = − 1
sin(2νπ )Γ(2 ν + 1) .
Proof . We can check out as follows
(p
1
2 , p
1
2 ; p)∞
(p− 2ν , p ; p)∞
(1 − p)2ν =
(p;p)∞
(p− 2ν ;p)∞
(1 − p)1+2ν
{
(p;p)∞
(p
1
2 ;p)∞
(1 − p)
1
2
}{
(p;p)∞
(p
1
2 ;p)∞
(1 − p)
1
2
} = Γ p(−2ν)
Γ p
(1
2
)
Γ p
(1
2
).
Here, Γ q(·) is Jackson’s q-gamma function which is defined by
Γ q(x) := (q; q)∞
(qx; q)∞
(1 − q)1− x, 0 < q < 1.
This function satisfies lim
q→ 1−
Γ q(x) = Γ( x) [2]. Therefore,
lim
p→ 1−
(p
1
2 , p
1
2 ; p)∞
(p− 2ν , p ; p)∞
(1 − p)2ν = Γ( −2ν)
Γ
(1
2
)
Γ
(1
2
).
By Euler’s reflection formula of the gamma function, we get
Γ( −2ν)
Γ
(1
2
)
Γ
(1
2
)= − 1
sin(2νπ )Γ(2 ν + 1) .
Therefore, we get the conclusion. ■
If we replace ν by −ν, we get the limit
lim
p→ 1−
(p
1
2 , p
1
2 ; p)∞
(p2ν , p ; p)∞
(1 − p)− 2ν = 1
sin(2νπ )Γ(1 − 2ν) .
In [8], the following proposition can be found:
Proposition 1. For any x ∈ C∗ (−π < arg x < π ), we have
lim
p→ 1−
θp
(
pν 1
(1− p2)x
)
θp
(
pν 2
(1− p2)x
)(
1 − p2)ν2− ν1
= xν1− ν2,
and
lim
p→ 1−
θp
(
− pν 1
(1− p2)x
)
θp
(
− pν 2
(1− p2)x
)(
1 − p2)ν2− ν1
= (−x)ν1− ν2.
A Connection Formula of the Hahn–Exton q-Bessel Function 9
Lemma 5. For any x ∈ C∗ (−π < arg x ≤ π ) and ﬁxed constant K, we have
θp(−√p)θp
(
− K
x
)
= θ√ p
(√
K
x
)
θ√ p
(
−
√
K
x
)
.
Proof . From Jacobi’s triple product identity and ( a2; q2)n = (a, −a; q)n, we obtain
(√p; √p)∞
(−√p; √p)∞
θp
(
− K
x
)
= θ√ p
(√
K
x
)
θ√ p
(
−
√
K
x
)
.
We remark that ( √p; √p)∞ / (−√p; √p)∞ can be rewritten as follows [2]:
(√p; √p)∞
(−√p; √p)∞
=
∑
n∈ Z
(−1)n(√p)n2
= θp(−√p).
We obtain the conclusion. ■
Therefore, we obtain the following relation.
Corollary 1. For any x ∈ C∗ (−π < arg x ≤ π ), we have
θp
(
p2ν+2 − 1
(1− p)2x
)
θp
(
pν+2 − 1
(1− p)2x
) =
θ√ p
(
pν+1 1
(1− p)√ x
)
θ√ p
(
pν+1 − 1
(1− p)√ x
)
θ√ p
(
p
ν
2 +1 1
(1− p)√ x
)
θ√ p
(
p
ν
2 +1 − 1
(1− p)√ x
) (11)
and
θp
(
p2 − 1
(1− p)2x
)
θp
(
pν+2 − 1
(1− p)2x
) =
θ√ p
(
p 1
(1− p)√ x
)
θ√ p
(
p − 1
(1− p)√ x
)
θ√ p
(
p
ν
2 +1 1
(1− p)√ x
)
θ√ p
(
p
ν
2 +1 − 1
(1− p)√ x
). (12)
We consider the limit p → 1− (i.e., √p → 1− ) of (11) and (12).
Lemma 6. For any x ∈ C∗ \ (−∞, 0] ( −π < arg x ≤ π ), we have
1. lim
p→ 1−
θp
(
− p2ν +2
x(1− p)2
)
θp
(
− pν +2
x(1− p)2
)(1 − p)− 2ν = eνπi xν and
2. lim
p→ 1−
θp
(
− p2
x(1− p)2
)
θp
(
− pν +2
x(1− p)2
)(1 − p)2ν = e− νπi x− ν .
Proof . Combining Proposition 1 and Corollary 1, we consider the lim it √p → 1− as follows:
θp
(
p2ν+2 − 1
(1− p)2x
)
θp
(
pν+2 − 1
(1− p)2x
)(1 − p)− 2ν =
θ√ p
(
pν+1 1
(1− p)√ x
)
θ√ p
(
pν+1 − 1
(1− p)√ x
)
θ√ p
(
p
ν
2 +1 1
(1− p)√ x
)
θ√ p
(
p
ν
2 +1 − 1
(1− p)√ x
)(1 − p)− 2ν
=



θ√
p
(
(√p)2ν+2 1
(1− (√ p)2)√ x
)
θ√ p
(
(√p)ν+2 1
(1−{ √ p)2)√ x
){
1 − (√p)2} − ν



×



θ√
p
(
−(√p)2ν+2 1
(1− (√ p)2)√ x
)
θ√ p
(
−(√p)ν+2 1
(1−{ √ p)2)√ x
){
1 − (√p)2} − ν



→ (√
x)ν · (−√x)ν = (−x)ν = eνπi xν , √p → 1− .
Similarly, we can prove the latter one. We obtain the conclus ion. ■
10 T. Morita
We consider the last part.
Lemma 7. For any x ∈ C∗, we have
lim
p→ 1− 1ϕ 1
(
0; p1+2ν ; p, (1 − p)2x
)
= 0F1 (−, 1 + 2ν; −x)
and
lim
p→ 1− 1ϕ 1
(
0; p1− 2ν ; p, p − 2ν (1 − p)2x
)
= 0F1 (−, 1 − 2ν; −x) .
Proof . We check each of the term of
1ϕ 1
(
0; p1+2ν ; p, (1 − p)2x
)
=
∑
n≥ 0
1
(p1+2ν , p ; p)n
(−1)np
n(n− 1)
2
{
(1 − p)2x
} n
.
For any n ≥ 0,
1
(p1+2ν , p ; p)n
(−1)np
n(n− 1)
2
{
(1 − p)2x
} n
= (1 − p)n(1 − p)n
(p1+2ν ; p)n(p; p)n
p
n(n− 1)
2 (−x)n → 1
(1 + 2ν)n · n! (−x)n , p → 1− .
Summing up all terms, we get
∑
n≥ 0
1
(1 + 2ν)n · n! (−x)n = 0F1 (−, 1 + 2ν; −x) .
Therefore, we obtain the conclusion. Similarly, we can prov e the latter. ■
We give the proof of Theorem 2.
Proof . Apply Lemma 4, Lemma 6 and Lemma 7 to (10), we obtain
hν
( 1
(1 − p)2x ; p
)
→
{
− 1
sin(2νπ )Γ(1 + 2 ν)
}
eνπi xν 0F1 (−, 1 + 2ν; −x)
+
{ 1
sin(2νπ )Γ(1 − 2ν)
}
e− νπi x− ν 0F1 (−, 1 − 2ν; −x)
= −eνπi J2ν (2√x) + e− νπi J− 2ν (2√x)
sin(2νπ )
= e− νπi
i H (2)
2ν
(
2√x
)
, p → 1− .
Therefore, we acquire the conclusion. ■
Acknowledgements
The author would like to express his deepest gratitude to Pro fessor Yousuke Ohyama for many
valuable comments. The author also expresses his thanks to P rofessor Lucia Di Vizio for fruitful
discussions when she was invited to the University of Tokyo i n the winter 2011. The author
would like to give thanks to the referee for some useful comme nts.
A Connection Formula of the Hahn–Exton q-Bessel Function 11
