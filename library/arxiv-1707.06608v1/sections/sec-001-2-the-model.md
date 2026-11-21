---
doc_id: arxiv-1707.06608v1
doc_title: "Fractional Hopﬁons in the Faddeev-Skyrme model with a symmetry breaking potential"
section_id: sec-001-2-the-model
section_title: "The model"
section_number: 2
pages: 2-5
source_pdf: 1707.06608v1.pdf
source_sha256: 7b7db6dce87dc81e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.849
doc_brief: "Fractional Hopﬁons in the Faddeev-Skyrme model with a symmetry breaking potential — We construct new solutions of the Faddeev-Skyrme model with a symmetry breaking potential admitting S1 vacuum."
---
The Lagrangian density of the Faddeev-Skyrme model in (3+1)-dimensional flat space can be written in terms of the real triplet of scalar fields $\vec\phi=(\phi_1,\phi_2,\phi_3)$ as [@Faddeev-Hopf; @Faddeev:1996zj] $$\label{lagr}
\ensuremath{\mathcal{L}}=\int d^3 x\left[c_2\partial_\mu \vec\phi\cdot\partial^\mu \vec\phi -
\frac{c_4}{2}\left(\partial_\mu \vec\phi\times\partial_\nu \vec\phi\right)^2 - V(\phi)\right]$$ where $c_2,c_4$ are some real positive parameters and $g^{\mu\nu}=diag(1,-1,-1,-1)$.

As in the usual non-linear $O(3)$ sigma model, the scalar field is constrained to the unit sphere $S^2$:  $|\vec{\phi}|=1$. The topological restriction on the field $\vec \phi$ is that it approaches its vacuum value at spacial boundary, i.e. $\vec \phi_\infty = (0,0,1)$. This allows a one-point compactification of the domain space $\mathbb{R}^3$ to $S^3$ and the field of the finite energy solutions of the model, the Hopfions, is a map $\phi^a:\mathbb{R}^3 \mapsto S^2$ which belongs to an equivalence class characterized by the homotopy group $\pi_3(S^2)=\mathbb{Z}$.

Mathematically, the definition of the Hopf invariant can be given by defining an area form $\omega$, which is a generator of the second cohomology group $H^2(S^3)$ on the target space $S^2$. Then the Hopf map $\phi: S^3 \mapsto S^2$ has an induced pullback of the cohomology group $\phi^*:H^2(S^2) \mapsto H^2(S^3)$. Since the second cohomology group of $S^3$ is trivial $H^2(S^3)=0$, the pullback $F=\phi^* \omega$ of the area two-form $\omega$ by $\phi$ is exact, $F=dA$ where $A$ is a one-form. Explicitly, the corresponding Hopf invariant is defined as the integral of a Chern-Simons three-form over the space $S^3$ $$Q=\frac{1}{8\pi^2}\int\limits_{S^3}\!\! F \wedge A \in \mathbb{Z}
\label{Hopf-charge}$$ where $F=\frac12 F_{\mu\nu} dx^\mu \wedge dx^\nu$ is a 2-form with components $$F_{\mu\nu} = \vec\phi \cdot \partial_\mu \vec \phi \times  \partial_\nu \vec\phi$$ Note that the Hopf invariant cannot be written in terms of $\phi$ as a local density. More simple geometrical definition of this invariant is as the linking number of two loops on the domain space $S^3$, which are the preimages of two distinct points on the target space $S^2$.

The static energy functional of the model ([\[lagr\]](#lagr){reference-type="ref" reference="lagr"}) is $$\label{hopfenergy}
E=\int d^3 x \mathcal{E} = \int d^3 x\left[c_2\partial_i\vec\phi\cdot\partial_i\vec\phi +
\frac{c_4}{2}\left(\partial_i\vec\phi\times\partial_j\vec\phi\right)^2 + V\right]$$ The soliton solutions of the Faddeev-Skyrme model, correspond to the stationary points of this functional.

Similarity of the Lagrangian ([\[lagr\]](#lagr){reference-type="ref" reference="lagr"}) to the planar Skyrme model [@BB; @Bsk] suggests that the model can support extended stringlike solutions, which can be constructed from baby Skyrmions located in the plane transverse to the direction of the string [@Kobayashi:2013xoa]. Intuitively, the topological charge of such a configuration can be given by the product of the winding number of the planar Skyrmions and the number of the twists of the string in the extra spatial direction. Thus, the solutions we expect to find may in some way resemble the elastic rods that can bend, twist and stretch. Physically, field configurations of that type can be considered as a vortex, which is bended and twisted a few times [@Harland:2010wc]. Then the identification of the end points of the vortex yields the loop, which can transform itself into a knot to minimise its energy.

Another peculiar feature of the Faddeev-Skyrme model is that for a given degree $Q$, there are usually several different stable static soliton solutions of rather similar energy [@Sutcliffe:2007ui]. The number of solutions seems to grow with $Q$, thus the identification of a global minimum of the energy functional in a given sector becomes rather involved.

In the absence of the potential term the corresponding solutions are well known, they are constructed in the sectors of degrees up to $Q=29$ or even higher [@Sutcliffe:2007ui; @Jennings:2014mca]. In the model with the simple potential term, which breaks global $SO(3)$ symmetry [@Kundu:1982bc; @Foster:2010zb; @Harland:2013uk; @Battye:2013xf], the structure of the solutions of the massive Faddeev-Skyrme model is not very much different from the massless case. Note also the modification of the model via inclusion other 4th order on derivative terms does not change this pattern [@Gladikowski:1996mb].

It is known that the energy functional of the Faddeev-Skyrme model is bounded from below by the Vakulenko-Kapitanskii inequality [@Vakulenko:1979uw] $$E\ge c |Q|^{3/4}
\label{VK-bound}$$ where $c$ is a positive constant. However, this bound is modified if a potential term is included in the model [@Harland:2013rxa].

Note that the relation between the topological charge of the Hopfions and the energy is not linear as the Bogomolny-type bound in the Skyrme model. The physical reason of that is that the topological charge of Hopfions is produced via knotting of the vortex lines and/or their linking. This difference is important because the linear dependence between the topological charge and the energy means that the multisoliton configuration of degree $Q$ can be decomposed into set of $Q$ interacting solitons of unit charge and the interaction energy is vanishing as the individual solitons become infinitely separated. This is not the case for the soliton solutions of the usual Faddeev-Skyrme model.

Here we will consider the modification of the usual Faddeev-Skyrme model by an additional potential term $$\label{potential}
V=m^2\left(\phi_1\sin\alpha-(1-\phi_3)\cos\alpha\right)^2$$ where $m$ is a mass parameter and $\alpha\in [0,\pi]$ is an angular parameter. Depending on the value of this parameter the potential interpolates between the usual term, which explicitly breaks global $SO(3)$ symmetry [@Kundu:1982bc; @Foster:2010zb; @Harland:2013uk; @Battye:2013xf], as $\alpha=0$, and the Heisenberg type potential $$V=m^2{\phi_1}^2$$ as $\alpha=\pi/2$.

Potential of this form in the usual Skyrme model allows us to construct half-Skyrmion solutions [@Gudnason:2015nxa], as we will see in the Faddeev-Skyrme model it will also significantly affect the structure of the Hopfions. Note that the vacuum of the model with the potential ([\[potential\]](#potential){reference-type="ref" reference="potential"}) is a circle $S^1$ on the target space $S^2$ and the vacuum boundary condition remains the same, since $V\to 0$ as $\vec \phi\to \vec\phi_\infty = (0,0,1)$. Another remark is that the potential ([\[potential\]](#potential){reference-type="ref" reference="potential"}) can be equivalently written as $V=m^2(\phi_1-c)^2$ via an appropriate rotation of the fields in the internal space and by setting $c=\cos\alpha$. Also the corresponding vacuum boundary condition should be imposed.

Unlike Skyrmions, the location of the Hopfions cannot be identified with a maximum of the topological charge density distribution. Instead, it is convenient to look on the position of the maxima of the energy density. Since it costs a lot of energy to deviate from the vacuum $\vec \phi_\infty$, the corresponding curve usually follows the positions of the preimage of antipodal point $\vec\phi_0 = (0,0,-1)$. This curve is usually referred to as the position curve [@Sutcliffe:2007ui], considering the Hopfions most authors make use of it to visualize the shape of the configuration.

It is instructive to visualize the linking invariant via plotting not just the position curve but also another curve in its neighborhood, which allows us to see the Hopf charge as the linking number of these two curves. Actually, any other preimage curve of $\vec\phi$ will be linked with the preimage of $\vec\phi_0$ $Q$ times. In the absence of the symmetry breaking potential, or in the model with usual pion-mass type potential [@Foster:2010zb], it is convenient to define this linking curve as a tube given by an isosurface of the preimage of the vector $\vec \phi= (-1+\mu, 0, 0)$, where typically $\mu=0.1$. The linking number then is just the number of times the linking curve wraps around the position curve.

The situation is different however in the model ([\[lagr\]](#lagr){reference-type="ref" reference="lagr"}) with potential ([\[potential\]](#potential){reference-type="ref" reference="potential"}). Then, for the relatively large values of the mass parameter $m$ the location of the soliton can be identified as collection of curves of maximal energy, it interpolates between the preimages of antipodal point $\vec\phi
= (0,0,-1)$ as above for $\alpha=0$ to the loops, which follow the preimages of two distinct points $\vec\phi = (\pm 1,0,0)$, as $\alpha=\pi/2$: $\mathcal{C}_1 = \vec \phi^{-1}(1,0,0)$ and $\mathcal{C}_{-1} = \vec \phi^{-1}(-1,0,0)$. Since these loops are linked $Q$ times, the definition of the linking number now can be related with the positions of the preimages of these points: $Q= {\rm link} (\mathcal{C}_1,\mathcal{C}_{-1})$.

Note that the first two terms of the energy functional ([\[hopfenergy\]](#hopfenergy){reference-type="ref" reference="hopfenergy"}) are invariant with respect to global $SO(3)$ transformations. Thus, the internal rotations of the triplet $\vec \phi$ allow us to consider the limiting symmetry breaking potentials $V\sim{\phi_1}^2$, $\sim{\phi_2}^2$ and $\sim{\phi_3}^2$ all on equal footing.
