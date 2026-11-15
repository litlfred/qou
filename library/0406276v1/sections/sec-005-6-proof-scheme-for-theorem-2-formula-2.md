---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-005-6-proof-scheme-for-theorem-2-formula-2
section_title: "Proof scheme for Theorem 2, formula (2)."
section_number: 6
pages: 15-18
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
toc_source: inferred
doc_brief: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 16 sections: Front matter; Linking integrals in S3 and H3 .; Historical background."
---
Now we are working on  S3  in parallel transport format, and use an entirely different 
approach. 
 
 
KEY LEMMA, spherical version. 
 
     ∇y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x (cos α  ϕ)}   
 
                                                                 =  (∆ϕ  —  ϕ) (V(x)  —  < V(x), y > y) .  
 
 
The above lemma is quite flexible:  V  can be a smooth vector field defined on all 
of  S3 ,  or just on a bounded subdomain  Ω  of  S3 ,  or just along a smooth closed 
curve  K  in  S3 ,  or even just at the single point  x .  The kernel function  ϕ(α)  is 
any smooth function, which typically blows up at  α = 0  and is asymptotic there to  
—1/(4πα) .  As usual,  α  =  α(x, y)  is the distance on  S3  between  x  and  y .  The 
dot product  ∙  on the left hand side of the above equation is in the tangent space to  
S3  at  x ,  while the inner product  < , >  on the right hand side is in  R4 . 
 
The proof of the lemma exploits the interplay between the geometry of  S3  and 
the linear algebra of the space  R4  in which it lies.  Here are four samples: 
 
∙  We define a triple vector product  [A, B, C]  in  R4 ,  whose value is a vector 
orthogonal to the 3-space spanned by  A ,  B  and  C ,  and whose length is the  
3-dimensional volume of the parallelepiped spanned by these three vectors.   
 
∙  If  u  and  v  are both tangent to  S3  at  x ,  then   u × v  =  [x, u, v] . 
 
∙  If  x  and  y  are points of  S3  and  V(x)  is tangent to  S3  at  x ,  then 
 
∇y × [x, V(x), y]  =  2 < x, y > V(x)  —  2 < V(x), y > x . 
 
∙  Under these same hypotheses, 
 
[y, x, [y, x, V(x)]]  =  — sin2α V(x)  +  < V(x), y > y  —  cos α  < V(x), y > x . 
 
 
 
 
Once the Key Lemma is proved, we apply it using the kernel function 
 
ϕ(α)  =  (—1/(4π2)) (π — α) csc α , 
 
which, as we noted earlier, is a fundamental solution of the shifted Laplacian on  S3 , 
 
∆ϕ  —  ϕ  =  δ . 
 
With this choice of kernel function, we have 
 
(cos α) ϕ(α)  =  ϕ0(α)  =  (—1/(4π2)) (π — α) cot α , 
 
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
 
The integral on the right hand side above equals   
 
V(y)  —  < V(y), y > y  =  V(y) , 
 
since  V(y) is a tangent vector to  S3  at  y ,  and hence orthogonal to  y  in  R4 . 
 
 
 
Taking the curl and the gradient outside the two integrals on the left-hand side,  
we then get 
 
∇y × ∫S3  PyxV(x) × ∇yϕ(x, y)  dx   —   ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx   =   V(y) , 
 
or 
 
∇y × BS(V)(y)  =  V(y)  +  ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx . 
 
Integrating by parts over  S3 ,  we have 
 
∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx  =  — ∫S3  ∇x ∙V(x)  ϕ0(x, y)  dx , 
 
and inserting this, we get 
 
∇y × BS(V)(y)  =  V(y)  — ∫S3  ∇x ∙V(x)  ϕ0(x, y)  dx . 
 
If we think of the vector field  V(x)  as a steady current, then the negative divergence,  
— ∇x ∙V(x) ,  is the time rate of accumulation of charge at  x ,  and hence the integral 
 
— ∫S3  ∇x ∙V(x)  ϕ0(x, y)  dx 
 
is the time rate of increase of the electric field at  y  (see section 8) .  Thus the above 
equation is Maxwell's equation 
 
∇ × B  =  J  +  ∂E/∂t . 
 
With this line of reasoning in mind, we view the Key Lemma, with our specific 
choice of kernel functions, as a pointwise version of Maxwell's equation. 
 
It is now easy to verify that  BS(V)  satisfies the four properties required of it in 
section 4. 
 
Remark.  Jason Parsley, in his thesis (2004), proves Maxwell's equation in the 
case that the current flow  J  runs only within some bounded subdomain  Ω  ⊂  S3 . 
In that situation, the  ∂E/∂t  term also reflects the time rate of change of the 
electric field due to the gradual deposit or removal of charge along the boundary  
of  Ω .  His proof of this in left-invariant format inspired our own arguments.
