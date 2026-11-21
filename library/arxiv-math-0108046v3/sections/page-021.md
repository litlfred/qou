---
doc_id: arxiv-math-0108046v3
doc_title: "arXiv:math/0108046v3 [math.RT] 3 May 2002"
section_id: page-021
section_title: "Page 21"
section_number: null
pages: 21-21
source_pdf: 0108046v3.pdf
source_sha256: f47c1bd39c671cf3
toc_source: undetermined
doc_brief: "Presenting Schur algebras — Motivated by work of R.M. Green, we obtain a pre- sentation of Schur algebras (both the classical and quantized ver- sions) in terms of generators and relations."
---
PRESENTING SCHUR ALGEBRAS
21
From the deﬁning relations (R1′) and the deﬁnition of the Hj it
follows that
n
X
j=1
Hj =
n
X
j=1
X
λ
λj1λ =
X
λ
 n
X
j=1
λj
!
1λ =
X
λ
d 1λ = d · 1 = d.
This proves that the Hj satisfy relation (R6). Moreover, we also have
equalities
1λ Hj = Hj 1λ =
X
µ
µj1µ 1λ = λj1λ
for each λ, j, from which we obtain the equalities
Hj(Hj −1) · · ·(Hj −b) =
 X
λ
λj 1λ
!
(Hj −1) · · · (Hj −b)
=
X
λ
λj(λj −1) · · · (λj −b) 1λ
(6.1)
for any b ∈N. This is 0 when b = d, since λ is a composition of d, and
thus each part λj of λ is an integer in the interval 0, . . . , d. This proves
that the Hj satisfy relation (R7).
We now want to show that the Hj also satisfy relation (R3). For this
we will use the deﬁning relations (R2′). For convenience, we extend the
deﬁnition of the symbol 1λ to all λ ∈Zn such that |λ| = P λi = d,
deﬁning it to have the value 0 if any part of λ is negative. With this
convention we have
Hjei =
X
λ
λj 1λei =
X
λ
λj ei1λ−αi
(6.2)
where the sums are taken over all λ ∈Zn such that |λ| = d. Replacing
λ −αi by µ and noting that λj = µj if j̸ = i, i + 1, λj = µj + 1 if j = i,
and λj = µj −1 if j = i + 1 we obtain
Hjei =
X
µ
λj ei1µ = eiHj + (δij −δi+1,j)ei.
(6.3)
where again the sum is over all µ ∈Zn satisfying |µ| = d. This proves
that the Hj, ei satisfy relation (R3); a similar argument shows the same
for the Hj, fi.
From (6.1) it follows (upon replacing b by b −1 and dividing by b!)
that
Hj
b

=
X
λ
λj
b

1λ
(6.4)
