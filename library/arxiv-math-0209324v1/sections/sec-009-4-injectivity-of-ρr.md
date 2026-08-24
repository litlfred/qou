---
doc_id: arxiv-math-0209324v1
doc_title: "Cyclotomic completions of polynomial rings"
section_id: sec-009-4-injectivity-of-ρr
section_title: "Injectivity of ρR"
section_number: 4
pages: 9-10
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
doc_brief: "Cyclotomic completions of polynomial rings — The main object of study in this paper is the completion Z[q]N = lim←− n Z[q]/ ((1− q)(1− q2)···(1− qn)) of the polynomial ring Z[q], which arises from"
---
S,S ′
If R a ring, and S ⊂ N is a subset, then we have R[q]S = R[q]Φ S . If
S′⊂ S, then we have
ρR
S,S ′ = ρR
Φ S, Φ S′ : R[q]S→ R[q]S′
.
We will use the following well-known properties of cyclotom ic polynomi-
als.
Lemma 4.1. (1) Let n∈ N, p a prime, and e≥ 1. Then we have
(6) Φ pen(q)≡ Φ n(q)d (mod ( p)),
in Z[q], where d = deg Φ pen(q)/ deg Φ n(q). (We have d = ( p− 1)pe−1 if
(n, p ) = 1 and d = pe if p|n.)
(2) If m, n ∈ N, and n/m ∈ Q is not an integer power of a prime, then
we have (Φ n(q), Φ m(q)) = (1) in Z[q].
For m, n ∈ N, we deﬁne cm,n ∈{ 0, 1}∪{ p| prime} by
(1) cn,n = 0,
(2) cm,n = p if p is a prime and n/m = pj for some j∈ Z\{ 0}, and
(3) cm,n = 1 if n/m is not an integer power of a prime.
Note that cm,n = cn,m for all m, n ∈ N. It is straightforward to see that
m⇔R n if and only if R is ( cm,n )-adically separated.
Lemma 4.1 implies that for each m, n ∈ N we have Φ m(q)∈
√
(Φ n(q), c m,n )
in R[q], i.e., Φ m(q)
(cm,n )
⇒ R Φ n(q). It follows that if m⇔R n, then we have
Φ m(q)⇒R Φ n(q). Note also that if S⊂ N is⇔R-connected, then Φ S is
⇒R-connected. The following follows immediately from Theore m 3.4 and
Corollary 3.5.
Theorem 4.2. Let R be a ring and let S′⊂ S⊂ N. Suppose that each
connected component of the graph Γ R(S) contains at least one vertex of
Γ R(S′). (In other words, for each element n∈ S, there is a sequence S′∋
n′⇔R···⇔ R n in S.) Then the homomorphism ρR
S,S ′ is injective.
In particular, if S⊂ N is⇔R-connected, then for any nonempty subset
S′⊂ S the homomorphism ρR
S,S ′ : R[q]S→ R[q]S′
is injective. More partic-
ularly, for any nonempty subset S′⊂ N the homomorphism ρZ
N,S ′ : Z[q]N→
Z[q]S′
is injective.
