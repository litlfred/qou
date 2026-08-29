---
doc_id: arxiv-math-9906120v3
doc_title: "Discrete orthogonal polynomial ensembles and the Plancherel measure By Kurt Johansson"
section_id: sec-004-31-the-limit-of-the-charlier-ensemble-the-charli
section_title: "The limit of the Charlier ensemble. The Charlier ensemble is deﬁned"
section_number: 3.1
pages: 12-14
source_pdf: 9906120v3.pdf
source_sha256: 436982ef45e940bd
doc_brief: "Discrete orthogonal polynomial ensembles and the Plancherel measure By Kurt Johansson — We consider discrete orthogonal polynomial ensembles which are discrete analogues of the orthogonal polynomial"
---
by (1.16). It can be obtained as a limit of the Meixner ensemble (1.14) by
taking q = α/MN and letting N →∞with M ﬁxed. In this limit
(1 −q)MN
M−1
Y
j=0
(N −M)!
j!(N −M + j)!
M
Y
i=1
λi + N −i
λi + M −i

qλi
(3.1)
→


M−1
Y
j=1
1
j!

WM(λ)
M
Y
i=1
 α
M
λi e−α/M

,
so we obtain (1.16). In light of Theorem 1.1 we see that it is reasonable to
expect that the Poissonized Plancherel measure should be the limit of the
Charlier ensemble as M →∞. The interpretation of the Charlier ensemble
in connection with random words, Proposition 1.5, also supports this since a
random word in the limit M →∞is like a permutation (no letter is used
twice), see also [TW3]. We will give an analytical proof of Theorem 1.2 that
does not use the RSK-correspondence. We start with the following simple but
important lemma.
Lemma 3.1. If M ≥ℓ(λ), then
(3.2)
VM(λ)WM(λ) = Vℓ(λ)(λ)Wℓ(λ)(λ).
Proof. We may assume that M > ℓ(λ). Note that, by deﬁnition, λi = 0
if i > ℓ(λ). Hence,
VM(λ) = Vℓ(λ)(λ)
ℓ(λ)
Y
i=1
M
Y
j=ℓ(λ)+1
(λi + j −i)
Y
ℓ(λ)<i<j≤M
(j −i)
= Vℓ(λ)(λ)
ℓ(λ)
Y
i=1
(λi + M −i)!
(λi + ℓ(λ) −i)!
Y
ℓ(λ)<i<j≤M
(j −i).
Thus in order to prove (3.2) we must show that
Y
ℓ(λ)<i<j≤M
(j −i) =
M
Y
i=ℓ(λ)+1
(λi + M −i)!,
but this is immediate since λi = 0 if i > ℓ(λ).
Proof of Theorem 1.2. It follows from the deﬁnition (1.12) of g(λ) that
(3.3)
|g(λ)| ≤c(g)max(ℓ(λ),L) ≤c(g)ℓ(λ)+L.
ENSEMBLES AND THE PLANCHEREL MEASURE
271
Let PCh,M,N be deﬁned by (1.21). Then,
Eα
Ch,M[g] =
X
λ∈ΩM
g(λ)


M−1
Y
j=1
1
j!

VM(λ)2WM(λ)
M
Y
j=1
 α
M
λj e−α/M

(3.4)
=
∞
X
N=0
e−α αN
N!
X
λ∈Ω(N)
M
g(λ)PCh,M,N[{λ}].
Thus, by (3.3) and the fact that ℓ(λ) ≤N if λ ∈Ω(N)
M ,
(3.5)

X
λ∈Ω(N)
M
g(λ)PCh,M,N[{λ}]

 ≤c(g)L+N,
since PCh,M,N is a probability measure on Ω(N)
M . Given ε > 0 we can choose K
so large that
(3.6)

∞
X
N=K+1
e−α αN
N! c(g)L+N

 ≤ε.
Consequently,
(3.7)

Eα
Ch,M[g] −
K
X
N=0
e−α αN
N!
X
λ∈Ω(N)
M
g(λ)PCh,M,N[{λ}]

 ≤ε.
If M ≥K ≥N ≥ℓ(λ), λ ∈Ω(N)
M , we can identify Ω(N)
M
with P(N) and use
(3.2) to write
(3.8)
X
λ∈Ω(N)
M
g(λ)PCh,M,N[{λ}]
=
X
λ∈Ω(N)
M
g(λ)N!Vℓ(λ)(λ)2Wℓ(λ)(λ)2
M
Y
j=1
(λj + M −j)!
Mλj
M−1
Y
j=1
1
j!
=
X
λ∈P(N)
g(λ)PPlan,N[{λ}]
ℓ(λ)
Y
j=1
(λj + M −j)!
Mλj(M −j)! ,
where the last equality is a straightforward computation using the fact that
λj = 0 if j > ℓ(λ). Now,
ℓ(λ)
Y
j=1
(λj + M −j)!
Mλj(M −j)! =
ℓ(λ)
Y
j=1

1 −j −1
M

. . .

1 −j −ℓ(λ)
M

272
KURT JOHANSSON
which goes to 1 as M →∞for a ﬁxed λ. Since the sum in (3.7) is, for a ﬁxed
K, a sum over ﬁnitely many λ, we obtain
(3.9)
lim
M→∞
K
X
N=0
e−α αN
N!
X
λ∈Ω(N)
M
g(λ)PCh,M,N[{λ}]
=
K
X
N=0
e−α αN
N!
X
λ∈P(N)
g(λ)PPlan,N[{λ}].
Using (3.6) and the fact that PPlan,N is a probability measure on P(N), we
obtain
(3.10)

Eα
Plan[g] −
K
X
N=0
e−α αN
N!
X
λ∈Ω(N)
M
g(λ)PPlan,N[{λ}]

 ≤ε.
The theorem now follows from (3.7), (3.9) and (3.10).
