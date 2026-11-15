---
doc_id: arxiv-0808.1533v3
doc_title: "On the third order helicity of magnetic fields on invariant domains in S³"
section_id: sec-008-equations-for-the-frozen-in-field-forms
section_title: "Equations for the frozen-in-field forms"
section_number: null
pages: 28-29
source_pdf: 0808.1533v3.pdf
source_sha256: 3e003cc35a4e5711
toc_source: outline
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order helicity of a volume preserving vector ﬁeld B, which leads us to a"
---
Equations for the frozen-in-ﬁeld forms
Given a volume preserving vector ﬁeld B on M and a path t −→g(t) ∈SDiﬀ(M), let
Bt := g∗(t)B .
Then for B0 = B, by deﬁnition
˙Bt = d
dtBt

t=0= −LV B = −[V, B],
(A.1)
and as a result
d
dtιBtµ|t=0 = −ι[V,B]µ
Next, calculate (∂t + LV ≡L∂t+V )
(∂t + LV )ιBtµ
=
∂t(ιBtµ) + LV ιBtµ
=
ι ˙Btµ + ιBt(LV µ) + ι[V,Bt]µ
=
ι ˙Bt+[V,Bt]µ,
where in the second identity we applied the general formula: ι[A,B] = LAιB −ιBLA, and in
the third equation the fact that V is volume preserving i.e. LV µ = 0. As a result of (A.1)
we obtain
(∂t + LV )ιBtµ = 0 .
Next, we justify Formula (5.5). First use (5.6) to calculate
ιBi(µj ∧µk) = (ιBiµj) ∧µk −µj ∧(ιBiµk)
ιBi(µ1 ∧µ2 ∧µ3) = (ιBiµ1) ∧µ2 ∧µ3 −µ1 ∧ιBi(µ2 ∧µ3)
= (ιBiµ1) ∧µ2 ∧µ3 −µ1 ∧ιBiµ2 ∧µ3 + µ1 ∧µ2 ∧ιBiµ3,
(A.2)
28
since ιBiµj = 0 for i̸ = j only one term in the above expressions remains for each i. Set
α := ιB2ιB1β, β ∈Ω3((S3)3), since α ∧µ1 ∧µ2 ∧µ3 = 0 and α is a 1-form we obtain
0 = ιB3(α ∧µ1 ∧µ2 ∧µ3)
= (ιB3α) ∧µ1 ∧µ2 ∧µ3 −α ∧µ1 ∧µ2 ∧ιB3µ3,
where in the last step we used (A.2). Therefore
(ιB3ιB2ιB1β) ∧µ1 ∧µ2 ∧µ3 = (ιB2ιB1β) ∧µ1 ∧µ2 ∧ιB3µ3 .
Analogously, (ιB2ιB1β) ∧µ1 ∧µ2 = (ιB1β) ∧µ1 ∧ιB2µ2 and ιB1β ∧µ1 = β ∧ιB1µ1 which
justiﬁes Equation (5.5).
