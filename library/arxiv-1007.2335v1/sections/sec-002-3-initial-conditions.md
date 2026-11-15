---
doc_id: arxiv-1007.2335v1
doc_title: "Hopf solitons in the Nicole model"
section_id: sec-002-3-initial-conditions
section_title: "Initial conditions"
section_number: 3
pages: 6-7
source_pdf: 1007.2335v1.pdf
source_sha256: a55d544d1740523f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 1.0
doc_brief: "Hopf solitons in the Nicole model — The Nicole model is a conformal ﬁeld theory in three-dimensional space."
---
Initial conditions, for a range of values of $Q,$ need to be provided for the volume-preserving flow algorithm discussed in the previous section. We use the approach introduced in [@Su], which is briefly reviewed in this section.

To construct an initial field the spatial coordinates $(x_1,x_2,x_3)\in \hbox{\mybb R}^3$ are first mapped to the unit three-sphere via a degree one spherically equivariant map. Explicitly, introduce the complex coordinates $Z_1,Z_0$ (on the unit three-sphere $|Z_1|^2+|Z_0|^2=1$) as $$(Z_1,Z_0)=\bigg((x_1+ix_2)\frac{\sin g}{r},\cos
g+i\frac{\sin g}{r}x_3\bigg),$$where the profile function $g(r)$ is a monotonically decreasing function of the radius $r$, with boundary conditions $g(0)=\pi$ and $g(\infty)=0.$

The initial condition is obtained by taking the stereographic projection of $\mbox{\boldmath $\phi$}$ to be a rational function of $Z_1$ and $Z_0.$ The simplest example is to take $$\frac{\phi_1+i\phi_2}{1+\phi_3}=\frac{Z_1}{Z_0},
\label{Qnm11}$$ which has $Q=1$ and is identical to the exact solution ([\[Q1\]](#Q1){reference-type="ref" reference="Q1"}) if the profile function is taken to be $g=\tan^{-1}(2r\lambda/(r^2-\lambda^2)).$

Other choices of rational functions and profile functions do not give exact solutions but do provide suitable initial conditions for the numerical simulation.

An obvious generalization of ([\[Qnm11\]](#Qnm11){reference-type="ref" reference="Qnm11"}) is given by $$\frac{\phi_1+i\phi_2}{1+\phi_3}=\frac{Z_1^n}{Z_0^m}.
\label{Qnm}$$ This is an axially symmetric field with Hopf charge $Q=nm.$ As discussed later, under volume-preserving flow this initial condition yields the solution of type ${\cal A}_{n,m},$ obtained previously using toroidal coordinates [@ASVW].

Initial fields that are not axially symmetric and include knots and links can be obtained from less symmetric rational maps. For full details see [@Su] but some examples that are used in this paper include the $(a,b)$-torus knot (here $a,b$ are coprime positive integers with $a>b$) $$\frac{\phi_1+i\phi_2}{1+\phi_3}=\frac{Z_1^\alpha Z_0^\beta}{Z_1^a+Z_0^b},
\label{Qab}$$ where $\alpha$ is a positive integer and $\beta$ is a non-negative integer. The Hopf charge of this field is $Q=\alpha b+\beta a.$ The position of this field is an $(a,b)$-torus knot and we denote a field of this type by ${\cal K}_{a,b}.$ Of particular relevance will be the simplest torus knot, the trefoil knot, which corresponds to $(a,b)=(3,2)$ and can be obtained with $Q=7$ from the choice $\alpha=2$ and $\beta=1.$

In all the configurations discussed above, the position curve contains only a single component. However, Hopf solitons also exist in which the position curve contains disconnected components that are linked. In the simplest case there are just two components and such a linked configuration will be denoted by the type ${\cal L}_{p,q}^{\alpha,\beta},$ where $p$ and $q$ denote the Hopf charges of the two components if each is taken in isolation, and $\alpha$ and $\beta$ are the additional contributions to the Hopf charge due the linking of each of the components with the other. The total Hopf charge is therefore $Q=p+q+\alpha+\beta.$ Initial fields of this type can be constructed using a rational map in which the denominator is reducible. As an example, the field $$\frac{\phi_1+i\phi_2}{1+\phi_3}=\frac{Z_1^{n+1}}{Z_1^2-Z_0^2},
\label{Qlink}$$ is of the type ${\cal L}_{n,n}^{1,1}.$ It consists of two Hopf solitons that are each of the topological type ${\cal A}_{n,1}$ and are linked once to create a field with Hopf charge $Q=2n+2.$

The construction described in this section is easily applied to the situation of a finite simulation region $\Omega$ by replacing the profile function boundary condition $g(\infty)=0$ by the condition that $g=0$ on the boundary $\partial \Omega.$
