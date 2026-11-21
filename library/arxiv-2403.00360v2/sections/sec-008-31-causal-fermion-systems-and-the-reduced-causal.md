---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-008-31-causal-fermion-systems-and-the-reduced-causal
section_title: "Causal Fermion Systems and the Reduced Causal Action Principle"
section_number: 3.1
pages: 10-11
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.992
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
We begin with the general definition of a causal fermion system.

::: Def
[]{#defcfs label="defcfs"} (causal fermion systems) * Given a separable complex Hilbert space $\mathscr{H}$ with scalar product $\langle.|. \rangle_\mathscr{H}$ and a parameter $n \in \mathbb{N}$ (the *"spin dimension"*), we let ${\mathscr{F}}\subset \text{\rm{L}}(\mathscr{H})$ be the set of all symmetric operators on $\mathscr{H}$ of finite rank, which (counting multiplicities) have at most $n$ positive and at most $n$ negative eigenvalues. On ${\mathscr{F}}$ we are given a positive measure $\rho$ (defined on a $\sigma$-algebra of subsets of ${\mathscr{F}}$). We refer to $(\mathscr{H}, {\mathscr{F}}, \rho)$ as a *causal fermion system*. *
:::

A causal fermion system describes a spacetime together with all structures and objects therein. In order to single out the physically admissible causal fermion systems, one must formulate physical equations. To this end, we impose that the measure $\rho$ should be a minimizer of the causal action principle, which we now introduce. For brevity of the presentation, we only consider the *reduced causal action principle* where the so-called boundedness constraint has been incorporated by a Lagrange multiplier term. This simplification is no loss of generality, because the resulting Euler-Lagrange (EL) equations are the same as for the non-reduced action principle as introduced for example in [@cfs Section §1.1.1].

For any $x, y \in {\mathscr{F}}$, the product $x y$ is an operator of rank at most $2n$. However, in general it is no longer a symmetric operator because $(xy)^* = yx$, and this is different from $xy$ unless $x$ and $y$ commute. As a consequence, the eigenvalues of the operator $xy$ are in general complex. We denote the rank of $xy$ by $k \leq 2n$. Counting algebraic multiplicities, we choose $\lambda^{xy}_1, \ldots, \lambda^{xy}_{k} \in \mathbb{C}$ as all the non-zero eigenvalues and set $\lambda^{xy}_{k+1}, \ldots, \lambda^{xy}_{2n}=0$. Given a parameter $\kappa>0$ (which will be kept fixed throughout this paper), we introduce the $\kappa$-Lagrangian and the causal action by $$\begin{aligned}
\text{\em{$\kappa$-Lagrangian:}} && {\mathcal{L}}(x,y) &= 
\frac{1}{4n} \sum_{i,j=1}^{2n} \Big( \big|\lambda^{xy}_i \big|
- \big|\lambda^{xy}_j \big| \Big)^2 + \kappa\: \bigg( \sum_{j=1}^{2n} \big|\lambda^{xy}_j \big| \bigg)^2 \label{Lagrange} \\
\text{\em{causal action:}} && {\mathcal{S}}(\rho) &= \iint_{{\mathscr{F}}\times {\mathscr{F}}} {\mathcal{L}}(x,y)\: d\rho(x)\, d\rho(y) \:. \label{Sdef}
\end{aligned}$$ The *reduced causal action principle* is to minimize ${\mathcal{S}}$ by varying the measure $\rho$ under the following constraints, $$\begin{aligned}
\text{\em{volume constraint:}} && \rho({\mathscr{F}}) = 1 \quad\;\; \label{volconstraint} \\
\text{\em{trace constraint:}} && \int_{\mathscr{F}}\mathop{\mathrm{tr}}(x)\: d\rho(x) = 1 \:. \label{trconstraint}
\end{aligned}$$ This variational principle is mathematically well-posed if $\mathscr{H}$ is finite-dimensional. For a review of the existence theory and the analysis of general properties of minimizing measures we refer to [@intro Chapter 12].
