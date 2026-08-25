---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-016-72-generalized-p-adic-dimensions
section_title: "Generalized p-adic dimensions"
section_number: 7.2
pages: 32-35
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
eration of the generalized quantum dimension Dq(λ) and we relate it to the complex di-
mension of the MF-spherical irreducible KF-representation V F
λ for non-Archimedean local
ﬁelds F (see Section 4). Denote δk,l (k,l ∈ Z) for the Kronecker delta function: it is one if
k =l and zero otherwise.
Lemma 7.3. The functions vi(m;q), w±
j,k(m;q) ( see Lemma 7.1 ) for m ∈ Z+ are regular
at q = 0 . If we write vi(m) = vi(m; 0) and w±
j,k(m) = w±
j,k(m; 0) for their constant terms,
then vi(0) = w±
j,k(0) = 1 and
vi(m) =
(1 −atn−i
1 −btn−i
)
ti−n(
1 − (1 −δm,1)abtn−i)
,
w+
j,k(m) =
(1 −abt2n−j−k+1−δm,1
1 −abt2n−j−k−1
)
t,
w−
j,k(m) = 1 −tk−j+1
1 −tk−j
for m ≥ 1.
Proof. As an example, we compute vi(m) form ∈ Z≥1 (the other computations are similar).
To compute vi(1) we rewrite vi(1;q) as
vi(1;q) =
(1 −qabt2(n−i)
1 −qtn−i
)( 1 −atn−i
1 −btn−i
)( q −abtn−i
q −abt2(n−i)
)
,
which yields
vi(1) = vi(1; 0) =
(1 −atn−i
1 −btn−i
)
ti−n.
To compute vi(m) for m ≥ 2 we write vi(m;q) as
vi(m;q) =
(
(1 −q2m−1abt2(n−i))
(
qatn−i;q
)
m−1
(
qabtn−i;q
)
m−2(
qtn−i;q
)
m
(
qbtn−i;q
)
m−1
)
×
((1 −atn−i)(1 −abtn−i)
(1 −btn−i)
)( q −abtn−i
q −abt2(n−i)
)
,
which yields
vi(m) = vi(m; 0) =
(1 −atn−i
1 −btn−i
)
ti−n(1 −abtn−i), m ≥ 2.
□
Proposition 7.4. Let λ ∈ Λ n. The generalized quantum dimension Dq(λ) ( see (2.4)) is
regular at q = 0. Writing D0(λ) = D0(λ;a,b ;t) for Dq(λ;a,b ;t)|q=0, we have
D0(λ) = a−|λ|t−2(ρ,λ)
n∏
i=1
vi(λi)
∏
1≤j<k≤n
w+
j,k(λj +λk)w−
j,k(λj −λk), λ ∈ Λ n.
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 33
Proof. This is immediate from Lemma 7.1 and the previous lemma. □
Example 7.5. Forn = 1, so that Λ 1 = Z+, we have D0(0) = 1 and
D0(λ) = a−λ
(1 −a
1 −b
) (
1 − (1 −δλ,1)ab
)
, λ ≥ 1.
In contrast to the quantum case, the explicit expression for D0(λ) = D0(λ;a,b ;t) from
Proposition 7.4 simpliﬁes for all partitions λ ∈ Λ n as follows.
Theorem 7.6. Forλ ∈ Λ n we have
(7.4) D0(λ) = a−|λ|t−2(ρ,λ)
[ n
∂λ′
]
t
(
atn−λ′
1;t
)
λ′
1
(
abt2n−λ′
1−λ′
2;t
)
λ′
1+λ′
2
(
btn−λ′
1,abt n−λ′
1−1;t
)
λ′
1
(1 −abt2n−2λ′
1−1
1 −abt2n−1
)
.
As remarked already in Subsection 4.3, the generalized p-adic dimension formula (7.4)
combined with its representation theoretic interpretation (4.14) f rom [23] leads to the
explicit dimension formulas (4.13) for the irreducible MF-spherical KF-representationsV F
λ
(λ ∈ Λ n).
Corollary 7.7. Forr = 0,...,n we have
(7.5) D0(ωr) =
(
tn+1−r,at n−r,abt 2n−r;t
)
r(
t,bt n−r,abt n−r−1;t
)
r
(1 −abt2n−2r−1
1 −abt2n−1
)
a−rtr(r+1−2n).
Proof. Follows either by specializing Theorem 7.6 to λ =ωr, or by taking q = 0 in (7.1). □
We next proceed to prove Theorem 7.6, which is based on the expres sion for D0(λ) as
given in Proposition 7.4. We divide the proof into several elementary le mmas. Since the
theorem is obviously correct for λ = 0, we ﬁx for the proof a nonzero partition λ ∈ Λ n.
Lemma 7.8.
n∏
i=1
vi(λi) = t
1
2 λ′
1(λ′
1+1)−nλ′
1
(
atn−λ′
1;t
)
λ′
1
(
abtn−λ′
2;t
)
λ′
2
(
btn−λ′
1;t
)
λ′
1
.
Proof. Using the explicit expression for vi (see Lemma 7.3), we have
n∏
i=1
vi(λi) =
λ′
2∏
i=1
(1 −atn−i
1 −btn−i
)
ti−n(
1 −abtn−i)
λ′
1∏
i=λ′
2+1
(1 −atn−i
1 −btn−i
)
ti−n
=
λ′
1∏
i=1
(1 −atn−i1 −btn−i
)
ti−n
λ′
2∏
i=1
(
1 −abtn−i)
=t
1
2 λ′
1(λ′
1+1)−nλ′
1
(
atn−λ′
1;t
)
λ′
1
(
abtn−λ′
2;t
)
λ′
2
(
btn−λ′
1;t
)
λ′
1
,
as desired. □
34 URI ONN AND JASPER V. STOKMAN
Lemma 7.9. ∏
1≤j<k≤n
w−
j,k(λj −λk) =
[ n
∂λ′
]
t
.
Proof. Since w−
j,k(0) = 1 and w−
j,k(m) = 1−tk−j+1
1−tk−j for m ⁄= 0 (see Lemma 7.3), the term
w−
j,k(λj −λk) contributes to the product only if λj ⁄=λk. Hence
∏
1≤j<k≤n
w−
j,k(λj −λk) = A/B,
with
A =
∏
1≤j<k≤n
1 −tk−j+1
1 −tk−j =
n∏
l=1
(1 −tl+1)n−l
(1 −tl)n−l = [n]t!
B =
∏
1≤j<k≤n
λj =λk
1 −tk−j+1
1 −tk−j =
∏
l≥0
∏
1≤j<k≤λ′
l−λ′
l+1
1 −tk−j+1
1 −tk−j =
∏
l≥0
[λ′
l −λ′
l+1]t!,
as desired. □
Lemma 7.10.
∏
1≤j<k≤n
w+
j,k(λj+λk) = t
1
2 λ′
1(λ′
1−1)+λ′
1(n−λ′
1) (abt2n−λ′
1;t)λ′
1−1
(abt2n−2λ′
1;t)λ′
1−1
(abt2n−2λ′
1−1;t)λ′
1(abt2n−λ′
1−λ′
2;t)λ′
2
(abtn−λ′
1−1;t)λ′
1(abtn−λ′
2;t)λ′
2
.
Proof. The term w+
j,k(m) has three possible values depending on m being 0, 1 or ≥ 2 (see
Lemma 7.3). We are hence led to consider the following sets
X1 = {(j,k ) | 1 ≤j <k ≤n, λj +λk = 1} = {(j,k ) |λ′
2<j ≤λ′
1 <k ≤n}
X2 = {(j,k ) | 1 ≤j <k ≤n, λj +λk ≥ 2} =X a
2 ⊔X b
2,
where the disjoint subsets X a
2 and X b
2 are given by
X a
2 = {(j,k ) | 1 ≤j <k ≤λ′
1}, X b
2 = {(j,k ) | 1 ≤j ≤λ′
2, λ′
1 <k ≤n}.
We then have ∏
1≤j<k≤n
w+
j,k(λj +λk) = Π( X1)Π(X a
2 )Π(X b
2)
where we write Π( X) = ∏
(j,k)∈Xw+
j,k(λj +λk) for a subset X ⊆ { (j,k ) | 1 ≤ j < k≤ n}.
We have
Π(X1) = t(n−λ′
1)(λ′
1−λ′
2)
λ′
1∏
j=λ′
2+1
n∏
k=λ′
1+1
( 1 −abt2n−j−k
1 −abt2n−j−k−1
)
=t(n−λ′
1)(λ′
1−λ′
2)
λ′
1∏
j=λ′
2+1
(1 −abt2n−j−λ′
1−1
1 −abtn−j−1
)
=t(n−λ′
1)(λ′
1−λ′
2)
(
abt2n−2λ′
1−1;t
)
λ′
1−λ′
2
(
abtn−λ′
1−1;t
)
λ′
1−λ′
2
.
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 35
Using the same notations and simpliﬁcation arguments as in the proof of Proposition 7.2,
we have
Π(X a
2 ) = t
1
2 λ′
1(λ′
1−1)eλ′
1(abt2n)eλ′
1(abt2n−1) = t
1
2 λ′
1(λ′
1−1)
(
abt2n−λ′
1;t
)
λ′
1−1
(
abt2n−2λ′
1;t
)
λ′
1−1
.
By a similar computation as for Π( X1), we ﬁnally have
Π(X b
2) = t(n−λ′
1)λ′
2
(
abt2n−λ′
1−λ′
2,abt 2n−λ′
1−λ′
2−1;t
)
λ′
2
(
abtn−λ′
2,abt n−λ′
2−1;t
)
λ′
2
.
Combining these expressions leads to the desired result. □
We can now use Proposition 7.4, Lemma 7.8, Lemma 7.9 and Lemma 7.10 to obtain
an explicit expression for the generalized p-adic dimension D0(λ). After straightforward
simpliﬁcations, we arrive at the desired expression (7.4) for D0(λ).
