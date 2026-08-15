---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-002-12-motivation
section_title: "Motivation"
section_number: 1.2
pages: 3-6
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
What does it take to solve a q-diﬀerence equation?
Solving a linear equation usually means giving a basis of solutions, say at t = 0 and
t =∞ (the only two canonical points, ﬁxed under the shift transformation t↦→ qt), and
to compute the monodromy (i.e., the connection) between t = 0 and t =∞ in terms of
“known” functions. This problem has a rich history with an interesting balance between
concrete special functions and the abstract, which the reader may consult in Okounkov’s
talks and their references.
A key to the solution is to choose linearq-diﬀerence equations of natural origin, for instance
the ones appearing in quantum cohomology [61], in Kontsevich’s talks on resurgence [48], or
in quantum topology and Chern–Simons theory [25, 34].
Recently, it was observed that the solutions of some linear q-diﬀerence equations con-
cerning quantum knot invariants [36, 37] or resurgence and Borel resummation of pertur-
bative Chern–Simons theory [26, 27, 28], have an improved analyticity property. Roughly
speaking, this means that some holomorphic functions on C \ R extend on the cut plane
C ′ = C \ (−∞, 0]. This extension property has been formalised recently by Zagier as
holomorphic quantum modular forms [70]. This extends previous ideas around quantum
modularity [72] that appeared in Chern–Simons theory [11, 14, 43, 50].
Our attempt to understand the mechanism behind this property abstractly led us to the
notion of a modular q-holonomic module. Quite by accident, this suggests an answer to the
question posed above, namely:
Modularity can solve eﬀectively a q-diﬀerence equation.
1.3. Deﬁnition and properties. To explain the new concept, consider the linearq-diﬀerence
equation
σX =AX (3)
for a vector-valued function X = X(t,q ), where ( σX)(t,q ) = X(qt,q ) denotes the shift
operator, A(t,q )∈ GLr(Q (t,q )) and q is a nonzero complex number with |q|⁄ = 1. Fix a
fundamental matrix solution U to (3) at t = 0, which we assume is ﬁltration-preserving and
of weight κU = diag(τκU,1,...,τ κU,r) and deﬁne
ΩU,γ = (U|κUγ)U−1, γ =
(a b
c d
)
∈ SL2(Z ) (4)
where the slash operator|κUγ is deﬁned in Section 2.4 below. The map γ↦→ ΩU,γ is a cocycle
of SL2(Z ), i.e., it satisﬁes
ΩU,γγ′(z,τ ) = ΩU,γ(γ′(z,τ ))ΩU,γ′(z,τ ) (5)
for all γ,γ′∈ SL2(Z ). Likewise, let V denote a ﬁltration-preserving fundamental solution at
t =∞, and
−→
M =V−1U denote the monodromy matrix (often called “connection matrix”).
The monodromy is always an elliptic function (i.e., σ-invariant). If it satisﬁes the equation
−→
M = ∆κV,γ(
−→
M|κUγ), γ =
(a b
c d
)
∈ SL2(Z ) (6)
4 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
for some γ =
(a b
c d
)
∈ SL2(Z ) then the cocycle matrices associated to U and V are equal:
ΩU,γ = ΩV,γ γ =
(a b
c d
)
∈ SL2(Z ). (7)
(The converse holds, too, and the equivalence of (7) and (6) holds for each ﬁxedγ). A priori,
Ωγ = ΩU,γ = ΩV,γ is a holomorphic function of τ∈ C \ R and a meromorphic function of
z (with t = e(z)) with poles in a ﬁnite union of translates of the lattice Z +τ Z . For an
element γ =
(a b
c d
)
∈ SL2(Z ), we let C γ denote the cut plane C \ (−∞,−d/c] (if c > 0),
C \ [−d/c,∞) (if c <0) and C \ R when c = 0. The next deﬁnition concerns an improved
analytic property of Ωγ.
Deﬁnition 1.1. We say that a q-diﬀerence equation is modular if for all γ∈ SL2(Z ), its
cocycle Ωγ extends to a meromorphic function of ( z,τ )∈ C × C γ with potential poles at
z∈Sγ + Z +τ Z for a ﬁnite set Sγ.
We make several comments concerning this deﬁnition.
1. For a modular q-diﬀerence equation, the two sides of τ∈ C \ R communicate: the restric-
tion of Ωγ on the one side of the plane Im( τ) > 0 uniquely determines (and is determined
by) the function on the other side Im( τ)< 0.
2. In a sense, our notion of modular linear q-diﬀerence equation is a q-analogue of the
second, third and fourth order modular linear diﬀerential equations studied by Kaneko,
Nagatomo, Zagier and others [4, 45, 46] in relation to Conformal Field Theory and Vertex
Operator Algebras. The characters of a VOA (under a mild C2-condition) are solutions to
a modular linear diﬀerential equation [19, 73]. An alternative title of our paper could be
“Modular linearq-diﬀerence equations” in direct analogy with the modular linear diﬀerential
equations of CFTs and VOAs. On the other hand, the current title emphasises the “module”
aspect as opposed to the “equation aspect”.
3. Our notion explains conceptually the improved analyticity properties conjectured in
relation to the structure of exact and perturbative invariants of Chern–Simons theory [26,
27, 28, 36, 37], as well as the work of Gukov et al relating logarithmic CFTs and VOAs to
Chern–Simons theory [13].
4. Our notion leads to a diﬀerent perspective on quantum Jacobi forms [10]. While the
matrix valued aspect is more general, the analytic conditions are much stricter. However,
many examples, with some reﬁnements, are expected to ﬁt into our deﬁnition.
5. Modular linear diﬀerential equations seem rare. On the other hand, modular linear q-
diﬀerence equations appear abundant: we conjecture (see the end of Section 1) that the
ˆA-polynomial of a knot (i.e., the linear q-diﬀerence equation satisﬁed by the colored Jones
polynomial of a knot [34]) is a modular linear q-diﬀerence equation. This brings a new
perspective to the Jones polynomial of a knot.
6. The modularity of the monodromy for modular q-holonomic modules is a restricted condi-
tion, which leads to the complete determination of the monodromy even when a fundamental
solution is deﬁned byq-Borel resummation. This in turn completely determines the so-called
q-Stokes phenomenon coming from the change of the ray of the q-Laplace transform.
7. The cocycle Ω U,γ as a function of a fundamental solution of a linear q-diﬀerence equation
appears new and diﬀerent from the matrices considered in Etingof [22] that generate the
Galois group of the equation.
MODULAR q-HOLONOMIC MODULES 5
8. The above deﬁnition involves all elements of SL 2(Z ), although it imposes no improved
extension when γ2,1 = 0. The third part of the next theorem (under the hypothesis that
ΩT =I which is satisﬁed in all of our examples), rephrases the modularity of Deﬁnition 1.1
in terms of ΩS alone, whereS =
( 0−1
1 0
)
andT =
( 1 1
0 1
)
of SL2(Z ) are the standard generators
of SL2(Z ). Recall that C ′ = C S = C \ (−∞, 0].
Theorem 1.2. (a) If Equation (6) for the monodromy holds for γ =S and γ =T , then it
holds for all γ∈ SL2(Z ).
(b) If Ω is an SL2(Z )-cocycle with ΩT = I, then ΩS satisﬁes the 4-term and the 3-term
functional equations
1 = ΩS
(
−z
τ,−1
τ
)
ΩS (−z,τ ) ΩS
(z
τ,−1
τ
)
ΩS(z,τ ) (8a)
ΩS(z,τ ) = ΩS
( z
τ + 1, τ
τ + 1
)
ΩS(z,τ + 1). (8b)
Conversely, given ΩT = I and ΩS that satisﬁes the above functional equations, there is a
SL2(Z )-cocycle with those values.
(c) If Ω is a cocycle such that ΩT =I and ΩS extends as a meromorphic function of (z,τ )∈
C × C ′, then Ωγ extends as a meromorphic function of (z,τ )∈ C × C γ for all γ∈ SL2(Z ).
Note that with the assumptions of part (c) above, we have
Ω−I(z,τ ) = ΩS
(z
τ,−1
τ
)
ΩS(z,τ ) (9)
which is meromorphic on C ×(C \R ), in general does not extend any further; see for instance
the cocycle of Theorem 1.5 below.
9. Our ﬁnal comment concerns the distinction between a linear q-diﬀerence equation to a
q-holonomic module. A linear q-diﬀerence equation leads to a pair ( M,e ) of a q-holonomic
module M over the q-Weyl algebraW = Q (q,t )⟨σ⟩/(σt−qtσ) and a cyclic vector e of M.
The categoryM ofq-holonomic modules is an abelian category, which admits a multivariable
extension closed under the usual operations on sheaves. For a detailed introduction, see [16]
and [65], and also [33]. Whereas D-modules over the Weyl algebra have only one dual (see
for example, [67, Sec.2.2]), modules over the q-Weyl algebra have two duals M∧ (the usual
Hom-dual as in the case of D-modules) and a dual M∨ coming from the involutionq↦→q−1,
discussed in Section 2.5 below. The next lemma summarises some categorical properties of
modular q-holonomic modules.
Lemma 1.3. (a) Modularity of aq-holonomic module is independent of the choice of a cyclic
vector.
(b) If 0→M′→M→M′′→ 0 is a short exact sequence of q-holonomic modules and M is
modular, then M and M′ are also modular.
(c) M is a modular, then M∧ and M∨ are modular with cocycles given by
Ω∧(z,τ ) := Ω(z,−τ), and Ω ∨ = (Ω−1)t (10)
where Ω is a cocycle of M.
6 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
