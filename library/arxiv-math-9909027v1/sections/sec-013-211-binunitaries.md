---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California"
section_id: sec-013-211-binunitaries
section_title: "Binunitaries"
section_number: 2.11
pages: 54-63
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
doc_brief: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California — We introduce a notion of planar algebra, the simplest exampl e of which is a vector space of tensors, closed"
---
Commuting squares have been used to construct subfactors (see [GHJ],[Ha])
and the general theory of calculating the subfactor planar a lgebra of §4.2 from
a commuting square will be dealt with in a future paper. The tr eatment uses
the language of statistical mechanical models with some att ention paid to
critical points as in chapter 4 of [JS]. Here we give a diﬀeren t approach
which seems more natural from a planar point of view and will a llow us to
capture, as special cases, spin model commuting squares and some vertex
model ones with no extension of the planar algebra formalism . The main
concept is that of a bi-invertible element in a planar algebr a which is the
next step in the hierarchy discussed at the end of Example 2.1 0.
Deﬁnition 2.11.1. Let P be a general planar algebra. An invertible
element u ∈ P2 will be called bi-invertible if
u−1u u−1 = = u∆
for some non-zero scalar ∆. (If P is planar ∆ is necessarily δ1 (δ2). If P
is a planar ∗-algebra, a bi-invertible u is called biunitary if u∗ = u−1. Bi-
invertible elements deﬁne planar subalgebras as we now desc ribe. It will
be convenient to consider labelled tangles containing cert ain distinguished
curves joining boundary points, which intersect with only t he other strings
in a tangle and do not meet any internal boxes. From such a tang le, and a
bi-invertible element u, we construct an honest labelled tangle, in the sense
of §1, in two steps.
(i) Orient the distinguished curves. The global orientatio n will be denoted
։− and the tangle orientation by →−.
(ii) At a point of intersection between the distinguished cu rves and the
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
From now on we suppose for convenience that ∆ = 1.
Lemma 2.11.2 The Reidemeister type II moves are satisﬁed, i.e.,
,= =
where either of the two curves is distinguished and its globa l orientation is
arbitrary.
Proof. This is just a re-expression of bi-invertibility. □
Theorem 2.11.3 If P is a general planar algebra and u is bi-invertible, let
P u
k be
{x ∈ Pk s.t.
=x
y
for some y∈Pk}.
Then P u is a general planar subalgebra, P u is a (general) planar ∗-subalgebra
55
if P is a planar ∗-algebra and u is bi-unitary. The properties of being planar,
C ∗ and spherical are inherited from P .
Proof. That P u is a subalgebra is obvious. The ∗-property is more
interesting. Applying ∗ to the pictures we obtain (using u∗ = u−1)
=x∗
y∗
Now we surround these pictures with the annular tangle
and then apply type II Reidemeister moves. We see that x∗ ∈ P u if x does
(though note that the “ y” for x∗ is y∗, but rotated.
To show that P u is a general planar subalgebra, we only have to show by
1.18 that it is invariant under A(φ). But if we arrange the annular tangle A
so that all critical points of the height function on strings are local maxima
and minima, the distinguished line
πA(x)
can be moved through πA(x), close to x using only planar isotopy and
type II Reidemeister moves. It can then go past x, producing a y, and down
to the bottom via type II Reidemeister moves. Thus πA(x) is in P u.
56
Planarity, positivity and sphericity are all inherited. □
Notes. (i) We will see that P u may be planar even when P is only general
planar.
(ii) When k = 2 the equation of Theorem 2.11.3 is an abstract version of
the Yang-Baxter equation ([Ba]).
We now recast the equation of Theorem 2.11.3 in some equivale nt forms
which reveal some of its structure. The idea of the equation, as seen clearly
in the proof of 2.11.3 is just that the distinguished lines ca n move freely
past the boxes. As stated this requires a special conﬁgurati on as the distin-
guished line approaches a box, but by Reidemeister type II in variance any
approach will do. We record this below, keeping the notation of 2.11.3. (Note
that it is somewhat cumbersome to force all the pictures to ﬁt appropriately
into the standard k-box. We use a disk with 2 k boundary points-as in the
introduction.)
Proposition 2.11.4 An x in Pk is in P u
k iﬀ there is a y in P u
k with
=
q points q points
p pointsp points
x y
where p + q = 2 k, where the pictures may be isotoped in any way so that
the annular region becomes the standard annular region (wit h ∗ anywhere
allowed by the orientations).
Proof. If p > q , surround the two pictures with the annular tangle
k points
57
and use isotopy, rotation (if necessary to get ∗ in the right place), and type
II Reidemeister moves to obtain the same picture as in 2.11.3 . □
Deﬁnition 2.11.5. Given P and u as above, deﬁne σu : Pk → Pk+1 by
the tangle below:
xσu(x) =
Proposition 2.11.6 The map σu is a unital endomorphism of the ﬁltered
algebra P (a ∗-endomorphism if u is unitary) and P u
k = {x | σu(x) ∈ P1,k+1}.
Proof. That σu preserves multiplication follows from type II Reidemeis-
ter moves. The alternative deﬁnition of P u is just the case q = 0, with ∗
appropriately placed, in 2.11.4. □
Note that the endomorphism σu is the obvious “shift de un” when re-
stricted to the Temperley-Lieb subalgebra.
The condition of 2 .11.5 involved a pair ( x, y). In fact x is determined by
y and vice versa as we now record.
Proposition 2.11.7 Suppose P is a general planar algebra. If x ∈ P u with
σu(x) = y . Then
andy = 1
δ2
x y =x 1
δ1
Proof. Just apply the appropriate annular tangles and use Reidemei ster
moves. □
58
Thus we could rewrite equations for x ∈ P u entirely in terms of x. The
least obvious reformulation of these equations involves le ss boundary points
than above and requires positivity.
Theorem 2.11.8 Let P be a spherical ﬁnite-dimensional C ∗-planar algebra
and u ∈ P2 be bi-unitary. Then x ∈ P u iﬀ
x x = δ2
.
Proof. (⇒) This is easy and requires no positivity.
(⇐) We begin by observing that δσ ∗
u(z) is given by the tangle below
z
Here the adjoint of σu is as a map between the ﬁnite-dimensional Hilbert
spaces Pk and Pk+1 with inner products given by the normalized traces. This
formula for σ∗
u thus follows from the equality by isotopy of the following tw o
59
networks, the ﬁrst of which is, up to a power of δ, ⟨σu(x), z∗⟩
z
x
z
x
=
Thus orthogonal projection E onto σu(Pk) is σuσ∗
u which is given on z ∈ Pk
by 1
δ times the following picture
z
Orthogonal projection F onto P1,k+1 is given by δF (z) = z . An
element w of σu(Pk) is in P1,k+1 iﬀ EF (w) = w. But if x satisﬁes the
condition of the theorem we have
EF (σu(x)) = 1
δ ( x ) = 1
δ2 x = σu(x).
Hence x ∈ P u. □
60
B
C
u
D
A
Figure 2:
Remark. We did not use the full force of the hypotheses. The result
will hold in a ﬁnite-dimensional general C ∗-planar algebra provided isolated
circles can be removed with a multiplicative factor δ, that the tangle formula
for orthogonal projection onto P1,k+1 is correct, and dim P1 = 1.
We will see in the case of spin models that P u may be planar although
P is not. (But the conditions of the above remark are satisﬁed b y P σ.)
It is easy to check that a bi-invertible u ∈ P2 may be altered by four
invertible elements A, B, C, D in P1 as in Figure 2.11.9
Deﬁnition 2.11.10. Two bi-invertibles are said to diﬀer by a gauge
transformation if one is obtained from the other as in Figure 2.11.9.
Gauge transformations have an inessential eﬀect on P u; A and C change
absolutely nothing, B and D change P u by a planar algebra isomorphism
(induced by one on P -conjugation by d d d . . .).
In the ∗ case, gauge transformations on bi-unitary matrices are one s with
A, B, C, D unitary.
A signiﬁcant observation about the equations deﬁning P u above is that
they are linear so the calculation of P u
k , given Pk and u, is a ﬁnite problem,
unlike the calculation of the planar subalgebra generated b y some set, which
requires consideration of inﬁnitely many tangles. In pract ice, however, the
brute force calculation, even just of dim P u
k , runs into a serious problem. For
61
the dimension of Pk grows exponentially with k. For k = 2 the calculation is
usually easy enough (indeed we give an entirely satisfactor y general solution
for k = 2 when P = P σ, below) and somewhat harder for k = 3. For
k = 4 it tends to be very demanding even for relatively “small” P ’s. On the
other hand, we are dealing with objects with a lot of structur e. For instance,
once we have calculated P u
2 by brute force or otherwise, the fact that P u
is a planar algebra means that every unlabelled 2-tangle giv es a nonlinear
constraint. For if a 2-tangle is given labels with elements in P , in order
for the corresponding element of P2 to be in P u, it must lie in the linear
subspace of P2 already calculated. It was the desire to systematically exp loit
these highly interesting nonlinear constraints that led to the theory of planar
algebras — their generality was only appreciated afterward s.
There are good reasons for wanting to calculate P u. In general the cal-
culation is greatly facilitated by the presence of group sym metry but there
are many cases of bi-invertible elements with no apparent sy mmetry. We
hope that the planar algebra P u plays the role of “higher”, non-group-like
symmetries which reveal structural properties of the combi natorial object u.
We turn now to a special case where this program has had some pa r-
tial success, namely in Hadamard matrices. The theory is no d iﬀerent for
generalized Hadamard matrices, which occur as biunitaries for spin models.
Consider the spin model P σ with Q spins and its spherical planar algebra
structure (§2.8). A bi-invertible element u of P σ
2 is an invertible Q×Q matrix
ub
a such that
= =∗
∗u ∗ ∗uandu−1 u−1
So if ( u−1)b
a = vb
a we have ua,bvb,a = 1 /Q where the factor 1 /Q comes from
counting oriented circles after smoothing. If u is biunitary, va,b = ub,a, so the
condition is precisely
|ua,b| = 1√Q
We call a unitary matrix satisfying 2.11.11 a generalized Hadamard matrix.
A Hadamard matrix is just √Q times a real generalized Hadamard matrix.
62
Gauge transformations alter a generalized Hadamard matrix by multi-
plying rows and columns by scalars of modulus one ( ±1 in the Hadamard
case). This, together with permutations of the rows and colu mns, gives what
is called Hadamard equivalence of (generalized) Hadamard matrices. Row
and column permutations are easily seen by 2.11.6 to produce equivalent
P u’s so any information about u obtained from P u alone will be invariant
under Hadamard equivalence. (The endomorphism σu of 2.11.5 itself is more
information than just P u.)
Proposition 2.11.12 If u is a generalized Hadamard matrix, P u is planar,
hence a spherical C ∗-planar algebra. Moreover, dim P u
1 = 1, and P u
2 and P u
1,3
are abelian.
Proof. Obviously dim P u
1 = 1 implies planarity, so consider a tangle
T representing an element of P1. It consists of a vertical straight line with
a 1-box on it, and networks to the left and right. The networks to the left
have exterior shaded white so only contribute scalars. The p icture below is
the condition for such an element to be in P u
