---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-020-a2-correlation-functions-of-determinantal-proces
section_title: "Correlation functions of determinantal processes"
section_number: A.2
pages: 38-39
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
X ∈Conf(X)0, let ρ(X) be the probability that a random conﬁguration
contains X, that is,
ρ(X) = Prob ({Y ∈Conf(X)0, X ⊂Y }) .
We call ρ(X) the correlation functions. The fundamental fact about
determinantal point processes is that their correlation functions have
again a determinantal form.
Proposition A.6. Let L be as above and set K = L(1 + L)−1. Then
ρ(X) = det KX.
Proof. We follow the argument in [10], Exercise 5.4.7. Let f(x) be an
arbitrary function on X such that f(x) = 1 for all but a ﬁnite number
of x’s. Form the probability generating functional:
Φ(f) =
X
X
Y
x∈X
f(x) · Prob(X).
Then, viewing f as a diagonal matrix, we get
Φ(f) =
P
X det(fL)
det(1 + L) = det(1 + fL)
det(1 + L) ,
where the last equality is justiﬁed by Proposition A.4 applied to the
operator fL.
Now, set g(x) = f(x) −1, so that g(x) = 0 for all but ﬁnitely many
x’s. Then we can rewrite this relation as follows
Φ(f) = det(1 + fL)
det(1 + L) = det(1 + L + gL)
det(1 + L)
= det(1 + gK),
where the last equality follows by Corollary A.3.
Next, as gK is in L1|2(H) (it is even ﬁnite–dimensional), this can be
rewritten as
Φ(f) =
X
X
det((gK)X) =
X
X
Y
x∈X
g(x) · det KX.
On the other hand, by the very deﬁnition of Φ(f),
Φ(f) =
X
X
Y
x∈X
g(x) · ρ(X).
This implies ρ(X) = det KX, as desired.
Remark A.7. If L =

0
A
−A∗
0

then
K =

AA∗(1 + AA∗)−1
(1 + AA∗)−1A
−(1 + A∗A)−1A∗
A∗A(1 + A∗A)−1

.
ASYMPTOTICS OF PLANCHEREL MEASURES
