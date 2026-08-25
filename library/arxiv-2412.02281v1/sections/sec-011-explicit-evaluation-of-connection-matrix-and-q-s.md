---
doc_id: arxiv-2412.02281v1
doc_title: "u + A"
section_id: sec-011-explicit-evaluation-of-connection-matrix-and-q-s
section_title: "Explicit Evaluation of Connection Matrix and q-Stokes Matrix of (33)"
section_number: null
pages: 14-17
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
doc_brief: "Explicit evaluation of the q-Stokes matrices for certain confluent hypergeometric q-difference equations — We prove a connection formula for the basic hypergeomtric fu nction nϕn−1 (a1,...,a n−1"
---
In this subsection, we compute the connection matrix Uq(z,λ ;Enn,A n−1) (see Theorem 3.8) and the q-Stokes
matrix Sq (z,λ,µ ;Enn,A n−1) (see Theorem 3.10) of the system (33). The computation depe nds on the con-
nection formula of the equation (5) (see Theorem 1.2 or Theor em 2.26 equivalently).
We introduce the following conditions:
µi −µj /∈ Z, for all 1 ≤i,j ≤n, (with the nonresonant condition (4) included) ,
νi −νj /∈ Z, for all 1 ≤i,j ≤n − 1, (with the condition (30) included) ,
λ (n−1)
j ⁄=λ (n−2)
l , for all 1 ≤j ≤n − 1, 1 ≤l ≤n − 2.
(42)
14
Theorem 3.8. Under the condition (42), and for z,λ such that
λ ∈ C∗, λ /∈ − 1 −q
qν l
qZ, for 1 ≤l ≤n − 1, and z ∈ C∗, z /∈ qν n
1 −qqZ, z /∈ − 1
λqZ,
the entries of the connection matrix Uq(z,λ ;Enn,A n−1) are (see (34) for νn)
Uq(z,λ ;Enn,A n−1)ij = a(n−1)
i
λ (n)
j −λ (n−1)
i
∏ n−1
l=1,l ⁄=i(q1+µ j −ν l ;q)∞
∏ n
l=1,l ⁄=j(q1+ν i−µ l ;q)∞
∏ n
l=1,l ⁄=j(q1+µ j −µ l ;q)∞
∏ n−1
l=1,l ⁄=i(q1+ν i−ν l ;q)∞
× θq
(
−qµ j −ν i−ν n(1 −q)z
)
θq (−q−ν n (1 −q)z) zµ j −ν i, for 1 ≤i ≤n − 1, 1 ≤j ≤n, (43)
Uq(z,λ ;Enn,A n−1)nj =
∏ n−1
l=1 (q1+µ j −ν l ;q)∞∏ n
l=1,l ⁄=j(q1+µ j −µ l ;q)∞
×
∏ n
l=1,l ⁄=jθq((1 −q)q1−µ l/λ )
∏ n−1
l=1 θq((1 −q)q1−ν l/λ )
θq
( qµ j −ν nλz)
θq(λz ) zµ j −ν n, for 1 ≤j ≤n. (44)
Proof. To prove this theorem, we only need to verify that when (43) an d (44) hold, one has
F (0)
q (z;Enn,A n−1)ij =
n∑
k=1
Uq(z,λ ;Enn,A n−1)kjF (∞)
q (z,λ ;Enn,A n−1)ik, for all 1 ≤i,j ≤n. (45)
For every i,j ∈ {1,...,n }, we take the parameters a = (a1,...,a n−1), b = (b1,...,b n−1) in Theorem 2.26 as
al =q1+µ j −ν l−δli, for all 1 ≤l ≤n − 1,
bl =
ß q1+µ j −µ l, for all 1 ≤l ≤j − 1,
q1+µ j −µ l+1, for all j ≤l ≤n − 1,
and replace λ,z by λq 1−δ ni +µ j
1−q ,
∏ n−1
l=1 qν l
∏ n
l=1qµ l (1 −q)z. Therefore, together with Proposition 3.6, Proposition 3. 7,
(39) and (41), we have
F (0)
q (z;Enn,A n−1)ij =
n∑
k=1
Cij,kF (∞)
q (z,λ ;Enn,A n−1)ik.
Here Cij,k is given as follows.
• When 1 ≤i ≤n − 1, 1 ≤j ≤n, we denote that
Cij,k := 1
λ (n)
j −λ (n−1)
i
∏ n−1
l=1,l ⁄=k(q1+µ j −ν l−δli ;q)∞
∏ n
l=1,l ⁄=j(qν k−µ l ;q)∞
∏ n
l=1,l ⁄=j(q1+µ j −µ l ;q)∞
∏ n−1
l=1,l ⁄=k(qν k−ν l−δli ;q)∞
× θq
(
−q1+µ j −ν k−ν n (1 −q)z
)
θq (−q−ν n (1 −q)z)
(
qν k −q1+ν i
)
z1+µ j −ν k
q(1 −q)b(n−1)
k
,
for all k ⁄=i,n , and
Cij,i := a(n−1)
i
λ (n)
j −λ (n−1)
i
∏ n−1
l=1,l ⁄=i(q1+µ j −ν l ;q)∞
∏ n
l=1,l ⁄=j(q1+ν i−µ l ;q)∞
∏ n
l=1,l ⁄=j(q1+µ j −µ l ;q)∞
∏ n−1
l=1,l ⁄=i(q1+ν i−ν l ;q)∞
θq
(
−qµ j −ν i−ν n (1 −q)z
)
θq (−q−ν n (1 −q)z) zµ j −ν i,
Cij,n :=
∏ n−1
l=1 (q1+µ j −ν l ;q)∞
∏ n
l=1,l ⁄=j(q1+µ j −µ l ;q)∞
∏ n
l=1,l ⁄=jθq((1 −q)q1−µ l/λ )
∏ n−1
l=1 θq((1 −q)q1−ν l/λ )
θq
(
qµ j −ν nλz
)
θq(λz ) zµ j −ν n.
• When i =n, 1 ≤j ≤n, we denote that
Cnj,k := − 1
b(n−1)
k
∏ n−1
l=1,l ⁄=k(q1+µ j −ν l ;q)∞
∏ n
l=1,l ⁄=j(qν i−µ l ;q)∞
∏ n
l=1,l ⁄=j(q1+µ j −µ l ;q)∞
∏ n−1
l=1,l ⁄=k(qν i−ν l ;q)∞
θq
( −q1+µ j −ν k−ν n (1 −q)z)
θq (−q−ν n (1 −q)z) z1+µ j −ν k,
for all 1 ≤k ≤n − 1, and
Cnj,n :=
∏ n−1
l=1 (q1+µ j −ν l ;q)∞
∏ n
l=1,l ⁄=j(q1+µ j −µ l ;q)∞
∏ n
l=1,l ⁄=jθq((1 −q)q1−µ l/λ )
∏ n−1
l=1 θq((1 −q)q1−ν l/λ )
θq
(
qµ j −ν nλz
)
θq(λz ) zµ j −ν n.
15
Comparing the explicit expressions of Cij,k and Uq (z,λ ;Enn,A n−1)kj given in (43), (44), by (32) one can
ﬁnd that
Uq (z,λ ;Enn,A n−1)kj =Cij,k, for any 1 ≤i,j,k ≤n.
Thus, (45) is true and this theorem holds.
Theorem 3.9. Under the condition (42), and for z,λ such that
λ ∈ C∗, λ /∈ − 1 −q
qν l
qZ, for 1 ≤l ≤n − 1, and z ∈ C∗, z /∈ qν n
1 −qqZ, z /∈ − 1
λqZ,
the entries of Uq(z,λ ;Enn,A n−1)−1 are for 1 ≤i ≤n, 1 ≤j ≤n − 1:
Ä
Uq(z,λ ;Enn,A n−1)−1ä
ij
= −b(n−1)
j
∏ n
l=1,l ⁄=i(q1+µ l−ν j ;q)∞
∏ n−1
l=1,l ⁄=j(qν l−µ i ;q)∞
∏ n−1
l=1,l ⁄=j(q1+ν l−ν j ;q)∞
∏ n
l=1,l ⁄=i(qµ l−µ i ;q)∞
× θq
(
λz/q 1+µ i−ν j
)
θq (λz )
θq (λqµ i/ (1 −q))
θq (λqν j −1/ (1 −q))zν j −µ i−1, (46)
Ä
Uq(z,λ ;Enn,A n−1)−1ä
in
=
∏ n−1
l=1
( qν l−µ i ;q)
∞∏ n
l=1,l ⁄=i (qµ l −µ i ;q)∞
θq
( −q1+µ i
/ ((1 −q)z))
θq (−q−ν n(1 −q)z) zν n−µ i. (47)
Proof. To prove this theorem, we only need to verify that when (46) an d (47) hold, one has
F (∞)
q (z,λ ;Enn,A n−1)ij =
n∑
k=1
Ä
Uq(z,λ ;Enn,A n−1)−1ä
kj
F (0)
q (z;Enn,A n−1)ik, for all 1 ≤i,j ≤n. (48)
Set the constant Nij,k as follows:
Nij,k :=



















q(1−q)b(n−1)
j
(
λ (n)
k −λ (n−1)
i
)
qν j −q1+ν i , for all 1 ≤i ⁄=j ≤n − 1, 1 ≤k ≤n,
λ (n)
k −λ (n−1)
i
a(n−1)
i
, for all 1 ≤i =j ≤n − 1, 1 ≤k ≤n,
−b(n−1)
j , for all i =n, 1 ≤j ≤n − 1, 1 ≤k ≤n,
q
Ä
λ (n)
k −λ (n−1)
i
ä
, for all 1 ≤i ≤n − 1,j =n, 1 ≤k ≤n,
1, for all i =n,j =n, 1 ≤k ≤n.
Then we have:
• ForF (∞)
q (z,λ ;Enn,A n−1)ij, 1 ≤ i ≤ n, 1 ≤ j ≤ n − 1, we take the parameters a = (a1,...,a n), b =
(b1,...,b n−2) in Lemma 2.23 as
al =q1+µ l−ν j −δij, for all 1 ≤l ≤n,
bl =
ß q1+ν l+δli−ν j −δij, for all 1 ≤l ≤j − 1,
q1+ν l+1+δl+1,i −ν j −δij, for all j ≤l ≤n − 2,
and replace λ,z by λq ν j +δ ij −δ ni
1−q , qν j +δ ij −δ ni
(1−q)z . Therefore, together with Proposition 3.6 and Proposition
3.7, it follows that
F (∞)
q (z,λ ;Enn,A n−1)ij =
n∑
k=1
Mij,kF (0)
q (z;Enn,A n−1)ik,
where
Mij,k :=Nij,k
∏ n
l=1,l ⁄=k(q1+µ l −ν j −δij ;q)∞
∏ n−1
l=1,l ⁄=j(qν l−µ k +δli ;q)∞
∏ n−1
l=1,l ⁄=j(q1+ν l+δli−ν j −δij ;q)∞
∏ n
l=1,l ⁄=k(qµ l−µ k ;q)∞
× θq
(
q2+µ k−ν j −δij/ (λz )
)
θq (q/ (λz ))
θq
(
λq 1+µ k−δni/ (1 −q)
)
θq
(
λqν j +δij −δni/ (1 −q)
) zν j −µ k−1+δij, for all 1 ≤k ≤n.
• ForF (∞)
q (z,λ ;Enn,A n−1)in, 1 ≤ i ≤ n, we take the parameters a = (a1,...,a n−1), b = (b1,...,b n−1) in
Corollary 2.27 as
al =q1+µ n−ν l−δli, for all 1 ≤l ≤n − 1,
bl =q1+µ n −µ l, for all 1 ≤l ≤n − 1,
16
and replace z byq−ν n (1 −q)z. Then, together with (39), (41) and Proposition 3.7 we have
F (∞)
q (z,λ ;Enn,A n−1)in =
n∑
k=1
Min,kF (0)
q (z;Enn,A n−1)ik,
where
Min,k :=Nin,k
∏ n−1
l=1
(
qν l+δli−µ k ;q
)
∞
∏ n
l=1,l ⁄=k (qµ l−µ k ;q)∞
θq
(
−q2−δin+µ k
/
((1 −q)z)
)
θq (−q−ν n(1 −q)z) zν n−µ k −1+δin, for all 1 ≤k ≤n.
Using (32), one can show that if the explicit expressions of Uq(z,λ ;Enn,A n−1)−1 are given by (46) and (47),
then Ä
Uq(z,λ ;Enn,A n−1)−1ä
ks
=Mis,k, for any 1 ≤i,s,k ≤n.
Thus, (48) is true and this theorem holds.
Theorem 3.10. Under the condition (42), and for z,λ,µ such that
λ,µ ∈ C∗, λ,µ / ∈ − 1 −q
qν l
qZ, for 1 ≤l ≤n − 1, µ /∈λq Z, and z ∈ C∗, z /∈ − 1
λqZ, z /∈ − 1
µqZ,
the q-Stokes matrix Sq (z,λ,µ ;Enn,A n−1) of the system (33) takes the block matrix form
Sq (z,λ,µ ;Enn,A n−1) =
Ç
Idn−1 0
b(n)
q 1
å
, (49)
where Idn−1 is the (n − 1) × (n − 1) identity matrix, b(n)
q =
Ä( b(n)
q
)
1,..., ( b(n)
q
)
n−1
ä
with (see (34) for νn)
( b(n)
q
)
j = −b(n−1)
j
n∑
k=1
∏ n−1
l=1 (q1+µ k−ν l ;q)∞
∏ n
l=1,l ⁄=k(q1+µ k −µ l ;q)∞
∏ n
l=1,l ⁄=k(q1+µ l −ν j ;q)∞
∏ n−1
l=1,l ⁄=j(qν l−µ k ;q)∞
∏ n−1
l=1,l ⁄=j(q1+ν l−ν j ;q)∞
∏ n
l=1,l ⁄=k(qµ l−µ k ;q)∞
×
∏ n
l=1,l ⁄=kθq((1 −q)q1−µ l/λ )
∏ n−1
l=1 θq((1 −q)q1−ν l/λ )
θq
( qµ k −ν nλz)
θq(λz )
θq
( qν j −µ k −1µz)
θq (µz )
θq (µqµ k/ (1 −q))
θq (µqν j −1/ (1 −q))zν j −ν n−1.
Proof. From Deﬁnition 3.3, we get
Uq(z,λ ;Enn,A n−1) = Sq(z,λ,µ ;Enn,A n−1)Uq(z,µ ;Enn,A n−1),
from which the entries of Sq(z,λ,µ ;Enn,A n−1) can be derived explicitly.
