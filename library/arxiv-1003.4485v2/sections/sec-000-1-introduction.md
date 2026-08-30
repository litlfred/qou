---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
port for particles and strings in terms of 2-connections on 2 -bundles. Just
as ordinary gauge theory involves a gauge group, this genera lization in-
volves a gauge ‘2-group’. We focus on 6 examples. First, ever y abelian
Lie group gives a Lie 2-group; the case of U(1) yields the theo ry of U(1)
gerbes, which play an important role in string theory and mul tisymplec-
tic geometry. Second, every group representation gives a Li e 2-group; the
representation of the Lorentz group on 4d Minkowski spaceti me gives the
Poincar´ e 2-group, which leads to a spin foam model for Minko wski space-
time. Third, taking the adjoint representation of any Lie gr oup on its own
Lie algebra gives a ‘tangent 2-group’, which serves as a gaug e 2-group in
4d BF theory, which has topological gravity as a special case. Fou rth,
every Lie group has an ‘inner automorphism 2-group’, which s erves as the
gauge group in 4d BF theory with cosmological constant term. Fifth, ev-
ery Lie group has an ‘automorphism 2-group’, which plays an i mportant
role in the theory of nonabelian gerbes. And sixth, every com pact simple
Lie group gives a ‘string 2-group’. We also touch upon higher structures
such as the ‘gravity 3-group’, and the Lie 3-superalgebra th at governs
11-dimensional supergravity.
1 Introduction
Higher gauge theory is a generalization of gauge theory that descr ibes parallel
transport, not just for point particles, but also for higher-dimen sional extended
objects. It is a beautiful new branch of mathematics, with a lot of r oom left
for exploration. It has already been applied to string theory and loo p quantum
gravity—or more speciﬁcally, spin foam models. This should not be sur prising,
since while these rival approaches to quantum gravity disagree abo ut almost
1
everything, they both agree that point particles are not enough: we need higher-
dimensional extended objects to build a theory suﬃciently rich to de scribe the
quantum geometry of spacetime. Indeed, many existing ideas from string theory
and supergravity have recently been clariﬁed by higher gauge theo ry [82, 83].
But we may also hope for applications of higher gauge theory to othe r less
speculative branches of physics, such as condensed matter phys ics.
Of course, for this to happen, more physicists need to learn higher gauge
theory. It would be great to have a comprehensive introduction to the subject
which started from scratch and led the reader to the frontiers of knowledge. Un-
fortunately, mathematical work in this subject uses a wide array o f tools, such as
n-categories, stacks, gerbes, Deligne cohomology, L∞ algebras, Kan complexes,
and ( ∞, 1)-categories, to name just a few. While these tools are beautiful, im-
portant in their own right, and perhaps necessary for a deep unde rstanding of
higher gauge theory, learning them takes time—and explaining them a ll would
be a major project.
Our goal here is far more modest. We shall sketch how to generalize the
theory of parallel transport from point particles to 1-dimensional objects, such
as strings. We shall do this starting with a bare minimum of prerequisit es:
manifolds, diﬀerential forms, Lie groups, Lie algebras, and the tra ditional theory
of parallel transport in terms of bundles and connections. We shall give a small
taste of the applications to physics, and point the reader to the lite rature for
more details.
In Section 2 we start by explaining categories, functors, and how p arallel
transport for particles can be seen as a functor taking any path in a manifold
to the operation of parallel transport along that path. In Section 3 we ‘add
one’ and explain how parallel transport for particles and strings ca n be seen as
‘2-functor’ between ‘2-categories’. This requires that we genera lize Lie groups
to ‘Lie 2-groups’. In Section 4 we describe many examples of Lie 2-gro ups, and
sketch some of their applications:
• Section 4.1: shifted abelian groups, U(1) gerbes, and their role in st ring
theory and multisymplectic geometry.
• Section 4.2: the Poincar´ e 2-group and the spin foam model for 4d Minkowski
spacetime.
• Section 4.3: tangent 2-groups, 4d BF theory and topological gravity.
• Section 4.4: inner automorphism 2-groups and 4d BF theory with cosmo-
logical constant term.
• Section 4.5: automorphism 2-groups, nonabelian gerbes, and the g ravity
3-group.
• Section 4.6: string 2-groups, string structures, the passage fr om Lie n-
algebras to Lie n-groups, and the Lie 3-superalgebra governing 11-dimensional
supergravity.
2
Finally, in Section 5 we discuss gauge transformations, curvature a nd nontrivial
2-bundles.
