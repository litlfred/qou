---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-016-a2-correlation-functions-of-determinantal-proces
section_title: "A.2. Correlation functions of determinantal processes"
section_number: null
pages: 30-31
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 22 sections: Front matter; Plancherel measures; Introduction"
---
let ρ(X) be the probability that a random conﬁguration contains X, that is,
ρ(X) = Prob ({Y ∈Conf(X)0, X ⊂Y }) .
We call ρ(X) the correlation functions. The fundamental fact about determinantal
point processes is that their correlation functions again have a determinantal form.
Proposition A.6. Let L be as above and set K = L(1 + L)−1. Then ρ(X) =
det KX.
Proof. We follow the argument in [11], Exercise 5.4.7. Let f(x) be an arbitrary
function on X such that f(x) = 1 for all but a ﬁnite number of x’s. Form the
probability generating functional:
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
det(1 + L)
= det(1 + fL)
det(1 + L) ,
where the last equality is justiﬁed by Proposition A.4 applied to the operator fL.
Now, set g(x) = f(x) −1, so that g(x) = 0 for all but ﬁnitely many x’s. Then
we can rewrite this relation as
Φ(f) = det(1 + fL)
det(1 + L) = det(1 + L + gL)
det(1 + L)
= det(1 + gK),
where the last equality follows by Corollary A.3.
ASYMPTOTICS OF PLANCHEREL MEASURES
511
Next, as gK is in L1|2(H) (it is even ﬁnite–dimensional), this can be rewritten
as
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
 0
A
−A∗
0

, then
K =

AA∗(1 + AA∗)−1
(1 + AA∗)−1A
−(1 + A∗A)−1A∗
A∗A(1 + A∗A)−1

.
In the recent survey [35], the determinantal formula ρ(X) = det KX for the
correlation functions is taken as a deﬁnition. The paper [35] contains a more general
and detailed discussion of the basics of the theory of determinantal processes which
in [35] are called determinantal random point ﬁelds.
