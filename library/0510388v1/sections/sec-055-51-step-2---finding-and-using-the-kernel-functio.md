---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-055-51-step-2---finding-and-using-the-kernel-functio
section_title: "Step 2 - Finding and using the kernel function ϕ3 ."
section_number: 51
pages: 95-98
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Continuing our calculation of the Laplacian of  A(V, ϕ2)(y) ,  we have 
       
           ∆y A(V, ϕ2)(y)  =  V(y)  —  G(V, ϕ0)(y)   +  ∇y(∇y ∙ A(V, ϕ2)(y))  
 
                                     =  V(y)  —  G(V, ϕ0)(y)  +  G(V, ψ)(y)  +  G(V, ϕ2)(y) 
 
                                     =  V(y)  —  G(V, ϕ0  —  ϕ2  —  ψ)(y) . 
 
Using the values for  ϕ0 ,  ϕ2  and  ψ  given above, we calculate that 
 
ϕ0  —  ϕ2  —  ψ  =  (1/4π)  —  (1/4π) sinh α / (1 + cosh α)  +  (1/4π) α / (1 + cosh α) . 
 
Now let  ϕ3(α)  be chosen to satisfy 
 
            ∆ϕ3(α)  =  ϕ0  —  ϕ2  —  ψ 
 
                          =  (1/4π)  —  (1/4π) sinh α / (1 + cosh α)  +  (1/4π) α / (1 + cosh α) . 
 
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
 
                           =  ∫H3  PyxV(x)  ϕ2(x, y)  dx   +   ∇y ∫H3  PyxV(x) ∙ ∇yϕ3(x, y)  dx , 
 
we have                           
 
         ∆y Gr(V)(y)  =  V(y) , 
 
as desired. 
 
This completes the proof of Theorem 3, formula (3) for the vector-valued Green's 
operator in  H3 ,  modulo the explicit determination of the kernel function  ϕ3 . 
 
We break the calculation of  ϕ3  into two pieces, and begin by writing 
 
ϕ0  —  ϕ2  —  ψ  =  (1/4π)  —  (1/4π) sinh α / (1 + cosh α)  +  (1/4π) α / (1 + cosh α) . 
 
                         =                            ψ1                               +                    ψ2 . 
 
To solve the equation 
 
∆ϕ3  =  ϕ0  —  ϕ2  —  ψ  =  ψ1  +  ψ2 , 
 
we will solve separately the equations 
 
∆Ψ1  =  ψ1     and     ∆Ψ2  =  ψ2 , 
 
and then add these solutions together to get 
 
ϕ3  =  Ψ1  +  Ψ2 . 
 
 
 
 
 
 
First piece. 
 
If we define 
Ψ1(α)  =  (1/4π) α / (e2α
 — 1)  —  (1/4π) csch α , 
 
then 
∆Ψ1  =  (1/4π)  —  (1/4π) sinh α / (1 + cosh α)  =  ψ1 . 
 
 
Second piece. 
 
We want to solve the equation 
 
∆Ψ2  =  (1/4π) α / (1 + cosh α)  =  ψ2 . 
 
Following the procedure used on  S3  in section 31, we find that 
 
Ψ2  =  (1/4π) csch α  +  (1/4π) ∫0
α ((α / sinh α)  —  (α2 / 2 sinh2α))  dα . 
 
The integral in the second term is non-elementary and involves dilogarithms, 
so we simply leave it as is. 
 
Putting this all together, we have that 
 
        ϕ3  =  Ψ1  +  Ψ2 
 
              =  (1/4π) α / (e2α
 — 1)  —  (1/4π) csch α 
 
                        +  (1/4π) csch α  +  (1/4π) ∫0
α ((α / sinh α)  —  (α2 / 2 sinh2α))  dα  
 
              =  (1/4π) α / (e2α
 — 1)  +  (1/4π) ∫0
α ((α / sinh α)  —  (α2 / 2 sinh2α))  dα , 
 
thanks to one cancellation. 
 
This completes the proof of Theorem 3, formula (3) for the Green's operator in  H3 .
