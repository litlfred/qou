---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-001-21-knot-invariants-from-closed-braids-and-traces
section_title: "Knot invariants from closed braids and traces"
section_number: 2.1
pages: 4-4
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
There are two main constructions of quantum knot invariants from YBOs: one is through braid group representations and their trace maps that are invariant under Markov moves, and the other is by fixing a height function on the plane of projection and incorporate maps corresponding to maxima/minima of knot diagrams. Although these two approaches are closely related, we examine these approaches separately to take advantages of computations of known invariants and their deformations. In this subsection we review the first approach of trace, and in the next subsection we review the second maxima/minima approach.

Recall [@Tur] that an *enhanced YBO* (EYBO) is a quadruple $S = (R, \alpha, \beta, \mu)$ consisting of a YBO $R$, two invertible scalars $\alpha, \beta \in \mathbb k^\times$, and a linear map $\mu: V\longrightarrow V$ satisfying the following two compatibility conditions $$\begin{aligned}
        (\mu\otimes \mu) R &=& R (\mu\otimes \mu),\label{eqn:mu_comm}\\
        \mathop{\mathrm{Tr}}_2(R^{\pm}(\mu\otimes \mu)) &=& \alpha^\pm\beta\mu, \label{eqn:partial_tr}
\end{aligned}$$ where $\mathop{\mathrm{Tr}}_2$ indicates the partial trace of an operator with respect to its second tensorand. To shorten notation, in this article we also indicate an EYBO simply by $R$, when no risk of confusion arises. Observe that when $\mu$ is invertible, Equation [\[eqn:partial_tr\]](#eqn:partial_tr){reference-type="eqref" reference="eqn:partial_tr"} is equivalent to $$\begin{aligned}
        \mathop{\mathrm{Tr}}_2(R^{\pm}(\mathbb 1\otimes \mu)) = \alpha^{\pm}\beta \mathbb 1,
\end{aligned}$$ where $\mathbb 1$ denotes the identity mapping. Using EYBOs, Turaev [@Tur] gave a definition of quantum invariants of knots and links as follows. Let $\mathbb B_m$ denote the $m$-string braid group, whose elements are represented by vertical string diagrams with crossings. A knot or a link $K$ is represented as a closed braid form (Alexander's theorem), where the closure is to connect the top and bottom end points of a braid by parallel nested circular arcs to the right. Let $b_m  \in \mathbb B_m$ denote a braid whose closure represents $K$. Diagrams in closed braid form are oriented downwards on the braid portion unless otherwise stated. Let $w(b_m)$ denote the writhe of $b_m$, that is the number of positive crossings (positive braid generators) minus the negative ones. For an EYBO $S=(R, \alpha, \beta, \mu)$, a knot invariant $T_S(K)$ is defined by

$$\begin{aligned}
        T_S(K) = \alpha^{w(b_m)} \beta^{-m}\mathop{\mathrm{Tr}}(b_m \mu^{\otimes m}). 
\end{aligned}$$

The well definedness is proved by showing its invariance under Markov moves, that are conjugations and (de)stabilizations.
