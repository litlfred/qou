---
doc_id: arxiv-math-9808030v1
doc_title: "Planscherel Measure on Eq(2)"
section_id: sec-011-c-unitary-representations-of-e2-from-su-2-by-con
section_title: "Unitary Representations of E(2) from SU (2) by Contraction"
section_number: C
pages: 15-17
source_pdf: 9808030v1.pdf
source_sha256: 7889d6481b876b12
doc_brief: "Planscherel Measure on Eq(2) — Following the construction of the invariant integral and the scalar p roduct for the quantum Euclidean group Eq(2), we obtained the full matrix elements of its unitary"
---
[9]
Matrix elements tp
kj , p ∈ (0, ∞), −∞ < k, j < ∞, of the unitary
irreducible representation of E(2) has the following integral representation
tp
kj (gE) = e−i(kφ +j(ζ−φ ))
2π
∫ 2π
0
eipρ cosψei(k−j)ψdψ, (C.1)
where
gE =



cosζ − sinζ ρ cosφ
sinζ cosζ ρ sinφ
0 0 1


. (C.2)
Matrix elements tl
ij, l ∈ 1
2Z0, −l ≤i,j ≤l, of the unitary irreducible repre-
sentation of SU (2) are given by
tl
kj(gS) = e−i(kφ +jφ ′)Pl
kj(cosθ), (C.3)
where Pl
kj is the Jacobi polynomial which has the following integral repre-
sentation
Pl
kj(cosθ) = 1
2π
/radicaltp
/radicalvertex
/radicalvertex
√
(l −j)!(l +j)!
(l −k)!(l +k)!
∫ 2π
0
dψeijψ (i sin(θ/ 2)eiψ/ 2 + cos(θ/ 2)e−iψ/ 2)l−k
(i sin(θ/ 2)e−iψ/ 2 + cos(θ/ 2)eiψ/ 2)l+k (C.4)
15
and
gS =
(
ei(φ +φ ′)/ 2 cosθ/ 2 iei(φ −φ ′)/ 2 sinθ/ 2
iei(φ ′−φ )/ 2 sinθ/ 2 e−i(φ +φ ′)/ 2 cosθ/ 2
)
(C.5)
Putting θ =pρ/l in (C.4) for l>> 1 we have
Pl
kj(cos(pρ/l )) = 1
2π
∫ 2π
0
dψei(j−k)ψdψ (1 + ipρ
2l e−iψ/ 2)l−k(1 + ipρ
2l eiφ/ 2)l+k.
(C.6)
By the virtue of lim l→∞(1 +x/l )l =ex we obtain
lim
l→∞
Pl
kj(cos(pρ/l )) = 1
2π
∫ 2π
0
eipρ cosψei(k−j)ψdψ. (C.7)
Hence the matrix elements of the unitary irreducible representatio n of the
Euclidean group E(2) with weight p can be obtained from those of SU (2) by
the following contraction formula
tp
kj(φ,ρ,ζ ) = lim
l→∞
tl
kj (φ,pρ/l,ζ −φ). (C.8)
16
