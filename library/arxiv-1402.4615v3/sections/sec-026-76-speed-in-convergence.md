---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-026-76-speed-in-convergence
section_title: "Speed in convergence"
section_number: 7.6
pages: 51-53
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
estimate for ⏐
⏐
⏐E(α)
n h( ˜Wd) − Eh(˜Ξ d)
⏐
⏐
⏐
for non-smooth test functions h. In particular, we shall consider functions h in the
set H of indicator functions of convex sets. We have the followingresult, which is
stronger than Theorem 1.3.
Theorem 7.11. For any integer d ≥ 2, we have
sup
h∈H
|E(α)
n h( ˜Wd) − E h(˜Ξ d)| = O
(
n−1/4)
.
Proof. Fix an integer d ≥ 2 and consider the exchangeable pair ( ˜Wd, ˜W ⋆
d ) deﬁned
as in the previous sections.
As shown in Section 7.3, this exchangeable pair fulﬁlls the condition of [RR09,
Theorem 2.1]. Besides, as mentioned in [RR09, Section 3], th e set H of functions
fulﬁlls conditions (C1), (C2) and (C3) (with a = 2
√
d) from this paper. There-
fore, one can apply [RR09, Corollary 3.1] and we ﬁnd that ther e exists a constant
ζ = ζ(d) such that
(42) sup
h∈H
|E(α)
n h( ˜Wd) − E h(˜Ξ d)| ≤ ζ 2
(A′ log(1/T ′)
2 + B′
2
√
T ′ + 2
√
dT ′
)
,
52 M. DOŁ ˛ EGA AND V . FÉRAY
where we deﬁne
ˆλ(i) :=
d∑
m=1
|(Σ−1/2Λ −1Σ1/2)m,i|,
A′ :=
∑
i,j
ˆλ(i)
√
∑
k,l
Σ−1/2
i,k Σ−1/2
j,ℓ Var(E(α)
n ) ˜Wd(W ′
k − Wk)(W ′
ℓ − Wℓ),
B′ :=
∑
i,j,k
ˆλ(i)E(α)
n
⏐
⏐
⏐
⏐
⏐
∑
r,s,t
Σ−1/2
i,r Σ−1/2
j,s Σ−1/2
k,t (W ′
r − Wr)(W ′
s − Ws)(W ′
t − Wt)
⏐
⏐
⏐
⏐
⏐,
T ′ := 1
4d
(
A′
2 +
√
B′
√
d + (A′)2
4
) 2
.
Comparing this with the statement in [RR09], note that in our case, there is no
remaining matrix R, and hence C ′ = 0 . Besides, for the set H considered here
(indicator functions of convex subsets of Rd), one can choose a = 2
√
d.
We shall now describe the asymptotic behaviour of the quanti ties above. Note
that all sums appearing above have ﬁxed number of summands since the summation
index set is always the set of integers less or equal to d.
Recall that, in our setting, Λ −1 is the diagonal matrix (n/(i + 1) · δi,j). Be-
sides Σ−1/2 (well-deﬁned for n big enough) is a bounded matrix (Proposition 7.6).
Hence for any i ≤ d,
ˆλ(i) = O(n).
Consider now A′. It was proven in Section 7.4 (Lemma 7.7 and equation (38)) that,
for any k and ℓ,
| Var(E(α)
n )
˜Wd(W ′
k − Wk)(W ′
ℓ − Wℓ)| = O(n−3).
Together with the bound on ˆλ(i) and the fact that Σ−1/2 is bounded, this implies
A′ = O(n−1/2).
Consider now B′. We have proved that the bound (39) holds in expectation, that is
E(α)
n
⏐
⏐(W ′
r − Wr)(W ′
s − Ws)(W ′
t − Wt)
⏐
⏐ ≤ O(n−3/2).
As before, the bound above on ˆλ(i) and the fact that Σ−1/2 is bounded implies
B′ = O(n−1/2).
Combining the bounds forA′ and B′, we get T ′ = O(n−1/2). Strictly from the def-
inition of T ′, we also get T ′ ≥ B′, which implies that B′
2
√
T ′ ≤
√
B′ = O(n−1/4).
Plugging all these estimates in equation (42), we get the desired result. □
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 53
