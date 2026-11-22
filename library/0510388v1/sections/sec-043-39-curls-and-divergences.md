---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-043-39-curls-and-divergences
section_title: "Curls and divergences."
section_number: 39
pages: 80-82
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
If  x  is a fixed point on  H3  and  V  is a tangent vector to  H3  at  x ,  then the parallel 
transport  PyxV  of  V  to the point  y  is defined for all  y ∊ H3 ,  and may be viewed 
as a vector field on  H3 . 
 
We need to know the curl and divergence of this vector field. 
 
 
PROPOSITION 39.1.     
                                                                       [y , x , V] 
                                          ∇y  ×  PyxV  =  ——————————— . 
                                                                    1  +  < x , y > 
 
 
PROPOSITION 39.2. 
                               — 2 < y, V > 
                                         ∇y ∙ PyxV  =  —————————— . 
                                                                     1 + < x, y > 
 
 
We use the same definitions as on  S3  for the curl and the divergence, namely 
 
∇ × W  =  ⇑ d ↓ W , 
and 
∇ ∙ W  =  * d ⇓ W . 
 
For example, suppose  W  is the vector field  E1  =  PyxX1 .  Then 
 
       ∇y × E1  =  ⇑ d ↓ E1  =  ⇑ d θ1   
 
                        =  ⇑ — (y2/(1 + y0)  θ1 ∧ θ2  +  y3/(1 + y0)  θ3 ∧ θ1) 
 
                        =  — y2/(1 + y0)  E3  +  y3/(1 + y0)  E2 . 
 
And likewise  
 
       ∇y × E2  =  — y3/(1 + y0)  E1  +  y1/(1 + y0)  E3 
 
       ∇y × E3  =  — y1/(1 + y0)  E2  +  y2/(1 + y0)  E1 . 
 
Note that these formulas are the negatives of the ones obtained on  S3  in section 18. 
 
 
 
 
 
 
They can be viewed as special instances of the formula given above in  
Proposition 39.1.  For example, if  y  =  (y0 , y1 , y2 , y3 ) ,  x  =  (1, 0, 0, 0)   
and  V  =  X1 ,  then one easily calculates that 
 
      [y , x , V]  =  y3 E2  —  y2 E3 .  
 
Dividing through by  1  +  < x, y >  =  1  +  y0  gives the formula for  ∇y × E1 
appearing above, and so verifies Proposition 39.1 in this instance.  Just as in the 
case of  S3 ,  the verification of the proposition in this single instance also serves  
as its proof. 
 
 
 
The divergence of a vector field  W  was defined above by   ∇ ∙ W  =  * d ⇓ W . 
If  W  is the vector field  E1  =  PyxX1 ,  then 
 
                       ∇ ∙ E1  =  * d ⇓ E1  =  * d (θ2 ∧ θ3) 
 
                                           =  * (dθ2 ∧ θ3  —  θ2 ∧ dθ3) 
 
                                           =  * (2 y1/(1 + y0)) θ1 ∧ θ2 ∧ θ3 
 
                                           =  2 y1/(1 + y0) , 
 
using the formulas for  dθ2  and  dθ3  appearing in the previous section. 
 
The above example can be viewed as a special instance of the formula given in 
Proposition 39.2, since   
 
< y , V >  =  < y , X1 >  =  — y1   and  1  +  < x , y >  =  1  +  y0 . 
 
And just as before, this single verification of the proposition also serves as its 
proof.
