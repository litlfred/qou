---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-019-3-twisted-hochschild-homology
section_title: "Twisted Hochschild homology"
section_number: 3
pages: 10-11
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.971
---
[]{#xxsec3 label="xxsec3"}

## Definition {#xxsec3.1}

Let $A$ be an algebra and let $\sigma$ be an algebra automorphism. A $\sigma$-twisted version of the standard cochain complex used to define cyclic cohomology is defined in [@KMT Section 2], and used to define *$\sigma$-twisted cyclic and Hochschild (co)homology*; the notation is $HC^{\sigma}_{\ast}(A)$ and $HH^{\sigma}_{\ast}(A)$ in the case of the homology groups, and analogously for the cohomology groups. As shown in [@HK1 Proposition 2.1], when $\sigma$ is diagonalisable, as will be the case in the most of the examples of particular interest to us, one has $$\begin{aligned}
 HH^\sigma_n(A)\; \cong \;  H_n(A,{^\sigma A}),
\end{aligned}$$ where the right hand side denotes Hochschild homology with coefficients in $^\sigma A$.

::: definition
The *Hochschild dimension* of $A$ is defined to be $$\mathop{\mathrm{Hdim}}A=\max\{i\;|\; HH_{i}(A)=H_i(A,A)\neq 0\}.$$ The *twisted Hochschild dimension of* $A$ is defined to be $$\mathop{\mathrm{tHdim}}A \;=\; \max\{i\;|\; H_{i}(A,{^\sigma A})\neq 0
\quad \text{for some automorphism $\sigma$ of $A$}\}.$$
:::

::: remark
Ideally the twisted Hochschild dimension should be defined in terms of twisted Hochschild homology $HH^\sigma_n(A)$. Unfortunately our computation in later sections uses knowledge of $H_{n}(A,{^\sigma A})$; and we don't know in general when $\sigma$ will be diagonalisable. Further, it's not immediately obvious whether $H_{n}(A,{^\sigma A}) \neq 0$ is equivalent to $HH^\sigma_n(A)\neq 0$ when $\sigma$ is not diagonalisable. The above definition is therefore chosen so as to finesse this uncertainty.

In Section 6 we will comment on the diagonalisability of the relevant automorphisms for particular classes of examples.
:::

Of course, in some cases diagonalisability is automatic. The following lemma is a standard result of linear algebra.

::: lemma
If $\sigma$ has finite order and the characteristic of $k$ is zero, then $\sigma$ is diagonalisable.
:::

## Ischebeck's spectral sequence {#xxsec3.2}

We need the following special case of Ischebeck's spectral sequence [@Is 1.8]. Let $A$ be an algebra, let $M$ be a left $A$-module and $N$ a right $A$-module. Suppose that $_AM$ has a resolution by finitely generated projectives and that $N_A$ has finite injective dimension. Then Ischebeck's spectral sequence is a convergent spectral sequence of vector spaces $$\begin{aligned}
E^{p,q}_2\; :=\; \mathop{\mathrm{Ext}}^p_{A^{\sf op}}(\mathop{\mathrm{Ext}}^{-q}_{A}(M,A),N)
\; \Longrightarrow \; \mathop{\mathrm{Tor}}^A_{-p-q}(N,M).
\end{aligned}$$ If $N$ is an $A$-bimodule, then this is a sequence of left $A$-modules. In particular, if $A$ has finite injective dimension, then we obtain the double Ext-spectral sequence of left $A$-modules $$\begin{aligned}
E^{p,q}_2\; :=\; \mathop{\mathrm{Ext}}^p_{A^{\sf op}}(\mathop{\mathrm{Ext}}^{-q}_{A}(M,A),A)
\; \Longrightarrow \; {\mathbb H}^{p+q}(M)
\end{aligned}$$ where ${\mathbb H}^n(M)=\begin{cases} 0& n\neq 0\\
M&n=0\end{cases}$ .

As an immediate application we record here the fact that, when $A$ is a noetherian Hopf algebra the (AS2) condition of Definition ([\[xxsec1.2\]](#xxsec1.2){reference-type="ref" reference="xxsec1.2"})(b) can be replaced by a weaker form, as follows:

::: lemma
Let $A$ be a noetherian Hopf algebra of injective dimension $d$. If $\mathop{\mathrm{Ext}}^i_A(k,A)$ and $\mathop{\mathrm{Ext}}^i_{A^{\sf op}}(k,A)$ are finite dimensional over $k$ for all $i$ and if $\mathop{\mathrm{Ext}}^d_A(k,A)\neq 0$, then $A$ is AS-Gorenstein.
:::

::: proof
*Proof.* Suppose that the stated hypotheses on the Ext-groups hold. Using the double Ext-spectral sequence, or following the proof of [@BG1 Theorem 1.13], one shows that $\mathop{\mathrm{Ext}}^i_A(M,A)=0$ and $\mathop{\mathrm{Ext}}^i_{A^{\sf op}}(N,A)=0$ for all $i\neq d$ and all finite dimensional left $A$-modules $M$ and finite dimensional right $A$-modules $N$. By the proof of [@WZ2 Lemma 4.8] $\dim \mathop{\mathrm{Ext}}^d_A(M,A)=\dim M\cdot
\dim \mathop{\mathrm{Ext}}^d_A(k,A)$ for any finite dimension left $A$-module $M$. Thus $$\dim \mathop{\mathrm{Ext}}^d_{A}(\mathop{\mathrm{Ext}}^d_{A^{\sf op}}(k,A),A)\; =\;
\dim \mathop{\mathrm{Ext}}^d_{A^{\sf op}}(k,A) \cdot \dim \mathop{\mathrm{Ext}}^d_{A}(k,A).$$ By the double-Ext spectral sequence (3.2.2), $\mathop{\mathrm{Ext}}^d_{A}(\mathop{\mathrm{Ext}}^d_{A^{\sf op}}(k,A),A)\cong k$. Hence $$\dim \mathop{\mathrm{Ext}}^d_{A^{\sf op}}(k,A)\; =\; \dim \mathop{\mathrm{Ext}}^d_{A}(k,A)
\; =\; 1.$$ Thus we have proved (AS2). ◻
:::
