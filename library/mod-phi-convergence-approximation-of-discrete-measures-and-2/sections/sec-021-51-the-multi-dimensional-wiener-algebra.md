---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-021-51-the-multi-dimensional-wiener-algebra
section_title: "The multi-dimensional Wiener algebra"
section_number: 5.1
pages: 60-69
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
Definition 5.1. — The multi-dimensional Wiener algebra A = A (Td)
is the algebra of continuous functions on the d-torus whose Fourier series
converges absolutely. It is a Banach algebra for the norm
∥f∥A :=
X
n∈Zd
|cn(f)|,
where cn(f) denotes the Fourier coeﬃcient
cn(f) =
Z 2π
θ1=0
· · ·
Z 2π
θd=0
f(eiθ1, . . . , eiθd) e−iPd
i=1 niθi
dθ
(2π)d ,
where n = (n1, . . . , nd).
As in the case d = 1, if µ is a (signed) measure on Zd, then its total
variation norm is equal to ∥µ∥TV = ∥bµ∥A . On the other hand, one has the
analogue of Proposition 2.1:
Proposition 5.2. — There is a constant CH,d such that, for any f ∈
A (Td),
∥f∥A ⩽CH,d
sup
|α|⩽Kd
∥∂αf∥L 2,
TOME 70 (2020), FASCICULE 3
1174
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
where K = Kd = ⌊d
2⌋+ 1, and L 2 = L 2(Td) is the space of square-
integrable functions on the torus, endowed with the norm
∥f∥L 2 =
sZ 2π
θ1=0
· · ·
Z 2π
θd=0
|f(eiθ1, . . . , eiθd)|2
dθ
(2π)d .
Proof. — Note that Kd ⩾d+1
2
for any d ⩾1. We use again the Cauchy–
Schwarz inequality and the Parseval identity:
∥f∥A =
X
n∈Zd
|cn(f)| =
X
n∈Zd
 
1 + Pd
i=1(ni)2
1 + Pd
i=1(ni)2
!Kd
2
|cn(f)|
⩽
v
u
u
t X
n∈Zd
 
1
1 + Pd
i=1(ni)2
!Kd
v
u
u
u
t
X
n∈Zd
 
1 +
d
X
i=1
(ni)2
!Kd
|cn(f)|2
⩽
v
u
u
u
t X
n∈Zd
 
1
1 + Pd
i=1(ni)2
!d+1
2
×
v
u
u
t
X
α0+···+αd=Kd

Kd
α0, . . . , αd
 X
n∈Zd
|cn(∂(α1,...,αd)f)|2
⩽
v
u
u
u
t(d + 1)Kd X
n∈Zd
 
1
1 + Pd
i=1(ni)2
!d+1
2
sup
|α|⩽Kd
∥∂αf∥L 2,
hence the result since the series (CH,d)2 under the square root sign is
ﬁnite.
□
This inequality leads to the analogue of Theorem 2.3 in a multi-dimensio-
nal setting. We consider two measures µ and ν on Zd with Fourier trans-
forms
bµ(ξ) = eλφ(ξ) ψ(ξ);
bν(ξ) = eλφ(ξ) χ(ξ)
where φ(ξ) = Pd
i=1 φi(ξi). We assume φ to have moments at least up to
order Kd, and denote
φi(ξi) = i miξi −σ2
i ξ2
i
2
+ o(ξ2
i )
the Taylor expansion around 0 of each law on Z with Lévy exponent φi.
We ﬁx an integer r ⩾⌊d
2⌋such that
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1175
(1) the residues ψ and χ are (r + 1) times continuously diﬀerentiable
on Td;
(2) their Taylor expansions at 0 coincide up to order r:
∀|α| ⩽r, (∂α(ψ −χ)) (0) = 0.
A parameter ε ∈(0, 1) being ﬁxed, we also introduce the non-negative
quantities
βr+1(ε) =
sup
|α|=r+1
sup
ξ∈[−ε,ε]d |∂α(ψ −χ)(ε)|;
γ(ε) = sup
i∈[[1,d]]
sup
θ∈[−ε,ε]
|φ′′
i (θ) + σ2
i |;
M = −sup
i∈[[1,d]]
sup
θ∈[−π,π]
Re(φi(θ))
θ2

.
The quantity βr+1(ε) allows one to bound any derivative up to order (r+1)
of ψ−χ on [−ε, ε]d. Indeed, this is obvious for exponents α with |α| = r+1,
and otherwise,
|∂α(ψ −χ)(ξ)| =

Z 1
t=0
d
dt(∂α(ψ −χ)(tξ)) dt

⩽
d
X
i=1
|ξi|

Z 1
t=0
∂
∂αi
(∂α(ψ −χ)(tξ)) dt

 ,
which leads by descending induction on |α| to the bound
|∂α(ψ −χ)(ξ)| ⩽
 d
X
i=1
|ξi|
!r+1−|α|
βr+1(ε) ⩽(dε)r+1−|α| βr+1(ε)
for any ξ ∈[−ε, ε]d.
Theorem 5.3. — Fix ε ∈(0, 1) such that γ(ε) ⩽mini∈[[1,d]]
σ2
i
2 . There
exist some positive constants C1(d, c, φ) and C2(d, c, φ), that depend only
on d, the cut function c and the reference distribution φ, such that
∥bµ −bν∥A ⩽C1(d, c, φ)

1 + C2(d, c, φ)
√
λ

×
 
∥ψ −χ∥A
λK e−λMε2
4
ε
+ εr+1 βr+1(ε)
λ
d
4
√
λ + 1
ε
K!
for any ε ∈(0, 1) and any λ > 0.
TOME 70 (2020), FASCICULE 3
1176
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Since Proposition 5.2 involves higher order derivatives than Proposi-
tion 2.1, in order to prove Theorem 5.3, we shall use a smoother cut-
function than in the proof of Theorem 2.3. Thus, in the following, cd,ε(ξ) =
Qd
i=1 c( ξi
ε ), where c(x) is a function of one variable with values in [0, 1], that
is of class C Kd on R, with c(x) = 0 outside [−1, 1] and c(x) = 1 on [−1
2, 1
2].
In particular, cd,ε (respectively, 1−cd,ε) vanishes on [−π, π]d\[−ε, ε]d (resp.,
on [−ε
2, ε
2]d).
Lemma 5.4. — Under the assumptions of Theorem 5.3, there exists a
constant C(d, c, φ) such that

(1 −cd,ε) eλφ

A ⩽C(d, c, φ) λK
ε e−λMε2
4

1 + O
 1
λ

,
where the constant hidden in the O( · ) also depends only on d, c and φ.
Proof. — We combine Proposition 5.2 with the rules of diﬀerentiation of
functions of several variables:

(1 −cd,ε) eλφ

A
CH,d
⩽
sup
|α|⩽Kd
∥∂α((1 −cd,ε) eλφ)∥L 2([−π,π]d\[−ε
2 , ε
2 ]d)
⩽
sup
|α|⩽Kd
X
β⩽α
d
Y
i=1
αi
βi

∥∂α−β(1 −cd,ε)∥L 2 ∥∂β(eλφ)∥L ∞([−π,π]d\[−ε
2 , ε
2 ]d)
⩽2Kd
 
sup
|γ|⩽Kd
∥∂γ(1 −cd,ε)∥L 2
! 
sup
|β|⩽Kd
∥∂β(eλφ)∥L ∞([−π,π]d\[−ε
2 , ε
2 ]d)
!
.
Since the Lévy–Khintchine exponent φ is assumed to have the factorization
property, for any multi-index β,
∂β(eλφ) =
d
Y
i=1
∂βieλφi(ξi)
∂ξβi
i
,
and
∂neλφi(θ)
∂θn
= eλφi(θ)
n
X
k=1
Bn,k(λφ′
i(θ), λφ′′
i (θ), . . . , λφ(n−k+1)
i
(θ)),
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1177
where Bn,k(x1, . . . , xn+k−1) is the incomplete Bell polynomial of parame-
ters n and k, see [9]. More precisely,
Bn,k(x1, . . . , xn+k−1)
=
X
m1+m2+···+mn−k+1=k
m1+2m2+···+(n−k+1)mn−k+1=n
n!
Qn−k+1
i=1
(i!mi mi!)
(x1)m1 · · · (xn−k+1)mn−k+1
and
|Bn,k(x1, . . . , xn+k−1)| ⩽
 
sup
i∈[[1,n+k−1]]
|xi|
!k
S(n, k)
where S(n, k) = Bn,k(1, 1, . . . , 1) is the Stirling number of the second kind.
As a consequence,

∂neλφi(θ)
∂θn

 ⩽|eλφi(θ)| Tn(λ∥φi∥C n(T)) ⩽|eλφi(θ)| Tn(λ∥φ∥C n(Td)),
where Tn(x) = Pn
k=1 S(n, k) xk is the n-th Touchard polynomial, with
leading term S(n, n) xn = xn. Thus,
|∂βeλφ| ⩽|eλφ|
d
Y
i=1

Tβi(λ∥φ∥C βi(Td))

⩽|eλφ| (λ∥φ∥C K(Td))|β|

1 + O

1
λ∥φ∥C K(Td)

if |β| ⩽Kd. Now, if ξ /∈[−ε
2, ε
2]d, then one of the coordinates ξi has modulus
larger than ε
2, so |eφ(ξ)| ⩽e−Mε2
4 . We conclude that

(1 −cd) eλφ

A
⩽2Kd CH,d
 
sup
|γ|⩽Kd
∥∂γ(1 −cd,ε)∥L 2
!
(λ ∥φ∥C K(Td))K e−λ Mε2
4
+O( 1
λ ),
where the constant in the O( · ) only depends on d and the exponent φ.
Finally, as soon as γ̸ = 0, ∂γ(1 −cd,ε) = −
1
ε|γ| (∂γcd,1)( ξ
ε), so,
∥∂γ(1 −cd,ε)∥L 2 =
1
ε|γ|
sZ
[−ε,ε]d

(∂γcd,1)
ξ
ε


2
dξ
(2π)d
=
1
ε|γ|−d
2
sZ
[−1,1]d |(∂γcd,1)(θ)|2
dθ
(2π)d
= O

1
ε|γ|−d
2

.
TOME 70 (2020), FASCICULE 3
1178
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
We conclude by taking the maximal possible value |γ| = Kd, which gives
Kd −d
2 = 1 if d is even, and 1
2 if d is odd.
□
Lemma 5.5. — Under the assumptions of Theorem 5.3, there exists an-
other constant C(d, c, φ) such that

cd,ε (ψ −χ) eλφ

A
⩽C(d, c, φ) εr+1 βr+1(ε)
λ
d
4
√
λ + 1
ε
K 
1 + O
 1
√
λ

.
Again, the constant hidden in the O( · ) depends only on d, c and φ.
Proof. — The hypothesis on γ(ε) ensures that, for any index i ∈[[1, d]]
and any θ ∈[−ε, ε], Re(φ′′
i (θ)) ⩽−σ2
i /2 and |φ′′
i (θ)| ⩽2σ2
i . On the other
hand, as in the case d = 1 dealt with by Lemma 2.5, we can shift phases
by S(ξ) = i Pd
i=1 ξi⌊λmi⌋:

cd,ε (ψ −χ) eλφ

A
=

cd,ε (ψ −χ) eλφ−S

A
⩽CH,d
sup
|α|⩽Kd
∥∂α(cd,ε (ψ −χ) eλφ−S)∥L 2([−ε,ε]d)
⩽CH,d
sup
|α|⩽Kd


X
β+γ+δ=α
d
Y
i=1

αi
βi, γi, δi

∥∂βcd,ε ∂γ(ψ −χ)∥L ∞([−ε,ε]d)
× ∥∂δeλφ−S∥L 2([−ε,ε]d)

.
On the last line, we can bound ∥∂βcd,ε∥L ∞([−ε,ε]d) by C(d, c) ε−|β|, and
∥∂γ(ψ −χ)∥L ∞([−ε,ε]d) by βr+1(ε) (dε)r+1−|γ|. Thus,

cd,ε (ψ −χ) eλφ

A
is smaller than
C(d, c) εr+1 βr+1(ε)
×
sup
|α|⩽Kd

X
ρ+δ=α
d
Y
i=1
 αi
ρi, δi

ε−|ρ| ∥∂δeλφ−S∥L 2([−ε,ε]d)


where C(d, c) is some positive constant depending only on d and the cut
function c.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1179
To bound the norms ∥∂δeλφ−S∥L 2([−ε,ε]d), we use the same combinatorics
of Bell polynomials as in the previous lemma. Speciﬁcally, we have

∂n(eλφi(θ)−i⌊λmi⌋θ)
∂θn

⩽

eλφi(θ)

n
X
k=1
Bn,k(λφ′
i(θ) −i⌊λmi⌋, λφ′′
i (θ), . . . , λφ(n−k+1)
i
(θ))

 ,
and the variables of the incomplete Bell polynomials that appear above are
bounded as follows:
|λφ′
i(θ) −i⌊λmi⌋| ⩽λ|φ′
i(θ) −φ′
i(0)| + |λmi −⌊λmi⌋|
⩽λ ∥φ′′
i ∥L ∞([−ε,ε]) |θ| + 1 ⩽2λ σ2
i |θ| + 1;
|λφ(r⩾2)
i
(θ)| ⩽λ ∥φ(r)
i ∥∞⩽λ ∥φ∥C n(Td),
Rewriting the complete Bell polynomial Bn = Pn
k=1 Bn,k as a sum over
integer partitions of size n, we thus obtain

∂n(eλφi(θ)−i⌊λmi⌋θ)
∂θn

 e
λσ2
i θ2
4
⩽
X
L partition
of size n
Bn,L
 2λ σ2
i |θ| + 1
m1(L)  λ ∥φ∥C n(Td)
ℓ(L)−m1(L) .
where Bn,L =
n!
Q
i⩾1((i!)mi(L) mi(L)!) is the number of set partitions of [[1, n]]
whose parts have their sizes prescribed by the integer partition L. Conse-
quently,
sZ ε
−ε

∂n(eλφi(θ)−i⌊λmi⌋θ)
∂θn

2 dθ
2π
⩽
X
L partition
of size n
Bn,L (λ ∥φ∥)ℓ(L)−m1(L)
sZ ε
−ε
e−
λσ2
i θ2
2
(2λ σ2
i |θ| + 1)2m1(L) dθ
2π ,
and each integral under the square root sign is equal to
v
u
u
t
1
p
2πλ σ2
i
2m1(L)
X
k=0
2m1(L)
k

(2
√
λ σi)k
Z
R
e−x2
2 |x|k dx
√
2π
= 2m1(L) p
(2m1(L) −1)!!
(2π)1/4
(λ σ2
i )
m1(L)
2
−1
4

1 + O
 1
√
λ

.
TOME 70 (2020), FASCICULE 3
1180
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Thus, the term corresponding to an integer partition L in the previous
bound on the norm

∂n(eλφi(θ)−i⌊λmi⌋θ)
∂θn

L 2([−ε,ε])
is of order O(λℓ(L)−m1(L)
2
−1
4 ), where the constant in the O( · ) can depend
only on n and φ. The integer partitions that maximise the exponent ℓ(L)−
m1(L)
2
among those of ﬁxed size n are those with parts 1 or 2, of the form
L = ( 2, 2, . . . , 2
|
{z
}
j parts of size 2
,
1, 1, . . . , 1
|
{z
}
n−2j parts of size 1
).
Therefore,

∂n(eλφi(θ)−i⌊λmi⌋θ)
∂θn

L 2([−ε,ε])
≲
1
(2πλ σ2
i )
1
4
⌊n
2 ⌋
X
j=0
n! (λ ∥φ∥C n(Td))j
2j j! (n −2j)!
2n−2j p
(2n −4j −1)!! (λ σ2
i )
n
2 −j
≲C(n, φ) λ
n
2 −1
4 ,
where the symbol ≲means that the inequality holds up to a multiplicative
factor 1 + O( 1
√
λ). The constant C(n, φ) and the constant hidden in the
O( · ) depend only on n and φ. Finally,

cd,ε (ψ −χ) eλφ

A
⩽C(d, c, φ) εr+1 βr+1(ε)
λ
d
4

1 + O
 1
√
λ
 
sup
|α|⩽Kd
√
λ + 1
ε
|α|!
⩽C(d, c, φ) εr+1 βr+1(ε)
λ
d
4
√
λ + 1
ε
Kd 
1 + O
 1
√
λ

.
□
Proof of Theorem 5.3. — As in the one dimensional case, it suﬃces now
to write
∥bµ −bν∥A ⩽∥ψ −χ∥A

(1 −cd,ε) eλφ

A +

cd,ε (ψ −χ) eλφ

A ,
and to use the two previous lemmas.
□
Corollary 5.6. — With the assumptions of Theorem 5.3, for any r ⩾
⌊d
2⌋, there exists a positive constant C3(r, d, c, φ) such that, if ε > 0 is ﬁxed
and λ ⩾2 is suﬃciently large (chosen according to ε), then
∥bµ −bν∥A ⩽C3(r, d, c, φ) (∥ψ −χ∥A + βr+1(ε)) (log λ)r+1
λ
r
2 + 1
4
.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1181
Proof. — Set ε = t log λ
√
λ
with t > 0. We then have, up to a multiplicative
remainder (1 + o(1)), a bound on the norm ∥bµ −bν∥A equal to the sum of
the two terms:
C1(d, c, φ) ∥ψ −χ∥A
λK+ 1
2 −tM
4
t log λ
and C1(d, c, φ) βr+1(ε) (t log λ)r+1 λ
K
2 −r+1
2 −d
4 .
We set t =
1
M (d + 2r + 2K + 4), so that the two powers of λ agree. Note
that
Kd
2 −r + 1
2
−d
4 =
d
2 + 1
2
−r + 1
2
−d
4 =
(
−r
2
if d is even,
−r
2 −1
4
if d is odd.
So,
∥bµ −bν∥A ⩽



C3(r, d, c, φ) (∥ψ −χ∥A + βr+1(ε)) (log λ)r+1
λ
r
2
if d is even,
C3(r, d, c, φ) (∥ψ −χ∥A + βr+1(ε)) (log λ)r+1
λ
r
2 + 1
4
if d is odd.
If d is odd, the claim is proven. Otherwise, notice that if µ and ν are two
measures satisfying the hypotheses of Theorem 5.3 in even dimension d,
then
µ+(k1, . . . , kd, kd+1) = µ(k1, . . . , kd) e−λ λkd+1
(kd+1)! ;
ν+(k1, . . . , kd, kd+1) = ν(k1, . . . , kd) e−λ λkd+1
(kd+1)!
are signed measures on Zd+1 that again satisfy the hypotheses of Theo-
rem 5.3:
c
µ+(ξ1, . . . , ξd+1) = bµ(ξ1, . . . , ξd+1) eλ(eiξd+1−1)
= eλΦ(x1,...,xd+1) ψ(ξ1, . . . , ξd);
c
ν+(ξ1, . . . , ξd+1) = bν(ξ1, . . . , ξd+1) eλ(eiξd+1−1)
= eλΦ(x1,...,xd+1) χ(ξ1, . . . , ξd),
where Φ(ξ1, . . . , ξd+1) = φ(ξ1, . . . , ξd) + eλ(eiξd+1−1). Since

c
µ+ −c
ν+

A = ∥bµ −bν∥A ,
we can apply our result in dimension d + 1, assuming r ⩾⌊d+1
2 ⌋:
∥bµ −bν∥A ⩽C3(r, d + 1, c, φ) (∥ψ −χ∥A + βr+1(ε)) (log λ)r+1
λ
r
2 + 1
4
.
TOME 70 (2020), FASCICULE 3
1182
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
However, for d even, ⌊d+1
2 ⌋= ⌊d
2⌋, so the minimum r that one can take is
again ⌊d
2⌋.
□
In comparison to the one dimensional case, we lost a logarithmic factor
(log λ)r+1 in our estimate of norms (cf. Theorem 2.3). This will not be a
problem for the calculation of asymptotics of distances.
