---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-022-72-an-exchangeable-pair
section_title: "An exchangeable pair"
section_number: 7.2
pages: 41-43
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
7.2. An exchangeable pair. The ﬁrst step consists in building a d-tuple ˜W ∗
d , such
that ( ˜Wd, ˜W ∗
d ) is an exchangeable pair. The construction that we will describe here
is due to Fulman [Ful04].
His construction uses Markov chains, so let us begin by ﬁxing some terminol-
ogy. Let X be a ﬁnite set. A Markov chain M on X is the data of transition
probability M (x, y) indexed by pairs of elements of X with
M (x, y) ≥ 0 and
∑
y∈X
M (x, y) = 1 .
If x is a random element of X distributed with probability P, then, applying once
the Markov chain M, we obtain by deﬁnition a random element y of X, deﬁned on
the same probability space as x, whose conditional distribution is given by:
P (y = y0|x = x0) = M (x0, y0).
Using the notation above, the Markov chain M is termed reversible with respect
to P if the distribution of (x, y) is the same as the distribution of (y, x), or equiva-
lently, for any x0, y0 in X,
P({x0})M (x0, y0) = P({y0})M (y0, x0).
42 M. DOŁ ˛ EGA AND V . FÉRAY
Reversible Markov chains can be used to construct exchangeable pairs as follows.
Let M be a reversible Markov chain on a ﬁnite set X with respect to a probability
measure P. Consider also a Rd-valued function W on X. We consider a random
element x distributed with respect to P and y obtained by applying the Markov
chain M to P. Then, directly from the deﬁnition, one sees that (W (x), W (y)) is
exchangeable.
So, to construct an exchangeable pair for ˜Wd, it is enough to construct a re-
versible Markov chain with respect to Jack measure. We prese nt now Fulman’s
construction of such a Markov chain.
Let τ ⊢ n − 1 and λ ⊢ n. If τ is not contained in λ (as Young diagrams), then
deﬁne φ(α)(λ/τ ) = 0 . Otherwise, denote by λ/τ the box which is in λ and not
in τ. Let Cλ/τ (Rλ/τ , respectively) be the column (row, respectively) of λ that
contains λ/τ. We deﬁne
φ(α)(λ/τ ) =
∏
□ ∈Cλ/τ \Rλ/τ
(αaλ(□ ) + ℓλ(□ ) + 1)(αaτ (□ ) + ℓτ (□ ) + α)
(αaλ(□ ) + ℓλ(□ ) + α)(αaτ (□ ) + ℓτ (□ ) + 1) .
Let
c(α)
λ =
∏
□ ∈λ
(αa(□ ) + ℓ(□ ) + 1)
and
(c′
λ)(α) =
∏
□ ∈λ
(αa(□ ) + ℓ(□ ) + α).
We recall that j(α)
λ = c(α)
λ (c′
λ)(α). For λ, ρ ⊢ n we deﬁne two functions:
(22) M (α)(λ, ρ) = (c′
λ)(α)
nαc(α)
ρ
∑
τ ⊢n−1
φ(α)(λ/τ )φ(α)(ρ/τ )c(α)
τ
(c′
τ )(α)
and
(23) L(α)(λ, ρ) = 1
αnn!j(α)
ρ
∑
µ⊢n
(zµ)2α2ℓ(µ)θµ(λ)θµ(ρ)θµ((n − 1, 1)).
As explained by Fulman [Ful04], both M (α) and L(α) are deﬁned to be a defor-
mation of a certain Markov chain which is reversible with res pect to Plancherel
measure. Roughly speaking, this Markov chain remove one box from a given
Young diagram with certain probability and add another box w ith some proba-
bility to obtain a new Young diagram of the same size as the one from which we
started. Fulman [Ful04] proved the following:
Proposition 7.2. [Ful04, Section 4]
(1) If ρ ⁄= λ then
L(α)(λ, ρ) = α(n − 1) + 1
α(n − 1) M (α)(λ, ρ);
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 43
(2) Let λ ⊢ n. Then
∑
ρ⊢n
L(α)(λ, ρ) =
∑
ρ⊢n
M (α)(λ, ρ) = 1;
(3) L(α) (hence M (α) as well) is reversible with respect to Jack measure.
For more details about this construction (and in particular , the intuition behind
it), we refer to Fulman [Ful04].
