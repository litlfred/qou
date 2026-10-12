---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-021-22-vertex-operator-algebras-the-linear-category-re
section_title: "Vertex operator algebras, the linear category Rep(V ) and Zhu algebra A(V )"
section_number: 22
pages: 133-138
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
22. Vertex operator algebras, the linear category Rep(V ) and Zhu
algebra A(V )
In this section we recall the basic theory of vertex operator algebras, their modules. We
give a reformulation in a Tannakian framework of a result that has roots in Zhu’s work on
the correspondence between V -modules and modules of the associated Zhu algebra A(V ).
We also recall the important rationality conditions on V under which Huang proved
modularity of the category Rep(V ) of V -modules.
In the next section we recall the basic theory of intertwining operators and Huang and
Lepowsky’s tensor product theory. We shall discuss applications in Sects. 33, 21, 34.
We refer the reader to textbooks [60], [59], [102] for the general theory of vertex operator
algebras.
Definition 22.1. A vertex operator algebra is a Z-graded vector space V
V =
M
n∈Z
V(n),
with finite dimensional homogeneous spaces V(n) and V(n) = 0 for n sufficiently small,
together with a triple (Y, 1, ν), where Y is the state-field correspondence, a linear map
Y : V → End(V )[[x, x−1
]], a → Y (a, x) = X
n∈Z
a(n)x
−n−1
,
with x is a formal variable. The element Y (a, x) is called the vertex operator associated
with a. The element 1 lies in V(0) and is called the vacuum, and ν ∈ V(2) is called the
Virasoro vector. The following conditions form the definition for all a, b ∈ V ,
a) (lower truncation condition): a(n)b = 0 for n sufficiently large.
b) (vertex operator associated to the vacuum) Y (1, x) = idV
c) (creation property) Y (a, x)1 ∈ V [[x]] (power series with non-negative integral powers)
and
limx→0Y (a, x)1 = a,
d) (Virasoro algebra relations and spectrum condition for L0) Set
Ln = ν(n+1)
, i.e. Y (ν, x) = P
n∈Z Lnx
−n−2
, then
[Lm, Ln] = (m − n)Lm+n +
1
12
(m3 − m)δm+n,0c, (22.1)
with c ∈ C the central charge of V . Moreover
L0a = na, a ∈ V(n), (22.2)
n is called the conformal weight, energy, or degree of the vector a ∈ V(n), and denoted
deg(a); L0 is the energy operator, or conformal Hamiltonian on V .

134 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
e) L−1-derivative (or translation) property
d
dxY (a, x) = Y (L−1a, x), (22.3)
f) (Jacobi identity) for l, m, n ∈ Z,
X∞
i=0

m
i

Y (a(l+i)b, x)x
m+n−i =
X∞
i=0
(−1)i

l
i

a(m+l−i)Y (b, x)x
n+i −
X∞
i=0
(−1)l+i

l
i

Y (b, x)a(m+i)x
n+l−i
,
This completes the definition. The formal limit limx→0 and the formal derivative d
dx are
defined in the natural way. On a fixed vector of V , only finitely many addenda appearing
in the series of the Jacobi identity f) are possibly non-zero, thus both sides of the identity
are well-defined. The axioms of vertex operator algebra have a number of consequences.
A special case of the Jacobi identity for l = n = 0 gives
[a(m), Y (b, x)] = X∞
i=0

m
i

Y (a(i)b, x)x
m−i
, (22.4)
thus the operators a(m) are in particular closed under the Lie bracket. Moreover, together
with the translation property e) of L−1 this equation implies for L−1 = ν(0) and L0 = ν(1),
[L−1, Y (b, x)] = d
dxY (b, x), [L0, Y (b, x)] = ddxY (b, x)x + Y (L0b, x).
The right hand side together with the eigenvalue property (22.2) of L0 and implies the
useful grading relation
b(n) : V(m) → V(m+deg(b)−n−1). (22.5)
It also follows that a(n)1 = 0 for n ≥ 0.
The Jacobi identity can be written in readily equivalent forms, and we have chosen one
of them. A compact form is the following
x
−1
0
δ(
x1 − x2
x0
)Y (a, x1)Y (b, x2) − x
−1
0
δ(
x2 − x1
−x0
)Y (b, x2)Y (a, x1) = (22.6)
x
−1
2
δ(
x1 − x0
x2
)Y (Y (a, x0)b, x2)),
where δ(x) = P
n∈Z
x
n
, we refer the reader to the references at the beginning of the
section for complete explanation of the use of the δ. There is yet another set of properties
equivalent to the Jacobi identity, in presence of the other axioms of vertex operator algebra.
This set properties are the rationality of products, iterates, commutativity of products, and
associativity, the latter being a property involving products and iterates. We refer the
reader to Sect. 8.10 in [60] and also Sect. 2 in [84]. This formulation of the Jacobi identity
turns out useful for the development of tensor product theory by Huang and Lepowsky and

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 135
we encourage a non-expert reader to consider this viewpoint for insight. We shall come
back to this in Sect. 37. We next give the definition of a V -module.
Definition 22.2. (V -module) Given a vertex operator algebra (V, Y, 1, ν), a V -module is
a pair (M, YM), with M an R-graded vector space
M =
M
r∈R
Mr,
by finite dimensional subspaces Mr that eventually vanish for r small and a linear map
YM : V → End(M)[[x, x−1]], a → YM(a, x) = X
n∈Z
a
M
(n)x
−n−1
,
defining a vertex operator YM(a, x) associated with M, satisfying properties analogous
to the defining properties of the vertex operators Y (a, x) associated to V , except for the
creation property of the vacuum vector, that is omitted. In particular, the endomorphism
a(l+i) appearing at the left hand side of the Jacobi identity f) and the operator L−1 defining
the derivative property for the V -module M are associated to V , while the remaining
equations in the definition involve vertex operators YM(a, x) associated to M. The constant
c in the Virasoro algebra relations for M equals the central charge of V .
Let M be a V -module. If ν ∈ V is the conformal vector we write
YM(ν, x) = X
n∈Z
L
M
n x
−n−2
, a ∈ V . (22.7)
In particular L
M
0 denotes the conformal Hamiltonian on M. For m ∈ Mr, the spectral
property of L
M
0 holds,
L
M
0
(m) = ∆mm, (22.8)
where ∆m := r is called the conformal weight or energy of the homogeneous vector m. For
M = V and a ∈ V(n), ∆a = deg(a) = n in the notation of [197].
Definition 22.3. (The category Rep(V )) Given V -modules M1 and M2, a morphism T ∈
HomV (M1, M2) is is a linear map satisfying T YM1(a, x) = YM2(a, x)T for all a ∈ V . In
particular, for a = ν this condition shows that T preserves the gradings of the modules.
This defines the category Rep(V ) of V -modules.
We wish to define a canonical functor FV : Rep(V ) → Vec. When the assumption in
Theorem 7.9 are satisfied then, thanks to the Tannaka-Krein duality result in Theorem 7.6
we will be able to associate a weak quasi-Hopf algebra to Rep(V ).
The defining properties of a V -module imply, similarly to the case of a vertex operator
algebra (22.5). The Jacobi identity for a V -module for l = n = 0 gives
[a
M(m), YM(b, x)] = X∞
i=0

m
i

YM(a(i)b, x)x
m−i
, (22.9)
and implies
[L
M
−1
, YM(b, x)] = d
dxYM(b, x), [L
M
0
, YM(b, x)] = d
dxYM(b, x)x + YM(L0b, x). (22.10)

136 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
and we similarly derive from the right hand side and the spectral property of L
M
0
, the
following grading relations for the modes, or coefficients b
M
(n)
of the associated vertex operators, for b ∈ V homogeneous
b
M
(n)
: Mr → Mr+deg(b)−n−1 for r ∈ R, n ∈ Z. (22.11)
It follows particular (or from the Virasoro algebra relations)
L
M
n = ν(n+1) : Mr → Mr−n.
Every V -invariant subspace of M is a V -module, see Remark 1.5 in [73]. It follows from
(22.11) that every V -module M can be canonically decomposed compatibly with the original grading of M as a direct sum of V -modules
M =
M
s∈S
M(s),
where M(s) =
L
n∈Z≥0 Ms+n, and S is the collection of s ∈ R such that Ms−n = 0 for all
n ∈ N and Ms ̸= 0 [197].
Moreover, M is irreducible if and only if it has no V -invariant subspace. If M is irreducible then S consists of a single element
∆M := inf{r ∈ R : Mr ̸= 0} ∈ S, (22.12)
called the conformal weight of the irreducible module M. We set, for n ∈ Z≥0,
M(n):= Mn+∆M = Ker(L
M
0 − (∆M + n)1M). (22.13)
If M is irreducible then
M =
M
n∈Z≥0
M(n),
We shell refer to M(0) the lowest energy subspace, or top space of M.
The Virasoro algebra relations for L
M
n
(or the grading equation (22.11)) implies that for
an integer n ̸= 0 and b ∈ M homogeneous L
M
0 L
M
n
b = (∆b − n)L
M
n
b. Let M be irreducible.
We then have the following relations
L
M
0
b = ∆Mb; L
M
n
b = 0, n > 0; b ∈ M(0). (22.14)
This property will turn out useful in Sect. 38 to discuss primary fields. Thanks to (22.9)
and the first equation in (22.10), the conditions (22.14) are equivalently written as
[L
M
m , YM(b, x)] = x
m(x
d
dxYM(b, x) + (m + 1)∆MYM(b, x)), m ∈ Z. (22.15)
Remark 22.4. 1) The study of rationality in conformal field theory has roots in the work
by Anderson and Moore [5]. A definition of rationality for a vertex operator algebra was
introduced by Zhu [197]. The definition was later simplified by Dong, Li and Mason, and
we try to summarize some of their main results.
2) The definition of a weak module is given in [32]. The weakness as compared to the Def.
22.2 of V -module means that the grading assumption for M and the spectral condition
(22.2) for L
M
0
are omitted for a weak module. Moreover the Virasoro and translation

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 137
relations (22.1), (22.3) are redundant for a weak module, and thus for a V -module, by
Lemma 2.2 in [32].
3) Dong, Li and Mason call a weak module ordinary if it is endowed with a C-grading by
finite dimensional subspaces Mλ such that for each λ ∈ C, Mλ+n = 0 for n small enough,
and the usual spectral property for L
M
0 holds. They also call a weak module admissible
if it is graded by Z≥0 and the grading relation (22.11) holds for modes of the associated
vertex operators, for all r ∈ Z≥0 and n ∈ Z. Any ordinary module is admissible. If
every admissible is a direct sum of irreducible admissible modules then every irreducible
admissible is ordinary by [33].
4) Note that a more general definition of V -module starts with a C-graded vector space. If
each admissible V -module is completely reducible then V has only finitely many inequivalent admissible modules, and every such module is ordinary [33].
5) By [5] and Theorem 11.3 in [35] the grading of a V -module is automatically in R. More
in detail, the conformal weight of an irreducible ordinary module is rational and the central
charge is rational.
The rationality assumptions for V in the sense of Dong, Li, Mason as in 3) of Remark
22.4 imply [33] in particular that there are only finitely many inequivalent irreducible
V -modules, and that a V -module M can be written as a finite direct sum
M =
M
i
Mi(22.16)
of irreducible V-modules Micompatibly with the grading, by Theorem 8.1 [33], see also
Theorem 3.2 in [35]. For each Mi we write
Mi =
M
n∈Z≥0
Mi
(n)
(22.17)
with Mi
(n) = Ker(L
Mi
0 − (∆Mi + n)1Mi ) and Mi
(0) ̸= {0}. Note that every Mi(n)
is finite
dimensional. We now define a finite dimensional subspace M(0) ⊂ M by
M(0) := M
i
Mi
(0) . (22.18)
It is easy to see that M(0) is independent from the choice of the direct sum decomposition
in Eq. (22.16). Moreover, it can be shown that U(M, V )M(0) = M where U(M, V ) is the
subalgebra of End(M) generated by the vertex operator coefficients a
M
(n)
, a ∈ V , n ∈ Z.
Now let Mα and Mβ be V -modules Mα and Mβ and T : Mα → Mβ a V -module
homomorphism. Recall that from the equality T LMα
0 = L
Mβ
0 T it follows that TMα
(0) ⊂
M
β
(0).
We now define a linear functor FV : Rep(V ) → Vec in the following way. If M is an
object in Rep(V ), i.e. a V -module, then FV (M) = M(0). If T : Mα → Mβis a morphism
in Rep(V ), i.e. a V -module homomorphism, then FV (T) = T ↾Mα
(0)
.

138 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
If FV (T) = 0 then, TMα = TU(Mα, V )Mα
(0) = U(Mβ
, V )TMα
(0) = {0} so that T = 0
and hence FV is faithful. We are now in the position to apply Theorem 7.6. Let A(V ) :=
Nat0(FV ).
Theorem 22.5. Let V be a VOA such that every admissible module is a direct sum of
simple admissible modules. Then A(V ) is a semisimple associative algebra that can be
identified with the Zhu’s algebra of V . Moreover, there is an equivalence EV : Rep(V ) →
Rep(A(V )) which, after composition with the forgetful functor : Rep(A(V )) → Vec is
isomorphic to FV .
Definition 22.6. We refer to FV : Rep(V ) → Vec as Zhu’s functor and to EV : Rep(V ) →
Rep(A(V )) as Zhu’s equivalence.
Remark 22.7. Zhu’ functor FV and equivalence EV recalled at the end of Sect. 22 play
an important role in our paper. Moreover, Zhu constructs a canonical linear equivalence
SV : Rep(A(V )) → Rep(V ),
that is a right inverse of EV ,
EV SV = 1.
The previous theorem is a reformulation of part of the work by Zhu, and Dong, Li and
Mason in a Tannakian setting. By Theorem 8.1 in [33], see also Theorem 3.2 in [35],
[117], every simple admissible is ordinary and V admits only finitely many inequivalent
simple ordinary modules. Thus V is a rational vertex operator algebra in the sense of
[197]. We then apply Theorems 2.1.2, 2.2.1, 2.2.2, and 2.2.3 in [197]. These results say
that A(V ) is associative and finite dimensional semi-simple under the assumptions of the
previous theorem, and that F induces a linear equivalence of semisimple categories between
the category of finite-dimensional A(V ) modules and the category of ordinary V -modules.
Moreover an inverse equivalence is explicitly described in [197] and [33]. It should also
be noted that the functor F may be described intrinsically, i.e. without resorting to an
irreducible decomposition, by Prop. 5.4 in [33].
