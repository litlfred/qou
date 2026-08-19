---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-071-432-reﬁnement-and-categoriﬁcation
section_title: "Reﬁnement and categoriﬁcation"
section_number: 4.3.2
pages: 65-66
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
The reﬁned version of ( 4.43) reads
(qt;q)∞ˆZa(q,t ;Wλ) = 1
|Wb|
∫ dz
2πiz
(z2;q)∞(z−2;q)∞
(z2tq;q)∞(z−2tq;q)∞
χλ(z)
∑
n∈pZ+b
qn2/pz2n. (4.48)
One can show that it has the positivity property ( 3.87) and, therefore, can be interpreted as
the Poincar´ e polynomial of the homological invariant that categoriﬁesSU (2) WRT invariants
of M3 =L(p, 1) with knots wrapping the Hopf ﬁber.
For example, consider M3 = L(5, 1). With our choice of G = SU (2), it has three
abelian ﬂat connections and, correspondingly, three homological blocks, all tabulated in [27,
sec.6]. Now, we can see that incorporating knots does not spoil the positivity of ( 4.48) and
its interpretation as the Poincar´ e polynomial. Yet, the presence of the knot changes all
homological blocks in a non-trivial way, mixing homological invariants of the knot K and the
ambient 3-manifold M3 in one combined entity, e.g. for M3 =L(5, 1) and λ = 2:
− (−qt;q)∞ˆZ0(q,−t;W2) = (t + 1)q +
(
t2 + 2t + 1
)
q2 +
(
t3 + 3t2 + 4t + 2
)
q3+
(
t4 + 4t3 + 8t2 + 8t + 3
)
q4 +
(
t5 + 4t4 + 10t3 + 16t2 + 14t + 5
)
q5+
(
t6 + 4t5 + 11t4 + 23t3 + 31t2 + 23t + 7
)
q6+
(
t7 + 4t6 + 12t5 + 28t4 + 47t3 + 54t2 + 37t + 11
)
q7 +O
(
q8)
, (4.49)
(−qt;q)∞ˆZ1(q,−t;W2) = 5√q+(t+1)q6/5+
(
2t2 + 4t + 2
)
q11/5+
(
2t3 + 6t2 + 8t + 4
)
q16/5+
(
2t4 + 7t3 + 14t2 + 15t + 6
)
q21/5 +
(
2t5 + 8t4 + 19t3 + 29t2 + 25t + 9
)
q26/5+
(
2t6 + 8t5 + 22t4 + 43t3 + 55t2 + 41t + 13
)
q31/5 +O
(
q36/5
)
, (4.50)
and
−(−qt;q)∞ˆZ2(q,−t;W2) =q4/5+(t+1)q9/5+
(
t2 + 2t + 1
)
q14/5+
(
2t3 + 4t2 + 4t + 2
)
q19/5+
(
2t4 + 5t3 + 8t2 + 8t + 3
)
q24/5 +
(
2t5 + 5t4 + 11t3 + 17t2 + 13t + 4
)
q29/5+
(
2t6 + 6t5 + 14t4 + 25t3 + 29t2 + 21t + 7
)
q34/5 +O
(
q36/5
)
. (4.51)
Note that, when p = 1, we have L(p, 1)∼= S3 and the unknot wrapping the Hopf ﬁber
becomes the familiar unknot inS3, yet with a nontrivial framing equal to 1. SinceH1(S3, Z) =
0, as in section 4.2, we expect factorization in this case:
Wλ =W0⊗H 0;i,j;𝓁
λ , (4.52)
– 64 –
Ha[S3;Kλ,Rλ] =
⨁
i,j,𝓁∈Z
H0;i,j;𝓁
λ ⊗Ha[S3] (4.53)
Moreover, as in section 4.2, we expect that (Kλ,Rλ) is the cabling of the unknot determined
byλ. In appendix B, we present evidence for this by comparing it with the ordinary Khovanov
homology of the cabling of the unknot, cf. [80].
