---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-010-41-definition
section_title: "Definition"
section_number: 4.1
pages: 30-36
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.99
---
[]{#sec:defTM label="sec:defTM"}

In order to implement the first step, we begin by defining a theory $T_{\Delta, \Pi_Z}$ that we associate to a single tetrahedron $\Delta$ in polarization $\Pi_Z$ (as in [\[tetpols\]](#tetpols){reference-type="eqref" reference="tetpols"}): $$\boxed{\phantom{\int}
T_{\Delta, \Pi_Z} = \mathcal{T}_1\,.
\phantom{\int}}
\label{TDelta}$$

Recall from Section [\[sec:MS\]](#sec:MS){reference-type="ref" reference="sec:MS"} that $\mathcal{T}_1$ is a theory of a single chiral multiplet coupled to a background $U(1)$ gauge field, with a level $-\frac12$ Chern-Simons term turned on. We will say from now on that the free chiral is associated to the edges of the tetrahedron $\Delta$ labelled by $Z$, and denote it as $\phi_Z$ or $\mathcal{O}_Z$. It is also useful to think of the twisted mass of $\mathcal{O}_Z$ as ${\rm Re}(Z)$, and its R-charge as ${\rm Im}(Z)/\pi$, where $Z$ is the classical edge/shape parameter of $\Delta$. We use this interpretation here as an intuitive aid to motivate our gluing construction; it will be made much more precise in Sections [\[sec:moduli\]](#sec:moduli){reference-type="ref" reference="sec:moduli"} and [\[sec:S3b\]](#sec:S3b){reference-type="ref" reference="sec:S3b"}.

We can extend the definition [\[TDelta\]](#TDelta){reference-type="eqref" reference="TDelta"} to any other polarization $\Pi$ obtained by an (affine) $SL(2,{\mathbb Z})$ transformation $g$ on $\Pi_Z$:

$$T_{\Delta, g \circ \Pi_Z} = g \circ \mathcal{T}_1 \label{TDeltaPi}$$

For example, in a polarization $\Pi_Z^-$ as in [\[PiZm\]](#PiZm){reference-type="eqref" reference="PiZm"}, we would find $T_{\Delta,\Pi_Z^-}=T\circ \mathcal{T}_1$ to be the theory of a free chiral coupled to a background $U(1)$ with Chern-Simons level $k=+\frac12$. This definition is consistent with the ${\mathbb Z}_3$ symmetry of the tetrahedron: the triality symmetry permutes three equivalent polarizations $\Pi_{Z}$, $\Pi_{Z'}$, $\Pi_{Z''}$ in [\[tetpols\]](#tetpols){reference-type="eqref" reference="tetpols"} which, on the $\mathcal{N}=2$ gauge theory side, correspond to the three duality frames [\[STonT1\]](#STonT1){reference-type="eqref" reference="STonT1"} of the theory $\mathcal{T}_1$ permuted by the $ST$ element of $SL(2,{\mathbb Z})$.

The second step is the definition of $T_{\{ \Delta_i\}, \tilde\Pi}$, the theory associated to the union of $N$ tetrahedra $\Delta_i$, in a generic polarization $\tilde\Pi$. We can always write $\tilde\Pi = g \circ \{ \Pi_i \}$ for some $g\in Sp(2N,{\mathbb Z})$, where $\{ \Pi_i \}$ is a polarization defined as a product of independent polarizations $\Pi_i$ of the individual tetrahedra. We choose each $\Pi_i$ to be either $\Pi_{Z_i}$, $\Pi_{Z'_i}$ or $\Pi_{Z''_i}$. Then we define $$\boxed{\phantom{\int}
M = \bigcup_{i=1}^N \Delta_i^{(\Pi)} \qquad \leadsto \qquad T_{ \{\Delta_i\} , \tilde\Pi} \; = \; g \circ \bigotimes_{i=1}^N T_{\Delta_i,\Pi_i}
\phantom{\int}}
\label{TMoutofTD}$$ where we regard the product of $N$ copies of $\mathcal{T}_1$ theories as a theory with a canonical coupling to a $U(1)^N$ background gauge field. We should think of each $U(1)$ as corresponding to an *independent* position coordinate in the polarization $\tilde \Pi$. This definition is independent of the choice of $\Pi_i\in \{\Pi_{Z_i},\Pi_{Z'_i},\Pi_{Z''_i}\}$ due to the the symmetry $ST \circ \mathcal{T}_1 = \mathcal{T}_1$.

In order to define the actual SCFT $T_{M,\Pi}$ associated to the 3-manifold $M$, we need to implement a field-theory version of the gluing constraints $C_I\to 2\pi i$ for each internal edge $I$ in the triangulation. The basic idea is to choose a polarization $\tilde\Pi = g\circ\{\Pi_i\}$ for the collection of tetrahedra such that

-   it is compatible with the final desired polarization $\Pi$ of the boundary $\mathcal{P}_{\partial M}$; and

-   all the internal edge coordinates $C_I$ are "positions" in $\tilde\Pi$.

If we are careful, we can then construct operators $\mathcal{O}_I$ in the theory $T_{\{\Delta_i\},\tilde\Pi}$, one for each internal edge. These operators will be charged under a subset of $U(1)$ flavor symmetries, also associated to the edges $C_I$ --- or rather to independent linear combinations of them. We can then define $T_{M,\Pi}$ by adding a superpotential to $T_{\{\Delta_i\},\tilde\Pi}$ of the form

$$\boxed{\phantom{\int}
\mathcal{W}\; = \; \sum_{{I \in \, \text{internal} \atop \text{edges of~} M}} \mathcal{O}_I\,.
\phantom{\int}}
\label{WforTM}$$

This superpotential breaks all the $U(1)$ symmetries under which the $\mathcal{O}_I$ are charged. It also sets the R-charge of each $\mathcal{O}_I$ equal to $2$. We will see later that this is precisely equivalent to setting $C_I=2\pi i$.

In addition to the internal edge operators $\mathcal{O}_I$, the theories $\mathcal{T}_{\{\Delta_i\},\tilde\Pi}$ and $\mathcal{T}_{M,\Pi}$ also have a set of operators $\mathcal{O}_E$ associated to the external edges that are "positions" in $\Pi \subset \tilde\Pi$. These operators are charged precisely under the $U(1)$ gauge symmetries that persist as symmetries of $T_{M,\Pi}$ --- one for each independent position in $\Pi$. Indeed, it is easy to see that the flavor group of $T_{M,\Pi}$ will contain exactly $\frac12\dim \mathcal{P}_{\partial M}$ $U(1)$'s. In summary, we have built a correspondence:

$$\begin{array}{c@{\quad}|@{\quad}c}
\text{geometry} & \text{gauge theory} \\\hline
\Delta,\,\Pi_Z & T_{\Delta,\Pi_Z}= \mathcal{T}_1 \\[.1cm]
\{\Delta_i\},\, \{\Pi_i\} & T_{\{\Delta_i\},\{\Pi_i\}}=\otimes_i T_{\Delta_i,\Pi_i} \\[.1cm]
\text{positions, \emph{e.g.}\ $Z_i$} & \text{operators $\mathcal{O}_{Z_i}$ with $U(1)$ symmetries} \\[.1cm]
\{\Pi_i\} \to \tilde\Pi=g\circ \{\Pi_i\} & T_{\{\Delta_i\},\{\Pi_i\}}\to \mathcal{T}_{\{\Delta_i\},\tilde\Pi}=  g\circ T_{\{\Delta_i\},\{\Pi_i\}} \\[.1cm]
\text{internal edges}\;C_I & \text{operators}\; \mathcal{O}_I \\[.1cm]
\text{external positions, \emph{e.g.}\ $X_E$} & \text{operators $\mathcal{O}_E$} \\[.1cm]
C_I \to 2\pi i \;\text{(symp$^\text{c}$ reduction)} & \mathcal{W}= \sum_I \mathcal{O}_I \\[.1cm]
M = \cup_i\Delta_i,\;\;\Pi  & T_{M,\Pi} = \mathcal{T}_{\{\Delta_i\},\tilde\Pi}\;\text{+ superpotential $\mathcal{W}$}
\end{array}$$

The construction of operators $\mathcal{O}_I$ (and also $\mathcal{O}_E$) in the product theory $\mathcal{T}_{\{\Delta_i\},\tilde\Pi}$ is a little tricky. In order to describe it, we must distinguish two classes of edges. We call an edge "easy" if its classical coordinate $C_I$ (or $X_E$) is a sum containing at most one of the edge parameters $Z_i,\,Z_i',\,Z_i''$ for any tetrahedron $\Delta_i$; otherwise the edge is "hard." Thus, $C_I = Z_1+Z_2$ or $C_I=2Z_1''+Z_3+Z_4'$ would be examples of easy edges, while the internal edges [\[C41\]](#C41){reference-type="eqref" reference="C41"} in the standard triangulation of the figure-eight knot complement are hard.

Suppose that a triangulation $M=\{\Delta_i\}_{i=1}^N$ only contains easy edges, and let us focus on the internal ones $C_I$. For every edge $I$, we can define a polarization $\{\Pi_i^I\}$ so that the tetrahedron parameters appearing in $C_I$ are all position coordinates. Due to the definition of easy edges, we can always choose $\Pi_i\in \{\Pi_Z,\Pi_{Z'},\Pi_{Z''}\}$ so that the product polarization has this property. Then, in the theory $T_{\{\Delta_i\},\{\Pi_i^I\}}$ there will automatically exist an operator $\mathcal{O}_I$ for the edge $C_I$, constructed as a product of elementary chiral fields. For example, if our easy edge is $C_I = 2Z_1''+Z_3+Z_4'$, we choose a product polarization $\{\Pi_i^I\}$ that includes $\Pi_1^I = \Pi_{Z_1''},\,\Pi_3^I=\Pi_{Z_3},$ and $\Pi_4^I=\Pi_{Z_4'}$. Then $T_{\{\Delta_i\},\{\Pi_i^I\}}$ will have operators $\mathcal{O}_{Z_1''}$, $\mathcal{O}_{Z_3}$ and $\mathcal{O}_{Z_4'}$, all elementary chiral fields, from which we define $\mathcal{O}_I = (\mathcal{O}_{Z_1''})^2\mathcal{O}_{Z_3}\mathcal{O}_{Z_4'}$.

Now, we are really interested in the theory $T_{\{\Delta_i\},\tilde\Pi}$, associated to the polarization $\tilde\Pi$ in which every internal edge is a position coordinate. For each individual $C_I$, there exists an (affine) $Sp(2N,{\mathbb Z})$ transformation $g_I$ such that

$$\tilde\Pi = g_I\circ \{\Pi_i^I\}\,,\qquad T_{\{\Delta_i\},\tilde\Pi} = g_I\circ T_{\{\Delta_i\},\{\Pi_i^I\}}\,. \label{gI}$$

This is not quite an arbitrary transformation. In particular, since $C_I$ is a position coordinate in both $\{\Pi_i^I\}$ and $\tilde \Pi$, the action of $g_I$ cannot gauge any of the $U(1)$ flavor symmetries under which the operator $\mathcal{O}_I$ transforms. Therefore, we can easily pull $\mathcal{O}_I$ through the transformation on the right of [\[gI\]](#gI){reference-type="eqref" reference="gI"} to define the corresponding internal edge operator in $T_{\{\Delta_i\},\tilde\Pi}$.

If a triangulation only contains easy edges, we can repeatedly use this construction to define all the operators appearing in the superpotential [\[WforTM\]](#WforTM){reference-type="eqref" reference="WforTM"}. Notice, however, that we define each $\mathcal{O}_I$ using a different mirror Lagrangian description of $T_{\{\Delta_i\},\tilde\Pi}$. In any given description, one of the internal edge operators is "simple," being a gauge-invariant product of elementary chiral multiplets. The other operators may appear more complicated, and will in general take the form of monopole operators.

Just as we defined operators for internal edges, we can also define operators $\mathcal{O}_E$ for any easy external edges (or cusp holonomies) that are positions in $\Pi\subset\tilde\Pi$. In various mirror duality frames, they will appear either as products of chiral fields or monopole operators, and they will be charged under the flavor symmetries of $T_{M,\Pi}$ that correspond to the positions $X_E$ (or $U$, etc.).

Currently, we only have a rigorous construction of operators $\mathcal{O}_I$ and $\mathcal{O}_E$ for triangulations with easy edges. Indeed, it appears that if we try to define a theory $T_{M,\Pi}$ using a triangulation of $M$ with hard edges, the theory will be slightly degenerate --- and potentially missing some expected operators. We will see an example of this behavior in Section [\[sec:gauge41\]](#sec:gauge41){reference-type="ref" reference="sec:gauge41"}. Fortunately, it seems that we can always refine a given triangulation of a 3-manifold $M$ so that no hard edges are present, and then use this triangulation to construct $T_{M,\Pi}$.\
One of our central claims is that the theories $T_{M,\Pi}$ constructed here are topological invariants of a three-manifold $M$ (and a polarization of its boundary), which do not depend on the actual triangulation being used to define them --- or on the choice of refinement, should a given triangulation include hard edges. In particular, we claim that different triangulations lead to different mirror-symmetric descriptions of the same underlying 3d SCFT. To understand this, we now proceed to analyze the simplest and most important example of a triangulated 3-manifold: the bipyramid.

## The bipyramid and the 2--3 move {#sec:gauge23}

Let's consider the theory of the bipyramid, as constructed from two different triangulations. To keep things simple, we will focus on the "equatorial" polarization $\Pi=\Pi_{\rm eq}$ for the bipyramid, as defined in [\[bipcoord3\]](#bipcoord3){reference-type="eqref" reference="bipcoord3"} or [\[bipcoord2\]](#bipcoord2){reference-type="eqref" reference="bipcoord2"}. In particular, the three equatorial edges of the bipyramid are position coordinates in $\Pi$. We keep the same notation as in Section [\[sec:geom\]](#sec:geom){reference-type="ref" reference="sec:geom"}, and repeat Figure [\[fig:Pach\]](#fig:Pach){reference-type="ref" reference="fig:Pach"} here as a visual reference.

![Decompositions of the bipyramid, with labelled edge coordinates (Figure [\[fig:Pach\]](#fig:Pach){reference-type="ref" reference="fig:Pach"}).](Pach){#fig:Pach2 width="5in"}

If we decompose the bipyramid into three tetrahedra, then according to our rules $T_{ \{\Delta_i\} , \Pi}$ is a theory of three free chiral multiplets, coupled to a background $U(1)^3$, with some extra CS couplings determined by our choice of momenta in $\Pi$. The operator associated to the unique internal edge is simply the product of the three chiral fields. Hence $T_{M,\Pi}$ is simply the XYZ model, with appropriate coupling to the unbroken $U(1)^2$ flavor symmetry. The operators associated to the external edges are the three chiral multiplets themselves.

Being more explicit, we can start with a product polarization $\{\Pi_i\} = \{\Pi_Z,\Pi_W,\Pi_Y\}$, such that $Z,W,Y$ are coordinates and $Z'',W'',Y''$ are momenta. In the equatorial polarization $\Pi_{\rm eq}$, we know that $X_1 = Z$ and $X_2=W$ are positions while $P_1=Z''+Y'$ and $P_2=W''+Y'$ are momenta; we therefore choose a compatible polarization $\tilde\Pi$ on $\mathcal{P}_{\{\partial\Delta_i\}}$ with positions $X_1,X_2,C$ and momenta $P_1,P_2,\Gamma$, where $C=X+Y+Z$ and $\Gamma=-Y'$. The affine symplectic transformation $g$ from $\{\Pi_i\}$ to $\tilde\Pi$ is encoded as

$$\begin{pmatrix} X_1\\X_2\\C\\P_1\\P_2\\\Gamma\end{pmatrix}= \begin{pmatrix} 1&0&0&0&0&0\\ 0&1&0&0&0&0\\1&1&1&0&0&0 \\0&0&0&1&0&-1\\0&0&0&0&1&-1\\0&0&0&0&0&1\end{pmatrix}\begin{pmatrix} 1&0&0&0&0&0\\0&1&0&0&0&0\\0&0&1&0&0&0\\0&0&0&1&0&0 \\0&0&0&0&1&0\\0&0&1&0&0&1\end{pmatrix} \begin{pmatrix} Z\\W\\Y\\Z''\\W''\\Y''\end{pmatrix}+\begin{pmatrix} 0\\0\\0\\i\pi\\i\pi\\-i\pi\end{pmatrix}\,, \label{Spbip3}$$

which involves a $T$-type transformation, a $GL$-type transformation, and a shift that will not be visible at the level of Lagrangians. Thus, starting with a Lagrangian description

$$\begin{aligned}
 \mathcal{L}_{\{\Pi_i\}}[V_Z,V_W,V_Y] &= \frac{1}{4\pi}\int d^4\theta\Big(-\frac12 \Sigma_ZV_Z-\frac12 \Sigma_WV_W-\frac12\Sigma_YV_Y\Big)+ \notag\\ &\hspace{.8in} \int d^4\theta \big( \phi_Z^\dagger e^{V_Z}\phi_Z+\phi_W^\dagger e^{V_W}\phi_W+\phi_Y^\dagger e^{V_Y}\phi_Y\big) 
\end{aligned}$$

for $T_{\{\Delta_i\},\{\Pi_i\}}$, we construct the Lagrangian for $T_{\{\Delta_i\},\tilde\Pi} = g\circ T_{\{\Delta_i\},\{\Pi_i\}}$ simply as

$$\mathcal{L}_{\tilde\Pi}[V_{X_1},V_{X_2},V_C] = \mathcal{L}_{\{\Pi_i\}}[V_{X_1},V_{X_2},V_C-V_{X_1}-V_{X_2}]+\frac{1}{4\pi}\int d^4\theta(\Sigma_C-\Sigma_{X_1}-\Sigma_{X_2})\,(V_C-V_{X_1}-V_{X_2})\,, \label{Lbip3eq}$$

in other words by adding a level 1 Chern-Simons term for $V_Y$, and redefining $V_Z=V_{X_1},\,V_W=V_{X_2}$, and $V_Y=V_C-V_{X_1}-V_{X_2}$. It is trivial to see that the elementary operator

$$\mathcal{O}_C \equiv \phi_Z\phi_W\phi_Y \label{WXYZ}$$

exists in $T_{\{\Delta_i\},\tilde\Pi}$, as do the individual operators $\phi_Z,\phi_W,\phi_Y$ associated to the equatorial external edges. The bipyramid theory $T_{M,\Pi_{\rm eq}}$ is then defined by adding the superpotential $\mathcal{W}= \mathcal{O}_C$ to [\[Lbip3eq\]](#Lbip3eq){reference-type="eqref" reference="Lbip3eq"}, which forces $V_C=\theta\bar\theta m_C=0$; direct calculation then shows

$$\begin{aligned}
 \mathcal{L}_{M,\Pi_{\rm eq}}[V_{X_1},V_{X_2}]&=\frac{1}{4\pi}\int d^4\theta\, \Sigma_{X_1}V_{X_2} + \int d^4\theta \big( \phi_Z^\dagger e^{V_{X_1}}\phi_Z+\phi_W^\dagger e^{V_{X_2}}\phi_W+\phi_Y^\dagger e^{-V_{X_1}-V_{X_2}}\phi_Y\big) \notag\\
 &\hspace{.8in} + \int \big(d^2\theta \,\phi_Z\phi_W\phi_Y +c.c.\big)\,.
\label{XYZbip}
\end{aligned}$$

This is the promised XYZ model, with slightly redefined $U(1)^2$ symmetries, and a mixed Chern-Simons term.

If we decompose the bipyramid into two tetrahedra instead of three, we need no superpotential. On the other hand, the transformation $g$ from the polarization $\{\Pi_R,\Pi_{S''}\}$ for the two tetrahedra to $\Pi_{\rm eq}$ is non-trivial: as the positions are $X_1=R + S''$, $X_2=R'' + S$, and $R'+S'$, it is easy to see that $g$ involves gauging (with no CS coupling) the $U(1)$ under which the two chiral multiplets have opposite charge. Hence with this definition $T_{M,\Pi}$ is simply $N_f=1$ SQED, with appropriate coupling to the $U(1)^2$ flavor symmetry. The operator associated to the edge coordinate $X_1=R+S''$ is simply the meson operator.

Again, one can go through explicit Lagrangian manipulations as above. Starting from a polarization $\{\Pi_i\}=\{\Pi_R,\Pi_{S''}\}\sim (R,S'';R'',S')$ we reach the equatorial polarization $\Pi_{\rm eq}\sim (X_1,X_2;P_1,P_2)$ via a symplectic transformation $g = g_S\,g_T\,g_U$, with

$$\label{gbip2}
g_S = \begin{pmatrix} 1&0&0&0\\0&0&0&-1\\0&0&1&0\\0&1&0&0\end{pmatrix},\quad
g_T = \begin{pmatrix} 1&0&0&0\\0&1&0&0\\0&0&1&0\\0&1&0&1\end{pmatrix},\quad
g_U = \begin{pmatrix} 1&1&0&0\\0&1&0&0\\0&0&1&0\\0&0&-1&1 \end{pmatrix}\,.$$

Therefore, we obtain $\mathcal{L}_{M,\Pi_{\rm eq}}[V_{X_1},V_{X_2}]$ by starting with

$$\mathcal{L}_{\{\Delta_i\},\{\Pi_i\}}[V_R,V_{S''}]=\frac{1}{4\pi}\int d^4\theta\Big(-\frac12 \Sigma_RV_R-\frac12 \Sigma_{S''}V_{S''}\Big)+ \int d^4\theta \big( \phi_R^\dagger e^{V_R}\phi_R+\phi_{S''}^\dagger e^{V_{S''}}\phi_{S''}\big)\,,$$

redefining the $U(1)^2$ symmetry, adding a Chern-Simons term, and gauging a $U(1)$. A straightforward calculation produces

[^1]

$$\begin{aligned}
 \mathcal{L}_{M,\Pi_{\rm eq}}[V_{X_1},V_{X_2}] &= \frac{1}{4\pi}\int d^4\theta\big(\Sigma_{X_1}V_{X_2}+(\Sigma_{X_1}+2\Sigma_{X_2})\,V\big) \notag \\
 &\qquad\qquad +\int d^4\theta\big( \phi_R^\dagger e^{V+\frac12{V_{X_1}}}\phi_R+\phi_{S''}^\dagger e^{-V+\frac12{V_{X_1}}}\phi_{S''}\big)\,, \label{SQEDbip}
\end{aligned}$$

with the $U(1)$ gauge multiplet $V$ dynamical. This is precisely $N_f=1$ SQED, with a mixed Chern-Simons coupling, and slightly redefined $U(1)^2$ symmetry. The meson operator $\mathcal{O}_{X_1}\equiv \phi_R\phi_{S''}$ is obviously charged under $V_{X_1}$. We know that SQED also has two monopole operators $v_+$ and $v_-$, and from the form of the FI term in [\[SQEDbip\]](#SQEDbip){reference-type="eqref" reference="SQEDbip"} we see that they must be charged under the combinations $V_{X_2}$ and $-V_{X_1}-V_{X_2}$, respectively. Thus, they correspond to the remaining two equatorial edges.

Thanks to the basic $\mathcal{N}=2$ mirror symmetry statement [\[XYZmir\]](#XYZmir){reference-type="eqref" reference="XYZmir"}, our construction gives the same theory $T_{M,\Pi}$ for the bipyramid, *no matter how we triangulate it*. By carefully comparing the Lagrangian descriptions [\[XYZbip\]](#XYZbip){reference-type="eqref" reference="XYZbip"} and [\[SQEDbip\]](#SQEDbip){reference-type="eqref" reference="SQEDbip"}, we see that the three equatorial edge operators --- elementary fields in the XYZ model and a meson/monopoles in SQED --- are mapped to each other by mirror symmetry, and their coupling to the background $U(1)$ gauge multiplets $V_{X_1}$ and $V_{X_2}$ coincide perfectly.

One can also repeat the exercise for the longitudinal polarization. The two triangulations give respectively $\mathcal{N}=4$ SQED with $N_f=1$ and the theory of a free hypermultiplet, *i.e.* the basic $\mathcal{N}=4$ mirror pair. This is a useful exercise in order to show that the operators associated to longitudinal edges by the two polarizations are also mapped into each other by mirror symmetry.

With this result, we are in position to argue that the theories $T_{M,\Pi}$ defined by different triangulations of the same three-manifold $M$ are mirror to each other. Different triangulations are related by a sequence of $2-3$ moves.

[^2]

Two triangulations that differ by a $2-3$ move give two definitions of the theory $T_{M,\Pi}$ that differ only by a basic mirror symmetry relation. The mirror symmetry acts on the degrees of freedom associated to the particular bipyramid that is decomposed in two different ways in the course of a $2-3$ move.

[^1]: []{#foot:half label="foot:half"} In the last step of the derivation of [\[SQEDbip\]](#SQEDbip){reference-type="eqref" reference="SQEDbip"}, we shifted the dynamical gauge multiplet $V\to V+\frac12 V_{X_1}$, thereby adding to the '$X_1$' flavor current a half-integral multiplet of the gauge current. This non-integral shift is not necessary, but can be made sense of because the multiplet $V_{X_1}=\theta\bar\theta m_{X_1}$ is nondynamical. In the form [\[SQEDbip\]](#SQEDbip){reference-type="eqref" reference="SQEDbip"} of the Lagrangian, the identification of $\frac12 V_{X_1}$ with an axial flavor multiplet becomes immediate.

[^2]: Strictly speaking, we should only consider triangulations that have easy edges, as discussed in Section [\[sec:defTM\]](#sec:defTM){reference-type="ref" reference="sec:defTM"}. It is very plausible --- although not mathematically proven --- that to connect two "easy" triangulations, one can always find a chain of $2-3$ moves that only pass through other easy triangulations.
