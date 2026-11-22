---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-032-29-the-divergence-of-av-ϕ2
section_title: "The divergence of A(V, ϕ2) ."
section_number: 29
pages: 63-65
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
We begin as follows. 
 
     ∇y ∙ A(V, ϕ2)(y)  =  ∫S3  ∇y ∙ {PyxV(x) ϕ2(x, y)}  dx 
 
              =  ∫S3  {∇y ∙ PyxV(x)} ϕ2(x, y)  dx   +  ∫S3  PyxV(x) ∙ ∇yϕ2(x, y)  dx . 
 
The second integral on the RHS above is simply  g(V, ϕ2)(y) ,  so we put that aside.   
 
Turning to the first integral and using formula (3) and the fact that  < x, V(x) >  =  0 , 
we get 
 
                                                 — 2 <y, V(x)> 
  ∫S3  {∇y ∙ PyxV(x)} ϕ2(x, y)  dx   =   ∫S3  ——————————  ϕ2(x, y)  dx    
                                                                         1 + <x, y> 
 
                                                                                        — 2 ϕ2(α)       
                                                          =  ∫S3  <y, V(x)>  ————————  dx 
                                                                                         1 + cos α 
 
                                                                            cos α x — y                2 sin α ϕ2(α) 
                                                          =  
                                                          =  
                                                          =  
                                                          =  ∫S3  < —————————, V(x) > —————————  dx  
                                                                                 sin α                        1 + cos α 
 
                                                                                                 2 sin α ϕ2(α) 
                                                          =  ∫S3  < ∇xα , V(x) >  ——————————  dx 
                                                                                                   1 + cos α 
 
                                                                                  2 sin α ϕ2(α) 
                                                          =  ∫S3  V(x) ∙ —————————— ∇xα  dx 
                                                                                    1 + cos α 
 
                                                                                       — 2 sin α ϕ2(α) 
                                                          =  ∫S3  PyxV(x) ∙ ———————————— ∇yα  dx 
 
 
 
 
 
                                         1 + cos α 
 
                                                          =  ∫S3  PyxV(x) ∙ ∇yψ(α)  dx 
 
                                                          =  g(V, ψ)(y) . 
 
 
 
 
 
 
The new kernel function  ψ  satisfies  
 
ψ'(α)  =  [— 2 sin α / (1 + cos α)] ϕ2(α)  
 
    =  [— 2 sin α / (1 + cos α)] [(—1/4π2) (π — α) csc α  +  (1/8π2) (π — α)2 / (1 + cos α)] 
 
    =  (1/2π2) (π — α) / (1 + cos α)  —  (1/4π2) (π — α)2 sin α / (1 + cos α)2 , 
 
and hence 
 
ψ(α)  =  (—1/4π2) (π — α)2 / (1 + cos α) . 
 
 
Collecting information, we have 
 
∇y ∙ A(V, ϕ2)(y)   
 
                   =  ∫S3  {∇y ∙ PyxV(x)} ϕ2(x, y)  dx   +  ∫S3  PyxV(x) ∙ ∇yϕ2(x, y)  dx  
 
                   =  g(V, ψ)(y)  +  g(V, ϕ2)(y) , 
 
and hence 
 
∇y (∇y ∙ A(V, ϕ2)(y))  =  G(V, ψ)(y)  +  G(V, ϕ2)(y) .
