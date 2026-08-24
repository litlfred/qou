---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-050-2-2l3mm1l2jm
section_title: "(2l+3)m(m+1)−(l+2+j)m"
section_number: 2
pages: 44-47
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
[
(l + 1)(N− 2m) +l + 2 +j
m
]
q
·
(
1− (q2mx)1+j)(x;q)m
(q;q)m
(mod deg qN ).
Taking the limit N→∞ one can obtain the Watson–Andrews identity (9).
B. (Fusion algebra). Let us deﬁne the level r fusion algebraFr as a ﬁnite dimensional
algebra over rational numbers Q with generators {vj| j = 0, 1
2, 1, 3
2,..., r− 2
2 } and the
following multiplication rule (the level r Clebsch-Gordan series):
vj1
ˆ⊗vj2 =
min(j1+j2, r −2−j1−j2)∑
j=|j1−j2|, j −j1−j2∈Z
vj. (4)
It is well known (see e.g. [Kac]), that the fusion algebra Fr is a commutative and associative
one. Note also, that the fusion rules (4) correspond to a deco mposing the tensor product
Vj1
ˆ⊗Vj2 of the restricted representations [Ros] Vj1 and Vj2 of the Hopf algebra Uq(sl(2))
when q is the root of unity q = exp
(2πi
r
)
into the irreducible parts (see e.g. [Lu3]).
Further, let us denote by Mult Vk (Vj1
ˆ⊗··· ˆ⊗VjN ) the coeﬃcients which appear in the
decomposition of the product vj1
ˆ⊗··· ˆ⊗vjN in the fusion algebra Fr:
vj1
ˆ⊗··· ˆ⊗vjN =
∑
k
MultVk (vj1
ˆ⊗··· ˆ⊗vjN )·vk.
i) Prove the following relation (see Exercise 7, part A, 0 ≤j≤l)
a(l+1)
j,N (1, 1) = Mult Vr(j) (Vˆ⊗(N+1)
s ), s :=
[ l + 1
2
]
,
where for given j,r(j) is the unique integer such that
0≤r(j)≤ r− 3
2 and jr− 3
2 ≡±r(j) (mod (r− 2)).
ii) Prove the following multiplicity formula (cf. [Kir6]):
MultVk (Vj1
ˆ⊗··· ˆ⊗VjN ) =
∑
{ν}
∏
n≥1
(
Pn,r(νij) +mn(ν)
mn(ν)
)
,
where the summation is taken over all partitions ν = (ν1≥ν2≥···≥ 0) such that
Dilogarithm identities 45
a)|ν| :=ν1 +ν2 +... =
N∑
s=1
js−k,
b) (inequalities for vacancy numbers)
Pn,r(ν;j) :=
N∑
s=1
min(n, 2js)− max(n + 2k + 2−r, 0)− 2Qn(ν)≥ 0.
Here Qn(ν) :=
∑
j≥1
min(n,ν j) and mn(ν) is the number of parts of partition ν which are
equal to n.
C. (Restricted Kostka-Foulkes polynomials).
For the given natural number l, partition λ = (λ1≥ λ2≥ 0) and composition µ, we
deﬁne the level l (or restricted) Kostka-Foulkes polynomial K (l)
λ,µ(q) by the following way
K (l)
λ,µ(q) :=
∑
ν, l (ν ′)≤l
q2n(ν)∏
n≥1
[
Pn(ν;µ) +mn(ν)
mn(ν)
]
q
,
where summation is taken over all partitions ν such that
i)|ν| =ν1 +ν2 +··· =λ2, ν1≤l,
ii) Pn(ν;µ) :=
∑
j
min(n,µ j)− 2Qn(ν)≥ 0,∀n.
It follows from the Exercise 7, A, that
a(l+1)
0,N (x;q) =
∑
0≤m≤ N l
2
(qx)mK (l)
(N l−m,m),(lN )(q).
• Prove, that if m≤l, then
K (l)
(N l−m,m),(lN )(q) = K (N l−m,m),(lN )(q) =
[
m +l− 1
l− 1
]
q
.
• Using the deﬁnition of restricted Kostka polynomials K (l)
λ,µ(q), prove that the q-
binomial coeﬃcients
[
m
n
]
q
are the unimodal and symmetric polynomials (cf. [Kir5]).
Conjecture 2. Polynomials K (l)
(N l−m,m),(lN )(q) are unimodal.
Let us consider a simple example with l = 2, N =m = 4. One can compute the Kostka
polynomialK(4,4),(24)(q) by using the Theorem 10. Namely, there exist three conﬁgura tions
0, c = 1 + 1 + 1 + 1− 4 = 0,
0
0
, c = 3 + 1 + 1 + 1− 4 = 2,
0, c = 3 + 3 + 1 + 1− 4 = 4.
46 Anatol N. Kirillov
Consequently, K(4,4),(24)(q) = 1 + q2 + q4 and this is a non-unimodal polynomial,
whereas the level 2 Kostka polynomial K (2)
(4,4),(24)(q) = q4 is the unimodal one.
D. (Polynomial analog of Gordon-Andrews’ identities).
Let us remind the basic facts about the minimal series irredu cible representations of
the Virasoro algebra. Given two (coprime) positive integer sp′>p ≥ 2, then central charge
and highest weights of the corresponding irreducible repre sentationsV (p,p′)
r,s of the Virasoro
algebra are (see e.g. [FF])
c(p,p′) = 1− 6(p′−p)2
pp′ and
∆ (p,p′)
r,s = (rp′−sp)2− (p′−p)2
4pp′ , 1≤r≤p− 1, 1≤s≤p′− 1.
The characters of these representations are ([R-C], [FF])
χ(p,p′)
r,s (q) := q−∆ (p,p ′ )
r,s TrV (p,p ′)
r,s
qL0 = 1
(q)∞
∑
k∈Z
(
qk(kpp′+rp′−sp)−q(kp+r)(kp′+s)
)
. (5)
Note the symmetry of the ”conformal grid”
{(r,s )| 1≤r≤p− 1, 1≤s≤p′− 1}, (6)
(r,s )↔ (p−r,p ′−s) : ∆ (p,p′)
r,s = ∆ (p,p′)
p−r,p′−s⇒χ(p,p′)
r,s (q) = χ(p,p′)
p−r,p′−s(q).
Note also that the RHS(3) is precisely χ(2,5)
1,2−a(q) as given by the RHS(5).
We are interested in ﬁnding a natural polynomial analog for t he character χ(p,p′)
r,s (q).
For this purpose let us introduce the polynomials (cf. [Me2] )
B(N)
p,p′;r,s(q) :=
∑
k∈Z







qk(kpp′+rp′−sp)



N
[ N +s−r−d(p,p ′)
2
]
−p′k



q
−q(pk+r)(p′k+s)



N
[ N−s−r−d(p,p ′)
2
]
−p′k



q







, (7)
where d(p,p ′) :=
[ p′−p
2
]
.
It is clear that in the ”physical region” (6)
lim
N→∞
B(N)
p,p′;r,s(q) = χ(p,p′)
r,s (q).
• Prove the following properties of the ”bosonic” polynomial s (7)
Dilogarithm identities 47
i) (Symmetry) If p≡p′ (mod 2), 1 ≤r≤p− 1 and 1 ≤s≤p′− 1, then
B(N)
p,p′;r,s(q) = B(N)
p,p′;p−r,p′−s(q).
ii) (Positivity) All coeﬃcients of the polynomials B(N)
p,p′:r,s(q) in the ”physical region” (6)
are the non-negative integers.
iii) (Recurrence relations and initial conditions)
B(N)
