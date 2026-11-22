---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-033-30-step-2---finding-and-using-the-kernel-functio
section_title: "Step 2 - Finding and using the kernel function ϕ3 ."
section_number: 30
pages: 65-69
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Continuing our calculation of the Laplacian of  A(V, ϕ2)(y) ,  we have 
       
           ∆y A(V, ϕ2)(y)  =  V(y)  —  G(V, ϕ0)(y)   +  ∇y(∇y ∙ A(V, ϕ2)(y))  
 
                                     =  V(y)  —  G(V, ϕ0)(y)  +  G(V, ψ)(y)  +  G(V, ϕ2)(y) 
 
                                     =  V(y)  —  G(V, ϕ0  —  ϕ2  —  ψ)(y) . 
 
We note that 
 
ϕ0  —  ϕ2  —  ψ  =  (—1/4π2) (π — α) cot α 
 
                                    +  (1/4π2) (π — α) csc α  —  (1/8π2) (π — α)2 / (1 + cos α) 
 
                                         + (1/4π2) (π — α)2 / (1 + cos α) 
 
                         =  (1/4π2) (π — α) (1 — cos α) / sin α   +   (1/8π2) (π — α)2 / (1 + cos α) . 
 
Now let  ϕ3(α)  be chosen to satisfy 
 
∆ϕ3(α)  =  ϕ0  —  ϕ2  —  ψ  +  C 
 
              =  (1/4π2) (π — α) (1 — cos α) / sin α   +   (1/8π2) (π — α)2 / (1 + cos α)  +  C , 
 
where the constant  C  is chosen to make the right hand side have average value  zero 
over  S3 ,  and where the function  ϕ3(α)  has a singularity at  α = 0  but not at  α = π . 
 
 
 
 
 
 
 
We have yet to calculate  ϕ3  explicitly, but once this is done, we will have 
 
∆yG(V, ϕ3)(y)  =  G(V, ∆ϕ3)(y)  =  G(V, ϕ0 — ϕ2 — ψ)(y) ,  
 
and hence 
 
∆y {A(V, ϕ2)(y)  +  G(V, ϕ3)(y)} 
 
                              =  ∆y A(V, ϕ2)(y)  +  ∆y G(V, ϕ3)(y) 
 
                              =  ∆y A(V, ϕ2)(y)  +  G(V, ∆ϕ3)(y) 
 
          =  V(y)  —  G(V, ϕ0 — ϕ2 — ψ)(y)  +  G(V, ϕ0 — ϕ2 — ψ)(y) 
 
                              =  V(y) . 
 
Therefore, if we define 
 
           Gr(V)(y)  =  A(V, ϕ2)(y)  +  G(V, ϕ3)(y) 
 
                           =  ∫S3  PyxV(x)  ϕ2(x, y)  dx   +   ∇y ∫S3  PyxV(x) ∙ ∇yϕ3(x, y)  dx , 
 
we have                           
 
         ∆y Gr(V)(y)  =  V(y) , 
 
as desired.   
 
This completes the proof of Theorem 3, formula (2) for the vector-valued Green's 
operator on  S3 ,  modulo the explicit determination of the kernel function  ϕ3 . 
 
We break the calculation of  ϕ3  into three pieces. 
 
 
 
 
 
 
 
First piece.   
 
Let   
 
ϕ0(α)  =  (—1/4π2) (π — α) cot α 
 
be the fundamental solution of the Laplacian on  S3 , 
 
∆ϕ0  =  δ  —  1/2π2 . 
 
The average value of  ϕ0  over  S3  is  [ϕ0]  =  —1/8π2 . 
 
If we define 
Φ0(α)  =  (—1/16π2) α (2π — α) , 
 
then we have 
∆Φ0  =  ϕ0  —  [ϕ0] . 
 
 
Second piece.   
 
Let  
 
ϕ1(α)  =  (—1/4π2) (π — α) csc α 
 
be the kernel function for the Biot-Savart operator on  S3  in parallel transport 
format.  The average value of ϕ1  over  S3  is  [ϕ1]  =  —1/2π2 . 
 
If we define 
Φ1(α)  =  (—1/4π2) (π — α) (1  —  cos α) / sin α , 
 
then we have 
∆Φ1  =  ϕ1  —  [ϕ1] . 
 
 
 
 
 
 
 
Third piece.   
 
Let   
 
ψ(α)  =  (1/8π2) (π — α)2 / (1  +  cos α) , 
 
which is the right-most term in the expression for  ∆ϕ3  in the statement of 
Theorem 3, formula (2) . 
 
The average value of  ψ  over  S3  is   
 
[ψ]  =  —1/2π2  +  1/12 . 
 
If we find the function  Ψ(α)  which satisfies 
 
∆Ψ  =  ψ  —  [ψ] , 
 
and which has no singularity at  α  =  π ,  then 
 
ϕ3  =  Φ0  —  Φ1  +  Ψ 
 
satisfies 
 
∆ϕ3  =  (ϕ0  —  [ϕ0])  —  (ϕ1  —  [ϕ1])  +  (ψ  —  [ψ]) , 
 
and is the kernel function we are seeking.
