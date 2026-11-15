---
doc_id: arxiv-1910.09966v1
doc_title: "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics"
section_id: sec-009-42-from-immersed-surfaces-in-k3-surfaces-to-ferm
section_title: "From Immersed Surfaces in K3 Surfaces to Fermions and Knot Complements"
section_number: 4.2
pages: 15-16
source_pdf: 1910.09966v1.pdf
source_sha256: 21798500c98ed25a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 1.0
doc_brief: "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics — In this paper, we will describe a topological model for elementary par- ticles based on 3-manifolds."
---
In the previous subsection, we described a relation between the octonions and a system of eight intersecting surfaces in the K3 surface. In this system of surfaces, every surface has two self-intersections (the diagonal of the matrix ([\[eq:E8-matrix\]](#eq:E8-matrix){reference-type="ref" reference="eq:E8-matrix"})). Therefore, every surface is not embedded but immersed in the K3 surface. For immersed surfaces, there is a whole theory, called Weierstrass representation, with a close connection between immersed surfaces and spinors. The following discussion is borrowed from [@AsselmeyerRose2012], and we will present it here again for completeness. First, we start with the immersion $I:\Sigma\to\mathbb{R}^{3}$ of a surface $\Sigma$ into $\mathbb{R}^{3}$. This immersion $I$ can be defined by a spinor $\varphi$ on $\Sigma$ fulfilling the Dirac equation $$D\varphi=H\varphi,\label{eq:2D-Dirac}$$ with $|\varphi|^{2}=1$ (or an arbitrary constant) (see Theorem 1 of [@Friedrich1998]). A spinor bundle over a surface splits into two sub-bundles $S=S^{+}\oplus S^{-}$, representing spinors of different helicity, with the corresponding splitting of the spinor $\varphi$ in components $$\varphi=\left(\begin{array}{c}
\varphi^{+}\\
\varphi^{-}
\end{array}\right),$$ and we have the Dirac equation $$D\varphi=\left(\begin{array}{cc}
0 & \partial_{z}\\
\partial_{\bar{z}} & 0
\end{array}\right)\left(\begin{array}{c}
\varphi^{+}\\
\varphi^{-}
\end{array}\right)=H\left(\begin{array}{c}
\varphi^{+}\\
\varphi^{-}
\end{array}\right)$$ with respect to the coordinates $(z,\bar{z})$ on $\Sigma$. In dimension 3, the spinor bundle has the same fiber dimension as the spinor bundle $S$ (but without a splitting $S=S^{+}\oplus S^{-}$into two sub-bundles). Now, we define the extended spinor $\phi$ over the 3-torus $\Sigma\times[0,1]$ via the restriction $\phi|_{T^{2}}=\varphi$. The spinor $\phi$ is constant along the normal vector $\partial_{N}\phi=0$ fulfilling the three-dimensional Dirac equation $$D^{3D}\phi=\left(\begin{array}{cc}
\partial_{N} & \partial_{z}\\
\partial_{\bar{z}} & -\partial_{N}
\end{array}\right)\phi=H\phi\label{eq:Dirac-equation-3D}$$ induced from the Dirac equation ([\[eq:2D-Dirac\]](#eq:2D-Dirac){reference-type="ref" reference="eq:2D-Dirac"}) via restriction and where $|\phi|^{2}=const.$ In this picture, we shift the description from surfaces to 3-manifolds. The description above showed that the essential information is contained in the surface, but fermions are at least three-dimensional objects: fermions and bosons appear beginning with dimension 3 (irreducible representation of the group $SO(3)$ as given by the lift to $SU(2)$). In dimension 2, we have anyons with a spin of any rational number. However, how did we get the corresponding 3-manifold representing the fermion?

To answer this question, we consider the branched covering of the K3 surface $M$. As explained above, it must be a 4-fold covering $M\to S^{4}$ branched along a surface with singularities of two types cusp and fold. The cusp can be described as a cone over the trefoil knot, whereas the fold is the cone over the Hopf link (see Figure 9 in [@PiergalliniZuddas2018]). Now, we consider a 4-manifold with boundary, for instance by cutting out a 4-disk $D^{4}$ form $M$ to get 4-manifold $M\setminus D^{4}$ with boundary $\partial(M\setminus D^{4})=S^{3}$, the 3-sphere. Then, the branched covering of $M$ induced a branched covering of the boundary $\partial M$, so that the branching set of $M$, a surface, induces a branching set of $\partial M$, a knot or link. In our case, the singularities of the surface (cusp and fold) given as cones over the trefoil knot and Hopf link will correspond to the trefoil knot and Hopf link in the 3-sphere. Then, the branched covering is given by the mappings of the complements $S^{3}\setminus\left\{ trefoil\right\}$ and $S^{3}\setminus\left\{ Hopf-link\right\}$ to the permutation group $S_{3}$. We see the appearance of these two complements as a sign to use these structures as particles and interactions. The complement of the knot is a 3-manifold with one boundary component. In contrast, the complement of the link looks like a cylinder $T^{2}\times[0,1]$ which can connect two knot complements. Therefore, we have the conjecture that knot complements are fermions and link complements are bosons.
