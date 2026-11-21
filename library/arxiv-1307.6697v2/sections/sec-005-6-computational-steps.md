---
doc_id: arxiv-1307.6697v2
doc_title: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS"
section_id: sec-005-6-computational-steps
section_title: "Computational steps"
section_number: 6
pages: 12-16
source_pdf: 1307.6697v2.pdf
source_sha256: a3afaefdaebe0292
toc_source: outline
doc_brief: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS — In this paper we are interested in computing representations of the funda- mental group of a 3-manifold into PGL(3, C) (in particular in PGL(2"
---
Our goal is to obtain the solutions of the system in the cross-ratio coordinates zij and
then compute the holonomy representations. We compute:
(1) Solving the constraints on gluing decorated tetrahedra, which reduces to study a
constructible set deﬁned implicitly by
(a) The consistency relations which deﬁne Edge and Face equations (4.1),
(b) The holonomy equations (see section 5),
(c) The cross-ratio equations (see 3.1),
(d) The restrictions on the coordinate values, precisely zi,j must be diﬀerent from
0 and 1.
(2) Distinguishing hyperbolic, real ﬂags and CR solutions (see 3.5.1)
(3) Computing the resulting volumes (4.2)
(4) Computing representations of the fundamental group (see section 5).
Each system depends on the 12n variables Z = {zij(T )}, where T denotes a tetrahedron in
the triangulation (containing n tetrahedra) and ij one of its oriented edges.
— Le (resp. Lf) denotes the set of the 2n edge (resp. face) equations;
— Lh denotes the set of the polynomials deﬁning the holonomy equations (their number
is 4t, where t is the number of tori in the boundary and in most cases treated here
they correspond to unipotent conditions).
— Lc denotes the polynomials deﬁning the cross-ratio relations, say zik(T )(1−zij(T ))−
1 and zil(T )zij(T ) −zij(T ) + 1;
— P0 = Q
z∈Z z(1 −z) is the polynomial deﬁning the forbidden values for the zij(T ).
13
We have to compute an exhaustive and exact description of the constructible set
S = {z ∈Z | P(z) = 0, P ∈Le ∪Lf ∪Lh ∪Lc, P0(z)̸ = 0}.
Some preliminary remarks are essential in order to understand the contents of the present
section.
For ﬁxed holonomy values (for example unipotent solutions), a straightforward approach
that would consist in ﬁrst solving the large algebraic system given by the consistency equa-
tions, the holonomy equations and the cross-ratio relation would certainly fail because of
the number of variables (12n) and the degree. Moreover it may happen that this system is
not 0-dimensional even if the holonomies are ﬁxed.
We chose to perform exclusively exact computation, using elimination techniques. We
will ﬁrst simplify the system using speciﬁc adapted pre-processing, then we will use general
methods essentially based on Gröbner basis computations (see [7]).
When the system we obtain is 0-dimensional, we then make use of the Rational Univariate
Representation ([20]) to get formal parameterizations of the solutions.
6.1. The pre-processing. Using the cross-ratio relations at each vertex of a tetrahedron
one can reduce the number of variables to 4n. We pick a variable at each vertex and write
the equations in terms of these variables. For example, such a substitution reduces the
study of the 41 knot complement to the solutions of a 0-dimensional system depending on
8 variables (instead of 24).
After these simpliﬁcations, some new simple aﬃne relations Azij + B may appear, where
A divides some power of P0, A being a product of z or (1 −z) for some z ∈Z −{zij}. The
coordinate zij may be replaced everywhere by −B/A. We then obtain a simpliﬁed system.
This simpliﬁcation pre-processing reduces the study of the 41 knot complement to a
simpliﬁed system of two equations in two variables. The other coordinates of the solutions
can then be recovered from simple relations.
Note that the degree of the equations in the ﬁnal simpliﬁed system depends strongly
on the way these simpliﬁcations are performed. Blind simpliﬁcations may lead to consider
systems of equations with very large degrees. The general methods for solving such systems
formally have polynomial complexity in the Bézout’s bound. Unappropriate choices in the
simpliﬁcations will generate huge systems that are impossible to solve with state of the art
algorithms.
We have implemented some tricky choice functions that minimize the degree of the ﬁnal
simpliﬁed system. There is no interest in describing them in detail here, but this straight-
forward step must be carefully implemented if one wants to succeed in the determination of
the solutions.
6.2. Solving the reduced system using Gröbner Basis. We now have to solve a system
of equations and (simple) inequalities. In the case of systems with ﬁxed holonomy values
(for example unipotent solutions), three cases may occur:
— The set of equations deﬁnes a 0-dimensional variety (ﬁnite set of points);
— The set of equations deﬁnes a variety of positive dimension but the full constructible
set is 0-dimensional (consider for example the system {X(XY −1) = 0, X(X2+Y 2−
1) = 0} and the constructible set {X(XY −1) = 0, X(X2 + Y 2 −1) = 0, X̸ = 0}).
— The constructible set has positive dimension.
14
E. FALBEL, P.-V. KOSELEFF AND F. ROUILLIER
In the case of unipotent solutions for problems with 2 or 3 tetrahedra, the ﬁrst case happened
only for the m004 variety (41 complement), the last case occurs for example for the m003
variety (41-sister) and also for the m006. The second case occurs for example for the m007
and the m015 (52 complement). The procedure we follow is divided into the following steps:
(1) Compute a Gröbner basis of the reduced system of equations.
(2) Saturate the ideal by the polynomials deﬁning the inequalities.
(3) Compute the dimension of this ideal.
These computations are based on Gröbner Basis computations.
A Gröbner basis of a polynomial ideal I is a set of generators of I, such that there is a
natural and unique way (the normal form) of reducing canonically a polynomial P (mod I).
A Gröbner basis is uniquely deﬁned for a given admissible ordering on the monomials. Given
I ⊂Q[Y1, . . . , Yk][X1, . . . , Xm], the use of an elimination ordering such that Yi < Xj for all
i, j, allows to deduce straightforwardly a Gröbner basis of I ∩Q[Y1, . . . , Yk] and therefore to
eliminate X1, . . . , Xm. (see [7, Ch. 3]).
We obtain the saturation of the ideal I ⊂Q[X1, . . . , Xm] by a polynomial P0 by computing
a Gröbner basis of

I+⟨T P0 −1⟩

∩Q[X1, . . . , Xm], where T is a new independent variable.
This is the usual way for computing an ideal whose zeroes set is the Zariski closure of a
given constructible set (the constructible set itself when it is 0-dimensional).
Even if the basic principles used for computing a Gröbner basis are simple (see [7] for a
general description), their eﬀective computation is known to be hard. The ﬁrst algorithm
due to Buchberger has been a lot improved and we use, in practice, the algorithm F4 by J.-
C. Faugère (see [13]), implemented in recent versions of Maple, and known to be currently
the fastest variant.
Once a Gröbner Basis of I is known, one can compute the associated Hilbert polynomial
and then deduce the (Hilbert) dimension and the (Hilbert) degree of I (see [7] Chapter 9 -
Section 3).
6.3. Prime decompositions. In general, the ideal generated by the equations as well as
its saturation by the inequalities is not prime. When it is of positive dimension, it has
components of mixed dimensions. A key point at this stage is to be able to compute a
prime or at least a primary decomposition.
There are several existing strategies for computing such a decomposition and it would be
too long to enumerate them in the present article. One can mention two classes: methods
based on Gröbner bases with an elimination ordering and factorization (see [7] - chapter 7)
and those based on triangular sets (see [1] for example). Note however that the Maple func-
tion we use for this operation implements heuristics in order to select a favorable strategy.
6.4. Rational Univariate Representation. When a system is 0-dimensional, the so
called Rational Univariate Representation (see [20]) deﬁnes a one-to-one correspondence
between the solutions and the roots of some univariate polynomial f, preserving the mul-
tiplicities.
If this systems depends on m variables X1, . . . , Xm, the Rational Univariate
Representation consists in a polynomial f ∈Q[Y ] and a set of m + 1 polynomials such that
the solutions are
{xi = fi(γ)
f0(γ), i = 1, . . . , m | f(γ) = 0}.
15
The algorithm is based on the fact that, when I is 0-dimensional, V = Q[X1, . . . , Xm]/I
is a ﬁnite dimensional Q-algebra generated by the monomials that are irreducible modulo
I. These elements than can be directly obtained from a Gröbner basis.
There exists a linear combination Y = Pm
i=1 λiXi ∈V which separates the zeroes of I.
Then f is the characteristic polynomial of the map V →V , P 7→Y · P.
The polynomials f, fi, i = 0, . . . , m are then computed by linear algebra.
This full parametrization is computed in two steps: ﬁrst compute a suitable set of gen-
erators for the ideal (the best being a Gröbner basis), then compute a Rational Univariate
Representation of the reduced 0-dimensional system.
Factorization of f leads to consider that the solutions are parameterized by a ﬁnite number
of algebraic numbers γ, deﬁned by their minimal polynomials f and each coordinate z is a
polynomial fz(γ).
Then, we substitute the variables that have been extracted during the pre-processing by
their expression in Q(γ) = Q[Y ]/(f) using modular computation. We obtain a rational
parametrization of the full system. Each of these parametrization may be described as
rur := {z = fz(γ), z ∈Z | f(γ) = 0}.
Furthermore, γ ∈R if an only if z(γ) = fz(γ) ∈R for all z ∈Z.
6.5. Sorting the solutions. In this section we explain an exact procedure to sort solutions
in SL(3, R), PGL(2, C) and PU(2, 1) for 0-dimensional components. Thanks to the previ-
ous computations, the solutions of the initial system are expressed by means of rational
parameterizations (here f is a prime polynomial)
rur := {z = fz(Y ), z ∈Z | f(Y ) = 0}.
(1) Real solutions are in correspondence with the real zeroes of f. The number of real
roots can be determined exactly by Sturm algorithms and their approximate values
are computed by certiﬁed algorithms (see )
(2) The hyperbolic solutions are extracted from the global solutions as follows. Equation
3.3.1 becomes
z12 ≡z21 ≡z34 ≡z43 (mod f).
From the Rational Univariate Representation it is just a matter of testing if some
formal coordinates are equal in a ﬁeld extension.
(3) For the CR solutions, we consider the 3 × n equations 3.5.1:
zijzji = zkl zlk.
Let γ = x + iy be one of the root of f. We obtain a new 0-dimensional system in
Q[x, y] consisting of the 2 polynomial equations: Re f(γ) = 0, Im f(γ) = 0 and the
2 × 3n equations:
Re [zij(γ)zji(γ)] = Re [zkl(γ) zlk(γ)] , Im [zij(γ)zji(γ)] = −Im [zkl(γ) zlk(γ)] .
This last system may be solved by computing a Rational Univariate Representation.
There exists an integer λ such that the algebraic number η = x + λy describes the
solutions:
rurCR :=

x = gx(η)
g1(η) , y = gy(η)
g1(η) | g(η) = 0

.
16
E. FALBEL, P.-V. KOSELEFF AND F. ROUILLIER
Real solutions of the system are in a one-to-one correspondance with the real roots
of g.
6.6. Computing the rank of the boundary holonomy representation. We compute
ﬁrst the meridian and the longitude as upper triangular matrices, say
gM =


1
a
c
0
1
b
0
0
1

,
gL =


1
a′
c′
0
1
b′
0
0
1

.
We easily obtain that gn
M =


1
n a
n c + 1
2n(n −1)ab
0
1
n b
0
0
1

. We thus deduce that gn
M = gn′
L
iﬀa
a′ = b
b′ =
2c −ab
2c′ −a′b′ = n′
n ∈Q. This can be decided by computing ﬁrst the reduced
row echelon form of


a
a′
b
b′
2c −ab
2c′ −a′b′

in the ground ﬁeld Q[Y ]/(f(Y )) where f is the
minimal irreducible polynomial parameterizing the solutions. If the reduced row echelon
form has rank one, we test if a and a′ are Q-dependant or not.
6.7. Certiﬁed numerical approximations. For simplicity, and in order to get a human
readable output, we often express the results by means of numerical approximations instead
of formal (large) expressions.
We assert that all these approximations are certiﬁed (in
practice, all the digits are correct but the last one). We make use of multi-precision ﬂoating
point numbers coupled with interval arithmetic or well known results on error control for
the evaluation of univariate polynomials that allows to accurately evaluate the Rational
Univariate Representations at the roots of a given univariate polynomial. A fully treated
example in the case of systems with two variables is described in [4].
