---
doc_id: witten1989-cmp-jones
doc_title: "Commun. Math. Phys. 121, 351-399 (1989) Mathematical Physics © Springer-Verlag 1989 Quantum Field Theory and the Jones Polynomial Edward Witten **"
section_id: sec-000-1-the-chern-simons-action
section_title: "The Chern-Simons Action"
section_number: 1
pages: 3-15
source_pdf: witten1989-cmp-jones.pdf
source_sha256: 32f98ed8f7b23588
toc_source: inferred
doc_brief: "Quantum field theory and the Jones polynomial (Witten, Commun. Math. Phys. 121 (1989) 351–399) — Chern–Simons gauge theory gives the Jones polynomial; framing dependence of Wilson loops"
---
We have been urged [1] to try to interpret the Jones polynomial in terms of three
dimensional Yang-Mills theory. So we begin on an oriented three manifold M
with a compact simple gauge group G. We pick a G bundle E, which may as well be
trivial, and on E we place a connection /if, which can be viewed as a Lie algebra
valued one form (a runs over a basis of the Lie algebra, and / is tangent to M). An
infinitesimal gauge transformation is
A^Ai-DiC, 
(1.1)
where £, a generator of the gauge group, is a Lie algebra valued zero form and the
covariant derivative is Dts = dtε -h [ A t , ε]. The curvature is the Lie algebra valued
two form Fίj = [Dί,Dj] = dίAJ — dJAi + [ A i , A j ] . Now we need to choose a
Lagrangian. We will not pick the standard Yang-Mills action !
^o=Jl/££'VTr(F ;,F w), 
(1.2)
M
as this depends on the choice of a metric gtj. We want to formulate a generally
covariant theory (in which all observables will be topological invariants), and to
this aim we want to pick a Lagrangian which does not require any choice of metric.
1 In what follows, the symbol
 ςTr" denotes an invariant bilinear form on the Lie algebra of G, a
multiple of the Cartan-Killing form; we will specify the normalization presently
354 
E.Witten
Precisely in three dimensions there is a reasonable choice, namely the integral of
the Chern-Simons three form:
<e = ~ $Ίϊ(A Λ dA+^A Λ A Λ A)
= £-$ε
ijkrTr(Ai(djAk-dkAj) 
+ lAί[Aj,Ak]). 
(1.3)
oπ M
The Chern-Simons term in three dimensional gauge theory has a relatively long
history. The abelian gauge theory with only a Chern-Simons term was studied by
Schwarz [18] and in unpublished work by I. Singer. Three dimensional gauge
theories with the Chern-Simons term added to the usual action (1.2) were
introduced in [19-21]. The nonabelian theory with only Chern-Simons action was
studied classically by Zuckerman [22]. The abelian Chern-Simons theory has
recently been studied in relation to fractional statistics by Hagen [24] and by
Arovas et al. [25] and in relation to linking numbers by Polyakov [23] and Frόh-
lich [15]. The novelty in our present discussion is that we will consider the quantum
field theory defined by the nonabelian Chern-Simons action and argue that it is
exactly soluble and has important implications for three dimensional geometry
and two dimensional conformal field theory.
The first fundamental property of the Chern-Simons theory is the quanti-
zation law first discussed in [21]. It arises because the group G of continuous maps
M -> G is not connected. In the homotopy classification of such maps one meets at
least the fact that π3 (G) ~ Z for every compact simple group G. Though (1.3) is
invariant under the component of the gauge group that contains the identity, it is
not invariant under gauge transformations of non-zero "winding number", gauge
transformations associated with non-zero elements of π3(G). Under a gauge
transformation of winding number m, the transformation law of (1.3) is
eS?-»«£? + const m. 
(1.4)
As in Dirac's famous work on magnetic monopoles, consistency of quantum field
theory does not quite require the single-valuedness of J5f, but only of exp (z J5f). For
this purpose, it is necessary and sufficient that the "constant" in (1.4) should be an
integral multiple of 2π. This gives a quantization condition on the parameter
called k in (1.3). If G is SU(N) and "Tr" means a trace in the TV dimensional
representation, then the requirement is that k should be an integer. In general, for
any G, we can uniquely fix the so far unspecified normalization of "Tr" so that the
quantization condition is kεZ.
We will see later that k is very closely related to the central charge in the theory
of highest weight representations of affine Lie algebras. It is no accident that the
reasoning which shows that k must be quantized in (1.3) has a 1 + 1 dimensional
analogue [26] which leads to quantization of the central charge in the represent-
ation theory of affine algebras.
In quantum field theory, in addition to a Lagrangian, one also wishes to pick a
suitable class of gauge invariant observables. In the present context, the usual
gauge invariant local operators would not be appropriate, as they spoil general
covariance. However, the "Wilson lines" so familiar in QCD give a natural class of
Quantum Field Theory and the Jones Polynomial 
355
Fig. 2. Several linked but non-intersecting oriented knots in a three manifold M. Such a
collection of knots is called a "link"
gauge invariant observables that do not require a choice of metric. Let C be an
oriented closed curve in M. Intrinsically C is simply a circle, but the topological
classification of embeddings of a circle in Mis very complicated, as we observe in
Fig. 1. Let R be an irreducible representation of G. One then defines the "Wilson
line" WR(C} to be the following functional of the connection At. One computes
the holonomy of A{ around C, getting an element of G that is well-defined up to
conjugacy, and then one takes the trace of this element in the representation R.
Thus, the definition is
WR (C) - ΎΪR P exp f At dx
l. 
(1.5)
c
The crucial property of this definition is that there is no need to introduce a metric,
so general covariance is maintained.
We now can formulate the general problem of interest. In an oriented three
manifold M, we take r oriented and non-intersecting knots Ch i = 1 ... r, whose
union is what knot theorists would call a "link" L. We assign a representation Rt
to each Cί5 and we propose to calculate the Feynman path integral
f/>^exp(/JS?) Π WRι(C{). 
(1.6)
i= 1
The symbol Djtf represents Feynman's integral over all gauge orbits, that is, an
integral over all equivalence classes of connections modulo gauge transfor-
mations. Of course, (1.6) has exactly the formal structure of some familiar
observables in QCD, the difference being that we are in three dimensions instead
of four and we have chosen a somewhat exotic gauge theory action. We will call
(1.6) the "partition function" of M with the given link, or the (unnormalized)
"expectation value" of the given link; we will denote it as Z(M\ C^R{) or simply
as Z(M L) for short.
For the case of links in S
3, we will claim that the invariants (1.6) are exactly
those that appear in the Jones theory and its generalizations. Simply replacing S
3
with a general oriented three manifold M gives a very intriguing (and as we will
see, effectively computable) generalization of the known knot polynomials.
Taking r = 0 (no knots), (1.6) gives invariants of the oriented three manifold M
which also turn out to be effectively computable. Before getting into any details,
let us note a few preliminary indications of a possible connection between (1.6) and
the Jones theory:
(1) In (1.6) we see the right variables, namely a compact Lie group G, a choice
of representation Rt for each component Ci of the link L, and an additional
356 
E.Witten
variable k. [In knot theory one usually makes an analytic continuation and
replaces k by a complex variable q, but it has been known since Jones' original
work that there are special properties at special values of q. We claim that these
properties reflect the fact that the three dimensional gauge theory with action (1.3)
is well-defined only if k is an integer.] The two variable generalization of the Jones
polynomial corresponds to the case that G is SU(N), and the R{ are all the defining
N dimensional representation of SU(N). The two variables are TV and k,
analytically continued to complex values. The Kauffman polynomial similarly
arises for G = SO(N) and R the N dimensional representation.
(2) As a further check on the plausibility of a relation between (1.6) and the
knot polynomials, let us note first of all that (1.6) depends on a choice of the
orientation of M, as this enters in fixing the sign of the Chern-Simons form.
Likewise, (1.6) depends on the orientations of the Ct , since these enter in defining
the Wilson lines (in computing the holonomy around Ch one must decide in which
direction to integrate around Ct ). If, however, one reverses the orientation of one
of the Cϊ and simultaneously exchanges the representation Rt with its complex
conjugate Rh then the definition of the Wilson lines is unchanged, so (1.6) is
invariant under this process. And if (without changing the Rt) one reverses the
orientations of all components Ct of the link L, then (1.6) is unchanged because of
a symmetry that physicists would call "charge conjugation". This is an involution
of the Lie algebra of G that exchanges all representations with their complex
conjugates; applying this involution to all integration variables in (1.6) leaves (1.6)
invariant while exchanging all Rt with their conjugates or equivalently reversing
the orientation of all the Q. These are important formal properties of the knot
polynomials.
2. The Weak Coupling Limit
To begin with, since a non-abelian gauge theory with only a Chern-Simons action
may seem unfamiliar, one might ask whether this Lagrangian really does lead to a
sensible quantum theory, and really can be regulated to give topologically
invariant results. In this section, we will briefly investigate this point by studying
the theory in a weak coupling limit in which computations are comparatively
straightforward. This is the limit of large k.
 2 For large k, the path integral
Z= (D^Qxp (^ f Tr (A Λ dA + ^A Λ A Λ A } ] 
(2.1)
\4π ά 
V 
3 
//
(for the moment we omit knots) contains an integrand which is wildly oscillatory.
The large k limit of such an integral is given by a sum of contributions from the
points of stationary phase. The stationary points of the Chern-Simons action are
precisely the "fiat connections", that is, the gauge fields for which the curvature
vanishes
Ff, = 0. 
(2.2)
2 The reader may wish to bear in mind that the discussion in this section and the next contains a
number of technicalities which are part of the logical story but perhaps not essential on a first
reading
Quantum Field Theory and the Jones Polynomial 
357
Gauge 
equivalence 
classes 
of 
such 
flat 
connections 
correspond 
to
homomorphisms
φ: MM) -> G, 
(2.3)
or more exactly to equivalence classes of such homomorphisms, up to conjug-
ation. If for simplicity we suppose that the topology of M is such that there are
only finitely many classes of homomorphisms (2.3), then the large k behavior of
(2.1) will be a sum
(2.4)
where the A
(^ are a complete set of gauge equivalence classes of fiat connections,
and μ(A
(a}) is to be obtained by stationary phase evaluation of (2.1), expanding
around A
(a). This reduction to a stationary phase evaluation means that the
nonabelian theory, for large fc, is closely related to the abelian theory. This in turn
has been shown [18] to lead to Ray-Singer analytic torsion [27], which is closely
related to the purely topological Reidemeister torsion. The μ(A
(a}) may be
evaluated as follows. We make in (2.1) the change of variables A{ = A\*
} -f- B{,
where B{ is the new integration variable. An important invariant of the fiat
connection A
(Cί} is its Chern-Simons invariant
I(A
(Λ)) = -- J Tr(A
( a } Λ dA
(a) + fΛ
( α ) Λ A
(a} Λ A
(«
}). 
(2.5)
4π M
When the Chern-Simons action is expanded in powers of Bt, the first terms are
<e = k - I(A
(y ]} + ~ J Tr (B Λ DB). 
(2.6)
4π M
Here it is understood that in (2.6), the expression DB denotes the covariant
exterior derivative of B with respect to the background gauge field A
(a); it does not
depend on a metric on M. A salient point is that in (2.6) there is no term linear in B,
since A
(a} is a critical point of the action.
To carry out the Gaussian integral in (2.6), gauge fixing is needed. There is no
way to carry out this gauge fixing without picking a metric on M (or in some other
way breaking the symmetry of the problem). After picking such a metric, a
convenient gauge choice is Dt B
1 = 0 (with Dί the covariant derivative constructed
from the metric and the background gauge field /l
(α)). The standard Faddeev-
Popov construction then gives rise to a gauge fixing Lagrangian
Here φ is a Lagrangian multiplier that enforces the gauge condition Dt B
1 = 0, and
c, c are anticommuting "ghosts" that are introduced to get the right measure on
the space of gauge fields modulo gauge transformations. The quadratic terms in φ
and B that can be found in (2.6), (2.7) have a natural geometric interpretation,
described (in the abelian case) in [18]. Let D be the exterior derivative on M,
twisted by the fiat connection A
(a\ and let * be the Hodge operator that maps k
forms to 3 — k forms. On a three manifold one has a natural self-adjoint operator
L = *D + Z>* which maps differential forms of even order to forms of even order
358 
E.Witten
and forms of odd order to forms of odd order. Let L_ denote its restriction to
forms of odd order. With B and φ regarded as a one form and a three form,
respectively, the boson kinetic operator in (2.6), (2.7) is precisely this operator L_ .
The kinetic operator of the ghosts is also a natural geometrical operator, the
Laplacian, which we will call A. We can now give a formula for the stationary
point contributions μ(A
(a}) that appear in (2.4). This is
μ (A
(a}) = exp (ίkI(A
(*
}}) 
- 
_ 
t 
(2.8)
]/det(LΓy
The phase factor in (2.8) is the value of the integrand in (2.1) at the point of
stationary phase, and the determinants (whose absolute values can be defined by
zeta functions) result from the Gaussian integral over B, φ, c, and c.
Now we come to the crucial point. To regularize the path integral, we have had
to pick a Riemannian metric on M. Therefore, it is not obvious a priori that the
μ(A
(a}} computed this way will really be topological invariants. Perhaps the
Chern-Simons theory suffers from anomalies, and cannot be regularized in a
generally co variant fashion. Happily, we can now appeal to [18], where it was
shown (in the context of the abelian theory, but this aspect of [18] generalizes) that
the absolute value of the ratio of determinants appearing in (2.8) is precisely the
Ray-Singer analytic torsion of the flat connection A
(a\ and so in particular is a
topological invariant. (The phase of this ratio of determinants is more delicate,
and will be discussed later.) This is the first indication that topological invariants
really can be obtained from the Chern-Simons theory.
The Phase of the Determinant
Though the absolute value of the ratio of determinants in (2.8) is the analytic
torsion discussed long ago by Schwarz, the phase requires additional study. The
ghost determinant detz) is real and positive, so the real issue is to study the phase
of det L _ . Because the operator L _ can be interpreted as a twisted Dirac operator,
the phase of its determinant can be related to the study of the phase of odd
dimensional fermion determinants, as studied by various authors [28]. However, I
will here give a brief derivation of the relevant facts from the bosonic point of view,
which is perhaps more natural in the present context. After an irrelevant rescaling
of B and φ, the integral of interest is
(2.9)
M 
/
Upon changing variables to an orthonormal basis of eigenfunctions x{ of the
operator L_ , with eigenvalues λh (2.9) becomes
]-] j ^U" < 
(2.10)
ϊ 
-oc |/π
Therefore the crucial integral to understand is
00 
/7γ
1= 
f ~eίλx\ 
(2.11)
Quantum Field Theory and the Jones Polynomial 
359
for real λ. We consider this integral to be defined by taking the limit as ε -> 0 of the
absolutely convergent integral
] 
Le
ίλχ2
 
- e~
εχ2. 
(2.12)
With this or any other physically reasonable definition, the integral (2.11) is
(2.13)
The phase of the path integral is thus proportional to £sign/,f, or better, to its
i
regularized version which is the "eta invariant" of Atiyah et al. [29]:
s. 
(2.14)
Thus, the phase of the path integral may be expressed in the formula
l 
exp (^ η (A^)} . 
(2.15)
-==
j/detL.
This can be made more explicit by using the Atiyah-Patodi-Singer theorem, which
for our purposes can be regarded as a formula that expresses the dependence oΐη
on the flat connection A
((ί} about which we are expanding. In fact, in the case of the
operator L_, the formula is
) - //(O)) = 
- I (AW) . 
(2.16)
Here I(A
(Cί}) is the Chern-Simons invariant of the flat connection A
(y \ as defined in
(2.5), η (0) is the eta invariant of the trivial gauge field A = 0, and c2 (G) is the value
of the quadratic Casimir operator of the group G in the adjoint representation,
normalized so that c2 (SU(N)) = 2N. The effect of this factor is to replace k in
(2.8) by k + c2(G)/2; in fact, the partition function (2.4) may now be written
2"_ e ί π η ( 0 ) / 2 , y 
ei(k + c 2 ( G ) / 2 ) I ( A W ) 
. j 
(2 17)
α
with Γα [the absolute value of the ratio of determinants in (2.8)] being the torsion
invariant of the flat connection A
(a~\
Unfortunately, although I(A
(y }) and Ty are topological invariants, η(0) is not;
it depends on the choice of a metric on Min gauge fixing. Thus, to make sense of
the phase of (2.17) requires further discussion, in the next subsection.
Before launching into that technical discussion, let us note that the computa-
tion just sketched actually has a very interesting spin-off. The fact that k in (2.8)
has been replaced by k
J
Γc2(G)/2 in (2.17) appears to be the beginning of an
explanation of the fact that in many formulas of 1 -|- 1 dimensional current
algebra, quantum corrections have the effect of replacing k by £ + c 2 ( G ) / 2 . In
turn, this is probably related to the fact that in various integrable models in 1 + 1
360 
E.Witten
dimensions, such as the sine-gordon model, the WKB approximation is exact if
one makes suitable and seemingly ad hoc changes in the values of the parameters,
analogous to replacing k by k + c 2 ( G ) / 2 .
Triυialization of the Tangenί Bundle
Now, let us discuss how the mysterious phase factor e
ίπη(0]/2 in (2.17) should be
interpreted.
First of all, η (0) is the η invariant of the L _ operator coupled to (i) some metric
g on M, and (ii) the trivial gauge field A = 0. Let d= dim G be the dimension of the
gauge group G. Since the gauge field is trivial, the L_ operator consists of d copies
of the purely gravitational L_ operator coupled to the metric only. Thus, as a
preliminary, we write
η(0) = d ηgιav, 
(2.18)
where ηgrάv is the eta invariant of the purely gravitational operator. Our
problematical phase factor is
(2.19)
Now, with a particular regularization of the Chern-Simons quantum field
theory, we have obtained the formula (2.17) which contains the ambiguous phase
factor Λ. The goal is to find a different regularization which will preserve general
covariance. Two regularizations should differ by a local counterterm, and in this
case, since the problem phase (2.19) depends on the background metric only, we
want a counterterm that depends on the background metric only. It is easy to see
that the counterterm with the right properties is a multiple of the gravitational
Chern-Simons term, which is defined (by analogy with the Yang-Mills Chern-
Simons term) as
I(g) = ΊΓ~ J Tr (ω Λ Jω -1- f ω Λ ω Λ ω) . 
(2.20)
4π M
Here ω is the Levi-Civita connection on the spin bundle of M.
 3 1(g] suffers from
an ambiguity just similar to that of the Yang-Mills Chern-Simons action. To
define I(g) as a number, one requires a trivialization of the tangent bundle of M.
Although the tangent bundle of a three manifold can be trivialized, there is no
canonical way to do this. Any two trivializations differ by an invariantly defined
integer, which is the number of relative "twists". The gravitational Chern-Simons
functional has the property that if the trivialization of the tangent bundle of M is
twisted by s units, I(g) transforms by
(2.21)
Now, the Atiyah-Patodi-Singer theorem says that the combination
(222)
{ '
2π
3 (2.20) is not the integral of an intrinsic local functional, so it would not usually arise as a
counterterm. Whether or not "counterterm" is the right word, we will have to view (2.20) as a
correction that must be added to the action if one wishes to work in the gauge DtA
l = 0
Quantum Field Theory and the Jones Polynomial 
361
is a topological invariant, depending that is on the oriented three manifold M with
a choice of trivialization of the tangent bundle, but not on the metric of M. 4 It is
clear, therefore, what we must do. We replace η(0)/2 in (2.17) by d times the
combination that appears in (2.22) [the factor of dis the one that entered in (2.19)],
so (2.17) is replaced by
— 
V e
i(k + C2(G)l2)I(A) 
T
19 
2π 
/ / ^
So, finally, we can see that the Chern-Simons partition function, at least for large
k, can be defined as a topological invariant of the oriented, framed three manifold
M (a framed three manifold being one that is presented with a homotopy class of
trivializations of the tangent bundle).
The fact that it is necessary to specify a framing of the three manifold may look
like a nuisance, but there is no real loss of information. From (2.21) we see that if
the framing is shifted by s units, the partition function is transformed by
(2.24)
A topological invariant of framed, oriented three manifolds, together with a law
for the behavior under change of framing, is more or less as good as a topological
invariant of oreinted three manifolds without a choice of framing.
Of course, all of the discussion in this section, and in particular (2.24), has been
limited to the behavior at large k. In Sect. (4.5), we will see that the generalization
of (2.24) to finite k is
(2.25)
with c being the central charge of two dimensional current algebra with symmetry
group G at level k. It is well known that the large k limit of c is exactly d.
Moduli Spaces of Flat Connections
There is still an important gap in the above discussion of the large k behavior. The
formula (2.8) is really only valid if the determinants that appear are all non-zero.
In fact, the fiat connection A
{ΰί) determines a flat bundle E. The determinants in
(2.8) are non-zero if and only if A
(a) is such that the de Rham cohomology of M,
with values in £, is zero. If H
l (M, E) φ 0, then the fiat connection A
(*
} is not
isolated but lies on a moduli space !/ of gauge inequivalent flat connections; and
the proper evaluation of the path integral (2.1) leads not to the discrete sum (2.4)
but to an integral on £f . If H
Q (M, E) is not zero, then the fields </>, c and c in the
above treatment have zero modes, and the gauge fixing requires more care. It is
plausible that by more careful study of the path integral, the large k contribution
of arbitrary flat connections can be extracted without assumptions about
H*(M,E). But we will not attempt this.
4 The crucial factor of 1/12 in (2.22) reflects the discrepancy between the Chern character
e
x = 1 + Λ-
2/2 4- ... 
that appears in gauge theory index theorems and 
the A 
genus
(x/2)/sinh(jc/2) = 1 — x
2/24 + ... that appears in gravitational index theorems
362 
E. Witten
Some Examples
We will later on determine the partition functions of some simple three manifolds,
giving results that can be compared to large k computations. For S
2 x S
1, Z = 1,
for any G and any k. For S
3 and G = SU(2), we will obtain the formula
 5
(2.26)
Of course, on S
3 the only flat connection is the trivial connection, for which (2.8) is
not valid, since H° (M, E) φ 0 in this case. For G = SU(2), the behavior Z~k~
3/2
in (2.26) is probably the general behavior of the contribution of the flat connection
for homology spheres (on which the flat connection is isolated); it would be
interesting to know how to obtain this behavior from path integrals. In Donaldson
and Floer theory, the trivial connection, which has a negative formal dimension, is
the cause of many subtleties. The vanishing of (2.26) in the classical limit of large k
appears to be an interesting quantitative reflection of the "negative dimension" of
the trivial connection.
2.1. Incorporation of Knots
We now wish to consider the large k behaviour in the presence of knots. For
simplicity, we will limit ourselves to the case of S
3, and an abelian gauge group
G = U(i). Though the abelian gauge group is relatively trivial in the context of
knot theory, it gives a quick and simple way to confirm the fact that the Chern-
Simons action really does lead to topological invariants, and it also gives a simple
context for explaining a technicality that is crucial in all that follows.
In the abelian theory, the gauge field is simply a one form A and the
Lagrangian is
^=£-τ$e
ί*AίdJAk. 
(2.27)
oπ M
We pick some circles Ca and some integers na [corresponding to representations of
the gauge group £/(!)]. As always in this paper, we assume Ca does not intersect Cb
for a^rb. We wish to calculate the expectation value of the product
W= Π expfzXj Λ) 
(2.28)
fl=l 
\ 
Cα 
/
with respect to the Gaussian measure determined by e
1^'. As was recently discussed
by Polyakov (in a paper [23] in which he proposed to apply the Abelian Chern-
Simons theory to high temperature superconductors), the result can be written in
the form
< wy = exp (^ Σ «-««. f <**' ί & ^ I~~
\
Z/C a,b 
Ca 
Cb 
\X~ y
Here one has identified a region Uof S
3 containing the knots with a region of three
dimensional Euclidean space, and x\ y
j are the Euclidean coordinates of U
The appearance of/: + 2 in this formula is presumably an illustration of the k + c2 (G)/2 in (2.17)
Quantum Field Theory and the Jones Polynomial 
363
evaluated along the knots. For a φ b, the integral in (2.29) is essentially the Gauss
linking number, which can be written as
Cb) = ~ d X
i \ jy £ i,,fc. 
(2.30)
As long as Ca and Cb do not intersect, Φ (Cfl, Cb) is a well defined integer; in fact, it
is the most classic invariant in knot theory. Thus, if we could ignore the term a = b,
we would have
(2.31)
a,b
The appearance of the Gauss linking number illustrates the fact that the Chern-
Simons theory does lead to topological invariants as we hope. But we have to
worry about the term with a — b. This integral is ill-defined near x = y\ how do we
wish to interpret it?
It is well known in knot theory that there is no natural and topologically
invariant way to regularize the self-linking number of a knot. Polyakov in [23]
used a regularization that is not generally covariant to get an answer that is
interesting geometrically but not a topological invariant. We need a different
approach for our present treatment in which general covariance is a primary goal.
Though there is no completely invariant substitute for Polyakov's regularization,
in the sense that there is no way to get a natural topological invariant from the
integral in (2.29) or (2.30) with a = b, we cannot simply throw away the self-linking
term and its non-abelian generalizations (which are sketched in Fig. 3 a), since
these terms are in fact not naturally zero. There is no reason to think that one
could retain general covariance by dropping these terms. In the abelian theory, on
a general three manifold M, on topological grounds the self-linking number can be
a non-zero fraction, well-defined only modulo one. In such a case, it cannot be
correct to set the self-linking number to zero, since it is definitely not zero.
[Topologically, in such a situation, the self-linking number is well defined only
modulo an integer, and this precision is definitely not good enough to evaluate
(2.31).] In the non-abelian theory, we will get results later which amount to
assigning definite, non-zero values to the non-abelian generalizations of the self-
linking integral, so it would not be on the right track to try to throw these terms
away.
Topologically, it is clear what data are needed to make sense of the self-linking
of a knot C. One needs to give a "framing" of C; this is a normal vector field along
C. The idea is that by displacing C slightly in the direction of this vector field one
gets a new knot C", and it makes sense to calculate the linking number of C and C' '.
This can be defined as the self-linking number of the framed knot C. One can think
of the framing as a thickening of the knot into a tiny ribbon bounded by C and C';
this is how it is drawn in Fig. 3 b. It is clear that the self-linking number defined this
way depends not on the actual vector field used to displace C to C' but only on the
topological class of this vector field; and indeed by a "framing" we mean only the
topological class. Though a choice of framing gives a definition of the self-linking
number of a knot C, it is clear that by picking a convenient framing of C one can
364
E. Witten
t=2
C BEFORE
AFTER
Fig. 3a-c. The self-linking integral is, in a non-abelian theory, the first in an infinite series of
Feynman diagrams, with gauge fields emitted and absorbed by the same knot, as in a; these all
pose similar problems. A topologically invariant but not uniquely determined regularization can
be obtained by supposing that each knot is ''framed", as in b. In c, the framing is shifted by 2 units
by making a 2-fold twist
get any desired answer for its self-linking number; as illustrated in Fig. 3c, a ί-fold
twist in the framing of C will change its self-linking by t.
 6
Physically, the role of the framing is that it makes possible what physicists
would call a point-splitting regularization. This is defined as follows: when one has
to do the self-linking integral in (2.29), one lets x run on C andj on C'. This gives a
well-defined integral, though of course it depends on the framing. In this paper, we
will assume, without proof, that the framing gives sufficient information to make
possible a consistent point-splitting regularization of all the non-abelian generali-
zations of the self-linking integral, without further arbitrary choices. This question
is, perhaps, comparable to the question of whether the non-abelian Chern-Simons
action defines a sensible quantum theory in the first place (even without
introducing Wilson lines as observables); neither of these questions will be tackled
here.
Of course, if it were always possible to pick a canonical framing of knots, then
we could pick this framing and hide the question. On 5
3, there is a canonical
framing of every knot; it is determined by asking that the self-linking number
should be zero. (This makes the abelian linking integral zero, but not its non-
abelian generalizations.) On general three manifolds, this cannot be done since the
self-linking number may be ill-defined or may differ from an integer by a definite
fraction (so that it does not vanish with any choice of framing). Even when the
canonical framing does exist, it is not convenient to be restricted to using it, since
natural operations (like the surgery we study in Sect. 4) may not preserve it.
In general, therefore, we give up on finding a natural choice, and simply pick
some framing and proceed. It would be rather unpleasing if the "physical" results
depended uncontrollably on the framing of knots. What saves the day is that
although we cannot in general make a natural choice of the framing, we can state a
general rule for how expectation values of Wilson lines change under a change of
the framing. First of all, let us note that while, in general, there is no canonical zero
in the set of possible framings of a knot in a three manifold, if one compares two
framings they always differ by a definite integer, which is the relative twist in going
6 The discussion should make it clear that the need to frame knots is analogous to the need to
frame three manifolds, as found in the last section. This hopefully justifies the use of the same
word "framing" in each case
Quantum Field Theory and the Jones Polynomial 
365
around the knot (Fig. 3c). (That is, in general there is no natural way to count how
many times the ribbon in Fig. 3 b is twisted, but there is a natural local operation of
adding t extra twists to this ribbon.) In the abelian theory, it is clear from (2.29)
and (2.30) how the partition function transforms under a change of framing. If we
shift the framing of the link Ca by t units, its self-linking number is increased by ί,
and the partition function is shifted by a phase
