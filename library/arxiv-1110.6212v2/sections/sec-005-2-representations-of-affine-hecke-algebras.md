---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras"
section_id: sec-005-2-representations-of-affine-hecke-algebras
section_title: "Representations of affine Hecke algebras"
section_number: 2
pages: 7-8
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.983
doc_brief: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras — This paper has two main purposes."
---
Let $M$ be a finite dimensional $\mathscr{H}_L$-module. For each $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$ let $$\begin{aligned}
M_t&=\{v\in M\mid x^{\lambda}\cdot v=t^{\lambda}v\quad\textrm{for all $\lambda\in L$}\}\\
M_t^{\mathrm{gen}}&=\{v\in M\mid \textrm{for each $\lambda\in L$ there is a $k>0$ such that $(x^{\lambda}-t^{\lambda})^k\cdot v=0$}\}
\end{aligned}$$ be the *$t$-weight space* and the *generalised $t$-weight space* respectively. Each finite dimensional $\mathscr{H}_L$-module $M$ decomposes into a direct sum of generalised $t$-weight spaces $$M=\bigoplus_{t\in\mathrm{supp}(M)}M_t^{\mathrm{gen}}$$ where $\mathrm{supp}(M)=\{t\in\mathrm{Hom}(L,\mathbb{C}^{\times})\mid M_t^{\mathrm{gen}}\neq 0\}$ is the *support* of $M$.

A finite dimensional $\mathscr{H}_L$-module $M$ is *calibrated* if $$M_t^{\mathrm{gen}}=M_t\qquad\textrm{for all $t\in\mathrm{supp}(M)$}.$$ (In the literature this is also refereed to as *tame*). The main purpose of the first half of this paper is to construct calibrated irreducible representations of general affine Hecke algebras. We suspect that a complete classification of calibrated representations along the lines of the $1$-parameter case is possible (perhaps with some restrictions like $W_t=W_{(t)}$), although such a classification requires detailed information about the representation theory of rank $2$ (multi-parameter) affine Hecke algebras, and this would take us beyond the scope of the present paper. Thus the focus of this paper is on construction, and the question of classification will be pursued in later work.

The elements $\tau_i\in\mathscr{H}_L$, considered as operators on a representation, are often called *intertwining operators* because of the following fundamental and important fact.

::: lemma
[]{#lem:bijection label="lem:bijection"} Let $1\leq i\leq n$. Let $M$ be a finite dimensional $\mathscr{H}_L$-module, and suppose that $t\in\mathrm{supp}(M)$. Then as operators, $$\tau_i:M^{\mathrm{gen}}_t\to M^{\mathrm{gen}}_{s_it}\qquad\textrm{and}\qquad\tau_i:M_{s_it}^{\mathrm{gen}}\to M_t^{\mathrm{gen}}.$$ Moreover, $n_i(t)n_i(t^{-1})\neq 0$ if and only if each operator is bijective.
:::

::: proof
*Proof.* Let $m\in M_t^{\mathrm{gen}}$. By ([\[eq:simpbernstein\]](#eq:simpbernstein){reference-type="ref" reference="eq:simpbernstein"}) we compute $$(x^{\lambda}-(s_it)^{\lambda})^k\tau_i\cdot m=\tau_i(x^{s_i\lambda}-t^{s_i\lambda})^k\cdot m=0$$ for sufficiently large $k$. Thus $\tau_i\cdot m\in M_{s_it}^{\mathrm{gen}}$. For the final claim, note that by ([\[eq:tausquared\]](#eq:tausquared){reference-type="ref" reference="eq:tausquared"}) the operator $\tau_i^2:M_t^{\mathrm{gen}}\to M_t^{\mathrm{gen}}$ is given by $\tau_i^2\cdot m=q_in_i(t)n_i(t^{-1})m$. ◻
:::

By Schur's Lemma (see [@varadarajan]) the centre $\mathbb{C}[L]^{W_0}$ of $\mathscr{H}_L$ acts on an irreducible module $M$ by scalars. It follows that there exists $t\in \mathrm{Hom}(L,\mathbb{C}^{\times})$ such that $$p(x)\cdot v=p(t)v\qquad\textrm{for all $p(x)\in\mathbb{C}[L]^{W_0}$ and all $v\in M$.}$$ The element $t$ is only defined up to $W_0$ orbits. The orbit $W_0t$ is called the *central character* of $M$, although as is customary we will usually refer to any $t'\in W_0t$ as 'the' central character of $M$. A central character $t\in\mathrm{Hom}(L,\mathbb{C}^{\times})$ is called *regular* if $t^{\alpha^{\vee}}\neq 1$ for all $\alpha\in R_0$.
