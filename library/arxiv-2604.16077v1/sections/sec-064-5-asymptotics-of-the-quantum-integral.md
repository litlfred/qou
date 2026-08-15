---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-064-5-asymptotics-of-the-quantum-integral
section_title: "Asymptotics of the quantum integral"
section_number: 5
pages: 47-49
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
Recall that in Section 4 we deﬁned the functions
• (case (a), function f−) L−(z; −2iπ,iπ ) = Li 2(ez) +z2 −iπz,
• (case (a), function f+) L+(z; −2iπ,iπ ) = Li 2(ez) +z2 +iπz,
• (case (b), function f−) L−(z; −2iπ, 2iπ) = Li 2(ez) +z2 − 2iπz,
• (case (b), function f+) L+(z; −2iπ, 2iπ) = Li 2(ez) +z2,
and we studied the asymptotics of the integrals
∫
[is−
N,2iπ−is+
N ]e
N
2iπ L±(z,−2iπ,ℓ)dz forℓ =iπ (case
(a)) or ℓ = 2iπ (case (b)).
In this section we extend this study to obtain asymptotics of the integral on the right side of
(88),
∫
CN
e
N
2iπ (z2−l1,Nz) ˆSN (l0,N +z) coth(Nz
2 )dz, thus ﬁnishing the proof of Theorem 1.1 (see
the steps IX and X in Section 1.3).
Because the integrand depends on N in a complicated way, we need a preliminary result,
Lemma 5.1 below, to approximate the integral.
To state this lemma, denote by C +
N and C −
N the intersections of the contour CN (deﬁned in
(87)) with the right and left half-spaces; see Figure 6. Reca ll that we assume s−
N :=απ
N with
α ∈]0, 1[ (see (107)), and s+
N ∈]0, 2π
N [. Consider the following shift of the function Ψ N that
we studied in the lemmas 3.3-3.5:
(119) Ψ u0,N (z) := ΨN
( 1
N Log(u0) +z
)
.
48 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
It is holomorphic on the domain (63) shifted by − 1
N Log(u0). Finally, recall the log-parameters
l′
k := Log(uk) +iπak from (7), and that the edge colors a0,a 1 ∈ Z were speciﬁed in Sections
2.3 and 3.6. Deﬁne
(120) ρ(z) := e−
l′
1
2iπz(1 −ez)−
l′
0
2iπ − 1
2.
Note that our choice of a0 ≥ 2 makes R( l′
0
2iπ + 1
2 ) > 0, so ρ(z) has poles at the points
z ∈ (2iπ)Z. This will have important consequences in the analysis of th e integrals in Lemma
5.1, which will be done in Lemma 5.5.
·ε·0
·2πi
· 2πi − 2π
Ni
·
2π
Ni
·
C +
N
·
C −
N
is−
N
2πi −is+
N
Figure 6. The contour CN and its subcontours C +
N and C −
N
Lemma 5.1. If l0,∞ = −2iπ and l1,∞ =:ℓ ∈ {πi, 2πi} (as in Lemma 3.12) we have
∫
CN
e
N
2iπ (z2−l1,Nz) ˆSN (l0,N +z) coth(Nz
2 )dz
=
∫
C+
N
(
e
N
2iπ L−(z;−2iπ,ℓ) −u0e
N
2iπ L+(z;−2iπ,ℓ)
)
ρ(z) exp
( 1
N Ψu0,N (z)
)(
1 + 1
NRN (z)
)
dz
−
∫
C−
N
(
e
N
2iπ L−(z;−2iπ,ℓ) −u0e
N
2iπ L+(z;−2iπ,ℓ)
)
ρ(z) exp
( 1
N Ψu0,N (z)
)(
1 + 1
NRN (z)
)
dz
= 2
∫
C+
N
(
e
N
2iπ L−(z;−2iπ,ℓ) −u0e
N
2iπ L+(z;−2iπ,ℓ)
)
ρ(z) exp
( 1
N Ψu0,N (z)
)(
1 + 1
NRN (z)
)
dz,
where the function RN , with formula (130), is holomorphic on the domain
(121) C \
(⋃
k∈Z
(
2iπk − 1
N Log(u0) + [0, +∞[
) ⋃ (⋃
k∈Z
(2iπk + [0, +∞[)
))
,
and |RN | is bounded from above by a constant independent of N on any compact subset of a
strip R +i(2πk + [δ + π
N, 2π −δ − π
N ]), δ ∈]0,π [, k ∈ Z, contained in this domain.
Proof. Step 1: Rephrasing ˆSN (l0,N +z).
Recall from (84)-(86)-(89) that l0,N = −2iπ + 1
N (Log(u0) + πia0) where a0 is even and
I(Log(u0) +πia0)> 0. We can use the functional equation ˆSN (z) = ˆSN (z + 2iπ
N )(1 −ez+ 2iπ
N )
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 49
(see (52)) in order to shift N −a0
2 times the argument l0,N +z: since l0,N +z + 2iπ
N (N −a0
2 ) =
1
N Log(u0) +z we have
(122) ˆSN (l0,N +z) = ˆSN
( 1
N Log(u0) +z
) N −a0/2∏
k=1
(
1 −el0,N +z+ 2iπ
N k
)
.
Step 2: Approximating ˆSN
(1
N Log(u0) +z
)
.
Let us approximate ˆSN
(1
N Log(u0) +z
)
. Since −π <I (Log(u0))< π, for every z ∈CN we
have
(123) −π
N +s−
N ≤ I
( 1
N Log(u0) +z
)
≤ 2π −s+
N + π
N.
We can get ﬁner bounds, depending on u0. Indeed, assume that ℑ(Log(u0)) satisﬁes
(124) −πυ< ℑ(Log(u0))<πυ ′,
where 0 <υ,υ ′ < 1. Let υ′′ > 0 be such that υ′ <υ ′′ < 1. Take
(125)







s−
N :=α−π
N, with α− := 1 +υ
2 ,
s+
N :=α+π
N, with α+ := 1 +υ′′.
Then the inequalities (123) become:
(126)
0< (1 −υ)π
2N = −πυ
N +s−
N ≤ I
( 1
N Log(u0) +z
)
≤ 2π −s+
N + υ′π
N < 2π − (υ′′ −υ′)π
N − π
N.
Note that the choices of s−
N = α− π
N , with α− ∈]0, 1[, and of s+
N = α+ π
N , with α+ ∈]1, 2[,
satisfy the assumptions of Section 4 (see (107)); moreover α− = 1+υ
2 ensures that strips like
(126) avoid cuts. The choice of α+, which must lie within ]0 , 2[ by the deﬁnition of s+
N , in
the subinterval ]1, 2[ is relevant only for Remark 5.2 below.
By Remark 3.4 (ii) we can use the equality (56). Taking the exp onential we get
ˆSN
( 1
N Log(u0) +z
)
= exp
(N
2iπ Li2
(
e
1
N Log(u0)+z
)
− 1
