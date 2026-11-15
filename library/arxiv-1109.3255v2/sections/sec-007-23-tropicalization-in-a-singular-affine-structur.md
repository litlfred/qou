---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-007-23-tropicalization-in-a-singular-affine-structur
section_title: "Tropicalization in a singular affine structure"
section_number: 2.3
pages: 17-19
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.986
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:tropicalization label="sec:tropicalization"}

Our goal is to find the same affine manifold $B$ (that comes from symplectic structure of $\CP^2\setminus D$) embedded in the base of the torus fibration on $X^\vee$, equipped with the *complex* affine structure. We shall see that it is obtained as a bounded chamber inside a particular tropical curve, the tropicalization of the fiber of $W$.

For some real number $\epsilon > 0$, consider the curve $W^{-1}(e^{\epsilon \Lambda})$: $$\label{eq:fiber-to-trop}
  W = u + \frac{e^{-\Lambda}v^2}{w} = e^{\epsilon \Lambda}$$ The tropicalization corresponds to the limit $\Lambda \to \infty$, or $t := e^{-\Lambda} \to 0$. The amoeba of $A(W^{-1}(t^{-\epsilon}))$ is the image of the curve in the affine base of the torus fibration on $X^\vee$. We want to produce a tropical curve in the base that reflects the asymptotic geometry of these amoebas $A(W^{-1}(t^{-\epsilon}))$ as $t \to 0$. In the standard situation, this is done by rescaling the amoebas by $\log t$ and taking the Hausdorff limit. Our situation is not standard because the affine manifold in which our tropical curve is to live has a singularity. Thus, none of the standard tropicalization techniques [@tropical-AG] apply directly. Since we do not know of any general theory of tropicalization when the affine structure is singular, we will here content ourselves with an ad hoc method involving explicit computation in two coordinate charts, and checking that the results fit together in the singular affine structure.

In the standard picture of tropicalization, one considers a family of subvarieties of an algebraic torus $V_t \subset (\C^*)^n$. The map $\Log: (\C^*)^n \to \R^n$ given by $\Log(z_1,\dots,z_n) =
(\log|z_1|,\dots,\log|z_n|)$ projects these varieties to their amoebas $\Log(V_t)$, and the rescaled limit of these amoebas is the tropicalization of the family $V_t$. The tropicalization is also given as the non-archimedean amoeba of the defining equation of $V_t$.

The map $\Log: (\C^*)^n \to \R^n$ is special Lagrangian fibration. Its fibers are the tori $\{|z_1| = r_1, \dots,|z_n| = r_n\}$. These tori are Lagrangian with respect to the standard symplectic form, and they are special with respect to the holomorphic volume form $$\label{eq:toric-vol-form}
  \Omega_{\text{toric}} = \frac{dz_1}{z_1} \wedge \cdots \wedge \frac{dz_n}{z_n},$$ which has logarithmic poles along the coordinate hyperplanes in $\C^n$. The complex affine coordinates are $\log |z_i|$.

The torus fibration on $X^\vee$ is approximated by this standard structure as follows. Equation [\[eq:vol-form-uw\]](#eq:vol-form-uw){reference-type="eqref" reference="eq:vol-form-uw"} shows that in the $(w,u)$ coordinates (where $u \neq 0$), the holomorphic volume form is standard. If the special Lagrangian fibration were also standard, the affine coordinates would be $(\log|w|,\log|u|)$. Proposition [\[prop:affine-coords\]](#prop:affine-coords){reference-type="ref" reference="prop:affine-coords"} shows that, while $\eta = \log|w|$ is still an affine coordinate (reflecting the fact that there is still an $S^1$-symmetry), the other affine coordinate $\xi$ is the average value of $\log|u|$ along a loop in the fiber. We also see that as $|\lambda|$ becomes large, the approximation $\xi \approx \log|u|$ holds with increasing accuracy. Similarly, in the $(w,v)$ coordinates (when $v \neq 0$), the holomorphic volume form is standard, and $\eta
= \log|w|$ and $\psi \approx \log|v|$ form affine coordinates.

We shall see that as $t = e^{-\Lambda} \to 0$, the amoebas $A(W^{-1}(t^{-\epsilon}))$ move farther away from the singularity, where the approximations $\xi \approx \log|u|$ and $\psi \approx
\log|v|$ hold with increasing accuracy, while $\eta = \log|w|$ holds exactly everywhere.

The approximations $\xi \approx \log|u|$ and $\psi \approx \log|v|$ and the identity $\eta = \log|w|$ suggest the approach to finding the tropicalization. We represent the equation $W = u + e^{-\Lambda}v^2/w = e^{\epsilon \Lambda}$ as a polynomial equation in the coordinates $(w,u) \in (\C^*)^2$. We then compute the corresponding tropical curve, using the standard procedures [@tropical-AG], and we plot the result in the affine plane whose coordinates are $(\log|w|, \log|u|)$. This is shown in Figure [1](#fig:tropical-fiber){reference-type="ref" reference="fig:tropical-fiber"}(a). We repeat the process in the coordinate system $(w,v)$, and plot the resulting tropical curve in the affine plane whose coordinates are $(\log|w|, \log|v|)$. This is shown in Figure [1](#fig:tropical-fiber){reference-type="ref" reference="fig:tropical-fiber"}(b). We then transfer these tropical curves into the singular affine manifold by simply identifying $\xi$ with $\log|u|$ and $\psi$ with $\log|v|$.

We now observe that the two curves actually match up, at least away from the vertical line passing through the singularity, and we claim that the result is as depicted in Figure [1](#fig:tropical-fiber){reference-type="ref" reference="fig:tropical-fiber"}(c). This is evident in comparing the left-hand portions of parts (a) and (b) of Figure [1](#fig:tropical-fiber){reference-type="ref" reference="fig:tropical-fiber"}. On the right-hand portion, we must take into account that the coordinate $\psi \approx \log|v|$ has been affected by a shear in passing from (b) to (c).

There is apparently a problem along the vertical line passing through the singularity, since the curves depicted in (a) and (b) have vertical legs there, which we claim do not appear in (c). Our reasoning is this: the coordinate system $(w,u) \in (\C^*)^2$ only covers the locus where $u \neq 0$, which is also where the function $\xi$ is well defined. Thus we cannot expect the curve in (a) to be valid near the vertical going down from the singularity, it is valid above the singularity. Conversely, the figure in (b) is only valid in the region below the singularity. Thus the extra vertical legs are illusory.

We call the resulting tropical curve $T_\epsilon$.

::: proposition
[]{#prop:tropical-fiber label="prop:tropical-fiber"} For $\epsilon > 0$, $T_\epsilon$ is a trivalent graph with two vertices, a cycle of two finite edges, and two infinite edges.
:::

![The tropical fiber of $W$ for $\epsilon > 0$. (a) $(w,u)$ coordinates. (b) $(w,v)$ coordinates. (c) The tropical fiber $T_\epsilon$.](tropical-fiber){#fig:tropical-fiber width="5.75in"}

::: proposition
[]{#prop:tropical-fiber-chamber label="prop:tropical-fiber-chamber"} For $\epsilon > 0$, the complement of $T_\epsilon$ has a bounded component that is an integral affine manifold with singularities that is isomorphic, after rescaling, to the base $B$ of the special Lagrangian fibration on $\CP^2 \setminus D$ with the affine structure coming from the symplectic form.
:::

::: remark
The topology of the tropical curve $T_\epsilon$ corresponds to that of a twice-punctured elliptic curve.
:::

::: remark
We can apply the same patching procedure for $\epsilon$ in the range $(-1/3) < \epsilon < 0$. This changes Figure [1](#fig:tropical-fiber){reference-type="ref" reference="fig:tropical-fiber"} so that the triangles in (a) and (b) become smaller and they lie entirely below point marked with $\times$. Thus, assuming that (a) is valid above the singularity, while (b) is valid below the singularity, we find that $T_\epsilon$ is essentially the same as what appears in (b), but that the vertical leg must terminate at the singularity, in order to be consistent with the fact that in (a) no part of the curve appears above the singularity. Thus we find that $T_\epsilon$ is a trivalent graph with three vertices, a cycle of three finite edges, two infinite edges and one edge connecting a vertex to the singular point of the affine structure.

We note that the value $\epsilon = -1/3$ corresponds to the critical values of $W$.
:::

::: remark
This proposition is another case of the phenomenon, described in Abouzaid's paper [@abouzaid06], that for toric varieties, the bounded chamber of the fiber of the superpotential is isomorphic to the moment polytope. In the general case of a manifold $X$ with effective anticanonical divisor $D$, the boundary of the symplectic affine base of the torus fibration on $X\setminus D$ corresponds to a torus fiber collapsing onto $D$, a particular class of holomorphic disks having vanishing area, and the corresponding term of the superpotential having unit norm. On the other hand, the tropicalization of the fiber of the superpotential has some parts corresponding to one of the terms having unit norm, and it is expected that these bound a chamber which is isomorphic to the base of the original torus fibration.
:::
