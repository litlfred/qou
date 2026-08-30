---
doc_id: arxiv-2412.02281v1
doc_title: "u + A"
section_id: sec-008-diagonalization-of-the-upper-left-submatrix-of-a
section_title: "Diagonalization of the Upper Left Submatrix of A"
section_number: null
pages: 11-12
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
doc_brief: "Explicit evaluation of the q-Stokes matrices for certain confluent hypergeometric q-difference equations — We prove a connection formula for the basic hypergeomtric fu nction nϕn−1 (a1,...,a n−1"
---
We ﬁrst introduce a diagonalized system under the condition s:
λ (n−1)
i ⁄=λ (n−1)
j , for 1 ≤i ⁄=j ≤n − 1, (30)
λ (n−1)
i ⁄=λ (n−2)
j , for 1 ≤i ≤n − 1, 1 ≤j ≤n − 2. (31)
Under the conditions (30) and (31), let us take the ( n − 1) × (n − 1) matrix Pn−1 given by
(Pn−1)ij :=
(−1)i+j∆ 1,...,n −2
1,..., ˆi,...,n −1
Ä
A −λ (n−1)
j · Idn
ä
√ ∏ n−1
l=1,l ⁄=j
Ä
λ (n−1)
l −λ (n−1)
j
ä ∏ n−2
l=1
Ä
λ (n−2)
l −λ (n−1)
j
ä.
Here ∆ 1,...,n −2
1,..., ˆi,...,n −1
Ä
A −λ (n−1)
j · Idn
ä
is the minor of the matrix A −λ (n−1)
j · Idn, formed by the ﬁrst n − 2 rows
and the ﬁrst n − 1 columns, with the i-th column omitted. Then the inverse matrix of Pn−1 is given explicitly
as follows and we can use Pn−1 to diagonalize the upper left submatrix A(n−1) of A.
11
Proposition 3.4 (see e.g., [15]) . If A satisﬁes (30) and (31), then Pn−1 is invertible and the inverse matrix
P −1
n−1 is given by
Ä
P −1
n−1
ä
ij
=
(−1)i+j ∆ 1,..., ˆj,...,n −1
1,...,n −2
Ä
A −λ (n−1)
i · Idn
ä
√ ∏ n−1
l=1,l ⁄=i
Ä
λ (n−1)
l −λ (n−1)
i
ä ∏ n−2
l=1
Ä
λ (n−2)
l −λ (n−1)
i
ä, for 1 ≤i,j ≤n − 1.
Moreover, we have
P −1
n−1A(n−1)Pn−1 = diag
Ä
λ (n−1)
1 ,...,λ (n−1)
n−1
ä
,
and we introduce
An−1 := diag
Ä
P −1
n−1, 1
ä
·A · diag (Pn−1, 1) =
à
λ (n−1)
1 0 a(n−1)
1
. . . .
.
.
0 λ (n−1)
n−1 a(n−1)
n−1
b(n−1)
1 · · · b(n−1)
n−1 ann
í
.
Herea(n−1)
i and b(n−1)
i are
a(n−1)
i =
n−1∑
v=1
Ä
P −1
n−1
ä
iv
·avn =
(−1)i+n−1∆ 1,...,n −1
1,...,n −2,n
Ä
A −λ (n−1)
i · Idn
ä
√ ∏ n−1
l=1,l ⁄=i
Ä
λ (n−1)
l −λ (n−1)
i
ä ∏ n−2
l=1
Ä
λ (n−2)
l −λ (n−1)
i
ä,
b(n−1)
i =
n−1∑
v=1
anv · (Pn−1)vi =
(−1)i+n−1∆ 1,...,n −2,n
1,...,n −1
Ä
A −λ (n−1)
i · Idn
ä
√ ∏ n−1
l=1,l ⁄=i
Ä
λ (n−1)
l −λ (n−1)
i
ä ∏ n−2
l=1
Ä
λ (n−2)
l −λ (n−1)
i
ä,
and we have
a(n−1)
i b(n−1)
i = −
∏ n
l=1
Ä
λ (n)
l −λ (n−1)
i
ä
∏ n−1
l=1,l ⁄=i
Ä
λ (n−1)
l −λ (n−1)
i
ä. (32)
Now let us use the conjugation of the n ×n matrix diag (Pn−1, 1) to diagonalize the upper left part of the
equation (2) and obtain the equation
DqFq (z) =
Å
Enn + An−1
z
ã
Fq (z). (33)
