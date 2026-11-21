---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-018-45-the-octahedron
section_title: "The octahedron"
section_number: 4.5
pages: 37-39
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.995
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:oct label="sec:oct"}

We include two more brief examples of three-manifold theories. The first, the octahedron, demonstrates how $2-3$ moves can be used in the interior of a manifold, resulting in interesting chains of $\mathcal{N}=2$ SCFT dualities. The second, the figure-eight knot complement, will illustrate how potential difficulties with "hard" edges can be resolved.

![The octahedron from four tetrahedra](oct4){#fig:oct4 width="3.5in"}

The simplest way to construct an octahedron is from four tetrahedra, glued together along a central edge (Figure [1](#fig:oct4){reference-type="ref" reference="fig:oct4"}). Suppose we we work in an equatorial polarization $\Pi_{\rm eq}$ as shown, with independent positions $(X,Y,Z,C)$, where the internal edge has parameter $C=X+Y+Z+W$. The resulting theory $T_{{\rm oct},\Pi_{\rm eq}}$ is a simple generalization of the bipyramid theory [\[XYZbip\]](#XYZbip){reference-type="eqref" reference="XYZbip"}. It starts with four chirals $\phi_X,\phi_Y,\phi_Z,\phi_W$ and four background gauge multiplets $V_X, V_Y, V_Z, V_W$. The multiplet $V_W$ is redefined as $V_W \to V_C-V_X-V_Y-V_Z-V_W$, and then we add a quartic superpotential

$$\mathcal{W}_{\rm eq} = \phi_X\phi_Y\phi_Z\phi_W$$

to break the global symmetry $U(1)_C$. We are still left with $U(1)_X\times U(1)_Y\times U(1)_Z$.

To be more specific, we should fix conjugate momenta in $\Pi_{\rm eq}$, taking (say) $(X+W'',Y+W'',Z+W'',-W'')$. This choice of momenta will add some background Chern-Simons couplings to the Lagrangian of $T_{{\rm oct},\Pi_{\rm eq}}$, which we encourage the careful reader to work out.

Now, if we change to a different polarization $\Pi_\times$, as in the center of Figure [2](#fig:oct5){reference-type="ref" reference="fig:oct5"}, we must perform an $Sp(6,{\mathbb Z})$ transformation on the theory $T_{{\rm oct},\Pi_{\rm eq}}$. This transformation, call it $g_\times$, gauges the $U(1)$ symmetry under which $(\phi_X,\phi_Y)$ transform as a hypermultiplet. Thus, we obtain a new theory $T_{{\rm oct},\Pi_\times} = g_\times\circ T_{{\rm oct},\Pi_{\rm eq}}$ which has a subsector that looks like $N_f=1$ SQED. By the basic $\mathcal{N}=2$ mirror symmetry (acting on this subsector), if must be equivalent to a theory of five chirals, with no dynamical gauge group, and superpotential

$$\mathcal{W}_\times = \phi_T\phi_Z\phi_W + \phi_T\phi_{ R}\phi_{ S}\,. \label{Woct5}$$

From the perspective of SQED, $\phi_T \equiv \phi_X\phi_Y$ is a meson, and the new fields $\phi_{R},\,\phi_S$ are monopole operators; the second term in [\[Woct5\]](#Woct5){reference-type="eqref" reference="Woct5"} is just the "XYZ" superpotential that we must add during mirror symmetry.

![The octahedron from five tetrahedra, two ways. Positions of the polarization $\Pi_\times$ are indicated in the middle.](oct5){#fig:oct5 width="5.5in"}

By looking at the left-hand side of Figure [2](#fig:oct5){reference-type="ref" reference="fig:oct5"}, we should immediately identify the description of $T_{{\rm oct},\Pi_\times}$ using five chirals as arising from a five-tetrahedron triangulation of the octahedron. The two terms in the superpotential $\mathcal{W}_\times$ come directly from the two internal edge coordinates $C_1 = T+Z+W$ and $C_2 = T+R+S$ in this triangulation.

To go a bit further, we notice that there another possible triangulation into five tetrahedra, shown on the right side of Figure [2](#fig:oct5){reference-type="ref" reference="fig:oct5"}. In a sense, it is maximally incompatible with the polarization $\Pi_\times$. If we try to use triangulation to define $T_{{\rm oct},\Pi_\times}$, we will again start with five chirals $\phi_{\tilde R},\phi_{\tilde S},\phi_{\tilde T},\phi_{\tilde Z},\phi_{\tilde W},$ but will have to gauge the two $U(1)$ symmetries which treat the respective pairs $\phi_{\tilde R},\phi_{\tilde S}$ and $\phi_{\tilde Z},\phi_{\tilde W}$ as hypermultiplets. What results is a mirror description of $T_{{\rm oct},\Pi_\times}$ as a *dynamical* $U(1)^2$ gauge theory with two hypermultiplets and a neutral chiral $\phi_{\tilde T}$, coupled by a superpotential

$$\mathcal{W}_\times' = \phi_{\tilde T}\phi_{\tilde Z}\phi_{\tilde W} + \phi_{\tilde T}\phi_{\tilde R}\phi_{\tilde S}\,. \label{Woct5g}$$

It is not too hard to recognize that these two descriptions of $T_{{\rm oct},\Pi_\times}$ correspond to the case $N=2$, $r=0$, $k=1$ of the infinite family of mirror pairs [\[mirrorR\]](#mirrorR){reference-type="eqref" reference="mirrorR"}.

There are infinitely more splittings of the octahedron, all giving dual descriptions of $T_{{\rm oct},\Pi_\times}$ and its $Sp(6,{\mathbb Z})$ images. We could similarly analyze triangulations of larger polyhedra or more general 3-manifolds to generate a huge class of 3d $\mathcal{N}=2$ mirror symmetries. We expect, in particular, that the family of dual theories mentioned in [\[mirrorR\]](#mirrorR){reference-type="eqref" reference="mirrorR"} is realized as a (small!) subset of these.
