---
doc_id: 0510388v1
doc_title: "ELECTRODYNAMICS and the GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-005-14-geodesics-in-s
section_title: "Geodesics in S"
section_number: 14
pages: 36-38
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
doc_brief: "ELECTRODYNAMICS and the GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 10 sections: Magnetic fields in R; Vector-valued Green’s operators in; IN LEFT-TRANSLATION FORMAT"
---
3 . 
 
If  x , y  ∊  R4 ,  we will write  < x , y >  for the standard Euclidean inner product 
 
< x , y >  =  x0 y0  +  x1 y1  +  x2 y2  +  x3 y3 
 
in  R
4 .  Then 
 
S3  =  { x ∊ R4 :  < x , x >  =  1} . 
 
We will freely identify points in  R4  with the vectors at the origin that point to 
them, and we will also identify the tangent spaces at various points in  R4  in the 
usual way, so that we can say  v  ∊  Tx S3  if and only if  < x , v >  =  0 .  We will 
always write  < v , w >  for the inner product of vectors when we’re thinking of 
them as belonging to  R4 ,  and reserve the notation  v ∙ w  for the induced inner 
product on  Tx S3 . 
 
Suppose  x ∊ S3  so that  < x , x >  =  1 ,  and suppose  v  is a unit vector tangent 
to  S3  at  x ,  so that  < x , v >  =  0  and  < v , v >  =  1 .  Then the great circle 
 
G(t)  =  cos t  x  +  sin t  v 
 
is a geodesic in  S3  parametrized by arc length.   
                                                                                                   
Since  < x , G(t) >  =  cos t ,  we have that for any pair of points  x , y  ∊  S3 ,   
their inner product  < x , y >  is equal to the cosine of the distance (along  S3)  
from   x  to  y . 
 
 37 
 
 
 
Now let  x  and  y  be any pair of distinct, non-antipodal points in  S3 . 
Then the vector  v  =  y  —  < x , y > x  is nonzero and orthogonal to  x ,  and 
|v|2  =  < v , v >  =  1  —  < x , y >2 .  Therefore the unique, length-minimizing 
geodesic from  x  to  y  is given by 
 
G(t)  =  cos t  x  +  sin t  (v / |v|) . 
 
If  α   is the distance from  x  to  y ,  so that  cos α   =  < x , y > ,  then we can 
rewrite this as 
 
G(t)  =  cos t  x  +  sin t  
((y  —  cos α   x) / sin α ) . 
 
When  t  =  α  ,  we have  G(α )  =  y  and 
 
                          G’(α )  =  — sin α   x  +  cos α  ((y  —  cos α   x) / sin α ) 
 
                                     =  (cos α   y  —  x) / sin α  . 
 
Because  G  is parametrized by arc-length and is length-minimizing, and  α   is 
the distance in  S3  from  x  to  y ,  we deduce that 
 
∇y α (x, y)  =  G’(α )  =  (cos α   y  —  x) / sin α  . 
 
                                 
  
                           The gradient vectors of  αααα (x, y)  at  x  and at  y    
                                                  
                                               
We note that 
 
Pxy ∇y α (x, y)  =  —  ∇x α (x, y) . 
 
 
 38
