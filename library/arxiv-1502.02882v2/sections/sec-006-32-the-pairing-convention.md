---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-006-32-the-pairing-convention
section_title: "The pairing convention"
section_number: 3.2
pages: 8-10
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
The pairing convention
Deﬁnition 3.5. A root choice on a fusion category is a symmetric choice {di}
of square roots of the paired dimensions; that is, one which satisﬁes
d2
i = d{i,i∗} and di = di∗for all i ∈I.
1The notion of a paired dimension is due to M¨uger [18, Prop 2.4], where it is written as
d2(X), but not named explicitly. The terminology and notation is our own.
8
The utility of a root choice is that it allows the following diagrammatic
convention.
Pairing convention. Whenever a unit
which is part of a unit-
counit pair expressing a simple object X∗
i as a right dual of Xi appears
together in some equation with a counit
which is part of a unit-
counit pair expressing X∗
i as a left dual of Xi, it will always be under-
stood that the former is arbitrary while the latter is determined uniquely
by the requirement that
= di
Similarly (and equivalently), whenever
appears in a diagram to-
gether with
, the latter will always be ﬁxed uniquely by the re-
quirement that
= di.
The pairing convention is the key diagrammatic idea in this paper. Using
this convention, we only need to ﬁx a root choice (and not a pivotal struc-
ture, which is not known to exist in general) on the fusion category in order to
unambiguously perform string diagram calculations where both left and right
duals appear. Note that the pairing convention extends uniquely to the whole
category and not just the simple objects, see Section 3.5.
Remark 3.6. We will presently show in Theorem 3.19 that the paired dimen-
sions d{i,i∗} are positive real numbers. From then on, we will always work with
the canonical root choice on a fusion category given by the positive square roots.
Although we will not need it in this paper, we can extend the pairing conven-
tion to all objects in C, not just simple ones. Namely, suppose V ∈C. For each
representative simple object Xi, choose a basis ei,α : Xi →V for Hom(Xi, V ),
with corresponding dual basis ˆei,α : V →Xi. If, in a diagram, a unit
which is part of a unit-counit pair (η, ϵ) expressing V ∗as a right dual of V
appears together with a counit
which is part of a unit-counit pair (n, e) expressing V ∗as a left dual of V , it
9
will be understood that the former is arbitrary while the latter is deﬁned as
:=
X
i,α
.
Note that this deﬁnition is independent of the choice of basis ei,α.
