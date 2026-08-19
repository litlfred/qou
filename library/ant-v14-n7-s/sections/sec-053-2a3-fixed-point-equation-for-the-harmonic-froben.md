---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-053-2a3-fixed-point-equation-for-the-harmonic-froben
section_title: "2A3. Fixed point equation for the harmonic Frobenius"
section_number: null
pages: 62-62
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Section 2A2, an expression of the iterated harmonic Frobenius of integrals at (1, 0) as a function of its
number of iterations, whose coefﬁcients are expressed in terms of the ﬁxed point of the Frobenius at
(1, 0); this is (0-3).
By Proposition 2B.1, we haveτ(q˜α)8q,∞◦∫1,08q,˜α=8q,∞. By deﬁnition, the inverse of8q,∞ for◦∫1,0
is8q,−∞ thus the inverse ofτ(q˜α)(8q,∞) isτ(q˜α)(8q,−∞). Whence8q,˜α=τ(q˜α)8q,−∞◦∫1,08q,∞. By
applying Ad(e1), we deduce Ad8q,˜α(e1)=τ(q˜α) Ad8q,−∞(e1)◦
∫1,0
Ad Ad8q,∞(e1), whence S Ad8q,˜α(e1)=
S(τ(q˜α) Ad8q,−∞(e1)◦
∫1,0
Ad Ad8q,∞(e1)). By the commutative diagram in Deﬁnition 2A.3, this amounts
to S Ad8q,˜α(e1)=τ(q˜α) Ad8q,−∞(e1)◦
∫1,0
har S Ad8q,∞(e1)). By (1-19), we have S Ad8q,˜α(e1)= harq,˜α and
S Ad8q,∞(e1))= harq,∞. Whence (0-3).
Remark 2A.8. The power series expansion of any harq˜α((ni)d;(ξi)d+1) in terms of q˜α, given by (0-3)
have coefﬁcients of degrees in{1,..., min1⩽i⩽d ni− 1} equal to 0. This follows from 8(ξ)
q,−∞[e0]= 0
which implies Ad8(ξ)
q,−∞
(eξ)= eξ+ terms of depth > 2, for allξ∈µN(K).
Example 2A.9. In depth one and two and for P1\{ 0, 1,∞}, we have
harq˜α(n1)= harq∞(n1)+
∞∑
n=n1
(q˜α)n Ad8q,−∞(e1)[en−n1
0 e1en1−1
0 e1],
harq˜α(n1, n2)= harq∞(n1, n2)+
∞∑
n=n1+n2
(q˜α)n Ad8q,−∞(e1)[en−n1−n2
0 e1en2−1
0 e1en1−1
0 e1]
+
n1−1∑
r1=0
∞∑
n=n2+r1
(q˜α)n Ad8q,−∞(e1)[en−n2−r1
0 e1en2−1
0 e1er1
0] harq∞(n1− r1)
+
n2−1∑
r2=0
(q˜α)n1+r2 Ad8q,−∞(e1)[er
0e1en1−1
0 e1] harq∞(n2− r2).
