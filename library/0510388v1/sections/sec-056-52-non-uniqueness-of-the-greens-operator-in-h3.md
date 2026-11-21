---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-056-52-non-uniqueness-of-the-greens-operator-in-h3
section_title: "Non-uniqueness of the Green's operator in H3 ."
section_number: 52
pages: 98-100
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
We have been seeking a formula for the vector-valued Green's operator in  H3  of 
the type 
 
        Gr(V)(y)  =  A(V, ϕ2)(y)  +  G(V, ϕ3)(y)    
 
                        =  ∫H3  PyxV(x)  ϕ2(x, y)  dx   +   ∇y∫H3  PyxV(x) ∙ ∇yϕ3(x, y)  dx . 
 
The ambiguity in the choice of  ϕ2(α)  appeared in section 49, and is of the form  
(1/4π) C / (1  +  cosh α) .  So let's set 
 
φ2  =  1 / (1  +  cosh α) , 
 
and think of this as the difference between two competing choices of  ϕ2 .  
We will have 
 
∇y × A(V, φ2)(y)  =  0 , 
 
since the corresponding integrals for the two choices of  ϕ2  both have the 
same curl, namely  — BS(V)(y) . 
 
Let  φ3  denote the difference between the corresponding choices of  ϕ3 .  This 
kernel function satisfies the equation 
 
∆y{A(V, φ2)(y)  +  G(V, φ3)(y)}  =  0 . 
 
We follow the routine of sections 50 and 51 and learn that 
 
∆φ3  =  1/(1 + cosh α) . 
 
We solve this for  φ3  and get 
 
φ3'(α)  =  (sinh α  —  α) / sinh2α , 
 
and then 
 
φ3(α)  =  2α / (e2α
 — 1)   +   2 ln(eα / (eα + 1)) . 
 
 
 
 
 
 
Putting this together, we get an explicit formula for the difference  δGr  between 
two competing vector-valued Green's operators in  H3 , 
 
        δGr(V)(y)  =  A(V, φ2)(y)  +  G(V, φ3)(y) 
 
                          =  ∫H3  PyxV(x)  φ2(x, y)  dx   +   ∇y∫H3  PyxV(x) ∙ ∇yφ3(x, y)  dx 
 
                          =  ∫H3  PyxV(x)  (1 / (1 + cosh α))  dx    
 
                                        +   ∇y∫H3  PyxV(x)  ∙  ((sinh α  —  α) / sinh2α)  ∇yα   dx . 
 
We certainly know that  δGr(V)  is a harmonic vector field, that is, its Laplacian 
∆y δGr(V)(y)  =  0 .  But recall from the construction that the first integral in the 
definition of  δGr(V)  is curl-free.  Since  H3  is simply connected, this integral is 
actually a gradient vector field.  The second integral is visibly a gradient field, so  
δGr(V)  is actually a gradient field.  Since it is harmonic, it is the gradient of some 
harmonic function on  H3 , that is, 
 
δGr(V)(y)  =  ∇y(some harmonic function of  y) . 
 
Further computation reveals that this harmonic function on  H3  is in general not 
constant, and hence the arbitrary choice of the constant  C  in the definition of  ϕ2  
in section 49 does have an effect on  Gr(V) .  As a consequence, the vector-valued 
Green's operator in  H3 ,  even restricted to the form that we are seeking, is not 
unique.
