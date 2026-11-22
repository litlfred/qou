---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.973
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
Representation varieties of finitely presented  groups into Lie groups has been studied since a long time.  A recent by Sikora paper with many references
is  \cite{Sikora}.  In this paper we concentrate on the representations of 3-manifold groups in $\PGL(3,\bC)$ or $\SL(3,\bC)$.
  The case of surface groups have been studied more extensively and their  representation varieties
into $\SL(3,\bC)$ are treated by Lawton in \cite{Lawton}.  On the other hand, only recently the study
of representations of 3-manifold groups into $\SL(3,\bC)$ or  $\PGL(3,\bC)$  has been started. See for instance the work of Porti and Menal-Ferer \cite{MF}, of Garoufalidis, Goerner, Thurston and Zickert \cite{GTZ,GGZ} and of Bergeron with the two first named authors \cite{BFG} among others.  One has to keep in mind
the deep study which was started in the last decades of the last century on representations into $\SL(2,\bC)$ by several authors among them
Thurston \cite{Thurston}.  It gives a paradigm for the present study in the case of  $\PGL(3,\bC)$.  

Let $\Geight$ be the fundamental group of the figure eight knot complement. We present here a thorough study of the space of representations of $\Geight$ into $\PGL(3,\bC)$ and $\SL(3,\bC)$.  It turns out that all the irreducible representations we find in  $\PGL(3,\bC)$ can be lifted to $\SL(3,\bC)$.  Therefore, most of the computations will be made in $\PGL(3,\bC)$ but we will occasionally work with $\SL(3,\bC)$.

We begin with a review of different versions of this space (representation variety, character variety, decorated representations among others) and the coordinates we use to study these varieties in a rather general setting.  A diagram, displayed in Figure \ref{fig:diagram}, shows the several representation spaces and their relations.  The main coordinate system we use is derived from projective flag decorations of ideal triangulations of a 3-manifold as introduced in \cite{BFG} (see also \cite{GGZ}).   Another view of these spaces is given in  \cite{Zickert-A-pol} using Ptolemy coordinates, which are coordinates for affine flags decorations of ideal triangulations. Those work are accessible through the website CURVE \cite{CURVE}.

\begin{comment}
A simplest representation variety for the fundamental group of a 3-manifold is the one for representations  into $\SL(3,\bC)$ instead of $\PGL(3,\bC)$. 
In section \ref{dimension} we obtain a lower bound for the dimension of the representation space
of the fundamental group of a 3-manifold into $\SL(3,\bC)$ analogue to the bound obtained 
in \cite{CS}  (propostion 3.2.1) and \cite{Thurston}.  In the case of a 3-manifold with 
a torus boundary it implies that all components containing an irreducible representation with infinite 
image are of dimension at least two.  
Moreover, in the case of a hyperbolic manifold with boundary,  the irreducible component containing the 
geometric representation (that is the composition of the $\SL(2,\bC)$ representation with the
irreducible monomorphism of $\SL(2,\bC)$ into $\SL(3,\bC)$)
has dimension equal to twice the number of cusps. 
\end{comment}

Then we proceed in section \ref{computations} to an explicit description of these different spaces for the group $\Geight$ and the different maps relating these spaces.  We use coordinates on a Zariski open set of our spaces which are associated to a given triangulation.  In particular, we describe 
a Zariski open set (called the deformation variety) of the set of decorated representations into $\PGL(3,\bC)$ given by coordinates we introduced in \cite{BFG}.
The main theorem is  Theorem \ref{3components}: 
Given the standard triangulation of the figure eight knot  complement, there exits precisely three irreducible components of the
 deformation variety.  Each component is smooth of dimension two. Whereas this result is stated and proved only for the deformation variety, we strongly believe this is also the case for the whole character variety. A precise statement and proof should appear elsewhere.
This section begins with a reminder about Groebner basis and saturation, then a presentation of the actual equations for the figure eight knot complement in \S \ref{ss:equations}. We then proceed with a general presentation of our method to achieve computations. Eventually, we give precisions of the specific case of the figure eight knot complement.
The three components are finally described in subsection \ref{results}.  It turns out that each representation can be lifted to an $\SL(3,\bC)$ representation. Once these components are identified, we may check the properties stated in the theorem (irreducibility, smoothness...).

The next section \ref{s:A-var} is devoted to some more precise understanding of these components: description the $A$-variety associated to this knot (it is a natural analog of the A-polynomial), identification of the boundary unipotent representation and identification of the space of representations in $\PGL(2,\bC)$.

Finally, in section \ref{deformation}, we describe a deformation method to obtain a parametrization of some generators of $\Geight$ on each irreducible components.
This method allows one to obtain a particular irreducible component
of the representation variety containing a given representation.  It is based on a Newton method and LLL algorithm and was successfully used in other contexts
\cite{CLTa,CLTb}. We applied it to the boundary unipotent representations
of the fundamental group of the figure eight knot complement. A great interest of this method is that its output is indeed a parametrization of matrices. It opens the path to a geometric study of those representations, see e.g. \cite{DF}.
However it does not belong to its scope to determine all the irreducible components. We insist on the fact that it is the conjunction of both methods that gives a satisfactory result: a parametrization of each component.


We thank Nicolas Bergeron, Martin Deraux,  Matthias Goerner, Julien March\'e, Pierre Will, Maxime Wolff and Christian Zickert for many discussions and exchanges during this project.
The authors are grateful to the ANR 'Structures G\'eom\'etriques Triangul\'ees' which has financed this project during  the last two years.
