---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action Bogus/suppress law Broda1 Department of Theoretical Physics University of /suppress L´ od´ z Pomorska 149/153 PL 90–236 /suppress L´ od´ z Pola"
section_id: sec-005-13-contents
section_title: "Contents"
section_number: 1.3
pages: 4-7
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
doc_brief: "Non-Abelian Stokes theorem in action Bogus/suppress law Broda1 Department of Theoretical Physics University of /suppress Lódź Pomorska 149/153 PL 90–236 /suppress Lódź Poland — In this short review"
---
The propert part of the paper consists of two sections. The ﬁrst section is de-
voted to the non-Abelian Stokes theorem itself. In the beginning, w e introduce
necessary notions and conventions. The operator version of the non-Abelian
Stokes theorem is formulated in the ﬁrst subsection. The second subsection con-
cerns the path-integral versions of the non-Abelian Stokes theo rem: coherent-
state approach and holomorphic approach. The last subsection de scribes gen-
eralizations of the non-Abelian Stokes theorem. First of all, to topo logically
more general situations, and also to higher-degree forms. The se cond section
is devoted to applications of the non-Abelian Stokes theorem in math ematical
and theoretical physics. In the ﬁrst subsection an approach to t he computation
of Wilson loops in two-dimensional Yang-Mills theory is presented. The second
subsection deals with the analogous problem for three-dimensional (topological)
Chern-Simons gauge theory. Other possibilities, including higher-dim ensional
gauge theories and QCD are mentioned in the last subsection.
2 Non-Abelian Stokes theorem
What is the non-Abelian Stokes theorem? To answer this question we should
recall ﬁrst of all the form of the well-known Abelian Stokes theorem . Namely
4
(see, Eq.2) ∫
∂M
ω =
∫
M
dω, (6)
where the integral of the form ω along the boundary ∂N of the submanifold N is
equated to the integral of the diﬀerentialdω of this form over the submanifoldN.
The diﬀerential form ω is usually an ordinary (i.e. Abelian) diﬀerential form, but
it could also be something more general, e.g. connection one-form A. Thus, the
non-Abelian Stokes theorem should be a version of 6 for non-Abelian (say, Lie-
algebra valued) forms. Since it could be risky to directly integrate Lie -algebra
valued diﬀerential forms, the generalization of 6 may be a non-trivia l task. We
should not be too ambitious perhaps from the very beginning, and no t try to
formulate the non-Abelian Stokes theorem in full generality at once , as it could
be diﬃcult or even impossible simply. The lowest non-trivial dimensionalit y of
the objects entering 6 is as follows: dim N = 2 (dim ∂N = 1) and deg ω = 1
(deg dω = 2). A short reﬂection leads us to the ﬁrst candidate for the LHS o f
the non-Abelian Stokes theorem, the Wilson loop
P exp
(
i
∮
C
A
)
, (7)
called the holonomy, in mathematical context, where P denotes the , so-called,
path ordering, A is a non-Abelian connection one-form, and C is a closed loop,
a boundary of the surface S (∂S = C). Correspondingly, the RHS of the non-
Abelian Stokes theorem should contain a kind of integration over S. Therefore,
the actual Abelian prototype of the non-Abelian Stokes theorem is of the form
5 rather than of 4. More often, the trace of Eq.7 is called the Wilson lo op,
WR(C) = TrRP exp
(
i
∮
C
A
)
, (8)
or even the “normalized” trace of it,
1
dim RTrRP exp
(
i
∮
C
A
)
, (9)
where the character R means a(n irreducible) representation of the Lie group G
corresponding to the given Lie algebra g. Of course, one can easily pass from
5
7 to 8 and ﬁnally to 9. In fact, the operator 7 is a particular case of a more
general parallel-transport operator
UL = P exp
(
i
∫
L
A
)
, (10)
where L is a smooth path, which for the L a closed loop ( L = C) yields 7.
Eq.10 could be considered as an ancestor of Eq.7. As the LHS of the n on-
Abelian Stokes theorem we can assume any of the formulas given abo ve for
the closed loop C (i.e. Eqs.7, 8, 9) yielding possibly various versions of the
non-Abelian Stokes theorem. For some reason or another, somet imes it is more
convenient to use the Wilson loop in the operator version 7 rather th an in the
version with the trace 8. Sometimes it does not make any bigger diﬀer ence.
The RHS should be some expression deﬁned on the surface S, and essentially
constituting the non-Abelian Stokes theorem.
From the point of view of a physicist the expression 10 is typical in quantum
mechanics and corresponds to the evolution operator. By the way , Eqs.8, 9 are
very typical in gauge theory, e.g. in QCD. Thus, guided by our intuition we can
reformulate our chief problem as a quantum-mechanical one. In ot her words,
the approaches to the LHS of the non-Abelian Stokes theorem are analogous to
the approaches to the evolution operator in quantum mechanics. T here are the
two main approaches to quantum mechanics, and especially to the co nstruction
of the evolution operator: opearator approach and path-integr al approach. The
both can be applied to the non-Abelian Stokes theorem successfully , and the
both provide two diﬀerent formulations of the non-Abelian Stokes t heorem.
Conventions Sometimes, especially in a physical context, a coupling con-
stant, denoted e.g. e, appears in front of the integral in Eqs.7–10. For simplicity,
we will omit the coupling constant in our formulas.
The non-Abelian curvature or the strength ﬁeld on the manifoldM is deﬁned
by
Fij(A) = ∂iAj − ∂jAi − i[Ai, Aj].
Here, the connection or the gauge potentialA assuming values in a(n irreducible)
6
representation R of the compact, semisimple Lie algebra g of the Lie group G
is of the form
Ai(x) = Aa
i (x)T a, i = 1, . . . ,dim M,
where the Hermitian generators, T a† = T a, T a = T a
kl, k, l = 1, . . . ,dim R, fulﬁl
the commutation relations
[T a, T b] = if abcT c, a, b, c = 1, . . . ,dim G. (11)
The line integral 10 can be rewritten in more detailed (being frequent ly used in
our further analysis) forms,
U(x′′, x′) = P exp
[
i
∫ x′′
x′
Ai(x) dxi
]
,
or
Ukl = P exp
[
i
∫ x′′
x′
Aa
i (x)T a dxi
]
,
without parametrization, and
U(t′′, t′) = P exp
{
i
∫ x′′
x′
Aa
i [x(t)]T a dxi(t)
dt dt
}
,
with an explicit parametrization, or some variations of thereof. Her e, the ori-
ented smooth path L starting at the point x′ and endng at the point x′′ is
parametrized by the function xi(t), where t′ ≤ t ≤ t′′, and x′i = xi(t′),
x′′i = xi(t′′).
