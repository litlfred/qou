---
doc_id: gambaudo-ghys-braids-signatures-2005
doc_title: "Braids and signatures"
section_id: sec-059-51-the-ω--signatures-of-torus-knots-we-choose-a
section_title: "The ω -signatures of torus knots. — We choose a primitive k-"
section_number: 5.1
pages: 34-36
source_pdf: gambaudo-ghys-braids-signatures-2005.pdf
source_sha256: 647f4c28cab7428d
doc_brief: "Braids and signatures — 62 sections: Introduction; (v1) −v1 =v2 −γ 2(v2) and deﬁne; (α,β ) which is a 2-fold branched"
---
th root of unity ω and an integer p ≥ 1 and we would like to compute
signω (σ 1 · · ·σ n− 1)p. When p is a multiple of n, this reduces to the computation
of the ω -signatures in the center of Bn.
Proposition 5.1 . — Let ω = exp(2iπθ ) be a root of unity with 0 < θ <1.
The ω -signature of (σ 1 · · ·σ n− 1)p is equal to the Dedekind sum
signω (σ 1 · · ·σ n− 1)p =
∑
1≤ 𝓁 1≤ n− 1
1≤ 𝓁 2≤ p− 1
ϵ θ [𝓁 1,𝓁 2]
where
ϵ θ [𝓁 1,𝓁 2] =





+1 if 0<θ +𝓁 1/n +𝓁 2/p< 1, (mod 2),
−1 if 1<θ +𝓁 1/n +𝓁 2/p< 2, (mod 2),
0 if θ +𝓁 1/n +𝓁 2/p ∈ Z.
Proof. — This is a simple adaptation of a proof from [7, p. 296], wher e Kauﬀ-
man computes the usual signature ( ω = −1) for torus knots. For a suitable
Seifert surface for the braid ( σ 1 · · ·σ n− 1)p, the Seifert matrix B is shown to
be −Λ n− 1 ⊗ Λ p− 1 where Λ a denotes the (a − 1) × (a − 1) matrix









1 −1 0 ... 0
0 1 −1 . . . .
.
.
.
.
. . . . . . . . . . .
.
.
.
.
. . . . 1 −1
0 ... ...0 1









.
Over the complex numbers, Λ a can be written as PaΩ aP ⋆
a where Pa is some
invertible matrix and
Ω a =





1 − e2iπ/a 0 ... 0
0 1 − e2·2iπ/a 0
.
.
. .
.
. . . . .
.
.
0 0 ... 1 − e(a− 1)·2iπ/a




 .
Therefore, in order to compute the ω -signature of ( σ 1 · · ·σ n− 1)p, one has to
compute the signature of the hermitian matrix
−
[
(1 −ω )Ω n ⊗ Ω p + (1 −
ω )(Ω n ⊗ Ω p)⋆ ]
which is diagonal. One ﬁnds
signω (σ 1 · · ·σ n− 1)p =
∑
1≤ 𝓁 1≤ n− 1
1≤ 𝓁 2≤ p− 1
σ ign
{
Re(1 −ω )
(
1 − e
2iπ𝓁 1
n
)(
1 − e
2iπ𝓁 2
p
)}
tome 133 – 2005 – n o 4
BRAIDS AND SIGNATURES 575
where σ ign denotes the sign of a real number (we are out of symbols for signs
and signatures!) and Re the real part of a complex number. Not e that
(1 −ω )
(
1 − e
2iπ𝓁 1
n
)(
1 − e
2iπ𝓁 2
p
)
= 8i sin(πθ ) sin
( π𝓁 1
n
)
sin
( π𝓁 2
p
)
e
iπ (θ + 𝓁 1
n + 𝓁 2
p )
so that the above formula for the ω -signature reduces to the formula in the
proposition. A challenging exercise for the reader would be to give another
proof of this proposition using Theorem A.
When ω = −1 and p = 2n, one gets the value 1 −n2 that we used earlier.
For every root of unity ω , deﬁne the map
Signω :α ∈ Bn ↦− →lim
p→∞
1
p signω (α p) ∈ R.
The existence of the limit follows from the quasi-additivit y of the sequence
signω (α p). Note that Sign ω is a quasimorphism Bn → R and that the absolute
value of the diﬀerence between Sign ω and sign ω is bounded by 2n. The interest
of this slight modiﬁcation from sign ω to Sign ω is that Sign ω is homogeneous,
i.e. Signω (α p) = p Signω (α ) for all p and α .
As a simple corollary of Proposition 5.1, we give the homogen eous signatures
of torus knots. Indeed, ﬁxing θ and𝓁 1, the sum (1/p ) ∑
1≤ 𝓁 2≤ p− 1ϵ θ [𝓁 1,𝓁 2] diﬀers
by at most by 1 /p from the integral
∫ 1
0
ϵ θ [𝓁 1,x ] dx
where
ϵ θ [𝓁 1,x ] =
{ +1 if 0 <θ +𝓁 1/n +x< 1, (mod 2),
−1 if 1 <θ +𝓁 1/n +x< 2, (mod 2).
It follows that
Signexp(2iπθ )(σ 1· · ·σ n− 1) =
∑
1≤ 𝓁 1≤ n− 1
∫ 1
0
ϵ θ [𝓁 1,x ] dx.
The latter integral is of course easy to determine and we leav e the computation
to the reader. Here is the result:
Proposition 5.2 . — The value of Signexp(2iπθ )(σ 1· · ·σ n− 1) is a piecewise
aﬃne function of θ ∈ [0, 1] ∩ Q. More precisely:
Signexp(2iπθ )(σ 1· · ·σ n− 1) = −2
(
n − (2𝓁 − 1)
)
θ − 2𝓁(𝓁 − 1)
n
for (𝓁 − 1)/n<θ<𝓁/n and 𝓁 = 1,...,n .
BULLETIN DE LA SOCI ´ET´E MATH ´EMATIQUE DE FRANCE
576 GAMBAUDO (J.-M.) & GHYS (E.)
Signexp(2iπ
 θ
)(∆
 2
5) θ
1
5
2
5
3
5
4
5
−
 8
5
−
 12
5
1
Figure 23. Homogeneous signature
Note in particular that for 0 <θ < 1/n , one has
Signexp(2iπθ )(σ 1· · ·σ n− 1) = −2(n − 1)θ
and that when n is odd and ( n − 1)/ 2n<θ < (n + 1)/ 2n
Signexp(2iπθ )(σ 1· · ·σ n− 1) = 1 −n2
2n ·
Note also that when n = 3 and 0 < θ < 1
3 , we have Sign ω (σ 1 ·σ 2) = −4θ
so that sign ω (∆ 2k
3 ) = sign ω ((σ 1 ·σ 2)3k) = −4θ ·3k if ω is a k-th root of unity.
We used this value in the proof of Theorem 4.3.
