---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-028-101-bounds-on-l1-norm-of-q-holonomic-functions
section_title: "Bounds on l1-norm of q-holonomic functions"
section_number: 10.1
pages: 23-24
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
K, the functions JK and HK are q-holonomic. Recall that a sequence f : N − →Q(q) is q-holonomic if
satisﬁes a q-linear diﬀerence equation. In other words, there exists a natura l number d and polynomial
aj(u, v) ∈ Q[u, v] for j = 0, . . . , d with ad ⁄= 0 such that for all n ∈ N we have:
(45)
d∑
j=0
aj(qn, q)fn+j(q) = 0 .
In this section we observe that q-holonomic functions satisfy a priori upper bounds on their degrees and
(under an integrality assumption) on their l1-norm. As a simple corollary, we obtain another proof of the
quadratic bounds in Proposition 6.1, though not as explicit.
Deﬁnition 10.1. We say that a sequence f : N − →Z[q±1] is q-integral holonomic if it satisﬁes an q-diﬀerence
equation as above with ad = 1.
Question 10.2. Is it true that JK and CK are q-integral holonomic for every knot K?
For a partial answer, see [ GS06].
Theorem 10.3. (a) If f : N − →Z[q±1] is q-holonomic, then for all n we have:
deg+(fn) = O(n2) and deg−(fn) = O(n2).
(b) If f is q-integral holonomic, then for all n we have:
||fn||1 ≤ Cn
for some constant C. In particular,
lim sup
n→∞
log |fn(eα/n )|
n ≤ Cα
24 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
for all α ∈ C.
In other words, integral q-holonomic functions grow at most exponentially.
Proof. Suppose f satisﬁes ( 45). It is easy to see that for every a(u, v) ∈ Q[u, v], there exists a constant C′
such that deg +(a(qn, q)) < C ′n for every n ≥ 1. We choose such a common C′ for all aj(qn, q), j = 0, 1, . . . , d,
and, in addition, C′ > deg+f (n) for n = 0, 1, . . . , d.
We will prove by induction on n ≥ 1 that deg +f (n) ≤ C′n2. By assumption, it is true for n = 1 , . . . , d.
For n ≥ 1, Then, by induction we have:
deg+fn+d(q) = deg +
(
ad(qn, q) fn+d(q)
)
− deg+ad(qn, q)
= deg +

−
d−1∑
j=0
aj(qn, q)fn+j(q)

 − deg+ad(qn, q)
< C ′n + C′(n + d − 1)2 + C′n ≤ C′(n + d)2.
The second claim in (a) follows similarly.
For (b), let cj = ||aj(Q, q)||1 for j = 0, . . . , d− 1, and choose C so that
• Cd ≥ cd−1Cd−1 + · · · + c0C0, and
• || fn(q)||1 ≤ Cn for n = 0, . . . , d− 1.
Then, it is easy to see by induction that (b) holds for all n. □
Remark 10.4. It is easy to see that the bounds of Theorem
10.3 are sharp. For example, consider the
sequence fn(q) = (1 + q)(1 + q2) . . . (1 + qn).
Theorem 10.3 gives an alternative proof of the quadratic bounds for the degree s of the color Jones poly-
nomial, though not as explicit as in Proposition 6.1. If Question 10.2 has a positive answer then Theorem
10.3 also gives an alternative proof of Theorem 6.2.
