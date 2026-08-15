---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-004-extension-to-skew-functions
section_title: "Extension to skew functions"
section_number: null
pages: 5-6
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
Now, one can easily obtain similar formulas for sums of the skew Schur functions SR/P . To this end, one needs
a slight generalization of the Cauchy identity (4):
X
R
SR/P{p}SR{¯p} = exp
 ∞X
k=1
pk ¯pk
k
!
SP{¯p} (27)
Taking the average of this identity over ¯pk with measure (13), one obtains
X
R
SR/P{p}
D
SR{¯p}
EA
¯p
=
X
R
SR/P{p} =
*
exp
 ∞X
k=1
pk ¯pk
k
!
SP{¯p}
+A
¯p
(28)
Let us prove that the r.h.s. of this formula is given by
*
exp
 ∞X
k=1
pk ¯pk
k
!
SP{¯p}
+A
¯p
= exp
(∞X
k=1
p2
k
2k + p2k−1
2k− 1
)X
Q
SP/Q{p} (29)
5
with literally the same p-dependent factor as in (12). To this end, we convert this formula with the Schur
functions SP{p′}. This gives
*
exp
 ∞X
k=1
(pk +p′
k)¯pk
k
!+A
¯p
= exp
(∞X
k=1
p2
k
2k + p2k−1
2k− 1 + pkp′
k
k
)X
Q
SQ{p′} (30)
where we once again used the Cauchy identities (4) and (27) at the l.h.s. and at the r.h.s. Now it remains to
calculate the Gaussian integral at the l.h.s. as it was done in (12), and also to use (12) to evaluate the sum at
the r.h.s. Hence, formula (29) is correct, and we finally obtain from (28)
X
R
SR/P{p} = exp
(∞X
k=1
p2
k
2k + p2k−1
2k− 1
)X
Q
SP/Q{p} (31)
We can now make one more check that (31) is correct. Convert this formula with SP{p′} and use the Cauchy
identity (27) and the definition of the skew Schur polynomial
SR{p +p′} =
X
P
SR/P{p}SP{p′} (32)
Then
X
R
SR{p +p′} = exp
(∞X
k=1
p2
k
2k + p2k−1
2k− 1 + pkp′
k
k
)X
Q
SQ{p} (33)
Both sums can be calculated using (12) in order to validate this formula. We emphasize once again that,
according to this argument, the p-dependent factor at the r.h.s. is literally the same as in (12), and the same
will be true for the skew Schur counterparts of all other identities in this section.
