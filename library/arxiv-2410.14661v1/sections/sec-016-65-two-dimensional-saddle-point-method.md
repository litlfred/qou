---
doc_id: arxiv-2410.14661v1
doc_title: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eigh"
section_id: sec-016-65-two-dimensional-saddle-point-method
section_title: "Two-dimensional saddle point method"
section_number: 6.5
pages: 52-55
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
doc_brief: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eight knot — This is"
---
ˆV (p,q ;θ1,θ 2,θ 3;m1,m 2,m 3)
(6.82)
=π
√
−1
3q
2 +
q
2− 1

θ2
1− (2m1 + 1)θ1− (2m2 + 2)θ2 + (2p + 1)θ2
3− (2p + 3 + 2m3)θ3

+ 1
2π√−1
π2
6 + Li2(e2π√−1(θ2+θ3)) + Li2(e2π√−1(θ2−θ3))− Li2(e2π√−1(θ2+θ1))
−Li2(e2π√−1θ2)− Li2(e2π√−1(θ2−θ1))

.
6.5.1. The case θ3 =c3. Fixing θ3 =c3, then
ˆVθ1 =π
√
−1(−2m1− 1 +qθ1− 2θ1) + log(1−e2π√−1(θ2+θ1))− log(1−e2π√−1(θ2−θ1))
(6.83)
ˆVθ2 =−(2m2 + 2)π
√
−1 + log(1−e2π√−1(θ2+θ1)) + log(1−e2π√−1(θ2−θ1))(6.84)
+ log(1−e2π√−1θ2)− log(1−e2π√−1(θ2+c3))− log(1−e2π√−1(θ2−c3))
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 53
Let z1 =e2π√−1θ1, z2 =e2π√−1t, C3 =e2π√−1c3, then from the critical point equations
ˆVθ1 = 0, ˆVθ2 = 0,(6.85)
we obtain
z2 = z1 +z
q
2
1
1 +z
q
2 +1
1
,(6.86)
z2
2− (z1 + 1
z1
)z2 +z1 + 1
z1
−C3− 1
C3
+ 1 = 0.(6.87)
It follows that
zq+4
1 − (C3 +C−1
3 )zq+3
1 +zq+2
1 −z
q
2 +4
1 + 2z
q
2 +3
1(6.88)
− 2(C3 +C−1
3 − 1)z
q
2 +2
1 + 2z
q
2 +1
1 −z
q
2
1 +z2
1− (C3 +C−1
3 )z1 + 1 = 0.
Suppose z1(q,c 3) is a solution of the equation (6.88), set
θ1(q,c 3) = log(z1(q,C 3))
2π√−1 + Z,(6.89)
θ2(q,c 3) = log(z2(q,C 3))
2π√−1 + Z,
then (θ1(q,c 3),θ 2(q,c 3)) satisfies the critical point equations up to an argument.
Moreover, by using the method in [4], we can show that the critical point equations
( ˆVθ1(θ1,θ 2,c 3) = 0,
ˆVθ2(θ1,θ 2,c 3) = 0.
(6.90)
has a unique solution denoted by (θ1(c3),θ 3(c3)).
Proposition 6.10. For 1
2 + 1
8p <c 3 = 1
2 + ˜c3 < 3
4, we have
2πReˆV (p,q ;θ1(c3),θ 2(c3),c 3)< 2πReˆV (p,q ;θ0
1,θ 0
2,θ 0
3)−ϵ(6.91)
for some ϵ> 0.
Proof. For 1
2 + 1
8p <c 3 = 1
2 + ˜c3 < 3
4, by Theorems 6.6 and 6.7, we have
2πRe ˆV (p,q ;θ1(q,c 3),θ 2(q,c 3),c 3) (6.92)
≤ 2πRe ˆV

p,q,θ 1
1
2

,θ 2
1
2

, 1
2

−π2˜c2
3
< 2πRe ˆV

p,q,θ 1
1
2

,θ 2
1
2

, 1
2

− 49
64π2γ2
1
<Vol (Mp,q) = 2πRe ˆV (p,q,θ 0
1,θ 0
2,θ 0
3).
□
54 QINGTAO CHEN AND SHENGMAO ZHU
Let θ3 = c3 and D0(c3) ={θ3 = c3}∩ D0, we need to estimate the following integral
used in Theorem 5.7,
Z
D0(c3)
sin(πθ1) sin(2πc3)e(N + 1
2 ) ˆVN (θ1,θ2,c3;0,0,m3)dθ1dθ2.(6.93)
Theorem 6.11. For 1
2 + 1
8p <c 3 = 1
2 + ˜c3 < 3
4, we have
Z
D0(c3)
sin(πθ1) sin(2πc3)e(N + 1
2 ) ˆVN (θ1,θ2,c3;0,0,m3)dθ1dθ2 =O(e(N + 1
2 )(ζR(p,q)−ϵ))(6.94)
for ϵ> 0.
Proof. On the region D0(c3), we can check the saddle point method condition for two-
dimensional integral following the procedure in [4], we omit the details here. Then,
together with Proposition 6.10, we prove the Theorem. □
6.5.2. The case θ1 = c1. In this case, let θ1 = c1 and D0(c1) ={θ1 = c1}∩ D0, we need
to estimate the following integral in Theorem 5.8,
Z
D0(c1)
sin(πc1) sin(2πθ3)e(N + 1
2 ) ˆVN (c1,θ2,θ3;0,0,m3)dθ2dθ3.(6.95)
Similarly to previous subsection, we have
Theorem 6.12. For 2
q <c 1 < 1
4, we have
Z
D0(c1)
sin(πc1) sin(2πθ3)e(N + 1
2 ) ˆVN (c1,θ2,θ3;0,0,m3)dθ2dθ3 =O(e(N + 1
2 )(ζR(p,q)−ϵ))(6.96)
for ϵ> 0.
Lemma 6.13. When c3 = 1
2 + ˜c3≥ 1
2 + 7
8p, we have
2πReˆV (p,q ;m1, 0,m 3,c 1,T 2(c1, 1
2 + ˜c3), 1
2 + ˜c3) (6.97)
< 2πReˆV (p,q,m 1, 0, 0,c 1,θ 2(c1),θ 3(c1)).
Proof. First, we have the estimates,
2πRe ˆV (p,q,m 1, 0,m 3,c 1,T 2(c1, 1
2 + ˜c3), 1
2 +c3) (6.98)
=v8− 2π2c2
1−π2˜c2
3 + 1
3π4c4
1−π4c2
1˜c2
3− 1
12π4˜c4
3 +...
=v8− 2π2c2
1 + 1
3π4c4
1 +...
−π2˜c2
3−π4c2
1˜c2
3− 1
12π4˜c4
3 +...
= 2πRe ˆV (p,q,m 1, 0,m 3,c 1,T 2(c1, 1
2), 1
2)−π2˜c2
3−π4c2
1˜c2
3− 1
12π4˜c4
3 +...
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 55
On the other hand,
2πRe ˆV (p,q,m 1, 0, 0,c 1,θ 2(γ1,c 1),θ 3(γ1,c 1))
(6.99)
=v8− 1
4π2γ2
1− 1
8π2γ3
1− ( 1
32π2 + 1
192π4)γ4
1+
+ (−2π2− 1
4π4γ2
1− 1
8π4γ3
1− 5
192π6γ4
1 +...)c2
1
+ (1
3π4− 1
24π6γ2
1− 1
48π6γ3
1 + ( 3
64π6− 23
1152π8)γ4
1 +...)c4
1 +...
=v8− 2π2c2
1 + 1
3π4c4
1 +...
− 1
4π2γ2
1− 1
8π2γ3
1− ( 1
32π2 + 1
192π4)γ4
1 + (−1
4π4γ2
1− 1
8π4γ3
1− 5
192π6γ4
1 +...)c2
1
+ (− 1
24π6γ2
1− 1
48π6γ3
1 + ( 3
64π6− 23
1152π8)γ4
1 +...)c4
1 +...
= 2πRe ˆV (∞,q,m 1, 0, 0,c 1,θ 2(γ1 = 0,c 1),θ 3(γ1 = 0,c 1))− 1
4π2γ2
1− 1
8π2γ3
1− ( 1
32π2 + 1
192π4)γ4
1
+ (−1
4π4γ2
1− 1
8π4γ3
1− 5
192π6γ4
1 +...)c2
1 + (− 1
24π6γ2
1− 1
48π6γ3
1 + ( 3
64π6− 23
1152π8)γ4
1 +...)c4
1 +...
= 2π RebV (p,q,m 1, 0,m 3,c 1,T 2(c1, 1
2), 1
2)− 1
4π2γ2
1− 1
8π2γ3
1− ( 1
32π2 + 1
192π4)γ4
1
+ (−1
4π4γ2
1− 1
8π4γ3
1− 5
192π6γ4
1 +...)c2
1 + (− 1
24π6γ2
1− 1
48π6γ3
1 + ( 3
64π6− 23
1152π8)γ4
1 +...)c4
1 +...
Thus finally we have
2πRe ˆV (p,q,m 1, 0,m 3,c 1,T 2(c1, 1
2 + ˜c3), 1
2 +c3) (6.100)
= 2πRe ˆV (p,q,m 1, 0,m 3,c 1,T 2(c1, 1
2), 1
2)−π2˜c2
3−π4c2
1˜c2
3− 1
12π4˜c4
3 +...
< 2πRe ˆV (p,q,m 1, 0,m 3,c 1,T 2(c1, 1
2), 1
2)−π2˜c2
3
< 2πRe ˆV (p,q,m 1, 0,m 3,c 1,T 2(c1, 1
2), 1
2)− 49
64π2γ2
1.
In principal, by formula (6.99), we can prove the Lemma. □
