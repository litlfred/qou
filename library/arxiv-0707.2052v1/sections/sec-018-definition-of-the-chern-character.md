---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-018-definition-of-the-chern-character
section_title: "Definition of the Chern character."
section_number: null
pages: 22-22
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.957
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
Suppose $X$ is a space, and ${\mathscr E}$ is an object in $\mathbf{D}(X)$. Consider ${\mathscr E}$ as an object of $\mathbf{D}({\mathsf{pt}}\times X)$, i.e., as a kernel ${\mathsf{pt}}\rightarrow
X$, so there is an induced linear map $${\mathscr E}_*\colon\mathop{\mathrm{HH}}_\bullet({\mathsf{pt}}) \rightarrow\mathop{\mathrm{HH}}_\bullet(X).$$ Now, because the Serre functor on a point is trivial, $\mathop{\mathrm{HH}}_0({\mathsf{pt}})$ is canonically identifiable with $\mathop{\mathrm{Hom}}_{{\mathsf{pt}}\times {\mathsf{pt}}}({\mathscr O}_{\mathsf{pt}}, {\mathscr O}_{\mathsf{pt}})$ so there is a distinguished class ${\mathbf 1}\in \mathop{\mathrm{HH}}_0({\mathsf{pt}})$ corresponding to the identity map. Define the Chern character of ${\mathscr E}$ as $$\mathop{\mathrm{ch}}({\mathscr E}) := {\mathscr E}_*({\mathbf 1}) \in \mathop{\mathrm{HH}}_0(X).$$ Graphically this has the following description: $$\mathop{\mathrm{ch}}({\mathscr E}):=\raisebox{-.45\height}{}.$$ Naturality of push-forward leads to the next theorem.

::: Theorem
[]{#thm:commut label="thm:commut"} If $X$ and $Y$ are spaces and $\Phi\colon X\to Y$ is a kernel then the diagram below commutes. $$\begin{diagram}[height=2em,width=2em,labelstyle=\scriptstyle]
\mathbf{D}(X) & \rTo^{\Phi\circ {-}} & \mathbf{D}(Y) \\
\dTo_{\mathop{\mathrm{ch}}} & & \dTo_{\mathop{\mathrm{ch}}} \\
\mathop{\mathrm{HH}}_0(X) & \rTo^{\Phi_*} & \mathop{\mathrm{HH}}_0(Y).
\end{diagram}$$
:::

::: Proof
Let ${\mathscr E}$ be an object of $\mathbf{D}(X)$. We will regard it either as an object in $\mathbf{D}(X)$, or as a kernel ${\mathsf{pt}}\rightarrow X$, and similarly we will regard $\Phi\circ{\mathscr E}$ either as an object in $\mathbf{D}(Y)$ or as a kernel ${\mathsf{pt}}\rightarrow Y$. By Theorem [\[thm:functorial\]](#thm:functorial){reference-type="ref" reference="thm:functorial"} we have $$\begin{aligned}
    \Phi_* \mathop{\mathrm{ch}}({\mathscr E}) & = \Phi_* \left({\mathscr E}_* ({\mathbf 1})\right) = (\Phi\circ
    {\mathscr E})_* {\mathbf 1}= \mathop{\mathrm{ch}}(\Phi\circ{\mathscr E}).\qedhere
  
\end{aligned}$$
:::
