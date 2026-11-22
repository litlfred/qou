---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-053-49-the-curl-of-av-ϕy
section_title: "The curl of A(V, ϕ)(y) ."
section_number: 49
pages: 92-94
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
∇y × A(V, ϕ)(y)  =  ∫H3  ∇y × {PyxV(x) ϕ(x, y)}  dx 
 
          =  ∫H3  {∇y × PyxV(x)} ϕ(x, y)   —   PyxV(x) × ∇yϕ(x, y)  dx 
 
                      [y, x, V(x)]                                          ϕ'(α) 
          =  ∫H3  ———————— ϕ(x, y)   +    [y, x, V(x)] —————  dx 
                       1 + <x, y>                                          sinh α 
 
                                                  ϕ                   ϕ' 
          =  ∫H3  [y, x, V(x)] {——————— + —————}  dx   , 
                                            1 + cosh α         sinh α 
 
thanks to formulas (2) and (4) above. 
 
On the other hand, 
 
      BS(V)(y)  =  B(V, ϕ1)(y)  =  ∫H3  PyxV(x)  ×  ∇yϕ1(x, y)  dx 
 
                                                                               — ϕ1'(α) 
                                               =  ∫H3  [y, x, V(x)] ———————   dx  , 
                                                                                sinh α 
 
again by formula (4) . 
 
Thus, in order that 
 
∇y  ×  A(V, ϕ)(y)  =  — BS(V)(y)  =  — B(V, ϕ1)(y)  , 
 
we must choose  ϕ  to satisfy the ODE 
 
                                 ϕ                   ϕ'                 ϕ1' 
                         ————————  +  —————   =   ————— . 
                          1 + cosh α         sinh α          sinh α 
 
This ODE is solved just like the corresponding one in section 28, and we get 
 
(1 + cosh α) ϕ  =  (1 + cosh α) ϕ1  +  (1/4π) (α  +  C) . 
 
The choice of the constant  C  represents the nonuniqueness in carrying out Step 1. 
We discuss this further in section 52, but here set  C  =  0  and continue. 
 
 
 
 
 
Dividing through by (1 + cosh α) ,  we get 
 
          ϕ(α)  =  ϕ1(α)  +  (1/4π) α / (1 + cosh α)   
 
                    =   (—1/4π) csch α  +  (1/4π) α / (1 + cosh α) . 
 
Note that  ϕ(α)  has a singularity at  α  =  0 .   
 
We call this solution  ϕ2(α) ,  and with it we have completed Step 1: 
 
∇y  ×  A(V, ϕ2)(y)  =  — B(V, ϕ1)(y)  =  — BS(V)(y) . 
 
We take the negative curl of both sides to get 
 
        — ∇y × ∇y × A(V, ϕ2)(y)  =  ∇y × BS(V)(y)   
 
                                                   =  V(y)  —  ∇y ∫H3  (∇x ∙ V(x))  ϕ0(x, y)  dx , 
 
thanks to Maxwell's equation.  Integrating by parts, we have 
 
          ∫H3  (∇x ∙ V(x))  ϕ0(x, y)  dx  =  — ∫H3  V(x) ∙ ∇xϕ0(x, y)  dx 
 
                                                                 =  ∫H3  PyxV(x) ∙ ∇yϕ0(x, y)  dx   
 
                                                                 =  g(V, ϕ0)(y) . 
 
Hence 
 
∆y A(V, ϕ2)(y)  =  — ∇y × ∇y × A(V, ϕ2)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) 
 
                      =  V(y)  —  ∇y ∫H3  ∇x ∙ V(x)  ϕ0(x, y)  dx   +  ∇y(∇y ∙ A(V, ϕ2)(y))  
 
                      =  V(y)  —  G(V, ϕ0)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) . 
 
 
Just as on  S3 ,  the next step is to compute  ∇y ∙ A(V, ϕ2)(y) .
