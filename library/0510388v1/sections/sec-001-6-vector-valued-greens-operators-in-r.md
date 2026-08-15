---
doc_id: 0510388v1
doc_title: "ELECTRODYNAMICS and the GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-001-6-vector-valued-greens-operators-in-r
section_title: "Vector-valued Green’s operators in R"
section_number: 6
pages: 17-22
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
doc_brief: "ELECTRODYNAMICS and the GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 10 sections: Magnetic fields in R; Vector-valued Green’s operators in; IN LEFT-TRANSLATION FORMAT"
---
3 ,  S3  and  H3 . 
 
The vector Laplacian in  R3 ,  S3  and  H3 , 
 
∆V  =  — ∇ × ∇ × V  +  ∇(∇ ∙ V) , 
 
corresponds to the Laplacian on 1-forms, 
 
∆β  =  (dδ  +  δd)β , 
 
where  δ  =  –* d *  ,  with  *  the Hodge star operator, in the following sense. 
Given the vector field  V ,  if we define the 1-form  ↓V  by  (↓V)(W)  =  V ∙ W ,   
then we get  ∆(↓V)  =  ↓(∆V) .  The symbol  ↓  reminds us of lowering indices 
in tensor notation. 
 
In  R
3 ,  the vector Laplacian can be computed component-wise in rectangular 
coordinates. 
 
If  V  is a smooth compactly supported vector field in  R
3 ,  then the Green's 
operator acting on  V  is given by the convolution formula 
 
Gr(V)(y)  =  ∫R3  V(x) ϕ0(x, y)  dx , 
 
where  ϕ0(α )  =  —1/(4πα )  is the fundamental solution of the Laplacian.  It has 
the following properties: 
 
(1)  ∆ Gr(V)  =  V . 
 
(2)  Gr(V)(y)  →   0  as  y  →   ∞ . 
 
In  R
3 ,  S3  and  H3 ,  a linear operator satisfying conditions (1) and (2) above 
will be referred to as a vector-valued Green's operator. 
 
 
 18 
 
 
 
 
Comments. 
 
 
∙  In  R
3 ,  conditions (1) and (2) are easily seen to characterize the Green’s operator,  
as follows.  The difference  Gr1(V)  —  Gr2(V)  between two candidates for the  
Green’s operator is a harmonic vector field, and therefore its three components in 
rectangular coordinates are harmonic functions.  By property (2), they go to zero at 
infinity and hence must be identically zero.  Thus  Gr
1(V)  =  Gr2(V) . 
 
 
∙  In  R
3 ,  the statement that  Gr(V)(y)  →   0  as  y  →   ∞  can be improved: 
Gr(V)(y)  →   0  at infinity like  1/|y|  in general, and if  V  is divergence-free, then  
it goes to zero at infinity like  1/|y|2 .  See our paper (2001) on the Biot-Savart operator. 
 
 
∙  In  S
3 ,  condition (1) alone suffices to characterize the Green’s operator, since 
the vector Laplacian  ∆: VF(S3)  →   VF(S3)  is bijective. 
 
 
∙  In  S
3 ,  because the vector Laplacian is bijective and commutes with grad, curl 
and div, we immediately get the same for the scalar and vector-valued Green’s 
operators: 
 
∇ Gr(f)  =  Gr(∇f)  ,     ∇ × Gr(V)  =  Gr(∇ × V)  ,     ∇ ∙ Gr(V)  =  Gr(∇ ∙ V) . 
 
 
∙  In  H
3 ,  it is not yet clear to us how to characterize the vector-valued Green’s 
operator.  Even strengthening (2) to require that  Gr(V)(y)  goes to zero exponentially 
fast at infinity is not quite enough.   
 
 
The following theorem asserts the existence of vector-valued Green’s operators  
in  S
3  and  H3 ,  and provides explicit integral formulas. 
    
 
 
 
 
 
 19 
 
 
 
 
THEOREM 3.  GREEN’S OPERATORS  in  S
3  and  H3 . 
 
Vector-valued Green's operators exist in  S3  and  H3 ,  and are given by the 
following formulas, in which  V  is a smooth, compactly supported vector field: 
 
(1)  On  S3  in left-translation format: 
 
     Gr(V)(y)  =   ∫∫∫∫S3  Lyx—1 V(x) ϕϕϕϕ0(x, y)  dx 
 
                          +  2 ∫∫∫∫S3  Lyx—1 V(x) ×××× ∇∇∇∇y ϕϕϕϕ1(x, y)  dx      
 
                                    +  4 ∇∇∇∇y ∫∫∫∫S3  Lyx—1 V(x) ∙∙∙∙ ∇∇∇∇y ϕϕϕϕ2(x, y)  dx , 
 
where 
    
        ϕ ϕϕϕ0(αααα )  =  (—1/4ππππ2) (ππππ—αααα ) cot αααα  
 
        ϕ ϕϕϕ1(αααα )  =  (—1/16ππππ2) αααα  (2ππππ—αααα )    
 
        ϕ ϕϕϕ2(αααα )  =  (—1/192ππππ2) (3αααα (2ππππ—αααα ) + 2αααα (ππππ—αααα )(2ππππ—αααα )cot αααα ) , 
 
and these three kernel functions are related by 
 
                               ∆∆∆∆                                                                                                ∆∆∆∆                                                                                                ∆∆∆∆ ϕϕϕϕ2        →→→→  ϕ  ϕ  ϕ  ϕ1        —  [ϕ  [ϕ  [ϕ  [ϕ1]  ]  ]  ]  →→→→  ϕ  ϕ  ϕ  ϕ0  —  [ϕϕϕϕ0]  →→→→   δδδδ  —  [δδδδ] . 
 
 
 20 
 
(2)  On  S3  in parallel transport format: 
 
Gr(V)(y)  =   ∫∫∫∫S3  PyxV(x)  ϕϕϕϕ2(x, y)  dx   +   ∇∇∇∇y∫∫∫∫S3  PyxV(x) ∙∙∙∙ ∇∇∇∇yϕϕϕϕ3(x, y)  dx , 
 
where 
 
       ϕ       ϕ       ϕ       ϕ2(αααα )  =  (—1/4ππππ2) (ππππ — αααα ) csc αααα   +  (1/8ππππ2) (ππππ — αααα )2 / (1 + cos αααα ) 
 
and  
 
       ϕϕϕϕ
3(αααα )  =  (—1/24) (ππππ — αααα ) cot αααα   —  (1/16ππππ2) αααα  (2ππππ — αααα ) 
 
                                +  (1/8ππππ2) ∫∫∫∫αααα
ππππ  ((ππππ — αααα )3 / (3 sin2αααα ))  +  ((ππππ — αααα )2 / sin αααα ))))   dα .α .α .α .    
 
 
(3)  On  H3  in parallel transport format: 
 
Gr(V)(y)  =   ∫∫∫∫S3  PyxV(x)  ϕϕϕϕ2(x, y)  dx   +   ∇∇∇∇y∫∫∫∫S3  PyxV(x) ∙∙∙∙ ∇∇∇∇yϕϕϕϕ3(x, y)  dx , 
 
where 
 
       ϕϕϕϕ2(αααα )  =  (—1/4ππππ) csch αααα   +  (1/4ππππ) αααα  / (1 + cosh αααα ) 
 
and  
 
       ϕϕϕϕ3(αααα )  =  (1/4ππππ) αααα  / (e2αααα
 — 1)  +  (1/4ππππ) ∫∫∫∫0
αααα ((αααα  / sinh αααα )  —  (αααα 2 / 2 sinh2αααα ))  dα .α .α .α .    
 
 
Comment.  In formula (2), the third term in the expression for the kernel function  
ϕ
3(α )  is left as a definite integral because it is a non-elementary function involving 
polylogarithms of indices 2  and  3 ,  where the polylogarithm of index  s  is 
defined by 
polylog(s, x)  =  Li
s(x)  =  ∑n≥1  xn / ns . 
 
In formula (3), the second term in the expression for the kernel function  ϕ
3(α )  is 
left as a definite integral because it is a non-elementary function involving 
dilogarithms, that is, polylogarithms of index 2. 
 
 
 21 
 
7. Classical electrodynamics and Maxwell’s equations on  S3  and  H3 . 
 
As mentioned in section 2, our route to the Gauss linking integral begins by 
developing a steady-state version of classical electrodynamics. 
 
Maxwell’s equations, so familiar to us in Euclidean 3-space  R
3 ,  can also be shown 
to hold on  S3  and  H3 ,  with the appropriate definitions, as follows. 
 
Let  ρ  be a smooth real-valued function, which we think of as a charge density.  
On  R3  and  H3 ,  we ask that  ρ  have compact support, while on  S3  we ask that  
it have average value zero. 
 
In each case, we define the corresponding electric field  E  =  E(ρ)  by the formula 
 
E(ρ)(y)  =  ∇
y ∫ ρ(x) ϕ0(x, y) dx , 
 
where  ϕ0  is the fundamental solution of the Laplacian. 
 
Let  V  be a smooth vector field, which we think of as a steady-state (i.e., time- 
independent) current distribution.  On  R
3  and  H3 ,  we ask that  V  have compact 
support, while on  S3  we impose no restriction on  V . 
 
In each case, we define the corresponding magnetic field  B  =  BS(V)  by one of 
the formulas in Theorem 2.  Since  V  is steady-state, so is  B ,  and therefore 
∂B/∂t  =  0 . 
 
 
THEOREM 4.  MAXWELL’S EQUATIONS  in  S
3  and  H3 . 
 
With these definitions, Maxwell's equations,  
 
        ∇∇∇∇ ∙∙∙∙ E  =  ρρρρ     ∇∇∇∇ ×××× E  =  0    
 
  ∇∇∇∇ ∙∙∙∙ B  =  0     ∇∇∇∇ ××××  B  =  V  +  ∂E/∂t , 
 
hold on  S3  and in  H3 ,  just as they do in  R3 . 
 
 
Additionally, as in  R
3 ,  Ampere’s Law follows immediately from the last of the 
Maxwell equations and the curl theorem. 
 
 22 
 
 
    
 
B.  PROOFS ON  S
