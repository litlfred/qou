---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-017-5-graces-theorem
section_title: "Grace's theorem"
section_number: 5
pages: 16-17
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
We now prove the multivariate homogeneous Grace’s theorem for some specific projectively
convex regions and then derive a few important corollaries. These corollaries will be almost

D Springer
A representation theoretic explanation...
1375
immediate once Grace’s theorem has been proven, and yet will quickly yield stronger results
regarding linear operators in the next section.
In the usual proof of the classical univariate Grace’s theorem, reference to linear factors of
f ∈Cn[x]isnecessary.ThismakesgeneralizationtoCλ[x1, . . . , xm]difﬁcult,asmultivariate
polynomials do not necessarily have any linear factors. In our new proof, we are able avoid
reference to linear terms by using particular features of the D map. This means that our proof
method works for any λ.
Theorem 5.1 Fix λ ∈Nm
0 and p, q ∈V (λ). Also, denote C := H+∪R+ and 
C := H−∪R−,
where the closures are considered to be in CP1. If p is Cm-stable and q is 
Cm-stable, then
Dλ(p ⊗q)̸ = 0.
Proof We prove the theorem by induction on degree. For λ ≡0, the result is obvious. For
|λ| ≥1, we can assume WLOG that λ1 ≥1 by permuting the variables. Deﬁne δ1 :=
(1, 0, 0, . . . , 0) ∈Nm
0 .
Since C and 
C are projectively convex, Corollary 4.7 implies (a∂x1 + b∂y1)p is Cm-
stable for all (a : b) ∈C and (c∂x1 + d∂y1)q is 
Cm-stable for all (c : d) ∈
C. To obtain
a contradiction, we assume Dλ(p ⊗q) = 0. For α ∈H+ ∪R+ ⊂C (equivalently, −α ∈
H−∪R−⊂
C), this gives:
Dλ−δ1
(α∂x1 + ∂y1)p ⊗(α∂x1 −∂y1)q
	
= α2Dλ−δ1(∂x1 p ⊗∂x1q) −Dλ−δ1(∂y1 p ⊗∂y1q)
−αDλ(p ⊗q) = α2Dλ−δ1(∂x1 p ⊗∂x1q) −Dλ−δ1(∂y1 p ⊗∂y1q)
By induction and the stability properties discussed above, we have Dλ−δ1(∂x1 p ⊗∂x1q)̸ = 0,
Dλ−δ1(∂y1 p ⊗∂y1q)̸ = 0, and Dλ−δ1
(α∂x1 + ∂y1)p ⊗(α∂x1 −∂y1)q
	̸
= 0. This implies:
α2Dλ−δ1(∂x1 p ⊗∂x1q) −Dλ−δ1(∂y1 p ⊗∂y1q)̸ = 0 ⇒α2̸ = Dλ−δ1(∂y1 p ⊗∂y1q)
Dλ−δ1(∂x1 p ⊗∂x1q) ∈C\{0}
However, we can pick α ∈H+ ∪R+ such that α2 is any value of C\{0} we want, including
that of
Dλ−δ1(∂y1 p⊗∂y1q)
Dλ−δ1(∂x1 p⊗∂x1q). This contradiction gives the result.
⊓⊔
