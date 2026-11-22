---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-038-proposition
section_title: "Proposition"
section_number: null
pages: 16-16
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.974
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
\textit{The set} $\{\text{Pr}_w \st w \in W\}$ \textit{is the set of non-isomorphic indecomposable projective objects in} $\mathcal{O}_0.$ \textit{Moreover, every projective object $Q \in \mathcal{O}_0$ is isomorphic to a finite direct sum }
$$Q \simeq \bigoplus_{w \in W}\text{Pr}^{\oplus m(\text{Pr}_w, Q)}_w$$
\textit{for unique multiplicites } $m(\text{Pr}_w, Q) \ge 0$, with $m(\text{Pr}_w, Q) = \dim \Hom(Q, L_w).$ \\\\
\textit{Proof:} Let $Q \in \mathcal{O}_0$ be a projective object. Choose a filtration 
$$0 = N_0 \subset N_1 \subset \ldots \subset N_n = Q$$
with simple successive subquotients. Then we have the natural projection $Q \rightarrow N_n/N_{n-1} \simeq L_x$ for some $x \in W.$ Since $\text{Pr}_x$ is projective, there exist maps $f: \text{Pr}_x \rightarrow Q$ and $g: Q \rightarrow \text{Pr}_x$ such that $gf(\text{Pr}_x) \subset \text{Pr}_x$ is a submodule of $\text{Pr}_x.$ Since $\text{Pr}_x$ is indecomposable, we have $gf(\text{Pr}_x) = \text{Pr}_x.$ Hence $\text{Pr}_x$ is a direct summand of $Q.$ By induction on the length of filtration, we ascertain the decomposition 
$$Q \simeq \bigoplus_{w \in W}\text{Pr}^{\oplus m_w}_w, \text{  }m_w \ge 0.$$
Let $y \in W.$ We have $\Hom(\text{Pr}_w, L_y) = 0$ if $w \ne y.$ Since $L_y$ is a unique simple quotient of $\text{Pr}_y$, and $\text{End}(L_y) = \C,$ we have 
$$\dim \Hom(\text{Pr}_y, L_y) = 1.$$
Hence 
$$\dim \Hom(Q, L_y) = \sum m_w \cdot \Hom(\text{Pr}_w, L_y) = m_y  $$  \Laughey
