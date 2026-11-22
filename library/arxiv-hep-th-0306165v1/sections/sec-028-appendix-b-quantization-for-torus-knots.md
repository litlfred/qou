---
doc_id: arxiv-hep-th-0306165v1
doc_title: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial"
section_id: sec-028-appendix-b-quantization-for-torus-knots
section_title: "Quantization for Torus Knots"
section_number: Appendix B
pages: 59-62
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
toc_source: inferred
doc_brief: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial — We study three-dimensional Chern-Simons theory with complex gauge group SL(2,C), which has many interesting connections"
---
One simple way of classifying knots (in IR3) is to associate to every knot K a non-
negative number, g(K), called the genus of the knot. Indeed, every knot can be embedded
in some Riemann surface of genus g, and, as the name suggests, g(K) is the minimal
value of genus for which this can be done (without self-crossing or breaking the knot).
For example, the only knot with g = 0 is the unknotted circle. The next simplest case
corresponds to knots of genus one, the so-called torus knots.
Since torus knots are special in a number of ways, we can’t really call them generic
representatives. In particular, since torus knots are not hyperbolic, most of the motivation
discussed in the introduction does not apply here. Nevertheless, torus knots provide a sim-
ple toy model, which includes all the ingredients that one would ﬁnd in a more complicated
non-linear quantum system, say, corresponding to a ﬁgure-eight knot. Therefore, in order
to emphasize the general ideas, here we will ignore the subtleties, slightly oversimplifying
our discussion.
(0,0)
(2π,2π)
Fig. 13: Trefoil knot on a torus.
By deﬁnition, torus knots are knots which can be drawn on the surface of a torus.
They are labeled by an unordered pair of relatively prime numbers (r, s), which refers to
the number of times the image of the knot winds basic cycles on the torus. For example,
the trefoil knot is a torus knot of type (2, 3), see ﬁg. 13.
The A-polynomial of a non-trivial (r, s)-torus knot has a very simple form [46]:
A(l, m) = lmrs + 1
(B.1)
58
The zero locus of this polynomial deﬁnes a character variety L, linearly embedded into
P = C∗× C∗. In terms of the (u, v)-variables (3.4), the variety L can be deﬁned by the
following two equations:
Re(u) + rs · Re(v) = 0
Im(u) + rs · Im(v) −π = 0
(B.2)
Our goal is to quantize a Hamiltonian system associated with L֒ →P and, in particular, to
ﬁnd the quantum wave function Z(M) supported on L. The result can be interpreted as a
partition function in the SL(2,C) Chern-Simons theory on a complement M = S3 \ K of
the torus knot K. Notice, that M is not a hyperbolic 3-manifold. Therefore, as suggested
by the asymptotic expression (3.34), it is natural to consider a special case23 corresponding
to σ = 0.
In this case, the canonical commutation relations that follow from the Chern-Simons
action (1.1) look like:
[Re(v), Re(u)] = [Im(u), Im(v)] = 2πi
k
[Re(u), Im(v)] = −[Re(v), Im(u)] = 0
(B.3)
and the Liouville 1-form (3.26) is given by
θ = k
π

Re(v)dRe(u) + Im(u)dIm(v)

(B.4)
It can be written in the canonical form (3.16) provided that we deﬁne the coordinates qi
and the conjugate momenta pj as

p1
p2

=

Re(v)
Im(u)

and

q1
q2

=

Re(u)
Im(v)

(B.5)
Here we omit the overall factor k/4π, which can be treated as the inverse Planck constant.
In these variables, the Lagrangian submanifold L can be written as:
q1 + rs · p1 = 0
rs · q2 + p2 −π = 0
(B.6)
Notice, that the Hamiltonian system splits into two non-interacting subsystems de-
scribed by the canonical variables (q1, p1) and (q2, p2), respectively. The phase space of
23 In another special case, k = 0 and σ̸ = 0, we ﬁnd that the action integral S is identically
zero.
59
the ﬁrst system is non-compact, whereas in the second system both the coordinate and
the momentum are compact. For now, let us ignore the compactness of q2 and p2. Then,
in the coordinate representation the action integral reads:
S = k
π
Z
p1dq1 + p2dq2 =
= −k
π
 1
2rsq2
1 + rs
2 q2
2 −πq2

(B.7)
If ψ is a constant half-density on L, then the transformation rule for half-densities im-
plies that the Reidemeister-Ray-Singer torsion, T, is also constant (independent on qi) in
this class of examples. Therefore, in the semi-classical limit the partition function of the
SL(2,C) Chern-Simons theory on the complement of a torus knot looks like:
Z(M) ∼exp

−ik
2πrsq2
1 −ikrs
2π q2
2 + ikq2

+ . . .
(B.8)
This result gives a prediction for the Chern-Simons invariant of the torus knot complement
M (as a function of the holonomies l and m). Using (B.2) and (B.5), we can write it as:
CS(M) =
1
2π2rs

log2 |l| + arg2(l) −π2
(B.9)
Here, we slightly oversimpliﬁed our discussion assuming that the phase spaces of both
dynamical systems are non-compact. A nice way to incorporate the compactness of q2 and
p2 is to notice that they parameterize a torus24, which can be viewed as a phase space of
the SU(2) Chern-Simons theory on a 3-manifold M with boundary Σ, see (2.13). Hence,
the exact partition function of the SL(2,C) Chern-Simons theory on M can be written as
a product,
ZSL(2,C)(M) = ZSU(2)(M) × exp

−ik
2πrsq2
1 + iπ
4 sign (rs)

(B.10)
where ZSU(2)(M) is the partition function of the SU(2) Chern-Simons theory (see e.g.
[43,61,97,98,99]), and the rest represents the wave function in the ﬁrst system, with non-
compact phase space parametrized by p1 and q1. Notice, that the semi-classical approx-
imation is exact in this case.
This has to be compared with the computation of the
Reshetikhin-Turaev-Witten invariants [3,100] for torus knots in S3, where the stationary
phase approximation is also exact, see e.g. [101].
24 Once again, we should remind that we tacitly omit the quotient by the Weyl group.
60
