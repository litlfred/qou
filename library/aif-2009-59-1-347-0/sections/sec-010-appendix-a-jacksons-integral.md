---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-010-appendix-a-jacksons-integral
section_title: "Appendix A. Jackson's integral"
section_number: null
pages: 21-22
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
toc_source: outline
doc_brief: "On q-summation and confluence — 28 sections: Front matter; Introduction; Part 1. Convergent q-Borel and q-L"
---
Definition A.1. — We set
F(x) =
Z x
0
f(t)dqt = (1 −q)x
X
n⩾0
f(qnx)qn,
whenever the right hand side converges.
Remark A.2. —
1. Notice that if F(x) is well-deﬁned then dqF(x) = f(x).
2. If f(x) is continuous on the closed disk D(0, r+), then F(x) is well deﬁned
for any x ∈D(0, r+). In fact there exists M > 0 such that |f(qnx)qn| ⩽
M|q|n, which guarantees the convergence of the inﬁnite sum.
Proposition A.3. —
1. If f(x) is an analytic function over the disk D(0, r−), then F(x) is also
analytic over D(0, r−).
2. If F(x) is analytic over the disk D(0, r−) and if G(x) is another analytic
function over D(0, r−) such that dqG(x) = f(x), then
Z x
0
f(t)dqt = G(x) −G(0).
Proof. —
1. It follows from the fact that F(x) is a uniformly convergent series of
analytic function over D(0, r −ε+), for any r > ε > 0.
2. It follows immediately from the remark that the subﬁeld of constants
of the ring of analytic function over D(0, r−) with respect to the operator
f(x) 7→f(qx) is C. In fact this implies that F(x) −G(x) ∈C.
□
Definition A.4. — Let us ﬁx a q-orbit qZα ⊂C and suppose that for
any x ∈qZα the integral F(x) =
R x
0 f(t)dqt is well-deﬁned. Then we set
Z
qZα
f(t)dqt =
lim
|x|→∞
x∈qZα
Z x
0
f(t)dqt.
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
367
Remark A.5. —
A straightforward calculation shows that
Z
qZα
f(t)dqt = (1 −q)α
X
n∈Z
f(qnα)qn
and in particular that
Z
qZα
f(t)dqt
t
= (1 −q)
+∞
X
n=−∞
f(qnα),
whenever the right side converges.
