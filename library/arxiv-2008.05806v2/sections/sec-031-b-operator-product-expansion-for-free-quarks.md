---
doc_id: arxiv-2008.05806v2
doc_title: "Sum rule for the Compton amplitude and implications for the proton-neutron mass diﬀerence"
section_id: sec-031-b-operator-product-expansion-for-free-quarks
section_title: "B Operator product expansion for free quarks"
section_number: null
pages: 24-25
source_pdf: 2008.05806v2.pdf
source_sha256: 4e1f9af118ba81b1
toc_source: outline
doc_brief: "Sum rule for the Compton amplitude and implications for the proton-neutron mass difference — The Cottingham formula expresses the lead- ing contribution of the electromagnetic interaction to the"
---
For free quarks, the time-ordered product of two cur-
rents can be decomposed as
T jµ(x)jν(y)=P
fQ2
f tr{γµSf(x −y)γνSf(y −x)}1
+ 1
i
P
fQ2
fN{ ¯f(x)γµSf(x −y)γνf(y)
+ ¯f(y)γνSf(y −x)γµf(x)}
+Njµ(x)jν(y) ,
(B.1)
where Sf(z) is the quark propagator and N stands for
normal ordering. In this expression, the singularities ex-
clusively reside in the propagator – the matrix elements
of the normal ordered products are regular at x = y.
The short distance expansion of the propagator starts
with
Sf(z) = −
γαzα
2π2(−z2 + iǫ)2 +
imf
4π2(−z2 + iǫ) + O(z−1) .
(B.2)
The leading singularity is contained in the ﬁrst line of
equation (B.1) and is proportional to (−z2+iǫ)−3 – the
matrix elements thereof represent the disconnected part
of the amplitude. We are interested in the singularities
of the connected part, i.e. in the terms that contain
one quark propagator and two quark ﬁelds. To analyze
these, we set x = X + 1
2z, y = X −1
2z and expand in
powers of z. The expansion of the connected part starts
with
T jµ(x)jν(y) =
ǫµναβzα
π2(−z2 + iǫ)2
P
fQ2
f ¯fγβγ5f
(B.3)
−
zαzβ
2π2(−z2 + iǫ)2
P
fQ2
f (gµαOf
νβ + gναOf
µβ −gµνOf
αβ)
+
gµν
2π2(−z2 + iǫ)
P
fQ2
f mf ¯ff + O(z−1) ,
where Of
αβ stands for
Of
αβ = i ¯fγα∂
↔
βf .
(B.4)
We have dropped the normal ordering prescription as
well as the argument of the quark ﬁelds – it is under-
stood that the quark bilinears occurring here are to be
normal ordered and evaluated at the point X.
The operator Of
αβ contains components with spin 0,
1 and 2:
Of
αβ =Of0
αβ + Of1
αβ + Of2
αβ
(B.5)
Of0
αβ = 1
4gαβOf λ
λ ,
Of1
αβ = 1
2(Of
αβ −Of
βα) ,
Of2
αβ = 1
2(Of
αβ + Of
βα −1
2gαβOf λ
λ ) .
Neither the axial vector ¯fγβγ5f nor the spin 1 operator
Of1
αβ contribute to the spin average. The equation of
motion relates the spin 0 part to the scalar operator
¯ff,
Of λ
λ
= 2mf ¯ff ,
(B.6)
and Of2
αβ is what becomes of the spin 2 operator speci-
ﬁed in equation (38) when g is set equal to zero. Drop-
ping terms that do not contribute to the spin average
of the connected part, we obtain
T jµ(x)jν(y)=−
zαzβ
2π2(−z2 + iǫ)2 ×
(B.7)
×P
fQ2
f(gµαOf2
βν + gναOf2
βµ −gµνOf2
αβ)
−2zµzν + gµνz2
4π2(−z2 + iǫ)2
P
fQ2
fmf ¯ff + O(z−1) ,
We denote the Fourier transform with respect to z
at ﬁxed X = 1
2(x + y) by
˜Tµν(q, X) = i
2
Z
d4z eiq·zT jµ(x)jν(y) .
(B.8)
The OPE determines the behaviour of this quantity at
large momenta. With the formulae
i
4π2
Z
d4zeiq·z
1
−z2 + iǫ =
1
−q2 −iǫ
(B.9)
i
4π2
Z
d4zeiq·z
zαzβ
(−z2 + iǫ)2 = −qαqβ + 1
2gαβq2
(−q2 −iǫ)2
,
the various terms occurring in (B.7) yield:
˜Tµν(q, X) =
qαqβ −1
2gαβq2
(−q2 −iǫ)2
P
fQ2
f(gµαOf2
νβ + gναOf2
µβ −gµνOf2
αβ)
+qµqν −gµνq2
(−q2 −iǫ)2
P
fQ2
fmf ¯ff + O(q−3) .
(B.10)
The spin 2 part is indeed of the same structure as the
coeﬃcient of c2 in equation (A.3): for free quarks, the
spin 2 coeﬃcients are given by
cf
2(q2) =
Q2
f
(−q2 −iǫ)2 ,
cf
3(q2) = 0 .
(B.11)
Finally, comparison of the term proportional to Of0 =
mf ¯ff with equation (40) shows that for free quarks,
the coeﬃcient cf
1 is given by
cf
1(q2) =
Q2
f
(−q2 −iǫ)2 .
(B.12)
