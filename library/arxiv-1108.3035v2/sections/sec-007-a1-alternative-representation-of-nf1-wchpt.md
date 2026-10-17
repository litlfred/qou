---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-007-a1-alternative-representation-of-nf1-wchpt
section_title: "A.1 Alternative representation of Nf=1 WchPT"
section_number: null
pages: 20-20
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
Alternative representation of Nf = 1 WchPT
Finally we would like to make the equivalence between the Nf = 1 ﬂavour partition function for the
large-N limit of our even polynomials R2n(x) explicit. The reason why we present this check in detail
is that we require a slightly diﬀerent form from the one given in [20] eq. (13), or in [21] eq. (151) (for
ˆz = 0 there):
Z(Nf =1)
ν
( ˆm, ˆz, ˆa)
=
e−2ˆa2 Z π
−π
dθ
2π eiθν exp[ ˆm cos(θ) + iˆz sin(θ) + 4ˆa2 sin2(θ)]
=
e−2ˆa2 Z π
−π
dθ
2π eiθν
Z ∞
−∞
dx
√πe−x2 exp[ ˆm cos(θ) + iˆz sin(θ) −4xˆa sin(θ)] , (A.5)
where after using a trigonometric identity we have linearised the sine-squared term instead. We can
now use the following identity [37] for generic matrices A, B
Z
U(Nf )
det[U]ν exp
1
2Tr(AU + BU †)

= 2Nf (Nf −1)/2
Nf −1
Y
j=1
j!
det[B]
det[A]
ν/2 det[µj−1
i
Iν+j−1(µi)]
∆Nf({µ2})
,
(A.6)
with µ2
i being the eigenvalues of the product matrix AB. Specifying to U = eiθ ∈U(1) and identifying
A = ˆm + ˆz + 4ixˆa, B = ˆm −(ˆz + 4ixˆa) we arrive at
Z(Nf =1)
ν
( ˆm, ˆz, ˆa) = e−2ˆa2 Z ∞
−∞
dx
√πe−x2  ˆm −(ˆz + 4ixˆa)
ˆm + ˆz + 4ixˆa
ν/2
Iν
p
ˆm2 −(ˆz + 4ixˆa)2

,
(A.7)
which agrees perfectly with eq. (5.3), see also eq. (99) in [27].
