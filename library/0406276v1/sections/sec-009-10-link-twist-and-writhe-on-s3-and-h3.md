---
doc_id: 0406276v1
doc_title: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-009-10-link-twist-and-writhe-on-s3-and-h3
section_title: "Link, twist and writhe on S3 and H3 ."
section_number: 10
pages: 24-28
source_pdf: 0406276v1.pdf
source_sha256: 8fdf4b5950e8b5f5
toc_source: inferred
doc_brief: "The GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 16 sections: Front matter; Linking integrals in S3 and H3 .; Historical background."
---
We follow Calugareanu's lead and replace the two closed curves  K1  and  K2  in our 
linking integrals by a single closed curve  K ,  which we must assume to be simple.   
Now the points  x(s)  and  y(t)  run along the same curve, and therefore can coincide, 
making three out of the four linking integrals appearing in Theorem 1 seem improper  
(the second integral on  S3  in left-translation format is clearly proper).  But as 
Calugareanu noted for the corresponding  R3 integral, the three threatening integrands 
actually vanish along the diagonal of  K × K ,  so the integrals converge.  The resul- 
ting value  Wr(K)  is a real number called the writhing number of  K .  It is, as we 
mentioned earlier, a measure of the extent to which  K  wraps and coils around itself. 
 
DEFINITION of the WRITHING INTEGRALS in  S3  and  H3 . 
 
(1)  On  S3  in left-translation format: 
 
           WrL(K)  =defn  1/(4π2)∫K×K  Lyx—1 dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt 
 
                     —  1/(4π2)∫K×K  Lyx—1 dx/ds ∙ dy/dt  ds dt  , 
 
where     ϕ(α)  =  (π — α) cot α . 
 
(2)  On  S3  in parallel transport format: 
 
 
WrP(K)  =defn  1/(4π2)∫K×K  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x,y)  ds dt , 
 
where     ϕ(α)  =  (π — α) csc α . 
 
(3)  On  H3  in parallel transport format: 
 
 
WrP(K)  =defn  1/(4π) ∫K×K  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x,y)  ds dt , 
 
where     ϕ(α)  =  csch α . 
 
The two versions of the writhing number on  S3  are not the same, and one can show 
that 
WrL(K)  =  WrP(K)  +  L/(2π) , 
 
where  L  is the length of the closed curve  K .  The parallel transport version of 
writhe is the more intuitively satisfying, since in this version the writhing number 
of a great circle is zero. 
 
 
 
We turn next to the definition of "twist". 
 
Let  K  be a smooth simple closed curve in  S3  or  H3 ,  parametrized by arc length  s ,  
with  0  ≤  s  ≤  L .   Let  x(s)  be a moving point along  K ,  and  T(s)  =  x'(s)  the unit 
tangent vector field. 
 
Let  V(s)  be a unit normal vector field along  K .  Our intention is to define the (total) 
twist of  V  along  K  by a formula such as 
 
Tw(V)  =  1/(2π) ∫K  T(s) × V(s) ∙ V'(s)  ds , 
 
as in Euclidean 3-space. 
 
 
But on  S3  there are two flavors of twist, according as  V'(s)  is calculated as a  
"left-invariant" derivative or a covariant derivative.  If we fall back into Euclidean  
mode and write 
 
V'(s)  =  limh→0 (V(s + h)  —  V(s)) / h , 
 
then the vectors  V(s + h)  and  V(s)  lie in different tangent spaces, and we must 
move them together in order to subtract.  If we use left-translation in the group  S3   
to move  V(s + h)  back to the tangent space at  x(s)  which contains  V(s) ,  then the 
resulting limit is the left-invariant derivative  V'L(s) .  If we use parallel transport to 
move  V(s + h)  back, then the resulting limit is the covariant derivative V'P(s) . 
 
 
 
 
The two flavors of twist on  S3  are then given by 
 
(1)                             TwL(V)  =  1/(2π) ∫K  T(s) × V(s) ∙ V'L(s)  ds  
 
and 
 
(2)                             TwP(V)  =  1/(2π) ∫K  T(s) × V(s) ∙ V'P(s)  ds . 
 
It is an easy exercise to prove that 
 
TwL(V)  =  TwP(V)  —  L/(2π) , 
 
where  L  is the length of the curve  K . 
 
 
 
Example.  Consider the great circle  K  =  {(cos s ,  sin s ,  0 ,  0):  0  ≤  s  ≤  2π} 
on  S3 ,  and along it the unit normal vector field  V(s)  =  (0 ,  0 ,  cos s ,  sin s) . 
Then we have  TwL(V)  =  0  and  TwP(V)  =  1 . 
 
 
 
In hyperbolic 3-space  H3 ,  we have only the parallel transport version of twist, 
 
(3)                             TwP(V)  =  1/(2π) ∫K  T(s) × V(s) ∙ V'P(s)  ds . 
 
 
 
 
Now consider in  S3  or  H3  a narrow ribbon of width  ε  obtained by starting with 
a simple closed curve  K  =  {x(s)}  and then exponentiating a unit normal vector 
field  V(s)  along  K .  One edge of this ribbon is the original curve  K ,  and the 
other edge is the curve  Kε  =  {yε(s)} ,  given explicitly by 
 
 
 
yε(s)  =  cos ε  x(s)  +  sin ε  V(s) 
 
in  S3 ; 
 
 
 
yε(s)  =  cosh ε  x(s)  +  sinh ε  V(s) 
 
in  H3 . 
 
The vector field  V(s)  then points "across" the ribbon.                                    
 
 
THEOREM 5.  LINK  =  TWIST  +  WRITHE  in  S3  and  H3 . 
 
(1)  On  S3  in left-translation format:        
 
 
 
               Lk(K, Kε)  =  TwL(V)  +  WrL(K) . 
 
(2)  On  S3  in parallel transport format:    
 
                                  Lk(K, Kε)  =  TwP(V)  +  WrP(K) . 
 
(3)  On  H3  in parallel transport format:   
 
                                   Lk(K, Kε)  =  TwP(V)  +  WrP(K) .
