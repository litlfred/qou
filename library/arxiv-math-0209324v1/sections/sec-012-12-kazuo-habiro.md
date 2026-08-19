---
doc_id: arxiv-math-0209324v1
doc_title: "CYCLOTOMIC COMPLETIONS OF POL YNOMIAL RINGS KAZUO HABIRO"
section_id: sec-012-12-kazuo-habiro
section_title: "KAZUO HABIRO"
section_number: 12
pages: 12-12
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
doc_brief: "CYCLOTOMIC COMPLETIONS OF POLYNOMIAL RINGS KAZUO HABIRO — The main object of study in this paper is the completion Z[q]N = lim←− n Z[q]/ ((1− q)(1− q2)···(1− qn)) of the polynomial ring Z[q], which"
---
For each m with m|n, set Zm = Z R
{m} ={ζ∈ Z R| ord ζ = m}. By
R[q]{n}≃ R[q]Zn and Theorem 5.2, it suﬃces to prove that the set Zn is⇔R-
connected. The case n = 1 is trivial, so we assume not. Let n = pe1
1 ··· per
r
be a factorization into prime powers, where p1, . . . , p r are distinct primes
and e1, . . . , e r≥ 1. There is a bijection
Zpe1
1
×···× Zperr
≃−→Zn, (ξ1, . . . , ξ r)↦→ξ1··· ξr.
It suﬃces to show that if ( ξ1, . . . , ξ r), (ξ′
1, . . . , ξ ′
r)∈ Zpe1
1
×···× Zperr satisﬁes
ξj = ξ′
j for all j ∈{ 1, . . . , r }\{ i} and ξi⁄= ξ′
i for some i, then we have
ξ1··· ξr⇔R ξ′
1··· ξ′
r, which is equivalent to that ξi⇔R ξ′
i. Since Z2 ={−1}
contains only one element, the case pi = 2 and ei = 1 does not occur. We
have (ξi− ξ′
i)⊂
√
(pi), and hence ξi⇔R ξ′
i. □
Corollary 5.5. Let R be an integral domain of characteristic 0, and S⊂ N
a⇔R-connected subset. Suppose that there is n ∈ S such that R is p-
adically separated for each odd prime factor p of n, and if 4|n, then R is
also 2-adically separated. Then the ring R[q]S is an integral domain.
In particular, Z[q]S is an integral domain for any nonempty subset S⊂ N.
Proof. The result follows from Theorem 5.4 and the fact that the form al
power series ring R[ζ][[q− ζ]] is an integral domain. □
