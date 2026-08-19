---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-017-44-derivation-of-the-torsion
section_title: "Derivation of the torsion"
section_number: 4.4
pages: 19-20
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
let us derive the k-twisted torsion or “1-loop invariant” τγ,k of (12), starting from (46). Let
us set ζ =e
2πi
k and θi =z1/k
i =eZ∗
i/k as usual, and work at ﬁxed m∈ (Z/kZ)N to start.
There are two contributions to the torsion. First there is the integrand itself, evaluated
at Z =Z∗, keeping only terms of order ℏ0 in the exponent:
(51) ζ
1
4f B−1ν
kN(−2πiℏ)
N
2
√
det B
× (−ζ
1
2 )mB−1Ame− 1
2kZ∗B−1ν
N∏
i=1
k∏
s=1
(1−ζmi+se−Z∗
i/k)
1
2−s
k ,
20 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
where we have used that Li 1(x) = − log(1−x). Second, there is the determinant of the
Hessian, coming from the leading-order Gaussian integration,
(52)
[
det 1
2πkℏ(−B−1A + ∆z)
]− 1
2.
Combining these terms, using Af +Bf′′ =ν and AZ∗ +B(Z∗)′′ =iπν to rewriteZ∗B−1ν as
Z∗·f′′− (Z∗)′′·f +iπfB−1ν, and observing that ∏N
i=1
∏k
s=1(1−ζmi+se−Z∗
i/k)
1
2 =∏N
i=1(1−
e−Z∗
i )
1
2 = (det ∆z′′)
1
2 , we arrive at
(53) τγ,k = 1
(ik)
N
2
√
det(A∆′′
z + B∆−1
z′ )zf′′/kz′′f/k
(−ζ
1
2 )mB−1Am
N∏
i=1
k−1∏
s=0
(1−ζmi−sθ−1
i )s/k.
The product may be manipulated further using
k−1∏
s=0
(1−ζmi−sθ−1
i )
s
k =
k−1−mi∏
s=−mi
(1−ζ−sθ−1
i )
s+mi
k
=z′′
i
mi
k
k−1∏
s=k−mi
(1−ζ−sθ−1
i )
s
k−1
k+mi∏
s=0
(1−ζ−sθ−1
i )
s
k =z′′
i
mi
k D∗
k(θ−1
i )
1
k (ζθ−1
i ;ζ)−1
mi.
Finally, setting∏
iz′′
i
mi
k = exp[ 1
k(Z∗)′′·m] = exp[iπ
kmB−1ν− 1
kmB−1AZ] =ζ
1
2mB−1νθ−B−1Am,
and summing the whole expression over m∈ (Z/kZ)N, we recover (12).
