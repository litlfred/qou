---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-010-4-proof-of-fact-3
section_title: "Proof of Fact 3"
section_number: 4
pages: 14-15
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
toc_source: outline
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
Proof of Fact 3
Let ρ : [−1, 1]n →R be the harmonic extension of dν
dµ. A calculation gives and write g(x) :=
log ρ(tanh(x)),
g(x) = log
Z
Cn
Y
i∈[n]
(1 + tanh(xi)) dν(x)
= −
X
i∈[n]
log cosh(xi) + L[ν](x).
Therefore,
Cov(τxν) = ∇2L[ν](x) = ∇2g(x) + diag

1
cosh2(x)

.
On the other hand, a direct calculate gives
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
2 tanh(xi)
cosh2(xi) [∇i log ρ](tanh(x)) −
1
cosh2(xi)

.
Observe that
1
xi −1 ≤∇i log ρ(x) ≤
1
xi + 1,
and therefore

∇i log ρ(tanh(x))
cosh2(xi)

 ≤2.
Finally, since 1/ cosh(x) ≤1 and by assumption ∇2 log ρ ⪯βIn, we obtain
Cov(τx[ν]) ⪯(β + 3)In.
