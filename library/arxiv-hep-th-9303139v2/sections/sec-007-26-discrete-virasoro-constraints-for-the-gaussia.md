---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-007-26-discrete-virasoro-constraints-for-the-gaussia
section_title: "Discrete Virasoro constraints for the Gaussian Kontsevich model"
section_number: 2.6
pages: 2-32
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
2.7. Continuous Virasoro constraints for the V = X3
3 Kontsevich model
2.8. ˜W-constraints for the asymmetric 2-matrix model
2.9. ˜W-constraints for generic 2-matrix model
2.10. ˜W-operators in Kontsevich model
3. Eigenvalue models
3.1. What are eigenvalue models
3.2. 1-matrix model
3.3. Itzykson-Zuber and Kontsevich integrals
3.4. Conventional Multimatrix models
3.5. Determinant formulas for eigenvalue models
3.6. Orthogonal polinomials
3.7. Two-component models in Miwa parametrization
3.8. Equivalence of the discrete 1-matrix and Gaussian Kontsevich models
3.9. Volume of unitary group
4. Integrable structure of eigenvalue models
4.1. The concept of integrability
4.2. The notion of τ-function
4.3. τ-functions, associated with free fermions
4.4. Basic determinant formula for the free-fermion correlator
4.5. Toda-lattice τ-function and linear reductions of Toda-lattice hierar-
chy
4.6. Fermion correlator in Miwa coordinates
4.7. Matrix models versus τ-functions.
4.8. String equations and generic concept of reduction
4.9. On the theory of GKM
4.10 1-Matrix model versus Toda-chain hierarchy
5. Continuum limits of discrete matrix models
2
5.1. What is continuum limit
5.2. From Toda-chain to KdV
5.3. Double-scaling limit of 1-matrix model
5.4. From Gaussian to X3-Kontsevich model
6. Conclusion
7. Acknowledgements
8. References
3
1
Introduction
The purpose of these notes is to review one of the branches of modern string
theory: the theory of matrix models with the emphasize on their intrinsic
integrable structure. We begin with a brief description of the ﬁeld and its
place in the closest environement within entire string theory.
The main content of the string theory 2 is the study of symmetries in
the broadest possible sense of the word by methods of the quantum ﬁeld
theory. The usual scheme is to start from some symmetry and construct a
ﬁeld-theoretical model (usually 2-dimensional, for the reason that we do not
discuss here), which possesses this symmetry in some simple sense (e.g. as
Noether symmetry or as a chiral algebra). The main idea at this stage is to
ﬁnd a model which is exactly solvable (if nothing but the symmetry is given
this is a nice principle to restrict dynamics). The next step is to study the
hidden symmetries of the model, which are somehow responsible for its exact
solvability and are usually much larger than the original symmetry.
This ”inverse” step: model −→symmetry can be made at least with three
diﬀerent ideas in mind.
One can look for some hidden local (gauge) symmetry of the model, which
is ﬁxed or spontaneously broken, i.e. identify it with some other model which
had more ﬁelds - auxiliary from the point of view of the smaller model and
gauge - from that of the larger one. (Examples: gauged Wess-Zumino-No-
vikov- Witten (WZNW) model, topological theories in BRST formalism etc.)
One can take for a new (full) symmetry of the model just its operator
algebra (algebra of observables) (see [2], [3] and also [4] for the ﬁrst results
in this direction).
It deserves mentioning that gauging of entire algebra
of observables gives rise to a ”string ﬁeld theory”, associated with original
model (considered as a string model).
One can construct eﬀective action of the theory by exact evaluation of
the functional integral.
As to direct step symmetry −→model, one can take as example the best
understood case, when original symmetry is just a Lie algebra. Then the
quantum mechanical model can be constructed by geometrical quantization
technique (see [5] for the most important example of Kac-Moody algebra and
the WZNW model).
2See [1] for a general review
1
From the mathematical point of view the two elements of the above
scheme look like algebra (theory of symmetries) and Analysis & Geometry
(ﬁeld-theoretical models). The idea of constructing models with a given sym-
metry (and nothing else relevant for the dynamics) can be identiﬁed with the
mathematical concept of ”universal objects”.
|
SY MMETRY
|
=
|
ALGEBRA
|
↑
↓
|
MODEL
|
=
|
ANALYSIS
|
| with this symmetry |
|
GEOMETRY
|
Theory of everything
The sequence of iterations of the two arrows in the picture leads to
a deaper understanding, enlargening and generalization of all the notions
involved: symmetry, exact solvability, ﬁeld theory, geometrical structures,
quantization etc, thus stimulating considerable progress both in physics and
mathematics. If this iterative process can somehow converge, the limit point
will deserve the name of the theory of everything, which will indeed unify all
the possible ﬁeld theoretical models by embedding them into a huge, but well
structuired theory, which will be also exactly solvable in some, yet unspeciﬁed
sense of the word. We refer to [1] for more details about this semiphilosoph-
ical programm, known under the name of (modern) string theory, and now
turn to a more narrow subject: the theory of matrix models.
At the moment it is mainly associated with the theory of eﬀective ac-
tions, at least so far this is where the main results of the modern theory of
matrix models ﬁnd their applications. This technique is especially suited for
the study of eﬀective actions, obtained after integration over 2-dimensional
geometries (including the sum over genera) and it produces non-perturbative
(exact) partition functions of particular string models. The main result of
these studies points out that these partition functions exhibit two remarkable
(though expected [6]) properties:
First, eﬀective action for a given model is essentially the same as for
any other model. In fact eﬀective action is a function of coupling constants
2
(”sources” in the old-fashioned terms), which are nothing but coordinates
in the space of various models (conﬁguration space of entire string theory):
variation of couplings change one model for another.
Second, eﬀective action possesses a huge additional symmetry, which is
somewhat similar to the general covariance in the space of all models (the
above mentioned conﬁguration space) and in the simplest examples, which
have been studied so far, can be expressed in terms of integrable hierarchies.
(This ”general covariance” in the conﬁguration space can after all turn into
the main dynamical principle of the string theory.)
Both these features seem to be very general, arising whenever the largest
possible Lagrangian with a given symmetry is considered (without restric-
tions on the possible counterterms, imposed by requirements of renormaliz-
ability or by locality-minimality ”principles” - this is why this phenomenon
is not widely known to ﬁeld theorists). An example of highly-nontrivial cal-
culations leading to similar conclusions can be found in ref.[7].
We hope that these remarks will become more clearer after some speciﬁc
examples will be considered below. Still they deserve being fromulated in
the full generality, not only to intrigue the reader, but also because they can
serve for better understanding of the ideas and outcomes of generic string
theory.
The ”corner” of the string theory, associated with matrix models, can be
described by the following picture: see Fig.1.
The big blocks within the body of string theory, which are directly re-
lated to matrix models are: theory of conformal models, that of the N = 2
supersymmetry and the (loop-equation version of) the Yang-Mills theory (in
any dimension). Also the Einstein gravity should be related to the subject
in a way, similar to Yang-Mills theory, but these links are yet not clariﬁed.
Both conformal theory and N = 2 supersymmetry are sources of the con-
cept of ”topological models” [8]-[11]. These arise after gauging of all contin-
uous symmetries of the WZNW models and/or as models with BRST-exact
stress tensors, naturally appearing in the context of N = 2 supersymmetry.
If formulated in a self-consisted way in the ”universal module space” (uni-
ﬁcation of module spaces of all ﬁnite-genus Riemann surfaces and bundles
over them) these models turn into those of ”topological gravity”. Generating
functionals of topological gravity models in fact generate inﬁnite sequences
3
of topological invariants of certain spaces (inverse deﬁnition is also possible
in some cases [8], though the universal (generic) algorithm for the operation
topology of some space −→topological gravity is not yet formulated).
Alternative models of 2d quantum gravity arise straightforwardly from
conformal models through a procedure of ”summation over geometries”.
There are two essentially diﬀerent approaches to the problem. One (”Polyakov
approach”) is to make use of the complex structure, intrinsic for conformal
theory [12] and sum over Riemann surfaces, what involves integration over
module spaces and sum over genera. The main technique used in this ap-
proach is the theory of free ﬁelds on Riemann surfaces [13], [14] and bosoniza-
tion formalism for conformal ﬁeld theories [15], [16]. This approach requires
solution of Liouville theory, which still remains a problem under intensive
investigation (in turn related to conformal ﬁeld theory). Further progress in
this direction should be related (or can be expressed in terms of) the adequate
theory of the universal module space, handle-gluing operators etc. Similar ob-
jects arise in the ﬁeld-theoretical approach to the topological gravity (see [17]
for a recent review).
Alternative approach to summation over geometries does not refer at all
to the complex structure and instead involves a sum over random equilateral
triangulations [18]-[20]. 3 This is the place where matrix models ﬁrst appear
in the context of string theory. The random triangulation approach is by no
means speciﬁc for conformal models (since it ignores the complex structure)
and can be applied in many other situations - for example, to Yang-Mills
(YM) theories in any dimensions (where instead of summation over geome-
tries one needs ”simply” to sum over ordinary Feynman diagramms).
Applications of the matrix-model method usually involve two steps: for-
mulation and the study of ”discrete” model and then taking its ”continuum
limit”, giving rise to a new - ”continuous matrix model”, which sometimes
can again be represented in a form of some matrix integral.
One of the main discoveries in the ﬁeld of matrix models is that continuous
3Its relation to the Polyakov approach is a separate very interesting, important and
badly understood problem, which allows a non-trivial reformulation in terms of num-
ber theory (see [21]). The main puzzle here is that equilateral triangulations are in fact
arithmetic Riemann surfaces - a dense discrete subset in the entire module space, with
interesting and deap algebraic properties. Equivalence of the two approaches to 2d quan-
tum gravity should imply the existence of some number-theoretical background behind
the scene, which would be very nice to discover in full purity.
4
models arising ﬁnally from the random-equilateral-triangulation description
of the simplest (minimal with c < 1) string models coincide with the sim-
plest (CP 1 Landau-Ginzburg) models of topological gravity [9],[22]-[24]: two
(classes of) theories are identical (this is not yet proved in full detail, but is
more than plausible).
So far continuous models are actually found and somehow understood
only for string models, based on the c < 1 minimal conformal theories (more-
over, only for q = 1 in the (p, q)-seria). Conformal models with c ≥1, which
are relevant for description of gauge theories in space-time dimension d ≥2
(which possess particles, rather than only topological degrees of freedom),
should give rise to the discrete matrix models with ”non-factorizable” inte-
gration over ”angular variables”, of which the simplest (solvable) example is
Kazakov-Migdal model [25]. The issue of continuum limit for such models is
yet not understood (at least in terms of integrable structures, which should
probably generalize the familiar theory of Toda hierarchies).
The goal of the study of matrix models is three-fold. First of all, one can
look for the non-perturbative (exact) answers for the physical amplitudes in
the given model. This is the subject which attracts most attention in the
literature (for several obvious reasons). However, it is equally (and, perhaps,
even more) important to understand the mathematical structure behind the
matrix models (which involves topics like general theory of integrable hierar-
chies, geometrical quanization, Duistermaat-Heckman theorem (”localization
theory”) etc). Also important for the purposes of string theory is to use the
results of the study of matrix models in order to unify a priori diﬀerent mod-
els (according to the above mentioned principle: non-perturbative partition
functions for diﬀerent models diﬀer by a change of variables in the space
of coupling constants). Matrix models already played an important role in
making this principle more clear and acceptable for many string theorists.
Let us make the next step and look even closer at the ﬁeld of matrix
models, especially, at its mostly studied domain, associated with the d < 2
string models. Then the following structure will be seen: Fig.2.
The sample example of matrix model is that of 1-matrix integral
ZN{t} ≡cN
Z
N×N dHe
P∞
k=0 tkTrHk,
(1.1)
5
where the integral is over N × N Hermitian matrix H and dH = Q
i,j dHij.
There are three directions in which one can proceed starting from (1.1).
The ﬁrst one [26] is to look for an invariant formulation of properties
of the functional ZN{t}. It appears to satisfy the inﬁnite set of diﬀerential
equations (in fact these are just Ward identities for the functional integral
(1.1) [27]):
LnZN{t} = 0,
n ≥−1,
Ln ≡
P∞
k=0 ktk
∂
∂tk+n +
Pn
k=0
∂2
∂tk∂tn−k ,
(1.2)
∂
∂t0ZN = NZN,
which is known under the name of ”discrete Virasoro constraints”. ZN{t}
can be represented as a correlator of screening operators in some auxiliary
conformal model (of one free ﬁeld on the ”spectral surface”), and Virasoro
constraints (1.2) are of course related to the Virasoro algebra in that con-
formal model.
Also ZN{t} is some τ-function of integrable ”Toda-chain”
hierarchy (in fact this statement should be a corollary of the Virasoro con-
straints, but this relation is still not very well understood).
The most straightforward further developement [26],[28] is to take the
continuum limit of the Toda-chain hierarchy. In the specially adjusted (”double-
scaling”) limit [20]) it gives rise to the KdV-hierarchy, and the correspond-
ing τ-function appears subjected to the slightly diﬀerent constraints [29],[28]
(which again form a Borel subalgebra of some other ”continuous Virasoro
algebra”):
L2nZcont{T} = 0,
n ≥−1,
L2n ≡1
2
P∞
odd k=1 k(Tk + rk)
∂
∂Tk+2n + 1
4
P2n−1
odd k=1
∂2
∂Tk∂T2n−k +
+ 1
16δn,0 + 1
4(T1 + r1)2δn,−1,
(1.3)
where rk = −2
3δk,3. In fact
Zcont{T} ∼
lim
d.s.{N→∞}
q
ZN{t}

t2k+1=0
,
(1.4)
and T are related to t by linear transformation [19],[28]:
Tk = 1
2
X
m≥k−1
2
gm
(m −k−1
2 )!
Γ(m + 1
2)
Γ( k
2 + 1) ,
k odd;
gm = mt2m, m ≥1;
g0 = 2N.
(1.5)
6
This Zcont{T} can be again represented in the form of a matrix integral (over
n × n Hermitian matrix) [22],[30]-[33]:
Zcont{T} = ZV {T}
(1.6)
with V (X) = X3
3 , where
ZV {T} ∼FV,n{L} ≡
Z
n×n dXe−trV (X)+trLX
(1.7)
and
Tk = 1
ktrL−k/2,
k odd.
(1.8)
The function ZV {T} (but not FV,n{L}) is in fact independent of n: the
only thing that happens for ﬁnite values of n is that the r.h.s. of (1.7) can
not describe ZV {T} at arbitrary points in the T-space, in accordance with
(1.8). Continuous Virasoro constraints (1.3) are in fact equivalent to the
trivial matrix-valued Ward identity
 
V ′
 ∂
∂Ltr
!
−L
!
FV,n{L} = 0.
(1.9)
Another direction to proceed from the discrete 1-matrix model is to
rewrite it identically in the form of Kontsevich model: this time with V (X) =
X2 and additional factor of (det X)N aunder the integral in FV,n{L} [56].
Then the double scaling limit can be studied in internal terms of Kontsevich
models [36].
The third direction is towards multimatrix models. In continuous version
they should provide τ-functions of reduced KP-hierarchies [37] (KdV is the
p = 2 reduction), which are subjected to ”continuous W-constraints” [29].
Matrix models of such τ-functions are Kontsevich models with V (X) ∼Xp+1
[30]-[33]. At discrete level, however, things are not so simple. The most
popular discrete multimatrix models [34] are deﬁned as the multiple matrix
integrals of the form:
ZN{t(α)} ≡
cp−1
N
Z
N×N dH(1)...dH(p−1)
p−1
Y
α=1
e
P∞
k=0 t(α)
k
TrHk
(α)
p−2
Y
α=1
eTrH(α)H(α+1)
(1.10)
7
(the form of the ”interaction term” TrH(α)H(α+1) is restricted by the ”solv-
ability” principle, but not unambiguously). In fact these models are particu-
lar examples of the ”scalar-product eigenvalue models” and are not really dis-
tinguished except for the 1-matrix (p = 2) and 2-matrix (p = 3) cases. This
is reﬂected in the absense of any reasonable Ward identites and integrable
structures for these models, which would somehow involve their dependence
on the variables t(α) with 2 ≤α ≤p −2. Therefore the ”multi-scaling con-
tinuum limit” of these models can hardly be investigated at any degree of
rigourousness. (It is not so much important for ”physical” applications to
have any discrete models associated with the continuum ones, but this is an
interesting problem for the ”science for science”.) For the 2-matrix (p = 3)
case the Ward identities can be expressed in the form of ” ˜W-constraints”
[38] and look like [30]
˜W (m+1)
n−m {t}ZN{t, ¯t} = (−)m+n ˜W (n+1)
m−n {¯t}ZN{t, ¯t}
(1.11)
(here t and ¯t stand for t(1) and t(2), and m, n are any non-negative integers).
The really interesting set of discrete multimatrix models does exist, but
it is somewhat diﬀerent from (1.10). These theories will be refered to as
”conformal matrix models”, since they arise straightforwardly as general-
ization of the ”CFT-formulation” of the 1-matrix model [39]: it is enough
to substitute discrete Virasoro constraints in the theory of one free ﬁeld by
the Wp-constraints in the theory of p −1 free ﬁelds. Matrix integral for-
mulation then involves an ”interaction term” Det

H(α) ⊗I −I ⊗H(α+1)
instead of eTrH(α)H(α+1), which is not very easy to guess a priori, but so
deﬁned models and their continuum limits can be examined in a manner,
quite parallel to the one-matrix case (though not all is already done in
this direction). Also this approach opens a possibility to formulate discrete
models for any set of constraints, e.g. assosiated with the more exotic W-
algebras and with quantum groups (i.e.can help to solve the inverse problem:
constraints
−→
discrete matrix model). This is an option which also
deserves further investigation. Another natural name for this set of theoris
is ”multi-component eigenvalue models”.
Kontsevich models should be also related to topological models of Landau-
Ginzburg gravity (LGG), though this relation is not yet clariﬁed in full detail
(see, however [40],[17]) .
Among the main unresolved puzzles in this whole ﬁeld is the description of
8
generic (p, q)-models. Formally, Generalized Kontsevich model (1.7) provides
this description, but in fact the partition function (τ-function) gets singular
when the ”phase transition” point where the q changes is approached, and
Kontsevich model with V (X) = polinomial of degree p + 1 provides a nice
description only of (p, 1)-models. Generically, Kontsevich integral describes
a duality transformation between (p, q) and (q, p) models: (p, q) −→(q, p)
[41], but not any of these models separately. (The only exclusion are (p, 1)-
models because they are related by Kontsevich transformation to the (1, p)
models which are completely trivial.)
In fact continuous models have two different sets of ”time-variables”.
Thus far we introduced T, which are essentially expansion parameters of the
generating functional for correlation functions. More exact, these parameters
ˆT depend on the particular model (vacuum), around which the perturbation
expansion is performed, and they diﬀer slightly from the model-independent
T. Another set of ”times”, rk =
p
k(p−k)Res (V ′(µ))1−k
p dµ, parametrizes the
shape of the polinomial ”potential” Vp(X) (of degree p + 1) and it describes
the coordinates in the space of (matrix) models. These two types of variables
- parameters of the generating functional and those labeling the shape of the
Lagrangian - are almost the same (in fact they would be just the same, if
there were no loop (quantum) eﬀects). This similarity between T’s and r’s is
reﬂected in the remarkable property of partition function of the (p, 1) model
- it essentially depends only on the sum of ”times” ˆT and r [40]:
ZVp{T} = fp(r | ˆTk + rk)τp{ ˆTk + rk}
(1.12)
with some simple (and explicitly known) function fp. (In eq.(1.8) above for
monomial cubic potential V3(x) =
x3
3 ,
ˆTk = Tk =
1
ktrL−k/2, while rk =
−2
3δk,3.)
The last thing to be mentioned in this general description of the ﬁeld
of the matrix model theory is their relation to group theory. Generalized
Kontsevich model (1.7) is intimately connected to the ”integrable nature”
of group chracters and the coadjoint orbit integrals (characters of all the
irreducible representations of U(N) are usually KP τ-functions [101]). In
fact some ”discrete (or quantum) version” of Kontsevich integral is a sum
over all unitary irreps of U(n) (”integral” over a model of U(n), or over the
9
set of all coadjoint orbits):
F qu
V {G} ≡
X
R
dRχR(G)e−P∞
k=0 vkCk(R),
(1.13)
where dR, χR and Ck(R) stand for dimension, character and the k-th Casimir
of irreducible representation R of U(n). Time variables Tk ∼1
ktrGk, while
potential V (X) = P∞
k=0 skXk. This expression can be further generalized to
F qu
V {G} ≡
X
R
χR( ¯G)χR(G)e−P∞
k=0 vkCk(R).
(1.14)
Properties of these ”quantum” Kontsevich models deserve further investiga-
tion (objects like (1.13) are also known to arise in the localization theory, in
particular, in the study of the d = 2 YM theory, see, for example, [43] and
[44]).
These notes are essentially a review of the views and results of the group,
working at Moscow (and Kiev). Since references will not be given every time,
I present here the list of people involved into these investigations:
L.Chekhov, A.Gerasimov, A.Losev, S.Kharchev, Yu.Makeenko, A.Mar-
shakov, A.Mikhailov, A.Mironov, A.Orlov, S.Pakuliak, I.Polyubin, A.Zab-
rodin.
I also apologize for the somewhat sporadic references to the works of other
groups.
2
Ward identities for the simplest matrix mod-
els
2.1
Ward identites versus equations of motion
We begin systematic consideration of matrix models from their simplest and
at the same time the most basic property: the Ward identites (WI) for
partition functions. Partition function is by deﬁnition a functional of the
coupling constants in the Lagrangian and WI will be understood here as
(diﬀerentiual or ﬁnite-diﬀerence) equations, imposed on this functional. If
10
partition function is represented in the form of a matrix integral, 4 the WI
are usually implied by its invariance (or, better to say - covariance) under
the change of the integration variables (thus the name ”WI”).
In ordinary ﬁeld theory we are usually dealing with models, where WI
either do not exist at all, or at most there is ﬁnite number of them - then
they are interpreted as reﬂecting the symmetry of the theory. However, by
no means the ﬁnite set of these WI provides a complete description of dy-
namics of the theory: the number of (quantum) equations of motion (EqM)
is usually inﬁnite and their solutions are never ﬁxed by the WI. In fact this
diﬀerence between WI and EqM arises because the Lagrangians, considered
in the ordinary ﬁeld theory are not of the most general form: they are usu-
ally severely restricted by ”principles” like renormalizability or minimality.
Because of this there is simply not many enough coupling constants in the
Lagrangian to describe the result of any variation of integration variables as
that of the variation of coupling constants, and thus not every equation of
motion can be represented as (diﬀerential) equation for the partition function.
In other words, by restricting the shape of Lagrangian for ”non-symmetric”
reasons one breaks the original huge ”symmetry” (covariance) of the model,
which was enough to describe all the dynamics (all EqM) as dictated by
symmetry,- and a broader view is necessary in order to recognize EqM as the
WI, associated with that original high symmetry. This symmetry (it is not of
Noether type, of course) is peculiar property of all the quantum mechanical
partition functions, since these usually arise from the procedure of functional
integration.
It happened so that matrix models appeared to be the ﬁrst class of
quantum-mechanical systems (functional integrals) for which this identity:
all EqM ≡all WI
4To avoid confusion we emphasize that such representation does not need to exist, at
least in any simple form. The more the theory of matrix models develops, the less it has
to do with matrices and matrix integrals. However (as in the case of entire string theory)
original name has a tendency to survive. Anyhow, the main content of the theory of matrix
models (at least of its branch, analyzed in these notes) is the search for invariant formu-
lations of the properties of partition functions, while matrix integrals (if at all existing)
are considered as their particular realizations (representations). Moreover, there can exist
very diﬀerent matrix integral representations of the same partition function, the simplest
example being just the basic discrete 1-matrix model, which can be also represented in
the form of Kontsevich integral (see below).
11
was not simply observed as a curious phenomenon, but became a subject
of intensive investigation and is identiﬁed as the source of exact solvability
(integrability) of the theory. Of course, signiﬁcance of this observation (and
its implications) is quite universal, by no means restricted to the ﬁeld of
matrix models themselves, however, it is yet not enough appreciated by the
experts in other ﬁelds. In any case, we are going to deal only with matrix
models in these notes.
We proceed to consideration of the WI according to the following plan
(not all the arrows will be actually discussed): see Fig.3.
2.2
Virasoro constraints for the discrete 1-matrix model
The basic example [26],[27] which illustrates the arguments from the previous
subsection is provided by the 1-matrix model
ZN{t} ≡cN
Z
N×N dHe
P∞
k=0 tkTrHk.
(2.1)
This integral is invariant under any change of variables H →f(H). It is
convenient to choose the special basis in the space of such transformations:
δH = ǫnHn+1.
(2.2)
Here ǫn is some inﬁnitesimal matrix and, of course, n ≥−1. The value of
integral can not change under the change of integration variable, and we
obtain the identity:
Z
N×N dHe
P∞
k=0 tkTrHk =
Z
d(H + ǫnHn+1)e
P∞
k=0 tkTr(H+ǫnHn+1)k,
i.e.
Z
dHe
P∞
k=0 tkTrHk
 ∞
X
k=0
ktkTrHk+n + TrδHn+1
δH
!
≡0.
(2.3)
In order to evaluate the Jacobian TrδHn+1
δH
let us restore the matrix indices:
(δHn+1)ij =
n
X
k=0
(HkδHHn−k)ij =
n
X
k=0
(Hk)il(δH)lm(Hn−k)mj.
12
In Tr δHn+1
δH
one should take l = i and m = j, so that
TrδHn+1
δH
=
n
X
k=0
TrHkTrHn−k.
(2.4)
Now we can note that since we started from Lagrangian of the most
general form (consistent with the symmetry H →UHU†), any correlation
function can be obtained as variation of the coupling constants (all possible
sources are included as counterterms). In our particular example this is just
a trivial remark:
< TrHa1...TrHan > =
R dHe
P∞
k=0 tkTrHkTrHa1...TrHan =
=
∂n
∂ta1...∂tan ZN{t}.
(2.5)
We can use this relation together with (2.4) in order to rewrite (2.3) as:
LnZN{t} = 0,
n ≥−1
(2.6)
with
Ln ≡
∞
X
k=0
ktk
∂
∂tk+n
+
n
X
k=0
∂2
∂tk∂tn−k
.
(2.7)
Note that according to the deﬁnition (2.1)
∂
∂t0
ZN = NZN.
Several remarks are now in order.
First of all, expression in brackets in (2.3) represents just all the equations
of motion for the model (2.1), and (2.6) is nothing but another way to rep-
resent the same set of equations. This is an example of the above-mentioned
identiﬁcation of EqM and WI.
Second, commutator of any two operators Ln apearing in (2.6) should also
annihilate ZN{t}. It is another indication (not a convincing one, however)
that we already got a complete set of constraints, that Ln’s form a closed
(Virasoro) algebra:
[Ln, Lm] = (n −m)Ln+m,
n, m ≥−1.
(2.8)
13
Third, (2.6) can be considered as invariant formulation of what is ZN: it is
a solution of this set of compatible diﬀerential equations. From this point
of view eq.(2.1) is rather a particular representation of ZN and it is sensible
to look for other representations as well (we shall later discuss two of them:
one in terms of CFT, another in terms of Kontsevich integrals).
Fourth, one can try to analyze the uniqueness of the solutions to (2.6).
If there are not too many of them the set of constraints can be considered
complete. A natural approach to classiﬁcation of solutions to the algebra of
constraints is in terms of the orbits of the corresponding group [45]. Let us
consider an oversimpliﬁed example, which can still be usefull to understand
implications of the complete set of WI as well as clarify the meaning of classes
of universality and of integrability.
Imagine, that instead of (2.6) with Ln’s deﬁned in (2.7) we would obtain
somewhat simpler equations: 5
lnZ = 0,
n ≥0 with ln =
∞
X
k=1
ktk
∂
∂tk+n
.
Then operator l1 can be interpreted as generating the shifts
t2 −→t2 + ǫ1t1,
t3 −→t3 + 2ǫ1t2,
.
We can use it to shift t2 to zero, and eq. l1Z = 0 then implies that
Z(t1, t2, t3, ...) = Z(t1, 0, ˜t3, ...)
(˜tk = tk −(k−1)t2tk−1
t1
, k ≥3).
Next, operator l2 generates the shifts
t3 −→t3 + ǫ2t1,
t4 −→t4 + 2ǫ2t2,
.
5One can call them ”classical” approximation to (2.6), since they would arise if the
variation of measure (i.e. a ”quantum eﬀect”) was not taken into account in the derivation
of (2.6). Though this concept is often used in physics it does not have much sense in the
present context, when we are analyzing exact properties of functional (matrix) integrals.
14
and does not aﬀect t2. We can now use eq. l2Z = 0 to argue that
Z(t1, t2, t3, t4, ...) = Z(t1, 0, ˜t3, ˜t4, ...) = Z(t1, 0, 0,˜˜t4, ...)
etc. Assuming that Z is not very much dependent on tk with k →∞, 6 we
can conclude, that
Z(t1, t2, t3, ...) = Z(t1, 0, 0, ...) = Z(1, 0, 0, ...)
(at the last step we also used the equation l0Z = 0 to rescale t1 to unity).
All this reasoning was correct provided t1̸ = 0. Otherwise we would get
Z(0, 1, 0, 0, ...), if t1 = 0, t2̸ = 0, or Z(0, 0, 1, 0, ...), if t1 = t2 = 0, t3̸ = 0 etc.
In other words, we obtain classes of universality (such that the value of parti-
tion function is just the same in the whole class), which in this oversimpliﬁed
example are labeled just by the ﬁrst non-vanishing time-variable. Analysis
of the orbit structure for the actually important realizations of groups, like
that connected to eq.(2.7) has never been performed in the context of matrix
model theory. It may deserve emphasizing that the constraints, as we saw,
can actually allow one to eliminate (solve exactly) all the dependence on the
time-variables, in less trivial examples they somehow imply the integrabil-
ity structure, which is just a slightly more complicated version of the same
solvability phenomenon.
2.3
CFT formulation of matrix models
Given a complete set of the constraints on partition function of inﬁnitely
many variables which form some closed algebra we can now ask an inverse
question: how these equations can be solved or what is the integral repre-
sentation of partition function. One approach to this problem is analysis of
orbits, brieﬂy mentioned at the end of the previous section. Now we turn
to another technique [39], which makes use of the knowledge from conformal
ﬁeld theory. This constructions can have some meaning from the ”physi-
cal”point of view, which implies certain duality between the 2-dimensional
world surfaces and the spectral surfaces, associated to conﬁguration space of
the string theory. However, our goal now is more formal: to use the means
of CFT for solution of the constraint equations.
6This, by the way, is hardly correct in this particular example, when the group has no
compact orbits.
15
This is very natural in the case when the algebra of constraints is Virasoro
algebra, as in the case of the 1-matrix model, or some other algebra if it is
known to arise naturally as chiral algebra in some simple conformal models.
In fact the approach which will be now discussed is rather general and can
be applied to construction of matrix models, associated with many diﬀerent
algebraic structures.
We begin from the set of equations (2.6) which we shall further refer to as
”discrete Virasoro constraints”. The CFT formulation of interest should pro-
vide the solution to these equations in the form of some correlation function
in some conformal ﬁeld theory. Of course, it becomes natural, if we somehow
identify the operators Ln, which form Virasoro algebra with the harmonics
of the stress-tensor Tn, which satisfy the same algebra, and manage to relate
the constraint that Ln annihilate the correlator to the statement that Tn
annihilate the vacuum state. Thus the procedure is naturally split into two
steps: First we should ﬁnd a t-dependent operator (”Hamiltonian”) H(t),
such that
Ln(t)⟨eH(t) . . . = ⟨eH(t)Tn . . .
(2.9)
This will relate diﬀerential operators Ln to Tn’s expressed through the ﬁelds
of conformal model. Second we need to enumerate the states, that are anni-
hilated by the operators Tn with n ≥−1, i.e. solve equation
Tn | G⟩= 0
(2.10)
for the ket-states, what is an internal problem of conformal ﬁeld theory. If
both ingredients H(t) and | G⟩are found, solution to the problem is given
by
⟨eH(t) | G⟩.
(2.11)
To be more explicit, for the case of the discrete Virasoro constraints we
can just look for solutions in terms of the simplest possible conformal model:
that of a one holomorphic scalar ﬁeld
φ(z) = ˆq + ˆp log z +
X
k̸=0
J−k
k zk
[Jn, Jm] = nδn+m,0,
[ˆq, ˆp] = 1.
(2.12)
16
Then the procedure is as follows: Deﬁne vacuum states
Jk|0⟩= 0,
⟨N|J−k = 0,
k > 0
ˆp|0⟩= 0,
⟨N|ˆp = N⟨N|,
(2.13)
the stress-tensor
T(z) = 1
2[∂φ(z)]2 =
X
Tnz−n−2,
Tn =
X
k>0
J−kJk+n + 1
2
X
a+b=n
a,b≥0
JaJb,
(2.14)
and the Hamiltonian
H(t) =
1
√
2
P
k>0 tkJk =
1
√
2
H
C0 U(z)J(z)
U(z) =
P
k>0 tkzk,
J(z) = ∂φ(z).
(2.15)
It can be easily checked now that
Ln⟨N|eH(t) . . . = ⟨N|eH(t)Tn . . .
(2.16)
and
Tn|0⟩= 0,
n ≥−1.
(2.17)
As an immediate consequence, any correlator of the form
ZN{t | G} = ⟨N|eH(t)G|0⟩
(2.18)
gives a solution to (2.6) provided
[Tn, G] = 0,
n ≥−1.
(2.19)
In fact operators G that commute with the stress tensor are well known:
these are just any functions of the ”screening charges” 7
Q± =
I
J± =
I
e±
√
2φ.
(2.20)
The correlator (2.18) will be non-vanishing only if the matching condition
for zero-modes of φ is satisﬁed. If we demand the operator to depend only
7For notational simplicity we omit the normal ordering signs, in fact the involved
operators are : eH : and : e±
√
2φ :
17
on Q+, this implies that only one term of the expansion in powers of Q+
will contribute to (2.18), so that the result is essentially independent on the
choice of the function G(Q+), we can for example take G(Q+) = eQ+ and
obtain:
ZN{t} ∼1
N!⟨N|eH(t)(Q+)N|0⟩.
(2.21)
This correlator is easy to evaluate using the Wick theorem and the propagator
φ(z)φ(z′) ∼log(z −z′) and ﬁnally we get
ZN{t} =
1
N!⟨N |: e
1
√
2
H
C0 U(z)∂φ(z) :
QN
i=1
H
Ci dzi : e
√
2φ(zi) :| 0⟩=
=
1
N!
QN
i=1
H
Ci dzieU(zi) QN
i<j(zi −zj)2
(2.22)
in the form of a multiple integral, which can in fact be directly related to the
matrix integral in (2.1), see [46] and the next section.
Thus in the simplest case we resolved the inverse problem: reconstructed
the integral representation from the set of discrete Virasoro constraints. How-
ever, the answer we got seems a little more general than (2.1): the r.h.s. of
eq.(2.22) still depends on the contours of integration. Moreover, we can also
recall that the operator G above could depend not only on Q+, but also on
Q−. The most general formula is a little more complicated than (2.22):
ZN{t | Ci, Cr} ∼
1
(N + M)!M!⟨N|eH(t)(Q+)N+M(Q−)M|0⟩=
=
1
(N + M)!M!
N+M
Y
i=1
I
Ci
dzieU(zi)
M
Y
r=1
I
C′r
dz′
reU(z′
r)·
·
QN+M
i<j
(zi −zj)2 QN
r<s(z′
r −z′
s)2
QN+M
i
QM
r (zi −zr)2
.
(2.23)
We refer to the papers [39] for discussion of the issue of the contour-dependence.
In certain sense all these diﬀerent integrals can be considered as branches of
the same analytical function ZN{t}. Dependence on M is essentially elimi-
nated by Cauchy integration around the poles in denominator in (2.23).
Above construction can be straightforwardly applied to other algebras of
constraints, provided:
(i) The free-ﬁeld representation of the algebra is known in the CFT-
framework, such that the generators are polinomials in the ﬁelds φ (only in
18
such case it is straightforward to construct a Hamiltonian H, which relates
CFT-realization of the algebra to that in terms of diﬀerential operators w.r.to
the t-variables; in fact under this condition H is usually linear in t’s and
φ’s).
There are examples (like Frenkel-Kac representation of level k = 1
simply-laced Kac-Moody algebras [47] or generic reductions of the WZNW
model [16],[48]-[51]) when generators are exponents of free ﬁelds, then this
construction should be slightly modiﬁed.
(ii) It is easy to ﬁnd vacuum, annihilated by the relevant generators (here,
for example, is the problem with application of this approach to the case
of ”continuous” Virasoro and W-constraints). The resolution to this prob-
lem involves consideration of correlates on Riemann surfaces with non-trivial
topologies, often - of inﬁnite genus.
(iii) The free-ﬁeld representation of the ”screening charges”, i.e. operators
that commute with the generators of the group within the conformal model,
is explicitly known.
These conditions are fulﬁlled in many case in CFT, including conventional
W-algebras [52] and N = 1 8 supersymmetric models [53].
For illustration purposes we present here several formulas from the last
paper of ref.[39] for the case of the Wr+1-constraints, associated with the
simply-laced algebras A of rank r.
Partition function in such ”conformal multimatrix model” is a function
of ”time-variables” t(λ)
k , k = 0...∞, λ = 1...r = rankA, and also depends on
the integer-valued r-vector N = {N1...nr}. The Wr+1-constraints imposed
on partition function are:
W (a)
n (t)ZA
N {t} = 0,
n ≥1 −a,
a = 2...r + 1.
(2.24)
The form of the W-operators is somewhat complicated, for example, in the
case of r + 1 = 3 (i.e. for A = A2 (SL(3)))
W (2)
n
=
∞
X
k=0
(ktk
∂
∂tk+n
+ k¯tk
∂
∂¯tk+n
)+
+
X
a+b=n
(
∂2
∂ta∂tb
+
∂2
∂¯ta∂¯tb
)
(2.25)
8In the case of N = 2 supersymmetry a problem arises because of the lack of reasonable
screening charges. At the most naive level the relevant operator to be integrated over
superspace (over dzdN θ) in order to produce screening charge has dimension 1 −1
2N,
which vanishes when N = 2.
19
W (3)
n
=
X
k,l>0
(ktkltl
∂
∂tk+n+l
−k¯tkl¯tl
∂
∂tk+n+l
−2ktkl¯tl
∂
∂¯tk+n+l
)+
+2
X
k>0


X
a+b=n+k
(ktk
∂2
∂ta∂tb
−ktk
∂2
∂¯ta∂¯tb
−2k¯tk
∂2
∂ta∂¯tb)

+
+4
3
X
a+b+c=n
(
∂3
∂ta∂tb∂tc
−
∂3
∂ta∂¯tb∂¯tc
),
(2.26)
and two types of time-variables, denoted through tk and ¯tk. are ossociated
with two orthogonal directions in the Cartan plane of A2: e = α1
√
2 , ¯e =
√
3ν2
√
2 .
9
All other formulas, however, are very simple: Conformal model is usually
that of the r free ﬁelds, S ∼
R ¯∂φ∂φd2z, which is used to describe represen-
tation of the level one Kac-Moody algebra, associated with A. Hamiltonian
H(t(1) . . . t(r+1)) =
r+1
X
λ=1
X
k>0
t(λ)
k µλJk,
(2.27)
where {µλ} are associated with ”fundamental weight” vectors νλ in Cartan
hyperplane and in the simplest case of A = Ar (SL(r + 1)) satisfy
µλ · µλ′ = δλλ′ −
1
r + 1,
r+1
X
λ=1
µλ = 0,
thus only r of the time variables t(1) . . . t(r+1) are linearly independent. Re-
lation between diﬀerential operators W (a)
n (t) and operators W(a)
n
in the CFT
is now deﬁned by
W (a)
n ⟨N|eH(t) . . . = ⟨N|eH(t)W(a)
i
. . . ,
a = 2, . . . , p;
i ≥1 −a,
(2.28)
where
W(a)
n
=
I
za+n−1W(a)(z)
W(a)(z) =
X
λ
[µλ∂φ(z)]a + . . .
(2.29)
9Such orthogonal basis is especially convenient for discussion of integrability properties
of the model, these t and ¯t are linear combinations of time-variables tλ
k appearing in eqs.
(2.27) and (2.32).
20
are spin-a generators of the WA
r+1 algebra. The screening charges, that com-
mute with all the W(a)(z) are given by
Q(α) =
I
J(α) =
I
eαφ
(2.30)
{α} being roots of ﬁnite-dimensional simply laced Lie algebra A.
Thus partition function arises in the form:
ZA
N {t} = ⟨N|eH(tG{Q(α)}|0⟩
(2.31)
where G is an exponential function of screening charges. Evaluation of the
free-feild correlator gives:
ZA
N {t} ∼
Z Y
α


Nα
Y
i=1
dz(α)
i
exp

X
λ;k>0
t(λ)
k (µλα)(z(α)
i
)k



×
×
Y
(α,β)
Nα
Y
i=1
Nβ
Y
j=1
(z(α)
i
−z(β)
j )αβ
(2.32)
In fact this expression can be rewritten in terms of an r-matrix integral - a
”conformal multimatrix model”:
ZA
N {t(α)} = cp−1
N
Z
N×N dH(1)...dH(p−1)
p−1
Y
α=1
e
P∞
k=0 t(α)
k
TrHk
(α) ·
·
Y
(α,β)
Det

H(α) ⊗I −I ⊗H(α+1)αβ
(2.33)
In the simplest case of W3 algebra eq.(2.32) with insertion of only two (of
the six) screenings Qα1 and Qα2 turns into
ZA2
N1,N2(t, ¯t) =
1
N1!N2!⟨N1, N2|eH(t,¯t)(Q(α1))N1(Q(α2))N2|0⟩=
=
1
N1!N2!
Y
i
Z
dxieU(xi) Y
j
Z
dyje
¯U(yi)∆(x)∆(x, y)∆(y),
(2.34)
where ∆(x, y) ≡∆(x)∆(y) Q
i,j(xi −yj). This model is associated with the
algebra A = A2 (SL(3)), while the original 1-matrix model (2.21)-(2.23) -
with A = A1 (SL(2)).
21
The whole series of models (2.32-2.33) for A = Ar (SL(r + 1)) is distin-
guished by its relation to the level k = 1 simply-laced Kac-Moody algebras.
In this particular situation the underlying conformal model has integer cen-
tral charge c = r = rankA and can be ”fermionized”.10 The main feature
of this formulation is that the Kac-Moody currents (which after integration
turn into ”screening charges” in the above construction) are quadratic in
fermionic ﬁelds, while they are represented by exponents in the free-boson
formulation.
In fact fermionic (spinor) model naturally possesses GL(r+1) rather than
SL(r+1) symmetry (other simply-laced algebras can be embedded into larger
GL-algebras and this provides fermionic descriprion for them in the case of
k = 1). The model contains r + 1 spin-1/2 ﬁelds ψi and their conjugate ˜ψi
(b, c-systems);
S =
r+1
X
j=1
Z
˜ψj ¯∂ψjd2z,
central charge c = r + 1, and operator algebra is
˜ψj(z)ψk(z′) =
δjk
z−z′ + : ˜ψj(z)ψk(z′) :
ψj(z)ψk(z′) = (z −z′)δjk : ψj(z)ψk(z′) : + (1 −δjk) : ψj(z)ψk(z′) :
˜ψj(z) ˜ψk(z′) = (z −z′)δjk : ˜ψj(z) ˜ψk(z′) : + (1 −δjk) : ˜ψj(z) ˜ψk(z′) :
The Kac-Moody currents of level k = 1 GL(r + 1) are just Jjk =: ˜ψjψk :
j, k = 1 . . . r+1, and screening charges are Q(α) = iE(α)
jk
H : ˜ψjψk :, where E(α)
jk
are representatives of the roots α in the matrix representation of GL(r + 1).
Cartan subalgebra is represented by Jjj, while positive and negative Borel
subalgebras - by Jjk with j < k and j > k respectively. In eq.(2.23) Q+ =
i
H ˜ψ1ψ2,
Q−= i
H ˜ψ2ψ1
while in eq.(2.34) Q(α1) = i
H ˜ψ1ψ2,
Q(α2) =
i
H ˜ψ1ψ3 (and Q(α3) = i
H ˜ψ2ψ3, Q(α4) = i
H ˜ψ2ψ1, Q(α5) = i
H ˜ψ3ψ1, Q(α6) =
i
H ˜ψ3ψ2). Q(α6) can be substituted instead of Q(α2) in (2.34) without changing
10 This is possible only for very special Kac-Moody algebras, and such formulation is
important in order to deal with conventional formulation of integrability, which usually
involves commuting Hamiltonian ﬂows (not just a closed algebra of ﬂows) and fermionic
realization of the universal module space (universal Grassmannian). In fact these restric-
tions are quite arbitrary and can be removed (though this is not yet done in full details),
see section 4 below for more detailed discussion.
22
the answer. For generic r the similar choice of ”adjacent” (not simple!) roots
(such that their scalar products are +1 or 0) leads to selection of the following
r screening operators Q(1) = i
H ˜ψ1ψ2 Q(2) = −i
H ψ2 ˜ψ3, Q(3) = i
H ˜ψ3ψ4, . . .,
i.e. Q(j) = i
H ˜ψjψj+1 for odd j and Q(j) = −i
H ψj ˜ψj+1 for even j.
2.4
Gross-Newman equation
We turn now to consideration of the WI for another sort of matrix mod-
els. This subject concerns at least two important classes: the conventional
discrete two-matrix models and Kontsevich models.
As it was explained
in the Introduction the theories of the second type arise in consderation of
the (p, 1) continuous matrix models, as well as in the study of topological
Landau-Ginzburg theories, while the two-matrix model is believed to exhibit
a rich pattern of continuous limits and is capable to provide representatives
of all the (p, q) universality classes (this line of reasoning, however, has never
been really developed and we shall not discuss it in these notes).
The starting point and the basic example is provided by the integral
FV,n{L} ≡
Z
n×n dXe−trV (X)+trLX
(2.35)
over n × n Hermitean matrix, which we shall further refer to as ”Kontsevich
integral”, keeping in mind its most important application (though this obvi-
ous quantity has been of course considered by many other people). It may
seem that the action in this integral is not of the most general type and we
can no longer perform arbitrary change of variables X −→f(X) without
changing the functional form of the integral. In fact this is incorrect, because
”external ﬁeld” L is matrix valued and coupled to X linearly, and therefore
any correlator of X-ﬁelds can be represented through L-derivatives. Con-
sider again the shift X →X + ǫnXn+1, n ≥−1. Invariance of the integral
implies:
Z
dXe−trV (X)+trLXtr ǫn
 
−Xn+1V ′(X) + LXn+1 +
n
X
k=0
XktrXn−k
!
= 0,
which can be rewritten as 11
tr ǫn

−
∂
∂Ltr
n+1 V ′ 
∂
∂Ltr

+ L

−
∂
∂Ltr
n+1 +
11The obvious relation is used here: XγδetrLX =
∂
Lδγ etrLX.
Note that the order of
23
Pn
k=0

−
∂
∂Ltr
k tr

−
∂
∂Ltr
n−k
FV {L} =
= tr ǫn

−
∂
∂Ltr
n+1 
V ′ 
∂
∂Ltr

−L

FV {L} = 0
(2.36)
This system is in fact equivalent to a single matrix-valued equation
 
V ′
 ∂
∂Ltr
!
−L
!
FV {L} = 0.
(2.37)
As well as I know this equation was ﬁrst written down in [54], therefore it will
be refered to as the Gross-Newman (GN) equation. It was rediscovered and
implications for the theory of matrix models were investigated in [24],[30],[38].
There are essentially two types of corollaries, which will be discussed in
the next two subsections. First, GN equation can be used to characterize
the function FV {L} itself. This will lead us to consideration of Kontsevich
models. Second, it can be used to derive equations for the 2-matrix model,
which arises after FV {L} is further integrated with some weight over L.
2.5
Ward identities for Generalized Kontsevich Model
Being just the complete set of equation of motion the GN equation (2.37)
provides complete information about the function FV {L}.
However, this
statement needs to be formulated more carefully. A need for this comes, for
example, from the observation that operators
trLm
 
V ′
 ∂
∂Ltr
!
−L
!
(2.38)
do not form a closed algebra: their commutators have some diﬀerent func-
tional form. One of the reasons for these complications is that eq.(2.37) does
not account explicitly for a very important property of FV {L}: this func-
tion in fact depends only on the eigenvalues of L. This information should
be still added somehow to the GN equation. We shall analyze this issue of
eigenvalue-dependence in more details in next sections. For our current pur-
poses this argument implies that one should try to express equation (2.37) in
matrix indices γδ is reversed at the r.h.s. as compared to the l.h.s., i.e. derivatives are in
fact w.r.to transponed matrix L:
f(X)etrLX = f(
∂
∂Ltr )etrLX (at least for any function
f(x), which can be represented as a formal seria in integer powers of X).
24
terms of eigenvalues. Here, however, one should be carefull again. Clearly,
not only FV {L} depends on eigenvalues, it depends on their ”symmetric”
(Weyl-group invariant) combinations, i.e. it rather depends on quantities
like trLa then on particular eigenvalues. Moreover, powers a here should be
negative and fractional.
Indeed, integrals like (2.35) are usually understood as analytical contin-
uation from some values of parameters in the potential V , when integral is
convergent. They can be also related to the formal (perturbation) seria aris-
ing when integrand is expanded around a stationary point. To begin with it
is reasonable to take n = 1 i.e. consider just an ordinary integral. For the
sake of simplicity also take particular V (x) = −xp+1
p+1 . Then the stationary
point is at x = λ
1
p and
Z
dxe−xp+1
p+1 +lx ∼l−p−1
2 e
p
p+1l
p+1
p
X
k≥0
ckl−k
p .
(2.39)
It is now easy to understand what should be done in the general situa-
tion with matrices and arbitrary potentials. First of all, one needs to solve
equation for the stationary point, V ′(X) = L. For this purpose it is most
convenient to introduce a new matrix variable Λ instead of L, which by def-
inition satisﬁes V ′(Λ) = L. Then stationary point is just X = Λ. Second,
one should separate the analogue of the complicated prefactor (quasiclassical
contribution):
CV {Λ} = (2π)n2/2etr(ΛV ′(Λ)−V (Λ))
q
detV ′′(Λ)
,
(2.40)
Then the function that describes pure ”quantum” contribution 12
ZV {T} ≡CV {Λ}−1FV {V ′(Λ)}
(2.41)
12The ”classical action” in (2.40) can be also represented as tr (ΛV ′(Λ) −V (Λ)) =
tr
R
ΛdV ′(Λ). Determinant of quadratic ﬂuctuations is deﬁned as
(2π)n2/2 (detV ′′(Λ))−1/2 ∼
Z
dY e−trV2(Λ,Y ),
where V2(Λ, Y ) ≡limǫ→0 1
ǫ2 (V (Λ + ǫY ) −V (Λ) −ǫV ′(Λ)Y ). For V (Λ) = Λp+1
p+1
we have
V ′′(Λ) = (Pp−1
k=0 Λk ⊗Λp−k−1). One could easily choose an ”opposite” parametrization
in eq.(2.42): Tk = −1
ktrΛ−k. Though not quite obvious, this never inﬂuences any results
(see section 2.10 for an example). Our choice of signs is motivated by simpliﬁcation of
25
to be refered as partition function of the Generalized Kontsevich Model
(GKM) [30], can be represented as a formal (perturbation) series expansion
in variables
Tk = 1
ktrΛ−k.
(2.42)
GN (2.37) equation can be now rewritten as a set of diﬀerential equations
for ZV {T}. Indeed, we already have:
C−1
V
 
V ′
 ∂
∂Ltr
!
−L
!
CV ZV {T} = 0,
(2.43)
but it is still necessary to express the operator at the l.h.s. in terms of T.
This is in fact possible to do, using the relation:
∂
∂Ltr
ZV {T} =
X
k
∂Tk
∂Ltr
∂Z
∂Tk
(2.44)
and substituting the traces of Λ-matrices, which can arise in the process of
calculation, by T’s. It is important only that Λ’s usually appear in negative
powers: this is already achieved by the choice of a proper normalization
factor CV {Λ}. For monomial potential Vp(X) = Xp+1
p+1 this is especialy simple:
L = Λp and
∂Tk
∂Ltr = −1
pΛ−p−k.
This reasoning allows one to rewrite eq.(2.43) identically in the form
X
l
Λ−lOl(T)ZV {T} = 0,
(2.45)
where Ol are some diﬀerential operators, depending on the shape of V , but
independent on the size n of the matrix (as all the above reasoning never
refered to particular values of n, except for a sample example at the very
beginning). It remains to use the fact that matrix L can be arbitrary large
and have arbitrarily many independent entries, in order to conclude that we
derived a set of constraints on ZV in the form
Ol(T)ZV {T} = 0.
(2.46)
formulas for the GKM, including the relation between L and Λ. Instead, some sign factors
appear in formulas, related to Toda-like representations of partition functions and those
involving ˜W-operators.
26
For potential V of degree p + 1 these appear to be exactly the ”continu-
ous Virasoro constraints”. See refs.[24] and [30] for detailed analysis of the
Virasoro case p = 2 (associated with the pure topological gravity and with
the double-scaling limit of the 1-matrix model), and [55] for the exhaustive
presentation of the case of p = 3.
2.6
Discrete Virasoro constraints for the Gaussian Kont-
sevich model
As a simplest illustration of the technique, described in the previous subsec-
tion, we derive now the constraints for the Gaussian Kontsevich model [56]
with potential V (X) = 1
2X2:
Z X2
2 {N, T} =
e−tr L2
2
(detL)N
Z
dX(detX)Ne−tr X2
2 +LX.
(2.47)
In this case L = V ′(Λ) = Λ, and the time-variables are just
Tk = 1
ktrΛ−k = 1
ktrL−k.
(2.48)
To make the model non-trivial an extra ”zero-time” variable N [36] is in-
troduced, which was not included into the previous deﬁnition (2.41). Now
note that the N-dependence of Kontsevich integral (2.35) can be described
simply as an extra term in the potential: V (X) →ˆV (X) = V (X) −N log X
(though this can not be done neither in the quasiclassical factor CV nor in
the deﬁnition of time-variables T). Since the GN equation depends only on
Kontsevich equation, we can use it with V substituted by ˆV . Then we have
instead of (2.43):
e−tr L2
2
(detL)N
 ∂
∂Ltr
!n+1
·

∂
∂Ltr
−N
 ∂
∂Ltr
!−1
−L

·
·(detL)Ne+tr L2
2 Z X2
2 {N, T} = 0.
(2.49)
In order to get rid of the integral operator ( ∂
∂L)−1 one should take here n ≥0
rather than n ≥−1. In fact all the equations with n > 0 follow from the one
27
with n = 0, and we restrict our consideration to the last one. For n = 0 we
obtain from (2.49):


 ∂
∂Ltr
+ N
L + L
!2
−2N −L
 ∂
∂Ltr
+ N
L + L
!
Z = 0
or


 ∂
∂Ltr
!2
+

L + 2N
L

∂
∂Ltr
+ N2
L2 −N
L tr 1
L

Z = 0,
(2.50)
and it remains to substitute:
∂Z
∂Ltr
= −P∞
k=0
1
Lk+1
∂Z
∂Tk ;
∂2Z
∂L2
tr
= P∞
k=1
Pk+1
a=1
1
Lk+2−atr 1
La

∂Z
∂Tk + P∞
k,l=1
1
Lk+l+2
∂2Z
∂Tk∂Tl =
= P∞
m=−1
1
Lm+2
P
k>max(m,0)

tr
1
Lk−m

∂Z
∂Tk + Pm−1
k=1
∂2Z
∂Tk∂Tm−k

and ﬁnally obtain:
∞
X
m=−1
1
Lm+2
P∞
k=1+δm,−1

tr 1
Lk

∂
∂Tk+m + Pm−1
k=1
∂2
∂Tk∂Tm+k −
−
∂
∂Tm+2 −2N
∂
∂Tm + N2δm,0 −N

tr 1
L

δm,−1

Z =
= P∞
m=−1
1
Lm+2eNT0Lm(T + r)e−NT0Z = 0.
(2.51)
Here Lm(t) are just the generators (2.7) of the discrete Virasoro algebra (2.6):
eNt0Lm(t)e−Nt0 = eNt0
 ∞
X
k=1
ktk
∂
∂tk+m
+
m
X
k=0
∂2
∂tk∂tm−k
!
e−Nt0.
(2.52)
and at the r.h.s. of (2.51) rk = −1
2δk,2.13
13 This small correction is a manifestation of a very general phenomenon: from the
point of view of symmetries (Ward identities) it is more natural to consider ZV not as a
function of T -variables, but of some more complicated combination ˆTk + rk, depending on
the shape of potential V . If V is a polinomial of degree p + 1, ˆTk = 1
ktr(V ′(λ))−k/p, while
rk =
p
k(p−k)Res (V ′(µ))1−k
p dµ. For monomial potentials these expressions become very
simple: ˆTk = Tk and rk = −
p
p+1δk,p+1. See [39] and section 4.9 below for more details.
In most places in these notes we prefer to use invariant potential-independent times Tk,
instead of ˆTk, but then Ward identites acquire some extra terms with rk (which in fact
will be very simple in our examples, which are all given for monomial potentials).
28
Thus we found that the WI of the Gaussian Kontsevich model (2.47)
coincide with those of the ordinary 1-matrix model, moreover the size of the
matrix N in the latter model is associated with the ”zero-time” in the former
one. This result [56] of course implies, that the two models are identical:
e−NT0Z X2
2 {N, T1, T2, . . .} ∼ZN{T0, T1, T2, . . .}.
(2.53)
We shall discuss direct connection between these two matrix integrals (2.1)
and (2.47) in the next section, after some more details will be presented
about the structure of ”eigenvalue” matrix models.
2.7
