---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-017-44-canonical-integrals
section_title: "Canonical integrals"
section_number: 4.4
pages: 16-17
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.918
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Using the squared antipode, one can construct integrals on a weak Hopf algebra $A$ called the *canonical integrals*. Namely, we have the following proposition, a particular case of which was proved in [@BNSz].

::: proposition
[]{#chi label="chi"} Let $A$ be a finite-dimensional weak Hopf algebra and let $\{q_i\}$ be primitive central idempotents in $A_t$. Then $\chi_i(h) := \text{Tr}(L_h\circ S^2|_{AS(q_i)})$, where $L_h \in \text{End}_k(A)$ is given by $L_h(x)=hx,\,h, x\in A$, defines a left integral in $A^*$ such that $$\begin{aligned}
\label{chi1}
\chi_i(q_j) &=& \text{Tr}(S^2|_{q_jAS(q_i)})  \qquad \mbox{and } \\
\label{q-trace}
\chi_i(gh) &=& \chi(h S^2(g)),
\end{aligned}$$ for all $g,h\in A$.
:::

::: proof
*Proof.* The identities [\[chi1\]](#chi1){reference-type="eqref" reference="chi1"} and [\[q-trace\]](#q-trace){reference-type="eqref" reference="q-trace"} follow immediately from the definition of $\chi$, since $A$ is regular and $S^2\circ L_g = L_{S^2(g)}\circ S^2$ for all $g\in A$.

Next, for all $\phi\in A^*$ we define $R_\phi \in \text{End}_k(A)$ by $R_\phi(x) = x\leftharpoonup\phi,\, x\in A^*$. Then $R_\phi(xS(q_i)) = R_\phi(x)S(q_i)$ so that $AS(q_i)$ is $R_\phi$-invariant. A direct computation shows that $L_{(h \leftharpoonup\phi)} = R_{\phi_{(1)}}\circ L_h \circ R_{S^{-1}(\phi_{(2)})}$ for all $h\in A,\, \phi\in A^*$, and hence, $$\begin{aligned}
(\phi \otimes \chi_i)(\Delta(h))
&=& \text{Tr}(L_{(h \leftharpoonup\phi)}\circ S^2|_{AS(q_i)}) \\
&=& \text{Tr}( R_{\phi_{(1)}}\circ L_h \circ R_{S^{-1}(\phi_{(2)})}\circ S^2|_{AS(q_i)}) \\
&=& \text{Tr}( R_{\varepsilon_t(\phi)}\circ  L_h \circ S^2|_{AS(q_i)}),
\end{aligned}$$ therefore, $(\text{id}\otimes \chi_i)\Delta(h) =  
(\varepsilon_t \otimes \chi)\Delta(h)$ for all $h\in A$, i.e., $\chi_i$ is a left integral in $A^*$. ◻
:::
