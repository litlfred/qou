---
doc_id: arxiv-1007.2335v1
doc_title: "Hopf solitons in the Nicole model"
section_id: sec-001-2-the-nicole-model-and-volume-preserving-flow
section_title: "The Nicole model and volume-preserving flow"
section_number: 2
pages: 3-6
source_pdf: 1007.2335v1.pdf
source_sha256: a55d544d1740523f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.997
doc_brief: "Hopf solitons in the Nicole model — The Nicole model is a conformal ﬁeld theory in three-dimensional space."
---
The Nicole model [@Ni] is a rather exotic modification of the $O(3)$ sigma model, although it involves the same field $\mbox{\boldmath $\phi$}:\hbox{\mybb R}^3\mapsto S^2,$ which is realized as a real three-component vector $\mbox{\boldmath $\phi$}=(\phi_1,\phi_2,\phi_3),$ of unit length, $\mbox{\boldmath $\phi$}\cdot\mbox{\boldmath $\phi$}=1.$ As we are concerned only with static solutions then the Nicole model may be defined by its static energy $$E=\frac{1}{32\pi^2\sqrt{2}}\int (\partial_i\mbox{\boldmath $\phi$}\cdot\partial_i\mbox{\boldmath $\phi$})
^\frac{3}{2}\ d^3x, \label{energy_ni}$$ where the normalization is chosen for later convenience.

The fractional power in ([\[energy_ni\]](#energy_ni){reference-type="ref" reference="energy_ni"}) is a novel modification of the sigma model energy density and is clearly engineered to produce a conformal theory in three spatial dimensions. Although there is no known physical motivation for this theory, there is a mathematical stimulus to investigate the model as the conformal symmetry leads to interesting mathematical properties: including an explicit exact solution for the $Q=1$ Hopf soliton. By studying this theory it is possible to make comparisons with Hopf solitons of the Skyrme-Faddeev model and hence determine which features appear to be generic. This should help in understanding the properties of Hopf solitons in theories constructed from more conventional terms.

Finite energy boundary conditions require that the field tends to a constant value at spatial infinity, which is chosen to be $\mbox{\boldmath $\phi$}=(0,0,1)\equiv{\bf e}_3.$ This boundary condition compactifies space to $S^3,$ so that the field becomes a map $\mbox{\boldmath $\phi$}:
S^3\mapsto S^2.$ There is a homotopy classification of such maps, given by the Hopf charge $Q\in\hbox{\mybb Z}=\pi_3(S^2).$ This integer has a geometrical interpretation as the linking number of two curves obtained as the preimages of any two distinct points on the target two-sphere.

The position of the soliton is the closed curve obtained as the preimage of the point $\mbox{\boldmath $\phi$}=(0,0,-1),$ which is antipodal to the vacuum value ${\bf e}_3$ on the target two-sphere. Hopf solitons are therefore novel string-like topological solitons.

The static field equation that follows from the variation of the energy ([\[energy_ni\]](#energy_ni){reference-type="ref" reference="energy_ni"}) is the

nonlinear partial differential equation $$\partial_i\partial_i\mbox{\boldmath $\phi$}
+(\partial_i\mbox{\boldmath $\phi$}\cdot\partial_i\mbox{\boldmath $\phi$})\mbox{\boldmath $\phi$}
+\frac{(\partial_i\partial_j\mbox{\boldmath $\phi$}\cdot\partial_j\mbox{\boldmath $\phi$})\partial_i\mbox{\boldmath $\phi$}}
{\partial_k\mbox{\boldmath $\phi$}\cdot\partial_k\mbox{\boldmath $\phi$}}={\bf 0}.
\label{eom_ni}$$

Using combinations of stereographic projection and the standard Hopf map, the solution with Hopf charge $Q=1$ is explicitly given by [@Ni] $$\frac{\phi_1+i\phi_2}{1+\phi_3}
=\frac{2\lambda(x_1+ix_2)}{r^2-\lambda^2+2i\lambda x_3}.
\label{Q1}$$ Here $r^2=x_ix_i$ and $\lambda$ is an arbitrary positive real constant associated with the scale of the soliton. It is easily seen from ([\[Q1\]](#Q1){reference-type="ref" reference="Q1"}) that the position of the soliton is the circle in the plane $x_3=0$ with centre the origin and radius $\lambda.$ The fact that $\lambda$ is arbitrary is a result of the conformal symmetry of the Nicole model.

The energy of this soliton is $E=1,$ as a result of the convenient normalization of the energy in ([\[energy_ni\]](#energy_ni){reference-type="ref" reference="energy_ni"}). The soliton is axially symmetric and is of the type ${\cal A}_{1,1}.$

In this paper we are interested in Hopf solitons of the Nicole model with $Q>1,$ for which explicit closed form solutions are not available. Numerical methods are therefore required to find solutions of equation ([\[eom_ni\]](#eom_ni){reference-type="ref" reference="eom_ni"}) that correspond to local minima of the energy ([\[energy_ni\]](#energy_ni){reference-type="ref" reference="energy_ni"}), including the global energy minimum in each sector with Hopf charge $Q$ that we consider.

The discretization (and restriction to a finite simulation region) involved in the numerical simulation of a conformal field theory breaks the conformal invariance of the continuum theory and leads to technical difficulties. This has been studied in detail for solitons in a simpler conformal field theory, namely the $O(3)$ sigma model in two-dimensional space. The numerical discretization is equivalent to studying a lattice version of the theory and in the planar case the resulting energy minimization leads to an exceptional configuration on the lattice [@Lu]. In the continuum theory this is associated with a reduction of the soliton scale until it is of the same order as the lattice spacing, at which point the topology of the soliton is lost as it unwinds by essentially falling through the lattice [@LPZ]. In the case of the planar sigma model a novel lattice formulation has been devised [@Ward] that preserves topology on the lattice. However, the topology of Hopf solitons in the Nicole model is significantly more complicated than that of solitons in the planar sigma model, and no analogous topology preserving lattice formulation is known.

As expected, a standard discretization and energy minimization of the Nicole model leads to the same technical difficulties as described above. Namely, any initial condition with $Q\ne 0$ shrinks until the size of the configuration is of the same order as the lattice spacing, upon which the topology is lost, leading to a trivial vacuum solution with $Q=0$. An additional, though related, issue is that in numerical simulations Euclidean space is typically replaced by a finite region $\Omega,$ with the field fixed to its vacuum value on the boundary of $\Omega.$ This will be a good approximation if $\Omega$ is large compared to the soliton size. However, in a conformal theory there is no fixed soliton size and the restriction to a finite volume also results in the shrinking of a soliton. To overcome these difficulties we introduce a volume-preserving flow, using ideas based on a similar approach developed in the context of domain walls [@GS].

To describe the construction of our volume-preserving flow we initially concentrate on the continuum theory defined in a finite region $\Omega,$ with vacuum boundary conditions, $\mbox{\boldmath $\phi$}={\bf e}_3$ on $\partial\Omega.$ In the later numerical simulations $\Omega$ will be taken to be a cube.

A standard method to minimize the energy ([\[energy_ni\]](#energy_ni){reference-type="ref" reference="energy_ni"}) is to evolve any given initial condition using gradient flow. A flow which is proportional to gradient flow is given by $$\partial_{t}\mbox{\boldmath $\phi$}={\bf F},
\label{gf0}$$ where the force ${\bf F}$ is the left-hand-side of the static field equation ([\[eom_ni\]](#eom_ni){reference-type="ref" reference="eom_ni"}), and is proportional to the variation of the energy (taking into account the constraint that $\mbox{\boldmath $\phi$}$ lies on the unit two-sphere). Theoretically, the end-point of this flow yields static solutions that solve equation ([\[eom_ni\]](#eom_ni){reference-type="ref" reference="eom_ni"}). As described above, a numerical discretization introduces a spatial lattice that breaks the conformal symmetry of the theory, so that a numerical solution of a standard discrete version of ([\[gf0\]](#gf0){reference-type="ref" reference="gf0"}) results in a Hopf soliton that continually shrinks during the flow. A minimal energy Hopf soliton in the continuum theory has zero modes (in particular a scale invariance) associated with the conformal symmetry and the spatial lattice produces negative modes associated with the broken zero modes. The idea is to modify the standard gradient flow ([\[gf0\]](#gf0){reference-type="ref" reference="gf0"}) by projecting out the component in the direction of the zero mode. The subsequent discretization will then not produce negative modes since their origin has been removed from the flow.

Define the following volume associated with a field configuration $$V=\int_\Omega (1-\phi_3)\ d^3x.
\label{vol}$$ This volume will serve as a measure of the size of a soliton, since the integrand is maximal along the position of the soliton and is zero if the field takes its vacuum value. In particular, the shrinking of a soliton that results from the numerical discretization corresponds to a decrease of the volume $V$ during the gradient flow ([\[gf0\]](#gf0){reference-type="ref" reference="gf0"}). The aim is to construct a modified version of gradient flow that preserves the volume $V,$ and hence fixes the soliton scale.

Associated with the volume ([\[vol\]](#vol){reference-type="ref" reference="vol"}) is the gradient flow $$\partial_{t}\mbox{\boldmath $\phi$}={\bf e_3}-\phi_3\mbox{\boldmath $\phi$}\equiv {\bf f},
\label{gf1}$$ which results in a decrease in the volume $V$ during this flow, since the force ${\bf f}$ is proportional to the variation of $V.$ Define the inner product $$<{\bf f},{\bf g}>\ =\int_{\Omega} {\bf f}\cdot {\bf g}\ d^3x,
\label{inner}$$ then the volume-preserving flow is given by $$\partial_t\mbox{\boldmath $\phi$}={\bf F}-\frac{<{\bf F},{\bf f}>}{<{\bf f},{\bf f}>}{\bf f}.
\label{vpgf}$$ This flow has been constructed by taking the standard gradient flow and then projecting out the component due to the volume reducing flow ([\[gf1\]](#gf1){reference-type="ref" reference="gf1"}). The resulting flow is therefore orthogonal to the volume reducing flow and hence preserves the volume. It is easy to prove that the volume-preserving flow ([\[vpgf\]](#vpgf){reference-type="ref" reference="vpgf"}) indeed preserves the volume $V$ and reduces the energy $E$: the proof is a simple modification of that presented in [@GS] but the result should be obvious from the geometrical aspect of its construction.

Equation ([\[vpgf\]](#vpgf){reference-type="ref" reference="vpgf"}) is a nonlinear partial differential equation but it is also nonlocal, because of the appearance of the inner product. However, it can be solved numerically using standard finite difference methods. In section [\[sec-num\]](#sec-num){reference-type="ref" reference="sec-num"} we shall present results for a scheme using fourth-order accurate finite difference approximations to spatial derivatives on a cubic lattice consisting of $151^3$ points with unit lattice spacing (taking advantage of the scale invariance of the continuum problem in $\hbox{\mybb R}^3$). The flow is evolved using a simple first-order accurate explicit method with timestep $\Delta t=0.1.$ All inner products are evaluated by approximating integrals by sums over lattice sites.
