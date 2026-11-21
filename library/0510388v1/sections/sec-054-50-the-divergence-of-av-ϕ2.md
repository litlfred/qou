---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-054-50-the-divergence-of-av-ϕ2
section_title: "The divergence of A(V, ϕ2) ."
section_number: 50
pages: 94-95
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
We begin as follows. 
 
     ∇y ∙ A(V, ϕ2)(y)  =  ∫H3  ∇y ∙ (PyxV(x) ϕ2(x, y))  dx 
 
              =  ∫H3  (∇y ∙ PyxV(x)) ϕ2(x, y)  dx   +  ∫H3  PyxV(x) ∙ ∇yϕ2(x, y)  dx . 
 
The second integral on the RHS above is simply  g(V, ϕ2)(y) ,  so we put that aside.   
 
Turning to the first integral and using formula (3) and the fact that  < x, V(x) >  =  0 , 
we follow the pattern set in section 29 for  S3 ,  and get 
 
         ∫H3  (∇y ∙ PyxV(x)) ϕ2(x, y)  dx  =  ∫H3  PyxV(x) ∙ ∇yψ(α)  dx 
 
                                                                   =  g(V, ψ)(y) , 
 
where the new kernel function  ψ  satisfies  
 
       ψ'(α)  =  [2 sinh α / (1 + cosh α)] ϕ2(α)  
 
                  =  [2 sinh α / (1 + cosh α)] [(—1/4π) csch α  +  (1/4π) α / (1 + cosh α)] 
 
                  =  (—1/2π) / (1 + cosh α)   +   (1/2π) α sinh α / (1 + cosh α)2 , 
 
and hence 
ψ(α)  =  (—1/2π) α / (1 + cosh α) . 
 
We have set the constant of integration to zero, so that  ψ(α)  →  0  as  α  →  ∞ . 
 
Collecting information, we have 
 
∇y ∙ A(V, ϕ2)(y)   
 
                   =  ∫H3  (∇y ∙ PyxV(x)) ϕ2(x, y)  dx   +  ∫H3  PyxV(x) ∙ ∇yϕ2(x, y)  dx  
 
                   =  g(V, ψ)(y)  +  g(V, ϕ2)(y) , 
 
and hence 
∇y (∇y ∙ A(V, ϕ2)(y))  =  G(V, ψ)(y)  +  G(V, ϕ2)(y) .
