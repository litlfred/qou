---
doc_id: 1-s20-s002212362200012x-main
doc_title: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-011-4-proof-of-fact-4
section_title: "Proof of Fact 4"
section_number: 4
pages: 19-20
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
toc_source: outline
doc_brief: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube — V Article history: Received 17 December 2020 Accepted 13 January 2022 Available online"
---
Let ρ : [−1, 1]n →R be the harmonic extension of dν
dμ and write g(x) := log ρ(tanh(x))
where, throughout this section, for x ∈[−1, 1]n, tanh(x) := (tanh(x1), ..., tanh(xn)). A 
calculation gives
g(x) = log

Cn

i∈[n]
(1 + tanh(xi)yi) dν(y)
= −

i∈[n]
log cosh(xi) + L[ν](x).
Therefore,
20
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
Cov(τxν) = ∇2L[ν](x) = ∇2g(x) + diag

1
cosh2(x)
 
.
On the other hand, a direct calculation gives
∇2
i,jg(x) = [∇2
i,j log ρ](tanh(x))
cosh2(xi) cosh2(xj) −δi,j
2 tanh(xi)
cosh2(xi) [∇i log ρ](tanh(x)),
thus we have
Covi,j(τxν) = [∇2
i,j log ρ](tanh(x))
cosh2(xi) cosh2(xj) −δi,j
2 tanh(xi)
cosh2(xi) [∇i log ρ](tanh(x)) −
1
cosh2(xi)
 
.
Observe that
1
xi −1 ≤∇i log ρ(x) ≤
1
xi + 1,
and therefore

∇i log ρ(tanh(x))
cosh2(xi)
 ≤2.
Finally, since 1/ cosh(x) ≤1 and by assumption ∇2 log ρ ⪯βIn, we obtain
Cov(τx[ν]) ⪯(β + 5)In.
