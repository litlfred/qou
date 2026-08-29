---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-003-22-the-weighted-bergman-spaces-and-kernels-let-ω
section_title: "The weighted Bergman spaces and kernels. Let Ωbe a domain in C, and let ω : Ω→R+"
section_number: 2.2
pages: 2-4
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
be a continuous function (ω is frequently called a weight). Here, we write R+ :=]0, +∞[ for the
positive half-axis. The space L2(Ω, ω) is the weighted L2-space on Ωwith ﬁnite norm
(2.2.1)
∥f∥2
L2(Ω,ω) :=
Z
Ω
| f(z)|2ω(z)dA(z),
and associated sesquilinear inner product
(2.2.2)
⟨f, g⟩L2(Ω,ω) :=
Z
Ω
f(z)g(z)ω(z)dA(z).
The corresponding weighted Bergman space A2(Ω, ω) is the linear subspace of L2(Ω, ω) consisting
of functions holomorphic in Ω, supplied with the inner product structure of L2(Ω, ω). Given
the assumptions on the weight ω, it is easy to check that point evaluations are locally uni-
formly bounded on A2(Ω, ω), and, therefore, A2(Ω, ω) is a norm-closed subspace of L2(Ω, ω).
As L2(Ω, ω) is separable, so is A2(Ω, ω), and we may ﬁnd a countable orthonormal basis
φ1, φ2, φ3, . . . in A2(Ω, ω). We then form the function K = KΩ,ω – called the weighted Bergman
kernel – given by
(2.2.3)
K(z, w) :=
+∞
X
j=1
φj(z)φj(w),
(z, w) ∈Ω× Ω,
and observe that for ﬁxed w ∈Ω, the function K(·, w) ∈A2(Ω, ω) has the reproducing property
(2.2.4)
f(w) = ⟨f, K(·, w)⟩L2(Ω,ω),
w ∈Ω.
Here, it is assumed that f ∈A2(Ω, ω). In fact, the weighted Bergman kernel K is uniquely
determined by these two properties, which means that K – initially deﬁned by (2.2.3) in terms
of an orthonormal basis – actually is independent of the choice of basis. Note that above, we
implicitly assumed that A2(Ω, ω) is inﬁnite-dimensional, which need not generally be the case.
If it is ﬁnite-dimensional, the corresponding sums would range over a ﬁnite set of indices j
instead.
2.3. The weighted polyanalytic Bergman spaces and kernels. Given an integer q = 1, 2, 3, . . .,
a continuous function f : Ω→C is said to be q-analytic (or q-holomorphic) in Ωif it solves the
partial diﬀerential equation
¯∂q
z f(z) = 0,
z ∈Ω,
in the sense of distribution theory. So the 1-analytic functions are just the ordinary holomorphic
functions. A function f is said to be polyanalytic if it is q-analytic for some q; then the number
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
3
q −1 is said to be the polyanalytic degree of f. By solving the ¯∂-equation repeatedly, it is easy to
see that f is q-holomorphic if and only if it can be expressed in the form
(2.3.1)
f(z) = f1(z) + ¯zf2(z) + · · · + ¯zq−1 fq(z),
where each fj is holomorphic in Ω, for j = 1, . . ., q. So the dependence on ¯z is polynomial of
degree at most q −1. We observe quickly that the vector-valued holomorphic function
V[f](z) := (f1(z), f2(z), . . ., fq(z)),
is in a one-to-one relation with the q-analytic function f. We will think of V[f](z) as a column
vector. In a way, this means that we may think of a polyanalytic function as a vector-valued
holomorphic function supplied with the additional structure of scalar point evaluations Cq →C
given by
(f1(z), f2(z), . . ., fq(z)) 7→f1(z) + ¯zf2(z) + · · · + ¯zq−1 fq(z).
We associate to f not only the vector-valued holomorphic function V[f] but also the function
of two complex variables
(2.3.2)
E[f](z, z′) = f1(z) + ¯z′ f2(z) + · · · + (¯z′)q−1 fq(z),
which we call the extension of f. The function E[f](z, z′) is holomorphic in (z, ¯z′) ∈Ω× C, with
polynomial dependence on ¯z′. To recover the function f, we just restrict to the diagonal:
(2.3.3)
E[f](z, z) = f(z),
z ∈Ω.
We observe here for the moment that
(2.3.4)
| f(z)|2 = V[f](z)∗A(z)V[f](z),
where the asterisk indicates the adjoint, and A(z) is the singular q × q matrix
(2.3.5)
A(z) =


1
· · ·
¯zq−1
...
...
...
zq−1
· · ·
zq−1¯zq−1


.
For some general background material on polyanalytic functions, we refer to the book [6].
As before, we let the weight ω : Ω→R+ be continuous, and deﬁne PA2
q(Ω, ω) to be the
linear subspace of L2(Ω, ω) consisting of q-analytic functions in Ω. Then PA2
1(Ω, ω) = A2(Ω, ω),
the usual weighted Bergman we encountered in Subsection 2.2. For general q = 1, 2, 3, . . ., it
is not diﬃcult to show that point evaluations are locally uniformly bounded on PA2
q(Ω, ω),
and therefore, PA2
q(Ω, ω) is a norm-closed subspace of L2(Ω, ω). We will refer to PA2
q(Ω, ω) as a
weighted q-analytic Bergman space, or as a weighted polyanalytic Bergman space of degree q −1. In
view of (2.3.4) and (2.3.5), we may view PA2
q(Ω, ω) as a space of vector-valued holomorphic
functions on Ω, supplied with the singular matrix-valued weight ω(z)A(z).
If we let φ1, φ2, φ3, . . . be an orthonormal basis for PA2
q(Ω, ω), we can form the weighted
polyanalytic Bergman kernel Kq = Kq,Ω,ω given by
(2.3.6)
Kq(z, w) :=
+∞
X
j=1
φj(z)φj(w),
(z, w) ∈Ω× Ω.
As was the case with the weighted Bergman kernel, Kq is independent of the choice of basis φj,
j = 1, 2, 3, . . ., and has the reproducing property
(2.3.7)
f(w) = ⟨f, Kq(·, w)⟩L2(Ω,ω),
w ∈Ω,
4
ANTTI HAIMI AND HAAKAN HEDENMALM
for all f ∈PA2
q(Ω, ω). Alongside with the kernel Kq, we should also be interested in its lift
(2.3.8)
E⊗2[Kq](z, z′; w, w′) :=
+∞
X
j=1
E[φj](z, z′)E[φj](w, w′),
(z, z′, w, w′) ∈Ω× C × Ω× C.
The lifted kernel E⊗2[Kq] is also independent of the choice of basis, just like the kernel Kq itself.
If PA2
q(Ω, ω) would happen to be ﬁnite-dimensional, the above sums deﬁning kernels should
be replaced by sums ranging over a ﬁnite set of indices j.
2.4. The polyanalyticBergman space in the model case of the unit disk with constantweight.
For q = 1, 2, 3, . . ., we consider the spaces PA2
q(D) := PA2
q(D, π−1) where the domain is the unit
disk D and the weight is ω(z) ≡1/π. The corresponding reproducing kernel Kq was obtained
Koshelev [22]:
(2.4.1)
Kq(z, w) = q
q−1
X
j=0
(−1)j
 q
j + 1
! 
q + j
q
!(1 −w¯z)q−j−1|z −w|2j
(1 −z ¯w)q+j+1
.
Its diagonal restriction is given by
(2.4.2)
Kq(z, z) =
q2
(1 −|z|2)2 .
Based on (2.4.1), the lift is Kq is then easily calculated,
(2.4.3)
E⊗2[Kq](z, z′; w, w′) = q
q−1
X
j=0
(−1)j
 q
j + 1
! 
q + j
q
!(1 −w′¯z′)q−j−1(z −w′)j(¯z′ −¯w)j
(1 −z ¯w)q+j+1
.
so that
(2.4.4)
E⊗2[Kq](z, z′; z, z′) = q
q−1
X
j=0
 q
j + 1
! 
q + j
q
!(1 −|z′|2)q−j−1|z −z′|2j
(1 −|z|2)q+j+1
= q(1 −|z|2)−2
q−1
X
j=0
 q
j + 1
! 
q + j
q
!1 −|z′|2
1 −|z|2
q−j−1 |z −z′|
1 −|z|2
2j
.
