---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-021-62-shape-convergence
section_title: "Shape convergence"
section_number: 6.2
pages: 40-41
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
polynomial functions at D1/√n
(
Aα(λ(n))
)
converge towards the evaluation at Ω .
Ivanov and Olshanski has established that, if one can prove that the support of these
renormalized Young diagrams lies in some compact, this would imply the uniform
convergence, that is Theorem 1.1.
The following technical lemma, proved by Fulman [Ful04, Lem ma 6.6] will
allow us to conclude:
Lemma 6.3. Suppose that α > 0. Then
(1)
P(α)
n
(
λ1 ≥ 2e
√
n
α
)
≤ αn24−e
√ n
α ,
(2)
P(α)
n (λ′
1 ≥ 2e√
nα) ≤ n2
α 4−e√nα.
In particular
lim
n→∞
P(α)
n
([
− λ′
1
√n ; λ1√n
]
⊆
[
−2e√α, 2e√α
])
= 1.
End of proof of Theorem 1.1. It follows from Proposition 6.2 and Lemma 6.3 by
the same argument as the one given in [IO02, Theorem 5.5]. □
7. J ACK MEASURE : CENTRAL LIMIT THEOREM FOR JACK CHARACTERS
In this section we prove the central limit theorem for Jack ch aracters (Theorem
1.2) and the bound of the speed of convergence in this theorem (Theorem 1.3).
7.1. Multivariate Stein’s method. As explained in introduction, our main tool
will be a multivariate analog of the so-called Stein’s method due to Reinert and
Röllin [RR09]. For any discrete random variables W, W ∗ with values in Rd,
we say that the pair (W, W ∗) is exchangeable if for any w1, w2 ∈ Rd one has
P(W = w1, W ∗ = w2) = P(W = w2, W ∗ = w1). Let EW (·) denotes the condi-
tional expected value givenW . The theorem of Reinert and Röllin is the following
[RR09, Theorem 2.1]:
Theorem 7.1 (multivariate Stein’s theorem). Let (W, W ∗) be an exchangeable
pair of Rd-valued random variables such that E(W ) = 0 and E(W W t) = Σ,
where Σ ∈ Md×d(R) is symmetric and positive deﬁnite matrix. Suppose that
EW (W ∗ − W ) = −Λ W , where Λ ∈ Md×d(R) is invertible. Then, if Z is a
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 41
d-dimensional standard normal distribution, we have for eve ry three times differ-
entiable function h : Rd → R,
(21)
⏐
⏐
⏐Eh(W ) − Eh(Σ1/2Z)
⏐
⏐
⏐ ≤ |h|2
4 A + |h|3
12 B,
where, using the notation λ(i) :=∑
1≤m≤d |(Λ −1)m,i|,
|h|n = sup
i1,...,in
‖
‖
‖
‖
∂n
∂xi1 · · ·∂xin
h
‖
‖
‖
‖ ,
A =
∑
1≤i,j≤d
λ(i)
√
VarEW (W ∗
i − Wi)(W ∗
j − Wj),
B =
∑
1≤i,j,k≤d
λ(i)E|(W ∗
i − Wi)(W ∗
j − Wj)(W ∗
k − Wk)|.
Let d be a positive integer. For k ≥ 2, as in the statement of Theorem 1.2, we
deﬁne the following function of Young diagrams of size n:
Wk = n−k/2√
k θ(α)
(k,1n−k) = n−k/2√
k
−1
Ch(k) .
It can be seen as a random variable on the probability space of Young diagrams of
size n endowed with Jack measure. We also consider the correspondi ng random
vector
˜Wd = (W2, . . . , Wd+1).
Theorem 1.2 states that ˜Wd converges in distribution towards a vector of indepen-
dent Gaussian random variables. Therefore we would like to a pply the theorem
above to this d-uplet of random variables. In the next sections, we shall co ntruct
