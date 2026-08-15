---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND"
section_id: sec-013-31-the-riemann-hilbert-problem
section_title: "The Riemann-Hilbert problem"
section_number: 3.1
pages: 9-10
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
sider an associated Riemann-Hilbert problem. It depends on a choice of a point ξ∈ T which we
call the constant term. We discuss the statement of this problem m ore carefully in Section
4; for
now we just give the rough idea.
Problem 3.1. Fix a point ξ∈ T. Construct a piecewise holomorphic map
X : C∗→ T
with the following three properties:
10 TOM BRIDGELAND
(a) As t ∈ C∗ crosses an active ray ℓ ⊂ C∗ in the clockwise direction, the function X(t)
undergoes a discontinuous jump described by the formula
X(t)↦→S(ℓ)(X(t)).
(b) As t→ 0 one has exp(Z/t)· X(t)→ ξ.
(c) As t→∞ the element X(t) has at most polynomial growth.
The gist of condition (a) is that the function X should be holomorphic in the complement of
the active rays, and for each active ray ℓ⊂ C∗ the analytic continuations of the two functions on
either side should diﬀer by composition with the corresponding autom orphism S(ℓ).
To make sense of (b), note that
exp(Z/t) : Γ→ C∗
is an element of the torus T+, and recall that T = T− is a torsor for T+. We often write
exp(Z/t)· X(t) = Y (t)· ξ, (12)
which then deﬁnes a map Y : C∗→ T+. Clearly the maps X and Y are equivalent data; we use
whichever is most convenient.
Composing with the (twisted) characters of T±, we can alternatively encode the solution in
either of the two systems of maps
Xγ = xγ◦ X : C∗→ C∗, Y γ = yγ◦ Y : C∗→ C∗.
Condition (c) is then the statement that for each γ∈ Γ there should exist k > 0 such that
|t|−k <|Xγ(t)| <|t|k, |t|≫ 0.
Problem 3.1 is closely analogous to the Riemann-Hilbert problems which arise in the s tudy of
diﬀerential equations with irregular singularities. In that case the S tokes factors S(ℓ) lie in a ﬁnite-
dimensional group GL n(C), whereas in our situation they are elements of the inﬁnite-dimensio nal
group of Poisson automorphisms of the torus T. We will return to this analogy in the sequel to
this paper [ 8].
