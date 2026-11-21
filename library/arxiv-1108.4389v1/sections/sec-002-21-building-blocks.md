---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-002-21-building-blocks
section_title: "Building blocks"
section_number: 2.1
pages: 9-11
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.89
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
The fundamental building block used in building our 3-manifolds $M$ is an ideal hyperbolic tetrahedron (Figure [\[fig:tet\]](#fig:tet){reference-type="ref" reference="fig:tet"}). Geometrically, an ideal tetrahedron $\Delta$ has faces that are geodesic surfaces and vertices that lie right on the boundary of hyperbolic 3-space ${\mathbb H}^3$. As shown in Figure [\[fig:tet\]](#fig:tet){reference-type="ref" reference="fig:tet"}, hyperbolic 3-space can be viewed as the interior of a 3-ball, with the Riemann sphere as its boundary.

The full hyperbolic structure of $\Delta$ is determined by a single complex cross-ratio of the positions of its vertices on $\partial{\mathbb H}^3$. There are three different ways to write this one cross-ratio, encoded in three different *edge parameters* $(z,z',z'')$. Geometrically, the edge parameters are dihedral angles on pairs of opposite edges of the tetrahedron [@thurston-1980]. Explicitly,

$$z \,\equiv\, \exp(Z) \qquad\text{with}\qquad Z = \text{(torsion)}+i\,(\text{angle})\,,$$

and similarly for $z'=\exp(Z')$ and $z''=\exp(Z'')$, where "torsion" measures the twisting of the hyperbolic metric as one moves around an edge. As discussed in [@Dimofte-QRS], the edge parameters satisfy $zz'z''=-1$, which leads to the definition of the boundary phase space

$$\mathcal{P}_{\partial\Delta} \,=\, \big\{(z,z',z'')\in ({\mathbb C}^*\backslash\{1\})^3\;\big|\; zz'z''=-1\big\} \,\simeq\, ({\mathbb C}^*\backslash\{1\})^2\,,$$

or in a lifted, logarithmic form,

$$\mathcal{P}_{\partial\Delta} \,=\, \big\{(Z,Z',Z'') \in({\mathbb C}\backslash 2\pi i{\mathbb Z})\;\big|\; Z+Z'+Z''=i\pi \big\}\,. \label{PDelta}$$

This is an affine linear space, with symplectic form $\omega_{\partial\Delta} = \frac{1}{\hbar}dZ\wedge dZ'$ or, equivalently, a Poisson structure such that

$$\{Z,Z'\} = \{Z',Z''\} = \{Z'',Z\} = \hbar\,. \label{DPoisson}$$

The edge parameters also obey a second relation $z+z'^{-1}-1=0$, which defines the Lagrangian submanifold

$$\mathcal{L}_\Delta = \{ z+ z'^{-1}-1=0\} = \{e^Z+e^{-Z'}-1=0\}\quad \subset\;\mathcal{P}_{\partial\Delta}\,. \label{LDelta}$$

Any cyclic permutation of the Lagrangian equation (with $z\to z'\to z''\to z$) could also be used.

Topologically, it is convenient to truncate or regularize the four vertices of an ideal tetrahedron, as in Figure [\[fig:trunc\]](#fig:trunc){reference-type="ref" reference="fig:trunc"}. The tetrahedron then has four large, geodesic boundaries, whose induced metric is hyperbolic; and four small boundaries at the truncated vertices, whose induced metric is Euclidean. In fact, the condition $Z+Z'+Z''=i\pi$ that defines the phase space in [\[PDelta\]](#PDelta){reference-type="eqref" reference="PDelta"} simply says that the sum of angles in the small Euclidean triangles at the vertices is always $\pi$.

While the Lagrangian equation $z+z'^{-1}-1=0$ follows directly from the geometric definition of $(z,z',z'')$ as equivalent cross-ratios, it also has an intrinsic description in terms of $SL(2,{\mathbb C})$ connections. If we view the boundary $\partial\Delta$ of a tetrahedron as a four-punctured sphere, the phase space $\mathcal{P}_{\partial\Delta}$ is the set of flat $SL(2,{\mathbb C})$ connections with *unipotent* monodromy around the four punctures. The Lagrangian $\mathcal{L}_\Delta$ is then the subspace of flat connections with *trivial* monodromy --- in other words, the flat connections that can be extended from the boundary into the bulk of the tetrahedron. Understanding this description explicitly in coordinates $(z,z',z'')$ requires a bit of further background, which we defer to Section [\[sec:geobdy\]](#sec:geobdy){reference-type="ref" reference="sec:geobdy"}.

In order to define the gauge theory associated to a tetrahedron, we will need to choose a polarization $\Pi$ for its boundary phase space. This means choosing affine linear coordinates on $\mathcal{P}_{\partial\Delta}$ that are canonically conjugate to each other with respect to the Poisson structure above, with one coordinate thought of as "position" and the other as "momentum." There are three natural possibilities, which we call $\Pi_Z$, $\Pi_{Z'}$, and $\Pi_{Z''}$ ,

$$\begin{array}{lc@{\quad}c@{\qquad}c}  && \text{position $X$} & \text{conjugate momentum $P$} \\[.1cm]
 \Pi_Z &: & Z & 
 Z'' \\[.1cm]
 \Pi_{Z'} &: & Z' & 
 Z \\[.1cm]
 \Pi_{Z''} &: & Z'' & 
 Z'
 \end{array}
\label{tetpols}$$

Each of these polarizations can be encoded in a choice of opposite edges on the tetrahedron, such that the edge parameters of the distinguished edges act as "positions" (Figure [1](#fig:tetpol){reference-type="ref" reference="fig:tetpol"}).

![Natural polarizations for a tetrahedron, with the thickened pairs of opposite edges corresponding to the "position" coordinate.](tetpol){#fig:tetpol width="4.8in"}

We can define a larger class of polarizations by starting with any of those in [\[tetpols\]](#tetpols){reference-type="eqref" reference="tetpols"}, and acting with an affine symplectic transformation $Sp(2,{\mathbb Z})\ltimes (i\pi{\mathbb Z})^2$. By this we mean taking the vector $\big(\text{position},\,\text{momentum}\big)$, multiplying by $Sp(2,{\mathbb Z})\simeq SL(2,{\mathbb Z})$ matrices, and shifting both position and momentum by integer multiples of $i\pi$. For example, instead of $\Pi_Z$, we could have considered polarization $\Pi^-_Z$ in which $X^-=Z$ is position and $P^-=-Z'$ is momentum; then the transformation from $\Pi_Z$ to $\Pi^-_Z$ is

$$\hspace{-.2in} \Pi_Z\;\to\;\Pi^-_Z\;:\qquad \begin{pmatrix} X^-\\P^- \end{pmatrix}= \begin{pmatrix}1 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} X\\P \end{pmatrix} + \begin{pmatrix} 0 \\ -i\pi \end{pmatrix}\,. \label{PiZm}$$

Similarly, to go from $\Pi_Z$ to $\Pi_{Z'}$, we transform

$$\begin{pmatrix} Z' \\ Z \end{pmatrix} = \begin{pmatrix} -1 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} Z \\ Z'' \end{pmatrix} + \begin{pmatrix}i\pi \\ 0\end{pmatrix}\,,$$

where the matrix involved is $ST = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0\end{smallmatrix}\right)\left(\begin{smallmatrix} 1&0\\1&1 \end{smallmatrix}\right)\in Sp(2,{\mathbb Z})$. The identity $(ST)^3=I$ corresponds to the fact that three cyclic permutations of shape parameters brings us back where we started.
