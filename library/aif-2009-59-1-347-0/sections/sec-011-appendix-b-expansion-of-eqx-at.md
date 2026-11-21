---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-011-appendix-b-expansion-of-eqx-at
section_title: "Appendix B. Expansion of Eq(x) at"
section_number: null
pages: 22-23
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
toc_source: outline
doc_brief: "On q-summation and confluence — 28 sections: Front matter; Introduction; Part 1. Convergent q-Borel and q-L"
---
The purpose of this section is the proof of Proposition 1.5. We recall the
notation
(B.1)
an+1 =
n
X
k=0
1
qk+1 −1,
n ⩾0,
A(q) =
X
n⩾0
qn+1
qn+1 −1,
and
θ(x) =
X
n∈Z
qn(n−1)/2xn,
and the statement of the proposition:
Proposition B.1. — For any x ∈C∗\ q−N:
(B.2)
X
n⩾0
(q; q)nxn+1 = −

−qxθ′(−qx)
θ(−qx) + 1 + A(q)
  q
x; q

∞
+
X
n⩾1
an
(q; q)n
qn(n+1)/2

−1
x
n
.
The proof of the proposition above is based on a Watson’s formula for
basic hypergeometric functions, which is the analogue of a Barnes’ formula
for Gauss hypergeometric function. Barnes (cf. [19, §14.51] and [3]) proved
that if | arg(−x)| < π, c /∈Z⩽0 and a−b /∈Z, then the analytic continuation
of 2F1(a, b; c; x) for |x| > 1 is given by:
2F1(a, b; c; x) = Γ(c)Γ(b −a)
Γ(b)Γ(c −a)(−x)−a
2F1(a, a −c + 1, a −b + 1; x−1)
+ Γ(c)Γ(a −b)
Γ(a)Γ(c −b)(−x)−b
2F1(b, b −c + 1, b −a + 1; x−1).
TOME 59 (2009), FASCICULE 1
368
Lucia DI VIZIO & Changgui ZHANG
G.N. Watson (cf. [8, §4.3]) proved a formula of the same kind for Heine
series, namely if:
(B.3)
x /∈q−N ∪
cq
abqN
,
c /∈q−N,
a
b /∈qZ,
abcx̸ = 0.
then
2φ1(a, b; c; q, x) = (b, c/a; q)∞
(c, b/a; q)∞
θ(−ax)
θ(−x) 2φ1

a, aq/c; aq/b; q, cq
abx

+ (a, c/b; q)∞
(c, a/b; q)∞
θ(−bx)
θ(−x) 2φ1

b, bq/c; bq/a; q, cq
abx

,
where (α1, ..., αk; q)n = Qk
i=1(αi; q)n. We are going to consider a degener-
ation of Watson’s formula letting b →a and c →0. In this way we obtain
an expression for 2φ1(a, a; 0; q, x) that we can apply to
Eq(x) = x2φ1

q, q; 0; q, −
x
1 −q

.
