---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-021-18-curls-and-divergences
section_title: "Curls and divergences."
section_number: 18
pages: 43-46
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
If  x  is a fixed point on  S3  and  V  is a tangent vector to  S3  at  x ,  then the parallel 
transport  PyxV  of  V  to the point  y  is defined for all  y  ≠  —x ,  and may be 
viewed as a vector field on  S3  —  {—x} ,  as illustrated in section 13. 
 
We need to know the curl and divergence of this vector field. 
 
 
PROPOSITION 18.1.     
                                                                       [y , x , V] 
                                          ∇y  ×  PyxV  =  ——————————— . 
                                                                    1  +  < x , y > 
 
 
PROPOSITION 18.2. 
                               — 2 < y, V > 
                                         ∇y ∙ PyxV  =  —————————— . 
                                                                     1 + < x, y > 
 
 
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
 
For example,  ↓Ei  =  θi   and  ↑θi  =  Ei   for  i  =  1, 2, 3.  Likewise  ⇓E1  =  θ2 ∧ θ3 ,  
⇓E2  =  θ3 ∧ θ1   and   ⇓E3  =  θ1 ∧ θ2 ,   and  ⇑  is simply the inverse of this. 
 
 
 
 
 
With these notations set, the curl of a vector field  W  is defined, as usual, by 
 
∇ × W  =  ⇑ d ↓ W , 
 
that is, we convert  W  to the 1-form  ↓W ,  take its exterior derivative to get the 
2-form  d ↓ W ,  and then convert this to the vector field  ⇑ d ↓ W . 
 
For example, suppose  W  is the vector field  E1  =  PyxX1 .  Then 
 
       ∇y × E1  =  ⇑ d ↓ E1  =  ⇑ d θ1   
 
                        =  ⇑ (y2/(1 + y0)  θ1 ∧ θ2  —  y3/(1 + y0)  θ3 ∧ θ1) 
 
                        =  y2/(1 + y0)  E3  —  y3/(1 + y0)  E2 . 
 
And likewise  
 
       ∇y × E2  =  y3/(1 + y0)  E1  —  y1/(1 + y0)  E3 
 
       ∇y × E3  =  y1/(1 + y0)  E2  —  y2/(1 + y0)  E1 . 
 
These formulas can be viewed as special instances of the formula given above in 
Proposition 18.1.  For example, if  y  =  (y0 , y1 , y2 , y3 ) ,  x  =  (1, 0, 0, 0)  and 
V  =  X1 ,  then one easily calculates that 
 
      [y , x , V]  =  y2 E3  —  y3 E2 .  
 
Dividing through by  1  +  < x, y >  =  1  +  y0  gives the formula for  ∇y × E1 
appearing above, and so verifies Proposition 18.1 in this instance. 
 
Both sides of the formula in Proposition 18.1 are linear in  V ,  so we can certainly 
rescale  V  to be a unit vector.  Also, both sides of this formula are invariant under 
an orientation preserving isometry of  S3 ,  so we can move  x  to the point   
(1, 0, 0, 0)  and  V  to the tangent vector  E1 . 
 
Thus the above verification of Proposition 18.1 in this single instance also serves  
as its proof. 
 
 
 
 
 
The divergence of a vector field  W  is defined by 
 
∇ ∙ W  =  * d ⇓ W , 
 
where  *  is the Hodge star operator which converts the 3-form  f d(vol)  to the 
function  f .  Thus the divergence of the vector field  W  is calculated by converting 
it to the 2-form  ⇓ W ,  taking its exterior derivative to get the 3-form  d ⇓ W , 
and then converting this to the function  * d ⇓ W . 
 
For example, suppose  W  is the vector field  E1  =  PyxX1 .  Then 
 
                       ∇ ∙ E1  =  * d ⇓ E1  =  * d (θ2 ∧ θ3) 
 
                                           =  * (dθ2 ∧ θ3  —  θ2 ∧ dθ3) 
 
                                           =  * (—2 y1/(1 + y0)) θ1 ∧ θ2 ∧ θ3 
 
                                           =  —2 y1/(1 + y0) , 
 
using the formulas for  dθ2  and  dθ3  appearing in the previous section. 
 
The above example can be viewed as a special instance of the formula given in 
Proposition 18.2, since   
 
< y , V >  =  < y , X1 >  =  y1   and  1  +  < x , y >  =  1  +  y0 . 
 
And just as in the case of the curl formula of Proposition 18.1, this single 
verification of Proposition 18.2 also serves as its proof.
