---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-002-12-motivation
section_title: "Motivation"
section_number: 1.2
pages: 3-5
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
What does it take to solve a q-diﬀerence equation?
Solving a linear equation usually means giving a basis of solutions, say at t = 0 and
t = ∞ (the only two canonical points, ﬁxed under the shift transformat ion t ↦→qt), and
to compute the monodromy (i.e., the connection) between t = 0 and t = ∞ in terms of
“known” functions. This problem has a rich history with an interestin g balance between
concrete special functions and the abstract, which the reader m ay consult in Okounkov’s
talks and their references.
A key to the solution is to choose linear q-diﬀerence equations of natural origin, for instance
the ones appearing in quantum cohomology [ 55], in Kontsevich’s talks on resurgence [ 43], or
in quantum topology and Chern–Simons theory [ 21, 30].
Recently, it was observed that the solutions of some linear q-diﬀerence equations con-
cerning quantum knot invariants [ 32, 33] or resurgence and Borel resummation of pertur-
bative Chern–Simons theory [ 22, 23, 24], have an improved analyticity property. Roughly
speaking, this means that some holomorphic functions on /BV \ /CA extend on the cut plane
/BV
′ = /BV \ (−∞, 0]. This extension property has been formalised recently by Zagier a s holo-
morphic quantum modular forms [ 64].
Our attempt to understand the mechanism behind this property ab stractly led us to the
notion of a modular q-holonomic module. Quite by accident, this suggests an answer to th e
question posed above, namely:
Modularity can solve eﬀectively a q-diﬀerence equation.
1.3. Deﬁnition and properties. To explain the new concept, consider the linear q-diﬀerence
equation
σX = AX (3)
for a vector-valued function X = X(t, q), where ( σX )(t, q) = X(qt, q) denotes the shift
operator, A(t, q) ∈ GLr( /C9 (t, q)) and q is a nonzero complex number with |q| ⁄= 1. Fix a
fundamental matrix solution U to ( 3) at t = 0, which we assume is ﬁltration-preserving and
of weight κU = diag(τ κU, 1, . . . , τκU,r ) and deﬁne
Ω U,γ = (U|κU γ)U −1, γ =
( a b
c d
)
∈ SL2( /CI ) (4)
where the slash operator |κU γ is deﬁned in Section 2.4 below. The map γ ↦→Ω U,γ is a cocycle
of SL 2( /CI ), i.e., it satisﬁes
Ω U,γγ ′(z, τ ) = Ω U,γ(γ′(z, τ ))Ω U,γ′(z, τ ) (5)
for all γ, γ ′ ∈ SL2( /CI ). Likewise, let V denote a ﬁltration-preserving fundamental solution at
t = ∞, and
− →
M = V −1U denote the monodromy matrix (often called “connection matrix”).
The monodromy is always an elliptic function (i.e., σ-invariant). If it satisﬁes the equation
− →
M = ∆ κV ,γ(
− →
M|κU γ), γ =
( a b
c d
)
∈ SL2( /CI ) (6)
4 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
for some γ =
( a b
c d
)
∈ SL2(
/CI ) then the cocycle matrices associated to U and V are equal:
Ω U,γ = Ω V,γ γ =
( a b
c d
)
∈ SL2( /CI ) . (7)
(The converse holds, too, and the equivalence of ( 7) and ( 6) holds for each ﬁxed γ). A priori,
Ω γ = Ω U,γ = Ω V,γ is a holomorphic function of τ ∈ /BV \ /CA and a meromorphic function of
z (with t = e(z)) with poles in a ﬁnite union of translates of the lattice /CI + τ /CI . For an
element γ =
( a b
c d
)
∈ SL2( /CI ), we let /BV
γ denote the cut plane /BV \ (−∞, −d/c] (if c > 0),
/BV \ [−d/c, ∞) (if c < 0) and /BV \ /CA when c = 0. The next deﬁnition concerns an improved
analytic property of Ω γ.
Deﬁnition 1.1. We say that a q-diﬀerence equation is modular if for all γ ∈ SL2( /CI ), its
cocycle Ω γ extends to a meromorphic function of ( z, τ ) ∈ /BV × /BV
γ with potential poles at
z ∈ Sγ + /CI + τ /CI for a ﬁnite set Sγ.
We make several comments concerning this deﬁnition.
1. For a modular q-diﬀerence equation, the two sides of τ ∈
/BV \ /CA communicate: the restric-
tion of Ω γ on the one side of the plane Im( τ ) > 0 uniquely determines (and is determined
by) the function on the other side Im( τ ) < 0.
2. In a sense, our notion of modular linear q-diﬀerence equation is a q-analogue of the
second, third and fourth order modular linear diﬀerential equation s studied by Kaneko,
Nagatomo, Zagier and others [ 4, 40, 41] in relation to Conformal Field Theory and Vertex
Operator Algebras. The characters of a VOA (under a mild C2-condition) are solutions to
a modular linear diﬀerential equation [ 15, 66]. An alternative title of our paper could be
“Modular linear q-diﬀerence equations” in direct analogy with the modular linear diﬀere ntial
equations of CFTs and VOAs. On the other hand, the current title e mphasises the “module”
aspect as opposed to the “equation aspect”.
3. Our notion explains conceptually the improved analyticity propert ies conjectured in
relation to the structure of exact and perturbative invariants of Chern–Simons theory [
22,
23, 24, 32, 33], as well as the work of Gukov et al relating logarithmic CFTs and VOAs to
Chern–Simons theory [ 10].
4. Modular linear diﬀerential equations seem rare. On the other han d, modular linear q-
diﬀerence equations appear abundant: we conjecture (see the e nd of Section 1) that the
ˆA-polynomial of a knot (i.e., the linear q-diﬀerence equation satisﬁed by the colored Jones
polynomial of a knot [ 30]) is a modular linear q-diﬀerence equation. This brings a new
perspective to the Jones polynomial of a knot.
5. The modularity of the monodromy for modular q-holonomic modules is a restricted condi-
tion, which leads to the complete determination of the monodromy ev en when a fundamental
solution is deﬁned by q-Borel resummation. This in turn completely determines the so-calle d
q-Stokes phenomenon coming from the change of the ray of the q-Laplace transform.
6. The cocycle Ω U,γ as a function of a fundamental solution of a linear q-diﬀerence equation
appears new and diﬀerent from the matrices considered in Etingof [
18] that generate the
Galois group of the equation.
7. The above deﬁnition involves all elements of SL 2(
/CI ), although it imposes no improved
extension when γ2,1 = 0. The third part of the next theorem (under the hypothesis tha t
Ω T = I which is satisﬁed in all of our examples), rephrases the modularity of Deﬁnition 1.1
MODULAR q-HOLONOMIC MODULES 5
in terms of Ω S alone, where S =
( 0 −1
1 0
)
and T =
( 1 1
0 1
)
of SL2(
/CI ) are the standard generators
of SL 2( /CI ). Recall that /BV
′ = /BV
S = /BV \ (−∞, 0].
Theorem 1.2. (a) If Equation (6) for the monodromy holds for γ = S and γ = T , then it
holds for all γ ∈ SL2( /CI ).
(b) If Ω is an SL2( /CI )-cocycle with Ω T = I, then Ω S satisﬁes the 4-term and the 3-term
functional equations
1 = Ω S
(
− z
τ , − 1
τ
)
Ω S (−z, τ ) Ω S
( z
τ , − 1
τ
)
Ω S(z, τ ) (8a)
Ω S(z, τ ) = Ω S
( z
τ + 1 , τ
τ + 1
)
Ω S(z, τ + 1) . (8b)
Conversely, given Ω T = I and Ω S that satisﬁes the above functional equations, there is a
SL2( /CI )-cocycle with those values.
(c) If Ω is a cocycle such that Ω T = I and Ω S extends as a meromorphic function of (z, τ ) ∈
/BV × /BV
′, then Ω γ extends as a meromorphic function of (z, τ ) ∈ /BV × /BV
γ for all γ ∈ SL2( /CI ).
Note that with the assumptions of part (c) above, we have
Ω −I(z, τ ) = Ω S
( z
τ , − 1
τ
)
Ω S(z, τ ) (9)
which is meromorphic on /BV ×( /BV \ /CA ), in general does not extend any further; see for instance
the cocycle of Theorem 1.5 below.
8. Our ﬁnal comment concerns the distinction between a linear q-diﬀerence equation to a
q-holonomic module. A linear q-diﬀerence equation leads to a pair ( M, e) of a q-holonomic
module M over the q-Weyl algebra W = /C9 (q, t)⟨σ⟩/(σt − qtσ) and a cyclic vector e of M.
The category M of q-holonomic modules is an abelian category, which admits a multivariable
extension closed under the usual operations on sheaves. For a de tailed introduction, see [ 12]
and [ 59], and also [ 29]. Whereas D-modules over the Weyl algebra have only one dual (see
for example, [ 61, Sec.2.2]), modules over the q-Weyl algebra have two duals M ∧ (the usual
Hom-dual as in the case of D-modules) and a dual M ∨ coming from the involution q ↦→q−1,
discussed in Section 2.5 below. The next lemma summarises some categorical properties of
modular q-holonomic modules.
Lemma 1.3. (a) Modularity of a q-holonomic module is independent of the choice of a cyclic
vector.
(b) If 0 → M ′ → M → M ′′ → 0 is a short exact sequence of q-holonomic modules and M is
modular, then M and M ′ are also modular.
(c) M is a modular, then M ∧ and M ∨ are modular with cocycles given by
Ω ∧(z, τ ) := Ω( z, −τ ), and Ω ∨ = (Ω −1)t (10)
where Ω is a cocycle of M.
