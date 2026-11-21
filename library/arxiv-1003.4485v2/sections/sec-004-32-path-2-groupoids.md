---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-004-32-path-2-groupoids
section_title: "Path 2-Groupoids"
section_number: 3.2
pages: 14-15
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 1.0
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
Path groupoids play a big though often neglected role in physics: the
path groupoid of a spacetime manifold describes all the possible
motions of a point particle in that spacetime.  The path 2-groupoid
does the same thing for particles \textit{and strings}.

First of all, a {\bf 2-groupoid} is a 2-category where:
\begin{itemize}
\item
Every morphism $f \maps x \to y$ has an \define{inverse},
$f^{-1} \maps y \to x$, such that:
\[      f^{-1} f = 1_x  
\quad \textrm{and} \quad
f f^{-1} = 1_y . \]
\item
Every 2-morphism $\alpha \maps f \To g$ has a \define{vertical inverse},
$\alpha^{-1}_{\textrm{\small vert}} \maps g \To f$, such that:
\[     \alpha^{-1}_{\textrm{\small vert}} \cdot \alpha = 1_f   
\quad \textrm{and} \quad
       \alpha \cdot \alpha^{-1}_{\textrm{\small vert}} = 1_f . \]
\end{itemize}
It actually follows from this definition that every 2-morphism 
$\alpha \maps f \To g$ also has a \define{horizontal inverse}, 
$\alpha^{-1}_{\textrm{\small hor}} \maps f^{-1} \To g^{-1}$, such that:
\[     \alpha^{-1}_{\textrm{\small hor}} \circ \alpha = 1_{1_x}  
\quad \textrm{and} \quad
       \alpha \circ \alpha^{-1}_{\textrm{\small hor}} = 1_{1_x} . \]
So, a 2-groupoid has every kind of inverse your heart could desire.

An example of a 2-group is the `path 2-groupoid' of a smooth manifold
$M$.  To define this, we can start with the path groupoid $\P_1(M)$ as
defined in the previous section, and then throw in 2-morphisms.  Just
as the morphisms in $\P_1(M)$ were thin homotopy classes of lazy paths, 
these 2-morphisms will be thin homotopy classes of lazy surfaces.

What is a `lazy surface'?   First, recall that a \define{homotopy}
between lazy paths $\gamma, \delta \maps x \to y$ is a smooth map
$\Sigma \maps [0,1]^2 \to M$ with
\[   \Sigma(0,t) = \gamma(t)  \]
\[   \Sigma(1,t) = \delta(t)  \] 
We say this homotopy is a \define{lazy surface} if 
\begin{itemize}
\item
$\Sigma(s,t)$ is independent of $s$ near $s = 0$ and near $s = 1$, 
\item
$\Sigma(s,t)$ is constant near $t = 0$ and constant near $t = 1$.
\end{itemize}
Any homotopy $\Sigma$ yields a one-parameter family of paths 
$\gamma_s$ given by
\[             \gamma_s(t) = \Sigma(s,t) .\]
If $\Sigma$ is a lazy surface, each of these paths is lazy.
Furthermore, the path $\gamma_s$ equals $\gamma_0$ when $s$ is
sufficiently close to $0$, and it equals $\gamma_1$ when $s$ is
sufficiently close to $1$.  This allows us to compose lazy homotopies
either vertically or horizontally and obtain new lazy homotopies!

However, vertical and horizontal composition will only obey the
2-groupoid axioms if we take 2-morphisms in the path 2-groupoid to be
\emph{equivalence} classes of lazy surfaces.  We saw this kind of
issue already when discussing the path groupoid, so we we will allow
ourselves to be a bit sketchy this time.  The key idea is to define a
concept of `thin homotopy' between lazy surfaces $\Sigma$ and $\Xi$.
For starters, this should be a smooth map $H \maps [0,1]^3 \to M$ such
that $H(0,s,t) = \Sigma(s,t)$ and $H(1,s,t) = \Xi(s,t)$.  But we also
want $H$ to be `thin'.  In other words, it should sweep out no volume:
the rank of the differential $dH$ should be less than $3$ at every
point.  

To make thin homotopies well-defined between thin homotopy classes of
paths, some more technical conditions are also useful.  For these, the
reader can turn to Section 2.1 of Schreiber and Waldorf
\cite{SchreiberWaldorf:functors}.  The upshot is that we obtain
for any smooth manifold $M$ a \define{path 2-groupoid} $\P_2(M)$, 
in which:
\begin{itemize}
\item An object is a point of $M$.
\item A morphism from $x$ to $y$ is a thin homotopy class of lazy paths
from $x$ to $y$.  
\item A 2-morphism between equivalence classes of lazy paths
$\gamma_0, \gamma_1 \maps x \to y$ is a thin homotopy class of
lazy surfaces $\Sigma \maps \gamma_0 \To \gamma_1$.  
\end{itemize}
As we already did with the concept of `lazy path', we will often use
`lazy surface' to mean a thin homotopy class of lazy surfaces.  But 
now let us hasten on to another important class of 2-groupoids, the 
`2-groups'.  Just as groups describe symmetries in gauge theory, these
describe symmetries in higher gauge theory.
