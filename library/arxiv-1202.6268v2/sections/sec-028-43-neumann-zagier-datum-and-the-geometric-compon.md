---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-028-43-neumann-zagier-datum-and-the-geometric-compon
section_title: "Neumann-Zagier datum and the geometric component"
section_number: 4.3
pages: 24-25
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.963
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sub.GE label="sub.GE"}

Let $M$ be a manifold with torus boundary and $\mathcal{T}$ a (combinatorial) ideal triangulation. The Neumann-Zagier datum $\beta_\mathcal{T}=(z,\mathbf A,\mathbf B)$ may be generalized for representations $\rho\in X_M$ besides the discrete faithful.

To begin, choose a representation $\rho:\pi_1(M)\longrightarrow\mathrm{PSL}(2,\mathbb C)$, and, if desired, a lift to ${\rm SL}(2,\mathbb C)$. Let $(\mu,\lambda)$ be meridian and longitude cycles

[^1]

on $\partial M$, and let $(m^{\pm 1},\ell^{\pm 1})$ be the eigenvalues of $\rho(\mu)$ and $\rho(\lambda)$, respectively. For example, for the lift of the discrete faithful representation to ${\rm SL}(2,\mathbb{C})$, we have $(m,\ell)=(1,-1)$ [@Calegari]. These eigenvalues define a map

$$\label{Amap} X_M \longrightarrow(\mathbb C^*)^2/\mathbb Z_2\,,$$

whose image is a curve $Y_M$, the zero-locus of the A-polynomial $A_M(\ell,m)=0$ [@CCGLS].

We will denote the representation $\rho$ as $\rho_m$ to emphasize its meridian eigenvalue.

Now, given a triangulation $\mathcal{T}$, and with $\mathbf A$, $\mathbf B$, and $\nu$ defined as in Section [\[sec.NZ\]](#sec.NZ){reference-type="ref" reference="sec.NZ"}, the gluing equations [\[glueeqs\]](#glueeqs){reference-type="eqref" reference="glueeqs"} can easily be deformed to account for $m\neq 1$. Namely, we find [@NZ]

$$\label{uglue} 
\prod_{j=1}^Nz_j{}^{\mathbf A_{ij}}z_j''{}^{\mathbf B_{ij}} = (-1)^{\nu_i} m^{2\delta_{iN}}\,.$$

The developing map [\[eq.dev\]](#eq.dev){reference-type="eqref" reference="eq.dev"} maps every solution of these equations to a representation $\pi_1(M)\longrightarrow\mathrm{PSL}(2,\mathbb C)$ with meridian eigenvalue $\pm m$. The triangulation $\mathcal{T}$ is $\rho_m$-regular if and only if $\rho_m$ is in the image of this map. We can similarly express the longitude eigenvalue as a product of shape parameters

$$\label{uglueL} 
\prod_{j=1}^N z_j{}^{2 C_j}z_j''{}^{2D_j} = (-1)^{2\nu_\lambda}\ell^2\,,$$

for some $2 C_j,2 D_j,2\nu_\lambda \in \mathbb Z$. Then, if $\mathcal{T}$ is a $\rho_m$-regular triangulation, the irreducible component of $Y_M$ containing $\rho_m$ is explicitly obtained by eliminating all shapes $z_j$ from [\[uglue\]](#uglue){reference-type="eqref" reference="uglue"}--[\[uglueL\]](#uglueL){reference-type="eqref" reference="uglueL"}.

In general, the shapes $z_j$ are algebraic functions on components of the variety $Y_M$. However, if $M$ is hyperbolic and $\mathcal{T}$ is regular for all but finitely many representations on the geometric component $Y_M^{\rm geom}$, then the shapes $z_j$ become rational functions, $z_j\in C(Y_M^{\rm geom})$. We provide a proof of this fact in Appendix [\[app.shapes\]](#app.shapes){reference-type="ref" reference="app.shapes"}. The field of functions $C(Y_M^{\rm geom})$ may be identified with $\mathbb Q(m)[\ell]/\big(A^{\rm geom}(\ell,m)\big)$, and the functions $z_j(\ell,m)$ can easily be obtained from equations [\[uglue\]](#uglue){reference-type="eqref" reference="uglue"}--[\[uglueL\]](#uglueL){reference-type="eqref" reference="uglueL"}.

[^1]: Recall again that these cycles are only canonically defined for knot complements. In general there is some freedom in choosing them, but the torsion depends in a predictable way on the choice, *cf.* [@Ya].
