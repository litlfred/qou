---
doc_id: celebratio-mathematica-neumann-hyperbolic-3-manifolds
doc_title: "Jump to Bibliography by Stavros Garoufalidis and Don Zagier Published: 2023"
section_id: sec-005-6-connections-to-number-theory
section_title: "Connections to number theory"
section_number: 6
pages: 16-23
source_pdf: Celebratio Mathematica — Neumann — Hyperbolic 3-Manifolds.pdf
source_sha256: 9e541693c60cbd3f
toc_source: inferred
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
duplicate_of: "arxiv-2304.12545v1"
---
The paper [1] and its sequel [2] suggested or led to several interesting develop‐
ments in pure number theory as well as in topology. In this final section we de‐
scribe of a few of these.
Values of Dedekind zeta functions and higher Bloch groups
⇧
An important subclass of hyperbolic manifolds 
 are the arithmetic
ones, where  is either the Bianchi group 
 for some imaginary quadratic
field  or more generally a group of units in a quaternion algebra over a number
field 
 of higher degree 
 having only one complex embedding up to
complex conjugation. In both cases, classical results (proved in the first case by
Humbert already in 1919) say that the volume of  
 is a simple multiple (a power
of  times the square-root of the discriminant) of the value at 
 of the Dede‐
kind zeta function 
 of the field  . An immediate consequence of this and of
the volume formulas discussed in Section 2 is that this zeta value is a multiple of a
linear combination of values of the Bloch–Wigner dilogarithm at algebraic argu‐
ments. This consequence was observed in [e3] and was also generalized there to
the value of 
 for arbitrary number fields  , with 
 for any
value of 
. (If 
, then the well-known Klingen–Siegel theorem asserts
that 
 is a rational multiple of 
.) Now the group 
 acts as a
discrete group of isometries of 
 with a quotient of finite volume,
and there are also quaternionic groups  over 
 that act freely and discretely on 
, the volume of the quotient in both cases being an elementary multiple of 
. This gives a “poly-3-hyperbolic” manifold 
 with volume
proportional to 
. A rather amusing lemma says that any such manifold has a
decomposition (disjoint except for the boundaries) into finitely many 
-fold
products of hyperbolic tetrahedra, and it follows that 
 for any number field
has an expression as a linear combination of 
-fold products of values of 
 at
algebraic arguments, generalizing the Klingen–Siegel theorem in an unexpected
way.
The connection with 3-dimensional hyperbolic geometry applies only to the val‐
ues of Dedekind zeta functions at 
, but suggested that there might be similar
statements for 
 with 
 in terms of the 
-th polylogarithm function 
. Extensive numerical experiments led to a concrete conjecture saying that
this is the case and also to a definition (originally highly speculative, but now sup‐
ported by more theory) of “higher Bloch groups” 
 that should be iso‐
morphic after tensoring with 
 to the higher algebraic 
-groups 
 and
should express the Borel regulator in terms of polylogarithms. (For a survey, see
[e9].) This conjecture, now over 30 years old, has been studied extensively by Beil‐
inson, Deligne, de  Jeu, Goncharov, Rudenko and others, with the cases 
and 
 now being essentially settled.
Units in cyclotomic extensions of number fields
As already mentioned in the last section, the analysis of the Kashaev invariant and
the modular generalization of the Volume Conjecture discussed below led to the
definition of certain power series 
 associated to a hyperbolic knot and a
⇧
number 
 that can be computed numerically in any given case. Extensive
numerical computations for simple knots and simple rational numbers  sugges‐
ted that this power series not only has algebraic coefficients, but that (up to a root
of a unity and the square-root of a number in the trace field 
 of the knot inde‐
pendent of  ) its -th power belongs to 
, where  is the denominator of 
and 
 the -th cyclotomic extension of 
. Equivalently, 
itself is the product of a power series in 
 with the -th root of an element
of 
. Moreover, in each case studied the latter factor turned out to be the -th
root of a unit, and not just a nonzero number, of 
, and the “sister knots” (like 
 and the 
-pretzel knot) having the same Bloch group class were the
same for both knots, even though the rest of the power series were completely dif‐
ferent. This led us, together with Frank Calegari, to conjecture and later to prove
[e35] that there was a canonical class of elements in cyclotomic extensions of arbit‐
rary number fields associated to elements of their Bloch groups, whether or not
the fields arise from topology. Explicitly, to any number field  and any element 
of the Bloch group of 
 one can associate canonically defined elements of
 for every  , where 
 denotes the group of units (more pre‐
cisely, of -units for some  depending on  but independent of  ) of the -th
cyclotomic extension 
 of 
. Actually, two quite different constructions were
given, one in terms of an element of 
 and one in terms of an element in 
, and work in progress announced in [e35] suggests that there will be a gen‐
eralization to 
 and 
 for any 
. The construction in terms of
the Bloch group is quite simple, although the proof that it gives units and is inde‐
pendent (up to 
-th powers) of all choices is long: if  is represented by
, then the number 
 is the product of an -th power in 
with an -unit, and this is the unit we are looking for. Here  is a primitive -th
root of unity and
is the “cyclic quantum dilogarithm” function, which by a result of Kashaev,
Mangazeev and Stroganov satisfies an analogue of the five-term relation of the
classical dilogarithm.
-series and Nahm’s conjecture
An unexpected consequence of the work on units just described was a proof of
one direction of a conjecture by the mathematical physicist Werner Nahm that
had predicted an extremely surprising connection between the Bloch group and
the modularity of certain -hypergeometric series. The simplest case of such a
⇧
“Nahm sum” is the infinite series
where
is the so-called quantum factorial. This function is known to be modular (in  ,
where 
) when 
 is 
 or 
 by the famous Rogers–
Ramanujan identities and in a handful of other cases by classical results of Euler,
Gauss and others. It is very rare that a -hypergeometric series (meaning an infin‐
ite sum whose adjacent terms differ by fixed rational functions of  and 
) is at
the same time a modular function, and in fact for the special series (15) this hap‐
pens only for seven triples 
, as predicted by Nahm’s conjecture and proved
in [e14]. Nahm raised the general question when a (multidimensional) -hyper‐
geometric series can be modular and, motivated by examples coming from charac‐
ters of vertex operator algebras, discovered a possible answer in terms of the Bloch
group. Concretely, he generalized (16) to
for any 
, where  is now a positive definite symmetric 
 matrix with
rational coefficients,  a vector in 
, and  a rational number. There is still no
complete “if and only if” conjecture predicting exactly when these Nahm sums are
modular functions, but Nahm gave a precise conjecture for a necessary condition
and a partial conjecture for the sufficiency. It is the first part that was proved in
[e35] while the correct formulation and proof of the converse direction is still an
active research subject.
The modularity criterion that Nahm found depended on his observation that for
any solution 
 of the system of equations
the element 
 of 
 belongs to 
. This is a direct con‐
sequence of the symmetry of  , because
⇧
(This is the same argument as was used in Section 4 for the corresponding state‐
ment for the Neumann–Zagier equations, and applies more generally to all half-
symplectic matrices, as discussed below.) The “only if” direction of Nahm’s con‐
jecture then says that 
 can be modular only if this element of the Bloch
group vanishes for the unique solution of the Nahm equation having all
. The proof, given in [e35] uses both the results there about the units
coming from Bloch elements as described above and an asymptotic analysis of
Nahm sums near roots of unity published separately by the two of us.
Half-symplectic matrices and the Bloch group
At the end of Section 4, we saw how the NZ equations lead to a “half-symplectic
matrix,” meaning the upper half 
 of a 
 symplectic matrix
over  . To any such matrix we associate the system of polynomial equations
This is a straight generalization of the original NZ equations in the topological
setting except possibly for the sign, but we checked in thousands of examples us‐
ing SnapPy [e24] that this is the right sign, and this could presumably be proved
using the “parity condition” in [2]. Another special case of (18) is the Nahm equa‐
tion (17), at least when the matrix  is integral and even, the half-symplectic mat‐
rix then being 
 and the full symplectic matrix
For any solution  of  (18), the element 
 belongs to the usual Bloch
group by the same argument as was used for Nahm sums. We can in fact divide
by 2 and lift to an element 
 of the extended Bloch group by setting
where 
 and 
 are arbitrary choices of logarithms of 
 and 
, respectively, 
is defined as
⇧
for any completion 
of 
 to a full symplectic matrix, and  is any choice of
logarithm of 
. The facts that this is in the kernel of 
 and
that its image modulo extended five-term relations is independent of all choices
(at least modulo 8-torsion in the Bloch group of the field generated by the  ’s) can
be checked by direct computations which are sketched in Section 6.1 of [e33], to‐
gether with a more precise form that eliminates the torsion ambiguity.
We have the five following equivalence relations among pairs, each motivated by a
change of the choices made in the topological situation, that do not change this
class:
⇧
Stability: increase 
 by 
, replace  and  in 
 by their dir‐
ect sums with 
 and 
, respectively, and set 
, corresponding in
the topological case to adding a degenerate simplex to a 3-manifold triangu‐
lation.
Changing the equations: multiply 
 on the left by an element of 
without changing the ’s. This corresponds to replacing the 
 relations (18)
by multiplicative combinations of them in an invertible way.
Renumbering: multiply 
 on the right by an 
 permutation matrix,
and permute the 
’s by the same matrix, corresponding to a renumbering of
the simplices of a triangulation.
New shape parameters: for each 
, multiply the 
 matrix
 (where 
 and 
 denote the -th columns of 
 and 
, respect‐
ively) by a power of the element
of order 3 in 
, and replace 
 correspondingly by 
, 
,
or 
.
Algebraic 2-3 Pachner moves: remove two columns of 
 and the same two
columns of 
 and replace them by three new columns that are specific -
linear combinations, simultaneously replacing 
 by 
 and changing
two of the 
 to three others in such a way that the corresponding change of
 is a five-term relation. The explicit formulas were first written down
in the special case corresponding to the Nahm sums (16) by Sander Zwegers
in an unpublished 2011 conference talk and were then given for arbitrary
symplectic matrices in equation (3-27) of [e20]. This corresponds to stabiliz‐
ing 
 three times and then multiplying it on the left by a specific element of 
, and then unstabilizing three times.
–
–
–
–
–
This gives us a new abelian group that maps to the extended Bloch group, namely
the set of all pairs 
 as above modulo these equivalence relations, with addi‐
tion given by direct sum. In fact this map is an isomorphism, meaning that any
element of the Bloch group can be realized by some half-symplectic matrix and
solution of the corresponding generalized Neumann–Zagier equations and that
any five-term relation can be lifted to one coming from an algebraic 2-3 Pachner
move. A more complete discussion is given in Section 6.1 of [e33] (full details will
be given later), while Section 6.3 of the same paper shows how to attach Nahm
sum-like -series to arbitrary half-symplectic matrices.
From the Kashaev invariant to quantum modular forms
Nahm’s conjecture already highlighted a connection between half-symplectic
matrices and questions of modularity, but there are other and more direct connec‐
tions between hyperbolic 3-manifolds and the modular group 
 that we
now describe.
At the end of Section 5 we discussed Kashaev’s volume conjecture and its refine‐
ment (13). That statement in turn was generalized in [e19] on the basis of numer‐
ical computations to a conjectural asymptotic formula having a strong modular
flavor. To state it, we first note that the Kashaev invariant 
 of a knot 
 can be
generalized to a function 
 whose value at 
 for any 
 is
 and which is 
-equivariant. Then the conjectural generalization
of (13) is the statement that
for every matrix
as  tends to infinity through either integers or rational numbers with bounded
denominator, with (13) being the special case when
and  is integral. Here 
 for 
 is a power series that is conjectured to
be the one constructed in [e31] and discussed at the end of Section 5.
In [e33], this modularity conjecture was verified experimentally for a few knots to
many terms and to a high degree of precision, and was also successively refined in
several different directions, the final statement being the existence of a whole mat‐
⇧
rix 
 of 
-valued functions on 
 (generalized Kashaev invariants), which
conjecturally has much better modularity properties than the original scalar func‐
tion 
. Explicitly, (20) lifts to a similar statement with 
 replaced by the mat‐
rix 
 and the completed formal power series
by a matrix 
 of completed formal power series acting by right multiplica‐
tion. The rows and columns of these matrices are indexed by the bounded para‐
bolic flat connections, or equivalently by an index 0 (trivial connection) and in‐
dices 
 corresponding to the solutions of the NZ equation for a triangula‐
tion of the knot complement, with the original scalar-valued functions 
 and
 being the 
 and 
 entries of 
 and 
, respectively. The really new
aspect is that, by replacing the original scalar functions by matrices, we obtain a
matrix of completed formal power series in  that (conjecturally, like everything
else in this story) extend to real-analytic functions on the positive and negative
real line and in fact to holomorphic functions on the two cut planes 
and 
. This discovery, which arises through the possibility of associating
matrix-valued -series to the knot [e34], gives rise to the new concept of “holo‐
morphic quantum modular form” that then turned out to appear also in many
other situations, including various known modular objects like mock modular
forms or Eisenstein series of odd weight on the full modular group.
Finally, we mention that the new generalized Kashaev invariants have beautiful
arithmetic properties generalizing the known property [e10] that the original
Kashaev invariant belongs to the so-called Habiro ring 
The results of [e33] and [e34] suggest that there should be a Habiro ring 
 asso‐
ciated to any number field 
 in which the generalized Kashaev invariants take
their values and which is graded by the Bloch group of 
. (The latter property is
invisible in the classical case since 
.) We are currently working
on this jointly with Peter Scholze, and already have a candidate for 
, as well as a
partial lifting of the algebraic units of [e35] to formal power series with Habiro-
like properties.
