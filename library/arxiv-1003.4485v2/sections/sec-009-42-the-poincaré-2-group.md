---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-009-42-the-poincaré-2-group
section_title: "The Poincaré 2-Group"
section_number: 4.2
pages: 32-33
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.994
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{poincare}

Suppose we have a representation $\alpha$ of a Lie group $G$ on a
finite-dimensional vector space $H$.  We can regard $H$ as an abelian
Lie group with addition as the group operation.  This lets us
regard $\alpha$ as an action of $G$ on this abelian Lie group.
So, we can build a 2-group $\G$ where:
\begin{itemize}
\item $G$ is any Lie group,
\item $H$ is any vector space,
\item $\alpha$ is the representation of $G$ on $H$, and
\item $t$ is trivial.
\end{itemize}
In particular, note that the Peiffer identity holds.  In this way, we
see that any group representation gives a crossed module---so group
representations are secretly 2-groups!

For example, if we let $G$ be the Lorentz group and let $\alpha$ be
its obvious representation on $\R^4$:
\[ G = \SO(3,1) \]
\[ H = \R^4 \]
we obtain the so-called \define{Poincar\'e 2-group}, which has the
Lorentz group as its group of morphisms, and the Poincar\'e group as
its group of 2-morphisms \cite{BaezLauda:2groups}.

What is the Poincar\'e 2-group good for?  It is not clear, but there
are some clues.  Just as we can study representations of groups on
vector spaces, we can study representations of 2-groups on `2-vector
spaces' \cite{BBFW, BarrettMackaay,CraneYetter,Elgueta2}.  The
representations of a group are the objects of a category, and this
sort of category can be used to build `spin foam models' of
background-free quantum field theories \cite{Baez:spinfoam}.  This
endeavor has been most successful with 3d quantum gravity
\cite{FreidelLouapre}, but everyone working on this subject dreams
of doing something similar for 4d quantum gravity \cite{Rovelli}.
Going from groups to 2-groups boosts the dimension of everything:
the representations of a 2-group are the objects of a
\emph{2-category}, and Crane and Sheppeard outlined a program for
building a 4-dimensional spin foam model starting from the 2-category of
representations of the Poincar\'e 2-group \cite{CraneSheppeard}.

Crane and Sheppeard hoped their model would be related to quantum
gravity in 4 spacetime dimensions.  This has not come to pass, at least
not yet---but this spin foam model \textit{does} have interesting
connections to 4d physics.  The spin foam model of 3d quantum gravity
automatically includes point particles, and Baratin and Freidel have
shown that it reduces to the usual theory of Feynman diagrams in 3d
Minkowski spacetime in the limit where the gravitational constant
$G_{\textrm{{\tiny Newton}}}$ goes to zero \cite{BaratinFreidel:3d}.
This line of thought led Baratin and Freidel to construct a spin foam
model that is equivalent to the usual theory of Feynman diagrams in 4d
Minkowski spacetime \cite{BaratinFreidel:4d}.  At first the
mathematics underlying this model was a bit mysterious---but it now
seems clear that this model is based on the representation theory of
the Poincar\'e 2-group!  For a preliminary report on this fascinating
research, see the paper by Baratin and Wise \cite{BaratinWise}.

In short, it appears that the 2-category of representations of the
Poincar\'e 2-group gives a spin foam description of quantum field
theory on 4d Minkowski spacetime.  Unfortunately, while spin foam
models in 3 dimensions can be obtained by quantizing gauge theories,
we do not see how to obtain this 4d spin foam model by quantizing a
higher gauge theory.  Indeed, we know of no classical field theory in
4 dimensions whose solutions are 2-connections on a principal
$\G$-2-bundle where $\G$ is the Poincar\'e 2-group.

However, if we replace the Poincar\'e 2-group by a closely related
2-group, this puzzle \emph{does} have a nice solution.  Namely, if
we take 
\[ G = \SO(3,1) \]
\[ H = \so(3,1) \]
and take $\alpha$ to be the adjoint representation, we obtain the
`tangent 2-group' of the Lorentz group.  As we shall see,
2-connections for this 2-group arise naturally as solutions of a 
4d field theory called `topological gravity'.
