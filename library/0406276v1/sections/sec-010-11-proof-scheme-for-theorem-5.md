---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-010-11-proof-scheme-for-theorem-5
section_title: "Proof scheme for Theorem 5."
section_number: 11
pages: 28-30
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
toc_source: inferred
doc_brief: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 16 sections: Front matter; Linking integrals in S3 and H3 .; Historical background."
---
In spirit, our proof of Theorem 5 for ribbons in  S3  and  H3  follows Calugareanu's 
original proof in  R3 :  we begin with the linking integrals given in Theorem 1 for 
the edges  K  and  Kε  of our ribbon, let  ε  shrink to zero, and observe the behavior 
of the linking integrand. 
 
Of course, the value of the linking integral is independent of  ε  for  ε  >  0 ,  since 
the linking number is invariant under this kind of homotopy.  But the linking  
integrand develops a δ-function type singularity along the diagonal of  K × K ,   
which is handled as follows.   
 
Outside an appropriately chosen neighborhood of the diagonal, the linking integrand 
converges to the writhing integrand as  ε  →  0 ,  and its integral converges to the 
writhing number of the curve  K .  Inside this neighborhood of the diagonal, the 
linking integrand blows up, but its integral converges to the total twist of the normal 
vector field  V  along  K . 
 
The crucial thing, recognized by Calugareanu, is that the width of the neighborhood 
of the diagonal in  K × K  must go to zero much more slowly than the width  ε  of the 
ribbon.  In fact, we will choose the neighborhood of the diagonal to have width  εp , 
where  0  <  p  <  1/3 . 
 
To give a sense of this in action, we will outline here the proof of Theorem 5, 
part (2), dealing with  Link = Twist + Writhe  in parallel transport format on  S3 .   
The proofs for  H3  and for left-translation format on  S3  are essentially the same.   
In particular, in left-translation format, the integrand of the second integral in the 
expression for the linking number converges uniformly to the corresponding  
integrand for the writhing number. 
 
Consider, in parallel transport format on  S3 ,  the linking integrand of  K  with  Kε , 
 
 
Fε(s, t)  =  (1/(4π2)) dx/ds  ∙  Px(s)yε(t)(dyε/dt  ×  ∇yε(t) ϕ(α(x(s), yε(t)))) 
 
and the writhing integrand of  K , 
 
 
F0(s, t)  =  (1/(4π2)) dx/ds  ∙  Px(s)x(t)(dx/dt  ×  ∇x(t) ϕ(α(x(s), x(t)))) , 
 
where   ϕ(α)  =  (π  —  α) csc α . 
 
Then the linking number of  K  and  Kε  is given by 
 
                                         Lk(K, Kε)  =  ∫∫0 ≤ s,t ≤ L  Fε(s, t)  ds dt , 
 
and the writhing number of  K  is given by 
 
                                              WrP(K)  =  ∫∫0 ≤ s,t ≤ L  F0(s, t)  ds dt . 
 
Since  α(x, y)  is the distance between  x  and  y ,  and since  ϕ  has a singularity 
just at  α  =  0 ,  the only difficulty in considering the convergence of the linking  
integral as  ε → 0  happens near the diagonal, where  s  =  t . 
 
To handle this, we first show that because the singularity of  ϕ''(α)  at  α = 0  is like  
1/α3 ,  we have that for sufficiently small  ε > 0 , 
 
|Fε(s, t)  —  F0(s, t)|  ≤  C ε1—3p  , 
 
provided that  |s — t|  ≥  εp .   
 
If  0  <  p  <  1/3 ,  then  1 — 3p  >  0 ,  and hence  C ε1—3p  →  0  as  ε  →  0 . 
Therefore  Fε(s, t)  converges uniformly to  F0(s, t)  in the region  |s — t|  ≥  εp .   
Since the writhing integrand  F0(s, t)  remains bounded even along the diagonal,  
this shows that 
 
∫∫|s—t| ≥ εp  Fε(s, t)  ds dt   →   ∫∫0 ≤ s,t ≤ L  F0(s, t)  ds dt  =  WrP(K) , 
 
as  ε →  0 ,  that is, a portion of the linking integral converges to the entire writhing 
integral. 
 
The more delicate part of the argument is the integral near the diagonal.  A careful 
analysis using the Frenet equations reveals that for  0  <  p  <  1 , 
                                                      t+εp 
                         limε→0 ∫t—εp  Fε(s, t)  ds  =  (1/(2π)) x'(t) × V(t) ∙ V'P(t) . 
 
Hence 
 
∫∫|s—t| ≤ εp  Fε(s, t)  ds dt   →   ∫0 ≤ t ≤ L (1/(2π)) x'(t) × V(t) ∙ V'P(t)  dt  =  TwP(V) . 
 
That is, the remaining portion of the linking integral converges to the entire 
twisting integral.  In this way, we see that 
 
Lk(K, Kε)  =  TwP(V)  +  WrP(K) .
