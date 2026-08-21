---
doc_id: arxiv-hep-th-0306165v1
doc_title: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial"
section_id: sec-041-22-i-am-endebted-to-g-moore-and-a-strominger-for
section_title: "I am endebted to G. Moore and A. Strominger for very helpful co mments and suggestions"
section_number: 22
pages: 56-62
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting"
---
on these points.
55
of the group Γ. Therefore, comparing (A.10) with (2.10), we c onclude that in the present
case the holonomies l andm are given by
l =e(Σ+ iΘ) / 2 , m =eπ (r++i|r−|) (A.15)
In particular, we ﬁnd that, with the choice (A.14), the “mass shell” condition (A.11) looks
like
l + 1 = 0 (A.16)
and has the ‘wrong’ sign compared to (A.8). This result does n ot agree with the fact that
the 1-cycle γl becomes contractible in the on-shell BTZ black hole geometr y and, therefore,
the corresponding holonomy should be trivial. Finally, let us remark that this problem can
not be ﬁxed by applying a gauge transformation to (A.14) sinc e any (non-singular) gauge
transformation can not change the holonomy.
Therefore, we need to construct a ﬂat SL(2,C) gauge connection that would be non-
singular everywhere inside M . It is convenient to introduce a new set of coordinates:
̺ = logR
ξ =f (χ) cosθ
η =f (χ) sinθ
(A.17)
where the function,
f (χ) = cosχ
1 + sinχ, (A.18)
is chosen such that the metric induced in the ( ξ,η )-plane is conformal to the usual Eu-
clidean metric, ds2 =dξ2 +dη2. Speciﬁcally, rewriting the BTZ black hole metric (A.6) in
the coordinates (A.17), we ﬁnd
ds2 =
( 1 +f 2
1−f 2
) 2[
d̺2 + 4
(1 +f 2)2 (dξ2 +dη2)
]
(A.19)
The corresponding components of the vielbein and the spin co nnection can be written
as
e1 = 1 +f 2
1−f 2d̺
e2 = 2
1−f 2dξ
e3 = 2
1−f 2dη
w1 =ξe3−ηe2
w2 = 2η
1 +f 2e1
w3 =− 2ξ
1 +f 2e1
(A.20)
56
Combining these together we ﬁnd the explicit expression for the components of the ﬂat
SL(2,C) gauge connection, Aa =wa +iea,
A1 = 2ξ
1−f 2dη− 2η
1−f 2dξ +i 1 +f 2
1−f 2d̺
A2 = 2η
1−f 2d̺ +i 2
1−f 2dξ
A3 =− 2ξ
1−f 2d̺ +i 2
1−f 2dη
(A.21)
which is non-singular everywhere in the interior of the soli d torus, M = S1× D2.
Now let us evaluate the SL(2,C) holonomies (A.12). For simplicity, let us consider
a non-rotating BTZ black hole, with J = 0. Then, the second identiﬁcation in (A.7) is
trivially realized in the coordinates (A.17), whereas the ﬁ rst one reads:
(a) : ( ̺,ξ,η )∼ (̺ + 2πr+,ξ,η ) (A.22)
Therefore, we can choose the cycles γl andγm to be parametrized in the following way, cf.
(A.13),
γm : s↦→(̺0 + 2πr+s, ξ = 0, η = 0)
γl : s↦→(̺0, ξ =ξ0 cos 2πs, η =ξ0 sin 2πs)
(A.23)
Since only the A1-component of the gauge connection is non-trivial along the curve
γm, we can easily ﬁnd the corresponding holonomy,
ρ(γm) =
(
eπr + 0
0 e−πr +
)
(A.24)
Comparing this result with (A.15), we ﬁnd that the holonomy o f the gauge connection
(A.21) around γm is the same as in the previous calculation, based on the singu lar gauge
connection (A.14). On the other hand, since the connection ( A.21) is ﬂat and non-singular
everywhere in the interior of the solid torus, the holonomy a round a contractible cycle γl
is guaranteed to vanish automatically,
l = 1
However, since many components of the gauge connection (A.2 1) do not vanish along the
curveγl, to verify this directly would require some work. Perhaps th e best way to approach
this problem would be to ﬁnd a gauge transformation, which re moves non-commuting
components of the gauge connection, and allows to write the h olonomy (A.12) in a simple
form.
57
Appendix B. Quantization for T orus Knots
One simple way of classifying knots (in I R 3) is to associate to every knot K a non-
negative number, g(K), called the genus of the knot. Indeed, every knot can be embe dded
in some Riemann surface of genus g, and, as the name suggests, g(K) is the minimal
value of genus for which this can be done (without self-cross ing or breaking the knot).
For example, the only knot with g = 0 is the unknotted circle. The next simplest case
corresponds to knots of genus one, the so-called torus knots .
Since torus knots are special in a number of ways, we can’t rea lly call them generic
representatives. In particular, since torus knots are not h yperbolic, most of the motivation
discussed in the introduction does not apply here. Neverthe less, torus knots provide a sim-
ple toy model, which includes all the ingredients that one wo uld ﬁnd in a more complicated
non-linear quantum system, say, corresponding to a ﬁgure-e ight knot. Therefore, in order
to emphasize the general ideas, here we will ignore the subtl eties, slightly oversimplifying
our discussion.
(0,0)
(2π,2π)
Fig. 13: Trefoil knot on a torus.
By deﬁnition, torus knots are knots which can be drawn on the s urface of a torus.
They are labeled by an unordered pair of relatively prime num bers (r,s ), which refers to
the number of times the image of the knot winds basic cycles on the torus. For example,
the trefoil knot is a torus knot of type (2 , 3), see ﬁg. 13.
The A-polynomial of a non-trivial ( r,s )-torus knot has a very simple form [46]:
A(l,m ) = lmrs + 1 (B.1)
58
The zero locus of this polynomial deﬁnes a character variety L, linearly embedded into
P = C∗× C∗. In terms of the ( u,v )-variables (3.4), the variety L can be deﬁned by the
following two equations:
Re(u) +rs· Re(v) = 0
Im(u) +rs· Im(v)−π = 0
(B.2)
Our goal is to quantize a Hamiltonian system associated with֒P and, in particular, to
ﬁnd the quantum wave function Z(M ) supported on L. The result can be interpreted as a
partition function in the SL(2,C) Chern-Simons theory on a complement M = S3\K of
the torus knot K. Notice, that M is not a hyperbolic 3-manifold. Therefore, as suggested
by the asymptotic expression (3.34), it is natural to consid er a special case 23 corresponding
to σ = 0.
In this case, the canonical commutation relations that foll ow from the Chern-Simons
action (1.1) look like:
[Re(v), Re(u)] = [Im(u), Im(v)] = 2πi
k
[Re(u), Im(v)] =−[Re(v), Im(u)] = 0
(B.3)
and the Liouville 1-form (3.26) is given by
θ = k
π
(
Re(v)dRe(u) + Im(u)dIm(v)
)
(B.4)
It can be written in the canonical form (3.16) provided that w e deﬁne the coordinates qi
and the conjugate momenta pj as
(
p1
p2
)
=
(
Re(v)
Im(u)
)
and
(
q1
q2
)
=
(
Re(u)
Im(v)
)
(B.5)
Here we omit the overall factor k/4π, which can be treated as the inverse Planck constant.
In these variables, the Lagrangian submanifold L can be written as:
q1 +rs·p1 = 0
rs·q2 +p2−π = 0
(B.6)
Notice, that the Hamiltonian system splits into two non-int eracting subsystems de-
scribed by the canonical variables ( q1,p 1) and ( q2,p 2), respectively. The phase space of
23 In another special case, k = 0 and σ ⁄= 0, we ﬁnd that the action integral S is identically
zero.
59
the ﬁrst system is non-compact, whereas in the second system both the coordinate and
the momentum are compact. For now, let us ignore the compactn ess of q2 and p2. Then,
in the coordinate representation the action integral reads :
S = k
π
∫
p1dq1 +p2dq2 =
=−k
π
( 1
2rsq2
1 + rs
2 q2
2−πq2
) (B.7)
If ψ is a constant half-density on L, then the transformation rule for half-densities im-
plies that the Reidemeister-Ray-Singer torsion, T , is also constant (independent on qi) in
this class of examples. Therefore, in the semi-classical li mit the partition function of the
SL(2,C) Chern-Simons theory on the complement of a torus knot look s like:
Z(M )∼ exp
(
− ik
2πrsq2
1− ikrs
2π q2
2 +ikq2
)
+... (B.8)
This result gives a prediction for the Chern-Simons invaria nt of the torus knot complement
M (as a function of the holonomies l and m). Using (B.2) and (B.5), we can write it as:
CS (M ) = 1
2π2rs
(
log2|l| + arg2(l)−π2
)
(B.9)
Here, we slightly oversimpliﬁed our discussion assuming th at the phase spaces of both
dynamical systems are non-compact. A nice way to incorporat e the compactness of q2 and
p2 is to notice that they parameterize a torus 24, which can be viewed as a phase space of
the SU (2) Chern-Simons theory on a 3-manifold M with boundary Σ, see (2.13). Hence,
the exact partition function of the SL(2,C) Chern-Simons theory on M can be written as
a product,
ZSL(2, C)(M ) = ZSU (2)(M )× exp
(
− ik
2πrsq2
1 + iπ
4 sign (rs)
)
(B.10)
where ZSU (2)(M ) is the partition function of the SU (2) Chern-Simons theory (see e.g.
[43,61,97,98,99]), and the rest represents the wave functi on in the ﬁrst system, with non-
compact phase space parametrized by p1 and q1. Notice, that the semi-classical approx-
imation is exact in this case. This has to be compared with the computation of the
Reshetikhin-Turaev-Witten invariants [3,100] for torus k nots in S3, where the stationary
phase approximation is also exact, see e.g. [101].
24 Once again, we should remind that we tacitly omit the quotien t by the Weyl group.
60
