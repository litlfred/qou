---
doc_id: arxiv-1908.11677v1
doc_title: "Variational formulae and estimates of O’Hara’s knot energies"
section_id: sec-003-32-estimates-and-continuity-of-the-quantities-in
section_title: "Estimates and continuity of the quantities in (??)"
section_number: 3.2
pages: 12-19
source_pdf: 1908.11677v1.pdf
source_sha256: c53663eeb457daf9
doc_brief: "Variational formulae and estimates of O’Hara’s knot energies — O’Hara’s energies, introduced by Jun O’Hara, were proposedto answer the question of what is the canonical shape in a given knot typ e"
---
As we can see from Lemma 2.4, δN (τ )[φ ] and δN (τ )[φ , ψ ] may be expressed
in terms of N (u, v) and K (u, v). First, we discuss N (u, v).
Lemma 3.1. Assume that f is bi-Lipschitz. Then, the following properties
hold.
1. Let α ∈ (0, ∞) and p ∈ [1, ∞) satisfy 2 ≤ αp < 2p + 1 . If u, v ∈
W σ, 2p(R/ LZ, Rd), then there exists C = C(f ) > 0 such that
‖‖‖‖
N (u, v)
‖∆f ‖α
Rn
‖‖‖‖
Lp
≤ C[u]W σ, 2p [v]W σ, 2p .
2. Let 0 < β ≤ 1. If u,v ∈ C0,β (R/ LZ, Rd), then there exists C = C(f ) > 0
such that ‖‖‖‖D(f )α −2β N (u, v)
‖∆f ‖α
Rn
‖‖‖‖
L∞
≤ C[u]C 0,β [v]C 0,β .
3. Let 0 < β ≤ 1. If u,v ∈ X β (R/ LZ, Rd), then for s ∈ R/ LZ,
lim
(s1,s 2)→(s,s )
|∆ s|α −2β N (u, v)
‖∆f ‖α
Rn
=



0 (0 < β < 1),
1
12u′(s) ·v′(s) ( β = 1)
holds.
Proof. 1. By H¨ older’s inequality and the bi-Lipschitz continuity of f , we
have
‖‖‖‖
N (u, v)
‖∆f ‖α
Rn
‖‖‖‖
p
Lp
= 1
2p
∫
R/ LZ
∫ s2+ L
2
s2− L
2
1
‖∆f ‖αp +2p
Rn
⏐⏐⏐⏐
∫ s1
s2
∫ s1
s2
∆ 3
4u · ∆ 3
4vds3ds4
⏐⏐⏐⏐
p
ds1ds2
≤ C
∫
R/ LZ
∫ s2+ L
2
s2− L
2
1
|∆ s|αp +2
∫ s1
s2
∫ s1
s2
‖∆ 3
4u‖p
Rd ‖∆ 3
4v‖p
Rdds3ds4ds1ds2
= (†).
We change variables
t1 = s1 − s2, t 2 = s2, s 3 = t2 + t1t3, s 4 = t2 + t1t4
in ( †). Then, we obtain
(†) = C
∫
R/ LZ
∫ L
2
− L
2
1
|t1|αp
×
∫ 1
0
∫ 1
0
‖u(t2+t1t3)−u(t2+t1t4)‖p
Rd ‖v(t2+t1t3)−v(t2+t1t4)‖p
Rd dt3dt4dt1dt2
= (‡).
We use Fubini’s theorem and change variables
w1 = (t3 − t4)t1, w 2 = t2 + t1t4
12
in ( ‡). Then, we obtain
(‡) = C
∫ 1
0
∫ 1
0
∫ L
2
− L
2
∫
R/ LZ
1
|t1|αp
× ‖u(t2 + t1t3) −u(t2 + t1t4)‖p
Rd ‖v(t2 + t1t3) −v(t2 + t1t4)‖p
Rd dt2dt1dt3dt4
= C
∫ 1
0
∫ 1
0
∫ L
2 |t3−t4|
− L
2 |t3−t4|
∫
R/ LZ
1
|w1|αp |t3 − t4|αp −1
× ‖u(w1 + w2) −u(w2)‖p
Rd ‖v(w1 + w2) −v(w2)‖p
Rd dw1dw2dt3dt4
≤ C
∫
R/ LZ
∫ L
2
− L
2
‖u(w1 + w2) −u(w2)‖p
Rd
|w1|
αp
2
‖v(w1 + w2) −v(w2)‖p
Rd
|w1|
αp
2
dw1dw2
≤ C[u]p
W σ, 2p [v]p
W σ, 2p ,
by H¨ older’s inequality, and the claim holds.
2. Without loss of generality, we assume that s1, s2 ∈ R/ LZ satisfy 0 <
|∆ s| < L/ 2. Then, we have
⏐⏐⏐⏐|∆ s|α −2β N (u, v)
‖∆f ‖α
Rn
⏐⏐⏐⏐ ≤ C|∆ s|−2β −2
∫ s1
s2
∫ s1
s2
‖∆ 3
4u‖Rd‖∆ 3
4v‖Rd ds3ds4
≤ C|∆ s|−2
∫ s1
s2
∫ s1
s2
‖∆ 3
4u‖Rd
|∆ 3
4s|β
‖∆ 3
4v‖Rd
|∆ 3
4s|β ds3ds4
≤ C[u′]C 0,β [v′]C 0,β .
3. First, we consider the case where 0 < β < 1, i.e. u,v ∈ h0,β (R/ LZ, Rd).
As is well known, the little H¨ older space h0,β is characterized as
h0,β (R/ LZ, Rd) =
{
u ∈ C0,β (R/ LZ, Rd)
⏐⏐⏐⏐ lim
R→+0
[u]C 0,β ,R = 0
}
,
where
[u]C 0,β ,R = sup
s1,s 2∈R/ LZ
0<|∆ s|<R
‖∆u‖Rd
|∆ s|β .
For R > 0, let s1, s2 ∈ R/ LZ satisfy 0 < |∆ s| < R. Then, we have
⏐⏐⏐⏐|∆ s|α −2β N (u, v)
‖∆f ‖α
Rn
⏐⏐⏐⏐ ≤ C[u]C 0,β ,R [v]C 0,β ,R . (3.4)
Taking lim sup on left-hand side in (3.4), we have
lim sup
(s1,s 2)→(s,s )
⏐⏐⏐⏐|∆ s|α −2β N (u, v)
‖∆f ‖α
Rn
⏐⏐⏐⏐ ≤ C[u]C 0,β ,R [v]C 0,β ,R .
Taking R → +0 on right-hand side, we obtain
lim
(s1,s 2)→(s,s )
|∆ s|α −2β N (u, v)
‖∆f ‖α
Rn
= 0.
13
Next, we assume u, v ∈ C1. If s5, s6 ∈ R/ LZ are such that ‖(s5, s 6) −
(s, s )‖R2 is suﬃciently small, we can take ε > 0 arbitrarily such that
‖u′(s5)−u′(s)‖Rd ≤ ε
2(‖v′‖L∞ + 1) , ‖v′(s6)−v′(s)‖Rd ≤ ε
2(‖u′‖L∞ + 1) .
Then, using the fact that
∫ s1
s2
∫ s1
s2
∫ s3
s4
∫ s3
s4
ds5ds6ds3ds4 = 1
6 |∆ s|2,
we have
⏐⏐⏐⏐
1
|∆ s|4
∫ s1
s2
∫ s1
s2
∫ s3
s4
∫ s3
s4
u′(s5) ·v′(s6)ds5ds6ds3ds4 − 1
6u′(s) ·v′(s)
⏐⏐⏐⏐
≤ 1
|∆ s|4
∫ s1
s2
∫ s1
s2
∫ s3
s4
∫ s3
s4
|u′(s5) ·v′(s6) −u′(s) ·v′(s)|ds5ds6ds3ds4
≤ 1
|∆ s|4
∫ s1
s2
∫ s1
s2
∫ s3
s4
∫ s3
s4
(‖u′(s5)‖Rd‖v′(s6) −v′(s)‖Rd
+ ‖v′(s)‖Rd ‖u′(s5) −u′(s)‖Rd )ds5ds6ds3ds4
≤ ε.
Hence, we have
lim
(s1,s 2)→(s,s )
1
|∆ s|4
∫ s1
s2
∫ s1
s2
∫ s3
s4
∫ s3
s4
u′(s5) ·v′(s6)ds5ds6ds3ds4
= 1
6u′(s) ·v′(s).
Using this and
lim
(s1,s 2)→(s,s )
|∆ s|
‖∆f ‖Rn
= 1
‖τ (s)‖Rn
= 1,
we obtain
|∆ s|α −2 N (u, v)
‖∆f ‖α
Rn
= 1
2
|∆ s|α +2
‖∆f ‖α +2
Rn
1
|∆ s|4
∫ s1
s2
∫ s1
s2
∫ s3
s4
∫ s3
s4
u′(s5) ·v′(s6)ds5ds6ds3ds4
→ 1
12u′(s) ·v′(s) as ( s1, s 2) → (s, s ).
Since the function K (u, v) fulﬁlls
|K (u, v)| ≤ C‖u′‖L∞ ‖v′‖L∞ , lim
(s1,s 2)→(s,s )
K (u, v) =u′(s) ·v′(s),
we obtain estimates and continuity of δ‖∆f ‖2
Rn[φ ]
‖∆f ‖2
Rn
and δ2‖∆f ‖2
Rn[φ , ψ ]
‖∆f ‖2
Rn
from
Lemma 2.2 as follows.
14
Lemma 3.2. 1. Assume that f , φ , ψ ∈ W 1, ∞(R/ LZ, Rn) and f is bi-
Lipschitz. Then, there exists C = C(f ) > 0 such that
‖‖‖‖
δ‖∆f ‖2
Rn[φ ]
‖∆f ‖2
Rn
‖‖‖‖
L∞
≤ C‖φ ′‖L∞ ,
‖‖‖‖
δ2‖∆f ‖2
Rn[φ , ψ ]
‖∆f ‖2
Rn
‖‖‖‖
L∞
≤ C‖φ ′‖L∞ ‖ψ ′‖L∞ .
2. Iff ,φ ,ψ ∈ C1(R/ LZ, Rn), then it follows that
lim
(s1,s 2)→(s,s )
δ‖∆f ‖2
Rn[φ ]
‖∆f ‖2
Rn
=τ (s) ·φ ′(s),
lim
(s1,s 2)→(s,s )
δ2‖∆f ‖2
Rn[φ , ψ ]
‖∆f ‖2
Rn
=φ ′(s) ·ψ ′(s)
for s ∈ R/ LZ.
To deal with S5(f ), we need estimates for τ ·φ ′. The proof is easy, therefore
we omit the details.
Lemma 3.3. Assume that f is bi-Lipschitz. Then, the following properties
hold.
1. Let α ∈ (0, ∞) and p ∈ [1, ∞) satisfy 2 ≤ αp < 2p + 1 . If f , φ ∈
W 1+σ, 2p(R/ LZ, Rn) ∩ W 1, ∞(R/ LZ, Rd), then there exists C = C(f ) > 0
such that
[(τ ·φ ′)]W σ, 2p ≤ C(‖τ ‖L∞ [φ ′]W σ, 2p + [τ ]W σ, 2p ‖φ ′‖L∞ ).
2. Let 0 < β ≤ 1. If f ,φ ∈ C1,β (R/ LZ, Rn), then it holds that
[(τ ·φ ′)]C 0,β ≤ ‖τ ‖L∞ [φ ′]C 0,β + [τ ]C 0,β ‖φ ′‖L∞ .
3. Let 0 < β ≤ 1. If τ , φ ′ ∈ X β (R/ LZ, Rn), then (τ ·φ ′) ∈ X β (R/ LZ, R).
Moreover, if f ,φ ∈ C2(R/ LZ, Rn), then it holds that
d
ds (τ (s) ·φ ′(s)) =κ (s) ·φ ′(s) +τ (s) ·φ ′′(s)
for s ∈ R/ LZ.
3.3 Proof of Theorem 1.1
In this subsection we complete the proof of Theorem 1.1 combining th e facts
in previous subsection. First, we show the L1-estimates of the ﬁrst and second
variational formulae for M(α,p )(f ). Using the expression of the ﬁrst and second
15
variational formulae for N (τ ) in Lemma 2.4, it follows that
‖‖‖‖
R1(f )[φ ]
‖∆f ‖α
Rn
‖‖‖‖
Lp
≤ C‖φ ′‖L∞ ,
‖‖‖‖
R2(f )[φ ]
‖∆f ‖α
Rn
‖‖‖‖
Lp
≤ C[φ ′]W σ, 2p ,
‖‖‖‖
S1(f )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
Lp
≤ C‖φ ′‖L∞ ‖ψ ′‖L∞ ,
‖‖‖‖
S2(f )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
Lp
≤ C{‖φ ′‖L∞ (‖ψ ′‖L∞ + [ψ ′]W σ, 2p ) + ‖ψ ′‖L∞ (‖φ ′‖L∞ + [φ ′]W σ, 2p )},
‖‖‖‖
S3(f )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
Lp
≤ C(‖ψ ′‖L∞ [φ ′]W σ, 2p + ‖φ ′‖L∞ [ψ ′]W σ, 2p ),
‖‖‖‖
S4(f )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
Lp
≤ C[φ ′]W σ, 2p [ψ ′]W σ, 2p ,
‖‖‖‖
S5(f )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
Lp
≤ C([φ ′]W σ, 2p + ‖φ ′‖L∞ )([ψ ′]W σ, 2p + ‖ψ ′‖L∞ )
by Lemmas 3.1 and 3.3. Hence, from these estimates and Lemma 3.2, w e obtain
‖‖‖‖
δN (τ )[φ ]
‖∆f ‖α
Rn
‖‖‖‖
Lp
≤ C‖φ ′‖W σ, 2p∩L∞
‖‖‖‖
δN (τ )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
Lp
≤ C‖φ ′‖W σ, 2p∩L∞ ‖ψ ′‖W σ, 2p∩L∞ ,
and L1-estimates for G(α,p )(f ) and H(α,p )(f ).
Next, we consider L∞-estimates of M(α,p )(f ), G(α,p )(f ), and H(α,p )(f ) with
the weight |∆ s|α −2β . We assume that f ,φ ,ψ ∈ C1,β and s1, s2 ∈ R/ LZ satisfy
0 < |∆ s| < L/ 2. Because we have
1 − xα ≤
(α
2 + 1
)
(1 − x2)
for all x ∈ [0, 1], it follows that
|∆ s|α −2β Mα (f ) ≤ C 1
|∆ s|2β
(
1 − ‖∆f ‖α
Rn
|∆ s|α
)
≤ C 1
|∆ s|2β
(
1 − ‖∆f ‖2
Rn
|∆ s|2
)
≤ C 1
|∆ s|2β +2
∫ s1
s2
∫ s1
s2
‖∆ 3
4τ ‖2
Rnds3ds4
≤ C. (3.5)
16
Moreover, by Lemmas 3.1–3.3, we have
‖‖‖‖|∆ s|α −2β R1(f )[φ ]
‖∆f ‖α
Rn
‖‖‖‖
L∞
≤ C‖φ ′‖L∞ ,
‖‖‖‖|∆ s|α −2β R2(f )[φ ]
‖∆f ‖α
Rn
‖‖‖‖
L∞
≤ C[φ ′]C 0,β ,
‖‖‖‖|∆ s|α −2β S1(f )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
L∞
≤ C‖φ ′‖L∞ ‖ψ ′‖L∞ ,
‖‖‖‖|∆ s|α −2β S2(f )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
L∞
≤ C{‖φ ′‖L∞ (‖ψ ′‖L∞ + [ψ ′]C 0,β ) + ‖ψ ′‖L∞ (‖φ ′‖L∞ + [φ ′]C 0,β )},
‖‖‖‖|∆ s|α −2β S3(f )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
L∞
≤ C(‖ψ ′‖L∞ [φ ′]C 0,β + ‖φ ′‖L∞ [ψ ′]C 0,β ),
‖‖‖‖|∆ s|α −2β S4(f )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
L∞
≤ C[φ ′]C 0,β [ψ ′]C 0,β ,
‖‖‖‖|∆ s|α −2β S5(f )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
L∞
≤ C([φ ′]C 0,β + ‖φ ′‖L∞ )([ψ ′]C 0,β + ‖ψ ′‖L∞ ).
Therefore, we obtain
‖‖‖‖|∆ s|α −2β δN (τ )[φ ]
‖∆f ‖α
Rn
‖‖‖‖
L∞
≤ C‖φ ′‖C 0,β
‖‖‖‖|∆ s|α −2β δ2N (τ )[φ , ψ ]
‖∆f ‖α
Rn
‖‖‖‖
L∞
≤ C‖φ ′‖C 0,β ‖ψ ′‖C 0,β ,
and the L∞-estimates for M(α,p )(f ), G(α,p )(f ), and H(α,p )(f ) with the weight
|∆ s|α −2β .
Lastly, we consider the continuity. Because continuity on the outs ide of the
diagonal set is clear, we consider the property on the diagonal set . First, we
assume f , φ , ψ ∈ h1,β with 0 < β < 1, and f is bi-Lipschitz. Let R > 0 be
suﬃciently small. In a similar manner to the proof of (3.5), it holds that
|∆ s|α −2β Mα (f ) ≤ ˜C[τ ]C 0,β ,R
for 0 < |∆ s| < R, and therefore
lim
(s1,s 2)→(s,s )
|∆ s|α −2β Mα (f ) = 0 ,
where ˜C is a positive constant depending only on α , p, and Cb. Moreover, by
Lemma 3.1, we have
lim
(s1,s 2)→(s,s )
⏐⏐⏐⏐|∆ s|α −2β Ri(f )[φ ]
‖∆f ‖α
Rn
⏐⏐⏐⏐ = 0, (i = 1, 2),
lim
(s1,s 2)→(s,s )
⏐⏐⏐⏐|∆ s|α −2β Si(f )[φ , ψ ]
‖∆f ‖α
Rn
⏐⏐⏐⏐ = 0, (i = 1, . . . , 5).
Considering Lemma 3.2, we obtain the desired continuity when f ,φ ,ψ ∈ h1,β
with 0 < β < 1.
17
Next, we consider the case where β = 1. We denote the curvature vector of
f byκ , i.e. κ =f ′′. Using Lemma 3.1 and L’Hospital’s theorem, we have
|∆ s|α −2Mα (f ) = |∆ s|α −2 ϕ α (N (τ ))
‖∆f ‖α
Rn
= |∆ s|α −2 ϕ 2(N (τ ))
‖∆f ‖α
Rn
ϕ α (N (τ ))
ϕ 2(N (τ ))
= |∆ s|α −2 N (τ )
‖∆f ‖α
Rn
1
1 + N (τ )
ϕ α (N (τ ))
ϕ 2(N (τ ))
→ α
24 ‖κ (s)‖2
Rn as ( s1, s 2) → (s, s ).
Similarly, it follows that
|∆ s|α −2 R1(f )[φ ]
‖∆f ‖α
Rn
→ − 1
6τ (s) ·φ ′(s)‖κ (s)‖2
Rn ,
|∆ s|α −2 R2(f )[φ ]
‖∆f ‖α
Rn
→ 1
6κ (s) ·φ ′′(s),
|∆ s|α −2 S1(f )[φ , ψ ]
‖∆f ‖α
Rn
→ − 1
6 {φ ′(s) ·ψ ′(s) − (τ (s) ·φ ′(s))(τ (s) ·ψ ′(s))}‖κ (s)‖2
Rn ,
|∆ s|α −2 S2(f )[φ , ψ ]
‖∆f ‖α
Rn
→ 1
6 (τ (s) ·φ ′(s))(κ (s) ·ψ ′′(s) −τ (s) ·ψ ′(s)‖κ (s)‖2
Rn )
+ 1
6 (τ (s) ·ψ ′(s))(κ (s) ·φ ′′(s) −τ (s) ·φ ′(s)‖κ (s)‖2
Rn ),
|∆ s|α −2 S3(f )[φ , ψ ]
‖∆f ‖α
Rn
→ − 1
6 (τ (s) ·ψ ′(s))(κ (s) ·φ ′′(s)) − 1
6 (τ (s) ·φ ′(s))(κ (s) ·ψ ′′(s)),
|∆ s|α −2 S4(f )[φ , ψ ]
‖∆f ‖α
Rn
→ 1
6φ ′′(s) ·ψ ′′(s),
|∆ s|α −2 S5(f )[φ , ψ ]
‖∆f ‖α
Rn
→ − 1
6 {(τ (s) ·φ ′′(s)) + (φ ′(s) ·κ (s))}{(τ (s) ·ψ ′′(s)) + (ψ ′(s) ·κ (s))}
as ( s1, s 2) → (s, s ). Hence, the desired continuity holds when f ,φ ,ψ ∈ C2.
This completes the proof of Theorem 1.1. □
References
[1] A. Abrams, J. Cantarella, J. H. G. Fu, M. Ghomi, and R. Howard, Circles
minimize most knot energies , Topology, 42 (2) (2003), 381–394.
[2] S. Blatt, The gradient ﬂow of the M¨ obius energy near local minimizers ,
Calc. Var. Partial Diﬀerential Equations, 43 (1) (2012), 1250010, 9 pp.
[3] S. Blatt, Boundedness and regularizing eﬀects of O’Hara’s knot energ ies,
J. Knot Theory Ramiﬁcations, 21 (2012), 1250010, 9pp.
[4] S. Blatt, The gradient ﬂow of O’Hara’s knot energies , Math. Ann., 370
(3–4) (2018), 993–1061.
18
[5] S. Blatt, P. Reiter, and A. Schikorra, Harmonic analysis meets critical
knots. Critical points of the M¨ obius energy are smooth, Trans. Amer. Math.
Soc. 368 (9) (2016), 6391–6438.
[6] S. Blatt and P. Reiter, Stationary points of O’Hara’s knot energies ,
Manuscripta Math., 140 (1–2) (2013), 29–50.
[7] S. Blatt and N. Vorderobermeier, On the analyticity of critical points of the
M¨ obius energy, Calc. Var. Partial Diﬀerential Equations, 58 (1) (2019), 28
pp.
[8] M. H. Freedman, Z.-X. He, and Z. Wang, M¨ obius energy of knots and
unknots, Ann. of Math., 139 (1994), 1–50.
[9] Z.-X. He, The Euler-Lagrange equation and heat ﬂow for the M¨ obius energy,
Comm. Pure Appl. Math., 53 (4) (2000), 399–431.
[10] A. Ishizeki and T. Nagasawa, A decomposition theorem of the M¨ obius energy
I: Decomposition and M¨ obius invariance, Kodai. Math. J., 37 (3) (2014),
737–754.
[11] A. Ishizeki and T. Nagasawa, A decomposition theorem of the M¨ obius energy
I I: Variational formulae and estimates, Math. Ann., 363 (1–2) (2015), 617–
635.
[12] A. Ishizeki and T. Nagasawa, Decomposition of generalized O’Hara’s ener-
gies, preprint, arXiv:1904.06812 (2019).
[13] J. O’Hara, Energy of a knot , Topology, 30 (2) (1991), 241–247.
[14] J. O’Hara, Family of energy functionals of knots , Topology Appl., 48 (2)
(1992), 147–161.
[15] J. O’Hara, Energy functionals of knots I I , Topology Appl., 56 (1) (1994),
45–61.
[16] P. Reiter, Repulsive knot energies and pseudodiﬀerential calculus fo r
O’Hara’s knot energy familyE(α ), α ∈ [2, 3), Math. Nachr., 285 (7) (2012),
889–913.
19
