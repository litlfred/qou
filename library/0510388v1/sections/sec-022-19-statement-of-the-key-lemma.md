---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-022-19-statement-of-the-key-lemma
section_title: "Statement of the Key Lemma."
section_number: 19
pages: 46-47
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
The following result plays a lead role in obtaining the formulas for the Biot-Savart 
and Green's operators on  S3  in parallel transport format. 
 
 
KEY LEMMA, spherical version. 
 
     
     
     
     ∇y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x (cos α 
α 
α 
α  ϕ)}   
 
                                                                 =  (∆ϕ  —  ϕ) (V(x)  —  < V(x), y > y) .  
 
 
This formula is quite flexible: it is useful whether  V  is a smooth vector field 
defined on all of  S3 ,  or just on a bounded subdomain  Ω  of  S3 ,  or just along  
a smooth closed curve  K  in  S3 ,  or even just at the single point  x .   
 
As usual,  α  is the distance on  S3  between  x  and  y .  The kernel function  ϕ(α)   
is any smooth function, which typically blows up at  α = 0  and is asymptotic there 
to  —1/(4πα) .   
 
The Key Lemma can be understood intuitively in the special case that  ϕ(α)  is the 
fundamental solution of the operator  ϕ  →  ∆ϕ  —  ϕ   on  S3 ,  in which case we  
will see that  cos α ϕ(α)  is the fundamental solution of the scalar Laplacian there. 
 
With this choice of kernel function, the quantity  PyxV(x) × ∇yϕ  can be viewed  
as the contribution made by a little bit of current  V(x)  at the location  x  to the 
magnetic field at the location  y .  When integrated over  S3  with respect to  x ,   
the result will be the magnetic field  B  at  y .  Thus the first term on the left hand 
side of the Key Lemma integrates to  ∇ × B . 
 
In similar fashion, the term  ∇y {V(x) ∙ ∇x (cos α  ϕ)}  integrates to the time 
derivative  ∂E/∂t  of the electric field at  y  due to the accumulation or dispersion  
of charge by the current flow  V ,  while the right hand side of the Key Lemma 
integrates to the current flow  V  itself. 
 
Thus the Key Lemma, for this special choice of kernel function  ϕ ,  can be 
viewed as a pointwise or infinitesimal version of Maxwell's equation 
 
∇ × B  —  ∂E/∂t    =  V  .
