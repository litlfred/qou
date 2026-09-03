---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-005-4-poly-bargmann-transforms
section_title: "Poly-Bargmann transforms"
section_number: 4
pages: 21-22
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
Purpose of the section. In this section, we discuss the poly-Bargmann transforms,
a generalization of the classical Bargmann transform, which are needed later
when we analyze the Berezin density at a boundary point. The poly-Bargmann
transforms appeared in Vasilevski’s paper [25], where the basic properties were
presented.
The Hermite polynomials and the Bargmann transform. We denote by Hj the
j-th Hermite polynomial with respect to the Gaussian weight e−1
2 t2 (“probabilistic
Hermite polynomials”). The generating function identity
etz−1
2 z2 =
+∞
X
j=0
Hj(t)zj
j!
allows us to write
1
(2π)1/4 ezt−1
2 z2−1
4 t2 =
+∞
X
j=0
Hj(t)e−t2/4
(2π)1/4 p
j!
× zj
p
j!
.
We recall the standard deﬁnition of the Bargmann transform:
B[ f](z) =
1
(2π)1/4
Z
R
ezt−1
2 z2−1
4 t2 f(t) dt,
f ∈L2(R).
As the function systems
n
1
(2π)1/4 p
j!
Hj(t)e−1
4 t2o+∞
j=0
and
n zj
p
j!
o+∞
j=0
form orthonormal bases for L2(R) and the Bargmann-Fock space A2
1,1(C) (this is
A2
m,q(C) with m = q = 1), respectively, we obtain the following well-known fact.
Proposition 4.1. The Bargmann transform B : L2(R) →A2
1,1(C) acts isometrically and
bijectively, and for each j = 0, 1, 2, . . ., the basis function (2π)−1/4(j!)−1/2Hj(t)e−1
4 t2 is
mapped to the basis function (j!)−1/2zj.
A class of auxiliary operators. Let ∂z, ¯∂z denote the standard Wirtinger diﬀerential
operators
∂z := 1
2(∂x −i∂y),
¯∂z := 1
2(∂x + i∂y),
where z = x + iy.
For r = 0, 1, 2, . . ., we introduce the operator
Tr[ f](z) :=
1
√
r!
e|z|2 ∂r
z
n
f(z)e−|z|2o
,
with the semi-group property T1 ◦Tr−1 = r1/2Tr. We also consider the dilated
variant
Tm,r[ f](z) = Tr[ fm−1/2](m1/2z),
where fm−1/2(z) = f(m−1/2z). It has the semi-group property Tm,1 ◦Tm,r−1 = r1/2Tm,r,
and may be expressed in more concrete terms:
Tm,r[ f](z) = m−r/2
√
r!
em|z|2 ∂r
z
n
f(z)e−m|z|2o
.
We now study the eﬀect of Tr on the basis elements (j!)−1/2zj.
22
Haimi and Hedenmalm
Proposition 4.2. For j ≥r, we have
Tr
 zj
p
j!

=
1
√
r!
e|z|2∂r
z

e−|z|2 zj
p
j!

=
s
r!
j!zj−rLj−r
r (|z|2)
while for j ≤r,
Tr
 zj
p
j!

=
1
√
r!
e|z|2∂r
z

e−|z|2 zj
p
j!

= (−1)r−j
r
n!
r! ¯zr−jLr−j
j (|z|2)
Proof. The proof is based on an induction argument. The statement is obviously
true for r = 0 and all j. So, by induction, we assume that the statement holds for
some r −1 ≥0 and all j. In case j ≥r, we then have
∂r
z{e−|z|2zj} = ∂z
n
(r −1)! zj−r+1Lj−r+1
r−1 (|z|2)e−|z|2o
= (r −1)!zj−rn
(j −r + 1)Lj−r+1
r−1 (|z|2) −Lj−r+2
r−2 (|z|2)|z|2 −|z|2Lj−r+1
r−1 (|z|2)
o
e−|z|2
= r!Lj−r
r (|z|2)zj−re−|z|2,
if we use the standard identity rLα
r (x) = (α + 1 −x)Lα+1
r−1 (x) −xLα+2
r−2 (x). Next, in case
j ≤r −1, we have instead
∂r
z{e−|z|2zj} = (−1)r−1−j∂
n
j! ¯zr−1−jLr−1−j
j
(|z|2)e−|z|2o
= (−1)r−j j!¯zr−jn
Lr−j
j−1(|z|2) + Lr−j−1
j
(|z|2)
o
e−|z|2 = (−1)r−j j! ¯zr−jLr−j
j (|z|2)e−|z|2,
which completes the proof.
□
Pure poly-analytic Fock spaces. Write ej(z) := (j!)−1/2zj for j = 0, 1, 2, . . ., which
functions form the standard orthonormal basis for the space A2
1,1(C). The function
Tr[ej] ∈A2
1,r+1(C) is then a polynomial in z, ¯z, where the degree in z remains
equal to j, and the degree in ¯z equals r. For general positive m, the functions
ej,m(z) := (j!)−1/2m
1
