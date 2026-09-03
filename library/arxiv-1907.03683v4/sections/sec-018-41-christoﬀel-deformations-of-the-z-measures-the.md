---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-018-41-christoﬀel-deformations-of-the-z-measures-the
section_title: "Christoﬀel deformations of the z-measures. The z-measures on partitions were"
section_number: 4.1
pages: 18-25
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
introduced and extensively studied by Borodin and Olshanski in a series of papers, see e.g.
[7], [9], [10] and [11] and references therein. We ﬁrst brieﬂy explain their construcion. The
z-measures are deﬁned on the set Y of all partitions by:
Mz,z′,ξ(λ) = (1 −ξ)zz′ξ|λ|(z)λ(z′)λ
dim(λ)
|λ|!
2
.
They depend on three complex parameters, z, z′ and ξ and they are in general complex mea-
sures. The following choices ensure that it is a probability measure (see e.g. [10] Proposition
1.2 for a proof). First of all, the parameter ξ is real and lies in the open unit interval (0, 1).
Next, we distinguish three cases:
• [Principal series] The parameters z and z′ are conjugate to each other.
• [Complementary series] The parameters z and z′ are both real and belong to the
same interval (m, m + 1) where m ∈Z.
• [Degenerate series] One of the parameter, say z, is a non-zero integer, while the other
has the same sign and satisfy |z′| > |z| −1.
If z and z′ satisfy one of these three conditions, we say that they are admissible parameters.
The Christoﬀel defomations of the z-measure are then deﬁned as follows:
18
Deﬁnition 4.1. Let z, z′ be admissible parameters and Mz,z′,ξ the corresponding z-measure.
Let u1,...,uk, v1,...,vk ∈C be 2k complex numbers which satisfy:
k
Y
i=1
(x −ui + z)(x −vi + z′) > 0
for any x ∈Z. We deﬁne the Christoﬀel deformation of Mz,z′,ξ by:
Mk
z,z′,ξ(λ) = C
l(λ)
Y
j=1
k
Y
i=1
(λj −j −ui + z)(λj −j −vi + z′)Mz,z′ξ(λ),
(13)
where C is the normalisation constant chosen such that Mk
z,z′,ξ is a probability measure.
We ﬁrst have to focus on the degenerate case. For simplicity, we assume that z = N is
a positive integer and z′ > z −1. The z-measure Mz,z′ξ is then supported on the subset of
Young diagrams of length less than or equal to N, and we map Y on Conf(N) ⊂Conf(Z) via
λ 7→SN(λ) := {λi −i + N, i = 1, ..., N}.
The pushforward of the z-measure Mz,z′ξ under SN is then the N-th Meixner ensemble (see
e.g. [10], Proposition 1.4), i.e. the N-th orthogonal ensemble with weight
ωβ,ξ(x) = (β)xξx
x!
,
where β = z′ −z + 1 > 0. The corresponding orthogonal polynomials are the Meixner
polynomials deﬁned by:
Mn(x; β, ξ) = 2F1 (−n, −x; β; 1 −1/ξ), n ∈N.
Their leading coeﬃcient cn and their squared norm hn are given by
cn =

1 −1
ξ
n
n!(β)n
,
hn =
n!
ξn(1 −ξ)β(β)n
.
We now choose k real numbers u1, ..., uk ∈R\N which are not integers, and set vi = ui+β−1.
We thus have:
l(λ)
Y
j=1
k
Y
i=1
(λj −j −ui + z)(λj −j −vi + z′) =
Y
x∈SN(λ)
k
Y
j=1
(x −ui)2
from which we deduce that the pushforward of Mk
z,z′,ξ under SN is the Christoﬀel defor-
mation of the N-th Meixner ensemble at points u1, ..., uk as deﬁned in deﬁnition 2.4. As a
consequence, it deﬁnes a determinantal point process with an explicit kernel given by Propo-
sition 2.5. We now prepare a similar statement for other choices of admissible parameters z
and z′. For this aim, we will reproduce the analytic continuation argument developed in [10]
and [11], although the simpliﬁcations we need are less obvious. We will note: Z′ = Z + 1/2
the set of proper half integers. For a ∈Z′, x ∈Z′ and z and z′ admissible parameters that
19
are not in the degenerate case, we deﬁne:
ψa(x; z,z′, ξ) :=
Γ(x + z + 1/2)Γ(x + z′ + 1/2)
Γ(z −a + 1/2)Γ(z′ −a + 1/2)
1/2
ξ1/2(x+a)(1 −ξ)1/2(z+z′)−a
×
2F1

−z + a + 1/2, −z′ + a + 1/2; x + a + 1;
ξ
ξ−1

Γ(x + a + 1)
.
(14)
Observe that these functions are symmetric in z, z′. We now recall the following integral
representation, which is due to Borodin-Olshanski (see [10], Proposition 2.3):
ψa(x; z, z′, ξ) =
Γ(x + z + 1/2)Γ(x + z′ + 1/2)
Γ(z −a + 1/2)Γ(z′ −a + 1/2)
1/2 Γ(z′ −a + 1/2)
Γ(z′ + x + 1/2)(1 −ξ)
z′−z+1
2
× 1
2iπ
I
(1 −
p
ξω)−z′+a−1/2

1 −
√ξ
ω
z−a−1/2
ω−x−adω
ω .
(15)
Observe that it is now not obvious that such an expression is symmetric in z, z′, i.e. none of
its factor is symmetric in z, z′, but since expression (14) is, it has to be symmetric in z, z′. We
will also need the following Proposition, relating the functions ψa to Meixner polynomials,
which comes from Borodin and Olshanski ([10], Proposition 2.8).
Proposition 4.1. Suppose z = N ∈N and z′ = N + β −1. Suppose that:
˜x := x + N −1/2 ∈N,
n := N −a −1/2 ∈N,
are non-negative integers. Then, ψa(x; z, z′, ξ) is well deﬁned and we have:
ψa(x; z, z′, ξ) =
s
ωβ,ξ(˜x)
hn
Mn(˜x; β, ξ).
In what follows, we will sometimes omit the dependance on the parameters z, z′ and ξ
when the context is clear. The ﬁrst Theorem of this section states that, for any pair of
admissible parameters (z, z′), the modiﬁed z-measure given by formula (13) gives rise to a
determinantal point process with an explicit kernel expressed through the functions ψa and
their derivatives.
Theorem 4.2. For any admissible parameters z and z′ which are not in the degenerate case,
and any ui ∈R, vi = ui +z′ −z −1/2, the pushforward of the measure Mk
z,z′,ξ under the map
S : λ 7→{λi −i + 1/2} ∈Conf(Z′),
is a determinantal point process on Z′. Its correlation kernel is given by:
(16)
Kk
z,z′,ξ(x, y) :=
Cz,z′,k
Qk
i=1 |(x −ui)(y −ui)|
Bk,0(x; z, z′, ξ)Bk,1(y; z, z′, ξ) −Bk,0(y; z, z′, ξ)Bk,1(x; z, z′, ξ)
Dk(z, z′, ξ)2(x −y)
,
20
with
Bk,p(x) =

ψ−1/2+p(u1)
ψ−3/2+p(u1)
. . .
ψ−1/2−2k+p(u1)
...
...
...
ψ−1/2+p(uk)
. . .
. . .
ψ−1/2−2k+p(uk)
ψ′
−1/2+p(u1)
. . .
. . .
ψ′
−1/2−2k+p(u1)
...
...
...
ψ′
−1/2+p(uk)
. . .
. . .
ψ′
−1/2−2k+p(uk)
ψ−1/2+p(x)
. . .
. . .
ψ−1/2−2k+p(x)

,
p = 0, 1 ,
Dk =

ψ−1/2(u1)
ψ−3/2(u1)
. . .
ψ1/2−2k(u1)
...
...
...
ψ−1/2(uk)
. . .
. . .
ψ1/2−2k(uk)
ψ′
−1/2(u1)
. . .
. . .
ψ′
1/2−2k(u1)
...
...
. . .
ψ′
−1/2(uk)
. . .
. . .
ψ′
1/2−2k(uk)

,
and
Cz,z′,k =

ξ
ξ −1
1+2k Γ(z + 2k + 1)
Γ(z)
Γ(z′ + 2k)
Γ(z′ −1) .
Proof. The proof requires some steps. We ﬁrst establish in step 1 that the statement of the
Theorem holds for the degenerate series case. This fact is precisely formulated in Lemma
4.3 below. In step 2, we prove that quantities of interest involving the modiﬁed z-measures
have an analytic in ξ (and thus in √ξ), with polynomial coeﬃcients in (z, z′), for all values
of the admissible parameters. In step 3, we prove that a modiﬁcation of the kernel also have
an analytic expansion in √ξ with polynomials coeﬃcients in (z, z′). We here use the integral
reprensentations of the functions ψa. We conclude the proof in the ﬁnal step.
Step 1. Assume that z = N ∈N and z′ = N + β −1, and:
˜x := x + N −1/2,
˜y := y + N −1/2
˜ui ∈R,
˜vi = ˜ui + β −1,
i = 1, ..., k.
Then, by means of Propositions 2.5 and 4.1, and computations similar to those performed
at the beginning of the proof of Theorem 3.1, formula (16) makes sense and holds with:
˜ui = ui + N −1/2.
Indeed, the factor Cz,z′,k comes from the ratio
cN−1
cN+2k appearing in Proposition 2.5, while the
expressions for Ak, Bk and Dk are obtained from Proposition 2.5 after performing operations
similar to those in the proof of Theorem 3.1: the polynomials Mn are replaced by the func-
tions ψa thanks to homogeneity, and their derivatives M′
n are replaced by ψ′
a by operations
on rows. We resume this fact in the following Lemma:
Lemma 4.3. Suppose that z = N ∈N is a positive integer, β > 0 is a positive number and
that z′ = N + β −1. Let ˜u1, ..., ˜uk ∈R be k real numbers, and set:
˜vi = ˜ui + β −1,
i = 1, ..., k.
21
Let Mk
z,z′,ξ be the Christoﬀel deformation of the z-measure Mz,z′,ξ deﬁned by (13), with ui
(resp. vi) replaced by ˜ui (resp. ˜vi). We then have, for every n ∈N and every {˜x1, ..., ˜xn} ⊂N:
Mk
z,z′,ξ ({x1, ..., xn} ⊂S(λ)) = Mk
z,z′,ξ ({˜x1, ..., ˜xn} ⊂SN(λ)) = det
 Kk
z,z′,ξ(xi, xj)
n
i,j=1
where Kk
z,z′,ξ is deﬁned by (16) and:
xj = ˜xj −N + 1/2,
j = 1, ..., n
and
ui = ˜ui −N + 1/2,
i = 1, ..., k.
Step 2. For any values of the parameters z and z′, and for any n ∈N, and any {x1, .., xn} ⊂
Z′, Borodin and Olshanski ([10], Proposition 3.9) show that the quantity:
Mz,z′,ξ ({x1, ..., xn} ⊂S(λ)) ,
as a function of ξ, can be expanded in series around zero, and its coeﬃcients are polynomials
in (z, z′). As an immediate consequence, we also have that, viewed as a function of ξ, the
quantity:
Mk
z,z′,ξ ({x1, ..., xn} ⊂S(λ))
has an analytic expansion around zero with coeﬃcients that are polynomials in (z, z′).
Step 3. We will prove that the same statement holds for a slight modiﬁcation of the kernel
Kz,z′,ξ(x, y). We ﬁrst assume that z and z′ are admissible parameters not in the degenerate
series case. Following [10] (or [11]), we deﬁne:
fz,z′(x) =
Γ(x + z′ + 1/2)
p
Γ(x + z + 1/2)Γ(x + z′ + 1/2)
(17)
where x ∈Z′. By the assumptions on z and z′, this function is well deﬁned. Indeed, the
Gamma functions are well deﬁned and the fact that:
Γ(x + z + 1/2)Γ(x + z′ + 1/2) > 0
allows to deﬁne the square root. We also assume that u1, ...uk are such that fz,z′(x) is well
deﬁned for x ∈{u1, ..., uk}. Observe that interchanging z and z′ corresponds to turning f
into 1/f. We will also use the notation:
Ia(x; z, z′, ξ) =
1
2iπ
I
(1 −
p
ξω)−z′+a−1/2

1 −
√ξ
ω
z−a−1/2
ω−x−adω
ω
for any a ∈Z′ and x ∈Z′ ∪{u1, ...uk}. By means of the integral representation (15), we can
decompose:
ψa(x; z, z′, ξ) = (1 −ξ)
z−z′+1
2
fz,z′(x)
fz,z′(−a)Ia(x; z, z′, ξ)
(18)
Since the initial deﬁnition (14) is symmetric in (z, z′), we can also write:
ψa(x; z, z′, ξ) = (1 −ξ)
z′−z+1
2
fz,z′(−a)
fz,z′(x) Ia(x; z′, z, ξ),
(19)
22
Similarly, we have for the derivatives:
ψ′
a(x; z, z′, ξ) −f ′
z,z′(x)
fz,z′(x)ψa(x; z, z′, ξ) = (1 −ξ)
z−z′+1
2
fz,z′(x)
fz,z′(−a)I′
a(x; z, z′, ξ)
(20)
and:
ψ′
a(x; z, z′, ξ) + f ′
z,z′(x)
fz,z′(x)ψa(x; z, z′, ξ) = (1 −ξ)
z′−z+1
2
fz,z′(−a)
fz,z′(x) I′
a(x; z′, z, ξ).
(21)
Observe that the integrals Ia and their derivatives I′
a have an analytic expansion in √ξ with
coeﬃcients polynomial in (z, z′). We thus want to get rid of the factors involving fz,z′ and
fz′,z appearing in formula (16) through the functions ψa. We begin with the constant factor
D2
k. By (18) and (20) and their multiplicative structure, we can write
Dk = (1 −ξ)k(z′−z+1)
 k
Y
i=1
fz,z′(ui)
!2 2k
Y
i=1
fz,z′(−1/2 −i + 1)
!−1
× det



 I−1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k

I′
−1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k


.
But using (19) and (21), we see that Dk can also be expressed in the following way
Dk = (1 −ξ)k(z−z′+1)
 k
Y
i=1
fz,z′(ui)
!−2 2k
Y
i=1
fz,z′(−1/2 −i + 1)
!
× det



 I−1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k

I′
−1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k


.
Thus, writing the determinants Dk in D2
k in these two diﬀerent ways leads to:
D2
k = (1 −ξ)2k det



 I−1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k

I′
−1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k


det



 I−1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k

I′
−1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k


.
For the products Bk,0(x)Bk,1(y) and Bk,1(x)Bk,0(y), we also write the functions ψa and ψ′
a in
two diﬀerent ways, but now, we have to take care of the ”boundary factors”, i.e. the factors
that are not shared by both determinants. For instance, we have
Bk,0(x)Bk,1(y) = (1 −ξ)2k+1fz,z′(x)
fz,z′(y)
fz,z′(1/2)
fz,z′(−1/2 −2k)
× det





 I−1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k+1

I′
−1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k+1
 I−1/2−j+1(x; z, z′, ξ)

j=1,..2k+1




det





 I1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k+1

I′
1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k+1
 I1/2−j+1(y; z′, z, ξ)

j=1,...,2k+1




,
23
and
Bk,0(y)Bk,1(x) = (1 −ξ)2k+1fz,z′(x)
fz,z′(y)
fz,z′(−1/2 −2k)
fz,z′(1/2)
× det





 I1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k+1

I′
1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k+1
 I1/2−j+1(x; z, z′, ξ)

j=1,..2k+1




det





 I−1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k+1

I′
−1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k+1
 I−1/2−j+1(y; z′, z, ξ)

j=1,...,2k+1




.
This gives
Bk,0(x)Bk,1(y) −Bk,0(y)Bk,1(x) = (1 −ξ)2k+1fz,z′(x)
fz,z′(y)
×





fz,z′(1/2)
fz,z′(−1/2 −2k) det





 I−1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k+1

I′
−1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k+1
 I−1/2−j+1(x; z, z′, ξ)

j=1,..2k+1




det





 I1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k+1

I′
1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k+1
 I1/2−j+1(y; z′, z, ξ)

j=1,...,2k+1





−fz,z′(−1/2 −2k)
fz,z′(1/2)
det





 I1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k+1

I′
1/2−j+1(ui; z, z′, ξ)

i=1,...,k
j=1,...,2k+1
 I1/2−j+1(x; z, z′, ξ)

j=1,..2k+1




det





 I−1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k+1

I′
−1/2−j+1(ui; z′, z, ξ)

i=1,...,k
j=1,...,2k+1
 I−1/2−j+1(y; z′, z, ξ)

j=1,...,2k+1










=
(1 −ξ)2k+1
p
(z′ + 1)z′...(z′ −2k −1)(z + 1)z...(z −2k −1)
fz,z′(x)
fz,z′(y)
×


(z′ + 1)z′...(z′ −2k −1) det



 I−1/2−j+1(ui; z, z′, ξ)


I′
−1/2−j+1(ui; z, z′, ξ)

 I−1/2−j+1(x; z, z′, ξ)



det



 I1/2−j+1(ui; z′, z, ξ)


I′
1/2−j+1(ui; z′, z, ξ)

 I1/2−j+1(y; z′, z, ξ)




−(z + 1)z...(z −2k −1) det



 I1/2−j+1(ui; z, z′, ξ)


I′
1/2−j+1(ui; z, z′, ξ)

 I1/2−j+1(x; z, z′, ξ)



det



 I−1/2−j+1(ui; z′, z, ξ)


I′
−1/2−j+1(ui; z′, z, ξ)

 I−1/2−j+1(y; z′, z, ξ)






,
where we used:
a
bC + b
aD = a2C + b2D
ab
and direct simpliﬁcations due to the standard property of the Gamma function
Γ(A + 1) = AΓ(A).
Let us introduce the auxilliary kernel ˜Kk
z,z′,ξ(x, y):
˜Kk
z,z′,ξ(x, y) = fz,z′(y)
fz,z′(x)D2
k
p
(z′ + 1)z′...(z′ −2k −1)(z + 1)z...(z −2k −1)Kk
z,z′,ξ(x, y),
24
i.e.
˜Kk
z,z′,ξ(x, y)
=


(z′ + 1)z′...(z′ −2k −1) det



 I−1/2−j+1(ui; z, z′, ξ)


I′
−1/2−j+1(ui; z, z′, ξ)

 I−1/2−j+1(x; z, z′, ξ)



det



 I1/2−j+1(ui; z′, z, ξ)


I′
1/2−j+1(ui; z′, z, ξ)

 I1/2−j+1(y; z′, z, ξ)




−(z + 1)z...(z −2k −1) det



 I1/2−j+1(ui; z, z′, ξ)


I′
1/2−j+1(ui; z, z′, ξ)

 I1/2−j+1(x; z, z′, ξ)



det



 I−1/2−j+1(ui; z′, z, ξ)


I′
−1/2−j+1(ui; z′, z, ξ)

 I−1/2−j+1(y; z′, z, ξ)






,
and observe that it has an expansion in √ξ around zero with coeﬃcients that are polynomials
in (z, z′), since it is the case for the integrals Ia and their derivatives. Observe also that, for
any {x1, ..., xn} ⊂Z′, we have
det

˜Kk
z,z′,ξ(xi, xj)
n
i,j=1
= D2n
k
p
(z′ + 1)z′...(z′ −2k −1)(z + 1)z...(z −2k −1)
n det
 Kk
z,z′,ξ(xi, xj)
n
i,j=1 .
Final step. Our computations above remain valid for z and z′ belonging to the degenerate
series case, provided z > 2k+2. Assume now that we are in this case, and let {x1, ..., xn} ⊂Z′
be a ﬁnite subset of Z′. We have established the following equality between series in √ξ with
coeﬃcients that are polynomials in (z, z′):

det

˜Kk
z,z′,ξ(xi, xj)

i,j=1,...,n
2
= D4n
k ((z′ + 1)z′...(z′ −2k −1)(z + 1)z...(z −2k −1))n
× Mk
z,z′,ξ ({x1, ..., xn} ⊂S(λ))2 .
Indeed, the equality follows from the ﬁrst step and Lemma 4.3. The right hand side has an
analytic expansion in ξ with polynomial coeﬃcients in (z, z′), by step 2 and 3, while it also
holds for the left hand side by step 3. Since the set:
{(z, z′) ∈C2, z ∈N, z > 2k + 2 and z′ ∈R, z′ > z −1}
is a set of uniqueness for polynomials in two variables, the latter equality holds for all values
of (z, z′), in particular for all admissible values. This proves the Theorem.
□
