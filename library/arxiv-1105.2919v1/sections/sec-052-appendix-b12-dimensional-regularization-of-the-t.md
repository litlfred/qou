---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-052-appendix-b12-dimensional-regularization-of-the-t
section_title: "Appendix B.1.2 Dimensional regularization of the triangles"
section_number: null
pages: 66-68
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The integral is divergent and, therefore, requires regularization. In Ref. [54], this is done by introducing a
Gaussian cutoﬀfunction exp(−⃗l2/Λ2) which, however, makes the results dependent on the cutoﬀparameter
Λ. To avoid such cutoﬀdependence, we will use dimensional regularization which was ﬁrst introduced by ’t
Hooft and Veltman in 1972 [227].6
For this it is convenient to go back to Eq. (B.14) and apply a trick discovered by Feynman [230],
1
ab =
Z 1
0
dx
[b + (a −b)x]2 ,
(B.19)
which allows to write the product of propagators in terms of a linear combination. Applying Feynman’s
trick in Eq. (B.14) yields
V = τ 1 · τ 2
g2
A
2f 4π
Z 1
0
dx
Z
d4l
i(2π)4⃗
l2 +⃗l ·⃗q
[l2 + (2lq + q2)x −m2π + iϵ]2 .
(B.20)
The momentum integral is not yet quite ready for dimensional regularization because the integrand mixes
three- and four-dimensional versions of the loop-momentum l. The dimension of the integration variable l
must be consistent throughout the integrand.
Formal (four-dimensional) covariance can be re-covered by re-introducing the four-vector vµ = (1, 0, 0, 0)
and re-writing the numerator as⃗l2 +⃗l ·⃗q = (l · v)2 −l2 −l · q. After a shift of the integration variable
l →l +xq, well-known formulae for the dimensional regularization of covariant integrals can be applied [see,
e.g., Eqs. (10.23) and (10.32)-(10.34) of Ref. [229]].
Alternatively, one may go for consistency in three dimensions and reduce the momentum integral of
Eq. (B.20) to the three space-dimensions—which is what we will do here. This has the advantage that the
integration variable observes an Euclidean metric from the outset (and there is no need for a Wick rotation).
Moreover, the planar box diagram (see below) requires treatment in three dimensions.
The integrand of Eq. (B.20) has two poles as evidenced through
l2 + (2lq + q2)x −m2
π + iϵ =

l0 +
q⃗
l2 + m2π + (2⃗l ·⃗q +⃗q2)x −iϵ
 
l0 −
q⃗
l2 + m2π + (2⃗l ·⃗q +⃗q2)x + iϵ

(B.21)
where we used q0 = 0. The pole in the lower half-plane is
l0
1
=
q⃗
l2 + m2π + (2⃗l ·⃗q +⃗q2)x −iϵ ,
(B.22)
and, using the residue theorem, one obtains
V
=
τ 1 · τ 2
g2
A
2f 4π
Z 1
0
dx
Z dl0 d3l
i(2π)4⃗
l2 +⃗l ·⃗q
(l0 −l0
1)2(l0 + l0
1)2
=
τ 1 · τ 2
g2
A
2f 4π
Z 1
0
dx
Z
d3l
(2π)3
1
4⃗
l2 +⃗l ·⃗q
(l0
1)3
.
(B.23)
To proceed towards dimensional regularization, we now generalize the three-dimensional integral to (D −1)
dimensions. Moreover, we introduce the renormalization scale λ and multiply the integral by λ4−D such
that the dimension of the amplitude stays the same for any D [228, 231],
V = τ 1 · τ 2
g2
A
8f 4π
λ4−D
Z 1
0
dx
Z
dD−1l
(2π)D−1⃗
l2 +⃗l ·⃗q
(l0
1)3
.
(B.24)
6Accessible introductions into dimensional regularization can be found in Refs. [228, 229] and a very pedagogical presentation
is provided in appendix A.2 of the Scherer review [113].
66
For convenience, we now divide all dimension-full quantities involved in the integral by λ and denote all
dimensionless quantities (except for the dimensionless momentum⃗k) by a tilde; for example, ˜q =⃗q/λ.
Furthermore, we shift the integration variable by introducing the new variable⃗k with λ⃗k =⃗l + x⃗q, so that
there are no terms linear in the integration variable in the denominator. Thus, we have now
l0
1
=
λ
q⃗
k2 + ˜m2π + ˜q2x(1 −x) −iϵ ,
(B.25)
and our integral reads
V
=
τ 1 · τ 2
g2
A
8f 4π
λ2
Z 1
0
dx
Z
dD−1k
(2π)D−1
(k −x˜q)2 + (k −x˜q) · ˜q
[k2 + ˜m2π + ˜q2x(1 −x)]3/2 .
(B.26)
Terms with odd powers of k vanish,
V
=
τ 1 · τ 2
g2
A
8f 4π
λ2
Z 1
0
dx
Z
dD−1k
(2π)D−1
k2 −x(1 −x)˜q2
[k2 + ˜m2π + ˜q2x(1 −x)]3/2 .
(B.27)
The volume element in (D −1) dimensions is
dD−1k
=
kD−2 dk dΩD−1
(B.28)
with
Z
dΩD−1
=
2π(D−1)/2
Γ( D−1
2 ) .
(B.29)
Thus,
V
=
τ 1 · τ 2
g2
A
8f 4π
2λ2
Γ( D−1
2 )(4π)(D−1)/2
Z 1
0
dx
Z ∞
0
dk
kD −x(1 −x)˜q2kD−2
[k2 + ˜m2π + ˜q2x(1 −x)]3/2 .
(B.30)
Using [cf. for example, Eq. (A.35) of Ref. [113]]
Z ∞
0
kD−2+n1
(k2 + s)n/2 dk = Γ( D+n1−1
2
)Γ( n+1−D−n1
2
)
2Γ( n
2 )
1
s
n+1−D−n1
2
,
(B.31)
we obtain
V
=
τ 1 · τ 2
g2
A
8f 4π
λ2
Γ( 3
2)Γ( D−1
2 )(4π)(D−1)/2
Z 1
0
dx
(
Γ( D+1
2 )Γ( 2−D
2 )
[ ˜m2π + ˜q2x(1 −x)](2−D)/2
−x(1 −x)˜q2
Γ( D−1
2 )Γ( 4−D
2 )
[ ˜m2π + ˜q2x(1 −x)](4−D)/2
)
.
(B.32)
We choose D = 4 −η and then take the limit η →0. To prepare for the latter, we expand the various
expressions involved up to ﬁrst order in η:
Γ( D+1
2 )
Γ( D−1
2 )
=
D −1
2
= 3 −η
2
Γ
4 −D
2

=
Γ
η
2

= 2
η −γ + O(η)
Γ
2 −D
2

=
Γ( η
2)
η
2 −1 = −2
η + γ −1 + O(η)
67
1
(4π)
D−1
2
=
1
(4π)
3
2 (4π)
η
2 ≈
1
(4π)
3
2

1 + η
2 ln(4π)

1
( ˜m2π + ˜q2x(1 −x))
4−D
2
≈
1 −η
2 ln( ˜m2
π + ˜q2x(1 −x))
1
( ˜m2π + ˜q2x(1 −x))
2−D
2
≈
h
1 −η
2 ln( ˜m2
π + ˜q2x(1 −x))
i
( ˜m2
π + ˜q2x(1 −x))
(B.33)
Concerning the properties of the Γ-function, see, e.g., Ref. [232]; γ = 0.5772 . . . is Euler’s constant; and we
used aϵ = exp(ϵ ln a) ≈1 + ϵ ln a + . . ..
Hence
V
=
τ 1 · τ 2
g2
A
8f 4π
λ2
Γ( 3
2)
1
(4π)
3
2

1 + η
2 ln(4π)
 Z 1
0
dx
3 −η
2

−2
η + γ −1 + O(η)
 h
1 −η
2 ln( ˜m2
π + ˜q2x(1 −x))
i
( ˜m2
π + ˜q2x(1 −x))
−x(1 −x)˜q2
2
η −γ + O(η)
 h
1 −η
2 ln( ˜m2
π + ˜q2x(1 −x))
i
(B.34)
and neglecting terms of order η
V
=
τ 1 · τ 2
g2
A
8f 4π
λ2
Γ( 3
2)
1
(4π)
3
2

−2
η + γ −1 −ln(4π)
 3
2 ˜m2
π + 5
12 ˜q2

+ ˜m2
π + 1
3 ˜q2 +
Z 1
0
dx
3
2 ˜m2
π + 5
2 ˜q2x(1 −x)

ln( ˜m2
π + ˜q2x(1 −x))

.
(B.35)
The integral over the logarithmic term is
Z 1
0
dx
3
2 ˜m2
π + 5
2 ˜q2x(1 −x)

ln( ˜m2
π + ˜q2x(1 −x))
=
−4
3 ˜m2
π −25
36 ˜q2 +

3 ˜m2
π + 5
6 ˜q2

ln( ˜mπ)
+1
6(8 ˜m2
π + 5˜q2)L(q) ,
(B.36)
where
L(q) ≡w
q ln w + q
2mπ
,
w ≡
p
4m2π + q2 ,
and
q = |⃗q| .
(B.37)
Introducing the abbreviation
R
≡
−2
η + γ −1 −ln(4π) ,
(B.38)
the ﬁnal result for the triangle diagrams at NLO in dimensional regularization reads
V = τ 1 · τ 2
g2
A
384π2f 4π

(18m2
π + 5q2)R −4m2
π −13
3 q2 + 2(18m2
π + 5q2) ln
mπ
λ

+ (16m2
π + 10q2)L(q)

.
(B.39)
Renormalization in a Modiﬁed Minimal Subtraction scheme (MS-scheme) [228] amounts to omitting the
R-term.
