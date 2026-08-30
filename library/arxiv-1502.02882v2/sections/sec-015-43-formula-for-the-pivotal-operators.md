---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-015-43-formula-for-the-pivotal-operators
section_title: "Formula for the pivotal operators"
section_number: 4.3
pages: 24-25
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
We now show how to compute the pivotal operators directly in terms of the
associator matrix elements. More precisely, we express them in terms of the
apex associator monodromy.
Deﬁnition 4.12. The apex associatorsare the associator matrix elements where
the top strand is the identity 2:
=
∑
β
(Sijk)βα
 (29)
That is, (Sijk)βα = (F 1
ijk)ηkk∗β
ηi∗i∗α. The apex associator monodromy Aijk is the
product of matrices SjkiSkijSijk.
Example 4.13. In the Yang-Lee category, we read oﬀ from (9) that Sτττ = 1.
For categoryE, we read oﬀ from (11) and (12) that
Sxxx = 1√
2e
7πi
12
(
1 −i
−i i
)
and the apex associator monodromy is Axxx =S3
xxx = id.
Remark 4.14. In all examples that the author knows of, the apex associator
monodromy in a fair basis is the identity.
Proposition 4.15. In a fair basis, the cyclic operators Cijk compute as
Cijk =pkSijk
wherepk is the pivotal indicator of Xk and Sijk are the apex associators.
2Thus they form a sharp angle diagrammatically, hence the name.
24
Proof. By deﬁnition, and using the pairing convention, the bending matrix ele-
ments (Cijk)βα are the coeﬃcients appearing in the expansion
dk
 =
∑
β
(Cijk)βα
 .
We can rewrite the left-hand side using the apex associators (29):
LHS =dk
∑
β
(Sijk)βα
 =dkak∗
∑
β
(Sijk)βα
The second equality uses (28b) and Lemma 4.5. In a fair basis, dkak∗ =pk and
we are done.
We have thus proved the following result.
Corollary 4.16. In a fair basis, the monodromy of the cyclic operators is the
product of the pivotal indicators with the apex associator monodromy:
Tijk =pipjpkAijk. (30)
Combining this with Lemma 4.2 gives the following explicit formula for the
pivotal operators Ti
jk in terms of the apex associator monodromy.
Theorem 4.17. In a fair basis, the pivotal operator Ti
jk is equal to the product
of the pivotal indicators with the conjugate of the apex-associator monodromy,
Ti
jk =pipjpkY−1Ai∗jkY . (31)
Remark 4.18. The above formula (31) reﬁnes a formula of Wang [27, Prop
4.17], which treats the multiplicity-free case and does not include the pivotal
indicators.
Example 4.19. In the Yang-Lee category,Tτττ = (−1)3 =−1. In category E,
all the pivotal operators are the identity.
