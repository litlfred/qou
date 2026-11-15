---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-051-47-plan-of-the-proof
section_title: "Plan of the proof."
section_number: 47
pages: 90-91
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Consider the usual vector convolutions,  
 
     A(V, ϕ)(y)  =  ∫H3  PyxV(x) ϕ(x, y)  dx 
 
     B(V, ϕ)(y)  =  ∫H3  PyxV(x)  ×  ∇yϕ(x, y)  dx 
 
      g(V, ϕ)(y)  =  ∫H3  PyxV(x)  ∙  ∇yϕ(x, y)  dx 
 
     G(V, ϕ)(y)  =  ∇y g(V, ϕ)(y)  =  ∇y ∫H3  PyxV(x)  ∙  ∇yϕ(x, y)  dx . 
 
Step 1.  First we will determine the unknown kernel function  ϕ  so as to make 
 
∇y  ×  A(V, ϕ)(y)  =  — B(V, ϕ1)(y)  =  — BS(V)(y) . 
 
The solution we obtain is not unique. 
 
Step 2.  Then, as a consequence of Maxwell's equation, we will have 
 
        — ∇y × ∇y × A(V, ϕ2)(y)  =  ∇y × BS(V)(y)   
 
                                                  =  V(y)  —  ∇y ∫H3  ∇x ∙ V(x)  ϕ0(x, y)  dx . 
Hence 
 
∆y A(V, ϕ2)(y)  =  — ∇y × ∇y × A(V, ϕ2)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) 
 
                      =  V(y)  —  ∇y ∫H3  ∇x ∙ V(x)  ϕ0(x, y)  dx   +  ∇y(∇y ∙ A(V, ϕ2)(y)) 
 
                      =  V(y)  +  some gradient field . 
 
We then find the kernel function  ϕ3  so that  ∆y G(V, ϕ3)(y)  =  G(V, ∆ϕ3)(y)   
is the negative of the above gradient field, in which case, defining 
 
Gr(V)(y)  =  A(V, ϕ2)(y)  +  G(V, ϕ3)(y) 
 
yields the desired  equation  ∆y Gr(V)(y)  =  V(y) .
