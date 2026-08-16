---
doc_id: arxiv-2412.02281v1
doc_title: "u + A"
section_id: sec-007-fundamental-solution-connection-matrix-and-q-sto
section_title: "Fundamental Solution, Connection Matrix and q-Stokes Matrix"
section_number: null
pages: 10-11
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
doc_brief: "Explicit evaluation of the q-Stokes matrices for certain confluent hypergeometric q-difference equations — We prove a connection formula for the basic hypergeomtric fu nction nϕn−1 (a1,...,a n−1"
---
The fundamental solution of (1) is studied in [5] (especiall y when u is invertible). If u is not invertible, there
is a slightly diﬀerent formal fundamental solution (see e.g ., [6]). Particularly, the system (2) has a formal
fundamental solution around inﬁnity as follows
ˆFq(z;Enn,A ) = ˆHq(z;Enn,A )zδ (n−1)
q (A)eq
Å
Ennq−δ (n−1)
q (A)z
ã
,
10
where ˆHq(z;Enn,A ) = Idn + ∑ ∞
m=1H (∞)
m z−m and
δ(n−1)
q (A)ij =



logq(1 − (1 −q)A(n−1))ij, if 1 ≤i,j ≤n − 1,∑ n
l=1µl − ∑ n−1
l=1 νl, if i =j =n,
0, otherwise,
(29)
with A(n−1) being the upper left ( n − 1) × (n − 1) submatrix of A = (aij) and
eq
(
Ennq−δ (n−1)
q (A)z
)
= diag
(
0,..., 0,e q
(
q−δ (n−1)
q (A)nnz
))
.
Proposition 3.1 (see e.g., [2]) . The entries in the last column of ˆFq(z;Enn,A ) are convergent, while the other
entries of ˆFq(z;Enn,A ) are in general divergent.
But still, the entries of (the ﬁrst n − 1 columns of) the formal fundamental solution ˆFq(z;Enn,A ) (or
equivalently ˆHq(z;Enn,A )) of the equation (2) are [ λ ;q]-summable for any λ ∈ C∗\ ∪1≤j≤n−1 [−(1 −q)/q ν j ;q]
(see [1, 6]). That is,
Proposition 3.2 ([1, 6]) . For any λ ∈ C∗\ ∪ 1≤j≤n−1 [−(1 −q)/q ν j ;q], there is a fundamental solution
F (∞)
q (z,λ ;Enn,A ) of the equation (2) obtained from the q-Borel resummation as follows
F (∞)
q (z,λ ;Enn,A ) := H (∞)
q (z,λ ;Enn,A )zδ (n−1)
q (A)eq
Å
Ennq−δ (n−1)
q (A)z
ã
,
with the n ×n matrix H (∞)
q (z,λ ;Enn,A ) given by
H (∞)
q (z,λ ;Enn,A )ij := L[λ ;q]
q;1 ◦ ˆBq;1( ˆHq(z;Enn,A )ij), for i,j = 1,...,n.
Moreover, there is a convergent fundamental solution aroun d the origin of the form (see [5])
F (0)
q (z;Enn,A ) = H (0)
q (z;Enn,A )zlogq(1−(1−q)An ), with H (0)
q (z;Enn,A ) = H (0)
0 +
∞∑
m=1
H (0)
m zm,
where An :=
Ä
λ (n)
1 ,...,λ (n)
n
ä
, logq(1 − (1 −q)An) = diag(µ 1,...,µ n), and H (0)
0 satisﬁes A =H (0)
0 An
Ä
H (0)
0
ä−1
.
Deﬁnition 3.3. For any λ ∈ C∗\ ∪1≤j≤n−1 [−(1 −q)/q ν j ;q], the connection matrix Uq(z,λ ;Enn,A ) of (2) is
deﬁned by
F (∞)
q (z,λ ;Enn,A )Uq(z,λ ;Enn,A ) = F (0)
q (z;Enn,A ).
For another µ ∈ C∗ satisfying µ /∈ [λ ;q] and µ /∈ [−(1 −q)/q ν j ;q], 1 ≤ j ≤ n − 1, the q-Stokes matrix
Sq(z,λ,µ ;Enn,A ) of (2) is deﬁned by
F (∞)
q (z,µ ;Enn,A ) = F (∞)
q (z,λ ;Enn,A )Sq(z,λ,µ ;Enn,A ).
