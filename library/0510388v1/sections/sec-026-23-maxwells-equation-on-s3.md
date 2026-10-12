---
doc_id: 0510388v1
doc_title: "ELECTRODYNAMICS and the GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE Dennis DeTurck and Herman Gluck"
section_id: sec-026-23-maxwells-equation-on-s3
section_title: "Maxwell's equation on S3 ."
section_number: 23
pages: 53-55
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
---
We now apply the Key Lemma to the proof of Maxwell's equation 
 
∇ × B  =  V  +  ∂E/∂t  
 
on  S3 .  In the Key Lemma, we use the kernel function 
 
ϕ(α)  =  (—1/4π2) (π — α) csc α , 
 
which, as we noted earlier, is a fundamental solution of the shifted Laplacian on  S3 , 
 
∆ϕ  —  ϕ  =  δ . 
 
With this choice of kernel function, we have that 
 
(cos α) ϕ(α)  =  ϕ0(α)  =  (—1/4π2) (π — α) cot α , 
 
which is the fundamental solution of the Laplacian on  S3 , 
 
∆ϕ0  =  δ  —  1/(2π2) .  
 
With these choices, the Key Lemma reads 
 
     ∇y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x ϕ0}   
 
                                                                 =  δ(x, y) (V(x)  —  < V(x), y > y) .  
 
Keeping these choices of kernel functions, we now define the Biot-Savart operator 
by formula (2) of Theorem 2, 
 
BS(V)(y)  =  ∫S3  PyxV(x) × ∇y ϕ(x, y) dx . 
 
Then we integrate the Key Lemma over  S3  and get 
 
   ∫S3  ∇y × {PyxV(x) × ∇yϕ} dx   —   ∫S3  ∇y {V(x) ∙ ∇x ϕ0}  dx 
 
                                                          =   ∫S3  δ(x, y) (V(x)  —  < V(x), y > y)  dx . 
 
 
54 
 
 
 
 
The integral on the right hand side above equals   
 
V(y)  —  < V(y), y > y  =  V(y) , 
 
since  V(y) is a tangent vector to  S3  at  y ,  and hence orthogonal to  y  in  R4 . 
 
Taking the curl and the gradient outside the two integrals on the left-hand side,  
we then get 
 
∇y × ∫S3  PyxV(x) × ∇yϕ(x, y)  dx   —   ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx   =   V(y) , 
 
or 
∇y × BS(V)(y)  =  V(y)  +  ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx . 
 
As indicated in section 3, this is Maxwell's equation 
 
∇ × B  =  V  +  ∂E/∂t . 
 
This explains our remark in section 19 that, for this special choice of kernel 
function  ϕ ,  the Key Lemma can be viewed as a pointwise or infinitesimal  
version of Maxwell's equation. 
 
 
 
55
