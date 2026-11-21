---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-011
section_title: "Page 11"
section_number: null
pages: 11-11
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Proposition 2.5. Let λ ∈Y, let λ( · ) ∈D0 be the corresponding continual dia-
gram, and consider the local extrema (2.4). We have
epk[λ( · )] =
m+1
X
i=1
xk
i −
m
X
j=1
yk
j ,
k = 1, 2, . . ..
Proof. Let σ be associated with ω = λ( · ), as deﬁned in (2.1). Then we get
σ′′(x) =
m+1
X
i=1
δ(x −xi) −
m
X
j=1
δ(x −yj) −δ(x).
Note that
R
xkδ(x)dx = 0 for any k = 1, 2, . . . and apply (2.3).
□
Proposition 2.6. Let λ ∈Y and let {xi} ∪{yj} be the local extrema of λ( · ). The
following identity holds
Φ(z −1
2; λ)
Φ(z + 1
2; λ) =
z Qm
j=1(z −yj)
Qm+1
i=1 (z −xi)
.
(2.6)
Proof. We shall prove the identity
Φ(z −1
2; λ) =
Qm+1
i=1 Γ(z −xi)
Γ(z) Qm
j=1 Γ(z −yj) ,
(2.7)
which implies (2.6). Using (1.3), we rewrite (2.7) as
d
Y
i=1
z + bi
z −ai
=
Qm+1
i=1 Γ(z −xi + 1
2)
Γ(z + 1
2) Qm
j=1 Γ(z −yj + 1
2) .
(2.8)
Let (r, s) be the row and column coordinates in the quarter–plane, see the proof
of Proposition 1.1.
Draw the diagonal lines s −r = xi (1 ≤i ≤m + 1) and
s −r = yj (1 ≤j ≤m), which divide the boundary line ∂λ into interlacing vertical
and horizontal pieces.
Assume ﬁrst that xl < 0 < yl for a certain l. Consider an arbitrary vertical piece
of ∂λ which sits above the main diagonal s −r = 0. The ends of such a piece lie on
the lines s −r = yk and s −r = xk+1, where l ≤k ≤m. Inside this piece, the row
Frobenius coordinates increase by one and form the sequence
yk + 1
2,
yk + 3
2,
. . . ,
xk+1 −3
2,
xk+1 −1
2 ,
so that the partial product in Qd
i=1 1/(z−ai) corresponding to this sequence equals
Γ(z −xk+1 + 1
2)
Γ(z −yk + 1
2)
.
It follows that
d
Y
i=1
1
z −ai
=
m
Y
k=l
Γ(z −xk+1 + 1
2)
Γ(z −yk + 1
2)
=
Qm+1
k=l+1 Γ(z −xk + 1
2)
Qm
k=l Γ(z −yk + 1
2)
.
(2.9)
11
