---
doc_id: arxiv-hep-th-0205308v2
doc_title: "WDVV Equations as Functional Relations"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0205308v2.pdf
source_sha256: 2de5a4f40d80174c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.932
doc_brief: "WDVV Equations as Functional Relations — 6 sections: Front matter; Introduction; WDVV and dispersionless Hirota equ"
---
The associativity or Witten-Dijkgraaf-Verlinde-Verlinde (WDVV) equations [@WDVV] have been widely discussed in connection with various problems of mathematical physics for over ten years. They have arisen in the context of quantum cohomologies and mirror symmetry, and also with regard to multidimensional supersymmetric gauge field theories. In their most general form these equations may be expressed as [@MMM] $$\label{WDVV}
{\sf F}_i\cdot {\sf F}_j^{-1}\cdot{\sf F}_k = {\sf F}_k\cdot {\sf F}_j^{-1}\cdot{\sf F}_i
\qquad \forall i,j,k.$$ Here the matrices $\|{\sf F}_i\|_{jk} \equiv {\cal F}_{ijk}$ are constructed from the third derivatives of the function ${\cal F}({\bf a})$, $$\label{thirdder}
{\cal F}_{ijk} =\dfrac{\partial^3{\cal F}}{\partial a\sp{i}\,\partial a\sp{j}\,\partial a\sp{k}}.$$ When ${\cal F}$ is a function of one or two variables then ([\[WDVV\]](#WDVV){reference-type="ref" reference="WDVV"}) are empty: that is they are satisfied by any function. For more variables however, despite the simplicity of their compact matrix form, these equations form a highly nontrivial overdetermined system of nonlinear partial differential equations satisfied by the function ${\cal F}$.

In their original two-dimensional topological field theoretic setting the WDVV equations ([\[WDVV\]](#WDVV){reference-type="ref" reference="WDVV"}) were supplemented by a further constraint: there was a distinguished coordinate such that the matrix ${\cal F}_{1jk}$ was a constant. This came from the existence of a distinguished operator, the identity operator $\Phi_1$, and the third derivatives of ${\cal F}$ being related to three-point functions via $\langle \Phi_i\Phi_j\Phi_k\rangle=  {\cal F}_{ijk}$. This distinguished coordinate meant their was a preferred "metric", ${\sf F}_1$. Associated with this class of solutions to ([\[WDVV\]](#WDVV){reference-type="ref" reference="WDVV"}) -- together with a quasi-homogeneity condition -- Dubrovin introduced the notion of Frobenius manifold [@Dub]. However, there are physically interesting solutions of ([\[WDVV\]](#WDVV){reference-type="ref" reference="WDVV"}) that fail to possess these extra properties and for these the notion of Frobenius manifold fails to encapsulate their geometry.

This more general class of solutions to ([\[WDVV\]](#WDVV){reference-type="ref" reference="WDVV"}) includes some prepotentials arising from low-energy effective actions of ${\cal N}=2$ supersymmetric gauge theories in four dimensions via Seiberg-Witten theory. Supersymmetry typically restricts the possible *geometries* encountered in field theories. Thus sigma models have target spaces that are Riemannian, or possibly Kähler or hyper-Kähler depending on the number of supersymmetry generators. For ${\cal N}=2$ SUSY gauge theories the moduli space of vector multiplets is a special[^1] Kähler manifold [@speKa; @SW]. This means that on the moduli space there exists a single *holomorphic* function ${\cal F}({\bf a})$ whose second derivatives $$\label{pematr}
T_{ij} =\dfrac{\partial^2{\cal F}}{\partial a\sp{i}\,\partial a{\sp{j}}}$$ determines the metric via $$\label{metric}
ds\sp2= g_{i{\bar j}}\,d a\sp{i} d\overline{ a\sp{j}},\qquad
g_{i{\bar j}}=\dfrac{1}{2}({\rm Im}T)_{ij}.$$ Here $a\sp{i}$ are complex coordinates on the Kähler manifold (and $\overline{ a\sp{j}}$ their complex conjugates). The connection with Seiberg-Witten theory is that the second derivatives $T_{ij}$ coincide with the matrix elements of the period matrix of the Seiberg-Witten auxiliary curve and ${\cal F}$ is the prepotential. In [@GKMMM] it was argued that this auxiliary curve could be identified with the spectral curve of a completely integrable system. Indeed, the phase space of (appropriate algebraically) completely integrable systems can be identified as a toric fibration (the angles $x\sp{i}$) over a special Kähler manifold (the actions $y_j$). The Kähler form is then $$\label{kform}
\omega=dx\sp{i}\wedge dy_i
=\dfrac{\sqrt{-1}}{2}\, ({\rm Im}T)_{ij}\, d a\sp{i}\wedge d\overline{ a\sp{j}},$$ and the real coordinates $\{x\sp{i},y_j\}$ are related to complex coordinates by $$\dfrac{\partial}{\partial a\sp{i}}=\dfrac{1}{2}\bigg(\dfrac{\partial}{\partial x\sp{i}}
-T_{ij}\, \dfrac{\partial}{\partial y_{j}}\bigg).$$ The Kähler potential here is $K({\bf a}, {\bf\bar a})=\frac{1}{2}\bigg(\overline{ a\sp{i}}\,\dfrac{\partial{\cal F}}
{\partial a\sp{i}}\bigg)$. A special Kähler manifold has two natural connections associated with it. There is the Levi-Civita connection $D$, with Christoffel symbols $\Gamma_{{\bar i}jk}=-\frac{\sqrt{-1}}{4}{\cal F}_{ijk}$, and there is also a flat torsionfree connection $\nabla= D+A$ such that $\nabla d x\sp{i}=0
=\nabla d y_{j}$. Here the connection $A$, $$\label{connection}
A\bigg(\dfrac{\partial}{\partial a\sp{i}}\bigg)=\big(A_j\big)\sp{\bar l}_{\ i}\,
d a\sp{j}\otimes \dfrac{\partial}{\partial\overline{ a\sp{l}}}
=\dfrac{\sqrt{-1}}{4}\, \bigg(g\sp{{\bar l}m} {\cal F}_{jim}\bigg)\,
d a\sp{j}\otimes \dfrac{\partial}{\partial\overline{ a\sp{l}}},$$ satisfies $0=\partial\sp{D} A=\partial A+\Gamma\wedge A-A\wedge \Gamma$. Because the Levi-Civita connection connection is torsionfree we may also write this as $D_i A\sp{\bar l}_{\, jk}=D_j A\sp{\bar l}_{\, ik}$ with $A\sp{\bar l}_{\, jk}=(A_j)\sp{\bar l}_{\ k}$. We refer to [@mars; @brkr] for further material on the connections between Seiberg-Witten theory and integrable systems.

Following the work of [@GKMMM], it seemed to be very important that the function ${\cal F}$ satisfied some well-known nonlinear integrable differential equations. The connection between Seiberg-Witten theory and the WDVV equations is that *some* prepotentials lead to solutions of ([\[WDVV\]](#WDVV){reference-type="ref" reference="WDVV"}). Certainly not all prepotentials yield solutions and a characterisation of what special Kähler manifolds give solutions is still sought. Now the geometric origin of the WDVV equations in Seiberg-Witten theory appears to be completely different from that of Frobenius manifolds. Seiberg-Witten theory lacks the analogue of the identity operator and constant "topological metric". Indeed there appears no obvious connection between the (nonholomorphic) metric of special Kähler geometry, built out of second derivatives of the prepotential, and the "topological metric" ${\sf F}_1$ of the Frobenius manifolds which is a third derivative. Further, the WDVV equations were shown to be covariant with respect to arbitrary symplectomorphisms in [@dWM], which is quite natural in the special Kähler setting, but such do *not* preserve the Frobenius manifold structure.

The geometric origin underlying the WDVV equations has yet be clarified. In this note we will reformulate these equations as functional relations. In particular, they will be in terms of second derivatives. These functional relations are reminiscent of the Hirota equations and we will give an example making this clearer.

[^1]: In the original supergravity context such a manifold was called "rigid special Kähler\" with "special Kähler\" referring to the local (supergravity) setting; since [@Freed] the local setting is often known by "projective special Kähler\". See [@cortes] for a survey of these manifolds.
