---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-048-44-maxwells-equation-in-h3
section_title: "Maxwell's equation in H3 ."
section_number: 44
pages: 87-88
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
We now apply the Key Lemma to the proof of Maxwell's equation 
 
∇ × B  =  V  +  ∂E/∂t  
 
in  H3 .  In the Key Lemma, we use the kernel function 
 
ϕ(α)  =  (—1/4π) csch α , 
 
which, as we noted earlier, is a fundamental solution of the shifted Laplacian on  H3 , 
 
∆ϕ  +  ϕ  =  δ . 
 
With this choice of kernel function, we have that 
 
(cosh α) ϕ(α)  =  (—1/4π) coth α , 
 
which differs from the fundamental solution of the Laplacian on  H3 , 
 
ϕ0(α)  =  (—1/4π) (coth α  —  1) , 
 
only by a constant.  Since we take the gradient of this function below, the 
difference is irrelevant. 
 
Hence with these choices, the Key Lemma reads 
 
     ∇y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x ϕ0}   
 
                                                                 =  δ(x, y) (V(x)  —  < V(x), y > y) .  
 
Keeping these choices of kernel functions, we now define the Biot-Savart operator 
by formula (3) of Theorem 2, 
 
BS(V)(y)  =  ∫H3  PyxV(x) × ∇y ϕ(x, y) dx , 
 
for smooth, compactly supported vector fields  V . 
 
 
 
 
 
 
Then we integrate the Key Lemma over  H3  and get 
 
   ∫H3  ∇y × {PyxV(x) × ∇yϕ} dx   —   ∫H3  ∇y {V(x) ∙ ∇x ϕ0}  dx 
 
                                                          =   ∫H3  δ(x, y) (V(x)  —  < V(x), y > y)  dx . 
 
We process this just as we did on  S3  in section 23, and obtain 
 
∇y × BS(V)(y)  =  V(y)  +  ∇y ∫H3  V(x) ∙ ∇x ϕ0(x, y)  dx . 
 
As in  R3  and on  S3 ,  we recognize this as Maxwell's equation 
 
∇ × B  =  V  +  ∂E/∂t .
