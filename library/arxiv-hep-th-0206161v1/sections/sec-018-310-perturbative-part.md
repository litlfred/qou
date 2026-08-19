---
doc_id: arxiv-hep-th-0206161v1
doc_title: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING Nikita A. Nekrasov 1"
section_id: sec-018-310-perturbative-part
section_title: "Perturbative part"
section_number: 3.10
pages: 23-24
source_pdf: 0206161v1.pdf
source_sha256: 9530c40215baa02d
doc_brief: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING Nikita A. Nekrasov 1 — 26 sections: Introduction; (1 .3); (α±"
---
So far we were calculating the nonperturbative part of the pr epotential. It would
be nice to see the perturbative part somewhere in our setup, s o as to combine the whole
expression into something nice.
One way is to calculate carefully the equivariant Chern char acter of the tangent bundle
to ~Mk along the lines sketched in the end of the previous section[1 0]. The faster way in
the ǫ1 +ǫ2 = 0 case is to note that the expression (1.6) is a sum over parti tion with
the universal denominator, which is not well-deﬁned withou t the non-universal numerator.
Nevertheless, let us try to pull it out of the sum.
We get the inﬁnite product (up to an irrelevant constant):
∞∏
i,j=1
∏
l⁄=n
1
aln + ¯h(i −j) ∼
exp −
∑
l⁄=n
∫ ∞
0
ds
s
e−saln
(e¯hs − 1)(e−¯hs − 1) (3.27)
If we regularize this by cutting the integral at s ∼ε → 0, we get a ﬁnite expression, which
actually has the form
exp F pert(a,ǫ 1,ǫ 2)
ǫ1ǫ2
,
with F pert being analytic in ǫ1,ǫ 2 at zero. In fact
F pert(a, 0, 0) =
∑
l⁄=n
1
2a2
lnlog aln + ambiguous quadratic polynomial in aln.
22
The formula (3.27) is a familiar expression for the Schwinge r amplitude of a mass aln
particle in the electromagnetic ﬁeld
F ∝ǫ1 dx1 ∧dx2 +ǫ2 dx3 ∧dx4 . (3.28)
Its appearance will be explained in the next section.
Let us now combine F inst and F pert into a single ǫ-deformed prepotential
F (a,ǫ 1,ǫ 2) = F pert(a,ǫ 1,ǫ 2) + F inst(a,ǫ 1,ǫ 2)
where for general ǫ1,ǫ 2 we deﬁne:
F pert(a,ǫ 1,ǫ 2) =
∑
l⁄=n
∫ ∞
ε
ds
s
e−saln
sinh
( sǫ1
2
)
sinh
( sǫ2
2
) (3.29)
with the singular in ε part dropped. We deﬁne:
Z(a,ǫ 1,ǫ 2;q) = exp F (a,ǫ 1,ǫ 2;q)
ǫ1ǫ2
(3.30)
