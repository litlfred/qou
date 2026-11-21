---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-026-41-a-review-of--regular-ideal-triangulations
section_title: "A review of -regular ideal triangulations"
section_number: 4.1
pages: 23-23
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.851
latex_coverage_ratio: 0.981
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sub.revrho label="sub.revrho"}

In this section we discuss the $\rho$-regular ideal triangulations that are needed to generalize our torsion invariant. Let $M$ denote a 3-manifold with nonempty boundary and let $\rho: \pi_1(M)\longrightarrow\mathrm{PSL}(2,\mathbb C)$ be a $\mathrm{PSL}(2,\mathbb C)$ representation of its fundamental group. Let $\mathcal X$ denote the set of combinatorial ideal triangulations $\mathcal T$ of $M$. Matveev and Piergallini independently showed that every two elements of $\mathcal X$ with at least two ideal tetrahedra are connected by a sequence of 2-3 moves (and their inverses) [@Ma1; @Pi]. For a detailed exposition, see [@Ma2; @BP].

Given an ideal triangulation $\mathcal T$, let $V_{\mathcal T}$ denote the affine variety of non-degenerate solutions (i.e., solutions in $\mathbb C\setminus\{0,1\}$) of the gluing equations of $\mathcal T$ corresponding to its edges. There is a developing map $$\label{eq.dev}
V_{\mathcal T} \longrightarrow X_M\,,$$ where $X_M:=\mathrm{Hom}(\pi_1(M),\mathrm{PSL}(2,\mathbb C))/\mathrm{PSL}(2,\mathbb C)$ denotes the affine variety of all $\mathrm{PSL}(2,\mathbb C)$ representations of $\pi_1(M)$.

::: definition
[]{#def.rhoregular label="def.rhoregular"} Fix a $\mathrm{PSL}(2,\mathbb C)$-representation of $M$. We say that $\mathcal T\in \mathcal X$ is $\rho$-*regular* if $\rho$ is in the image of the developing map [\[eq.dev\]](#eq.dev){reference-type="eqref" reference="eq.dev"}.
:::

Let $\mathcal X_\rho \subset \mathcal X$ denote the set of all $\rho$-regular ideal triangulations of $M$. When $M$ is hyperbolic, let $\rho_0$ denote its discrete faithful representation $\rho_0$ and let $X^{\mathrm{geom}}_M \subset X_M$ denote the geometric component of its character variety [@Th; @NZ]. We then have the following result.

::: lemma
[]{#lem.wellknown label="lem.wellknown"} (a) $\mathcal T\in \mathcal X_{\rho_0}$ if and only if $\mathcal T$ has no homotopically peripheral (*i.e.*, univalent) edges. (b) If $\mathcal T\in \mathcal X_{\rho_0}$, then $\mathcal T\in \mathcal X_{\rho}$ for all but finitely many $\rho \in X^{\mathrm{geom}}_M$.
:::

::: proof
*Proof.* Part (a) has been observed several times; see [@Champanerkar], [@BDR-V Sec.10.3], [@Till Thm.2.3] and also [@DnG Rem.3.4]. For part (b), fix $\mathcal T\in \mathcal X_{\rho_0}$. Observe that $\mathcal T$ is $\rho$-regular if the image of every edge

[^1]

of $\mathcal T$ under $\rho$ does not commute with the image under $\rho$ of the peripheral subgroup of $M$. This is an algebraic condition on $\rho$, and moreover, when $\rho \in X^{\mathrm{geom}}_M$ is analytically nearby $\rho_0$, the condition is satisfied. It follows that the set of points of $X^{\mathrm{geom}}_M$ that satisfy the above condition is Zariski open. On the other hand, $X^{\mathrm{geom}}_M$ is an affine curve [@Th; @NZ]. It follows that $\mathcal T$ is $\rho$-regular for all but finitely many $\rho \in  X^{\mathrm{geom}}_M$. ◻
:::

[^1]: Note that every edge can be completed to a closed loop by adding a path on the boundary $T^2$. The choice of completion does not matter for studying commutation with the peripheral subgroup.
