---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-007-6-vector-valued-greens-operators-in-r3-s3-and-h3
section_title: "Vector-valued Green's operators in R3 , S3 and H3 ."
section_number: 6
pages: 17-21
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
The vector Laplacian in  R3 ,  S3  and  H3 , 
 
∆V  =  — ∇ × ∇ × V  +  ∇(∇ ∙ V) , 
 
corresponds to the Laplacian on 1-forms, 
 
∆β  =  (dδ  +  δd)β , 
 
where  δ  =  ±* d *  ,  with  *  the Hodge star operator, in the following sense. 
Given the vector field  V ,  if we define the 1-form  ↓V  by  (↓V)(W)  =  V ∙ W ,   
then we get  ∆(↓V)  =  ↓(∆V) .  The symbol  ↓  reminds us of lowering indices 
in tensor notation. 
 
In  R3 ,  the vector Laplacian can be computed component-wise in rectangular 
coordinates. 
 
If  V  is a smooth compactly supported vector field in  R3 ,  then the Green's 
operator acting on  V  is given by the convolution formula 
 
Gr(V)(y)  =  ∫R3  V(x) ϕ0(x, y)  dx , 
 
where  ϕ0(α)  =  —1/(4πα)  is the fundamental solution of the Laplacian.  It has 
the following properties: 
 
(1)  ∆ Gr(V)  =  V . 
 
(2)  Gr(V)(y)  →  0  as  y  →  ∞ . 
 
In  R3 ,  S3  and  H3 ,  a linear operator satisfying conditions (1) and (2) above 
will be referred to as a vector-valued Green's operator. 
 
 
 
 
 
 
 
Comments. 
 
 
∙  In  R3 ,  conditions (1) and (2) are easily seen to characterize the Green's operator,  
as follows.  The difference  Gr1(V)  —  Gr2(V)  between two candidates for the  
Green's operator is a harmonic vector field, and therefore its three components in 
rectangular coordinates are harmonic functions.  By property (2), they go to zero at 
infinity and hence must be identically zero.  Thus  Gr1(V)  =  Gr2(V) . 
 
 
∙  In  R3 ,  the statement that  Gr(V)(y)  →  0  as  y  →  ∞  can be improved: 
Gr(V)(y)  →  0  at infinity like  1/|y|  in general, and if  V  is divergence-free, then  
it goes to zero at infinity like  1/|y|2 .  See our paper (2001) on the Biot-Savart operator. 
 
 
∙  In  S3 ,  condition (1) alone suffices to characterize the Green's operator, since 
the vector Laplacian  ∆: VF(S3)  →  VF(S3)  is bijective. 
 
 
∙  In  S3 ,  because the vector Laplacian is bijective and commutes with grad, curl 
and div, we immediately get the same for the scalar and vector-valued Green's 
operators: 
 
∇ Gr(f)  =  Gr(∇f)  ,     ∇ × Gr(V)  =  Gr(∇ × V)  ,     ∇ ∙ Gr(V)  =  Gr(∇ ∙ V) . 
 
 
∙  In  H3 ,  it is not yet clear to us how to characterize the vector-valued Green's 
operator.  Even strengthening (2) to require that  Gr(V)(y)  goes to zero exponentially 
fast at infinity is not quite enough.   
 
 
The following theorem asserts the existence of vector-valued Green's operators  
in  S3  and  H3 ,  and provides explicit integral formulas. 
 
 
 
 
 
 
 
 
 
 
 
THEOREM 3.  GREEN'S OPERATORS  in  S3  and  H3 . 
 
Vector-valued Green's operators exist in  S3  and  H3 ,  and are given by the 
following formulas, in which  V  is a smooth, compactly supported vector field: 
 
(1)  On  S3  in left-translation format: 
 
 
    Gr(V)(y)  =   ∫S3  Lyx—1 V(x) ϕ0(x, y)  dx 
 
 
 
                        +  2 ∫S3  Lyx—1 V(x) × ∇y ϕ1(x, y)  dx   
 
 
 
                                  +  4 ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ2(x, y)  dx , 
 
where 
 
 
 
ϕ0(α)  =  (—1/4π2) (π—α) cot α 
 
 
 
ϕ1(α)  =  (—1/16π2) α (2π—α) 
 
 
 
ϕ2(α)  =  (—1/192π2) (3α(2π—α) + 2α(π—α)(2π—α)cot α) , 
 
and these three kernel functions are related by 
 
                               ∆                        
                        
                        
                        ∆                        
                        
                        
                        ∆ 
ϕ2        →  ϕ
  ϕ
  ϕ
  ϕ1        —  [ϕ
  [ϕ
  [ϕ
  [ϕ1]  
]  
]  
]  →  ϕ
  ϕ
  ϕ
  ϕ0  —  [ϕ0]  →  δ  —  [δ] . 
 
 
 
 
(2)  On  S3  in parallel transport format: 
 
Gr(V)(y)  =   ∫S3  PyxV(x)  ϕ2(x, y)  dx   +   ∇y∫S3  PyxV(x) ∙ ∇yϕ3(x, y)  dx , 
 
where 
 
       ϕ
       ϕ
       ϕ
       ϕ2(α)  =  (—1/4π2) (π — α) csc α  +  (1/8π2) (π — α)2 / (1 + cos α) 
 
and  
 
       ϕ3(α)  =  (—1/24) (π — α) cot α  —  (1/16π2) α (2π — α) 
 
                                +  (1/8π2) ∫α
π  ((π — α)3 / (3 sin2α))  +  ((π — α)2 / sin α)   dα .
α .
α .
α . 
 
 
(3)  On  H3  in parallel transport format: 
 
Gr(V)(y)  =   ∫S3  PyxV(x)  ϕ2(x, y)  dx   +   ∇y∫S3  PyxV(x) ∙ ∇yϕ3(x, y)  dx , 
 
where 
 
       ϕ2(α)  =  (—1/4π) csch α  +  (1/4π) α / (1 + cosh α) 
 
and  
 
       ϕ3(α)  =  (1/4π) α / (e2α
 — 1)  +  (1/4π) ∫0
α ((α / sinh α)  —  (α2 / 2 sinh2α))  dα .
α .
α .
α . 
 
 
Comment.  In formula (2), the third term in the expression for the kernel function  
ϕ3(α)  is left as a definite integral because it is a non-elementary function involving 
polylogarithms of indices 2  and  3 ,  where the polylogarithm of index  s  is 
defined by 
polylog(s, x)  =  Lis(x)  =  ∑n≥1  xn / ns . 
 
In formula (3), the second term in the expression for the kernel function  ϕ3(α)  is 
left as a definite integral because it is a non-elementary function involving 
dilogarithms, that is, polylogarithms of index 2.
