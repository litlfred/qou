---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-022-61-connection-with-the-work-of-biane
section_title: "Connection with the work of Biane"
section_number: 6.1
pages: 53-53
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 1.0
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
[]{#subsec:bianeconnection label="subsec:bianeconnection"} The following connection with article [@Biane1998] was pointed out to me by Philippe Biane.

Biane shows [@Biane1998] that the matrix $\Gamma$ defined in [\[eq:macierzjucysia\]](#eq:macierzjucysia){reference-type="eqref" reference="eq:macierzjucysia"} fulfills $$\begin{gathered}

M^{\mathop{\mathrm{JM}}}_n=\frac{1}{q+1} \mathop{\mathrm{Tr}}\Gamma^n=\\
\frac{1}{q+1} \sum_{p_1,\dots,p_{n} \in\{1,\dots,q+1\}} \Gamma_{p_1
p_2} \Gamma_{p_2 p_3} \cdots \Gamma_{p_{n-1} p_n} \Gamma_{p_n p_1},
\end{gathered}$$ where the sum runs only over tuples $(p_1,\dots,p_n)$ such that no neighbor elements are equal. Under identification $\ast=q+1$ summands in Biane's formula coincide with pushing sequences; the only modification is that one does not assume that $p_1=\ast$.

This connection goes much deeper: in Section 4.3 of [@Biane1998] one considers pairs $(J,\pi)$ where $J=\{r_1,\dots,r_k\}\subseteq\{1,2,\dots,n\}$ is the set of indices such that $p_{r_1}=\cdots=p_{r_k}=\ast$ and $\pi$ is a partition of the set $\{1,2,\dots,n\}\setminus J$ which tells us which of the elements in the tuple $(p_1,\dots,p_n)$ are equal. One can easily see that the union $\{J\} \cup \pi$ is a pushing partition. We leave it as an exercise to the reader to verify that the conjugacy class assigned to a pair $(J,\pi)$ by Biane coincides with the conjugacy class which appears in $\Phi^{\mathop{\mathrm{P}}}_{{{S}}_{A}}(\{J\} \cup \pi)$. Methods presented in this article can be used therefore to simplify some of the arguments in the papers [@Biane1998; @Biane2001approximate].
