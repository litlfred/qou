---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-022-34-independence-of-a-choice-of-meridian-path
section_title: "Independence of a choice of meridian path"
section_number: 3.4
pages: 18-19
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.976
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.invmerid label="sec.invmerid"}

Recall that an ideal triangulation on $M$ induces a triangulation of its boundary torus $\partial M$. Consider two simple closed meridian loops in $\partial M$ in general (normal) position with respect to the triangulation of $\partial M$. Recall that these paths are drawn on the triangulated 2-dimensional torus $\partial M$ where faces of tetrahedra correspond to edges in the 2-dimensional triangulation, and edges of tetrahedra to vertices. In particular, for a one-cusped manifold $M$, every edge of the triangulation intersects a pair of vertices on the boundary $\partial M$.

![The fundamental move for changing a meridian path. Here, we deform through an edge $E_I$ with gluing constraint $X_I = Z+W+R_1+...+R_j+S_1+...+S_{j'}=2\pi i$.](meridmove){#fig.meridmove width="4.5in"}

We can deform one of our meridian paths into the other by using repeated applications of the fundamental move shown in Figure [1](#fig.meridmove){reference-type="ref" reference="fig.meridmove"} --- locally pushing a section of the path across a vertex of $\partial M$. Thus, it suffices to assume that the two paths only differ by one such move. Suppose that we cross the $I^{\text{th}}$ edge (by Section [\[sec.invglue\]](#sec.invglue){reference-type="ref" reference="sec.invglue"} we may assume that $I\neq N$), which has a combinatorial gluing constraint

$$X_I := 
\sum_{i=1}^N \big(\mathbf{G}_{Ii}Z_i+\mathbf{G}_{Ii}'Z_i'+\mathbf{G}_{Ii}''Z_i''\big) 
= 2\pi i\,,$$

and that the two tetrahedra where the paths enter and exit the vicinity of the edge have parameters $(Z,Z',Z'')$ and $(W,W',W'')$, as in the figure. We do not exclude the possibility that $(Z,Z',Z'')$ and $(W,W',W'')$ both coincide with the same triple $(Z_i,Z_i',Z_i'')$, in some cyclic permutation.

Then the difference in the logarithmic meridian equations [\[merid\]](#merid){reference-type="eqref" reference="merid"} for the two paths will be

$$\delta_\mu = \pm \big(X_I - (Z+Z'+Z'')-(W+W'+W'')\big)\,. 
\label{meridchange}$$ Note that two logarithmic meridian constraints that differ by [\[meridchange\]](#meridchange){reference-type="eqref" reference="meridchange"} are compatible and equivalent, since upon using the additional equations $X_I=2\pi i$ and $Z+Z'+Z''=W+W'+W''=i\pi$, we find that $\delta_\mu = 0$. A discretized version of this observation demonstrates that that the same flattening satisfies both discretized meridian constraints.

[^1]

If we compute matrices $\mathbf A,\,\mathbf B$ using one meridian path and $\widetilde{\mathbf A},\,\widetilde{\mathbf B}$ using the other --- keeping quad type, flattening, and edge the same --- the change [\[meridchange\]](#meridchange){reference-type="eqref" reference="meridchange"} implies that

$$\widetilde{\mathbf A} = P^{(\mu)}_I{}^{\pm 1}\mathbf A\,,
\qquad \widetilde{\mathbf B} = P^{(\mu)}_I{}^{\pm 1}\mathbf B\,,$$

where $P^{(\mu)}_I$ is the $\mathrm{SL}(N,\mathbb{Z})$ matrix

$$P^{(\mu)}_I = I + E_{NI}\,,$$

*i.e.* the identity plus an extra entry '1' in the $N^{\text{th}}$ (meridian) row and $I^{\text{th}}$ column. Since $\det P^{(\mu)}_I=1$, this immediately shows that $\det\big(\widetilde{\mathbf A}\Delta_{z''}+\widetilde{\mathbf B}\Delta_{z}^{-1}\big)
= \det\big({\mathbf A}\Delta_{z''}+{\mathbf B}\Delta_{z}^{-1}\big)$, and so the a change in the meridian path cannot affect $\tau_{\mathcal{T}}$.

[^1]: Note that this would not be the case if we allowed self-intersections of the meridian loops.
