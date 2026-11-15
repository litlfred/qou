---
doc_id: s00453-026-01372-w
doc_title: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence"
section_id: sec-004-21-notions-of-negative-dependence
section_title: "Notions of Negative Dependence"
section_number: 2.1
pages: 5-6
source_pdf: s00453-026-01372-w.pdf
source_sha256: 98b569eff84fb489
toc_source: outline
doc_brief: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence — We study the question of whether submodular functions of random variables satisfying various notions of negative"
---
We begin by deﬁning the notion of negative dependence commonly found in the
literature.
Negative Cylinder Dependence.
A collection of Boolean random variables X1, . . . , Xn is said to be negative cylinder
dependent if for every S ⊆[n],
E

i∈S Xi

≤
i∈S E [Xi]
and
E

i∈S (1 −Xi)

≤
i∈S E [1 −Xi] .
Negative cylinder dependence is the weaker notion considered here. It is known to
imply Chernoff bounds for linear combinations of X1, . . . , Xn but it is insufﬁcient to
show our submodular concentration results.
Negative Association.
A collection of random variables X1, . . . , Xn is said to be negatively associated if for
any I, J ⊂[n], I ∩J = ∅and any pair of non-decreasing functions f : RI →R, g :
RJ →R,
E [ f (X I) g (X J)] ≤E [ f (X I)] E [g (X J)] .
Here and in the following, XS refers to those random variables that are indexed by the
elements in S, XS = {Xi : i ∈S}. Negative association is a signiﬁcant strengthening
of negative cylinder dependence, and has many additional useful closure properties.
This will be one of the focuses of the paper.
Negative Regression.
A collection of random variables X1, . . . , Xn is said to satisfy negative regression,
if for any I, J ⊂[n], I ∩J = ∅, any non-decreasing function f : RI →R and
a ≤b ∈RJ,
E [ f (X I) | X J = a] ≥E [ f (X I) | X J = b] .
Negative regression is a strengthening of negative cylinder dependence, but its rela-
tionship with negative association is not yet well understood. It is known that negative
21
Page 6 of 19
Algorithmica (2026) 88 :21
association doesn’t imply negative regression [22], but the opposite implication is not
known. This will be the other focus of the paper.
Strong Rayleigh.
A collection of random variables X1, . . . , Xn is said to satisfy the strong Rayleigh
property if the generating function
F(z1, . . . , zn) = E[n
j=1 z
X j
j ]
is a real stable polynomial (i.e., it has no root (z1, . . . , zn) ∈Cn with all positive
imaginary components). The strong Rayleigh property is the strongest notion of neg-
ative dependence, and has been shown to imply all other studied negative dependence
deﬁnitions [28]. As a result, all of our results apply here as well.
