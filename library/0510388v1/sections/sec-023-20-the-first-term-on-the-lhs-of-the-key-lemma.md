---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-023-20-the-first-term-on-the-lhs-of-the-key-lemma
section_title: "The first term on the LHS of the Key Lemma."
section_number: 20
pages: 47-50
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
The plan for the proof of the Key Lemma is simple.  Applying an appropriate 
rotation of  S3 ,  we can assume that  x  is the point  (1, 0, 0, 0)  and that, after 
scaling,  V(x)  =  X1  =  (0, 1, 0, 0) .  At each point  y  =  (y0 , y1 , y2 , y3)  of   
S3  —  {—x} ,  we will expand both sides of the Key Lemma in terms of the ortho- 
normal basis  E1 ,  E2  and  E3  for  TyS3 ,  and prove equality component-wise. 
 
We begin with the first term on the LHS of the equation, and note that 
 
PyxV(x)  ×  ∇y ϕ  =  PyxV(x)  ×  (—Pyx ∇x ϕ)  =  Pyx (— V(x)  ×  ∇x ϕ) . 
 
From section 14, we have that 
 
                      ∇x α  =  (cos α  x  —  y) / sin α 
 
                                      =  ((y0 , 0 , 0 , 0)  —  (y0 , y1 , y2 , y3)) / sin α 
 
                                      =  (—1 / sin α) (y1 X1  +  y2 X2  +  y3 X3) . 
 
Hence 
 
∇x ϕ  =  ϕ'(α) ∇x α  =  (— ϕ'(α) / sin α) (y1 X1  +  y2 X2  +  y3 X3) . 
 
Thus 
 
     — V(x) × ∇x ϕ  =  (—X1)  ×  (— ϕ'(α) / sin α) (y1 X1  +  y2 X2  +  y3 X3) 
 
                                     =  (ϕ'(α) / sin α) ( —y3 X2  +  y2 X3) . 
Hence 
 
        PyxV(x)  ×  ∇y ϕ  =  Pyx (— V(x)  ×  ∇x ϕ) 
 
                                     =  (ϕ'(α) / sin α) ( —y3 E2  +  y2 E3) . 
 
 
 
 
 
Now we take curls and evaluate the first term on the LHS of the Key Lemma, 
 
∇y  ×  {PyxV(x)  ×  ∇y ϕ}  =  ∇y  ×  {(ϕ'(α) / sin α) ( —y3 E2  +  y2 E3)} . 
 
We begin by computing the curl of the vector field 
 
W  =  W(y)  =  —y3 E2  +  y2 E3 . 
 
Following the recipe given in section 18, we have 
 
∇y × W  =  ⇑ d ↓ W . 
 
Going part way, we have 
 
                      d ↓ W  =  d (—y3 θ2  +  y2 θ3)   
 
                                  =  — dy3 ∧ θ2  —  y3 dθ2  +  dy2 ∧ θ3  +  y2 dθ3 . 
 
We use the formulas from section 17 to express  dy3  and  dy2  in terms of 
θ1 ,  θ2  and  θ3 ,  and compute that 
 
         d ↓ W  =  2 (y0  +  y1
2/(1 + y0)) θ2 ∧ θ3  +  2 (y1y2 / (1 + y0)) θ3 ∧ θ1   
 
                                                +  2 (y1y3 / (1 + y0)) θ1 ∧ θ2  . 
 
Hence 
 
     ∇y × W  =  ⇑ d ↓ W  =  2 (y0  +  y1
2/(1 + y0)) E1  +  2 (y1y2 / (1 + y0)) Ε2   
 
                                                                   +  2 (y1y3 / (1 + y0)) Ε3 . 
 
Now to compute  ∇y  ×  {(ϕ'(α) / sin α) ( —y3 E2  +  y2 E3)} ,  we use the formula 
 
∇  ×  (f W)  =  f (∇ × W)  +  ∇f  × W , 
 
with  f (α)  =  ϕ'(α) / sin α . 
 
 
 
 
 
 
 
 
We find that 
 
∇y  ×  {PyxV(x)  ×  ∇y ϕ}  =  ∇y  ×  {(ϕ'(α) / sin α) ( —y3 E2  +  y2 E3)} 
 
=  { (ϕ'/sin α) 2 (y0  +  y1
2/(1 + y0))  +  (ϕ"/sin2α  —  ϕ' cos α/sin3α) (y2
2 + y3
2) } E1 
 
        +  { (ϕ'/sin α) 2 y1y2/(1 + y0)     +      (ϕ"/sin2α  —  ϕ' cos α/sin3α) (—y1y2) } E2 
 
        +  { (ϕ'/sin α) 2 y1y3/(1 + y0)     +      (ϕ"/sin2α  —  ϕ' cos α/sin3α) (—y1y3) } E3 . 
 
This puts the first term on the LHS of the Key Lemma in the form we want it.
