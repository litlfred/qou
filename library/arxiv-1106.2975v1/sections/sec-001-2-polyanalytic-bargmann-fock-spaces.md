---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-001-2-polyanalytic-bargmann-fock-spaces
section_title: "Polyanalytic Bargmann-Fock spaces"
section_number: 2
pages: 8-12
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
An orthogonal basis. We will consider the Bargmann-Fock space A2
m,q(C) of poly-
analytic functions of degree ≤q −1, i.e., functions of the form
f(z) =
q−1
X
r=0
¯zr fr(z),
where all the components fr are entire, subject to the norm integrability condition
∥f∥2
A2
m,q(C) := ∥f∥2
L2(C,e−m|z|2) =
Z
C
|f(z)|2e−m|z|2dA(z) < +∞.
Here, as always, m > 0. We note that A2
1,1(C) is the standard Bargmann-Fock
space. As before, let Polm,n,q be the closed subspace of A2
m,q(C), deﬁned by the
condition that all the components fr are polynomials of degree less or equal to
n −1. Moreover, let Km,q and Km,n,q denote the reproducing kernels for A2
m,q(C) and
Polm,n,q, respectively. We will be concerned with the asymptotic behaviour of the
kernel Km,n,q, as m, n →+∞while n = m + O(1).
The Polyanalytic Ginibre Ensembles
9
Bargmann-Fock-spaces of polyanalytic functions have been considered in,
e.g., [25], where the reproducing kernels and orthonormal bases were identiﬁed.
We will attempt to supply a self-contained account of these basic matters.
To begin with, we identify an orthonormal basis for the space Polm,n,q. Here,
and later as well, we will need some standard properties of the classical orthogonal
polynomials. For details, we refer the reader to [16]. We need the generalized
Laguerre polynomials ((x)j := x(x + 1) · · · (x + j −1) is the Pochhammer symbol)
Lα
k (x) :=
k
X
i=0
(−1)i
 
k + α
k −i
!
xi
i! =
k
X
i=0
(−1)i (α + i + 1)k−i
i!(k −i)!
xi.
Proposition 2.1. For q ≤n, the following functions form an orthonormal basis for
Polm,n,q (i, r, j, k are all integer parameters):
e1
i,r(z) :=
r
r!
(r + i)! m(i+1)/2zi Li
r(m|z|2),
0 ≤i ≤n −r −1, 0 ≤r ≤q −1,
e2
j,k(z) :=
s
j!
(j + k)! m(k+1)/2¯zk Lk
j(m|z|2),
0 ≤j ≤q −k −1, 1 ≤k ≤q −1.
Proof. Clearly, all the above functions belong to the space Polm,n,q. Also, all the
functions e1
i,r are orthogonal to each of the functions e2
j,k, for the indicated ranges
of the indices, as can be seen by integrating along circles using polar coordinates.
Next, we show that the functions e1
i,r form an orthonormal set. Any two functions
there having diﬀerent parameter i are orthogonal, again by integrating along
circles using polar coordinates. So, we ﬁx i, and pick two indices r1, r2. We compute
the inner product of two such functions:
Z
C
e1
i,r1(z)e1
i,r2(z)e−m|z|2dA(z)
=
r
r1!
(r1 + i)!
r
r2!
(r2 + i)!mi+1
Z
C
|z|2iLi
r1(m|z|2)Li
r2(m|z|2)e−m|z|2dA(z)
=
r
r1!r2!
(r1 + i)!(r2 + i)!
Z ∞
0
Li
r1(t)Li
r2(t) tie−tdt = δr1,r2,
where the delta is in Kronecker’s sense. In a similar fashion, the functions e2
j,k
form an orthonormal set. So, the functions e1
i,r, e2
j,k together form an orthonormal
set. Next, the dimension of the span equals the total number of vectors, which we
calculate to nq, which equals the known dimension of the space Polm,n,q. The proof
is complete.
□
The reproducing kernel. For q ≤n, we conclude that the reproducing kernel of
Polm,n,q equals
(2.1)
Km,n,q(z, w) = m
q−1
X
r=0
n−r−1
X
i=0
r!
(r + i)!(mz ¯w)iLi
r(m|z|2)Li
r(m|w|2)
+ m
q−2
X
j=0
q−j−1
X
k=1
j!
(k + j)!(mzw)kLk
j(m|z|2)Lk
j(m|w|2).
10
Haimi and Hedenmalm
We note that by plugging in n = +∞in Proposition 2.1 we get an orthonormal
basis for the space A2
m,q(C). It follows that the same procedure of plugging in
n = +∞in the above expression for Km,n,q gives us Km,q, the reproducing kernel
for A2
m,q(C). What is probably less obvious is that Km,q may be written in a much
simpler form (this representation is, however, known; compare with [5], [19]).
Proposition 2.2. We have that
Km,q(z, w) = m
q−1
X
r=0
∞
X
i=0
r!
(r + i)!(mz ¯w)iLi
r(m|z|2)Li
r(m|w|2)
+ m
q−2
X
j=0
q−j−1
X
k=1
j!
(j + k)!(m¯zw)kLk
j(m|z|2)Lk
j(m|w|2) = m L1
q−1(m|z −w|2)emz ¯w.
Proof. It is clear from Proposition 2.1 that the double sum expression equals
Km,q(z, w), so the only thing that needs attention is the last equality. We ﬁrst do the
case w = 0. Many of the terms in the double sum vanish, so that we are left with
Km,q(z, 0) = m
q−1
X
r=0
L0
r(m|z|2)L0
r(0),
It is well-known that L0
r(0) = 1 and that Pq−1
r=0 Lα
r = Lα+1
q−1, so that the above reduces
to
Km,q(z, 0) = m L1
q−1(m|z|2).
We turn to general w ∈C. It is well-known that the transformation
Tw[ f](z) := e−1
2 m|w|2−mz ¯w f(z + w)
acts unitarily on A2
m,q(C); its adjoint is T∗
w = T−w. By the reproducing property of
Km,q(z, 0), we have, for f ∈A2
m,q(C),
e−1
2 m|w|2 f(w) = Tw[ f](0) =
Z
C
Tw f(z)Km,q(z, 0)e−m|z|2dA(z)
=
Z
C
f(z)T∗
w[Km,q(·, 0)](z) e−m|z|2dA(z)
= me−1
2 m|w|2 Z
C
f(z) L1
q(m|z −w|2)em¯zwe−m|z|2dA(z),
The claim that Km,q(z, w) = m L1
q−1(m|z −w|2)emz ¯w now follows immediately.
□
Szegö asymptotics. We shall show that the kernel Km,n,q(z, w) is approximated
well by Km,q(z, w), provided that z, w ∈D are rather close to one another. It will be
instrumental to study the asymptotic behavior of the partial sums
Ek(ζ) =
k
X
j=0
1
j!ζj
of the Taylor expansion of the exponential function. In [23], Szegö showed that
Ek(kζ)
ekζ
= 1 −
1
√
2πk
(ζe1−ζ)k
ζ
1 −ζ(1 + ϵ1
k(ζ)),
(2.2)
The Polyanalytic Ginibre Ensembles
11
provided that |ζe1−ζ| < 1 and |ζ| < 1, whereas
Ek(kζ)
ekζ
=
1
√
2πk
(ζe1−ζ)k
ζ
ζ −1(1 + ϵ2
k(ζ)),
(2.3)
provided that |ζe1−ζ| < 1 and |ζ| > 1. Here, we have the convergence
lim
k→+∞ϵ1
k(z) = lim
k→+∞ϵ2
k(z) = 0
uniformly on compact subsets of the respective domains. As for (2.3), the uniform
convergence ϵ2
k(ζ) →0 as k →+∞holds also in certain unbounded subdomains;
in particular, along the real line, we have uniform convergence on all intervals
[a, +∞[ with a > 1.
An elementary estimate of Laguerre polynomials. The following elementary
estimate of generalized Laguerre polynomials will prove useful.
Lemma 2.3. Suppose α is a positive real. Then, for k = 0, 1, 2, . . ., we have that
|Lα
k (x)| ≤1
k!(x + α + k)k,
x ∈[0, +∞[.
Moreover, with β := α + 2k −2 + 2
q
1
4 + (k −1)(k + α −1), we have that
1
k!(x −β)k ≤(−1)kLα
k (x) ≤1
k!xk,
x ∈[β, +∞[.
Actually, the related inequality |Lα
k (x)| ≤1
k!xk holds for all x ∈[ 1
2β, +∞[.
Proof. We begin with the estimate (0 ≤i ≤k is assumed)
(α + i + 1)k−i ≤(α + k)j.
Next, we note that for x ≥0 and k = 0, 1, 2, . . ., we have
Lα
k (x) =
k
X
i=0
(−1)k (α + i + 1)k−i
i!(k −i)!
xi =
X
i even
(α + i + 1)k−i
i!(k −i)!
xi −
X
i odd
(α + i + 1)k−i
i!(k −i)!
xi,
and in view of the above estimate,
X
i even
(α + i + 1)k−i
i!(k −i)!
≤
X
i even
(α + k)k−i
i!(k −i)! =
1
2 k!

(α + k + x)k + (α + k −x)k
,
and, analogously,
X
i odd
(α + i + 1)k−i
i!(k −i)!
≤
X
i odd
(α + k)k−i
i!(k −i)! =
1
2 k!

(α + k + x)k −(α + k −x)k
.
By discarding alternatively the even or odd contribution, we arrive at
|Lα
k (x)| ≤
1
2 k!

(x + α + k)k + |α + k −x|k
,
which is slightly stronger than the ﬁrst estimate.
It is well-known that Lα
k is a polynomial of degree k all of whose zeros are
distinct and real, and they all fall in the interval ]0, β[ (see 18.16.13 of [16]). The
second estimate follows immediately from this.
□
Approximation of the polynomial polyanalytic reproducing kernel. We estimate
the diﬀerence Km,n,q −Km,q.
12
Haimi and Hedenmalm
Proposition 2.4. Let z, w ∈C be such that |zw| ≤θ1 < 1 and |zw|e1−|zw| ≤θ2 < 1. Let
M be a positive real number. Then, as m, n →+∞while |m −n| ≤M,
|Km,n,q(z, w) −Km,q(z, w)| e−m|zw| ≤Cmqθm
