---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function"
section_id: sec-003-3-the-bloch-wigner-function-dz-and-its-generaliz
section_title: "The Bloch-Wigner function D(z) and its generalizations"
section_number: 3
pages: 8-11
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
toc_source: inferred
doc_brief: "The Dilogarithm Function — 14 sections: Front matter; The dilogarithm function in geomet; Special values"
---
and its generalizations
D
The function Li2(z), extended as above to C ∖[1, ∞), jumps by 2πi log |z| as
z crosses the cut. Thus the function Li2(z) + i arg(1 −z) log |z|, where arg
denotes the branch of the argument lying between −π and π, is continuous.
Surprisingly, its imaginary part
D(z) = ℑ(Li2(z)) + arg(1 −z) log |z|
is not only continuous, but satisﬁes
(I) D(z) is real analytic on C except at the two points 0 and 1, where it is
continuous but not diﬀerentiable (it has singularities of type r log r there).
The above graph shows the behaviour of D(z). We have plotted the level
curves D(z) = 0, 0.2, 0.4, 0.6, 0.8, 0.9, 1.0 in the upper half-plane. The val-
ues in the lower half-plane are obtained from D(¯z) = −D(z). The maximum
of D is 1.0149 . . . , attained at the point (1 + i
√
3)/2.
The function D(z), which was discovered by D. Wigner and S. Bloch
(cf. [1]), has many other beautiful properties. In particular:
(II)
D(z), which is a real-valued function on C, can be expressed in terms of
a function of a single real variable, namely
D(z) = 1
2

D
z
¯z

+ D
1 −1/z
1 −1/¯z

+ D
1/(1 −z)
1/(1 −¯z)

(2)
The Dilogarithm Function
11
which expresses D(z) for arbitrary complex z in terms of the function
D(eiθ) = ℑ[Li2(eiθ)] =
∞

n=1
sin nθ
n2
.
(Note that the real part of Li2 on the unit circle is elementary:
∞

n=1
cos nθ
n2
=
π2
6 −θ(2π −θ)
4
for 0 ≤θ ≤2π.) Formula (2) is due to Kummer.
(III) All of the functional equations satisﬁed by Li2(z) lose the elementary
correction terms (constants and products of logarithms) when expressed
in terms of D(z). In particular, one has the 6-fold symmetry
D(z) = D

1 −1
z

= D

1
1 −z

= −D
1
z

= −D(1 −z) = −D
 −z
1 −z

(3)
and the ﬁve-term relation
D(x) + D(y) + D
 1 −x
1 −xy

+ D(1 −xy) + D
 1 −y
1 −xy

= 0,
(4)
while replacing Li2 by D in the many-term relation (1) makes the con-
stant C(f) disappear.
The functional equations become even cleaner if we think of D as being
a function not of a single complex number but of the cross-ratio of four such
numbers, i.e., if we deﬁne
D(z0, z1, z2, z3) = D
z0 −z2
z0 −z3
z1 −z3
z1 −z2

(z0, z1, z2, z3 ∈C).
(5)
Then the symmetry properties (3) say that D is invariant under even and anti-
invariant under odd permutations of its four variables, the ﬁve-term relation
(4) takes on the attractive form
4

i=0
(−1)i D(z0, . . . , zi, . . . , z4) = 0
(z0, . . . , z4 ∈P1(C))
(6)
(we will see the geometric interpretation of this later), and the multi-variable
formula (1) generalizes to the following beautiful formula:

z1 ∈f−1(a1)
z2 ∈f−1(a2)
z3 ∈f−1(a3)
D(z0, z1, z2, z3) = n D(a0, a1, a2, a3)
(z0, a1, a2, a3 ∈P1(C)) ,
12
Don Zagier
where f : P1(C) →P1(C) is a function of degree n and a0 = f(z0). (Equa-
tion (1) is the special case when f is a polynomial, so f −1(∞) is ∞with
multiplicity n.)
Finally, we mention that a real-analytic function on P1(C) ∖{0, 1, ∞},
built up out of the polylogarithms in the same way as D(z) was constructed
from the dilogarithm, has been deﬁned by Ramakrishnan [6]. His function
(slightly modiﬁed) is given by
Dm(z) = ℜ

im+1
 m

k=1
(−log |z|)m−k
(m −k)!
Lik(z) −(−log |z|)m
2m!

(so D1(z) = log |z1/2 −z−1/2|, D2(z) = D(z)) and satisﬁes
Dm
1
z

= (−1)m−1Dm(z) ,
∂
∂z Dm(z) =
i
2z

Dm−1(z) + i
2
(−i log |z|)m−1
(m −1)!
1 + z
1 −z

.
However, it does not seem to have analogues of the properties (II) and (III):
for example, it is apparently impossible to express D3(z) for arbitrary complex
z in terms of only the function D3(eiθ) = 
∞
n=1(cos nθ)/n3, and passing from
Li3 to D3 removes many but not all of the numerous lower-order terms in the
various functional equations of the trilogarithm, e.g.:
D3(x) + D3(1 −x) + D3

x
x −1

= D3(1) + 1
12 log
x(1 −x)
 log

x
(1 −x)2
 log

x2
1 −x
 ,
D3
x(1 −y)2
y(1 −x)2

+ D3(xy) + D3
x
y

−2D3
x(1 −y)
y(1 −x)

−2D3
1 −y
1 −x

−2D3
x(1 −y)
x −1

−2D3
y(1 −x)
y −1

−2D3(x) −2D3(y)
= 2D3(1) −1
4 log
xy
 log

x
y
 log

x(1 −y)2
y(1 −x)2
 .
Nevertheless, these higher Bloch-Wigner functions do occur. In studying the
so-called “Heegner points” on modular curves, B. Gross and I had to study
for n = 2, 3, . . . “higher weight Green’s functions” for H/Γ (H = complex
upper half-plane, Γ = SL2(Z) or a congruence subgroup). These are func-
tions Gn(z1, z2) = GH/Γ
n
(z1, z2) deﬁned on H/Γ × H/Γ, real analytic in both
variables except for a logarithmic singularity along the diagonal z1 = z2, and
satisfying ∆z1Gn = ∆z2Gn = n(n −1)Gn, where ∆z = y2(∂2/∂x2 + ∂2/∂y2)
is the hyperbolic Laplace operator with respect to z = x + iy ∈H. They are
The Dilogarithm Function
13
obtained as
GH/Γ
n
(z1, z2) =

γ∈Γ
GH
n(z1, γz2)
where GH
n is deﬁned analogously to GH/Γ
n
but with H/Γ replaced by H. The
functions GH
n (n = 2, 3, . . . ) are elementary, e.g.,
GH
2 (z1, z2) =

1 + |z1 −z2|2
2y1y2

log |z1 −z2|2
|z1 −¯z2|2 + 2 .
In between GH
n and GH/Γ
n
are the functions GH/Z
n
= 
r∈Z GH
n(z1, z2 + r). It
turns out [10] that they are expressible in terms of the Dm (m = 1, 3, . . . ,
2n −1), e.g.,
GH/Z
2
(z1, z2) =
1
4π2y1y2

D3(e2πi(z1−z2)) + D3(e2πi(z1−¯z2))

+ y2
1 + y2
2
2y1y2

D1(e2πi(z1−z2)) + D1(e2πi(z1−¯z2))

.
I do not know the reason for this connection.
