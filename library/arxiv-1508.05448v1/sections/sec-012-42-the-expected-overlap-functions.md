---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-012-42-the-expected-overlap-functions
section_title: "The Expected Overlap Functions"
section_number: 4.2
pages: 65-67
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
---
Since the moments Mn(p, q) satisfy concentration of measure, one is primarily only
interested in their expectations. The next quantity we introduce is also deﬁned just
for the expectation. (Studying its distribution may be interesting, but we will not
comment on this, here.) It is the expected overlap function of Chalker and Mehlig,
introduced in [Chalker and Mehlig, 1998] and further studied by them in [Mehlig and
Chalker, 2000].
Given An ∈ Matn(C), randomly distributed according to Ginibre’s ensemble,
almost surely it may be diagonalized. This means that we can ﬁnd eigenvalues
57
λ1,...,λ n∈ C as well as pairs of vectors ψ1,φ 1,...,ψ n,φn∈ Cn such that
Anψk = λkψk, φ ∗
kAn = λkφ∗
k, φ ∗
kψj = δjk. (4.11)
Using this, for any other vector Ψ ∈ Cn, there is the formula
AnΨ =
n∑
k=1
λk⟨φk, Ψ⟩ψk. (4.12)
These are random because they depend on An, but we may take the expectation over
the randomness.
Given any continuous function, f, with compact support on C, one may deﬁne
ω(1)
n [f] = 1
n E
[ n∑
k=1
f(λk)‖φk‖2‖ψk‖2
]
. (4.13)
Similarly, given any continuous function,F , with compact support on C× C, we may
deﬁne
ω(2)
n [F ] = 1
n E
[ n∑
j=1
∑
k⁄=j
F (λj,λk)⟨ψk,ψj⟩⟨φj,φk⟩
]
. (4.14)
Regularity of the eigenvalues and eigenvectors with respect to the matrix entries
guarantees existence of functionsO(1)
n : C→ C andO(2)
n : C× C→ C such that
ω(1)
n [f] =
∫
C
f(z)O(1)
n (z)d2z and ω(2)
n [F ] =
∫
C
∫
C
F (z,w )O(2)
n (z,w )d2zd 2w.
(4.15)
Using these deﬁnitions, one may determine a relation between these expected over-
lap functions and the correlation functions for the eigenvalues. Deﬁne ρ(1)
n and ρ(2)
n ,
analogously to ω(1)
n and ω(2)
n as
ρ(1)
n [f] = 1
n E
[ n∑
k=1
f(λk)
]
, and ρ(2)
n [F ] = 1
n E
[ n∑
j=1
∑
k⁄=j
F (λj,λk)
]
. (4.16)
58
Then there are functionsR(1)
n : C→ C andR(2)
n : C× C→ C such that
ρ(1)
n [f] =
∫
C
f(z)R(1)
n (z)d2z and ρ(2)
n [F ] =
∫
C
∫
C
F (z,w )R(2)
n (z,w )d2zd 2w.
(4.17)
Then
O(1)
n (z) +
∫
C
O(2)
n (z,w )d2w =R(1)
n (z). (4.18)
In terms of these functions, for any nonnegative integers p and q,
mn((p); (q)) =
∫
C
zpzqO(1)
n (z)d2z +
∫
C
∫
C
zpwqO(2)
n (z,w )d2zd 2w. (4.19)
Therefore, the mixed matrix moments are calculable from the overlap functions.
Moreover, the limiting values of the moments give some constraints for the limit-
ing behavior of the overlap functions. It is easy to see that O(1)
n (eiθz) =O(1)
n (z) and
O(2)
n (eiθz,eiθw) =O(2)
n (z,w ), consistent with the fact thatmn((p); (q)) equals 0 unless
p =q.
