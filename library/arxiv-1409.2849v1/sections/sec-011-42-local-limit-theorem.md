---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-011-42-local-limit-theorem
section_title: "Local limit theorem"
section_number: 4.2
pages: 30-32
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
local limit theorems for mod- φ convergence, we obtain the following local limit theo-
rem for the magnetization in the Curie-Weiss model:
Theorem 17. In the Curie-Weiss model, if we note M n for the total magnetization, then we
have:
lim
n→∞
n1/2 P[n−1/4Mn∈ B] = 2
121/4Γ( 1
4 )
m(B),
for relatively compact sets B with m(∂B) = 0, m denoting the Lebesgue measure.
Proof. With the notation of §4.1, Yn = n−1/4Mn and we need to check assumptions H1,
H2 and H3 of [DKN11] for (Yn)n∈N in order to apply Theorem 5 in loc. cit.
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS31
• H1. The Fourier transform of the limit law µ(dx) = ψ(x) dx
I∞ of Yn
n1/2 is in the Schwartz
space, hence is integrable.
• H2. The Fourier transforms
ˆψn(ξ)
In e
ξ2
2n1/2 of Yn
n1/2 converge locally uniformly in ξ to-
wards the Fourier transform
ˆψ(ξ)
I∞ . Indeed, by Theorem 8,
ψn(x)
In
→L1(R)
ψ(x)
I∞
,
so
ˆψn(ξ)
In →
ˆψ(ξ)
I∞ , and the term e
ξ2
2n1/2 converges locally uniformly to 1.
• H3. Finally, we have to prove that for all k≥ 0,
fn,k(ξ) = E
[
eiξ Yn
n1/2
]
1|ξ|≤kn1/2
is uniformly integrable. Following Remark 2 in [DKN11], it is enough to show
that ⏐⏐⏐⏐E
[
eiξ Yn
n1/2
]⏐⏐⏐⏐≤ h(ξ)
for ξ such that|ξ|≤ kn1/2 for some non-negative and integrable function h on
R. This is a consequence of Proposition 15: since |ˆψn(ξ)|≤ C(k) e−k|ξ| for any
k > 0, one can write
⏐⏐⏐⏐E
[
eiξ Yn
n1/2
]⏐⏐⏐⏐ =|ˆψn(ξ)|
In
e
ξ2
2n1/2
≤ C(k)
I∞
e−k|ξ|+ ξ2
2n1/2
≤ C(k)
I∞
e− k
2|ξ|
for any|ξ| < k n1/2. We can hence apply Theorem 5 of [DKN11] with dµ
dm (0) =
1/I∞,and the value of I∞ was computed in the proof of Lemma 13.
□
Remark. A similar result would more generally hold for Yn whenever one has some
estimates of exponential decay onˆψn(ξ) similar to the one given in Lemma 15:
lim
n→∞
tn P[Yn∈ B] = 1
I∞
m(B).
In particular, the result holds for the random walks changed in measure studied in
§3.6.
Remark. The idea behind the proof the local limit theorem above and which is found in
[DKN11] is the following: thanks to approximation arguments, one can show that it is
enough to prove the local limit theorem for functions whose Fourier transforms have
32 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
compact support (instead of indicator functions 1B). Then, one uses Parseval’s relation
for such functions f to write:
E[ f (Yn)] = 1
2π
∫
R
ˆψn(ξ)
In
e
ξ2
2tnˆf
(
− ξ
tn
)
dξ
and then use the assumptions to conclude.
5. M OD-GAUSSIAN CONVERGENCE FOR THE ISING MODEL : THE CUMULANT
METHOD
In this appendix, we give another combinatorial proof of the mod-Gaussian conver-
gence of the magnetization in the Ising model, without ever computing the Laplace
transform of Mn. This serves as an illustration of the cumulant method developed in
[FMN13].
