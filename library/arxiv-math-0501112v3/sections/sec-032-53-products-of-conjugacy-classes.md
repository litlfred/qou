---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-032-53-products-of-conjugacy-classes
section_title: "Products of conjugacy classes"
section_number: 5.3
pages: 27-29
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.859
latex_coverage_ratio: 0.639
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
::: theorem
[]{#claim:mnozenie2 label="claim:mnozenie2"} []{#claim:mnozenie label="claim:mnozenie"} Let $i_1<\cdots<i_{n+1}$ be integers and for each $1\leq s\leq n$ let $\pi_s$ be a partition of the set $\rho_s=\{i_{s}+1,i_{s}+2,\dots,i_{s+1}\}$. We denote $$\pi_1 \bullet \cdots \bullet \pi_n=   (\pi_1 \cup \cdots \cup \pi_n) \vee
\big\{ \{i_2,i_3,\dots,i_{n+1} \} \big\}.$$ Then $$\label{eq:formulanailoczynrozlaczny} \Sigma_{\pi_1} \bullet \cdots
\bullet \Sigma_{\pi_n}= \Sigma_{(\pi_1 \bullet \cdots \bullet
\pi_n)}.$$

Furthermore, $$\label{eq:formulanailoczyn} \Sigma_{\pi_1} \cdots
\Sigma_{\pi_n}=\sum_{\sigma} \Sigma_{\sigma},$$

where the sum on the right-hand side runs over all partitions $\sigma$ of the set $\{i_1+1,i_1+2,\dots,i_{n+1}\}$ such that

1.  for any $a,b\in\rho_s$, $1\leq s\leq n$ we have that $a$ and $b$ are connected by $\sigma$ if and only if they are connected by $\pi_s$,

2.  elements $i_2,i_3,\dots,i_{n+1}$ belong to the same block of $\sigma$.

Furthermore, $$\label{eq:kumulantyklas} k^{\text{\rm
id}}(\Sigma_{\pi_1},\dots,\Sigma_{\pi_n})=\sum_{\sigma}
\Sigma_{\sigma},$$ where the sum on the right-hand side runs over all partitions $\sigma$ of the set $\{i_1+1,i_1+2,\dots,i_{n+1}\}$ such that

1.  for any $a,b\in\rho_s$, $1\leq s\leq n$ we have that $a$ and $b$ are connected by $\sigma$ if and only if they are connected by $\pi_s$,

2.  elements $i_2,i_3,\dots,i_{n+1}$ belong to the same block of $\sigma$; we will denote this block by $\sigma_1$,

3.  $(\sigma\setminus\sigma_1) \vee \{\rho_1,\dots,\rho_n\}$ is the maximal partition with only one block.
:::

::: proof
*Proof.* Equations [\[eq:formulanailoczynrozlaczny\]](#eq:formulanailoczynrozlaczny){reference-type="eqref" reference="eq:formulanailoczynrozlaczny"} and [\[eq:formulanailoczyn\]](#eq:formulanailoczyn){reference-type="eqref" reference="eq:formulanailoczyn"} follow immediately from the definition [\[equ:noweklasy2\]](#equ:noweklasy2){reference-type="eqref" reference="equ:noweklasy2"}.

We shall treat [\[eq:kumulantyklas\]](#eq:kumulantyklas){reference-type="eqref" reference="eq:kumulantyklas"} as a definition of the left-hand side and we shall verify that so defined cumulants fulfill the defining relation of cumulants [\[eq:moment-cumulant\]](#eq:moment-cumulant){reference-type="eqref" reference="eq:moment-cumulant"}. Before we do this we need to compute the corresponding partition-indexed cumulants. Let $\mu$ be a partition of $\{1,\dots,n\}$; we denote by $\tilde{\mu}$ a partition of the set $\{i_1+1,i_1+2,\dots,i_{n+1}\}$ such that $a\in \rho_s$ and $b\in\rho_t$ belong to the same block of $\tilde{\mu}$ if and only if $s$ and $t$ belong to the same block of $\mu$. Then [\[eq:kumulantyklas\]](#eq:kumulantyklas){reference-type="eqref" reference="eq:kumulantyklas"} implies $$\label{eq:kumulantymultiplikatywnie} k_{\mu}^{\text{\rm
id}}(\Sigma_{\pi_1},\dots,\Sigma_{\pi_n})=\sum_{\sigma}
\Sigma_{\sigma},$$ where the sum on the right-hand side runs over all partitions $\sigma$ of the set $\{i_1+1,i_1+2,\dots,i_{n+1}\}$ such that

1.  for any $a,b\in\rho_s$, $1\leq s\leq n$ we have that $a$ and $b$ are connected by $\sigma$ if and only if they are connected by $\pi_s$,

2.  elements $i_2,i_3,\dots,i_{n+1}$ belong to the same block of $\sigma$; we will denote this block by $\sigma_1$,

3.  $(\sigma\setminus\sigma_1) \vee
     \{\rho_1,\dots,\rho_n\}=\tilde{\mu}$.

Equation [\[eq:kumulantymultiplikatywnie\]](#eq:kumulantymultiplikatywnie){reference-type="eqref" reference="eq:kumulantymultiplikatywnie"} implies immediately [\[eq:moment-cumulant\]](#eq:moment-cumulant){reference-type="eqref" reference="eq:moment-cumulant"}. ◻
:::

For example, for $$\begin{gathered}
\label{eq:przykladmnozenie} \rho_1=\{1,2,3,4\},\
\rho_2=\{5,6,7,8\},\\  \pi_1=\big\{ \{1,3\},\{2,4\} \big\},
\pi_2=\big\{ \{5,7\}, \{6\},\{8\} \big\},\
\end{gathered}$$ the above theorem states that $$\Sigma_{\pi_1}  \Sigma_{\pi_2} =
\Sigma_{\big\{ \{1,3\},\{2,4,8\},\{5,7\},\{6\} \big\}}+
\Sigma_{\big\{ \{1,3,6\},\{2,4,8\},\{5,7\} \big\}}+  \Sigma_{\big\{
\{1,3,5,7\},\{2,4,8\},\{6\} \big\}}$$ and $$k^{\text{\rm
id}}(\Sigma_{\pi_1},  \Sigma_{\pi_2}) = \Sigma_{\big\{
\{1,3,6\},\{2,4,8\},\{5,7\} \big\}}+ \Sigma_{\big\{
\{1,3,5,7\},\{2,4,8\},\{6\} \big\}};$$ the readers acquainted with the results of Section [\[subsec:explicit\]](#subsec:explicit){reference-type="ref" reference="subsec:explicit"} may check that it is equivalent to $$\Sigma_{1} \Sigma_{1,1} = \Sigma_{1,1,1}+ \Sigma_{1,1} +
\Sigma_{1,1}$$ and $$k^{\text{\rm
id}}(\Sigma_{1}, \Sigma_{1,1}) = \Sigma_{1,1} + \Sigma_{1,1}.$$
