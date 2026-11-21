---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-007-8-maxwells-equations-on-s3-and-h3
section_title: "Maxwell's equations on S3 and H3 ."
section_number: 8
pages: 20-22
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
toc_source: inferred
doc_brief: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 16 sections: Front matter; Linking integrals in S3 and H3 .; Historical background."
---
Maxwell's equations, so familiar to us in Euclidean 3-space  R3 ,  can also be shown 
to hold on  S3  and  H3 ,  with the appropriate definitions, as follows. 
 
Let  ρ  be a smooth real-valued function, which we think of as a charge density.  
On  R3  and  H3 ,  we ask that  ρ  have compact support, while on  S3  we ask that  
it have average value zero. 
 
In each case, we define the corresponding electric field  E  =  E(ρ)  by the formula 
 
E(ρ)(y)  =  ∇y ∫ ρ(x) ϕ(x, y) dx , 
 
where  ϕ  is the fundamental solution of the Laplacian. 
 
Let  J  be a smooth vector field, which we think of as a steady-state (i.e., time- 
independent) current distribution.  On  R3  and  H3 ,  we ask that  J  have compact 
support, while on  S3  we impose no restriction on  J . 
 
In each case, we define the corresponding magnetic field  B  =  BS(J)  by one of 
the formulas in Theorem 2.  Since  J  is steady-state, so is  B ,  and therefore 
∂B/∂t  =  0 . 
 
 
THEOREM 4.  MAXWELL'S EQUATIONS  in  S3  and  H3 . 
 
With these definitions, Maxwell's equations,  
 
 
 
∇ ∙ E  =  ρ 
 
 
 
∇ × E  =  0 
 
 
 
∇ ∙ B  =  0  
 
 
 
∇ ×  B  =  J  +  ∂E/∂t , 
 
hold on  S3  and in  H3 ,  just as they do in  R3 . 
 
 
 
 
The proofs of Maxwell's equations are either self-evident or immediate 
consequences of information from previous sections, as follows. 
 
We have 
 
 
 
 
∇y ∙ E(ρ)(y)  =  ∇y ∙ ∇y ∫ ρ(x) ϕ(x, y) dx   
 
 
 
 
 
 
   =  ∆y ∫ ρ(x) ϕ(x, y) dx   
 
                                                       =  ρ(y) , 
 
because  ϕ  is the fundamental solution of the Laplacian. 
 
We have  ∇ × E  =  0  because  E  is a gradient field. 
 
We have  ∇ ∙ B  =  0  because that is one of the four properties required of  B . 
 
We have already noted in sections 6 and 7 how we get the last Maxwell equation,   
∇ × B  =  J  +  ∂E/∂t ,  from the Key Lemma. 
 
 
∙ The equation  dρ/dt  =  — ∇ ∙ J  expresses the fact that the divergence of the current 
flow  J  corresponds to the time rate of accumulation or dissipation of charge, which 
then leads to the  ∂E/∂t  term in Maxwell's equation above, as we noted in section 6. 
 
∙ If the current flow  J  is divergence-free, then  ∂E/∂t  =  0 ,  and hence  ∇ × B  =  J .  
In that case, we get Ampere's Law (just the curl theorem), which says that the 
circulation of  B  around a loop equals the flux of  J  through any surface bounded   
by that loop.
