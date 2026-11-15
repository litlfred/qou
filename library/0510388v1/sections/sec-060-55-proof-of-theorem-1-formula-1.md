---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-060-55-proof-of-theorem-1-formula-1
section_title: "Proof of Theorem 1, formula (1)."
section_number: 55
pages: 104-106
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Let  K1  =  {x(s)}  and  K2  =  {y(t)}  be disjoint oriented smooth closed curves 
in the unit 3-sphere  S3 .  We must show that in left-translation format, we have 
 
         Lk(K1, K2)  =  1/(4π2) ∫K1×K2  Lyx—1 dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt 
 
                     —  1/(4π2) ∫K1×K2  Lyx—1 dx/ds ∙ dy/dt  ds dt  , 
 
where  ϕ(α)  =  (π — α) cot α . 
 
For the moment, we assume that the curve  K1  is simple, and that its parametri- 
zation  x  =  x(s)  is by arc-length, so that  V(x)  =  dx/ds  is a unit tangent vector 
field along  K1 . 
 
Then we take Theorem 2, formula (1) for the Biot-Savart operator in left-translation 
format and, given the discussion in the preceding section, apply it to the current 
flow  V  along the loop  K1  to get 
 
 
 BS(V)(y)  =  ∫K1  Lyx—1 V(x) × ∇y ϕ0(x, y)  ds    
 
 
 
 
 
   — 1/4π2 ∫K1  Lyx—1 V(x)  ds 
 
 
 
 
 
 
     +  2 ∇y ∫K1  Lyx—1 V(x) ∙ ∇y ϕ1(x, y)  ds , 
 
where    ϕ0(α)  =  (—1/4π2) (π — α) cot α    and     ϕ1(α)  =  (—1/16π2) α (2π — α) . 
 
Note that 
 
           Lyx—1 V(x) ∙ ∇y ϕ1(x, y)  =  — V(x) ∙ ∇xϕ1(x, y) 
 
                                                   =  — dx/ds ∙ ∇xϕ1(x(s), y)   
 
                                                   =  —  (d/ds) ϕ1(x(s), y) , 
 
whose integral around the loop  K1  is zero.  So we can drop the third integral 
and are left with 
 
 
 BS(V)(y)  =  ∫K1  Lyx—1 V(x) × ∇y ϕ0(x, y)  ds    
 
 
 
 
 
   — 1/4π2 ∫K1  Lyx—1 V(x)  ds . 
 
 
 
 
Then we compute the circulation of  BS(V)  around the loop  K2 ,  as follows. 
 
∫K2  BS(V)(y) ∙ dy/dt  dt   
 
  =  ∫K2  (∫K1  Lyx—1 V(x) × ∇y ϕ0(x, y)  ds  — 1/4π2 ∫K1  Lyx—1 V(x)  ds) ∙ dy/dt  dt 
 
                                          =  ∫K1×K2  Lyx—1dx/ds × ∇y ϕ0(x, y) ∙ dy/dt  ds dt 
 
                          —  1/4π2
 ∫K1×K2  Lyx—1dx/ds  ∙  dy/dt  ds dt 
 
                                          =  —∫K1×K2  Lyx—1dx/ds × dy/dt  ∙ ∇y ϕ0(x, y)  ds dt 
 
                                                               —  1/4π2
 ∫K1×K2  Lyx—1dx/ds  ∙  dy/dt  ds dt , 
 
where we still have  ϕ0(α)  =  (—1/4π2) (π — α) cot α , 
 
                                           =  1/4π2 ∫K1×K2  Lyx—1dx/ds × dy/dt  ∙∇y ϕ0(x, y)  ds dt 
 
                                                               —  1/4π2
 ∫K1×K2  Lyx—1dx/ds  ∙  dy/dt  ds dt , 
 
where now  ϕ0(α)  =  (π — α) cot α . 
 
We apply Ampere's Law to the field  BS(V) ,  as indicated in the previous section,  
and conclude that 
 
              Lk(K1 , K2)  =  1/4π2 ∫K1×K2  Lyx—1dx/ds × dy/dt  ∙ ∇y ϕ0(x, y)  ds dt 
 
                                                     —  1/4π2
 ∫K1×K2  Lyx—1dx/ds  ∙  dy/dt  ds dt . 
 
The assumption that the loop  K1  is simple, which we needed to get an embedded 
tubular neighborhood, can now be dropped, since the linking number does not 
change as either curve crosses itself, and the value of the integral depends 
continuously on the curves  K1  and  K2 . 
 
The assumption that the loop  K1  is parametrized by arc length can also be dropped, 
since the two integrals on the right hand side above are independent of parametriza- 
tion of either curve, as long as these parametrizations respect the give orientations. 
 
This completes the proof of Theorem 1, formula (1) for the Gauss linking integral 
on  S3  in left-translation format.
