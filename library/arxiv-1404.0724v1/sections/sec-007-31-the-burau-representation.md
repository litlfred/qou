---
doc_id: arxiv-1404.0724v1
doc_title: "Introduction to representations of braid groups"
section_id: sec-007-31-the-burau-representation
section_title: "The Burau representation"
section_number: 3.1
pages: 7-10
source_pdf: 1404.0724v1.pdf
source_sha256: ea40edaad77c1617
toc_source: outline
doc_brief: "Introduction to representations of braid groups — These are lecture notes prepared for a minicourse given at the Cimpa Research School Algebraic and geometric aspects of representation the- ory, held"
duplicate_of: "ariasabad2015-revcolmat"
---
tion as action of mapping classes on homology, and their relation with the Alexander-Conway
polynomial of links. We also introduce the Lawrence-Krammer-Bigelow representation, which
has the remarkable property of being faithful. Our exposition follows closely the book by Kassel
and Turaev [18].
3.1
The Burau representation
Let us denote by Λ the ring of Laurent polynomials with integer coeﬃcients:
Λ := Z[t, t−1].
In [7], W. Burau constructed representations of the braid group Bn on the space Aut(Λn) of
n × n matrices with coeﬃcients in Λ. Let us deﬁne the n × n matrix Ui as follows:
Ui =




Ii−1
0
0
0
0
1 −t
t
0
0
1
0
0
0
0
0
In−i−1




Proposition 3.1. There is a unique group homomorphism ψn : Bn →Aut(Λn) characterized by
the property that:
σi 7→Ui.
This homomorphism is called the Burau representation of Bn.
Proof. We begin by proving that the matrices Ui are invertible. Let us set
U =
 1 −t
t
1
0

.
Since the matrices Ui are block diagonal matrices whose blocks are either identity matrices of
U it is enough to prove that U is an invertible matrix. For this we exhibit an explicit inverse:
U−1 =

0
1
t−1
1 −t−1

.
One can directly check that UU−1 = U−1U = id. The block form of the matrices implies that
UiUj = UjUi provided that |i −j| ≥2. Finally, it remains to show that
UiUi+1Ui = Ui+1UiUi+1.
This can be checked in the case n = 3 and becomes the following exercise in matrix multiplica-
tion:


1 −t
t
0
1
0
0
0
0
1




1
0
0
0
1 −t
t
0
1
0




1 −t
t
0
1
0
0
0
0
1

=


1
0
0
0
1 −t
t
0
1
0




1 −t
t
0
1
0
0
0
0
1




1
0
0
0
1 −t
t
0
1
0

.
□
Remark 3.2. Setting t = 1, each of the matrices Ui becomes a permutation matrix, and one
obtains representations of Bn that factor through the symmetric groups. For this reason, the
Burau representations may be seen as deformation of the usual permutation representation.
The Burau representation admits a one dimensional invariant subspace. By taking the quotient
of Λn by this invariant subspace one obtains the reduced Burau representations.
Proposition 3.3. Let n be a natural number greater that 2 and V1, . . . , Vn−1 be the (n−1)×(n−1)
matrices deﬁned as follows:
V1 =


−t
0
0
1
1
0
0
0
In−3

, Vn−1 =


In−3
0
0
0
1
t
0
0
−t

,
and for 1 < i < n −1 :
Vi =






Ii−2
0
0
0
0
0
1
t
0
0
0
0
−t
0
0
0
0
1
1
0
0
0
0
0
In−i−2






.
Also, Let C be the n × n matrix over Λ:
C =







1
1
1
. . .
1
0
1
1
. . .
1
0
0
1
. . .
1
...
...
...
...
...
0
0
0
. . .
1







.
Then:
C−1UiC =
 Vi
0
Xi
1

,
where Xi is the row of length n −1 which is (0, . . . , 0) in case i̸ = n −1 and is (0, . . . 0, 1) for
i = n −1.
Proof. We set
Wi :=
 Vi
0
Xi
1

.
It suﬃces to prove that UiC = CWi for all i = 1, . . . , n −1. A direct computation shows that:
UiC =














1
1
1
. . .
1
1
0
1
1
. . .
1
1
0
0
1
. . .
1
1
...
...
...
...
...
...
0
0
0
1 −t
. . .
1
0
0
0
1
. . .
1
...
...
...
...
...
...
0
0
0
. . .
0
1














.
Similarly, a simple calculation gives:
CWi =














1
1
1
. . .
1
1
0
1
1
. . .
1
1
0
0
1
. . .
1
1
...
...
...
...
...
...
0
0
0
1 −t
. . .
1
0
0
0
1
. . .
1
...
...
...
...
...
...
0
0
0
. . .
0
1














.
Here, the matrices on the right hand side of the equations are those obtained from C by replacing
the entry (i, i) by 1 −t and the entry (i + 1, i) by 1. This completes the proof.
□
Since conjugation with the matrix C is an automorphism, we conclude that the matrices Wi
satisfy the braid relations. Moreover, since det(Wi) = det(Vi), the matrices Vi are invertible as
elements of End(Λn−1). The fact that the last column of the matrices Wi is nonzero only in the
last entry also implies that the matrices Vi satisfy the braid relations. These observations allow
us to make the following deﬁnition:
Deﬁnition 3.4. For n ≥2 the reduced Burau representation of the braid group Bn is the
representation ψr
n : Bn →Aut(Λn−1) characterized by the property that:
σi 7→Vi.
For n = 2 the reduced Burau representation is given by ψr
2(σ1) = −t.
Remark 3.5. The Burau representation is known to be faithful for n ≤3 and not faithful for
n ≥5. It is not known whether it is faithful for n = 4. A theorem of Bigelow asserts that ψ4 is
faithful if and only if the Jones polynomial detects the unknot.
