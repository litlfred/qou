---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov Traces on Hecke Algebras ∗ R.C. Orellana"
section_id: sec-006-12-schur-functions
section_title: "Schur Functions"
section_number: 1.2
pages: 4-6
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
doc_brief: "Weights of Markov Traces on Hecke Algebras ∗ R.C. Orellana — We compute the weights, i.e. the values at the minimal idempo tents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
For details and proofs on the results mentioned in this subsection we refer the reader to [M]
Ch.I, sec. 3. Suppose x1, x2, . . . xr is a ﬁnite set of variables. For some partition α we set
Weights of Markov Traces on Hecke Algebras 5
xα = xα 1
1 . . . xα r
r . Let δ = [r − 1, r − 2, . . . , 1, 0]. We deﬁne the following determinant.
aα +δ = det(x
λ j +r−j
i )
This determinant is divisible in Z[x1, . . . , xr] by the Vandermonde determinant which is
given by
aδ = det(xr−j
i ).
Then the symmetric Schur function is deﬁned as follows:
sα (x1, . . . , xr) = aα +δ
aδ
.
Take xi = qi−1 (1 ≤ i ≤ r). If λ is a partition of length ≤ r, we have
sα (1, q, . . . , qr−1) = qn(α )
∏
1≤i<j≤r
1 − qα i−α j+j−i
1 − qj−i (1)
where n(α) = ∑ l(α )
i=1 (i − 1)αi. We deﬁne the following Schur function as a normalization of
equation (1):
sα,r (q) = sα (1, q, . . . , qr−1)
s[1](1, q, . . . , qr−1)|α | = qn(α ) ∏
1≤i<j≤r
(1 − q)(1 − qα i−α j +j−i)
(1 − qr)(1 − qj−i)
Notice that sα,r (q) = 0 whenever l(α) > r . Also if χα (q) denotes the character of a matrix
in Gl(r) with eigenvalues q(−r+1)/ 2, q(−r+3)/ 2, . . . , q(r−1)/ 2 and if the number of boxes in α is
n, sα,r (q) = χα (q)/(χ[1](q))n.
Let r = r1 + r2; then the Schur function for µ = [ m + α1, . . . , m + αr1, β1, . . . , βr2] is
given by
sµ,r (q) = qn(µ ) ∏
1≤i<j≤r
(1 − q)(1 − qµ i−µ j +j−i)
(1 − qr)(1 − qj−i) . (2)
After some rearrangement of equation (2) we get the following equ ation for the Schur function
of µ:
sµ,r (q) = qmr1(r1−1)/ 2+r1|β |( 1 − q
1 − qr )|µ |sα (1, q, . . . , qr1−1)sβ (1, q, . . . , qr2−1)
r1∏
i=1
r2∏
j=1
1 − qm+r1+α i−β j+j−i
1 − qr1+j−i . (3)
The expression of this Schur function in (3) is useful in the proof of the weight formula!
