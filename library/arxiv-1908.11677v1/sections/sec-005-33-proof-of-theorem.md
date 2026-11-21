---
doc_id: arxiv-1908.11677v1
doc_title: "Variational formulae and estimates of O’Hara’s knot energies"
section_id: sec-005-33-proof-of-theorem
section_title: "Proof of Theorem ??"
section_number: 3.3
pages: 15-19
source_pdf: 1908.11677v1.pdf
source_sha256: c53663eeb457daf9
toc_source: outline
doc_brief: "Variational formulae and estimates of O’Hara’s knot energies — O’Hara’s energies, introduced by Jun O’Hara, were proposed to answer the question of what is the canonical shape in a given knot type"
---
In this subsection we complete the proof of Theorem 1.1 combining the facts
in previous subsection. First, we show the L1-estimates of the ﬁrst and second
variational formulae for M(α,p)(f). Using the expression of the ﬁrst and second
15
variational formulae for N (τ) in Lemma 2.4, it follows that

R1(f)[φ]
∥∆f∥α
Rn

Lp
≤C∥φ′∥L∞,

R2(f)[φ]
∥∆f∥α
Rn

Lp
≤C[φ′]W σ,2p,

S1(f)[φ, ψ]
∥∆f∥α
Rn

Lp
≤C∥φ′∥L∞∥ψ′∥L∞,

S2(f)[φ, ψ]
∥∆f∥α
Rn

Lp
≤C{∥φ′∥L∞(∥ψ′∥L∞+ [ψ′]W σ,2p) + ∥ψ′∥L∞(∥φ′∥L∞+ [φ′]W σ,2p)},

S3(f)[φ, ψ]
∥∆f∥α
Rn

Lp
≤C(∥ψ′∥L∞[φ′]W σ,2p + ∥φ′∥L∞[ψ′]W σ,2p),

S4(f)[φ, ψ]
∥∆f∥α
Rn

Lp
≤C[φ′]W σ,2p[ψ′]W σ,2p,

S5(f)[φ, ψ]
∥∆f∥α
Rn

Lp
≤C([φ′]W σ,2p + ∥φ′∥L∞)([ψ′]W σ,2p + ∥ψ′∥L∞)
by Lemmas 3.1 and 3.3. Hence, from these estimates and Lemma 3.2, we obtain

δN (τ)[φ]
∥∆f∥α
Rn

Lp
≤C∥φ′∥W σ,2p∩L∞

δN (τ)[φ, ψ]
∥∆f∥α
Rn

Lp
≤C∥φ′∥W σ,2p∩L∞∥ψ′∥W σ,2p∩L∞,
and L1-estimates for G(α,p)(f) and H(α,p)(f).
Next, we consider L∞-estimates of M(α,p)(f), G(α,p)(f), and H(α,p)(f) with
the weight |∆s|α−2β. We assume that f, φ, ψ ∈C1,β and s1, s2 ∈R/LZ satisfy
0 < |∆s| < L/2. Because we have
1 −xα ≤
α
2 + 1

(1 −x2)
for all x ∈[0, 1], it follows that
|∆s|α−2βMα(f) ≤C
1
|∆s|2β

1 −∥∆f∥α
Rn
|∆s|α

≤C
1
|∆s|2β

1 −∥∆f∥2
Rn
|∆s|2

≤C
1
|∆s|2β+2
Z s1
s2
Z s1
s2
∥∆3
4τ∥2
Rnds3ds4
≤C.
(3.5)
16
Moreover, by Lemmas 3.1–3.3, we have

|∆s|α−2β R1(f)[φ]
∥∆f∥α
Rn

L∞
≤C∥φ′∥L∞,

|∆s|α−2β R2(f)[φ]
∥∆f∥α
Rn

L∞
≤C[φ′]C0,β,

|∆s|α−2β S1(f)[φ, ψ]
∥∆f∥α
Rn

L∞
≤C∥φ′∥L∞∥ψ′∥L∞,

|∆s|α−2β S2(f)[φ, ψ]
∥∆f∥α
Rn

L∞
≤C{∥φ′∥L∞(∥ψ′∥L∞+ [ψ′]C0,β) + ∥ψ′∥L∞(∥φ′∥L∞+ [φ′]C0,β)},

|∆s|α−2β S3(f)[φ, ψ]
∥∆f∥α
Rn

L∞
≤C(∥ψ′∥L∞[φ′]C0,β + ∥φ′∥L∞[ψ′]C0,β),

|∆s|α−2β S4(f)[φ, ψ]
∥∆f∥α
Rn

L∞
≤C[φ′]C0,β[ψ′]C0,β,

|∆s|α−2β S5(f)[φ, ψ]
∥∆f∥α
Rn

L∞
≤C([φ′]C0,β + ∥φ′∥L∞)([ψ′]C0,β + ∥ψ′∥L∞).
Therefore, we obtain

|∆s|α−2β δN (τ)[φ]
∥∆f∥α
Rn

L∞
≤C∥φ′∥C0,β

|∆s|α−2β δ2N (τ)[φ, ψ]
∥∆f∥α
Rn

L∞
≤C∥φ′∥C0,β∥ψ′∥C0,β,
and the L∞-estimates for M(α,p)(f), G(α,p)(f), and H(α,p)(f) with the weight
|∆s|α−2β.
Lastly, we consider the continuity. Because continuity on the outside of the
diagonal set is clear, we consider the property on the diagonal set. First, we
assume f, φ, ψ ∈h1,β with 0 < β < 1, and f is bi-Lipschitz. Let R > 0 be
suﬃciently small. In a similar manner to the proof of (3.5), it holds that
|∆s|α−2βMα(f) ≤˜C[τ]C0,β,R
for 0 < |∆s| < R, and therefore
lim
(s1,s2)→(s,s) |∆s|α−2βMα(f) = 0,
where ˜C is a positive constant depending only on α, p, and Cb. Moreover, by
Lemma 3.1, we have
lim
(s1,s2)→(s,s)

|∆s|α−2β Ri(f)[φ]
∥∆f∥α
Rn

 = 0,
(i = 1, 2),
lim
(s1,s2)→(s,s)

|∆s|α−2β Si(f)[φ, ψ]
∥∆f∥α
Rn

 = 0,
(i = 1, . . . , 5).
Considering Lemma 3.2, we obtain the desired continuity when f, φ, ψ ∈h1,β
with 0 < β < 1.
17
Next, we consider the case where β = 1. We denote the curvature vector of
f by κ, i.e. κ = f ′′. Using Lemma 3.1 and L’Hospital’s theorem, we have
|∆s|α−2Mα(f) = |∆s|α−2 ϕα(N (τ))
∥∆f∥α
Rn
= |∆s|α−2 ϕ2(N (τ))
∥∆f∥α
Rn
ϕα(N (τ))
ϕ2(N (τ))
= |∆s|α−2 N (τ)
∥∆f∥α
Rn
1
1 + N (τ)
ϕα(N (τ))
ϕ2(N (τ))
→α
24∥κ(s)∥2
Rn
as (s1, s2) →(s, s).
Similarly, it follows that
|∆s|α−2 R1(f)[φ]
∥∆f∥α
Rn →−1
6τ(s) · φ′(s)∥κ(s)∥2
Rn,
|∆s|α−2 R2(f)[φ]
∥∆f∥α
Rn →1
6κ(s) · φ′′(s),
|∆s|α−2 S1(f)[φ, ψ]
∥∆f∥α
Rn
→−1
6{φ′(s) · ψ′(s) −(τ(s) · φ′(s))(τ (s) · ψ′(s))}∥κ(s)∥2
Rn,
|∆s|α−2 S2(f)[φ, ψ]
∥∆f∥α
Rn
→1
6(τ(s) · φ′(s))(κ(s) · ψ′′(s) −τ(s) · ψ′(s)∥κ(s)∥2
Rn)
+ 1
6(τ(s) · ψ′(s))(κ(s) · φ′′(s) −τ(s) · φ′(s)∥κ(s)∥2
Rn),
|∆s|α−2 S3(f)[φ, ψ]
∥∆f∥α
Rn
→−1
6(τ(s) · ψ′(s))(κ(s) · φ′′(s)) −1
6(τ(s) · φ′(s))(κ(s) · ψ′′(s)),
|∆s|α−2 S4(f)[φ, ψ]
∥∆f∥α
Rn
→1
6φ′′(s) · ψ′′(s),
|∆s|α−2 S5(f)[φ, ψ]
∥∆f∥α
Rn
→−1
6{(τ(s) · φ′′(s)) + (φ′(s) · κ(s))}{(τ(s) · ψ′′(s)) + (ψ′(s) · κ(s))}
as (s1, s2) →(s, s). Hence, the desired continuity holds when f, φ, ψ ∈C2.
This completes the proof of Theorem 1.1.
□
References
[1] A. Abrams, J. Cantarella, J. H. G. Fu, M. Ghomi, and R. Howard, Circles
minimize most knot energies, Topology, 42 (2) (2003), 381–394.
[2] S. Blatt, The gradient ﬂow of the M¨obius energy near local minimizers,
Calc. Var. Partial Diﬀerential Equations, 43 (1) (2012), 1250010, 9 pp.
[3] S. Blatt, Boundedness and regularizing eﬀects of O’Hara’s knot energies,
J. Knot Theory Ramiﬁcations, 21 (2012), 1250010, 9pp.
[4] S. Blatt, The gradient ﬂow of O’Hara’s knot energies, Math. Ann., 370
(3–4) (2018), 993–1061.
18
[5] S. Blatt, P. Reiter, and A. Schikorra, Harmonic analysis meets critical
knots. Critical points of the M¨obius energy are smooth, Trans. Amer. Math.
Soc. 368 (9) (2016), 6391–6438.
[6] S. Blatt and P. Reiter, Stationary points of O’Hara’s knot energies,
Manuscripta Math., 140 (1–2) (2013), 29–50.
[7] S. Blatt and N. Vorderobermeier, On the analyticity of critical points of the
M¨obius energy, Calc. Var. Partial Diﬀerential Equations, 58 (1) (2019), 28
pp.
[8] M. H. Freedman, Z.-X. He, and Z. Wang, M¨obius energy of knots and
unknots, Ann. of Math., 139 (1994), 1–50.
[9] Z.-X. He, The Euler-Lagrange equation and heat ﬂow for the M¨obius energy,
Comm. Pure Appl. Math., 53 (4) (2000), 399–431.
[10] A. Ishizeki and T. Nagasawa, A decomposition theorem of the M¨obius energy
I: Decomposition and M¨obius invariance, Kodai. Math. J., 37 (3) (2014),
737–754.
[11] A. Ishizeki and T. Nagasawa, A decomposition theorem of the M¨obius energy
II: Variational formulae and estimates, Math. Ann., 363 (1–2) (2015), 617–
635.
[12] A. Ishizeki and T. Nagasawa, Decomposition of generalized O’Hara’s ener-
gies, preprint, arXiv:1904.06812 (2019).
[13] J. O’Hara, Energy of a knot, Topology, 30 (2) (1991), 241–247.
[14] J. O’Hara, Family of energy functionals of knots, Topology Appl., 48 (2)
(1992), 147–161.
[15] J. O’Hara, Energy functionals of knots II, Topology Appl., 56 (1) (1994),
45–61.
[16] P. Reiter, Repulsive knot energies and pseudodiﬀerential calculus for
O’Hara’s knot energy family E(α), α ∈[2, 3), Math. Nachr., 285 (7) (2012),
889–913.
19
