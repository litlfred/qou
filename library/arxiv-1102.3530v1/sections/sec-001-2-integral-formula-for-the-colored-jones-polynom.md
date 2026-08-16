---
doc_id: arxiv-1102.3530v1
doc_title: "THE COLORED JONES POL YNOMIAL, THE CHERN–SIMONS"
section_id: sec-001-2-integral-formula-for-the-colored-jones-polynom
section_title: "Integral formula for the colored Jones polynomial"
section_number: 2
pages: 4-6
source_pdf: 1102.3530v1.pdf
source_sha256: ad3edab19f3dc404
doc_brief: "THE COLORED JONES POLYNOMIAL, THE CHERN–SIMONS — W e show that from the asymptotic behavior of an evaluation of the colored Jones polynomial of the ﬁgure-eight knot we can extr act the Chern– Simons"
---
In this section we use the quantum dilogarithm function to express t he colored
Jones polynomial of the ﬁgure-eight knot as an integral. We mainly fo llow [1].
First of all we recall the following formula due to Habiro and Le (see fo r example
[17]).
JN (E;q) =
N −1∑
k=0
k∏
l=1
(
q(N −l)/ 2 −q−(N −l)/ 2
)(
q(N +l)/ 2 −q−(N +l)/ 2
)
=
N −1∑
k=0
q−kN
k∏
l=1
(
1 −qN −l)(
1 −qN +l)
.
(2.1)
For a complex number γ with Re(γ)> 0, deﬁne the quantum dilogarithm Sγ (z)
as follows [6]:
Sγ (z) := exp
( 1
4
∫
CR
ezt
sinh(πt) sinh(γt)
dt
t
)
,
where | Re(z)| < π + Re(γ) and CR is ( −∞, −R] ∪ Ω R ∪ [R, ∞) with Ω R :=
{R exp(√−1(π −s)) | 0 ≤ s ≤ π} for 0 < R < min{π/|γ|, 1}. Note that the
poles of the integrand are 0 , ±√−1, ±2√−1,... and ±π√−1/γ, ±2π√−1/γ,... .
Remark 2.1. Note that in [1] it is assumed that γ is real and 0 < γ <1 but we
can deﬁne Sγ (z) when Re( γ) > 0. See [3, (3.21)]. (Our quantum dilogarithm
Sγ (z) is equal to Φ( z/(2π);γ/π) in [3].) We give a proof of the analyticity of Sγ in
Lemma 5.1.
The following formula is well known and its proof can be found in [1, p. 53 0].
Note that they assume that γ is real but their proof is also valid in our case.
Lemma 2.2. If | Re(z)|<π , then we have
(2.2)
(
1 +e
√−1z
)
Sγ (z +γ) = Sγ (z −γ).
Putting γ := (2π − √−1u)/(2N ) and z :=π − √−1u − 2lγ (l = 1, 2,...,N − 1)
in (2.2), we have
(
1 +e
√−1(π −√−1u−2lγ )
)
Sγ (π −
√
−1u − 2lγ +γ) = Sγ (π −
√
−1u − 2lγ −γ).
So for k = 1, 2,...,N − 1 we have
k∏
l=1
(
1 − exp((N −l)ξ/N )
)
=
k∏
l=1
(
1 +e
√
−1(π −√−1u−2πl/N +√−1ul/N )
)
=
k∏
l=1
Sγ (π − √
−1u − (2l + 1)γ)
Sγ (π − √−1u − (2l − 1)γ)
= Sγ (π − √−1u − (2k + 1)γ)
Sγ (π − √−1u −γ) .
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 5
Similarly we have
k∏
l=1
(
1 − exp((N +l)ξ/N )
)
= Sγ (−π − √
−1u +γ)
Sγ (−π − √−1u + (2k + 1)γ).
Therefore we have
JN
(
E; exp(ξ/N )
)
= Sγ (−π − √−1u +γ)
Sγ (π − √−1u −γ)
N −1∑
k=0
exp(−ku) Sγ (π − √
−1u − (2k + 1)γ)
Sγ (−π − √−1u + (2k + 1)γ).
Using Sγ we deﬁne
(2.3) gN (w) := exp( −Nuw ) Sγ (π − √−1u + √−1ξw)
Sγ (−π − √−1u − √−1ξw).
SinceSγ (z) is deﬁned for | Re(z)|<π + Re(γ), the function gN (w) is deﬁned for w
with |π −Im(ξw)|<π +Re(γ) = π +π/N, that is, w is in the strip −(2π/u) Re(w)−
π/(Nu )< Im(w)< −(2π/u) Re(w) + 2π/u +π/(Nu ) (Figure 1).
/C7
Ꜽ
/BD /A0 Ꜽ
/CA/CT
/C1/D1
/D4
/A0 /BD
/A0
/D4
/A0 /BD
/BE /AP
/D4
/A0 /BD
/D9
Figure 1. The function gN (Φ, respectively) is deﬁned between
the two dotted (thick, respectively) lines. The dashed parallelo-
gram indicates the contour C+(ε) ∪C−(ε).
For 0 < ε < 1/(4N ), let C+(ε) be the polygonal line that connects 1 − ε,
1 −u/(2π) −ε + √
−1, −u/(2π) +ε + √−1, and ε, and C−(ε) be the polygonal line
that connects ε, u/(2π) − √−1, 1 + u/(2π) − √−1, and 1 −ε. See Figure 1. Put
C(ε) := C−(ε) ∪C+(ε). Note that the domain of gN (w) contains C(ε).
By the residue theorem we have
6 HITOSHI MURAKAMI
JN
(
E; exp(ξ/N )
)
= Sγ (−π − √−1u +γ)
Sγ (π − √−1u −γ)
√−1 exp(u/2)N
2
∫
C(ε)
tan(Nπw )gN (w)dw
since the set of the poles of tan( Nπw ) inside C(ε) is {(2k + 1)/(2N ) | k =
0, 1, 2,...,N − 1} and the residue of each pole is −1/(Nπ ).
Putting
G±(N,ε ) :=
∫
C±(ε)
tan(Nπw )gN (w)dw,
we have
(2.4)
JN
(
E; exp(ξ/N )
)
= Sγ (−π − √
−1u +γ)
Sγ (π − √−1u −γ)
√−1 exp(u/2)N
2
(
G+(N,ε ) +G−(N,ε )
)
.
