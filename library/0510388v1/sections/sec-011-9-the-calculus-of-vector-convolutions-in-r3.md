---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-011-9-the-calculus-of-vector-convolutions-in-r3
section_title: "The calculus of vector convolutions in R3 ."
section_number: 9
pages: 24-27
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Let  α  =  |x — y|  denote the distance between the points  x  and  y  in  R3 ,  and 
let  ϕ(α)  be some unspecified function of  α .  As usual, we'll write  ϕ(x, y)  in 
place of  ϕ(α(x, y))  for simplicity. 
 
Let  V  be a smooth vector field defined on  R3  and having compact support. 
Keeping the function  ϕ  unspecified, we define vector fields  A(V, ϕ)  and   
B(V, ϕ) ,  a scalar function  g(V, ϕ)  and another vector field  G(V, ϕ)  as follows. 
 
 
A(V, ϕ)(y)  =  ∫R3  V(x) ϕ(x, y)  dx 
 
 
B(V, ϕ)(y)  =  ∫R3  V(x) × ∇y ϕ(x, y)  dx 
 
 
g(V, ϕ)(y)  =  ∫R3  V(x) ∙ ∇y ϕ(x, y)  dx 
 
 
G(V, ϕ)(y)  =  ∇y g(V, ϕ)(y)  =  ∇y ∫R3  V(x) ∙ ∇y ϕ(x, y)  dx . 
 
If we use the fundamental solution  ϕ0(α)  =  —1/(4πα)  of the scalar Laplacian as  
the kernel in the above convolutions, then  A(V, ϕ0)  gives the Green's operator, and 
if we think of  V  as a current flow, then  B(V, ϕ0)  is the resulting magnetic field,   
— A(V, ϕ0)  is its vector potential,  and  — G(V, ϕ0)  is the rate of change  ∂E/∂t  of 
the electric field, caused by the accumulation and dissipation of charge by the 
current flow  V . 
 
 
 
 
 
The curl and divergence of the vector fields  A(V, ϕ)  and  B(V, ϕ)  are given by 
 
LEMMA 1.     ∇ × A(V, ϕ)  =  — B(V, ϕ) 
 
          ∇ ∙ A(V, ϕ)  =  g(V, ϕ) 
 
 
 
    ∇ × B(V, ϕ)  =  A(V, ∆ϕ)  —  G(V, ϕ)       ∇ ∙ B(V, ϕ)  =  0 . 
 
Proof.  The proofs are exercises in differentiating under the integral sign and then 
using the various Leibniz rules from vector calculus.  We will show the brief 
arguments for the first and last of the four formulas above, since these two will 
change when we move to the 3-sphere.  The other two formulas, whose proofs we 
leave to the reader, are the same in  R3  and  S3 . 
 
To begin with the first formula, 
 
          ∇y × A(V, ϕ)(y)  =  ∫R3  ∇y × {V(x) ϕ(x, y)}  dx 
 
                                          =  ∫R3  (∇y × V(x)) ϕ(x, y)  —  V(x) × ∇y ϕ(x, y)  dx 
 
                                          =  — ∫R3  V(x) × ∇y ϕ(x, y)  dx 
 
                                          =  — B(V, ϕ)(y) , 
 
as claimed,  since  ∇y × V(x)  =  0 .  When we move to  S3 ,  the corresponding term 
will not be zero. 
 
As for the last formula, 
 
∇y ∙ B(V, ϕ)(y)  =  ∫R3  ∇y ∙ {V(x) × ∇y ϕ(x, y)}  dx 
 
                            =  ∫R3  (∇y × V(x)) ∙ ∇y ϕ(x, y)  —  V(x) ∙ (∇y × ∇y ϕ(x, y))  dx 
 
                            =  0 , 
 
as claimed, because   ∇y × V(x)  =  0   and   ∇y × ∇y ϕ(x, y)  =  0 .  Again, when  
we move to  S3 ,  the expression corresponding to  ∇y × V(x)  will not be zero. 
 
 
 
 
 
Comment. 
 
If we use the fundamental solution  ϕ0  of the Laplacian as our kernel, think of  V  
as a current flow and  B(V, ϕ0)  as its magnetic field, we get 
 
                       ∇ × B(V, ϕ0)  =  A(V, ∆ϕ0)  —  G(V, ϕ0) , 
 
which is Maxwell's equation, 
 
                               ∇ × B  =  V  +  ∂E/∂t . 
 
 
Now we turn to the Laplacians of our convolutions. 
 
LEMMA 2.         ∆A(V, ϕ)  =  A(V, ∆ϕ) 
 
∆B(V, ϕ)  =  B(V, ∆ϕ) 
 
                           
∆g(V, ϕ)  =  g(V, ∆ϕ) 
 
∆G(V, ϕ)  =  G(V, ∆ϕ) . 
 
Proof.   
 
The arguments are straightforward, using the formula for the vector Laplacian, 
the information from Lemma 1, and the fact that Laplacian and gradient commute. 
We write it out for the first formula, and leave the other three to the reader. 
 
                   ∆A(V, ϕ)  =  — ∇ × ∇ × A(V, ϕ)  +  ∇(∇ ∙ A(V, ϕ)) 
 
                                      =  — ∇ × (— B(V, ϕ))  +  ∇g(V, ϕ) 
 
                                      =  A(V, ∆ϕ)  —  G(V, ϕ)  +  G(V, ϕ) 
 
                                      =  A(V, ∆ϕ) .
