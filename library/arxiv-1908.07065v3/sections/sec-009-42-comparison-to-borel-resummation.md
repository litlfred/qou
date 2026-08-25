---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-009-42-comparison-to-borel-resummation
section_title: "Comparison to Borel resummation"
section_number: 4.2
pages: 25-29
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
---
We now have two diﬀerent approaches to the calculation of (resummed) quantum periods: on
the one hand, we have the Borel resummation of the all-orders WKB expansion in ℏ2, which is
also calculated by the TBA equations of section 3. On the other hand, instanton calculus gives
a diﬀerent resummation, based on a convergent expansion in Λ, as a function of ℏ. An obvious
question is: what is the precise relation between these two resummations? Since both lead to the
same asymptotic expansion in powers of ℏ, we expect that they will diﬀer in non-perturbative
eﬀects. In this section we will address this issue. Results along these lines have been previously
– 24 –
terms included Borel sum
190 35.40661948105291481767982565157
191 35.40661948105291481767982565 207
gauge theory 35.40661948105291481767982564492
Table 8: Borel sum of quantum A period at u = 4 and ℏ = 1. Underlined are stabilised digits.
obtained in [15, 16]. For simplicity, we will restrict ourselves to the case in which ℏ> 0 and u is
real.
Let us ﬁrst consider the weak coupling region W. Here, the all-orders WKB quantum A
period is Borel summable for ℏ real, and we ﬁnd that its Borel sum agrees well with 2 πa(u, ℏ)
obtained by inverting (4.14) or with the solution (4.37) to the Riccati equation, i.e.
s(ΠA)(E, ℏ) = Πex
A (E, ℏ), |u|> 1, ℏ> 0. (4.41)
We illustrate this in Table 8 where we compare the Borel sum of the WKB quantum A period
at u = 4 and ℏ = 1, with increasing number of corrections, to the result of instanton calculus.
They agree with almost all the stabilised digits (27 of them).
The quantum B period, on the other hand, is not Borel summable along the real axis in
the weak coupling region. Nevertheless, we can make the following observation. The “exact”
quantumB period is given by
2iaD(u, ℏ) = 4iγ(a, ℏ) + 2i∂aF inst
NS (a, ℏ) (4.42)
where γ is deﬁned in (4.16) and has the following asymptotic expansion for large a/ℏ:
γ(a, ℏ)∼a
(
log
(a
Λ
)
− 1
)
+a
∑
n≥1
(−1)nB2n
2n(2n− 1)
( ℏ
a
)2n
. (4.43)
The series in ℏ/a in the r.h.s. is not Borel summable along the positive real axis. More precisely,
let us consider the following formal power series:
ϕ(z) =
∑
n≥0
cnz2n, c n−1 = (−1)nB2n
2n(2n− 1). (4.44)
A little numerical experimentation shows that the lateral resummations of this series along the
positive real axis are given by
s±(ϕ)(z) =f(z)± i
2z log
(
1− e−2π/z
)
, (4.45)
where
f(z) = 1
z2 (log(z) + 1)− π
4z− i
2z log Γ(1 + i/z)
Γ(1− i/z). (4.46)
(A similar series has been considered in [55]).
The above analysis suggests that the non-Borel summability of the sequence Π (n)
B along the
positive real axis in the weak coupling region is due to the asymptotic series appearing in γ(a, ℏ).
In view of (4.45), this leads to the right discontinuity across the positive real axis:
− 4ℏ log(1− e−4πa/ℏ). (4.47)
– 25 –
-50 50
-50
50
Figure 4: Poles of the Borel–Pad´ e transform of the “reduced” series Πred
B at u = 4.
This suggests that the “reduced” formal power series
Πred
B (E, ℏ) := ΠB(E, ℏ)− 4iΠA(E, ℏ)
∑
n≥1
(−1)nB2n
2n(2n− 1)
( ℏ
2ΠA(E, ℏ)
)2n
, (4.48)
where we subtract the non-Borel summable series in the function γ(a, ℏ), is actually Borel
summable along the positive real axis. We veriﬁed numerically that this indeed is true, as
can be seen from the Borel plane plot at u = 4 given in Figure 4. In fact the Borel sum of
Πred
B (E, ℏ) agrees with the gauge theory calculation in which the contribution of γ(a, ℏ) has been
removed; in other words,
s
(
Πred
B
)
(E, ℏ) = 2iared
D (u, ℏ) := 4ia
(
log
(a
Λ
)
− 1
)
+ 2i∂F inst
NS (a, ℏ)
∂a . (4.49)
We illustrate this in Table 9, where both the Borel sum of Πred
B (E, ℏ) and 2iared
D (u, ℏ) are evaluated
at u = 4 and ℏ = 1. We ﬁnd that all stabilised digits are in agreement (26 of them) 5.
We can now see a clear diﬀerence between the TBA equations of [1] and the TBA equations
of [5]. The TBA equations of [1] compute the Borel-summable part of the B period, where
we have removed the perturbative contribution due to the γ function, i.e. they compute (4.49),
which is the Borel resummation of Π red
B in (4.48). On the contrary, the conformal limit of the
GMN TBA equations computes the Borel resummation of the full quantumB period ΠB(E, ℏ),
including the perturbative γ function. Since the latter is not Borel summable, the corresponding
TBA has discontinuities, as discussed in section 3.2.
In the strong coupling region we have the following relation between the “exact” quantum
A period and lateral Borel resummations of quantum periods [15]
2 cosh(Πex
A/(2ℏ)) = e
1
2ℏs+(ΠA) + e
1
2ℏs+(ΠA+2ΠB) + e− 1
2ℏs+(ΠA+2ΠB)
= e
1
2ℏs−(ΠA) + e− 1
2ℏs−(ΠA) + e
1
2ℏs−(ΠA+2ΠB) .
(4.50)
5We also notice that the exact B period Π ex
B (E, ℏ) with E >2 agrees with the average of lateral Borel resum-
mations of the quantum B period ΠB(E, ℏ).
– 26 –
terms
Πred
B
159 16.474810551500808917635392219
161 16.474810551500808917635392 368
2iared
D
14 16.47481055150080891763539232909
15 16.474810551500808917635392329 20
Table 9: Comparison between the Borel sum of the “reduced” quantum B period Πred
B atu = 4
and ℏ = 1 (with increasing number of terms), and the exact, “reduced” period 2i ared
D deﬁned in
(4.49) (with increasing number of instanton corrections). Underlined are stabilised digits.
terms ﬁrst line of r.h.s. of (4.50)
191 806502 .11499751621351505261143
193 806502 .11499751621351505261260
l.h.s. of (4.50) 806502 .11499751621351505261016
Table 10: Numerical veriﬁcation of the characteristic exponent formula (4.50) at u = 0 and
ℏ = 1/4, with increasing number of terms for the lateral Borel resummations on the r.h.s.. All
the stabilised digits (underlined) are in agreement.
Numerical evidence for this relation is presented in Table 10 for the ﬁrst line of the formula,
evaluated at u = 0 and ℏ = 1/4. The second line of (4.50) can be derived from the Stokes
automorphism of quantum periods discussed in section 3.2. In the strong coupling region, Π D =
ΠB + ΠA is Borel summable along the positive real axis, while both the Borel resummations of
ΠB and ΠA have discontinuities across the positive real axis. The discontinuities for the B, and
A periods are:
s+(ΠB)−s−(ΠB) = 2ℏ log(1 + e− 1
ℏs(ΠD)) ,
s+(ΠA)−s−(ΠA) =−2ℏ log(1 + e− 1
ℏs(ΠD)) .
(4.51)
Starting from the ﬁrst line on the right hand side of (4.50), and applying the discontinuity
formulae, we immediately get the second line
ﬁrst line
= e
1
2ℏs+(ΠA) + e
1
2ℏs+(ΠA+2ΠB) + e− 1
2ℏs+(ΠA+2ΠB)
= e
1
2ℏs−(ΠA)
(
1 + e− 1
ℏs(ΠD)
)−1
+ e
1
2ℏs−(ΠA+2ΠB)
(
1 + e− 1
ℏs(ΠD)
)
+ e− 1
2ℏs−(ΠA+2ΠB)
(
1 + e− 1
ℏs(ΠD)
)−1
=
(
e
1
2ℏs−(ΠA) + e− 1
2ℏs−(ΠA+2ΠB)
)(
1 + e− 1
ℏs(ΠD)
)−1
+ e
1
2ℏs−(ΠA+2ΠB) + e− 1
2ℏs−(ΠA)
= e
1
2ℏs−(ΠA) + e− 1
2ℏs−(ΠA) + e
1
2ℏs−(ΠA+2ΠB) = second line . (4.52)
On the other hand, to derive a similar result for the “exact” quantumB period we can use results
on the Fredholm determinant of the modiﬁed Mathieu equation, which we present in section 5.
– 27 –
Eq.(5.44) then together (4.50) imply that
2 sinh(Πex
B/(2ℏ)) = e
1
2ℏs+(ΠB)− e− 1
2ℏs+(ΠB)− e− 1
2ℏs+(2ΠA+3ΠB),
= e
1
2ℏs−(ΠB)− e− 1
2ℏs−(ΠB) + e− 1
2ℏs−(2ΠA+ΠB) ,
(4.53)
and we have tested these identities numerically to very high precision.
Summarizing, in the weak coupling region the all-orders WKB quantum A period and the
B period (once the gamma function is subtracted) are Borel summable. Their Borel sums agree
with the gauge theory expressions of section 4.1. In the strong coupling region, the A and B
periods are not Borel summable, although their lateral Borel resummations can be related to
the exact quantum A period via (4.50). We ﬁnally note that the combination Π D = ΠA + ΠB
is Borel summable in the strong coupling region (only). However, its Borel sum does not agree
with the gauge theory expression of section (4.1), namely
s(ΠD)⁄= Πex
A + Πex
B = 2πa + 2iaD, (4.54)
and one should include additional non-perturbative corrections. We will ﬁnd the correct formula
at the end of section 5.3.
