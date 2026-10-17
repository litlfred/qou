---
doc_id: arxiv-math-0605314v1
doc_title: "arXiv:math/0605314v1 [math.GT] 11 May 2006"
section_id: sec-031-1231-derivatives-and-power-series-expansions
section_title: "Derivatives and power series expansions"
section_number: 12.3.1
pages: 41-42
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
---
12.3.1. Derivatives and power series expansions. Like polynomials and analytic
functions, the elements of d
Z[q] can be diﬀerentiated arbitrarily many times.
In
fact, the derivation
d
dq : Z[q] →Z[q] is continuous with respect to the topology
deﬁned by the ideals (q)nZ[q], n ≥0, since we have
d
dq (q)2n ∈(q)nZ[q].
(12.2)
Therefore,
d
dq induces a continuous Z-linear derivation
d
dq : d
Z[q] →d
Z[q].
(12.3)
This implies that there are higher derivations
1
k!
dk
dqk = 1
k!( d
dq )k : d
Z[q] →d
Z[q].
for all k ≥0. (Recall that ( d
dq)k(Z[q]) ⊂k!Z[q]. This implies that ( d
dq)k(d
Z[q]) ⊂
k!d
Z[q].) Suppose f(q) ∈d
Z[q] and ζ ∈Z. Deﬁne the “Taylor series at ζ” of f(q) by
Tζ(f(q)) =
X
k≥0
1
k!
dkf
dqk (ζ)(q −ζ)k ∈Z[ζ][[q −ζ]].
Then one can easily check Tζ(f(q)) = ιζ(f(q)).
12.3.2. The Ohtsuki series. As mentioned in the introduction, according to Lawrence’s
conjecture proved by Rozansky, the Ohtsuki series τ O(M) for an integral homology
sphere can be deﬁned as the unique element τ O(M) ∈Z[[q −1]] such that for each
root of unity ζ of odd prime power order r, τ O(M)|q=ζ converges p-adically to
τζ(M) ∈Z[ζ], i.e., we have
evζ(τ O(M)) = τζ(M)
(12.4)
in Zp[ζ] ∼= lim
←−nZ[ζ]/(pn) ∼= lim
←−nZ[ζ]/((ζ −1)n), where
evζ : Z[[q −1]] →Zp[ζ]
denote the ring homomorphism induced by the evaluation map
evζ : Z[q] →Z[ζ],
f(q) 7→f(ζ).
These properties characterize τ O(M).
Theorem 12.6. For every integral homology sphere M, we have ι1(JM) = τ O(M).
Proof. For each root of unity ζ of prime power order r = pe, we have the following
commutative diagram
d
Z[q]
ι1
−−−−→Z[[q −1]]
evζ
y
yevζ
Z[ζ] −−−−→
i
Zp[ζ].
Here i is the inclusion. By the commutativity of the diagram and by Theorem
11.1, we have evζ ι1(JM) = i evζ(JM) = i(τζ(M)). Therefore, by (12.4), we have
evζ(ι1(JM)) = evζ(τ O(M)). The assertion follows from Lemma 12.7.
42
KAZUO HABIRO
Lemma 12.7. The map
Z[[q −1]] →
Y
p:odd prime
Zp[ζp],
x 7→(evζp(x))p,
is injective. Here ζp = exp 2π√−1
p
.
Proof. Write x = P
n≥0 xn(q−1)n. We assume that evζp(x) = 0 for all p, and we see
that xn = 0 by induction on n. Let n ≥0 and suppose that x0 = · · · = xn−1 = 0.
Then, for every odd prime p, we have evζp(x) ≡xn(ζ −1)n mod (ζ −1)n+1.
Therefore, xn is divisible by p. It follows that xn = 0.
