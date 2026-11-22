---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-017-a3-complementation-principle
section_title: "A.3. Complementation principle"
section_number: null
pages: 31-32
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 22 sections: Front matter; Plancherel measures; Introduction"
---
observation which was communicated to us by S. Kerov. Consider an arbitrary
probability measure on Conf(X) such that its correlation functions
ρ(X) = Prob({Y ∈Conf(X), X ⊂Y }) ,
X ∈Conf(X)0 ,
have a determinantal form
ρ(X) = det
h
K(xi, xj)
i
xi∈X
for some kernel K.
Let Z ⊂X be an arbitrary subset of X.
Consider the symmetric diﬀerence
mapping
△Z : Conf(X) →Conf(X) ,
Y 7→Y △Z ,
which is an involution in Conf(X).
Let Prob△= (△Z)∗Prob be the image of
our probability measure under △Z and let ρ△(X) be the correlation functions of
the measure Prob△.
Deﬁne a new kernel K△as follows.
Let Z′ = X \ Z be
the complement of Z and write the matrix K in block form with respect to the
decomposition X = Z′ ⊔Z:
KZ′⊔Z =
A
B
C
D

.
By deﬁnition, set
K△
Z′⊔Z =

A
B
−C
1 −D

.
We have the following
Proposition A.8. ρ△(X) = det
h
K△(xi, xj)
i
xi∈X .
512
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
Proof. Set X1 = X \ Z, X2 = Z \ X. By the inclusion-exclusion principle we have
ρ△(X) = Prob ({Y ∈Conf(X), X1 ⊂Y, X2 ∩Y = ∅})
=
X
S⊂X2
(−1)|S|ρ(X1 ∪S) .
This alternating sum is easily seen to be identical by linearity to the expansion of
det
h
K△(xi, xj)
i
xi∈X using
 A
B
−C
1 −D

=
 A
B
−C
−D

+
0
0
0
1

.
