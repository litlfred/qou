---
doc_id: arxiv-math-ph-0405028v2
doc_title: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-17
source_pdf: 0405028v2.pdf
source_sha256: 90a0e4ba456988d6
doc_brief: "ON THE QUANTUM INVARIANT FOR THE BRIESKORN HOMOLOGY SPHERES — We study an exact asymptotic behavior of the Witten–Reshet ikhin–Turaev SU(2) in- variant for the Brieskorn homology spheres Σ( p1, p 2"
---
arXiv:math-ph/0405028v2  1 Jan 2005
ON THE QUANTUM INV ARIANT FOR THE BRIESKORN HOMOLOGY SPHERES
KAZUHIRO HIKAMI
ABSTRACT . We study an exact asymptotic behavior of the Witten–Reshet ikhin–Turaev SU(2) in-
variant for the Brieskorn homology spheres Σ( p1, p 2, p 3) by use of properties of the modular form
following a method proposed by R. Lawrence and D. Zagier. Key observation is that the invariant
coincides with a limiting value of the Eichler integral of th e modular form with weight 3/ 2. We
show that the Casson invariant is related to the number of the Eichler integrals which do not van-
ish in a limit τ → N ∈ Z. Correspondingly there is a one-to-one correspondence bet ween the
non-vanishing Eichler integrals and the irreducible representation of the fundamental group, and the
Chern–Simons invariant is given from the Eichler integral i n this limit. It is also shown that the
Ohtsuki invariant follows from a nearly modular property of the Eichler integral, and we give an
explicit form in terms of the L-function.
1. I NTRODUCTION
The quantum invariant for the 3-manifold M was introduced as a path integral on M by Wit-
ten [43]; as the SU (2) invariant we have
Zk(M) =
∫
exp
(
2 π i k CS(A)
)
DA (1.1)
where k ∈ Z, and CS(A) is the Chern–Simons functional deﬁned by
CS(A) = 1
8 π2
∫
M
Tr
(
A ∧ dA + 2
3 A ∧ A ∧ A
)
(1.2)
Since this work, studies of the quantum invariants of the 3-manifolds have been extensively devel-
oped, and a construction of the 3-manifold invariant was ref ormulated combinatorially and rigor-
ously in Refs. 15, 33 using a surgery description of M and the colored Jones polynomial deﬁned
in Ref. 14.
By applying a stationary phase approximation, an asymptoti c behavior of the Witten invariant
in large k → ∞ is expected to be [6, 43] (see also Ref. 2)
Zk(M) ∼ 1
2 e− 3
4 πi∑
α
√
Tα(M) e−2πiIα/4 e2πi(k+2) CS(A) (1.3)
Here the sum runs over a ﬂat connection α, and Tα and Iα are the Reidemeister torsion and the
spectral ﬂow deﬁned modulo 8 respectively.
Date: May 2, 2004. Accepted on December 21, 2004.
1
In this article we consider the Brieskorn homology spheres Σ( p1, p2, p3) where pi are pairwise
coprime positive integers. This is the intersection of the singular complex surface
z p1
1 + z p2
2 + z p3
3 = 0
in complex three-space with the unit ﬁve-sphere |z1|2 + |z2|2 + |z3|2 = 1. The manifold Σ(2 , 3, 5)
is the Poincar´ e homology sphere. These manifolds have a rational surgery description as in Fig. 1,
and the fundamental group has the presentation
π1
(
Σ( p1, p2, p3)
)
=
⟨
x1, x2, x3, h
⏐⏐h center, x pk
k = h−qk for k = 1, 2, 3, x1 x2 x3 = 1
⟩
(1.4)
where qk ∈ Z such that
P
3∑
k=1
qk
pk
= 1 (1.5)
Here and hereafter we use
P = P (p1, p2, p3) = p1 p2 p3 (1.6)
PSfrag replacements
0
p1/q1
p2/q2
p3/q3
Figure 1: Rational surgery description of the Brieskorn homology sphere Σ( p1, p 2, p 3)
Asymptotic behavior of the quantum invariant for the homology spheres was studied in Refs. 19,
20, 22, 34–39. Our purpose here is to reformulate these resul ts number theoretically by use of
properties of the modular form following a method of Lawrence and Zagier [23]. A key observation
is a fact that the Witten–Reshetikhin–Turaev (WRT) invariant for the Brieskorn homology spheres
is regarded as a limit value of the Eichler integral of the mod ular form with weight 3/2 as was
suggested in Ref. 23. Using a nearly modular property of the E ichler integral, we can derive an
exact asymptotic behavior of the WRT invariant. Correspondingly, we can ﬁnd an interpretation for
topological invariants such as the Chern–Simons invariant, the Casson invariant [42], the Ohtsuki
invariant [27–30], and the Ray–Singer–Reidemeister torsi on from the viewpoint of the modular
form.
This paper is organized as follows. In section 2 we constructthe WRT invariant for the Brieskorn
homology spheres Σ( p1, p2, p3) following Ref. 22. We use a surgery description of the 3-manifold,
and apply a formula in Ref. 13. In section 3 we introduce the modular form with weight 3/2. This
2
gives a (p1 − 1) (p2 − 1) (p3 − 1)/4-dimensional representation of the modular group P SL(2; Z).
We consider the Eichler integral thereof in section 4. We stu dy a limiting value of the Eichler
integral at τ ∈ Q, and show that the number of the Eichler integrals which have non-zero value in
a limit τ → N ∈ Z is related to the Casson invariant of the Brieskorn homology spheres. It will
be discussed that we have a one-to-one correspondence with t he irreducible representation of the
fundamental group, and that the Chern–Simons invariant is g iven from this limiting value of the
Eichler integral. We further give a nearly modular property of the Eichler integral. In section 5
we reveal a key identity that the WRT invariant for the Brieskorn spheres coincides with a limiting
value of the Eichler integral at τ → 1/N. This was suggested in Ref. 23 where a correspondence
was proved only for a case of the Poincar´ e homology sphere. Combining with results in section 4
we obtain an exact asymptotic expansion of the WRT invariantwhich is constituted from two terms;
one is a sum of dominating exponential term which gives the Ch ern–Simons term, and another is
a “tail” part which may be regarded as a contribution from a tr ivial connection. In section 6 we
prove that the S-matrix of the modular transformation gives both the Reidemeister torsion and the
spectral ﬂow. We show in section 7 that a tail part gives the Ohtsuki invariant. Explicitly computed
is the n-th Ohtsuki invariant in terms of the L-function. The last section is devoted to concluding
remarks.
2. T HE WITTEN –R ESHETIKHIN –TURAEV INVARIANT FOR THE BRIESKORN
HOMOLOGY SPHERES
We introduce the Reshetikhin–Turaev invariant τN (M) [33] for N ∈ Z+. This is related to the
Witten invariant Zk(M) deﬁned in eq. (1.1) as
Zk(M) = τk+2(M)
τk+2(S2 × S1) (2.1)
Here the invariant is normalized to be
τN (S3) = 1
and we have
τN (S2 × S1) =
√
N
2
1
sin(π/N)
When the 3-manifold M is constructed by the rational surgeries pj/qj on the j-th component of
n-component link L, it was shown [13, 33] that the invariantτN (M) is given by
τN (M) = e
πi
4
N−2
N (
∑ n
j=1 Φ( U (pj ,qj ))−3 sign(L))
N −1∑
k1,...,kn=1
Jk1,...,kn(L)
n∏
j=1
ρ(U (pj ,qj))kj,1 (2.2)
3
Here the surgery pj/qj is described by an SL(2; Z) matrix
U (pj ,qj) =
(
pj rj
qj sj
)
and Φ( U) is the Rademacher Φ -function deﬁned by (see, e.g., Ref. 31)
Φ
[(
p r
q s
)]
=



p + s
q − 12 s(p, q) for q ⁄= 0
r
s for q = 0
(2.3)
where s(b, a) denotes the Dedekind sum (see, e.g., Ref. 32, and also Ref. 16)
s(b, a) = sign( a)
|a|−1∑
k=1
(( k
a
))
·
(( k b
a
))
(2.4)
with
((x)) =



x − ⌊x⌋ − 1
2 if x ⁄∈Z
0 if x ∈ Z
and ⌊x⌋ is the greatest integer not exceeding x. It is known that the Dedekind sum is rewritten as
s(b, a) = 1
4 a
a−1∑
k=1
cot
( k
a π
)
cot
( k b
a π
)
An n × n matrix L is a linking matrix Lj,k = lk j,k + pj/qj · δj,k, and sign(L) is a signature of L,
i.e., the difference between the number of positive and negativeeigenvalues of L. The polynomial
Jk1,...,kn(L) is the colored Jone polynomial for linkL with the color kj for the j-th component link,
and ρ(U (p,q)) is a representation ρ of P SL(2; Z);
ρ(U (p,q))a,b
= −i sign(q)√
2 N |q|
e− πi
4 Φ( U (p,q)) e
πi
2N q sb2 ∑
γ mod 2 N q
γ=a mod 2 N
e
πi
2N q pγ2
(
e
πi
N q γb − e− πi
N q γb
)
(2.5)
for 1 ≤ a, b ≤ N − 1 [13], and we have
ρ(S)a,b =
√
2
N sin
( a b π
N
)
ρ(T )a,b = e
πi
2N a2− πi
4 δa,b
(2.6)
with
S =
(
0 −1
1 0
)
T =
(
1 1
0 1
)
(2.7)
satisfying
S2 = (S T )3 = 1
4
We should note [32] that the Dedekind sum satisﬁes
s(−b, a) = −s(b, a) (2.8)
s(b, a) = s(b′, a) for b b′ ≡ 1 (mod a) (2.9)
and that the Rademacher Φ -function fulﬁlls
Φ( S U (p,q)) = Φ( U (p,q)) − 3 sign( p q) (2.10)
Proposition 1 ( [22]). The WRT invariant for the Brieskorn homology spheres is given by
e
2πi
N ( φ
4 − 1
2 )
(
e
2πi
N − 1
)
τN
(
Σ( p1, p2, p3)
)
= eπi/4
2
√
2 P N
2 P N −1∑
n=0
N ∤ n
e− 1
2P N n2πi
∏ 3
j=1
(
e
n
N pj
πi
− e
− n
N pj
πi)
e
n
N πi − e− n
N πi (2.11)
where
φ = φ(p1, p2, p3) = 3 − 1
P + 12
(
s(p2 p3, p1) + s(p1 p3, p2) + s(p1 p2, p3)
)
(2.12)
Proof. This was proved in Refs. 22, 38 for a general n-ﬁbered manifold, but we give a proof here
again for completion.
The Jones polynomial for a link L depicted in Fig. 1 is given by
Jk0,k1,k2,k3(L) = 1
sin(π/N) ·
∏ 3
j=1 sin (k0 kj π/N)
sin2 (k0 π/N)
where k0 is a color of an unknotted component whose linking number wit h other components is
1, and kj (for j = 1 , 2, 3) denotes a color of a component of link L which is to be pj/qj-surgery.
With this setting we have
sign(L) =
3∑
j=1
sign
( qj
pj
)
− 1
From (2.2) we get the quantum invariant as
(
eπi/N − e−πi/N)
· τN
(
Σ( p1, p2, p3)
)
= e
πi
4
N−2
N (3+∑ 3
j=1 Φ( SU (pj ,qj )))
N −1∑
k0=1
ρ(S)k0,1
(
e
πi
N k0 − e− πi
N k0
) 2
×
3∏
j=1
N −1∑
kj=1
ρ(U (pj ,qj))kj,1
(
e
πi
N k0kj − e− πi
N k0kj
)
In this expression we have by deﬁnition
ρ(S)k0,1 = −i√
2 N
(
e
πi
N k0 − e− πi
N k0
)
5
and for ℓ ∈ Z we have
N −1∑
k=1
ρ(U (p,q))k,1
(
e
πi
N ℓk − e− πi
N ℓk
)
= −i e− πi
4 Φ( U (p,q))+ πis
2N q
sign(q)√
2 N |q|
N −1∑
k=1
∑
γ mod 2 N q
γ≡k mod 2 N
e
πip
2N q γ2
(
e
πi
N q γ − e− πi
N q γ
)(
e
πi
N ℓγ − e− πi
N ℓγ
)
= −i e− πi
4 Φ( U (p,q))+ πis
2N q
sign(q)√
2 N |q|
∑
γ mod 2 N q
e
πi
2N q pγ2
(
e2πi qℓ+1
2N q γ − e2πi qℓ−1
2N q γ
)
= −sign(p)√
|p|
e− πi
4 Φ( SU (p,q))+ πis
2N q
∑
n mod p
(
e− πi
2pqN (2N qn+qℓ+1)2
− e− πi
2pqN (2N qn+qℓ−1)2
)
Here in the ﬁrst equality we have used γ = k (mod 2 N), and applied a symmetry under γ →
2 N q − γ in the second equality. In the last equality, we have used an i dentity e
πi
2 (1−sign(p)) =
sign(p), and the Gauss sum reciprocity formula [13]
∑
n mod N
e
πi
N M n2+2πikn =
√ ⏐⏐⏐⏐
N
M
⏐⏐⏐⏐e
πi
4 sign(N M)
∑
n mod M
e− πi
M N (n+k)2
(2.13)
where N, M ∈ Z with N k ∈ Z and N M being even.
A combination of these results reduces to
(
eπi/N − e−πi/N)
· τN
(
Σ( p1, p2, p3)
)
= i sign( P )√
2 |P | N
e
3
4 πi+ πi
2N
∑
j
1
pj qj
− πi
2N φ
N −1∑
k0=1
∑
nj mod pj
1
e
πi
N k0 − e− πi
N k0
×
3∏
j=1
(
e
− πi
2N pj qj
(2N qj nj +k0qj+1)2
− e
− πi
2N pj qj
(2N qj nj+k0qj−1)2)
The summand is invariant under (i) k0 → k0 + 2 N and nj → nj − 1, (ii) nj → nj + pj. Using
this symmetry and recalling that pj are pairwise coprime integers, the sum,∑ N −1
k0=1
∑
nj mod pj, is
transformed into a sum,∑
k0=a+2N n
1≤a≤N −1
0≤n≤P −1
, with setting all nj = 0. As a result, we ﬁnd
(
eπi/N − e−πi/N)
· τN
(
Σ( p1, p2, p3)
)
= − i√
2 P N
e
3
4 πi− πi
2N φ
∑
k0=a+2N n
1≤a≤N −1
0≤n≤P −1
e− πi
2N P k 2
0
∏ 3
j=1
(
e
πi
N pj
k0
− e
− πi
N pj
k0
)
e
πi
N k0 − e− πi
N k0
Setting k0 → 2 P N − k0, we obtain a statement of the proposition. □
6
3. M ODULAR FORMS
We deﬁne the odd periodic function χ(ℓ1,ℓ2,ℓ3)
2P (n) with modulus 2 P by
χ(ℓ1,ℓ2,ℓ3)
2P (n) =



1 for n = P
(
1 +
3∑
j=1
εj
ℓj
pj
)
mod 2 P where ε1ε2ε3 = −1
−1 for n = P
(
1 +
3∑
j=1
εj
ℓj
pj
)
mod 2 P where ε1ε2ε3 = 1
0 others
(3.1)
Here P = p1 p2 p3 with pairwise coprime positive integers pj, and we mean εj = ±1. Integers ℓj
are
1 ≤ ℓj ≤ pj − 1 (3.2)
There exists a symmetry of the periodic function
χ(ℓ1,ℓ2,ℓ3)
2P (n) = χ(p1−ℓ1,p2−ℓ2,ℓ3)
2P (n)
= χ(p1−ℓ1,ℓ2,p3−ℓ3)
2P (n) = χ(ℓ1,p2−ℓ2,p3−ℓ3)
2P (n) (3.3)
With this periodic function, we deﬁne the function Φ (ℓ1,ℓ2,ℓ3)
p (τ ) for τ in the upper half plane,
τ ∈ H, by
Φ (ℓ1,ℓ2,ℓ3)
p (τ ) = 1
2
∑
n∈Z
n χ(ℓ1,ℓ2,ℓ3)
2P (n) q
n2
4P (3.4)
where as usual
q = exp(2 π i τ )
Eq. (3.3) makes the number of the independent functions Φ (ℓ1,ℓ2,ℓ3)
p (τ ) to be
D = D(p1, p2, p3) = 1
4 (p1 − 1) (p2 − 1) (p3 − 1) (3.5)
Proposition 2. The function Φ (ℓ1,ℓ2,ℓ3)
p (τ ) is a modular form with weight 3/2. Namely under the S-
and T -transformations (2.7) we have
Φ (ℓ1,ℓ2,ℓ3)
p (τ ) =
( i
τ
) 3/2 ∑
ℓ′
1,ℓ′
2,ℓ′
3
S
ℓ′
1,ℓ′
2,ℓ′
3
ℓ1,ℓ2,ℓ3 Φ
(ℓ′
1,ℓ′
2,ℓ′
3)
p (−1/τ ) (3.6)
Φ (ℓ1,ℓ2,ℓ3)
p (τ + 1) = Tℓ1,ℓ2,ℓ3Φ (ℓ1,ℓ2,ℓ3)
p (τ ) (3.7)
7
where the sum runs over D(p1, p2, p3) distinct triples. A D × D matrix S and diagonal matrix T
are respectively given by
S
ℓ′
1,ℓ′
2,ℓ′
3
ℓ1,ℓ2,ℓ3 =
√
32
P (−1)
1+P +P∑ 3
j=1
ℓj +ℓ′
j
pj
+(ℓ×ℓ′)·p
3∏
j=1
sin
(
P ℓj ℓ′
j
p 2
j
π
)
(3.8)
Tℓ1,ℓ2,ℓ3 = exp
(
π i
2 P
(
1 +
3∑
j=1
ℓj
pj
) 2
)
(3.9)
We omit a proof as it is tedious but straightforward. We only n eed the Poisson summation
formula
∑
n∈Z
f (n) =
∑
n∈Z
∫ ∞
−∞
e−2πitn f (t) dt (3.10)
4. T HE EICHLER INTEGRAL AND THE CHERN –SIMONS INVARIANT
The Eichler integral was originally deﬁned as a k − 1-fold integration of a modular form with
integral weight k ∈ Z≥2 (see, e.g., Ref. 18). Following Refs. 23, 44 (see also Refs. 9–11), we
deﬁne the Eichler integral of the modular form Φ (ℓ1,ℓ2,ℓ3)
p (τ ) with half-integral weight 3/2 by
~Φ (ℓ1,ℓ2,ℓ3)
p (τ ) =
∞∑
n=0
χ(ℓ1,ℓ2,ℓ3)
2P (n) q
n2
4P (4.1)
We should remark that there are D(p1, p2, p3) independent Eichler integrals due to the symme-
try (3.3).
Proposition 3. The function~Φ (ℓ1,ℓ2,ℓ3)
p (τ ) has a limiting value in τ → 1/N for N ∈ Z as
~Φ (ℓ1,ℓ2,ℓ3)
p (1/N) =
P N∑
n=0
χ(ℓ1,ℓ2,ℓ3)
2P (n)
(
1 − n
P N
)
e
1
2P N n2πi (4.2)
We also have
~Φ (ℓ1,ℓ2,ℓ3)
p (N) = − 1
2 P
( 2P∑
n=1
n χ(ℓ1,ℓ2,ℓ3)
2P (n)
)
e
πi
2 P N
(
1+∑
j
ℓj
pj
) 2
(4.3)
= − 1
2 P
( 2P∑
n=1
n χ(ℓ1,ℓ2,ℓ3)
2P (n)
)
(
Tℓ1,ℓ2,ℓ3
) N
To prove this proposition, we use the following formula for asymptotic expansions (see Refs. 23,
44);
8
Proposition 4. Let Cf (n) be a periodic function with mean value 0 and modulus f. Then we have
an asymptotic expansion as t ց 0;
∞∑
n=1
Cf (n) e−nt ≃
∞∑
k=0
L(−k, Cf ) (−t)k
k! (4.4)
∞∑
n=1
Cf (n) e−n2t ≃
∞∑
k=0
L(−2 k, Cf ) (−t)k
k! (4.5)
Here L(k, Cf ) is the Dirichlet L-function associated with Cf (n), and is given by
L(−k, Cf ) = − f k
k + 1
f∑
n=1
Cf (n) Bk+1
( n
f
)
where Bn(x) is the n-th Bernoulli polynomial deﬁned from
t ext
et − 1 =
∞∑
n=0
Bn(x)
n! tn
See, e.g., Ref. 23 for a proof.
Proof of Proposition 3. We assume M and N are coprime integers, and N > 0. By deﬁnition, we
have
~Φ (ℓ1,ℓ2,ℓ3)
p
( M
N + i y
2 π
)
=
∞∑
n=0
C (ℓ1,ℓ2,ℓ3)
2P N (n) e− y
4P n2
where y > 0 and
C (ℓ1,ℓ2,ℓ3)
2P N (n) = χ(ℓ1,ℓ2,ℓ3)
2P (n) e
M
2P N n2πi
We see that C (ℓ1,ℓ2,ℓ3)
2P N (n + 2 P N ) = C (ℓ1,ℓ2,ℓ3)
2P N (n), and C (ℓ1,ℓ2,ℓ3)
2P N (2 P N − n) = −C (ℓ1,ℓ2,ℓ3)
2P N (n).
Then we can apply Prop. 4, and we have an asymptotic expansion in y ց 0 as
~Φ (ℓ1,ℓ2,ℓ3)
p
( M
N + i y
2 π
)
≃
∞∑
k=0
L(−2 k, C (ℓ1,ℓ2,ℓ3)
2P N )
k!
(
− y
4P
) k
which gives a limiting value as
~Φ (ℓ1,ℓ2,ℓ3)
p (M/N) = L(0, C(ℓ1,ℓ2,ℓ3)
2P N ) (4.6)
Using a fact that χ(ℓ1,ℓ2,ℓ3)
2P (2 P − n) = −χ(ℓ1,ℓ2,ℓ3)
2P (n) and that an explicit form of the Bernoulli
polynomial is B1(x) = x − 1
2, we get
~Φ (ℓ1,ℓ2,ℓ3)
p (M/N) =
P N∑
n=0
χ(ℓ1,ℓ2,ℓ3)
2P (n)
(
1 − n
P N
)
e
M
2P N n2πi
Eq. (4.2) directly follows from this formula. Eq. (4.3) can a lso be given from the above formula
when we recall∑ 2P
n=1 χ(ℓ1,ℓ2,ℓ3)
2P (n) = 0 . □
9
We can see that, though we have D(p1, p2, p3) independent Eichler integrals, the limiting value
~Φ (ℓ1,ℓ2,ℓ3)
p (N) at N ∈ Z computed in eq. (4.3) becomes identically zero for some triples (ℓ1, ℓ2, ℓ3).
Proposition 5. Let γ(p1, p2, p3) be the number of independent Eichler integrals such that
~Φ (ℓ1,ℓ2,ℓ3)
p (N) ⁄≡0 for N ∈ Z, namely
2P∑
n=1
n χ(ℓ1,ℓ2,ℓ3)
2P (n) ⁄= 0 (4.7)
We then have
γ(p1, p2, p3) = s(p1 p2, p3) + s(p2 p3, p1) + s(p1 p3, p2)
+ P
12
(
1 − 1
p 2
1
− 1
p 2
2
− 1
p 2
3
)
− 1
12 P + 1
4 (4.8)
where s(b, a) is the Dedekind sum deﬁned in eq. (2.4).
Proof. For a sake of our brevity we set Ak = ℓi
pi
+ ℓj
pj
− ℓk
pk
for i ⁄= j ⁄= k ⁄= i and i, j, k ∈ {1, 2, 3}.
As we have 0 < ℓk
pk
< 1 by deﬁnition, we have 0 <∑
j
ℓj
pj
< 3 and −1 < A k < 2.
When 0 < ∑
j
ℓj
pj
< 1, we have 0 < A k + 1 < 2
(
1 − ℓk
pk
)
< 2. Then in a domain
0 < n < 2 P , the periodic function χ(ℓ1,ℓ2,ℓ3)
2P (n) deﬁned in eq. (3.1) takes a value 1 when
n = P
(
1 −∑
j
ℓj
pj
)
, P (1 + Ak), while it is −1 when n = P
(
1 +∑
j
ℓj
pj
)
, P (1 − Ak). Then
we ﬁnd∑ 2P
n=1 nχ(ℓ1,ℓ2,ℓ3)
2P (n) = 0 , and it is inconsistent with eq. (4.7).
We thus have a condition 1 < ∑
j
ℓj
pj
< 3 to fulﬁll eq. (4.7), because it is impossible to have
∑
j
ℓj
pj
∈ Z. Under this condition there are two possibilities for a condition of Ak; (i) −1 < A k < 1
for all k, or (ii) −1 < A k < 1 for two k’s and1 < A i < 2 for another i. By the same computation
we can check
2P∑
n=1
n χ(ℓ1,ℓ2,ℓ3)
2P (n) = 4 P (4.9)
for the former case, while we have ∑ 2P
n=1 nχ(ℓ1,ℓ2,ℓ3)
2P (n) = 0 for the latter. To conclude, a condi-
tion (4.7) is fulﬁlled when the triple of integers satisﬁes
1 < ℓ1
p1
+ ℓ2
p2
+ ℓ3
p3
< 3 − 1 < ℓ1
p1
+ ℓ2
p2
− ℓ3
p3
< 1
− 1 < ℓ1
p1
− ℓ2
p2
+ ℓ3
p3
< 1 − 1 < − ℓ1
p1
+ ℓ2
p2
+ ℓ3
p3
< 1
(4.10)
This constraint is depicted as the number of the integral lattice points of an interior of the tetrahe-
dron (see Fig. 2).
10
ℓ1
ℓ2
ℓ3
/Bullet
/Bullet
/Bullet
/Bullet
(p1, 0, 0)
(0, p2, 0)
(0, 0, p3)
Figure 2: The number of the integral lattice points in the tetrahedron coincides with γ(p1, p 2, p 3).
Let N3(p1, p2, p3) be the number of the integral lattice points (ℓ1, ℓ2, ℓ3) such that 0 < ℓ k < p k
and 0 <∑
j
ℓj
pj
< 1. Then by the symmetry of the triple,
(ℓ1, ℓ2, ℓ3) ( ℓ1, p2 − ℓ2, p3 − ℓ3)
(p1 − ℓ1, ℓ2, p3 − ℓ3) ( p1 − ℓ1, p2 − ℓ2, ℓ3) (4.11)
we have
γ(p1, p2, p3) = D(p1, p2, p3) − N3(p1, p2, p3)
It is well known that N3(p1, p2, p3) was computed by Mordell [26] (see also Ref. 32), and by
substituting this result, we get eq. (4.8). □
The Casson invariant λC(M) for the Brieskorn homology spheres M = Σ( p1, p2, p3) is given
by [4, 7] (also see, e.g., Ref. 41)
λC
(
Σ( p1, p2, p3)
)
= −1
2 (s(p1 p2, p3) + s(p2 p3, p1) + s(p1 p3, p2))
− P
24
(
1 − 1
p 2
1
− 1
p 2
2
− 1
p 2
3
)
+ 1
24 P − 1
8 (4.12)
With this result, we have the following theorem.
Theorem 6. The Casson invariant is a minus half of the number of the Eichler integrals which do
not vanish at τ → N ∈ Z;
λC
(
Σ( p1, p2, p3)
)
= −1
2 γ(p1, p2, p3) (4.13)
11
The fundamental group of the Brieskorn homology spheres has the presentation (1.4), and
the Casson invariant is related to the representation space of the fundamental group [4]. That
is to say, we see that γ(p1, p2, p3) coincides with the cardinality of the SU(2) representation
space of π1
(
Σ( p1, p2, p3)
)
, and that the triple (ℓ1, ℓ2, ℓ3) has a one-to-one correspondence with
the irreducible representation. Explicitly when we have an irreducible representation α of
π1
(
Σ( p1, p2, p3)
)
, the conjugacy class of α(xk) is
(
e
pk −ℓk
pk
πi
e
− pk −ℓk
pk
πi
)
(4.14)
where the triple of integers (ℓ1, ℓ2, ℓ3) satisﬁes a condition (4.10).
Using this correspondence with the irreducible representation of the fundamental group, we can
read off the Chern–Simons invariant of the Brieskorn homology spheres [4] (see also Ref. 17);
CS(A) = −P
4
(
1 +
3∑
j=1
ℓj
pj
) 2
mod 1 (4.15)
Theorem 7. The Chern–Simons invariant (4.15) for the Brieskorn homology spheres Σ( p1, p2, p3)
is related to a limit value of the Eichler integral which can b e regarded as the T-matrix of the
modular group; for N ∈ Z we have
~Φ (ℓ1,ℓ2,ℓ3)
p (N) = −2
(
Tℓ1,ℓ2,ℓ3
) N
= −2 e−2πi CS(A)N (4.16)
where the triple of integers (ℓ1, ℓ2, ℓ3) satisﬁes eq. (4.10). The triple (ℓ1, ℓ2, ℓ3) also gives a SU (2)
representation α of the fundamental group (1.4), where the conjugacy class of α(xk) is as in
eq. (4.14).
We should point out that, with s and t being coprime positive integers. the number, (s − 1) (t −
1)/2, of integral lattice points in the 2-dimensional space has a ppeared as the number of the irre-
ducible highest weight representation of the Virasoro algebra of the minimal model M(s, t) in the
conformal ﬁeld theory [3]. The character of the minimal mode l M(s, t) is modular with weight
1/2, and it was shown [11, 12] that the Eichler integral thereof i s a speciﬁc value of the colored
Jones polynomial for the torus knot Ts,t. Also we may say that a one-dimensional analogue of the
number of the integral lattice points is realized in a torus l ink; the colored Jones polynomial for
the torus link T2,2N coincides with the Eichler integral of the ˆsu(2)N −2 character [10], which is
a (N − 1)-dimensional representation (2.6) of the modular group wi th weight 3/2. In this sense,
the Brieskorn homology spheres may be regarded as a generali zation of the torus knot and link
from the viewpoint of the modular form. This may indicate the fact that the Brieskorn homology
sphere Σ( p1, p2, p3) is homeomorphic to thep3-fold cyclic branched covering ofS3 branched along
12
a torus knot Tp1,p2 [25], and that the manifold Σ( p, q, p q n ± 1) can be alternatively constructed by
±1/n-surgery of the torus knot Tp,q.
For our purpose to give an exact asymptotic behavior of the WRT invariant, we shall give an as-
ymptotic expansion of the Eichler integral at τ → 1/N. The Eichler integral is no longer modular,
but it has a nearly modular property when τ ∈ Q as was studied in Ref. 23.
Proposition 8. The Eichler integral ~Φ (ℓ1,ℓ2,ℓ3)
p (τ ) in τ → 1/N for N ∈ Z>0 fulﬁlls a nearly
modular property. Namely, under theS-transformation, we have an asymptotic expansion inN →
∞ as follows;
~Φ (ℓ1,ℓ2,ℓ3)
p (1/N) ≃ −
√
N
i
∑
ℓ′
1,ℓ′
2,ℓ′
3
S
ℓ′
1,ℓ′
2,ℓ′
3
ℓ1,ℓ2,ℓ3
~Φ
(ℓ′
1,ℓ′
2,ℓ′
3)
p (−N)
+
∞∑
k=0
L(−2 k, χ(ℓ1,ℓ2,ℓ3)
2P )
k!
( π i
2 P N
) k
(4.17)
Here the L-function is given by
L(−2 k, χ(ℓ1,ℓ2,ℓ3)
2P ) = −(2 P )2k
2 k + 1
2P∑
j=1
χ(ℓ1,ℓ2,ℓ3)
2P (j) B2k+1
( j
2 P
)
(4.18)
Proof. A proof is essentially the same with one given in Ref. 23 (see also Refs. 9–11). We use
ˆΦ (ℓ1,ℓ2,ℓ3)
p (z) = 1√
2 P i
∫ ∞
z∗
Φ (ℓ1,ℓ2,ℓ3)
p (τ )√τ − z dτ (4.19)
which is deﬁned for z in the lower half plane, z ∈ H−. We mean that z∗ denotes a complex con-
jugate, and we do not have a singularity in integral. Applying the modular S-transformation (3.6),
we see that the functionˆΦ (ℓ1,ℓ2,ℓ3)
p (z) has a nearly modular property;
1√
i z
∑
ℓ′
1,ℓ′
2,ℓ′
3
S
ℓ′
1,ℓ′
2,ℓ′
3
ℓ1,ℓ2,ℓ3
ˆΦ
(ℓ′
1,ℓ′
2,ℓ′
3)
p (−1/z) +ˆΦ (ℓ1,ℓ2,ℓ3)
p (z) = r(ℓ1,ℓ2,ℓ3)
p (z; 0) (4.20)
where we have an analogue of the period function
r(ℓ1,ℓ2,ℓ3)
p (z; α) = 1√
2 P i
∫ ∞
α
Φ (ℓ1,ℓ2,ℓ3)
p (τ )√τ − z dτ (4.21)
for α ∈ Q and z ∈ H−. On the other hand, substituting eq. (3.4) for eq. (4.19), we get for
z = x + i y with y < 0 as follows;
ˆΦ (ℓ1,ℓ2,ℓ3)
p (z) = 1√
2 P i
∑
n∈Z
n χ(ℓ1,ℓ2,ℓ3)
2P (n)
∫ ∞
z∗
e
n2
2P πiτ
√τ − z dτ
=
∞∑
n=0
χ(ℓ1,ℓ2,ℓ3)
2P (n) e
n2
2P πiz erfc
(
n
√
−π y
P
)
13
As a limit of z → α ∈ Q, we ﬁnd that
ˆΦ (ℓ1,ℓ2,ℓ3)
p (α) = ~Φ (ℓ1,ℓ2,ℓ3)
p (α) (4.22)
Then a nearly modular property (4.17) of ~Φ (ℓ1,ℓ2,ℓ3)
p (1/N) follows from eq. (4.20) by setting z →
1/N and taking an asymptotic expansion of the integral (4.21) in N → ∞. □
It should be noted that the sum in the ﬁrst term in the right han d side of eq. (4.17) runs over
D(p1, p2, p3) distinct triples, but, as was clariﬁed in the preceding sect ions, some of them vanish
and there are γ(p1, p2, p3) non-zero contributions, which correspond to a sum of the ﬂat connec-
tion (1.3).
5. T HE WITTEN –RESHETIKHIN –TURAEV INVARIANT AND THE EICHLER INTEGRAL
We have shown that the Eichler integral atτ → N ∈ Z gives the Chern–Simons invariant of the
Brieskorn homology spheres Σ( p1, p2, p3). We shall show that the WRT invariant for the Brieskorn
homology spheres can be expressed in terms of a limiting value of the Eichler integral atτ → 1/N
which is given in eq. (4.2).
Theorem 9. For the Brieskorn homology spheresΣ( p1, p2, p3) such that
1
p1
+ 1
p2
+ 1
p3
< 1
we have
e
2πi
N ( φ(p1,p2,p3)
4 − 1
2 )
(
e
2πi
N − 1
)
τN
(
Σ( p1, p2, p3)
)
= 1
2
~Φ (1,1,1)
p (1/N) (5.1)
Proof. Proof is essentially same with one given in Ref. 23.
We use the Gauss sum;
G(N) =
2N −1∑
n=0
e− 1
2N n2πi =
√
2 N e−πi/4 (5.2)
We see that
G(N) =
2N −1∑
k=0
e− 1
2N (k−n)2πi
= e − 1
2N n2πi
2N −1∑
k=0
e− 1
2N k2πi+ 1
N knπi (5.3)
These identities follow from the reciprocity formula (2.13).
14
As we see that~Φ (1,1,1)
p (1/N) is given by eq. (4.6), we have using Prop. 4 as follows;
~Φ (1,1,1)
p (1/N) = lim
tց0
∞∑
n=0
χ(1,1,1)
2P (n) e
1
2P N n2πi e−nt
= lim
tց0
1
G(P N )
∞∑
n=0
2P N−1∑
k=0
χ(1,1,1)
2P (n) e− 1
2P N k2πi+n( k
P N πi−t)
where in the second equality we have applied eq. (5.3).
We recall that we have the generating function of the odd periodic function χ(1,1,1)
2P (n) as
(zp1p2 − z−p1p2) (zp2p3 − z−p2p3) (zp1p3 − z−p1p3)
zp1p2p3 − z−p1p2p3
=
∞∑
n=0
χ(1,1,1)
2P (n) zn (5.4)
Thus we get
~Φ (1,1,1)
p (1/N) = 1
G(P N )
2P N−1∑
k=0
N ∤k
e− 1
2P N k2πi
∏ 3
j=1
(
e
k
N pj
πi
− e
− k
N pj
πi)
e
k
N πi − e− k
N πi
Here a contribution from the sum over N | k is written by use of eq. (2.13) as
lim
tց0
1
G(P N )
∞∑
n=0
∑
m mod 2 P
χ(1,1,1)
2P (n) e− N
2P m2πi+ mn
P πi−nt
= lim
tց0
1
N
∞∑
n=0
∑
k mod N
χ(1,1,1)
2P (n) e
2P
N πi(k+ n
2P )
2
−nt
which vanishes due to the odd periodicity χ(1,1,1)
2P (n) = −χ(1,1,1)
2P (2 P − n). Comparing with an
expression (2.11), this completes a proof of eq. (5.1). □
Theorem 10 ( [23]). For the Poincar´e homology sphere with p = (2, 3, 5), we have
e
2πi
N
(
e
2πi
N − 1
)
τN
(
Σ(2 , 3, 5)
)
= 1 + 1
2 e− 1
60N πi ·~Φ (1,1,1)
p (1/N) (5.5)
Proof. A proof is same with Theorem 9 and was done in Ref. 23. A difference follows from a fact
that the odd periodic function satisﬁes
(z6 − z−6) (z10 − z−10) (z15 − z−15)
z30 − z−30 = 1
z + z +
∞∑
n=0
χ(1,1,1)
60 (n) zn (5.6)
in place of eq. (5.4). □
Combining these theorems with a nearly modular property of t he Eichler integral (4.17), we
obtain an asymptotic expansion of the quantum invariant in N → ∞.
15
Corollary 11. For a case of 1
p1
+ 1
p2
+ 1
p3
< 1 we have
e
2πi
N ( φ(p1,p2,p3)
4 − 1
2 )
(
e
2πi
N − 1
)
τN
(
Σ( p1, p2, p3)
)
≃
√
N
i
∑
ℓ1,ℓ2,ℓ3
Sℓ1,ℓ2,ℓ3
1,1,1 e
− 1
2 πiP N
(
1+∑
j
ℓj
pj
) 2
+ 1
2
∞∑
k=0
L(−2 k, χ(1,1,1)
2P )
k!
( π i
2 P N
) k
(5.7)
Here the sum in the ﬁrst term runs over γ(p1, p2, p3) distinct triples, i.e., the triple (ℓ1, ℓ2, ℓ3)
satisﬁes a constraint (4.10) under a symmetry (4.11), and we have used eq. (4.16).
We give some examples below:
• Σ(2 , 3, 7):
The function Φ (ℓ1,ℓ2,ℓ3)(τ ) spans a D(2, 3, 7) = 3 -dimensional space, and the inde-
pendent functions are given for (ℓ1, ℓ2, ℓ3) = (1 , 1, 1), (1, 1, 2), and (1, 1, 3). For these
triples we have from eq. (4.3) that~Φ (ℓ1,ℓ2,ℓ3)(N) = 0 , −2 e
25
84 πiN , −2 e− 47
84 πiN, which shows
CS(A) = − 25
168 , 47
168. Indeed we see that (ℓ1, ℓ2, ℓ3) = (1 , 1, 1) does not satisfy a condi-
tion (4.10). This fact shows γ(2, 3, 7) = 2 , and is consistent with eq. (4.13) as we have
λC
(
Σ(2 , 3, 7)
)
= −1. As a result, we have
e− 2πi
N
167
168
(
e
2πi
N − 1
)
τN
(
Σ(2 , 3, 7)
)
≃
√
N
i
2√
7
(
− sin
( 2 π
7
)
e− 25
84 πiN − sin
( 3 π
7
)
e
47
84 πiN
)
+ 1
2
∞∑
k=0
L(−2 k, χ(1,1,1)
84 )
k!
( π i
84 N
) k
where
n mod 84 1 13 29 41 43 55 71 83 others
χ(1,1,1)
84 (n) 1 −1 −1 1 −1 1 1 −1 0
• Σ(3 , 4, 5):
There are D(3, 4, 5) = 6 independent functions Φ (ℓ1,ℓ2,ℓ3)(τ ); (ℓ1, ℓ2, ℓ3) =
(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 1), and (1, 2, 2). For these triples, we have the
Eichler integral ~Φ (ℓ1,ℓ2,ℓ3)(N) = 0 , 0, −2 e− 119
120 πiN , −2 e
49
120 πiN , −2 e
1
30 πiN , −2 e− 11
30 πiN re-
spectively, which indicates CS(A) = 119
240 , − 49
240 , − 1
60 , 11
60. We can check that two triples,
(1, 1, 1) and (1, 1, 2), do not satisfy a constraint (4.10). We thus have γ(3, 4, 5) = 4 , which
16
is consistent with λC
(
Σ(3 , 4, 5)
)
= −2. Then we obtain
e− 2πi
N
71
240
(
e
2πi
N − 1
)
τN
(
Σ(3 , 4, 5)
)
≃
√
N
i
1√
5
(
− sin
( π
5
)
e
119
120 πiN + sin
( 2 π
5
)
e− 49
120 πiN
−
√
2 sin
( 2 π
5
)
e− 1
30 πiN +
√
2 sin
( π
5
)
e
11
30 πiN
)
+ 1
2
∞∑
k=0
L(−2 k, χ(1,1,1)
120 )
k!
( π i
120 N
) k
where
n mod 120 13 37 43 53 67 77 83 107 others
χ(1,1,1)
120 (n) 1 −1 −1 −1 1 1 1 −1 0
The Poincar´ e homology sphere Σ(2 , 3, 5) was studied in Ref. 23. In this case we have a
D(2, 3, 5) = 2 dimensional representation of the modular group P SL(2; Z), and independent
functions~Φ (ℓ1,ℓ2,ℓ3)(τ ) can be deﬁned for (ℓ1, ℓ2, ℓ3) = (1 , 1, 1) and (1, 1, 2). We can check that
both triples fulﬁll a condition (4.10), and that we have ~Φ (ℓ1,ℓ2,ℓ3)(N) = −2 e
1
60 πiN , −2 e
49
60 πiN,
which indicates that the Chern–Simons invariant is given by − 1
120 and − 49
120 respectively. As we
have φ(2, 3, 5) = 181
30 , we obtain an exact asymptotic expansion as follows;
Corollary 12 ( [23]).
e
2πi
N
121
120
(
e
2πi
N − 1
)
τN
(
Σ(2 , 3, 5)
)
≃
√
N
i
2√
5
(
sin
( π
5
)
e− 1
60 πiN + sin
( 2 π
5
)
e− 49
60 πiN
)
+ e
πi
60N + 1
2
∞∑
k=0
L(−2 k, χ(1,1,1)
60 )
k!
( π i
60 N
) k
(5.8)
where
n mod 60 1 11 19 29 31 41 49 59 others
χ(1,1,1)
60 (n) −1 −1 −1 −1 1 1 1 1 0
