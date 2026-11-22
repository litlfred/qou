---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-021-52-boundary-conditions-for-hypermultiplets
section_title: "Boundary conditions for hypermultiplets"
section_number: 5.2
pages: 51-52
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.764
latex_coverage_ratio: 0.991
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
So far, we have considered $U(1)^N$ vector multiplets coupled to a boundary theory $T_M$. Generically, the 4d theories $T[\partial M]$ arising from a geodesic boundary $M$ will also involve hypermultiplet matter, which leads to further interesting observations in our 3d/4d setup.

A theory of a single hypermultiplet has two natural classes of boundary conditions. In one class, one of the chiral fields $Y$ in the hypermultiplet has Dirichlet-type boundary conditions, $$Y = \mathcal{O}$$ for some chiral operator $\mathcal{O}$ in the boundary theory, and the other chiral field $\tilde Y$ has Neumann-type boundary conditions. In the other class, the roles of $Y$ and $\tilde Y$ are exchanged. These boundary conditions were defined, *e.g.*, in Section 3 of [@DGG].

It turns out that each boundary condition in one class is mirror to a boundary condition in the other class. The corresponding boundary theories are related by an "F" transformation, which maps the theory with chiral operator $\mathcal{O}$ to a new theory with a new 3d chiral field $\phi$ coupled by the superpotential $\phi \mathcal{O}$. In the new theory, $\phi$ plays the role of the special chiral operator $\tilde \mathcal{O}$.

This mirror symmetry is manifest in the 3d/4d index calculations. The contribution of one hypermultiplet to the Schur index looks like $$\mathcal{I}_{hyper}= \frac{1}{\prod_{n>0} ( 1 - \zeta q^{n+1/2})( 1 - \zeta^{-1} q^{n+1/2})}\,.$$ This simply counts angular momentum modes of the two chiral fields $Y$ and $\tilde Y$, of charge $\pm 1$ under the flavor symmetry with fugacity $\zeta$.

If we impose Dirichlet boundary conditions on $\tilde Y$, we are left with the contribution from $Y$ only, $$\mathcal{I}_Y \; = \; \frac{1}{\prod_{n>0} ( 1 - \zeta q^{n+1/2})} \,.$$ Similarly, in the case of Dirichlet boundary conditions for $Y$ we get $$\mathcal{I}_{\tilde Y} \; = \; \frac{1}{\prod_{n>0} ( 1 - \zeta^{-1} q^{n+1/2})} \,.$$ And, of course, the product of $\mathcal{I}_{\tilde Y}$ with the 3d index of a free 3d chiral field of charge $1$, in the absence of magnetic flux, gives $\mathcal{I}_Y$, as expected from the discussion of the F move.

[^1]

Crucially, we expect the mirror relation to hold even in the presence of 't Hooft operators at the North pole. Thus we can predict, up to a prefactor, how the Schur index for a hypermultiplet should look in the presence of such a magnetic charge: $$\mathcal{I}_{hyper}(m; q,\zeta) \;= \; \frac{1}{\prod_{n>0} ( 1 - \zeta q^{n+1/2+|m|/2})( 1 - \zeta^{-1} q^{n+1/2+|m|/2})} \,. \label{eq:maghyper}$$

[^1]: Furthermore, $\mathcal{I}_{hyper} = \mathcal{I}_Y \mathcal{I}_{\tilde Y}$, while obvious, can be given a neat interpretation: in order to describe a hypermultiplet on the whole space, one can start with Dirichlet boundary conditions on $\tilde Y$ for a half-space, and Dirichlet boundary conditions on $Y$ for the second half-space, and "glue" them together by a $Y_- \tilde Y_+$ 3d superpotential integrated over the equator. Here $Y_-$ and $\tilde Y_+$ denote the boundary values of $Y$ and $\tilde Y$ from the two sides. This "gluing" prescription is akin to the idea that a gauge theory on the full space can be reconstructed from the gauge theory on two half-spaces with Dirichler boundary conditions by gauging the diagonal flavor symmetry at the boundary
