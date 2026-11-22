---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-021-a3-complementation-principle
section_title: "Complementation principle"
section_number: A.3
pages: 39-40
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
A.3. Complementation principle. In this section we discuss a sim-
ple but useful observation which was communicated to us by S. Kerov.
Consider an arbitrary probability measure on Conf(X) such that its
correlation functions
ρ(X) = Prob ({Y ∈Conf(X), X ⊂Y }) ,
X ∈Conf(X)0 ,
have a determinantal form
ρ(X) = det
h
K(xi, xj)
i
xi∈X
for some kernel K.
Let Z ⊂X be an arbitrary subset of X. Consider the symmetric
diﬀerence mapping
△Z : Conf(X) →Conf(X) ,
Y 7→Y △Z ,
which is an involution in Conf(X). Let Prob△= (△Z)∗Prob be the
image of our probability measure under △Z and let ρ△(X) be the
correlation functions of the measure Prob△. Deﬁne a new kernel K△
as follows. Let Z′ = X\Z be the complement of Z and write the matrix
K in the block form with respect to the decomposition X = Z′ ⊔Z
KZ′⊔Z =

A
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
Proof. Set X1 = X \ Z, X2 = Z \ X.
By the inclusion-exclusion
principle we have
ρ△(X) = Prob ({Y ∈Conf(X), X1 ⊂Y, X2 ∩Y = ∅})
=
X
S⊂X2
(−1)|S|ρ(X1 ∪S) .
This alternating sum is easily seen to be identical to the expansion of
det
h
K△(xi, xj)
i
xi∈X by linearity using

A
B
−C
1 −D

=

A
B
−C
−D

+

0
0
0
1

40
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
