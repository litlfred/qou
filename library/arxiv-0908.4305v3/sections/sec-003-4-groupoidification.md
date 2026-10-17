---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidiﬁcation"
section_id: sec-003-4-groupoidification
section_title: "Groupoidification"
section_number: 4
pages: 28-29
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
toc_source: outline
---
So, T deﬁnes a natural isomorphism between α-degroupoidiﬁcation and β-
degroupoidiﬁcation.
Now let us return to homology. We can also do α-degroupoidiﬁcation using
zeroth homology instead of zeroth cohomology. Recall that while the zeroth
cohomology of X consists of all real-valued functions on X, the zeroth homology
consists of such functions with ﬁnite support. So, we need to work with groupoids
over X that give functions of this type:
Deﬁnition 23. A groupoid Ψ over X is ﬁnitely supported if it is tame and
Ψ
e
is a ﬁnitely supported function on X.
Similarly, we must use spans of groupoids that give linear operators preserving
this ﬁnite support property:
Deﬁnition 24. A span:
S
q
 
p
@
@
@
@
@
@
@
Y
X
is of ﬁnite type if it is a tame span of groupoids and for any ﬁnitely supported
groupoid Ψ over X, the groupoid SΨ over Y (formed by weak pullback) is also
ﬁnitely supported.
With these deﬁnitions, we can reﬁne the previous propositions so they apply
to zeroth homology:
Proposition 25. Given any ﬁxed real number α and a span of ﬁnite type:
S
q
 
p
@
@
@
@
@
@
@
Y
X
there is a linear operator called its α-degroupoidiﬁcation:
Sα
f
: R[X] →R[Y ]
28
given by:
Sα
f
[x] =
X
[y]∈Y
X
[s]∈p−1(x) T q−1(y)
|Aut(x)|1−α|Aut(y)|α
|Aut(s)|
[y] .
Proposition 26. For any α ∈R there is a functor from the category of
groupoids and equivalence classes of spans of ﬁnite type to the category of real
vector spaces and linear operators, sending:
• each groupoid X to its zeroth homology R[X], and
• each span S of ﬁnite type from X to Y to the operator Sα
f
: R[X] →R[Y ].
Moreover, for all values of α ∈R, these functors are naturally isomorphic.
Proposition 27. Given a span of ﬁnite type:
S
q
 
p
@
@
@
@
@
@
@
Y
X
and a ﬁnitely supported groupoid over X, say v: Ψ →X, then SΨ is a ﬁnitely
supported groupoid over Y , and (SΨ)α
^
= Sα
f
Ψα
f
.
The moral of this section is that we have several choices to make before we
apply degroupoidiﬁcation to any speciﬁc example. The choice of α is merely
a matter of convenience, but there is a real diﬀerence between homology and
cohomology, at least for groupoids with inﬁnitely many nonisomorphic objects.
The process described in Section 2 is the combination of choosing to work with
cohomology and the convention α = 0 for degroupoidifying spans. This will
suﬃce for the majority of this paper. However, we will use a diﬀerent choice in
our study of Hall algebras.
4
Groupoidiﬁcation
Degroupoidiﬁcation is a systematic process; groupoidiﬁcation is the attempt
to undo this process. The previous section explains degroupoidiﬁcation—but
not why groupoidiﬁcation is interesting. The interest lies in its applications to
