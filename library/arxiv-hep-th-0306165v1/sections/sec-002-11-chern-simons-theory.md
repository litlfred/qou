---
doc_id: arxiv-hep-th-0306165v1
doc_title: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial"
section_id: sec-002-11-chern-simons-theory
section_title: "Chern-Simons Theory"
section_number: 1.1
pages: 2-4
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
toc_source: inferred
doc_brief: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial — We study three-dimensional Chern-Simons theory with complex gauge group SL(2,C), which has many interesting connections"
---
group. Of particular interest is a Chern-Simons theory with gauge group GC = SL(2,C)
(viewed as a complexiﬁcation of G = SU(2)), which has many interesting connections with
three-dimensional quantum gravity and geometry of hyperbolic three-manifolds. In this
introductory section we review some aspects of these relations, formulate the problem, and
describe various applications.
1.1. Chern-Simons Theory
Consider an oriented three-dimensional space M.
We wish to formulate a Chern-
Simons gauge theory on M with complex gauge group GC, whose real form we denote
by G. Let gC and g be the corresponding Lie algebras. In these notations, the gauge
connection A is a one-form on M valued in the complex Lie algebra gC. Explicitly, we
can write A = P
a Aa · Ta where Ta denote the generators of g, which are assumed to be
orthonormal, Tr(TaTb) = δab. Then, the Chern-Simons action can be written as a sum of
the holomorphic and anti-holomorphic terms,
I = t
8π
Z
M
Tr

A ∧dA + 2
3A ∧A ∧A

+
+ t
8π
Z
M
Tr

A ∧dA + 2
3A ∧A ∧A

(1.1)
where t = k + is and t = k −is are the corresponding coupling constants. Consistency of
the quantum theory requires the “level” k to be an integer, k ∈ZZ. The other parameter,
s, is not quantized. However, s must obey certain constraints imposed by unitarity [1].
In Euclidean space, unitarity implies that the argument of the Feynman path integral
Z(M) =
Z
DA eiI
(1.2)
must be complex conjugated under a reversal of the orientation on M. In the Chern-Simons
theory deﬁned by the action (1.1), there are two possibilities to achieve this, corresponding
to either purely real or purely imaginary values of s. In the ﬁrst case, A is invariant under
the reversal of the orientation and t is the usual complex conjugate of t. On the other
hand, the second possibility, s ∈iIR, is realized when the gauge connection transforms non-
trivially under the reversal of the orientation, A 7→A. In the rest of the paper we mainly
consider the case of imaginary s and GC = SL(2,C), which is related to the Euclidean
quantum gravity in three dimensions (see discussion below).
1
γ
Fig. 1: A knotted Wilson loop in the IR3.
Now let us consider observables in this theory. If M is a manifold without boundary,
holonomies of the gauge connection provide a complete set of observables, also known as
“Wilson lines” in the context of gauge theory or “loop variables” in the context of gravity
[2]. Speciﬁcally, given a closed oriented curve γ ⊂M and a representation R of GC, one
can deﬁne a gauge invariant observable as
WR(γ) = TrR Holγ(A) = TrR

P exp
I
γ
A

(1.3)
The Wilson loop observables WR(γ) are naturally associated with knots in M. Indeed,
even though intrinsically the curve γ is simply a circle, its embedding in M may be highly
non-trivial, represented by a knot, as in ﬁg. 1. More generally, an embedding of a collection
of circles into M is called a link, and the image of each circle is called a component of
the link. Thus, given a link with (non-intersecting) components γi, i = 1, . . ., r, and a
set of representations Ri assigned to each component of the link, one can study a natural
generalization of the Feynman path integral (1.2):
Z(M; γi, Ri) =
Z
DA exp(iI)
r
Y
i=1
WRi(γi)
(1.4)
which, following [3], we call the (unnormalized) expectation value of the link. By construc-
tion, it is a function of t and t, which also depends on the topology of the three-manifold
M, on the choice of the Wilson lines γi, and on the corresponding representations Ri.
A large class of representations Ri can be naturally obtained by complexiﬁcation from
the corresponding representations of the real Lie algebra g. However, no new information
can be gained by studying such representations since the evaluation of (1.4) essentially
reduces to the Chern-Simons theory with the real form of the gauge group, G, at least
2
in perturbation theory1.
On the other hand, of particular interest are certain inﬁnite
dimensional representations Ri that we describe explicitly in the next subsection, after
