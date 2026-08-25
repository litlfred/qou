---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-015-41-convergence-of-power-sums
section_title: "Convergence of power sums"
section_number: 4.1
pages: 13-15
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
14 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
4.1. Convergence of power sums. The q-Plancherel measure is a measure on Young diagrams, so the
functions on Young diagrams and in particular the elements o f O are in this context random variables.
In particular we will denote by /BX their expectation. Thanks to the characterization of the q-Plancherel
measure with the normalized trace (paragraph 2.2), one has immediately:
/BX [Σρ,q] =
{
n↓k if ρ = 1 k;
0 else.
By using the triangular relation between the Σρ and the Σν,q, we obtain:
/BX [Σρ] = 1
qρ − 1
∑
ν∈Yk
(q − 1)ℓ(ν) ⟨mν | pρ⟩ /BX [Σν,q] = (q − 1)|ρ|
qρ − 1 n↓|ρ| ⟨m1|ν| | pρ⟩
= (1 − q)|ρ|
1 − qρ n↓|ρ|(8)
This gives in particular the asymptotic order of magnitude:
/BX [Σρ] = O
(
n|ρ|)
= O
(
ndeg(Σρ))
In fact, this is true for any measure on Young diagrams, but is not always precise enough (for example,
to study the usual Plancherel measure, one has to use the fact that it is O(n(|ρ|+ℓ(ρ))/2)). In this context,
the exact computation above shows that we could not ﬁnd a bett er bound. As (Σρ)ρ∈Y is a linear basis
of O, the previous estimate remains true for any element of O.
Lemma 11. For any x ∈ O, one has /BX [x] = O(ndeg(x)).
This lemma allows us to forget terms of lower degree when we wa nt to look at the asymptotic behavior
of the expectation of some observable. In particular, one ca n obtain the following result for the power
sums of the Frobenius coordinates:
Lemma 12 (Convergence of power sums) . Under the q-Plancherel measures, we have convergence in
probability of the renormalized power sums pk(λ):
∀k ≥ 1, pk(λ)
|λ|k − →Mn,q
(1 − q)k
1 − qk .
Proof. An immediate consequence of equation ( 8) is that /BX [Σρ]/n|ρ| → (1 − q)|ρ|/(1 − qρ) when n goes
to inﬁnity. But Σρ − pρ is an observable of degree less than |ρ| − 1, so the same holds for pρ:
(9) lim
n→∞
/BX [pρ]
n|ρ| = (1 − q)|ρ|
1 − qρ
Fix ε > 0 and k ≥ 1. The Bienaymé-Chebyshev inequality ensures that
Mn,q
[ ⏐
⏐
⏐
⏐
pk
nk − (1 − q)k
1 − qk
⏐
⏐
⏐
⏐ ≥ ε
]
≤ 1
ε2
/BX
[ (pk
nk − (1 − q)k
1 − qk
)2]
≤ 1
ε2
(
/BX [pk,k]
n2k − 2
/BX [pk]
nk
(1 − q)k
1 − qk + (1 − q)2k
1 − qk,k
)
.
But the right-hand side tends to 0 (which is easily seen using equation ( 9) for ρ = ( k) and ρ = ( k, k))
and the proof is over. □
ASYMPTOTICS OF q-PLANCHEREL MEASURES 15
Corollary 13 (Convergence of the characters and q-characters). Under the q-Plancherel measures, in
probability,o ne has:
∀ρ ∈ Y , Σρ
n|ρ| − →Mn,q
(1 − q)|ρ|
1 − qρ i.e. χλ(ρ) − →Mn,q
(1 − q)|ρ|
1 − qρ ;
∀ρ ∈ Y , Σρ,q
n|ρ| − →Mn,q δρ=1|ρ| i.e. χλ(ρ, q) − →Mn,q δρ=1|ρ| .
Proof. It is a direct consequence of Proposition 7 and Lemma 12. □
