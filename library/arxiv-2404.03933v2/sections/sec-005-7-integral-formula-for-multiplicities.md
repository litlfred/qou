---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY"
section_id: sec-005-7-integral-formula-for-multiplicities
section_title: "Integral formula for multiplicities"
section_number: 7
pages: 18-21
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of"
---
7.1. Characters of tilting and Weyl modules. We define the character of an Uq(sl2)-
module V as the Laurent polynomial (see section 2.2) as
chV (x) =
X
j
dimVjxj
Here the sum is taken over weight subspaces of V and i ranges over all possible weights that
occur in V . We will treat x either as a formal variable, or, as a variable x =eiθ on a unit circle
in the complex plane. Because our characters are Laurent polynomials both make sense.
Theorem 2.3 and Theorem 2.6 give the following identifications and relations:
chL(k0)(x) = chW (k0)(x) = chT (k0)(x), 0≤k0≤l− 1,
chW (k1l+k0)(x) = chL(k1l+k0)(x) + chL(k1l−2−k0)(x), 0≤k0≤l− 2, k1∈ Z>0,
chT (k1l+k0)(x) = chW (k1l+k0)(x) + chW (k1l−2−k0)(x), 0≤k0≤l− 2, k1∈ Z>0,
chL(k1l+l−1)(x) = chW (k1l+l−1)(x) = chT (k1l+l−1)(x), k 1∈ Z>0.
Lemma 7.1. Characters of tilting modules are:
chT (k1l+k0)(x) =



xk0+1−x−(k0+1)
x−x−1 , if 0≤k0≤l− 1 and k1 = 0,
x(k1+1)l−x−(k1+1)l
x−x−1 , if k0 =l− 1 and k1∈ Z>0,
(xk0+1 +x−(k0+1))xk1l−x−k1l
x−x−1 , if 0≤k0≤l− 2 and k1∈ Z>0.
TENSOR POWERS 19
Proof. Weightk can be uniquely written as k =k1l +k0, where 0≤k0≤l− 1 and k1∈ Z≥0.
Characters for Weyl modules W (k) are
chW (k)(x) = xk+1−x−(k+1)
x−x−1 .
From Theorem 2.10 we know, that
(8) ch L(k1l+k0)(x) = chL(k1l)(x)chL(k0)(x),
and for 0≤k≤l− 2 or k =ml− 1, m∈ Z>0
(9) ch L(k)(x) = chW (k)(x) = chT (k)(x).
formulae (8) and (9) give
chW ((m+1)l−1)(x) = chL(ml)(x)chL(l−1)(x) = chL(ml)(x)chW (l−1)(x),
which gives
chL(ml)(x) = chW ((m+1)l−1)(x)
chW (l−1)(x) = x(m+1)l−x−(m+1)l
xl−x−l
and, concluding, we have
chL(k1l+k0)(x) = xk0+1−x−(k0+1)
x−x−1
x(k1+1)l−x−(k1+1)l
xl−x−l .
Note that this definition satisfies condition, given by short exact sequences in Theorem 2.3,
meaning that for k0̸=l− 1 we indeed have
chW (k1l+k0)(x) = chL(k1l+k0)(x) + chL(k1l−k0−2)(x).
Using exact sequences from Theorem 2.6, we can derive characters for the rest of the tilting
modules. Suppose k0̸=l− 1, k 1∈ Z>0, then
chT (k1l+k0)(x) = chW (k1l+k0)(x) + chW (k1l−k0−2)(x) =
= (xk0+1 +x−(k0+1))xk1l−x−k1l
x−x−1 ,
which concludes the proof. □
7.2. Scalar product and orthogonality. Consider the scalar product on functions on the
unit circle which is the radial part of the Haar measure onSU (2). For two functionsf,g :S1 =
{z =eiθ}→ C define
(10) ( f,g ) = 1
4π
Z 2π
0
f(eiθ)g(eiθ)|eiθ−e−iθ|2dθ
In particular it defines the scalar product on the space of Laurent polynomials in x which are
symmetric with respect to the Weyl reflection x7→x−1.
We will use the following notations for characters of irreducible representations L(k), Weyl
modules W (k) and tilting modules T (k).
chL(k1l+k0)(x) =χL
k1,k0, chW (k1l+k0)(x) =χW
k1,k0, chT (k1l+k0)(x) =χT
k1,k0.
20 ANNA LACHOWSKA, OLGA POSTNOV A, NICOLAI RESHETIKHIN, AND DMITRY SOLOVYEV
Characters of Weyl modules form an orthonormal basis in the space L2(S1) with respect to
the scalar product (10):
(χW
k1,k0,χW
m1,m0) =δk1,m1δm0,k0,
Scalar products between characters of tilting modules and Weyl modules are:
(χL
k1,k0,χT
m1,m0) =
(
δl−2−k0,m0(δk1+1,m1−δ0,m1), if k0̸=l− 1, k1∈ Z>0,
δk1,m1δk0,m0, otherwise.
In order to find an integral formula for multiplicities, similar to the one that exists for
compact Lie groups and is based on the orthogonality of characters of irreducible modules, let
us find the basis orthogonal to the basis of characters of tiltling modules.
Theorem 7.2. Functions
ηk1,k0 = (xk1l−1 +x−(k1l−1))(xk0−l+1−x−(k0−l+1))
(x−x−1)(xl−x−l) .
form a basis orthogonal to the basis of characters of tilting modules:
(χT
m1,m0,ηk1,k0) =δm1,k1δm0,k0
Proof. It is easy to find the decomposition of ηk1,k0 in the basis of Weyl modules:
ηk1,k0 =
∞X
j=0
(χW
k1+2j,k0−χW
k1+1+2j,l−2−k0).
Now let us use formulae expressing characters of tilting modules in terms of character of Weyl
modules, the formula above and the orthogonality of characters of Weyl modules. Fork0̸=l−1
and k1∈ Z>0 we have
(χT
m1,m0,ηk1,k0) =
∞X
j=0
((χW
m1,m0,χW
k1+2j,k0) + (χW
m1−1,l−2−m0,χW
k1+2j,k0)
−(χW
m1,m0,χW
k1+1+2j,l−2−k0)− (χW
m1−1,l−2−m0,χW
k1+1+2j,l−2−k0)) =
=
∞X
j=k1
(δm1,k1+2jδm0,k0 +δm1−1,k1+2jδl−2−m0,k0−
−δm1,k1+1+2jδm0,l−2−k0−δm1−1,k1+1+2jδl−2−m0,l−2−k0).
It is evident that this expression gives the right combination of Kroneker delta symbols:
(χT
m1,m0,ηm1,k0) =δm0,k0,
and for k1<m 1, again, 0. To resume, we have
(χT
m1,m0,ηk1,k0) =δm0,k0δm1,k1,
□
TENSOR POWERS 21
7.3. Multiplicities. Now we can use the basis ηk1,k0 to derive the integral formula for multi-
plicities of tilting modules.
The tensor product decomposition, implies the equality of characters:
(chT (1)(x))N =
X
0≤k0≤l−1,k 1∈Z≥0
M (l)
k1l+k0(N)chT (k1l+k0)(x).
Now that we have found the orthogonal basis, we can use it to derive the following integral
formula for the multiplicity
M (l)
k (N) = 1
4π
Z 2π
0
ηk1,k0(eiθ)(chT (1)(eiθ))N|eiθ−e−iθ|2dθ.
To compare this formula with Theorem 3.1, we use the definition ofηk1,k0, and decomposition
into a sign-alternating sum of characters of Weyl modules. Using the orthogonality of Weyl
characters we arrive to the expression
M (l)
k (N) =
∞X
j=0
(F (N )
k1l+2jl+k0−F (N )
k1l+2(j+1)l−2−k0
),
where F (N )
m are the same as in (3). Clearly, this agrees with Theorem 3.1. Moreover the
analytic derivation above is more or less a rephrasing of the algebraic proof of this theorem.
