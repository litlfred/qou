---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-012-45-automorphism-2-groups
section_title: "Automorphism 2-Groups"
section_number: 4.5
pages: 38-40
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 1.0
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{automorphism}

The inner automorphism group of the previous section is
closely related to the \define{automorphism 2-group} $\AUT(H)$, 
defined using the crossed module where:
\begin{itemize}
\item $G = \Aut(H)$,
\item $H$ is any Lie group,
\item $t \maps H \to \Aut(H)$ sends any group element to the operation
of conjugating by that element,
\item $\alpha \maps \Aut(H) \to \Aut(H)$ is the identity.
\end{itemize}
We use the term `automorphism 2-group' because $\AUT(H)$ really is the
2-group of symmetries of $H$.  Lie groups form a 2-category, any object
in a 2-category has a 2-group of symmetries, and the 2-group of 
symmetries of $H$ is naturally a Lie 2-group, which is none other than
$\AUT(H)$.  See \cite{BaezLauda:2groups} for details.

A principal $\AUT(H)$-2-bundle is usually called a \define{nonabelian 
gerbe} \cite{Breen:2006}.  Nonabelian gerbes are a major test case 
for ideas in higher gauge theory.  Indeed, almost the whole 
formalism of 2-connections was worked out first for nonabelian 
gerbes by Breen and Messing \cite{BreenMessing}.  The one aspect 
they did not consider is the one we have focused on here: parallel 
transport.  Thus, they did not impose the equation $\dt(B) = F$, 
which we need to obtain holonomies satisfying the conditions of 
Theorem \ref{thm:2-connections}.  Nonetheless, the quantity 
$F - \dt(B)$ plays an important role in Breen and Messing's 
formalism: they call it the \define{fake curvature}.  Generalizing
their ideas slightly, for any Lie 2-group $\G$, we may define a 
\define{connection} on a trivial principal $\G$-2-bundle to be a 
pair consisting of a $\g$-valued 1-form $A$ and an $\h$-valued 2-form.  
A 2-connection is then a connection with vanishing fake curvature.

The relation between the automorphism 2-group and the inner
automorphism 2-group is nicely explained in the work of Roberts and
Schreiber \cite{RobertsSchreiber}.   As they discuss, for any group $G$
there is an exact sequence of 2-groups
\[  
1 \to \ZZ(G) \to \INN(G) \to \AUT(G) \to \OUT(G) \to 1
\]
where $\ZZ(G)$ is the center of $G$ and $\OUT(G)$ is the group of
outer automorphisms of $G$, both regarded as 2-groups with only
identity 2-morphisms.  

Roberts and Schreiber go on to consider an analogous sequence of
\emph{3-groups} constructed starting from a 2-group.  Among these, the
`inner automorphism 3-group' $\INN(\G)$ of a 2-group $\G$ plays a
special role \cite{Schreiber:cafe}.  The reason is that any connection
on a principal $\G$-2-bundle, not necessarily obeying $\dt(B) = F$,
gives a flat 3-connection on a principal $\INN(\G)$-3-bundle!  This in
turn allows us to define a version of parallel transport for
particles, strings \emph{and 2-branes}.

This may give a way to understand general relativity in terms of
higher gauge theory.  As we have already seen in Section
\ref{tangent}, Palatini gravity in 4d spacetime involves an
$\so(3,1)$-valued 1-form $A$ and an $\so(3,1)$-valued 2-form $B = e
\wedge e$.  This is precisely the data we expect for a connection on a
principal $\G$-2-bundle where $\G$ is the tangent 2-group of the
Lorentz group.  Typically this connection fails to obey the equation
$\dt(B) = F$.  So, it is not a 2-connection.  But, it gives a flat
3-connection on an $\INN(\T\SO(3,1))$-3-bundle.  So, we may optimistically
call $\INN(\T\SO(3,1))$ the \define{gravity 3-group}.

Does the gravity 3-group actually shed any light on general relativity?
The work of Martins and Picken \cite{MartinsPicken:2009} establishes a
useful framework for studying these issues.  They define a path
3-groupoid $\P_3(M)$ for a smooth manifold $M$.  Given a Lie 3-group
${\bf G}$, they describe 3-connections on the trivial ${\bf
G}$-3-bundle over $M$ as 3-functors
\[                   \hol \maps \P_3(M) \to {\bf G}  \]
Moreover, they show how to construct these functors from a 1-form, a
2-form, and a 3-form taking values in three Lie algebras associated to
${\bf G}$.  In the case where ${\bf G} = \INN(\T\SO(3,1))$ and 
$\hol$ is a flat 3-connection, this data reduces to an
$\so(3,1)$-valued 1-form $A$ and an $\so(3,1)$-valued 2-form $B$.
