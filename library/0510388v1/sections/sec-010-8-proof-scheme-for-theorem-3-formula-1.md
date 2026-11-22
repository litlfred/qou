---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-010-8-proof-scheme-for-theorem-3-formula-1
section_title: "Proof scheme for Theorem 3, formula (1)."
section_number: 8
pages: 22-24
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
When working on  S3  in left-translation format, our first order of business will 
be to derive formula (1) of Theorem 3 for the vector-valued Green's operator. 
 
It is natural to hope, by analogy with  R3 ,  that 
 
A(V, ϕ0)(y)  =  ∫S3  Lyx—1 V(x) ϕ0(x, y)  dx 
 
will be the Green's operator on  S3  when  ϕ0  is the fundamental solution of the 
scalar Laplacian.   
 
It doesn't turn out this way, but the fundamental solution of the Laplacian is not 
the only possible kernel function, and  A(V, ϕ)  is not the only way of convolving  
a vector field with a kernel to get another vector field.   
 
Consider the convolutions 
 
 
 
A(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) ϕ(x, y)  dx 
 
 
 
B(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) × ∇y ϕ(x, y)  dx   
 
 
 
G(V, ϕ)(y)  =  ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ(x, y)  dx . 
 
 
 
 
 
 
 
 
 
 
We will develop a "calculus of vector convolutions", in which we compute formulas 
for curls, divergences and Laplacians of convolutions, first in  R3  to serve as a model, 
and then on  S3  in left-translation format, and in particular obtain 
 
 
PROPOSITION 2.  On  S3 ,  the vector Laplacian has the following effect on 
convolutions of types  A ,  B  and  G : 
 
 
 
∆A(V, ϕ)  =  A(V, ∆ϕ)       —  4 A(V, ϕ)     —  2 B(V, ϕ) 
 
 
 
∆B(V, ϕ)  =  B(V, ∆ϕ)        +  2 A(V, ∆ϕ)  —  2 G(V, ϕ) 
 
 
 
∆G(V, ϕ)  =  G(V, ∆ϕ) . 
 
 
The large spaces after the first terms on the right hand sides of the  A  and  B  lines 
serve as a reminder that in Euclidean space  R3 ,  only those first terms appear. 
In particular, in  R3  we have  ∆A(V, ϕ)  =  A(V, ∆ϕ) .  So naturally, when we 
choose  ϕ  =  ϕ0  to be a fundamental solution of the scalar Laplacian in  R3 ,   
we get  ∆A(V, ϕ0)  =  A(V, ∆ϕ0)  =  A(V, δ)  =  V ,  which tells us that   
A(V, ϕ0)  =  Gr(V)  there. 
 
Once we have Proposition 2 in hand, we will then get formula (1) of Theorem 3 
for the Green's operator on  S3  by adding one copy of line A to two copies of line B 
and four copies of line G,  each with a different choice of kernel function  ϕ .
