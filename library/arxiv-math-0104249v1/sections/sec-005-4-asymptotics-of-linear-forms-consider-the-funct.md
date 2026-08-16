---
doc_id: arxiv-math-0104249v1
doc_title: "IRRA TIONALITY OF V ALUES OF ZET A-FUNCTION W. Zudilin 1. Introduction. The irrationality of values of the zeta-function ζ(s) at odd integers s ≥ 3 is one of the most attractive pr"
section_id: sec-005-4-asymptotics-of-linear-forms-consider-the-funct
section_title: "Asymptotics of linear forms. Consider the functions"
section_number: 4
pages: 4-6
source_pdf: 0104249v1.pdf
source_sha256: c2fcdefc73b8df24
doc_brief: "IRRATIONALITY OF VALUES OF ZETA-FUNCTION W. Zudilin 1. Introduction. The irrationality of values of the zeta-function ζ(s) at odd integers s ≥ 3 is one of the most attractive problems in number theory"
---
cotbz = (−1)b−1
(b − 1)!
db−1 cotz
dzb−1 , b = 1, 2,....
Decomposing π cotπt in a sum of partial fractions we see that for each integer b ≥ 1
πb cotbπt = 1
(t −k)b +O(1) (11)
in a neighbourhood of t =k ∈ Z.
Lemma 2. For the value (4) there holds the integral presentation
I = − 1
2πi
∫ M +i∞
M −i∞
πb cotbπt ·R(t) dt, (12)
whereM ∈ R is an arbitrary positive constant from the interval n<M <cn .
Proof. Consider the integrand in (12) on a rectangle P with vertices M ±iN ,
N + 1
2 ±iN , where an integer N is suﬃciently large, N > cn. Expanding the func-
tion (3) in Taylor series in a neighbourhood of t =k ∈ Z and using the expansion (11)
by Cauchy’s theorem we obtain
1
2πi
∫
P
πb cotbπt ·R(t) dt =
∑
M <k≤N
Rest=k
(
πb cotbπt ·R(t)
)
=
∑
M <k≤N
R(b−1)(k)
(b − 1)! .
(13)
On the sides [N + 1
2 −iN,N + 1
2 +iN ], [M −iN,N + 1
2 −iN ], and [N + 1
2 +iN,M +iN ]
of the rectangle P there holds the relation R(t) = O(N −2), while the function cot bπt,
which is a polynomial in cot πt, is bounded. Hence, tending N to ∞ in (13) we get
the desired presentation (12).
Our next claim follows from Lemma 2 after the change of variab les t =nτ and an
application of Stirling’s formula to gamma-factors of the f unction (3).
IRRATIONALITY OF ZETA-V ALUES 5
Lemma 3. For the sum (4) there holds the asymptotic relation
I = ˜I · (−1)n(2√πn )a+b−bc(2π)b
na−1 ·
(
1 +O(n−1)
)
as n → ∞,
where
˜I = ˜In := − 1
2πi
∫
M
sinbπnτ · cotbπnτ ·enf (τ ) ·g(τ ) dτ, (14)
f (τ ) = (a +b −bc)2 log 2 +b(τ +c) log(τ +c) +b(−τ +c) log(−τ +c)
+ (a +b)(τ − 1) log(τ − 1) − (a +b)(τ + 1) log(τ + 1),
g(τ ) = (τ +c)b/ 2(−τ +c)b/ 2
(τ + 1)(a+b)/ 2(τ − 1)(a+b)/ 2,
and the contour M is a vertical line ℜ(τ ) = µ, 1 < µ < c, oriented from bottom to
top.
We mean the functions f (τ ) and g(τ ) in the complex τ -plane cut along the rays
(−∞, 1] and [c, +∞), where we choose that branches of the logarithm functions, which
we assume to take real values for τ ∈ (1,c ).
For each b ≥ 1 the function sin bz · cotbz is a polynomial in cos z with rational
coeﬃcients:
sinbz · cotbz =Vb(cosz), V b(−y) = ( −1)bVb(y), degVb = max{1,b − 2};
this fact immediately follows from the relations
V1(y) = y, V b+1(y) = yVb(y) + 1
b (1 −y2)V ′
b (y), b = 1, 2,....
Consequently, the integral (14) can be represented in the fo rm
˜I = −
b∑
k=−b
k is odd
ckJn,k, (15)
where ck =c−k are some (rational) constants satisfying c1 = 1 for b = 1, and cb = 0,
cb−2 ⁄= 0 for b> 1;
Jn,λ = 1
2πi
∫
M
en(f (τ )−λπiτ ) ·g(τ ) dτ =Jn, −λ, −b ≤λ ≤b, (16)
and the overline means the complex conjugation. To calculat e asymptotics of the
integrals (16), we apply the saddle point method exchanging the contour of integration
M : ℜ(τ ) = µ by a contour Mλ , which passes through a (unique) saddle point τλ in
such a way that the integrand achieves its maximal value at τλ . Saddle points in the
domain ℜ(τ )> 0 can be determined from the equation
f ′(τ ) = λπi, λ ∈ R. (17)
It follows easily that the polynomial
(τ +c)b(τ − 1)a+b − (τ −c)b(τ + 1)a+b (18)
has at least one real root on the interval ( c, +∞); by µ1 denote such the root nearest
to τ =c.
