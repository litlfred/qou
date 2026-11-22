---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-012-10-the-calculus-of-vector-convolutions-in-s3
section_title: "The calculus of vector convolutions in S3 ."
section_number: 10
pages: 27-30
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
We turn now to the calculus of vector convolutions in  S3 .  Our specific goal is to 
prove Theorem 3, formula (1). 
 
Let  V  be a smooth vector field defined on  S3 .  For any kernel function  ϕ(α) , 
we define 
 
 
 
A(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) ϕ(x, y)  dx 
 
 
 
B(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) × ∇y ϕ(x, y)  dx   
 
                     g(V, ϕ)(y)  =  ∫S3  Lyx—1 V(x) ∙ ∇y ϕ(x, y)  dx 
 
 
 
G(V, ϕ)(y)  =  ∇y g(V, ϕ)(y)  =  ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ(x, y)  dx . 
 
We now continue as in  R3 :  the curl and divergence of the vector fields  A(V, ϕ)  
and  B(V, ϕ)  are given by 
 
LEMMA 3.  
 
∇ × A(V, ϕ)  =  — B(V, ϕ)                          —  2 A(V, ϕ) 
 
∇ ∙ A(V, ϕ)  =  g(V, ϕ) 
 
∇ × B(V, ϕ)  =  A(V, ∆ϕ)  —  G(V, ϕ) 
 
∇ ∙ B(V, ϕ)  =                                            —  2 g(V, ϕ) . 
 
We have displayed these formulas so that the terms which already appeared in the 
corresponding formulas in  R3 ,  given in Lemma 1, are to the left, while those 
which are new in  S3  are to the far right. 
 
Proof.  We give the arguments for the first and last of these formulas, each of 
which looks like the corresponding formula in  R3  with an extra term added, and 
leave the other two formulas to the reader. 
 
We begin with the first formula, 
 
∇y × A(V, ϕ)(y)  =  ∇y ×  ∫S3  Lyx—1 V(x) ϕ(x, y)  dx 
 
                         =  ∫S3  ∇y × {Lyx—1 V(x) ϕ(x, y)}  dx 
 
                         =  ∫S3  (∇y × Lyx—1 V(x)) ϕ(x, y)  —  Lyx—1 V(x) × ∇y ϕ(x, y)  dx . 
 
 
 
 
 
In  R3 ,   ∇y × V(x)  was zero in the first term because we were differentiating with 
respect to  y  a vector field  V(x)  which did not depend on  y . 
 
In  S3 ,  the vector field  Lyx—1 V(x)  does depend on  y ,  and its curl,  ∇y × Lyx—1 V(x) , 
is not zero.  In fact, as we indicated in section 4, the vector field  Lyx—1 V(x)  is 
left-invariant with respect to  y ,  and as such is a curl-eigenfield with eigenvalue  —2 , 
that is,   
 
∇y × Lyx—1 V(x)  =  —2 Lyx—1 V(x) . 
 
This observation lets us continue and complete the calculation: 
 
∇y × A(V, ϕ)(y)  =  ∫S3  [{∇y × Lyx—1 V(x)} ϕ(x, y)  —  Lyx—1 V(x) × ∇y ϕ(x, y)]  dx 
 
                             =  ∫S3  [—2 Lyx—1 V(x) ϕ(x, y)  —  Lyx—1 V(x) × ∇y ϕ(x, y)]  dx 
 
                             =  —2 ∫S3  Lyx—1 V(x) ϕ(x, y)  dx  —  ∫S3  Lyx—1 V(x) × ∇y ϕ(x, y)  dx 
 
                             =  —2 A(V, ϕ)(y)  —  B(V, ϕ)(y) , 
 
as claimed. 
 
As for the last formula, 
 
∇y ∙ B(V, ϕ)(y)  =  ∇y ∙ ∫S3  Lyx—1 V(x) × ∇y ϕ(x, y)  dx   
 
=  ∫S3  ∇y ∙ {Lyx—1 V(x) × ∇y ϕ(x, y)}  dx   
 
=  ∫S3  [{∇y × Lyx—1 V(x)} ∙ ∇y ϕ(x, y)  dx  —  Lyx—1 V(x) ∙ {∇y × ∇y ϕ(x, y)}]  dx 
 
=  ∫S3  —2 Lyx—1 V(x) ∙ ∇y ϕ(x, y)  dx  
 
=  —2 g(V, ϕ)(y) , 
 
as claimed, since  ∇y × ∇y ϕ(x, y)  =  0 . 
 
 
 
 
 
Proof of Proposition 2. 
 
∆A(V, ϕ)  =  — ∇ × ∇ × A(V, ϕ)  +  ∇(∇ ∙ A(V, ϕ)) 
 
                            =  — ∇ × (— B(V, ϕ)  —  2 A(V, ϕ))  +  ∇g(V, ϕ) 
 
                            =  ∇ × B(V, ϕ)  +  2 ∇ × A(V, ϕ)  +  G(V, ϕ) 
 
                            =  A(V, ∆ϕ)  —  G(V, ϕ)  —  2 B(V, ϕ)  —  4 A(V, ϕ)  +  G(V, ϕ) 
 
                            =  A(V, ∆ϕ)  —  4 A(V, ϕ)  —  2 B(V, ϕ) , 
 
as claimed. 
 
∆B(V, ϕ)  =  — ∇ × ∇ × B(V, ϕ)  +  ∇(∇ ∙ B(V, ϕ)) 
 
                            =  — ∇ × (A(V, ∆ϕ)  —  G(V, ϕ))  +  ∇(—2 g(V, ϕ)) 
 
                            =  — ∇ × A(V, ∆ϕ)  — 2 G(V, ϕ) 
 
                            =  B(V, ∆ϕ)  +  2 A(V, ∆ϕ)  —  2 G(V, ϕ) , 
 
as claimed. 
 
            ∆g(V, ϕ)  =  ∇ ∙ ∇g(V, ϕ) 
 
                             =  ∇ ∙ G(V, ϕ) 
 
                             =  ∇ ∙ {A(V, ∆ϕ)  —  ∇ × B(V, ϕ)} 
 
                             =  g(V, ∆ϕ) , 
 
using the formulas for  ∇ × B(V, ϕ)  and for  ∇ ∙ A(V, ∆ϕ)  obtained in Lemma 3. 
 
Finally, 
 
            ∆G(V, ϕ)  =  ∆ ∇g(V, ϕ)   
 
                              =  ∇ ∆g(V, ϕ) 
 
                              =  ∇ g(V, ∆ϕ) 
 
                              =  G(V, ∆ϕ) , 
 
completing the proof of Proposition 2.
