---
doc_id: arxiv-hep-th-9609174v2
doc_title: "arXiv:hep-th/9609174v2 23 Sep 1996"
section_id: sec-006-32-universal-correlations
section_title: "Universal correlations"
section_number: 3.2
pages: 14-15
source_pdf: 9609174v2.pdf
source_sha256: 87885f4d03661f26
toc_source: inferred
doc_brief: "arXiv:hep-th/9609174v2 23 Sep 1996 — We prove the universality of correlation functions of chiral unitary and unitary ensembles of ran- dom matrices in the microscopic limit."
---
Universal correlations
The integration kernel associated with the eigenvalue problem of M is (for brevity we set N =
odd = 2N + 1)
KN(λ, µ)=(λ µ)α e−N
2 (V (λ2)+V (µ2)) 1
N
N−1
X
n=0
P (α)
n
(λ)P (α)
n
(µ)
h(α)
n
=(λ µ)α e−N
2 (V (λ2)+V (µ2)) 1
N
 N
X
n=0
1
h(α)
2n
!
P (α)
2N +1(λ)P (α)
2N (µ) −P (α)
2N (λ)P (α)
2N +1(µ)
λ −µ
.(3.29)
Here use is made of the Christoﬀel-Darboux identity, and the proportionality constant in the
second line is determined by matching O(λ0µ0) terms. Noting that the orthogonality relation
(3.3) in the microscopic limit
2
N 2α+1
Z ∞
0
dx x2α P (α)
2n ( x
N )

n=Nt/2
P (α)
2m ( x
N )

m=Nt′/2
= h(α)
2n
2
N δ(t −t′)
(3.30)
13
is identical to the Bessel closure relation (inversion of Hankel transform)
Z ∞
0
dx x Jα−1
2 (ux)Jα−1
2 (u′x) = 1
uδ(u −u′),
(3.31)
we can determine the asymptotic form of the norm as
h(α)
2n =
1
N 2α Γ(α + 1
2)2
 2
u(t)
2α q
r(t) + higher orders in 1
N .
(3.32)
Accordingly we obtain
N
X
n=0
1
h(α)
2n
=
N 2α
Γ(α + 1
2)2 22α · N
2
Z 1
0
dtu(t)2α
p
r(t) =
N 2α+1
Γ(α + 1
2)2 22α
u(1)2α+1
2α + 1 .
(3.33)
Using Theorem 2 and inserting eq. (3.33) into (3.29), we obtain the universal form of the kernel
(the generalized sine kernel of order α) in the microscopic limit
lim
N→∞
1
N KN( x
N , y
N ) = u(1)
2
√xy
Jα+ 1
2(u(1)x)Jα−1
2(u(1)y) −Jα−1
2(u(1)x)Jα+ 1
2(u(1)y)
x −y
.
(3.34)
Therefore all formulae for the correlation functions
ρN(λ1, · · · , λs) =
* s
Y
a=1
1
N tr δ(λa −M)
+
=
det
1≤a,b≤s KN(λa, λb),
(3.35)
previously calculated for the Gaussian unitary ensemble in the microscopic limit [15, 12]
ρS(x1, · · · , xs) = lim
N→∞
1
N s ρN(x1
N , · · · , xs
N ),
(3.36)
hold universally. Speciﬁcally, the spectral density ρN(λ) = ⟨1/N tr δ(λ−M)⟩= KN(λ, λ) univer-
sally takes the form (now ρ(0) = u(1)/π)
ρS(x) =
πρ(0)
2
2
x

J2
α+ 1
2 + J2
α−1
2 −Jα+ 1
2 Jα−3
2 −Jα−1
2Jα+ 3
2

(πρ(0)x) .
(3.37)
It enjoys the matching condition
lim
x→∞ρS(x) = ρ(0).
(3.38)
