---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-006-25-changing-the-triangulation
section_title: "Changing the triangulation"
section_number: 2.5
pages: 19-20
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 1.0
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:geom23 label="sec:geom23"}

We have explained, in principle, how to construct 3-manifolds $M$, phase spaces $\mathcal{P}_{\partial M}$, and Lagrangians $\mathcal{L}_M$ by gluing together ideal tetrahedra $\Delta_i$. It would be useful to verify that such constructions do not depend on a precise choice of triangulation $\{\Delta_i\}$. Geometrically, once we fix the triangulation of geodesic boundaries, any two triangulations of $M$ are related by a sequence of "2--3 Pachner moves," *cf.* [@Matveev-book]. These replace two tetrahedra glued along a common face with three tetrahedra glued along three faces and a common edge, and vice versa, as shown in Figure [1](#fig:Pach){reference-type="ref" reference="fig:Pach"}.

![The 2--3 Pachner move](Pach){#fig:Pach width="5in"}

Invariance of phase spaces and Lagrangians under the 2--3 move was verified

[^1]

in detail in (*e.g.*) [@Dimofte-QRS], guaranteeing the internal consistency of our present gluing constructions. For example, for phase spaces, the essence of the argument is that the product phase spaces corresponding to the bipyramid on the left of Figure [1](#fig:Pach){reference-type="ref" reference="fig:Pach"} is the symplectic reduction of the product phase space on the right,

$$\hspace{-.5in}\mathcal{P}_{\partial(\text{bipyramid})}\;\; =\qquad \mathcal{P}_{\Delta_R}\times \mathcal{P}_{\Delta_S} \;=\; \big(\mathcal{P}_{\Delta_Z}\times \mathcal{P}_{\Delta_W}\times \mathcal{P}_{\Delta_Y}\big)\big/\!\!\big/(C=2\pi i)\,, \label{bip23}$$

where $C$ is the gluing constraint coming from the internal edge. In fact, we already described the right-hand side of [\[bip23\]](#bip23){reference-type="eqref" reference="bip23"} in Section [\[sec:geobdy\]](#sec:geobdy){reference-type="ref" reference="sec:geobdy"}. The left-hand side is even easier to analyze. In the same two polarizations $\Pi_{\rm eq}$ and $\Pi_{\rm long}$ of Figure [\[fig:bippol\]](#fig:bippol){reference-type="ref" reference="fig:bippol"}, we now find coordinates for $\mathcal{P}_{\Delta_R}\times\mathcal{P}_{\Delta_S}$:

$$\label{bipcoord2}
\begin{array}{lc@{\;\;}c@{\qquad}c}
  && \text{positions} & \text{momenta} \\[.1cm]
  \Pi_{\rm eq} &:\;& X_1 = R+S''\,,\quad X_2=R''+S & P_1 = R''\,,\quad P_2 = S''\\[.1cm]
  \Pi_{\rm long} &:\;& X_1'=R\,,\quad X_2' =S & P_1' =R''\,,\quad P_2' = S''
\end{array}$$

The two equivalent descriptions [\[bipcoord3\]](#bipcoord3){reference-type="eqref" reference="bipcoord3"}--[\[bipcoord2\]](#bipcoord2){reference-type="eqref" reference="bipcoord2"} of $\mathcal{P}_{\partial(\text{bipyramid})}$ are related by combining or splitting the coordinates associated to the external dihedral angles, for example splitting $Z\leftrightarrow R''+S''$.

The 2--3 Pachner moves always preserve the triangulations of geodesic boundaries of $M$. In contrast, they do not preserve the "small" triangulations of cusp boundaries; but the triangulations of cusp boundaries are never important for defining phase spaces here, or 3d gauge theories later on.

If we want to change the triangulation of a geodesic boundary $\mathcal{C}\subset\partial M$, we must consider another type of fundamental move: a flip. The flip acts by gluing an additional tetrahedron $\Delta_F$ onto a quadrilateral in $\mathcal{C}$, as in Figure [\[fig:flip\]](#fig:flip){reference-type="ref" reference="fig:flip"}, and effectively "flipping" the diagonal of this quadrilateral. In the process of attaching $\Delta_F$, a new internal edge $I_F$ is created, which imposes a new gluing constraint $C_{I_F}$. The flipped phase space $\mathcal{P}_{\mathcal{C}'}$ is therefore related to $\mathcal{P}_\mathcal{C}$ by a symplectic reduction

$$\mathcal{P}_{\mathcal{C}'} = \big(\mathcal{P}_\mathcal{C}\times \mathcal{P}_{\partial\Delta_F}\big)\big/\!\!\big/(C_{I_F}=2\pi i)\,.$$

Obviously $\mathcal{P}_{\mathcal{C}'}$ and $\mathcal{P}_{\mathcal{C}}$ must be isomorphic, but the two have different "natural" polarizations.

To illustrate this explicitly, if we start with a polarized phase space $\mathcal{P}_\mathcal{C}$ in which one of the canonical position--momentum pairs $(X,P)$ corresponds to dihedral angles as in Figure [\[fig:flip\]](#fig:flip){reference-type="ref" reference="fig:flip"}, then gluing on the tetrahedron $\Delta_F$ yields an internal edge constraint

$$C_{I_F}  = X + Z \;\to\, 2\pi i\,. \label{Cflip}$$

Now, let us attach a new position coordinate $X'$ to the newly flipped diagonal, and its conjugate momentum $P'$ to the same edge as $P$. After the symplectic reduction (in particular, imposing [\[Cflip\]](#Cflip){reference-type="eqref" reference="Cflip"}), we find that

$$X' = 2\pi i - X\,,\qquad P' = -(P+Z')\,.$$

If we also keep track of Lagrangians, we would find that the flipped $\mathcal{L}_{M'}$ is related to $\mathcal{L}_M$ by substituting $x\to x'^{-1},\; p\to p'^{-1}(1-x')$ in the defining equations for $\mathcal{L}_M$.

[^2]

The flip transformation, described here from a 3-dimensional viewpoint, is very familiar in 2-dimensional Teichmüller (and quantum Teichmüller) theory, *cf.* [@Penner-decorated; @Fock-Teich; @FockChekhov; @Kash-Teich; @FG-Teich]. This should not be surprising, given the above observation that shear coordinates of Teichmüller theory should be identified with 3d dihedral angles.

[^1]: Again we note that the invariance of Lagrangians comes with a few subtle caveats, as discussed in [@Champ-hypA; @Dunfield-Mahler] and reviewed in Sections 4--5 of [@Dimofte-QRS]. For sufficiently generic triangulations, these caveats can be safely ignored.

[^2]: We suggest the verification of this statement as an exercise for the reader.
