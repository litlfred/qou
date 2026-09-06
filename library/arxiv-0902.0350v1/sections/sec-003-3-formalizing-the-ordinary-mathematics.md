---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE"
section_id: sec-003-3-formalizing-the-ordinary-mathematics
section_title: "Formalizing the ordinary mathematics"
section_number: 3
pages: 7-10
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
doc_brief: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
This section describes some of the work on formalizing Euclidean space and
measure theory, and the development of further proof automation, which
should be useful in this endeavor.
The computer code in Flyspeck has so far received the lion’s share of the
formal effort. This is entirely reasonable since there are, or at least were,
real questions about the feasibility of reproducing these results in a formal
way. However, the Flyspeck proof includes a large amount of ‘ordinary’
mathematics, which also needs to be formalized. Here we are on fairly
safe ground in principle, because by now we understand the formalization
of mainstream mathematics quite well [48]. It is safe to predict that this
formalization can be done, and we can even hope for a reasonably accurate
estimate of the effort involved. Nevertheless, the formalization is certainly
non-trivial and will require considerable work.
3.1. F ormalizing Euclidean space. Much of our work has been devoted
to developing a solid general theory of Euclidean spaceRN [25]. For Fly-
speck, we invariably just need the special caseR3. While some concepts,
e.g. vector cross products, are specific toR3, most of the theory has been
developed for generalRN so as to be more widely applicable. The theorem
prover HOL Light [24] is based on a logic without dependent types, but we
can still encode the indexN as a type (roughly, an arbitrary indexing type
of sizeN). This means that theorems about specific sizes like3 really are
just type instantiations of theorems for generalN stated with polymorphic
type variables. The theory contains the following:
• Basic properties of vectors inRN, linear operators and matrices, di-
mensions of vector subspaces and other bits of linear algebra. For
example, the following is a formal statement of the theorem that a
square matrixA′ is a left inverse to another oneA iff it is a right
inverse. Note that the double use of the same type variableN con-
strains the theorem to square matrices:
|- ∀A:real^N^N A’:real^N^N. (A ** A’ = mat 1) ⇔ (A’ ** A = mat 1)
• Metric and topological notions like distances, open sets, closure,
compactness and paths. Some of these are very general, others are
more specific to Euclidean space. Some results include the Heine-
Borel theorem, the Banach fixed-point theorem and Brouwer’s fixed-
point theorem. The following is a formal statement that continuous
functions preserve connectedness.
|- ∀f:real^M->real^N s. f continuous_on s ∧ connected s
⇒ connected(IMAGE f s)
8 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
• Properties of convex sets, convex hulls, cones etc. Results include
Helly’s theorem, Carathéodory’s theorem, and various classic results
about separating and supporting hyperplanes. The following states
a simpler but not entirely trivial result that convex hulls preserve
compactness.
|- ∀s:real^N->bool. compact s ⇒ compact(convex hull s)
• Sequences and series of vectors and uniform convergence, Fréchet
derivatives and their properties, up to various forms of the inverse
function theorem, as well as specific 1-dimensional theorems like
Rolle’s theorem and the Mean Value Theorem. Here is the formal
statement of the chain rule for Fréchet derivatives.
|- ∀f:real^M->real^N g:real^N->real^P f’ g’.
(f has_derivative f’) (at x) ∧
(g has_derivative g’) (at (f x))
⇒ ((g o f) has_derivative (g’ o f’)) (at x)
3.2. F ormalizing measure theory. Although the basic Euclidean theory
is an important foundation, and many of the concepts like ‘convex hull’ are
used extensively in the Flyspeck mathematics, perhaps the most important
thing to formalize is the concept of volume.
We define integrals of general vector-valued functions over subsets ofRN,
using the Kurzweil-Henstock gauge integral definition. We develop all the
usual properties such as additivity and the key monotone and dominated
convergence theorems. We also develop a theory of absolutely integrable
functions, where bothf and|f| are gauge integrable; this is known to co-
incide with the Lebesgue integral. Here is a formal statement of the simple
theorem that integration preserves linear scaling:
|- ∀f:real^M->real^N y s h:real^N->real^P.
(f has_integral y) s ∧ linear h ⇒ ((h o f) has_integral h(y)) s
Using this integral applied to characteristic functions, we develop a theory
of (Lebesgue) measure, which of course gives volume in the 3-dimensional
case. The specific notion ‘measure zero’ is formalized asnegligible, and
we also have a general notion of a set having a finite measure, and a function
measure to return that measure when it exists. For example, this is the basic
additivity theorem:
|- ∀s t. measurable s ∧ measurable t ∧ DISJOINT s t
⇒ measure(s UNION t) = measure s + measure t
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 9
We have proved that various ‘well-behaved’ sets such as bounded convex
ones and compact ones, or more generally those with negligible frontier
(boundary) are measurable, e.g.
|- ∀s:real^N->bool. bounded s ∧ negligible(frontier s) ⇒ measurable s
The main lack at the moment is a set of results for actually computing the
measures of specific sets, as needed for Flyspeck. We can evaluate most
basic 1-dimensional integrals by appealing to the Fundamental Theorem of
Calculus, but we need to enhance the theory of integration with stronger
Fubini-type results so that we can evaluate multiple integrals by iterated
one-dimensional integrals. This work is in progress at the time of writing.
3.3. Enhanced automation. Usingcoordinates, manynon-trivialgeomet-
ric statements inR3, or other Euclidean spaces of specific finite dimension,
can be reduced purely to the elementary theory of reals. This is known to
be decidable using quantifier elimination [44, 3, 28]. However, in practice
this is often problematic because quantifier elimination for nonlinear formu-
las is inefficient. The problem is particularly severe if we want to have any
kind of formal proof, as we do in Flyspeck, since producing such a proof
induces further slowdowns [30], [33]. With this in mind, we have explored a
different approach to the case of purely universally quantified formulas [26],
based on ideas of Parrilo [40]. This involves reducing the initial problem to
semidefinite programming, solving the SDP problem using an external tool
and reconstructing a ‘sum-of-squares’ (SOS) certificate that can easily be
formally checked.
For example, suppose we wish to verify that if a quadratic equationax2 +
bx +c = 0 has a real root, thenb2≥ 4ac. Using the SDP solver we find an
algebraic certificateb2− 4ac = (2ax +b)2− 4a(ax2 +bx +c), from which
the required fact follows easily:(2ax +b)2≥ 0 because it is a square, and
4a(ax2 +bx +c) = 0 because x is a root, and so we deduceb2− 4ac≥ 0.
This method seems very useful for automating routine nonlinear reasoning
in a way that is easy and quick to formally verify, so that we don’t have
to rely on the correctness of a complicated program. It is even capable of
solving the coordinate forms of some of the simpler Flyspeck inequalities
directly, though it seems unlikely to be competitive with customized non-
linear optimization methods as described in Section 5. For example, one
simple Flyspeck inequality is the following, which after being reduced to a
real problem with 9 variables (three coordinates for each point) is solved by
SOS in a second:
||u−v||≥ 2∧||u−w||≥ 2∧||v−w||≥ 2∧||u−v||<
√
8⇒|| w−(u+v)/2||>||u−v||/2.
10 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
A quite different approach to geometric theorem proving is to work in the
setting of a general real vector space or normed real vector space. In this
case, other decision methods are available [43]. In particular, one of these
decision procedures that we have implemented in HOL Light can sometimes
handle simple forms of spatial reasoning in a purely ‘linear’ way, and so be
much more efficient than the direct reduction to coordinates, even if we do
in fact have a specific dimension in mind. One real example from formalizing
complex analysis is the following inR2:
|||w−z||− r| =d∧||u−w||<d/ 2∧||x−z|| =r⇒d/2≤|| x−u||.
