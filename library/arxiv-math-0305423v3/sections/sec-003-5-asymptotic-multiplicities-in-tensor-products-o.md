---
doc_id: arxiv-math-0305423v3
doc_title: "Stein’s Method and Plancherel Measure of the Symmetric Group"
section_id: sec-003-5-asymptotic-multiplicities-in-tensor-products-o
section_title: "Asymptotic multiplicities in tensor products of representations"
section_number: 5
pages: 14-18
source_pdf: 0305423v3.pdf
source_sha256: e4554f9084ba4935
doc_brief: "Stein’s Method and Plancherel Measure of the Symmetric Group — We initiate a Stein’s method approach to the study of the Plancherel measure of the symmetric group."
---
representations
This section gives an intruiging method for understanding s ome asymp-
totic aspects of the decomposition of tensor products of cer tain representa-
tions of the symmetric group. A recent paper which investiga tes this topic
from the viewpoint of free probability theory is [Bi]. Howev er the methods
and results are completely diﬀerent from those presented her e. The main
new idea of this section is to use spectral theory of Markov ch ains. This is
further developed in [Fu1] (connections with card shuﬄing, generalization
to other groups) and in [Fu2] (generalizations to arbitrary representations
of ﬁnite groups).
Throughout this section X is the set of partitions of size n, endowed with
Plancherel measure π. We consider the space of real valued functions ℓ2(π)
with the norm
||f ||2 =
( ∑
x
|f (x)|2π(x)
) 1/ 2
.
15
If J(x,y ) is the transition rule for a Markov chain, the associated Ma rkov
operator (also denoted by J) on ℓ2(π) is given by Jf (x) = ∑
yJ(x,y )f (y).
Let J r(x,y ) = J r
x(y) denote the chance that the Markov chain started at x
is at y after r steps.
If the Markov chain with transition rule J(x,y ) is reversible with respect
to π (i.e. π(x)J(x,y ) = π(y)J(y,x ) for all x,y ), then the operator J is self
adjoint with real eigenvalues
−1 ≤βmin =β|X|−1 ≤ · · · ≤ β1 ≤β0 = 1.
Let ψi (i = 0, · · ·, |X| − 1) be an orthonormal basis of eigenfunctions such
that Jψ i =βiψi and ψ0 ≡ 1. Deﬁne β =max{|βmin|,β 1}.
The total variation distance between the measures J r
x and π is deﬁned
by ||J r
x −π||T V = 1
2
∑
y |J r
x(y) −π(y)|. (The application to representation
theory does not require total variation distance but this co ncept is useful
for understanding the Markov chain J; see Theorem 5.3).
The following lemma is well-known; for a proof see [DSa]. Par t 1 is
essentially Jensen’s inequality.
Lemma 5.1. (1) 2 ||J r
x −π||T V ≤ || J r
x
π − 1||2.
(2) J r(x,y ) =∑ |X|−1
i=0 βr
iψi(x)ψi(y)π(y).
(3) || J r
x
π − 1||2
2 =∑ |X|−1
i=1 β2r
i |ψi(x)|2 ≤ 1−π (x)
π (x) β2r.
Next we specify a class of Markov chains to which we will apply Lemma
5.1. Recall from Proposition 2.1 that there is a natural tran sition mechanism
for moving up one step in the Young lattice or down one step in t he Young
lattice. For 1 ≤k ≤n, let J(k) be the Markov chain which from a partition
of n ﬁrst moves down k steps in the Young lattice (one at a time according
to part 2 of Proposition 2.1), and then moves back up k steps in the Young
lattice (one at a time according to part 1 of Proposition 2.1) . Proposition
5.2 ﬁnds the eigenvalues and eigenfunctions for the corresp onding operators
J(k). The word Mult. stands for multiplicity.
Proposition 5.2. The eigenvalues and eigenfunctions of the operator J(k)
on partitions of size n are indexed by conjugacy classes C of the symmetric
group on n symbols.
(1) Letting n1(C) denote the number of ﬁxed points of the class C, the
eigenvalue parameterized by C is (n1(C))(n1(C)−1)···(n1(C)−k+1)
n(n−1)···(n−k+1) .
(2) The orthonormal basis of eigenfunctions ψC is deﬁned by ψC(λ) =
|C|
1
2 χ λ (C)
dim(λ ) .
Proof. From Proposition 2.1, the chance that the Markov chain J(k) moves
from λ to µ is easily seen to be
dim(µ)
(n)(n − 1) · · · (n −k + 1)dim(λ)
∑
τ
|τ |=n− k
dim(λ/τ )dim(µ/τ ).
16
From the branching rules of irreducible representations of the symmetric
group [Sa], this is
dim(µ)
dim(λ)
Mult. µ in IndSn
Sn− k
ResSn
Sn− k
(λ)
n(n − 1) · · · (n −k + 1) .
Now observe that the ψC(λ) = |C|
1
2 χ λ (C)
dim(λ ) is an eigenfunction with the
asserted eigenvalue because
|C|
1
2
(n) · · · (n −k + 1)dim(λ)
∑
µ
χµ (C) ·Mult. µ in IndSn
Sn− k
ResSn
Sn− k
(λ)
= |C|
1
2
n(n − 1) · · · (n −k + 1)dim(λ)Ind Sn
Sn− k
ResSn
Sn− k
(λ)[C]
= (n1(C))(n1(C) − 1) · · · (n1(C) −k + 1)
n(n − 1) · · · (n −k + 1)
|C|
1
2χλ (C)
dim(λ) .
The last equality is Lemma 3.5. The fact that ψC are orthonormal follows
from Lemma 3.1. Being linearly independent, they are a basis forℓ2(π) since
the number of conjugacy classes of Sn is equal to the number of partitions
of n. □
Remarks:
(1) A similar argument shows that the chain which moves up k steps
(one at a time) and then down k steps (one at a time) has the ψC as
an orthonormal basis with eigenvalues (n1(C)+1)(n1(C)+2)···(n1(C)+k)
(n+1)(n+2)···(n+k) .
The results in the remainder of this section could be applied to that
Markov chain as well.
(2) It is remarkable that the set of eigenvalues of the Markov chain
J(1) is precisely the set of eigenvalues of the top to random sh uﬄe
(see [DFP] for background on top to random shuﬄes). This is no t
coincidence; the paper [Fu1] explains this and more general facts in
terms of the Robinson-Schensted-Knuth correspondence.
Theorem 5.3 studies the convergence properties of the Marko v chains
J(k). Throughout all logs are taken base e, as usual.
Theorem 5.3. Let (n) denote the partition which consists of one part of size
n (corresponding to the trivial representation of Sn). Let β = (n−k)(n−k−1)
(n)(n−1) .
Then for n ≥ 3, 1 ≤k <n,
2||J(k)r
(n) −π||T V ≤



∑
λ
|λ |=n
|J(k)r((n),λ )
π(λ) − 1|2π(λ)



1/ 2
≤
√
n! (β)r.
17
Thus for r> nlog(n)+2c
2log( 1
β ) ,
||J(k)r
(n) −π||T V ≤ (2π)
1
4
2 e−c.
Proof. From parts 1 and 3 of Lemma 5.1, to prove the ﬁrst assertion it i s
enough to show that for the chain J(k),β = (n−k)(n−k−1)
(n)(n−1) and that 1−π ((n))
π ((n)) ≤
n!. The value of β follows from Proposition 5.2 (note that a permutation
on n symbols cannot have exactly n-1 ﬁxed points) and the ineq uality holds
since π((n)) = 1
n! . This proves the ﬁrst assertion.
The second assertion follows from the Stirling formula boun d [Fe]
n! ≤
√
2πe−n+ 1
12n +(n+ 1
2 )log(n),
for then
√
n! (β)r ≤ (2π)
1
4erlog(β )− n
2 + 1
24n + 1
2 (n+ 1
2 )log(n)
≤ (2π)
1
4erlog(β )+ nlog(n)
2 .
□
Now we give the application to representation theory. We rem ind the
reader that Ind Sn
Sn− 1(1) is the deﬁning representation of the symmetric group
(i.e. the n dimensional permutation representation on the s ymbols 1, · · ·,n ),
and hence corresponds to the case k = 1 below. As usual, π(λ) = dim(λ )2
n!
denotes the Plancherel measure of the symmetric group, and t he word Mult.
is short for multiplicity. We let ⊗r denote the operation of taking the r-fold
tensor product of a representation of a symmetric group Sn (yielding the
sum of various irreducible representations of Sn).
Theorem 5.4. Letβ = (n−k)(n−k−1)
(n)(n−1) . Then for n ≥ 3, 1 ≤k<n ,
∑
λ
|λ |=n
|
n![Mult. λ in ⊗rInd Sn
Sn− k
(1)]
dim(λ) ((n) · · ·(n −k + 1))r − 1|2π(λ) ≤n! (β)2r.
Forr> nlog(n)+c
2log( 1
β ) , this is at most
√
2πe−c.
Proof. Let (n) be the partition which consists of one row of size n, and let
n1(C) denote the number of ﬁxed points of a conjugacy class C. We now
consider the quantity ||
J(k)r
(n)
π − 1||2
2. One on hand, by part 2 of Lemma 5.1,
18
we know that
J(k)r
(n)(λ)
= dim(λ)
∑
C
( (n1(C)) · · · (n1(C) −k + 1)
n · · ·(n −k + 1)
) r |C|χλ (C)
n!
= dim(λ)
(n · · ·(n −k + 1))r
1
n!
∑
g∈Sn
(n1(g) · · · (n1(g) −k + 1))rχλ (g).
By Lemmas 3.2 and 3.5, and the fact that the character of a tens or product
is the product of the characters, this is precisely
dim(λ)
(n(n − 1) · · · (n −k + 1))r [Mult. λ in⊗rInd Sn
Sn− k
(1)].
Thus
||
J(k)r
(n)
π − 1||2
2 =
∑
λ
|λ |=n
|
n![Mult. λ in⊗rInd Sn
Sn− k
(1)]
dim(λ) ((n) · · ·(n −k + 1))r − 1|2π(λ).
The result now follows by the upper bound on ||
J(k)r
(n)
π − 1||2
2 in Theorem
5.3. □
