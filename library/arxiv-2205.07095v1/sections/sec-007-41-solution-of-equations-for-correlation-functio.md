---
doc_id: arxiv-2205.07095v1
doc_title: "Virial Expansions for Correlation Functions in Canonical Ensemble A. L. Rebenko"
section_id: sec-007-41-solution-of-equations-for-correlation-functio
section_title: "Solution of equations for correlation functions."
section_number: 4.1
pages: 8-10
source_pdf: 2205.07095v1.pdf
source_sha256: 2ec6916399150e2d
doc_brief: "Virial Expansions for Correlation Functions in Canonical Ensemble A. L. Rebenko — The inﬁnite set of coupled integral nonlinear equations for correlation func- tions in the case of classical"
---
Rewrite the equation (3.29), (3.31) as follows:
~Q(ρj)ρj(η) = ̺e−βW (x1;η(ˆx1))j(x1)
∫
Γ 0
K(x1;ξ)ρj(η(ˆx1) ∪ξ)λσ(dξ), (4.32)
~Q(ρj) =
∫
Γ 0
K(x1;ξ)ρj(ξ)λσ(dξ), (4.33)
where, following [12], a continuous positive function j : Rd → R+ is intro-
duced and ρ(η) becomes functional such as ρ(η) = ρj(η)|j=1.
8
We will look for the solution of these equations in the form:
ρj(η) = e(j;η)
∫
Γ 0
T (η|γ)e(j;γ)λσ(dγ), (4.34)
where e(j;η) is given by (2.4).
The idea of ﬁnding a solution is to consider the left side of th e equation
(4.32) as the product of two generating functionals (see (2. 5)) and compare
it with the right part, which is also written in the form of a ge nerating
functional of the form (2.3). So, substituting in (4.33) the corresponding
expression for ρj(ξ) we have:
~Q(ρj) =
∫
Γ 0
∫
Γ 0
e(j;ξ ∪γ)K(x1;ξ)T (ξ|γ)λσ(dγ)λσ(dξ). (4.35)
Apply to the integral on the right side of the (4.35) lemma 2.1 with
G(ξ ∪γ) = e(j;ξ ∪γ) and H(ξ;γ) = K(x1;ξ)T (ξ|γ). (4.36)
Then
~Q(ρj) = ~Fψ1(j) =
∫
Γ 0
e(j;γ)ψ1(γ)λσ(dγ), (4.37)
with
ψ1(γ) =
∑
ξ⊆γ
K(x1;ξ)T (ξ|γ \ξ). (4.38)
Write down (4.34) in the form of generating functional:
ρj(η) = ~Fψ2(j) =
∫
Γ 0
e(j;γ)ψ2(γ)λσ(dγ), (4.39)
with
ψ2(γ) = e(j;η)T (η|γ). (4.40)
Left hand side (4.32) is:
~Q(ρj)ρj(η) = ~Fψ1(j) ~Fψ2(j) = ~Fψ1∗ψ2(j) =
∫
Γ 0
e(j;γ)(ψ1 ∗ψ2)(γ)λσ(dγ),
(4.41)
where
(ψ1 ∗ψ2)(γ) =
∑
ξ⊆γ
ψ1(ξ)ψ2(γ \ξ) =
∑
ξ⊆γ
ψ2(γ \ξ)ψ1(ξ) = (4.42)
=e(j;η)
∑
ξ⊆γ
T (η|γ \ξ)
∑
ζ⊆ξ
K(x1;ζ)T (ζ|ξ \ζ)
9
Right hand side (4.32) after substitution of ρj(η(ˆx1) ∪ξ) in the form
(4.34) will look as:
̺e−βW (x1;η(ˆx1))e(j;η)
∫
Γ 0
∫
Γ 0
e(j;ξ ∪γ)K(x1;ξ)T (η(ˆx1) ∪ξ|γ)λσ(dγ)λσ(dξ).
(4.43)
Let us use lemma 2.1 again with
G(ξ ∪γ) = e(j;ξ ∪γ) and H(ξ;γ) = K(x1;ξ)T (η(ˆx1) ∪ξ|γ). (4.44)
Then right hand side of (4.32) will be as
̺e−βW (x1;η(ˆx1))e(j;η)
∫
Γ 0
e(j;γ)
∑
ξ⊆γ
K(x1;ξ)T (η(ˆx1) ∪ξ|γ \ξ)λσ(dγ). (4.45)
We equate the functions near e(j;γ) under the integrals of the expressions
(4.41) and (4.45) and, reducing the multiplier e(j;η) we get the relation:
∑
ξ⊆γ
T (η|γ \ξ)
∑
ζ⊆ξ
K(x1;ζ)T (ζ|ξ \ζ) = (4.46)
= ̺e−βW (x1;η(ˆx1)) ∑
ξ⊆γ
K(x1;ξ)T (η(ˆx1) ∪ξ|γ \ξ).
Select the term with ξ = ∅ in the left side of this relation and take into
account that T (∅|∅) = 1 and T (∅|γ) = 0, if γ ⁄= ∅), we obtain the following
nonlinear recurrent relation:
T (η|γ) = ̺e−βW (x1;η(ˆx1)) ∑
ξ⊆γ
K(x1;ξ)T (η(ˆx1) ∪ξ|γ \ξ)−
−
∑
∅⁄=ξ⊆γ
T (η|γ \ξ)
∑
∅⁄=ζ⊆ξ
K(x1;ζ)T (ζ|ξ \ζ). (4.47)
Initial conditions:
T (∅|∅) = 1 , T (∅|γ) = 0 , if γ ⁄= ∅, (4.48)
T ({η|γ) = 0 , if η ∩γ ⁄= ∅. (4.49)
