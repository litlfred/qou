---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-009-18-fusion-categories
section_title: "Fusion categories"
section_number: 1.8
pages: 5-5
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.919
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
[]{#sect-fusion label="sect-fusion"} A *fusion category* over a commutative ring $\Bbbk$ is a $\Bbbk$-linear autonomous category $\mathcal{C}$ endowed with a finite family $\{V_i\}_{i \in I}$ of objects of $\mathcal{C}$ satisfying:

-   $\mathrm{Hom}_\mathcal{C}(V_i,V_j)=\delta_{i,j} \, \Bbbk$ for all $i,j \in I$;

-   each object of $\mathcal{C}$ is a finite direct sum of objects of $\{V_i\}_{i \in I}$;

-   $\mathbb{1}$ is isomorphic to some $V_0$ with $0 \in I$.

An object $X$ of $\mathcal{C}$ is *scalar* if $\mathrm{End}(X)=\Bbbk$. The family $\{V_i\}_{i \in I}$ is a representative family of scalar objects of $\mathcal{C}$. Left and right dualities in $\mathcal{C}$ preserve scalar objects, and so induce bijections $i \mapsto \leftidx{^\vee}{\!i}{}$ and $i \mapsto {i}^\vee$ of $I$ such that $\leftidx{^\vee}{\!(V_i)}{} \cong V_{\leftidx{^\vee}{\!i}{}}$ and ${(V_i)}^\vee \cong V_{{i}^\vee}$. Note that $\leftidx{^\vee}{\!0}{}=0={0}^\vee$.

Let $\mathcal{C}$ be a fusion category. The $\mathrm{Hom}$ spaces in $\mathcal{C}$ are free $\Bbbk$-modules of finite type. The *multiplicity* of $i\in I$ in an objet $X$ of $\mathcal{C}$ is defined as: $$N^i_X=\mathrm{rank}_\Bbbk\,\mathrm{Hom}_\mathcal{C}(V_i,X)=\mathrm{rank}_\Bbbk\,\mathrm{Hom}_\mathcal{C}(X,V_i).$$ Note there exist morphisms $(p_X^{i,\alpha} \colon X \to V_i)_{1 \leq \alpha \leq N^i_X}$ and $(q_X^{i,\alpha}\colon V_i \to X)_{1
\leq \alpha \leq N^i_X}$ such that: $$\mathrm{id}_X=\!\!\!\!\!\sum_{\substack{i \in I \\ 1 \leq \alpha \leq N^i_X}} \!\!\!q_X^{i,\alpha}p_X^{i,\alpha} \quad \text{and}
\quad p_X^{i,\alpha}q_X^{j,\beta}=\delta_{i,j}\delta_{\alpha,\beta} \, \mathrm{id}_{V_i}.$$

A fusion category $\mathcal{C}$ admits a coend $C=\bigoplus_{i \in I} \leftidx{^\vee}{\!V_i}{} \otimes V_i$ with universal dinatural transformation given by: $$i_X=\sum_{\substack{i\in I \\ 1 \leq \alpha \leq N_X^i}} \leftidx{^\vee}{\!q}{}_X^{i,\alpha}\otimes p_X^{i,\alpha}.$$ Since $\dim_l(C)=\dim_r(C)$, the dimension of a sovereign fusion category $\mathcal{C}$ is: $$\dim \mathcal{C}=\sum_{i \in I} \dim_l(V_i) \dim_r(V_i) \in \Bbbk.$$

In a sovereign fusion category $\mathcal{C}$, the dimensions $\dim_l(V_i)$ and $\dim_r(V_i)$ of the scalar objects are invertible. However $\dim \mathcal{C}$ may be not invertible.

A fusion category $\mathcal{C}$ is *spherical* if it is sovereign and the left and right traces of endomorphisms in $\mathcal{C}$ coincide. This last condition is equivalent to the equality of left and right dimensions of the scalar objects $V_i$ for $i\in I$. In a spherical category, the left (and right) dimension of an object $X$ is denoted $\dim(X)$.
