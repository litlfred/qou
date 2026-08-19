---
doc_id: 0510388v1
doc_title: "ELECTRODYNAMICS and the GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-008-17-the-method-of-moving-frames-in-s
section_title: "The method of moving frames in S"
section_number: 17
pages: 40-107
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
doc_brief: "ELECTRODYNAMICS and the GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 10 sections: Magnetic fields in R; Vector-valued Green’s operators in; IN LEFT-TRANSLATION FORMAT"
---
3 . 
 
The computations which lead to the various integral formulas on  S3  in parallel 
transport format will be carried out using "moving frames" which are obtained via 
parallel transport from a single orthonormal frame, as follows. 
 
Let  x  =  (1, 0, 0, 0) ,  and let  X
1 ,  X2 ,  X3  be the usual orthonormal basis for the 
tangent space  TxS3  to  S3  at  x . 
                                            
For each point  y  =  (y0 , y1 , y2 , y3)  ≠  — x  in  S3
 ,  we parallel transport this 
orthonormal basis for  TxS3  along the unique shortest geodesic (great circle arc) 
from  x  to  y  to obtain an orthonormal basis 
 
E1  =  PyxX1 ,   E2  =  PyxX2 ,   E3  =  PyxX3 
 
for  TyS3 .   
                                      
  
                                                    Moving frames 
 
 41 
 
 
 
 
Using the formula for  P
yxV  from the previous section, we calculate that 
 
                 E1  =  (— y1 ,  1  —  y1
2/(1 + y0) ,  — y1y2/(1 + y0) ,  — y1y3/(1 + y0))  
 
                 E2  =  (— y2 ,  — y1y2/(1 + y0) ,  1  —  y2
2/(1 + y0) ,  — y2y3/(1 + y0)) 
 
                 E
3  =  (— y3 ,  — y1y3/(1 + y0) ,  — y2y3/(1 + y0) ,  1  —  y3
2/(1 + y0)) . 
 
 
Next, let  θ
1 ,  θ2 ,  θ3  denote the 1-forms on  S3  —  {—x}  which are dual to 
E1 ,  E2 ,  E3 ,  in the sense that  θi(V)  =  < Ei , V >  for all vectors  V  and for 
i  =  1, 2, 3. 
 
We can write 
 
    θ
1  =  — y1 dy0  +  (1  —  y1
2/(1 + y0)) dy1  —  y1y2/(1 + y0) dy2  —  y1y3/(1 + y0) dy3 
 
    θ2  =  — y2 dy0  —  y1y2/(1 + y0) dy1  +  (1  —  y2
2/(1 + y0)) dy2  —  y2y3/(1 + y0) dy3 
 
    θ3  =  — y3 dy0  —  y1y3/(1 + y0) dy1  —  y2y3/(1 + y0) dy2  +  (1  —  y3
2/(1 + y0)) dy3 , 
 
where we understand the right hand sides as restricted to  S
3 . 
 
Since   y0
2  +  y1
2  +  y2
2  +  y3
2  =  1   on  S3 ,  we can add a fourth equation to the 
three above, 
 
    0  =  y0 dy0  +  y1 dy1  +  y2 dy2  +  y3 dy3 . 
 
 42 
 
 
 
 
Using this fourth equation, we can simplify the first three to read 
 
    θ
1  =  — y1/(1 + y0) dy0  +  dy1 
 
    θ2  =  — y2/(1 + y0) dy0  +  dy2 
 
    θ
3  =  — y3/(1 + y0) dy0  +  dy3 . 
 
 
We then invert this system to obtain 
 
    dy
0  =  — y1 θ1  —  y2 θ2  —  y3 θ3 
 
    dy1  =  θ1  —  (y1/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3) 
 
    dy
2  =  θ2  —  (y2/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3) 
 
    dy3  =  θ3  —  (y3/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3) . 
 
 
With these equations in hand, we easily obtain 
 
    dθ
1  =  y2/(1 + y0)  θ1 ∧ θ2  —  y3/(1 + y0)  θ3 ∧ θ1 
 
    dθ
2  =  y3/(1 + y0)  θ2 ∧ θ3  —  y1/(1 + y0)  θ1 ∧ θ2 
 
    dθ3  =  y1/(1 + y0)  θ3 ∧ θ1  —  y2/(1 + y0)  θ2 ∧ θ3 . 
 
 
     
 
 
 43 
 
 
 
18. Curls and divergences. 
 
If  x  is a fixed point on  S3  and  V  is a tangent vector to  S3  at  x ,  then the parallel 
transport  PyxV  of  V  to the point  y  is defined for all  y  ≠  —x ,  and may be 
viewed as a vector field on  S3  —  {—x} ,  as illustrated in section 13. 
 
We need to know the curl and divergence of this vector field. 
 
 
PROPOSITION 18.1.     
                                                                       [y , x , V]                                           ∇
y  ×  PyxV  =  ——————————— .                                                                     1  +  < x , y > 
 
 
PROPOSITION 18.2. 
                               — 2 < y, V >                                          ∇y ∙ PyxV  =  —————————— .                                                                      1 + < x, y > 
 
 
To take curls and divergences of vector fields on an oriented Riemannian 3-manifold,  
we make use of the duality between vector fields and forms as follows. 
 
If  U  is a vector field, we can convert it to the dual 1-form  ↓U  which is defined by 
(↓U)(W)  =  < U , W >  for all vector fields  W .  If  µ  is a 1-form, we can convert it 
to the dual vector field  ↑µ  which is defined by  < ↑µ , W >  =  µ(W)  for all vector 
fields  W .  The down and up arrows remind us of lowering and raising indices in 
tensorial notation. 
 
If  U  is a vector field, we can convert it to the dual 2-form  ⇓U  which is defined by 
(⇓U)(Y, Z)  =  vol(U, Y, Z)  for all vector fields  Y  and  Z .  If  µ  is a 2-form, we can 
convert it to the dual vector field  ⇑µ  which is defined by  vol (⇑µ , Y, Z)  =  µ(Y, Z)  
for all vector fields  Y  and  Z . 
 
For example,  ↓E
i  =  θi   and  ↑θi  =  Ei   for  i  =  1, 2, 3.  Likewise  ⇓E1  =  θ2 ∧ θ3 ,  
⇓E2  =  θ3 ∧ θ1   and   ⇓E3  =  θ1 ∧ θ2 ,   and  ⇑  is simply the inverse of this. 
 
 44 
 
 
 
With these notations set, the curl of a vector field  W  is defined, as usual, by 
 
∇ × W  =  ⇑ d ↓ W , 
 
that is, we convert  W  to the 1-form  ↓W ,  take its exterior derivative to get the 
2-form  d ↓ W ,  and then convert this to the vector field  ⇑ d ↓ W . 
 
For example, suppose  W  is the vector field  E
1  =  PyxX1 .  Then 
 
       ∇y × E1  =  ⇑ d ↓ E1  =  ⇑ d θ1   
 
                        =  ⇑ (y2/(1 + y0)  θ1 ∧ θ2  —  y3/(1 + y0)  θ3 ∧ θ1) 
 
                        =  y
2/(1 + y0)  E3  —  y3/(1 + y0)  E2 . 
 
And likewise  
 
       ∇
y × E2  =  y3/(1 + y0)  E1  —  y1/(1 + y0)  E3 
 
       ∇
y × E3  =  y1/(1 + y0)  E2  —  y2/(1 + y0)  E1 . 
 
These formulas can be viewed as special instances of the formula given above in 
Proposition 18.1.  For example, if  y  =  (y
0 , y1 , y2 , y3 ) ,  x  =  (1, 0, 0, 0)  and 
V  =  X1 ,  then one easily calculates that 
 
      [y , x , V]  =  y
2 E3  —  y3 E2 .  
 
Dividing through by  1  +  < x, y >  =  1  +  y0  gives the formula for  ∇y × E1 
appearing above, and so verifies Proposition 18.1 in this instance. 
 
Both sides of the formula in Proposition 18.1 are linear in  V ,  so we can certainly 
rescale  V  to be a unit vector.  Also, both sides of this formula are invariant under 
an orientation preserving isometry of  S
3 ,  so we can move  x  to the point   
(1, 0, 0, 0)  and  V  to the tangent vector  E1 . 
 
Thus the above verification of Proposition 18.1 in this single instance also serves  
as its proof. 
 
 45 
 
 
 
The divergence of a vector field  W  is defined by 
 
∇ ∙ W  =  * d ⇓ W , 
 
where  *  is the Hodge star operator which converts the 3-form  f d(vol)  to the 
function  f .  Thus the divergence of the vector field  W  is calculated by converting 
it to the 2-form  ⇓ W ,  taking its exterior derivative to get the 3-form  d ⇓ W , 
and then converting this to the function  * d ⇓ W . 
 
For example, suppose  W  is the vector field  E
1  =  PyxX1 .  Then 
 
                       ∇ ∙ E1  =  * d ⇓ E1  =  * d (θ2 ∧ θ3) 
 
                                           =  * (dθ
2 ∧ θ3  —  θ2 ∧ dθ3) 
 
                                           =  * (—2 y1/(1 + y0)) θ1 ∧ θ2 ∧ θ3 
 
                                           =  —2 y1/(1 + y0) , 
 
using the formulas for  dθ
2  and  dθ3  appearing in the previous section. 
 
The above example can be viewed as a special instance of the formula given in 
Proposition 18.2, since   
 
< y , V >  =  < y , X
1 >  =  y1   and  1  +  < x , y >  =  1  +  y0 . 
 
And just as in the case of the curl formula of Proposition 18.1, this single 
verification of Proposition 18.2 also serves as its proof. 
 
 
 
 46 
 
19. Statement of the Key Lemma. 
 
The following result plays a lead role in obtaining the formulas for the Biot-Savart 
and Green’s operators on  S
3  in parallel transport format. 
 
 
KEY LEMMA, spherical version. 
 
                    ∇∇∇∇y ×××× {PyxV(x) ×××× ∇∇∇∇yϕϕϕϕ}  —  ∇∇∇∇y {V(x) ∙∙∙∙ ∇∇∇∇x (cos α α α α  ϕϕϕϕ)}   
 
                                                                 =  (∆∆∆∆ϕϕϕϕ  —  ϕϕϕϕ) (V(x)  —  < V(x), y > y) .  
 
 
This formula is quite flexible: it is useful whether  V  is a smooth vector field 
defined on all of  S
3 ,  or just on a bounded subdomain  Ω   of  S3 ,  or just along  
a smooth closed curve  K  in  S3 ,  or even just at the single point  x .   
 
As usual,  α   is the distance on  S3  between  x  and  y .  The kernel function  ϕ(α)   
is any smooth function, which typically blows up at  α  = 0  and is asymptotic there 
to  —1/(4πα ) .   
 
The Key Lemma can be understood intuitively in the special case that  ϕ(α )  is the 
fundamental solution of the operator  ϕ  →   ∆ϕ   —  ϕ   on  S3 ,  in which case we  
will see that  cos α  ϕ(α )  is the fundamental solution of the scalar Laplacian there. 
 
With this choice of kernel function, the quantity  P
yxV(x) × ∇yϕ  can be viewed  
as the contribution made by a little bit of current  V(x)  at the location  x  to the 
magnetic field at the location  y .  When integrated over  S3  with respect to  x ,   
the result will be the magnetic field  B  at  y .  Thus the first term on the left hand 
side of the Key Lemma integrates to  ∇ × B . 
 
In similar fashion, the term  ∇
y {V(x) ∙ ∇x (cos α   ϕ)}  integrates to the time 
derivative  ∂E/∂t  of the electric field at  y  due to the accumulation or dispersion  
of charge by the current flow  V ,  while the right hand side of the Key Lemma 
integrates to the current flow  V  itself. 
 
Thus the Key Lemma, for this special choice of kernel function  ϕ ,  can be 
viewed as a pointwise or infinitesimal version of Maxwell’s equation 
 
∇ × B  —  ∂E/∂t    =  V  . 
 
 47 
 
 
 
20. The first term on the LHS of the Key Lemma. 
 
The plan for the proof of the Key Lemma is simple.  Applying an appropriate 
rotation of  S3 ,  we can assume that  x  is the point  (1, 0, 0, 0)  and that, after 
scaling,  V(x)  =  X1  =  (0, 1, 0, 0) .  At each point  y  =  (y0 , y1 , y2 , y3)  of   
S3  —  {—x} ,  we will expand both sides of the Key Lemma in terms of the ortho- 
normal basis  E1 ,  E2  and  E3  for  TyS3 ,  and prove equality component-wise. 
 
We begin with the first term on the LHS of the equation, and note that 
 
PyxV(x)  ×  ∇y ϕ  =  PyxV(x)  ×  (—Pyx ∇x ϕ)  =  Pyx (— V(x)  ×  ∇x ϕ) . 
 
From section 14, we have that 
 
                      ∇
x α   =  (cos α   x  —  y) / sin α  
 
                                      =  
((y0 , 0 , 0 , 0)  —  (y0 , y1 , y2 , y3)) / sin α  
 
                                      =  (—1 / sin α ) (y1 X1  +  y2 X2  +  y3 X3) . 
 
Hence 
 
∇x ϕ  =  ϕ’(α ) ∇x α   =  (— ϕ’(α ) / sin α) (y1 X1  +  y2 X2  +  y3 X3) . 
 
Thus 
 
     — V(x) × ∇
x ϕ  =  (—X1)  ×  (— ϕ’(α ) / sin α) (y1 X1  +  y2 X2  +  y3 X3) 
 
                                     =  (ϕ’(α ) / sin α ) ( —y
3 X2  +  y2 X3) . 
Hence 
 
        P
yxV(x)  ×  ∇y ϕ  =  Pyx (— V(x)  ×  ∇x ϕ) 
 
                                     =  (ϕ’(α ) / sin α ) ( —y3 E2  +  y2 E3) . 
 
 48 
 
 
 
Now we take curls and evaluate the first term on the LHS of the Key Lemma, 
 
∇
y  ×  {PyxV(x)  ×  ∇y ϕ}  =  ∇y  ×  {(ϕ’(α ) / sin α ) ( —y3 E2  +  y2 E3)} . 
 
We begin by computing the curl of the vector field 
 
W  =  W(y)  =  —y3 E2  +  y2 E3 . 
 
Following the recipe given in section 18, we have 
 
∇y × W  =  ⇑ d ↓ W . 
 
Going part way, we have 
 
                      d ↓ W  =  d (—y
3 θ2  +  y2 θ3)   
 
                                  =  — dy
3 ∧ θ2  —  y3 dθ2  +  dy2 ∧ θ3  +  y2 dθ3 . 
 
We use the formulas from section 17 to express  dy3  and  dy2  in terms of 
θ1 ,  θ2  and  θ3 ,  and compute that 
 
         d ↓ W  =  2 (y0  +  y1
2/(1 + y0)) θ2 ∧ θ3  +  2 (y1y2 / (1 + y0)) θ3 ∧ θ1   
 
                                                +  2 (y1y3 / (1 + y0)) θ1 ∧ θ2  . 
 
Hence 
 
     ∇
y × W  =  ⇑ d ↓ W  =  2 (y0  +  y1
2/(1 + y0)) E1  +  2 (y1y2 / (1 + y0)) Ε2   
 
                                                                   +  2 (y1y3 / (1 + y0)) Ε3 . 
 
Now to compute  ∇
y  ×  {(ϕ’(α ) / sin α ) ( —y3 E2  +  y2 E3)} ,  we use the formula 
 
∇  ×  (f W)  =  f (∇ × W)  +  ∇f  × W , 
 
with  f (α )  =  ϕ’(α ) / sin α . 
 
 
 49 
 
 
 
 
 
We find that 
 
∇
y  ×  {PyxV(x)  ×  ∇y ϕ}  =  ∇y  ×  {(ϕ’(α ) / sin α ) ( —y3 E2  +  y2 E3)} 
 
=  { (ϕ’/sin α ) 2 (y0  +  y1
2/(1 + y0))  +  (ϕ"/sin2α   —  ϕ’ cos α /sin3α ) (y2
2 + y3
2) } E1 
 
        +  { (ϕ’/sin α ) 2 y1y2/(1 + y0)     +      (ϕ"/sin2α   —  ϕ’ cos α /sin3α ) (—y1y2) } E2 
 
        +  
{ (ϕ’/sin α ) 2 y1y3/(1 + y0)     +      (ϕ"/sin2α   —  ϕ’ cos α /sin3α ) (—y1y3) } E3 . 
 
This puts the first term on the LHS of the Key Lemma in the form we want it. 
 
 
 50 
 
 
 
 
21. The second term on the LHS of the Key Lemma.
 
 
Now, just as we did for the first term, we want to express the second term 
 
— ∇
y {V(x) ∙ ∇x (cos α   ϕ)} 
 
as a linear combination of the orthonormal basis vectors  E
1 ,  E2  and  E3  for  TyS3 . 
We keep in mind that  x  =  (1, 0, 0, 0)  and that  V(x)  =  X1  =  (0, 1, 0, 0) . 
 
To begin, 
 
           ∇
x (cos α   ϕ)  =  (cos α   ϕ)’ ∇x α  
 
                                      =  (cos α   ϕ)’  (—1/sin α ) (y1 X1  +  y2 X2  +  y3 X3) . 
 
Then taking the dot product of this with  V(x)  =  X
1  yields 
 
                     V(x) ∙ ∇x (cos α   ϕ)  =  (cos α   ϕ)’  (—1/sin α ) y1 
 
                                                         =  (— ϕ’ cos α  / sin α  +  ϕ) y1 . 
 
Thus 
 
— ∇
y {V(x) ∙ ∇x (cos α   ϕ)}  =  ∇y {(ϕ’ cos α  / sin α  —  ϕ)} y1 . 
 
To calculate this, recall that 
 
∇y α   =  (1/sin α ) (y1 E1  +  y2 E2  +  y3 E3) , 
 
and note that 
 
            ∇
y y1  =  ↑ dy1  =  ↑ {θ1  —  (y1/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3)} 
 
                                         =  E
1  —  (y1/(1 + y0)) (y1 E1  +  y2 E2  +  y3 E3) . 
 
 51 
 
 
 
 
 
We then calculate the second term on the LHS of the Key Lemma: 
 
— ∇
y {V(x) ∙ ∇x (cos α   ϕ)} 
 
               =  { (ϕ" cos α /sin2α   —  ϕ’(1/sin α   +  1/sin3α )) y1
2   
 
                                                +  (ϕ’ cos α /sin α   —  ϕ) (1  —  y1
2/(1 + y0)) } E1 
 
                    +  
{ (ϕ" cos α /sin2α   —  ϕ’(1/sin α   +  1/sin3α )) y1y2   
 
                                                        —  (ϕ’ cos α /sin α   —  ϕ) y1y2/(1 + y0) } E2 
 
                    +  { (ϕ" cos α /sin2α   —  ϕ’(1/sin α   +  1/sin3α )) y1y3   
 
                                                        —  (ϕ’ cos α /sin α   —  ϕ) y
1y3/(1 + y0) } E3 . 
  
 
If we combine the two terms on the LHS of the Key Lemma and simplify, we get 
 
     ∇
y  ×  {PyxV(x)  ×  ∇y ϕ}  —  ∇y {V(x) ∙ ∇x (cos α   ϕ)} 
 
                                =  {(ϕ"  +  2 ϕ’ cos α /sin α   —  ϕ) (1  —  y1
2/(1 + y0)) } E1 
 
                                   +  
{(ϕ"  +  2 ϕ’ cos α /sin α   —  ϕ) (— y1y2/(1 + y0)) } E2 
 
                                   +  {(ϕ"  +  2 ϕ’ cos α /sin α   —  ϕ) (— y1y3/(1 + y0)) } E3 . 
 
 
 52 
 
 
22. The RHS of the Key Lemma. 
 
Now we express the RHS 
 
(∆ϕ   —  ϕ) (V(x)  —  < V(x) , y > y) 
 
as a linear combination of  E
1 ,  E2  and  E3 . 
 
Recall that 
 
∆ϕ   =  ϕ"  +  2 ϕ’ cos α /sin α  , 
 
and hence 
 
∆ϕ   —  ϕ  =  ϕ"  +  2 ϕ’ cos α /sin α  —  ϕ . 
 
Next, note that  V(x)  =  (0, 1, 0, 0)  can be viewed as the gradient in  R
4  of the 
coordinate function  y1 ,  and that  V(x)  —  < V(x) , y > y  is the orthogonal 
projection of this onto the tangent plane  TyS3  to  S3  at  y ,  and is therefore the 
gradient on  S3  of  y1 .  Thus 
 
        V(x)  —  < V(x) , y > y  =  ∇y y1 
 
                                              =  E
1  —  (y1/(1 + y0)) (y1 E1  +  y2 E2  +  y3 E3) , 
 
according to our calculation in the preceding section. 
 
Hence the RHS of the Key Lemma is given by 
 
     (∆ϕ   —  ϕ) (V(x)  —  < V(x) , y > y)  
 
                                =  
{(ϕ"  +  2 ϕ’ cos α /sin α   —  ϕ) (1  —  y1
2/(1 + y0)) } E1 
 
                                   +  {(ϕ"  +  2 ϕ’ cos α /sin α   —  ϕ) (— y1y2/(1 + y0)) } E2 
 
                                   +  {(ϕ"  +  2 ϕ’ cos α /sin α   —  ϕ) (— y1y3/(1 + y0)) } E3 . 
 
This matches the LHS, as given in the previous section, and so completes the 
proof of the Key Lemma. 
 
 
 
 53 
 
 
23. Maxwell’s equation on  S3 . 
 
We now apply the Key Lemma to the proof of Maxwell’s equation 
 
∇ × B  =  V  +  ∂E/∂t  
 
on  S
3 .  In the Key Lemma, we use the kernel function 
 
ϕ(α )  =  (—1/4π2) (π — α ) csc α  , 
 
which, as we noted earlier, is a fundamental solution of the shifted Laplacian on  S3 , 
 
∆ϕ  —  ϕ  =  δ . 
 
With this choice of kernel function, we have that 
 
(cos α ) ϕ(α )  =  ϕ
0(α )  =  (—1/4π2) (π — α ) cot α , 
 
which is the fundamental solution of the Laplacian on  S3 , 
 
∆ϕ0  =  δ  —  1/(2π2) .  
 
With these choices, the Key Lemma reads 
 
     ∇
y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x ϕ0}   
 
                                                                 =  δ(x, y) 
(V(x)  —  < V(x), y > y) .  
 
Keeping these choices of kernel functions, we now define the Biot-Savart operator 
by formula (2) of Theorem 2, 
 
BS(V)(y)  =  
∫S3  PyxV(x) × ∇y ϕ(x, y) dx . 
 
Then we integrate the Key Lemma over  S3  and get 
 
   ∫S3  ∇y × {PyxV(x) × ∇yϕ} dx   —   ∫S3  ∇y {V(x) ∙ ∇x ϕ0}  dx 
 
                                                          =   ∫S3  δ(x, y) (V(x)  —  < V(x), y > y)  dx . 
 
 54 
 
 
 
 
The integral on the right hand side above equals   
 
V(y)  —  < V(y), y > y  =  V(y) , 
 
since  V(y) is a tangent vector to  S
3  at  y ,  and hence orthogonal to  y  in  R4 . 
 
Taking the curl and the gradient outside the two integrals on the left-hand side,  
we then get 
 
∇
y × ∫S3  PyxV(x) × ∇yϕ(x, y)  dx   —   ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx   =   V(y) , 
 
or 
∇y × BS(V)(y)  =  V(y)  +  ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx . 
 
As indicated in section 3, this is Maxwell’s equation 
 
∇ × B  =  V  +  ∂E/∂t . 
 
This explains our remark in section 19 that, for this special choice of kernel 
function  ϕ ,  the Key Lemma can be viewed as a pointwise or infinitesimal  
version of Maxwell’s equation. 
 
 
 55 
 
 
 
 
24.  Proof of Theorem 2, formula (2) . 
 
Let  V  be a smooth vector field on  S3 .  Thinking of  V  as a steady current flow, 
we defined the corresponding magnetic field  BS(V)  by  
 
BS(V)(y)  =  ∫S3  PyxV(x) × ∇y ϕ(x, y)  dx , 
 
where  ϕ(α )  =  (—1/4π2) (π — α ) csc α  . 
 
We saw in the preceding section that, as a consequence of the Key Lemma, the 
field  BS(V)  satisfies Maxwell’s equation 
 
∇
y × BS(V)(y)  =  V(y)  +  ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx . 
 
To complete the proof of Theorem 2, formula (2), we need only show that  BS(V)  
is divergence-free, and we do this as follows. 
 
            ∇
y ∙ BS(V)(y)  =  ∇y ∙ ∫S3  PyxV(x)  ×  ∇yϕ(x, y)  dx 
 
                                         =  ∫S3   ∇y ∙ {PyxV(x)  ×  ∇yϕ(x, y)}  dx , 
 
and we will show that the integrand is identically zero.  We use the standard 
formula 
 
     ∇ ∙ (A × B)  =  (∇ × A) ∙ B  —  A ∙ (∇ × B) ,   
 
and also the formula from Proposition 18.1, 
 
                   ∇
y  ×  PyxV(x)  =  [y , x , V] / (1  +  <x , y>) . 
 
 
 56 
 
 
 
 
 
 
Then 
 
        ∇
y ∙ {PyxV(x)  ×  ∇yϕ(x, y)} 
 
                               =  {∇
y × PyxV(x)} ∙ ∇yϕ(x, y)  —  PyxV(x)  ∙  ∇y × ∇yϕ(x, y) 
 
                               =  {∇y × PyxV(x)} ∙ ∇yϕ(x, y) 
 
                               =  {[y , x , V(x)] / (1  +  <x , y>)}  ∙  ∇yϕ(x, y) 
 
                               =  0 , 
 
since  [y , x , V(x)]  is orthogonal to the plane spanned by  x  and  y ,  while 
∇
yϕ(x, y)  lies in that plane. 
 
Thus the proposed magnetic field  BS(V)  is indeed divergence-free. 
 
This completes the proof of Theorem 2, formula (2) . 
 
We note that the above argument for the divergence-free character of  BS(V)   
does not depend on the particular choice of kernel function  ϕ . 
 
 
 
 57 
 
 
 
25. The Green’s operator on  S3  in parallel transport format. 
 
We turn now to the derivation of formula (2) of Theorem 3 for the Green’s operator  
on  S3  in parallel transport format, 
 
Gr(V)(y)  =   ∫S3  PyxV(x)  ϕ2(x, y)  dx   +   ∇y∫S3  PyxV(x) ∙ ∇yϕ3(x, y)  dx , 
 
where 
 
       ϕ
2(α )  =  (—1/4π2) (π — α ) csc α   +  (1/8π2) (π — α )2 / (1 + cos α ) 
 
and  
 
       ϕ
3(α )  =  (—1/24) (π — α ) cot α   —  (1/16π2) α  (2π — α ) 
 
                               +  (1/8π2) ∫α
π  ((π — α )3 / (3 sin2α ))  +  ((π — α )2 / sin α )   dα . 
 
 
The naming of the kernel functions  ϕ2  and  ϕ3  above leaves room in the ϕ-family  
for the fundamental solution of the Laplacian on  S3 , 
 
       ϕ0(α )  =  (—1/4π2) (π — α ) cot α                         ∆ϕ0  =  δ  —  1/2π2 
 
and for the kernel function of the Biot-Savart operator in parallel transport format,  
 
       ϕ
1(α )  =  (—1/4π2) (π — α ) csc α     ∆ϕ 1  —  ϕ1  =  δ . 
 
 
 
 58 
 
 
26. Plan of the proof. 
 
Consider the usual vector convolutions, this time in parallel transport format: 
 
     A(V, ϕ)(y)  =  ∫S3  PyxV(x) ϕ(x, y)  dx 
 
     B(V, ϕ)(y)  =  ∫S3  PyxV(x)  ×  ∇yϕ(x, y)  dx 
 
      g(V, ϕ)(y)  =  
∫S3  PyxV(x)  ∙  ∇yϕ(x, y)  dx 
 
     G(V, ϕ)(y)  =  ∇y g(V, ϕ)(y)  =  ∇y ∫S3  PyxV(x)  ∙  ∇yϕ(x, y)  dx . 
 
Step 1.  First we will determine the unknown kernel function  ϕ  so as to make 
 
∇y  ×  A(V, ϕ)(y)  =  — B(V, ϕ1)(y)  =  — BS(V)(y) . 
 
Insisting that  ϕ  have a singularity only at  α   =  0  and not at  α   =  π  leads 
to the unique solution  ϕ  =  ϕ2  given in the statement of the theorem above.   
 
Step 2.  Then, as a consequence of Maxwell’s equation, we will have 
 
        — ∇y × ∇y × A(V, ϕ2)(y)  =  ∇y × BS(V)(y)   
 
   
                                               =  V(y)  —  ∇y ∫S3  ∇x ∙ V(x)  ϕ0(x, y)  dx . 
Hence 
 
∆
y A(V, ϕ2)(y)  =  — ∇y × ∇y × A(V, ϕ2)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) 
 
                      =  V(y)  —  ∇y ∫S3  ∇x ∙ V(x)  ϕ0(x, y)  dx   +  ∇y(∇y ∙ A(V, ϕ2)(y)) 
 
                      =  V(y)  +  some gradient field . 
 
We then find the kernel function  ϕ
3  so that  ∆y G(V, ϕ3)(y)  =  G(V, ∆ϕ 3)(y)   
is the negative of the above gradient field, in which case defining 
 
Gr(V)(y)  =  A(V, ϕ2)(y)  +  G(V, ϕ3)(y) 
 
yields the desired equation  ∆y Gr(V)(y)  =  V(y) . 
 
 59 
27. Some formulas that we will use. 
 
In the formulas below,  V  is a single tangent vector at the single point  x ∊ S3 . 
 
                                                            <y, V> (1)                             P
yxV  =  V  —  ————————  (x  +  y)                                                           1 + <x, y> 
 
                                                  [y, x, V] (2)                 ∇y × PyxV  =  ————————                                                   1 + <x, y> 
 
                      — 2 <y, V> (3)                ∇y ∙ PyxV  =  ————————                                                   1 + <x, y> 
 
 
(4)                 PyxV  ×  ∇yϕ  =  [y, x, V] ϕ’(α ) / sin α  . 
 
Formula (1) appears in section 16, while formulas (2) and (3) appear in section 18.    
 
Formula (4) in the special case that  x  =  (1, 0, 0, 0)  and  V  =  X
1  =  (0, 1, 0, 0)  
is obtained from the formula 
 
PyxV  ×  ∇y ϕ  =  (ϕ’(α ) / sin α ) ( —y3 E2  +  y2 E3)  
 
of section 20, together with the remark of section 18 that in this case we have 
 
[y , x , V]  =  —y3 E2  +  y2 E3 . 
 
We leave it to the reader to confirm, as we did earlier in similar circumstances, 
that this single case of formula (4) can serve as its proof. 
 
We see from formula (1) that  P
yxV  lies in the 3-plane in  R4  spanned by  V ,  x , y ,     
and from formula (2) that its curl  ∇y × PyxV  is orthogonal to this 3-plane, and 
hence orthogonal to  PyxV . 
 
This is in marked contrast to the situation in left-translation format, where 
∇
y × Lyx—1V  =  — 2 Lyx—1V  is parallel to  Lyx—1V . 
 
We see from formulas (2) and (4) that  ∇
y × PyxV  and  PyxV × ∇yϕ  are parallel 
to one another.  It is this fact which makes possible the solution of the equation  
 
∇y  ×  A(V, ϕ)(y)  =  — B(V, ϕ1)(y)  =  — BS(V)(y) 
 
for the unknown kernel function  ϕ .
 
 60 
 
 
28. The curl of  A(V, ϕϕϕϕ)(y) . 
 
 
∇y × A(V, ϕ)(y)  =  ∫S3  ∇y × {PyxV(x) ϕ(x, y)}  dx 
 
          =  
∫S3  {∇y × PyxV(x)} ϕ(x, y)   —   PyxV(x) × ∇yϕ(x, y)  dx 
 
                      [y, x, V(x)]                                          ϕ’(α )           =  ∫S3  ———————— ϕ(x, y)   —    [y, x, V(x)] —————  dx                        1 + <x, y>                                           sin α 
 
                                                  ϕ                   ϕ’           =  ∫S3  [y, x, V(x)] {——————— — —————}  dx   ,                                             1 + cos α          sin α 
 
thanks to formulas (2) and (4) above. 
 
On the other hand, 
 
      BS(V)(y)  =  B(V, ϕ
1)(y)  =  ∫S3  PyxV(x)  ×  ∇yϕ1(x, y)  dx 
 
                                                                               ϕ1’(α )                                                =  ∫S3  [y, x, V(x)] —————   dx  ,                                                                                 sin α 
 
again by formula (4) . 
 
Thus, in order that 
 
∇
y  ×  A(V, ϕ)(y)  =  — BS(V)(y)  =  — B(V, ϕ1)(y)  , 
 
we must choose  ϕ  to satisfy the ODE 
 
                                 ϕ                   ϕ’                    ϕ1’                          ————————  —  —————   =   — ————— .                           1 + cos α           sin α               sin α 
 
 
 61 
 
 
 
 
We rewrite this as 
 
                            (1 + cos α ) ϕ’  —  (sin α) ϕ  =  (1 + cos α ) ϕ
1’ , 
 
equivalently, 
 
                        [(1 + cos α ) ϕ]’  =  [(1 + cos α ) ϕ
1]’  +  (sin α ) ϕ1 
 
                                                  =  [(1 + cos α ) ϕ1]’  —  (1/4π2) (π — α ) , 
 
since  ϕ1(α )  =  (—1/4π2) (π — α ) csc α  .  Now we integrate both sides to get 
 
(1 + cos α ) ϕ  =  (1 + cos α ) ϕ1  +  (1/8π2) (π — α)2 . 
 
Dividing through by (1 + cos α ) ,  we get 
 
          ϕ(α)  =  ϕ1(α )  +  (1/8π2) (π — α )2 / (1 + cos α )   
 
                    =   (—1/4π
2) (π — α ) csc α  +  (1/8π2) (π — α)2 / (1 + cos α ) . 
 
Note that  ϕ(α )  has a singularity only at  α   =  0  and not at  α   =  π .   
 
We call this solution  ϕ2(α ) ,  and with it we have completed Step 1: 
 
∇y  ×  A(V, ϕ2)(y)  =  — B(V, ϕ1)(y)  =  — BS(V)(y) . 
 
 62 
 
 
 
 
We take the negative curl of both sides to get 
    
        — ∇
y × ∇y × A(V, ϕ2)(y)  =  ∇y × BS(V)(y)   
 
                                                   =  V(y)  —  ∇y ∫S3  (∇x ∙ V(x))  ϕ0(x, y)  dx , 
 
thanks to Maxwell’s equation.  Integrating by parts, we have 
 
          ∫S3  (∇x ∙ V(x))  ϕ0(x, y)  dx  =  — ∫S3  V(x) ∙ ∇xϕ0(x, y)  dx 
 
                                                                 =  ∫S3  PyxV(x) ∙ ∇yϕ0(x, y)  dx   
 
                                                                 =  g(V, ϕ
0)(y) . 
 
Hence 
 
∆
y A(V, ϕ2)(y)  =  — ∇y × ∇y × A(V, ϕ2)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) 
 
                      =  V(y)  —  ∇
y ∫S3  ∇x ∙ V(x)  ϕ0(x, y)  dx   +  ∇y(∇y ∙ A(V, ϕ2)(y))  
 
                      =  V(y)  —  G(V, ϕ0)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) . 
 
 
Clearly the next step is to compute  ∇y ∙ A(V, ϕ2)(y) . 
 
 
 63 
 
 
 
29. The divergence of  A(V, ϕϕϕϕ2) . 
 
We begin as follows. 
 
     ∇
y ∙ A(V, ϕ2)(y)  =  ∫S3  ∇y ∙ {PyxV(x) ϕ2(x, y)}  dx 
 
              =  ∫S3  {∇y ∙ PyxV(x)} ϕ2(x, y)  dx   +  ∫S3  PyxV(x) ∙ ∇yϕ2(x, y)  dx . 
 
The second integral on the RHS above is simply  g(V, ϕ2)(y) ,  so we put that aside.   
 
Turning to the first integral and using formula (3) and the fact that  < x, V(x) >  =  0 , 
we get 
 
                                                 — 2 <y, V(x)>   ∫S3  {∇y ∙ PyxV(x)} ϕ2(x, y)  dx   =   ∫S3  ——————————  ϕ2(x, y)  dx                                                                             1 + <x, y> 
 
                                                                                        — 2 ϕ2(α )                                                                 =  ∫S3  <y, V(x)>  ————————  dx                                                                                          1 + cos α  
 
                                                                            cos α  x — y                2 sin α ϕ2(α )                                                           =                                                            =                                                            =                                                            =  ∫S3  < —————————, V(x) > —————————  dx                                                                                   sin α                        1 + cos α 
 
                                                                                                 2 sin α  ϕ2(α )                                                           =  ∫S3  < ∇xα  , V(x) >  ——————————  dx                                                                                                    1 + cos α 
 
                                                                                  2 sin α  ϕ2(α )                                                           =  ∫S3  V(x) ∙ —————————— ∇xα  dx                                                                                     1 + cos α 
 
                                                                                       — 2 sin α  ϕ2(α )                                                           =  ∫S3  PyxV(x) ∙ ———————————— ∇yα   dx                                               1 + cos α  
 
                                                          =  ∫S3  PyxV(x) ∙ ∇yψ (α )  dx 
 
                                                          =  g(V, ψ )(y) . 
 
 64 
 
 
 
 
The new kernel function  ψ   satisfies  
 
ψ ’(α )  =  [— 2 sin α  / (1 + cos α )] ϕ
2(α )  
 
    =  [— 2 sin α  / (1 + cos α )] [(—1/4π2) (π — α ) csc α  +  (1/8π2) (π — α)2 / (1 + cos α )] 
 
    =  (1/2π
2) (π — α ) / (1 + cos α )  —  (1/4π2) (π — α )2 sin α  / (1 + cos α )2 , 
 
and hence 
 
ψ (α )  =  (—1/4π
2) (π — α )2 / (1 + cos α ) . 
 
 
Collecting information, we have 
 
∇
y ∙ A(V, ϕ2)(y)   
 
                   =  ∫S3  {∇y ∙ PyxV(x)} ϕ2(x, y)  dx   +  ∫S3  PyxV(x) ∙ ∇yϕ2(x, y)  dx  
 
                   =  g(V, ψ )(y)  +  g(V, ϕ2)(y) , 
 
and hence 
 
∇
y (∇y ∙ A(V, ϕ2)(y))  =  G(V, ψ )(y)  +  G(V, ϕ2)(y) . 
 
 65 
 
 
 
 
 
30. Step 2 - Finding and using the kernel function  ϕϕϕϕ3 .    
 
Continuing our calculation of the Laplacian of  A(V, ϕ2)(y) ,  we have 
       
           ∆y A(V, ϕ2)(y)  =  V(y)  —  G(V, ϕ0)(y)   +  ∇y(∇y ∙ A(V, ϕ2)(y))  
 
                                     =  V(y)  —  G(V, ϕ0)(y)  +  G(V, ψ )(y)  +  G(V, ϕ2)(y) 
 
                                     =  V(y)  —  G(V, ϕ
0  —  ϕ2  —  ψ )(y) . 
 
We note that 
 
ϕ
0  —  ϕ2  —  ψ   =  (—1/4π2) (π — α ) cot α  
 
                                    +  (1/4π
2) (π — α ) csc α   —  (1/8π2) (π — α )2 / (1 + cos α ) 
 
                                         + (1/4π2) (π — α )2 / (1 + cos α ) 
 
                         =  (1/4π2) (π — α ) (1 — cos α ) / sin α    +   (1/8π2) (π — α )2 / (1 + cos α ) . 
 
Now let  ϕ
3(α )  be chosen to satisfy 
 
∆ϕ 3(α )  =  ϕ0  —  ϕ2  —  ψ  +  C 
 
              =  (1/4π2) (π — α ) (1 — cos α ) / sin α    +   (1/8π2) (π — α )2 / (1 + cos α )  +  C , 
 
where the constant  C  is chosen to make the right hand side have average value  zero 
over  S
3 ,  and where the function  ϕ3(α )  has a singularity at  α  = 0  but not at  α  = π . 
 
 
 66 
 
 
 
 
We have yet to calculate  ϕ
3  explicitly, but once this is done, we will have 
 
∆yG(V, ϕ3)(y)  =  G(V, ∆ϕ 3)(y)  =  G(V, ϕ0 — ϕ2 — ψ )(y) ,  
 
and hence 
 
∆
y {A(V, ϕ2)(y)  +  G(V, ϕ3)(y)} 
 
                              =  ∆y A(V, ϕ2)(y)  +  ∆y G(V, ϕ3)(y) 
 
                              =  ∆y A(V, ϕ2)(y)  +  G(V, ∆ϕ 3)(y) 
 
          =  V(y)  —  G(V, ϕ0 — ϕ2 — ψ )(y)  +  G(V, ϕ0 — ϕ2 — ψ )(y) 
 
                              =  V(y) . 
 
Therefore, if we define 
 
           Gr(V)(y)  =  A(V, ϕ
2)(y)  +  G(V, ϕ3)(y) 
 
                           =  ∫S3  PyxV(x)  ϕ2(x, y)  dx   +   ∇y ∫S3  PyxV(x) ∙ ∇yϕ3(x, y)  dx , 
 
we have                           
 
         ∆
y Gr(V)(y)  =  V(y) , 
 
as desired.   
 
This completes the proof of Theorem 3, formula (2) for the vector-valued Green’s 
operator on  S
3 ,  modulo the explicit determination of the kernel function  ϕ3 . 
 
We break the calculation of  ϕ3  into three pieces. 
 
 
 67 
 
 
 
 
First piece.   
 
Let   
 
ϕ
0(α )  =  (—1/4π2) (π — α ) cot α  
 
be the fundamental solution of the Laplacian on  S
3 , 
 
∆ϕ 0  =  δ  —  1/2π2 . 
 
The average value of  ϕ0  over  S3  is  [ϕ0]  =  —1/8π2 . 
 
If we define 
Φ
0(α )  =  (—1/16π2) α  (2π — α ) , 
 
then we have 
∆Φ
0  =  ϕ0  —  [ϕ0] . 
 
 
Second piece.   
 
Let  
 
ϕ
1(α )  =  (—1/4π2) (π — α ) csc α  
 
be the kernel function for the Biot-Savart operator on  S3  in parallel transport 
format.  The average value of ϕ1  over  S3  is  [ϕ1]  =  —1/2π2 . 
 
If we define 
Φ 1(α)  =  (—1/4π2) (π — α ) (1  —  cos α ) / sin α  , 
 
then we have 
∆Φ 1  =  ϕ1  —  [ϕ1] . 
 
 68 
 
 
 
 
 
Third piece.   
 
Let   
 
ψ (α )  =  (1/8π
2) (π — α )2 / (1  +  cos α ) , 
 
which is the right-most term in the expression for  ∆ϕ 3  in the statement of 
Theorem 3, formula (2) . 
 
The average value of  ψ   over  S
3  is   
 
[ψ ]  =  —1/2π2  +  1/12 . 
 
If we find the function  Ψ (α )  which satisfies 
 
∆Ψ   =  ψ   —  [ψ ] , 
 
and which has no singularity at  α   =  π ,  then 
 
ϕ
3  =  Φ 0  —  Φ 1  +  Ψ  
 
satisfies 
 
∆ϕ 3  =  (ϕ0  —  [ϕ0])  —  (ϕ1  —  [ϕ1])  +  (ψ   —  [ψ ]) , 
 
and is the kernel function we are seeking. 
 
 
 
 69 
 
 
 
 
 
31. Finding an explicit formula for  ΨΨΨΨ  .
 
 
The core issue is to solve the equation 
 
∆F(α )  =  (π — α )
2 / (1  +  cos α ) , 
 
after which we will have 
 
Ψ   =  (1/8π2) F  +  an appropriate function whose Laplacian is constant. 
 
Note that 
 
∆F  =  F"  + 2 F’ cot α   =  (1/sin
2α ) (sin2α  F ’)’ , 
 
which tells us that  sin
2α   is an integrating factor for our equation.   
 
Thus we must solve 
 
(sin
2α  F ’)’  =  (π — α )2 sin2α  / (1  +  cos α )  =  (π — α )2 (1  —  cos α ) . 
 
This integrates to 
 
sin
2α  F ’  =  —(π — α )3/3  —  (π — α )2 sin α   +  2(π — α ) cos α   +  2 sin α  . 
 
Notice that the right hand side vanishes at  α   =  π ,  so we do not add a constant 
of integration.  Dividing through by  sin2α  ,  we get 
 
F ’  =  —(π — α )3 / 3 sin2α   —  (π — α )2 / sin α   +  (2(π — α ) cos α   +  2 sin α ) / sin2α  . 
 
 70 
 
 
 
 
The right-hand half of this expression,  
 
(2(π — α ) cos α   +  2 sin α ) / sin2α , 
 
blows up as  α   →   0 ,  but approaches  0  as  α   →   π ,  and integrates to 
 
—2 (π — α ) / sin α  . 
 
The left-hand half of this expression, 
 
ω (α )  =  —(π — α )3 / 3 sin2α   —  (π — α )2 / sin α , 
 
blows up as  α   →   0 ,  but approaches  0  as  α   →   π . 
 
As mentioned earlier, the integral of  ω (α )  is a non-elementary function involving 
polylogarithms, so for momentary convenience we define 
 
Ω (α )  =  — ∫
α
π  ω (α )  dα  . 
 
Thus  Ω ’(α )  =  ω (α )   and  Ω (π)  =  0 . 
 
Then our equation for  F
 ’ , 
 
F ’  =  —(π — α )3 / 3 sin2α   —  (π — α )2 / sin α   +  (2(π — α ) cos α   +  2 sin α ) / sin2α  . 
 
      =  ω (α )  +  (2(π — α ) cos α   +  2 sin α ) / sin2α , 
 
integrates to 
 
F(α )  =  Ω (α )  —  2 (π — α ) / sin α . 
 
This function  F(α )  satisfies the equation 
 
∆F(α )  =  (π — α )
2 / (1  +  cos α ) . 
 
 71 
 
 
 
 
Since the function   G(α )  =  ‰ ( π — α ) cot α   has Laplacian  1  and no singularity  
at  α  = π ,  we conclude that the function 
 
       
 Ψ (α )  =  (1/8π2) F(α )  —  (—1/2π2  +  1/12) G(α ) 
 
                  =  (1/8π2) (Ω (α )  —  2 (π — α ) / sin α)  +  (1/4π2  —  1/24) (π — α) cot α 
 
satisfies the equation 
 
∆Ψ   =  ψ   —  [ψ ] , 
 
and has no singularity at  α   =  π ,  as desired. 
 
 
 
 
32. Explicit formula for  ϕϕϕϕ3 . 
 
Putting this all together, we have that 
 
  ϕ
3  =  Φ 0  —  Φ 1  +  Ψ 
 
        =  (—1/16π2) α  (2π — α )  +  (1/4π2) (π — α ) (1  —  cos α ) / sin α 
 
             +  (1/8π
2) (Ω (α )  —  2 (π — α ) / sin α)  +  (1/4π2  —  1/24) (π — α) cot α 
 
        =  (—1/24) (π — α ) cot α   —  (1/16π2) α  (2π — α )  +  (1/8π2) Ω (α ) , 
 
        =  (—1/24) (π — α ) cot α   —  (1/16π2) α  (2π — α ) 
 
                               +  (1/8π
2) ∫α
π  ((π — α )3 / (3 sin2α ))  +  ((π — α )2 / sin α )   dα , 
 
thanks to two cancellations. 
 
This completes the proof of Theorem 3, formula (2) . 
 
 
 
 
 
 72 
 
 
D. PROOFS IN  H3  IN PARALLEL TRANSPORT FORMAT 
 
 
33. The hyperboloid model of hyperbolic 3-space. 
 
In part  C ,  we considered the standard Euclidean inner product in  R
4 , 
 
< x , y >  =  x0 y0  +  x1 y1  +  x2 y2  +  x3 y3 , 
 
and then focused on the unit 3-sphere 
 
S3  =  { x ∊ R4 :  < x , x >  =  1 } . 
 
This concrete model for the 3-sphere of constant curvature  +1  is so common that  
we used it without further comment. 
 
We now replace  R
4  by Minkowski space  R1,3  with the indefinite inner product 
 
< x , y >  =  x0 y0  —  x1 y1  —  x2 y2  —  x3 y3 , 
 
and then regard hyperbolic 3-space as the hyperboloid 
 
H
3  =  { x ∊ R1,3 :  < x , x >  =  1   and   x0  >  0 } . 
 
                   
  
 
                           The hyperboloid model of hyperbolic 3-space  
                                            inside Minkowski 4-space 
 
 
 73 
 
 
                                                                                                           
  
This concrete model for the hyperbolic 3-space of constant curvature  —1  is not 
nearly so common as the PoincarØ ball model or the upper half-space model. 
But the hyperboloid model lets us exploit the interplay between the geometry of   
H
3  and the linear algebra of  R1,3  in much the same way that we did in part C  
for  S3  and  R4 ,  and hence lets us give proofs of the formulas for the Biot-Savart  
and Green’s operators in  H3  which are very closely patterned on the corresponding 
proofs already given for  S3 .    
 
Since the inner product  < x , x >  is positive for all  x ∊ H3 ,  these radius vectors 
to  H3  are "timelike".  Moreover, if  x , y ∊ H3 ,  then we have  < x , y >  ≥  1 , 
with equality if and only if  x  =  y . 
 
We will freely identify points in  R
1,3  with the vectors at the origin that point to 
them, and we will also identify the tangent spaces at various points in  R1,3  in the 
usual way, so that we can say  v  ∊  TxH3  if and only if  < x , v >  =  0 .  We 
necessarily have  < v , v >  <  0  for all nonzero  v ∊ TxH3 ;  in other words, the 
tangent vectors to  H3  are "spacelike". 
 
We will always write  < v , w >  for the inner product of vectors when we’re 
thinking of them as belonging to  R
1,3 .  If  v  and  w  both lie in  TxH3 ,  we define 
 
v ∙ w  =  — < v , w > . 
 
Because the tangent vectors to  H3  are spacelike, this gives a positive definite 
inner product on each tangent space  TxH3 .  The resulting Riemannian metric is 
complete and has constant curvature  —1 . 
 
 
 74 
 
 
 
34. Isometries of  H3 . 
 
A linear transformation  A: R1,3  →   R1,3  is called an isometry if 
 
< A(x) , A(y) >  =  < x , y > 
 
for all  x  and  y  ∊  R1,3 . 
 
An isometry of  R1,3  takes the two-sheeted hyperboloid  < x , x >  =  1  to itself ,  
but may interchange the two sheets.  If it does not interchange these sheets, then in 
particular it takes the "upper" sheet  H
3  to itself.  In that case, it also preserves the 
Riemannian metric on  H3 ,  so is an isometry of  H3  in the sense of Riemannian 
geometry. 
 
One example of an isometry of  R
1,3  which preserves  H3  is given by the linear 
transformation  A  with matrix 
 
                                         cosh t    sinh t    0    0 
                                         sinh t    cosh t    0    0 
                                            0           0        1    0 
                                            0           0        0    1   . 
 
A family of examples of isometries of  R
1,3  which preserve  H3  consists of those 
linear transformations  A  which fix identically the  x0-axis, and act as Euclidean 
rigid motions on the  x1x2x3-space. 
 
Compositions of these examples provide all possible isometries of  R1,3  which 
take  H3  to itself, and in particular provide all possible isometries of  H3  in the 
sense of Riemannian geometry. 
 
Half of these are orientation preserving, and constitute the group  SO(1,3) . 
 
 
 75 
35. Geodesics in  H3 . 
 
Let  x  ∊  H3 ,  so that  < x , x >  =  1 ,  and suppose that  v  is a unit vector tangent 
to  H3  at  x ,  so that  < x, v >  =  0  and  < v , v >  =  —1 .  Consider the curve 
 
G(t)  =  cosh t  x  +  sinh t  v , 
 
which we easily check to lie in  H3  and to be parametrized by arc length.   
 
If we complete  v  to an orthonormal basis  v , u , w  of  TxH3 ,  then the linear 
map of  R1,3  that fixes  x  and  v  but sends  u  and  w  to  —u  and  —w  is an 
isometry of  H3  whose fixed point set is the curve  G .  As usual in Riemannian 
geometry, this tells us that  G  is a geodesic. 
 
The inner product  < x , G(t) >  =  cosh t  is the hyperbolic cosine of the distance  t   
in  H
3  from  x  to  G(t) .  More generally, if  x  and  y  are any two points of  H3 ,  the 
inner product  < x , y >  is the hyperbolic cosine of the distance in  H3  between them. 
 
Now let  x  and  y  be any pair of distinct points in  H3 .  Then the vector 
v  =  y  —  < x , y > x  is nonzero and orthogonal to  x ,  so that  v  ∊  TxH3 .   
Moreover,  |v|2  =  < v , v >  =  1  —  < x , y >2  <  0 ,  so  v ∙ v  =  < x , y >2  —  1  >  0 , 
and hence  v / |v|  is a unit vector tangent to  H3  at  x .  Therefore the unique, 
length-minimizing geodesic from  x  to  y  is given by 
 
G(t)  =  cosh t  x  +  sinh t  (v / |v|) . 
 
If  α   is the distance from  x  to  y  in  H3 ,  so that  cosh α   =  < x , y > ,  then 
we can rewrite this as 
 
G(t)  =  cosh t  x  +  sinh t  
((y  —  cosh α   x) / sinh α ) . 
 
When  t  =  α  ,  we have  G(α )  =  y  and 
 
                       G’(α )  =  sinh α   x  +  cosh α   ((y  —  cosh α   x) / sinh α ) 
 
                                  =  (cosh α   y  —  x) / sinh α  . 
 
Since  G  is parametrized by arc-length and is length-minimizing, and  α   is the  
distance in  H
3  from  x  to  y ,  we deduce that 
 
                      ∇y α (x, y)  =  G’(α )  =  (cosh α   y  —  x) / sinh α  . 
 
We note that   
                                      Pxy ∇y α (x, y)  =  — ∇x α (x, y) . 
 
 76 
 
 
 
36.  The vector triple product in  R1,3 . 
 
Let  X0  =  (1, 0, 0, 0) ,  X1  =  (0, 1, 0, 0) ,  X2  =  (0, 0, 1, 0)  and  X3  =  (0, 0, 0, 1) 
be the standard orthonormal basis for  R1,3 .  Then for  x , v , w  ∊  R1,3 ,  we define 
the vector triple product 
 
                                                               x0   x1   x2   x3 
                                                               v0   v1   v2   v3                                                        [x, v, w]  =  det                               ∊  R1.3 .                                                                w0  w1  w2  w3         
                                                               X0 -X1 -X2 -X3  
 
Note that  [x, v, w]  is an alternating multilinear function of its three arguments. 
 
For  y  ∊  R
1,3 ,  we have 
 
                                                                          x
0   x1   x2   x3 
                                                                          v0   v1   v2   v3                                                        < [x, v, w] , y >  =  det                              .                                                                           w0  w1  w2  w3          
                                                                          y0   y1   y2   y3 
 
Thus  [x, v, w]  is a vector in  R
1,3  whose inner product with each of  x , v  and  w 
is zero.   
 
If  A  ∊  SO(1,3) ,  we have 
 
[Ax, Av, Aw]  =  A[x, v, w] . 
 
 
 77 
 
 
 
 
37. Explicit formula for parallel transport in  H
3 . 
 
Let  x  and  y  be any pair of distinct points in  H3  ⊂   R1,3 .  Then there is a unique 
element  M  ∊  SO(1,3)  that maps  x  to  y  and leaves fixed the two-dimensional 
subspace of  R1,3  consisting of all vectors orthogonal to both  x  and  y .  For 
v  ∊  R1,3 ,  this mapping is given by 
 
                           < x + y , v >                1 + 2 < x, y >                  1 M(v)  =  v   —    —————————   x   +   〈——————————  x  —  —————————  y ,  v 〉 y  .                           1  +  < x, y >                1  +  < x, y >             1  +  < x, y > 
 
Direct calculation shows that  M  ∊  SO(1,3) ,  and is therefore the desired isometry. 
 
If  v  ∊  TxH3 ,  then  < v , x >  =  0 ,  and the formula for  M(v)  simplifies to 
 
                                                             < y, v >                               M(v)  =  v   —   —————————— (x  +  y) .                                                         1  +  < x, y > 
 
In this case,  M(v)  is the result of parallel transport of  v  from  x  to  y ,  so we 
will write 
 
                                                                      < y, v >                           P
yxv  =  M(v)  =  v   —   —————————— (x  +  y) .                                                                   1  +  < x, y > 
 
Note that the formulas in this section are the same as those in section 16 in the  
case of  S
3  ⊂   R4 ,  except for the change in the definition of the inner product. 
 
 
 78 
 
38. The method of moving frames in  H3 . 
 
The computations which lead to the various integral formulas in  H3  in parallel 
transport format will be carried out using "moving frames" which are obtained  
via parallel transport from a single orthonormal frame, just as they were on  S3 ,  
as follows. 
 
Let  x  =  (1, 0, 0, 0)  in  H
3  ⊂   R1,3 ,  and let  X1 ,  X2 ,  X3  be the usual  
orthonormal basis for the tangent space  TxH3  to  H3  at  x . 
 
For each point  y  =  (y0 , y1 , y2 , y3)  ∊ H3 ,  we parallel transport this orthonormal 
basis for  TxH3  along the unique geodesic from  x  to  y  to obtain an orthonormal 
basis 
 
E1  =  PyxX1 ,   E2  =  PyxX2 ,   E3  =  PyxX3 
 
for  TyH3 .   
 
Using the formula for  P
yxV ,  we calculate that 
 
                 E1  =  (y1 ,  1  +  y1
2/(1 + y0) ,  y1y2/(1 + y0) ,  y1y3/(1 + y0))  
 
                 E2  =  (y2 ,  y1y2/(1 + y0) ,  1  +  y2
2/(1 + y0) ,  y2y3/(1 + y0)) 
 
                 E
3  =  (y3 ,  y1y3/(1 + y0) ,  y2y3/(1 + y0) ,  1  +  y3
2/(1 + y0)) . 
 
Next, let  θ1 ,  θ2 ,  θ3  denote the 1-forms on  H3  which are dual to  E1 ,  E2 ,  E3 ,  
in the sense that  θi(V)  =  Ei ∙ V  =  — < Ei , V >  for all vectors  V  and for   
i  =  1, 2, 3. 
 
We can write 
 
    θ
1  =  — y1 dy0  +  (1  +  y1
2/(1 + y0)) dy1  +  y1y2/(1 + y0) dy2  +  y1y3/(1 + y0) dy3 
 
    θ2  =  — y2 dy0  +  y1y2/(1 + y0) dy1  +  (1  +  y2
2/(1 + y0)) dy2  +  y2y3/(1 + y0) dy3 
 
    θ
3  =  — y3 dy0  +  y1y3/(1 + y0) dy1  +  y2y3/(1 + y0) dy2  +  (1  +  y3
2/(1 + y0)) dy3 , 
 
where we understand the right hand sides as restricted to  H3 . 
 
 79 
 
 
 
 
Since   y
0
2  —  y1
2  —  y2
2  —  y3
2  =  1   on  H3 ,  we can add a fourth equation to the 
three above, 
 
    0  =  y
0 dy0  —  y1 dy1  —  y2 dy2  —  y3 dy3 . 
 
Using this fourth equation, we can simplify the first three to read 
 
    θ
1  =  — y1/(1 + y0) dy0  +  dy1 
 
    θ
2  =  — y2/(1 + y0) dy0  +  dy2 
 
    θ3  =  — y3/(1 + y0) dy0  +  dy3 . 
 
 
We then invert this system to obtain 
 
    dy
0  =  y1 θ1  +  y2 θ2  +  y3 θ3 
 
    dy
1  =  θ1  +  (y1/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3) 
 
    dy2  =  θ2  +  (y2/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3) 
 
    dy3  =  θ3  +  (y3/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3) . 
 
 
With these equations in hand, we easily obtain 
 
    dθ
1  =  — y2/(1 + y0)  θ1 ∧ θ2  +  y3/(1 + y0)  θ3 ∧ θ1 
 
    dθ2  =  — y3/(1 + y0)  θ2 ∧ θ3  +  y1/(1 + y0)  θ1 ∧ θ2 
 
    dθ3  =  — y1/(1 + y0)  θ3 ∧ θ1  +  y2/(1 + y0)  θ2 ∧ θ3 . 
 
 
 80 
 
 
39. Curls and divergences. 
 
If  x  is a fixed point on  H
3  and  V  is a tangent vector to  H3  at  x ,  then the parallel 
transport  PyxV  of  V  to the point  y  is defined for all  y ∊ H3 ,  and may be viewed 
as a vector field on  H3 . 
 
We need to know the curl and divergence of this vector field. 
 
 
PROPOSITION 39.1.     
                                                                       [y , x , V]                                           ∇
y  ×  PyxV  =  ——————————— .                                                                     1  +  < x , y > 
 
 
PROPOSITION 39.2. 
                              
 — 2 < y, V >                                          ∇y ∙ PyxV  =  —————————— .                                                                      1 + < x, y > 
 
 
We use the same definitions as on  S3  for the curl and the divergence, namely 
 
∇ × W  =  ⇑ d ↓ W , 
and 
∇ ∙ W  =  * d ⇓ W . 
 
For example, suppose  W  is the vector field  E1  =  PyxX1 .  Then 
 
       ∇y × E1  =  ⇑ d ↓ E1  =  ⇑ d θ1   
 
                        =  ⇑ — (y
2/(1 + y0)  θ1 ∧ θ2  +  y3/(1 + y0)  θ3 ∧ θ1) 
 
                        =  — y2/(1 + y0)  E3  +  y3/(1 + y0)  E2 . 
 
And likewise  
 
       ∇
y × E2  =  — y3/(1 + y0)  E1  +  y1/(1 + y0)  E3 
 
       ∇y × E3  =  — y1/(1 + y0)  E2  +  y2/(1 + y0)  E1 . 
 
Note that these formulas are the negatives of the ones obtained on  S3  in section 18. 
 
 81 
 
 
 
 
They can be viewed as special instances of the formula given above in  
Proposition 39.1.  For example, if  y  =  (y
0 , y1 , y2 , y3 ) ,  x  =  (1, 0, 0, 0)   
and  V  =  X1 ,  then one easily calculates that 
 
      [y , x , V]  =  y3 E2  —  y2 E3 .  
 
Dividing through by  1  +  < x, y >  =  1  +  y
0  gives the formula for  ∇y × E1 
appearing above, and so verifies Proposition 39.1 in this instance.  Just as in the 
case of  S3 ,  the verification of the proposition in this single instance also serves  
as its proof. 
 
 
 
The divergence of a vector field  W  was defined above by   ∇ ∙ W  =  * d ⇓ W . 
If  W  is the vector field  E
1  =  PyxX1 ,  then 
 
                       ∇ ∙ E1  =  * d ⇓ E1  =  * d (θ2 ∧ θ3) 
 
                                           =  * (dθ
2 ∧ θ3  —  θ2 ∧ dθ3) 
 
                                           =  * (2 y1/(1 + y0)) θ1 ∧ θ2 ∧ θ3 
 
                                           =  2 y1/(1 + y0) , 
 
using the formulas for  dθ
2  and  dθ3  appearing in the previous section. 
 
The above example can be viewed as a special instance of the formula given in 
Proposition 39.2, since   
 
< y , V >  =  < y , X
1 >  =  — y1   and  1  +  < x , y >  =  1  +  y0 . 
 
And just as before, this single verification of the proposition also serves as its 
proof. 
 
 
 
 82 
 
 
 
 
40. Statement of the Key Lemma. 
 
The following result plays a lead role in obtaining the formulas for the Biot-Savart 
and Green’s operators on  H
3  in parallel transport format. 
 
 
KEY LEMMA, hyperbolic version. 
 
                    ∇∇∇∇y ×××× {PyxV(x) ×××× ∇∇∇∇y ϕϕϕϕ}  —  ∇∇∇∇y {V(x) ∙∙∙∙ ∇∇∇∇x (cosh α α α α  ϕϕϕϕ)}   
 
                                                                 =  (∆∆∆∆ϕϕϕϕ  +  ϕϕϕϕ) (V(x)  —  < V(x), y > y) .  
 
 
As usual,  α   is the distance on  H
3  between  x  and  y .  The kernel function  ϕ(α)   
is any smooth function, which typically blows up at  α  = 0  and is asymptotic there 
to  —1/(4πα ) .   
 
The Key Lemma can be understood intuitively when  ϕ(α )  is the fundamental 
solution of the operator  ϕ  →   ∆ϕ   +  ϕ   on  S3 ,  in which case we will see that  
cosh α  ϕ(α )  is, up to an additive constant, the fundamental solution of the scalar 
Laplacian there. 
 
Then, just as on  S
3 ,  the Key Lemma can be viewed as a pointwise or infinitesimal 
version of Maxwell’s equation 
 
∇ × B  —  ∂E/∂t    =  V  . 
 
 83 
 
 
41. The first term on the LHS of the Key Lemma. 
 
The plan is the same as it was for  S
3 .  Applying an appropriate isometry of  H3 ,  
we can assume that  x  is the point  (1, 0, 0, 0)  and that, after scaling,   
V(x)  =  X1  =  (0, 1, 0, 0) .  At each point  y  =  (y0 , y1 , y2 , y3)  of  H3 ,  we will 
expand both sides of the Key Lemma in terms of the orthonormal basis  E1 ,  E2  
and  E3  for  TyH3 ,  and prove equality component-wise. 
 
We begin with the first term on the LHS of the equation, and note that 
 
P
yxV(x)  ×  ∇y ϕ  =  PyxV(x)  ×  (—Pyx ∇x ϕ)  =  Pyx (— V(x)  ×  ∇x ϕ) . 
 
From section 35, we have that 
 
                      ∇
x α   =  (cosh α   x  —  y) / sinh α  
 
                                      =  ((y0 , 0 , 0 , 0)  —  (y0 , y1 , y2 , y3)) / sinh α  
 
                                      =  (—1 / sinh α ) (y1 X1  +  y2 X2  +  y3 X3) . 
 
Hence 
 
∇
x ϕ  =  ϕ’(α ) ∇x α   =  (— ϕ’(α ) / sinh α) (y1 X1  +  y2 X2  +  y3 X3) . 
 
Thus 
 
     — V(x) × ∇
x ϕ  =  (—X1)  ×  (— ϕ’(α ) / sinh α) (y1 X1  +  y2 X2  +  y3 X3) 
 
                                     =  (ϕ’(α ) / sinh α ) ( —y3 X2  +  y2 X3) . 
 
Hence 
 
        P
yxV(x)  ×  ∇y ϕ  =  Pyx (— V(x)  ×  ∇x ϕ) 
 
                                     =  (ϕ’(α ) / sinh α ) ( —y3 E2  +  y2 E3) . 
 
 
 84 
 
 
 
 
Now we take curls and evaluate the first term on the LHS of the Key Lemma, 
 
∇
y  ×  {PyxV(x)  ×  ∇y ϕ}  =  ∇y  ×  {(ϕ’(α ) / sinh α ) ( —y3 E2  +  y2 E3)} . 
 
We begin by computing the curl of the vector field 
 
W  =  W(y)  =  —y3 E2  +  y2 E3 , 
 
following the recipe   ∇y × W  =  ⇑ d ↓ W .  The computation is similar to the one 
on  S3 ,  and yields 
 
∇y × W  =  2 (y0  —  y1
2/(1 + y0)) E1  —  2 (y1y2 / (1 + y0)) Ε2  —  2 (y1y3 / (1 + y0)) E3 .                   
 
Now to compute  ∇y  ×  {(ϕ’(α ) / sinh α ) ( —y3 E2  +  y2 E3)} ,  we use the formula 
 
∇  ×  (f W)  =  f (∇ × W)  +  ∇f  × W , 
 
with  f (α )  =  ϕ’(α ) / sinh α ,  and find that 
 
∇y  ×  {PyxV(x)  ×  ∇y ϕ}  =  ∇y  ×  {(ϕ’(α ) / sinh α ) ( —y3 E2  +  y2 E3)} 
 
=  
{ (2ϕ’/sinh α ) (y0  —  y1
2/(1 + y0))  +  (ϕ"/sinh2α   —  ϕ’ cosh α /sinh3α ) (y2
2 + y3
2) } E1 
 
        +  { (—2ϕ’/sinh α ) y1y2/(1 + y0)   +      (ϕ"/sinh2α   —  ϕ’ cosh α /sinh3α ) (—y1y2) } E2 
 
        +  { (—2ϕ’/sinh α ) y1y3/(1 + y0)   +      (ϕ"/sinh2α   —  ϕ’ cosh α /sinh3α ) (—y1y3) } E3 . 
 
This puts the first term on the LHS of the Key Lemma in the form we want it. 
 
 
 85 
 
 
 
42. The second term on the LHS of the Key Lemma. 
 
Now, just as we did for the first term, we want to express the second term 
 
— ∇y {V(x) ∙ ∇x (cosh α   ϕ)} 
 
on the LHS of the Key Lemma as a linear combination of the orthonormal basis 
vectors  E
1 ,  E2  and  E3  for  TyH3 .   
 
We follow the procedure used on  S3  in section 21, and find that 
 
— ∇y {V(x) ∙ ∇x (cosh α   ϕ)} 
 
               =  
{ (ϕ" cosh α /sinh2α   +  ϕ’(1/sinh α   —  1/sinh3α )) y1
2   
 
                                                +  (ϕ’ cosh α /sinh α   +  ϕ) (1  +  y1
2/(1 + y0)) } E1 
 
                    +  { (ϕ" cosh α /sinh2α   +  ϕ’(1/sinh α   —  1/sinh3α )) y1y2   
 
                                                         +  (ϕ’ cosh α /sinh α   +  ϕ) y
1y2/(1 + y0) } E2 
 
                    +  { (ϕ" cosh α /sinh2α   +  ϕ’(1/sinh α   —  1/sinh3α )) y1y3   
 
                                                         +  (ϕ’ cosh α /sinh α   +  ϕ) y1y3/(1 + y0) } E3 . 
  
 
If we combine the two terms on the LHS of the Key Lemma and simplify, we get 
 
     ∇
y  ×  {PyxV(x)  ×  ∇y ϕ}  —  ∇y {V(x) ∙ ∇x (cosh α   ϕ)} 
 
                                =  {(ϕ"  +  2 ϕ’ cosh α /sinh α   +  ϕ) (1  +  y1
2/(1 + y0)) } E1 
 
                                   +  {(ϕ"  +  2 ϕ’ cosh α /sinh α   +  ϕ) (y1y2/(1 + y0)) } E2 
 
                                   +  {(ϕ"  +  2 ϕ’ cosh α /sinh α   +  ϕ) (y1y3/(1 + y0)) } E3 . 
 
 
 86 
 
 
 
 
43. The RHS of the Key Lemma.
 
 
Now we express the RHS 
 
(∆ϕ   +  ϕ) (V(x)  —  < V(x) , y > y) 
 
as a linear combination of  E
1 ,  E2  and  E3 . 
 
Recall that 
 
∆ϕ   =  ϕ"  +  2 ϕ’ cosh α /sinh α  , 
 
and hence 
 
∆ϕ   +  ϕ  =  ϕ"  +  2 ϕ’ cosh α /sinh α  +  ϕ . 
 
We follow the procedure used on  S
3  in section 22, and find that 
 
     (∆ϕ   +  ϕ) (V(x)  —  < V(x) , y > y)  
 
                                =  
{(ϕ"  +  2 ϕ’ cosh α /sinh α   +  ϕ) (1  +  y1
2/(1 + y0)) } E1 
 
                                      +  {(ϕ"  +  2 ϕ’ cosh α /sinh α   +  ϕ) (y1y2/(1 + y0)) } E2 
 
                                      +  {(ϕ"  +  2 ϕ’ cosh α /sinh α   +  ϕ) (y1y3/(1 + y0)) } E3 . 
 
This matches the LHS, as given in the previous section, and so completes the 
proof of the Key Lemma. 
 
 
 
 87 
 
 
44. Maxwell’s equation in  H3 . 
 
We now apply the Key Lemma to the proof of Maxwell’s equation 
 
∇ × B  =  V  +  ∂E/∂t  
 
in  H3 .  In the Key Lemma, we use the kernel function 
 
ϕ(α )  =  (—1/4π) csch α  , 
 
which, as we noted earlier, is a fundamental solution of the shifted Laplacian on  H3 , 
 
∆ϕ  +  ϕ  =  δ . 
 
With this choice of kernel function, we have that 
 
(cosh α ) ϕ(α )  =  (—1/4π) coth α , 
 
which differs from the fundamental solution of the Laplacian on  H
3 , 
 
ϕ0(α )  =  (—1/4π) (coth α   —  1) , 
 
only by a constant.  Since we take the gradient of this function below, the 
difference is irrelevant. 
 
Hence with these choices, the Key Lemma reads 
 
     ∇
y × {PyxV(x) × ∇yϕ}  —  ∇y {V(x) ∙ ∇x ϕ0}   
 
                                                                 =  δ(x, y) 
(V(x)  —  < V(x), y > y) .  
 
Keeping these choices of kernel functions, we now define the Biot-Savart operator 
by formula (3) of Theorem 2, 
 
BS(V)(y)  =  
∫H3  PyxV(x) × ∇y ϕ(x, y) dx , 
 
for smooth, compactly supported vector fields  V . 
 
 88 
 
 
 
 
Then we integrate the Key Lemma over  H
3  and get 
 
   ∫H3  ∇y × {PyxV(x) × ∇yϕ} dx   —   ∫H3  ∇y {V(x) ∙ ∇x ϕ0}  dx 
 
                                                          =   ∫H3  δ(x, y) (V(x)  —  < V(x), y > y)  dx . 
 
We process this just as we did on  S
3  in section 23, and obtain 
 
∇y × BS(V)(y)  =  V(y)  +  ∇y ∫H3  V(x) ∙ ∇x ϕ0(x, y)  dx . 
 
As in  R3  and on  S3 ,  we recognize this as Maxwell’s equation 
 
∇ × B  =  V  +  ∂E/∂t . 
 
 
 
45.  Proof of Theorem 2, formula (3) . 
 
Let  V  be a smooth compactly supported vector field in  H3 .  Thinking of  V  as a 
steady current flow, we defined the corresponding magnetic field  BS(V)  by  
 
BS(V)(y)  =  ∫H3  PyxV(x) × ∇y ϕ(x, y)  dx , 
 
where  ϕ(α )  =  (—1/4π) csch α  . 
 
We saw in the preceding section that, as a consequence of the Key Lemma, the 
field  BS(V)  satisfies Maxwell’s equation. 
 
To complete the proof of Theorem 2, formula (3), we need only show that  BS(V)  
is divergence-free.   
 
But the argument for this in  H
3  is identical to that in  S3 ,  so we are done. 
 
 
 
 
 89 
 
 
 
 
46. The Green’s operator on  H3  in parallel transport format. 
 
We turn now to the derivation of formula (3) of Theorem 3 for the vector-valued 
Green’s operator on  H3 , 
 
Gr(V)(y)  =   ∫H3  PyxV(x)  ϕ2(x, y)  dx   +   ∇y∫H3  PyxV(x) ∙ ∇yϕ3(x, y)  dx , 
 
where 
 
       ϕ
2(α )  =  (—1/4π) csch α   +  (1/4π) α / (1 + cosh α ) 
 
and  
 
       ϕ
3(α )  =  (1/4π) α  / (e2α
 — 1)  +  (1/4π) ∫0
α  ((α  / sinh α )  —  (α 2 / 2 sinh2α ))  dα . 
 
 
The naming of the kernel functions  ϕ
2  and  ϕ3  above leaves room in the ϕ-family  
for the fundamental solution of the Laplacian on  H3 , 
 
       ϕ
0(α )  =  (—1/4π) (coth α  —  1)                         ∆ϕ0  =  δ  
 
and for the kernel function of the Biot-Savart operator,  
 
       ϕ
1(α )  =  (—1/4π) csch α               ∆ϕ 1  +  ϕ1  =  δ . 
 
 
 90 
 
 
 
47. Plan of the proof. 
 
Consider the usual vector convolutions,  
 
     A(V, ϕ)(y)  =  
∫H3  PyxV(x) ϕ(x, y)  dx 
 
     B(V, ϕ)(y)  =  ∫H3  PyxV(x)  ×  ∇yϕ(x, y)  dx 
 
      g(V, ϕ)(y)  =  ∫H3  PyxV(x)  ∙  ∇yϕ(x, y)  dx 
 
     G(V, ϕ)(y)  =  ∇
y g(V, ϕ)(y)  =  ∇y ∫H3  PyxV(x)  ∙  ∇yϕ(x, y)  dx . 
 
Step 1.  First we will determine the unknown kernel function  ϕ  so as to make 
 
∇y  ×  A(V, ϕ)(y)  =  — B(V, ϕ1)(y)  =  — BS(V)(y) . 
 
The solution we obtain is not unique. 
 
Step 2.  Then, as a consequence of Maxwell’s equation, we will have 
 
        — ∇
y × ∇y × A(V, ϕ2)(y)  =  ∇y × BS(V)(y)   
 
   
                                               =  V(y)  —  ∇y ∫H3  ∇x ∙ V(x)  ϕ0(x, y)  dx . 
Hence 
 
∆
y A(V, ϕ2)(y)  =  — ∇y × ∇y × A(V, ϕ2)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) 
 
                      =  V(y)  —  ∇y ∫H3  ∇x ∙ V(x)  ϕ0(x, y)  dx   +  ∇y(∇y ∙ A(V, ϕ2)(y)) 
 
                      =  V(y)  +  some gradient field . 
 
We then find the kernel function  ϕ
3  so that  ∆y G(V, ϕ3)(y)  =  G(V, ∆ϕ 3)(y)   
is the negative of the above gradient field, in which case, defining 
 
Gr(V)(y)  =  A(V, ϕ2)(y)  +  G(V, ϕ3)(y) 
 
yields the desired  equation  ∆y Gr(V)(y)  =  V(y) . 
 
 91 
 
 
 
48. Some formulas that we will use. 
 
In the formulas below,  V  is a single tangent vector at the single point  x ∊ H3 . 
 
                                                            <y, V> (1)                             P
yxV  =  V  —  ————————  (x  +  y)                                                           1 + <x, y> 
 
                                                  [y, x, V] (2)                 ∇y × PyxV  =  ————————                                                   1 + <x, y> 
 
                      — 2 <y, V> (3)                ∇y ∙ PyxV  =  ————————                                                   1 + <x, y> 
 
 
(4)                 PyxV  ×  ∇yϕ  =  — [y, x, V] ϕ’(α ) / sinh α  . 
 
 
Formula (1) appears in section 37, while formulas (2) and (3) appear in section 39.  
 
Formula (4) in the special case that  x  =  (1, 0, 0, 0)  and  V  =  X
1  =  (0, 1, 0, 0) 
is obtained from the formula 
 
PyxV ×  ∇y ϕ  =  (ϕ’(α ) / sinh α ) (—y3 E2  +  y2 E3) 
 
of section 41, together with the remark of section 39 that in this case we have 
 
[y , x , V]  =  y
3 E2  —  y2 E3 . 
 
We leave it to the reader to confirm, as we did earlier in similar circumstances, 
that this single case of formula (4) can serve as its proof. 
 
We note that formulas (1), (2) and (3) are identical to the corresponding formulas 
for  S
3  in section 27, but that formula (4) has the opposite sign, in addition to the 
expected replacement of  "sin α "  by  "sinh α " . 
 
 
 92 
 
 
 
49. The curl of  A(V, ϕϕϕϕ)(y) . 
 
∇y × A(V, ϕ)(y)  =  ∫H3  ∇y × {PyxV(x) ϕ(x, y)}  dx 
 
          =  
∫H3  {∇y × PyxV(x)} ϕ(x, y)   —   PyxV(x) × ∇yϕ(x, y)  dx 
 
                      [y, x, V(x)]                                          ϕ’(α )           =  ∫H3  ———————— ϕ(x, y)   +    [y, x, V(x)] —————  dx                        1 + <x, y>                                          sinh α 
 
                                                  ϕ                   ϕ’           =  ∫H3  [y, x, V(x)] {——————— + —————}  dx   ,                                             1 + cosh α         sinh α 
 
thanks to formulas (2) and (4) above. 
 
On the other hand, 
 
      BS(V)(y)  =  B(V, ϕ
1)(y)  =  ∫H3  PyxV(x)  ×  ∇yϕ1(x, y)  dx 
 
                                                                               — ϕ1’(α )                                                =  ∫H3  [y, x, V(x)] ———————   dx  ,                                                                                 sinh α 
 
again by formula (4) . 
 
Thus, in order that 
 
∇
y  ×  A(V, ϕ)(y)  =  — BS(V)(y)  =  — B(V, ϕ1)(y)  , 
 
we must choose  ϕ  to satisfy the ODE 
 
                                 ϕ                   ϕ’                 ϕ1’                          ————————  +  —————   =   ————— .                           1 + cosh α         sinh α          sinh α 
 
This ODE is solved just like the corresponding one in section 28, and we get 
 
(1 + cosh α ) ϕ  =  (1 + cosh α ) ϕ1  +  (1/4π) (α   +  C) . 
 
The choice of the constant  C  represents the nonuniqueness in carrying out Step 1. 
We discuss this further in section 52, but here set  C  =  0  and continue. 
 
 93 
 
 
 
Dividing through by (1 + cosh α ) ,  we get 
 
          ϕ(α)  =  ϕ1(α )  +  (1/4π) α / (1 + cosh α )   
 
                    =   (—1/4π) csch α  +  (1/4π) α / (1 + cosh α ) . 
 
Note that  ϕ(α )  has a singularity at  α   =  0 .   
 
We call this solution  ϕ
2(α ) ,  and with it we have completed Step 1: 
 
∇y  ×  A(V, ϕ2)(y)  =  — B(V, ϕ1)(y)  =  — BS(V)(y) . 
 
We take the negative curl of both sides to get 
    
        — ∇y × ∇y × A(V, ϕ2)(y)  =  ∇y × BS(V)(y)   
 
    
                                               =  V(y)  —  ∇y ∫H3  (∇x ∙ V(x))  ϕ0(x, y)  dx , 
 
thanks to Maxwell’s equation.  Integrating by parts, we have 
 
          ∫H3  (∇x ∙ V(x))  ϕ0(x, y)  dx  =  — ∫H3  V(x) ∙ ∇xϕ0(x, y)  dx 
 
                                                                 =  
∫H3  PyxV(x) ∙ ∇yϕ0(x, y)  dx   
 
                                                                 =  g(V, ϕ0)(y) . 
 
Hence 
 
∆
y A(V, ϕ2)(y)  =  — ∇y × ∇y × A(V, ϕ2)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) 
 
                      =  V(y)  —  ∇y ∫H3  ∇x ∙ V(x)  ϕ0(x, y)  dx   +  ∇y(∇y ∙ A(V, ϕ2)(y))  
 
                      =  V(y)  —  G(V, ϕ0)(y)  +  ∇y(∇y ∙ A(V, ϕ2)(y)) . 
 
 
Just as on  S
3 ,  the next step is to compute  ∇y ∙ A(V, ϕ2)(y) . 
 
 
 94 
 
50. The divergence of  A(V, ϕϕϕϕ2) . 
 
We begin as follows. 
 
     ∇
y ∙ A(V, ϕ2)(y)  =  ∫H3  ∇y ∙ (PyxV(x) ϕ2(x, y))  dx 
 
              =  
∫H3  (∇y ∙ PyxV(x)) ϕ2(x, y)  dx   +  ∫H3  PyxV(x) ∙ ∇yϕ2(x, y)  dx . 
 
The second integral on the RHS above is simply  g(V, ϕ2)(y) ,  so we put that aside.   
 
Turning to the first integral and using formula (3) and the fact that  < x, V(x) >  =  0 , 
we follow the pattern set in section 29 for  S3 ,  and get 
 
         ∫H3  (∇y ∙ PyxV(x)) ϕ2(x, y)  dx  =  ∫H3  PyxV(x) ∙ ∇yψ (α )  dx 
 
                                                                   =  g(V, ψ )(y) , 
 
where the new kernel function  ψ   satisfies  
 
       ψ’(α )  =  [2 sinh α  / (1 + cosh α )] ϕ
2(α )  
 
                  =  [2 sinh α  / (1 + cosh α )] 
[(—1/4π) csch α   +  (1/4π) α  / (1 + cosh α )] 
 
                  =  (—1/2π) / (1 + cosh α )   +   (1/2π) α  sinh α  / (1 + cosh α )2 , 
 
and hence 
ψ (α )  =  (—1/2π) α  / (1 + cosh α ) . 
 
We have set the constant of integration to zero, so that  ψ (α )  →   0  as  α   →   ∞ . 
 
Collecting information, we have 
 
∇
y ∙ A(V, ϕ2)(y)   
 
                   =  ∫H3  (∇y ∙ PyxV(x)) ϕ2(x, y)  dx   +  ∫H3  PyxV(x) ∙ ∇yϕ2(x, y)  dx  
 
                   =  g(V, ψ )(y)  +  g(V, ϕ
2)(y) , 
 
and hence 
∇y (∇y ∙ A(V, ϕ2)(y))  =  G(V, ψ )(y)  +  G(V, ϕ2)(y) . 
 
 95 
 
 
51. Step 2 - Finding and using the kernel function  ϕϕϕϕ3 .    
 
Continuing our calculation of the Laplacian of  A(V, ϕ2)(y) ,  we have 
       
           ∆y A(V, ϕ2)(y)  =  V(y)  —  G(V, ϕ0)(y)   +  ∇y(∇y ∙ A(V, ϕ2)(y))  
 
                                     =  V(y)  —  G(V, ϕ0)(y)  +  G(V, ψ )(y)  +  G(V, ϕ2)(y) 
 
                                     =  V(y)  —  G(V, ϕ
0  —  ϕ2  —  ψ )(y) . 
 
Using the values for  ϕ0 ,  ϕ2  and  ψ   given above, we calculate that 
 
ϕ0  —  ϕ2  —  ψ   =  (1/4π)  —  (1/4π) sinh α  / (1 + cosh α )  +  (1/4π) α  / (1 + cosh α ) . 
 
Now let  ϕ
3(α )  be chosen to satisfy 
 
            ∆ϕ3(α )  =  ϕ0  —  ϕ2  —  ψ 
 
                          =  (1/4π)  —  (1/4π) sinh α  / (1 + cosh α )  +  (1/4π) α  / (1 + cosh α ) . 
 
We have yet to calculate  ϕ
3  explicitly, but once this is done, we will have 
 
∆yG(V, ϕ3)(y)  =  G(V, ∆ϕ 3)(y)  =  G(V, ϕ0 — ϕ2 — ψ )(y) ,  
 
and hence 
 
∆
y {A(V, ϕ2)(y)  +  G(V, ϕ3)(y)} 
 
                              =  ∆y A(V, ϕ2)(y)  +  ∆y G(V, ϕ3)(y) 
 
                              =  ∆y A(V, ϕ2)(y)  +  G(V, ∆ϕ 3)(y) 
 
          =  V(y)  —  G(V, ϕ0 — ϕ2 — ψ )(y)  +  G(V, ϕ0 — ϕ2 — ψ )(y) 
 
                              =  V(y) . 
 
 96 
 
 
 
Therefore, if we define 
 
           Gr(V)(y)  =  A(V, ϕ
2)(y)  +  G(V, ϕ3)(y) 
 
                           =  
∫H3  PyxV(x)  ϕ2(x, y)  dx   +   ∇y ∫H3  PyxV(x) ∙ ∇yϕ3(x, y)  dx , 
 
we have                           
 
         ∆
y Gr(V)(y)  =  V(y) , 
 
as desired. 
 
This completes the proof of Theorem 3, formula (3) for the vector-valued Green’s 
operator in  H
3 ,  modulo the explicit determination of the kernel function  ϕ3 . 
 
We break the calculation of  ϕ3  into two pieces, and begin by writing 
 
ϕ0  —  ϕ2  —  ψ   =  (1/4π)  —  (1/4π) sinh α  / (1 + cosh α )  +  (1/4π) α  / (1 + cosh α ) . 
 
                         =                            ψ
1                               +                    ψ 2 . 
 
To solve the equation 
 
∆ϕ
3  =  ϕ0  —  ϕ2  —  ψ  =  ψ1  +  ψ2 , 
 
we will solve separately the equations 
 
∆Ψ
1  =  ψ 1     and     ∆Ψ 2  =  ψ 2 , 
 
and then add these solutions together to get 
 
ϕ3  =  Ψ 1  +  Ψ 2 . 
 
 
 97 
 
 
 
First piece. 
 
If we define 
Ψ 1(α )  =  (1/4π) α  / (e2α
 — 1)  —  (1/4π) csch α  , 
 
then 
∆Ψ 1  =  (1/4π)  —  (1/4π) sinh α  / (1 + cosh α )  =  ψ 1 . 
 
 
Second piece. 
 
We want to solve the equation 
 
∆Ψ
2  =  (1/4π) α  / (1 + cosh α )  =  ψ 2 . 
 
Following the procedure used on  S3  in section 31, we find that 
 
Ψ 2  =  (1/4π) csch α   +  (1/4π) ∫0
α  ((α  / sinh α )  —  (α 2 / 2 sinh2α ))  dα . 
 
The integral in the second term is non-elementary and involves dilogarithms, 
so we simply leave it as is. 
 
Putting this all together, we have that 
 
        ϕ
3  =  Ψ 1  +  Ψ 2 
 
              =  (1/4π) α  / (e2α
 — 1)  —  (1/4π) csch α  
 
                        +  (1/4π) csch α   +  (1/4π) ∫0
α ((α  / sinh α )  —  (α 2 / 2 sinh2α ))  dα  
 
              =  (1/4π) α  / (e2α
 — 1)  +  (1/4π) ∫0
α ((α  / sinh α )  —  (α 2 / 2 sinh2α ))  dα , 
 
thanks to one cancellation. 
 
This completes the proof of Theorem 3, formula (3) for the Green’s operator in  H
3 . 
  
 
 98 
 
 
52.  Non-uniqueness of the Green’s operator in  H3 . 
 
We have been seeking a formula for the vector-valued Green’s operator in  H3  of 
the type 
 
        Gr(V)(y)  =  A(V, ϕ
2)(y)  +  G(V, ϕ3)(y)    
 
                        =  ∫H3  PyxV(x)  ϕ2(x, y)  dx   +   ∇y∫H3  PyxV(x) ∙ ∇yϕ3(x, y)  dx . 
 
The ambiguity in the choice of  ϕ2(α )  appeared in section 49, and is of the form  
(1/4π) C / (1  +  cosh α ) .  So let’s set 
 
φ2  =  1 / (1  +  cosh α ) , 
 
and think of this as the difference between two competing choices of  ϕ
2 .  
We will have 
 
∇y × A(V, φ2)(y)  =  0 , 
 
since the corresponding integrals for the two choices of  ϕ2  both have the 
same curl, namely  — BS(V)(y) . 
 
Let  φ3  denote the difference between the corresponding choices of  ϕ3 .  This 
kernel function satisfies the equation 
 
∆y{A(V, φ2)(y)  +  G(V, φ3)(y)}  =  0 . 
 
We follow the routine of sections 50 and 51 and learn that 
 
∆φ3  =  1/(1 + cosh α ) . 
 
We solve this for  φ3  and get 
 
φ3’(α )  =  (sinh α   —  α ) / sinh2α  , 
 
and then 
 
φ
3(α )  =  2α  / (e2α
 — 1)   +   2 ln(eα / (eα + 1)) . 
 
 99 
 
 
 
 
Putting this together, we get an explicit formula for the difference  δGr  between 
two competing vector-valued Green’s operators in  H
3 , 
 
        δGr(V)(y)  =  A(V, φ
2)(y)  +  G(V, φ3)(y) 
 
                          =  ∫H3  PyxV(x)  φ2(x, y)  dx   +   ∇y∫H3  PyxV(x) ∙ ∇yφ3(x, y)  dx 
 
                          =  ∫H3  PyxV(x)  (1 / (1 + cosh α ))  dx    
 
                                        +   ∇
y∫H3  PyxV(x)  ∙  ((sinh α   —  α ) / sinh2α )  ∇yα    dx . 
 
We certainly know that  δGr(V)  is a harmonic vector field, that is, its Laplacian 
∆y δGr(V)(y)  =  0 .  But recall from the construction that the first integral in the 
definition of  δGr(V)  is curl-free.  Since  H3  is simply connected, this integral is 
actually a gradient vector field.  The second integral is visibly a gradient field, so  
δGr(V)  is actually a gradient field.  Since it is harmonic, it is the gradient of some 
harmonic function on  H
3 , that is, 
 
δGr(V)(y)  =  ∇y(some harmonic function of  y) . 
 
Further computation reveals that this harmonic function on  H3  is in general not 
constant, and hence the arbitrary choice of the constant  C  in the definition of  ϕ2  
in section 49 does have an effect on  Gr(V) .  As a consequence, the vector-valued 
Green’s operator in  H3 ,  even restricted to the form that we are seeking, is not 
unique. 
 
 100 
 
 
E. ELECTRODYNAMICS AND THE 
GAUSS LINKING INTEGRAL ON  S3  AND  H3 
 
 
53.  Proof of Theorem 4. 
 
Recall from section 7 our assertion in Theorem 4 that the classical Maxwell 
equations, 
 
  ∇ ∙ E  =  ρ     ∇ × E  =  0 
 
  ∇ ∙ B  =  0     ∇ ×  B  =  V  +  ∂E/∂t , 
 
hold on  S
3  and in  H3 ,  just as they do in  R3 . 
 
We have 
 
   ∇
y ∙ E(ρ)(y)  =  ∇y ∙ ∇y ∫ ρ(x) ϕ0(x, y) dx   
 
        =   ∆y ∫ ρ(x) ϕ0(x, y) dx   
 
                                                       =  ρ(y) , 
 
because  ϕ
0  is the fundamental solution of the scalar Laplacian. 
 
We have  ∇ × E  =  0  because  E  is a gradient field. 
 
The equations 
 
∇ ∙ B  =  0     and     ∇ ×  B  =  V  +  ∂E/∂t 
 
were two of the properties required of  B  =  BS(V)  in section 4.  They were proved 
on  S
3  in left-translation format in section 12, on  S3  in parallel transport format in 
sections 23 and 24, and in  H3  in parallel transport format in sections 44 and 45. 
 
This completes the proof of Theorem 4. 
 
 
 101 
 
 
54. Proof scheme for Theorem 1. 
 
Recall from section 2 what we imagine to be Gauss’s second line of reasoning for 
obtaining his linking integral.  Run a current through the first loop, and calculate  
the circulation of the resulting magnetic field around the second loop.  By Ampere's 
Law, this circulation is equal to the total current enclosed by the second loop, 
which means the current flowing along the first loop multiplied by the linking 
number of the two loops.  Then the Biot-Savart formula for the magnetic field 
leads directly to Gauss's linking integral. 
 
                                  Linking numbers via Ampere’s Law 
 
The same line of reasoning in  S
3  and  H3  will lead us in the next two sections 
from the three formulas for the magnetic field given in Theorem 2 to the three 
linking integrals given in Theorem 1. 
 
But there is an issue which must be dealt with first.  We have proved Theorem 2 
only when  V  is a smooth, compactly supported current distribution on  R
3 ,  S3   
or  H3 .  As things stand, when currents run through wires, we have not proved  
the corresponding formula for the resulting magnetic field, nor the accompanying 
Ampere’s Law. 
 
We will get around this by observing that a field defined for a current running in a 
wire loop is the limit, in an appropriate sense, of magnetic fields caused by currents 
running in thin tubular neighborhoods of the loop.  Then the Ampere’s Law that  
we want will simply be the limit of Ampere’s Laws that we already know, as the 
thickness of the neighborhoods goes to zero. 
 
 102 
 
 
 
 
The argument is elementary, so we just outline it and leave the details to the reader. 
 
Let  K  be a simple closed curve in an oriented Riemannian 3-manifold  M ,  which 
in the present case is either  R
3 ,  S3  or  H3 .  Let  r0  >  0  be a small real number,  
and let  Nr0  be the  r0-neighborhood of  K  in  M ,  that is, the set of all points in  M  
whose distance from  K  is less than  r0 .  We choose  r0  small enough so that  Nr0   
is a traditional embedded tubular neighborhood of  K . 
 
Let  K  =  {X(s) ,  0  ≤  s  ≤  L}  be a parametrization of  K  by arc length, and let   
T(s)  =  dX/ds  =  X’(s)  be the resulting unit tangent vector field along  K  .  Extend 
this vector field to an orthonormal frame field  T(s) ,  N(s) ,  B(s)  along  K .  This is 
possible because the normal bundle of a smooth curve in an oriented manifold is 
always trivial.  The notation is chosen to remind us of the Frenet frame, consisting 
of the tangent, principal normal and binormal vectors along a smooth curve of 
nowhere vanishing curvature in Euclidean 3-space  R
3 . 
 
Given this orthonormal frame field along  K ,  we can use the exponential map of  
the Riemannian manifold  M  to parametrize the tubular neighborhood  Nr0  by the 
product of  K  and a Euclidean disk of radius  r0  as follows: 
 
(s, u, v)  →   X(s, u, v)  =  expX(s) (u N(s)  +  v B(s)) , 
 
where  0  ≤  s  ≤  L  and  0  ≤  u2  +  v2  <  r0
2 .  In  R3 ,  this would simplify to 
 
X(s, u, v)  =  X(s)  +  u N(s)  +  v B(s) . 
 
Now let  V(s, u, v)  =  ∂X(s, u, v)/∂s  be the tangent vector field to the s-coordinate 
curves, each of which is a simple closed curve having constant  u  and  v  coordinates. 
Since the exponential map takes rays in the normal plane to  K  at  X(s)  to geodesics 
orthogonal to  K , each of the s-coordinate curves remains at the constant geodesic 
distance  (u
2  +  v2)1/2  from  K .  
 
LEMMA.  The vector field  V(s, u, v)  =  ∂X(s, u, v)/∂s  can be rescaled to make 
it divergence-free. 
 
The proof is elementary and we leave it to the reader. 
 
 103 
 
 
 
 
 
It is easy to further rescale and concentrate the flow  V  in  N
r0  to a flow  fε V  that  
is supported in thinner and thinner tubular neighborhoods  N ε  of  K ,  yet always  
has unit flux through the cross-sectional disks. 
 
As  ε →  0 ,  we regard the fields  fε V  supported inside the neighborhoods  Nε 
of  K  as closer and closer approximations to the unit tangent field  X’(s)  =  T(s) 
along  K . 
 
We now change notation slightly for convenience. 
 
Let  K  =  {x(s)}  be a smooth simple closed curve in  R
3 ,  S3  or  H3 ,  and let   
V  =  dx/ds  be the unit tangent vector field along  K .  Let  BS(V)  denote the 
field defined in the complement of  K  by using any of the Biot-Savart formulas 
in  R3 ,  S3  or  H3  and by carrying out the required integrations with respect to  
arc length along  K ,  rather than with respect to volume in the ambient space. 
 
Let  Vε  denote a divergence-free field supported inside the tubular neighborhood 
Nε  of  K  and having unit flux through the cross-sectional disks, as constructed 
above.  In particular, all the vector fields  Vε
  are rescalings of a single vector field.  
Let  BS(Vε)  denote the corresponding magnetic field defined throughout the ambient 
space by using the same Biot-Savart formula as for  V . 
 
LEMMA.  As  ε  →   0 ,  the magnetic fields  BS(Vε)  converge uniformly to the  
field  BS(V)  on any compact subset of the complement of  K . 
 
Again, the proof of this is straightforward, and we leave the details to the reader. 
 
 
As a consequence, Ampere’s law for the field  BS(V)  is the limit of Ampere’s Laws 
for the fields  BS(V
ε)  as  ε →  0 .  In particular, it can and will be applied to a loop 
in the complement of  K  which bounds a surface cutting through  K . 
 
 
 104 
 
55. Proof of Theorem 1, formula (1). 
 
Let  K1  =  {x(s)}  and  K2  =  {y(t)}  be disjoint oriented smooth closed curves 
in the unit 3-sphere  S3 .  We must show that in left-translation format, we have 
 
         Lk(K1, K2)  =  1/(4π2) ∫K1×K2  Lyx—1 dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt 
 
                     —  1/(4π2) ∫K1×K2  Lyx—1 dx/ds ∙ dy/dt  ds dt  , 
 
where  ϕ(α )  =  (π — α ) cot α  . 
 
For the moment, we assume that the curve  K
1  is simple, and that its parametri- 
zation  x  =  x(s)  is by arc-length, so that  V(x)  =  dx/ds  is a unit tangent vector 
field along  K1 . 
 
Then we take Theorem 2, formula (1) for the Biot-Savart operator in left-translation 
format and, given the discussion in the preceding section, apply it to the current 
flow  V  along the loop  K
1  to get 
 
  BS(V)(y)  =  ∫K1  Lyx—1 V(x) × ∇y ϕ0(x, y)  ds    
 
       —  1/4π
2 ∫K1  Lyx—1 V(x)  ds 
 
          +  2 ∇y ∫K1  Lyx—1 V(x) ∙ ∇y ϕ1(x, y)  ds , 
 
where    ϕ0(α )  =  (—1/4π2) (π — α ) cot α    and     ϕ1(α )  =  (—1/16π2) α  (2π — α ) . 
 
Note that 
 
           L
yx—1 V(x) ∙ ∇y ϕ1(x, y)  =  — V(x) ∙ ∇xϕ1(x, y) 
 
                                                   =  — dx/ds ∙ ∇xϕ1(x(s), y)   
 
                                                   =  —  (d/ds) ϕ
1(x(s), y) , 
 
whose integral around the loop  K1  is zero.  So we can drop the third integral 
and are left with 
 
  BS(V)(y)  =  ∫K1  Lyx—1 V(x) × ∇y ϕ0(x, y)  ds    
 
       —  1/4π2 ∫K1  Lyx—1 V(x)  ds . 
 
 105 
 
 
Then we compute the circulation of  BS(V)  around the loop  K2 ,  as follows. 
 
∫
K2  BS(V)(y) ∙ dy/dt  dt   
 
  =  ∫K2  (∫K1  Lyx—1 V(x) × ∇y ϕ0(x, y)  ds  — 1/4π2 ∫K1  Lyx—1 V(x)  ds) ∙ dy/dt  dt 
 
                                          =  ∫K1×K2  Lyx—1dx/ds × ∇y ϕ0(x, y) ∙ dy/dt  ds dt 
 
                          —  1/4π
2
 ∫K1×K2  Lyx—1dx/ds  ∙  dy/dt  ds dt 
 
                                          =  —∫K1×K2  Lyx—1dx/ds × dy/dt  ∙ ∇y ϕ0(x, y)  ds dt 
 
                                                               —  1/4π2
 ∫K1×K2  Lyx—1dx/ds  ∙  dy/dt  ds dt , 
 
where we still have  ϕ
0(α )  =  (—1/4π2) (π — α ) cot α  , 
 
                                           =  1/4π2 ∫K1×K2  Lyx—1dx/ds × dy/dt  ∙∇y ϕ0(x, y)  ds dt 
 
                                                               —  1/4π2
 ∫K1×K2  Lyx—1dx/ds  ∙  dy/dt  ds dt , 
 
where now  ϕ
0(α )  =  (π — α ) cot α . 
 
We apply Ampere’s Law to the field  BS(V) ,  as indicated in the previous section,  
and conclude that 
 
              Lk(K
1 , K2)  =  1/4π2 ∫K1×K2  Lyx—1dx/ds × dy/dt  ∙ ∇y ϕ0(x, y)  ds dt 
 
                                                     —  1/4π2
 ∫K1×K2  Lyx—1dx/ds  ∙  dy/dt  ds dt . 
 
The assumption that the loop  K
1  is simple, which we needed to get an embedded 
tubular neighborhood, can now be dropped, since the linking number does not 
change as either curve crosses itself, and the value of the integral depends 
continuously on the curves  K
1  and  K2 . 
 
The assumption that the loop  K1  is parametrized by arc length can also be dropped, 
since the two integrals on the right hand side above are independent of parametriza- 
tion of either curve, as long as these parametrizations respect the give orientations. 
 
This completes the proof of Theorem 1, formula (1) for the Gauss linking integral 
on  S
3  in left-translation format. 
 
 106 
 
 
56. Proof of Theorem 1, formulas (2) and (3) . 
 
We start on  S3 ,  and begin with the same set-up and notation used in the preceding 
section.  We must show that in parallel transport format, we have 
 
         Lk(K1, K2)  =  1/4π2 ∫K1×K2  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt , 
   
where     ϕ(α )  =  (π — α ) csc α  . 
 
We take Theorem 2, formula (2) for the Biot-Savart operator in parallel transport 
format and apply it to the current flow  V  along the loop  K1  to get 
 
BS(V)(y)  =  ∫K1  PyxV(x)  ×  ∇y ϕ(x, y) ds , 
 
where  ϕ(α )  =  (—1/4π2) (π — α ) csc α  . 
 
Then we compute the circulation of  BS(V)  around the loop  K
2 ,  as follows. 
 
∫K2  BS(V)(y) ∙ dy/dt  dt  = 
 
                     =  ∫K2  (∫K1  Pyx dx/ds  ×  ∇y ϕ(x, y)  ds)  ∙  dy/dt  dt 
 
                              =  
∫K1×K2  Pyx dx/ds  ×  ∇y ϕ(x, y)  ∙  dy/dt  ds dt 
 
                              =  —∫K1×K2  Pyx dx/ds  ×  dy/dt  ∙  ∇y ϕ(x, y)  ds dt , 
 
where we still have   ϕ(α )  =  (—1/4π2) (π — α ) csc α , 
 
                              =  1/4π
2∫K1×K2  Pyx dx/ds  ×  dy/dt  ∙  ∇y ϕ(x, y)  ds dt , 
 
where now  ϕ(α )  =  (π — α ) csc α  . 
 
As before, we apply Ampere’s Law to the field  BS(V)  and conclude that 
 
         Lk(K
1, K2)  =  1/4π2 ∫K1×K2  Pyx dx/ds × dy/dt ∙ ∇y ϕ(x, y)  ds dt . 
 
Then, as in the preceding section, we can drop the assumptions that the loop  K1 
is simple and is parametrized by arc length, completing the proof of Theorem 1, 
formula (2) for the Gauss linking integral on  S3  in parallel transport format 
 
The proof of Theorem 1, formula (3) for the Gauss linking integral on  H3 
in parallel transport format is the same, and we are done. 
 
 107
