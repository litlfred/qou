---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-037-appendix-a-not-approximating-the-trivial-represe
section_title: "Appendix A Not approximating the trivial representation"
section_number: null
pages: 44-45
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.984
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
[]{#sec:notapprox label="sec:notapprox"}

For a manifold $M^3$ there are components of $X(M^3,\mathrm{PSL}_2(\mathbb{C}))$ that consist of characters of abelian representations. When $b_1(M^3)=1$ those components are curves, and their union is denoted by $$X^{ab}(M^3,\mathrm{PSL}_2(\mathbb{C})).$$ The number of components of $X^{ab}(M^3,\mathrm{PSL}_2(\mathbb{C}))$ depends on the torsion of $H_1(M^3;\mathbb{Z})$.

Being irreducible is a Zariski open property for a character [@CullerShalen83]. On the other hand, every reducible character is also the character of an abelian representation. This yields that $X^{ab}(M^3,\mathrm{PSL}_2(\mathbb{C}))$ are precisely the components consisting only of reducible characters.

::: lemma
[]{#lem:singlecomponent label="lem:singlecomponent"} Assume that $b_1(M^3)=1$. Then the trivial character belongs to a single irreducible component of $X(M^3,\mathrm{PSL}_2(\mathbb{C}))$, which is one of the curves of $X^{ab}(M^3,\mathrm{PSL}_2(\mathbb{C}))$.
:::

::: cor
If $b_1(M^3)=1$, then the trivial character does not belong to $X_0(M^3,\mathrm{PSL}_2(\mathbb{C}))$.
:::

::: proof
*Proof of Lemma [\[lem:singlecomponent\]](#lem:singlecomponent){reference-type="ref" reference="lem:singlecomponent"}.* The proof uses the projection $$\label{eqn:proj}
    \begin{array}{rcl}
     \pi\colon \hom(\pi_1 M^3,\mathrm{PSL}_2(\mathbb{C})) & \to & X(M^3,\mathrm{PSL}_2(\mathbb{C})) \\
     \rho & \mapsto &\chi_\rho
    \end{array}$$ and the dimension of its fibre. For the trivial character $\chi_0$, a representation $\rho\in \pi^{-1}(\chi_0)$ is conjugate to $$\label{eqn:rhoab}
  \rho(\gamma)= \pm \begin{pmatrix}
                 1 & h(\gamma) \\
                 0 & 1
                \end{pmatrix},
                \qquad \forall \gamma\in\pi_1M^3,$$ where $h\colon \pi_1M^3\to\mathbb{C}$ is a group homomorphism. (Not to be confused with the cusp shape of peripheral representations, as $h$ is defined in the whole group $\pi_1M^3$.) Conjugating the representation [\[eqn:rhoab\]](#eqn:rhoab){reference-type="eqref" reference="eqn:rhoab"} by a diagonal matrix means replacing the morphism $h$ by a multiple. Thus, as $b_1(M^3)=1$, there are only two orbits by conjugation in $\pi^{-1}(\chi_0)$: the trivial and the non-trivial morphism $h\colon \pi_1M^3\to\mathbb{C}$. By looking at the dimension of the stabilizers, these orbits have dimension either 0 (for $h$ trivial) or 2 (for $h$ non-trivial). Hence the dimension of $\pi^{-1}(\chi_0)$ is 2. On the other hand, on components $Y$ of $X(M^3,\mathrm{PSL}_2(\mathbb{C}))$ that contain irreducible representations, the generic dimension of $\pi^{-1}$ is 3, the dimension of $\mathrm{PSL}_2(\mathbb{C})$. Since this dimension is upper semi-continuous, the trivial character cannot belong to an irreducible component of $X(M^3,\mathrm{PSL}_2(\mathbb{C}))$ that contains irreducible characters. Hence it must belong to a component whose characters are all reducible. ◻
:::

::: lemma
[]{#lemma:acyclicorbit label="lemma:acyclicorbit"} Let $\rho_1,\rho_2\in\hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C}))$ have the same character. If $\chi_{\rho_1}=\chi_{\rho_2}$ is nontrivial, then $\rho_1$ is acyclic if and only if $\rho_2$ is acyclic.
:::

::: proof
*Proof.* For every character there is a unique closed orbit by conjugation, so that every other orbit accumulates to it, see [@LM85]. So we may assume that the conjugation orbit of $\rho_2$ accumulates to $\rho_1$. By semi-continuity, $\rho_1$ acyclic implies that so is $\rho_2$. Next assume that $\rho_1$ is not acyclic. Up to conjugacy, there exists a group homomorphism $\phi \colon \pi_1M^3\to\mathbb{Z}$ and $\lambda\in\mathbb{C}-\{0,\pm 1\}$ such that $$\rho_1(\gamma)=\begin{pmatrix}  \lambda^{\phi(\gamma)} & 0 \\
                0 & \lambda^{-\phi(\gamma)} 
        \end{pmatrix}
    \quad\textrm{ and }\quad
\rho_2(\gamma)=\begin{pmatrix}  \lambda^{\phi(\gamma)} & f(\gamma) \\
                0 & \lambda^{-\phi(\gamma)} 
        \end{pmatrix}$$ for every $\gamma\in\pi_1M^3$. Here $f\colon \pi_1M^3\to\mathbb{C}$ is a crossed morphism: $f(\gamma_1\gamma_2)= f(\gamma_1) + \lambda^{2\phi(\gamma)} f(\gamma_2)$, for all $\gamma_1,\, \gamma_2 \in \pi_1M^3$. The homology of $\rho_1$ decomposes as a direct sum of $\pi_1M^3$-modules: $\mathbb{C}\oplus\{0\}$ and $\{0\}\oplus\mathbb{C}$, and both are nonzero (one is dual from the other). The $\rho_2$-module does not decompose, but there is an exact sequence of $\pi_1M^3$-modules $$0\to \mathbb{C}\oplus\{0\} \to \mathbb{C}^2\to \mathbb{C}\to 0$$ where $\pi_1M^3$ acts on $\mathbb{C}^2$ via $\rho_2$, and the action on the other modules is the same as for $\rho_1$. From the corresponding long exact sequence in homology it follows easily that $\rho_2$ is not acyclic. ◻
:::
