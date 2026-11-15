---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-022-41-representations-of-sl2c
section_title: "Representations of SL2(C)"
section_number: 4.1
pages: 26-27
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.974
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
[]{#section:reps label="section:reps"}

Let $V_{k+1}$ be the space of degree $k$ homogeneous polynomials in two variables: $$V_{k+1}:=\{ P\in \mathbb{C}[X,Y]\mid P \textrm{ is homogeneous of degree } k\}.$$ The group $\mathrm{SL}_2(\mathbb{C})$ acts naturally on $V_{k+1}$ by precomposition on polynomials: $$\begin{array}{ccl}
 \mathrm{SL}_2(\mathbb{C})\times V_{k+1} & \to & V_{k+1} \\
 (A, P) & \mapsto & P\circ A^t
\end{array}$$ We consider the transpose matrix $A^t$ so that the action is on the left. We could also have considered the inverse instead of the transpose, as there exist a matrix $B\in \mathrm{SL}_2(\mathbb{C})$ such that $A^{-1}=B A^t B^{-1}$ for every $A\in \mathrm{SL}_2(\mathbb{C})$. This defines a representation $$\operatorname{Sym}^{k}\colon  \mathrm{SL}_2(\mathbb{C}) \to  \mathrm{SL}_{k+1}(\mathbb{C}).$$ Not only $\operatorname{Sym}^{k}$ has determinant $1$, but preserves a non-degenerate bilinear form that is symmetric for $k$ even, and skew-symmetric for $k$ odd. So $$\operatorname{Sym}^{k}\colon  \mathrm{SL}_2(\mathbb{C}) \to  
\left\{
\begin{array}{ll}
 \operatorname{SO} (2l+1,\mathbb{C}) & \textrm{for } k=2l \\
 \operatorname{Sp} (2l+2,\mathbb{C}) & \textrm{for } k=2l +1 \\
\end{array}
\right.$$ For $k=1$, $\operatorname{Sym}$ is the standard representation and the bilinear form is the determinant of the $2\times 2$ matrix obtained from two vectors. Then the form invariant for $\operatorname{Sym}^k$ is the $k$-th symmetric product of this determinant.

We shall also consider the complex conjugate $\overline{  \operatorname{Sym}^{k}}$, which is antiholomorphic.

::: prop
Classification of irreducible representations of $\mathrm{SL}_2(\mathbb{C})$, cf. [@BW00].

(a) Any irreducible holomorphic representation of $\mathrm{SL}_2(\mathbb{C})$ is equivalent to $\operatorname{Sym}^{k}$ for a unique $k\geq 0$.

(b) Any irreducible representation of $\mathrm{SL}_2(\mathbb{C})$ is equivalent to $$\operatorname{Sym}^{k_1,k_2}:= \operatorname{Sym}^{k_1}\otimes \overline{  \operatorname{Sym}^{k_2} }$$ for a unique pair of integers $k_1,k_2\geq 0$.
:::

Notice that $\operatorname{Sym}^{k}=\operatorname{Sym}^{k,0}$ and that $\operatorname{Sym}^{0}=\operatorname{Sym}^{0,0}$ is the trivial representation in $\mathbb{C}$.

The adjoint representation $\operatorname{Ad}\colon\mathrm{SL}_2(\mathbb{C})\to 
\operatorname{SO}(\mathfrak{sl}_2(\mathbb{C}))$ is equivalent to $\operatorname{Sym}^2$, the invariant form being the Killing form.

The representation $\operatorname{Sym}^{k,k}$ takes values in $\mathrm{SL}_{(k+1)^2}(\mathbb{R})$. More precisely, the image of $\operatorname{Sym}^{k,k}$ is contained in $\operatorname{SO}(p,q)$, with $$p=\frac{k^2+3k+2}{2}\quad\textrm{ and }\quad q= \frac{k^2+k}{2}.$$ For instance, $\operatorname{Sym}^{1,1}\colon \mathrm{PSL}_2(\mathbb{C}) \to  
\operatorname{SO}_0(3,1)$ is the canonical isomorphism between different presentations of the group of orientation preserving isometries of hyperbolic 3-space. This representation is used to study infinitesimal deformations of conformally flat structures on a hyperbolic 3-manifold. The representation $\operatorname{Sym}^{2,2}\colon\mathrm{PSL}_2(\mathbb{C}) \to  
\operatorname{SO}_0(6,3)$ is used in the study of infinitesimal deformations of projective structures on a hyperbolic 3-manifold.

Let $\varrho_\sigma\colon\pi_1 M^3\to \mathrm{SL}_2(\mathbb{C})$ denote a lift corresponding to a spin structure $\sigma$, we shall denote its composition with $\operatorname{Sym}^{k_1,k_2}$ by $$\label{eqn:varrho}
 \varrho_\sigma^{k_1,k_2}:=    \operatorname{Sym}^{k_1,k_2}\circ        \varrho_\sigma,$$ and $\varrho_\sigma^{k}= \varrho_\sigma^{k,0}$.

::: thm
[]{#thm:rig label="thm:rig"} Let $M^3$ be a compact hyperbolic orientable 3-manifold and $\widetilde{\mathrm{hol}}$ a lift of its holonomy. If $k_1\neq k_2$ then $$H^*(M^3 ;  \varrho_\sigma^{k_1,k_2} )=0\, .$$
:::

This theorem, due to Raghunathan, is commented in Appendix [\[sec:cohomology\]](#sec:cohomology){reference-type="ref" reference="sec:cohomology"}, with other facts about cohomology.
