---
doc_id: hyperbolicandneumann
doc_title: "HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP"
section_id: sec-005-6-connections-to-number-theory
section_title: "Connections to number theory"
section_number: 6
pages: 12-17
source_pdf: HyperbolicAndNeumann.pdf
source_sha256: 3d66fe4c64bdc62b
toc_source: outline
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
duplicate_of: "arxiv-2304.12545v1"
---
The paper [31] and its sequel [28] suggested or led to several interesting developments in
pure number theory as well as in topology. In this ﬁnal section we describe of a few of these.
Values of Dedekind zeta functions and higher Bloch groups
An important subclass of hyperbolic manifolds M = H3/Γ are the arithmetic ones, where Γ
is either the Bianchi group SL2(OF) for some imaginary quadratic ﬁeld F or more generally
a group of units in a quaternion algebra over a number ﬁeld F of higher degree n = r1 + 2
having only one complex embedding up to complex conjugation. In both cases, classical
results (proved in the ﬁrst case by Humbert already in 1919) say that the volume of M is
a simple multiple (a power of π times the square-root of the discriminant) of the value at
s = 2 of the Dedekind zeta function ζF(s) of the ﬁeld F. An immediate consequence of this
and of the volume formulas discussed in Section 2 is that this zeta value is a multiple of a
linear combination of values of the Bloch-Wigner dilogarithm at algebraic arguments. This
consequence was observed in [35] and was also generalized there to the value of ζF(2) for
HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF WALTER NEUMANN
13
arbitrary number ﬁelds F, with [F : Q] = r1+2r2 for any value of r2 ≥1. (If r2 = 0, then the
well-known Klingen-Siegel theorem asserts that ζF(2) is a rational multiple of π2r1√DF .)
Now the group SL2(OF) acts as a discrete group of isometries of (H2)r1 × (H3)r2 with a
quotient of ﬁnite volume, and there are also quaternionic groups Γ over F that acts freely and
discretely on (H3)r2, the volume of the quotient in both cases being an elementary multiple
of ζF(2). This gives a “poly-3-hyperbolic” manifold M = (H3)r2/Γ with volume proportional
to ζF(2). A rather amusing lemma says that any such manifold has a decomposition (disjoint
except for the boundaries) into ﬁnitely many r2-fold products of hyperbolic tetrahedra, and
it follows that ζF(2) for any number ﬁeld has an expression as a linear combination of r2-fold
products of values of D(z) at algebraic arguments, generalizing the Klingen-Siegel theorem
in an unexpected way.
The connection with 3-dimensional hyperbolic geometry applies only to the values of
Dedekind zeta functions at s = 2, but suggested that there might be similar statements for
ζF(m) with m > 2 in terms of the mth polylogarithm function Lim(z). Extensive numerical
experiments led to a concrete conjecture saying that this is the case and also to a deﬁnition
(originally highly speculative, but now supported by more theory) of “higher Bloch groups”
Bm(F) that should be isomorphic after tensoring with Q to the higher algebraic K-groups
K2m−1(F) and should express the Borel regulator in terms of polylogarithms. (For a survey,
see [38].) This conjecture, now over 30 years old, has been studied extensively by Beilinson,
Deligne, de Jeu, Goncharov, Rudenko and others, with the cases m = 3 and m = 4 now
being essentially settled.
Units in cyclotomic extensions of number ﬁelds
As already mentioned in the last section, the analysis of the Kashaev invariant and the
modular generalization of the Volume Conjecture discussed below led to the deﬁnition of
certain power series ΦK
α (h) associated to a hyperbolic knot and a number α ∈Q/Z that can
be computed numerically in any given case. Extensive numerical computations for simple
knots and simple rational numbers α suggested that this power series not only has algebraic
coeﬃcients, but that (up to a root of a unity and the square-root of a number in the trace
ﬁeld FK of the knot independent of α) its nth power belongs to FK,n[[h]], where n is the
denominator of α and FK,n = FK(e2πiα) the nth cyclotomic extension of FK. Equivalently,
ΦK
α (h) itself is the product of a power series in FK,n[[h]] with the nth root of an element of
F ×
K,n. Moreover, in each case studied the latter factor turned out to be the nth root of a
unit, and not just a non-zero number, of FK,n, and in the case of “sister knots” (like 52 and
the (−2, 3, 7)-pretzel knot) having the same Bloch group class were the same for both knots,
even though the rest of the power series were completely diﬀerent. This led us, together
with Frank Calegari, to conjecture and later to prove [2], that there was a canonical class of
elements in cyclotomic extensions of arbitrary number ﬁelds associated to elements of their
Bloch groups, whether or not the ﬁelds arise from topology. Explicitly, to any number ﬁeld F
and any element ξ of the Bloch group of F one can associate canonically deﬁned elements
of U(Fn)/U(Fn)n for every n, where U(Fn) denotes the group of units (more precisely, of
S-units for some S depending on ξ but independent of n) of the nth cyclotomic extension Fn
of F. Actually, two quite diﬀerent constructions were given, one in terms of an element
of B(F) and one in terms of an element in K3(F), and work in progress announced in [2]
14
STAVROS GAROUFALIDIS AND DON ZAGIER
suggests that there will be a generalization to Bm(F) and K2m−1(F) for any m > 2. The
construction in terms of the Bloch group is quite simple, although the proof that it gives
units and is independent (up to nth powers) of all choices is long: if ξ is represented by
P[zi] ∈Z[F], then the number Q Dζ(z1/n
i
) is the product of an nth power in Fn with an
S-unit, and this is the unit we are looking for. Here ζ is a primitive nth root of unity and
Dζ(x) = Qn−1
k=1(1 −ζkx)k is the “cyclic quantum dilogarithm” function, which by a result
of Kashaev, Mangazeev and Stroganov satisﬁes an analogue of the 5-term relation of the
classical dilogarithm.
q-series and Nahm’s conjecture
An unexpected consequence of the work on units just described was a proof of one direc-
tion of a conjecture by the mathematical physicist Werner Nahm that had predicted an
extremely surprising connection between the Bloch group and the modularity of certain
q-hypergeometric series. The simplest case of such a “Nahm sum” is the inﬁnite series
Fa,b,c(q) =
∞
X
n=0
q
1
2 an2+bn+c
(q)n
(a, b, c ∈Q, a > 0),
(15)
where (q)n = (1 −q)(1 −q2) · · · (1 −qn) is the so-called quantum factorial. This function
is known to be modular (in τ, where q = e2πiτ) when (a, b, c) is (2, 0, −1
60) or (2, 1, 11
60) by
the famous Rogers-Ramanujan identities and in a handful of other cases by classical results
of Euler, Gauss and others.
It is very rare that a q-hypergeometric series (meaning an
inﬁnite sum whose adjacent terms diﬀer by ﬁxed rational functions of q and qn) is at the
same time a modular function, and in fact for the special series (15) this happens only for
seven triples (a, b, c), as predicted by Nahm’s conjecture and proved in [36]. Nahm raised
the general question when a (multi-dimensional) q-hypergeometric series can be modular
and, motivated by examples coming from characters of vertex operator algebras, discovered
a possible answer in terms of the Bloch group. Concretely, he generalized (16) to
Fa,b,c(q) =
X
n1,...,nN≥0
q
1
2 ntan + btn + c
(q)n1 · · · (q)nN
(16)
for any N ≥1, where a is now a positive deﬁnite symmetric N × N matrix with rational
coeﬃcients, b a vector in QN, and c a rational number. There is still no complete “if and
only if” conjecture predicting exactly when these Nahm sums are modular functions, but
Nahm gave a precise conjecture for a necessary condition and a partial conjecture for the
suﬃciency. It is the ﬁrst part that was proved in [2], while the correct formulation and proof
of the converse direction is still an active research subject.
The modularity criterium that Nahm found depended on his observation that for any
solution (z1, . . . , zN) of the system of equations
1 −zi =
N
Y
j=1
z
aij
j
(i = 1, . . . , N) ,
(17)
the element [z1] + · · · + [zN] of Z[C] belongs to B(C). This is a direct consequence of the
symmetry of a, because P
i(zi) ∧(1 −zi) = P
i,j aij (zi) ∧(zj) = 0.
(This is the same
HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF WALTER NEUMANN
15
argument as was used in Section 4 for the corresponding statement for the Neumann-Zagier
equations, and applies more generally to all half-symplectic matrices, as discussed below.)
The “only if” direction of Nahm’s conjecture then says that Fa,b,c(q) can be modular only
if this element of the Bloch group vanishes for the unique solution of the Nahm equation
having all zi ∈(0, 1). The proof, given in [2], uses both the results there about the units
coming from Bloch elements as described above and an asymptotic analysis of Nahm sums
near roots of unity published separately by the two of us.
Half-symplectic matrices and the Bloch group
At the end of Section 4, we saw how the NZ equations lead to a “half-symplectic matrix,”
meaning the upper half H = (A B) of a 2N × 2N symplectic matrix ( A B
C D ) over Z. To any
such matrix we associate the system of polynomial equations
N
Y
j=1
z
Aij
j
= (−1)(ABt)ii
N
Y
j=1
(1 −zj)Bij
(i = 1, . . . , N) .
(18)
This is a straight generalization of the original NZ equations in the topological setting except
possibly for the sign, but we checked in thousands of examples using Snappy [5] that this
is the right sign, and this could presumably be proved using the “parity condition” in [28].
Another special case of (18) is the Nahm equation (17), at least when the matrix a is integral
and even, the half-symplectic matrix then being (1 a) and the full symplectic matrix ( 1 a
0 1 ).
For any solution z of (18), the element 2 PN
j=1[zj] belongs to the usual Bloch group by
the same argument as was used for Nahm sums. We can in fact divide by 2 and lift to an
element [H, z] of the extended Bloch group by setting
[H, z] =
N
X
j=1
[uj, vj] + [ξ, ξ′] + [−ξ, ξ′ −ξ + πi] ,
(19)
where uj and vj are arbitrary choices of logarithms of zj and 1−zj, respectively, ξ is deﬁned
as 1
π (Au−Bv)t(Cu−Dv) for any completion (C D) of H to a full symplectic matrix, and ξ′
is any choice of logarithm of 1 −eξ. The facts that this is in the kernel of d : Z[bC] →Λ2(C)
and that its image modulo extended 5-term relations is independent of all choices (at least
modulo 8-torsion the Bloch group of the ﬁeld generated by the z’s) can be checked by direct
computations which are sketched in Section 6.1 of [19], together with a more precise form
that eliminates the torsion ambiguity.
We have the ﬁve following equivalence relations among pairs, each motivated by a change
of the choices made in the topological situation, that do not change this class:
• Stability: increase N by N + 1, replace A and B in H = (A B) by their direct sums
with (1) and (0), respectively, and set zN+1 = 1, corresponding in the topological
case to adding a degenerate simplex to a 3-manifold triangulation.
• Changing the equations: multiply H on the left by an element of GLN(Z) without
changing the z’s. This corresponds to replacing the N relations (18) by multiplicative
combinations of them in an invertible way.
16
STAVROS GAROUFALIDIS AND DON ZAGIER
• Renumbering: multiply H on the right by an N×N permutation matrix, and permute
the zj’s by the same matrix, corresponding to a renumbering of the simplices of a
triangulation.
• New shape parameters: for each j = 1, . . . , N, multiply the N × 2 matrix (Aj Bj)
(where Aj and Bj denote the jth columns of A and B, respectively) by a power
of the element
 0 −1
1 −1

of order 3 in SL2(Z), and replace zj correspondingly by zj,
z′
j = 1/(1 −zj), or z′′
j = 1/(1 −zj).
• Algebraic 2–3 Pachner moves: remove two columns of A and the same two columns
of B and replace them by 3 new columns that are speciﬁc Z-linear combinations,
simultaneously replacing N by N + 1 and changing two of the zj to three others in
such a way that the corresponding change of [H, z] is a 5-term relation. The explicit
formulas were ﬁrst written down in the special case corresponding to the Nahm
sums (16) by Sander Zwegers in an unpublished 2011 conference talk and were then
given for abritrary symplectic matrices in Equation (3-27) of [9]. This corresponds
to stabilizing H three times and then multiplying it on the left by a speciﬁc element
of Sp10(Z), and then unstabilizing three times.
This gives us a new abelian group that maps to the extended Bloch group, namely the set
of all pairs (H, z) as above modulo these equivalence relations, with addition given by direct
sum. In fact this map is an isomorphism, meaning that any element of the Bloch group
can be realized by some half-symplectic matrix and solution of the coresponding generalized
Neumann-Zagier equations and that any 5-term relation can be lifted to one coming from an
algebraic 2–3 Pachner move. A more complete discussion is given in Section 6.1 of [19] (full
details will be given later), while Section 6.3 of the same paper shows how to attach Nahm
sum-like q-series to arbitrary half-symplectic matrices.
From the Kashaev invariant to quantum modular forms
Nahm’s conjecture already highlighted a connection between half-symplectic matrices and
questions of modularity, but there are other and more direct connections between hyperbolic
3-manifolds and the modular group SL2(Z) that we now describe.
At the end of Section 5 we discussed Kashaev’s volume conjecture and its reﬁnement (13).
That statement in turn was generalized in [37] on the basis of numerical computations to a
conjectural asymptotic formula having a strong modular ﬂavor. To state it, we ﬁrst note that
the Kashaev invariant ⟨K⟩n of a knot K can be generalized to a function JK : Q/Z →Q
whose value at −1/n for any n ≥1 is ⟨K⟩n and which is Gal(Q/Q)-equivariant. Then the
conjectural generalization of (13) is the statement that
JKan + b
cn + d

∼(cn + d)3/2 eVolC(K)(n+d/c)/2πi ΦK
a/c

2πi
c(cn + d)

JK(n)
(20)
for every matrix
 a b
c d

∈SL2(Z) as n tends to inﬁnity through either integers or rational
numbers with bounded denominator, with (13) being the special case when
 a b
c d

=
 0 −1
1
0

and n is integral. Here ΦK
α (h) for α ∈Q/Z is a power series that is conjectured to be the
one constructed in [10] and discussed at the end of Section 5.
HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF WALTER NEUMANN
17
In [19], this modularity conjecture was veriﬁed experimentally for a few knots to many
terms and to a high degree of precision, and was also successively reﬁned in several diﬀer-
ent directions, the ﬁnal statement being the existence of a whole matrix JK of Q-valued
functions on Q/Z (generalized Kashaev invariants) which conjecturally has much better
modularity properties than the original scalar function JK. Explicitly, (20) lifts to a sim-
ilar statement with JK replaced by the matrix JK and the completed formal power series
bΦK
a/c(h) = eVolC(K)/2πic2h ΦK
a/c(h) by a matrix bΦK
a/c(h) of completed formal power series act-
ing by right multiplication. The rows and columns of these matrices are indexed by the
bounded parabolic ﬂat connections, or equivalently by an index 0 (trivial connection) and
indices 1, . . . , r corresponding to the solutions of the NZ equation for a triangulation of the
knot complement, with the original scalar-valued functions JK and ΦK being the (0, 1) and
(1, 1) entries of JK and ΦK, respectively. The really new aspect is that, by replacing the
original scalar functions by matrices, we obtain a matrix of completed formal power series
in h that (conjecturally, like everything else in this story) extend to real-analytic functions
on the positive and negative real line and in fact to holomorphic functions on the two cut
planes C ∖(−∞, 0] and C ∖[0, ∞). This discovery, which arises through the possibility of
associating matrix-valued q-series to the knot [18], gives rise to the new concept of “holomor-
phic quantum modular form” that then turned out to appear also in many other situations,
including various known modular objects like mock modular forms or Eisenstein series of
odd weight on the full modular group.
Finally, we mention that the new generalized Kashaev invariants have beautiful arithmetic
properties generalizing the known property [22] that the original Kashaev invariant belongs
to the so-called Habiro ring H = lim
←−Z[q]/(q)n . The results of [19] and [18] suggest that
there should be a Habiro ring HF associated to any number ﬁeld F in which the generalized
Kashaev invariants take their values and which is graded by the Bloch group of F. (The
latter property is invisible in the classical case since B(Q) ⊗Q = {0}.) We are currently
working on this jointly with Peter Scholze, and already have a candidate for HF, as well as a
partial lifting of the algebraic units of [2] to formal power series with Habiro-like properties.
