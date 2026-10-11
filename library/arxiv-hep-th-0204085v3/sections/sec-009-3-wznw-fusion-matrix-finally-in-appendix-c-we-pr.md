---
doc_id: arxiv-hep-th-0204085v3
doc_title: "arXiv:hep-th/0204085v3 12 Nov 2002"
section_id: sec-009-3-wznw-fusion-matrix-finally-in-appendix-c-we-pr
section_title: "WZNW fusion matrix. Finally, in appendix C we present a way to ﬁnd degenerate"
section_number: 3
pages: 3-6
source_pdf: 0204085v3.pdf
source_sha256: e0df7d49c43273c4
toc_source: inferred
---
representations and fusion rules for ˆsl(2) from degenerate representations and fusion rules
for the Virasoro algebra.
1
Requisites
1.1
Liouville ﬁeld theory
Let the Vα(z, ¯z) be the primary ﬁelds with conformal weight ∆L
α = α(Q −α) where
Q = b+ b−1; b is the coupling constant in Liouville ﬁeld theory that we shall call for short
LFT. The central charge of the Virasoro algebra is c = 1 + 6Q2.
Let
⟨Vα4(∞)Vα3(1)Vα2(z, ¯z)Vα1(0)⟩≡Vα4,α3,α2,α1(z, ¯z)
denote a four point correlation function in LFT and
F s
α21(α1, α2, α3, α4|z)
(1)
be the corresponding conformal block in the s-channel. The conformal block is completly
determined by the conformal symmetry (although there is no known closed form for it in
general), and is normalized such that
F s
α21(α1, α2, α3, α4|z) ∼z→0 z∆L
α21−∆L
α1−∆L
α2(1 + O(z))
(2)
5We consider here the two most natural choices for the cuts, as in [26].
3
Let us note that the Liouville conformal block depends on conformal weights only.
There exist [24] invertible fusion transformations between s- and t-channel conformal
blocks, deﬁning the Liouville fusion matrix:
F s
α21(α1, α2, α3, α4|z) =
Z
Q
2 +iR+ dα32F L
α21α32

α3
α2
α4
α1

F t
α32(α1, α2, α3, α4|1 −z)
(3)
The explicit expression for the LFT fusion matrix was given in [9], in terms of a b-deformed
4F3 hypergeometric function in the Barnes representation:
F L
α21α32
 α3
α2
α4
α1

=
Γb(2Q −α3 −α2 −α32)Γb(α3 + α32 −α2)Γb(Q −α2 −α32 + α3)Γb(Q −α3 −α2 + α32)
Γb(2Q −α1 −α2 −α21)Γb(α1 + α21 −α2)Γb(Q −α2 −α21 + α1)Γb(Q −α2 −α1 + α21)
Γb(Q −α32 −α1 + α4)Γb(α32 + α1 + α4 −Q)Γb(α1 + α4 −α32)Γb(α4 + α32 −α1)
Γb(Q −α21 −α3 + α4)Γb(α21 + α3 + α4 −Q)Γb(α3 + α4 −α21)Γb(α21 + α4 −α3)
Γb(2Q −2α21)Γb(2α21)
Γb(Q −2α32)Γb(2α32 −Q)
1
i
i∞
Z
−i∞
ds Sb(U1 + s)Sb(U2 + s)Sb(U3 + s)Sb(U4 + s)
Sb(V1 + s)Sb(V2 + s)Sb(V3 + s)Sb(Q + s)
(4)
with
U1 = α21 + α1 −α2
V1 = Q + α21 −α32 −α2 + α4
U2 = Q + α21 −α2 −α1
V2 = α21 + α32 + α4 −α2
U3 = α21 + α3 + α4 −Q
V3 = 2α21
U4 = α21 −α3 + α4
The special function entering the formula above is Γb(x) ≡
Γ2(x|b,b−1)
Γ2(Q/2|b,b−1), where Γ2(x|ω1, ω2)
is the Double Gamma function introduced by Barnes [25], which deﬁnition is
logΓ2(x|ω1, ω2) =
 
∂
∂t
∞
X
n1,n2=0
(x + n1ω1 + n2ω2)−t
!
t=0
The function Γb(x) such deﬁned is such that Γb(x) ≡Γb−1(x), and satisﬁes the following
functional relation
Γb(x + b) =
√
2πbbx−1
2
Γ(bx)
Γb(x)
(5)
Γb(x) is a meromorphic function of x, which poles are located at x = −nb−mb−1, n, m ∈N.
The function Sb(x) is deﬁned as Sb(x) ≡
Γb(x)
Γb(Q−x).
Let us quote the following properties:
4
- The Liouville fusion matrix is holomorphic in the following range [9]
|Re(α2 + α3 + α32 −Q)| < Q
|Re(α4 + α1 + α32 −Q)| < Q
|Re(α2 + α3 −α32)| < Q
|Re(α4 + α1 −α32)| < Q
|Re(α3 + α32 −α2)| < Q
|Re(α4 + α32 −α1)| < Q
|Re(α2 + α32 −α3)| < Q
|Re(α1 + α32 −α4)| < Q
- It satisﬁes the symmetry properties
F L
α21,α32

α3
α2
α4
α1

= F L
α21,α32

α4
α1
α3
α2

= F L
α21,α32

α2
α3
α1
α4

(6)
- As the conformal blocks depends on conformal weights only, so does the Liouville
fusion matrix, i.e. is invariant when one of the αi is substituted by Q −αi.
The LFT fusion matrix was built in terms of the Racah-Wigner coeﬃcients for an ap-
propriate continuous series of representations of the quantum group Uq(sl(2, R)) with
deformation parameter q = eiπb2 [9,10]. This construction ensures that the fusion matrix
satisﬁes the set of Moore-Seiberg equations (or polynomial equations) [26].
Let us quote the pentagonal equation:
Z
Q
2 +iR+ dδ1F L
β1δ1

α3
α2
β2
α1

F L
β2γ2

α4
δ1
α5
α1

F L
δ1γ1

α4
α3
γ2
α2

= F L
β2γ1
 α4
α3
α5
β1

F L
β1γ2
 γ1
α2
α5
α1

(7)
and the two hexagonal equations:
F L
α21,β
 α4
α2
α3
α1

eiπǫ(∆L
α1+∆L
α2+∆L
α3+∆L
α4−∆L
α21−∆L
β) =
Z
Q
2 +iR+ dα32F L
α21,α32
 α3
α2
α4
α1

F L
α32,β
 α2
α4
α3
α1

eiπǫ∆α32
(8)
where ǫ = ±.
We will also need the Liouville three point function; an explicit formula for it was proposed
in [3,4]
CL(α3, α2, α1) =
h
πµγ(b2)b2−2b2i Q−α1−α2−α3
b
.
Υ0Υb(2α1)Υb(2α2)Υb(2α3)
Υb(α1 + α2 + α3 −Q)Υb(α1 + α2 −α3)Υb(α1 + α3 −α2)Υb(α2 + α3 −α1)
(9)
5
where Υb(x)−1 = Γb(x)Γb(Q −x), γ(x) =
Γ(x)
Γ(1−x), Υ0 = resx=0
dΥb(x)
dx
, and µ is the cosmo-
logical constant.
A four point function in LFT is written (if the Re(αi), i = 1 . . . 4 are close enough to Q/2)
Vα4,α3,α2,α1(z, ¯z) =
= 1
2
Z
Q
2 +iR
dα21CL(α4, α3, α21)CL(Q −α21, α2, α1)|F s
α21(α1, α2, α3, α4|z)|2
(10)
1.2
