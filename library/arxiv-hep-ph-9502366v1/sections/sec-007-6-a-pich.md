---
doc_id: arxiv-hep-ph-9502366v1
doc_title: ""
section_id: sec-007-6-a-pich
section_title: "A Pich"
section_number: 6
pages: 6-7
source_pdf: 9502366v1.pdf
source_sha256: 56df064956ca03f8
doc_brief: "An introduction to the basic ideas and methods of Chiral Perturbation Theory is presented."
---
of the hadronic spectrum, we can build an eﬀective ﬁeld theor y containing only the
Goldstone modes. Our basic assumption is the pattern of SCSB :
G ≡ SU (3)L ⊗ SU (3)R
SCSB
− →H ≡ SU (3)V . (3.1)
Let us denote φa (a = 1, . . . ,8) the coordinates describing the Goldstone ﬁelds in
the coset space G/H, and choose a coset representative ¯ξ(φ) ≡ (ξL(φ), ξR(φ)) ∈ G. The
change of the Goldstone coordinates under a chiral transfor mation g ≡ (gL, gR) ∈ G
is given by
ξL(φ)
G
− →gL ξL(φ) h†(φ, g) , ξ R(φ)
G
− →gR ξR(φ) h†(φ, g) , (3.2)
where h(φ, g) ∈ H is a compensating transformation which is needed to return t o the
given choice of coset representative ¯ξ; in general, h depends both on φ and g. Since the
same transformation h(φ, g) occurs in the left and right sectors (the two chiral sectors
can be related by a parity transformation, which obviously l eaves H invariant), we
can get rid of it by combining the two chiral relations in (3.2 ) into the simpler form
U (φ)
G
− →gR U (φ) g†
L , U (φ) ≡ ξR(φ) ξ†
L(φ) . (3.3)
Moreover, without lost of generality, we can take a canonica l choice of coset
representative such that ξR(φ) = ξ†
L(φ) ≡ u(φ). The 3 × 3 unitary matrix
U (φ) = u(φ)2 = exp
{
i
√
2Φ /f
}
(3.4)
gives a very convenient parametrization of the Goldstone ﬁe lds
Φ( x) ≡
⃗λ√
2
⃗φ =


1
√
2π0 + 1√
6 η8 π+ K +
π− − 1√
2π0 + 1√
6 η8 K 0
K − ¯K 0 − 2√
6 η8

 . (3.5)
Notice that U (φ) transforms linearly under the chiral group, but the induce d
transformation on the Goldstone ﬁelds ⃗φ is highly non-linear.
To get a low-energy eﬀective Lagrangian realization of QCD, for the light-quark
sector ( u, d, s), we should write the most general Lagrangian involving the matrix
U (φ), which is consistent with chiral symmetry. The Lagrangian can be organized in
terms of increasing powers of momentum or, equivalently, in terms of an increasing
number of derivatives (parity conservation requires an eve n number of derivatives):
Leﬀ (U ) =
∑
n
L2n . (3.6)
In the low-energy domain we are interested in, the terms with a minimum number of
derivatives will dominate.
Due to the unitarity of the U matrix, U U† = I, at least two derivatives are required
to generate a non-trivial interaction. To lowest order, the eﬀective chiral Lagrangian
is uniquely given by the term
L2 = f 2
4 ⟨∂µU †∂µU ⟩, (3.7)
Chiral Perturbation Theory 7
where ⟨A⟩denotes the trace of the matrix A.
Expanding U (φ) in a power series in Φ, one obtains the Goldstone kinetic ter ms
plus a tower of interactions involving an increasing number of pseudoscalars. The
requirement that the kinetic terms are properly normalized ﬁxes the global coeﬃcient
f 2/4 in equation (3.7). All interactions among the Goldstones c an then be predicted
in terms of the single coupling f :
L2 = 1
2 ⟨∂µΦ ∂µΦ ⟩+ 1
12f 2 ⟨(Φ
↔
∂ µ Φ) (Φ
↔
∂µ Φ) ⟩+ O(Φ 6/f 4) . (3.8)
To compute the ππ scattering amplitude, for instance, is now a trivial pertur bative
exercise. One gets the well-known (Weinberg 1966) result [ t ≡ (p′
+ − p+)2]
T (π+π0 → π+π0) = t
f 2 . (3.9)
Similar results can be obtained for ππ → 4π, 6π, 8π, . . . The non-linearity of the
eﬀective Lagrangian relates amplitudes with diﬀerent numb ers of Goldstone bosons,
allowing for absolute predictions in terms of f .
The eﬀective ﬁeld theory technique becomes much more powerf ul if one introduces
couplings to external classical ﬁelds. Let us consider an ex tended QCD Lagrangian,
with quark couplings to external Hermitian matrix-valued ﬁ elds vµ, aµ, s, p:
LQCD = L0
QCD + ¯qγ µ(vµ + γ5aµ)q − ¯q(s − iγ5p)q . (3.10)
The external ﬁelds will allow us to compute the eﬀective real ization of general Green
functions of quark currents in a very straightforward way. M oreover, they can be
used to incorporate the electromagnetic and semileptonic w eak interactions, and the
explicit breaking of chiral symmetry through the quark mass es:
rµ ≡ vµ + aµ = eQAµ + . . .
ℓµ ≡ vµ − aµ = eQAµ + e
√
2 sin θW
(W †
µT+ + h.c.) + . . . (3.11)
s = M + . . .
Here, Q and M denote the quark-charge and quark-mass matrices, respecti vely,
Q = 1
3 diag(2, −1, −1) , M = diag(mu, md, ms) , (3.12)
and T+ is a 3 × 3 matrix containing the relevant Cabibbo–Kobayashi–Maska wa factors
T+ =


