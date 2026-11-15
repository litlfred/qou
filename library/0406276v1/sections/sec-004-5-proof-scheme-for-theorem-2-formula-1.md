---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-004-5-proof-scheme-for-theorem-2-formula-1
section_title: "Proof scheme for Theorem 2, formula (1)."
section_number: 5
pages: 12-15
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
toc_source: inferred
doc_brief: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 16 sections: Front matter; Linking integrals in S3 and H3 .; Historical background."
---
Let  VF(S3)  denote the set of all smooth (C∞) vector fields on  S3 ,  regarded as an 
infinite-dimensional vector space with the L2 inner product   
 
<V, W>  =  ∫S3  V ∙ W  d(vol) . 
 
The vector Laplacian, 
 
∆V  =  — ∇ × ∇ × V  +  ∇(∇ ∙ V) , 
 
corresponds to the Laplacian on forms, 
 
∆βV  =  — *d*d βV  +  d*d* βV  , 
 
where the one-form  βV  is defined by  βV(W)  =  V ∙ W .   
 
The vector Laplacian  ∆: VF(S3)  →  VF(S3)  is an unbounded self-adjoint linear 
operator which is bijective, and which takes divergence-free fields to divergence- 
free fields, and gradient fields to gradient fields. 
 
The Green's operator  Gr: VF(S3)  →  VF(S3)  is defined to be the inverse of the 
vector Laplacian.  It is a bounded self-adjoint linear operator which takes 
divergence-free fields to divergence-free fields and gradient fields to gradient 
fields. 
 
Let  V  be a smooth vector field on  S3 .  Thinking of  V  as a steady current flow,  
we define the corresponding magnetic field, and the Biot-Savart operator  BS ,  by 
 
BS(V)  =  — ∇ × Gr(V) . 
 
It is easy to check that the magnetic field  BS(V)  satisfies the four properties 
required of it in the preceding section. 
 
Once we get an explicit formula for the Green's operator  Gr(V) ,  the negative of 
its curl will lead to the desired explicit formula for  BS(V) .  This in turn will lead 
us in section 9 to the linking integral formula given in Theorem 1, part (1). 
 
The fact that an explicit formula for the Green's operator can lead (via a different 
route) to an explicit formula for the linking integral was known to de Rham (1960, 
section 33).  The issue is to find the formula for the Green's operator, and we turn 
now to showing how to do this on  S3 . 
 
 
Working in left-translation format, it is natural to hope, by analogy with  R3 ,  that 
 
A(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) ϕ(x, y)  dx 
 
will be the Green's operator on  S3  when we choose  ϕ  to be the fundamental 
solution of the Laplacian.  But it doesn't work out this way. 
 
However,  ϕ  is not the only possible kernel function, and  A(V, ϕ)  is not the only 
way of convolving a vector field with a kernel to get another vector field. 
 
Consider the convolutions 
 
 
 
A(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) ϕ(x, y)  dx 
 
 
 
B(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) × ∇y ϕ(x, y)  dx   
 
 
 
G(V, ϕ)(y)  =  ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ(x, y)  dx . 
 
In  R3 ,  if we let  ϕ  be the fundamental solution of the scalar Laplacian, then the 
convolution  A(V, ϕ)  gives the Green's operator,  B(V, ϕ)  gives the magnetic 
field, and  G(V, ϕ)  gives the  ∂E/∂t  term in Maxwell's equation. 
 
On  S3 ,  it turns out that a linear combination of all three types of vector convo-
lution, each with a different kernel function  ϕ ,  will give the Green's operator. 
 
To prove this, we develop a "calculus of vector convolutions" in left-translation 
format, in which we compute formulas for curls, divergences and Laplacians of 
convolutions of types  A ,  B  and  G .  The key formulas are the following: 
 
 
 
∆A(V, ϕ)  =  A(V, ∆ϕ)       —  4 A(V, ϕ)     —  2 B(V, ϕ) 
 
 
 
∆B(V, ϕ)  =  B(V, ∆ϕ)        +  2 A(V, ∆ϕ)  —  2 G(V, ϕ) 
 
 
 
∆G(V, ϕ)  =  G(V, ∆ϕ) . 
 
The large spaces after the first terms on the right hand sides of the  A  and  B  lines 
serve as a reminder that in Euclidean space  R3 ,  only those first terms appear. 
In particular, in  R3  we have  ∆A(V, ϕ)  =  A(V, ∆ϕ) .  So naturally, when we 
choose  ϕ  to be a fundamental solution of the scalar Laplacian in  R3 ,  we get 
∆A(V, ϕ)  =  A(V, δ)  =  V ,  which tells us that  A(V, ϕ)  =  Gr(V)  there. 
 
 
 
On the 3-sphere  S3 ,  we get the Green's operator by adding one copy of line A 
to two copies of line B and four copies of line G, each with a different choice of 
kernel function  ϕ ,  as follows.   
 
 
THEOREM 3.  On  S3  in left-translation format, the Green's operator on vector 
fields is given by 
 
 
    Gr(V)(y)  =   ∫S3  Lyx—1 V(x) ϕ0(x, y)  dx 
 
 
 
                        +  2 ∫S3  Lyx—1 V(x) × ∇y ϕ1(x, y)  dx   
 
 
 
                                  +  4 ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ2(x, y)  dx , 
 
where 
 
 
 
ϕ0(α)  =  (—1/(4π2)) (π—α) cot α 
 
 
 
ϕ1(α)  =  (—1/(16π2)) α (2π—α) 
 
 
 
ϕ2(α)  =  (—1/(192π2)) (3α(2π—α) + 2α(π—α)(2π—α)cot α) , 
 
and these three kernel functions are related by 
 
                             ∆                       ∆                      ∆ 
ϕ2  →  ϕ1  —  [ϕ1]  →  ϕ0  —  [ϕ0]  →  δ  —  [δ] . 
 
 
The negative curl of the above formula for the Green's operator, 
 
BS(V)  =  — ∇ × Gr(V) , 
 
leads to formula (1) of Theorem 2 for the Biot-Savart operator on  S3 .
