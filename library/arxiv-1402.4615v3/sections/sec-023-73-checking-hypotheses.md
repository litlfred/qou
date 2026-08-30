---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-023-73-checking-hypotheses
section_title: "Checking hypotheses"
section_number: 7.3
pages: 43-45
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
Wk = n−k/2√
k
−1
Ch(k)
and the random vector
˜Wd = (W2, . . . , Wd+1)
on the probability space of Young diagrams of size n endowed with Jack mea-
sure. Let λ be a random partition distributed according to Jack measure , and λ∗
(λ′, respectively) be obtained from λ by applying the Markov chain M (α) (L(α),
respectively). By a small abuse of notations, set ˜Wd := ˜Wd(λ), ˜W ∗
d := ˜Wd(λ∗)
and ˜W ′
d := ˜Wd(λ′). We shall prove now, that for anyd ∈ N, the pair ( ˜Wd, ˜W ∗
d ) of
random vectors satisﬁes conditions of Theorem 7.1.
First, note that E(α)
n ( ˜Wd) = 0 from equation (8).
We should now verify the hypothesis involving (E(α)
n ) ˜Wd(W ∗
k ). Let us begin
with two technical known statements about Jack polynomials.
Lemma 7.3. (1) [Mac95, Page 382]
∑
ρ⊢n
θµ(ρ)θν (ρ)
j(α)
ρ
= δµ,ν
zµαℓ(µ) ;
(2) [Sta89, Page 107]
θµ((n − 1, 1)) = αn−ℓ(µ)n!
zµ
(α(n − 1) + 1)m1(µ) − n
αn(n − 1) .
Recall that (E(α)
n ) ˜Wd denotes the conditional expectation given ˜Wd. Similarly,
we denote by (E(α)
n )λ the conditional expectation given λ.
Proposition 7.4. Let d ∈ N and let 2 ≤ k ≤ d + 1. Then, one has
(E(α)
n )
˜Wd(W ∗
k ) = ( E(α)
n )λ(W ∗
k ) =
(
1 − k
n
)
Wk;
(E(α)
n )
˜Wd(W ′
k) = ( E(α)
n )λ(W ′
k) =
(
1 − k(α(n − 1) + 1)
αn(n − 1)
)
Wk.
Proof. By deﬁnition,
(E(α)
n )λ(W ∗
k ) =
∑
λ∗
M (λ, λ∗)W ∗
k (λ∗).
44 M. DOŁ ˛ EGA AND V . FÉRAY
From [Ful04, Proposition 6.2.], we have that(θµ(λ))λ⊢n is an eigenvector of M (α)
with eigenvalue
dµ := 1 + α(n − 1)
α(n − 1) + 1
( zµ
αn−ℓ(µ)n! θµ((n − 1, 1)) − 1
)
.
Using Lemma 7.3-(2), this eigenvalue can be simpliﬁed to (su rprisingly, this was
not noticed by Fulman)
dµ = (α(n − 1) + 1)m1(µ)
n(α(n − 1) + 1) = m1(µ)
n .
As (W ∗
k (λ))λ⊢n is a multiple of (θµ(λ))λ⊢n, it is also an eigenvector of M (α),
with the same eigenvalue. Hence,
(E(α)
n )λ(W ∗
k )(λ) = d(k,1n−k)W ∗
k (λ).
For µ = ( k, 1n−k), we have d(k,1n−k) = 1 − k
n, which ﬁnishes the proof of the
second equality of the ﬁrst statement.
In particular, we see that (E(α)
n )λ(W ∗
k ) depends only on Wk and hence on ˜Wd.
As, conversely, ˜Wd is determined by λ, one has
(E(α)
n )
˜Wd(W ∗
k ) = ( E(α)
n )λ(W ∗
k ).
The statement for W ′
k follows easily from the one forW ⋆
k , using Proposition 7.2.
□
Corollary 7.5. Let d ∈ N. Then
(E(α)
n )
˜Wd( ˜W ∗
d − ˜Wd) = −Λ ˜Wd,
with Λ i,j = δi,j i+1
n . In particular, with the notation of Theorem 7.1,
λ(i) = n
i + 1 .
Proof. It is a straightforward consequence of Proposition 7.4. □
Consider now Σ = E(α)
n ( ˜Wd ˜W t
d) as in the statement of Theorem 7.1. This
matrix is symmetric by deﬁnition, but one has to check that it is positive deﬁnite.
For a matrix A, let ‖A‖ := max i,j |Ai,j| denotes the supremum norm on matri-
ces.
Proposition 7.6. There exists a constantAd,α which depends only on d and α such
that for any n ≥ Ad,α the matrix Σ is positive deﬁnite. Moreover,
‖Σ1/2 − Id‖ = O(n−1/2).
Proof. Strictly from the deﬁnition we have that
(24) Σi,j = E(α)
n
( 1
√i + 1√j + 1n(i+j+2)/2 Ch(i+1) Ch(j+1)
)
= 1√
i + 1√j + 1n(i+j+2)/2
∑
λ
g(i+1),(j+1);λE(α)
n (Chλ).
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 45
Since
EP(α)
n
(Chµ) =
{
(n)k if µ = 1 k for some k ≤ n,
0 otherwise,
we have that
Σi,j = 1√i + 1√j + 1n(i+j+2)/2
∑
l
g(i+1),(j+1);(1l)(n)l,
and using items (1), (2) and (3) of Lemma 5.6, we have, that
Σi,j = δi,j + O(n−1/2).
In other terms,
‖Σ − Id‖ = O(n−1/2).
As the set of positive deﬁnite matrix is an open set of the spac e of symmetric
matrices, this implies that Σ is positive deﬁnite for n big enough.
Besides, the application A ↦→
√
A is differentiable on this open set, which im-
plies the bound ‖Σ1/2 − Id‖ = O(n−1/2). □
