---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-018-52-the-current-algebra-for-sln
section_title: "The current algebra for sln"
section_number: 5.2
pages: 35-43
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
Let us deﬁne the current algebra U(sln[t]) = U(sln ⊗ /C9 [t]). This algebra is generated over /CZ by
x+
i,r, x−
i,s and ξi,k for r,s,k ∈ /C6 ∪ {0} and 1 ≤i<n modulo the following relations:
C1: Fori,j inI and r,s ∈ /C6 ∪ {0}
[ξi,r,ξ j,s] = 0
C2: For any i,j ∈I and k ∈ /C6 ∪ {0},
[ξi,0,x ±
j,k] = ±aijx±
j,k
C3: For any i,j ∈I and r,k ∈ /C6 ∪ {0},
[ξi,r,x ±
j,k] = ±aijx±
j,r+k
C4: Fori,j ∈I and k,ℓ ∈ /C6 ∪ {0}
[x±
i,k+1,x ±
j,ℓ] = [x±
i,k,x ±
j,ℓ+1]
C5: Fori,j ∈I and k,ℓ ∈ /C6 ∪ {0}
[x+
i,k,x −
j,ℓ] = δi,jξi,k+ℓ
C6: Let i ⁄=j and set m = 1 −aij. For every k1,...,k m ∈ /C6 ∪ {0} and ℓ ∈ /C6 ∪ {0}
∑
π∈Sm
m∑
s=0
(−1)s
( m
s
)
x±
i,kπ (1)
...x ±
i,kπ (s)
x±
j,ℓx±
i,kπ (s+1)
...x ±
i,kπ (m)
= 0.
For more on the relationship between the current algebra and spec ializations of the Yangian see [3].
Recall that we denote by ˙U(sln[t]) the idempotented form of the current algebra.
Exercise 22. Show for t = 1 that the current algebra relations restrict to the deﬁning r elations for
U(sln).
The next proposition is a step towards generalizing Theorem 5.1.
Proposition 23. Let Ei,r, Fj,s, Hi,r denote the generators of Tr(U ∗(sln)):
Ei,r1λ :=


λ
/d79/d79•r
i

, Fj,s1λ :=


λ
/d15/d15
j
•s

, Hi,r1λ := [pi,r(λ) Id 1λ ],
where pi,r(λ) was deﬁned in equation 4.36. For any choice of scalars Q with t2
ij = t2
ji = tij−1tji = 1
for i ⁄=j, there is a well deﬁned homomorphism
(5.7) h : ˙U(sln[t]) − →Tr(U ∗(sln)),
36 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
given by
(5.8) x+
i,r1λ ↦→(−1)(i+1)r Ei,r1λ, x −
j,s1λ ↦→(−1)(j+1)s Fj,s1λ, ξ i,r1λ ↦→(−1)(i+1)r Hi,r1λ.
Proof. To prove this proposition we verify the current algebra relations us ing the relations in the 2-
category U ∗(sln). We only need to consider the case i ⁄= j, since the relations in U ∗(sl2) have been
proven in [8]. C1 is clear, since multiplication by a bubble is a commutative operation. We p rove the
equality C3 for the case j =i ± 1. For convenience we will only depict the interior of the annulus for
diagrams on the annulus in our calculation below where vij :=t−1
ij tji.
Hi,aEj,b1λ =
a∑
k=0
k
i
/d15/d15/d77/d77
•
♠+k
i
/d81/d81/d15/d15
•
♠+a−k
j
/d15/d15/d77/d77
•
b
λ
(4.32) a∑
k=0
k
i
/d81/d81/d15/d15
•
♠+a−k
i
/d15/d15/d77/d77
•
♠+k
λ
/d15/d15/d79/d79
j
•
b
+ vij
a∑
k=0
k
i
/d81/d81/d15/d15
•
♠+a−k
i
/d15/d15/d77/d77
•
♠+k−1
λ
/d15/d15/d79/d79
j
•
b+1
(4.34) a∑
k=0
a−k∑
ℓ=0
k (−vij)ℓ i
/d15/d15/d77/d77
•
♠+k
i
/d81/d81/d15/d15
•
♠+a−k−ℓ
λ
/d15/d15/d79/d79
j
•
ℓ+b
+ vij
a∑
k=0
a−k∑
ℓ=0
k (−vij)ℓ i
/d15/d15/d77/d77
•
♠+k−1
i
/d81/d81/d15/d15
•
♠+a−k−ℓ
λ
/d15/d15/d79/d79
j
•
ℓ+b+1
=
a∑
ℓ=0
a−ℓ∑
k=0
k (−vij)ℓ i
/d15/d15/d77/d77
•
♠+k
i
/d81/d81/d15/d15
•
♠+a−k−ℓ
λ
/d15/d15/d79/d79
j
•
ℓ+b
+vij
a∑
ℓ=0
a−ℓ−1∑
k=0
(k+1) (−vij)ℓ i
/d15/d15/d77/d77
•
♠+k
i
/d81/d81/d15/d15
•
♠+a−k−ℓ−1
λ
/d15/d15/d79/d79
j
•
ℓ+b+1
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 37
(4.36) a∑
ℓ=0
(−vij)ℓ
λ
Hi,a−ℓ /d15/d15/d79/d79
j
•
ℓ+b
−
a+1∑
ℓ=1
a−ℓ∑
k=0
(k + 1) ( −vij)ℓ i
/d15/d15/d77/d77
•
♠+k
i
/d81/d81/d15/d15
•
♠+a−k−ℓ
λ
/d15/d15/d79/d79
j
•
ℓ+b
Pulling oﬀ k of the summands in the second term and observing that the ℓ =a + 1 term vanishes we
have
=
a∑
ℓ=0
(−vij)ℓ
λ
Hi,a−ℓ /d15/d15/d79/d79
j
•
ℓ+b
−
a∑
ℓ=1
(−vij)ℓ
λ
Hi,a−ℓ /d15/d15/d79/d79
j
•
ℓ+b
−
a∑
ℓ=1
a−ℓ∑
k=0
(−vij)ℓ i
/d15/d15/d77/d77
•
♠+k
i
/d81/d81/d15/d15
•
♠+a−k−ℓ
λ
/d15/d15/d79/d79
j
•
ℓ+b
=
λ
Hi,a /d15/d15/d79/d79
j
•
b
−
a∑
ℓ=1
(−vij)ℓ
λ
δa−ℓ,0 /d15/d15/d79/d79
j
•
ℓ+b
=
λ
Hi,a /d15/d15/d79/d79
j
•
b
− (−vij)a λ /d15/d15/d79/d79
j
•
a+b
= Ej,bHi,a1λ − (−vij)a Ej,a+b1λ.
By choosing vij = 1, we get
[Hi,a, Ej,b]1λ = −(−1)aEj,a+b1λ.
The relation
[Hi,a, Fj,b]1λ = (−1)aFj,a+b1λ.
can be proven in a similar way. C4 follows from the relations (4.16) and (4.17):
tij
λ /d16/d16/d79/d79
j
•
b
/d15/d15/d79/d79
i
•
a+1
+tji
λ /d16/d16/d79/d79
j
•
b+1
/d15/d15/d79/d79
i
•
a
(4.16) λ
/d79/d79/d79/d79
/d15/d15/d79/d79 /d15/d15/d79/d79
j i
•a •b
(4.17) λ
/d79/d79/d79/d79
/d15/d15/d79/d79 /d15/d15/d79/d79
i j
•b •a
38 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
(4.16)
tji
λ /d16/d16/d79/d79
i
•
a
/d15/d15/d79/d79
j
•
b+1
+tij
λ /d16/d16/d79/d79
i
•
a+1
/d15/d15/d79/d79
j
•
b
.
Dividing both sides of this equation by tij, and by choosing vij = 1, we get
[Ei,a+1, Ej,b]1λ = −[Ei,a, Ej,b+1]1λ.
If we reverse the arrows in the preceding equation, they still hold:
[Fi,a+1, Fj,b]1λ = −[Fi,a, Fj,b+1]1λ.
The choice of signs in (5.8) correspond to
[x±
i,a+1,x ±
j,b] = [x±
i,a,x ±
j,b+1].
The relation C5 for the case i ⁄=j can be checked the following way:
Ei,aFj,b1λ = λ /d80/d80/d15/d15
j
•
b
/d15/d15/d79/d79
i
•
a
(4.20)
t−1
ji
λ
/d79/d79/d15/d15
/d79/d79/d18/d18 /d15/d15/d79/d79
j i
•a •b
(4.17)
(4.17)
t−1
ji
λ
/d15/d15/d79/d79
/d15/d15/d79/d79 /d79/d79/d18/d18
i j
•b •a
(4.20) λ /d16/d16/d79/d79
i
•
a
/d79/d79/d15/d15
j
•
b
= Fj,bEi,a1λ.
We now prove the Serre relation C6 in the case when i ·j = −1. Let us prove the identity
Ei,aEj,bEi,c1λ + Ei,cEj,bEi,a1λ = Ei,aEi,cEj,b1λ + Ej,bEi,aEi,c1λ.
(5.9)
Ei,aEj,bEi,c1λ = λ /d16/d16/d79/d79
i
•
c
/d15/d15/d79/d79
j
•
b
/d15/d15/d79/d79
i
•
a
(4.19)
t−1
ij /d79/d79/d79/d79
/d79/d79/d79/d79
/d79/d79/d79/d79
λ
i j i
•
c
•
b
•
a
/d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 /d15/d15/d79/d79 /d15/d15/d79/d79
−t−1
ij /d79/d79 /d79/d79
/d79/d79 /d79/d79
/d79/d79 /d79/d79
λ
iji
•
c
•
b
•
a
/d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 /d15/d15/d79/d79 /d15/d15/d79/d79
.
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 39
The ﬁrst term on the right-hand-side of (5.9) can be simpliﬁed
t−1
ij /d79/d79/d79/d79
/d79/d79/d79/d79
/d79/d79/d79/d79
λ
i j i
•
c
•
b
•
a
/d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 /d15/d15/d79/d79 /d15/d15/d79/d79
= tij
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79
/d79/d79 /d79/d79/d79/d79 /d15/d15/d15/d15
/d15/d15/d15/d15
/d15/d15
/d15/d15/d79/d79i ij
•
c
•
b
•
a
.(5.10)
using the biadjoint relations and equations (4.14) and (4.15) to slide c rossings around the annulus.
This diagram can be further simpliﬁed using the KLR relations
(5.11)
(4.16)
t3
ji
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79
/d79/d79 /d79/d79/d79/d79 /d15/d15/d15/d15/d15/d15
/d15/d15/d79/d79i ij
•
c
•
b+1
•
a
+ t2
jitij
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79
/d79/d79 /d79/d79/d79/d79 /d15/d15/d15/d15/d15/d15
/d15/d15/d79/d79i ij
•
c
•
b
•
a+1
where we freely slide dots through caps and cups using the dot cyclic ity relation (4.12). The second
term on the right-hand-side of (5.9) can also be simpliﬁed
t−1
ij /d79/d79 /d79/d79
/d79/d79 /d79/d79
/d79/d79 /d79/d79
λ
iji
•
c
•
b
•
a
/d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 /d15/d15/d79/d79 /d15/d15/d79/d79
= tij
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79
/d79/d79 /d79/d79 /d79/d79 /d15/d15/d15/d15
/d15/d15/d15/d15
/d15/d15
/d15/d15/d79/d79 i ji
• c • b • a
=
40 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
(4.16)
t2
ij
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79 /d79/d79 /d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 i ji
•
b+1
•
c
•
a
+ tijtji
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79 /d79/d79 /d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 i ji
•
b
•
c+1
•
a
Combining terms and simplifying using that t2
ij =t2
ji = 1, vij = 1 for our choice of scalars, we have
(5.12) λ /d16/d16/d79/d79
i
•
c
/d15/d15/d79/d79
j
•
b
/d15/d15/d79/d79
i
•
a
=
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79
/d79/d79 /d79/d79/d79/d79 /d15/d15/d15/d15/d15/d15
/d15/d15/d79/d79i ij
•
c
•
b+1
•
a
+
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79
/d79/d79 /d79/d79/d79/d79 /d15/d15/d15/d15/d15/d15
/d15/d15/d79/d79i ij
•
c
•
b
•
a+1
− λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79 /d79/d79 /d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 i ji
•
b+1
•
c
•
a
− λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79 /d79/d79 /d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 i ji
•
b
•
c+1
•
a
.
By interchanging a and c in the equation (5.12), we get
(5.13) λ /d16/d16/d79/d79
i
•
a
/d15/d15/d79/d79
j
•
b
/d15/d15/d79/d79
i
•
c
=
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79
/d79/d79 /d79/d79/d79/d79 /d15/d15/d15/d15/d15/d15
/d15/d15/d79/d79i ij
•
a
•
b+1
•
c
+
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79
/d79/d79 /d79/d79/d79/d79 /d15/d15/d15/d15/d15/d15
/d15/d15/d79/d79i ij
•
a
•
b
•
c+1
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 41
− λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79 /d79/d79 /d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 i ji
•
b+1
•
a
•
c
− λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79 /d79/d79 /d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 i ji
•
b
•
a+1
•
c
.
Using the relation (2.7) and induction, one can easily prove the followin g equation:
(5.14)
•a •c
iλ = −
•c •a
iλ .
Also, the following equation directly follows from (2.4) and (5.14)
(5.15) λ /d16/d16/d79/d79
i
•
c
/d15/d15/d79/d79
i
•
a
=
•a+1 •c
iλ +
•c+1 •a
iλ .
We add the right and left hand sides of the equations (5.12) and (5.13 ), and after eliminating terms
using (5.14), we get
(5.16) λ /d16/d16/d79/d79
i
•
a
/d15/d15/d79/d79
j
•
b
/d15/d15/d79/d79
i
•
c
+ λ /d16/d16/d79/d79
i
•
c
/d15/d15/d79/d79
j
•
b
/d15/d15/d79/d79
i
•
a
=
42 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
=
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79
/d79/d79 /d79/d79/d79/d79 /d15/d15/d15/d15/d15/d15
/d15/d15/d79/d79i ij
•
c
•
b
•
a+1
− λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79 /d79/d79 /d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 i ji
•
b
•
c+1
•
a
+
+
λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79
/d79/d79 /d79/d79/d79/d79 /d15/d15/d15/d15/d15/d15
/d15/d15/d79/d79i ij
•
a
•
b
•
c+1
− λ
/d15/d15/d79/d79 /d15/d15/d79/d79
/d79/d79/d79/d79 /d79/d79 /d15/d15 /d15/d15 /d15/d15
/d15/d15/d79/d79 i ji
•
b
•
a+1
•
c
.
Combining the respective terms using the relation (5.15) in the equat ion (5.16), we have
(5.17) λ /d16/d16/d79/d79
i
•
a
/d15/d15/d79/d79
j
•
b
/d15/d15/d79/d79
i
•
c
+ λ /d16/d16/d79/d79
i
•
c
/d15/d15/d79/d79
j
•
b
/d15/d15/d79/d79
i
•
a
=
= λ /d16/d16/d79/d79
i
•
c
/d15/d15/d79/d79
i
•
a
/d15/d15/d79/d79
j
•
b
+ λ /d16/d16/d79/d79
j
•
b
/d15/d15/d79/d79
i
•
c
/d15/d15/d79/d79
i
•
a
=
= Ej,bEi,aEi,c1λ + Ei,aEi,cEj,b1λ.
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 43
Reversing the orientation of the arrows, we get the identity
Fi,aFj,bFi,c1λ + Fi,cFj,bFi,a1λ = Fi,aFi,cFj,b1λ + Fj,bFi,aFi,c1λ.
□
