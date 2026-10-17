---
doc_id: li-braid-closures
doc_title: "Knot polynomials on braid closures"
section_id: sec-006-closures-of-3-braids
section_title: "Closures of 3-braids"
section_number: null
pages: 8-9
source_pdf: Li-braid-closures.pdf
source_sha256: f7410e7be5bc187e
toc_source: outline
doc_brief: "Knot polynomials on braid closures — We explore properties of the Jones and Alexander polynomials of braid closures of braids of index 3."
---
Closures of 3-braids
We investigate the Jones and Alexander polynomials of 3-braid closures at −1.
Recall from Examples 2.12 and 2.13 that S(1,1,1)
q
is the sign representation, where each
gi acts as −1, while S(3)
q
is the trivial representation, where each gi acts as q. When q = −1,
the representations become isomorphic, so χ(1,1,1)(α) = χ(3)(α). Hence
Vˆα(−1) = (
√
−1)e(α)−2(2χ(1,1,1)(α) −χ(2,1)(α))
and
∆ˆα(−1) = (
√
−1)−e(α)+2(χ(1,1,1)(α) −χ(2,1)(α) + χ(3)(α))
= (
√
−1)−e(α)+2(2χ(1,1,1)(α) −χ(2,1)(α)).
Note the use of √−1 rather than i or −i due to the lack of a continuous, single-valued square
root over C. If we define √−1 to be {i, −i}, then clearly Vˆα(−1) = ∆ˆα(−1) = Xˆα(−1, −1).
Otherwise, the usual convention where i = √−1 yields that Vˆα(−1) = (−1)e(α)∆ˆα(−1).
From now on, we will adopt the latter convention where Vˆα(−1) = (−1)e(α)∆ˆα(−1).
Definition 3.1. Let ϕ: B3 →SL2(Z) be the homomorphism satisfying ϕ(σi) = Mi, where
(M1, M2) =
 1
0
−1
1

,
1
1
0
1

.
Proposition 3.2. For a braid α ∈B3, the Jones and Alexander polynomials of ˆα satisfy
Vˆα(−1) = (−i)e(α)(tr(ϕ(α)) −2) and ∆ˆα(−1) = ie(α)(tr(ϕ(α)) −2).
Proof. From Example 2.14 we note that gi acts as −Mi in S−1
(2,1), while gi acts as −1 in
S−1
(1,1,1). Thus, as found above, we have
Vˆα(−1) = ie(α)−2(2χ(1,1,1)(α) −χ(2,1)(α))
= ie(α)(−1)(2(−1)e(α) −(−1)e(α) tr(ϕ(α)))
= (−i)e(α)(tr(ϕ(α)) −2),
as claimed.
An interesting question to consider is which integer values Vˆα(−1) can possibly take,
and what type of link ˆα corresponds to. Here, we shall consider two extremal cases: when
ˆα is split and when ˆα is a knot.
8
