---
doc_id: arxiv-2410.14661v1
doc_title: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eigh"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
doc_brief: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eight knot — This is"
---
2. Preliminaries 4
2.1. Defintion of the Reshetikhin-Turaev invariants 4
2.2. Dilogarithm and Lobachevsky functions 6
2.3. Quantum dilogrithm functions 7
2.4. Saddle point method 7
3. Computations of the potential function 8
4. Poisson summation formula 15
5. Asymptotic expansions 20
5.1. Preparations 20
5.2. The case m2̸= 0 24
5.3. The case m2 = 0 but (m1,m 3)̸= (0, 0) 29
5.4. The contribution of ˆhN(0, 0, 0) 32
5.5. Final proof 41
6. Appendices 41
6.1. Geometry of the critical point 41
6.2. Critical value gives the complex volume 43
6.3. Proof of Proposition 5.2 45
6.4. Estimation of the critical value 46
6.5. Two-dimensional saddle point method 52
6.6. One-dimensional saddle point method 55
References 61
1
arXiv:2410.14661v1  [math.GT]  18 Oct 2024
2 QINGTAO CHEN AND SHENGMAO ZHU
1. Introduction
Volume Conjectures relate the exponential growth rate of various quantum invariants of
hyperbolic 3- manifolds at certain root of unity to the hyperbolic volume of the manifolds.
In a series started from [4, 5], we plan to prove various volume conjectures related to the
twist knots.
In [4] and [5], we have proved the Detcherry-Kalfagianni-Yang’s volume conjecture
[7] and Kashaev-Murakami-Murakami’s volume conjecture [10, 14] for the colored Jones
polynomial of twist knotKp with p≥ 6.
Furthermore, the volume conjecture [3] relates the Reshetikhin-Turaev and the Turaev-
Viro invariants of a hyperbolic 3-manifold at certain roots of unity to the hyperbolic
volume of this hyperbolic 3-manifold. In [18], Ohtsuki proved the volume conjecture
[3] for the hyperbolic 3-manifolds obtained by doing integral surgery along the figure-8
knot. Later, in [23], Wong and Yang proved volume conjecture [3] for the hyperbolic
3-manifolds obtained by doing rational surgery along the figure-8 knot. The goal of
this article is to prove the volume conjecture for Reshetikhin-Turaev invariants of the
hyperbolic 3-manifoldsMp,q obtained by doing integralq-surgery along the twist knotKp.
Let us state the main results of this paper precisely. First, we recall that the volume
conjecture for Reshetikhin-Turaev invariant [3]:
Conjecture 1.1. LetM be an oriented closed hyperbolic 3-manifold, for an odd integerr,
let RTr(M) be its r-th Reshetikhin-Turaev invariant, then at the root of unity t =e
4π√−1
r ,
lim
r→∞
4π
r RTr(M) =Vol (M) +
√
−1CS(M) mod π2Z.(1.1)
We define the subset S⊂ Z+× Z+ as follows:
S ={(p,q )∈ Z+× Z+|(p,q ) satisfies the condition (1.3)}.(1.2)
(1.3) q≥



27 (if p = 6)
19 (if p = 7)
17 (if p = 8)
15 (if p = 9, 10)
14 (if p = 11, 12, 13)
13 (if 14 ≤p≤ 32)
12 (if p≥ 33).
Let ˆV (p,q,θ 1,θ 2,θ 3) be the potential function of Reshetikhin-Turaev invariants of Mp,q
given by formula (5.1). By Proposition 5.2, there exists a unique critical point ( θ0
1,θ 0
2,θ 0
3)
ON THE ASYMPTOTIC EXPANSION OF V ARIOUS QUANTUM INV ARIANTS III 3
of ˆV (p,q ;θ1,θ 2,θ 3). Let z0
i =e2π√−1θ0
i for i = 1, 2, 3, we put
ζ(p,q ) = ˆV (p,q ;θ0
1,θ 0
2,θ 0
3)
(1.4)
=π
√
−1
3q
2 + (q
2− 1)(θ0
1)2−θ0
1 + (2p + 1)(θ0
3)2− (2p + 3)θ0
3− 2θ0
2

+ 1
2π√−1
π2
6 + Li2(z0
2z0
3) + Li2
z0
2
z0
3

− Li2(z0
2z0
1)− Li2(z0
2)− Li2
z0
2
z0
1

.
and
ω(p,q ) =
z0
2(z0
3− (z0
3)−1)(
p
z0
1− 1√
z0
1
)
p
(1−z0
2z0
3)(1−z0
2(z0
3)−1)
p
H(p,q ;z0
1,z 0
2,z 0
3)
,(1.5)
where
H(p,q ;z0
1,z 0
2,z 0
3) = 4 z0
2
z0
1−z0
2
· z0
1z0
2
1−z0
1z0
2
 z0
2z0
3
1−z0
2z0
3
+ z0
2
z0
3−z0
2
(1.6)
− 4
 z0
2
z0
1−z0
2
+ z0
1z0
2
1−z0
1z0
2
 z0
2z0
3
1−z0
2z0
3
· z0
2
z0
3−z0
2
+
 z0
2
z0
1−z0
2
+ z0
1z0
2
1−z0
1z0
2
 z0
2
1−z0
2
 z0
2z0
3
1−z0
2z0
3
+ z0
2
z0
3−z0
2

+ (8p + 4) z0
2
z0
1−z0
2
· z0
1z0
2
1−z0
1z0
2
+ (2p + 1)
 z0
2
z0
1−z0
2
+ z0
1z0
2
1−z0
1z0
2
 z0
2
1−z0
2
− (2p + q
2)
 z0
2
z0
1−z0
2
+ z0
1z0
2
1−z0
1z0
2
 z0
2z0
3
1−z0
2z0
3
+ z0
2
z0
3−z0
2

− (q
2− 1) z0
2
1−z0
2
 z0
2z0
3
1−z0
2z0
3
+ z0
2
z0
3−z0
2

+ 4(q
2− 1) z0
2z0
3
1−z0
2z0
3
· z0
2
z0
3−z0
2
− (2p + 1)(q
2− 1)
 z0
2
z0
1−z0
2
+ z0
1z0
2
1−z0
1z0
2
+ z0
2
1−z0
2
− z0
2z0
3
1−z0
2z0
3
− z0
2
z0
3−z0
2

.
Then, we have
Theorem 1.2. For (p,q )∈S, the asymptotic expansion of Reshetikhin-TuraevRTr(Mp,q)
is given by the following form
RTr(Mp,q) = (−1)p+1√
−1eσ((Kp)q)( 3
r +r+1
4 )π√−1ω(p,q )e(N + 1
2 )ζ(p,q)(1.7)
·
 
1 +
dX
i=1
κi(p,q )
4π√−1
r
i
+O
 1
rd+1
!
,
for d≥ 1, where ω(p,q ) is given by formula (1.5) and κi(p,q ) are constants determined
by the 3-manifold Mp,q.
By Theorem 6.2, we know that
2πζ(p,q ) =Vol (Mp,q) +
√
−1CS(Mp,q) mod π2√
−1Z.(1.8)
It implies that
Corollary 1.3. For (p,q )∈S, we have
lim
r→∞
4π
r logRTr(Mp,q;e
4π√−1
r ) =Vol (Mp,q) +
√
−1CS(Mp,q) mod π2√
−1Z.(1.9)
4 QINGTAO CHEN AND SHENGMAO ZHU
Hence we proved Conjecture 1.1 for Mp,q.
The rest of this article is organized as follows. In Section 2, we fix the notations and
review the related materials that will be used in this paper. In Section 3, we compute the
potential function for the Reshetikhin-Turaev invariant for the 3-manifold obtained by
doing integral surgery along the twist knotKp. In Section 4, we express the Reshetikhin-
Turaev invariant as a summation of Fourier coefficients with the help of Poisson summa-
tion formula. In Section 5, we first show that infinite terms of the Fourier coefficients can
be neglected. Then we estimate the remained term of Fourier coefficients by using the
saddle point method, we obtain that only four main Fourier coefficients will contribute
to the final form of the asymptotic expansion. Hence we finish the proof of the main
Theorem 1.2. The final Appendix Section 6 is devoted to the proof of several results
which will be used in previous sections.
Acknowledgements.
The first author would like to thank Nicolai Reshetikhin, Kefeng Liu and Weiping
Zhang for bringing him to this area and a lot of discussions during his career, thank Fran-
cis Bonahon, Giovanni Felder and Shing-Tung Yau for their continuous encouragement,
support and discussions, and thank Jun Murakami and Tomotada Ohtsuki for their help-
ful discussions and support. He also want to thank Jørgen Ellegaard Andersen, Sergei
Gukov, Thang Le, Gregor Masbaum, Rinat Kashaev, Vladimir Turaev, Tian Yang and
Hiraku Nakajima for their support, discussions and interests, and thank Yunlong Yao
who built him solid analysis foundation twenty years ago. The second author would like
to thank Kefeng Liu and Hao Xu for bringing him to this area when he was a graduate
student at CMS of Zhejiang University, and for their constant encouragement and helpful
discussions since then. Both of us thanks Ruifeng Qiu for his interests and supports.
