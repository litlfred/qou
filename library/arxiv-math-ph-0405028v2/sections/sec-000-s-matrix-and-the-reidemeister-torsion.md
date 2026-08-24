---
doc_id: arxiv-math-ph-0405028v2
doc_title: "On the quantum invariant for the Brieskorn homology spheres"
section_id: sec-000-s-matrix-and-the-reidemeister-torsion
section_title: "S-matrix and the Reidemeister Torsion"
section_number: null
pages: 17-20
source_pdf: 0405028v2.pdf
source_sha256: 90a0e4ba456988d6
doc_brief: "On the quantum invariant for the Brieskorn homology spheres — We study an exact asymptotic behavior of the Witten–Reshet ikhin–Turaev SU(2) in- variant for the Brieskorn homology spheres Σ( p1, p 2"
---
An asymptotic behavior of the Witten invariant Zk(M) can be given from the deﬁnition (2.1).
In a large N limit, the ﬁrst term in eqs. (5.7) and (5.8) dominate an asymp totic behavior of the
quantum invariant, which will be shown to denote a contribution from ﬂat connections. We obtain
the following;
17
Corollary 13. We have an asymptotic behavior of the Witten invariant (1.1) for the Brieskorn
homology spheres in N → ∞ as
ZN −2
(
Σ( p1, p2, p3)
)
∼ 1
2 e− 3
4 πi e− φ(p1,p2,p3)
2N πi
∑
ℓ1,ℓ2,ℓ3
( √
2 Sℓ1,ℓ2,ℓ3
1,1,1
)
e
− P
2
(
1+∑ 3
j=1
ℓj
pj
) 2
πiN
(6.1)
where the S-matrix is deﬁned in eq. (3.6), and the sum runs over γ(p1, p2, p3) distinct triples
satisfying eq. (4.10).
We see that, except a decaying factor e− φ(p1,p2,p3)
2N πi, our result proves eq. (1.3) exactly as we
have seen that a dominating exponential factor denotes the Chern–Simons invariant (4.15) for the
Brieskorn homology spheres.
In fact we can establish a relationship among the S-matrix, the Reidemeister torsion, and the
spectral ﬂow;
Theorem 14.
√
2 Sℓ1,ℓ2,ℓ3
1,1,1 =
√
Tα e−2πiIα/4 (6.2)
where the triple (ℓ1, ℓ2, ℓ3) satisﬁes eq. (4.10).
Proof. A proof of the absolute value of
√
2 Sℓ1,ℓ2,ℓ3
1,1,1 is straightforward since it is known [5] that the
Reidemeister torsion of the Brieskorn homology sphere is given by
√
Tα = 8√
P
3∏
j=1
⏐
⏐
⏐
⏐sin
(
P ℓj
p 2
j
) ⏐
⏐
⏐
⏐ (6.3)
To prove a part of the phase factor, we recall that the spectra l ﬂow of the Brieskorn homology
spheres is given by [4]
Iα = −3 −
(
2
(
e(ℓ1, ℓ2, ℓ3)
) 2
P
+
3∑
j=1
2
pj
pj−1∑
k=1
cot
( k P π
p 2
j
)
cot
( k π
pj
)
sin2
( k e(ℓ1, ℓ2, ℓ3) π
pj
) )
mod 8 (6.4)
where
e ≡ e(ℓ1, ℓ2, ℓ3) = P
3∑
j=1
pj − ℓj
pj
(6.5)
18
Using this we have
e−2πiIα/4 = e
πi
2
(
3+2 e2
P
) 3∏
j=1
exp
(
πi
2 · 2
pj
pj−1∑
k=1
cot
( k P π
p 2
j
)
cot
( k π
pj
)
sin2
( k e π
pj
) )
= e πie
3∏
j=1
sign
(
sin
( qj e π
pj
)
sin
( e π
pj
))
Here in the second equality we have used P
pj
· qj = 1 (mod pj), and an identity [13, 34],
− i sign
(
sin
( r n π
p
)
sin
( n π
p
))
eπin
= exp
(
−πi
2
(
−2 + 2 r n2
p + 2
p
p−1∑
k=1
cot
( k q π
p
)
cot
( k π
p
)
sin2
( k n π
p
) ))
(6.6)
where we suppose n ∈ Z and q r = 1 (mod p). We further see that
3∏
j=1
sin
( e π
pj
)
= (−1)1+∑
j<k (pjpk+ℓj pk+pjℓk)
3∏
j=1
sin
(
π P ℓj
p 2
j
)
and
3∏
j=1
sign
(
sin
( qj e π
pj
))
= 1
which follows from
sin
( q1 e π
p1
)
= (−1)1+q1(p2p3+ℓ2p3+p2ℓ3) sin
(
π ℓ1
p1
· q1
P
p1
)
= (−1)1+q1(p2p3+ℓ2p3+p2ℓ3)−ℓ1(p2q3+q2p3) sin
( ℓ1 π
p1
)
Collecting these results, we obtain
e−2πiIα/4 = (−1)
1+P +P∑ 3
j=1
ℓj
pj
+∑
j<k (pjpk+ℓj pk+pjℓk)
3∏
j=1
sign
(
sin
( P ℓ j π
p 2
j
))
which proves a phase factor of eq. (6.2). □
We reconsider some examples from section 5;
• the Poincar´ e homology sphereΣ(2 , 3, 5):
We have two triples (ℓ1, ℓ2, ℓ3) = (1 , 1, 1) and (1, 1, 2). These respectively give the
spectral ﬂow (6.4) Iα = 4 and 0, which supports eq. (5.8).
• Σ(2 , 3, 7):
We have (ℓ1, ℓ2, ℓ3) = (1 , 1, 2) and (1, 1, 3), which give Iα = 6 and 2 respectively. This
is consistent with a result in previous section.
19
• Σ(3 , 4, 5):
We have four triples (ℓ1, ℓ2, ℓ3) = (1 , 1, 3), (1, 1, 4), (1, 2, 1), and (1, 2, 2). For these ir-
reducible representations, we get from eq. (6.4)Iα = 2, 4, 6, and 0. This result is consistent
with an asymptotic expansion given before.
7. T HE OHTSUKI INVARIANT
From asymptotic expansions (5.7) and (5.8) of the WRT invari ant, we can introduce a formal
power series which is ignored in section 6. This series may de note a trivial connection contribu-
tion [22, 38, 39]. By regarding e2πi/N as q, we can deﬁne τ∞(M) for a case of 1
p1
+ 1
p2
+ 1
p3
< 1
q
φ(p1,p2,p3)
4 − 1
2 (q − 1) τ∞
(
Σ( p1, p2, p3)
)
= 1
2
∞∑
k=0
L(−2 k, χ(1,1,1)
2P )
k!
( log q
4 P
) k
(7.1)
and for the Poincar´ e homology sphere
q
121
120 (q − 1) τ∞
(
Σ(2 , 3, 5)
)
= q
1
120 + 1
2
∞∑
k=0
L(−2 k, χ(1,1,1)
60 )
k!
( log q
120
) k
(7.2)
