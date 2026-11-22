---
doc_id: arxiv-math-0108046v3
doc_title: "arXiv:math/0108046v3 [math.RT] 3 May 2002"
section_id: page-014
section_title: "Page 14"
section_number: null
pages: 14-14
source_pdf: 0108046v3.pdf
source_sha256: f47c1bd39c671cf3
toc_source: undetermined
doc_brief: "Presenting Schur algebras — Motivated by work of R.M. Green, we obtain a pre- sentation of Schur algebras (both the classical and quantized ver- sions) in terms of generators and relations."
---
14
STEPHEN DOTY AND ANTHONY GIAQUINTO
Proposition 3.8. For any α ∈Φ, λ ∈Λ(n, d) we have the commuta-
tion formulas
xα1λ =
(
1λ+αxα
if λ + α ∈Λ(n, d)
0
otherwise
and similarly
1λxα =
(
xα1λ−α
if λ −α ∈Λ(n, d)
0
otherwise.
Proof. Write α = εi −εj with i̸ = j. From the deﬁning relation (R3)
and the deﬁnition (see §1) of xα we have
Hlxα = xα(Hl + (εl, α)).
(3.9)
From this we obtain equalities
xα1λ = xα
H1
λ1

· · ·
Hn
λn

=
 Hi −1
λi
Hj + 1
λj
 Y
l̸=i,j
Hl
λl
!
xα.
Multiplying on the left by Hi/(λi + 1) and then commuting with xα
yields the equality
xα
Hi + 1
λi + 1 1λ =
Hi
λi + 1
 Hi −1
λi
Hj + 1
λj
 Y
l̸=i,j
Hl
λl
!
xα
which by Proposition 3.6(a) simpliﬁes to give
xα1λ =
  Hi
λi + 1
Hj + 1
λj
 Y
l̸=i,j
Hl
λl
!
xα
which (if λj > 0) can be rewritten in the form
xα1λ =
 Hi
λi + 1
 Hj
λj

+
 Hj
λj −1
 Y
l̸=i,j
Hl
λl

xα.
The ﬁrst summand on the right-hand-side of the preceding equality
vanishes, by Proposition 3.4(c). This proves the ﬁrst part of the propo-
sition in the case λj > 0. In case λj = 0 the right-hand-side is zero.
This proves the ﬁrst part of the proposition. The proof of the second
part is similar.
Corollary 3.10. We have in T the equalities xd+1
α
= 0 for all α ∈Φ.
