---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-061-56-proof-of-theorem-1-formulas-2-and-3
section_title: "Proof of Theorem 1, formulas (2) and (3) ."
section_number: 56
pages: 106-107
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
We start on  S3 ,  and begin with the same set-up and notation used in the preceding 
section.  We must show that in parallel transport format, we have 
 
         Lk(K1, K2)  =  1/4π2 ∫K1×K2  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt , 
   
where     ϕ(α)  =  (π — α) csc α . 
 
We take Theorem 2, formula (2) for the Biot-Savart operator in parallel transport 
format and apply it to the current flow  V  along the loop  K1  to get 
 
BS(V)(y)  =  ∫K1  PyxV(x)  ×  ∇y ϕ(x, y) ds , 
 
where  ϕ(α)  =  (—1/4π2) (π — α) csc α . 
 
Then we compute the circulation of  BS(V)  around the loop  K2 ,  as follows. 
 
∫K2  BS(V)(y) ∙ dy/dt  dt  = 
 
 
                    =  ∫K2  (∫K1  Pyx dx/ds  ×  ∇y ϕ(x, y)  ds)  ∙  dy/dt  dt 
 
                              =  ∫K1×K2  Pyx dx/ds  ×  ∇y ϕ(x, y)  ∙  dy/dt  ds dt 
 
                              =  —∫K1×K2  Pyx dx/ds  ×  dy/dt  ∙  ∇y ϕ(x, y)  ds dt , 
 
where we still have   ϕ(α)  =  (—1/4π2) (π — α) csc α , 
 
                              =  1/4π2∫K1×K2  Pyx dx/ds  ×  dy/dt  ∙  ∇y ϕ(x, y)  ds dt , 
 
where now  ϕ(α)  =  (π — α) csc α . 
 
As before, we apply Ampere's Law to the field  BS(V)  and conclude that 
 
         Lk(K1, K2)  =  1/4π2 ∫K1×K2  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt . 
 
Then, as in the preceding section, we can drop the assumptions that the loop  K1 
is simple and is parametrized by arc length, completing the proof of Theorem 1, 
formula (2) for the Gauss linking integral on  S3  in parallel transport format 
 
The proof of Theorem 1, formula (3) for the Gauss linking integral on  H3 
in parallel transport format is the same, and we are done.
