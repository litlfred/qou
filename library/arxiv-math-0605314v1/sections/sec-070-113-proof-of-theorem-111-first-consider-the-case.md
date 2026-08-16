---
doc_id: arxiv-math-0605314v1
doc_title: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO"
section_id: sec-070-113-proof-of-theorem-111-first-consider-the-case
section_title: "Proof of Theorem 11.1. First consider the case r = 1, ζ = 1. We have"
section_number: 11.3
pages: 37-38
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the"
---
τ1(M ) = 1 by the deﬁnition. We also have ev 1(JM ) = 1 by Lemma 10.3. Hence,
we have (11.1) in this case.
Let r≥ 2. Let L be as in the last subsection. By the deﬁnition of JM , we have
evζ(JM ) = ev ζ(JL0(ω−f1,ω −f2,... ,ω −fm)) (11.4)
Setd =⌊ r−2
2 ⌋. It follows from Theorem 8.2 that if x1,... ,x m∈P and we have
xi∈P d+1 for some i∈{ 1,... ,m}, then we have ev ζ(JL(x1,... ,x m)) = 0. Hence,
by (11.4), we have
evζ (JM ) = ev ζ (JL0(ωr,−f1,ω r,−f2,... ,ω r,−fm)),
38 KAZUO HABIRO
where ωr,±1 is the truncation of ω±1 given by
ωr,±1 =
d∑
n=0
(±1)nv± 1
2 n(n+3)P ′
n∈P .
Note that ωr,±1∈ SpanAr{P0,P 1,... ,P d}⊂R Ar . We also have Ω r,±1∈R Ar .
Lemma 11.2. LetL =L1∪···∪ Lm∪K be an (m + 1)-component, algebraically-
split, 0-framed link. Then, for x1,... ,x m∈R Ar , we have
evζ (JL∪K(x1,... ,x m,ω r,±1)) = ev ζ(JL∪K(x1,... ,x m, Ω r,±1)).(11.5)
Proof. IfK is an unknot, then by Theorem 9.4 and the deﬁnition of ωr,±1 we have
evζ(JL∪K(x1,... ,x m,ω r,±1)) = ev ζ(JL(K, ∓1) (x1,... ,x m)),(11.6)
whereL(K,∓1) is the result from L by surgery along K with framing∓1. By (11.3)
and the standard fusing argument, we also have
evζ(JL∪K(x1,... ,x m, Ω r,±1)) = ev ζ(JL(K, ∓1) (x1,... ,x m)).
Hence, we have (11.5).
Now, we consider the general case. A crossing change of two st rands in K can
be done by a Hoste move. Applying this move ﬁnitely many times , we get a framed
link L∪K ′∪E1∪···∪ Et, t≥ 0, such that all the linking numbers between
two components of L∪ K ′∪E1∪···∪ Et are zero, K ′ is a 0-framed unknot,
E1∪···∪ Et is an admissible framed unlink with framings g1,... ,g t∈{± 1}, and
(L∪K ′)E1∪···∪Et
∼
=L∪K. Using (11.6) iteratively, we obtain
evζ(JL∪K(x1,... ,x m,y ))
= ev ζ(JL∪K ′∪E0
1 ∪···∪E0m
(x1,... ,x m,y,ω r,−g1,... ,ω r,−gt)),
where E0
i is Ei with 0-framing, and y is either ωr,±1 or Ω r,±1. Since K ′ is an
unknot, the assertion reduces to the special case proved abo ve.
