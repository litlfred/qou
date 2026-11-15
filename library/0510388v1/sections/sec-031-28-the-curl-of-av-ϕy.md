---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-031-28-the-curl-of-av-ϕy
section_title: "The curl of A(V, ϕ)(y) ."
section_number: 28
pages: 60-63
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
∇y × A(V, ϕ)(y)  =  ∫S3  ∇y × {PyxV(x) ϕ(x, y)}  dx 
 
          =  ∫S3  {∇y × PyxV(x)} ϕ(x, y)   —   PyxV(x) × ∇yϕ(x, y)  dx 
 
                      [y, x, V(x)]                                          ϕ'(α) 
          =  ∫S3  ———————— ϕ(x, y)   —    [y, x, V(x)] —————  dx 
                       1 + <x, y>                                           sin α 
 
                                                  ϕ                   ϕ' 
          =  ∫S3  [y, x, V(x)] {——————— — —————}  dx   , 
                                            1 + cos α          sin α 
 
thanks to formulas (2) and (4) above. 
 
On the other hand, 
 
      BS(V)(y)  =  B(V, ϕ1)(y)  =  ∫S3  PyxV(x)  ×  ∇yϕ1(x, y)  dx 
 
                                                                               ϕ1'(α) 
                                               =  ∫S3  [y, x, V(x)] —————   dx  , 
                                                                                sin α 
 
again by formula (4) . 
 
Thus, in order that 
 
∇y  ×  A(V, ϕ)(y)  =  — BS(V)(y)  =  — B(V, ϕ1)(y)  , 
 
we must choose  ϕ  to satisfy the ODE 
 
                                 ϕ                   ϕ'                    ϕ1' 
                         ————————  —  —————   =   — ————— . 
                          1 + cos α           sin α               sin α 
 
 
 
 
 
 
 
We rewrite this as 
 
                            (1 + cos α) ϕ'  —  (sin α) ϕ  =  (1 + cos α) ϕ1' , 
 
equivalently, 
 
                        [(1 + cos α) ϕ]'  =  [(1 + cos α) ϕ1]'  +  (sin α) ϕ1 
 
                                                  =  [(1 + cos α) ϕ1]'  —  (1/4π2) (π — α) , 
 
since  ϕ1(α)  =  (—1/4π2) (π — α) csc α .  Now we integrate both sides to get 
 
(1 + cos α) ϕ  =  (1 + cos α) ϕ1  +  (1/8π2) (π — α)2 . 
 
Dividing through by (1 + cos α) ,  we get 
 
          ϕ(α)  =  ϕ1(α)  +  (1/8π2) (π — α)2 / (1 + cos α)   
 
                    =   (—1/4π2) (π — α) csc α  +  (1/8π2) (π — α)2 / (1 + cos α) . 
 
Note that  ϕ(α)  has a singularity only at  α  =  0  and not at  α  =  π .   
 
We call this solution  ϕ2(α) ,  and with it we have completed Step 1: 
 
∇y  ×  A(V, ϕ2)(y)  =  — B(V, ϕ1)(y)  =  — BS(V)(y) . 
 
 
 
 
 
 
We take the negative curl of both sides to get 
 
        — ∇y × ∇y × A(V, ϕ2)(y)  =  ∇y × BS(V)(y)   
 
                                                   =  V(y)  —  ∇y ∫S3  (∇x ∙ V(x))  ϕ0(x, y)  dx , 
 
thanks to Maxwell's equation.  Integrating by parts, we have 
 
          ∫S3  (∇x ∙ V(x))  ϕ0(x, y)  dx  =  — ∫S3  V(x) ∙ ∇xϕ0(x, y)  dx 
 
                                                                 =  ∫S3  PyxV(x) ∙ ∇yϕ0(x, y)  dx   
 
                                                                 =  g(V, ϕ0)(y) . 
 
Hence 
 
∆y A(V, ϕ2)(y)  =  — ∇y × ∇y × A(V, ϕ2)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) 
 
                      =  V(y)  —  ∇y ∫S3  ∇x ∙ V(x)  ϕ0(x, y)  dx   +  ∇y(∇y ∙ A(V, ϕ2)(y))  
 
                      =  V(y)  —  G(V, ϕ0)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) . 
 
 
Clearly the next step is to compute  ∇y ∙ A(V, ϕ2)(y) .
