---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-024-21-the-second-term-on-the-lhs-of-the-key-lemma
section_title: "The second term on the LHS of the Key Lemma."
section_number: 21
pages: 50-52
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
Now, just as we did for the first term, we want to express the second term 
 
— ∇y {V(x) ∙ ∇x (cos α  ϕ)} 
 
as a linear combination of the orthonormal basis vectors  E1 ,  E2  and  E3  for  TyS3 . 
We keep in mind that  x  =  (1, 0, 0, 0)  and that  V(x)  =  X1  =  (0, 1, 0, 0) . 
 
To begin, 
 
           ∇x (cos α  ϕ)  =  (cos α  ϕ)' ∇x α 
 
                                      =  (cos α  ϕ)'  (—1/sin α) (y1 X1  +  y2 X2  +  y3 X3) . 
 
Then taking the dot product of this with  V(x)  =  X1  yields 
 
                     V(x) ∙ ∇x (cos α  ϕ)  =  (cos α  ϕ)'  (—1/sin α) y1 
 
                                                         =  (— ϕ' cos α / sin α  +  ϕ) y1 . 
 
Thus 
 
— ∇y {V(x) ∙ ∇x (cos α  ϕ)}  =  ∇y {(ϕ' cos α / sin α  —  ϕ)} y1 . 
 
To calculate this, recall that 
 
∇y α  =  (1/sin α) (y1 E1  +  y2 E2  +  y3 E3) , 
 
and note that 
 
            ∇y y1  =  ↑ dy1  =  ↑ {θ1  —  (y1/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3)} 
 
                                         =  E1  —  (y1/(1 + y0)) (y1 E1  +  y2 E2  +  y3 E3) . 
 
 
 
 
 
 
 
We then calculate the second term on the LHS of the Key Lemma: 
 
— ∇y {V(x) ∙ ∇x (cos α  ϕ)} 
 
               =  { (ϕ" cos α/sin2α  —  ϕ'(1/sin α  +  1/sin3α)) y1
2   
 
                                                +  (ϕ' cos α/sin α  —  ϕ) (1  —  y1
2/(1 + y0)) } E1 
 
                    +  { (ϕ" cos α/sin2α  —  ϕ'(1/sin α  +  1/sin3α)) y1y2   
 
                                                        —  (ϕ' cos α/sin α  —  ϕ) y1y2/(1 + y0) } E2 
 
                    +  { (ϕ" cos α/sin2α  —  ϕ'(1/sin α  +  1/sin3α)) y1y3   
 
                                                        —  (ϕ' cos α/sin α  —  ϕ) y1y3/(1 + y0) } E3 . 
  
 
If we combine the two terms on the LHS of the Key Lemma and simplify, we get 
 
     ∇y  ×  {PyxV(x)  ×  ∇y ϕ}  —  ∇y {V(x) ∙ ∇x (cos α  ϕ)} 
 
                                =  {(ϕ"  +  2 ϕ' cos α/sin α  —  ϕ) (1  —  y1
2/(1 + y0)) } E1 
 
                                   +  {(ϕ"  +  2 ϕ' cos α/sin α  —  ϕ) (— y1y2/(1 + y0)) } E2 
 
                                   +  {(ϕ"  +  2 ϕ' cos α/sin α  —  ϕ) (— y1y3/(1 + y0)) } E3 .
