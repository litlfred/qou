---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-013-11-proof-of-theorem-3-formula-1
section_title: "Proof of Theorem 3, formula (1)."
section_number: 11
pages: 30-32
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
We intend to show that on  S3  in left-translation format, the Green's operator on 
vector fields is given by 
  
 
    Gr(V)(y)  =   ∫S3  Lyx—1 V(x) ϕ0(x, y)  dx 
 
 
 
                        +  2 ∫S3  Lyx—1 V(x) × ∇y ϕ1(x, y)  dx   
 
 
 
                                  +  4 ∇y ∫S3  Lyx—1 V(x) ∙ ∇y ϕ2(x, y)  dx  
 
                               =  A(V, ϕ0))y)  +  2 B(V, ϕ1)(y)  +  4 G(V, ϕ2)(y) , 
 
where 
 
 
 
ϕ0(α)  =  (—1/4π2) (π—α) cot α 
 
 
 
ϕ1(α)  =  (—1/16π2) α (2π—α) 
 
 
 
ϕ2(α)  =  (—1/192π2) (3α(2π—α) + 2α(π—α)(2π—α)cot α) . 
 
Direct computation shows that these three kernel functions are related by 
 
                             ∆                       ∆                      ∆ 
ϕ2  →  ϕ1  —  [ϕ1]  →  ϕ0  —  [ϕ0]  →  δ  —  [δ] , 
 
with average values 
 
[ϕ0]  =  —1/(8π2)     and     [ϕ1]  =  —1/(32π2)  —  1/24 . 
 
 
 
 
 
 
To show that  ∆Gr(V)  =  V , we add up the three terms in  ∆Gr(V)  as follows. 
 
       ∆A(V, ϕ0)  =  A(V, ∆ϕ0)  —  4 A(V, ϕ0)  —   2 B(V, ϕ0) 
 
                          =  A(V, ∆ϕ0)  —  4 A(V, ϕ0)  —   2 B(V, ϕ0 — [ϕ0]) 
 
    2 ∆B(V, ϕ1)  =                        4 A(V, ∆ϕ1)  +  2 B(V, ∆ϕ1)  —  4 G(V, ϕ1) 
 
                          =                        4 A(V, ∆ϕ1)  +  2 B(V, ∆ϕ1)  —  4 G(V, ϕ1 — [ϕ1] ) 
 
    4 ∆G(V, ϕ2)  =                                                                             4 G(V, ∆ϕ2) . 
 
Notice that we take the gradient of the kernel function  ϕ0  in the definition of 
B(V, ϕ0) ,  and so replacing  ϕ0  by  ϕ0 — [ϕ0]  causes no change in value. 
Likewise, we replace  ϕ1  by  ϕ1 — [ϕ1]  in the definition of  G(V, ϕ1)  without 
changing its value. 
 
Now we add up the columns, use the facts that  ∆ϕ1  =  ϕ0 — [ϕ0]  and 
∆ϕ2  =  ϕ1 — [ϕ1] ,  and get 
 
                    ∆Gr(V)  =  ∆A(V, ϕ0)  +  2 ∆B(V, ϕ1)  +  4 ∆G(V, ϕ2) 
 
                                   =  A(V, ∆ϕ0)  —  4 A(V, ϕ0)  +  4 A(V, ∆ϕ1) 
 
                                   =  A(V, δ — [δ])  —  4 A(V, ϕ0)  +  4 A(V, ϕ0 — [ϕ0]) 
 
                                   =  A(V, δ)  —  A(V, [δ])  —  4 A(V, [ϕ0]) . 
 
Note that  [δ]  =  1/2π2 ,  and  [ϕ0]  =  —1/8π2 ,  so the last two terms above cancel, 
and we get 
 
∆Gr(V)  =  A(V, δ)  =  V , 
 
completing the proof of Theorem 3, formula (1).
