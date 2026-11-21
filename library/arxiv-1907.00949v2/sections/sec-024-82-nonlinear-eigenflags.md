---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-024-82-nonlinear-eigenflags
section_title: "Nonlinear eigenflags"
section_number: 8.2
pages: 25-26
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.937
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:disv label="sec:disv"}

This is a variation of the principal flag problem [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"}: $$\label{eq:eig}
\begin{tabular}{rl}
maximize & $\sum_{i=1}^{d}\mathop{\mathrm{tr}}(Y_i^{\scriptscriptstyle\mathsf{T}}MY_i)^2$\\[1ex]
subject to & $\llbracket Y_1,\dots,Y_d \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d; n)$.
\end{tabular}$$ Again $M \in \mathbb{R}^{n \times n}$ is a symmetric matrix and the flag is given in Stiefel coordinates $Y = [Y_1,\dots,Y_d] \in \mathbb{R}^{n \times n_d}$, $Y^{\scriptscriptstyle\mathsf{T}}Y = I$, but partitioned into submatrices $Y_i \in \mathbb{R}^{n \times (n_i - n_{i-1})}$, $Y_i^{\scriptscriptstyle\mathsf{T}}Y_i = I$, $i =1,\dots,d$. More generally, the objective function in [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"} may be replaced by $\sum_{i=1}^{d}f_i\bigl(\mathop{\mathrm{tr}}(Y_i^{\scriptscriptstyle\mathsf{T}}M Y_i)\bigr)$ with $f_1,\dots,f_d \in C^2(\mathbb{R})$. Choosing $f_1(x) = \dots = f_d(x) = x$ gives us [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"} and choosing $f_1(x) = \dots = f_d(x) = x^2$ gives us [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"}. Note that it will take considerable effort to formulate a problem like [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"} as a constrained optimization problem in Euclidean space.

![Convergence trajectories for [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"} on $\mathop{\mathrm{Flag}}(3,7,12; 60)$.](flag2log.pdf){#fig:convergence2}

The convergence trajectories for Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"} applied to [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"} are shown in Figure [1](#fig:convergence2){reference-type="ref" reference="fig:convergence2"}. The nonlinearity imposes a cost --- it takes around $390$ iterations to satisfy one of the our stopping criteria, although the function values stabilize after around $60$ iterations. The jagged spikes seen in Figure [1](#fig:convergence2){reference-type="ref" reference="fig:convergence2"} are a result of iterates moving along a geodesic and then jumping to another geodesic. So this is indicative of steepest descent following a path that comprises multiple geodesics. A caveat is that unlike the principal flag problem [\[eq:dis\]](#eq:dis){reference-type="eqref" reference="eq:dis"}, we do not have a closed-form solution for [\[eq:eig\]](#eq:eig){reference-type="eqref" reference="eq:eig"} and thus we may only guarantee convergence to a local minimizer, which is reflected in Figure [1](#fig:convergence2){reference-type="ref" reference="fig:convergence2"}.
