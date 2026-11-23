---
doc_id: s10052-020-08615-2
doc_title: "Sum rule for the Compton amplitude and implications for the proton–neutron mass difference"
section_id: sec-033-appendix-b-operator-product-expansion-for-free-q
section_title: "Appendix B: Operator product expansion for free quarks"
section_number: null
pages: 23-24
source_pdf: s10052-020-08615-2.pdf
source_sha256: 23becb0b1a2e7f1b
toc_source: outline
doc_brief: "Sum rule for the Compton amplitude and implications for the proton–neutron mass difference — The Cottingham formula expresses the leading contribution of the electromagnetic interaction to the"
---
For free quarks, the time-ordered product of two currents can
be decomposed as
T jμ(x) jν(y) =

f
Q2
f tr{γμS f (x −y)γνS f (y −x)}1
+1
i

f
Q2
f N{ ¯f (x)γμS f (x −y)γν f (y)
+ ¯f (y)γνS f (y −x)γμ f (x)}
+N jμ(x) jν(y),
(B.1)
where S f (z) is the quark propagator and N stands for nor-
mal ordering. In this expression, the singularities exclusively
reside in the propagator – the matrix elements of the normal
ordered products are regular at x = y. The short distance
expansion of the propagator starts with
S f (z) = −
γαzα
2π2(−z2 + iϵ)2 +
im f
4π2(−z2 + iϵ) + O(z−1).
(B.2)
The leading singularity is contained in the ﬁrst line of Eq.
(B.1) and is proportional to (−z2 + iϵ)−3 – the matrix ele-
ments thereof represent the disconnected part of the ampli-
tude. We are interested in the singularities of the connected
part, i.e. in the terms that contain one quark propagator and
two quark ﬁelds. To analyze these, we set x = X + 1
2z,
y = X −1
2z and expand in powers of z. The expansion of
the connected part starts with
T jμ(x) jν(y)
=
ϵμναβzα
π2(−z2 + iϵ)2

f
Q2
f ¯f γ βγ5 f
6 Hill and Paz [38] use a different normalization. In our notation, they
work with T HP
μν = 2Tμν and normalize the spin 2 operator formed with
the derivatives of the quark ﬁelds differently: O f2 HP
αβ
=
1
2 O f2
αβ. The
Wilson coefﬁcients are related by c f
1 = cHP
1 /(2q4), c f
2 = −cHP
3 /(4q4),
c f
3 = (cHP
2
+ cHP
3 )/(4q6).
123
−
zαzβ
2π2(−z2 + iϵ)2

f
Q2
f (gμαO f
νβ + gναO f
μβ −gμν O f
αβ)
+
gμν
2π2(−z2 + iϵ)

f
Q2
f m f ¯f f + O(z−1),
(B.3)
where O f
αβ stands for
O f
αβ = i ¯f γα∂↔
β f.
(B.4)
We have dropped the normal ordering prescription as well as
the argument of the quark ﬁelds – it is understood that the
quark bilinears occurring here are to be normal ordered and
evaluated at the point X.
The operator O f
αβ contains components with spin 0, 1 and
2:
O f
αβ = O f0
αβ + O f1
αβ + O f2
αβ
O f0
αβ = 1
4gαβ O f λ
λ ,
O f1
αβ = 1
2(O f
αβ −O f
βα),
O f2
αβ = 1
2(O f
αβ + O f
βα −1
2gαβ O f λ
λ ).
(B.5)
Neither the axial vector ¯f γ βγ5 f nor the spin 1 operator O f1
αβ
contribute to the spin average. The equation of motion relates
the spin 0 part to the scalar operator ¯f f ,
O f λ
λ
= 2m f ¯f f,
(B.6)
and O f2
αβ is what becomes of the spin 2 operator speciﬁed in
Eq. (38) when g is set equal to zero. Dropping terms that do
not contribute to the spin average of the connected part, we
obtain
T jμ(x) jν(y) = −
zαzβ
2π2(−z2 + iϵ)2
×

f
Q2
f (gμαO f2
βν + gναO f2
βμ −gμν O f2
αβ)
−2zμzν + gμνz2
4π2(−z2 + iϵ)2

f
Q2
f m f ¯f f + O(z−1),
(B.7)
We denote the Fourier transform with respect to z at ﬁxed
X = 1
2(x + y) by
˜Tμν(q, X) = i
2

d4z eiq·zT jμ(x) jν(y).
(B.8)
The OPE determines the behaviour of this quantity at large
momenta. With the formulae
i
4π2

d4zeiq·z
1
−z2 + iϵ =
1
−q2 −iϵ
i
4π2

d4zeiq·z
zαzβ
(−z2 + iϵ)2 = −qαqβ + 1
2gαβq2
(−q2 −iϵ)2
,
(B.9)
the various terms occurring in (B.7) yield:
˜Tμν(q, X)
= qαqβ −1
2gαβq2
(−q2 −iϵ)2

f
Q2
f
×(gμαO f2
νβ + gναO f2
μβ −gμν O f2
αβ)
+qμqν −gμνq2
(−q2 −iϵ)2

f
Q2
f m f ¯f f + O(q−3).
(B.10)
The spin 2 part is indeed of the same structure as the coefﬁ-
cient of c2 in Eq. (A.3): for free quarks, the spin 2 coefﬁcients
are given by
c f
2 (q2) =
Q2
f
(−q2 −iϵ)2 ,
c f
3 (q2) = 0.
(B.11)
Finally, comparison of the term proportional to O f0
=
m f ¯f f with Eq. (40) shows that for free quarks, the coef-
ﬁcient c f
1 is given by
c f
1 (q2) =
Q2
f
(−q2 −iϵ)2 .
(B.12)
