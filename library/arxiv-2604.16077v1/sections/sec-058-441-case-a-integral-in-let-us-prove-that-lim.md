---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-058-441-case-a-integral-in-let-us-prove-that-lim
section_title: "Case (a), integral In,−. Let us prove that lim"
section_number: 4.4.1
pages: 39-39
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
n→+∞
1
n Log |In,−| = 1
2 Vol(M ).
First we show thatf−(z) = Li 2(ez)+z2−iπz andz0 :=iπ
3 satisfy the properties of Proposition
4.2 for the contour λ =i[η, 2π −η′], where η,η ′ ∈ (0, 1).
We have∂zLi2(z) = −Log(1 −z)/z, so ∂zLi2(ez) = −Log(1 −ez)e−z.ez = −Log(1 −ez), and
therefore
(f−)′(z) = 2z − Log(1 −ez) −iπ, and (f−)′′(z) = 2 + ez
1 −ez = 1 + 1
1 −ez.
It follows (f−)′(z0) = (2iπ/3) − Log(1 −eiπ/3) −iπ = (−iπ/3) − Log(e−i π
3 ) = 0, which checks
(i). Also ( f−)′′(z0) = 1 + (1 −ei π
3 )−1 = 1 +ei π
3 ⁄= 0, which checks (ii).
Let us check property (iii). We parametrize the contour λ = i[η, 2π −η′] by z = it, where
t ∈ [η, 2π −η′]. Let us prove that [0 , 2π] ∋t ↦→ ℑ(f−)(it) has a strict maximum at π
3 .
Recall ([63]) that
(112) ∀y ∈ C, I(Li2(y)) = − arg(1 −y)Log|y| +D(y),
where arg is the branch of the argument with values in ] −π,π ], and D(y) is the Bloch-Wigner
dilogarithm, which computes the algebraic volume of an orie nted hyperbolic ideal tetrahedron
with cross–ratio modulus y. Hence we have
ℑ(f−)(it) = ℑ
(
Li2(eit) + (it)2 −iπit
)
= ℑ
(
Li2(eit)
)
=D(eit) = Cl 2(t),
where Cl 2 is Clausen’s function (108). Since it achieves its strict lo cal maxima at the points
π/3 + 2πn, n ∈ Z, (iii) follows.
We can now apply Proposition 4.2 and conclude that
lim
n→+∞
1
n Log
⏐
⏐
⏐
⏐
⏐
∫
[iη,2iπ−iη′]
en(−i)f−(z)dz
⏐
⏐
⏐
⏐
⏐ = ℑ(f−)(z0) = D
(
ei π
3
)
= 1
