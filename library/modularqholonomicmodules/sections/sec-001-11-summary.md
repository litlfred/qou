---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-001-11-summary
section_title: "Summary"
section_number: 1.1
pages: 1-3
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
1.2. Motivation 3
1.3. Deﬁnition and properties 3
1.4. The generalised q-hypergeometric equation is modular 6
1.5. Modular q-holonomic modules in Chern–Simons theory 7
2. A review of linear q-diﬀerence equations 12
2.1. Preliminaries 12
2.2. An algorithm for a fundamental matrix 13
2.3. The q-Borel and the q-Laplace transforms 14
2.4. The slash operator and proof of Theorem 1.2 17
2.5. Duality 20
2.6. Categorical aspects 23
3. Heine’s q-hypergeometric functions 24
3.1. Solutions 24
3.2. Self duality 25
3.3. State integral 28
3.4. Resonance 29
4. Proof of Theorems 1.5 and 1.6 31
4.1. The q-Pochhammer symbol 31
4.2. The Appell-Lerch sums 33
Date: 35 May 2022.
Key words and phrases : q-diﬀerence equations, modular linear q-diﬀerence equations, conformal ﬁeld
theory, vertex operator algebras, q-holonomic modules, modular q-holonomic modules, q-Borel transform,
q-Laplace transform, resummation, monodromy, elliptic functions,q-hypergeometric equations, generalisedq-
hypergeometric equations, Jacobi theta function, Appell-Lerch sums, Mordell integral, quantum dilogarithm,
knots, 3-manifolds, Chern-Simons theory, holomorphic quantum modular forms, Conformal Field Theory,
Vertex Operator Alegbras.
1
2 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
5. A q-diﬀerence equation of the 4 1 knot 37
5.1. Solutions 37
5.2. Monodromy 40
5.3. Residues 43
5.4. Determinants 45
5.5. State integral 46
5.6. The inhomogeneous equation 47
5.7. The x-deformation 52
5.8. An analytic lift of the colored Jones polynomial 62
5.9. Specialisation t =qm 62
Acknowledgements 63
References 63
1. Introduction
1.1. Summary. We introduce a new class of linear q-diﬀerence equations and (correspond-
ing q-holonomic modules) which we call modular, with several key features.
• Their fundamental solutions at 0 and inﬁnity have explicitly computable monodromy.
• A natural SL2(Z )-cocycle constructed from a fundamental solution extends fromC \R
to the complex plane minus a ray in the real numbers.
• Their fundamental solutions are meromorphic and their residues are expressed in
terms of the solutions themselves (kind of ’resurgence’).
Modularq-holonomic modules are abundant. We show that the generalisedq-hypergeometric
equation (11) (and in particular the q-hypergeometric equation) is modular and self-dual;
see Theorem 1.4 below. Among other things, this implies an improved analyticity for the
q-hypergeometric function
2φ1(a,b ;c;q,t ) =
∞∑
k=0
(a;q)k(b;q)k
(c;q)k(q;q)k
tk, (1)
namely, that the bilinear combination
(q;q)∞(c;q)∞
(a;q)∞(b;q)∞
(˜q˜a; ˜q)∞(˜q˜b; ˜q)∞
(˜q; ˜q)∞(˜q˜c; ˜q)∞
2φ1(a,b ;c;q,t )2φ1(˜a−1,˜b−1; ˜c−1; ˜q, ˜q˜a˜b˜c−1˜t)
+τθ(q−1ct;q)(q;q)3
∞
θ(t;q)θ(q−1c;q)
(q2c−1;q)∞(q;q)∞
(qac−1;q)∞(qbc−1;q)∞
θ(˜q˜c; ˜q)θ(˜t; ˜q)
θ(˜q˜c˜t; ˜q)(˜q; ˜q)3
∞
(˜a˜c−1; ˜q)∞(˜b˜c−1; ˜q)∞
(˜q−1˜c−1; ˜q)∞(˜q; ˜q)∞
× 2φ1(qac−1,qbc−1;q2c−1;q,t )2φ1(˜q˜a−1˜c, ˜q˜b−1˜c; ˜q2˜c; ˜q, ˜q˜a˜b˜c−1˜t)
(2)
(which a priori is a meromorphic function of τ∈ C \ R ) extends toτ∈ C \(−∞, 0]. We also
show that modular linear q-diﬀerence equations and the corresponding q-holonomic mod-
ules appear naturally in complex Chern-Simons theory. We illustrate with three examples
(Theorems 1.5, 1.6 and 1.7 below) whose corresponding cocycles are the Faddeev quantum
dilogarithm, the Appell-Lerch sums, and the Andersen–Kashaev state integrals of the 4 1
knot.
MODULAR q-HOLONOMIC MODULES 3
We expect that all proper (i.e., basic) q-hypergeometric modules are modular, and in par-
ticular the ones that appear in the quantum diﬀerential equation in Quantum Cohomology,
or the linear q-diﬀerence equation for the small J-function of Quantum K-Theory.
