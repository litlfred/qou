---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidification"
section_id: sec-001-3-homology-versus-cohomology
section_title: "Homology versus Cohomology"
section_number: 3
pages: 25-29
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
doc_brief: "Higher Dimensional Algebra VII: Groupoidification — Groupoidiﬁcation is a form of categoriﬁcation in which vect or spaces are replaced by groupoids and linear operators are replaced by spans of"
---
The work we have described so far has its roots in the cohomology of groupoids.
Any groupoid X can be turned into a topological space, namely the geometric
realization of its nerve [16], and we can deﬁne the cohomology of X to be the
cohomology of this space. The set of connected components of th is space is just
the set of isomorphism classes of X, which we have denoted X. So, the zeroth
cohomology of the groupoid X, with real coeﬃcients, is precisely the vector
space RX that we have been calling the degroupoidiﬁcation of X.
Indeed, one reason degroupoidiﬁcation has been overlooked until recently is
that every groupoid is equivalent to a disjoint union of one-object g roupoids,
which we may think of as groups. To turn a groupoid into a topological space it
suﬃces to do this for each of these groups and then take the disjo int union. The
space associated to a group G is quite famous: it is the Eilenberg–Mac Lane
spaceK(G, 1). Similarly, the cohomology of groups is a famous and well-studied
subject. But the zeroth cohomology of a group is always just R. So, zeroth
cohomology is not considered interesting. Zeroth cohomology only b ecomes
interesting when we move from groups to groupoids—and then only w hen we
consider how a tame span of groupoids induces a map on zeroth coho mology.
These reﬂections suggest an alternate approach to degroupoidiﬁ cation based
on homology instead of cohomology:
Deﬁnition 17. Given a groupoid X, let the zeroth homology of X be the
real vector space with the set X as basis. We denote this vector space as R[X].
We can also think of R[X] as the space of real-valued functions on X with
ﬁnite support. This makes it clear that the zeroth homology R[X] can be iden-
tiﬁed with a subspace of the zeroth cohomology RX . If X has ﬁnitely many
isomorphism classes of objects, then the set X is ﬁnite, and the zeroth homol-
ogy and zeroth cohomology are canonically isomorphic. For a groupo id with
inﬁnitely many isomorphism classes, however, the diﬀerence become s impor-
tant. The following example makes this clear:
Example 18. LetE be the groupoid of ﬁnite sets and bijections. In Example
3 we saw that
RE ∼= {ψ : N → R} ∼= R[[z]].
So, elements of R[E] may be identiﬁed with formal power series with only ﬁnitely
many nonzero coeﬃcients. But these are just polynomials:
R[E] ∼= R[z].
Before pursuing a version of degroupoidiﬁcation based on homology , we
should ask if there are other choices built into our recipe for degrou poidiﬁ-
cation that we can change. The answer is yes. Recalling Equation 4, w hich
describes the operator associated to a tame span:
(S
~
ψ)([y]) =
∑
[x]∈X
∑
[s]∈p−1(x) ⋂ q−1(y)
|Aut(x)|
|Aut(s)| ψ([x]).
25
one might wonder about the asymmetry of this formula. Speciﬁcally, one might
wonder why this formula uses information about Aut( x) but not Aut( y). The
answer is that we made an arbitrary choice of conventions. There is another
equally nice choice, and in fact an entire family of choices interpolating between
these two:
Proposition 19. Given α ∈ R and a tame span of groupoids:
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
there is a linear operator called its α -degroupoidiﬁcation :
Sα
~
: RX → RY
given by:
(Sα
~
ψ)([y]) =
∑
[x]∈X
∑
[s]∈p−1(x) ⋂ q−1(y)
|Aut(x)|1−α |Aut(y)|α
|Aut(s)| ψ([x]).
Proof. The only thing that needs to be checked is that the sums converge f or
any ﬁxed choice of y ∈Y . This follows from our explicit criterion for tameness
of spans, Theorem 36.
The most interesting choices of α are α = 0, α = 1, and the symmetrical
choiceα = 1/2. The last convention has the advantage that for a tame span S
with tame adjoint S†, the matrix for the degroupoidiﬁcation of S† is just the
transpose of that for S. We can show:
Proposition 20. For any α ∈ R there is a functor from the category of
groupoids and equivalence classes of tame spans to the categ ory of real vector
spaces and linear operators, sending:
• each groupoid X to its zeroth cohomology RX , and
• each tame span S fromX to Y to the operator Sα
~
: RX → RY .
In particular, if we have composable tame spans:
T
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d31/d31/d64/d64/d64/d64/d64/d64/d64 S
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Z Y X
then their composite
TS
/d125/d125/d124/d124/d124/d124/d124/d124/d124/d124
/d33/d33/d67/d67/d67/d67/d67/d67/d67/d67
Z X
26
is again tame, and
(TS )α
~
=Tα
~
Sα
~
.
We omit the proof because it mimics that of Theorem 41. Note that a
groupoid Ψ over X can be seen as a special case of a span, namely a span
Ψ
v
/d126/d126/d126 /d126 /d126/d126 /d126 /d126/d126
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63
X 1
where 1 is the terminal groupoid—that is, the groupoid with one obje ct and
one morphism. So, α-degroupoidiﬁcation also gives a recipe for turning Ψ into
a vector in RX :
Ψ α
~
[x] = |Aut(x)|α |v−1(x)|. (6)
This idea yields the following result as a special case of Proposition 20:
Proposition 21. Given a tame span:
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
and a tame groupoid over X, say v : Ψ →X, then (SΨ) α
~
=Sα
~
Ψ α
~
Equation 6 also implies that we can compensate for a diﬀerent choice o fα by
doing a change of basis. So, our choice of α is merely a matter of convenience.
More precisely:
Proposition 22. Regardless of the value of α ∈ R, the functors in Proposition
20 are all naturally isomorphic.
Proof. Givenα,β ∈ R, Equation 6 implies that
Ψ α
~
[x] = |Aut(x)|α −β Ψ β
~
[x]
for any tame groupoid Ψ over a groupoid X. So, for any groupoid X, deﬁne a
linear operator
TX : R[X] → R[X]
by
(TXψ)([x]) = |Aut(x)|α −βψ([x]).
We thus have
Ψ α
~
=TX Ψ β
~
.
27
By Proposition 21, for any tame span S fromX toY and any tame groupoid
Ψ over X we have
TYSα
~
Ψ α
~
= TY (SΨ) α
~= ( SΨ) β
~= Sβ
~
Ψ β
~= Sβ
~
TXΨ α
~
Since this is true for all such Ψ, this implies
TYSα
~
=Sβ
~
TX.
So, T deﬁnes a natural isomorphism between α-degroupoidiﬁcation and β-
degroupoidiﬁcation.
Now let us return to homology. We can also do α-degroupoidiﬁcation using
zeroth homology instead of zeroth cohomology. Recall that while th e zeroth
cohomology of X consists of all real-valued functions on X, the zeroth homology
consists of such functions with ﬁnite support . So, we need to work with groupoids
overX that give functions of this type:
Deﬁnition 23. A groupoid Ψ over X is ﬁnitely supported if it is tame and
Ψ
~
is a ﬁnitely supported function on X.
Similarly, we must use spans of groupoids that give linear operators p reserving
this ﬁnite support property:
Deﬁnition 24. A span:
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
is of ﬁnite type if it is a tame span of groupoids and for any ﬁnitely supported
groupoid Ψ over X, the groupoid SΨ over Y (formed by weak pullback) is also
ﬁnitely supported.
With these deﬁnitions, we can reﬁne the previous propositions so th ey apply
to zeroth homology:
Proposition 25. Given any ﬁxed real number α and a span of ﬁnite type:
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
there is a linear operator called its α -degroupoidiﬁcation :
Sα
~
: R[X] → R[Y ]
28
given by:
Sα
~
[x] =
∑
[y]∈Y
∑
[s]∈p−1(x) ⋂ q−1(y)
|Aut(x)|1−α |Aut(y)|α
|Aut(s)| [y].
Proposition 26. For any α ∈ R there is a functor from the category of
groupoids and equivalence classes of spans of ﬁnite type to t he category of real
vector spaces and linear operators, sending:
• each groupoid X to its zeroth homology R[X], and
• each span S of ﬁnite type from X to Y to the operator Sα
~
: R[X] → R[Y ].
Moreover, for all values of α ∈ R, these functors are naturally isomorphic.
Proposition 27. Given a span of ﬁnite type:
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
and a ﬁnitely supported groupoid over X, say v : Ψ →X, then SΨ is a ﬁnitely
supported groupoid over Y , and (SΨ) α
~
=Sα
~
Ψ α
~
.
The moral of this section is that we have several choices to make be fore we
apply degroupoidiﬁcation to any speciﬁc example. The choice of α is merely
a matter of convenience, but there is a real diﬀerence between ho mology and
cohomology, at least for groupoids with inﬁnitely many nonisomorphic objects.
The process described in Section 2 is the combination of choosing to w ork with
cohomology and the convention α = 0 for degroupoidifying spans. This will
suﬃce for the majority of this paper. However, we will use a diﬀeren t choice in
our study of Hall algebras.
4 Groupoidiﬁcation
Degroupoidiﬁcation is a systematic process; groupoidiﬁcation is the attempt
to undo this process. The previous section explains degroupoidiﬁca tion—but
not why groupoidiﬁcation is interesting. The interest lies in its applicat ions to
