---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-011-44-inner-automorphism-2-groups
section_title: "Inner Automorphism 2-Groups"
section_number: 4.4
pages: 37-38
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.995
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{inner}

There is also a Lie 2-group where:
\begin{itemize}
\item $G$ is any Lie group,
\item $H = G$,
\item $t$ is the identity map,
\item $\alpha$ is conjugation:
\[ \alpha(g) h = ghg^{-1}. \]
\end{itemize}
Following Roberts and Schreiber \cite{RobertsSchreiber} we call this
the \define{inner automorphism 2-group} of $G$, and denote it by
$\INN(G)$.  We explain this terminology in the next
section.  

A 2-connection on the trivial $\INN(G)$-2-bundle over a manifold
consists of a $\g$-valued 1-form $A$ and a $\g$-valued 2-form $B$ such
that
\[  B = F  \]
since $\dt$ is now the identity.  Intriguingly, 2-connections of this
sort show up as solutions of a slight variant of 4d $BF$ theory.  In a
move that he later called his biggest blunder, Einstein took general
relativity and threw an extra term into the equations: a `cosmological
constant' term, which gives the vacuum nonzero energy.  We can do the
same for topological gravity, or indeed 4d $BF$ theory for any group
$G$.  After all, what counts as a blunder for Einstein might count
as a good idea for lesser mortals such as ourselves.

So, fix a $4$-dimensional oriented manifold $M$ as our spacetime.  As
in ordinary $BF$ theory, take the fields to be a connection $A$ on the
trivial principal $G$-bundle over $M$, together with a $\g$-valued
$2$-form $B$.  The action for $BF$ theory `with cosmological constant'
is defined to be
\[  S(A,B) = \int_M \tr(B \wedge F - \frac{\lambda}{2} B \wedge B). \]
Setting the variation of the action equal to zero, we obtain these
field equations:
\[ dB + [A,B] = 0 , \quad F = \lambda B . \]
When $\lambda = 0$, these are just the equations we saw in the
previous section.  But let us consider the case $\lambda \ne 0$.  Then
these equations have a drastically different character!  The Bianchi
identity $dF + [A,F] = 0$, together with $F = \lambda B$,
automatically implies that $dB + [A,B] = 0$.  So, to get a solution of
this theory we simply take any connection $A$, compute its curvature
$F$ and set $B = F/\lambda$.

This may seem boring: a field theory where any connection is a
solution.  But in fact it has an interesting relation to higher gauge
theory.  To see this, it helps to change variables and work with the
field $\beta = \lambda B$.  Then the field equations become
\[ d \beta + [A,\beta] = 0 , \quad F = \beta. \]
Any solution of these equations gives a 2-connection on the
trivial principal $\INN(G)$-2-bundle over $M$!

There is also a tantalizing relation to the cosmological
constant in general relativity.  If the $B$ field arises
from a cotetrad as explained in the previous section:
\[           B = e \wedge e , \]
then the above action becomes 
\[  S = \int_M \tr(e \wedge e \wedge F - \frac{\lambda}{2} e \wedge
e \wedge e \wedge e). \]
When we choose the bilinear form `$\tr$' correctly, 
this is the action for general relativity with a cosmological 
constant proportional to $\lambda$.  

There is some evidence \cite{Baez:BF} that $BF$ theory with nonzero
cosmological constant can be quantized to obtain the so-called
Crane--Yetter model \cite{CKY, CY}, which is a spin foam model based
on the category of representations of the quantum group associated to
$G$.  Indeed, in some circles this is taken almost as an article of
faith.  But a rigorous argument, or even a fully convincing argument,
seems to be missing.  So, this issue deserves more study.

The $\lambda \to 0$ limit of $BF$ theory is fascinating but highly
singular, since for $\lambda \ne 0$ a solution is just a connection
$A$, while for $\lambda = 0$ a solution is a flat connection $A$
together with a $B$ field such that $dB + [A,B] = 0$.  At least in some
rough intuitive sense, as $\lambda \to 0$ the group $H$ in the crossed
module corresponding to $\INN(G)$ `expands and flattens out'
from the group $G$ to its tangent space $\g$.  Thus, $\INN(G)$
degenerates to the tangent 2-group $\T G$.  It would be nice to make
this precise using a 2-group version of the theory of group contractions.
