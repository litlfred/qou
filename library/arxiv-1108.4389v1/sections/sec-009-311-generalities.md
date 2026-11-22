---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-009-311-generalities
section_title: "Generalities"
section_number: 3.1.1
pages: 21-23
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
There is a beautiful $SL(2,{\mathbb Z})$ action on the space of 3-dimensional conformal field theories with $U(1)$ flavor symmetry. This action was first described in [@Witten-SL2] as a way to understand the meaning of different choices of boundary conditions for an abelian gauge field in $AdS_4$ in the context of $AdS_4/CFT_3$.

To be precise, $SL(2,{\mathbb Z})$ acts on the space of 3d theories equipped with a specific way to couple a $U(1)$ flavor symmetry to a background $U(1)$ gauge field. The $SL(2,{\mathbb Z})$ action can be defined by specifying the action of its generators $S$ and $T$, which obey the relations

$$S^4 = (ST)^3 = id.$$

The generator $T$ does not change the underlying 3d CFT. It only modifies the prescription of how to couple the theory to the background gauge field $A$, by adding to the conserved current for the background flavor symmetry the Hodge dual field strength $*F=*dA$. In terms of a Lagrangian, this is simply accomplished by adding a background Chern-Simons interaction at level $k=1$,

$$T\,:\quad \mathcal{L}\to \mathcal{L}+ \frac{1}{4\pi} A\wedge dA\,.$$

In contrast, the $S$ generator changes the structure of the 3d theory by making the background gauge field $A$ dynamical.

[^1]

The new 3d theory is then prescribed a coupling to a new background $U(1)$ gauge field $A_{\rm new}$: the new flavor current is the Hodge dual field strength $*F$ of the old, now dynamical, gauge field. Equivalently, one prescribes a Lagrangian coupling

$$S\,:\quad \mathcal{L}\to \mathcal{L}+ \frac{1}{2 \pi} A_{\mathrm{new}} \wedge dA \qquad\text{($A$ dynamical)}\,.$$

It is the monopole operators for $A$ that are charged under the new $U(1)$ flavor symmetry; thus this $U(1)$ is sometimes called "topological." From the definitions of $S$ and $T$, one can prove that the relations $S^2=C$ and $(ST)^3=id.$ hold, where the transformation $C$ (charge conjugation) just inverts the sign of the background gauge field. We will generally denote the action of an $SL(2,{\mathbb Z})$ group element $g$ on a theory $\mathcal{T}$ as $g \circ \mathcal{T}$.

There is a useful alternative interpretation of this $SL(2,{\mathbb Z})$ action: it is the action of electric-magnetic duality on the space of conformally invariant boundary conditions for a free abelian four-dimensional gauge theory. Indeed, given a three-dimensional CFT with a prescribed coupling to a background gauge field, we can build a boundary condition by coupling the CFT to the value of the 4d gauge field at the boundary. This gives a generalization of Neumann boundary conditions: the normal component of the 4d field strength at the boundary becomes proportional to the conserved current of the 3d CFT. If we denote the 3d theory as $\mathcal{T}$, we can denote the resulting boundary condition as $\mathcal{B}[\mathcal{T}]$.

Next, we can do an electric-magnetic duality transformation $g \in SL(2,{\mathbb Z})$ in the four-dimensional bulk, and ask how the boundary condition $\mathcal{B}[\mathcal{T}]$ looks in the new duality frame. This "new" boundary condition $g \circ \mathcal{B}[\mathcal{T}]$ turns out to coincide with $\mathcal{B}[g \circ \mathcal{T}]$. This fact can be shown readily with the help of "duality domain walls" [@GW-Sduality]: the action of bulk dualities on boundary conditions can be interpreted as the collision (or OPE) of these domain walls with the boundary, as illustrated in Figure [1](#fig:boundarywall){reference-type="ref" reference="fig:boundarywall"}. For an abelian gauge theory the duality walls are very easy to construct from the definition of electric-magnetic duality. The collision with the boundary then reproduces the $SL(2,{\mathbb Z})$ action defined above.

![The action of duality domain walls on boundary conditions. A duality transformation $g \in Sp(2N,{\mathbb Z})$ maps a generalized Neumann boundary condition defined by coupling to a 3d theory $\mathcal{T}$ into a boundary condition associated with a boundary CFT $g \circ \mathcal{T}$.](boundarywalls){#fig:boundarywall width="4.5in"}

The $SL(2,{\mathbb Z})$ action on boundary conditions is a little bit more general than the $SL(2,{\mathbb Z})$ action on 3d theories with a coupling to a background gauge field. For example, there exists an extra $SL(2,{\mathbb Z})$ orbit of boundary conditions which includes the pure Dirichlet boundary condition on the 4d gauge field. This boundary condition is invariant under $T$, and it is sent to the pure Neumann boundary condition by $S$.

Now, it is rather obvious how to generalize this $SL(2,{\mathbb Z})$ action to an $Sp(2N,{\mathbb Z})$ action on boundary conditions for a general four-dimensional $U(1)^N$ abelian gauge theory, or to an action on 3d CFTs with $U(1)^N$ flavor symmetry: it is the action of the electric-magnetic duality group of the $U(1)^N$ four-dimensional gauge theory. Notice that in this case, there are several orbits of boundary conditions which involve at some point Dirichlet boundary conditions for some of the bulk gauge fields. These orbits will look a bit singular from the point of view of an action on 3d CFTs. Concretely, they signal situations where the flavor symmetry is spontaneously broken to a subgroup in the IR [@GW-Sduality].

To make this a little more explicit, suppose we are given a Lagrangian description of a 3d CFT with $U(1)^N$ global symmetry, whose current is coupled to $N$ background gauge fields $\vec A=(A_1,...,A_N)$. The generators of $Sp(2N,{\mathbb Z})$ fall into three basic categories: "$T$-type," "$S$-type," and "$GL$-type" (*cf.* [@HuaReiner]). Representing them as matrices in $N\times N$ blocks, we find Lagrangian transformations

$$\text{``$T$-type''}\quad g=\begin{pmatrix} I & 0 \\ B & I \end{pmatrix},\; \text{$B$ symmetric}\quad:\qquad \mathcal{L}[\vec{A}]\to\mathcal{L}[\vec{A}_{\rm new}]+\frac{1}{4\pi} \vec A_{\rm new} \cdot B\,d\vec{A}_{\rm new}\,; \label{SpT}$$

$$\text{``$S$-type''}\quad g= \begin{pmatrix}I-J & -J \\ J & I-J \end{pmatrix}\quad:\qquad \mathcal{L}[\vec A]\to\mathcal{L}[\vec A]+\frac{1}{2\pi} \vec{A}_{\rm new}\cdot J\,d\vec A\, \label{SpS}$$

(where $J={\rm diag}(j_1,...,j_N)$ with $j_i\in \{0,1\}$, and we have gauged every $A_i$ for which $j_i=1$, replacing its $U(1)$ with a new topological flavor symmetry); and

$$\text{``$GL$-type''}\quad g = \begin{pmatrix} U & 0 \\ 0 & U^{-1\,t}\end{pmatrix},\;U\in GL(N,{\mathbb Z})\quad:\qquad \mathcal{L}[\vec A]\to \mathcal{L}[U^{-1}\vec A_{\rm new}]\,. \label{SpGL}$$

The latter $GL$-type action simply redefines the flavor currents by an invertible, integral transformation.

[^1]: One can add a Yang-Mills kinetic term at intermediate stages in the calculation. But for $S$ to have the correct properties, one must flow to the IR at the end, and then $g_{{\rm YM}}\to \infty$ and this term is removed.
