---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-015-41-poisson-approximation-of-a-sum-of-independent
section_title: "Poisson approximation of a sum of independent Bernoulli variables"
section_number: 4.1
pages: 38-41
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
variables
As in Example 1.5, we consider a sum Xn = Pn
j=1 B(pj) of independent
Bernoulli random variables, with P∞
j=1 pj = +∞and P∞
j=1(pj)2 < +∞.
The corresponding Fourier transforms are:
c
µn(ξ) = eλn(eiξ−1) ψn(ξ)
with ψn(ξ) =
n
Y
j=1
(1 + pj(eiξ −1)) e−pj(eiξ−1).
It is convenient to have an exact formula for the expansion in Laurent series
of the deconvolution residues ψn. Denote
p1,n = 0
and
pk⩾2,n =
n
X
j=1
(pj)k.
One has
ψn(ξ) =


n
Y
j=1
(1 + pj(eiξ −1))

e
−Pn
j=1 pj(eiξ−1)
= exp


n
X
j=1
log(1 + pj(eiξ −1)) −pj(eiξ −1)


TOME 70 (2020), FASCICULE 3
1152
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
= exp


n
X
j=1
∞
X
k=2
(−1)k−1
k
(pj(eiξ −1))k


= exp
 ∞
X
k=1
(−1)k−1
k
pk,n (eiξ −1)k
!
.
Denote P the set of integer partitions, that is to say ﬁnite non-increasing
sequences of positive integers
L = (L1 ⩾L2 ⩾· · · ⩾Lr > 0).
If L is an integer partition, we denote |L| = Pr
i=1 Li; ℓ(L) = r; mk(L) the
number of parts of L of size k; and zL = Q
k⩾1 kmk(L) mk(L)!, which is the
size of the centralizer of a permutation of cycle-type L in the symmetric
group S|L|. The previous power series in eiξ −1 expands then as
ψn(ξ) =
X
L∈P
(−1)|L|−ℓ(L)
zL
pL,n (eiξ −1)|L|,
where pL,n = Qℓ(L)
i=1 pLi,n. Since pn,1 = 0, the sum actually runs over integer
partitions without part equal to 1. In particular, one has
ψn(ξ) = 1 −p2,n
2
(eiξ −1)2 + p3,n
3 (eiξ −1)3 + o(|ξ|3).
Consider then the basic approximation scheme (ν(0)
n )n∈N of the sequence of
random variables (Xn)n∈N, which is mod-Poisson convergent with param-
eters λn = Pn
j=1 pj and limit ψ(ξ) = Q∞
j=1(1 + pj(eiξ −1)) e−pj(eiξ−1). It
satisﬁes the hypothesis (H1) with r = 1 and
βn = −1
2 p2,n ;
β = −1
2 p2 = −1
2
∞
X
j=1
(pj)2.
By Theorems 3.3 and 3.6, if (Yn)n∈N is a sequence of Poisson random
variables with parameters λn, then
dL(Xn, Yn) =
p2
2
√
2π(λn)
3
2 + o

1
(λn)
3
2

;
dK(Xn, Yn) =
p2
2
√
2πe λn
+ o
 1
λn

.
The sequence of inﬁnitely divisible laws (ν(0)
n )n∈N also satisﬁes the hypoth-
esis (H2), since the expansion of ψn(ξ) given before is exact and can be
derived term by term. So, one can apply Theorem 3.11, and
dTV(Xn, Yn) =
2 p2
√
2πe λn
+ o
 1
λn

.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1153
This last estimate should be compared with the unconditional bound
dTV(Xn, Yn) ⩽2 p2,n
λn
= 2
Pn
j=1(pj)2
Pn
j=1 pj
stemming from the Chen–Stein method. On the other hand, we recover the
asymptotic formula for dTV(Xn, Yn) established by Deheuvels and Pfeifer
in [22], using only tools from harmonic analysis (instead of the semi-group
method developed in loc. cit.).
We now look at a higher order approximation scheme, namely, the ap-
proximation scheme (ν(2)
n )n∈N of order r = 2. It is deﬁned by the Fourier
transforms
d
ν(2)
n (ξ) = eλn(eiξ−1) 
1 −p2,n
2
(eiξ −1)2
.
Again, the hypotheses (H1) and (H2) are satisﬁed, this time with r = 2
and
βn = 1
3 p3,n ;
β = 1
3 p3 = 1
3
∞
X
j=1
(pj)3.
So, applying the main theorems of Section 3, we obtain
dL(Xn, ν(2)
n ) =
(
√
6 −2) p3
p
2π e3−
√
6 (λn)2 + o

1
(λn)2

;
dK(Xn, ν(2)
n ) =
p3
3
√
2π (λn)
3
2
+ o

1
(λn)
3
2

;
dTV(Xn, ν(2)
n ) = 2(1 + 4e−3
2 ) p3
3
√
2π (λn)
3
2
+ o

1
(λn)
3
2

.
Thus, (ν(2)
n )n∈N is asymptotically a better approximation scheme than the
simple Poisson approximation (ν(0)
n )n∈N. Moreover, if
+∞
X
j=n+1
(pj)2 = o

(λn)−9
4

= o





n
X
j=1
pj


−9
4 

,
then all the results of Theorem 3.16 apply, and in the previous estimates
one can replace ν(2)
n
by σ(2)
n , deﬁned by the Fourier transform
d
σ(2)
n (ξ) = eλn(eiξ−1)
 
1 −
P∞
j=1(pj)2
2
(eiξ −1)2
!
.
with ﬁxed residue.
TOME 70 (2020), FASCICULE 3
1154
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Remark 4.1. — Performing the same computations as in Lemma 3.8, one
can give an exact formula for ν(2)
n ({k}):
ν(2)
n ({k}) = e−λn (λn)k
k!

1 + β

1 −2k
λn
+ k(k −1)
(λn)2

,
here with β = −p2,n
2 . At ﬁrst sight this might look like an important
deformation of the Poisson measure with parameter λn, but note that in
the range k = λn(1+o(1)) where the Poisson law ν(0)
n
= P(λn) has its mass
concentrated, one has
1 −2k
λn
+ k(k −1)
(λn)2
= 1 −2(1 + o(1)) + (1 + o(1)) = o(1).
More generally, assume that the remainder of the series P+∞
j=n+1(pj)2 is
asymptotically smaller than any negative power of λn. If
d
σ(r)
n (ξ) = eλn(eiξ−1)
 r
X
k=0
ek (eiξ −1)k
!
,
with
ek =
X
L partition of size k
without part of size 1
(−1)|L|−ℓ(L)
zL
pL ;
pk⩾2 =
∞
X
j=1
(pj)k,
then the sequence of signed measures (σ(r)
n )n∈N forms a scheme of approx-
imation of (Xn)n∈N, with
dL(Xn, σ(r)
n ) = |er+1 Gr+1(zr+2)|
√
2π (λn)
r
2 +1
+ o

1
(λn)
r
2 +1

;
dK(Xn, σ(r)
n ) = |er+1 Gr(zr+1)|
√
2π (λn)
r+1
2
+ o
 
1
(λn)
r+1
2
!
;
dTV(Xn, σ(r)
n ) =
R
R |er+1 Gr+1(α)| dα
√
2π (λn)
r+1
2
+ o
 
1
(λn)
r+1
2
!
.
Thus, one can in this setting approximate the law of Xn up to any order
(negative power of λn).
