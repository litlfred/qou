---
doc_id: 1-s20-s002212362200012x-main
doc_title: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-003-12-an-application-concentration-of-negatively-de
section_title: "An application: concentration of negatively dependent random variables"
section_number: 1.2
pages: 4-6
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
toc_source: outline
doc_brief: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube — V Article history: Received 17 December 2020 Accepted 13 January 2022 Available online"
---
For a sequence of Bernoulli variables X1, ..., Xn, there are several notions of negative-
dependence between those variables (see e.g., [4,17,16,5]), some of which are known or 
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
5
conjectured to imply concentration of Lipschitz functions. Some notable ﬁrst steps to-
wards a theory unifying those notions appear in the work of Pemantle [13], to which we 
also refer for a review of these notions.
The simplest notion of negative dependence is pairwise negative-correlations, hence 
the condition that E[XiXj] ≤EXiEXj for all i ̸= j. This condition, however, is too weak 
to imply any nontrivial concentration bounds. For example if (X1, ..., Xn) are distributed 
as a uniformly chosen row of the n ×n Hadamard matrix, then these variables are pairwise 
independent, and therefore have nonpositive correlations. However, if A is the subset of 
combinations given by the ﬁrst n/2 rows and ϕ(x) is the Hamming distance of x to the 
set A, then Var[ϕ(X1, . . . , Xn)] = Ω 

n2
.
A stronger notion which appears in the literature is negative-association: We say 
that X1, ..., Xn are negatively associated if for all I, J ⊂[n] with I ∩J = ∅and every 
monotone functions f : {0, 1}I →R and g : {0, 1}J →R one has E[f(XI)g(XJ)] ≤
Ef(XI)Eg(XJ). It was conjectured by E. Mossel that Lipschitz functions admit sub-
Gaussian concentration with respect to such measures.
To the best of our knowledge, there are two results in this direction in the literature: 
It was shown by Peres and Pemantle that sub-Gaussian concentration of Lipschitz func-
tions hold for measures satisfying the strong-Rayleigh property ([14]), which amounts to 
stability of the generating polynomial of the measure. More recently, Garbe and Vondrak 
([9]) showed that concentration is implied by the negative-regression property. We also 
refer to their paper for a discussion of related bounds and questions.
Here, we consider the following notion of negative dependence suggested by Wagner 
[18].
Deﬁnition 8. (Rayleigh measures). We say that X1, . . . , Xn satisfy the Rayleigh property 
if for every θ ∈Rn and for all i, j ∈[n], we have
E
	
XiXje

i θiXi
E
	
e

i θiXi
≤E
	
Xie

i θiXi
E
	
Xje

i θiXi
.
(6)
In other words, X1, ..., Xn satisﬁes the Rayleigh property if the correlations between all 
pairs are negative even after reweighing the measure by an exponential tilt. Equivalently, 
this is the largest family that exhibits pairwise negative correlations and is closed under 
the operation of applying a magnetic ﬁeld.
A corollary of our main theorem is the following concentration bound for measures 
with the Rayleigh property as well as a lower bound for the entropy.
Corollary 9. If X1, ..., Xn satisfy the Rayleigh property, then,
1. For any 1-Hamming-Lipschitz function ϕ, we have
Var[ϕ(X1, . . . , Xn)] ≤Cn2−c,
for universal constants C, c > 0.
6
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
2. One has,

i∈[n]
H(Xi) ≤2H(X1, ..., Xn).
Proof of Corollary 9. Let ν be the law of (2X1 −1, . . . , 2Xn −1). Observe that the 
condition (6) is equivalent to
∂i∂jL[ν](θ) ≤0,
∀i̸ = j.
Therefore, Rayleigh property is equivalent to the fact that ∇2L[ν](x) has non-positive 
oﬀ-diagonal entries for all x ∈Rn. Let u ∈Rn. Deﬁne u = u+ + u−where u+ ∈
[0, ∞)n and u−∈(−∞, 0)n. Recall that ∇2L[ν](x) is positive semi-deﬁnite and that 

∇2L[ν](x)

i,i ≤1 for all i (see the identity (8) below), so by convexity,

u, ∇2L[ν](x)u

≤2

u+, ∇2L[ν](x)u+

+ 2

u−, ∇2L[ν](x)u−

≤2⟨u+, diag

∇2L[ν](x)

u+⟩+ 2⟨u−, diag

∇2L[ν](x)

u−⟩
= 2⟨u, diag

∇2L[ν](x)

u⟩.
Thus, ν satisﬁes both (2) and (5) with β = 2. An application of Theorem 2 implies the 
ﬁrst part, and an application of Theorem 6, the second.

It was pointed out to us by P. Nuti and J. Vondrak the Rayleigh property (by the the-
orem of Feder and Mihail) implies the negative regression property ([9]), which in turn 
implies the stochastic covering property (see [14]) in the special case that the measure 
ν is homogeneous (namely when 
i Xi is deterministic). Therefore, in the homoge-
neous case, one attains a stronger version the above corollary (which gives sub-Gaussian 
concentration). In fact, the more recent paper [1] gives spectral gap in this case (see 
discussion below). However, all of the above seem to rely on homogeneity in a crucial 
way.
