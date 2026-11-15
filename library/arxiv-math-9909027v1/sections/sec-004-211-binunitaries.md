---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I"
section_id: sec-004-211-binunitaries
section_title: "Binunitaries"
section_number: 2.11
pages: 54-67
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
doc_brief: "Planar Algebras, I — We introduce a notion of planar algebra, the simplest example of which is a vector space of tensors, closed under planar contractions."
---
Commuting squares have been used to construct subfactors (see [GHJ],[Ha])
and the general theory of calculating the subfactor planar algebra of §4.2 from
a commuting square will be dealt with in a future paper. The treatment uses
the language of statistical mechanical models with some attention paid to
critical points as in chapter 4 of [JS]. Here we give a diﬀerent approach
which seems more natural from a planar point of view and will allow us to
capture, as special cases, spin model commuting squares and some vertex
model ones with no extension of the planar algebra formalism. The main
concept is that of a bi-invertible element in a planar algebra which is the
next step in the hierarchy discussed at the end of Example 2.10.
Deﬁnition 2.11.1. Let P be a general planar algebra. An invertible
element u ∈P2 will be called bi-invertible if
u−1
u
u−1
=
=
u
∆
for some non-zero scalar ∆. (If P is planar ∆is necessarily δ1 (δ2). If P
is a planar ∗-algebra, a bi-invertible u is called biunitary if u∗= u−1. Bi-
invertible elements deﬁne planar subalgebras as we now describe.
It will
be convenient to consider labelled tangles containing certain distinguished
curves joining boundary points, which intersect with only the other strings
in a tangle and do not meet any internal boxes. From such a tangle, and a
bi-invertible element u, we construct an honest labelled tangle, in the sense
of §1, in two steps.
(i) Orient the distinguished curves. The global orientation will be denoted
։−and the tangle orientation by →−.
(ii) At a point of intersection between the distinguished curves and the
strings of the tangle, insert 2-boxes containing u or u−1 according to the
54
following conventions
u
u−1
(global orientation)
going out)
(global orientation)
(=tangle orientation
(=tangel orientation
going in)
∗
∗
Thus along a distinguished curve one alternately meets u or u−1.
From now on we suppose for convenience that ∆= 1.
Lemma 2.11.2 The Reidemeister type II moves are satisﬁed, i.e.,
,
=
=
where either of the two curves is distinguished and its global orientation is
arbitrary.
Proof. This is just a re-expression of bi-invertibility.
□
Theorem 2.11.3 If P is a general planar algebra and u is bi-invertible, let
P u
k be
{x ∈Pk s.t.
=
x
y
for some
y∈Pk}.
Then P u is a general planar subalgebra, P u is a (general) planar ∗-subalgebra
55
if P is a planar ∗-algebra and u is bi-unitary. The properties of being planar,
C∗and spherical are inherited from P.
Proof. That P u is a subalgebra is obvious. The ∗-property is more
interesting. Applying ∗to the pictures we obtain (using u∗= u−1)
=
x∗
y∗
Now we surround these pictures with the annular tangle
and then apply type II Reidemeister moves. We see that x∗∈P u if x does
(though note that the “y” for x∗is y∗, but rotated.
To show that P u is a general planar subalgebra, we only have to show by
1.18 that it is invariant under A(φ). But if we arrange the annular tangle A
so that all critical points of the height function on strings are local maxima
and minima, the distinguished line
πA(x)
can be moved through πA(x), close to
x
using only planar isotopy and
type II Reidemeister moves. It can then go past x, producing a y, and down
to the bottom via type II Reidemeister moves. Thus πA(x) is in P u.
56
Planarity, positivity and sphericity are all inherited.
□
Notes. (i) We will see that P u may be planar even when P is only general
planar.
(ii) When k = 2 the equation of Theorem 2.11.3 is an abstract version of
the Yang-Baxter equation ([Ba]).
We now recast the equation of Theorem 2.11.3 in some equivalent forms
which reveal some of its structure. The idea of the equation, as seen clearly
in the proof of 2.11.3 is just that the distinguished lines can move freely
past the boxes. As stated this requires a special conﬁguration as the distin-
guished line approaches a box, but by Reidemeister type II invariance any
approach will do. We record this below, keeping the notation of 2.11.3. (Note
that it is somewhat cumbersome to force all the pictures to ﬁt appropriately
into the standard k-box. We use a disk with 2k boundary points-as in the
introduction.)
Proposition 2.11.4 An x in Pk is in P u
k iﬀthere is a y in P u
k with
=
q points
q points
p points
p points
x
y
where p + q = 2k, where the pictures may be isotoped in any way so that
the annular region becomes the standard annular region (with ∗anywhere
allowed by the orientations).
Proof. If p > q, surround the two pictures with the annular tangle
k points
57
and use isotopy, rotation (if necessary to get ∗in the right place), and type
II Reidemeister moves to obtain the same picture as in 2.11.3.
□
Deﬁnition 2.11.5. Given P and u as above, deﬁne σu : Pk →Pk+1 by
the tangle below:
x
σu(x) =
Proposition 2.11.6 The map σu is a unital endomorphism of the ﬁltered
algebra P (a ∗-endomorphism if u is unitary) and P u
k = {x | σu(x) ∈P1,k+1}.
Proof. That σu preserves multiplication follows from type II Reidemeis-
ter moves. The alternative deﬁnition of P u is just the case q = 0, with ∗
appropriately placed, in 2.11.4.
□
Note that the endomorphism σu is the obvious “shift de un” when re-
stricted to the Temperley-Lieb subalgebra.
The condition of 2.11.5 involved a pair (x, y). In fact x is determined by
y and vice versa as we now record.
Proposition 2.11.7 Suppose P is a general planar algebra. If x ∈P u with
σu(x) =
y
. Then
and
y
=
1
δ2
x
y
=
x 1
δ1
Proof. Just apply the appropriate annular tangles and use Reidemeister
moves.
□
58
Thus we could rewrite equations for x ∈P u entirely in terms of x. The
least obvious reformulation of these equations involves less boundary points
than above and requires positivity.
Theorem 2.11.8 Let P be a spherical ﬁnite-dimensional C∗-planar algebra
and u ∈P2 be bi-unitary. Then x ∈P u iﬀ
x
x
=
δ2
.
Proof. (⇒) This is easy and requires no positivity.
(⇐) We begin by observing that δσ∗
u(z) is given by the tangle below
z
Here the adjoint of σu is as a map between the ﬁnite-dimensional Hilbert
spaces Pk and Pk+1 with inner products given by the normalized traces. This
formula for σ∗
u thus follows from the equality by isotopy of the following two
59
networks, the ﬁrst of which is, up to a power of δ, ⟨σu(x), z∗⟩
z
x
z
x
=
Thus orthogonal projection E onto σu(Pk) is σuσ∗
u which is given on z ∈Pk
by 1
δ times the following picture
z
Orthogonal projection F onto P1,k+1 is given by δF(z) =
z
.
An
element w of σu(Pk) is in P1,k+1 iﬀEF(w) = w.
But if x satisﬁes the
condition of the theorem we have
EF(σu(x)) = 1
δ(
x
) =
1
δ2
x
= σu(x).
Hence x ∈P u.
□
60
B
C
u
D
A
Figure 2:
Remark. We did not use the full force of the hypotheses. The result
will hold in a ﬁnite-dimensional general C∗-planar algebra provided isolated
circles can be removed with a multiplicative factor δ, that the tangle formula
for orthogonal projection onto P1,k+1 is correct, and dim P1 = 1.
We will see in the case of spin models that P u may be planar although
P is not. (But the conditions of the above remark are satisﬁed by P σ.)
It is easy to check that a bi-invertible u ∈P2 may be altered by four
invertible elements A, B, C, D in P1 as in Figure 2.11.9
Deﬁnition 2.11.10.
Two bi-invertibles are said to diﬀer by a gauge
transformation if one is obtained from the other as in Figure 2.11.9.
Gauge transformations have an inessential eﬀect on P u; A and C change
absolutely nothing, B and D change P u by a planar algebra isomorphism
(induced by one on P-conjugation by
d
d
d
. . .).
In the ∗case, gauge transformations on bi-unitary matrices are ones with
A, B, C, D unitary.
A signiﬁcant observation about the equations deﬁning P u above is that
they are linear so the calculation of P u
k , given Pk and u, is a ﬁnite problem,
unlike the calculation of the planar subalgebra generated by some set, which
requires consideration of inﬁnitely many tangles. In practice, however, the
brute force calculation, even just of dim P u
k , runs into a serious problem. For
61
the dimension of Pk grows exponentially with k. For k = 2 the calculation is
usually easy enough (indeed we give an entirely satisfactory general solution
for k = 2 when P = P σ, below) and somewhat harder for k = 3.
For
k = 4 it tends to be very demanding even for relatively “small” P’s. On the
other hand, we are dealing with objects with a lot of structure. For instance,
once we have calculated P u
2 by brute force or otherwise, the fact that P u
is a planar algebra means that every unlabelled 2-tangle gives a nonlinear
constraint.
For if a 2-tangle is given labels with elements in P, in order
for the corresponding element of P2 to be in P u, it must lie in the linear
subspace of P2 already calculated. It was the desire to systematically exploit
these highly interesting nonlinear constraints that led to the theory of planar
algebras — their generality was only appreciated afterwards.
There are good reasons for wanting to calculate P u. In general the cal-
culation is greatly facilitated by the presence of group symmetry but there
are many cases of bi-invertible elements with no apparent symmetry. We
hope that the planar algebra P u plays the role of “higher”, non-group-like
symmetries which reveal structural properties of the combinatorial object u.
We turn now to a special case where this program has had some par-
tial success, namely in Hadamard matrices. The theory is no diﬀerent for
generalized Hadamard matrices, which occur as biunitaries for spin models.
Consider the spin model P σ with Q spins and its spherical planar algebra
structure (§2.8). A bi-invertible element u of P σ
2 is an invertible Q×Q matrix
ub
a such that
=
=
∗
∗
u
∗
∗u
and
u−1
u−1
So if (u−1)b
a = vb
a we have ua,bvb,a = 1/Q where the factor 1/Q comes from
counting oriented circles after smoothing. If u is biunitary, va,b = ub,a, so the
condition is precisely
|ua,b| =
1
√Q
We call a unitary matrix satisfying 2.11.11 a generalized Hadamard matrix.
A Hadamard matrix is just √Q times a real generalized Hadamard matrix.
62
Gauge transformations alter a generalized Hadamard matrix by multi-
plying rows and columns by scalars of modulus one (±1 in the Hadamard
case). This, together with permutations of the rows and columns, gives what
is called Hadamard equivalence of (generalized) Hadamard matrices. Row
and column permutations are easily seen by 2.11.6 to produce equivalent
P u’s so any information about u obtained from P u alone will be invariant
under Hadamard equivalence. (The endomorphism σu of 2.11.5 itself is more
information than just P u.)
Proposition 2.11.12 If u is a generalized Hadamard matrix, P u is planar,
hence a spherical C∗-planar algebra. Moreover, dim P u
1 = 1, and P u
2 and P u
1,3
are abelian.
Proof. Obviously dim P u
1 = 1 implies planarity, so consider a tangle
T representing an element of P1. It consists of a vertical straight line with
a 1-box on it, and networks to the left and right. The networks to the left
have exterior shaded white so only contribute scalars. The picture below is
the condition for such an element to be in P u
1 (for some element S)
T
S
=
If the bottom shaded region is assigned a spin a, and the top region a spin
b, the left-hand side gives ub
aTa and the right-hand side gives ub
aSb, so Ta is
independent of a, and dim P u
1 = 1. P u
1,3 is abelian because P1,3 is and P u
2 is
abelian since it is σ−1
u (σu(P2) ∩P1,3) by 2.11.6.
□
So by §4.3, a generalized Hadamard matrix u yields a subfactor whose
planar algebra invariant is P u. In fact such a subfactor was the starting point
of the theory of planar algebras, as the equations for P u are those for the
relative commutants of a spin model commuting square given in [JS]. Note
that the original subfactor is hyperﬁnite whereas the one obtained from 4.3
is not! We now determine P u
2 for a generalized Hadamard matrix u.
63
Deﬁnition 2.11.13. Given a Q × Q generalized Hadamard matrix ub
a
we deﬁne the Q2 × Q2 proﬁle matrix Prof(u) by
Prof(u)c,d
a,b =
X
x
ux
aux
b ux
c ux
d .
The proﬁle matrix is used in the theory of Hadamard matrices. We will see
that it determines P u.
Deﬁnition 2.11.14.
Given the Q2 × Q2 matrix
Prof(u), deﬁne the
directed graph Γu on Q2 vertices by (a, b) →−(c, d) iﬀProf(u)c,d
a,b̸ = 0.
The isomorphism class of Γu is an invariant of Hadamard equivalence.
Theorem 2.11.15 If u is a Q × Q generalized Hadamard matrix thought
of as a biunitary for the spin model P σ, then the minimal projections of
the abelian C∗-algebra P u
2 are in bijection with the connected components
of the graph Γu. Moreover the (normalized) trace of such a projection is
n/Q2 where n is the size of the connected component, which is necessarily a
multiple of Q.
Proof. For matrices xb
a, yb
a, the equations of Theorem 2.11.3 are the
“star-triangle” equations
X
d
ud
a ud
b xc
d = uc
a uc
b yb
a
which amount to saying that, for each (a, b), the vector v(a,b) whose dth com-
ponent is the ud
aud
b is an eigenvector of the matrix xc
d with eigenvalue yb
a. The
proﬁle matrix is just the matrix of inner products ⟨v(a,b), v(c,d)⟩so the or-
thogonal projection onto the linear span of v(a,b)’s in a connected component
is in P u
2 and is necessarily minimal since eigenvectors for distinct minimal
projections are orthogonal.
If the matrix x is an orthogonal projection, yb
a is either 1 or 0 depending
64
on whether v(a,b) is in the connected component or not. Consider the picture
x
y
=
Applying Reidemeister type II moves and summing we obtain the assertion
about the trace. (It is a multiple of 1/Q since x is a Q × Q matrix.)
□
If G is a ﬁnite abelian group and g 7→ˆg is an isomorphism of G with its
dual ˆG (=Hom(G, C∗)), we obtain a generalized Hadamard matrix u, with
Q = |G|, by setting uh
g =
1
√Q ˆh(g).
We call this a standard generalized
Hadamard matrix. It is Hadamard if G = (Z/2Z)n for some n. We leave it
to the reader to check that if u is standard P u is exactly the planar algebra
of §2.9 for the group G. In particular, dim(P u
k ) = Qk. It is well known in
subfactor theory that any subfactor with N′ ∩M1 = C[M:N] comes from a
group. It can also be seen directly from association schemes that if dim(P u
2 ) =
Q then u is standard up to gauge equivalence (recall that P u is always an
assocation scheme as remarked in §2.8).
We have, together with R. Bacher, P. de la Harpe, and M.G.V. Bogle
performed many computer calculations. So far we have not found a gener-
alized Hadamard matrix u for which dim(P u
2 ) = 2 but dim(P u
3 ) > 5. Such
an example would be a conﬁrmation of our non-group symmetry program as
group-like symmetries tend to show up in P2. In particular the ﬁve 16 × 16
Hadamard matrices have dimP u
2 = 16,8,5,3 and 3, and are completely dis-
tinguished by the trace. There are group-like symmetries in all cases corre-
sponding to the presence of normalizer in the subfactor picture.
Haagerup has shown how to construct many interesting examples and
given a complete classiﬁcation for Q = 5. In the circulant case he has shown
there are only ﬁnitely many examples for ﬁxed prime Q (see [
]).
Perhaps somewhat surprisingly, the presence of a lot of symmetry in u can
65
cause P u
2 to be small! The kind of biunitary described in the following result
is quite common — the Paley type Hadamard matrices give an example.
Proposition 2.11.17 Suppose Q−1 is prime and let u be a Q×Q generalized
Hadamard matrix with the following two properties (the ﬁrst of which is
always true up to gauge equivalence):
(i) There is an index ∗with ua
∗= u∗
a = 1 for all a.
(ii) The group Z/(Q −1)Z acts transitively on the spins other
than ∗, and uga
gb = ua
b for all g ∈Z/(Q −1)Z.
Then dim(P u
2 ) = 2 or u is gauge equivalent to a standard matrix.
Proof. The nature of the equations 2.11.15 makes it clear that Z/(Q −
1)Z acts by automorphisms on P u
2 , obviously ﬁxing the projection e1 which
is the matrix xb
a = 1/Q. Thus the action preserves (1 −e1)P u
2 (1 −e1). Since
(Q −1) is prime there are only two possibilities: either the action is non-
trivial and dim(P u
2 ) = Q so P u is standard, or every solution of 2.11.15 is
ﬁxed by Z/(Q −1)Z. In the latter case let xb
a, yb
a be a solution of 2.11.15.
Then putting c = ∗we obtain P
d ud
a ud
bx∗
d = yb
a, so yb
a is determined by the
two numbers x∗
∗and x∗
d, d̸ = ∗. So by 2.11.7 we are done.
□
Note that the standard case in the above result can occur. The 8 × 8
Hadamard matrix is of the required form, but it is Hadamard equivalent to
a standard matrix. For Q = 12 and 24 this cannot be the case and dim
P u
2 = 2.
We have very few general results on P u
k for k > 2. We only record the
observation that P u
k is the δ2 eigenspace for the Qk × Qk matrix given by
the “transfer matrix with periodic horizontal boundary conditions” for the
Q-spin vertex model having the proﬁle matrix as Boltzmann weights. The
transfer matrix is given by the picture:
66
where of course the internal spins have been summed over. This is an imme-
diate consequence of 2.11.8.
We would like to make the following two open problems about matrices
quite explicit. Both concern a generalized Hadamard matrix u.
(i) Is the calculation of dim P u
k feasible in the polynomial time
as a function of k?
(ii) Is there a u for which dim P u
k =
1
k+1
 2k
k

? (i.e., P u
k is just the
Temperley-Lieb algebra).
Finally we make some comments on vertex models.
There are many
formal connections with Hopf algebras here which is not surprising since
quantum groups arose from vertex models in statistical mechanical models
([Dr]). Banica has done some interesting work from this point of view — see
[Ban].
A vertex model, in the above context, is simply a biunitary (or biinvert-
ible) in the planar algebra P ⊗. The equations of Theorem 2.11.3 are then just
the equations for the higher relative commutants of a subfactor coming from
a certain commuting square (see [JS]). Perhaps the most interesting exam-
ples not coming from the quantum group machinery are the Krishan-Sunder
“bipermutation matrices” where u is a permutation matrix with respect to
some basis of the underlying vector space (see [KS]). B.Bhattacharya has
exhibited a planar algebra which is bigger than that of example 2.3. (Fuss
Catalan) and which is necessarily a planar subalgebra of P u if u is a biper-
mutation matrix.
