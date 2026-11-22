---
doc_id: arxiv-math-0108046v3
doc_title: "arXiv:math/0108046v3 [math.RT] 3 May 2002"
section_id: page-015
section_title: "Page 15"
section_number: null
pages: 15-15
source_pdf: 0108046v3.pdf
source_sha256: f47c1bd39c671cf3
toc_source: undetermined
doc_brief: "Presenting Schur algebras — Motivated by work of R.M. Green, we obtain a pre- sentation of Schur algebras (both the classical and quantized ver- sions) in terms of generators and relations."
---
PRESENTING SCHUR ALGEBRAS
15
Proof. By iterating the result of the preceding proposition we see that
xd+1
α
1λ = 0 for any α ∈Φ and any λ ∈Λ(n, d), since it is clear that
λ + (d + 1)α does not belong to Λ(n, d). Thus we have equalities
xd+1
α
= xd+1
α
· 1 = xd+1
α
X
λ∈Λ(n,d)
1λ =
X
λ∈Λ(n,d)
xd+1
α
1λ = 0
and this proves the claim.
4. Straightening
We need the following variants of the notion of content. We deﬁne
functions χL and χR (left and right content) on Kostant monomials by
setting
χR(x(m)
α ) = m εj,
χL(x(m)
α ) = m εi,
χR(
Hi
m

) = χL(
Hi
m

) = 0
(4.1)
where α = εi −εj, and again using the rule χL(XY ) = χL(X) + χL(Y )
(similarly for χR) whenever X and Y are Kostant monomials. Note
that for A, C ∈NΦ+ we have
χ(eA) = χR(eA),
χ(fC) = χL(fC).
(4.2)
From this it follows immediately that
χ(eAfC) = χR(eA) + χL(fC).
(4.3)
From Proposition 3.8 it follows that for any A, C ∈NΦ+, λ ∈Λ(n, d)
we have equalities
eA1λfC = 1λ′eAfC = eAfC1λ′′
(4.4)
where λ′ = λ + P
α A(α) α, λ′′ = λ + P
α C(α) α (both sums over Φ+).
Moreover, we have equalities
X
α∈Φ+
A(α) α =
X
α=εi−εj; i<j
A(α)(εi −εj)
= χL(eA) −χR(eA)
= −χL(fA) + χR(fA)
from which it follows that
λ′ = λ −χR(eA) + χL(eA),
λ′′ = λ + χR(fC) −χL(fC).
(4.5)
Lemma 4.6. χ(eA1λfC) ⪯λ ⇔χL(1λ′eAfC) ⪯λ′ ⇔χR(eAfC1λ′′) ⪯
λ′′.
