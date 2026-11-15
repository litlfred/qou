---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-000-1-linking-integrals-in-s3-and-h3
section_title: "Linking integrals in S3 and H3 ."
section_number: 1
pages: 2-4
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
toc_source: inferred
doc_brief: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 16 sections: Front matter; Linking integrals in S3 and H3 .; Historical background."
---
Let  K1  =  {x(s)}  and  K2  =  {y(t)}  be disjoint oriented smooth closed curves in 
either the unit 3-sphere  S3  or hyperbolic 3-space  H3 ,  and let  α(x, y)  denote the 
distance from  x  to  y .   
 
The integral formulas below contain vectors lying in different tangent spaces; in 
non-Euclidean settings we must move them to a common location to be combined. 
In  S3  regarded as the group of unit quaternions, the differential  Lyx—1  of left 
translation by  yx—1 moves tangent vectors from  x  to  y .  In either  S3  or  H3 , 
parallel transport  Pyx  along the geodesic segment from  x  to  y  also does this. 
 
 
THEOREM 1.  LINKING INTEGRALS  in  S3  and  H3 . 
 
(1)  On  S3  in left-translation format: 
 
         Lk(K1, K2)  =  1/(4π2) ∫K1×K2  Lyx—1 dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt 
 
                     —  1/(4π2) ∫K1×K2  Lyx—1 dx/ds ∙ dy/dt  ds dt  , 
 
where     ϕ(α)  =  (π — α) cot α . 
 
(2)  On  S3  in parallel transport format: 
 
         Lk(K1, K2)  =  1/(4π2) ∫K1×K2  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt , 
   
where     ϕ(α)  =  (π — α) csc α . 
 
(3)  On  H3  in parallel transport format: 
 
         Lk(K1, K2)  =  1/(4π) ∫K1×K2  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt , 
 
where     ϕ(α)  =  csch α . 
 
For each of the kernel functions  ϕ(α)  above, we have written  ϕ(x, y)  in place of 
ϕ(α(x, y)) . 
 
 
∙  The kernel functions appearing in these integrals have the following significance. 
 
 
In formula (1), the function  ϕ(α)  =  (—1/(4π2)) (π — α) cot α  ,  where  α  is 
 
distance from a fixed point, is the fundamental solution of the Laplacian on  S3 , 
 
∆ϕ  =  δ  —  1/(2π2) . 
 
 
Here  δ  is the Dirac δ-function, and, since the volume of  S3  is  2π2 ,  the right- 
 
hand side has average value zero. 
 
 
In formula (2), the function  ϕ(α)  =  (—1/(4π2)) (π — α) csc α  is the fundamental 
 
solution of a shifted Laplacian on  S3 , 
 
∆ϕ  —  ϕ  =  δ . 
 
 
In formula (3), the function  ϕ(α)  =  (—1/(4π)) csch α  is the fundamental 
 
solution of a shifted Laplacian on  H3 , 
 
∆ϕ  +  ϕ  =  δ . 
 
∙  In formula (1), the first integral is the dominant term when the curves are small. 
At the other extreme, for orthogonal great circles, say, the first integral vanishes 
and the second integral takes the value  ±1.  In 3-space, the second integral always 
vanishes. 
 
∙  In formula (2), it makes no difference that parallel transport from  x  to  y  on  S3 
is ambiguous when  y  is the antipode  —x  of  x ,  because when  α  =  π  we have 
∇y(ϕ(α(x, y))  =  0 . 
 
∙  All of the integrands in formulas (1), (2) and (3) are invariant under orientation- 
preserving isometries of the ambient space.  In formula (1), this follows from the 
fact that the group of left translations by unit quaternions is a normal subgroup of 
the group  SO(4)  of all orientation-preserving isometries of  S3 .  In formulas (2) 
and (3), this is transparent. 
 
∙  The fact that formula (1) on  S3  has no counterpart in  H3  is due to the simplicity 
of the group  SO(3, 1)  of orientation-preserving isometries of  H3 . 
 
∙  Greg Kuperberg, after receiving a copy of this research announcement, wrote to 
us, "As it happens, I thought about this question a few years ago and I obtained one 
of your formulas, I think, but I never wrote it up."  Subsequent correspondence shows 
that he did indeed obtain, by a beautiful geometric argument totally different from 
ours, an expression equivalent to formula (2).
