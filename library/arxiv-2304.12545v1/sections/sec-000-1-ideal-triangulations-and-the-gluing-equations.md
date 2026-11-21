---
doc_id: arxiv-2304.12545v1
doc_title: "HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF WALTER NEUMANN"
section_id: sec-000-1-ideal-triangulations-and-the-gluing-equations
section_title: "Ideal triangulations and the gluing equations"
section_number: 1
pages: 1-3
source_pdf: 2304.12545v1.pdf
source_sha256: bfc3c2be395b1b2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.881
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
---
\label{sec.2}

The starting point of the paper~\cite{NZ} was Thurston's amazing insight in the 1980's
that all 
3-dimensional manifolds should be canonically divisible into pieces having a well-defined 
geometric structure of one of 8 types, the most important of which is the hyperbolic one. 
In conjunction with the famous Mostow ridigity theorem, this means that 3-dimensional
topology becomes a part, first of differential geometry, and then of algebraic number
theory, something that is not at all the case in other dimensions.  The main class is
that of oriented hyperbolic 3-manifolds, which have a riemannian metric with constant
negative curvature that can be normalized to~$-1$ and hence are locally isometric to
hyperbolic 3-space~$\BH^3$.  Of particular interest is the
{\it volume spectrum}, the set of volumes of all complete hyperbolic 3-manifolds of finite
volume (in which case they are either compact or the union of a compact part and a finite
number of ``cusps'' diffeomorphic to the product of a half-line and a torus).  These
volumes have both striking number-theoretical properties (they belong to the image under
the regulator map of the Bloch group, as discussed in Section~\ref{sec.4}) and striking
metric properties (they form a countable well-ordered subset of~$\R_{>0}$, as discussed in
Section~\ref{sec.3}), and the primary goal of the paper~\cite{NZ} was to understand them
as thoroughly as possible.

In this section we discuss ideal triangulations and their NZ-equations in some detail. 
Ideal triangulations of 3-manifolds with torus boundary components were introduced by
Thurston~\cite{Thurston} as a convenient way to describe and effectively
compute~\cite{snappy} complete hyperbolic structures on 3-manifolds.
Recall that in hyperbolic geometry an {\it ideal tetrahedron} is the convex
hull of four points in the boundary $\partial (\BH^3)\cong\BP^1(\BC)$ of 3-dimensional
hyperbolic space $\BH^3$.  The (orientation preserving) isometry group of~$\BH^3$ is the
group~$\PSL_2(\BC)$, 
acting on the boundary by fractional linear transformations of~$\BP^1(\BC)$, and since under 
this group any four distinct points can be put in standard position~$(0,1,\infty,z)$ for some 
$z\in\BC\ssm\{0,1\}$ (the cross-ratio of the four points), any (oriented) ideal tetrahedron is 
the convex hull $\D(z)$ for some complex number~$z~\in \BC\ssm\{0,1\}$, called the
{\it shape parameter} 
of the tetrahedron. This number is not quite unique because of the choice of which three
vertices
we send to 0, 1 and~$\infty$, meaning that the oriented tetrahedra $\D(z)$, $\D(z')$ and
$\D(z'')$,
where $z'=1/(1-z)$ and $z''=1-1/z$, are isometric. In this way one attaches a shape parameter 
$z$, $z'$ or $z''$ to each pair of opposite edges of a given oriented ideal tetrahedron.
Note that the shape of a tetrahedron is an arbitrary complex number not equal to 0 or 1,
and whether it has positive, zero or negative imaginary part is irrelevant to our discussion.

When $\calT$ is an ideal triangulation of a hyperbolic 3-manifold $M$ with $N$ tetrahedra
with shape parameters $z_1,\dots,z_N$, then we get one polynomial equation
(``gluing equation'') 
for each edge.  Specifically, the shape parameters at that edge of all tetrahedra that are
incident with it must clearly have arguments that add up to~$2\pi$ (because otherwise the 
metric would not be smooth along that edge), but in fact the shape parameters themselves
have product~$+1$ by an easy argument.  Since each of the possible shape parameters 
$z,\,z',\,z''$ of~$\D(z)$ belongs to the multiplicative
group~$\big\langle z,1-z,-1\big\rangle$, this equation for each edge~$e_i$  has the form 
\be
\label{edge}
\pm\prod_{j=1}^N z_j^{R'_{ij}} (1-z_j)^{R''_{ij}} = 1\,.
\ee

Since it is easily seen that the number of edges in the triangulation is the same as 
the number~$N$ of simplices, this gives us $N$ polynomial equations among the $N$ complex
numbers $z_1,\dots,z_N$.  The obvious thought is that this leads to a 0-dimensional 
moduli space and explains the rigidity, but this is wrong since rigidity only applies 
to complete hyperbolic structures, and in fact the $N$ edge relations are never
multiplicatively
independent. An obvious example is that their product is always~1, and this is the
only dependence if the boundary of the 3-manifold is a torus (often called a cusp),
but in general there are $h$ multiplicatively independent relations among the $N$
equations~\eqref{edge}, where $h$ is the number of cusps of the 3-manifold (assuming that
all boundary components are tori). Thus the true expected 
dimension of the moduli space of hyperbolic structures is in fact~$h$.  That the 
dimension really is~$h$ is an important theorem of Thurston (\S5 of~\cite{Thurston}) and 
was given a new and simpler proof in~\cite{NZ} using the algebraic structure of the 
gluing equations.

The 0-dimensional moduli space (rigidity) arises when we require the hyperbolic structure
given by the shape parameters $z_i$ to be complete, because this entails two further
independent relations at each cusp.  Specifically, each ``peripheral curve'' (meaning an 
isotopy class of curves on the torus cross-section of one of the cusps) gives a relation,  
so if one chooses a meridian and a longitude $(\mu_i,\lambda_i)$ at each cusp 
$i=1,\dots,h$, one obtains $2h$ further equations
\be \label{ML}
\pm\prod_{j=1}^N z_j^{M'_{ij}} (1-z_j)^{M''_{ij}} \= 1, \qquad
\pm\prod_{j=1}^N z_j^{L'_{ij}} (1-z_j)^{L''_{ij}} \= 1, \qquad (i=1,\dots,h) \,.  
\ee
Thus the full set of gluing equations is described by an $(N+2h) \times 2N$ matrix 
$U=\Bigl(\!\begin{smallmatrix} R'&R''\\M'&M''\\L'&L''\end{smallmatrix}\!\Bigr)$. 


It was shown in~\cite{NZ} that the matrix~$U$ has some key symplectic properties, of which
the most important (Theorem~2.2) says that
\be\label{Th2.2} 
U J_{2N}U^t \= 

\begin{pmatrix} 0_{N,N}& 0_{2h,N} \\ \phantom2 0_{N,2h}  & 2 J_{2h} \end{pmatrix}\,,
\ee
where $J_{2n}:=\bigl(\!\begin{smallmatrix} 0&-1_n\\1_n&0\end{smallmatrix}\!\bigr)$, while
the others say that the $N\times2N$ matrix $R=\bigl(R'\,R''\bigr)$ has rank $N-h$,
the full matrix~$U$
has rank $N+h$, and that the space $[U]\subset\R^{2N}$ spanned by the rows of~$U$ is the 
orthogonal complement of~$[R]$ with respect to the symplectic structure~$J_{2N}$ (Prop.~2.3).
The rank statement was then used to prove that the dimension of the above-mentioned
deformation space of (non-complete) hyperbolic structures is at least~$h$, and then a
further argument using Mostow rigidity showed that it is exactly~$h$.  This gives rise in
the 1-cusp case to a polynomial $P(m,\ell)=0$, where $m^2$ and $\ell^2$ denote the
left-hand sides of the two equations~\eqref{ML} and $P$ is a certain polynomial (a factor
of what is now called the $A$-polynomial) that was calculated explicitly in~\cite{NZ} for 
the simplest hyperbolic knot~$4_1$ (figure~8).  In the general case the deformation space
is a component of the ``character variety'' as introduced and studied in~\cite{CCGLS} and
studied later by Walter and his students Abhijit Champanerkar~\cite{Champanerkar} and
Stefan Tillmann~\cite{Tillmann:bs}.

To get a complete manifold with $h$ cusps, we impose $h$ further gluing conditions, namely the
equations~\eqref{edge} and the first of each of the equations~\eqref{ML}. (But in fact these
$h$ meridian equations together with the edge equations imply the longitude equations, so in
the end all relations~\eqref{edge} and~\eqref{ML} hold.)  Now rigidity applies and there are 
no deformations.  But there is another process, with a lot more freedom, to obtain rigid
complete hyperbolic structures from the original cusped manifold, namely to do a Dehn 
surgery at some or all of the cusps.  Specifically, when we do a $(p,q)$-surgery at a
cusp (meaning that we truncate the \hbox{3-manifold} at the torus boundary and glue on a solid
torus in such a way as to kill the homotopy class of $p$ times a chosen meridian times $q$
times a chosen longitude), then we impose the gluing equation $m^{2p}\ell^{2q}=1$, where
$m^2$ and $\ell^2$ as above are the left-hand sides of one of the pairs of
equations~\eqref{ML}.  In the next section, still following~\cite{NZ}, we discuss how the
volumes behave under this process.
