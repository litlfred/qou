---
doc_id: arxiv-math-9910147v1
doc_title: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗"
section_id: sec-052-2-z-n-p-z-95
section_title: "Z, (n −p) ∈ Z, (95)"
section_number: 2
pages: 27-28
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
---
The last equation implies in particular that ϕ2
(α,n) = (−1)n, ∀α ∈ C, ∀n ∈ Z. Note that when n
is half an odd integer, ϕ(α,n) is not a fourth root of unity.
With our choice of square root, we have the more precise results:
ϕ(α,n) =e−i π
2 n ǫ (qα ), ∀n ∈ Z, ∀α ∈ C, (96)
|ϕ(−1+iρ,n)|2 =eiπ(p+1/2+ǫ(qiρ ))ϕ2
(iρ,−p), ∀n,p ∈ 1
2 + Z, ∀ρ ∈ R. (97)
We will also make an extensive use of the following basic hypergeometr ic functions, associated
to complex numbers α0, · · ·,α n,β 1, · · ·,β n and deﬁned by:
∀Z ∈ C, n+1Φ n
[ α0 α1 · · · αn
β1 · · · βn ;Z
]
=
+∞∑
k=0
∏ n
i=0(αi)k
(1)k
∏ n
i=1(βi)k
q2kZ,
n+3Wn+2(α0 ; α1, · · ·,α n ; Z) =
+∞∑
k=0
(1 −q2α0+4k)
(1 −q2α0 )
∏ n
i=0(αi)k
(1)k
∏ n
i=1(1 +α0 −αi)k
q2kZ.
In an expression involving n+1Φ n or n+1Wn, if Z is not speciﬁed it will mean that Z = 1.
27
Let us recall some properties of basic hypergeometric functions w hich are proved for example
in [24]:
2Φ 1
[ α0 α1,
β1 ;β1−α0−α1
]
= (β1 −α0)∞(β1 −α1)∞
(β1)∞(β1 −α0−α1)∞
, (98)
4Φ 3
[ −n α1 α2 α3
β1 β2 β3
]
=
4Φ 3
[
−n α 1 β1 −α2 β1 −α3
β1 1−n+α1−β2 1−n+α1−β3
]
q2nα1 (β2 −α1)−1n (β3 −α1)−1n (β2)n(β3)n
, (99)
6W5(α0 ; α1,α 2, −n ; 1+ n+α0−α1−α2) = (1 +α0)∞(1+α0−α1−α2)∞
(1+α0−α1)∞(1+α0−α2)∞
. (100)
Relation (98) is called Heine formula, relation (99) is the Sears Identit y.
Let us now recall the deﬁnitions of q−Racah polynomials p(R)
n , of the q−Racah discrete
measure w(R), and of the square of the norm of these polynomials [19][20]:
∀x ∈ C, ∀α,β,γ,δ ∈ C,µ (x) = q−2x +q2x+2+2γ+2δ,
p(R)
n (µ(x);q2α,q 2β,q 2γ,q 2δ) = 4Φ 3
[
−n n +1+α+β −x γ +δ+x+1
α+1 β +δ+1 γ +1
]
,
w(R)(x;q2α,q 2β,q 2γ,q 2δ) = (γ +δ+1,α +1,β +δ+1,γ +1)x(1 −q2(2x+γ+δ+1))
q2x(α+β+1)(1,γ +δ+ 1 −α,γ −β +1,δ +1)x(1 −q2(γ+δ+1)),
h(R)
n (q2α,q 2β,q 2γ,q 2δ) = q2n(γ+δ+1)(1 −q2(α+β+1))(1,β +1,α −δ+1,α +β −γ +1)n
(1 −q2(2n+α+β+1))(α+β +1,α +1,β +δ+1,γ +1)n
×
× (γ +δ+2,γ −α−β,δ −α, −β)∞
(γ +δ−α+1,γ −β +1,δ +1,−α−β−1)∞
. (101)
The deﬁnition of Askey-Wilson polynomials p(AW )
n , of the Askey-Wilson measure w(AW ) and of
the square of the norm of these polynomials is [21]:
∀z ∈ C, ∀α,β,γ,δ ∈ C,τ (z) = 1
