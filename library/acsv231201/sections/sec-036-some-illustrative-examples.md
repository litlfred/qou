---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-036-some-illustrative-examples
section_title: "Some illustrative examples"
section_number: null
pages: 189-200
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
171
Notational conventions
For the rest of this book we use the following notational conventions. Bold
quantities are reserved for vectors, such as z = (z1, . . . , zd), and we deﬁne z◦:=
(z1, . . . , zd−1). The d-variate function F(z) is a quotient of coprime polynomials
P(z)/Q(z), with the denominator Q vanishing on the singular variety V =
VQ = {z ∈Cd : Q(z) = 0}. We ﬁx a component B of the complement of
amoeba(Q) and consider the Laurent series expansion F(z) = P
r∈Zd arzr
that converges on D = Relog−1(B). As in previous chapters, for w ∈Cd
∗we
use the notation T(w) for the torus T(w) = {z ∈Cd : |z j| = |wj| for all j}.
The simplest and most common case, of a convergent power series expansion,
occurs when B is the component containing points of the form (−N, . . . , −N)
for N suﬃciently large, so that D is a neighborhood of the origin.
Remark 7.1. Although we mainly study rational generating functions, most
of our results also hold for meromorphic functions. We point out as we go
which major results still hold for meromorphic functions, and the small ways
in which they diﬀer from the rational case.
Given r ∈Zd the d-form ω = z−r−1F(z)dz is the integrand of the Cauchy
integral (7.1), with domain of analyticity M = Cd
∗\V. Unless otherwise stated,
we write |r| for the ℓ1-norm |r| = Pd
j=1 |rj| and as above deﬁne the normalized
vector ˆr = r/|r|. We seek to compute asymptotics for the series coeﬃcients
ar as r →∞with ˆr varying over a compact set, typically around some ﬁxed
direction.
7.1 Some illustrative examples
Example 7.2 (Binomial Coeﬃcients). We start with perhaps the simplest non-
trivial bivariate rational function for our purposes: F(x, y) = 1/Q(x, y) with
Q(x, y) = 1 −x −y. The amoeba of Q is pictured in Figure 7.1 (see Chapter 8
for methods to compute amoebas). Because there are three components in the
amoeba complement, there are three convergent Laurent series expansions of
F(x, y). Consider the power series expansion F(x, y) = P
i,j≥0
i+ j
i

xiyj, corre-
sponding to the component of the amoeba complement that lies in the third
quadrant. Since
X
i,j≥0

 i + j
i
!
xiyj

 =
X
i,j≥0
 i + j
i
!
|x|i|y| j =
1
1 −|x| −|y|,
(7.3)
172
Overview of analytic methods for multivariate GFs
Figure 7.1 Amoeba of the function 1 −x −y.
this series expansion has domain of convergence D = {(x, y) ∈C2 : |x| + |y| <
1}. For any a, b ∈(0, 1) with a + b < 1 we can write
 i + j
i
!
=
1
(2πi)2
Z
T(a,b)
1
1 −x −y
dxdy
xi+1y j+1
=
1
(2πi)2
Z
T(a,b)
1
1 −x −ye−φ(x,y) dxdy
xy
,
(7.4)
where φ(x, y) = i log x + j log y. We aim to use residue computations to reduce
the two-dimensional integral (7.4) to a one-dimensional integral over some
path in the singular set V = {(x, y) ∈C2 : x + y = 1}, and then compute a
saddle point integral. Thus, we set y = 1 −x in φ(x, y) and solve for a saddle
point, where the ﬁrst derivative of the function vanishes. The equation
0 = d
dxφ(x, 1 −x) = i
x −
j
1 −x
implies x = i/(i + j). Hence, we aim to determine asymptotic behavior by
studying the Cauchy integral near (x∗, y∗) = (i/(i + j), j/(i + j)) ∈V. For
this discussion we ﬁx positive integers r, s > 0 and derive asymptotics of the
7.1 Some illustrative examples
173
coeﬃcient sequence (i, j) = n(r, s) as n →∞. To that end, deﬁne
I =
1
(2πi)2
Z
|x|=x∗
 Z
|y|=y∗−ε
1
1 −x −y
dy
yns+1
! dx
xnr+1
Iloc =
1
(2πi)2
Z
N
 Z
|y|=y∗−ε
1
1 −x −y
dy
yns+1
! dx
xnr+1
Iout =
1
(2πi)2
Z
N
 Z
|y|=y∗+ε
1
1 −x −y
dy
yns+1
! dx
xnr+1 ,
where N = {x ∈C : |x| = x∗and arg(x) ∈(−δ, δ)} is any arbitrarily small
neighborhood of x∗in the circle {|x| = x∗}. As we will see in Chapter 9, both
I −Iloc and Iout grow exponentially slower than I, so (7.4) implies
 nr + ns
rn
!
= I = Iloc −Iout + exponentially negligible term.
Thus, we can use the (univariate) residue theorem to approximate
nr+ns
rn

by
Iloc −Iout =
1
(2πi)2
Z
N
 Z
|y|=y∗−ε
1
1 −x −y
dy
yns+1 −
Z
|y|=y∗+ε
1
1 −x −y
dy
yns+1
! dx
xnr+1
=
−1
(2πi)
Z
N
Res
y=1−x
y−ns−1
1 −x −y
dx
xnr+1
=
1
(2πi)
Z
N
dx
xnr+1(1 −x)ns+1 .
Making the change of variables x = x∗eiθ results in the saddle point integral
Iloc −Iout = x−rn
∗
y−sn
∗
2π
Z δ
−δ
A(θ)e−nφ(θ),
where
A(θ) =
1
1 −x∗eiθ = r + s
s
+ O(θ)
and
φ(θ) = r log(x∗eiθ)+s log(1−x∗eiθ)−r log(x∗)−s log(y∗) = r(r + s)
2s
θ2+O

θ3
.
Theorem 4.1 from Chapter 4 then gives an asymptotic expansion
 nr + ns
nr
!
=
r + s
r
rn r + s
s
sn
n−1/2
 √r + s
2rsπn + · · ·
!
.
◁
174
Overview of analytic methods for multivariate GFs
The approach taken in Example 7.2 is known as the surgery method for
multivariate asymptotics. It works by performing an explicit deformation to
move the torus of integration in the Cauchy integral near a critical point, then
changing the radius in one coordinate to enclose singularities. The ordinary
(univariate) residue theorem, a localization argument, and the saddle point re-
sults from Chapters 4 and 5 then yield asymptotics.
Although this approach can be generalized successfully, as will be done in
Section 9.1 of Chapter 9, such explicit deformations require additional assump-
tions on the singularities where local behavior of F(z) determines asymptotics.
In particular, such singularities need to be minimal in the sense of Section 6.4,
meaning they lie on the boundary of the domain of convergence of the Lau-
rent expansion being considered. In fact, we require ﬁnite minimality, meaning
such singularities are minimal and only a ﬁnite number of other singularities
have the same coordinatewise modulus. Although this is usually not an unrea-
sonable assumption, in practice it can be very expensive to verify formally (see
Chapter 8 for more details).
Exercise 7.1. Suppose we perturb Example 7.2 by taking Qε(x, y) = 1 −
x −y −εy2 for some ε > −1. Let Dε = {(x, y) ∈C2 : |x|, |y| < ρε} where
ρε =
 √
1 + ε −1

/ε the positive root of Qε(x, x). When ε = 0, the function
1/Qε(x, y) is the function in (7.3), whose power series domain of convergence
contains D0 = {(x, y) ∈C2 : |x|, |y| < 1/2}.
(a) As ε →0, determine the ﬁrst two terms of the asymptotic behavior of ρε.
(b) When ε > 0, is there an easy way to see that 1/Q(x, y) is analytic on Dε?
(c) When −1 < ε < 0, can you show that 1/Q(x, y) is analytic on Dε?
(d) What can you say when ε ≤−1?
We now study an example where the surgery method does not directly apply,
and sketch a more general topological method for multivariate asymptotics.
Although the topological method applies in a wider variety of situations, as its
name suggests it will require more advanced constructions from topology and
diﬀerential geometry. Our next example also illustrates how the topological
approach generalizes hands-on surgery in the smooth case to a topologically
characterized contour integration.
Example 7.3 (Non-Minimal Contributing Points). Consider the (1, 1)-diagonal
sequence an,n of the power series expansion
F(x, y) =
1
Q(x, y) =
X
i,j≥0
ai,jxiy j,
7.1 Some illustrative examples
175
where Q(x, y) = (1 −x −y)(1 + 3x), so
ai, j =
iX
k=0
 k + j
k
!
(−3)i−k.
The singular set V = VQ is the union of the hyperplane V1−x−y from Exam-
ple 7.2 with the hyperplane V1+3x. It contains the point (x∗∗, y∗∗) = (−1/3, 4/3)
on the intersection of the hyperplanes where V is not a manifold.
Since V still contains the hyperplane V1−x−y, the point (x∗, y∗) = (1/2, 1/2)
identiﬁed in Example 7.2 is still of interest for the asymptotic analysis. Fur-
thermore, the topology of V changes at the non-smooth point (x∗∗, y∗∗), so this
point is also of interest. The function φ(x, y) = log x + log y has nonvanish-
ing derivative when restricted to V1+3x, hence there are no other points where
we could restrict the Cauchy integrand to the singular variety and get a saddle
point integral.
As we will see later, asymptotics of the coeﬃcient sequence an,n are still de-
termined by reducing to an integral near (x∗, y∗). However, unlike Example 7.2
we cannot simply move the contour of integration in the Cauchy integral
an,n =
1
(2πi)2
Z
|x|=ε1
Z
|y|=ε2
1
(1 −x −y)(1 + 3x)
dxdy
xn+1yn+1
to a torus {(x, y) : |x| = x∗, |y| = y∗−ε} as we would cross the singular set
V at points where x = −1/3. To work around this, we expand y through the
singular variety, resulting in an integral over a tube around V1−x−y, reduce to an
integral on V1−x−y through a residue computation, and then move the contour
of integration to the saddle point.
For concreteness, we now take ε1 = ε2 = 1/10, although any positive values
satisfying 0 < ε1+ε2 < 1 and ε1 < 1/3 would work. Let T0 = {|x| = |y| = 1/10}
and, for any M > 0, deﬁne the map
KM : T0 × [0, 1] →C2
(x, y, t) 7→(x, y(1 + Mt)) .
Then KM is a homotopy from T0 to the torus T1 = {|x| = 1/10, |y| = (M+1)/10}.
As long as M > 10 then F(x, y) is analytic on T0 and T1, the image of KM does
not intersect the coordinate axes of C2, and this image intersects V in the set
C = {(x, 1 −x) : |x| = 1/10}. Furthermore, the image of KM intersects V
transversely, meaning the tangent planes of these sets jointly span C2 at their
common points. See Figure 7.2 for a visualization of the path of this homotopy
after taking the Relog map.
Because F(x, y) is analytic on C2 \ V, Stokes’s Theorem (Theorem A.24 in
176
Overview of analytic methods for multivariate GFs
Figure 7.2 The amoeba of (1 −x −y)(1 + 3x). We start by integrating over the
torus deﬁned by |x| = 1/10 and |y| = 1/10 and expand |y| to (M + 1)/10 >
11/10, resulting in an integral over a tubular neighborhood of V. Taking a residue
reduces to an integral over a curve lying on the hyperplane 1 −x −y = 0 then,
avoiding the set of points where 1 + 3x = 0, we slide this contour to a curve
near the point (1/2, 1/2) on V together with points that do not aﬀect dominant
asymptotics.
Appendix A) implies that the Cauchy integral over the boundary of any 3-cycle
in C2
∗\ V is zero. In particular,
Z
T0
F(x, y) dxdy
xn+1yn+1 =
Z
ν
F(x, y) dxdy
xn+1yn+1 +
Z
T1
F(x, y) dxdy
xn+1yn+1 ,
(7.5)
where ν is a tubular neighborhood of C: the union of circles normal to the tan-
gent plane of V with centers at the points of C (see Figure 7.3). Furthermore,
because (7.5) holds for any M > 10, and
Z
T1
F(x, y) dxdy
xn+1yn+1 = O  10n(M + 1)−n ,
7.1 Some illustrative examples
177
Figure 7.3 A visualization of the tubular neighborhood ν.
taking M →∞shows that the integral over T1 is zero for n > 0, and thus
an,n =
1
(2πi)2
Z
ν
F(x, y) dxdy
xn+1yn+1 =
1
(2πi)2
Z
ν
1
(1 −x −y)(1 + 3x)
dxdy
xn+1yn+1 .
The tubular neighborhood ν is the union of circles with centers on C, and each
point of C corresponds to a simple pole of F(x, y), where 1 −x −y = 0, so a
generalization of the classical univariate residue theorem implies
an,n = 1
2πi
Z
|x|=1/10
Res
y=1−x
1
(1 −x −y)(1 + 3x)
dx
xn+1yn+1
= 1
2πi
Z
|x|=1/10
1
1 + 3x
dx
xn+1(1 −x)n+1 .
(7.6)
As in the last example, the integrand of (7.6) becomes a saddle point integral
near x = 1/2. The diﬀerence is that while we previously used a residue to
localize near the saddle point, this time we took a more “convenient” residue
and obtained a univariate integral away from the saddle point. Because we
are dealing with an integrand having a linear denominator, we can move our
domain of integration to pass through the critical point without much diﬃculty.
We now describe three methods for doing this, listed in decreasing order of
explicitness but increasing order of generality.
Method One: Because the only singularity of the integrand in (7.6) between
the circles |x| = 1/10 and |x| = 1/2 occurs at x = −1/3, the domain of in-
tegration in (7.6) can be replaced by the union of the circle |x| = 1/2 and a
suﬃciently small clockwise circle around x = −1/3 (see Figure 7.4 left). The
178
Overview of analytic methods for multivariate GFs
1
2
WPcruQLEhbKkaFK3tdukaOwFlEzZqiVRoOjYsaGvsdfta+2T7HWkJsUjxy0nQEnJH/c0gdHd5sR74Xs2bznytXP/jwo48/ufZp5bPv/jyq+s3vj6OyYQ6+KVDfEJf2SjGvhfil8xjPn4VUYwC28cn9nhX8JNzTGOPhC/YRY
T7ARqGnus5iPGmXr3nUuQsrGRxOzm7Xm02munHhAUrL1SN/Ps7MbNbm9AnEmAQ+b4KI5PrWbE+gtEmef4OKn0JjGOkDNGQ3zKiyEKcNxfpINOzBpvGZguofwbMjNtVS0WKIji8DmygCxUawz0VjGTifMvdfeGE0YTh0so7ciW8yY
oImAOPYof5F7yAHOrxsZrOCPEwMB6nQi/MG8+TSqVmHiGZ3yIQYDCAdeEeJpXFr3gQcL/8FE4yF8SBKN7ip0F9A9he4Buq/QfUAPFHoA6COFPgL0sUIfA3qk0CNAnyj0CaBthbYB7Si0A2hXoV1AXyj0BaDHCj0G9EShJ5xq2F1
Gms+GcRpq/Zk7hYc+yq2LR4CjKRTGMql2pNOYWCati2Ua613QXSPdm2hDaAjoQOgFhCDKDrSuoCOpJwBKAnoQfgGwnfADiWcAxgKGEIYCBhAGAkYQglZACGEsY63DEUjxCTNXoHs6lh3MApxJOAZxJOAPwQsILAOcSznU416D+wO
KRbOIPxApM/EUv9oYBSDp/SNGAC0Nk+4jnrk+G0NWcR0Y4m59lQRrD4MxHLDm1+oqoapWqQtVRCXTlaPpJY6muaOp6kjTHMrwHAIHbQnBEmcvFyI+iY+BX5oFQ/QKs0yBIh9hJLGSpE1gTkJlJlvAHAt6jiOYs8noWZNaUbpiIB+
lxYr58KX3vsQ8ZIiyepgZqMoUlVZHQaCKBpaMh/TbJS0uy02QgzVZXVgQpNVA2vgcQrupmXeSEBHqirK6HkogdjvDzmDiuwS2OjFUMlj4yVTFYKchMxWCtIBcqBqsFSZeLFRerh64oCOCiQewsToqPkixZaSY5w/wukA9oEMhwTO
2EWA5RwDJ65DycDM3ZcMnKfakoFJ/Vqy1zp7Ltlzne1KBs5+HcnASej80rl6vn6uHhwtw3ZwBKL2bCK25M/cgU/6yTJ5uZ8a0sX8i1NvOupN8DZYgRygSuCgLstlxBC4uZTqcF+2k62j3M7xEUP+FheRphihihPUz5uYS6Sn9k
cR871K/KnUegPsijrPqpyLK0cKuXkOvcEQ4FoTRJzpZr4DIUM6rJ2rsyle17saCrRlAnUJ46HYgEtCEWTHvoO9pdvkBfT/bTAUbDEKCDYTmdOzdyjaGrGDEdmjJl2P+G3nCFNd8WKafIpOfTC9GITeQ6bUJycxvzsiX9tNlqtPk/I
MRYGtg4e5jbq9KPtrU9/7bOL8rfa91XTO7mE0iUyweZuqaX/MqR3iF1vG72dZ0BmOmV21Flhx6ta29u9ndDzk5oiSNure3q7ZQtamKIAx6p0/pv2yYbec64b24+3TLr9Vu3NqvW1n0h8NxZj2Ifzaqt7H8P+zFeVy567lesh
wb4TsLNfkb1073+QMv48O9O4TQgRfy62TaM2LmZnO7uXW/SNor0riXjkqzbP+eCxr3MkRq7TMvKsI6iX23WX39TX9d08yRV16KHAVl46gXVDAETy0Mm41Wtv8W+biYSt3ITR1KcqU6esSiVZJRMs7pbMrbXJtT673i2l3jen7PdPK
uylLIELk0n6/JksvhLWJ9IpX2u0izLU2hNb2JQe9/u/kyd6icJO+Rj78VuO6KUIuDlvl+PLaWtlnpwNzMrYrJusrWs+tVS/RDRaOWw3rbuPn53eqOw/zH+SuGd8Y3xmbhmX8YuwYj4xnxkvDMSLjT+Mv4+b/258u/H9xg+
Z9OqV3OamUfhs/PQf0+BmxA=</latexit>
−1
3
2obltV2BokPaZEnRpG7rtEnR2AsombZVS6JA0ZfY1TfZ6/ad9mEGjJRk+KRg7Uz4ITk738OqaPDm+3QcyPWbP597ZNP/v8iy+vf1X6+ptv/t+68YPpxGZUAe/dohH6BsbRdhzA/yauczDb0KkW97+Mwe7wl+NsU0cknwil2GuO
ejYeAOXAcx3nSxtfV+/v5hd0CRs7TipdWML7bKzUYz+ZiwYGWFspF9XlzcuHnS7RNn4uOAOR6KonOrGbLeElHmOh6OS91JhEPkjNEQn/NigHwc9ZbJ0GOzwlv65oBQ/g2YmbSqFkvkR9Glb3Olj9go0ploLGLnEza431u6QThOHDSj
gYTz2TEFHEw+y7FDvMueQE51OVjNZ0R4nFgPFq5Xpg7XsSlUsU8RgzP+RB9HwV9rgnwLKsu/6jmP/ho3CQt3wUxrdU+geoPsK3Qf0QKEHgB4q9BDQJwp9AuhThT4F9Fihx4A+U+gzQNsKbQPaUWgH0BOFngD6SqGvAD1V6CmgZwo
941TDg1Wk+XQYJ6HWn7mTe+iLtGLb4iHASDq5oVypPevkBqZp82IbZVp7sES6J9uW0AbQkdABEuIARwMJB0AOpJwBKAroQvgOwnfATiWcAxgIGEAoC+hD2AoYQglZACGEkY6XDEjxCTNXoHqbSwxTAmYQzAOcSzgG8lPASwIWECx
0uNKg/sHgkm3h9sQITb9mN3KEPks4bUtTnwgDZHuK565EhdLXgkRHOFhdpkMYwOIsRi8+tniIqW4WqQHUQMls7Wh2haNZ5mimOtI0RzI8R8BW0KwxNmrhYhP4lPgl6bBEL3CLFOgyEcYSawkaROYk0CZyRYwx4JOEcVh5Hok0Kwp
TSkdEdDvymLtXPjSex8iXlIkaR3MbBSGqiqtw0AQRUML5mOSjVJSmJ02G2GmqtI6UKGJquE1kHh5N4siL8THQ1WU1vVQErHDEX4qE4c2uMWRsYrB0kdmKgYrBZmrGKwV5FLFYLUgyXKx5mL10BU5AVw0iJ3GSfFRECm2ihRzvT7eFKh
HdCgkeM6WogiwnGPgxHUkGZi5B5KB81RbMjCp30r2VmcvJXupsz3JwNmvIxk4CU2vnKvTzXP18HgVtsNjELUXE7ElH/2eKfhZJ46r1cXOji7kW5p41zO3j9PFCOQCV/g5BdhtuYLmFjOdznL2s2S0+5jfIyh+xsPyPMQUMUK7mPJzC
R3EhfQWjyPme5X4U6p0+3g6jyrMi6uHAnk5hl0+xMBaI1js21auIxFDCoS9u5MpPu5GjqURTKlCfOBqKBTQnFE16DvYW71BXkz20xH/gojn2A7mTkVc5+imRkxHJoRZtr9hN9yhjTZFUumyafk0A2Si03oOmxCcXwe8bMnfths
tFo9npBjLAxsXF2MbdXpSV9tInvg/i/J70vdF1xTzBbBKaYvEwE9f8mldK7BC/3jJ+P0uDznDE7LK1TAu7btmq1bq7gevFUWQtJdbtfLPCVtWxBD7PFLn9V9rJhu5zrhnVp/vmPX67dvVsrXzQAjcwbxLsYfm5Vb6v4u9CK89rt
1B268GhvhOws1+RvXTvfZA6/iw707hNC+G/DrZNIzYma1WvuPMiT9po07iej0izbv2WCxv1UkscqLTI/UQT1AvuTVf1Df2fnKWKuvSQ4youHE7p4AjeGyl3Gq0avxb5OJxK3MhNHUpSpXJ6xKJVopFywemlsytjcm1Obs+LKU+N
qfsj08q6qUsgQuTCfr6mSy+EvYnEiFfa7TKLUtTKENvbYlB73+7+RJ36Jwk7xGPvxW47oJQ+4OW+X48toa2WunArGZW+WRdZ+vFVtnSf3SDhdNWw7rXuPvyTn3cfaD3HXjR+Mno2pYxi/GrvHEeG8Nhxjavxh/Gn8dfOf7fL
2re1aKv3kWmZz08h9tu/+CyTEaMs=</latexit>
|x| = 1
10
1
2
znytXP/jwo48/ufZp5bPv/jyq+s3vj6OyYQ6+KVDfEJf2SjGvhfil8xjPn4VUYwC28cn9nhX8JNzTGOPhC/YRYT7ARqGnus5iPGmXr3nUuQsrGRxOzm7Xm02munHhAUrL1SN/Ps7MbNbm9AnEmAQ+b4KI5PrWbE+gtEmef4OKn0JjGOkDNGQ3zKiyEKcNxfpINOzBpvGZguofwbMjNtVS0WKIji8DmygCxUawz0VjGTifMvdfeGE0YTh0so7ciW8yYoImAOPYof5F7yAHOrxsZrOCPEwMB6nQi/MG8+TSqVmHiGZ3yIQYDCAdeEeJpXFr3gQcL/8FE4yF8SBKN7ip0
F9A9he4Buq/QfUAPFHoA6COFPgL0sUIfA3qk0CNAnyj0CaBthbYB7Si0A2hXoV1AXyj0BaDHCj0G9EShJ5xq2F1Gms+GcRpq/Zk7hYc+yq2LR4CjKRTGMql2pNOYWCati2Ua613QXSPdm2hDaAjoQOgFhCDKDrSuoCOpJwBKAnoQfgGwnfADiWcAxgKGEIYCBhAGAkYQglZACGEsY63DEUjxCTNXoHs6lh3MApxJOAZxJOAPwQsILAOcSznU416D+wOKRbOIPxApM/EUv9oYBSDp/SNGAC0Nk+4jnrk+G0NWcR0Y4m59lQRrD4MxHLDm1+oqoapWqQtVRCXTlaPpJY6mu
aOp6kjTHMrwHAIHbQnBEmcvFyI+iY+BX5oFQ/QKs0yBIh9hJLGSpE1gTkJlJlvAHAt6jiOYs8noWZNaUbpiIB+lxYr58KX3vsQ8ZIiyepgZqMoUlVZHQaCKBpaMh/TbJS0uy02QgzVZXVgQpNVA2vgcQrupmXeSEBHqirK6HkogdjvDzmDiuwS2OjFUMlj4yVTFYKchMxWCtIBcqBqsFSZeLFRerh64oCOCiQewsToqPkixZaSY5w/wukA9oEMhwTO2EWA5RwDJ65DycDM3ZcMnKfakoFJ/Vqy1zp7Ltlzne1KBs5+HcnASej80rl6vn6uHhwtw3ZwBKL2bCK25M/cg
U/6yTJ5uZ8a0sX8i1NvOupN8DZYgRygSuCgLstlxBC4uZTqcF+2k62j3M7xEUP+FheRphihihPUz5uYS6Sn9kcR871K/KnUegPsijrPqpyLK0cKuXkOvcEQ4FoTRJzpZr4DIUM6rJ2rsyle17saCrRlAnUJ46HYgEtCEWTHvoO9pdvkBfT/bTAUbDEKCDYTmdOzdyjaGrGDEdmjJl2P+G3nCFNd8WKafIpOfTC9GITeQ6bUJycxvzsiX9tNlqtPk/IMRYGtg4e5jbq9KPtrU9/7bOL8rfa91XTO7mE0iUyweZuqaX/MqR3iF1vG72dZ0BmOmV21Flhx6ta29u9ndD
zk5oiSNure3q7ZQtamKIAx6p0/pv2yYbec64b24+3TLr9Vu3NqvW1n0h8NxZj2Ifzaqt7H8P+zFeVy567leshwb4TsLNfkb1073+QMv48O9O4TQgRfy62TaM2LmZnO7uXW/SNor0riXjkqzbP+eCxr3MkRq7TMvKsI6iX23WX39TX9d08yRV16KHAVl46gXVDAETy0Mm41Wtv8W+biYSt3ITR1KcqU6esSiVZJRMs7pbMrbXJtT673i2l3jen7PdPKuylLIELk0n6/JksvhLWJ9IpX2u0izLU2hNb2JQe9/u/kyd6icJO+Rj78VuO6KUIuDlvl+PLaWtlnpwNzM
rYrJusrWs+tVS/RDRaOWw3rbuPn53eqOw/zH+SuGd8Y3xmbhmX8YuwYj4xnxkvDMSLjT+Mv4+b/258u/H9xg+Z9OqV3OamUfhs/PQf0+BmxA=</latexit>
−1
3
97ZNP/v8iy+vf1X6+ptv/t+68YPpxGZUAe/dohH6BsbRdhzA/yauczDb0KkW97+Mwe7wl+NsU0cknwil2GuOejYeAOXAcx3nSxtfV+/v5hd0CRs7TipdWML7bKzUYz+ZiwYGWFspF9XlzcuHnS7RNn4uOAOR6KonOrGbLeElHmOh6OS91JhEPkjNEQn/NigHwc9ZbJ0GOzwlv65oBQ/g2YmbSqFkvkR9Glb3Olj9go0ploLGLnEza431u6QThOHDSjgYTz2TEFHEw+y7FDvMueQE51OVjNZ0R4nFgPFq5Xpg7XsSlUsU8RgzP+RB9HwV9rgnwLKsu/6jmP/ho3CQt3wU
xrdU+geoPsK3Qf0QKEHgB4q9BDQJwp9AuhThT4F9Fihx4A+U+gzQNsKbQPaUWgH0BOFngD6SqGvAD1V6CmgZwo941TDg1Wk+XQYJ6HWn7mTe+iLtGLb4iHASDq5oVypPevkBqZp82IbZVp7sES6J9uW0AbQkdABEuIARwMJB0AOpJwBKAroQvgOwnfATiWcAxgIGEAoC+hD2AoYQglZACGEkY6XDEjxCTNXoHqbSwxTAmYQzAOcSzgG8lPASwIWECx0uNKg/sHgkm3h9sQITb9mN3KEPks4bUtTnwgDZHuK565EhdLXgkRHOFhdpkMYwOIsRi8+tniIqW4WqQHUQMls7
Wh2haNZ5mimOtI0RzI8R8BW0KwxNmrhYhP4lPgl6bBEL3CLFOgyEcYSawkaROYk0CZyRYwx4JOEcVh5Hok0KwpTSkdEdDvymLtXPjSex8iXlIkaR3MbBSGqiqtw0AQRUML5mOSjVJSmJ02G2GmqtI6UKGJquE1kHh5N4siL8THQ1WU1vVQErHDEX4qE4c2uMWRsYrB0kdmKgYrBZmrGKwV5FLFYLUgyXKx5mL10BU5AVw0iJ3GSfFRECm2ihRzvT7eFKhHdCgkeM6WogiwnGPgxHUkGZi5B5KB81RbMjCp30r2VmcvJXupsz3JwNmvIxk4CU2vnKvTzXP18HgVtsNjELUXE7
ElH/2eKfhZJ46r1cXOji7kW5p41zO3j9PFCOQCV/g5BdhtuYLmFjOdznL2s2S0+5jfIyh+xsPyPMQUMUK7mPJzCR3EhfQWjyPme5X4U6p0+3g6jyrMi6uHAnk5hl0+xMBaI1js21auIxFDCoS9u5MpPu5GjqURTKlCfOBqKBTQnFE16DvYW71BXkz20xH/gojn2A7mTkVc5+imRkxHJoRZtr9hN9yhjTZFUumyafk0A2Si03oOmxCcXwe8bMnfthstFo9npBjLAxsXF2MbdXpSV9tInvg/i/J70vdF1xTzBbBKaYvEwE9f8mldK7BC/3jJ+P0uDznDE7LK1TAu7btm
q1bq7gevFUWQtJdbtfLPCVtWxBD7PFLn9V9rJhu5zrhnVp/vmPX67dvVsrXzQAjcwbxLsYfm5Vb6v4u9CK89rt1B268GhvhOws1+RvXTvfZA6/iw707hNC+G/DrZNIzYma1WvuPMiT9po07iej0izbv2WCxv1UkscqLTI/UQT1AvuTVf1Df2fnKWKuvSQ4youHE7p4AjeGyl3Gq0avxb5OJxK3MhNHUpSpXJ6xKJVopFywemlsytjcm1Obs+LKU+Nqfsj08q6qUsgQuTCfr6mSy+EvYnEiFfa7TKLUtTKENvbYlB73+7+RJ36Jwk7xGPvxW47oJQ+4OW+X48toa2W
WunArGZW+WRdZ+vFVtnSf3SDhdNWw7rXuPvyTn3cfaD3HXjR+Mno2pYxi/GrvHEeG8Nhxjavxh/Gn8dfOf7fL2re1aKv3kWmZz08h9tu/+CyTEaMs=</latexit>
|x| = 1
10
Figure 7.4 Left: The circle |x| = 1/10 can be expanded to |x| = 1/2 by intro-
ducing a circle around x = −1/3. This results in an extra residue integral which
is exponentially negligible. Right: Alternatively, we can expand from |x| = 1/10
to hit x = 1/2 while stopping the increase in an arbitrarily small circle around
x = −1/3.
residue theorem then implies
an,n = 1
2πi
Z
|x|=1/2
1
1 + 3x
dx
xn+1(1 −x)n+1 + 1
2πi
Z
|x+1/3|=ε
1
1 + 3x
dx
xn+1(1 −x)n+1
= 1
2πi
Z
|x|=1/2
1
1 + 3x
dx
xn+1(1 −x)n+1 −Res
x=−1/3(x + 1/3)−1
1/3
xn+1(1 −x)n+1
= 1
2πi
Z
|x|=1/2
1
1 + 3x
dx
xn+1(1 −x)n+1 −1
3
 9
4
!n+1
,
and a change of variables yields the saddle point approximation
an,n = 4n
2π
Z π
−π
1
(1 + 3eiθ/2)(1 −eiθ/2)e−niθ−n log(2−eiθ)dθ −1
3
 9
4
!n+1
=
4n
√πn
 2
5 + O
 1
n
!!
.
Method Two: In general we cannot work around other singularities by tak-
ing residues in such an explicit manner. Although this means we cannot get
an explicit representation for error terms coming from other singularities, all
we really need to determine dominant asymptotics is to bound any potential
asymptotic contributions from these singularities. The only factor of the inte-
grand in (7.6) that depends on n is x−n(1−x)−n, so when n is large the modulus
of the integrand is well approximated by enh(x), where
h(x) = −log |x| −log |1 −x|.
7.1 Some illustrative examples
179
Points with smaller height h make the integrand of (7.6) exponentially smaller,
so up to an exponentially negligible error we can ignore points with height
bounded below h(1/2) = log 4. Since h(−1/3) = log(9/4) we could proceed
by expanding the circle |x| = 1/10 to the circle |x| = 1/2 while stopping in
a tubular shape around x = −1/3 (see Figure 7.4 right). The integral over
the resulting curve can be truncated to a neighborhood of x = 1/2 in |x| =
1/2 while introducing an exponentially negligible error. The integral over this
neighborhood of x = 1/2 is again a saddle point integral.
Method Three: Although Method Two is more general than Method One,
it still requires that we know how to explicitly deform around V, which is
not always possible. We thus move to an even more general argument, which
will be fully described below. The key is to use the local geometry of V to
describe how to move the domain of integration |x| = 1/10 to heights below
h(1/2) = log 4, except in a neighborhood of x = 1/2, while avoiding V. This
is accomplished using a gradient ﬂow. Writing x = a + ib for real variables a
and b, so that |x| =
√
a2 + b2, we see that
h(a, b) = h(a + ib) = −log

a2 + b2
/2 −log

(1 −a)2 + b2
/2.
We want to move an arbitrary point aθ +ibθ = eiθ/10 on our starting circle |x| =
1/10 down to points on V of lower height with respect to h. Since (∇h)(a, b)
gives the direction of greatest increase of h, we want to locally move a point
(aθ, bθ) along the direction −(∇h)(aθ, bθ). In other words, we want to solve the
ﬁrst-order diﬀerential system of equations
 a′
θ(t)
b′
θ(t)
!
= −∇h(aθ(t), bθ(t)),
aθ(0) = cos(θ)/10,
bθ(0) = sin(θ)/10
for aθ(t) and bθ(t). Figure 7.5 shows the trajectories of points under this (neg-
ative) gradient ﬂow. Here it can be veriﬁed in a computer algebra system that
under the ﬂow all points will go below height h(1/2) = log 4, except in a
neighborhood of x = 1/2. Near x = 1/2 the ﬂow approaches a vertical line, ul-
timately resulting in a saddle point integral. The key reason this method can be
generalized is that techniques from Morse theory allow us to know when such
a ﬂow exists, and characterize the resulting domains of integration, without
having to actually compute them.
◁
In our last example the non-smooth point did not aﬀect dominant asymp-
totics, but this will not always be the case.
Example 7.4 (Dealing with Multiple Points). Consider now asymptotics in the
180
Overview of analytic methods for multivariate GFs
Figure 7.5 Left: The gradient ﬂow of |x| = 1/10 at three points in time, plotted on
C2 \ {0, 1} when arranged by height h(x) = h(a + ib). Right: The curves under the
ﬂow plotted in the complex plane.
main diagonal direction r = (1, 1) of the power series expansion of F(x, y) =
1/Q(x, y) with Q(x, y) = (1 −x −y)(1 −3x). The factor 1 −x −y is the same
as in the above examples, but having the second factor change from 1 + 3x to
1 −3x moves the non-smooth point to (1/3, 2/3). Because the height h(x, y) =
−log x −log y is now larger at (1/3, 2/3) than (1/2, 1/2), we can no longer
easily rule out the non-smooth point. In fact, following Method One from the
last example shows
an,n = 1
2πi
Z
|x−1/3|=ε
1
1 −3x
dx
xn+1(1 −x)n+1 + 1
2πi
Z
|x|=1/2
1
1 −3x
dx
xn+1(1 −x)n+1
= Res
x=1/3(x −1/3)−1
1/3
xn+1(1 −x)n+1 + 1
2πi
Z
|x|=1/2
1
1 + 3x
dx
xn+1(1 −x)n+1
= 1
3
 9
2
!n+1
+ O(4n).
More generally, if V is no longer a manifold then we compute a Whitney strat-
iﬁcation, partitioning V into a ﬁnite collection of manifolds such that the local
geometry of V is consistent near the points in any ﬁxed element of the par-
tition. We then perform an analysis similar to the smooth case on each of the
manifolds, obtaining a set of equations for each manifold that characterizes
the points of interest for our asymptotic calculations. The asymptotic contri-
bution of such a point depends on the geometry near the singularity. In this
text we study singularities where V is locally smooth (in Chapter 9), looks
like the union of hyperplanes (in Chapter 10), or looks like a cone point (in
7.1 Some illustrative examples
181
Figure 7.6 The gradient ﬂow of |x| = 1/10 at three points in time, plotted on
C2 \ {0, 1} when arranged by height h(x) = h(a + ib). Left: The ﬂow on V1−y−xy.
Right: The ﬂow on V1−x−y−x2y.
Chapter 11). Studying ﬂows on general algebraic varieties requires us to adapt
tools from stratiﬁed Morse theory.
◁
Exercise 7.2. Sketch the vector ﬁeld −(∇h)(a, b) on the right-hand side of
Figure 7.5.
Gradient ﬂows form an important component of our analytic toolbox. In-
deed, rather than computing a ﬂow for each example, standard results in Morse
theory usually guarantee the existence of ﬂows that push domains of integra-
tion down to points where saddle point approximations can be computed. Un-
fortunately, these results require the height map to be proper (meaning that the
set of points with height in a closed interval is compact). Because this proper-
ness condition is usually not satisﬁed in our setting, it is possible for the desired
ﬂows not to exist.
Example 7.5 (Critical Points at Inﬁnity). Consider the diagonal sequences
an,n of the power series expansions of 1/A(x, y) and 1/B(x, y), where A(x, y) =
1−y−xy and B(x, y) = 1−x−y−x2y. The negative gradient ﬂows of the circle
|x| = 1/10 on VA and VB are shown in Figure 7.6. Because y = 1/(x + 1) on
VA, the product xy = x/(x + 1) →1 as x →∞, and thus the height function
h(x, y) = −log |x|−log |y| →0 as x →∞on VA. Since h(x, y) can stay bounded
as (x, y) goes to inﬁnity, the height function is not proper. As seen in the left
of Figure 7.6, the circle |x| = 1/10 stays at bounded height but never reaches a
saddle. In fact, VA contains no saddles, and we say that it has a critical point
at inﬁnity.
182
Overview of analytic methods for multivariate GFs
Similarly, because y = (1 −x)/(1 + x2) on VB, the height function h(x, y)
approaches zero as x →∞on VB. However, on VB the circle |x| = 1/10 does
ﬂow to a saddle point of height greater than zero. Again we have a critical
point at inﬁnity, but this time it is of lower height than an actual saddle point
on the variety. Thus, non-properness of the height function does not preclude
an asymptotic analysis, as we can ignore points of height bounded below the
saddle point if we care only about dominant asymptotic behavior.
◁
In Section 7.5 we discuss computable conditions, often satisﬁed in practice,
that imply the conclusions of Morse theory we require apply even without a
proper height function.
Exercise 7.3. Let Q(x, y) = 1−x−y−x2y2 and hr(x, y) = −r1 log |x|−r2 log |y|
be the height function corresponding to the r-diagonal sequence (ar1n, r2n).
Prove that when r = (2, 1) the height function hr(x, y) approaches a ﬁnite
limit as y →∞and x →0, and evaluate the limit. Prove that when r = (1, 1)
the height function hr(x, y) has no ﬁnite limit as either x or y goes to inﬁnity.
