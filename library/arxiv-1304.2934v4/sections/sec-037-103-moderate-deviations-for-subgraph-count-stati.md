---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-037-103-moderate-deviations-for-subgraph-count-stati
section_title: "Moderate deviations for subgraph count statistics"
section_number: 10.3
pages: 85-91
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
10.3.1. End of the proof of Theorem 10.1. We would like to apply Proposition 5.2 to the
sequence Sn = X(n)
γ − E[X(n)
γ ] with αn = n2 and βn = nk−2. Let us check that Sn indeed
fulﬁlls the hypothesis.
(1) The uniform bound |κ(r)(Sn)|≤ (Cr)rαn(βn)r, where C does not depend on n,
corresponds to Proposition 10.3; we may even choose C = 2k4.
(2) We also have to check the speed of convergence:
κ(2)(Sn) = σ2 αn (βn)2 (1 + O(α−1/2
n )) ; κ(3)(Sn) = L αn (βn)3 (1 + O(α−1/4
n )). (51)
But these estimates follow directly from the bound above for r = 2, 3 and the
fact that κ(r)(Sn) is always a polynomial in n — see Corollary 10.6.
Finally, the mod-Gaussian convergence follows from the observations in Section 5. The
normality zone result follows from Proposition 4.14 and we can apply Proposition 5.2
to get the moderate deviation statement. This ends the proof of Theorem 10.1. □
Remark 10.7. Using Theorem 9.11, we could obtain a bound for joint cumulants of sub-
graph count statistics. Hence, it would be possible to derive mod-Gaussian conver-
gence and moderate deviation results for linear combinations of subgraph count statis-
tics. However, since we do not have a speciﬁc motivation for that and since the state-
ment for a single subgraph count statistics is already quite technical, we have chosen
not to present such a result.
10.3.2. Computing σ2 and L. The proof above does not give an explicit value for σ2 and
L. Yet, these values can be obtained by analyzing the graphs G that contribute to the
highest degree term of κ(2) and κ(3).
Lemma 10.8. Let γ be a graph with k vertices and h edges. Then the positive number σ
appearing in Theorem 10.1 is given by
σ2 = 2h2p2h−1(1− p).
Proof. By deﬁnition, σ2 is the coefﬁcient of n2k−2 in κ(2)(X(n)
γ ). As seen in Equation (50),
the quantity κ(2)(X(n)
γ ) can be written as
∑
G
κ(G)NG,
where the sum runs over some graphs G with vertex set V⊔ V. However, we have
seen that κ(G) = 0 unless the 2-contraction H2 of G is connected — see Inequality (47)
— and on the other hand, NG is a polynomial in n, whose degree is the number cG of
connected component of G.
As we are interested in the coefﬁcient of n2k−2, we should consider only graphs G with
at least 2k− 2 connected components and a connected 2-contraction. These graphs are
represented on Figure 13.
86 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
FIGURE 13. Graphs involved in the computation of the main term in κ(2)(X(n)
γ ).
Namely, we have to choose a pair of vertices on each side and connect each of these
vertices to one vertex of the other pair (there are 2 ways to make this connection, if
both pairs are ﬁxed). A quick computation shows that, for such a graph G,
κ(G) =
{
p2h−1(1− p) if both pairs correspond to an edge of γ;
0 else.
Finally there are 2h2 graphs with a non-zero contribution to the coefﬁcient of n2k−2 in
κ(2)(X(n)
γ ). For each of these graphs, NG = n(n− 1)··· (n− 2k + 3) = n2k−2(1 + o(1)).
Therefore, the coefﬁcient of n2k−2 in κ(2)(X(n)
γ ) is 2h2p2h−1(1− p), as claimed. □
The number L can be computed by the same method.
Lemma 10.9. Let γ be a graph with k vertices and h edges. Then the number L appearing in
Theorem 10.1 is given by
L = 12h3(h− 1)p3h−2(1− p)2 + 4h3p3h−2(1− p)(1− 2p).
Proof. Here, we have to consider graphs G on vertex set V⊔ V⊔ V with at least 3k− 4
connected components and with a connected 2-contraction. These graphs are of two
kinds, see Figure 14.
FIGURE 14. Graphs involved in the computation of the main term in κ(3)(X(n)
γ ).
In the ﬁrst case (left-hand side picture), an edge on the left can possibly have an
extremity in common with an edge on the right. In this case, one has to add an edge
to complete the triangle (indeed, all graphs G are disjoint unions of cliques). But this
cannot happen for both edges on the left simultaneously, otherwise the graph belong
to the second family.
MOD-φ CONVERGENCE, I 87
The following is now easy to check. There are 12 h3(h− 1) graphs of the ﬁrst kind
with a non-zero cumulant κ(G) — 3 choices for which copy of V plays the central role,
h3(h− 1) for pairs of vertices and 4 ways to link the chosen vertices — and, for these
graphs, the corresponding cumulant is always κ(G) = p3h−2(1− p)2. Similarly, there
are 4h3 graphs of the second kind with a non-zero cumulant κ(G). For these graphs,
κ(G) = p3h−2(1− p)(1− 2p). In both cases, NG = n3k−4(1 + o(1)). This completes the
proof. □
Example 10.10. Denote Tn the number of triangles in a random Erdös-Rényi graph
Γ(n, p) (each triangle being counted 6 times). According to the previous Lemmas, the
parameters σ2 and L are respectively
σ2 = 18 p5 (1− p) and L = 108 p7 (1− p)(7− 8p).
Moreover, E[Tn] = n↓3 p3 = n3 p3− 3 n2 p3 + O(n). So,
P
[
Tn≥ n3p3 + n2(v− 3p3)
]
≃
√
9p5(1− p)
π v2 exp
(
− v2
36 p5(1− p) + (7− 8p) v3
324 n p8(1− p)2
)
for 1≪ v≪ n1/2.
10.3.3. Case of a non-constant sequence pn. Proposition 10.3 still holds when pn is a non-
constant sequence (the particularly interesting case is pn→ 0). Applying Theorem 9.8
instead of Theorem 9.7, one gets a slightly sharper bound
⏐⏐⏐κ(r)(X(n)
γ )
⏐⏐⏐≤ Cr rr−2 nr(k−2)+2 (pn)h.
But, unlike in the case pn = p constant, this bound is not always optimal for a ﬁxed
r (even up to a multiplicative constant) . Indeed, [JŁR00, Lemma 6.17] gives stronger
bounds than ours (see also Example 6.19 in [JŁR00]). Finding a uniform bound for
cumulants, whose dependence in r is of order (Cr)r (so that we have mod-Gaussian
convergence), and which is optimal for ﬁxed r is an open problem.
Yet, we can still give a lower bound on the normality zone. Let αn and βn be deﬁned
as follows:
αn = n2 (pn)4h−3 (1− pn)3;
βn = nk−2 (pn)1−h (1− pn)−1.
With these choices, one has
⏐⏐⏐κ(r)(X(n)
γ )
⏐⏐⏐≤ (Cr)r αn(βn)r.
88 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
Notice that κ(2)(X(n)
γ ) and κ(3)(X(n)
γ ) are polynomials in n and pn, of degree 2h and 3h
in pn. Thanks to this observation, if pn→ 0, then
κ(2)(X(n)
γ ) = 2h2 n2k−2 (pn)2h−1(1− pn) + O(n2k−3)
= 2h2 αn (βn)2
(
1 + O
( 1
n (pn)2h−1
))
;
κ(3)(X(n)
γ ) = h3 n3k−4 (pn)3h−2(1− pn) (12(h− 1)(1− pn) + 4(1− 2pn)) + O(n3k−5)
= αn (βn)3
(
O((pn)2h−2) + O
( 1
n (pn)h
))
.
From the discussion of Section 5.1, we conclude that we have mod-Gaussian conver-
gence if (αn)1/3 = o(n (pn)2h−1) and n (pn)h→ +∞. The ﬁrst condition is equivalent
to n (pn)2h→ +∞, so, if
n− 1
2h≪ pn≪ 1,
then Conditions (25) are met, and one has a mod-Gaussian convergence of
X(n)
γ − E[X(n)
γ ]
nk− 4
3 (pn)
h
3
with parameters tn = 2h2 n
2
3 (pn)
4h
3−1 (1− pn) and limit ψ(z) = 1. Therefore, in this
setting,
X(n)
γ − E[X(n)
γ ]
h nk−1
√
2(pn)2h−1(1− pn)
has normality zone at least O(n
1
3 (pn)
2h
3− 1
2 ). Note that we only have a lower bound on
the normality zone, since the limit in the mod-Gaussian convergence is trivial.
Remark 10.11. Unfortunately the convergence speed hypotheses (51) are not satisﬁed,
so one cannot apply Proposition 5.2.
11. R ANDOM CHARACTER VALUES FROM CENTRAL MEASURES ON PARTITIONS
Our Theorem 9.7 can also be used to study certain models of random integer parti-
tions. Recall that if G is a ﬁnite group and if τ is a function G→ C with τ(eG) = 1 and
τ(gh) = τ(hg) (such a function is called atrace on G), then τ can be expanded uniquely
as a linear combination of normalized irreducible characters:
τ = ∑
λ∈ˆG
Pτ[λ]ˆχλ,
where ˆG is the (ﬁnite) set of isomorphism classes of irreducible representations of G
and ˆχλ the normalized ( i.e. divided by the dimension of the space) character of the
irreducible representation associated to λ.
Deﬁnition 11.1. The map λ↦→ Pτ[λ] is called the spectral measure of the trace τ. It takes
non-negative values if and only if, for every family (g1, . . . ,gn) of elements of G, the matrix
(τ(gi(gj)−1))1≤i,j≤n is Hermitian non-negative deﬁnite. Then, the spectral measure is a prob-
ability measure on ˆG.
MOD-φ CONVERGENCE, I 89
When G = S(n) is the symmetric group of order n, the irreducible representations
are indexed by integer partitions of size n, that is non-increasing sequences of positive
integers λ = ( λ1, . . . ,λ𝓁) with ∑𝓁
i=1 λi = n. In the following we denote P(n) = ˆS(n)
the set of integer partitions of size n, and 𝓁(λ) = 𝓁 the length of a partition. We shall
also consider the inﬁnite symmetric group S(∞) = ⋃
n≥1 S(n), which is the group of
permutations of the set of natural numbers that have a ﬁnite support.
Deﬁnition 11.2. A central measure on partitions is a family (Pτ,n)n∈N of spectral measures
on the sets P(n) that come from the same trace of the inﬁnite symmetric groupS(∞). In other
words (Pτ,n)n∈N is a central measure if there exists a trace τ : S(∞)→ C such that
τ|S(n) = ∑
λ∈P(n)
Pτ,n[λ]ˆχλ.
Example 11.3. The regular trace τ(σ) = 1 σ=id corresponds to the Plancherel measures
of the symmetric groups, given by the formula Pn[λ] = ( dim Vλ)2/n!, where Vλ is the
S(n)-irreducible module of label λ. They have been extensively studied in connection
with Ulam’s problem of the longest increasing subsequence and with random matrix
theory, see e.g. [BDJ99, BOO00, Oko00, IO02].
A central measure (Pτ,n)n∈N is non-negative if and only if (τ(ρiρ−1
j ))1≤i,j≤n is Her-
mitian non-negative deﬁnite for any ﬁnite family of permutations ρ1, . . . ,ρn. The set
of non-negative central measures, i.e., coherent systems of probability measures on
partitions has been identiﬁed in [Tho64] and later studied in [KV81]. Call extremal a
non-negative trace on S(∞) that is not a positive linear combination of non-negative
traces. Then, extremal central measures are indexed by the inﬁnite-dimensional Thoma
simplex
Ω =
{
ω = ( α, β) =
(
(α1≥ α2≥···≥ 0), (β1≥ β2≥···≥ 0)
)⏐⏐⏐⏐
∞
∑
i=1
αi + βi≤ 1
}
.
The trace on the inﬁnite symmetric group corresponding to a parameter ω is given by
τω(σ) = ∏
c∈C(σ)
p|c|(ω) with p1(ω) = 1, pk≥2(ω) =
∞
∑
i=1
(αi)k + (−1)k−1(βi)k, (52)
C(σ) denoting the set of cycles of σ. Kerov and Vershik have shown that if ω∈ Ω and
ρ∈ S(∞) are ﬁxed, then the random character valueˆχλ(ρ) with λ chosen according to
the central measure Pω,n converges in probability towards the trace τω(ρ). Informally,
central measures on partitions and extremal traces of S(∞) are concentrated. More
recently, it was shown by Féray and Méliot that this concentration is Gaussian, see
[FM12, Mél12]. The aim of this section is to use the techniques of Sections 9-10 in order
to prove the following:
Theorem 11.4. Fix a parameter ω∈ Ω, and denote ρ a k-cycle in S(∞) (for k≥ 2). Assume
p2k−1(ω)− (pk(ω))2⁄= 0. Denote then X (n)
ρ the random character valueˆχλ(ρ), where:
• λ∈ P(n) is picked randomly according to the central measure Pω,n,
90 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
• andˆχλ denotes the normalized irreducible character indexed by λ of S(n), that is
ˆχλ(ρ) = tr Πλ(ρ)
dim Vλ with (Vλ, Πλ) irreducible representation of S(n).
The rescaled random variable n2/3[
X(n)
(k)− pk(ω)
]
converges in the mod-Gaussian sense with
parameters tn = n1/3 σ2 and limiting function ψ(z) = exp(L z3
6 ), where
σ2 = k2(
p2k−1(ω)− pk(ω)2)
;
L = k3(
(3k− 2) p3k−2(ω)− (6k− 3) p2k−1(ω) pk(ω) + (3k− 1) pk(ω)3)
.
As in Section 10, the mod-Gaussian convergence is proved by bounds on cumulants
of type (24). Furthermore, the hypothesis (26) on the third and second cumulant are
ensured by the polynomiality of joint cumulants — Lemma 11.9. Therefore, we can
apply Propositions 5.2 and 4.14.
Corollary 11.5. Let X(n)
k = X(n)
(k) be the random character value on a k-cycle as deﬁned above.
Then n1/2 (X(n)
k − pk(ω)) satisﬁes a central limit theorem with normality zone o(n1/6). More-
over, at the edge of this normality zone and at a slightly larger scale, the deviation probabilities
are given by: for any sequence x of positive numbers bounded away from0 with xn = o
(
n1/12)
,
one has
P
[
n1/2(X(n)
k − pk(ω))≥ n1/6σ2xn
]
= e− (xn)2 n1/3 σ2
2
xn n1/6σ
√
2π
e
L(xn)3
6 (1 + o(1)).
P
[
n1/2(X(n)
k − pk(ω))≤− n1/6σ2xn
]
= e− (xn)2 n1/3 σ2
2
xn n1/6σ
√
2π
e
−L(xn)3
6 (1 + o(1)).
where σ2 and L as in Theorem 11.4.
Remark 11.6. The condition σ2 > 0 is satisﬁed as soon as the sequence α⊔ β associated
to the Thoma parameter ω contains two different non-zero coordinates. Indeed, for
any summable non-increasing non-negative sequence γ = ( γ1, γ2, . . .) with γi > γi+1
for some i, one has
(
∞
∑
i=1
(γi)k−ε
)(
∞
∑
i=1
(γi)k+ε
)
≥
(
∞
∑
i=1
(γi)k
)2
with equality if and only if ε = 0. Indeed, the derivative of the function of ε on the
left-hand side is
∑
i<j
(
γiγj
)k log
(
γi
γj
)((
γi
γj
)ε
−
( γj
γi
)ε)
.
Applying the result to γ = α⊔ β and ε = k− 1, we obtain on the left-hand side
(
∞
∑
i=1
γi
)(
∞
∑
i=1
(γi)2k−1
)
=
(
∞
∑
i=1
αi + βi
)
p2k−1(ω)≤ p2k−1(ω)
MOD-φ CONVERGENCE, I 91
and on the right-hand side
(
∞
∑
i=1
(γi)k
)2
≥
(
∞
∑
i=1
(αi)k + (−1)k−1(βi)k
)2
= ( pk(ω))2.
This proof shows that the condition σ2 > 0 is also satisﬁed if 0 < ∑∞
i=1 αi + βi < 1.
This Section is organized as follows. In Section 11.1, we present the necessary ma-
terial. In Section 11.2, we then prove bounds on these cumulants similar to those of
Proposition 10.3, and we compute the limits of the second and third cumulants. This
will allow us to use in Section 11.3 the framework of Section 5.2 in order to prove the
results stated above. We shall also detail some consequences of these results for the
shapes of the random partitions λ∼ Pn,ω viewed as Young diagrams, in the spirit of
[FM12, Mél12].
