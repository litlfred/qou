---
doc_id: arxiv-2309.04240v1
doc_title: "BURAU REPRESENTATION OF BRAID GROUPS AND q-RATIONALS"
section_id: sec-005-4-discussion
section_title: "Discussion"
section_number: 4
pages: 7-9
source_pdf: 2309.04240v1.pdf
source_sha256: 792154a0d6a57e34
toc_source: outline
doc_brief: "BURAU REPRESENTATION OF BRAID GROUPS AND q-RATIONALS — We establish a link between the new theory of q-deformed ratio- nal numbers and the classical Burau representation of the braid group B3."
---
Perhaps the most interesting question about specializations ρt
3 is to understand
the number-theoretic properties of the algebraic integers from the set Σ.
The
following results from the theory of q-rationals can give more information in this
direction.
• The sequences of coeﬃcients in the polynomials written in the parameter q
are unimodal. This fact, which was conjectured in [24] and studied in [22], was
eventually proved in [26].
This implies, in particular, that if an algebraic integer α ∈C has a conjugate
which is real and positive, then α cannot be part of Σ (and hence, corresponding
specialization of the Burau representation at t0 = −α is faithful).
• The trace of the matrix (3.1) is a palindromic polynomial (in variable q) [18].
We wonder if this is related to the invariant Hermitian form of [32].
• The “stabilisation phenomenon” of [25] is one of the main properties of q-
rationals.
Suppose that a sequence of rationals,
rm
sm , converges to an irrational
number x. Then the Taylor series of the rational functions
Rm(q)
Sm(q) stabilizes, as
m grows. This allows to deﬁne a q-deformation [x]q as Taylor series with integer
coeﬃcients. The study of the radii of convergence of these series is closely related
to the study of the singular set Σ. In particular if ϕ = 1+
√
5
2
is the golden ratio,
1We are very grateful to A.Yu. Olshanskiy for the help with this proof.
8
S. MORIER-GENOUD, V. OVSIENKO, AND A. VESELOV
then the radius of convergence of the corresponding series [ϕ]q is R(ϕ) =
3−
√
5
2
(see [19]).
The annulus in Theorem 2 can be reduced to 3−
√
5
2
≤|t| ≤3+
√
5
2
modulo the
following conjecture.
Conjecture 2. [19] For every real x > 0 the radius of convergence R(x) of the
series [x]q satisﬁes the inequality
R(x) ≥R(ϕ) = 3 −
√
5
2
and the equality holding only for x which are PSL(2, Z)-equivalent to ϕ.
Since for a q-rational
 r
s

q = R(q)
S(q) the radius of convergence equals the minimal
modulus of the roots of the denominator S(q), modulo this conjecture we can claim
that Σ∗lies within the annulus 3−
√
5
2
≤|q| ≤3+
√
5
2
and therefore the specialized
Burau representation ρt
3 is faithful for all t outside the annulus 3−
√
5
2
≤|t| ≤3+
√
5
2
.
In some special cases Conjecture 2 was proved in [19, 29]. Computer experiments
show that the bounds 3±
√
5
2
for the annulus in the conjectures are optimal. In par-
ticular, the polynomials in the entries of the matrices M +
q (1, 1, . . . , 1) = (RqLq)m
have roots closer and closer to the circle |t| = 3−
√
5
2
, as m grows.
As we have already mentioned in the Introduction, the Alexander polynomial of
the link L = L(β) related to a braid β ∈Bn can be given (up to a unit in Z[t, t−1])
by the Burau formula [10]
∆L(t) = 1 −t
1 −tn det(I −ρn(β)).
No general formula in terms of Burau representation is known for the Jones poly-
nomials. However, as it was noticed in [24], for the class of rational (or two-bridge)
knots the (normalised) Jones polynomial of the knot corresponding to a fraction r
s
can be expressed using the polynomials R(q) and S(q) in (2.5) via
J r
s (q) = qR(q) + (1 −q)S(q)
(see Appendix A in [24]). The proof is based on the results of the paper [20] by
Lee and Schiﬄer, using the combinatorics of snake graphs and cluster algebras.
Alternatively, in terms of the so-called left version of the q-deformed rationals
hr
s
i♭
q = R♭(q)
S♭(q) ,
which was observed in [25] (cf. Remark 2.3) and introduced and studied by Bapat
et al [4], one can express the normalised Jones polynomial as J r
s (q) = qmR♭(q−1)
with some m ∈Z (see Appendix A2 in [4] and [30]). It would be interesting to
see if all this can be explained using Burau representation.
In this relation we
would like to note that the role of the left q-rationals became more clear after the
recent preprint [33], where an inﬁnitesimal analogue of the Burau representation is
investigated.
The Burau representation ρn fails to be faithful for n ≥5, but there is another
homological representation
of the braid group Bn, ﬁrst introduced in [16] and
now known as Lawrence-Krammer-Bigelow representation, which is proved to be
faithful for all n [6, 14].
The work of Lawrence [16] was initially motivated by
BURAU REPRESENTATION OF B3
9
the desire to better understand the signiﬁcance of the Jones polynomial for links
[11]. Burau representation corresponds to the ﬁrst non-trivial case m = 1 in her
construction. The general case is related also to the monodromy representations
for the Knizhnik-Zamolodchikov equations
κ ∂ψ
∂zi
−
X
k̸=i
Ωik
zi −zk
ψ(z1, . . . , zn) = 0,
i = 1, . . . , n,
which were studied by Tsuchiya and Kanie [34] and Kohno [13].
This makes an important link of the braid groups and knots with the theory
of Yang-Baxter equations and quantum integrable systems (see more on this in
[12, 35]).
There is a well-known representation [11] of the braid group in the
Temperley-Lieb algebra, which appeared in a similar relation in statistical me-
chanics. Bigelow [7] proved the equivalence of the faithfulness problem for Burau,
Jones and Temperley-Lieb representations in the most interesting case n = 4. It
is known that the Temperley-Lieb representation of the braid group B3 is faithful
[28], but the same question about its specializations seems to be open. It would be
interesting to apply our approach to this problem as well.
Finally, we would like to mention that the specializations of Burau represen-
tations of Bn at the roots of unity naturally appear in algebraic geometry as the
homological monodromy in the moduli space of algebraic curves
yd = xn + a1xn−1 + · · · + a0.
This observation goes back to the work of Arnold [2], who considered the hy-
perelliptic case d = 2, and was explicitly stated by Magnus and Peluso [21] in
the general case. A more recent important development in this direction is due
to Venkataramana [36], who proved the arithmeticity of the image of the Burau
representation ρn specialized at the d-th roots of unity when n ≥2d + 1.
