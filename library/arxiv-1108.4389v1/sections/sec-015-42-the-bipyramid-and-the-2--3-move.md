---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-015-42-the-bipyramid-and-the-2--3-move
section_title: "The bipyramid and the 2--3 move"
section_number: 4.2
pages: 33-36
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.884
latex_coverage_ratio: 0.986
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:gauge23 label="sec:gauge23"}

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
