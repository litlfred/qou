---
doc_id: arxiv-2602.15276v1
doc_title: "Compact Q-balls and Q-shells within aCP N Skyrme-Faddeev type model"
section_id: sec-003-energy-density
section_title: "Energy density"
section_number: null
pages: 9-12
source_pdf: 2602.15276v1.pdf
source_sha256: 18d77d6aa140fc50
doc_brief: "Compact Q-balls and Q-shells within aCP N Skyrme-Faddeev type model — 11 sections: Introduction; The Lagrangian and Euler-Lagrange ; Radial reduction"
---
A crucial prerequisite for constructing physically meaningful solutions is ensuring the positive
definiteness of the energy density. Given that the Lagrangian for this model comprises multiple
terms connected by various coupling constants, it is essential to guarantee a non-negative energy
density across all configurations before proceeding to the derivation of solutions for specific param-
eter values. Consequently, the focus of the following section is a detailed analysis of the model’s
energy density.
The dimensionless Hamiltonian density, eH:=r 4
0H, is conventionally defined via the Legendre
transformation:
eH=
lX
m=−l
 
δeL
δ(∂tum)∂tum + δeL
δ(∂tu∗m)∂tu∗
m
!
− eL.(II.15)
Given the structure of the Lagrangian density, where its variation with respect to the derivative-
coupling-tensor isδ eL=− 1
2
˜Cµνδτνµ, the Hamiltonian density can be formally expressed using the
components involving time derivatives as:
eH=− eCµtτtµ− eCtµτµt− eL.(II.16)
For the field configuration defined by the ansatz (II.13), the dimensionless Hamiltonian density
eHcan be expressed in terms of the non-zero components of the derivative-coupling-tensorτ µν(ξ)
and the coefficient tensor eCµν(ξ) as:
eH=−2[ ˜Cttτtt + eCtrτtr]− ˜L(II.17)
where the full dimensionless Lagrangian density eLis:
eL=− 1
2
h
τtt−τrr− 2
r2τθθ + eCttτtt + eCrrτrr + 2eCtrτtr + 2
r4
eCθθτθθ
i
.
The dimensionless Hamiltonian density eHnaturally decomposes into a quadratic part ( eH02) and a
quartic part (eH4), such that eH= eH02 + eH4. The part of the Hamiltonian density originating from
10
the quadratic terms is given by:
eH02 = 4ω2f 2
(1 +f 2)2 + l(l+ 1)
r2
4f 2
1 +f 2 + 4f′2
(1 +f 2)2 + ˜µ2V.(II.18)
The portion of the Hamiltonian density arising from the quartic interactions is initially expressed
as:
eH4 =κ
"
6ω2f 2
(1 +f 2)2F1(r)− 2f′2
(1 +f 2)2F2(r)
+ 12ω2f′f
(1 +f 2)2F3(r)− l(l+ 1)
r2
2f 2
1 +f 2F4(r)
#
.(II.19)
By substituting the explicit forms of the functionsF n(r) into the above expression, the quartic
Hamiltonian density eH4 is obtained in the fully expanded form:
eH4 =−κ
"
−2
0
z }| {
(βe2 + 2γe2) 3ω4f 2−f′4
(1 +f 2)4
+ 4(βe2−4) ω2f 2f′2
(1 +f 2)4
+ 4(βe2−1) l(l+ 1)
r2
f 2(ω2f 2 +f′2)
(1 +f 2)3
+ (2βe2 + 2γe2−1)| {z }
βe2−1
l2(l+ 1) 2
r4
f 4
(1 +f 2)2
#
.(II.20)
The total energyEof the field configuration is determined by integrating the dimensionless Hamil-
tonian density over the volume, incorporating the √−gfactor for volume element transformation
(which simplifies tor 2 sinθin spherical coordinates):
E=
Z
R3
d3ξ√−g

eH02 + eH4

= 4π
Z ∞
0
drr 2

eH02 + eH4

.
Following our previous analysis of the extended Skyrme-Faddeev model [13], we assume that
e2 <0 andM 2 >0. The Hamiltonian density of the quadratic terms, eH02 (Equation (II.18)), is
inherently positive definite due to its structure. Upon examining the full Hamiltonian density eH
(Equation (II.16)), specifically the quartic contributioneH4 (Equation (II.20)), we observe that most
terms contribute positively to the energy density under the following constraints on the coupling
constants:
2βe2 + 2γe2−1≥0,andβe 2−4≥0.(II.21)
The only term in eH4 that is not intrinsically guaranteed to be positive definite is the one pro-
portional to the combination of coupling constantsβe 2 + 2γe2. To definitively ensure the overall
positive definiteness of the total Hamiltonian density eH, we impose the strong constraint:
βe2 + 2γe2 = 0.(II.22)
11
This condition not only nullifies the potentially negative term but also simplifies the combination
of coupling constants appearing in the last term of Equation (II.20) from (2βe 2 + 2γe2−1) to
βe2−1.
The parameter space defined by the constraints (II.21) andβe2+2γe2≤0 is visually represented
in FIG. 1. The upper boundary of this region, which is demarcated by the red line, corresponds
precisely to the equality condition established in Equation (II.22) (βe 2 +2γe 2 = 0). This boundary
line represents the specific combination of coupling constants that guarantees a positive definite
contribution of the quartic terms to the total energy density.
Notably, within the regime wheree 2<0, the requirement for positive definiteness imposes
constraints on the coupling constants such thatβ <0 (which impliesβe 2 >0) andγ >0 (which
impliesγe 2 <0). Below the upper boundary (the red line)–that is, forβe 2 + 2γe2<0?solutions
with a non-negative energy density may still be permissible, provided that the additional condition
3ω4f 2>f′4 is locally satisfied.
FIG. 1. The coupling constant space delimited by the conditionsβe 2 + 2γe2≤0, 2βe 2 + 2γe2−1≥0, and
βe2−4≥0, ensuring a non-negative contribution from the quartic terms.
By applying these constraints (βe 2 + 2γe2 = 0,e 2<0,M 2>0), the radial equation of motion
(Equation (II.12)) is simplified and can be expressed in the form:
f′′ + 2
rf′ +

ω2 1−f 2
1 +f 2− l(l+ 1)
r2

f− 2ff′2
1 +f 2
− ˜µ2
8 sgn(f)
p
1 +f 2 +κG(r) = 0.(II.23)
Here, the functionG(r) represents the non-linear contributions resulting from the quartic terms
and is defined as:
12
G(r) =−(βe 2 + 2γe2)| {z }
0
1
(1 +f 2)2
"
3f′2f′′ + 2
rf′3− 6ff′4
1 +f 2−ω 4 (1−f 2)f 3
1 +f 2
#
−(βe 2−1) l(l+ 1)
r2
1
1 +f 2
"
f 2f′′ + (1−2f 2)ff′2
1 +f 2 +ω 2 (2−f 2)f 3
1 +f 2
#
+ (βe2−4) ω2
(1 +f 2)2

f 2f′′ + 2
rf 2f′ + (1−3f 2)ff′2
1 +f 2

+ 1
2(2βe2 + 2γe2−1)| {z }
1
2 (βe2−1)
l2(l+ 1) 2
r4
f 3
1 +f 2,(II.24)
It is important to observe that the first term in the expression forG(r) vanishes due to the imposed
constraintβe 2 + 2γe2 = 0, and the coefficient of the final term simplifies to 1
2(βe2−1).
