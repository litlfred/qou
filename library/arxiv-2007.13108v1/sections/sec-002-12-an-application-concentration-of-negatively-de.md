---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-002-12-an-application-concentration-of-negatively-de
section_title: "An application: Concentration of negatively dependent random variables"
section_number: 1.2
pages: 3-5
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
ables
For a sequence of Bernoulli variablesX1, ..., X n, there are several notions of negative-dependence
between those variables (see e.g., [4, 16, 15, 5]), some of wh ich are known or conjectured to
imply concentration of Lipschitz functions. Some notable ﬁ rst steps towards a theory unifying
those notions appear in the work of Permantle [12], to which w e also refer for a review of these
notions.
The simplest notion of negative dependence is pairwise negative-correlations, hence the
condition that E[XiXj] ≤ EXiEXj for all i ⁄= j. This condition, however, is too weak to
imply any nontrivial concentration bounds. For example if (X1, ..., X n) are distributed as a
3
uniformly chosen row of the n × n Hadamard matrix, then these variables are pairwise inde-
pendent, and therefore have nonpositive correlations. How ever, if A is the subset of combi-
nations given by the ﬁrst n/ 2 rows and ϕ (x) is the Hamming distance of x to the set A, then
Var[ϕ (X1, . . . , X n)] = Ω ( n2).
A stronger notion which appears in the literature is negative-association: We say that
X1, ..., X n are negatively associated if for all I, J ⊂ [n] with I ∩ J = ∅ and every monotone
functions f : {0, 1}I → R and g : {0, 1}J → R one has E[f (XI)g(XJ)] ≤ Ef (XI)Eg(XJ ). It
was conjectured by E. Mossel that Lipschitz functions admit sub-Gaussian concentration with
respect to such measures.
To the best of our knowledge, there are two results in this dir ection in the literature: It
was shown by Peres and Pemantle that sub-Gaussian concentra tion of Lipschitz functions hold
for measures satisfying the strong-Rayleigh property ([13]), which amounts to stability of the
generating polynomial of the measure. More recently, Garbe and V ondrak ([9]) showed that
concentration is implied by the negative-regression property. We also refer to their paper for a
discussion of related bounds and questions.
Here, we consider the following notion of negative dependen ce suggested by Wagner [17].
Deﬁnition 7. (Rayleigh measures). We say that X1, . . . , X n satisfy the Rayleigh property if for
every θ ∈ Rn and for all i, j ∈ [n], we have
E
[
XiXje
∑
i θiXi
]
E
[
e
∑
i θiXi
]
≤ E
[
Xie
∑
i θiXi
]
E
[
Xje
∑
i θiXi
]
. (6)
In other words, X1, ..., X n satisﬁes the Rayleigh property if the correlations between all
pairs are negative even after reweighing the measure by an ex ponential tilt. Equivalently, this is
the largest family that exhibits pairwise negative correla tions and is closed under the operation
of applying a magnetic ﬁeld.
A corollary of our main theorem is the following concentrati on bound for measures with the
Rayleigh property as well a lower bound for the entropy.
Corollary 8. If X1, ..., X n satisfy the Rayleigh property, then,
1. F or any 1-Hamming-Lipschitz function ϕ , we have
Var[ϕ (X1, . . . , X n)] ≤ Cn 2−c,
for universal constants C, c > 0.
2. One has, ∑
i∈[n]
H(Xi) ≤ 2H(X1, ..., X n).
Proof of corollary 8. Let ν be the law of (2X1 − 1, . . . , 2Xn − 1). Observe that the condition
(6) is equivalent to
∂i∂jL[ν](θ) ≤ 0, ∀i ⁄= j.
Therefore, Rayleigh property is equivalent to the fact that ∇2L[ν](x) has non-positive off-
diagonal entries for all x ∈ Rn. Let u ∈ Rn. Deﬁne u = u+ + u− where u+ ∈ Rn
+ and
4
u− ∈ Rn
−. Recall that ∇2L[ν](x) is positive semi-deﬁnite and that (∇2L[ν](x))i,i ≤ 1 for all i
(see the identity (8) below), so by convexity,
⟨
u, ∇2L[ν](x)u
⟩
≤ 2
⟨
u+, ∇2L[ν](x)u+
⟩
+ 2
⟨
u−, ∇2L[ν](x)u−
⟩
≤ 2⟨u+, diag
(
∇2L[ν](x)
)
u+⟩ + 2⟨u−, diag
(
∇2L[ν](x)
)
u−⟩
= 2⟨u, diag
(
∇2L[ν](x)
)
u⟩.
Thus, ν satisﬁes both (2) and (5) with β = 2. An application of Theorem 2 implies the ﬁrst part,
and an application of Theorem 5, the second.
It was pointed out to us by P . Nuti and J. V ondrak, that in the sp ecial case that the mea-
sure ν is homogeneous (namely when ∑
i Xi is deterministic), the Rayleigh property implies
both the so-called stochastic covering property (see [13]) and the negative regression property
([9]), which in turn (using either of the above references) i mplies a stronger version the above
corollary (which gives sub-Gaussian concentration). In fa ct, the more recent paper [1] gives
spectral gap in this case (see discussion below). However, a ll of the above seem to rely on
homogeneouity in a crucial way.
