---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-011-32-a-mathbb-z-2-action-on-3d-mathcaln2-theories
section_title: "A ${\mathbb Z}_2$ action on 3d $\mathcal{N}=2$ theories with a chiral operator"
section_number: 3.2
pages: 24-25
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:F label="sec:F"}

The basic "matter" action on 3d $\mathcal{N}=2$ theories begins with a theory that has a coupling to a background 3d chiral multiplet $\phi$. In practice, what we mean is a choice of chiral operator $\mathcal{O}$ that can be inserted in a superpotential $$\mathcal{W}= \phi\,\mathcal{O}\,.$$ Here and elsewhere, we will not keep track of the normalization of superpotential terms. In particular, we will view a rescaling of $\mathcal{O}$ as a trivial operation.

We can define an operation $F$ that makes $\phi$ dynamical (thus, setting $\mathcal{O}$ effectively to zero). The new theory can be coupled to a new background chiral field $\phi'$ by coupling to the new chiral operator $\mathcal{O}'=\phi$, namely by the superpotential $$\mathcal{W}= \phi' \phi \,.$$ It is easy to see that $F^2=1$. We can simply look at the combined superpotential $$\mathcal{W}= \phi'' \phi'+\phi' \phi +\phi\,\mathcal{O}$$ and integrate out $\phi'$.

Much like the "gauge" $Sp(2N,{\mathbb Z})$ action of the previous subsection, the operation $F$ can be given an interesting four-dimensional interpretation. One can consider possible boundary conditions on a four-dimensional hypermultiplet. If we split the four real scalar fields in the hypermultiplet into two complex scalar fields, which we can denote as $X$ and $Y$, then the two basic boundary conditions are either Neumann for $X$ and Dirichlet for $Y$, or vice versa. A way to understand this is that $Y$ sits in a multiplet of the unbroken supersymmetry which contains the normal derivative of $X$.

If we introduce extra degrees of freedom at the boundary, say a 3d theory with a preferred chiral operator $\mathcal{O}$, then we can consider a deformed Dirichlet boundary condition $Y=\mathcal{O}$. This will be accompanied by a corresponding deformation of the Neumann boundary conditions for $X$, involving the corresponding piece of the supermultiplet $\mathcal{O}$. This defines a certain class of boundary conditions which we denote $\mathcal{B}_Y$, so that the boundary condition associated to a 3d theory $\mathcal{T}$ is denoted by $\mathcal{B}_Y[\mathcal{T}]$. An alternative way to describe this boundary condition is to start with the undeformed boundary condition and add the boundary superpotential coupling $$\mathcal{W}= X \mathcal{O}\,.$$

Naively, one can construct a completely different class of boundary conditions $\mathcal{B}_X$ as Dirichlet boundary conditions with $X=\mathcal{O}'$, where $\mathcal{O}'$ is a chiral operator in a 3d boundary theory $\mathcal{T}'$. It turns out that these two classes actually coincide, as every member $\mathcal{B}_Y[\mathcal{T}]$ of one class has a mirror $\mathcal{B}_X[\mathcal{T}']$ in the other class. One simply takes $\mathcal{T}'$ to be the image of $\mathcal{T}$ under $F$, with $\mathcal{O}' = \phi$; then we claim that

$$\mathcal{B}_Y[\mathcal{T}] = \mathcal{B}_X[F\circ\mathcal{T}]\,.$$

To see this, we simply follow the definition of $F\circ\mathcal{T}$ to obtain an overall superpotential coupling $$\mathcal{W}= Y \phi + \phi\,\mathcal{O}\,.$$ Integrating out $\phi$ sets $Y = - \mathcal{O}$. Furthermore, the boundary condition $X=\phi$ means that we can simply "absorb" $\phi$ into $X$, thus relaxing the Dirichlet boundary conditions. It takes a bit more work to make sure that $X$ acquires Neumann boundary conditions, but it follows from the fact that the normal derivative $\partial_n X$ plays the role of auxiliary field in the $Y$ supermultiplet. In summary, if we begin with Dirichlet boundary conditions for $X$ and perform an $F$ transformation --- adding a single boundary chiral multiplet $\phi$ and a superpotential $\mathcal{W}= Y\phi$ --- we will flow in the IR to Dirichlet boundary conditions for $Y$.
