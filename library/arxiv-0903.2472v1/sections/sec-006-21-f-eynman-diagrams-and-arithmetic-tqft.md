---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-006-21-f-eynman-diagrams-and-arithmetic-tqft
section_title: "F eynman diagrams and arithmetic TQFT"
section_number: 2.1
pages: 10-15
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
Let us examine more carefully each term in the perturbative e xpansion (1.8):
Z (ρ)(M ; ℏ) = exp
(
1
ℏS(ρ)
0 − 1
2δ(ρ) log ℏ +
∞∑
n=0
S(ρ)
n+1ℏn
)
. (2.1)
As already mentioned in the introduction, the leading term S(ρ)
0 is the value of the classical
Chern-Simons functional (1.9) evaluated on a ﬂat gauge conn ectionA(ρ) that corresponds
to a homomorphism ρ :π1(M )→GC. It is also easy to understand the integer coeﬃcient
δ(ρ) in (2.1). The homomorphism ρ deﬁnes a ﬂat GC bundle over M , which we denote as
Eρ. Letting H i(M ;Eρ) be the i-th cohomology group of M with coeﬃcients in the ﬂat
bundle Eρ, the coeﬃcient δ(ρ) is given by
δ(ρ) = h1−h0, (2.2)
where hi := dimH i(M ;Eρ). Both this term and S(ρ)
1 come from the “one-loop” contribu-
tion to the path integral (1.2); S(ρ)
1 can be expressed in terms of the Ray-Singer torsion of
M with respect to the ﬂat bundle Eρ (cf. [52, 5, 23]),
S(ρ)
1 = 1
2 log
(T (M ;Eρ)
2
)
. (2.3)
The geometric interpretation of the higher-order terms S(ρ)
n withn> 1 is more interest-
ing, yet less obvious. To understand it better, we note that t he saddle point approximation
to the path integral (1.2) gives an expression for S(ρ)
n as a sum of Feynman diagrams with
n loops. Since the Chern-Simons action (1.1) is cubic, all vac uum diagrams (that is, Feyn-
man diagrams with no external lines) are closed trivalent gr aphs; lines in such graphs have
no open end-points. Therefore, a Feynman diagram with n loops (n > 1) has 3( n− 1)
line segments with end-points meeting at 2( n− 1) trivalent vertices. Each such diagram
contributes an integral of the form ( cf. [3])
∫
M 2n−2
L3n−3, (2.4)
– 9 –
whereM 2n−2 denotes a product of 2 n− 2 copies of M andL3n−3 denotes a wedge product
of a 2-form L(x,y )∈ Ω 2(Mx×My; gC⊗ gC). The 2-form L(x,y ), called the “propagator,”
is a solution to the ﬁrst-order PDE,
dA(ρ )L(x,y ) = δ3(x,y ), (2.5)
where δ3(x,y ) is a δ-function 3-form supported on the diagonal in Mx×My and dA(ρ ) is
the exterior derivative twisted by a ﬂat connection A(ρ) on the GC bundle Eρ.
For example, suppose that M is a geodesically complete hyperbolic 3-manifold of ﬁnite
volume. As we pointed out in the introduction, such 3-manifo lds provide some of the most
interesting examples for Chern-Simons theory with complex gauge group. Every such M
can be represented as a quotient
M = H3/Γ (2.6)
of the hyperbolic space H3 by a discrete, torsion-free subgroup Γ ⊂PSL (2, C), which is a
holonomy representation of the fundamental group π1(M ) into Isom +(H3) = PSL (2, C).
In what follows, we call this representation “geometric” an d denote the corresponding ﬂat
PSL (2, C) connection as A(geom).
In order to explicitly describe the ﬂat connection A(geom), recall that H3 can be deﬁned
as the upper half-space with the standard hyperbolic metric
ds2 = 1
x2
3
(dx2
1 +dx2
2 +dx2
3), x 3 > 0. (2.7)
The components of the vielbein and spin connection correspo nding to this metric can be
written as
e1 = dx1
x3
w1=dx2
x3
e2 = dx2
x3
w2=− dx1
x3
e3 = dx3
x3
w3=0.
These satisfy dea +ǫabcwb∧ec = 0. It is easy to check that the corresponding PSL (2, C)
connection
A(geom) = −(w +ie) = 1
2x3
(
dx3 2dx1− 2idx2
0 −dx3
)
(2.8)
is ﬂat, i.e. obeys (1.3). In Chern-Simons theory with gauge group GC =PSL (2, C), this
gives an explicit expression for the ﬂat gauge connection th at corresponds to the hyperbolic
structure on M . In a theory with a larger gauge group, one can also deﬁne a geo metric
connectionA(geom) by embedding (2.8) into a larger matrix with extra rows and co lumns
of zero entries. We note, however, that A(geom) constructed in this way is not unique and
depends on the choice of embedding, cf. (1.11). Nevertheless, we will continue to use the
notationA(geom) even in the higher-rank case whenever the choice of embeddin g introduces
no confusion.
– 10 –
The action of Γ on H3 can be conveniently expressed by identifying a point (x1,x 2,x 3)∈
H3 with a quaternion q =x1 +x2i +x3j and deﬁning
γ :q↦→(aq +b)/(cq +d), γ =
(
a b
c d
)
∈PSL (2, C). (2.9)
Explicitly, setting z =x1 +ix2, we ﬁnd
γ(z +x3j) = z′ +x′
3j , (2.10)
where
z′ = (az +b)(¯c¯z + ¯d) +a¯cx2
3
|cz +d|2 +|c|2x2
3
, x ′
3 = x3
|cz +d|2 +|c|2x2
3
. (2.11)
Let L0(x,y ) be the propagator for H3, i.e. a solution to equation (2.5) on H3× H3
with the non-trivial ﬂat connection A(geom). Then, for a hyperbolic quotient space (2.6),
the propagator L(x,y ) can simply be obtained by summing over images:
L(x,y ) =
∑
γ∈Γ
L0(x,γy ). (2.12)
Now, we would like to consider what kind of values the perturb ative invariants S(ρ)
n
can take. For n≥ 1, the S(ρ)
n ’s are given by sums over Feynman diagrams, each of which
contributes an integral of the form (2.4). A priori the value of every such integral can
be an arbitrary complex number (complex because we are study ing Chern-Simons theory
with complex gauge group) that depends on the 3-manifold M , the gauge group GC, and
the classical solution ρ. However, for a hyperbolic 3-manifold M = H3/Γ and for the
ﬂat connection A(geom) associated with the hyperbolic structure on M , we ﬁnd that the
S(geom)
n ’s are signiﬁcantly more restricted.
Most basically, one might expect that the values of S(geom)
n ’s are periods [31]
S(geom)
n ∈P . (2.13)
HereP is the set of all periods, satisfying
Q⊂
Q⊂P⊂ C. (2.14)
By deﬁnition, a period is a complex number whose real and imag inary parts are (absolutely
convergent) integrals of rational functions with rational coeﬃcients, over domains in Rn
deﬁned by polynomial inequalities with rational coeﬃcient s [31]. Examples of periods are
powers of π, special values of L-functions, and logarithmic Mahler measures of polynomial s
with integer coeﬃcients. Thus, periods can be transcendent al numbers, but they form a
countable set, P. Moreover, P is an algebra; a sum or a product of two periods is also a
period.
Although the formulation of the perturbative invariants S(geom)
n≥1 in terms of Feynman
diagrams naturally leads to integrals of the form (2.4), whi ch have the set of periods, P,
as their natural home, here we make a stronger claim and conje cture that for n >1 the
– 11 –
S(geom)
n ’s are algebraic numbers, i.e. they take values in Q. As we indicated in (2.14), the
ﬁeld Q is contained in P, but leads to a much stronger condition on the arithmetic nat ure
of the perturbative invariants S(geom)
n . In order to formulate a more precise conjecture, we
introduce the following deﬁnition:
Deﬁnition : A perturbative quantum ﬁeld theory is called arithmetic if, for all n> 1, the
perturbative coeﬃcients S(ρ)
n take values in some algebraic number ﬁeld K,
S(ρ)
n ∈ K, (2.15)
and S(ρ)
1 ∈ Q· log K.
Therefore, to a manifold M and a classical solution ρ an arithmetic topological quan-
tum ﬁeld theory (arithmetic TQFT for short) associates an al gebraic number ﬁeld K,
(M,ρ )↝ K. (2.16)
This is very reminiscent of arithmetic topology, a program p roposed in the sixties by
D. Mumford, B. Mazur, and Yu. Manin, based on striking analog ies between number
theory and low-dimensional topology. For instance, in arit hmetic topology, 3-manifolds
correspond to algebraic number ﬁelds and knots correspond t o primes.
Usually, in perturbative quantum ﬁeld theory the normaliza tion of the expansion pa-
rameter is a matter of choice. Thus, in the notations of the pr esent paper, a rescaling
of the coupling constant ℏ→ λℏ by a numerical factor λ is equivalent to a redefnition
S(ρ)
n →λ1−nS(ρ)
n . While this transformation does not aﬀect the physics of the p erturbative
expansion, it certainly is important for the arithmetic asp ects discussed here. In particular,
the above deﬁnition of arithmetic QFT is preserved by such a t ransformation only if λ∈ Q.
In a theory with no canonical scale of ℏ, it is natural to choose it in such a way that makes
the arithmetic nature of the perturbative coeﬃcients S(ρ)
n as simple as possible. However,
in some cases (which include Chern-Simons gauge theory), th e coupling constant must obey
certain quantization conditions, which, therefore, can le ad to a “preferred” normalization
of ℏ up to irrelevant Q-valued factors.
We emphasize that our deﬁnition of arithmetic QFT is perturb ative. In particular, it
depends on the choice of the classical solution ρ. In the present context of Chern-Simons
gauge theory with complex gauge group GC, there is a natural choice of ρ when M is
a geodesically complete hyperbolic 3-manifold, namely the geometric representation that
corresponds to A(geom). In this case, we conjecture:
Conjecture 1 (Arithmeticity conjecture) : As in (2.6), let M be a geodesically com-
plete hyperbolic 3-manifold of ﬁnite volume, and let ρ = geom be the corresponding discrete
faithful representation of π1(M ) intoPSL (2, C). Then the perturbative Chern-Simons the-
ory with complex gauge group GC = PSL (2, C) (or its double cover, SL(2, C)) in the
background of a non-trivial ﬂat connection A(geom) is arithmetic on M .
– 12 –
In fact, we can be a little bit more speciﬁc. In all the example s that we studied, we
ﬁnd that, for M as in (2.6) and for all values of n> 1, the perturbative invariants S(geom)
n
take values in the trace ﬁeld of Γ,
S(geom)
n ∈ Q(tr Γ), (2.17)
where, by deﬁnition, Q(tr Γ) is the minimal extension of Q containing trγ for all γ∈ Γ. We
conjecture that this is the case in general, namely that the SL(2, C) Chern-Simons theory
on a hyperbolic 3-manifold M = H3/Γ is arithmetic with K = Q(tr Γ). This should be
contrasted with the case of a compact gauge group, where one u sually develops perturbation
theory in the background of a trivial ﬂat connection, and the perturbative invariants S(ρ)
n
turn out to be rational numbers.
Of course, in this conjecture it is important that the repres entationρ is ﬁxed, e.g. by
the hyperbolic geometry of M as in the case at hand. As we shall see below, in many cases
the representation ρ admits continuous deformations or, put diﬀerently, comes in a family.
For geometric representations, this does not contradict th e famous rigidity of hyperbolic
structures because the deformations correspond to incompl ete hyperbolic structures on M .
In a sense, the second part of this section is devoted to study ing such deformations. As
we shall see, the perturbative GC invariant Z (ρ)(M ; ℏ) is a function of the deformation
parameters, which on the geometric branch2 can be interpreted as shape parameters of the
associated hyperbolic structure.
In general, one might expect the perturbative coeﬃcients S(ρ)
n>1 to be rational functions
of these shape parameters. Note that, if true, this statemen t would imply the above
conjecture, since at the point corresponding to the complet e hyperbolic structure the shape
parameters take values in the trace ﬁeld Q(tr Γ). This indeed appears to be the case, at
least for several simple examples of hyperbolic 3-manifold s that we have studied.
For the arithmeticity conjecture to hold, it is important th at ℏ is deﬁned (up to Q-
valued factors) as in (1.7), so that the leading term S(ρ)
0 is a rational multiple of the classical
Chern-Simons functional, cf. (1.9). This normalization is natural for a number of reasons .
For example, it makes the arithmetic nature of the perturbat ive coeﬃcients S(ρ)
n as clear
as possible. Namely, according to the above arithmeticity c onjecture, in this normalization
S(geom)
1 is a period, whereas S(geom)
n>1 take values in Q. However, although we are not going
to use it here, we note that another natural normalization of ℏ could be obtained by a
redeﬁnition ℏ → λℏ with λ ∈ (2πi)−1· Q. As we shall see below, this normalization
is especially natural from the viewpoint of the analytic con tinuation approach. In this
normalization, the arithmeticity conjecture says that all S(geom)
n>1 are expected to be periods.
More speciﬁcally, it says that S(ρ)
n ∈ (2πi)n−1· Q, suggesting that the n-loop perturbative
invariantsS(geom)
n are periods of (framed) mixed Tate motives Q(n− 1). In this form, the
arithmeticity of perturbative Chern-Simons invariants di scussed here is very similar to the
motivic interpretation of Feynman integrals in [7].
Finally, we note that, for some applications, it may be conve nient to normalize the
path integral (1.2) by dividing the right-hand side by Z(S3; ℏ). (Since π1(S3) is trivial,
2i.e. on the branch containing the discrete faithful representat ion.
– 13 –
we have Z(S3; ℏ) = Z (0)(S3; ℏ).) This normalization does not aﬀect the arithmetic nature
of the perturbative coeﬃcients S(geom)
n because, for M = S3, all the S(0)
n ’s are rational
numbers. Speciﬁcally,
Z(S3; ℏ) =
( ℏ
iπ
) r/2(Vol Λ wt
Vol Λ rt
) 1/2 ∏
α∈Λ +
rt
2 sinh (ℏ(α·̺)), (2.18)
where the product is over positive roots α∈ Λ +
rt,r is the rank of the gauge group, and ̺ is
half the sum of the positive roots, familiar from the Weyl cha racter formula. Therefore, in
the above conjecture and in eq. (2.17) we can use the perturba tive invariants of M with
either normalization.
The arithmeticity conjecture discussed here is a part of a ri cher structure: the quan-
tum GC invariants are only the special case x = 0 of a collection of functions indexed by
rational numbers x which each have asymptotic expansions in ℏ satisfying the arithmetic-
ity conjecture and which have a certain kind of modularity be havior under the action of
SL(2, Z) on Q [59]. A better understanding of this phenomenon and its inte rpretation will
appear elsewhere.
