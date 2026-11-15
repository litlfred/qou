---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-005-14-deformation-variety
section_title: "Deformation variety"
section_number: 1.4
pages: 6-8
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.946
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
\label{ss:deformationvariety}

Thurston \cite{Thurston} defined coordinates on 
$$\DecX(\Gamma,\PGL(2,\bC))
$$ by defining the \emph{deformation variety} with the \emph{gluing equations}. We use in this paper an analog og this space for the group $\PGL(3,\bC)$. From now on, we will always assume that $n=3$. This space is defined by further assuming that $M$ is ideally triangulated: $M$ is homeomorphic to a gluing of tetrahedra with vertices removed as in \cite{Thurston, BFGKR}
So let $\mathcal T=(T_1,T_2,\ldots,T_\nu)$ be an ideal triangulation of $M$.

We now recall coordinates on these spaces as defined in \cite{BFG} (see Figure \ref{coordinates}).  For each of these (oriented) tetrahedra, one consider a set of $16$ coordinates: one on each half-edge and one in the center of this face. If the vertices of the tetrahedron $T$ are $(ijkl)$, one has twelve coordinates on half edges, denoted by $z_{ij}(T)$, $z_{ik}(T)$... and four on faces, denoted by $z_{ijk}(T)$.

\begin{figure}

\caption{Coordinates for a tetrahedron of flags}\label{coordinates}
\end{figure}

 As described in \cite{BFG}, these coordinates are subject to two different kinds of consistency relations: 
\begin{itemize}
 \item Internal relations: for a tetrahedron $T=(ijkl)$ we have around each vertex $z_{ij}(T)z_{ik}(T)z_{il}(T)=-1$ and $z_{ik}(T)=\frac{1}{1-z_{ij}(T)}$; and for each face $z_{ijk}(T)=-z_{il}(T)z_{kl}(T)z_{jl}(T)$.  
 \item Gluing relations: first, given two adjacent tetrahedra $T_{\mu}$, $T_{\mu'}$
of $T$ with a common face  
$(ijk)$ then 
\begin{equation} \label{face}
z_{ijk} (T_{\mu}) z_{ikj} (T_{\mu'}) = 1.
\end{equation}
second given a sequence $T_1, \ldots , T_{\mu}$ of tetrahedra sharing a
common edge $ij$ and such that $ij$ is an inner edge of the sub-complex composed by $T_1\cup \cdots \cup T_{\mu}$ 
then 
\begin{equation} \label{edge}
z_{ij} (T_1) \cdots z_{ij} (T_{\mu}) = z_{ji} (T_1) \cdots z_{ji} (T_{\mu}) = 1.
\end{equation}
 \end{itemize}
 
Given $M$ and a triangulation $\mathcal{T}$ with $n$ tetrahedra, we consider the space of solutions of these equations and denote it by 
$$
\mathrm{Defor}(M,\mathcal{T})\subset \bC^{16n}.
$$
We call it the {\it deformation variety} of a triangulation. 

Up to combinatoric choices, the holonomy map associates to each point in $\mathrm{Defor}(M,\mathcal T)$ a decorated representation into $\PGL(3,\bC)$ as in \cite[section 5]{BFG}: 
$$
\mathrm{Defor}(M,\mathcal{T})\rightarrow \mathrm{DecHom}(\pi_1(M),\PGL(3,\bC)).
$$
Moreover this map is algebraic\footnote{indeed, by construction, the expression of the matrix entries are algebraic.} and a different initial choice gives a conjugated decorated representation.  

So this gives two well defined maps, landing in $\DecMon$ or $\DecX$, both called holonomy maps and denoted by $\Hol$. Note that the second one is algebraic: 
$$
\Hol\: : \:\mathrm{Defor}(M,\mathcal{T})\rightarrow \DecMon(\pi_1(M),\PGL(3,\bC)),
$$
and
$$
\Hol\: : \:\mathrm{Defor}(M,\mathcal{T})\rightarrow \DecX(\pi_1(M),\PGL(3,\bC)),
$$
We extend the peripheral holonomy map defined in the previous section in a natural way:
\[
\Hol_\periph\: : \:\mathrm{Defor}(M,\mathcal{T})\rightarrow\DecX(\pi_1(T),\PGL(3,\bC))\simeq(\bC^*)^4
\]

Let us comment a bit on the properties of both the holonomy maps $\Hol$: the first map is injective but not surjective, as some representation are not detected by a given triangulation. Moreover, if you forget the decoration, the maps are not any more injective : there is a (generically) finite choice for a decoration of a given representation.  All this can be seen already in the case of representations
into $\PGL(2,\bC)$. In particular the identity representation can be obtained by gluing two tetrahedra to obtain the 
sphere $S^3$ minus  four points and the solutions to the hyperbolic equations has a curve such that the associated representations are 
trivial \cite{SegTill}.  Also, in the tables obtained in \cite{BFGKR} the 1-dimensional components give conjugated representations with  finite group image into $\PGL(3,\bC)$.
Examples where a given triangulation is not enough to describe all representation are given in \cite{SegTill} already in the case of
representations into $\PGL(2,\bC)$.

On the other hand, the situation is good on some components. First, recall that, as $M$ has been assumed to be hyperbolic, there is the monodromy $[\rho_{\mathrm{geom}}]\in\Mon(\Gamma,\PGL(2,\bC))$ of the unique oriented complete hyperbolic structure on $M$. We call it the \emph{geometric representation}. Moreover, the irreducible representation $\PGL(2,\bC)\to\PGL(n,\bC)$ gives a map $\Mon(\Gamma,\PGL(2,\bC))\to\Mon(\Gamma,\PGL(n,\bC))$. We still call the image of $[\rho_{\mathrm{geom}}]$ the \emph{geometric representation}, still denoted by $[\rho_{\mathrm{geom}}]\in\Mon(\Gamma,\PGL(n,\bC))$. One can then state the following theorem for $\PGL(2,\bC)$ see \cite{Thurston,SegTill}, with a mild assumption on the triangulation that we will not define here and that is verified for the triangulation of the figure eight knot complement we will use:

\begin{theorem} Let M be an orientable, connected, cusped hyperbolic manifold.  Let $\mathcal{T}$
be an ideal triangulation of M such that all edges are essential.  Then there exists $z_{\mathrm{geom}}\in \mathrm{Defor}(M,\mathcal{T})$
such that $\Hol(z_{\mathrm{geom}})$ is the geometric representation.  

Moreover the whole  component of $X(\Gamma,\PGL(2,\bC))$ containing the (image of) the geometric representation is in the image  of the holonomy map $\Hol$.
\end{theorem}

The analogous theorem in the case of $\PGL(3,\bC)$ is believed to be true:  
Let $M$ be an orientable, connected, cusped hyperbolic manifold.  Let $\mathcal{T}$
be an ideal triangulation of $M$ such that all edges are essential.  Then there exists $z_{\mathrm{geom}}\in \mathrm{Defor}(M,\mathcal{T})$
such that $\Hol(z_{\mathrm{geom}})$ is the geometric representation. We believe that the image of $\Hol$ contains the whole  component of $X(\Gamma,\PGL(3,\bC))$ containing the geometric representation.


We also know that $z_{\mathrm{geom}}\in \mathrm{Defor}(M,\mathcal{T})$ is a smooth point (see \cite{BFGKR}).
