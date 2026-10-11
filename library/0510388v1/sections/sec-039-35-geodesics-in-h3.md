---
doc_id: 0510388v1
doc_title: "ELECTRODYNAMICS and the GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE Dennis DeTurck and Herman Gluck"
section_id: sec-039-35-geodesics-in-h3
section_title: "Geodesics in H3 ."
section_number: 35
pages: 75-76
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
---
Let  x  ∊  H3 ,  so that  < x , x >  =  1 ,  and suppose that  v  is a unit vector tangent 
to  H3  at  x ,  so that  < x, v >  =  0  and  < v , v >  =  —1 .  Consider the curve 
 
G(t)  =  cosh t  x  +  sinh t  v , 
 
which we easily check to lie in  H3  and to be parametrized by arc length.   
 
If we complete  v  to an orthonormal basis  v , u , w  of  TxH3 ,  then the linear 
map of  R1,3  that fixes  x  and  v  but sends  u  and  w  to  —u  and  —w  is an 
isometry of  H3  whose fixed point set is the curve  G .  As usual in Riemannian 
geometry, this tells us that  G  is a geodesic. 
 
The inner product  < x , G(t) >  =  cosh t  is the hyperbolic cosine of the distance  t   
in  H3  from  x  to  G(t) .  More generally, if  x  and  y  are any two points of  H3 ,  the 
inner product  < x , y >  is the hyperbolic cosine of the distance in  H3  between them. 
 
Now let  x  and  y  be any pair of distinct points in  H3 .  Then the vector 
v  =  y  —  < x , y > x  is nonzero and orthogonal to  x ,  so that  v  ∊  TxH3 .   
Moreover,  |v|2  =  < v , v >  =  1  —  < x , y >2  <  0 ,  so  v ∙ v  =  < x , y >2  —  1  >  0 , 
and hence  v / |v|  is a unit vector tangent to  H3  at  x .  Therefore the unique, 
length-minimizing geodesic from  x  to  y  is given by 
 
G(t)  =  cosh t  x  +  sinh t  (v / |v|) . 
 
If  α  is the distance from  x  to  y  in  H3 ,  so that  cosh α  =  < x , y > ,  then 
we can rewrite this as 
 
G(t)  =  cosh t  x  +  sinh t  ((y  —  cosh α  x) / sinh α) . 
 
When  t  =  α ,  we have  G(α)  =  y  and 
 
                       G'(α)  =  sinh α  x  +  cosh α  ((y  —  cosh α  x) / sinh α) 
 
                                  =  (cosh α  y  —  x) / sinh α . 
 
Since  G  is parametrized by arc-length and is length-minimizing, and  α  is the  
distance in  H3  from  x  to  y ,  we deduce that 
 
                      ∇y α(x, y)  =  G'(α)  =  (cosh α  y  —  x) / sinh α . 
 
We note that   
                                      Pxy ∇y α(x, y)  =  — ∇x α(x, y) . 
 
 
76
