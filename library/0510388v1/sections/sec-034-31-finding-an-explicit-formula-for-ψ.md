---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-034-31-finding-an-explicit-formula-for-ψ
section_title: "Finding an explicit formula for Ψ ."
section_number: 31
pages: 69-71
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
The core issue is to solve the equation 
 
∆F(α)  =  (π — α)2 / (1  +  cos α) , 
 
after which we will have 
 
Ψ  =  (1/8π2) F  +  an appropriate function whose Laplacian is constant. 
 
Note that 
 
∆F  =  F"  + 2 F' cot α  =  (1/sin2α) (sin2α F ')' , 
 
which tells us that  sin2α  is an integrating factor for our equation.   
 
Thus we must solve 
 
(sin2α F ')'  =  (π — α)2 sin2α / (1  +  cos α)  =  (π — α)2 (1  —  cos α) . 
 
This integrates to 
 
sin2α F '  =  —(π — α)3/3  —  (π — α)2 sin α  +  2(π — α) cos α  +  2 sin α . 
 
Notice that the right hand side vanishes at  α  =  π ,  so we do not add a constant 
of integration.  Dividing through by  sin2α ,  we get 
 
F '  =  —(π — α)3 / 3 sin2α  —  (π — α)2 / sin α  +  (2(π — α) cos α  +  2 sin α) / sin2α . 
 
 
 
 
 
 
The right-hand half of this expression,  
 
(2(π — α) cos α  +  2 sin α) / sin2α , 
 
blows up as  α  →  0 ,  but approaches  0  as  α  →  π ,  and integrates to 
 
—2 (π — α) / sin α . 
 
The left-hand half of this expression, 
 
ω(α)  =  —(π — α)3 / 3 sin2α  —  (π — α)2 / sin α , 
 
blows up as  α  →  0 ,  but approaches  0  as  α  →  π . 
 
As mentioned earlier, the integral of  ω(α)  is a non-elementary function involving 
polylogarithms, so for momentary convenience we define 
 
Ω(α)  =  — ∫α
π  ω(α)  dα . 
 
Thus  Ω'(α)  =  ω(α)   and  Ω(π)  =  0 . 
 
Then our equation for  F ' , 
 
F '  =  —(π — α)3 / 3 sin2α  —  (π — α)2 / sin α  +  (2(π — α) cos α  +  2 sin α) / sin2α . 
 
      =  ω(α)  +  (2(π — α) cos α  +  2 sin α) / sin2α , 
 
integrates to 
 
F(α)  =  Ω(α)  —  2 (π — α) / sin α . 
 
This function  F(α)  satisfies the equation 
 
∆F(α)  =  (π — α)2 / (1  +  cos α) . 
 
 
 
 
 
 
Since the function   G(α)  =  ½ (π — α) cot α  has Laplacian  1  and no singularity  
at  α = π ,  we conclude that the function 
 
        Ψ(α)  =  (1/8π2) F(α)  —  (—1/2π2  +  1/12) G(α) 
 
                  =  (1/8π2) (Ω(α)  —  2 (π — α) / sin α)  +  (1/4π2  —  1/24) (π — α) cot α 
 
satisfies the equation 
 
∆Ψ  =  ψ  —  [ψ] , 
 
and has no singularity at  α  =  π ,  as desired.
