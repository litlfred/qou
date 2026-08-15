---
doc_id: 0510388v1
doc_title: "ELECTRODYNAMICS and the GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE"
section_id: sec-002-3-in-left-translation-format
section_title: "IN LEFT-TRANSLATION FORMAT"
section_number: 3
pages: 22-34
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
doc_brief: "ELECTRODYNAMICS and the GAUSS LINKING INTEGRAL on the 3-SPHERE and in HYPERBOLIC 3-SPACE — 10 sections: Magnetic fields in R; Vector-valued Green’s operators in; IN LEFT-TRANSLATION FORMAT"
---
8.  Proof scheme for Theorem 3, formula (1). 
 
When working on  S3  in left-translation format, our first order of business will 
be to derive formula (1) of Theorem 3 for the vector-valued Green’s operator. 
 
It is natural to hope, by analogy with  R3 ,  that 
 
A(V, ϕ0)(y)  =  ∫S3  Lyx—1 V(x) ϕ0(x, y)  dx 
 
will be the Green’s operator on  S
3  when  ϕ0  is the fundamental solution of the 
scalar Laplacian.   
 
It doesn’t turn out this way, but the fundamental solution of the Laplacian is not 
the only possible kernel function, and  A(V, ϕ)  is not the only way of convolving  
a vector field with a kernel to get another vector field.   
 
Consider the convolutions 
 
  A(V, ϕ)(y)  =  
∫S3  Lyx—1 V(x) ϕ(x, y)  dx 
 
  B ( V ,  ϕ)(y)  =  ∫S3  Lyx—1 V(x) × ∇y ϕ(x, y)  dx   
 
  G(V, ϕ)(y)  =  ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ(x, y)  dx . 
 
 
 
 23 
 
 
 
 
 
 
We will develop a "calculus of vector convolutions", in which we compute formulas 
for curls, divergences and Laplacians of convolutions, first in  R
3  to serve as a model, 
and then on  S3  in left-translation format, and in particular obtain 
 
 
PROPOSITION 2.  On  S
3 ,  the vector Laplacian has the following effect on 
convolutions of types  A ,  B  and  G : 
 
        ∆∆∆∆A(V, ϕϕϕϕ)  =  A(V, ∆∆∆∆ϕϕϕϕ)       —  4 A(V, ϕϕϕϕ)     —  2 B(V, ϕϕϕϕ) 
 
        ∆∆∆∆B(V, ϕϕϕϕ)  =  B(V, ∆∆∆∆ϕϕϕϕ)        +  2 A(V, ∆∆∆∆ϕϕϕϕ)  —  2 G(V, ϕϕϕϕ) 
 
        ∆∆∆∆G(V, ϕϕϕϕ)  =  G(V, ∆∆∆∆ϕϕϕϕ) . 
 
 
The large spaces after the first terms on the right hand sides of the  A  and  B  lines 
serve as a reminder that in Euclidean space  R
3 ,  only those first terms appear. 
In particular, in  R3  we have  ∆A(V, ϕ)  =  A(V, ∆ϕ) .  So naturally, when we 
choose  ϕ  =  ϕ0  to be a fundamental solution of the scalar Laplacian in  R3 ,   
we get  ∆A(V, ϕ0)  =  A(V, ∆ϕ0)  =  A(V, δ)  =  V ,  which tells us that   
A(V, ϕ0)  =  Gr(V)  there. 
 
Once we have Proposition 2 in hand, we will then get formula (1) of Theorem 3 
for the Green’s operator on  S
3  by adding one copy of line A to two copies of line B 
and four copies of line G,  each with a different choice of kernel function  ϕ . 
 
 
 24 
 
                      
 
 
 
 
9. The calculus of vector convolutions in  R3 . 
 
Let  α   =  |x — y|  denote the distance between the points  x  and  y  in  R3 ,  and 
let  ϕ(α )  be some unspecified function of  α  .  As usual, we’ll write  ϕ(x, y)  in 
place of  ϕ(α (x, y))  for simplicity. 
 
Let  V  be a smooth vector field defined on  R3  and having compact support. 
Keeping the function  ϕ  unspecified, we define vector fields  A(V, ϕ)  and   
B(V, ϕ) ,  a scalar function  g(V, ϕ)  and another vector field  G(V, ϕ)  as follows. 
 
 A(V, ϕ)(y)  =  ∫
R3  V(x) ϕ(x, y)  dx 
 
 B(V, ϕ)(y)  =  ∫R3  V(x) × ∇y ϕ(x, y)  dx 
 
 g(V, ϕ)(y)  =  ∫R3  V(x) ∙ ∇y ϕ(x, y)  dx 
 
 G(V, ϕ)(y)  =  ∇
y g(V, ϕ)(y)  =  ∇y ∫R3  V(x) ∙ ∇y ϕ(x, y)  dx . 
 
If we use the fundamental solution  ϕ0(α )  =  —1/(4πα )  of the scalar Laplacian as  
the kernel in the above convolutions, then  A(V, ϕ0)  gives the Green’s operator, and 
if we think of  V  as a current flow, then  B(V, ϕ0)  is the resulting magnetic field,   
— A(V, ϕ0)  is its vector potential,  and  — G(V, ϕ0)  is the rate of change  ∂E/∂t  of 
the electric field, caused by the accumulation and dissipation of charge by the 
current flow  V . 
 
 25 
 
 
 
The curl and divergence of the vector fields  A(V, ϕ)  and  B(V, ϕ)  are given by 
 
LEMMA 1.     ∇ × A(V, ϕ)  =  — B(V, ϕ)            ∇ ∙ A(V, ϕ)  =  g(V, ϕ) 
 
      ∇ × B(V, ϕ)  =  A(V, ∆ϕ )  —  G(V, ϕ)       ∇ ∙ B(V, ϕ)  =  0 . 
 
Proof.  The proofs are exercises in differentiating under the integral sign and then 
using the various Leibniz rules from vector calculus.  We will show the brief 
arguments for the first and last of the four formulas above, since these two will 
change when we move to the 3-sphere.  The other two formulas, whose proofs we 
leave to the reader, are the same in  R
3  and  S3 . 
 
To begin with the first formula, 
 
          ∇
y × A(V, ϕ)(y)  =  ∫R3  ∇y × {V(x) ϕ(x, y)}  dx 
 
                                          =  ∫
R3  (∇y × V(x)) ϕ(x, y)  —  V(x) × ∇y ϕ(x, y)  dx 
 
                                          =  — ∫R3  V(x) × ∇y ϕ(x, y)  dx 
 
                                          =  — B(V, ϕ)(y) , 
 
as claimed,  since  ∇
y × V(x)  =  0 .  When we move to  S3 ,  the corresponding term 
will not be zero. 
 
As for the last formula, 
 
∇
y ∙ B(V, ϕ)(y)  =  ∫R3  ∇y ∙ {V(x) × ∇y ϕ(x, y)}  dx 
 
                            =  ∫R3  (∇y × V(x)) ∙ ∇y ϕ(x, y)  —  V(x) ∙ (∇y × ∇y ϕ(x, y))  dx 
 
                            =  0 , 
 
as claimed, because   ∇
y × V(x)  =  0   and   ∇y × ∇y ϕ(x, y)  =  0 .  Again, when  
we move to  S3 ,  the expression corresponding to  ∇y × V(x)  will not be zero. 
 
 26 
 
 
 
Comment. 
 
If we use the fundamental solution  ϕ0  of the Laplacian as our kernel, think of  V  
as a current flow and  B(V, ϕ0)  as its magnetic field, we get 
 
                       ∇ × B(V, ϕ0)  =  A(V, ∆ϕ 0)  —  G(V, ϕ0) , 
 
which is Maxwell’s equation, 
 
                               ∇ × B  =  V  +  ∂E/∂t . 
 
 
Now we turn to the Laplacians of our convolutions. 
 
LEMMA 2.         ∆A(V, ϕ)  =  A(V, ∆ϕ )  ∆B(V, ϕ)  =  B(V, ∆ϕ ) 
 
                           ∆g(V, ϕ)  =  g(V, ∆ϕ )  ∆G(V, ϕ)  =  G(V, ∆ϕ ) . 
 
Proof.   
 
The arguments are straightforward, using the formula for the vector Laplacian, 
the information from Lemma 1, and the fact that Laplacian and gradient commute. 
We write it out for the first formula, and leave the other three to the reader. 
 
                   ∆A(V, ϕ)  =  — ∇ × ∇ × A(V, ϕ)  +  ∇
(∇ ∙ A(V, ϕ)) 
 
                                      =  — ∇ × (— B(V, ϕ))  +  ∇g(V, ϕ) 
 
                                      =  A(V, ∆ϕ )  —  G(V, ϕ)  +  G(V, ϕ) 
 
                                      =  A(V, ∆ϕ ) . 
 
 
 27 
 
10. The calculus of vector convolutions in  S3 . 
 
We turn now to the calculus of vector convolutions in  S3 .  Our specific goal is to 
prove Theorem 3, formula (1). 
 
Let  V  be a smooth vector field defined on  S3 .  For any kernel function  ϕ(α ) , 
we define 
 
  A(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) ϕ(x, y)  dx 
 
  B ( V ,  ϕ)(y)  =  ∫S3  Lyx—1 V(x) × ∇y ϕ(x, y)  dx   
 
                     g(V, ϕ)(y)  =  
∫S3  Lyx—1 V(x) ∙ ∇y ϕ(x, y)  dx 
 
  G(V, ϕ)(y)  =  ∇y g(V, ϕ)(y)  =  ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ(x, y)  dx . 
 
We now continue as in  R3 :  the curl and divergence of the vector fields  A(V, ϕ)  
and  B(V, ϕ)  are given by 
 
LEMMA 3.  
 
∇ × A(V, ϕ)  =  — B(V, ϕ)                          —  2 A(V, ϕ) 
 
∇ ∙ A(V, ϕ)  =  g(V, ϕ) 
 
∇ × B(V, ϕ)  =  A(V, ∆ϕ )  —  G(V, ϕ) 
 
∇ ∙ B(V, ϕ)  =                                            —  2 g(V, ϕ) . 
 
We have displayed these formulas so that the terms which already appeared in the 
corresponding formulas in  R3 ,  given in Lemma 1, are to the left, while those 
which are new in  S3  are to the far right. 
 
Proof.  We give the arguments for the first and last of these formulas, each of 
which looks like the corresponding formula in  R3  with an extra term added, and 
leave the other two formulas to the reader. 
 
We begin with the first formula, 
 
∇
y × A(V, ϕ)(y)  =  ∇y ×  ∫S3  Lyx—1 V(x) ϕ(x, y)  dx 
 
                         =  ∫S3  ∇y × {Lyx—1 V(x) ϕ(x, y)}  dx 
 
                         =  ∫S3  (∇y × Lyx—1 V(x)) ϕ(x, y)  —  Lyx—1 V(x) × ∇y ϕ(x, y)  dx . 
 
 28 
 
 
 
In  R3 ,   ∇y × V(x)  was zero in the first term because we were differentiating with 
respect to  y  a vector field  V(x)  which did not depend on  y . 
 
In  S3 ,  the vector field  Lyx—1 V(x)  does depend on  y ,  and its curl,  ∇y × Lyx—1 V(x) , 
is not zero.  In fact, as we indicated in section 4, the vector field  Lyx—1 V(x)  is 
left-invariant with respect to  y ,  and as such is a curl-eigenfield with eigenvalue  —2 , 
that is,   
 
∇
y × Lyx—1 V(x)  =  —2 Lyx—1 V(x) . 
 
This observation lets us continue and complete the calculation: 
 
∇
y × A(V, ϕ)(y)  =  ∫S3  [{∇y × Lyx—1 V(x)} ϕ(x, y)  —  Lyx—1 V(x) × ∇y ϕ(x, y)]  dx 
 
                             =  ∫S3  [—2 Lyx—1 V(x) ϕ(x, y)  —  Lyx—1 V(x) × ∇y ϕ(x, y)]  dx 
 
                             =  —2 
∫S3  Lyx—1 V(x) ϕ(x, y)  dx  —  ∫S3  Lyx—1 V(x) × ∇y ϕ(x, y)  dx 
 
                             =  —2 A(V, ϕ)(y)  —  B(V, ϕ)(y) , 
 
as claimed. 
 
As for the last formula, 
 
∇
y ∙ B(V, ϕ)(y)  =  ∇y ∙ ∫S3  Lyx—1 V(x) × ∇y ϕ(x, y)  dx   
 
=  ∫S3  ∇y ∙ {Lyx—1 V(x) × ∇y ϕ(x, y)}  dx   
 
=  
∫S3  [{∇y × Lyx—1 V(x)} ∙ ∇y ϕ(x, y)  dx  —  Lyx—1 V(x) ∙ {∇y × ∇y ϕ(x, y)}]  dx 
 
=  ∫S3  —2 Lyx—1 V(x) ∙ ∇y ϕ(x, y)  dx  
 
=  —2 g(V, ϕ)(y) , 
 
as claimed, since  ∇
y × ∇y ϕ(x, y)  =  0 . 
 
 
 29 
 
 
Proof of Proposition 2. 
 
∆A(V, ϕ)  =  — ∇ × ∇ × A(V, ϕ)  +  ∇(∇ ∙ A(V, ϕ)) 
 
                            =  — ∇ × (— B(V, ϕ)  —  2 A(V, ϕ))  +  ∇g(V, ϕ) 
 
                            =  ∇ × B(V, ϕ)  +  2 ∇ × A(V, ϕ)  +  G(V, ϕ) 
 
                            =  A(V, ∆ϕ )  —  G(V, ϕ)  —  2 B(V, ϕ)  —  4 A(V, ϕ)  +  G(V, ϕ) 
 
                            =  A(V, ∆ϕ )  —  4 A(V, ϕ)  —  2 B(V, ϕ) , 
 
as claimed. 
 
∆B(V, ϕ)  =  — ∇ × ∇ × B(V, ϕ)  +  ∇(∇ ∙ B(V, ϕ)) 
 
                            =  — ∇ × 
(A(V, ∆ϕ )  —  G(V, ϕ))  +  ∇(—2 g(V, ϕ)) 
 
                            =  — ∇ × A(V, ∆ϕ )  — 2 G(V, ϕ) 
 
                            =  B(V, ∆ϕ )  +  2 A(V, ∆ϕ )  —  2 G(V, ϕ) , 
 
as claimed. 
 
            ∆g(V, ϕ)  =  ∇ ∙ ∇g(V, ϕ) 
 
                             =  ∇ ∙ G(V, ϕ) 
 
                             =  ∇ ∙ {A(V, ∆ϕ )  —  ∇ × B(V, ϕ)} 
 
                             =  g(V, ∆ϕ ) , 
 
using the formulas for  ∇ × B(V, ϕ)  and for  ∇ ∙ A(V, ∆ϕ )  obtained in Lemma 3. 
 
Finally, 
 
            ∆G(V, ϕ)  =  ∆ ∇g(V, ϕ)   
 
                              =  ∇ ∆g(V, ϕ) 
 
                              =  ∇ g(V, ∆ϕ ) 
 
                              =  G(V, ∆ϕ ) , 
 
completing the proof of Proposition 2. 
 
 30 
 
 
 
 
 
11. Proof of Theorem 3, formula (1).
 
 
We intend to show that on  S
3  in left-translation format, the Green’s operator on 
vector fields is given by 
  
     Gr(V)(y)  =   ∫S3  Lyx—1 V(x) ϕ0(x, y)  dx 
 
                          +  2 ∫S3  Lyx—1 V(x) × ∇y ϕ1(x, y)  dx   
 
                                    +  4 ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ2(x, y)  dx  
 
                               =  A(V, ϕ
0))y)  +  2 B(V, ϕ1)(y)  +  4 G(V, ϕ2)(y) , 
 
where 
 
  ϕ
0(α )  =  (—1/4π2) (π—α ) cot α  
 
  ϕ
1(α )  =  (—1/16π2) α  (2π—α ) 
 
  ϕ 2(α )  =  (—1/192π2) (3α (2π—α ) + 2α (π—α )(2π—α )cot α ) . 
 
Direct computation shows that these three kernel functions are related by 
 
                             
∆                       ∆                      ∆ ϕ2  →  ϕ 1  —  [ϕ1]  →  ϕ 0  —  [ϕ0]  →   δ  —  [δ] , 
 
with average values 
 
[ϕ0]  =  —1/(8π2)     and     [ϕ1]  =  —1/(32π2)  —  1/24 . 
 
 31 
 
 
 
 
To show that  ∆Gr(V)  =  V , we add up the three terms in  ∆Gr(V)  as follows. 
 
       ∆A(V, ϕ
0)  =  A(V, ∆ϕ 0)  —  4 A(V, ϕ0)  —   2 B(V, ϕ0) 
 
                          =  A(V, ∆ϕ 0)  —  4 A(V, ϕ0)  —   2 B(V, ϕ0 — [ϕ0]) 
 
    2 ∆B(V, ϕ
1)  =                        4 A(V, ∆ϕ 1)  +  2 B(V, ∆ϕ 1)  —  4 G(V, ϕ1) 
 
                          =                        4 A(V, ∆ϕ 1)  +  2 B(V, ∆ϕ 1)  —  4 G(V, ϕ1 — [ϕ1] ) 
 
    4 ∆G(V, ϕ2)  =                                                                             4 G(V, ∆ϕ 2) . 
 
Notice that we take the gradient of the kernel function  ϕ
0  in the definition of 
B(V, ϕ0) ,  and so replacing  ϕ0  by  ϕ0 — [ϕ0]  causes no change in value. 
Likewise, we replace  ϕ1  by  ϕ1 — [ϕ1]  in the definition of  G(V, ϕ1)  without 
changing its value. 
 
Now we add up the columns, use the facts that  ∆ϕ 1  =  ϕ0 — [ϕ0]  and 
∆ϕ 2  =  ϕ1 — [ϕ1] ,  and get 
 
                    ∆Gr(V)  =  ∆A(V, ϕ0)  +  2 ∆B(V, ϕ1)  +  4 ∆G(V, ϕ2) 
 
                                   =  A(V, ∆ϕ 0)  —  4 A(V, ϕ0)  +  4 A(V, ∆ϕ 1) 
 
                                   =  A(V, δ — [δ])  —  4 A(V, ϕ
0)  +  4 A(V, ϕ0 — [ϕ0]) 
 
                                   =  A(V, δ)  —  A(V, [δ])  —  4 A(V, [ϕ0]) . 
 
Note that  [δ]  =  1/2π2 ,  and  [ϕ0]  =  —1/8π2 ,  so the last two terms above cancel, 
and we get 
 
∆Gr(V)  =  A(V, δ)  =  V , 
 
completing the proof of Theorem 3, formula (1). 
 
 
 32 
 
 
 
 
12. Proof of Theorem 2, formula (1).
 
 
Let  V  be a smooth vector field on  S3 .  Thinking of  V  as a steady current flow, 
we define the corresponding magnetic field  BS(V)  by the formula 
 
BS(V)  =  — ∇ × Gr(V) . 
 
It is easy to check that  BS(V)  satisfies the two properties required of it in 
section 4, as follows. 
 
(1)  ∇ ∙ BS(V)  =  0  because the divergence of a curl is always zero. 
 
(2)  To get Maxwell’s equation, we compute: 
 
              ∇ × BS(V)(y)  =  — ∇ × ∇ × Gr(V)(y) 
 
                                           =  ∆Gr(V)(y)  —  ∇(∇ ∙ Gr(V)(y) 
 
                                           =  V(y)  —  ∇(Gr(∇ ∙ V)(y) 
 
                                           =  V(y)  —  ∇
y ∫S3  (∇x ∙ V(x))  ϕ0(x, y)  dx  
 
                                           =  V(y)  +  ∇y ∫S3  V(x) ∙ ∇x ϕ0(x, y)  dx . 
 
where  ϕ
0  is the fundamental solution of the scalar Laplacian on  S3 .  Note that  
we used the fact, mentioned in section 6, that the Green’s operator on  S3  
commutes with divergence. 
 
 33 
 
 
 
 
 
 
The explicit expression for  BS(V)  given in formula (1) of Theorem 2 comes 
from the explicit formula for  Gr(V)  in left-translation format, given in Theorem 3, 
formula (1), together with the curl formulas given in Lemma 3, as follows. 
 
BS(V)  =  — ∇ × Gr(V)   
 
                       =  — ∇ × A(V, ϕ
0)  —  2 ∇ × B(V, ϕ1)  —  4 ∇ × G(V, ϕ2) 
 
                       =  B(V, ϕ0)  +  2 A(V, ϕ0)  —  2 A(V, ∆ϕ 1)  +  2 G(V, ϕ1) 
 
                       =  B(V, ϕ
0)  +  2 A(V, ϕ0)  —  2 A(V, ϕ0 — [ϕ0])  +  2 G(V, ϕ1) 
 
                       =  B(V, ϕ0)  +  2 A(V, [ϕ0])  +  2 G(V, ϕ1) 
 
                       =  B(V, ϕ0)  — (1/4π2) A(V, 1)  +  2 G(V, ϕ1) 
 
                       =  ∫
S3  Lyx—1 V(x) × ∇y ϕ0(x, y)  dx    
 
     —  1/(4π2) ∫S3  Lyx—1 V(x)  dx 
 
          +  2 ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ1(x, y)  dx , 
 
as claimed.
 
 
 
 34
