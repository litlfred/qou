---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-012-31-solutions
section_title: "Solutions"
section_number: 3.1
pages: 24-25
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
equation (11). Since that equation depends on parameters, it will be convenient to consider
the following system of equations
(r−1∏
j=0
(1−q−1bjσt)−t
r∏
j=1
(1−ajσt)
)
f = 0
(
σ−1
ai −q−1aiσtσ−1
ai − (1−q−1ai)
)
f = 0
(
1−q−1biσt− (1−q−1bi)σ−1
bi
)
f = 0.
(111)
The ﬁrst equation describes the q-diﬀerence equation in t, namely Equation (11) whose
Newton polygon shown in Figure 1.
g(a−1
1 ) g(a−1
r )
f (1) f (qb−1
r−1)
Figure 1. The Newton polygon of the ﬁrst Equation (111).
We see that there are no slopes of the Newton polygon and therefore all solutions are
determined by the top and bottom edges and their indicial polynomials. We will normalise
MODULAR q-HOLONOMIC MODULES 25
the solutions coming from the Frobenius algorithm so that they satisfy the full system of
Equations (111). The bottom edge of the Newton polygon in Figure 1 has indicial polynomial
(1−ρ)(1−q−1b1ρ)... (1−q−1br−1ρ) = 0. (112)
The solutions corresponding to the roots are given by f (q−1bj ) in Equation (14), with the
convention that b0 = q. The top edge of the Newton polygon in Figure 1 has indicial
polynomial
(1−a1ρ)... (1−arρ) = 0. (113)
The solutions corresponding to the roots are given byg(a−1
j ) in Equation (16). The companion
matrix of Equation (11) is given by
A(t,a,b,q ) =


0 1 ... 0
: : ... :
0 0 ... 1
−(−1)r 1−t
er(b/q)−ter(a) (−1)re1(b/q)−te1(a)
er(b/q)−ter(a) ... er−1(b/q)−ter−1(a)
er(b/q)−ter(a)

 (114)
where
ek(x) =
∑
1≤j1<···<jk≤r
xj1...x jk (115)
are the elementary symmetric polynomials and so with U and V in Equation (13),
U(qt,a,b,q ) =A(t,a,b,q )U(t,a,b,q ) and V (qt,a,b,q ) =A(t,a,b,q )V (t,a,b,q ). (116)
