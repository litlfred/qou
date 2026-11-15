---
doc_id: s00526-018-1443-6
doc_title: "On the analyticity of critical points of the Möbius energy"
section_id: sec-009-4-estimate-of-the-main-term-q
section_title: "Estimate of the main term Q"
section_number: 4
pages: 8-10
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
toc_source: outline
doc_brief: "On the analyticity of critical points of the Möbius energy — We prove that smooth critical points of the Möbius energy E parametrized by arc-length are analytic."
---
Let
λn := 2
3
 nπ
0
1
t

1 −t
nπ
3
sin(t)dt.
The following theorem is an immediate consequence of [17, Lemma 2.3].
Theorem 4.1 For every f ∈C∞(R/Z, Rn) the expression Q f is a C∞function whose
Fourier coefﬁcients are given by

Q f (k) = π3λk|k|3 ˆf (k) ∀k ∈Z.
The constants λk satisfy 0 ≤λk = π
3 + O( 1
k ) as k →∞.
Proof Using Taylor’s expansion up to third order we get
Q f (x) = lim
ε↓0 2

|w|∈

ε, 1
2

 1
0 (1 −t)2...
f (x + tw)dt
w
dw
= lim
ε↓0 2

|w|∈

ε, 1
2

 1
0 (1 −t)2 ...
f (x + tw) −
...
f (x)

dt
w
dw,
(4.1)
On the analyticity of critical points of the Möbius energy
Page 9 of 28
16
from which one immediately gets that Q maps C3,α to L∞, 0 < α ≤1. As Q is linear and
hence ∂l Qγ (x) = Q∂lγ (x), Q also maps Cl+3,α to Cl−1,1, l ∈N. This proves the ﬁrst
claim. For f , g ∈H
3
2 (R/Z, Rn) we deﬁne the bilinear functional

Q( f , g) := lim
ε↓0

R/Z

|w|∈[ε, 1
2 ]
⟨f (x + w) −f (x), g(x + w) −g(x)⟩Rn
w4
−⟨˙f (x), ˙g(x)⟩Rn
w2

dwdx.
Using partial integration and a discrete version thereof, we see that

Q( f , g) = lim
ε↓0

R/Z

|w|∈[ε, 1
2 ]
⟨f (x + w) −f (x), g(x + w) −g(x)⟩Rn
w4
−⟨˙f (x), ˙g(x)⟩Rn
w2

dwdx
= lim
ε↓0

R/Z

|w|∈[ε, 1
2 ]

−2⟨f (x + w) −f (x), g(x)⟩Rn
w4
−⟨˙f (x), ˙g(x)⟩Rn
w2

dwdx
= −1
2 lim
ε↓0

R/Z
⟨Qε f , g⟩dx = −1
2

R/Z
⟨Q f , g⟩dx
(4.2)
since Qε f converges to Q f in L∞(R/Z, Rn) by (4.1).
From [17, Lemma 2.3] we know that

Q( f , g) = −π3
2
	
k∈Z
λk|k|3 ˆf (k) ˆg(k)
and Plancherel’s identity yields

R/Z
⟨Q f , g⟩dx =
	
k∈Z

Q f (k)g(k).
Thus comparing the Fourier coefﬁcients in (4.2) gives 
Q f (k) = π3λk|k|3 ˆf (k) for all k ∈Z.
⊓⊔
All we need in the following is
Corollary 4.2 (of Theorem 4.1) Let l ∈N0 and m ≥0. There exists a positive constant

C < ∞, which is independent of l, such that
∥∂l+3γ ∥Hm ≤
C∥∂l Qγ ∥Hm
for every γ ∈C∞(R/Z, Rn).
Proof By Theorem 4.1 we can rewrite the Fourier coefﬁcients of Qγ as

Qγ (k) = π3λk|k|3 ˆγ (k)
(4.3)
for all k ∈Z where λk = π
3 + O( 1
k ) and λk > 0 for all k̸ = 0. We obtain by (4.3), the
deﬁnition of the Sobolev norm and elementary properties of Fourier coefﬁcients using the
positive constant 
C := infk∈Z\0{λ2
k2−6}−1
2 < ∞
∥∂l Qγ ∥2
Hm =
	
k∈Z
(1 + |k|2)m|
∂l Qγ (k)|2
=
	
k∈Z
(1 + |k|2)m(2π|k|)2l|
Qγ (k)|2
16
Page 10 of 28
S. Blatt, N. Vorderobermeier
=
	
k∈Z
(1 + |k|2)m(2π|k|)2lπ6λ2
k|k|6| ˆγ (k)|2
≥inf
k∈Z{λ2
k2−6}
	
k∈Z
(1 + |k|2)m(2π|k|)2(l+3)| ˆγ (k)|2
= 
C−2 	
k∈Z
(1 + |k|2)m| 
∂(l+3)γ (k)|2
= 
C−2∥∂(l+3)γ ∥2
Hm,
which proves the statement.
⊓⊔
5 Form of PT
