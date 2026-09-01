---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-006-4-asymptotic-analysis-of-q-deformed-plancherel-g
section_title: "Asymptotic analysis of q-deformed Plancherel growth of second kind"
section_number: 4
pages: 15-17
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
---
In this section, we discuss the growth process controlled by the q-deformed probability
measure considered in [9], given by (2.11). The partition function (3.2) can be written as
Zq =
∞∑
k=1
∑
λk
exp[Seff (hi)]e− lnq
6 N(N−1)(N−2) (4.1)
where the eﬀective action is given by (see Appendix B)
Seff (hi) =k lnt(1−q) +k lnk−k +
∑
i⁄=j
1
2 ln|hi−hj|−
∑
i
(hi lnhi−hi)
+
∑
i⁄=j
1
2 ln|qhj−qhi|−
N∑
i=1
hi∑
j=1
ln(1−qj).
(4.2)
In the continuum limit, the eﬀective action takes the form
Seff [h(x)] =N 2
[
k′ lnt(1−q)N +k′ lnk′−k′−
∫ 1
0
dx (h(x) lnh(x)−h(x))
+1
2
∫ 1
0
dx−
∫ 1
0
dy
(
ln|qNh(x)−qNh(y)| + ln|h(x)−h(y)|
)
−
∫ 1
0
dx
∫ h(x)
0
dy ln(1−qNy )
]
.
(4.3)
In the double scaling limit (3.6), the dominant contribution to the partition function comes
from the conﬁgurations satisfying the saddle point equation
−
∫ hU
hL
dh′u(h′)
[
cothλ(h−h′)
2 + 2
λ(h−h′)
]
= 1 + 2
λ lnh(1−e−λh)
tλk′ (4.4)
where [hL,hU] denotes the support of u(h). Our goal is to ﬁnd a solution of (4.4) for λ⁄= 0.
In order to solve the saddle point equation (4.4), we take the following ansatz for u(h)
u(h) =
{
1 for 0 ≤h≤a
˜u(h) for a≤h≤b. (4.5)
15
The equation of motion (4.4) takes the form
−
∫ b
a
dh′ ˜u(h′)
[
cothλ(h−h′)
2 + 2
λ(h−h′)
]
= 1−a + 2
λ ln
[(h−a)(1−e−λ(h−a))
λξ2
]
. (4.6)
The kernel in the above integral equation is nontrivial. It is diﬃcult to do a change of
variable which brings the kernel to a standard form. However, the coth part of the kernel
has the same singular structure as that of the second part. We therefore expand the coth
part in powers of λ and separate out the singular part. The derivation is given in Appendix
C. To ﬁnd ˜u(h), we again deﬁne a resolvent function as in (3.20). We provide the explicit
calculations for the resolvent in Appendix C. Here, we present the ﬁnal answer.
H(h) = lnh
ξ + ln
√
b−√a√
b +√a
+ lnh +
√
ab−
√
(h−a)(h−b)
h−
√
ab +
√
(h−a)(h−b)
+ λ
4 (1−a) +
∞∑
k=1
A(1)
k
√
(h−a)
(h−b)
+
∞∑
k=1
A(2)
k
2F1(1, 1
2 +k, 2 +k, a−b
a−h)√
(h−a)(h−b)
+
∞∑
k=1
2k−1∑
n=0
A(1)
k,n
√
(h−a)
(h−b)
+
∞∑
k=1
2k−1∑
n=0
A(2)
k,n
2F1(1, 1
2 +n, 2 +n, a−b
a−h)√
(h−a)(h−b)
(4.7)
where Ak’s are given by equation (C.11). Diﬀerent moments, hn (deﬁned in (C.6)) appear
on the right hand side of this expression, which are a priori not known. Hence, the saddle
point equation has to be solved recursively. However, if we calculate the resolvent order by
order in λ, the moments start appearing only at order λ2. The result up to order λ is given
by
H(h) = lnh
ξ + ln
√
b−√a√
b +√a
+ lnh +
√
ab−
√
(h−a)(h−b)
h−
√
ab +
√
(h−a)(h−b)
+ λ
4 (1−h)
+ λ
√
(h−a)(h−b)
4 .
(4.8)
The support of ˜u(h) can be found from the asymptotic behaviour of the resolvent. Up to
ﬁrst order in λ, we get
a = 1− 2ξ +λξ2
2, b = 1 + 2ξ +λξ2
2. (4.9)
and the Young diagram density is given by
˜u(h) = 1
π cos−1
(2h−a−b
b−a
)
− λ
√
(h−a)(b−h)
4π . (4.10)
Since a≥ 0, the above solution is valid for
0<ξ ≤ 1
2 + λ
16. (4.11)
16
˜u(h) given by (4.10) describes the automodel class of [5] corrected up to ﬁrst order in λ. It
is easy to check from equations (3.25) and (4.10) that the order λ correction to automodel
density in both the cases is same apart from a factor of half. The reason behind this is the
appearance of dimλk in (2.11).
The limit shape corresponds to the upper limit of ξ given in (4.11). We plot the limit
shape in a rotated coordinate system (see [1] for coordinate transformation) in ﬁg 5. It is
clear that the symmetric property of the distribution [1] is lost under q deformation.
-2 -1 1 2
u
0.5
1.0
1.5
2.0
2.5
v
Figure 5: The limit shape for a q-deformed (λ = 0.97) Plancherel growth process (green curve) and itsq→ 1
(λ→ 0) limit (orange curve) for comparison.
Thus, we see that both the measures (2.11 and 2.16) qualitatively give the similar asymp-
totic behaviour up to order λ. However, we emphasise that (3.25) is exact in λ.
