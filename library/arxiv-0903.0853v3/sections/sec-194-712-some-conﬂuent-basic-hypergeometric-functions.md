---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-194-712-some-conﬂuent-basic-hypergeometric-functions
section_title: "Some conﬂuent basic hypergeometric functions. — Usual basic"
section_number: 7.1.2
pages: 121-122
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
hypergeometrics series have the form:
2Φ1(a,b ;c;q,z ) :=
∑
n≥0
(a,b ;q−1)n
(c,q −1;q−1)n
zn , where a,b,c ∈ C∗.
(Remember that here,|q|> 1.) Writing for shortF(z) this series, the rescaling
F(−q−1z/c) degenerates, whenc→∞ , into a conﬂuent basic hypergeometrics
series:
φ(a,b ;q,z ) :=
∑
n≥0
(a,b ;q−1)n
(q−1;q−1)n
qn(n+1)/2zn , where a,b∈ C∗.
Writing un := (a,b ;q−1)n
(q−1;q−1)n
qn(n+1)/2 the general coeﬃcient, we have, for all
n≥ 0:
(qn+1− 1)un+1 =q2(qn−a)(qn−b)un,
whence, multiplying by zn+1 and summing:
(σq− 1) ˆf =q2z(σq−a)(σq−b) ˆf,
where we write for short ˆf(z) the divergent seriesφ(a,b ;q,z ). We shall denote
the corresponding q-diﬀerence operator as:
L :=q2z(σq−a)(σq−b)− (σq− 1) =q2zσ 2
q−
(
1 + (a +b)q2z)
)
σq + (1 +abq2z).
We are interested in the equationLf = 0. Its Newton polygon ( i.e. that of L)
has slopes 0 and 1. The slope 0 has exponent 1 and gives rise to t he divergent
solution ˆf. To tackle the slope 1, we compute:
(zθq)L(zθq)−1 = 1
qz
(
σ2
q−
(
1 + (a +b)q2z)
)
σq +qz(1 +abq2z)
)
,
which has slopes 0 and−1, the latter having exponent 0. According to Adams
lemma (see the footnote in the introduction to this chapter) , we thus get a
116 CHAPTER 7. EXAMPLES OF THE STOKES PHENOMENON
unique solution g0∈ 1 +zC{z}, whence the “convergent” solution f0 := g0
zθq
of equation Lf = 0.
