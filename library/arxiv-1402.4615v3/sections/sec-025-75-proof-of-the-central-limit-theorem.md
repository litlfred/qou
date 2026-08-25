---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-025-75-proof-of-the-central-limit-theorem
section_title: "Proof of the central limit theorem"
section_number: 7.5
pages: 50-51
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
result of this section:
Proof of Theorem 1.2. Let ˜Ξ d = (Ξ 2, . . . ,Ξ d+1). In order to show that
( Ch(k)
√
knk/2
)
k=2,3,...
d− →(Ξ k)k=2,3,...
as n → ∞, it is enough to show, that for all d ∈ N and for any smooth function h
on Rd, with all derivatives bounded, one has, as n → ∞:
⏐
⏐
⏐E(α)
n h( ˜Wd) − Eh(˜Ξ d)
⏐
⏐
⏐ → 0.
Fix a positive integer d and a function h : Rd → R as above. Let Σ =
(E(α)
n )( ˜Wd ˜W t
d). As h has its ﬁrst derivative bounded, one has
⏐
⏐
⏐E
(
h(˜Ξ d) − h(Σ1/2 ˜Ξ d)
) ⏐
⏐
⏐ ≤ |h|1 · d ‖Id −Σ1/2‖ · E(‖˜Ξ d‖).
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 51
But |h|1 and E(α)
n (‖˜Ξ d‖) are ﬁxed ﬁnite numbers, while ‖Id −Σ1/2‖ is O(n−1/2)
by Proposition 7.6. Hence,
(41)
⏐
⏐
⏐E
(
h(˜Ξ d) − h(Σ1/2 ˜Ξ d)
) ⏐
⏐
⏐ = O(n−1/2).
By Corollary 7.5 and Proposition 7.6 we know, that the pair ( ˜Wd, ˜W ∗
d ) satisﬁes
all hypotheses of Theorem 7.1. Using this theorem, we get
⏐
⏐
⏐E(α)
n h( ˜Wd) − Eh(Σ ˜Ξ d)
⏐
⏐
⏐ ≤ |h|2
A
4 + |h|3
B
12 ,
where
A =
∑
2≤i,j≤d+1
n
i
√
Var(α)
n
(
(E(α)
n ) ˜Wd(Wi − W ∗
i )(Wj − W ∗
j )
)
and
B =
∑
2≤i,j,k≤d+1
n
i E(α)
n |(W ∗
i − Wi)(W ∗
j − Wj)(W ∗
k − Wk)|.
Propositions 7.8 and 7.10 imply that
⏐
⏐
⏐E(α)
n h( ˜Wd) − Eh(Σ1/2 ˜Ξ d)
⏐
⏐
⏐ = O(n−1/2).
Together with equation (41), it ﬁnishes the proof. □
