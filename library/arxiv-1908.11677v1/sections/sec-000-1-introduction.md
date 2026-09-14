---
doc_id: arxiv-1908.11677v1
doc_title: "Variational formulae and estimates of O’Hara’s knot energies"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1908.11677v1.pdf
source_sha256: c53663eeb457daf9
doc_brief: "Variational formulae and estimates of O’Hara’s knot energies — O’Hara’s energies, introduced by Jun O’Hara, were proposedto answer the question of what is the canonical shape in a given knot typ e"
---
In his papers [13, 14], O’Hara proposed several energies for knots to determine
the canonical shape of a knot in a given knot class. In order to describe these
energies, let f : R/ LZ ∋ s ↦→f (s) be an arclength parametrization of a knot, or
more generally, of a closed curve in Rn without self-intersections. For positive
constants α and p, the O’Hara ( α, p )-energy is deﬁned as
E(α,p )(f ) =
∫∫
(R/ LZ)2
M(α,p )(f )(s1, s 2)ds1ds2,
where
M(α,p )(f )(s1, s 2) =
( 1
‖f (s1) −f (s2)‖α
Rn
− 1
D(f (s1), f (s2))α
) p
.
Here, ‖f (s1) −f (s2)‖Rn and D(f (s1), f (s2)) are the extrinsic and the intrinsic
distances between two points f (s1) and f (s2) on the curve, respectively.
Amongst these energies, the case p = 1 has been well-studied by many
authors and here we describe several important contributions in t his direction.
For example, the ﬁrst variational formula was derived in [8, 16], and t he existence
of a minimizer in a given knot class was studied in [8, 15]. In [1], it was shown
1
that the right circle is the only global minimizer of the energy under len gth-
constraint for appropriate α . We also mention that there are several recent
works concerning the gradient ﬂow [2, 4] and the regularity of critic al points [5,
6, 7, 8, 9, 16] of the ( α, 1)-energies. The obvious diﬃculty in the analysis is that
the energy density has a singularity on the diagonal set {(s, s ) | s ∈ R/ LZ}. To
avoid this, the variational formulae were ﬁrst derived using Cauchy ’s principal
value [8, 16]. The absolute integrability of the ﬁrst and second variat ional
formulae was shown by Ishizeki-Nagasawa [11] in the energy class. T hey used
the decomposition of the (2 , 1)-energy shown in [10], which gives an expression
of the energy density without using the intrinsic distance. Further more, in [11],
they derived other estimates of variational formulae in several fu nction spaces
and a similar technique is applicable to other ( α, 1)-energies; see [12].
By comparison, the case p > 1 is rather less well studied. Even the explicit
expression of the ﬁrst variational formula in the sense of Cauchy’s principle value
seems not to have been given. In this paper, the ﬁrst and second v ariational
formulae of ( α, p )-energies will be given, and several estimates will be shown:
absolute integrability, uniform boundedness, and continuity. We, h owever, do
not have a decomposition like the ( α, 1) case, and therefore the technique in
[11, 12] cannot be used. Instead, we pay attention to the functio n
N (u, v) = 1
2‖f(s1) −f (s2)‖2
Rn
∫ s2
s1
∫ s2
s1
(u(s3) −u(s4)) · (v(s3) −v(s4))ds3ds4.
By use of N , the ( α, p )-energy may be written as
E(α,p )(f ) =
∫∫
(R/ LZ)2
(
ϕ α
(
N (f ′, f ′)
)
‖f (s1) −f (s2)‖α
Rn
) p
ds1ds2,
where
ϕ α (t) = 1 − 1
(1 + t)
α
2
.
Here, we note that if E(α,p )(f ) < ∞, then f ′ exists almost everywhere; we refer
the reader to [3] for this fact. Since N (f ′, f ′) is non-negative, and since ϕ α is
smooth for t ≥ 0, the derivation and estimation of variational formulae mainly
reduce to the study of N .
We are now in a position to describe our main result of this article. For t he
simplicity of notation, we will use ∆ i
ju to mean u(si) −u(sj) for a function
u : R/ LZ → Rd, where d = 1 or n, and ∆ i
js to mean si − sj for si, sj ∈
R/ LZ. Furthermore, we rewrite ∆ 1
2u and D(f (s1), f (s2)) as ∆ u and D(f ),
respectively. Also, we let τ =f ′ be the unit tangent vector.
For a geometric quantity F (f ) of the closed curve f , and for functions φ ,
ψ , from R/ LZ to Rn, let δ and δ2 be given by
δF (f )[φ ] = d
dεF (f + εφ )
⏐⏐⏐⏐
ε=0
,
δ2F (f )[φ , ψ ] = ∂ 2
∂ε1∂ε2
F (f + ε1φ + ε2ψ )
⏐⏐⏐⏐
ε1=ε2=0
.
2
The ﬁrst and second variational formulae, G(α,p )(f )[φ ] and H(α,p )(f )[φ , ψ ], are
given by
G(α,p )(f )[φ ] ds1ds2 = δ(M(α,p )(f ) ds1ds2)[φ ],
H(α,p )(f )[φ , ψ ]ds1ds2 = δ2(M(α,p )(f ) ds1ds2)[φ , ψ ].
The purpose of this article is to give certain new expressions and est imates for
these variational formulae. The expression will be given in § 2. In § 3, we prove
the L1, L∞ and C0-estimates for them on the appropriate function spaces. The
ﬁrst space is the Sobolev-Slobodeckij space W k+σ,q (R/ LZ, Rn) given by
W k+σ,q (R/ LZ, Rn) = {f ∈ W k,q (R/ LZ, Rn) | [f (k)]W σ,q < ∞}
for k ∈ { 0} ∪ N, 0 < σ < 1, and q ≥ 1. We equip W k+σ,q (R/ LZ, Rn) with the
norm
‖f ‖W k+σ,q =
(
‖f ‖q
W k,q + [f (k)]q
W σ,q
) 1
q
,
where
[f (k)]W σ,q =
(∫∫
(R/ LZ)2
‖∆f (k)‖q
Rn
|∆ s|1+σq ds1ds2
) 1
q
.
For α ∈ (0, ∞), p ∈ [1, ∞) such that 2 ≤ αp < 2p + 1, and σ = ( αp −
1)/ (2p), it was shown in [3] that E(α,p )(f ) < ∞ if and only if f belongs to
W 1+σ, 2p(R/ LZ, Rn) ∩ W 1, ∞(R/ LZ, Rn) and is bi-Lipschitz. We will show the
L1-estimate for the variational formulae on the same space.
By use of an appropriate weight, the L∞-estimate holds on some H¨ older or
Lipschitz space Ck,β (R/ LZ, Rn) with k ∈ N ∪ {0} and β ∈ (0, 1]. Here,
Ck,β (R/ LZ, Rn) = {f ∈ Ck(R/ LZ, Rn) | [f (k)]C 0,β < ∞}
and this space is equipped with the norm
‖f ‖C k,β = ‖f‖C k + [f (k)]C 0,β ,
where
[f (k)]C 0,β = sup
s1,s 2∈R/ LZ
‖∆f (k)‖Rn
|∆ s|β .
Note that we will see later that the weight is necessary.
The completion of C∞(R/ LZ, Rn) in the H¨ older space is known as the little
H¨ older spacehk,β (R/ LZ, Rn) when β < 1. The completion of C∞(R/ LZ, Rn)
in Ck, 1(R/ LZ, Rn) is Ck+1(R/ LZ, Rn). We have the continuity of the energy
density, and the ﬁrst and second variational formulae in the comple tion space.
The precise statement is as follows.
Theorem 1.1. Let α ∈ (0, ∞), p ∈ [1, ∞) satisfy 2 ≤ αp < 2p + 1, and set
σ = ( αp − 1)/ (2p). Assume that f is bi-Lipschitz, i.e., there exists a positive
constant Cb > 0 such that D(f ) ≤ Cb‖∆f ‖Rn .
1. If f , φ , ψ ∈ W 1+σ, 2p(R/ LZ, Rn) ∩ W 1, ∞(R/ LZ, Rn), then M(α,p )(f ),
G(α,p )(f )[φ ], H(α,p )(f )[φ , ψ ] ∈ L1((R/ LZ)2). Moreover, there exists a
positive constant C depending on ‖τ ‖W σ, 2p∩L∞ , Cb, α , and p such that
‖M(α,p )(f )‖L1((R/ LZ)2) ≤ C,
‖G(α,p )(f )[φ ]‖L1((R/ LZ)2) ≤ C‖φ ′‖W σ, 2p∩L∞ ,
‖H(α,p )(f )[φ , ψ ]‖L1((R/ LZ)2) ≤ C‖φ ′‖W σ, 2p∩L∞ ‖ψ ′‖W σ, 2p∩L∞ .
3
2. Let β ∈ (0, 1]. If f ,φ ,ψ ∈ C1,β (R/ LZ, Rn), then D(f )(α −2β )pM(α,p )(f ),
D(f )(α −2β )pG(α,p )(f )[φ ], D(f )(α −2β )pH(α,p )(f )[φ , ψ ] ∈ L∞((R/ LZ)2).
Moreover, there exists a positive constant C depending on ‖τ ‖C 0,β , Cb,
α , and p such that
‖D(f )(α −2β )pM(α,p )(f )‖L∞ ((R/ LZ)2) ≤ C,
‖D(f )(α −2β )pG(α,p )(f )[φ ]‖L∞ ((R/ LZ)2) ≤ C‖φ ′‖C 0,β ,
‖D(f )(α −2β )pH(α,p )(f )[φ , ψ ]‖L∞ ((R/ LZ)2) ≤ C‖φ ′‖C 0,β ‖ψ ′‖C 0,β .
3. For β ∈ (0, 1], let
X β (R/ LZ, Rn) =
{
h0,β (R/ LZ, Rn) for 0 < β < 1,
C1(R/ LZ, Rn) for β = 1.
Ifτ ,φ ′,ψ ′ ∈ X β (R/ LZ, Rn), then D(f )(α −2β )pM(α,p )(f ), D(f )(α −2β )pG(α,p )(f )[φ ],
D(f )(α −2β )pH(α,p )(f )[φ , ψ ] can be extended to the diagonal set {(s, s ) | s ∈
R/ LZ} such that these functions are continuous everywhere on (R/ LZ)2,
and they satisfy the estimates
‖D(f )(α −2β )pM(α,p )(f )‖C 0((R/ LZ)2) ≤ C,
‖D(f )(α −2β )pG(α,p )(f )[φ ]‖C 0((R/ LZ)2) ≤ C‖φ ′‖X β ,
‖D(f )(α −2β )pH(α,p )(f )[φ , ψ ]‖C 0((R/ LZ)2) ≤ C‖φ ′‖X β ‖ψ ′‖X β
for some positive constant C depending on ‖τ ‖X β , Cb, α , and p. The
limit functions
lim
(s1,s 2)→(s,s )
D(f )(α −2β )pM(α,p )(f ),
lim
(s1,s 2)→(s,s )
D(f )(α −2β )pG(α,p )(f )[φ ],
lim
(s1,s 2)→(s,s )
D(f )(α −2β )pH(α,p )(f )[φ , ψ ]
exist and are ﬁnite. These vanish everywhere on R/ LZ when β ∈ (0, 1).
The second assertion gives us the L∞-estimates for M(α,p ), G(α,p ), and H(α,p )
without the weight, when α ≤ 2.
Corollary 1.2. Let α ∈ (0, ∞), p ∈ [1, ∞) satisfy 2/p ≤ α ≤ 2. If f , φ ,
ψ ∈ C1, α
2 (R/ LZ, Rn) and f is bi-Lipschitz, then M(α,p )(f ), G(α,p )(f )[φ ], and
H(α,p )(f )[φ , ψ ] belong to L∞((R/ LZ)2).
The corresponding estimates to our main result were shown for the spacial
case E(2, 1) in [11], and in this sense our result is an extension to a wider class of
O’Hara’s energies.
Remark 1.3. When α > 2, we need the weight D(f )(α −2β )p to obtain the
uniform boundedness even if f is analytic. For example, let us consider the
right circle with the total length 2 π , i.e.,
f (s) = (cos s, sin s, 0, . . . , 0) for s ∈ R/ 2π Z.
4
Since ‖∆f ‖2
Rn = 2(1 − cos ∆ s), it follows that
M(α,p )(f ) = 1
‖∆f ‖αp
Rn
[
1 −
{ 2(1 − cos ∆ s)
(∆ s)2
} α
2
] p
. (1.1)
Using Taylor’s theorem
2(1 − cos x) = x2 − 1
12 x4 + O(x6) as x → 0,
and thus we have
1 −
{ 2(1 − cos ∆ s)
(∆ s)2
} α
2
= α
24 (∆ s)2 + O((∆ s)4) as ∆ s → 0.
Hence, the right-hand side of (1.1) is equal to
( |∆ s|
‖∆f ‖Rn
) αp(α
24 |∆ s|2−α + O(|∆ s|4−α )
) p
as ∆ s → 0.
Therefore, when α > 2, D(f )γ M(α,p )(f ) is uniformly bounded if and only if
γ ≥ (α − 2)p.
Acknowledgments The authors would like to thank Professor Richard Neal
Bez for English language editing and mathematical comments.
The second author is supported by Grant-in-Aid for Scientiﬁc Rese arch (C)
(No.17K05310), Japan Society for the Promotion of Science.
