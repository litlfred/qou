---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-023-74-rises-in-random-permutations
section_title: "Rises in random permutations"
section_number: 7.4
pages: 58-61
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
ods of singularity analysis and the transfer theorems between the singularities of a gen-
erating series and the asymptotic behavior of its coefﬁcients (see e.g. [FS09, Chapter
VI]) can be use to prove mod-φ convergence (this is not surprising as they can be used
to establish the related concept of quasi-powers, see Section 4.5.3). We examine here an-
other example where we do not have strictly speaking mod- φ convergence since the
reference law is not inﬁnitely divisible, but where our methods can nevertheless be
used.
If σ∈ S(n) is a permutation, a rise of σ is an integer i∈ [ [1, n− 1] ]such that σ(i) <
σ(i + 1). The number of rises R(σ) is thus a quantity between 0 and n− 1, the two ex-
tremal values corresponding to the permutationsn(n− 1) . . . 21 and 12 . . .(n− 1)n. We
denote Rn = R(σn) the random variable which counts the number of rises of a random
MOD-φ CONVERGENCE, I 59
permutation σn∈ S(n) chosen under the uniform measure. The double generating
series
R(z, t) =
∞
∑
n=0
E[ezRn] tn
is computed in [FS09, III.7, p. 209]:
R(z, t) = ez− 1
ez− et(ez−1) .
If Re(z)≤ log 2, then|ez|≤ 2 and the smallest (in modulus) root of the denominator is
t = ρ(z) = z
ez− 1.
We then have R(z, t) = 1
ρ(z)−t + (ez− 1) S(z, t) with S(z, t) = 1
ez−et(ez−1)− 1
z−t(ez−1)
analytic in t and on the band z∈S (−∞,log 2). This implies:
Theorem 7.23 ([FS09], p. 658). For z∈S (−∞,log 2), one has locally uniformly
E[ezRn] = τ(z)n+1 + O(|z| 2−n),
where τ(z) = ez−1
z .
Notice that τ(z) = ez−1
z = ∫ 1
0 ezu du is the Laplace transform of a uniform random
variable U in the interval [0, 1]. Informally, the previous should be thought as follows:
(Rn)n∈N converges mod-U onS(−∞,log 2) with parameters tn = n + 1 and limit ψ(z) =
1. However, the uniform law U is not inﬁnitely divisible, and τ(z) vanishes on any
z∈ 2iπZ, therefore the error term O(|z| 2−n) cannot be rewritten as a multiplicative
error term, as we did before. Still, every computation of Section 4 can be performed in
this case. Let us stress out the necessary adjustments:
• Berry-Esseen estimates. Set Fn(x) = P[Rn− n+1
2 ≥
√
n+1
12 x] and Gn(x) =∫ x
−∞ g(y) dy. We have by Feller’s lemma
|Fn(x)− Gn(x)|≤ 24m
∆π√tn
+ 1
π√tn
∫
[±δ√tn]
⏐⏐⏐⏐⏐⏐
f∗
n (ξ)− e− ξ2
2
ξ
⏐⏐⏐⏐⏐⏐
dξ
+ 1
πδ√tn
∫
[±∆√tn]\[±δ√tn]
⏐⏐⏐⏐ f∗
n (ξ)− e− ξ2
2
⏐⏐⏐⏐ dξ,
where as in the proof of Proposition 4.1, f∗
n (ξ) is the Fourier transform of Rn− tn
2√ tn
12
.
From Theorem 7.23 and a Taylor expansion of τ(iξ), one has
f∗
n (ξ) = e
− ξ2
2
(
1+O
(
ξ2
tn
))
+ O(|ξ| 2−tn).
In the ﬁrst integral of Feller’s bound, we are integrating
⏐⏐⏐⏐
f∗
n (ξ)− g∗(ξ)
ξ
⏐⏐⏐⏐ = O
(
δ2 e− ξ2
2
)
+ O(2−tn),
so we get a o( 1√tn
) as δ goes to zero. Then, regarding the second integral, we
are integrating a O((qδ)tn) for some qδ∈ [ 1
2, 1), so it does not contribute to the
60 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
asymptotics. Thus, we get the uniform estimate|Fn(x)− Gn(x)| = o( 1√tn
) as in
Proposition 4.1.
• Tilting method and large deviation estimates. When tilting by h > 0, the new
random variable Rh
n with law P[Rh
n∈ dy] = ehy
E[ehRn ] P[Rn∈ dy] has its Fourier
transform that has asymptotics
τ(h + iξ)n+1 + O(2−n)
τ(h)n+1 + O(2−n) =
( τ(h + iξ)
τ(h)
)n+1
(1 + o(1))
the second formula holding if h and ξ are small enough (more precisely, we
want 0 < h < log 2 and then ξ small enough with bounds depending on h).
Notice that the new exponent τ(h+iξ)
τ(h) does not vanish anymore, so we can now
use the same argument as in Theorem 4.3. Thus, if F is the Legendre-Fenchel
transform of the uniform law on[0, 1] (not really explicit), and ifh is the solution
of 1+ε
2 = η′(h) with η(h) = log
(
eh−1
h
)
, then for
ε∈ (2η′(0)− 1, 2η′(log 2)− 1) =
(
0, 3− 2
log 2
)
⊇ (0, 0.114),
we obtain the large deviation estimate:
P
[
Rn≥ (1 + ε)(n + 1)
2
]
= e−tn F( 1+ε
2 )
h
√
2πtn η′′(h) (1 + o(1))
since we have mod- U convergence of (Rn)n∈N with parameters tn = n+1
2 and
residue ψ(x) = 1. Similarly, for the negative deviations, the estimate of the
Fourier transform of the tilted random variable Rh
n can be used if h > h0, where
h0≈− 1.594 is the solution of the equation τ(h) = 1
2. Therefore, for
ε∈
(
0, 2
h0
− 1
)
⊇ (0, 0.254),
we have
P
[
Rn≤ (1− ε)(n + 1)
2
]
= e−tn F( 1−ε
2 )
|h|
√
2πtn η′′(h) (1 + o(1)),
where h is the solution of 1−ε
2 = η′(h).
• Extended central limit theorem. The result of Lemma 4.9 holds, because
⏐⏐⏐⏐
τ(h + iu)
τ(h)
⏐⏐⏐⏐
2
=
⏐⏐⏐⏐⏐
eh+iu− 1
eh− 1
h
h + iu
⏐⏐⏐⏐⏐
2
=
(
1 + 2eh (1− cos u)
(eh− 1)2
)
h2
h2 + u2 = h2 + 2t(h) (1− cos(u))
h2 + u2 ,
where t(h) = h2eh
(eh−1)2≤ 1 for any h. From this inequality, one deduces that
qδ = max
u∈R\[−δ,δ]
⏐⏐⏐⏐
τ(h + iu)
τ(h)
⏐⏐⏐⏐≤ 1− Dδ2
for some constant D > 0 and any h∈ (−ε, ε), with ε small enough.
MOD-φ CONVERGENCE, I 61
Since η(x) = log(τ(x)) has Taylor expansion x
2 + x2
24− x4
2880 + o(x5), we thus
get from Equation (19):
P
[
Rn≥ n + 1
2 +
√
n + 1
12 y
]
= (1 + o(1))
y
√
2π
exp
(
− y2
2 + y4
240tn
)
for any positive y with y = o((tn)
1
2− 1
6 ) = o((tn)
5
12 ).
