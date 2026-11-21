---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-012-13-upper-bounds-for-helicity-in-r3-s3-and-h3
section_title: "Upper bounds for helicity in R3 , S3 and H3 ."
section_number: 13
pages: 32-34
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
toc_source: inferred
doc_brief: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 16 sections: Front matter; Linking integrals in S3 and H3 .; Historical background."
---
Let  Ω  be a compact, smoothly bounded subdomain of  R3 ,  S3  or  H3 ,  and  V  a 
smooth vector field defined on  Ω .  Thinking of  V as a current flow, its magnetic 
field  BS(V)  is defined by the same formulas as before, except that the integration is 
carried out only over  Ω .   
 
If  Ω  ⊂  R3 ,  then 
 
BS(V)(y)  =  ∫Ω  V(x) × ∇y ϕ(x, y)  dx , 
 
where  ϕ(α)  =  —1/(4πα) . 
 
If  Ω  ⊂  S3 ,  then, for example in parallel transport format, we have 
 
BS(V)(y)  =  ∫Ω  PyxV(x) × ∇y ϕ(x, y)  dx , 
 
where  ϕ(α)  =  (—1/(4π2)) (π — α) csc α .   
 
If  Ω  ⊂  H3 ,  then we have 
 
BS(V)(y)  =  ∫Ω  PyxV(x) × ∇y ϕ(x, y)  dx , 
 
where  ϕ(α)  =  (—1/(4π)) csch α . 
 
The magnetic field  BS(V)  is defined throughout the ambient space.  It is continuous 
everywhere, but its first derivatives suffer a discontinuity as one crosses the boundary 
of  Ω .  This is a familiar situation from electrodynamics in Euclidean 3-space. 
 
In what follows, we will restrict  BS(V)  to  Ω ,  and ignore its behavior outside this 
domain. 
 
Let  VF(Ω)  denote the space of all smooth vector fields on  Ω ,  with the L2 inner 
product 
 
< V , W >  =  ∫Ω  V ∙ W  d(vol) , 
 
and associated energy  < V , V >  and norm  |V|  =  < V , V > 1/2  . 
 
We seek a bound for the energy or norm of the output magnetic field  BS(V)  on  Ω  in 
terms of that of the input current flow  V .  Or to put it another way, we seek an 
upper bound for the L2 operator norm of the Biot-Savart operator,  
 
BS :  VF(Ω)  →  VF(Ω) , 
 
in terms of the geometry of the underlying domain  Ω . 
 
As a consequence, we will determine an upper bound for the helicity   
H(V)  =  < BS(V) , V >  of the vector field  V  in terms of its energy  < V , V >  
and the geometry of  Ω . 
 
THEOREM 7.  Let  Ω  be a compact, smoothly bounded subdomain of  R3 ,  S3   
or  H3 ,  and let  R  =  R(Ω)   be the radius of a ball in that space having the same 
volume as  Ω .  Let  V  be a smooth vector field defined on  Ω  .  Then 
 
|BS(V)|  ≤  N(R) |V| , 
 
where in  R3  we have  N(R)  =  R ; 
 
           in  S3  we have  N(R)  =  (1/π) (2(1 — cos R)  +  (π — R) sin R) ; 
 
           in  H3  we have  N(R)  =  sinh R . 
 
It follows immediately that the helicity  H(V)  =  < BS(V), V >  is bounded by 
 
|H(V)|  ≤  N(R) |V|2 . 
 
The proof in  R3  appears in our "upper bounds" paper (2000).  Using the formulas  
for  BS(V)  provided in Theorem 2 above,  the arguments in  S3  and  H3  are then 
substantially the same as in that paper. 
 
Here are three observations. 
 
∙  In  R3 ,  the overestimate  N(R)  =  R  for the norm of  BS  grows like the  
cube root of the volume  (4/3)πR3  of  Ω .    
 
∙  By contrast, in  H3 ,  the overestimate  N(R)  =  sinh R  for the norm of  BS  
grows like the square root of the volume  2π(sinh R  cosh R  —  R)  of  Ω . 
 
∙  In  S3 ,  the overestimate  N(π)  =  4/π  for the norm of  BS  on the entire 3-sphere 
can be compared with the known exact value,  |BS|  =  1/2 .
