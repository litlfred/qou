---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-007-21-preliminaries
section_title: "Preliminaries"
section_number: 2.1
pages: 12-13
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
toc_source: outline
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
equations with a small parameter are typically factorially divergent series, which lead to
MODULAR q-HOLONOMIC MODULES
13
analytic solutions to the diﬀerence equation after applying the process of a Borel transfor-
mation, followed by a Laplace transformation. This subject is classical and well-studied, see
for example [6, 15, 52, 53].
A corresponding theory for linear q-diﬀerence equations was developed recently by di Vizio,
Sauloy, Ramis and others [20, 42, 64], with particular emphasis given on the arithmetic
and the Galois theoretic aspects of the theory. A q-holonomic module has two canonical
ﬁltrations, one from t = 0 and another from t = ∞. These ﬁltrations can be computed
concretely choosing a cyclic vector which converts the q-holonomic module into a linear
q-diﬀerence equation.
To explain the solutions of linear q-diﬀerence equations, let us recall the Jacobi theta
function which is given by a one dimensional lattice sum, and by an inﬁnite product (known
as the Jacobi triple product identity) by
θ(t; q) =
X
k∈Z
(−1)kqk(k+1)/2tk = (qt; q)∞(t−1; q)∞(q; q)∞.
(46)
From the above representation, it is easy to see that it satisﬁes the functional equations
θ(t−1; q) = θ(q−1t; q) = −tθ(t; q)
(47)
which imply that
θ(qℓt; q) = (−1)ℓq−ℓ(ℓ+1)/2t−ℓθ(t; q),
(ℓ∈Z) .
(48)
The Jacobi theta function is modular. Its transformation under the element S of SL2(Z) is
given by
θ(˜t; ˜q) = e(−3/8)e
 z2
2τ

t
1
2 ˜t−1
2q
1
8 ˜q−1
8√τ θ(t; q) .
(49)
The derivative of θ with respect to td/dt = 1/(2πi)d/dz,
θ′(t; q) =
X
k
(−1)kkqk(k+1)/2tk
(50)
satisﬁes the q-diﬀerence equation
θ′(qℓt; q)
θ(qℓt; q) = θ′(t; q)
θ(t; q) −ℓ.
(51)
It has transformation under the element S of SL2(Z) given by
θ′(t; q)
θ(t; q)

1S := 1
τ
θ′(˜t; ˜q)
θ(˜t; ˜q) = θ′(t; q)
θ(t; q) + z
τ + 1
2 −1
2τ .
(52)
