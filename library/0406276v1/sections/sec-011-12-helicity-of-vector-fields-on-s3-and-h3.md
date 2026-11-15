---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-011-12-helicity-of-vector-fields-on-s3-and-h3
section_title: "Helicity of vector fields on S3 and H3 ."
section_number: 12
pages: 30-32
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
toc_source: inferred
doc_brief: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 16 sections: Front matter; Linking integrals in S3 and H3 .; Historical background."
---
If  V  is a smooth vector field on  R3  with compact support,  then the Woltjer-
Moffatt formula for its helicity, 
 
H(V)  =  1/(4π) ∫ R3 × R3   V(x) × V(y) ∙ (x — y)/|x — y|3  dx dy , 
 
can be written succinctly as 
 
H(V)  =  ∫ R3  BS(V)(y) ∙ V(y)  dy . 
 
This is how Woltjer originally presented his invariant,  ∫A ∙ B d(vol) ,  with the 
role of  V  played by the magnetic field  B  and the role of  BS(V)  played by its 
vector potential  A .  The helicity of a vector field, as we mentioned earlier, is a 
measure of the extent to which its orbits wrap and coil around one another. 
 
We use the above formula to define the helicity of a vector field  V  on  S3  or  H3 ,  
and then immediately obtain explicit integral formulas from Theorem 2.  
 
THEOREM 6.  HELICITY INTEGRALS  in  S3  and  H3 . 
 
(1)  On  S3  in left-translation format: 
___ 
      H(V)  =  ∫S3×S3  Lyx—1 V(x) × V(y) ∙ ∇y ϕ0(x, y)  dx dy     
               
              — 1/(4π2) ∫S3×S3  Lyx—1V(x) ∙ V(y)  dx dy    
                                
                                          +  2 ∫S3×S3 ∇y (Lyx—1 V(x) ∙ ∇y ϕ1(x, y)) ∙ V(y)  dx dy , 
 
where     ϕ0(α)  =  (1/(4π2)) (π—α) cot α     and     ϕ1(α)  =  (—1/(16π2)) α (2π—α) . 
 
(2)  On  S3  in parallel transport format: 
 
H(V)  =  ∫S3×S3  Pyx V(x)  ×  V(y)  ∙  ∇y ϕ(x, y)  dx dy , 
 
where     ϕ(α)  =  (1/(4π2)) (π — α) csc α . 
 
(3)  On  H3  in parallel transport format: 
 
H(V)  =  ∫H3×H3  Pyx V(x)  ×  V(y)  ∙  ∇y ϕ(x, y)  dx dy , 
 
where     ϕ(α)  =  (1/(4π)) csch α . 
 
 
∙ In formula (1), if  V  is divergence-free, then the third integral in the definition 
of  H(V)  vanishes. 
 
 
∙ In formulas (1) and (2), if the smooth vector field  V  on  S3  is divergence-free, 
then its helicity is the same as its asymptotic (or mean) Hopf invariant, as defined 
by Arnold (1974), and is invariant under the group of volume-preserving diffeo- 
morphisms of  S3 . 
 
 
∙ In formula (3), we assume that  V  has compact support, in order to guarantee 
convergence of the integral. 
 
 
∙ If  V  is a left-invariant unit vector field on  S3 , recall that  BS(V)  =  — ½ V .   
Then its helicity is given by 
 
                     H(V)  =  ∫S3  BS(V)(y) ∙ V(y)  dy 
 
 
 
 
=  ∫S3  — ½ V(y) ∙ V(y)  dy   
 
                               =  — ½ vol(S3)  =  — ½ (2π2)  
 
                               =  — π2 .   
 
If  V  is a right-invariant unit vector field on  S3 ,  then  BS(V)  =  ½ V ,  and hence 
 
                     H(V)  =  + π2 .
