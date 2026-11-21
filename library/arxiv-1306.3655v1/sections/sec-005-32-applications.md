---
doc_id: arxiv-1306.3655v1
doc_title: "The Murnaghan-Nakayama rule and some virtual S n characters"
section_id: sec-005-32-applications
section_title: "Applications"
section_number: 3.2
pages: 8-9
source_pdf: 1306.3655v1.pdf
source_sha256: 45dd8bd55687ecce
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.981
doc_brief: "The Murnaghan-Nakayama rule and some virtual S n characters — We construct certain virtual characters for the symmetric groups, then compute a formula which calculates the values of these virtual"
---
::: example
1. In Example [\[v2\]](#v2){reference-type="ref" reference="v2"}.1 we saw that $\psi_{\emptyset,n}= \sum_{j=0}^{n-1}(-1)^j\chi^{(n-j,1^j)}.$ Theorem [\[v4\]](#v4){reference-type="ref" reference="v4"} with $k=0$ then implies that $$\begin{aligned}
\label{general.conjecture}
  \psi_{\emptyset,n}(\mu)= \sum_{j=0}^{n-1}(-1)^j\chi^{(n-j,1^j)}(\mu) =\begin{cases}n & if  ~\mu= (n)
\\
0 & if ~\mu\ne (n)\\
\end{cases}
\end{aligned}$$

2. Similarly, by Example [\[v2\]](#v2){reference-type="ref" reference="v2"}.2, $~\psi_{(1),n}=\chi^{(n)}+\sum_{j=0}^{n-4}(-1)^{j+1}\chi^{(n-2-j,2,1^j)} + (-1)^n\chi^{(1^n)},$ and we get $$\psi_{(1),n}(\mu)=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$$

$$\begin{aligned}
\label{general.conjecture2}
  =\chi^{(n)}(\mu)+\sum_{j=0}^{n-4}(-1)^{j+1}\chi^{(n-2-j,2,1^j)}(\mu) + (-1)^n\chi^{(1^n)}(\mu) =\begin{cases}n-1 & if  ~\mu= (n-1,1)
\\
0 & if ~\mu\ne (n-1,1)\\
\end{cases}
\end{aligned}$$

Clearly, there are infinitely many identities that can be deduced this way.

.  Consider the first column $\{f^\lambda\mid \lambda\vdash n\}$ in the charcter table of $S_n.$ Let $n\ge 2k+2$, fix some $\nu\vdash k$, then construct the sequence of partitions of $n$: $\nu*S_1,\nu*S_2,\ldots$. Finally, form the corresponding alternating sum, then always $$\begin{aligned}
\label{v22}
\sum_{j=1}^{n-k}(-1)^jf^{\nu*S_j}=0.
\end{aligned}$$ This follows from Theorem [\[v4\]](#v4){reference-type="ref" reference="v4"}, since this corresponds to $\mu=(1^n)$, so $\mu_1=1\ne n-k$. When $k=0$ this is the well known identity $$\begin{aligned}
\label{general.conjecture02}
\sum_{j=1}^n(-1)^j{n\choose j}=0,
\end{aligned}$$ see [\[general.conjecture\]](#general.conjecture){reference-type="eqref" reference="general.conjecture"}. Thus, [\[v22\]](#v22){reference-type="eqref" reference="v22"} can be seen as a generalization of [\[general.conjecture02\]](#general.conjecture02){reference-type="eqref" reference="general.conjecture02"}.
:::

::: remark
In [@regev] a formula is proved for the values $$\sum_{i\ge 0} \chi^{(n-i,1^i)}(\mu),\quad \mu\vdash n.$$ Of course, here we deduced a formula for the values for the corresponding alternating sum $$\sum_{i\ge 0} (-1)^i\chi^{(n-i,1^i)}(\mu),\quad \mu\vdash n.$$

Adding, we get a formula for $$\sum_{i~even} \chi^{(n-i,1^i)}(\mu),\quad \mu\vdash n,$$ hence also for $$\sum_{i~odd} \chi^{(n-i,1^i)}(\mu),\quad \mu\vdash n.$$ We leave the details for the reader.
:::
