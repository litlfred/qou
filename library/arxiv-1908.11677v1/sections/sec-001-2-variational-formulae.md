---
doc_id: arxiv-1908.11677v1
doc_title: "Variational formulae and estimates of O’Hara’s knot energies"
section_id: sec-001-2-variational-formulae
section_title: "Variational formulae"
section_number: 2
pages: 5-11
source_pdf: 1908.11677v1.pdf
source_sha256: c53663eeb457daf9
---
We begin by recalling the deﬁnition of the function N . For functions u, v :
R/ LZ → Rd, where d = 1 or n, we set
N (u, v) = 1
2‖∆f‖2
Rn
∫ s1
s2
∫ s1
s2
∆ 3
4u · ∆ 3
4vds3ds4.
We use N (u) instead of N (u, u) for simplicity.
Setting
Mα (f ) = ϕ α (N (τ ))
‖∆f ‖α
Rn
, (2.1)
then the energy can be written as
E(α,p )(f ) =
∫∫
(R/ LZ)2
(Mα (f ))pds1ds2.
The ﬁrst variational formula G(α,p ) can be derived as
G(α,p )(f )[φ ]ds1ds2 = δ{(Mα (f ))p}[φ ]ds1ds2 + Mα (f )δ(ds1ds2)[φ ],
and
δ{(Mα (f ))p}[φ ] = p(Mα (f ))p−1δMα (f )[φ ].
The second variational formula H(α,p ) is calculated similarly. Since δ(dsj)[φ ] =
τ (sj ) ·φ ′(sj )dsj holds (see, for example, [11]), we obtain the following.
5
Theorem 2.1. G(α,p )(f )[φ ] and H(α,p )(f )[φ , ψ ] can be written as
G(α,p )(f )[φ ] =
2∑
i=1
Gi(f )[φ ], H(α,p )(f )[φ , ψ ] =
6∑
i=1
Hi(f )[φ , ψ ],
where
G1(f )[φ ] = p(Mα (f ))p−1δMα (f )[φ ],
G2(f )[φ ] = ( Mα (f ))p(τ (s1) ·φ ′(s1) +τ (s2) ·φ ′(s2)),
H1(f )[φ , ψ ] = p(Mα (f ))p−1δ2Mα (f )[φ , ψ ],
H2(f )[φ , ψ ] = p(p − 1)(Mα (f ))p−2δMα (f )[φ ]δMα (f )[ψ ],
H3(f )[φ , ψ ] = G1(f )[φ ](τ (s1) ·ψ ′(s1) +τ (s2) ·ψ ′(s2)),
H4(f )[φ , ψ ] = G1(f )[ψ ](τ (s1) ·φ ′(s1) +τ (s2) ·φ ′(s2)),
H5(f )[φ , ψ ] = ( Mα (f ))p{φ ′(s1) ·ψ ′(s1) +φ ′(s2) ·ψ ′(s2)
−2(τ (s1) ·φ ′(s1))(τ (s1) ·ψ ′(s1)) − 2(τ (s2) ·φ ′(s2))(τ (s2) ·ψ ′(s2))
}
,
H6(f )[φ , ψ ] = ( Mα (f ))p(τ (s1) ·φ ′(s1) +τ (s2) ·φ ′(s2))(τ (s1) ·ψ ′(s1) +τ (s2) ·ψ ′(s2)).
In the remainder of this section, we will give the exact expression of δMα (f )[φ ]
and δ2Mα (f )[φ , ψ ]. First we note that, by (2.1), we have
δMα (f )[φ ] = ϕ ′
α (N (τ )) δN (τ )[φ ]
‖∆f ‖α
Rn
− α
2
ϕ α (N (τ ))δ‖∆f ‖2
Rn[φ ]
‖∆f ‖α +2
Rn
, (2.2)
and therefore we need variational formulae for N (τ ), and ‖∆f ‖2
Rn. It follows
from the deﬁnition of N (τ ) that δN (τ ) can be written in terms of δτ as well as
δ‖∆f ‖2
Rn. We can derive the second variational formula from the correspon ding
ingredients.
Firstly, we show the ingredients as Lemma 2.2. The variational formu lae
δN (τ ) and δ2N (τ ) will be given in the forthcoming Lemma 2.4. Also, we give
representations of δMα (f ) and δ2Mα (f ) in Proposition 2.5.
Foru,v : R/ LZ → Rn, let
K (u, v) = ∆u · ∆v
‖∆f ‖2
Rn
.
Lemma 2.2. The following variational formulae hold.
1. δτ (sj)[φ ] =φ ′(sj) − (τ (sj) ·φ ′(sj ))τ (sj).
2. δ‖∆ i
jτ ‖2
Rn[φ ] = 2∆ i
jτ · ∆ i
jφ ′ − ‖∆ i
jτ ‖2
Rn (τ (si) ·φ ′(si) +τ (sj) ·φ ′(sj)).
3. δ‖∆f ‖2
Rn[φ ] = 2 K (f , φ )‖∆f ‖2
Rn .
4. δ
( 1
‖∆f ‖2
Rn
)
[φ ] = −2 K (f , φ )
‖∆f‖2
Rn
.
5. δ2‖∆f ‖2
Rn[φ , ψ ] = 2 K (φ , ψ )‖∆f ‖2
Rn.
Proof. See [11, Lemma 1].
Before proving Lemma 2.4, we establish the following sublemma.
6
Lemma 2.3. 1. Assume thatu : R/ LZ → Rn isτ orφ ′. Then, δN (τ , u)[ψ ]
can be written as
δN (τ , u)[ψ ] = −2K (f , ψ )N (τ , u)
+ 1
2‖∆f‖Rn
∫ s1
s2
∫ s1
s2
{δ(∆ 3
4τ · ∆ 3
4u)[ψ ]
+ (∆ 3
4τ · ∆ 3
4u)(τ (s3) ·ψ ′(s3) +τ (s4) ·ψ ′(s4))}ds3ds4,
where
δ(∆ 3
4τ · ∆ 3
4u)[ψ ]
=



2∆ 3
4τ · ∆ 3
4φ ′ − ‖∆ 3
4τ ‖2
Rn(τ (s3) ·φ ′(s3) +τ (s4) ·φ ′(s4)), u =τ ,
∆ 3
4φ ′ · ∆ 3
4ψ ′ − (∆ 3
4τ · ∆ 3
4φ ′)(τ (s3) ·ψ ′(s3) +τ (s4) ·ψ ′(s4))
− {∆ 3
4(τ ·φ ′)}{∆ 3
4(τ ·ψ ′)}, u =φ ′.
2. It holds that
δK (f , φ )[ψ ] = K (φ , ψ ) − 2K (f , φ )K (f , ψ ).
Proof. 1. By Lemma 2.2, we have
δN (τ , u)[ψ ] = δ
( 1
2‖∆f‖2
Rn
∫ s1
s2
∫ s1
s2
∆ 3
4τ · ∆ 3
4uds3ds4
)
[ψ ]
= 1
2 δ
( 1
‖∆f ‖2
Rn
)
[ψ ]
∫ s1
s2
∫ s1
s2
∆ 3
4τ · ∆ 3
4uds3ds4
+ 1
2‖∆f‖2
Rn
∫ s1
s2
∫ s1
s2
δ(∆ 3
4τ · ∆ 3
4u)[ψ ]ds3ds4
+ 1
2‖∆f‖2
Rn
∫ s1
s2
∫ s1
s2
(∆ 3
4τ · ∆ 3
4u)δ(ds3ds4)[ψ ]
= −2K (f , ψ )N (τ , u) + 1
2‖∆f‖2
Rn
∫ s1
s2
∫ s1
s2
{δ(∆ 3
4τ · ∆ 3
4u)[φ ]
+ (∆ 3
4τ · ∆ 3
4u)(τ (s3) ·ψ ′(s3) +τ (s4) ·ψ ′(s4))}ds3ds4.
It remains to calculate δ(∆ 3
4τ · ∆ 3
4u)[φ ]. Since the case where u =τ may
be handled by Lemma 2.2, we deal with the case where u =φ ′. Then, it
7
follows from Lemma 2.2 and δφ ′(sj )[ψ ] = −(τ (sj) ·ψ ′(sj))φ ′(sj) that
δ(∆ 3
4τ · ∆ 3
4φ ′)[ψ ]
= δ(∆ 3
4τ )[ψ ] · ∆ 3
4φ ′ + ∆ 3
4τ · δ(∆ 3
4φ ′)[ψ ]
= ∆ 3
4ψ ′ · ∆ 3
4φ ′ − ∆ 3
4{(τ ·ψ ′)τ } · ∆ 3
4φ ′ − ∆ 3
4τ · ∆ 3
4{(τ ·ψ ′)φ ′}
= ∆ 3
4φ ′ · ∆ 3
4ψ ′ − [(τ (s3) ·ψ ′(s3))∆ 3
4τ + {∆ 3
4(τ ·ψ ′)}τ (s4)] · ∆ 3
4φ ′
− ∆ 3
4τ · [{∆ 3
4(τ ·ψ ′)}φ ′(s3) + (τ (s4) ·ψ ′(s4))∆ 3
4φ ′]
= ∆ 3
4φ ′ · ∆ 3
4ψ ′
− (∆ 3
4τ · ∆ 3
4φ ′)(τ (s3) ·ψ ′(s3) +τ (s4) ·ψ ′(s4))
− {∆ 3
4(τ ·ψ ′)}(τ (s4) · ∆ 3
4φ ′ + ∆ 3
4τ ·φ ′(s3))
= ∆ 3
4φ ′ · ∆ 3
4ψ ′
− (∆ 3
4τ · ∆ 3
4φ ′)(τ (s3) ·ψ ′(s3) +τ (s4) ·ψ ′(s4))
− {∆ 3
4(τ ·φ ′)}{∆ 3
4(τ ·ψ ′)}.
2. Using Lemma 2.2, we have
δK (f , φ )[ψ ] = δ(∆f · ∆φ )[ψ ]
‖∆f ‖2
Rn
+ (∆f · ∆φ )δ
( 1
‖∆f ‖2
Rn
)
[ψ ]
= ∆ψ · ∆φ
‖∆f ‖2
Rn
− 2∆f · ∆φ K (f , ψ )
‖∆f ‖2
Rn
= K (φ , ψ ) − 2K (f , φ )K (f , ψ ).
Lemma 2.4. δN (τ )[φ ] and δ2N (τ )[φ , ψ ] can be written as
δN (τ )[φ ] =
2∑
i=1
Ri(f )[φ ], δ 2N (τ )[φ , ψ ] =
5∑
i=1
Si(f )[φ , ψ ],
where
R1(f )[φ ] = −2K (f , φ )N (τ ),
R2(f )[φ ] = 2 N (τ , φ ′),
S1(f )[φ , ψ ] = −2(K (φ , ψ ) − 2K (f , φ )K (f , ψ ))N (τ ),
S2(f )[φ , ψ ] = −K (f , φ )δN (τ )[ψ ] − K (f , ψ )δN (τ )[φ ],
S3(f )[φ , ψ ] = −2K (f , ψ )N (τ , φ ′) − 2K (f , φ )N (τ , ψ ′),
S4(f )[φ , ψ ] = 2 N (φ ′, ψ ′),
S5(f )[φ , ψ ] = −2N ((τ ·φ ′), (τ ·ψ ′)).
8
Proof. By Lemmas 2.2 and 2.3, we have
δN (τ )[φ ] = −2K (f , φ )N (τ )
+ 1
2‖∆f ‖2
Rn
∫ s1
s2
∫ s1
s2
{δ‖∆ 3
4τ ‖2
Rn [φ ]
+ ‖∆ 3
4τ ‖2
Rn(τ (s3) ·φ ′(s3) +τ (s4) ·φ ′(s4))}ds3ds4
= −2K (f , φ )N (τ ) + 1
‖∆f ‖2
Rn
∫ s1
s2
∫ s1
s2
∆ 3
4τ · ∆ 3
4φ ′ds3ds4
= −2K (f , φ )N (τ ) + 2N (τ , φ ′)
=
2∑
i=1
Ri(f )[φ ].
Next we calculate δ2N (τ )[φ , ψ ]. Firstly, we have
δ2N (τ )[φ , ψ ] = 1
2 δ(δN (τ )[φ ])[ψ ] + 1
2 δ(δN (τ )[ψ ])[φ ].
By the symmetry with respect toφ andψ , it is suﬃcient to calculate δ(δN (τ )[φ ])[ψ ],
for which we ﬁrst note that
δ(δN (τ )[φ ])[ψ ] =
2∑
i=1
δ(Ri(f )[φ ])[ψ ].
Using Lemma 2.3 again, we can show that
δ(R1(f )[φ ])[ψ ] = −2δK (f , φ )[ψ ]N (τ ) − 2K (f , φ )δN (τ )[ψ ]
= −2K (φ , ψ )N (τ ) + 4K (f , φ )K (f , ψ )N (τ )
− 2K (f , φ )δN (τ )[ψ ],
and
δ(R2(f )[φ ])[ψ ] = 2 δ(N (τ , φ ′))[ψ ]
= −4K (f , ψ )N (τ , φ ′)
+ 1
‖∆f ‖2
Rn
∫ s1
s2
∫ s1
s2
[∆ 3
4φ ′ · ∆ 3
4ψ ′
− (∆ 3
4τ · ∆ 3
4φ ′)(τ (s3) ·ψ ′(s3) +τ (s4) ·ψ ′(s4))
− {∆ 3
4(τ ·φ ′)}{∆ 3
4(τ ·ψ ′)}
+ (∆ 3
4τ · ∆ 3
4φ ′)(τ (s3) ·ψ ′(s3) +τ (s4) ·ψ ′(s4))]ds3ds4
= −4K (f , ψ )N (τ , φ ′) + 2N (φ ′, ψ ′) − 2N ((τ ·φ ′), (τ ·ψ ′)),
from which the claim follows.
Next, we give expressions of δMα (f )[φ ] and δ2Mα (f )[φ , ψ ] in terms of N ,
δN , and δ2N .
Proposition 2.5. δMα (f )[φ ] and δ2Mα (f )[φ , ψ ] can be written as
δMα (f )[φ ] =
2∑
i=1
Pi(f )[φ ], δ 2Mα (f )[φ , ψ ] =
6∑
i=1
Qi(f )[φ , ψ ],
9
where
P1(f )[φ ] = ϕ ′
α (N (τ )) δN (τ )[φ ]
‖∆f ‖α
Rn
,
P2(f )[φ ] = − α
2 Mα (f ) δ‖∆f ‖2
Rn[φ ]
‖∆f ‖2
Rn
,
Q1(f )[φ , ψ ] = ϕ ′
α (N (τ )) δ2N (τ )[φ , ψ ]
‖∆f ‖α
Rn
,
Q2(f )[φ , ψ ] = − α
2 ϕ ′
α (N (τ )) δN (τ )[φ ]
‖∆f ‖α
Rn
δ‖∆f ‖2
Rn[ψ ]
‖∆f ‖2
Rn
,
Q3(f )[φ , ψ ] = ϕ ′′
α (N (τ )) δN (τ )[φ ]
‖∆f ‖
α
2
Rn
δN (τ )[ψ ]
‖∆f ‖
α
2
Rn
,
Q4(f )[φ , ψ ] = − α
2 δMα (f )[ψ ] δ‖∆f ‖2
Rn [φ ]
‖∆f ‖2
Rn
,
Q5(f )[φ , ψ ] = − α
2 Mα (f ) δ2‖∆f ‖2
Rn [φ , ψ ]
‖∆f ‖2
Rn
,
Q6(f )[φ , ψ ] = α
2 Mα (f ) δ‖∆f ‖2
Rn[φ ]
‖∆f ‖2
Rn
δ‖∆f ‖2
Rn[ψ ]
‖∆f ‖2
Rn
.
Proof. The assertion for δMα (f ) follows immediately from (2.1) and (2.2).
Regarding δ2Mα (f ), we have
δ2Mα (f )[φ , ψ ] = δ(δMα (f )[φ ])[ψ ] =
2∑
i=1
δ(Pi(f )[φ ])[ψ ],
and
δ(P1(f )[φ ])[ψ ] = ϕ ′′
α (N (τ ))δN (τ )[ψ ] δN (τ )[φ ]
‖∆f ‖α
Rn
+ ϕ ′
α (N (τ )) δ2N (τ )[φ , ψ ]
‖∆f ‖α
Rn
− α
2 ϕ ′
α (N (τ )) δN (τ )[φ ]δ‖∆f ‖2
Rn [ψ ]
‖∆f ‖α +2
Rn
= Q3(f )[φ , ψ ] + Q1(f )[φ , ψ ] + Q2(f )[φ , ψ ],
δ(P2(f )[φ ])[ψ ] = − α
2 δMα (f )[ψ ] δ‖∆f ‖2
Rn[φ ]
‖∆f ‖2
Rn
− α
2 Mα (f ) δ2‖∆f ‖2
Rn[φ , ψ ]
‖∆f ‖2
Rn
+ α
2 Mα (f ) δ‖∆f ‖2
Rn[φ ]δ‖∆f ‖2
Rn [ψ ]
‖∆f ‖4
Rn
= Q4(f )[φ , ψ ] + Q5(f )[φ , ψ ] + Q6(f )[φ , ψ ].
Plugging Lemma 2.4 and Proposition 2.5 into Theorem 2.1, we obtain the
ﬁrst and second variational formulae of the ( α, p )-O’Hara energies. Since the
expressions are rather lengthy, we omit their explicit formulae here .
10
3 Estimates of the ﬁrst and second variational
formulae
