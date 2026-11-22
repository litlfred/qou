---
doc_id: s00526-018-1443-6
doc_title: "On the analyticity of critical points of the Möbius energy"
section_id: sec-010-5-form-of-pt-qγ-and-the-bilinear-hilbert-transfo
section_title: "Form of PT Qγ and the bilinear Hilbert transform"
section_number: 5
pages: 10-16
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
toc_source: outline
doc_brief: "On the analyticity of critical points of the Möbius energy — We prove that smooth critical points of the Möbius energy E parametrized by arc-length are analytic."
---
Recall that in the ﬁrst variation of the Möbius energy E there appears the functional H given
by Hγ = P⊥
˙γ ( 
Hγ ) where 
Hγ = Qγ + R1γ + R2γ for every closed, simple, and by
arc-length parametrized curve γ ∈C∞(R/Z, Rn). In this section we will see that a type of
bilinear Hilbert transform can help to estimate the tangential part of Qγ , i.e.
(PT
˙γ Qγ )(x) :=PT
˙γ (x)(Qγ (x)) = ⟨Qγ (x), ˙γ (x)⟩Rn ˙γ (x)
= lim
ε↓0 ⟨Qεγ (x), ˙γ (x)⟩Rn ˙γ (x) = lim
ε↓0(PT
˙γ Qεγ )(x).
In order to avoid problems coming from the singularities of the integrand we will mainly
work with the truncated functional Qε, 0 < ε ≤1
2. We use Taylor’s approximation up to
second order with remainder term in integral from, ⟨˙γ (x), ¨γ (x)⟩Rn = 0 for all x ∈R/Z
coming from the arc-length parametrization of γ , together with the bilinearity of the scalar
product to reach
⟨Qεγ (x), ˙γ (x)⟩Rn = 2

|w|∈

ε, 1
2


2γ (x + w) −γ (x) −w ˙γ (x)
w2
−¨γ (x), ˙γ (x)

Rn
dw
w2
= 4

|w|∈

ε, 1
2

 1
0
(1 −t)
 ¨γ (x + tw) −¨γ (x)
w2
, ˙γ (x)

Rn dtdw
= 4

|w|∈

ε, 1
2

 1
0
(1 −t)⟨¨γ (x + tw), ˙γ (x)⟩Rn
w2
dtdw
= 4

|w|∈

ε, 1
2

 1
0
(1 −t)⟨¨γ (x + tw), ˙γ (x) −˙γ (x + tw)⟩Rn
w2
dtdw
= 4

|w|∈

ε, 1
2

 1
0
 1
0
(1 −t)(−t)⟨¨γ (x + tw), ¨γ (x + stw)⟩Rn
w
dsdtdw.
(5.1)
With ε ↓0 we also get
(PT
˙γ Qγ )(x) = 4 lim
ε↓0

|w|∈

ε, 1
2


[0,1]2(1 −t)(−t)⟨¨γ (x + tw), ¨γ (x + stw)⟩Rn
w
˙γ (x)dsdtdw.
(5.2)
The last terms of (5.1) and (5.2) motivate us to introduce the following
On the analyticity of critical points of the Möbius energy
Page 11 of 28
16
Deﬁnition 5.1 Let s1, s2 ∈[0, 1]. We deﬁne the truncated bilinear Hilbert transform on R/Z
for an arbitrary 1
2 ≥ε > 0 by
Hε
s1,s2 : C1(R/Z, R) × C1(R/Z, R) →L∞(R/Z, R),
Hε
s1,s2( f , g)(x) :=

|w|∈[ε, 1
2 ]
f (x + s1w)g(x + s2w)
w
dw
and the bilinear Hilbert transform by
Hs1,s2 : C1(R/Z, R) × C1(R/Z, R) →L∞(R/Z, R),
Hs1,s2( f , g)(x) := lim
ε↓0 Hε
s1,s2( f , g)(x).
(5.3)
for all x ∈R/Z.
It is straight forward to prove that the bilinear Hilbert transform is well-deﬁned.
Lemma 5.2 For every s1, s2 ∈[0, 1] the bilinear Hilbert transform Hs1,s2 as well as the
truncated bilinear Hilbert transform Hε
s1,s2, 0 < ε ≤1
2, are indeed bilinear, well-deﬁned and
continuousonC1(R/Z, R)×C1(R/Z, R)to L∞(R/Z, R).Furthermore, Hε
s1,s2 iscontinuous
on C(R/Z, R) × C(R/Z, R) to L∞(R/Z, R).
Proof Let s1, s2 ∈[0, 1]. It is easy to see due to the linearity of the integral in (5.3) that Hs1,s2
is indeed linear in both components. Hs1,s2 is also well-deﬁned for every f , g ∈C1(R/Z, R),
which we can see by inserting two times a zero and by Lipschitz-continuity of continuously
differentiable functions on a compact set such that
Hs1,s2( f , g)(x)

=
lim
ε↓0

|w|∈[ε, 1
2 ]
f (x + s1w)g(x + s2w)
w
−f (x)g(x)
w
dw

≤lim
ε↓0

|w|∈

ε, 1
2
 | f (x + s1w)g(x + s2w) −f (x)g(x + s2w) + f (x)g(x + s2w) −f (x)g(x)|
|w|
dw
≤lim
ε↓0

|w|∈

ε, 1
2
 | f (x + s1w) −f (x)||g(x + s2w)| + | f (x)||g(x + s2w) −g(x)|
|w|
dw
≤lim
ε↓0

|w|∈

ε, 1
2
 ∥˙f ∥∞s1|w|∥g∥∞+ ∥f ∥∞∥˙g∥∞s2|w|
|w|
dw
≤C(s1, s2)∥f ∥C1∥g∥C1 < ∞
(5.4)
for all x ∈[0, 1] and 0 < C(s1, s2) < ∞. Hence we can deduce from (5.4) that Hs1,s2 is
continuous. By the same arguments we get the same properties for Hε
s1,s2 for any 1
2 ≥ε >
0. Additionally, since we cut off the singularity in the deﬁnition of Hε
s1,s2, we get by the
elementary estimate
16
Page 12 of 28
S. Blatt, N. Vorderobermeier
Hε
s1,s2( f , g)(x)
 =


|w|∈[ε, 1
2 ]
f (x + s1w)g(x + s2w)
w
−f (x)g(x)
w
dw

≤

|w|∈

ε, 1
2
 | f (x + s1w)||g(x + s2w)| + | f (x)||g(x)|
|w|
dw
≤

|w|∈

ε, 1
2
 ∥f ∥∞∥g∥∞+ ∥f ∥∞∥g∥∞
|w|
dw
≤C(s1, s2, ε)∥f ∥L∞∥g∥L∞< ∞
for all x ∈[0, 1] and a constant 0 < C(s1, s2, ε) < ∞the continuity of Hϵ
s1,s2 on
C(R/Z, R) × C(R/Z, R) to L∞(R/Z, R).
⊓⊔
The next theorem allows us to estimate the truncated bilinear Hilbert transform in a way
that does not depend on the truncation parameter ε. It will later be used to estimate the last
term of (5.1).
Theorem 5.3 Let m > 1
2 and 1
2 ≥ε > 0. Then there exists a positive constant CH < ∞
independent of ε such that
∥Hε
s1,s2( f , g)∥Hm ≤CH∥f ∥Hm∥g∥Hm
(5.5)
for all s1, s2 ∈[0, 1] and f , g ∈C∞(R/Z, Rn).
In order to prove Theorem 5.3, we require Young’s inequality for the convolution of
series and Sobolev’s inequality which we state for the reader’s convenience. We consider for
p ∈[1, ∞) the sequence space
ℓp := {x = (xk)k∈Z ∈CZ | ∥x∥ℓp :=
	
k∈Z
|xk|p
 1
p
< ∞},
which is a Banach space. The following is well known (cf. [19, Theorem 20.18]).
Lemma 5.4 (Young’s inequality) Let p, q,r ≥1 such that 1
p + 1
q = 1
r + 1. For x ∈ℓp and
y ∈ℓq we let (x ∗y)(k) := 
n∈Z x(n)y(k −n) denote the convolution. Then x ∗y ∈ℓr and
∥x ∗y∥ℓr ≤∥x∥ℓp∥y∥ℓq
We will use Hölder’s inequality to prove the following version of the Sobolev inequality:
Lemma 5.5 (Sobolev’s lemma) Let f ∈Hm(R/Z, Rn) for m > 1
2. Then ˆf := ( ˆf (k))k∈Z ∈
ℓ1 and there exists a positive constant C0 < ∞such that
∥ˆf ∥ℓ1 ≤C0∥f ∥Hm.
Proof Simply by the deﬁnition of the ℓ1-norm and by Hölder’s inequality we yield
∥ˆf ∥ℓ1 =
	
k∈Z
| ˆf (k)|
=
	
k∈Z
| ˆf (k)|(1 + k2)
m
2 (1 + k2)−m
2
On the analyticity of critical points of the Möbius energy
Page 13 of 28
16
≤
	
k∈Z
| ˆf (k)|2(1 + k2)m
 1
2 	
k∈Z
1
(1 + k2)m
 1
2
= C0∥f ∥Hm
where C0 :=


k∈Z
1
(1+k2)m

 1
2 which is ﬁnite since m > 1
2.
⊓⊔
Now we are ready to prove Theorem 5.3.
Proof of Theorem 5.3 Let s1, s2 ∈[0, 1], m > 1
2 and 1
2 ≥ε > 0. Moreover, let f , g ∈
C∞(R/Z, R) ⊆Hm(R/Z, R). Due to m > 1
2 and [8, Theorem 8.2], the partial sums of the
Fourier series converge uniformly to the functions f and g, more precisely
∥f −pn∥∞
n→∞
−→0 and
∥g −qn∥∞
n→∞
−→0
(5.6)
where pn(x) := n
k=−n ˆf (k)e−2πikx, qn(x) := n
k=−n ˆg(k)e−2πikx for all x ∈R/Z and
n ∈N0, and pn, qn ∈C∞(R/Z, R).
The strategy of the proof is to ﬁrst compute and estimate the Fourier coefﬁcient of the
truncated bilinear Hilbert transform of pn, qn. Then we derive the main estimate (5.5) for
pn, qn, n ∈N0, and pass to the limit n →∞to obtain the main estimate (5.5) for f , g. Let
n ∈N0. So we start by calculating the k-th Fourier coefﬁcient of Hε
s1,s2(pn, qn), k ∈Z, more
precisely

Hεs1,s2(pn, qn)(k) =
 1
0

|w|∈

ε, 1
2
 pn(x + s1w)qn(x + s2w)
w
e−2πikxdwdx.
(5.7)
Below we will interchange the integrals of (5.7) two times, which is allowed since the
integrand is smooth on

−1
2, −ε

∪

ε, 1
2

. By using that the Fourier coefﬁcients of a
product of two functions is the convolution of the Fourier coefﬁcients of the two functions
we get

|w|∈

ε, 1
2

 1
0
pn(x + s1w)qn(x + s2w)e−2πikxdx dw
w
=

|w|∈

ε, 1
2
 	
l∈Z

pn(l)e2πils1w 
qn(k −l)e2πi(k−l)s2w dw
w
=
⎧
⎨
⎩
0
if |k| > 2n,

|w|∈

ε, 1
2
 n
l=−n e2πi(ls1+(k−l)s2)w f (l)g(k −l) dw
w
if |k| ≤2n.
(5.8)
16
Page 14 of 28
S. Blatt, N. Vorderobermeier
By a simple substitution we gain for |k| ≤2n

|w|∈

ε, 1
2

n
	
l=−n
e2πi(ls1+(k−l)s2)w f (l)g(k −l)dw
w
=

1
2
ε
n
	
l=−n
e2πi(ls1+(k−l)s2)w −e2πi(ls1+(k−l)s2)w
w
f (l)g(k −l)dw
=

1
2
ε
n
	
l=−n
eiwφl,k −e−iwφl,k
w
f (l)g(k −l)dw
=

1
2
ε
n
	
l=−n
2i sin(wφl,k)
w
f (l)g(k −l)dw
(5.9)
where φl,k := 2π(ls1 + (k −l)s2) ∈R. By interchanging integral and sum we get
n
	
l=−n
f (l)g(k −l)2i

1
2
ε
sin(wφl,k)
w
dw
=
n
	
l=−n
f (l)g(k −l)2i

φl,k
2
φl,kε
sin(w)
w
dw
=
n
	
l=−n
f (l)g(k −l)2i

Si
φl,k
2

−Si(φl,kε)

,
(5.10)
where the sine integral is deﬁned by Si(x) :=
 x
0
sin t
t dt. Now we estimate by using (5.8),
(5.9), and (5.10) the k-th Fourier coefﬁcient of the approximation of the bilinear Hilbert
transform Hε
s1,s2 as follows


Hεs1,s2(pn, qn)(k)
 =

 1
0

|w|∈

ε, 1
2
 pn(x + s1w)qn(x + s2w)e−2πikx
w
dwdx

=


|w|∈

ε, 1
2

 1
0
pn(x + s1w)qn(x + s2w)e−2πikx
w
dxdw

≤

|w|∈

ε, 1
2

 1
0

pn(x + s1w)qn(x + s2w)e−2πikx
w
 dxdw
≤
n
	
l=−n
| f (l)||g(k −l)|2
Si
φl,k
2

−Si(φl,kε)

≤
n
	
l=−n
| f (l)||g(k −l)|2
Si
φl,k
2
 +
Si(φl,kε)


≤M
n
	
l=−n
| f (l)||g(k −l)|
≤M(|pn| ∗|qn|)(k)
(5.11)
where M := 4 supφ∈[0,∞[ Si(φ) < ∞.
On the analyticity of critical points of the Möbius energy
Page 15 of 28
16
Moreover, we can deduce from (5.11) using the elementary estimate
(k2 + 1)
m
2 ≤2m 
(l2 + 1)
m
2 + ((k −l)2 + 1)
m
2

,
which immediately follows from |k| ≤2 max{|l|, |k −l|}, that
(k2 + 1)
m
2

Hεs1,s2(pn, qn)(k)
 ≤M

(k2 + 1)
m
2 (|pn| ∗|qn|)(k)

≤MCm
	
l∈Z
(l2 + 1)
m
2 |
pn(l)| |
qn(k −l)|
+ MCm
	
l∈Z
|
pn(l)| ((k −l)2 + 1)
m
2 |
qn(k −l)| .
(5.12)
This motivates us to introduce the following two series component-wise for all k ∈Z

pn(k) := (k2 + 1)
m
2 |
pn(k)| and

qn(k) := (k2 + 1)
m
2 |
qn(k)|
such that (5.12) can be written as
(k2 + 1)
m
2

Hεs1,s2(pn, qn)(k)
 ≤MCm ((

pn ∗|
qn|)(k) + (|
pn| ∗
qn)(k)) .
In the end we get the desired estimate (5.5) for pn, qn by applying the deﬁnition of the
Sobolev norm, triangle inequality, Young’s inequality with 1+ 1
2 = 1
2 +1 in Lemma 5.4 and
Sobolev’s lemma 5.5 such that
∥Hε
s1,s2(pn, qn)∥Hm = ∥((k2 + 1)
m
2

Hεs1,s2(pn, qn)(k))k∈Z∥ℓ2
≤MCm

∥((

pn ∗|
qn|)(k))k∈Z∥ℓ2 + ∥((|
pn| ∗
qn)(k))k∈Z∥ℓ2

≤MCm

∥

pn∥ℓ2∥
qn∥ℓ1 + ∥
qn∥ℓ2∥
pn∥ℓ1

≤MCmC0 (∥pn∥Hm∥qn∥Hm + ∥pn∥Hm∥qn∥Hm)
= CH∥pn∥Hm∥qn∥Hm
(5.13)
where CH := 2MCmC0 is a constant only depending on m. This proves (5.5) for pn and qn
instead of f and g.
Finally, we come to the last step, passing to the limit n →∞. First of all we gain for any
n ∈N0
∥Hε
s1,s2(pn, qn)∥Hm ≤CH∥pn∥Hm∥qn∥Hm
≤CH∥f ∥Hm∥g∥Hm
(5.14)
by (5.13) and the deﬁnition of pn and qn. In order to pass to the limit on the left-hand side
of (5.14), we check the uniform convergence
0 ≤∥Hε
s1,s2( f , g) −Hε
s1,s2(pn, qn)∥∞
≤∥Hε
s1,s2( f , g) −Hε
s1,s2(pn, g)∥∞+ ∥Hε
s1,s2(pn, g) −Hε
s1,s2(pn, qn)∥∞
= ∥Hε
s1,s2( f −pn, g)∥∞+ ∥Hε
s1,s2(pn, g −qn)∥∞
≤C(s1, s2, ε) ∥f −pn∥∞

 !
"
n→∞
−→0
∥g∥∞+ C(s1, s2, ε)∥pn∥∞∥g −qn∥∞

 !
"
n→∞
−→0
n→∞
−→0
16
Page 16 of 28
S. Blatt, N. Vorderobermeier
by Lemma 5.2 and (5.6) so that we may infer by the uniqueness of the Fourier coefﬁcients
of Hε
s1,s2(pn, qn) ∈Hm(R/Z, R) ⊆L2(R/Z, R) that for all k ∈Z


Hεs1,s2( f , g)(k) −

Hεs1,s2(pn, qn)(k)

n→∞
−→0.
Thus, we get for all N ∈N

⎛
⎝	
|k|≤N
(1 + |k|2)m|

Hεs1,s2(pn, qn)(k)|2
⎞
⎠
1
2
−
⎛
⎝	
|k|≤N
(1 + |k|2)m|

Hεs1,s2( f , g)(k)|2
⎞
⎠
1
2

n→∞
−→0,
which implies
⎛
⎝	
|k|≤N
(1 + |k|2)m|

Hεs1,s2( f , g)(k)|2
⎞
⎠
1
2
≤CH∥f ∥Hm∥g∥Hm
by (5.14). Therefore, it also holds
∥Hε
s1,s2( f , g)∥Hm ≤CH∥f ∥Hm∥g∥Hm
and the main estimate (5.5) is proven.
⊓⊔
