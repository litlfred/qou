---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-045-41-the-first-term-on-the-lhs-of-the-key-lemma
section_title: "The first term on the LHS of the Key Lemma."
section_number: 41
pages: 83-85
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
The plan is the same as it was for  S3 .  Applying an appropriate isometry of  H3 ,  
we can assume that  x  is the point  (1, 0, 0, 0)  and that, after scaling,   
V(x)  =  X1  =  (0, 1, 0, 0) .  At each point  y  =  (y0 , y1 , y2 , y3)  of  H3 ,  we will 
expand both sides of the Key Lemma in terms of the orthonormal basis  E1 ,  E2  
and  E3  for  TyH3 ,  and prove equality component-wise. 
 
We begin with the first term on the LHS of the equation, and note that 
 
PyxV(x)  ×  ∇y ϕ  =  PyxV(x)  ×  (—Pyx ∇x ϕ)  =  Pyx (— V(x)  ×  ∇x ϕ) . 
 
From section 35, we have that 
 
                      ∇x α  =  (cosh α  x  —  y) / sinh α 
 
                                      =  ((y0 , 0 , 0 , 0)  —  (y0 , y1 , y2 , y3)) / sinh α 
 
                                      =  (—1 / sinh α) (y1 X1  +  y2 X2  +  y3 X3) . 
 
Hence 
 
∇x ϕ  =  ϕ'(α) ∇x α  =  (— ϕ'(α) / sinh α) (y1 X1  +  y2 X2  +  y3 X3) . 
 
Thus 
 
     — V(x) × ∇x ϕ  =  (—X1)  ×  (— ϕ'(α) / sinh α) (y1 X1  +  y2 X2  +  y3 X3) 
 
                                     =  (ϕ'(α) / sinh α) ( —y3 X2  +  y2 X3) . 
 
Hence 
 
        PyxV(x)  ×  ∇y ϕ  =  Pyx (— V(x)  ×  ∇x ϕ) 
 
                                     =  (ϕ'(α) / sinh α) ( —y3 E2  +  y2 E3) . 
 
 
 
 
 
 
 
Now we take curls and evaluate the first term on the LHS of the Key Lemma, 
 
∇y  ×  {PyxV(x)  ×  ∇y ϕ}  =  ∇y  ×  {(ϕ'(α) / sinh α) ( —y3 E2  +  y2 E3)} . 
 
We begin by computing the curl of the vector field 
 
W  =  W(y)  =  —y3 E2  +  y2 E3 , 
 
following the recipe   ∇y × W  =  ⇑ d ↓ W .  The computation is similar to the one 
on  S3 ,  and yields 
 
∇y × W  =  2 (y0  —  y1
2/(1 + y0)) E1  —  2 (y1y2 / (1 + y0)) Ε2  —  2 (y1y3 / (1 + y0)) E3 .                   
 
Now to compute  ∇y  ×  {(ϕ'(α) / sinh α) ( —y3 E2  +  y2 E3)} ,  we use the formula 
 
∇  ×  (f W)  =  f (∇ × W)  +  ∇f  × W , 
 
with  f (α)  =  ϕ'(α) / sinh α ,  and find that 
 
∇y  ×  {PyxV(x)  ×  ∇y ϕ}  =  ∇y  ×  {(ϕ'(α) / sinh α) ( —y3 E2  +  y2 E3)} 
 
=  { (2ϕ'/sinh α) (y0  —  y1
2/(1 + y0))  +  (ϕ"/sinh2α  —  ϕ' cosh α/sinh3α) (y2
2 + y3
2) } E1 
 
        +  { (—2ϕ'/sinh α) y1y2/(1 + y0)   +      (ϕ"/sinh2α  —  ϕ' cosh α/sinh3α) (—y1y2) } E2 
 
        +  { (—2ϕ'/sinh α) y1y3/(1 + y0)   +      (ϕ"/sinh2α  —  ϕ' cosh α/sinh3α) (—y1y3) } E3 . 
 
This puts the first term on the LHS of the Key Lemma in the form we want it.
