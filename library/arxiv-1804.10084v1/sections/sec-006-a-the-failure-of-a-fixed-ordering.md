---
doc_id: arxiv-1804.10084v1
doc_title: "Concentration of Lipschitz Functions of Negatively Dependent Variables"
section_id: sec-006-a-the-failure-of-a-fixed-ordering
section_title: "A The failure of a fixed ordering"
section_number: null
pages: 9-10
source_pdf: 1804.10084v1.pdf
source_sha256: 716da9708f06d930
toc_source: outline
doc_brief: "Concentration of Lipschitz Functions of Negatively Dependent Variables — We explore the question whether Lipschitz functions of random variables under various forms of negative correlation satisfy"
---
The failure of a ﬁxed ordering
Here we review brieﬂy the argument presented in [5] and why it is ﬂawed. In Proposition 31, [5]
states Theorem 1 under the assumption of f being monotone and Lipschitz with constant ci in
variable Xi; here let us assume ci = 1. The proof proceeds by deﬁning Yk = E[f(X) | X1, . . . , Xk]
(using our notation) and claiming that this martingale has bounded diﬀerences. In the last line of
the proof, it is claimed that “Similarly it follows that . . . ”. However, the desired inequality does
not follow by the same argument, and can be false.
Example. Consider the following random variables X1, . . . , Xn: X2, . . . , Xn are independent and
uniformly random in {0, 1}. X1 is the NAND function of X2, . . . , Xn, i.e., X1 = 1 −Qn
i=2 Xi. Note
that Pr[X1 = 1] = 1 −1/2n−1. We claim that X1, . . . , Xn satisfy negative regression:
Let I, J ⊂[n] be disjoint and a ≤b ∈{0, 1}J. We consider the following cases:
• If 1 /∈I ∪J, then there is no dependence between XI and XJ.
• If 1 ∈I, then the distribution of XI diﬀers under XJ = a, b only if a̸ = 1J and b = 1J. In
this case, the XJ = b is consistent with Xi = 0 or Xi = 1, while XJ = a implies X1 = 1.
The other variables in I are independent of XJ. Hence, conditioning on XJ = a as opposed
to XJ = b can only increase the expectation of any monotone function f(XI).
• If 1 ∈J, then the distribution of XI diﬀers under XJ = a, b only if a1 = 0 and b1 = 1. In this
case, XI = a implies that all the other variables are equal to 1, while XI = b is consistent
with any assignment to the other variables except all 1’s. Therefore, conditioning on XJ = a
as opposed to XJ = b can only increase the expectation of any monotone function f(XI).
9
Now consider the martingale Y0, Y1, . . . , Yn, where Yk = E[f(X) | X1, . . . , Xk] for f(X) =
Pn
i=1 Xi.
Y0 = E[f(X)] =
n
X
i=1
E[Xi] = (1 −
1
2n−1 ) + 1
2(n −1) = 1
2(n + 1) −
1
2n−1 .
If X1 = 0 (which happens with probability 1/2n−1), this implies that all the remaining variables
are equal to 1, which means that Y1 = n −1. Therefore, the diﬀerence between Y0 and Y1 can be
Ω(n). Clearly, the issue here is the enormous inﬂuence of X1 via its correlation with the remaining
variables, and this is what motivates our adaptive ordering of variables.
10
