---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-020-51-the-tetrahedron
section_title: "The tetrahedron"
section_number: 5.1
pages: 42-44
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.942
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
Now, let us illustrate this in a few concrete examples, starting with the theory $T_{\Delta,\Pi_Z}$ that we associate to a single tetrahedron. The theory $T_{\Delta,\Pi_Z}$ is a single chiral multiplet $\phi_Z$ coupled to a $U(1)$ background gauge field that also has a (supersymmetric) Chern-Simons interaction at level $-\tfrac{1}{2}$. On a circle of finite radius $\beta$, this theory has the effective twisted superpotential (*cf.* [@Nek-5d; @LN; @NS-I; @DG-Sdual])

$$T_{\Delta,\Pi_Z}\;:\quad \widetilde{\mathcal{W}}_{{\rm eff}} (Z) \; = \; {\rm Li}_2(e^{-Z}) = {\rm Li}_2(z^{-1})\,, \label{CWT1}$$

where

$$Z := \beta\,\tilde m_Z$$

is proportional to the twisted mass in the 2d background gauge multiplet (which contains the real mass $m_Z={\rm Re}(\tilde m_Z)$ of the 3d chiral $\phi_Z$). Note that the superpotential [\[CWT1\]](#CWT1){reference-type="eqref" reference="CWT1"} includes an infinite tower of Kaluza-Klein modes on the circle $S^1$, which have been re-summed.

According to [\[uidef\]](#uidef){reference-type="eqref" reference="uidef"} the effective complexified FI parameter in the IR is given by $$Z'' = \frac{\partial \widetilde{\mathcal{W}}_{{\rm eff}}}{\partial Z'} = \log(1-e^{-Z})$$ The relation between $Z$ and $Z''$ can be conveniently written as

$$\label{Aone}
\mathcal{M}_{\rm SUSY}^{\rm (param)} ~:~\quad
e^{Z''} + e^{-Z} -1=z''+z^{-1}-1=0\,,$$

and, as promised, describes a nice algebraic curve in the variables [\[lmviauv\]](#lmviauv){reference-type="eqref" reference="lmviauv"}. This is precisely the curve [\[LDelta\]](#LDelta){reference-type="eqref" reference="LDelta"} that describes the space of $SL(2,{\mathbb C})$ structures on a tetrahedron. Hence, we just verified [\[MMclaim\]](#MMclaim){reference-type="eqref" reference="MMclaim"} in a basic example of a tetrahedron and its gauge theory counterpart $T_{\Delta,\Pi_Z}$:

$$\mathcal{L}_{\Delta} \; = \; \mathcal{M}_{{\rm SUSY}}^{\rm (param)} (T_{\Delta,\Pi_Z})\,.$$

Equation [\[Aone\]](#Aone){reference-type="eqref" reference="Aone"} appears to allow any value of the twisted mass $Z$ (given appropriate FI parameter $Z''$) except $Z=0$. At $Z=0$, we hit a singular point, where it looks like the FI parameter must run off to infinity to preserve supersymmetry. This can be understood directly in the gauge theory: at $Z=0$ the chiral field $\phi_Z$ is massless, and hence we were not supposed to integrate it out. The effective description of a gauge theory theory with massive vacua breaks down there.

Had we chosen any other polarization for the tetrahedron theory, say $\Pi'=g\circ \Pi_Z$ with position $X$ and momentum $P$ such that

$$\begin{pmatrix} X\\P \end{pmatrix} = \begin{pmatrix}a & b\\ c & d\end{pmatrix} \begin{pmatrix}Z\\Z''\end{pmatrix}\,,$$

the Lagrangian [\[Aone\]](#Aone){reference-type="eqref" reference="Aone"} would be mapped to the isomorphic curve

$$p^ax^{-c}+p^b x^{-d}-1 = 0\,.$$

As a beautiful example of this behavior, we can consider the particular transformation

$$\sigma\;:\quad \begin{pmatrix}Z\\Z''\end{pmatrix}\mapsto
\begin{pmatrix}Z'\\Z\end{pmatrix}= \begin{pmatrix}-1 & -1\\ 1 & 0\end{pmatrix} \begin{pmatrix}Z\\Z''\end{pmatrix} + \begin{pmatrix} i\pi \\ 0 \end{pmatrix}\,, \label{sST}$$

which is an affine extension of $ST = \big(\begin{smallmatrix} -1 & -1\\ 1 & 0\end{smallmatrix}\big)\in SL(2,{\mathbb Z})$ that generates the triality symmetry [\[STonT1\]](#STonT1){reference-type="eqref" reference="STonT1"}. (Note that, just like $ST$ itself, $\sigma$ satisfies $\sigma^3 = id$.)

From the general $Sp(2N,{\mathbb Z})$ action on theories $T_{M,\Pi}$ [\[Sp2T\]](#Sp2T){reference-type="eqref" reference="Sp2T"}--[\[Sp2GL\]](#Sp2GL){reference-type="eqref" reference="Sp2GL"}, it is easy to see how the twisted superpotentials $\widetilde\mathcal{W}_{\rm eff}$ on ${\mathbb R}^2\times S^1$ should transform. For example, the element $T$ adds a level 1 Chern-Simons term $\frac1{4\pi}\int d^4\theta \,\Sigma_ZV_Z$ to the Lagrangian of $T_{\Delta,\Pi_Z}$, which descends (with proper normalization) to

$$T\;:\quad \widetilde\mathcal{W}_{\rm eff}(Z) \;\mapsto\; \widetilde\mathcal{W}_{\rm eff}'(Z)=\widetilde\mathcal{W}_{\rm eff}(Z) + \frac12 Z^2\,.$$

Similarly, $S$ adds a mixed Chern-Simons term $\frac1{2\pi}\int d^4\theta\,\Sigma_{Z'}V_Z$ and makes $V_Z$ dynamical. Since we now should extremize with respect to $Z$, this must act as a Legendre transform,

$$S\;:\quad \widetilde\mathcal{W}_{\rm eff}(Z) \;\mapsto\; \widetilde\mathcal{W}_{\rm eff}'(Z') = \left[\widetilde\mathcal{W}_{\rm eff}(Z)+Z'Z \right]_{\frac{\partial}{\partial Z}=0}\,.$$

Finally, we have affine shifts. While these were unimportant for defining Lagrangians on ${\mathbb R}^3$, the do show up in the theory on ${\mathbb R}^2\times S^1$. Namely, shifts by $i\pi$ in "position" and "momentum" coordinates appear as half-integral shifts in Wilson loops and theta angles, respectively. Thus, for the tetrahedron theory on ${\mathbb R}^2\times S^1$, it is the affine $\sigma$ in [\[sST\]](#sST){reference-type="eqref" reference="sST"} that implements mirror symmetry,

$$\sigma \circ T_{\Delta,\Pi_Z} \,\simeq\, T_{\Delta,\Pi_Z}\,,$$

rather than simply $ST$

Putting together the above ingredients, we find that

$$\sigma\;:\quad \widetilde\mathcal{W}_{\rm eff}(Z)\;\mapsto\; \widetilde\mathcal{W}_{\rm eff}'(Z') \equiv \left[\widetilde\mathcal{W}_{\rm eff}(Z)+\frac12 Z^2+(Z'-i\pi)Z\right]_{\frac{\partial}{\partial Z}=0}\,.$$

Setting $Z=\partial\widetilde\mathcal{W}_{\rm eff}(Z') /\partial Z'$ and exponentiating, we obtain

$$\mathcal{M}_{\rm SUSY}^{\rm (param)}(T_{\Delta,\Pi_{Z'}})\;:\quad z+z'{}^{-1}-1=0\,.$$

As expected, this transformation leaves the moduli space invariant.
