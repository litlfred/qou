---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-008-9-proof-scheme-for-theorem-1
section_title: "Proof scheme for Theorem 1."
section_number: 9
pages: 22-24
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
toc_source: inferred
doc_brief: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 16 sections: Front matter; Linking integrals in S3 and H3 .; Historical background."
---
With steady-state electrodynamics in hand, we can follow what we imagine to be 
Gauss's second line of reasoning and obtain the linking integral formulas on  S3   
and  H3  given in Theorem 1. 
 
To do this, run a unit current  V  =  dx/ds  along the first loop  K1 ,  and use one of 
the three Biot-Savart formulas from Theorem 2 to calculate the resulting magnetic 
field  B .  For example, on  S3  in parallel transport format, we have 
 
B(y)  =  BS(dx/ds)(y)  =  ∫K1  Pyx dx/ds  ×  ∇y ϕ(x, y)  ds , 
 
where  ϕ(α)  =  (—1/(4π2)) (π — α) csc α ,  and where the integration takes place with 
respect to arc length along  K1  rather than with respect to volume in  S3 . 
 
We intend to calculate the circulation of this magnetic field  B  along the second 
loop  K2 ,  and then apply Ampere's Law to get the formula for the linking integral. 
 
 
 
 
We can view  V  as the limit of divergence-free current flows  Vε  supported in 
smaller and smaller tubular neighborhoods  Nε  of  K1 ,  each disjoint from  K2 ,  and 
each with unit flux through a cross-sectional disk.  Let  Bε  be the corresponding 
magnetic field, defined throughout  S3  or  H3 .  Since  Vε  is divergence-free, we 
have  ∇ × Bε  =  Vε ,  and so by Ampere's Law, the circulation of  Bε  around the 
second loop  K2  equals the unit flux of  Vε  through the cross-sectional disks of  Nε ,  
multiplied by the linking number of  K1  and  K2 . 
 
Now the magnetic fields  Bε  converge uniformly to  B  on the complement of any 
fixed tubular neighborhood of  K1 ,  and in particular along the loop  K2 .  Hence 
the circulation of  B  along  K2  also equals the linking number of  K1  and  K2 . 
   
The three formulas for the magnetic field given in Theorem 2 then lead quickly to 
the three linking integrals in Theorem 1. 
 
For example, working on  S3  in parallel transport format, 
 
 
Lk(K1, K2)  =  circulation of  B  along  K2 
 
                              =  ∫K2  BS(dx/ds)(y)  ∙  dy/dt  dt 
 
 
                    =  ∫K2  (∫K1  Pyx dx/ds  ×  ∇y ϕ(x, y)  ds)  ∙  dy/dt  dt 
 
                              =  ∫K1×K2  Pyx dx/ds  ×  ∇y ϕ(x, y)  ∙  dy/dt  ds dt 
 
                              =  —∫K1×K2  Pyx dx/ds  ×  dy/dt  ∙  ∇y ϕ(x, y)  ds dt , 
 
where  ϕ(α)  =  (—1/(4π2)) (π — α) csc α , 
 
                              =  1/(4π2)∫K1×K2  Pyx dx/ds  ×  dy/dt  ∙  ∇y ϕ(x, y)  ds dt , 
 
where now  ϕ(α)  =  (π — α) csc α ,  giving us formula (2) of Theorem 1. 
 
 
∙  Note that the third integral in the formula for  BS(V)  in left-translation format  
on  S3 ,  given in Theorem 2 part (1), is missing from the corresponding linking 
integral, given in Theorem 1 part (1), because the approximating current flows  Vε 
are all divergence-free.
