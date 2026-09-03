---
doc_id: 1-s20-s002212362200012x-main
doc_title: "www.elsevier.com/locate/jfa"
section_id: sec-010-4-proof-of-fact-4
section_title: "Proof of Fact 4"
section_number: 4
pages: 19-20
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
doc_brief: "www.elsevier.com/locate/jfa — 13 sections: Log concavity and concentration of; Introduction; A lower bound on the entropy"
---
Let ρ :[ −1, 1]n → R be the harmonic extension of dν
dμ and write g(x) := log ρ(tanh(x))
where, throughout this section, for x ∈ [−1, 1]n, tanh(x) := (tanh(x1), ...,tanh(xn)). A 
calculation gives
g(x)=l o g
∫
Cn
∏
i∈[n]
(1 + tanh(xi)yi) dν(y)
= −
∑
i∈[n]
log cosh(xi)+ L[ν](x).
Therefore,
20 R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
Cov(τxν)= ∇2L[ν](x)= ∇2g(x)+d i a g
( 1
cosh2(x)
)
.
On the other hand, a direct calculation gives
∇2
i,jg(x)= [∇2
i,j log ρ](tanh(x))
cosh2(xi)c o s h2(xj) − δi,j
2t a n h (xi)
cosh2(xi) [∇i log ρ](tanh(x)),
thus we have
Covi,j(τxν)= [∇2
i,j log ρ](tanh(x))
cosh2(xi)c o s h2(xj) − δi,j
(2t a n h (xi)
cosh2(xi) [∇i log ρ](tanh(x)) − 1
cosh2(xi)
)
.
Observe that
1
xi − 1 ≤∇ i log ρ(x) ≤ 1
xi +1 ,
and therefore
⏐⏐⏐⏐
∇i log ρ(tanh(x))
cosh2(xi)
⏐⏐⏐⏐≤ 2.
Finally, since 1/ cosh(x) ≤ 1a n d by assumption ∇2 log ρ ≼ βIn, we obtain
Cov(τx[ν]) ≼ (β +5 )In.
