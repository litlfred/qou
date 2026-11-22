---
doc_id: s00453-026-01372-w
doc_title: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence"
section_id: sec-005-22-submodular-functions
section_title: "Submodular Functions"
section_number: 2.2
pages: 6-7
source_pdf: s00453-026-01372-w.pdf
source_sha256: 98b569eff84fb489
toc_source: outline
doc_brief: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence — We study the question of whether submodular functions of random variables satisfying various notions of negative"
---
We also give a quick review of the basics of submodular functions.
Submodular Functions.
We say that a function f : {0, 1}n →R is submodular if
f (X1, . . . , Xi−1, 1, Xi+1, . . . Xn) −f (X1, . . . , Xi−1, 0, Xi+1, . . . Xn)
is a non-increasing function of X1, . . . , Xi−1, Xi+1, . . . , Xn for each i ∈[n]. When
viewing the binary input of f as the indicator vector for a set, this is equivalent to the
more common deﬁnition that f is submodular if for any X, Y ⊆[n] with X ⊆Y and
any x /∈Y, we have
f (X ∪{x}) −f (X) ≥f (Y ∪{x}) −f (Y).
Supermodular Functions.
We say that a function g : {0, 1}n →R is supermodular if
g(X1, . . . , Xi−1, 1, Xi+1, . . . Xn) −g(X1, . . . , Xi−1, 0, Xi+1, . . . Xn)
is a non-decreasing function of X1, . . . , Xi−1, Xi+1, . . . , Xn for each i ∈[n]. When
viewing the binary input of g as the indicator vector for a set, this is equivalent to the
more common deﬁnition that g is supermodular if for any X, Y ⊆[n] with X ⊆Y
and any x /∈Y, we have
g(X ∪{x}) −g(X) ≤g(Y ∪{x}) −g(Y).
Mutlilinear Extension.
The multilinear extension of a function f is
F(x) = E[ f (x)] = 
S⊆N f (S) 
i∈S xi

i /∈S(1 −xi),
Algorithmica (2026) 88 :21
Page 7 of 19
21
for x ∈[0, 1]n. If we view x as a probability vector, the multilinear extension F is
simply the expected value of f when each coordinate is rounded independently in
{0, 1}.
