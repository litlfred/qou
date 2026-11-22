---
doc_id: arxiv-math-9802116v1
doc_title: "arXiv:math/9802116v1 [math.QA] 25 Feb 1998"
section_id: sec-001-2-preliminaries-general-constructions
section_title: "Preliminaries: General constructions"
section_number: 2
pages: 2-7
source_pdf: 9802116v1.pdf
source_sha256: be7999751ffb6db3
toc_source: inferred
doc_brief: "Quasialgebra structure of the octonions — We show that the octonions are a twisting of the group algebra of Z2 × Z2 × Z2 in the quasitensor category of representations of a quasi-Hopf algebra asso"
---
An introduction to quantum groups, including quasitensor categories and quasi-Hopf algebras
is in [2], the main notations of which we use here. In fact, the natural setting for us is the dual
of Drinfeld’s axioms[1], namely the notion of a dual quasi-Hopf algebra[3][2].
Thus, a dual quasibialgebra is a (H, ∆, ǫ, φ) where the coproduct ∆: H →H ⊗H and counit
ǫ : H →k form a coalgebra (the axioms are those of a unital associative algebra with arrows
reversed) and are multiplicative with respect to a ‘product’ H ⊗H →H. This is required to be
2
associative up to‘conjugation’ by φ in the sense
X
a(1) · (b(1) · c(1))φ(a(2), b(2), c(2)) =
X
φ(a(1), b(1), c(1))(a(2) · b(2)) · c(2)
(1)
for all a, b, c ∈H. Here ∆h = P h(1) ⊗h(2) is a notation and φ is a unital 3-cocycle in the sense
X
φ(b(1), c(1), d(1))φ(a(1), b(2)c(2), d(2))φ(a(2), b(3), c(3)) =
X
φ(a(1), b(1), c(1)d(1))φ(a(2)b(2), c(2), d(2)),
(2)
for all a, b, c, d ∈H, and φ(a, 1, b) = ǫ(a)ǫ(b) for all a, b ∈H.
We also require that φ is
convolution-invertible in the algebra of maps H⊗3 →k, i.e. that there exists φ−1 : H⊗3 →k
such that
X
φ(a(1), b(1), c(1))φ−1(a(2), b(2), c(2)) = ǫ(a)ǫ(b)ǫ(c) =
X
φ(a(1), b(1), c(1))φ−1(a(2), b(2), c(2))
for all a, b, c ∈H.
A dual quasibialgebra is a quasi-Hopf algebra if there is a linear map S : H →H and linear
functionals α, β : H →k such that
X
(Sa(1))a(3)α(a(2)) = 1α(a),
X
a(1)Sa(3)β(a(2)) = 1β(a),
(3)
X
φ(a(1), Sa(3), a(5))β(a(2))α(a(4)) = ǫ(a),
X
φ−1(Sa(1), a(3), Sa(5))α(a(2))β(a(4)) = ǫ(a)
(4)
for all a ∈H.
Finally, H is called dual quasitriangular if there is a convolution-invertible map R : H ⊗H →
k such that
R(a · b, c) =
X
φ(c(1), a(1), b(1))R(a(2), c(2))φ−1(a(3), c(3), b(2))R(b(3), c(4))φ(a(4), b(4), c(5)),
(5)
R(a, b · c) =
X
φ−1(b(1), c(1), a(1))R(a(2), c(2))φ(b(2), a(3), c(3))R(a(4), b(3))φ−1(a(5), b(4), c(4)),
(6)
X
b(1) · a(1)R(a(2), b(2)) =
X
R(a(1), b(1))a(2) · b(2)
(7)
for all a, b, c ∈H.
We recall also that a corepresentation or comodule under a coalgebra means vector space V
and a map β : V →V ⊗H obeying (id ⊗∆) ◦β = (β ⊗id) ◦∆and (id ⊗ǫ) ◦β = id. This is the
notion of an action with arrows reversed. In the ﬁnite-dimensional case a coaction of H means
an action of the associative algebra H∗.
A monoidal category is a category C of objects V, W, Z,etc. a functor ⊗: C × C →C and a
natural transformation Φ : (( ⊗) ⊗) →( ⊗( ⊗)) between the two functors C × C × C →C,
where Φ obeys Mac Lane’s ‘pentagon identity’ for equality of the two obvious isomorphisms[4]
(((V ⊗W) ⊗Z) ⊗U∼=V ⊗(W ⊗(Z ⊗U)))
built from Φ for any four objects V, W, Z, U. A braided or ‘quasitensor’ category is a monoidal
one which has, in addition, a natural transformation Ψ : ⊗→⊗op obeying two ‘hexagon’
coherence conditions, see [5].
The comodules MH over a quasi-Hopf algebra form such a category with
ΦV,W,Z((v ⊗w) ⊗z) =
X
v ¯
(1) ⊗(w ¯
(1) ⊗z ¯
(1))φ(v ¯
(2), w ¯
(2), z ¯
(2))
for v ∈V , w ∈W, z ∈Z. Here β(v) = P v ¯
(1) ⊗v ¯
(2) is a notation and the tensor product is
two comodules is a comodule by composition with the product of H. In the quasitriangular
case the category is braided[1], with ΨV,W(v ⊗w) = P w ¯
(1) ⊗v ¯
(1)R(v ¯
(2), w ¯
(2)). There is also a
conjugate or dual coaction on V ∗made possible by the antipode S. The converse is also true,
namely any (braided) monoidal category with duals and with a multiplicative functor to the
category of vector spaces (and some ﬁniteness properties) comes from the comodules over a dual
(quasitriangular) quasi-Hopf algebra[3].
If H is a dual quasi-Hopf algebra then so is HF with the new product, Φ, R, α, β given by
a ·F b = P F −1(a(1), b(1))a(2)b(2)F(a(3), b(3))
φF (a, b, c) = P F −1(b(1), c(1))F −1(a(1), b(2)c(2))φ(a(2), b(3), c(3))F(a(3)b(4), c(4))F(a(4), b(5))
αF(a) = P F(Sa(1), a(3))α(a(2)),
βF (a) = P F −1(a(1), Sa(3))β(a(2))
RF (a, b) = P F −1(b(1), a(1))R(a(2), b(2))F(a(3), b(3))
(8)
for all a, b, c ∈H. Here F is any convolution-invertible map F : H ⊗H →k obeying F(a, 1) =
F(1, a) = ǫ(a) for all a ∈H (a 2-cochain). This is the dual version of the twisting operation or
‘gauge equivalence’ of Drinfeld, so called because it does not change the category of comodules
up to monoidal equivalence.
Deﬁnition 2.1 Let H be a dual quasi-Hopf algebra.
An H-comodule quasialgebra A is an
algebra in the category of H-comodules. This means an H-comodule, a product map · associative
in the category and equivariant under the action of H. Explicitly,
(a · b) · c =
X
a ¯
(1) · (b ¯
(1) · c ¯
(1))φ(a ¯
(2), b ¯
(2), c ¯
(2)),
β(a · b) = β(a)β(b),
∀a, b ∈H
where the last expression uses the tensor product algebra in A ⊗H.
Proposition 2.2 If A is an H-comodule quasialgebra and F : H ⊗H →k a 2-cochain, then
AF with the new product
a ·F b =
X
a ¯
(1)b ¯
(1)F(a ¯
(2), b ¯
(2))
and unchanged unit, is an HF -comodule quasialgebra.
Proof
This is elementary and follows from the equivalence of the comodule categories under
twisting. See also [6] in the module version. ⊔⊓
There is a parallel theory with all arrows reversed. Thus, H can be a quasi-Hopf algebra, with
associative product and ∆coassociative up to conjugation by an invertible 3-cocycle φ ∈H⊗3[1].
In this case the modules of H form a monoidal category and, in the quasitriangular case a braided
one. In this case we work with H-module quasialgebras and their twistings by F ∈H ⊗H.
When the theory is developed in this comodule form, it is an easy matter to specialize to the
following class of examples: let H = kG the group algebra of a group. This has coproduct etc.
∆x = x ⊗x,
ǫx = 1,
Sx = x−1,
∀x ∈G
forming a Hopf algebra. However, for any point-wise invertible group cocycle φ : G×G×G →k
in the sense
φ(y, z, w)φ(x, yz, w)φ(x, y, z) = φ(x, y, zw)φ(xy, z, w),
φ(x, e, y) = 1
(9)
extended linearly to kG⊗3, we can regard (kG, φ) as a dual quasi-Hopf algebra. Group inversion
provides an antipode with α = ǫ, β(x) = 1/φ(x, x−1, x). Finally, a dual quasitriangular structure
is possible only when G is Abelian and corresponds to invertible R : G × G →k such that
R(xy, z) = R(x, z)R(y, z)φ(z, x, y)φ(x, y, z)
φ(x, z, y)
,
R(x, yz) = R(x, z)R(x, y)
φ(y, x, z)
φ(y, z, x)φ(x, y, z)
(10)
for all x, y, zıG.
A special case is when φ is a coboundary
φ(x, y, z) = F(x, y)F(xy, z)
F(y, z)F(x, yz) ,
R(x, y) = R0(x, y)F(x, y)
F(y, x),
β(x) = F(x−1, x)
F(x, x−1)
(11)
for any invertible F obeying F(x, e) = 1 = F(e, x) for all x ∈G and any invertible bicharacter
R0. This is the twisting of the group algebra (kG, R0) regarded as a dual quasitriangular Hopf
algebra[2] with trivial initial φ0.
Next, a coaction of kG means precisely a G-grading, where β(v) = v ⊗|v| on homogeneous
elements of degree |v|. Hence the notion of an H-comodule quasialgebra in this case becomes:
Deﬁnition 2.3 A G-graded quasialgebra is an G-graded vector space A, a product map A ⊗A →
A preserving the total degree and associative in the sense
(a · b) · c = a · (b · c)φ(|a|, |b|, |c|),
∀a, b, c ∈A
(of homogeneous degree), for a 3-cocycle φ. A G-graded quasi-algebra is called coboundary if φ
is a coboundary as in (11).
This is the setting which we will use, with the above as the underlying explanation of the
constructions. If G is ﬁnite we can equally regard its function algebra k(G) with φ ∈k(G)⊗3
as a quasi-Hopf algebra kφ(G) as in [7], and then view a G-graded quasialgebra as equivalently
a kφ(G)-module quasialgebra. Here the action of h ∈kφ(G) is h.v = vh(|v|) on homogeneous
elements.
Corollary 2.4 kF G deﬁned as kG with a modiﬁed product
x ·F y = xyF(x, y),
∀x, y ∈G
is a coboudary G-graded quasialgebra. The degree of x ∈G is x, and F is any 2-cochain on G.
Proof
This is a special case of the twisting proposition. Here kG coacts on itself by β = ∆,
i.e. the degree of x ∈G is x. We now twist kG to the dual quasi-Hopf algebra (kG, φ = ∂F). In
the process, we also twist kG as a comodule algebra to kF G as a comodule quasialgebra under
this dual quasi-Hopf algebra. ⊔⊓
We note an elementary properties of kF G.
Proposition 2.5 With trivial initial bicharacter R0, the category of G-graded vector spaces is
symmetrically braided (in the sense Ψ2 = id) and kF G is braided-commutative in the sense
a · b = · ◦Ψ(a ⊗b),
∀a, b ∈kF G.
Proof
This is immediate from (11) and the deﬁnition of Ψ from R.
The latter is clearly
Ψ(a ⊗b) = b ⊗a F (|a|,|b|)
F (|b|,|a|) for elements of homogeneous degree |a|, |b|, which is braided but trivially
braided in the sense Ψ2 = id (i.e. the category of G-graded spaces in this case is symmetric
monoidal rather than strictly braided.) ⊔⊓
