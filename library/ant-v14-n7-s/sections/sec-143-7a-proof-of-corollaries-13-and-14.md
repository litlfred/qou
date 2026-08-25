---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-143-7a-proof-of-corollaries-13-and-14
section_title: "7A. Proof of Corollaries 1.3 and 1.4"
section_number: null
pages: 276-278
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
case of Corollary 1.3, simply set c0= 1 in each instance below. We recall from Theorem 1.1 that
|S(F; N, H)|≪‖ H‖1−1/(2r)H−1/(2r)
min q(n2+1)/4r2(log q)n+1, (7-5)
where for every r≥ 1 we have set
2=2n,r=
⌊ r−1
n−1
⌋
.
First let us determine for a given n≥ 2 the threshold governing for which lengths H the bound (7-5) is
nontrivial, that is o(‖H‖), under the assumption that‖H‖1/n= qβ and Hmin≫‖ H‖c0/n= qc0β. Then
the bound (7-5) is nontrivial as long as
(
1− 1
2r
)
nβ− c0
2rβ+ n2+ 1
4r2 < nβ,
that is,
β>β n,r:= n2+ 1
22(n+ c0)= 1
2− c02− 1
22(n+ c0). (7-6)
Given n≥ 2 and 0< c0≤ 1, as long as we take r sufﬁciently large that2=2n,r> 1/c0, we haveβn,r< 1
2.
(In particular if c0= 1, note that2n,r> 1 when(r− 1)/(n− 1)≥ 2, or equivalently, r≥ 2n− 1.) On the
other hand, note that for ﬁxed n≥ 2, for all r≥ 1
1
2− c02− 1
22(n+ c0)> 1
2− c0
2(n+ c0)≥ 1
2− 1
2(n+ 1),
for all 0< c0≤ 1, and this a limitation on the range of β for which the bound is nontrivial.
We now compute that the bound (7-5) is of the form‖H‖q−δ where
δ= n+ c0
2r β− n2+ 1
4r2 . (7-7)
Burgess bounds for short character sums evaluated at forms 1943
We make the approximation that2=(r− 1)/(n− 1), which is an identity when n= 2, and will not be
far from the truth, when we later take r very large. Then we compute that after this approximation, δ can
be represented as a function of r by
fa,b,c(r)= a
r− br− c
r(r− 1),
where
a=(n+ c0)β
2 , b= n
4, c= 1
4.
As a function of r, this attains a maximum at
r=(a− b)−1{(a− c)±
√
(a− c)2−(a− c)(a− b)}. (7-8)
To have r> 0 we must have(a− b)> 0, that is
β>β n,c0:= n
2(n+ c0)= 1
2− c0
2(n+ c0), (7-9)
agreeing with our previous observation. Thus from now on we assume β=βn,c0+κ for some smallκ,
and we will study how δ=δn(κ) behaves as κ→ 0. From (7 -7) with β=βn,c0+κ (and without
approximating2), we see that for any r,
δ=δn(κ):= n+ c0
2r κ− 1
4r2.
To maximize this, according to (7-8), asκ→ 0 we will take r to be the integer closest to
n− 1
κ(n+ c0).
For an approximation, we set r= (n− 1)/(κ(n+ c0)) in the expression for δn(κ), and using the
approximation2≈ r/(n− 1) (which is reasonable asκ→ 0 since then r→∞ ), we see that
δn(κ)≈(n+ c0)2
4(n− 1)κ2 (7-10)
asκ→0. Here we use≈ because we have made two types of approximations: ﬁrst, we used approximations
of the value of2 and r for simplicity, which introduced errors that become vanishing small, relative to
the true size of δn(κ), asκ→ 0. Second, to simplify certain expressions, we used the fact that we are in
the limiting caseκ→ 0.
Alternatively, we can encapsulate the restriction (7-9) by recording it as the restriction
‖H‖Hmin≫‖ H‖1+c0/n≫(qnβ)1+c0/n,
where β=βn,c0+κ for any small κ >0. Therefore we will obtain a nontrivial bound as long as
‖H‖Hmin≫ qn/2+κ for any smallκ> 0.
1944 Lillian B. Pierce and Junyan Xu
