---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-027-24-proof-of-theorem-2-formula-2
section_title: "Proof of Theorem 2, formula (2) ."
section_number: 24
pages: 55-57
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Let  V  be a smooth vector field on  S3 .  Thinking of  V  as a steady current flow, 
we defined the corresponding magnetic field  BS(V)  by  
 
BS(V)(y)  =  ∫S3  PyxV(x) × ∇y ϕ(x, y)  dx , 
 
where  ϕ(α)  =  (—1/4π2) (π — α) csc α . 
 
We saw in the preceding section that, as a consequence of the Key Lemma, the 
field  BS(V)  satisfies Maxwell's equation 
 
∇y × BS(V)(y)  =  V(y)  +  ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx . 
 
To complete the proof of Theorem 2, formula (2), we need only show that  BS(V)  
is divergence-free, and we do this as follows. 
 
            ∇y ∙ BS(V)(y)  =  ∇y ∙ ∫S3  PyxV(x)  ×  ∇yϕ(x, y)  dx 
 
                                         =  ∫S3   ∇y ∙ {PyxV(x)  ×  ∇yϕ(x, y)}  dx , 
 
and we will show that the integrand is identically zero.  We use the standard 
formula 
 
     ∇ ∙ (A × B)  =  (∇ × A) ∙ B  —  A ∙ (∇ × B) ,   
 
and also the formula from Proposition 18.1, 
 
                   ∇y  ×  PyxV(x)  =  [y , x , V] / (1  +  <x , y>) . 
 
 
 
 
 
 
 
 
 
Then 
 
        ∇y ∙ {PyxV(x)  ×  ∇yϕ(x, y)} 
 
                               =  {∇y × PyxV(x)} ∙ ∇yϕ(x, y)  —  PyxV(x)  ∙  ∇y × ∇yϕ(x, y) 
 
                               =  {∇y × PyxV(x)} ∙ ∇yϕ(x, y) 
 
                               =  {[y , x , V(x)] / (1  +  <x , y>)}  ∙  ∇yϕ(x, y) 
 
                               =  0 , 
 
since  [y , x , V(x)]  is orthogonal to the plane spanned by  x  and  y ,  while 
∇yϕ(x, y)  lies in that plane. 
 
Thus the proposed magnetic field  BS(V)  is indeed divergence-free. 
 
This completes the proof of Theorem 2, formula (2) . 
 
We note that the above argument for the divergence-free character of  BS(V)   
does not depend on the particular choice of kernel function  ϕ .
