---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-004-bracket-and-jones-polynomials
section_title: "Bracket and Jones polynomials"
section_number: null
pages: 8-11
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Bracket and Jones polynomials
Skein relation and Hecke algebras allow to compute Markov traces diagrammatically, without explicitly
defining matrix representations [45]. Recall that we agreed to substitute any disconnected circle by the
8
number d = −A2 −A−2. First, one can check that the diagrammatic closure of a braid has the Markov
property. Applying the skein relation one finds that
βn
= A
βn
+ A−1
βn
= −A−3
βn
.
(29)
Note that we are not simply using the I Reidemeister move here, but rather the algebraic properties of
braids. It is therefore not so trivial to conclude that the second diagram in the first line is equivalent to
the diagram in the second line. It might be intuitively clear to those familiar with tensor algebras and
Feynman diagrams.
Note also that the initial and final diagrams differ by an overall numerical factor, which means that
the Markov property is only satisfied up to this factor. This factor has a special meaning and the next
few paragraphs will be dedicated to explaining it, although, skein relations can be rescaled to eliminate
it from the trace.
The discrepancy is related to the intrinsic nonplanarity of the knot and to its attribute called framing.
In general, framing is a rule to introduce an orthogonal vector to a curve at each point. The endpoint of
this vector is transported along the curve and defines a satellite curve that may arbitrarily wind around
its parent curve. In a planar projection this winding (which is nothing but the Gauss’ linking number of
the satellite and the parent curve) is split into the sum of two components, twist and writhe, according
to the theorem introduced by Gheorghe Calugareanu (Calugareanu-Fuller-White theorem) [49–52].
While the twist is a single naive winding of one curve around the other – it appears as a pair of
braidings – the writhe is the number of loops, like the one in the first diagram of (29), that the parent
loop has. Calugareanu’s theorem states that, for a chosen framing, the sum of the twist and the writhe
is a topological invariant.
Unmaking the loop in the I Reidemeister move removes a unit of writhe,
therefore, assuming that the first and the last diagrams above have the same twist number, the prefactor
introduces a compensating factor indicating how much the framing changes in passing from one diagram
to another. In all the computations the framing factor will appear as (−A3)w, where w is the writhe
number. Altogether, one says that what is being computed is an invariant of framed knots.
Skein relations can be used to “resolve” all crossings in the braid diagram, so that its closure is reduced
to a weighted sum of collections of embedded nonintersecting circles, where weights are polynomial
functions of A. At the final step of the calculation every circle can be replaced by d, according to our
prescription, giving a Laurent polynomial of A as a final result. This is the bracket polynomial introduced
by Louis Kauffman, which is an invariant of framed knots [9].
Our faithfulness assumption allows not only application of the skein relation to braids, but directly to
arbitrary diagrams. Figure 1 shows a sequence of skein relations applied to the trefoil knot and computing
their invariants without casting the knots as braid closures. For the trefoil knot one gets the following
bracket polynomial:
*
+
= (−A3)3(−A2 −A−2)(A−4 + A−12 −A−16).
(30)
9
=
+
A
A-1
=
+
A2
+
+A-2
+
A3
+
(2-A-2(A2+A-2))
=
A
(
+
)
A-1
A
Figure 1: Calculation of the bracket polynomial of the trefoil knot 31 using skein relations (25).
One can see in this example the appearance of three units of the writhe factor and another overall factor
of d. This is the general structure obtained by applying the skein relations. To get the original definition
of Kauffman one divides the result by d. In such a normalization the invariant of the unknot is unity up
to the writhe. The remaining term has a simple relation to the polynomial obtained originally by Jones:
• Remove the writhe and the d factors
• Substitute A4 →q−1
One then gets the following Jones polynomial of the trefoil knot:
V





= q + q3 −q4 .
(31)
Note that there are two trefoil knots differing by mirror reflection. If one applies the skein procedure
to the mirror-reflected knot one will get
V





= q−1 + q−3 −q−4 .
(32)
In other words, mirror reflection acts as q →q−1 (A →A−1) on Jones (bracket) polynomials.
In the rest of this review we will work with the Kauffman bracket version of the Jones polynomial. The
whole purpose of section 2 is to explain what knot is and how the bracket polynomial can be computed,
for example, using the skein relation. We will need this calculus for quantum mechanical applications.
Let us summarize the main steps:
• Draw the knot (link) diagram;
• Choose a crossing, apply the skein relation by replacing the diagram by a pair of new diagrams
with the crossing modified according to skein relation (25);
• Repeat the procedure for the next crossing for each of the generated diagrams until the diagrams
are nothing but a collection of nested nonintersecting circles;
• replace each circle by factor d = −A2 −A−2.
10
