---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-003-13-the-1-loop-invariant
section_title: "The 1-loop invariant"
section_number: 1.3
pages: 5-6
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.929
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sub.1loopdef label="sub.1loopdef"}

::: definition
[]{#def.1loopdef label="def.1loopdef"} Given a one-cusped hyperbolic manifold $M$ with regular ideal triangulation $\mathcal{T}$ and enhanced Neumann-Zagier datum $\widehat\beta_\mathcal{T}$ we define:

$$\qquad\tau_{\mathcal{T}} := 
\pm \frac12\det\big(\mathbf A\Delta_{z''}
+\mathbf B\Delta_z^{-1}\big)z^{f''}z''^{-f}
\quad\in\,E_M/\{\pm 1\}\,,
\label{torintro}$$

where $\Delta_z:=\text{diag}(z_1,...,z_N)$ and $\Delta_{z''}:=\text{diag}(z_1'',...,z_N'')$ are diagonal matrices, and $z^{f''}z''^{-f} := \prod_i z_i{}^{f''_i}z''_i{}^{-f_i}$.
:::

Note that $\tau_{\mathcal{T}}$ takes value in the invariant trace field of $M$ and is only defined up to a sign. In Section [\[sec.torsion\]](#sec.torsion){reference-type="ref" reference="sec.torsion"} we will show that

::: theorem
[]{#thm.indep label="thm.indep"} $\tau_{\mathcal{T}}$ is independent of the quad type of $\mathcal T$, the chosen edge of $\mathcal T$, the choice of a meridian loop, and the choice of a combinatorial flattening.
:::

We now consider the dependence of $\tau_{\mathcal{T}}$ on the choice of a regular ideal triangulation of $M$. It is well known that the set $\mathcal X$ of ideal triangulations of a cusped hyperbolic manifold is non-empty [@Ca] and connected by 2--3 moves [@Ma1; @Ma2; @Pi]. That is, a sequence of 2--3 moves can be used to take any one ideal triangulation to any other. The subset $\mathcal X_{\rho_0}$ of $\mathcal X$ of regular triangulations is also non-empty, see Section [\[sec.extensions\]](#sec.extensions){reference-type="ref" reference="sec.extensions"}. Topologically, these are the triangulations without any univalent edges [@Champanerkar; @BDR-V; @DnG; @Till]. We will prove in Section [\[sec.torsion\]](#sec.torsion){reference-type="ref" reference="sec.torsion"} that

::: theorem
[]{#thm.1 label="thm.1"} $\tau_{\mathcal{T}}$ is constant on every component of $\mathcal X_{\rho_0}$ connected by 2--3 moves.
:::
