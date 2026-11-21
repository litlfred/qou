---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-006-7-proof-scheme-for-theorem-2-formula-3
section_title: "Proof scheme for Theorem 2, formula (3)."
section_number: 7
pages: 18-20
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
toc_source: inferred
doc_brief: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 16 sections: Front matter; Linking integrals in S3 and H3 .; Historical background."
---
We replace  R4   by Minkowski space  R1,3  with the indefinite inner product 
 
< x, y >  =  x0 y0  —  x1 y1  —  x2 y2  —  x3 y3 , 
 
and then regard hyperbolic 3-space as the hyperboloid 
 
H3  =  { x  ∊  R1,3 :  < x, x >  =  1  and  x0  >  0 }  ⊂  R1,3 . 
 
 
 
If  u  and  v  are tangent to  H3  at  x ,  we define the induced inner product  ∙   
on  TxH3  by 
u ∙ v  =  — < u, v > . 
 
This time we exploit the interplay between the geometry of  H3  and the linear 
algebra of  R1,3  to prove the following 
 
KEY LEMMA, hyperbolic version. 
 
     ∇y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x (cosh α  ϕ)}   
 
                                                                 =  (∆ϕ  +  ϕ) (V(x)  —  < V(x), y > y) .  
 
Comparing the Key Lemmas in  S3  and  H3 ,  we see that the only changes are that 
cos α  has been replaced by  cosh α  on the left-hand side, and  ∆ϕ  —  ϕ  has been 
replaced by  ∆ϕ  +  ϕ  on the right-hand side. 
 
 
 
 
After proving the Key Lemma for  H3 ,  we apply it using the kernel function 
 
ϕ(α)  =  (—1/(4π)) csch α , 
 
which, as we noted earlier, is a fundamental solution of the shifted Laplacian on  H3 , 
 
∆ϕ  +  ϕ  =  δ . 
 
With this choice of kernel function, we have 
 
(cosh α) ϕ(α)  =  ϕ0(α)  =  (—1/(4π)) coth α , 
 
which is the fundamental solution of the Laplacian on  H3 , 
 
∆ϕ0  =  δ .  
 
With these choices, the Key Lemma reads 
 
     ∇y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x ϕ0}   
 
                                                                 =  δ(x, y) (V(x)  —  < V(x), y > y) .  
 
When we define the Biot-Savart operator by formula (3) of Theorem 2, 
 
BS(V)(y)  =  ∫H3  PyxV(x) × ∇y ϕ(x, y) dx , 
 
and follow the line of reasoning from the previous section, we obtain Maxwell's 
equation 
 
∇ × B  =  J  +  ∂E/∂t , 
 
and learn that  BS(V)  satisfies the four properties required of it in section 4.
