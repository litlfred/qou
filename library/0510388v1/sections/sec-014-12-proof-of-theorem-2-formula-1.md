---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-014-12-proof-of-theorem-2-formula-1
section_title: "Proof of Theorem 2, formula (1)."
section_number: 12
pages: 32-34
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Let  V  be a smooth vector field on  S3 .  Thinking of  V  as a steady current flow, 
we define the corresponding magnetic field  BS(V)  by the formula 
 
BS(V)  =  — ∇ × Gr(V) . 
 
It is easy to check that  BS(V)  satisfies the two properties required of it in 
section 4, as follows. 
 
(1)  ∇ ∙ BS(V)  =  0  because the divergence of a curl is always zero. 
 
(2)  To get Maxwell's equation, we compute: 
 
              ∇ × BS(V)(y)  =  — ∇ × ∇ × Gr(V)(y) 
 
                                           =  ∆Gr(V)(y)  —  ∇(∇ ∙ Gr(V)(y) 
 
                                           =  V(y)  —  ∇(Gr(∇ ∙ V)(y) 
 
                                           =  V(y)  —  ∇y ∫S3  (∇x ∙ V(x))  ϕ0(x, y)  dx  
 
                                           =  V(y)  +  ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx . 
 
where  ϕ0  is the fundamental solution of the scalar Laplacian on  S3 .  Note that  
we used the fact, mentioned in section 6, that the Green's operator on  S3  
commutes with divergence. 
 
 
 
 
 
 
 
 
The explicit expression for  BS(V)  given in formula (1) of Theorem 2 comes 
from the explicit formula for  Gr(V)  in left-translation format, given in Theorem 3, 
formula (1), together with the curl formulas given in Lemma 3, as follows. 
 
BS(V)  =  — ∇ × Gr(V)   
 
                       =  — ∇ × A(V, ϕ0)  —  2 ∇ × B(V, ϕ1)  —  4 ∇ × G(V, ϕ2) 
 
                       =  B(V, ϕ0)  +  2 A(V, ϕ0)  —  2 A(V, ∆ϕ1)  +  2 G(V, ϕ1) 
 
                       =  B(V, ϕ0)  +  2 A(V, ϕ0)  —  2 A(V, ϕ0 — [ϕ0])  +  2 G(V, ϕ1) 
 
                       =  B(V, ϕ0)  +  2 A(V, [ϕ0])  +  2 G(V, ϕ1) 
 
                       =  B(V, ϕ0)  — (1/4π2) A(V, 1)  +  2 G(V, ϕ1) 
 
                       =  ∫S3  Lyx—1 V(x) × ∇y ϕ0(x, y)  dx    
 
 
 
 
 
 — 1/(4π2) ∫S3  Lyx—1 V(x)  dx 
 
 
 
 
 
 
     +  2 ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ1(x, y)  dx , 
 
as claimed.
