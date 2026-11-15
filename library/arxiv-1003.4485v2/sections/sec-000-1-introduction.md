---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.881
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{introduction}

Higher gauge theory is a generalization of gauge theory that describes
parallel transport, not just for point particles, but also for
higher-dimensional extended objects.  It is a beautiful new branch of
mathematics, with a lot of room left for exploration.  It has already
been applied to string theory and loop quantum gravity---or more
specifically, spin foam models.  This should not be surprising, since
while these rival approaches to quantum gravity disagree about almost
everything, they both agree that point particles are not enough: we
need higher-dimensional extended objects to build a theory
sufficiently rich to describe the quantum geometry of spacetime.
Indeed, many existing ideas from string theory and supergravity have
recently been clarified by higher gauge theory \cite{Sati,SSS}.  But
we may also hope for applications of higher gauge theory to other less
speculative branches of physics, such as condensed matter physics.

Of course, for this to happen, more physicists need to learn higher
gauge theory.  It would be great to have a comprehensive introduction
to the subject which started from scratch and led the reader to the
frontiers of knowledge.  Unfortunately, mathematical work in this
subject uses a wide array of tools, such as $n$-categories, stacks,
gerbes, Deligne cohomology, $L_\infty$ algebras, Kan complexes, and
$(\infty,1)$-categories, to name just a few.  While these tools are
beautiful, important in their own right, and perhaps necessary for a
deep understanding of higher gauge theory, learning them takes
time---and explaining them all would be a major project.

Our goal here is far more modest.  We shall sketch how to generalize
the theory of parallel transport from point particles to 1-dimensional
objects, such as strings.  We shall do this starting with a bare
minimum of prerequisites: manifolds, differential forms, Lie groups,
Lie algebras, and the traditional theory of parallel transport in
terms of bundles and connections.  We shall give a small taste of the
applications to physics, and point the reader to the literature for
more details.

In Section \ref{connections} we start by explaining categories,
functors, and how parallel transport for particles can be seen as a
functor taking any path in a manifold to the operation of parallel
transport along that path.  In Section \ref{2-connections} we `add
one' and explain how parallel transport for particles and strings can
be seen as `2-functor' between `2-categories'.  This requires that we
generalize Lie groups to `Lie 2-groups'.  In Section \ref{examples}
we describe many examples of Lie 2-groups, and sketch some of their
applications:
\begin{itemize}
\item Section \ref{abelian}: shifted abelian groups, $\U(1)$ gerbes,
and their role in string theory and multisymplectic geometry.
\item Section \ref{poincare}: the Poincar\'e 2-group and the 
spin foam model for 4d Minkowski spacetime.
\item Section \ref{tangent}: tangent 2-groups, 4d $BF$ theory and
topological gravity.  
\item Section \ref{inner}: inner automorphism 2-groups and 
4d $BF$ theory with cosmological constant term.
\item Section \ref{automorphism}: automorphism 2-groups, nonabelian
gerbes, and the gravity 3-group.
\item Section \ref{string}: string 2-groups, string structures, 
the passage from Lie $n$-algebras to Lie $n$-groups, and the
Lie 3-superalgebra governing 11-dimensional supergravity.
\end{itemize}
Finally, in Section \ref{last} we discuss gauge transformations,
curvature and nontrivial 2-bundles.
