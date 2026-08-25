---
doc_id: arxiv-hep-th-0306165v1
doc_title: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial"
section_id: sec-028-51-a-brief-review-of-the-volume-conjecture
section_title: "A Brief Review of the Volume Conjecture"
section_number: 5.1
pages: 37-38
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting"
---
A well-known invariant of knots is the Jones polynomial J(K,q ) [78]. Here we consider
a more general invariant, the so-called N -colored Jones polynomial JN (K,q ), associated
with an N -dimensional irreducible representation of SU (2). Thus, the usual Jones poly-
nomial appears as a special case, J(K,q ) = J2(K,q ). Like the ordinary Jones polynomial,
JN (K,q ) can be deﬁned by skein relations and is a Laurent polynomial in the variable
q1/ 2. Remarkably, there is a relation between the colored Jones p olynomial of a knot and
the volume of its complement.
The ﬁrst observation along these lines was made by Kashaev, w ho introduced a link
invariant associated with quantum dilogarithm [34]. The Ka shaev’s invariant assocated
with a knot K — usually denoted by ⟨K⟩N — is based on the theory of quantum diloga-
rithms at the N -th root of unity, q = exp(2πi/N). Moreover, it was noticed in [34] that
for certain knots the asymptotic behavior of this invariant is related to the volume of the
knot complement
lim
N→∞
log|⟨K⟩N|
N = 1
2π Vol(M ) (5 .1)
15 The work presented in this section originated from discussi ons with K. Krasnov.
16 See also [75,76,77] for a previous work in this direction.
36
A generalization of this relation to all knots is known as the volume conjecture [34].
Later, it was realized in [35] that the Kashaev’s invariant i s related to the colored
Jones polynomial evaluated at the special value of q:
q =e2πi/N (5.2)
Therefore, the volume conjecture can be reformulated as a re lation between the volume of
the knot complement and a special limit of the colored Jones p olynomial:
The V olume Conjecture:
lim
N→∞
log|JN (K,e 2πi/N )|
N = 1
2π Vol(M ) (5 .3)
In this form, the volume conjecture has been veriﬁed in a numb er of examples. In partic-
ular, Kashaev and Tirkkonen [79] proved that it is true for al l torus knots, in a sense that
the limit (5.3) is zero.
The volume conjecture was extended further in [36], where it was shown that for a
large class of knots one can remove the absolute value in (5.3 ), so that the following limit
holds17:
lim
N→∞
logJN (K,e 2πi/N )
N = 1
2π
(
Vol(M ) +i2π2CS (M )
)
(5.4)
This version of the volume conjecture — which relates the asy mptotic behavior of JN (K,q )
to the volume and Chern-Simons invariant of the knot complem ent — is the one we are
going to use here. For more work on the volume conjecture see e.g. [77,80,81,82].
