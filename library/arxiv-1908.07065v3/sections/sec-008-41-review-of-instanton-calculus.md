---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-008-41-review-of-instanton-calculus
section_title: "Review of instanton calculus"
section_number: 4.1
pages: 21-25
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
---
Let us ﬁrst review some basic ingredients of instanton calculus in the 4d N = 2 SYM with gauge
group G =SU (N) [1, 45–48].
We denote a partition (or Young tableaux) by
Y = (y1,y 2,··· ), (4.2)
its transposed by
Yt = (yt
1,yt
2,··· ), (4.3)
and a vector of Young tableaux as
Y = (Y1,··· ,YN). (4.4)
It is useful to deﬁne
hY (s) =yi−j, v Y (s) =yt
j−i, (4.5)
where s = (i,j ) is a box (not necessarily in the partition Y ). We will also use
𝓁(Y ) =
N∑
I=1
𝓁(YI) , (4.6)
whith
𝓁(Y ) =
∑
i
yi . (4.7)
The four dimensional SU (N) Nekrasov partition function is [45, 47]
Z(a;ϵ1,ϵ 2) =
∑
Y
(
(−1)NΛ2N)𝓁(Y )
ZY, (4.8)
where
ZY =
N∏
I,J =1
∏
s∈YI
1
αI−αJ−ϵ1vYJ (s) +ϵ2 (hYI(s) + 1)
×
∏
s∈YJ
1
αI−αJ +ϵ1 (vYI(s) + 1)−ϵ2hYJ (s),
(4.9)
– 20 –
with
N∑
i=1
αi = 0, (4.10)
and
ai =αi−αi+1, i = 1,··· ,N− 1. (4.11)
The four dimensional SU (N) Nekrasov-Shatashvili (NS) free energy is then deﬁned by [1]
F inst
NS (a, ℏ) = iℏ lim
ϵ2→0
ϵ2 logZ(a; iℏ,ϵ 2). (4.12)
An important property of this free energy is that it is given as a power series in Λ which is
expected to have a non-vanishing radius of convergence in a certain range of values of a and ℏ
around the semiclassical region |Λ/a|≪ 14.
In order to make contact with the (modiﬁed) Mathieu equation, the relevant gauge theory
isN = 2,SU (2) SYM theory, hence we have to consider (4.12) with N = 2. In this case the ﬁrst
few terms read
F inst
NS (a, ℏ) =− 2Λ4
a2 + ℏ2 + Λ8(
7ℏ2− 5a2)
(a2 + ℏ2)3 (a2 + 4ℏ2)
+O
(
Λ16)
. (4.13)
Once the NS free energy is known, the quantum A period a(u, ℏ) can be obtained by inverting
the quantum Matone relation [29, 49–54]
u = a2
8 − Λ
8∂ΛF inst
NS (a, ℏ, Λ). (4.14)
This leads to a series expansion for a(u, ℏ) in powers of Λ 4 which is expected to converge in an
appropriate range of the parameters Λ, E, ℏ around the semiclassical region |Λ2/E|≪ 1. The
quantumB period aD(u, ℏ) is then obtained from the quantum special geometry relation
aD(a, ℏ) =∂aFNS(a, ℏ, Λ) =2γ(a, ℏ, Λ) +∂aF inst
NS (a, ℏ, Λ) (4.15)
where [55]
γ(a, ℏ) = a
2 log
( ℏ2
Λ2
)
− πℏ
4 − iℏ
2
(
log Γ
(
1 + ia
ℏ
)
− log Γ
(
1− ia
ℏ
))
, (4.16)
and we replace a bya(u, ℏ).
We also note that it is possible to express the NS free energy via a TBA system [1, 56]
(diﬀerent from the one discussed in section 3.2). This TBA system however has a range of
validity/convergence which is smaller than the one of the instanton calculus. For instance, the
TBA breaks down if Re( a)⁄= 0, while the instanton counting expression for F inst
NS (4.12) is still
well deﬁned.
4Recall that for ℏ = 0, in the electric frame both a(u) and aD(u) are convergent series of Λ 2/u up to the
monopole and dyon points. The prepotential, which is related to a,aD by the special geometry relation, is thus
also convergent series of Λ /a up to these points. The NS free energy is its smooth deformation which tends to
enlarge the domain of convergence.
– 21 –
It was found in [11] that by expanding (4.13), (4.14) at small values of ℏ, it is possible to
recover the WKB periods (2.22). More precisely, at order ℏ2n, one ﬁnds an expansion in Λ which
agrees with the expansion of Π (n)(E) at large E:
2πa (u, ℏ)−→
∞∑
n=0
ℏ2nΠ(n)
A (E = 2u),
2iaD(a(u, ℏ), ℏ) = 2i∂a(FNS(a, ℏ))
⏐⏐⏐
a=a(u,ℏ)
−→
∞∑
n=0
ℏ2nΠ(n)
B (E = 2u).
(4.17)
Therefore, the Bethe/gauge correspondence provides an analytic way to resum the WKB periods
period into well deﬁned functions which are exact in ℏ. We will denote these functions by
Πex
A,B(E, ℏ), and we will refer to them as “exact” quantum periods. In terms of the quantities
that we have introduced, they are given by
Πex
A (E, ℏ) = 2πa(E, ℏ),
Πex
B (E, ℏ) = 2i∂aFNS(a(E, ℏ), ℏ),
(4.18)
where we use the notation a(E, ℏ) :=a(u =E/2, ℏ).
It turns out that one can ﬁnd the series expansion for a(u, ℏ) by using elementary methods.
To do this, we use the WKB method, but we solve the Riccati equation (2.3) perturbatively in
Λ, i.e. we solve
Y 2(x)− iℏdY (x)
dx =E− 2Λ2 cosh(x) (4.19)
with an ansatz
Y (x) =
∑
n≥0
Yn(x, ℏ,E )Λ2n. (4.20)
Clearly, we should set
Y0(x, ℏ,E ) =
√
E, (4.21)
The equation for Y1(x, ℏ,E ) is
2Y0Y1− iℏdY1
dx =−2 cosh(x). (4.22)
The general solution to this equation is of the form
Y1(x, ℏ,E ) =−4
√
E cosh(x) + 2iℏ sinh(x)
4E + ℏ2 +ce− 2i
√
Ex
ℏ . (4.23)
We note that the term involving the unknown coeﬃcient leads to a non-perturbative eﬀect in ℏ.
We will set it to zero to recover the perturbative series. The general term Yn satisﬁes
2
√
EYn(x, ℏ,E )− iℏdYn
dx +
n−1∑
k=1
Yk(x, ℏ,E )Yn−k(x, ℏ,E ) = 0. (4.24)
This can be integrated order by order, setting to zero non-perturbative terms. We ﬁnd in this
way,
Y2(x, ℏ,E ) =−4E2 + 5Eℏ2 + i
√
Eℏ
(
8E− ℏ2)
sinh(2x) +E
(
4E− 5ℏ2)
cosh(2x) + ℏ4
√
E (E + ℏ2) (4E + ℏ2)2 . (4.25)
– 22 –
The functions Yn(x, ℏ,E ) are complicated, but their integrals are slightly simpler. As it follows
from (2.19), we have to calculate
In(E, ℏ) = 1
2π
∫ π
−π
Yn(ix, ℏ,E )dx. (4.26)
As expected, only even terms contribute. We ﬁnd, for example,
I2(E, ℏ) =− 1
4E3/2 +
√
Eℏ2,
I4(E, ℏ) =− 60E2 + 35Eℏ2 + 2ℏ4
4E3/2 (E + ℏ2) (4E + ℏ2)3,
I6(E, ℏ) =−6720E5 + 18480E4ℏ2 + 15260E3ℏ4 + 4705E2ℏ6 + 413Eℏ8 + 18ℏ10
4E5/2 (E + ℏ2)2 (4E + ℏ2)5 (4E + 9ℏ2)
,
(4.27)
and so on. Then, one ﬁnds
a(E, ℏ) = 2
(
√
E +
∞∑
m=1
I2m(E, ℏ)Λ4m
)
. (4.28)
When ℏ = 0, we recover the standard SW period (2.19):
2πa(E, 0) = 4π
√
2 +E 2F1
(
−1
2, 1
2, 1; 4
2 +E
)
= 8
√
2Λ2 +E E
( 4Λ2
2Λ2 +E
)
. (4.29)
At ﬁnite ℏ, Λ we also ﬁnd perfect agreement between (4.28) and the standard result of instanton
calculus.
We note that the integrals above can be calculated as residues, since
In(E, ℏ) =
∮
|X|=1
Yn(X, ℏ,E )dX
X = ResX=0
Yn(X, ℏ,E )
X , (4.30)
where
X = ex. (4.31)
In fact, it is more convenient to solve the diﬀerential equation directly in the X variable, since
everything is algebraic, i.e. it is better to solve
2
√
EYn(X, ℏ,E )− iℏX dYn
dX (X, ℏ,E ) +
n−1∑
k=1
Yk(X, ℏ,E )Yn−k(X, ℏ,E ) = 0. (4.32)
It turns out that the function Y (ix, ℏ,E ) can be calculated exactly in terms of Mathieu
functions. To see this, we note that Y(x, ℏ,E ) =Y (ix, ℏ,E ) satisﬁes the Riccati equation
Y2(x, ℏ,E )− ℏdY
dx (x, ℏ,E ) =E− 2Λ2 cos(x), (4.33)
which is the Mathieu equation with imaginary Planck constant. The solution to this equation is
Y(x, ℏ,E ) =−ℏ d
dx log
{
S
(
−4E
ℏ2,−4Λ2
ℏ2 ,x
2
)
+cC
(
−4E
ℏ2,−4Λ2
ℏ2 ,x
2
)}
, (4.34)
– 23 –
wherec is an integration constant andS(α,q,x ),C(α,q,x ) are the odd (even) Mathieu functions,
respectively. Since we want
Y(x, ℏ,E )≈
√
E (4.35)
as Λ→ 0, we ﬁnd that this leads to
c =±i (4.36)
(where the sign depends on the branch cut of the square root). We eventually ﬁnd
Πex
A (E, ℏ) = 2
∫ π
−π
Y(x)dx =−2ℏ log
S
(
− 4E
ℏ2,− 4Λ2
ℏ2 , π
2
)
+cC
(
− 4E
ℏ2,− 4Λ2
ℏ2 , π
2
)
−S
(
− 4E
ℏ2,− 4Λ2
ℏ2 , π
2
)
+cC
(
− 4E
ℏ2,− 4Λ2
ℏ2 , π
2
). (4.37)
Note that
Πex
A (E, ℏ) = 2πiℏν
(
−4E
ℏ2,−4Λ2
ℏ2
)
, (4.38)
where ν is the characteristic exponent of the Mathieu equation (this relation has been noted in
the context of the Mathieu equation in e.g. [12, 15]). The advantage of the expressions (4.37),
(4.38) is that they make sense for values ofE for which the Λ expansion (4.28) does not converge,
so they extend (4.28) to a larger domain.
Let us consider some numerical examples. When E = 100, ℏ = 3π and Λ = 1, we can
evaluate the series (4.28) by truncating it up to order Λ 28, and we ﬁnd:
1
4π Πex
A (100, 3π) =−9.9997954179096157891757... (4.39)
This is precisely what is also obtained from (4.37) and (4.38). At the same time, by using (4.37)
we can go all the way to E = 0, where (4.28) cannot be used. We ﬁnd, for example,
1
4π Πex
A (0, 3π) = 0.1501122164563802133431995...i. (4.40)
This procedure for evaluating the value of Π ex
A at E = 0 seems to be well-deﬁned for suﬃciently
large ℏΛ−2 (e.g. ℏΛ−2≥ 1 works).
We conclude that the “exact” quantum A period can be computed either by the expression
given by instanton calculus (or equivalently, by the closely related series (4.28)), or by the expres-
sion (4.38) involving the Mathieu characteristic exponent (4.38). When these two expressions
are both well-deﬁned, they agree, but (4.38) has a larger range of validity. In the case of the
quantumB period, it might be possible to obtain an alternative expression to the one in (4.18),
in terms of inﬁnite Hill determinants, by using results in [57].
