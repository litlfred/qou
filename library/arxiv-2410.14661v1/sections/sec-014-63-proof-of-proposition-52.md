---
doc_id: arxiv-2410.14661v1
doc_title: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eigh"
section_id: sec-014-63-proof-of-proposition-52
section_title: "Proof of Proposition 5.2"
section_number: 6.3
pages: 45-46
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
doc_brief: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eight knot — This is"
---
Proposition 5.3 in [4].
Lemma 6.4. Suppose (θ0
1,θ 0
2,θ 0
3) is a critical point of ˆV (θ1,θ 2,θ 3) with (Re(θ0
1), Re(θ0
2), Re(θ0
3))∈
D0, then we have (Re(θ0
1), Re(θ0
2), Re(θ0
3))∈U0.
Proof. Supposeθ0
i =θ0
iR+X 0
i
√−1, (i = 1, 2, 3) is a critical point ofˆV with (θ0
1R,θ 0
2R,θ 0
3R)∈
D0, i.e.
(6.34)



∂ ˆV
∂θ1
(θ0
1,θ 0
2,θ 0
3) = 0,
∂ ˆV
∂θ2
(θ0
1,θ 0
2,θ 0
3) = 0.
∂ ˆV
∂θ3
(θ0
1,θ 0
2,θ 0
3) = 0
We will prove that (θ0
1R,θ 0
2R,θ 0
3R)∈U0. Note that
∂f
∂Xi
= ∂Re ˆV (θ1 +X1
√−1,θ 2 +X2
√−1,θ 3 +X3
√−1)
∂X2
(6.35)
= Re
 
√
−1∂ ˆV (θ1 +X1
√−1,θ 2 +X2
√−1,θ 3 +X3
√−1)
∂θi
!
=−Im
 
∂ ˆV
∂θi
!
,
According to the equation (6.34), we obtain
∂ ˆf
∂Xi
(θ0
1R +X 0
1
√
−1,θ 0
2R +X 0
2
√
−1,θ 0
3R +X 0
3
√
−1) = 0,(6.36)
46 QINGTAO CHEN AND SHENGMAO ZHU
By a straightforward computation, we obtain
∂ ˆf
∂X1
=−π(q− 2)θ1 +π− arg(1−e2π√−1(θ2+θ1+(X1+X2)√−1)) (6.37)
+ arg(1−e2π√−1(θ2−θ1+(X2−X1)√−1)),
∂ ˆf
∂X2
= 2π + arg(1−e2π√−1(θ2+θ3+(X2+X3)√−1)) (6.38)
+ arg(1−e2π√−1(θ2−θ3+(X2−X3)√−1)) + arg(1−e2π√−1(θ2−θ1+(X2−X1)√−1))
− arg(1−e2π√−1(θ2+θ1+(X2+X1)√−1))− arg(1−e2π√−1(θ2+X2
√−1))
− arg(1−e2π√−1(θ2−θ1+(X2−X1)√−1)),
∂ ˆf
∂X3
=−π(4p + 2)θ3 + (2p + 3)π + arg(1−e2π√−1(θ2+θ3+(X2+X3)√−1))(6.39)
− arg(1−e2π√−1(θ2−θ3+(X2−X3)√−1)).
Furthermore, for 0<θ 2±θ3− 1< 1
2, then
2π

θ2±θ3− 3
2

< arg(1−e2π√−1(θ2±θ3+(X2±X3)√−1))< 0 (6.40)
and for 1
2 <θ 2±θ3− 1< 1, then
0< arg(1−e2π√−1(θ2±θ3+(X2±X3)√−1))< 2π

θ2±θ3− 3
2

(6.41)
By using the equation (6.36), we get that if ( θ0
1R,θ 0
2R,θ 0
3R)∈D0, then (θ0
1R,θ 0
2R,θ 0
3R)∈
DH. Then ( θ0
1R,θ 0
2R,θ 0
3R) must lie in U0. Since if ( θ0
1R,θ 0
2R,θ 0
3R)∈ DH\U0, by Propo-
sition 5.4, the Hessian matrix ˆf(X1,X 2,X 3) is positive definite on ( θ0
1R,θ 0
2R,θ 0
3R), and
(X 0
1,X 0
2,X 0
3) is a critical point of ˆf(X1,X 2,X 3). On the other hand, by Lemma , we have
thatf(X1,X 2,X 3)→−∞ in some direction ofX 2
1 +X 2
2 +X 2
3→∞ . It is a contradiction.
Hence (θ0
1R,θ 0
2R,θ 0
3R)∈U0. □
Note that it is easy to generalize Lemmas 6.5-6.9 in [4] to be used in our case. Then
we can finish the proof as in [4].
