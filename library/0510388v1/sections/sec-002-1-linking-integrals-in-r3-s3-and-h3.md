---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-002-1-linking-integrals-in-r3-s3-and-h3
section_title: "Linking integrals in R3 , S3 and H3 ."
section_number: 1
pages: 3-7
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Let  K1  =  {x(s)}  and  K2  =  {y(t)}  be disjoint oriented smooth closed curves in 
either Euclidean 3-space  R3 ,  the unit 3-sphere  S3  or hyperbolic 3-space  H3 ,   
and let  α(x, y)  denote the distance from  x  to  y .  
 
                        
 
 
                                                            Two linked curves 
                                
                                                                                                            
The linking number of these two curves is defined to be the intersection number of 
either one of them with an oriented surface bounded by the other.  It is understood 
that the ambient space is also oriented.  The linking number depends neither on the 
choice of surface, nor on which of the curves is used to bound the surface. 
 
 
 
 
Carl Friedrich Gauss, in a half-page paper dated January 22, 1833, gave an integral  
formula for the linking number in Euclidean 3-space, 
 
Lk(K1, K2)  =  1/(4π) ∫K1×K2  dx/ds × dy/dt ∙ (x — y)/|x — y|3  ds dt . 
 
It will be convenient for us to write this as 
 
Lk(K1, K2)  =  1/(4π) ∫K1×K2  dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt , 
 
where  ϕ(α)  =  1/α ,  and where we use  ϕ(x, y)  as an abbreviation for  ϕ(α(x, y)) .  
The subscript  y  in the expression  ∇y ϕ(x, y)  tells us that the differentiation is  
with respect to the  y  variable. 
 
The following theorem gives the corresponding linking integrals on the 3-sphere 
and in hyperbolic 3-space.  Since the location of tangent vectors is now important, 
we note that the vector  ∇y ϕ(x, y)  is located at the point  y . 
 
 
THEOREM 1.  LINKING INTEGRALS  in  S3  and  H3 . 
 
(1)  On  S3  in left-translation format: 
 
         Lk(K1, K2)  =  1/(4π2) ∫K1×K2  Lyx—1 dx/ds × dy/dt ∙ ∇y ϕ
 ϕ
 ϕ
 ϕ(x, y)  ds dt 
 
                     —  1/(4π2) ∫K1×K2  Lyx—1 dx/ds ∙ dy/dt  ds dt  , 
 
where     ϕ(α)  =  (π — α) cot α . 
 
(2)  On  S3  in parallel transport format: 
 
         Lk(K1, K2)  =  1/(4π2) ∫K1×K2  Pyx dx/ds × dy/dt ∙ ∇y ϕ
 ϕ
 ϕ
 ϕ(x, y)  ds dt , 
   
where     ϕ(α)  =  (π — α) csc α . 
 
(3)  On  H3  in parallel transport format: 
 
         Lk(K1, K2)  =  1/(4π)
π)
π)
π) ∫K1×K2  Pyx dx/ds × dy/dt ∙ ∇y ϕ
 ϕ
 ϕ
 ϕ(x, y)  ds dt , 
 
where     ϕ(α)  =  csch α
 α
 α
 α . 
 
 
 
 
 
 
 
 
The kernel functions used here have the following significance. 
 
In Gauss's linking integral, the function  ϕ0(α)  =  —1/(4πα) ,  where  α  is distance  
from a fixed point, is the fundamental solution of the Laplacian in  R3 , 
 
∆ϕ0  =  δ . 
 
Here  δ  is the Dirac δ-function. 
 
In formula (1), the function  ϕ0(α)  =  (—1/4π2) (π — α) cot α  ,  is the fundamental 
solution of the Laplacian on  S3 , 
 
∆ϕ0  =  δ  —  1/2π2 . 
 
Since the volume of  S3  is  2π2 ,  the right-hand side has average value zero. 
 
In formula (2), the function  ϕ(α)  =  (—1/4π2) (π — α) csc α  is the fundamental  
solution of a shifted Laplacian on  S3 , 
 
∆ϕ  —  ϕ  =  δ . 
 
In formula (3), the function  ϕ(α)  =  (—1/4π) csch α  is the fundamental solution  
of a shifted Laplacian on  H3 , 
 
∆ϕ  +  ϕ  =  δ . 
 
 
Note on typesetting.  In fractions such as  1/4π ,  (—1/4π2)  or  1/2π2 ,   
                                   the  π  and the  π2  are always in the denominator. 
 
 
 
 
 
 
 
 
Comments. 
 
∙  For two linked circles in a small ball, the first integral in formula (1) is the 
dominant term.  At the other extreme, for orthogonal great circles, say, the first 
integral vanishes and the second integral takes the value  ±1.  In 3-space, the  
analogue of the second integral would be 
 
∫K1×K2  dx/ds ∙ dy/dt  ds dt  =  (∫K1  dx/ds  ds) ∙ (∫K2  dy/dt  dt)  =  0 ∙ 0  =  0 , 
 
and therefore does not appear in the classical Gauss linking integral. 
 
 
∙  In formula (2), it makes no difference that parallel transport from  x  to  y  on  S3 
is ambiguous when  y  is the antipode  —x  of  x ,  because when  α  =  π  we have 
∇y(ϕ(α(x, y))  =  0 . 
 
 
∙  The integrand in Gauss's formula, and the integrands in formulas (1), (2) and 
(3), are invariant under orientation-preserving isometries of the ambient space.  In  
Gauss's formula, this is clear.  In formula (1), this follows from the fact that the 
group of left translations by unit quaternions is a normal subgroup of the group  
SO(4)  of all orientation-preserving isometries of  S3 .  In formulas (2) and (3),  
this is again clear. 
 
 
∙  The fact that formula (1) on  S3  has no counterpart in  H3  is due to the simplicity 
of the group  SO(1, 3)  of orientation-preserving isometries of  H3 . 
 
 
∙  Greg Kuperberg, after receiving a copy of the announcement of these results,  
wrote to us, "As it happens, I thought about this question a few years ago and I 
obtained one of your formulas, I think, but I never wrote it up."  Subsequent corres-
pondence shows that he did indeed obtain, by a beautiful geometric argument totally 
different from ours, an expression equivalent to formula (2).
